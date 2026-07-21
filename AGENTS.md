# AGENTS.md

> **Codex:** complete agent instructions are in [`CLAUDE.md`](CLAUDE.md).

This file exists for Codex compatibility. Before any non-trivial change, read `CLAUDE.md` completely; do not assume the linked file has already been loaded.

The short version:

- Builtin skills live under `skills/builtin/<runtime-category|general>/.../<slug>/`; Marketplace skills live under `skills/marketplace/<market-primary>/.../<slug>/`.
- Intermediate directories are organizational; recursive discovery stops at the first `SKILL.md`, and frontmatter is the runtime source of truth.
- Preserve stable `metadata.mind.id` values when updating or moving a skill.
- Follow `categories.yaml`, `policies/review-policy.yaml`, and `policies/trust.md`.
- Run `python3 scripts/validate_skills.py`, `python3 tests/test_validate.py`, `python3 scripts/generate_skill_catalog.py --check`, and `git diff --check` before handoff.
- A merged Registry PR is not live until Mind Webadmin syncs and approves the candidate.
- Builtin availability skips tenant subscription but never bypasses an Agent's `all` / `selected` / `none` activation policy; Marketplace requires subscription before the same Agent activation step.
- Do not push, merge, approve, or unlist unless that action is explicitly requested.
