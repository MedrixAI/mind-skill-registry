---
name: methodology-explainer
description: Explain analysis methodology to diverse audiences. Use when documenting
  'how we did this' sections, building trust through transparency, or teaching analytical
  approaches to stakeholders.
metadata:
  mind.id: ai.medrix.skill.methodology-explainer
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools", "knowledge-learning"]'
  mind.marketplace-summary: methodology-explainer (nimrodfisher)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Explain analysis methodology to diverse audiences. Use when documenting ''how we did this'' sections, building trust through transparency, or teaching analytical approaches to stakeholders.","starter_prompts":["Help me use methodology explainer for my task. Start by asking for the goal, inputs, deadline, constraints, and desired output, then complete the workflow.","Apply methodology explainer to the material I provide, identify missing or inefficient steps, and produce a clearer, more reliable result.","Review my existing approach with methodology explainer and turn it into a practical checklist or plan with priorities, owners, and validation steps."]},"zh-CN":{"description":"面向不同受众解释分析方法。适用于撰写“我们如何完成”部分、通过透明度建立信任，或向利益相关者讲解分析方法。","starter_prompts":["请帮我用methodology explainer完成任务。先询问目标、输入、截止时间、约束和所需输出，然后完成整个流程。","请对我提供的材料应用methodology explainer，找出缺失或低效步骤，并产出更清晰、更可靠的结果。","请使用methodology explainer审查我现有的方法，并将其整理为包含优先级、负责人和验证步骤的实用清单或计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/nimrodfisher/data-analytics-skills
  mind.upstream.commit: 88498848c174ef162eba31fe5b6071faf02f8dc2
  mind.upstream.license: NOASSERTION
  mind.upstream.path: 05-stakeholder-communication/methodology-explainer/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/88498848c174ef162eba31fe5b6071faf02f8dc2/05-stakeholder-communication/methodology-explainer/SKILL.md"]'
license: NOASSERTION
---

# When to use

Any time you deliver findings that require the audience to trust the method — A/B tests, attribution models, forecasts, statistical analyses, or anything where "how did you get that?" is a likely question. Write the methodology section before distributing results, not after questions arrive.

# Process

1. **Identify the audience tier** — use `references/audience_depth_guide.md` to determine the appropriate level: executive (why/what), business analyst (what/how at high level), or technical peer (full detail).
2. **Select the explanation pattern** — use `references/methodology_explanation_patterns.md` to pick the structure: narrative, layered (short summary + appendix), or Q&A format.
3. **Draft the core explanation** — cover: what question was asked, what data was used, what method was applied, what assumptions were made, and what the key limitation is.
4. **Apply plain-language rewrites** — replace statistical terms with business equivalents per the translation table in `references/methodology_explanation_patterns.md`.
5. **Add a limitations paragraph** — every methodology explanation must include at least one honest limitation and what it means for the conclusions.
6. **Produce deliverables** — write-up using `assets/methodology_writeup_template.md`; if the methodology will be presented, use `assets/methodology_slide_template.md`.

# Inputs the skill needs

- Description of the analytical method used (technique, data, steps)
- Audience type (executive / business / technical)
- Any assumptions or known limitations

# Output

- Plain-language methodology write-up
- Limitations section
- Completed `methodology_writeup_template.md` or `methodology_slide_template.md`
