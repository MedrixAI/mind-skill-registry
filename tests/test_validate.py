#!/usr/bin/env python3
"""Self-test harness for scripts/validate_skills.py.

Exercises the parser + frontmatter validator against fixtures under
tests/fixtures/. Run with: ``python3 tests/test_validate.py``.

Not wired into .github/workflows/ci.yml (CI only runs the Phase-A skills/
gate). This harness is the local authoring check; CI remains green as long
as skills/ is clean.
"""
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


def main():
    cases = [
        # (fixture dir, expected to FAIL with this substring, or None=pass)
        ("valid-builtin", None),
        ("missing-mind-distribution", "mind.distribution is required"),
        ("description-with-dashes", None),
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
    if failures:
        print("\nFAIL — self-test:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print("\nPASS — all self-test fixtures behaved as expected.")
    sys.exit(0)


if __name__ == "__main__":
    main()
