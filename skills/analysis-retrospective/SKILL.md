---
name: analysis-retrospective
description: Post-analysis learning and process improvement. Use when completing major
  analysis projects, documenting lessons learned, or improving team analytical practices.
metadata:
  mind.id: ai.medrix.skill.analysis-retrospective
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools", "knowledge-learning"]'
  mind.marketplace-summary: analysis-retrospective (nimrodfisher)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Post-analysis learning and process improvement. Use when completing major analysis projects, documenting lessons learned, or improving team analytical practices.","starter_prompts":["Help me use analysis retrospective for my task. Start by asking for the goal, inputs, deadline, constraints, and desired output, then complete the workflow.","Apply analysis retrospective to the material I provide, identify missing or inefficient steps, and produce a clearer, more reliable result.","Review my existing approach with analysis retrospective and turn it into a practical checklist or plan with priorities, owners, and validation steps."]},"zh-CN":{"description":"对已完成的分析进行复盘和流程改进。适用于重大分析项目结束后总结经验、记录教训，或改进团队的分析实践。","starter_prompts":["请帮我用analysis retrospective完成任务。先询问目标、输入、截止时间、约束和所需输出，然后完成整个流程。","请对我提供的材料应用analysis retrospective，找出缺失或低效步骤，并产出更清晰、更可靠的结果。","请使用analysis retrospective审查我现有的方法，并将其整理为包含优先级、负责人和验证步骤的实用清单或计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/nimrodfisher/data-analytics-skills
  mind.upstream.commit: 88498848c174ef162eba31fe5b6071faf02f8dc2
  mind.upstream.license: NOASSERTION
  mind.upstream.path: 06-workflow-optimization/analysis-retrospective/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/88498848c174ef162eba31fe5b6071faf02f8dc2/06-workflow-optimization/analysis-retrospective/SKILL.md"]'
license: NOASSERTION
---

# When to use

Within one week of completing a significant analysis project — while the details are still fresh. Also use after an analysis that went wrong (late delivery, stakeholder rejection, data error discovered post-delivery) to prevent recurrence. Run team retros quarterly even without a specific incident.

# Process

1. **Time-box the retro** — 30 minutes for solo, 60 minutes for team. Use the structured format in `references/retro_frameworks.md` to stay focused (Start/Stop/Continue or 4Ls: Liked/Lacked/Learned/Longed for).
2. **Review the project against plan** — compare actual timeline, scope, and effort to what was planned; note the gaps.
3. **Identify what went well** — capture at least two things that worked and should be repeated; these are as important as problems.
4. **Identify root causes of issues** — for each problem, apply 5-whys to find the actual cause rather than the symptom.
5. **Capture reusable learning** — use `references/learning_capture.md` to decide which learnings belong in: templates, reference docs, checklists, or team norms.
6. **Record and track actions** — fill in `assets/retrospective_template.md` with owners and due dates; log durable learnings in `assets/learnings_log_template.md`.

# Inputs the skill needs

- Completed analysis project (name, scope, timeline)
- Original plan or brief (for comparison)
- Participants (solo or team members involved)

# Output

- Completed retrospective (`retrospective_template.md`) with what-went-well, issues, root causes, and action items
- Learnings log entry (`learnings_log_template.md`) for reusable insights
