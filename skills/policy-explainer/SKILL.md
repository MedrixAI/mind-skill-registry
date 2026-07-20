---
name: policy-explainer
description: Explain a policy or document in plain language, covering scope, obligations, exceptions, and examples. Use when a user needs to understand, summarize, or communicate what a policy requires of them or their team.
license: Apache-2.0
compatibility: Requires Mind Agent Harness 1.0 or later. No network access or external packages required.
metadata:
  mind.id: "ai.medrix.skill.policy-explainer"
  mind.distribution: "marketplace"
  mind.market-primary: "business-operations"
  mind.market-categories: '["business-operations","knowledge-learning"]'
  mind.marketplace-summary: "Plain-language explanations of policies and compliance documents."
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Explain a policy or document in plain language, covering scope, obligations, exceptions, and examples. Use when a user needs to understand, summarize, or communicate what a policy requires of them or their team.","starter_prompts":["Explain the policy I provide in plain language, highlighting who it applies to, required actions, deadlines, exceptions, and practical examples.","Compare the two policy versions I provide and summarize the material changes, affected teams, and actions we need to take.","Turn the compliance document I provide into a concise employee FAQ with clear guidance on what to do and what to avoid."]},"zh-CN":{"description":"用通俗语言解释政策或文档，涵盖适用范围、义务、例外和示例。适用于用户需要理解、总结或传达某项政策对个人或团队的要求。","starter_prompts":["请用通俗语言解释我提供的政策，重点说明适用对象、必须采取的行动、截止时间、例外情况和实际示例。","请比较我提供的两个政策版本，总结重要变化、受影响的团队以及我们需要采取的行动。","请把我提供的合规文档整理成简明的员工常见问题，明确说明应该做什么和不应该做什么。"]}}}'
  mind.publisher: "medrixai"
  mind.runtime-category: "markdown"
  mind.tags: '["policy","compliance","writing"]'
  mind.min-harness-version: ">=1.0.0"
---

# policy-explainer

Turn a dense policy, regulation, or compliance document into a plain-language explanation a non-specialist can act on. The output is a single Markdown document that preserves fidelity to the source while making obligations and exceptions unambiguous.

## When to use

Invoke this skill when the user asks to:
- Explain what a policy requires of them or their team.
- Summarize a regulation or internal policy for a stakeholder email.
- Onboard a team to a new compliance requirement.
- Translate a legalistic clause into operational guidance.

Do not use it to draft new policy, nor to give binding legal advice — always note that interpretation is informational and the authoritative source is the policy text itself.

## Inputs

Collect (or ask for) each of these:

1. **Source document** — the policy text, clause, or regulation (pasted or referenced). Quote, do not paraphrase, when a binding clause is at issue.
2. **Audience** — who the explanation is for (engineers, managers, all staff, a specific team).
3. **Scope of interest** — what the user cares about (their obligations, their team's obligations, exceptions they may qualify for, deadlines).
4. **Jurisdiction or org context** — the entity the policy applies to, if not obvious from the source.
5. **Known edge cases** — any scenarios the user already suspects are ambiguous.

## Explanation structure

Emit one Markdown document with exactly these sections:

1. **Title** — `Plain-language explanation: <policy name or short ref>`.
2. **At a glance** — 2–3 sentences: what the policy is, who it binds, and the one obligation most readers must walk away knowing.
3. **Scope** — who and what is covered, and explicitly what is not covered. Bullet list.
4. **Key obligations** — a table: obligation | who it applies to | when | how to comply. Each obligation is one row, phrased as an action the reader can take or must take.
5. **Exceptions & exemptions** — bullet list. For each exception: who qualifies, what it relieves, and how to claim it.
6. **Deadlines & cadence** — a table: milestone | date or cadence | owner.
7. **Definitions** — glossary of any term the audience may not know, defined from the source text (cite the source clause).
8. **Example scenarios** — 2–3 short worked scenarios showing how the obligations apply in practice and how an exception changes the outcome. Each scenario ends with the resulting obligation or relief.
9. **Open questions** — bullet list of ambiguities the source text leaves unresolved, each flagged for human/legal follow-up.
10. **Source references** — a list of clause numbers or section anchors used, so the reader can verify against the original.

Keep the document under ~800 words. If it would exceed that, move full clause quotes into footnotes and keep the ten sections above concise.

## Worked example

Source (abbreviated): "All production deployments must be approved by a change advisory board (CAB) meeting no less than 48 hours before the deployment window, except for emergency changes which require verbal approval from the on-call director and a retroactive CAB filing within one business day."

At a glance: Every production deployment needs CAB approval 48 hours ahead, unless it is an emergency, in which case the on-call director approves verbally and CAB is filed within one business day.

Key obligations (fragment):

| Obligation | Applies to | When | How to comply |
|---|---|---|---|
| Obtain CAB approval | Release engineer | Before any prod deployment | Submit change request to CAB ≥ 48h before window |
| File retroactive CAB | Release engineer | After an emergency change | Submit CAB filing within 1 business day |

Exceptions & exemptions:
- Emergency changes: qualify if production is degraded or about to degrade. Relieves the 48-hour lead time. Claim by obtaining on-call director verbal approval and filing retroactively.

Example scenario:
> Scenario: A hotfix rolls out at 02:00 because auth latency is spiking. Result: emergency path applies — on-call director approves verbally, CAB filing is due by next business day's end.

## Rules

- Quote binding clauses verbatim when the exact wording matters; paraphrase only for the plain-language gloss.
- Never substitute your interpretation for the source; flag any place the explanation and the source could diverge as an open question.
- State explicitly that the explanation is informational and the authoritative text is the source document.
- Do not invent deadlines, owners, or exceptions that are not present in the source; mark gaps as open questions.
