---
name: stakeholder-requirements-gathering
description: Structured requirements elicitation for analysis requests. Use when scoping
  new analysis projects, clarifying ambiguous business questions, or documenting analysis
  acceptance criteria with stakeholders.
metadata:
  mind.id: ai.medrix.skill.stakeholder-requirements-gathering
  mind.distribution: marketplace
  mind.market-primary: business-operations
  mind.market-categories: '["business-operations", "knowledge-learning"]'
  mind.marketplace-summary: stakeholder-requirements-gathering (nimrodfisher)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Structured requirements elicitation for analysis requests. Use when scoping new analysis projects, clarifying ambiguous business questions, or documenting analysis acceptance criteria with stakeholders.","starter_prompts":["Help me with stakeholder requirements gathering. Start by asking for the business goal, stakeholders, available inputs, constraints, and desired decision or deliverable, then complete the workflow.","Apply stakeholder requirements gathering to the material I provide, identify the most important findings, risks, and evidence gaps, and produce a decision-ready result.","Review my existing stakeholder requirements gathering work, correct weak assumptions or missing details, and return an improved version with clear next actions."]},"zh-CN":{"description":"为分析请求进行结构化需求获取。适用于界定新的分析项目、澄清模糊业务问题，或记录分析验收标准。","starter_prompts":["请帮我完成stakeholder requirements gathering。先询问业务目标、利益相关者、现有输入、约束以及需要支持的决策或交付物，然后完成整个流程。","请对我提供的材料开展stakeholder requirements gathering，找出最重要的发现、风险和证据缺口，并输出可用于决策的结果。","请审查我现有的stakeholder requirements gathering成果，修正薄弱假设和遗漏细节，并给出改进版本及明确的后续行动。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/nimrodfisher/data-analytics-skills
  mind.upstream.commit: 88498848c174ef162eba31fe5b6071faf02f8dc2
  mind.upstream.license: NOASSERTION
  mind.upstream.path: 05-stakeholder-communication/stakeholder-requirements-gathering/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/88498848c174ef162eba31fe5b6071faf02f8dc2/05-stakeholder-communication/stakeholder-requirements-gathering/SKILL.md"]'
license: NOASSERTION
---

# When to use

At the start of any non-trivial analysis request, especially when the ask is vague ("can you look into X?"), when multiple stakeholders have a stake in the outcome, or when the result will drive an important decision. Spending 30 minutes on requirements prevents days of rework.

# Process

1. **Run the intake interview** — use the question guide in `assets/interview_guide.md` to surface: the business decision being made, who the audience is, what "done" looks like, and what constraints exist.
2. **Identify the decision type** — apply `references/decision_maker_framework.md` to classify the decision (strategic / operational / tactical) and calibrate the required rigour and format.
3. **Document requirements** — fill in `assets/requirements_doc_template.md` covering: business question, success criteria, scope inclusions/exclusions, data sources, and timeline.
4. **Resolve ambiguities** — use the elicitation techniques in `references/elicitation_techniques.md` for any requirement still unclear after the interview (5-whys, scenario walkthrough, MoSCoW prioritisation).
5. **Get explicit sign-off** — send the requirements doc to the requestor for confirmation before starting work; update based on feedback.
6. **Produce the analysis brief** — convert approved requirements into `assets/analysis_brief_template.md`, which becomes the authoritative scope document for the project.

# Inputs the skill needs

- Stakeholder's initial request (however vague)
- Name and role of primary requestor and any other stakeholders
- Proposed deadline or urgency level

# Output

- Completed requirements doc (`requirements_doc_template.md`)
- Analysis brief ready to hand to the analyst (`analysis_brief_template.md`)
- Interview notes (optional, for complex projects)
