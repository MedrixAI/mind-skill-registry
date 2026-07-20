---
name: peer-review-template
description: Structured peer review for analytical work. Use when reviewing teammates'
  analysis, providing constructive feedback, or establishing analysis quality standards.
metadata:
  mind.id: ai.medrix.skill.peer-review-template
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools", "knowledge-learning"]'
  mind.marketplace-summary: peer-review-template (nimrodfisher)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Structured peer review for analytical work. Use when reviewing teammates'' analysis, providing constructive feedback, or establishing analysis quality standards.","starter_prompts":["Help me use peer review template for my task. Start by asking for the goal, inputs, deadline, constraints, and desired output, then complete the workflow.","Apply peer review template to the material I provide, identify missing or inefficient steps, and produce a clearer, more reliable result.","Review my existing approach with peer review template and turn it into a practical checklist or plan with priorities, owners, and validation steps."]},"zh-CN":{"description":"对分析工作进行结构化同行评审。适用于审查团队成员的分析、提供建设性反馈，或建立分析质量标准。","starter_prompts":["请帮我用peer review template完成任务。先询问目标、输入、截止时间、约束和所需输出，然后完成整个流程。","请对我提供的材料应用peer review template，找出缺失或低效步骤，并产出更清晰、更可靠的结果。","请使用peer review template审查我现有的方法，并将其整理为包含优先级、负责人和验证步骤的实用清单或计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/nimrodfisher/data-analytics-skills
  mind.upstream.commit: 88498848c174ef162eba31fe5b6071faf02f8dc2
  mind.upstream.license: NOASSERTION
  mind.upstream.path: 06-workflow-optimization/peer-review-template/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/88498848c174ef162eba31fe5b6071faf02f8dc2/06-workflow-optimization/peer-review-template/SKILL.md"]'
license: NOASSERTION
---

# When to use

Before any analysis that will influence a significant decision is delivered to stakeholders. Peer review should be part of the standard delivery checklist for: dashboards going into production, reports used for strategic decisions, A/B test conclusions, and any analysis that will be cited externally.

# Process

1. **Agree scope of review** — clarify with the author what kind of review is needed: logic check, statistical validity, code review, or presentation clarity. Use `references/peer_review_framework.md` to set expectations.
2. **Review analytical rigour** — work through `references/analytical_rigor_checklist.md`: are the question and method aligned? Are assumptions valid? Is the conclusion supported by the data?
3. **Review code or SQL** — if the analysis involves code, apply `references/code_review_for_analysis.md`: reproducibility, correctness, readability, and performance.
4. **Write feedback** — use the feedback structure in `assets/peer_review_template.md`: must-fix issues, should-fix suggestions, and optional improvements. Be specific; "this is unclear" is not actionable.
5. **Author responds** — the author addresses each point and notes disposition (fixed / accepted as-is with rationale / deferred); use `assets/review_response_template.md`.
6. **Close the review** — reviewer confirms must-fix items are resolved and signs off; document the outcome in `assets/peer_review_template.md`.

# Inputs the skill needs

- Analysis output to review (notebook, report, dashboard spec, or SQL)
- Review scope agreed with author
- Reviewer name and role

# Output

- Completed review with categorised feedback (`peer_review_template.md`)
- Author response log (`review_response_template.md`)
- Sign-off confirmation
