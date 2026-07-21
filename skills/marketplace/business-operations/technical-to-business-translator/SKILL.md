---
name: technical-to-business-translator
description: Translate technical analysis into business language. Use when explaining
  statistical concepts to non-analysts, simplifying technical findings, or bridging
  communication between data teams and business stakeholders.
metadata:
  mind.id: ai.medrix.skill.technical-to-business-translator
  mind.distribution: marketplace
  mind.market-primary: business-operations
  mind.market-categories: '["business-operations", "knowledge-learning"]'
  mind.marketplace-summary: technical-to-business-translator (nimrodfisher)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Translate technical analysis into business language. Use when explaining statistical concepts to non-analysts, simplifying technical findings, or bridging communication between data teams and business stakeholders.","starter_prompts":["Help me with technical to business translator. Start by asking for the business goal, stakeholders, available inputs, constraints, and desired decision or deliverable, then complete the workflow.","Apply technical to business translator to the material I provide, identify the most important findings, risks, and evidence gaps, and produce a decision-ready result.","Review my existing technical to business translator work, correct weak assumptions or missing details, and return an improved version with clear next actions."]},"zh-CN":{"description":"将技术分析翻译为业务语言。适用于向非分析人员解释统计概念、简化技术发现，或连接数据团队与业务沟通。","starter_prompts":["请帮我完成technical to business translator。先询问业务目标、利益相关者、现有输入、约束以及需要支持的决策或交付物，然后完成整个流程。","请对我提供的材料开展technical to business translator，找出最重要的发现、风险和证据缺口，并输出可用于决策的结果。","请审查我现有的technical to business translator成果，修正薄弱假设和遗漏细节，并给出改进版本及明确的后续行动。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/nimrodfisher/data-analytics-skills
  mind.upstream.commit: 88498848c174ef162eba31fe5b6071faf02f8dc2
  mind.upstream.license: NOASSERTION
  mind.upstream.path: 05-stakeholder-communication/technical-to-business-translator/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/88498848c174ef162eba31fe5b6071faf02f8dc2/05-stakeholder-communication/technical-to-business-translator/SKILL.md"]'
license: NOASSERTION
---

# When to use

When technical output (model results, statistical tests, query findings) needs to be understood by a business audience. Also use to review your own writing before sending — it is easy to slip into jargon without noticing.

# Process

1. **Detect jargon** — run `scripts/jargon_detector.py` on the draft text to flag technical terms that need translation.
2. **Score readability** — run `scripts/readability_scorer.py` to get Flesch-Kincaid grade level and sentence complexity metrics; target ≤ grade 10 for executive audiences.
3. **Identify the audience persona** — use `references/stakeholder_personas.md` to select the persona that best matches your reader; each persona has vocabulary preferences and typical questions.
4. **Apply translation patterns** — use `references/translation_pattern_library.md` to swap technical language for business equivalents (e.g., "p-value < 0.05" → "we're 95% confident this isn't random chance").
5. **Replace with metaphors where needed** — for complex statistical concepts, pick an appropriate metaphor from `references/metaphor_bank.md`.
6. **Draft the translated version** — use `assets/translation_template.md` to produce the parallel technical/business version; keep the original in an appendix for technical reviewers.

# Inputs the skill needs

- Draft technical text or findings
- Target audience role (VP, product manager, operations, finance, etc.)

# Output

- Jargon detection report
- Readability score before/after
- Translated text with original in appendix (`translation_template.md`)
