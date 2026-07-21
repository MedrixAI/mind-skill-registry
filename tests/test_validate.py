#!/usr/bin/env python3
"""Self-test harness for scripts/validate_skills.py.

Exercises the parser + frontmatter validator against fixtures under
tests/fixtures/. Run with: ``python3 tests/test_validate.py``.

CI runs this harness after validating the live Registry packages.
"""
import json
import os
import sys
import tempfile
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import validate_skills  # noqa: E402

FIXTURES = os.path.join(HERE, "fixtures")


def _fixture_errors(name):
    skill_md = os.path.join(FIXTURES, name, "SKILL.md")
    data, err = validate_skills.parse_frontmatter(skill_md)
    if err:
        return [err]
    return validate_skills.validate_frontmatter(data, skill_md)


def _fixture_data(name):
    skill_md = os.path.join(FIXTURES, name, "SKILL.md")
    data, err = validate_skills.parse_frontmatter(skill_md)
    if err:
        raise AssertionError(err)
    return data


def _presentation_errors(presentation, description="A canonical description."):
    return validate_skills.validate_presentation(
        json.dumps(presentation, ensure_ascii=False), description
    )


def main():
    cases = [
        # (fixture dir, expected to FAIL with this substring, or None=pass)
        ("valid-builtin", None),
        ("valid-presentation", None),
        ("missing-mind-distribution", "mind.distribution is required"),
        ("description-with-dashes", None),
        ("invalid-presentation-json", "mind.presentation is not valid JSON"),
        (
            "invalid-presentation-description",
            "default locale description must equal",
        ),
        (
            "invalid-presentation-prompts",
            "default locale must contain at least one starter prompt",
        ),
    ]
    failures = []
    for name, expected_err in cases:
        errs = _fixture_errors(name)
        if expected_err is None:
            if errs:
                failures.append(f"{name}: expected PASS, got errors {errs}")
            else:
                print(f"PASS  {name}: validated cleanly")
        else:
            joined = " | ".join(errs)
            if any(expected_err in e for e in errs):
                print(f"PASS  {name}: correctly rejected ({expected_err})")
            else:
                failures.append(
                    f"{name}: expected error containing '{expected_err}', got: {joined}"
                )

    limit_cases = [
        (
            "too-many-locales",
            {
                "default_locale": "en-US",
                "locales": {
                    **{
                        "en-US": {
                            "description": "A canonical description.",
                            "starter_prompts": ["Help me complete this task."],
                        }
                    },
                    **{
                        f"en-{index:03d}": {"description": f"Description {index}."}
                        for index in range(1, 11)
                    },
                },
            },
            "at most 10 locales",
        ),
        (
            "too-many-prompts",
            {
                "default_locale": "en-US",
                "locales": {
                    "en-US": {
                        "description": "A canonical description.",
                        "starter_prompts": [f"Prompt {index}." for index in range(9)],
                    }
                },
            },
            "at most 8 prompts",
        ),
        (
            "description-too-long",
            {
                "default_locale": "en-US",
                "locales": {
                    "en-US": {
                        "description": "x" * 1025,
                        "starter_prompts": ["Help me complete this task."],
                    }
                },
            },
            "exceeds 1024 Unicode code points",
            "x" * 1025,
        ),
        (
            "prompt-too-long",
            {
                "default_locale": "en-US",
                "locales": {
                    "en-US": {
                        "description": "A canonical description.",
                        "starter_prompts": ["x" * 4097],
                    }
                },
            },
            "exceeds 4096 Unicode code points",
        ),
    ]
    for case in limit_cases:
        name, presentation, expected_err, *description = case
        errs = _presentation_errors(
            presentation, description[0] if description else "A canonical description."
        )
        if any(expected_err in error for error in errs):
            print(f"PASS  {name}: correctly rejected ({expected_err})")
        else:
            failures.append(
                f"{name}: expected error containing '{expected_err}', got: {' | '.join(errs)}"
            )

    runtime_cases = [
        ("unknown-runtime-category", {"mind.runtime-category": "not-a-runtime"}, "mind.runtime-category must be one of"),
        ("unknown-runtime-capability", {"mind.runtime-capabilities": '["webapp:unknown"]'}, "contains unknown values"),
        (
            "style-recipe-wrong-category",
            {"mind.runtime-category": "deck", "mind.runtime-capabilities": '["webapp:style-recipes"]'},
            "requires mind.runtime-category=webapp",
        ),
        ("invalid-runtime-default", {"mind.runtime-category": "deck", "mind.runtime-default": "yes"}, "must be the string 'true' or 'false'"),
        ("runtime-default-missing-category", {"mind.runtime-default": "true"}, "requires mind.runtime-category"),
        (
            "marketplace-runtime-default",
            {"mind.distribution": "marketplace", "mind.runtime-category": "deck", "mind.runtime-default": "true"},
            "allowed only for builtin skills",
        ),
    ]
    for name, overrides, expected_err in runtime_cases:
        data = _fixture_data("valid-builtin")
        data["metadata"].update(overrides)
        errs = validate_skills.validate_frontmatter(data, os.path.join(FIXTURES, "valid-builtin", "SKILL.md"))
        if any(expected_err in error for error in errs):
            print(f"PASS  {name}: correctly rejected ({expected_err})")
        else:
            failures.append(f"{name}: expected error containing '{expected_err}', got: {' | '.join(errs)}")

    original_skills_dir = validate_skills.SKILLS_DIR
    with tempfile.TemporaryDirectory() as temp_dir:
        validate_skills.SKILLS_DIR = temp_dir
        builtin_path = Path(temp_dir) / "builtin" / "webapp" / "nested" / "demo" / "SKILL.md"
        builtin_path.parent.mkdir(parents=True)
        data = _fixture_data("valid-builtin")
        data["metadata"]["mind.runtime-category"] = "webapp"
        errs = validate_skills.validate_package_layout(data, str(builtin_path))
        if errs:
            failures.append(f"recursive-builtin-layout: expected PASS, got {errs}")
        else:
            print("PASS  recursive-builtin-layout: validated cleanly")
        marketplace_path = Path(temp_dir) / "marketplace" / "general" / "nested" / "demo" / "SKILL.md"
        marketplace_path.parent.mkdir(parents=True)
        data["metadata"].update({
            "mind.distribution": "marketplace",
            "mind.market-primary": "general",
            "mind.market-categories": '["general"]',
        })
        errs = validate_skills.validate_package_layout(data, str(marketplace_path))
        if errs:
            failures.append(f"recursive-marketplace-layout: expected PASS, got {errs}")
        else:
            print("PASS  recursive-marketplace-layout: validated cleanly")
    validate_skills.SKILLS_DIR = original_skills_dir

    multibyte_description = "界" * 1024
    errs = _presentation_errors(
        {
            "default_locale": "zh-CN",
            "locales": {
                "zh-CN": {
                    "description": multibyte_description,
                    "starter_prompts": ["界" * 4096],
                }
            },
        },
        multibyte_description,
    )
    if errs:
        failures.append(
            "multibyte-character-limits: expected PASS, got errors " + " | ".join(errs)
        )
    else:
        print("PASS  multibyte-character-limits: validated cleanly")
    if failures:
        print("\nFAIL — self-test:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print("\nPASS — all self-test fixtures behaved as expected.")
    sys.exit(0)


if __name__ == "__main__":
    main()
