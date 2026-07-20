#!/usr/bin/env python3
"""Refresh the embedded data in the standalone interactive Skill catalog.

Marketplace entries always come from this Registry working tree. Builtin entries
come from ``--mind-api-root`` when supplied; otherwise the existing embedded
Builtin snapshot is preserved so normal Registry-only maintenance stays local.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

import yaml


REGISTRY_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_HTML = REGISTRY_ROOT / "skill-catalog.html"
DATA_BLOCK_RE = re.compile(
    r'(<script id="skill-data" type="application/json">\n)(.*?)(\n</script>)',
    re.DOTALL,
)
FRONTMATTER_RE = re.compile(r"^---\s*$", re.MULTILINE)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    parts = FRONTMATTER_RE.split(text, maxsplit=2)
    if len(parts) < 3:
        raise ValueError(f"malformed frontmatter: {path}")
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError(f"frontmatter is not a mapping: {path}")
    return data


def parse_json_list(value: object, field: str, path: Path) -> list[str]:
    if value in (None, ""):
        return []
    try:
        parsed = json.loads(value) if isinstance(value, str) else value
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid {field} JSON in {path}: {exc}") from exc
    if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
        raise ValueError(f"{field} must be a string array in {path}")
    return parsed


def repository_label(repo_url: str, commit: str) -> str:
    match = re.search(r"github\.com/([^/]+/[^/]+?)(?:\.git)?$", repo_url.rstrip("/"))
    repo = match.group(1) if match else repo_url
    return f"{repo}@{commit[:7]}" if commit else repo


def upstream_source(metadata: dict, path: Path) -> tuple[str, str]:
    repo_url = str(metadata.get("mind.upstream.repo", "")).rstrip("/")
    if repo_url.endswith(".git"):
        repo_url = repo_url[:-4]
    commit = str(metadata.get("mind.upstream.commit", ""))
    upstream_path = str(metadata.get("mind.upstream.path", "")).strip("/")
    if not (repo_url and commit and upstream_path):
        raise ValueError(f"incomplete upstream source metadata: {path}")
    if not upstream_path.lower().endswith("skill.md"):
        upstream_path = f"{upstream_path}/SKILL.md"
    source_url = f"{repo_url}/blob/{commit}/{quote(upstream_path, safe='/-._~')}"
    return repository_label(repo_url, commit), source_url


def load_marketplace_categories() -> set[str]:
    data = yaml.safe_load((REGISTRY_ROOT / "categories.yaml").read_text(encoding="utf-8"))
    return {
        item["slug"]
        for item in data.get("categories", [])
        if item.get("status") == "active" and item.get("slug")
    }


def build_marketplace_entries() -> list[dict]:
    canonical_categories = load_marketplace_categories()
    entries = []
    for skill_path in sorted((REGISTRY_ROOT / "skills").glob("*/SKILL.md")):
        slug = skill_path.parent.name
        data = parse_frontmatter(skill_path)
        metadata = data.get("metadata") or {}
        if not isinstance(metadata, dict):
            raise ValueError(f"metadata is not a mapping: {skill_path}")

        primary = str(metadata.get("mind.market-primary", ""))
        categories = parse_json_list(
            metadata.get("mind.market-categories"), "mind.market-categories", skill_path
        )
        if not primary or primary not in canonical_categories:
            raise ValueError(f"invalid Marketplace primary category in {skill_path}: {primary!r}")
        invalid_categories = sorted(set(categories) - canonical_categories)
        if invalid_categories:
            raise ValueError(
                f"invalid Marketplace categories in {skill_path}: {invalid_categories}"
            )
        if primary not in categories:
            raise ValueError(f"primary category missing from category list: {skill_path}")

        upstream_repo = metadata.get("mind.upstream.repo")
        if upstream_repo:
            source_label, source_url = upstream_source(metadata, skill_path)
            source_kind = "third-party"
            publisher = str(metadata.get("mind.publisher") or source_label.split("/", 1)[0])
        else:
            source_label = "MedrixAI/mind-skill-registry"
            source_url = (
                "https://github.com/MedrixAI/mind-skill-registry/blob/main/"
                f"skills/{quote(slug, safe='-._~')}/SKILL.md"
            )
            source_kind = "first-party"
            publisher = str(metadata.get("mind.publisher") or "MedrixAI")

        description = str(data.get("description", "")).strip()
        entries.append(
            {
                "type": "marketplace",
                "slug": slug,
                "name": str(data.get("name", slug)),
                "description": description,
                "summary": str(
                    metadata.get("mind.marketplace-summary") or description
                ).strip(),
                "primaryCategory": primary,
                "categories": categories,
                "sourceKind": source_kind,
                "sourceLabel": source_label,
                "sourceUrl": source_url,
                "publisher": publisher,
                "mindId": str(metadata.get("mind.id", "")),
                "license": str(data.get("license", "")),
                "tags": parse_json_list(metadata.get("mind.tags"), "mind.tags", skill_path),
            }
        )
    return entries


def classify_builtin(name: str) -> str:
    normalized = name.lower()
    if (
        normalized == "ppt-master"
        or normalized.startswith("html-deck-")
        or normalized.startswith("html-ppt-")
        or normalized.startswith("html-poster-")
        or normalized.startswith("html-frame-")
        or normalized in {"html-social-carousel", "html-magazine-poster"}
    ):
        return "deck"
    if normalized in {"flashcard-master", "quiz-master"}:
        return "flashcard"
    if normalized in {
        "report-master",
        "html-data-report",
        "html-finance-report",
        "html-exec-briefing-memo",
        "html-experiment-readout",
        "html-doc-kami-parchment",
        "html-docs-page",
        "html-article-magazine",
        "html-blog-post",
        "html-meeting-notes",
        "html-pm-spec",
        "html-eng-runbook",
        "html-weekly-update",
        "html-digital-eguide",
        "html-competitive-teardown",
    }:
        return "report"
    if (
        normalized in {"html-web-design-engineer", "web-design-engineer"}
        or normalized.startswith("html-mobile-")
        or normalized.startswith("html-saas-")
        or normalized.startswith("html-pricing-")
        or normalized.startswith("html-waitlist-")
        or normalized.startswith("html-prototype-")
        or normalized.startswith("html-web-proto-")
        or normalized.startswith("html-flowai-")
        or normalized.startswith("html-card-")
        or normalized.startswith("html-social-")
        or normalized
        in {
            "html-gamified-app",
            "html-kanban-board",
            "html-dashboard",
            "html-live-dashboard",
            "html-social-media-dashboard",
            "html-team-okrs",
            "html-resume-modern",
            "html-invoice",
            "html-email-marketing",
            "html-dating-web",
            "html-hr-onboarding",
            "html-wireframe-sketch",
        }
    ):
        return "webapp"
    return "uncategorized"


def build_builtin_entries(mind_api_root: Path) -> list[dict]:
    skills_root = mind_api_root / "knowledge" / "skills" / "preloaded"
    if not skills_root.is_dir():
        raise ValueError(f"Builtin directory not found: {skills_root}")

    entries = []
    for skill_path in sorted(skills_root.glob("*/SKILL.md")):
        slug = skill_path.parent.name
        data = parse_frontmatter(skill_path)
        name = str(data.get("name", slug))
        description = str(data.get("description", "")).strip()
        category = classify_builtin(name)
        entries.append(
            {
                "type": "builtin",
                "slug": slug,
                "name": name,
                "description": description,
                "summary": description,
                "primaryCategory": category,
                "categories": [category],
                "sourceKind": "first-party",
                "sourceLabel": "MedrixAI/mind-api",
                "sourceUrl": (
                    "https://github.com/MedrixAI/mind-api/blob/main/"
                    f"knowledge/skills/preloaded/{quote(slug, safe='-._~')}/SKILL.md"
                ),
                "publisher": "MedrixAI",
                "mindId": "",
                "license": str(data.get("license", "")),
                "tags": [],
            }
        )
    return entries


def load_existing_catalog(html: str) -> dict:
    match = DATA_BLOCK_RE.search(html)
    if not match:
        raise ValueError("skill-data JSON block not found in HTML")
    try:
        data = json.loads(match.group(2))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid embedded catalog JSON: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("skills"), list):
        raise ValueError("embedded catalog JSON has an unexpected shape")
    return data


def validate_unique(entries: list[dict]) -> None:
    seen = set()
    duplicates = set()
    for entry in entries:
        key = (entry["type"], entry["slug"].lower())
        if key in seen:
            duplicates.add(f"{entry['type']}:{entry['slug']}")
        seen.add(key)
    if duplicates:
        raise ValueError(f"duplicate catalog entries: {sorted(duplicates)}")


def serialize_data(data: dict) -> str:
    serialized = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False)
    return (
        serialized.replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", type=Path, default=DEFAULT_HTML)
    parser.add_argument(
        "--mind-api-root",
        type=Path,
        help="Refresh Builtin entries from this mind-api checkout.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero when the embedded Marketplace data is stale.",
    )
    args = parser.parse_args()

    html_path = args.html.resolve()
    html = html_path.read_text(encoding="utf-8")
    existing = load_existing_catalog(html)

    if args.mind_api_root:
        builtin_entries = build_builtin_entries(args.mind_api_root.resolve())
    else:
        builtin_entries = [
            entry for entry in existing["skills"] if entry.get("type") == "builtin"
        ]
        if not builtin_entries:
            raise ValueError(
                "no embedded Builtin snapshot; supply --mind-api-root for the initial build"
            )

    marketplace_entries = build_marketplace_entries()
    entries = sorted(
        [*builtin_entries, *marketplace_entries],
        key=lambda item: (item["type"], item["slug"].casefold()),
    )
    validate_unique(entries)

    data = {
        "schemaVersion": 1,
        "sources": [
            {
                "type": "builtin",
                "repository": "MedrixAI/mind-api",
                "ref": "main",
                "count": len(builtin_entries),
            },
            {
                "type": "marketplace",
                "repository": "MedrixAI/mind-skill-registry",
                "ref": "main",
                "count": len(marketplace_entries),
            },
        ],
        "skills": entries,
    }
    replacement = serialize_data(data)
    rendered = DATA_BLOCK_RE.sub(
        lambda match: f"{match.group(1)}{replacement}{match.group(3)}", html, count=1
    )

    if args.check:
        if rendered != html:
            print(
                "ERROR: skill-catalog.html is stale; run "
                "python3 scripts/generate_skill_catalog.py",
                file=sys.stderr,
            )
            return 1
        print(
            f"PASS: catalog is current ({len(builtin_entries)} Builtin, "
            f"{len(marketplace_entries)} Marketplace)"
        )
        return 0

    html_path.write_text(rendered, encoding="utf-8")
    print(
        f"Updated {html_path.relative_to(REGISTRY_ROOT)}: "
        f"{len(builtin_entries)} Builtin, {len(marketplace_entries)} Marketplace"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
