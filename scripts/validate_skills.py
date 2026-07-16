#!/usr/bin/env python3
"""Phase-A validator for Registry skills.

For each skills/<pkg>/SKILL.md:
  1. Parse YAML frontmatter.
  2. Assert required fields: name, description, license.
  3. If metadata.mind.* keys are present:
     - assert mind.id is present
     - assert mind.distribution is present and in {builtin, marketplace}
     - reject any unknown mind.* key (only the recognized set is allowed)

  Spec §6.3: when any mind.* key is present, BOTH mind.id AND mind.distribution
  are required; missing either is an error.
  4. If mind.market-primary and mind.market-categories are present,
     assert the primary appears in the categories array.
  5. Allow executable/script files under skills/ (script-capable skills run in the
     claw sandbox via the shell tool; human-reviewed at webadmin-approve before
     listing). Script files are reported as INFO, not rejected.
  6. Compute and print a content digest per package (sorted relative paths +
     file bytes + length) for reproducibility (informational in Phase A).

Exit non-zero on any violation.

Spec: docs/superpowers/specs/2026-07-14-official-skill-registry-marketplace-design.md §6.7.
The full §6.7 gate suite (deterministic archive build twice, SBOM, provenance
attestation, secret scanning, static capability analysis) is deferred to Phase B.
"""
import hashlib
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

# Frontmatter delimiter: a line that is exactly --- (with optional trailing
# whitespace). Matching the delimiter LINE (not the bare substring) avoids
# mis-splitting on values that happen to contain "---" (e.g. a description
# like "a---b"). See spec §6.3 frontmatter framing.
FRONTMATTER_DELIMITER_RE = re.compile(r"^---\s*$", re.MULTILINE)

REGISTRY_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REGISTRY_ROOT, "skills")

RECOGNIZED_MIND_KEYS = {
    "mind.id",
    "mind.distribution",
    "mind.market-primary",
    "mind.market-categories",
    "mind.marketplace-summary",
    "mind.publisher",
    "mind.runtime-category",
    "mind.tags",
    "mind.min-harness-version",
    "mind.upstream.repo",
    "mind.upstream.commit",
    "mind.upstream.path",
    "mind.upstream.import-mode",
    "mind.upstream.license",
    "mind.upstream.evidence-urls",
}

# Script files are allowed (reviewed at approve); collected to report as INFO.
EXECUTABLE_EXTENSIONS = {".sh", ".py", ".bat", ".ps1", ".exe", ".cmd"}


def parse_frontmatter(path):
    """Parse the YAML frontmatter block from a SKILL.md file.

    Splits on the ``---`` DELIMITER LINE only (``^---\\s*$``), never on the
    bare substring, so values containing ``---`` (e.g. ``description: "a---b"``)
    do not truncate the frontmatter block.
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return None, "file does not start with YAML frontmatter (---)"
    parts = FRONTMATTER_DELIMITER_RE.split(text, maxsplit=2)
    if len(parts) < 3:
        return None, "malformed frontmatter block"
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return None, f"YAML parse error: {e}"
    if data is None:
        return None, "empty frontmatter"
    if not isinstance(data, dict):
        return None, "frontmatter is not a mapping"
    return data, None


def validate_frontmatter(data, skill_path):
    """Validate frontmatter fields per spec §6.3/§6.7. Returns list of errors."""
    errors = []
    # Required top-level fields
    for field in ("name", "description", "license"):
        val = data.get(field)
        if val is None or (isinstance(val, str) and not val.strip()):
            errors.append(f"missing or empty required field: {field}")
    # metadata.mind.* validation
    metadata = data.get("metadata")
    if metadata is not None:
        if not isinstance(metadata, dict):
            errors.append("metadata must be a mapping (string-to-string)")
            return errors
        mind_keys = [k for k in metadata.keys() if k.startswith("mind.")]
        if mind_keys:
            # Spec §6.3: when any mind.* key is present, BOTH mind.id AND
            # mind.distribution are required. Missing either is an error.
            if not metadata.get("mind.id"):
                errors.append("mind.id is required when any mind.* key is present")
            dist = metadata.get("mind.distribution")
            if not dist:
                errors.append(
                    "mind.distribution is required when any mind.* key is present"
                )
            elif dist not in ("builtin", "marketplace"):
                errors.append(
                    f"mind.distribution must be 'builtin' or 'marketplace', got: {dist!r}"
                )
            # Reject unknown mind.* keys
            for key in mind_keys:
                if key not in RECOGNIZED_MIND_KEYS:
                    errors.append(f"unknown mind.* key (rejected): {key}")
            # market-primary must be in market-categories if both present
            primary = metadata.get("mind.market-primary")
            cats_raw = metadata.get("mind.market-categories")
            if primary and cats_raw:
                try:
                    cats = json.loads(cats_raw) if isinstance(cats_raw, str) else cats_raw
                    if isinstance(cats, list) and primary not in cats:
                        errors.append(
                            f"mind.market-primary '{primary}' not in mind.market-categories {cats}"
                        )
                except (json.JSONDecodeError, TypeError) as e:
                    errors.append(f"mind.market-categories is not valid JSON: {e}")
    return errors


def find_skill_packages():
    """Walk skills/ and find directories containing SKILL.md (stop-on-first rule).
    Returns list of (package_dir, skill_md_path)."""
    packages = []
    if not os.path.isdir(SKILLS_DIR):
        return packages
    for root, dirs, files in os.walk(SKILLS_DIR):
        if "SKILL.md" in files:
            packages.append((root, os.path.join(root, "SKILL.md")))
            # stop-on-first: don't descend further into this package
            dirs.clear()
    return packages


def check_no_executables():
    """Collect executable/script files under skills/ (reported as INFO; allowed, reviewed at approve)."""
    violations = []
    if not os.path.isdir(SKILLS_DIR):
        return violations
    for root, dirs, files in os.walk(SKILLS_DIR):
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext in EXECUTABLE_EXTENSIONS:
                rel = os.path.relpath(os.path.join(root, fname), REGISTRY_ROOT)
                violations.append(rel)
    return violations


def compute_digest(package_dir):
    """Deterministic content digest per spec §6.6.

    For each file (sorted POSIX relative paths): fold the path, the byte
    length, the file bytes, and the executable bit (``os.stat(st_mode) &
    0o111`` → ``1`` or ``0``) into the per-file digest stream. Phase A has
    no executables so the bit is always 0, but the implementation honors
    the spec for forward compatibility.
    """
    files = []
    for root, dirs, fs in os.walk(package_dir):
        for fname in fs:
            full = os.path.join(root, fname)
            rel = os.path.relpath(full, package_dir).replace(os.sep, "/")
            files.append(rel)
    files.sort()
    h = hashlib.sha256()
    for rel in files:
        full = os.path.join(package_dir, rel)
        with open(full, "rb") as f:
            content = f.read()
        exec_bit = "1" if (os.stat(full).st_mode & 0o111) else "0"
        h.update(rel.encode("utf-8"))
        h.update(str(len(content)).encode("ascii"))
        h.update(exec_bit.encode("ascii"))
        h.update(content)
    return h.hexdigest()


def main():
    all_errors = []

    # 1. Script-capable skills are ALLOWED (run in the claw sandbox via the shell
    #    tool; human-reviewed at webadmin-approve before listing). Report as INFO.
    script_files = check_no_executables()
    for v in script_files:
        print(f"INFO: script-capable (reviewed at approve): {v}")

    # 2. Validate each package's SKILL.md frontmatter
    packages = find_skill_packages()
    if not packages:
        print("INFO: no skill packages found under skills/ (nothing to validate)")
    for pkg_dir, skill_path in packages:
        rel_pkg = os.path.relpath(pkg_dir, REGISTRY_ROOT)
        data, err = parse_frontmatter(skill_path)
        if err:
            all_errors.append(f"{rel_pkg}/SKILL.md: {err}")
            continue
        errs = validate_frontmatter(data, skill_path)
        for e in errs:
            all_errors.append(f"{rel_pkg}/SKILL.md: {e}")
        # Print content digest (informational in Phase A)
        digest = compute_digest(pkg_dir)
        mind_id = data.get("metadata", {}).get("mind.id", "<no-mind-id>") if isinstance(data.get("metadata"), dict) else "<no-mind-id>"
        print(f"OK  {rel_pkg}  mind.id={mind_id}  digest=sha256:{digest}")

    if all_errors:
        print("\nFAIL — validation errors:")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    print("\nPASS — all skills valid (Phase A gates).")
    sys.exit(0)


if __name__ == "__main__":
    main()
