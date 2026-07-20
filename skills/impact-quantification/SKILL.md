---
name: impact-quantification
description: Estimate and communicate business impact of insights. Use when sizing
  opportunities discovered in analysis, calculating ROI of recommended actions, or
  prioritizing initiatives by potential impact.
metadata:
  mind.id: ai.medrix.skill.impact-quantification
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools", "business-operations", "knowledge-learning"]'
  mind.marketplace-summary: impact-quantification (nimrodfisher)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Estimate and communicate business impact of insights. Use when sizing opportunities discovered in analysis, calculating ROI of recommended actions, or prioritizing initiatives by potential impact.","starter_prompts":["Help me use impact quantification for my task. Start by asking for the goal, inputs, deadline, constraints, and desired output, then complete the workflow.","Apply impact quantification to the material I provide, identify missing or inefficient steps, and produce a clearer, more reliable result.","Review my existing approach with impact quantification and turn it into a practical checklist or plan with priorities, owners, and validation steps."]},"zh-CN":{"description":"估算并沟通洞察的商业影响。适用于量化分析中发现的机会、计算建议行动的 ROI，或按潜在影响确定计划优先级。","starter_prompts":["请帮我用impact quantification完成任务。先询问目标、输入、截止时间、约束和所需输出，然后完成整个流程。","请对我提供的材料应用impact quantification，找出缺失或低效步骤，并产出更清晰、更可靠的结果。","请使用impact quantification审查我现有的方法，并将其整理为包含优先级、负责人和验证步骤的实用清单或计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/nimrodfisher/data-analytics-skills
  mind.upstream.commit: 88498848c174ef162eba31fe5b6071faf02f8dc2
  mind.upstream.license: NOASSERTION
  mind.upstream.path: 05-stakeholder-communication/impact-quantification/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/88498848c174ef162eba31fe5b6071faf02f8dc2/05-stakeholder-communication/impact-quantification/SKILL.md"]'
license: NOASSERTION
---

# When to use

After an analytical finding surfaces a potential action, change, or opportunity. Use to produce a defensible numeric estimate that stakeholders can act on. Also use when prioritizing a backlog of initiatives — quantified impact is the primary ranking signal.

# Process

1. **Classify the impact type** — revenue growth, cost reduction, risk reduction, or efficiency gain. Each type has a different formula family (see `references/impact_quantification_framework.md`).
2. **Gather inputs** — collect baseline metrics, affected population size, expected lift/reduction, time horizon, and confidence level.
3. **Build the point estimate** — use `scripts/revenue_impact.py` for revenue/growth scenarios or `scripts/cost_savings.py` for cost/efficiency scenarios.
4. **Add uncertainty bounds** — use `scripts/confidence_interval.py` to produce low/base/high estimates. Never deliver a single number without a range.
5. **Document assumptions** — fill in `references/assumption_documentation.md` for every input that is estimated rather than directly measured; note the sensitivity of the output to each.
6. **Package the estimate** — complete `assets/impact_estimate_template.md` with the range, assumptions, confidence, and recommended action; optionally build the full `assets/business_case_template.md` for larger decisions.

# Inputs the skill needs

- Baseline metric value (current state)
- Affected population or volume
- Expected change (lift %, absolute, or rate change)
- Time horizon (monthly / annual)
- Confidence level in inputs (high / medium / low)

# Output

- Impact estimate with low/base/high range
- Assumption log (source and sensitivity for each input)
- Completed `impact_estimate_template.md` or `business_case_template.md`
