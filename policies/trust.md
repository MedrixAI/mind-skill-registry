# Trust Policy

The official Mind Skill Registry (`MedrixAI/mind-skill-registry`) is a
**trusted first-party source**. It is MedrixAI's protected public Git repository
whose content is CI-gated and reviewed before merge, including vendored
third-party skills (which are reviewed + LICENSE/NOTICE/MODIFICATIONS-annotated
before they land).

## Phase A scope

- Registry packages may contain scripts and other executable-capable bundled
  files. The validator reports them as `INFO`; it does not grant execution
  permission or security approval. Changes to scripts, network behavior, or
  capability declarations require the product-security review defined in
  `policies/review-policy.yaml`.
- The full §6.7 gate suite (deterministic archive build twice, SBOM, provenance
  attestation, secret scanning, static capability analysis) is **deferred to
  Phase B**. Current CI runs frontmatter validation and content-digest
  computation; risk-based manual review remains required.
- The **publisher-repo worker** lane (untrusted external Git, dedicated
  non-root intake worker with mTLS, no business secrets) is deferred (spec
  §4.2/§7.4). Phase A ships only the first-party Registry lane.

## Two-commit boundary

Two commits are recorded separately and never conflated:

- The **Registry commit** (this repo) is Mind's version axis
  (`upstream_ref.commit`). mind-api SHA-pins it, computes the package digest,
  stages a review candidate, and can re-sync a historical commit for rollback.
- The **upstream source commit** (`mind.upstream.commit` frontmatter) records
  the exact third-party snapshot used for provenance and review. Current CI
  validates the metadata but does not re-fetch that origin; mind-api runtime
  never fetches the third-party origin.

## Reference

Design spec: `mind-api` repo
`docs/superpowers/specs/2026-07-14-official-skill-registry-marketplace-design.md`
§4.2 (trust boundaries), §6.7 (CI gates), §7.4 (deferred items).
