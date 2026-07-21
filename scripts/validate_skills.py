#!/usr/bin/env python3
"""Validator for recursively organized Registry skill packages.

For each recursively discovered skills/**/SKILL.md:
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
  5. If mind.presentation is present, validate its localized descriptions and
     ordered starter prompts.
  6. Allow executable/script files under skills/ (script-capable skills run in the
     claw sandbox via the shell tool; manually reviewed at webadmin-approve before
     listing). Script files are reported as INFO, not rejected.
  7. Compute and print a content digest per package (sorted relative paths +
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
    "mind.presentation",
    "mind.publisher",
    "mind.runtime-category",
    "mind.runtime-default",
    "mind.runtime-capabilities",
    "mind.tags",
    "mind.min-harness-version",
    "mind.upstream.repo",
    "mind.upstream.commit",
    "mind.upstream.path",
    "mind.upstream.import-mode",
    "mind.upstream.license",
    "mind.upstream.evidence-urls",
}

LOCALE_RE = re.compile(
    r"^[a-z]{2,3}(?:-[A-Z][a-z]{3})?(?:-(?:[A-Z]{2}|[0-9]{3}))?"
    r"(?:-[A-Za-z0-9]{5,8})*$"
)
MAX_PRESENTATION_LOCALES = 10
MAX_STARTER_PROMPTS = 8
MAX_DESCRIPTION_CHARACTERS = 1024
MAX_STARTER_PROMPT_CHARACTERS = 4096

# Script files are allowed (reviewed at approve); collected to report as INFO.
EXECUTABLE_EXTENSIONS = {".sh", ".py", ".bat", ".ps1", ".exe", ".cmd"}
RUNTIME_CATEGORIES = {
    "deck",
    "report",
    "flashcard",
    "webapp",
    "video",
    "audio",
    "infographic",
    # Legacy values remain valid for existing Marketplace packages. New
    # Builtin packages use the canonical categories above.
    "ppt",
    "html",
    "slides",
    "markdown",
}
RUNTIME_CAPABILITIES = {"webapp:style-recipes"}


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


def validate_presentation(raw, canonical_description):
    """Validate the JSON-encoded Marketplace presentation contract."""
    errors = []
    if not isinstance(raw, str):
        return ["mind.presentation must be a JSON object encoded as a string"]
    try:
        presentation = json.loads(raw)
    except json.JSONDecodeError as e:
        return [f"mind.presentation is not valid JSON: {e}"]
    if not isinstance(presentation, dict):
        return ["mind.presentation must decode to an object"]

    unknown_keys = sorted(set(presentation) - {"default_locale", "locales"})
    if unknown_keys:
        errors.append(f"mind.presentation has unknown fields: {unknown_keys}")

    default_locale = presentation.get("default_locale")
    if not isinstance(default_locale, str) or not LOCALE_RE.fullmatch(default_locale):
        errors.append("mind.presentation.default_locale must be a canonical locale tag")

    locales = presentation.get("locales")
    if not isinstance(locales, dict) or not locales:
        errors.append("mind.presentation.locales must be a non-empty object")
        return errors
    if len(locales) > MAX_PRESENTATION_LOCALES:
        errors.append(
            f"mind.presentation.locales must contain at most {MAX_PRESENTATION_LOCALES} locales"
        )
    if isinstance(default_locale, str) and default_locale not in locales:
        errors.append("mind.presentation.default_locale entry is missing from locales")

    for locale, localized in locales.items():
        prefix = f"mind.presentation.locales[{locale!r}]"
        if not isinstance(locale, str) or not LOCALE_RE.fullmatch(locale):
            errors.append(f"{prefix} uses an invalid locale tag")
        if not isinstance(localized, dict):
            errors.append(f"{prefix} must be an object")
            continue
        unknown_localized_keys = sorted(
            set(localized) - {"description", "starter_prompts"}
        )
        if unknown_localized_keys:
            errors.append(f"{prefix} has unknown fields: {unknown_localized_keys}")

        description = localized.get("description")
        if not isinstance(description, str) or not description.strip():
            errors.append(f"{prefix}.description must be a non-empty string")
        elif len(description) > MAX_DESCRIPTION_CHARACTERS:
            errors.append(
                f"{prefix}.description exceeds {MAX_DESCRIPTION_CHARACTERS} "
                "Unicode code points"
            )
        if locale == default_locale and description != canonical_description:
            errors.append(
                "mind.presentation default locale description must equal the "
                "canonical top-level description"
            )

        prompts = localized.get("starter_prompts")
        if prompts is None:
            prompts = []
        elif not isinstance(prompts, list):
            errors.append(f"{prefix}.starter_prompts must be an array of strings")
            continue
        if len(prompts) > MAX_STARTER_PROMPTS:
            errors.append(
                f"{prefix}.starter_prompts must contain at most {MAX_STARTER_PROMPTS} prompts"
            )
        if locale == default_locale and not prompts:
            errors.append(
                "mind.presentation default locale must contain at least one starter prompt"
            )
        for index, prompt in enumerate(prompts):
            prompt_prefix = f"{prefix}.starter_prompts[{index}]"
            if not isinstance(prompt, str) or not prompt.strip():
                errors.append(f"{prompt_prefix} must be a non-empty string")
            elif len(prompt) > MAX_STARTER_PROMPT_CHARACTERS:
                errors.append(
                    f"{prompt_prefix} exceeds {MAX_STARTER_PROMPT_CHARACTERS} "
                    "Unicode code points"
                )
    return errors


def validate_frontmatter(data, skill_path):
    """Validate frontmatter fields per spec §6.3/§6.7. Returns list of errors."""
    errors = []
    # Required top-level fields
    for field in ("name", "description", "license"):
        val = data.get(field)
        if val is None or (isinstance(val, str) and not val.strip()):
            errors.append(f"missing or empty required field: {field}")
    allowed_tools = data.get("allowed-tools")
    if allowed_tools is not None:
        valid_tools = (
            isinstance(allowed_tools, str) and bool(allowed_tools.strip())
        ) or (
            isinstance(allowed_tools, list)
            and bool(allowed_tools)
            and all(isinstance(tool, str) and tool.strip() for tool in allowed_tools)
        )
        if not valid_tools:
            errors.append(
                "allowed-tools must be a non-empty string or an array of non-empty tool names"
            )
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
            presentation = metadata.get("mind.presentation")
            if presentation is not None:
                errors.extend(validate_presentation(presentation, data.get("description")))
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
            runtime_category = metadata.get("mind.runtime-category")
            if runtime_category and runtime_category not in RUNTIME_CATEGORIES:
                errors.append(
                    "mind.runtime-category must be one of "
                    f"{sorted(RUNTIME_CATEGORIES)}, got: {runtime_category!r}"
                )
            runtime_default = metadata.get("mind.runtime-default")
            if runtime_default is not None:
                if runtime_default not in {"true", "false"}:
                    errors.append("mind.runtime-default must be the string 'true' or 'false'")
                elif runtime_default == "true":
                    if dist != "builtin":
                        errors.append("mind.runtime-default=true is allowed only for builtin skills")
                    if not runtime_category:
                        errors.append("mind.runtime-default=true requires mind.runtime-category")
            capabilities_raw = metadata.get("mind.runtime-capabilities")
            if capabilities_raw is not None:
                try:
                    capabilities = json.loads(capabilities_raw) if isinstance(capabilities_raw, str) else capabilities_raw
                except (json.JSONDecodeError, TypeError) as e:
                    errors.append(f"mind.runtime-capabilities is not valid JSON: {e}")
                    capabilities = None
                if not isinstance(capabilities, list) or any(
                    not isinstance(capability, str) for capability in capabilities or []
                ):
                    errors.append("mind.runtime-capabilities must be a JSON array of strings")
                elif unknown := sorted(set(capabilities) - RUNTIME_CAPABILITIES):
                    errors.append(f"mind.runtime-capabilities contains unknown values: {unknown}")
                if isinstance(capabilities, list) and "webapp:style-recipes" in capabilities and runtime_category != "webapp":
                    errors.append("webapp:style-recipes requires mind.runtime-category=webapp")
    errors.extend(validate_package_layout(data, skill_path))
    return errors


def find_skill_packages():
    """Find every package root, regardless of organizational directory depth."""
    packages = []
    if not os.path.isdir(SKILLS_DIR):
        return packages
    for root, dirs, files in os.walk(SKILLS_DIR):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        if "SKILL.md" in files:
            packages.append((root, os.path.join(root, "SKILL.md")))
    return sorted(packages)


def validate_package_layout(data, skill_path):
    """Validate lane/category directories without using them as runtime truth."""
    package_dir = os.path.dirname(skill_path)
    skills_root = os.path.realpath(SKILLS_DIR)
    package_root = os.path.realpath(package_dir)
    if package_root != skills_root and not package_root.startswith(skills_root + os.sep):
        return []
    rel = os.path.relpath(package_dir, SKILLS_DIR).replace(os.sep, "/")
    parts = rel.split("/")
    if len(parts) < 3 or parts[0] not in {"builtin", "marketplace"}:
        return ["package path must be skills/<builtin|marketplace>/<category>/.../<slug>"]
    lane, organization = parts[0], parts[1]
    metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
    distribution = metadata.get("mind.distribution")
    errors = []
    if distribution != lane:
        errors.append(f"path lane {lane!r} must match mind.distribution {distribution!r}")
    if lane == "builtin":
        expected = metadata.get("mind.runtime-category") or "general"
        if organization != expected:
            errors.append(f"builtin organization {organization!r} must match runtime category {expected!r}")
    else:
        expected = metadata.get("mind.market-primary")
        if not expected:
            errors.append("marketplace packages require mind.market-primary")
        elif organization != expected:
            errors.append(f"marketplace organization {organization!r} must match mind.market-primary {expected!r}")
    return errors


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
    0o111`` → ``1`` or ``0``) into the per-file digest stream. Script-capable
    packages are allowed, so this bit is part of the stable digest contract.
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
    #    tool; manually reviewed at webadmin-approve before listing). Report as INFO.
    script_files = check_no_executables()
    for v in script_files:
        print(f"INFO: script-capable (reviewed at approve): {v}")

    # 2. Validate each package's SKILL.md frontmatter
    packages = find_skill_packages()
    if not packages:
        print("INFO: no skill packages found under skills/ (nothing to validate)")
    seen_names = {}
    seen_ids = {}
    seen_runtime_defaults = {}
    package_roots = {os.path.realpath(pkg_dir) for pkg_dir, _ in packages}
    for pkg_dir, skill_path in packages:
        rel_pkg = os.path.relpath(pkg_dir, REGISTRY_ROOT)
        data, err = parse_frontmatter(skill_path)
        if err:
            all_errors.append(f"{rel_pkg}/SKILL.md: {err}")
            continue
        errs = validate_frontmatter(data, skill_path)
        for e in errs:
            all_errors.append(f"{rel_pkg}/SKILL.md: {e}")
        name = data.get("name")
        metadata = data.get("metadata", {}) if isinstance(data.get("metadata"), dict) else {}
        mind_id = metadata.get("mind.id")
        for value, seen, label in ((name, seen_names, "name"), (mind_id, seen_ids, "mind.id")):
            if not value:
                continue
            if value in seen:
                all_errors.append(f"{rel_pkg}/SKILL.md: duplicate {label} {value!r}; first used by {seen[value]}")
            else:
                seen[value] = rel_pkg
        if metadata.get("mind.runtime-default") == "true":
            category = metadata.get("mind.runtime-category")
            if category in seen_runtime_defaults:
                all_errors.append(
                    f"{rel_pkg}/SKILL.md: duplicate runtime default for {category!r}; first used by {seen_runtime_defaults[category]}"
                )
            else:
                seen_runtime_defaults[category] = rel_pkg
        parent = os.path.realpath(os.path.dirname(pkg_dir))
        while parent.startswith(os.path.realpath(SKILLS_DIR) + os.sep):
            if parent in package_roots:
                all_errors.append(
                    f"{rel_pkg}/SKILL.md: nested package roots are not allowed; parent package is {os.path.relpath(parent, REGISTRY_ROOT)}"
                )
                break
            parent = os.path.dirname(parent)
        # Print content digest (informational in Phase A)
        digest = compute_digest(pkg_dir)
        print(f"OK  {rel_pkg}  mind.id={mind_id or '<no-mind-id>'}  digest=sha256:{digest}")

    if all_errors:
        print("\nFAIL — validation errors:")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    print("\nPASS — all skills valid (Phase A gates).")
    sys.exit(0)


if __name__ == "__main__":
    main()
