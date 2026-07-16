---
name: vendor-compare
description: Compare vendors or suppliers side-by-side across weighted criteria and produce a defensible recommendation. Use when a user needs to evaluate two or more vendors for a purchase, renewal, or consolidation decision.
license: Apache-2.0
compatibility: Requires Mind Agent Harness 1.0 or later. No network access or external packages required.
metadata:
  mind.id: "ai.medrix.skill.vendor-compare"
  mind.distribution: "marketplace"
  mind.market-primary: "data-analysis"
  mind.market-categories: '["data-analysis","productivity-tools"]'
  mind.marketplace-summary: "Side-by-side vendor comparison with a weighted recommendation."
  mind.publisher: "medrixai"
  mind.runtime-category: "report"
  mind.tags: '["vendor","comparison","procurement"]'
  mind.min-harness-version: ">=1.0.0"
---

# vendor-compare

Produce a defensible vendor comparison from the criteria, weights, and evidence the user provides. The output is a single Markdown report a decision-maker can read and act on in one sitting.

## When to use

Invoke this skill when the user asks to:
- Evaluate two or more vendors for a purchase or renewal.
- Consolidate redundant tools and pick the survivor.
- Build a comparison matrix for a stakeholder review.

Do not use it for single-vendor deep reviews or for pure feature documentation.

## Inputs

Collect (or ask for) each of these. Mark any that are missing as `unknown` in the output; do not fabricate vendor attributes.

1. **Vendors** — the two or more vendors being compared (names and the specific product/tier).
2. **Criteria** — the dimensions that matter (e.g. price, support SLA, security posture, integration coverage, scalability).
3. **Weights** — the relative importance of each criterion. Accept either explicit percentages or a ranked list; convert ranks to percentages and show the conversion.
4. **Evidence** — per-vendor, per-criterion data points. Accept the user's pasted specs, vendor RFP responses, or notes; cite each datum.
5. **Decision rule** — how the recommendation is made (highest weighted score; or highest score within a hard requirement gate). Default: weighted score with hard-requirement gates applied first.
6. **Constraints** — any hard requirements a vendor must meet to be eligible (e.g. SOC 2 Type II, data residency).

## Method

1. Normalize each criterion to a 0–5 score per vendor (0 = absent, 5 = best-in-class). Show the rubric you applied for each criterion so scores are auditable.
2. Apply hard-requirement gates: any vendor failing a constraint is marked ineligible and excluded from the weighted total (but kept in the table for transparency).
3. Compute weighted score = Σ (score × weight) for each eligible vendor.
4. Rank eligible vendors by weighted score. The top-ranked vendor is the provisional recommendation.
5. Record the single strongest reason to pick the leader and the single strongest reason to pick the runner-up. If the gap is < 10% of the max possible score, flag the decision as marginal and list the tiebreaker criteria the user should weigh manually.

## Output format

Emit one Markdown document with exactly these sections:

1. **Title** — `Vendor comparison: <decision context>`.
2. **Decision context** — one paragraph: what is being decided and the deadline.
3. **Criteria & weights** — a table: criterion | weight % | why it matters | scoring rubric (0–5).
4. **Hard requirements** — bullet list; mark each vendor as PASS/FAIL.
5. **Scored matrix** — a table: criterion (rows) × vendors (columns), cells = 0–5 score + one-line evidence citation.
6. **Weighted totals** — a table: vendor | weighted score | rank | eligible?.
7. **Recommendation** — the provisional pick, the strongest reason for it, the strongest reason for the runner-up, and (if marginal) the tiebreaker list.
8. **Assumptions & gaps** — bullet list of any `unknown` cells, assumed scores, or missing evidence.

Keep the report under ~700 words. If it would exceed that, move the evidence citations to an appendix table and keep the main report to the eight sections above.

## Worked example

Decision context: "Pick a log-shipper between Vendor A and Vendor B for a 90-day renewal."

Scored matrix (fragment):

| Criterion (weight) | Vendor A | Vendor B |
|---|---|---|
| Price (30%) | 4 — $2.4k/mo, fits budget | 3 — $3.1k/mo, at budget ceiling |
| Support SLA (20%) | 5 — 15-min P1 | 3 — 1-hr P1 |
| SOC 2 (hard req.) | PASS | PASS |

Weighted totals:

| Vendor | Weighted score | Rank | Eligible |
|---|---|---|---|
| Vendor A | 4.2 | 1 | yes |
| Vendor B | 3.1 | 2 | yes |

Recommendation: Vendor A. Strongest reason: materially better support SLA at lower price. Runner-up strength: Vendor B has richer pre-built integrations. Gap > 10%, decision is not marginal.

## Rules

- Never invent vendor attributes; an `unknown` cell is always preferable to a fabricated score.
- Cite the source of each scored datum (user paste, vendor doc, URL). If unsourced, mark `[uncited]`.
- Hard-requirement failures are absolute; do not allow a failing vendor to win on weighted score.
- Keep the recommendation provisional; the human decision-maker owns the final call.
