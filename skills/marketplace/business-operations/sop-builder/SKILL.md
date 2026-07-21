---
name: sop-builder
description: Build clear, executable standard operating procedures from goals, roles, inputs, controls, and escalation rules. Use when a user needs to create or improve an SOP, runbook, or repeatable process.
license: Apache-2.0
compatibility: Requires Mind Agent Harness 1.0 or later. No network access or external packages required.
metadata:
  mind.id: "ai.medrix.skill.sop-builder"
  mind.distribution: "marketplace"
  mind.market-primary: "business-operations"
  mind.market-categories: '["business-operations","productivity-tools"]'
  mind.marketplace-summary: "Build clear and executable operating procedures."
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Build clear, executable standard operating procedures from goals, roles, inputs, controls, and escalation rules. Use when a user needs to create or improve an SOP, runbook, or repeatable process.","starter_prompts":["Help me create an SOP. Start by asking for the process goal, roles, inputs, controls, exceptions, and escalation rules, then produce the finished procedure.","Review the SOP I provide, identify ambiguous or missing steps, and rewrite it so a new operator can execute it without additional guidance.","Turn the process notes I provide into a concise runbook with owners, prerequisites, numbered steps, validation checks, and escalation paths."]},"zh-CN":{"description":"根据目标、角色、输入、控制措施和升级规则，创建清晰且可执行的标准操作程序。适用于用户需要创建或改进 SOP、运行手册或可重复流程。","starter_prompts":["请帮我创建一份 SOP。先询问流程目标、角色、输入、控制措施、例外情况和升级规则，然后输出完整程序。","请审查我提供的 SOP，找出含糊或缺失的步骤，并重写为新操作人员无需额外指导即可执行的版本。","请把我提供的流程笔记整理成简明的运行手册，包含负责人、前置条件、编号步骤、验证检查和升级路径。"]}}}'
  mind.publisher: "medrixai"
  mind.runtime-category: "report"
  mind.tags: '["operations","sop","writing"]'
  mind.min-harness-version: ">=1.0.0"
---

# sop-builder

Build clear, executable standard operating procedures (SOPs) from the inputs a user provides or extracts from source material. Produce a single self-contained Markdown document an operator can follow step-by-step without consulting any other source.

## When to use

Invoke this skill when the user asks to:
- Create a new SOP, runbook, or repeatable process.
- Improve or repair an existing SOP that operators find ambiguous.
- Convert an incident postmortem or ad-hoc playbook into a maintained SOP.

Do not use it for one-off checklists or for reference documentation that is not procedural.

## Inputs

Collect (or ask for) each of these. State any assumption explicitly and flag missing inputs in the output rather than silently inventing them.

1. **Goal** — the single outcome the SOP produces (one sentence, verifiable).
2. **Roles** — who performs, who approves, who is notified. Use role names, not individuals.
3. **Triggers** — what event or schedule starts the procedure (time, signal, request).
4. **Preconditions** — access, tooling, environment state that must hold before step 1.
5. **Controls** — gates, sign-offs, or quality checks that must pass between phases.
6. **Escalation** — who to contact, and the threshold that triggers escalation, for each phase.
7. **Source material** — any existing docs, tickets, or transcripts the SOP must reflect.

## Output format

Emit one Markdown document with exactly these sections, in this order:

1. **Title** — `<procedure name> — SOP`.
2. **Purpose** — the Goal sentence.
3. **Scope** — what this procedure covers and explicitly what it does not.
4. **Roles & responsibilities** — a table of role → responsibility.
5. **Triggers & preconditions** — bullet lists.
6. **Procedure** — numbered steps. Each step has: actor, action (imperative), expected result, and (if applicable) control gate. Steps are atomic: one action per step.
7. **Escalation matrix** — a table of phase → trigger → contact → SLA.
8. **Definitions** — glossary of any non-obvious term used above.
9. **Revision history** — one-row table: version, date, author, change.

Keep the whole document under ~600 words. If it would exceed that, split the procedure into sub-procedures and note the split.

## Worked example

Goal: "Restart the billing-worker service without dropping in-flight jobs."

A minimal procedure fragment:

> 4. On-call engineer runs `billing-worker drain --timeout 5m`.
>    - Actor: on-call engineer.
>    - Expected result: `drained=OK, in_flight=0` printed to stdout.
>    - Control gate: do not proceed until `in_flight=0`. If it stays >0 after 5m, go to Escalation row B.
> 5. On-call engineer runs `systemctl restart billing-worker`.
>    - Expected result: `systemctl status` reports `active (running)`.
> 6. On-call engineer verifies queue depth is draining via `billing-worker queue-depth`.
>    - Control gate: queue depth must be decreasing over 3 consecutive 30s samples.

Escalation matrix fragment:

| Phase | Trigger | Contact | SLA |
|---|---|---|---|
| Drain | `in_flight > 0` after timeout | Platform on-call | 5 min |
| Restart | service fails to reach active | Platform on-call + billing lead | 10 min |

## Rules

- Use only the inputs provided; never fabricate runbook commands, hostnames, or contacts.
- Number steps consecutively across the whole procedure; do not restart per section.
- Prefer present-tense imperative verbs for actions ("Run", "Verify", "Notify").
- If a step depends on a tool the user has not confirmed exists, mark it `[assumes: <tool>]`.
