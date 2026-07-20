# CLAUDE.md

This is the complete operating guide for agents working in
`MedrixAI/mind-skill-registry`. Read it before every non-trivial change. Do not
assume any prior conversation, local setup, or production state.

## 1. Mission and System Boundary

This repository is the reviewed Git source for officially maintained Mind
Marketplace Skill packages. It owns:

- `SKILL.md` instructions and discovery metadata;
- bundled scripts, references, templates, and assets;
- canonical Marketplace classification intent;
- package license records;
- immutable third-party provenance;
- Registry validation, policy, and release evidence.

It does not directly serve live Skill content. The release chain is:

```text
Registry working tree
  -> focused commit and PR
  -> merge to Registry main
  -> WebAdmin sync of official-registry
  -> pending candidate in Mind database
  -> WebAdmin candidate approval
  -> shared live Marketplace row
  -> tenant subscription
  -> Agent skill_search / read_skill
```

A commit, push, PR, merge, sync, approval, listing change, or removal is a
separate state transition. Perform only the transitions explicitly included in
the task. An edit request authorizes working-tree changes and validation; it
does not authorize commit, push, merge, or WebAdmin actions.

The live runtime source is the approved Mind database row. Existing
Marketplace subscriptions reference that shared row rather than a copied Skill,
so an approved content update reaches existing subscriptions immediately.

Platform builtins are a separate release lane under
`mind-api/knowledge/skills/preloaded/`. Current packages in this Registry use
`mind.distribution: marketplace`. Although the contract accepts `builtin`, that
value alone does not move a package into the platform-builtin lane.

## 2. Source-of-Truth Order

Use this order when facts conflict:

1. The requested outcome and explicit authority boundary.
2. Current Registry package bytes and stable `metadata.mind.id` values.
3. `categories.yaml` for Marketplace category slugs.
4. `policies/review-policy.yaml` and `policies/trust.md` for review and trust.
5. `schemas/skill.schema.json` and `scripts/validate_skills.py` for the local
   contract.
6. Current `mind-api` implementation for sync, approval, storage,
   subscription, and runtime behavior.
7. The approved production database row for current live state.

Important implementation paths in the `mind-api` repository:

```text
knowledge/internal/agent/skills/skill.go
knowledge/internal/application/service/skill_frontmatter.go
knowledge/internal/application/service/skill_seed.go
knowledge/internal/application/service/skill_syncer.go
knowledge/internal/application/service/skill_update_admin.go
knowledge/internal/application/service/skill_subscription_service.go
knowledge/internal/application/repository/skill_repository.go
knowledge/internal/agent/skills/db_source.go
knowledge/internal/agent/tools/skill_search.go
knowledge/internal/agent/tools/skill_read.go
```

If a Registry document disagrees with current runtime code, do not silently
choose one. Record the mismatch, determine whether the task includes the
required cross-repository change, and stop before release if the mismatch can
change production behavior.

## 3. Mandatory Startup Procedure

Run from the Registry root:

```bash
git status --short
git branch --show-current
git remote -v
git fetch origin
git rev-parse HEAD
git rev-parse origin/main
```

Then:

1. Preserve every existing modification and untracked file.
2. Do not pull, rebase, switch branches, or overwrite files while overlapping
   changes are unresolved.
3. Read `README.md`, this file, the affected packages, `categories.yaml`,
   `policies/review-policy.yaml`, `policies/trust.md`, and
   `scripts/validate_skills.py`.
4. Read `schemas/skill.schema.json` and `.github/workflows/ci.yml` when changing
   frontmatter, validation, policy, CI, or release behavior.
5. Compare against current `origin/main`; do not assume the checkout is current.
6. Classify the operation using the next section before editing.
7. Inventory slug, `name`, and `mind.id` collisions across the whole Registry.

Use a focused feature branch for normal Registry changes. Do not create a
commit or push unless explicitly requested.

## 4. Classify the Operation First

| Operation | Stable identity | Expected Registry sync result | Separate live action |
|---|---|---|---|
| Add first-party package | New `mind.id` | New pending draft | Approve candidate |
| Add third-party package | New `mind.id` plus pinned provenance | New pending draft | Required review, then approve |
| Update content/resources | Preserve `mind.id` | Pending update when content hash changes | Approve candidate |
| Re-vendor upstream | Preserve `mind.id`; update upstream SHA | Pending update when vendored bytes change | Required review, then approve |
| Move directory only | Preserve `mind.id` and `name` | Usually `skipped`; provenance path can backfill | Usually none |
| Rename `name` | Preserve `mind.id` | Registry approval currently preserves the live name | Separate supported rename path |
| Reclassify primary category only | Preserve `mind.id` | Usually `skipped` | WebAdmin category update or runtime enhancement |
| Change tags/summary/publisher only | Preserve `mind.id` | Usually `skipped` | WebAdmin for live display; tags are not fully projected |
| Remove package | Retire `mind.id`; never reuse | No deletion candidate | Unlist or stronger withdrawal first |
| Batch maintenance | Preserve every existing `mind.id` | One result per content-drift package | Reconcile each candidate before approval |

Do not convert one operation into another to bypass a system limitation. In
particular, do not add whitespace or no-op instruction edits merely to force a
pending candidate.

## 5. Conditions That Require a Pause

Pause and request clarification when any of these conditions applies:

- The requested capability already exists under a different slug or name.
- An existing published `mind.id` would need to change, be reused, or be split.
- The desired live effect depends only on metadata that current approval does
  not project.
- A live `name` rename is required but no separate rename path is in scope.
- An update removes the final bundled file but no runtime fix or verified
  content-replacement path is in scope.
- `builtin` versus `marketplace` changes the release lane.
- Third-party ownership, license, redistribution rights, or evidence is unclear.
- The package requests credentials, private data, broad filesystem access,
  destructive commands, undeclared network access, or unavailable tools.
- A vendored package contains suspicious instruction overrides or data-exfiltration
  behavior.
- Existing working-tree changes overlap the requested package.
- WebAdmin shows an unexpected source SHA, candidate set, sync status, or live
  version.
- Removal intent is ambiguous between stopping new discovery and blocking all
  existing runtime access.

No policy, validation rule, identity value, or provenance record may be weakened
to avoid a pause.

## 6. Repository and Package Discovery Model

Current packages use this flat layout:

```text
skills/<slug>/
├── SKILL.md
├── LICENSE or LICENSE.txt
├── NOTICE.txt              # when required
├── MODIFICATIONS.md        # curated third-party changes
├── scripts/                # optional
├── references/             # optional
└── assets/                 # optional
```

Important root files:

```text
categories.yaml                 # canonical Marketplace taxonomy
schemas/skill.schema.json       # documented frontmatter shape
policies/review-policy.yaml     # change class to required approval
policies/trust.md               # trust and security boundary
skill-catalog.html              # standalone interactive Builtin/Marketplace catalog
scripts/generate_skill_catalog.py # refreshes the catalog's embedded data
scripts/validate_skills.py      # local and CI phase-A validator
tests/test_validate.py          # validator self-test, run locally
.github/workflows/ci.yml        # currently runs the validator only
```

The Mind scanner walks recursively. The first `SKILL.md` found in a subtree
defines the package root; every regular file beneath it becomes part of that
package. The scanner then stops descending for additional packages. Therefore:

- keep one package at `skills/<slug>/`;
- never place a second Skill package beneath another package;
- treat a nested `SKILL.md` as an accidental bundled file unless that is
  explicitly intended;
- remove `.DS_Store`, caches, build output, virtual environments, dependency
  trees, and other generated files from package directories;
- assume every file under a package is shipped and hashed, even when it is not
  referenced by the instructions.

Hidden directories above package roots are skipped by the Mind scanner, but
hidden files inside a package can still be bundled. The official source fetch
also performs a repository-wide unsafe-worktree scan before package discovery.

There is no hand-maintained Registry manifest. Filesystem discovery plus
`metadata.mind.id` determines the candidate set and stable reconciliation key.

## 7. Identity Invariants

Three identifiers have different roles:

| Identifier | Role | Change rule |
|---|---|---|
| `skills/<slug>` | Git location | May move; keep readable and unique |
| frontmatter `name` | Runtime discovery name | Keep stable; live rename needs separate handling |
| `metadata.mind.id` | Source reconciliation identity | Permanent after first publication |

Use lowercase ASCII kebab-case for both slug and `name`, and normally keep them
equal. Use a reverse-domain key such as
`ai.medrix.skill.<stable-slug>` for `mind.id`.

The runtime parser currently enforces:

- `name` is required and has a 64-byte implementation limit;
- `description` is required and has a 1024-byte implementation limit;
- the name matches Unicode letters, numbers, and hyphens;
- XML-like tags are rejected in `name` and `description`;
- substrings `anthropic` and `claude` are reserved except for an explicit
  runtime allowlist;
- YAML frontmatter must start and end with a `---` delimiter line.

The parser error text says lowercase even though the regex currently permits
uppercase and Unicode. Follow the stricter Registry convention: lowercase ASCII
letters, digits, and hyphens only.

Before adding or renaming, inspect all identities:

```bash
rg -n '^name:' skills/*/SKILL.md
rg -n '^  mind\.id:' skills/*/SKILL.md
find skills -mindepth 1 -maxdepth 1 -type d -print | sort
rg --no-filename '^name:' skills/*/SKILL.md | sort | uniq -d
rg --no-filename '^  mind\.id:' skills/*/SKILL.md | sort | uniq -d
```

The last two commands must produce no output.

For a targeted check:

```bash
rg -n '^name: <name>$|mind\.id: <mind-id>$' skills
test ! -e 'skills/<slug>'
```

Do not rely on the current validator to detect duplicate names, duplicate
`mind.id` values, or case-insensitive path collisions.

Mind resolves an existing Registry Skill by `(source_id, mind.id)` first, then
falls back to `(tenant_id, name)`. Changing `mind.id` can bind incorrectly by
the name fallback or create an unintended identity. A retired `mind.id` remains
retired permanently.

## 8. Exact `SKILL.md` Contract

Every package requires YAML frontmatter followed by instruction content.

### 8.1 First-party template

```markdown
---
name: example-skill
description: Perform a specific workflow. Use when the task needs X, Y, or Z.
license: Apache-2.0
compatibility: Requires Mind Agent Harness 1.0 or later.
allowed-tools:
  - web_search
metadata:
  mind.id: ai.medrix.skill.example-skill
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools"]'
  mind.marketplace-summary: A short Marketplace-facing summary.
  mind.publisher: medrixai
  mind.tags: '["example"]'
  mind.min-harness-version: ">=1.0.0"
---

# Example Skill

...instructions...
```

Only declare `allowed-tools` and `compatibility` when the package actually needs
them. A declaration describes a requirement; it never grants runtime
permission.

### 8.2 Top-level fields

| Field | Requirement | Rule |
|---|---|---|
| `name` | Required | Stable discovery name; runtime limit above |
| `description` | Required | State capability and activation conditions |
| `license` | Required | Match package evidence and redistributed bytes |
| `metadata` | Required for Registry extensions | Flat string-to-string map |
| `allowed-tools` | Optional | Array of tool names; no permission grant |
| `compatibility` | Optional | String describing dependencies or constraints |

First-party packages may not invent other top-level fields. Vendored packages
may preserve unknown upstream top-level fields, but may not invent unknown
`mind.*` keys.

### 8.3 Recognized `mind.*` keys

The recognized set is closed:

| Key | Required | Meaning and current projection |
|---|---|---|
| `mind.id` | Yes | Permanent Registry reconciliation key |
| `mind.distribution` | Yes | `marketplace` for this Registry's current release lane |
| `mind.market-primary` | Expected | Primary Marketplace category; approval copies this value |
| `mind.market-categories` | Expected | JSON array string; secondary values remain Registry metadata |
| `mind.marketplace-summary` | Optional | Registry display default; current candidate approval does not copy it |
| `mind.publisher` | Optional | Registry provenance/display default; not copied by current approval |
| `mind.runtime-category` | Optional | Runtime/artifact hint; not a Marketplace category and not currently copied |
| `mind.tags` | Optional | JSON array string; parsed into the candidate projection but not currently copied |
| `mind.min-harness-version` | Optional | Compatibility intent; not currently enforced during sync or runtime load |
| `mind.upstream.repo` | Vendored | Canonical upstream HTTPS repository |
| `mind.upstream.commit` | Vendored | Full 40-character upstream commit SHA |
| `mind.upstream.path` | Vendored | Upstream package path |
| `mind.upstream.import-mode` | Vendored | `exact-snapshot` or `curated-fork` |
| `mind.upstream.license` | Vendored | License at the pinned upstream snapshot |
| `mind.upstream.evidence-urls` | Vendored | JSON array string of immutable evidence URLs |

Do not add `mind.categories`, `mind.attestation.*`, or any other unrecognized
extension. Attestation is a Registry release concern, not frontmatter.

### 8.4 JSON-array string fields

These metadata values are JSON arrays encoded as YAML strings:

- `mind.market-categories`
- `mind.tags`
- `mind.upstream.evidence-urls`

Correct:

```yaml
mind.market-categories: '["business-operations","productivity-tools"]'
```

Incorrect:

```yaml
mind.market-categories: business-operations,productivity-tools
```

Keep all Registry metadata values as strings. The server parser accepts some
native YAML arrays, but the Registry schema and current package convention use
string-encoded JSON arrays.

### 8.5 Third-party template

```yaml
---
name: example-vendored-skill
description: Perform the vendored workflow. Use when the task needs X.
license: Apache-2.0
metadata:
  mind.id: ai.medrix.skill.example-vendored-skill
  mind.distribution: marketplace
  mind.market-primary: knowledge-learning
  mind.market-categories: '["knowledge-learning"]'
  mind.marketplace-summary: A short Marketplace-facing summary.
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/example/project
  mind.upstream.commit: 0123456789abcdef0123456789abcdef01234567
  mind.upstream.path: path/to/skill
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.license: Apache-2.0
  mind.upstream.evidence-urls: '["https://github.com/example/project/blob/0123456789abcdef0123456789abcdef01234567/LICENSE"]'
---
```

The local validator and Mind frontmatter validator do not fully enforce
third-party provenance completeness. The complete field set above is a manual
Registry requirement.

## 9. Marketplace and Runtime Classification

Use only active slugs from `categories.yaml`:

| Slug | Meaning | Legacy aliases not used for new content |
|---|---|---|
| `general` | General | none |
| `development-tools` | Development tools | `code` |
| `content-creation` | Content creation | `writing`, `image`, `slides`, `video`, `web` |
| `data-analysis` | Data analysis | `data` |
| `productivity-tools` | Productivity tools | none |
| `business-operations` | Business operations | none |
| `knowledge-learning` | Knowledge and learning | `learning` |

Classification rules:

1. Choose the primary category by the most natural Marketplace discovery path.
2. Include the primary value in `mind.market-categories`.
3. Add a secondary value only when it materially improves discovery.
4. Never use legacy aliases for new metadata.
5. Validate every category against `categories.yaml`; current local validation
   checks containment but not canonical membership.

`mind.runtime-category` is a separate runtime/artifact hint. Known documented
values are `report`, `ppt`, `html`, `flashcard`, `slides`, `markdown`, and
`video`. Do not use a Marketplace category slug as a runtime category merely
because the words are similar.

Current projection limits are load-bearing:

- candidate approval copies only `mind.market-primary` to the single-value
  `marketplace_category` database column;
- secondary Marketplace categories are not persisted as filterable live data;
- `mind.tags` does not populate the live `tags` column through current approval;
- `skill_search` reads the separate runtime `category` and `tags` fields, not
  Registry secondary categories;
- `mind.runtime-category` does not currently populate that runtime category.

Do not promise live filtering that these fields cannot currently provide.

## 10. Content Quality Contract

Every content change must satisfy these checks.

### Discovery

- `description` states both what the Skill does and when it applies.
- Trigger phrases are specific enough to avoid accidental activation.
- The name and description do not imitate platform identity or claim unavailable
  capabilities.

### Instructions

- Define the required inputs and the expected output.
- Describe prerequisites before the first action that needs them.
- Use an ordered workflow with verifiable intermediate results.
- State error, ambiguity, and safety behavior at the relevant step.
- Keep the main path in `SKILL.md`; move large reference material into bundled
  files only when progressive disclosure improves execution.
- Refer to bundled files with exact relative POSIX paths.
- Do not depend on prior conversation, implicit local state, or undocumented
  credentials.
- Do not instruct an agent to claim completion without checking the output.

### Tools and dependencies

- Use actual Mind tool names and supported capability boundaries.
- Treat tools as optional unless the Skill cannot function without them.
- Describe a fallback or a clear stop condition for unavailable dependencies.
- Do not claim that `allowed-tools` grants shell, network, browser, connector, or
  filesystem access.
- Pin dependency versions when reproducibility or compatibility depends on them.

### Bundled resources

- Every referenced file exists with matching case.
- Every bundled file is required, licensed, and safe to distribute.
- Templates and examples contain no secrets or production data.
- Script output and failure modes match the written instructions.
- Removed references are removed from both instructions and package files.

### Verification

- Exercise the primary workflow with a representative fixture when practical.
- Exercise failure paths for scripts or high-risk instructions.
- Compare actual output with the stated output contract.
- Record any step that cannot be tested and the remaining risk.

## 11. First-Party Creation Playbook

1. Translate the requested outcome into activation conditions, inputs, outputs,
   required tools, constraints, and verification criteria.
2. Search for overlapping Registry packages by name, description, tags, and
   purpose. Update an existing package when it already owns the capability.
3. Select a new slug, `name`, and `mind.id`; run collision checks.
4. Select canonical Marketplace categories.
5. Create only the package files required by the workflow.
6. Write the frontmatter using the first-party contract. Do not add upstream
   fields.
7. Write self-contained instructions and exact resource references.
8. Review scripts, network behavior, data access, dependencies, and destructive
   actions.
9. Run package-specific checks and the complete Registry validation sequence.
10. Inspect the final diff and prepare the required handoff.

Use the package's actual license. A root repository license does not
automatically establish the package license.

## 12. Third-Party Intake Playbook

Third-party content is vendored into this repository. Mind production sync
fetches only the Registry commit; it never fetches `mind.upstream.repo` during
runtime sync.

### 12.1 Establish the immutable source

1. Select a full 40-character upstream commit SHA, never a moving branch or tag
   name alone.
2. Verify the checked-out upstream `HEAD` equals that SHA.
3. Record the canonical repository URL and package path at that commit.
4. Inspect license, notice, ownership, and redistribution evidence at the same
   commit.
5. Inspect source and scripts statically before any execution. Unknown upstream
   code is not executed as part of intake.

A safe temporary checkout pattern is:

```bash
tmpdir="$(mktemp -d)"
git init "$tmpdir/upstream"
git -C "$tmpdir/upstream" remote add origin <https-upstream-repo>
git -C "$tmpdir/upstream" fetch --depth 1 origin <40-hex-sha>
git -C "$tmpdir/upstream" checkout --detach FETCH_HEAD
git -C "$tmpdir/upstream" rev-parse HEAD
```

Remove the temporary checkout after comparison and intake evidence are complete.

### 12.2 Choose the import mode

- `exact-snapshot`: preserve upstream behavior and resource bytes. Registry
  frontmatter extensions and required license wrappers may be added without
  converting the behavioral content into a curated fork.
- `curated-fork`: behavior or resources differ from upstream. Record each
  material change and its reason in `MODIFICATIONS.md`.

Never label behaviorally modified content as `exact-snapshot`.

### 12.3 Copy the complete resource closure

- Copy `SKILL.md` plus every relative resource needed by its instructions.
- Preserve paths when behavior depends on them.
- Remove references to upstream-only files only when the corresponding
  instruction is intentionally changed and recorded.
- Copy required `LICENSE`, `NOTICE`, and attribution content.
- Do not copy `.git`, submodules, symlinks, LFS pointers, dependency trees,
  caches, or build output.

### 12.4 Record provenance

- Fill every `mind.upstream.*` field.
- Use immutable evidence URLs containing the pinned SHA when possible.
- Make top-level `license`, `mind.upstream.license`, package license files, and
  evidence consistent.
- Preserve unknown upstream top-level fields only when they belong to the
  vendored format and remain necessary.
- Do not add unknown `mind.*` fields.

### 12.5 Compare and review

- Compare vendored bytes against the pinned upstream snapshot.
- Explain every difference outside Registry metadata and license wrappers.
- Inspect instruction overrides, network endpoints, credential access,
  subprocesses, file writes, package installation, and data transfer.
- Apply every review class in `policies/review-policy.yaml`.

Third-party addition and re-vendoring require `skill-curation` plus recorded
legal approval. Script, network, or capability changes also require
`product-security`.

## 13. Update and Re-Vendor Playbooks

### 13.1 First-party content update

1. Preserve `mind.id`.
2. Confirm the requested behavior delta and affected workflows.
3. Update instructions and the complete resource closure together.
4. Remove only files made obsolete by this change.
5. If the update removes all bundled files, stop before release: the current
   approval path treats a `nil` file snapshot as “preserve existing files,” so
   old live files can remain. Include a `mind-api` fix or a separately verified
   full content-replacement path in the release plan.
6. Run targeted checks for changed executable content.
7. State that approval updates the shared row for existing subscriptions.

### 13.2 Re-vendor to a new upstream commit

1. Preserve Registry slug, `name`, and `mind.id` unless a separately approved
   rename plan exists.
2. Verify the old and new upstream SHAs and compare the entire upstream package.
3. Review upstream license and notice changes before copying content.
4. Replace all changed vendored bytes, not only `SKILL.md`.
5. Add and remove resources to match the new pinned snapshot.
6. Update commit, path, import mode, license, evidence URLs, notices, and
   `MODIFICATIONS.md` together.
7. Re-run static risk review even when the upstream changelog appears benign.
8. Run targeted tests for changed scripts and the full Registry checks.

If only provenance metadata changes and content bytes remain identical, Mind
can report `skipped`; this is expected because production drift detection does
not hash most frontmatter metadata.

## 14. Move and Rename Playbook

### Directory move with unchanged live name

1. Preserve `mind.id` and `name`.
2. Use a Git move so history remains understandable.
3. Update internal paths and Registry references.
4. Validate the destination has no slug or case-insensitive path collision.
5. Expect content to be skipped when bytes are unchanged; source provenance path
   can still backfill during sync.

### Live name rename

Preserve `mind.id`. Never create a replacement identity merely to rename the
display or discovery name.

Current review-path limitations:

- drift detection does not hash `name`;
- the pending snapshot does not carry `name`;
- candidate approval preserves the existing live `name`.

Therefore a Registry-only name edit does not guarantee a live rename. A complete
rename plan must include a supported WebAdmin catalog update or a `mind-api`
change, collision checks, content-preservation checks, subscription verification,
and rollback. Do not claim a live rename after Registry sync alone.

## 15. Metadata and Reclassification Playbook

Production drift detection currently hashes only:

```text
description + instructions + sorted bundled file paths and contents
```

It excludes `name`, license, categories, tags, summary, publisher,
distribution, minimum harness version, and most provenance metadata.

Consequences:

- a pure primary-category change normally produces no pending candidate;
- a primary category is copied only when another real content change produces a
  candidate and that candidate is approved;
- secondary categories, tags, publisher, runtime category, and minimum harness
  version are not fully applied by current candidate approval;
- Marketplace summary, showcase media, featured/recommended state, sort weight,
  and listing state are operational WebAdmin fields.

For a pure live reclassification:

1. Update Registry metadata to preserve desired Git intent.
2. Apply the live primary category through WebAdmin only when explicitly in
   scope, or implement the missing projection in `mind-api` when that is the
   requested outcome.
3. Verify Marketplace category filtering after the live update.
4. Do not add a no-op content change to manufacture drift.

For display-only changes, use WebAdmin and do not rewrite Skill content. For
tags or runtime-category behavior, state the current projection gap explicitly.

## 16. Removal and Withdrawal Playbook

Deleting a Registry directory does not delete, disable, reject, or unlist the
existing database row. The scanner has no deletion reconciliation.

First determine the intended live effect:

| Intended effect | Required action |
|---|---|
| Stop new Marketplace discovery | Set the live row to unlisted |
| Preserve current subscriptions | Unlisting is compatible with this intent |
| Block current runtime access | Requires a separate disable, revocation, or deletion plan |
| Remove Registry source bytes | Delete package only after the live lifecycle action |

Unlisting removes Marketplace discovery, but runtime loading for an existing
active subscription does not currently check listing or review status. Do not
describe unlisting as a full runtime kill switch.

Safe sequence:

1. Record current Registry commit, live Skill ID, `mind.id`, version, listing,
   and subscription impact.
2. Apply the required live withdrawal action in WebAdmin when explicitly
   authorized.
3. Verify the intended discovery and runtime behavior.
4. Remove the Registry package in a reviewed PR.
5. Mark the `mind.id` as retired in release records; never reuse it.
6. Record the recovery path.

If WebAdmin action is outside the task, prepare the Git change only when its
ordering is explicitly accepted, and make the required live action a blocking
handoff item.

Restoring a removed Skill requires restoring the package in a new Registry
commit before sync. Syncing a historical commit where the package is absent
cannot create a rollback candidate for that package.

## 17. Batch Maintenance Controls

Before a batch edit, build a package matrix containing:

- slug;
- `name`;
- `mind.id`;
- first-party or third-party mode;
- old and new upstream SHA when applicable;
- content, script, license, category, and identity changes;
- required review classes;
- expected candidate result;
- targeted test command.

Batch rules:

- Never regenerate or reformat unrelated vendored content.
- Preserve every stable identity independently.
- Review licenses and provenance per package, not by repository-level inference.
- Group changes by risk and provenance when practical.
- Validate the whole Registry after package-level checks.
- After sync, reconcile candidate names, count, commit SHA, and failures against
  the matrix.
- Do not bulk-approve an unexpected candidate set.
- A `partial` or `failed` source status is not release-ready; a disabled source
  row must be enabled before syncing.

Repeated sync of the same Registry commit may refresh an existing pending row.
It does not justify skipping candidate review.

## 18. Bundled Files, Size, and Portability

Official sync accepts regular text and binary files. Binary bytes are stored as
base64 in the database and restored when materialized. `read_skill` does not
return binary files as text, so instructions must not depend on reading a binary
asset through that tool.

Repository-wide source-sync blockers:

- any symlink;
- `.gitmodules` or a submodule;
- a Git LFS pointer;
- a non-regular file;
- path escape from the clone root.

Package path rules:

- use forward-slash relative paths;
- use canonical paths with no `.` or `..` segments;
- avoid absolute paths, Windows drive prefixes, control characters, and trailing
  slashes;
- avoid case-insensitive collisions;
- reserve root `SKILL.md` for instructions;
- keep paths at or below 1024 bytes and 32 components.

Stay within the direct Skill API compatibility budgets even though current
Registry sync does not enforce every limit consistently:

- instruction body: 5 MiB;
- one bundled file: 10 MiB;
- bundled files: 500 maximum;
- total bundled bytes: 100 MiB.

Smaller focused packages are preferred. Do not use the Registry as a general
artifact store.

## 19. Scripts, Network Behavior, and Security

Scripts are permitted bundled files. They do not grant shell permission.
Execution still depends on the Agent tool set and sandbox environment.

The local validator reports only a partial extension set as `INFO`. The runtime
classifies these extensions as scripts:

```text
.py .sh .bash .js .ts .rb .pl .php
```

The local validator additionally reports `.bat`, `.ps1`, `.exe`, and `.cmd`.
Review the union plus executable file modes:

```bash
find skills/<slug> -type f -perm -111 -print
find skills/<slug> -type f | rg '\.(py|sh|bash|js|ts|rb|pl|php|bat|ps1|cmd|exe)$'
```

For every executable or capability change, inspect:

- network destinations, protocols, redirects, and transmitted data;
- environment variables, credentials, cookies, browser profiles, keychains, and
  local configuration;
- subprocesses, interpreters, package installation, and downloaded code;
- filesystem reads, writes, deletion, path traversal, and permission changes;
- background processes, persistence, scheduling, and resource exhaustion;
- prompt or instruction overrides that bypass task or platform constraints;
- collection or transfer of private, tenant, or production data;
- destructive behavior and whether confirmation is required;
- declared tool and compatibility requirements versus actual behavior.

This is a public repository. Never commit secrets, tokens, cookies, private
keys, internal credentials, production data, private endpoints, or confidential
configuration.

Current CI does not provide secret scanning, static capability analysis, SBOM,
deterministic archive comparison, provenance attestation, or license approval.
Manual risk review remains required.

## 20. License and Review Policy

Apply all matching classes from `policies/review-policy.yaml`:

| Change class | Required approval |
|---|---|
| First-party content | `skill-curation` |
| Third-party addition or re-vendoring | `skill-curation` and recorded legal approval |
| License field/file change | `skill-platform-maintainers` and recorded legal approval |
| Script, network, or capability change | `product-security` |
| Schema, policy, CI, or release workflow | `skill-platform-maintainers` |

When multiple rows apply, all apply. A policy change cannot weaken the policy
that governs the same change.

Validation success is not license approval. Pause on `NOASSERTION`, custom
terms, unclear ownership, copyleft obligations, commercial restrictions,
missing notices, or inconsistent evidence.

The Registry root license covers Registry tooling and schema. Each package must
carry its own correct license record.

## 21. Validation: Necessary but Not Sufficient

Current CI runs only:

```bash
python3 scripts/validate_skills.py
```

`tests/test_validate.py` is a local self-test for the validator and currently
has a small fixture set. `schemas/skill.schema.json` is not executed by current
CI.

### 21.1 Gate matrix

| Check | Local validator | Mind sync/runtime | Required manual control |
|---|---|---|---|
| Required `name`, `description`, `license` | Yes | Yes | Confirm quality and byte limits |
| Closed `mind.*` key set | Yes | Yes | None when both pass |
| `mind.id` / distribution present | Yes | Yes | Confirm format, uniqueness, and lifecycle |
| Primary contained in category array | Partial; only when both fields exist | Yes when primary exists | Confirm presence and canonical slug membership |
| `mind.tags` JSON syntax | No | Yes | Validate locally before handoff |
| Evidence URL JSON syntax | No | Yes | Validate locally before handoff |
| First-party unknown top-level fields | No | Rejected by Mind sync | Inspect mode and top-level keys |
| Complete third-party provenance | No | Not fully enforced | Verify every upstream field and evidence |
| Duplicate slug/name/`mind.id` | No | Can reconcile incorrectly or conflict | Registry-wide collision scan |
| Unsafe symlink/submodule/LFS content | No | Official source sync rejects | Repository-wide scan |
| Script capability risk | Partial `INFO` only | Script classification only | Static and targeted review |
| Secret/license approval | No | No | Required review and evidence |
| Metadata-only drift | No candidate prediction | Usually `skipped` | Plan separate live action |
| Content size/portable paths | Incomplete | Inconsistent across sync and direct APIs | Apply compatibility budgets |

The Registry validator prints an informational package digest. Mind sync
computes a different canonical digest stream containing separators and file
mode data. Never compare the two digest values for equality. Each value is
useful only inside its own implementation.

### 21.2 Required local checks

Run for every Registry change:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_skills.py
PYTHONDONTWRITEBYTECODE=1 python3 tests/test_validate.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_skill_catalog.py --check
git diff --check
git status --short
```

Install PyYAML only if missing:

```bash
python3 -m pip install pyyaml
```

Also run:

```bash
git diff --name-status
git diff --stat
git diff -- skills/<affected-slug>
find . -name __pycache__ -type d -print
find . -type l -print
find . -name .gitmodules -o -name .gitattributes
```

Inspect `.gitattributes` results for LFS filters and inspect suspected files for
the Git LFS pointer header. Remove generated `__pycache__` directories created
by local checks.

For multiple packages, inspect every package explicitly. For executable
changes, run narrow package tests or a safe fixture-based invocation. Do not
execute unreviewed third-party scripts merely to satisfy a test checkbox.

Before handoff, verify:

- YAML examples and changed frontmatter parse;
- every relative reference resolves with exact case;
- no duplicate slug, name, or `mind.id` was introduced;
- all categories exist in `categories.yaml`;
- every third-party field matches the pinned snapshot;
- `skill-catalog.html` contains the current Marketplace package set;
- the diff contains no unrelated or generated file;
- no `__pycache__` remains.

## 22. Git, Commit, and PR Rules

- Keep the diff limited to the requested package and directly required policy or
  documentation changes.
- Do not clean up adjacent packages.
- Preserve vendored formatting unless the task requires a content change.
- Use explicit file staging; never use `git add .` in a dirty checkout.
- Keep one logical change per commit when practical.
- Do not force-push, rewrite shared history, or merge without explicit authority.
- Record the full merged Registry commit SHA for release.

The PR description must include:

- affected slugs and operation type;
- stable `mind.id` values;
- behavior delta and subscription impact;
- first-party or third-party classification;
- upstream repo, SHA, path, import mode, license, and evidence when applicable;
- category decision;
- script, network, binary, dependency, and data-risk notes;
- local validation and targeted test results;
- all required approval classes and evidence;
- expected WebAdmin candidate set;
- release and rollback steps.

Do not describe a merged PR as published.

## 23. WebAdmin Release State Machine

Run WebAdmin actions only when explicitly included in the task.

### 23.1 Source configuration

WebAdmin entry: `https://admin.mind.medrixai.com`.

The `Skills -> 来源同步` entry for this Registry should use:

```text
name: official-registry
source_type: github_repo
repo_url: https://github.com/MedrixAI/mind-skill-registry
branch: main
trust_profile: official_registry
target_scope: builtin
auto_update: review
enabled: true
```

WebAdmin provides `添加 Official Registry 来源` to prefill these values. Do not
change the source to `auto`, remove the official trust profile, add credentials,
or point it at an unreviewed repository.

Official sync uses HTTPS and an allowed host, resolves the configured ref to a
full Registry commit SHA, fetches that SHA in a clean Git environment, verifies
`HEAD`, rejects unsafe worktree content, and then scans packages.

### 23.2 Pre-sync release evidence

Record:

- merged Registry commit SHA;
- affected slug and `mind.id` set;
- expected new, changed, skipped, and absent candidates;
- previous live Skill IDs and versions for updates;
- previous Registry commit for rollback;
- display settings that must remain unchanged.

### 23.3 Sync

1. Open `Skills -> 来源同步`.
2. Confirm the exact `official-registry` configuration.
3. Trigger `同步`.
4. Require `last_sync_status=ok`.
5. Stop on `partial` or `failed`; inspect `last_sync_error` and the
   failed package set.

Sync does not publish. Under `auto_update=review`:

- a new Registry identity creates a minimal disabled, unlisted pending anchor
  plus a pending content snapshot;
- a content-changed existing identity creates or refreshes a pending snapshot;
- unchanged content is skipped;
- package deletion creates no removal candidate.

### 23.4 Candidate review and approval

1. Open `Skills -> 更新队列`.
2. Match candidate count and names to release evidence.
3. Match candidate `Commit SHA` to the merged Registry commit.
4. Review description, instructions, every bundled file, diff summary,
   provenance, primary category, and risk notes.
5. Reject or stop on unexpected content or identity.
6. Use `批准` only after the complete candidate is verified.

Candidate approval is a transactional compare-and-swap. It copies
description, instructions, bundled files, Registry commit provenance, and the
primary Marketplace category; bumps the live version; and sets approved,
listed, and enabled. A concurrent version conflict requires re-sync and fresh
review.

### 23.5 Operational display settings

After approval, use `Skills -> 目录` for live operational fields:

- Marketplace summary;
- showcase media and cover order;
- featured and recommended state;
- sort weight;
- primary live category when a metadata-only reclassification is required;
- listed/unlisted state.

Do not replace Git-owned instructions or bundled content with a divergent
WebAdmin copy. A WebAdmin catalog update sends a full content payload and stamps
the row as admin-managed, so verify current content before any display-field
update.

### 23.6 Production verification

Verify all applicable paths:

1. Marketplace discovery by exact name and primary category.
2. Marketplace detail, summary, and showcase media.
3. Subscription from a clean test tenant.
4. `skill_search` visibility after subscription.
5. `read_skill` instructions and text bundled files.
6. Primary workflow in a safe environment.
7. Existing subscription behavior for an approved update.
8. Absence from new discovery after unlisting.

Do not report `published` until approval and production verification both
complete.

## 24. Rollback and Incident Handling

Choose rollback by current state:

### Before approval

- Reject the candidate. The live Skill remains unchanged.
- Fix Registry content in a new commit, merge, and sync again.

### After approval

1. Identify the last known-good Registry commit containing the package.
2. In `Skills -> 更新队列`, use `回滚` with that full 40-character Registry
   commit SHA.
3. Review the newly generated pending snapshot.
4. Approve the rollback candidate.
5. Restore any separately changed WebAdmin display settings.
6. Repeat production verification.

Rollback never auto-approves. It re-syncs a historical Registry commit and
creates a new pending snapshot.

A normal Git revert merged to `main` can also produce a corrective pending
candidate. Do not force-push Registry history.

For urgent discovery removal, unlist the Skill. Remember that unlisting alone
does not block active subscriptions from runtime loading. A full runtime
withdrawal requires a separate disable, revocation, or deletion response.

## 25. Common Failure Modes

| Symptom | Likely cause | Correct response |
|---|---|---|
| Local validator passes, sync rejects | Stricter server frontmatter or unsafe-worktree check | Read sync error; fix the package or repository blocker |
| Sync reports `skipped` after category/tag edit | Metadata excluded from content hash | Use the metadata playbook; do not add no-op content |
| Registry `name` changed but live name did not | Name absent from drift hash and pending snapshot | Use the separate rename plan |
| Final bundled file was removed but remains live | A `nil` candidate file snapshot preserves existing live files | Stop release; fix approval semantics or use a verified full replacement path |
| Secondary category or tag is absent live | Current approval does not persist it | Record projection limitation or implement runtime support |
| Candidate SHA differs from release SHA | Wrong source ref or newer Registry main | Stop; reconcile source and release evidence |
| Unexpected candidate appears | Earlier pending drift or additional main changes | Review individually; do not bulk-approve |
| Source status is `partial` | At least one package failed while others scanned | Resolve the complete failure set before release |
| Source is disabled in WebAdmin | The source row is not enabled | Enable the intended official source before syncing |
| Sync fails for unrelated package | Repository-wide symlink, submodule, or LFS blocker | Remove the blocker in a reviewed Registry change |
| Git package deletion has no candidate | No deletion reconciliation exists | Apply the removal playbook |
| Unlisted Skill still runs for an existing subscription | Runtime access ignores listing/review status | Use the stronger withdrawal plan |
| Binary asset cannot be read through `read_skill` | Binary entries are base64 and text reads reject them | Materialize through a supported execution path |
| Approval returns a version conflict | Live version changed after candidate creation | Re-sync and review a fresh candidate |

## 26. Interactive and Cross-Repository Catalog Maintenance

The standalone combined catalog is maintained in this repository at:

```text
skill-catalog.html
```

It embeds both release lanes so it works when opened directly without a server:

- Marketplace entries come from the current Registry working tree;
- Builtin entries are a snapshot of
  `mind-api/knowledge/skills/preloaded/`;
- Marketplace and Builtin categories remain separate because they have
  different runtime meanings;
- source links point to the corresponding Registry, `mind-api`, or pinned
  third-party GitHub file.

Every package add, update, re-vendor, move, rename, reclassification, removal,
or batch operation must update `skill-catalog.html` in the same change. This
includes description, summary, category, publisher, tag, provenance, and source
changes. Do not hand-edit the embedded JSON block.

After changing any Registry Skill, regenerate Marketplace data and preserve the
existing Builtin snapshot:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_skill_catalog.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_skill_catalog.py --check
```

When the Builtin lane changed or a fresh `mind-api` checkout is available,
refresh both lanes by supplying its repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_skill_catalog.py \
  --mind-api-root /path/to/mind-api
PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_skill_catalog.py --check
```

The generator always rebuilds Marketplace entries from `skills/*/SKILL.md`.
Without `--mind-api-root`, it intentionally preserves the embedded Builtin
snapshot so Registry-only maintenance does not depend on a second checkout.
After generation, verify the displayed totals, type tabs, categories, search,
source filters, source links, empty state, and mobile layout. A stale or missing
catalog is a blocking validation failure, not an optional documentation
follow-up.

The audit-oriented Markdown inventory remains in the `mind-api` repository at:

```text
docs/skill-catalog.md
```

When a Registry change adds, removes, renames, or reclassifies a package, update
that catalog when cross-repository edits are explicitly in scope. Otherwise
record the exact required catalog delta in the handoff. Do not claim the catalog
is current without checking it.

## 27. Definition of Done

A Registry change is ready for handoff only when:

1. The operation type and authority boundary are explicit.
2. The package is self-contained and every reference resolves.
3. Stable identity and collision checks pass.
4. Categories, distribution, license, and provenance are correct.
5. Scripts, network behavior, dependencies, and data risk have been reviewed.
6. Package-specific verification and all required local checks pass.
7. The final diff contains only intended files and no generated artifacts.
8. Required approval classes are identified.
9. Expected WebAdmin candidates and metadata projection limits are recorded.
10. The interactive catalog is regenerated and its filters and links are
    verified.
11. Production verification and rollback steps are concrete.

For an authorized full release, definition of done additionally requires an
`ok` source sync, exact candidate reconciliation, candidate approval,
operational display verification, and production workflow verification.

## 28. Required Handoff Format

End every Registry task with:

```text
Affected skills: <slugs>
Operation: add | update | re-vendor | move | rename | reclassify | remove | batch
Identity: <name -> mind.id; preserved/new/retired>
Content delta: <instructions/resources/scripts>
Provenance: <first-party or upstream repo/SHA/path/import mode>
Classification: <primary and secondary categories>
Risk: <scripts/network/data/dependencies/license>
Validation: <validator/self-test/targeted checks/diff check>
Git state: <branch and full commit SHA when committed>
Approval required: <curation/legal/security/platform>
Expected candidates: <new/updated/skipped count and names>
Projection limits: <metadata not applied automatically>
WebAdmin next step: <none/sync/approve/display update/unlist/withdraw>
Catalog follow-up: <updated or exact required delta>
Rollback: <Registry commit and live action>
Unverified: <remaining checks or none>
```

Never report `committed`, `pushed`, `merged`, `synced`, `approved`, `unlisted`,
`withdrawn`, or `published` unless that exact state transition completed and was
verified.
