#!/usr/bin/env python3
"""Self-test harness for scripts/validate_skills.py.

Exercises the parser + frontmatter validator against fixtures under
tests/fixtures/. Run with: ``python3 tests/test_validate.py``.

Not wired into .github/workflows/ci.yml (CI only runs the Phase-A skills/
gate). This harness is the local authoring check; CI remains green as long
as skills/ is clean.
"""
import json
import os
import sys

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
