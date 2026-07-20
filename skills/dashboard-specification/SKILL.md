---
name: dashboard-specification
description: Design specifications for effective dashboards. Use when planning new
  dashboards, improving existing ones, or documenting dashboard requirements before
  development starts.
metadata:
  mind.id: ai.medrix.skill.dashboard-specification
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools"]'
  mind.marketplace-summary: dashboard-specification (nimrodfisher)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Design specifications for effective dashboards. Use when planning new dashboards, improving existing ones, or documenting dashboard requirements before development starts.","starter_prompts":["Help me use dashboard specification for my task. Start by asking for the goal, inputs, deadline, constraints, and desired output, then complete the workflow.","Apply dashboard specification to the material I provide, identify missing or inefficient steps, and produce a clearer, more reliable result.","Review my existing approach with dashboard specification and turn it into a practical checklist or plan with priorities, owners, and validation steps."]},"zh-CN":{"description":"设计有效仪表盘的规格说明。适用于规划新仪表盘、改进现有仪表盘，或在开发前记录仪表盘需求。","starter_prompts":["请帮我用dashboard specification完成任务。先询问目标、输入、截止时间、约束和所需输出，然后完成整个流程。","请对我提供的材料应用dashboard specification，找出缺失或低效步骤，并产出更清晰、更可靠的结果。","请使用dashboard specification审查我现有的方法，并将其整理为包含优先级、负责人和验证步骤的实用清单或计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/nimrodfisher/data-analytics-skills
  mind.upstream.commit: 88498848c174ef162eba31fe5b6071faf02f8dc2
  mind.upstream.license: NOASSERTION
  mind.upstream.path: 04-data-storytelling-visualization/dashboard-specification/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/88498848c174ef162eba31fe5b6071faf02f8dc2/04-data-storytelling-visualization/dashboard-specification/SKILL.md"]'
license: NOASSERTION
---

# Dashboard Specification

# When to use
- A new dashboard is being built and developers need a clear brief before starting
- An existing dashboard is confusing or underused and needs a structured redesign
- Stakeholders and the data team have different ideas about what a dashboard should show
- Documenting dashboard requirements as part of a broader data product process
- Creating a self-service analytics specification that can be handed off without multiple Q&A rounds

# Process
1. **Define the purpose** — write one sentence: "This dashboard answers [question] for [audience] who need to [decision or action]." If it can't be stated in one sentence, the scope needs narrowing first. See `references/dashboard_design_principles.md`.
2. **Profile target users** — for each audience (executive, manager, IC), document their visit frequency, the primary question they come to answer, and their technical comfort level. Users with different needs usually need different dashboards, not more filters on one.
3. **Define the metric hierarchy** — list primary KPIs (hero numbers at the top), secondary supporting metrics, and detail-level breakdowns. A dashboard with more than 10–12 distinct metrics is trying to do too much.
4. **Design the information architecture** — sketch the layout using the hero → trends → breakdowns → details pattern. Position the most important information in the top-left. Use `references/dashboard_requirements_guide.md` for layout patterns.
5. **Specify interactivity** — list global filters (date range, region, segment), drill-down paths, click actions, and hover tooltip content. Every filter and drill-down adds complexity; justify each one.
6. **Document data requirements and success criteria** — for each metric, record the source table, transformation logic, and refresh frequency. Define how dashboard success will be measured (adoption rate, reduction in ad-hoc requests). Complete `assets/dashboard_spec_template.md`.

# Inputs the skill needs
- The business question the dashboard is meant to answer
- A list of candidate metrics (team can provide a rough list; you'll curate it)
- The primary audience (role, visit frequency, decision they make)
- Data availability: confirmed source tables and refresh schedules
- Any constraints: tool (Tableau, Looker, Metabase, etc.), branding guidelines

# Output
- `references/dashboard_design_principles.md` — layout hierarchy, chart selection, information density guidelines
- `references/dashboard_requirements_guide.md` — how to run requirements gathering, avoid scope creep, and validate the spec
- `assets/dashboard_spec_template.md` — complete spec: purpose, users, metric hierarchy, layout wireframe, interactivity, data sources, success criteria
