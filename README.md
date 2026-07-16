# mind-skill-registry

The official Skill Registry for Mind (MedrixAI) — a protected, public, vendored
Git repository that is the authoritative version store for officially maintained
Agent Harness Skills. A Registry commit is synchronized into Mind as a staged
candidate gated by review before it becomes visible, subscribable, or runnable.
Git merge or source sync never publishes directly to the Marketplace.

**Design spec:** `mind-api` repo
`docs/superpowers/specs/2026-07-14-official-skill-registry-marketplace-design.md`

**Mind API implementation:** `mind-api` repo (knowledge service
`github_repo` source sync, `official_registry` trust profile).

## Repository layout

```
mind-skill-registry/
├── README.md                  # this file
├── LICENSE                    # Apache-2.0 (covers tooling/schema only)
├── CODEOWNERS                 # review ownership
├── categories.yaml            # v1 seven-class taxonomy (spec §6.5)
├── schemas/
│   └── skill.schema.json      # SKILL.md frontmatter schema (spec §6.3)
├── policies/
│   ├── trust.md               # trust model + Phase A scope (spec §4.2)
│   └── review-policy.yaml     # change-class → required-review mapping (spec §6.7)
├── skills/                    # one directory per skill package
│   ├── mind/<skill-name>/     # MedrixAI originals
│   └── curated/<publisher>/<skill-name>/  # vendored third-party
└── .github/workflows/
    └── ci.yml                 # Phase-A CI gates
```

There is no source-of-truth `catalog.yaml`. The package list is derived from a
filesystem scan (stop on first `SKILL.md` in a subtree) plus each package's
frontmatter `mind.id` (spec §3, §6.6).

## Categories

The v1 taxonomy has seven stable slugs defined in `categories.yaml` (spec §6.5):

| Slug | zh-CN | Legacy aliases |
|---|---|---|
| `general` | 通用 | — |
| `development-tools` | 开发工具 | `code` |
| `content-creation` | 内容创作 | `writing`, `image`, `slides`, `video`, `web` |
| `data-analysis` | 数据分析 | `data` |
| `productivity-tools` | 效率工具 | — |
| `business-operations` | 商业运营 | — |
| `knowledge-learning` | 知识与学习 | `learning` |

Five legacy single-value categories fold into `content-creation` by deliberate
consolidation. Category IDs are permanent.

## CI gates (Phase A)

The CI workflow (`.github/workflows/ci.yml`) runs on every push/PR to `main` and
on any `skills/**` change. Phase-A gates:

- Parse YAML frontmatter for each `skills/*/SKILL.md`.
- Assert required fields: `name`, `description`, `license`.
- If `metadata.mind.*` keys present: assert `mind.id` + `mind.distribution` in
  `{builtin, marketplace}`; reject unknown `mind.*` keys.
- Assert `mind.market-primary` is in `mind.market-categories` (if both present).
- Reject any `.sh`, `.py`, `.bat`, `.ps1`, `.exe`, `.cmd` file under `skills/`
  (Phase A = no executables; fail closed).
- Compute + print a content digest per package (sorted relative paths + file
  bytes + length) for reproducibility (informational in Phase A).

**Deferred to Phase B** (full §6.7 suite): deterministic archive build twice,
SBOM, provenance attestation, secret scanning, static capability analysis,
per-package SPDX/license/notice consistency, risk-based review-policy
enforcement, contract tests and eval fixtures.

## Contribution model

1. Author or vendor a skill under `skills/mind/<name>/` or
   `skills/curated/<publisher>/<name>/`.
2. Ensure the `SKILL.md` frontmatter passes `python scripts/validate_skills.py`.
3. Open a PR against `main`.
4. CI runs Phase-A gates. Required CODEOWNER review applies per
   `policies/review-policy.yaml` (spec §6.7).
5. Merge is a Registry commit — it is the version record, not a Marketplace
   publish. Mind Webadmin sync resolves the commit SHA, verifies the digest,
   stages a candidate, and a separate approve + list action publishes to the
   Marketplace.

**Registry merge ≠ Marketplace publish.** A merged commit becomes a Mind
candidate only after Webadmin sync + review + approve.

## License

Apache-2.0. The root license covers Registry tooling and schema only. Each
package carries its own `LICENSE.txt` (and `NOTICE.txt`/`MODIFICATIONS.md` when
applicable for vendored third-party content).
