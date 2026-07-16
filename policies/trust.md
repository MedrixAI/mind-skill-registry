# Trust Policy

The official Mind Skill Registry (`MedrixAI/mind-skill-registry`) is a
**trusted first-party source**. It is MedrixAI's protected public Git repository
whose content is CI-gated and reviewed before merge, including vendored
third-party skills (which are reviewed + LICENSE/NOTICE/MODIFICATIONS-annotated
before they land).

## Phase A scope

- Registry content is **script-free text** in Phase A. No executables
  (`.sh`, `.py`, `.bat`, `.ps1`, `.exe`, `.cmd`) are permitted anywhere under
  `skills/`; CI fails closed on any such file.
- The full §6.7 gate suite (deterministic archive build twice, SBOM, provenance
  attestation, secret scanning, static capability analysis) is **deferred to
  Phase B**. Phase A CI runs frontmatter validation, executable rejection, and
  content-digest computation only.
- The **publisher-repo worker** lane (untrusted external Git, dedicated
  non-root intake worker with mTLS, no business secrets) is deferred (spec
  §4.2/§7.4). Phase A ships only the first-party Registry lane.

## Two-commit boundary

Two commits are recorded separately and never conflated:

- The **Registry commit** (this repo) is Mind's version axis
  (`upstream_ref.commit`). mind-api syncs from it, verifies the digest against
  it, and rolls back to it.
- The **upstream source commit** (`mind.upstream.commit` frontmatter) is
  consumed only by Registry CI for drift detection; mind-api runtime never
  fetches the third-party origin.

## Reference

Design spec: `mind-api` repo
`docs/superpowers/specs/2026-07-14-official-skill-registry-marketplace-design.md`
§4.2 (trust boundaries), §6.7 (CI gates), §7.4 (deferred items).
