---
name: context-packager
description: Efficiently package context for AI-assisted analysis. Use when preparing
  to work with Claude on analysis, organizing context documents, or structuring prompts
  for complex analytical tasks.
metadata:
  mind.id: ai.medrix.skill.context-packager
  mind.distribution: marketplace
  mind.market-primary: knowledge-learning
  mind.market-categories: '["knowledge-learning"]'
  mind.marketplace-summary: context-packager (nimrodfisher)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Efficiently package context for AI-assisted analysis. Use when preparing to work with Claude on analysis, organizing context documents, or structuring prompts for complex analytical tasks.","starter_prompts":["Help me with context packager. Start by asking for the question, sources or material, required depth, constraints, and output format, then complete the analysis.","Use context packager to synthesize the sources I provide, distinguish evidence from assumptions, identify gaps or contradictions, and produce clear conclusions.","Critically review my current understanding with context packager, challenge weak reasoning, and turn the findings into an actionable learning or research plan."]},"zh-CN":{"description":"高效整理并打包用于 AI 辅助分析的上下文。适用于准备分析材料、组织上下文文档，或为复杂分析任务构建结构化提示。","starter_prompts":["请帮我完成context packager。先询问研究问题、来源或材料、所需深度、约束和输出格式，然后完成分析。","请使用context packager综合我提供的来源，区分证据与假设，识别缺口或矛盾，并形成清晰结论。","请使用context packager批判性审查我当前的理解，挑战薄弱推理，并将发现转化为可执行的学习或研究计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/nimrodfisher/data-analytics-skills
  mind.upstream.commit: 88498848c174ef162eba31fe5b6071faf02f8dc2
  mind.upstream.license: NOASSERTION
  mind.upstream.path: 06-workflow-optimization/context-packager/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/88498848c174ef162eba31fe5b6071faf02f8dc2/06-workflow-optimization/context-packager/SKILL.md"]'
license: NOASSERTION
---

# When to use

Before starting an AI-assisted analysis session when the task requires more than a single prompt — complex investigations, multi-step analyses, or work that depends on project-specific knowledge. A well-packaged context bundle reduces back-and-forth and produces better first responses.

# Process

1. **Identify required context layers** — use `references/context_layering_guide.md` to decide which layers are needed: task definition, business context, data schema, prior findings, constraints, and output format.
2. **Collect and deduplicate sources** — run `scripts/context_bundler.py` to merge multiple context files into a single structured bundle; it deduplicates and applies the layering order.
3. **Check token budget** — run `scripts/token_counter.py` on the bundle to estimate token count; trim lower-priority layers if over budget (see `references/context_layering_guide.md` for trimming priority).
4. **Score context quality** — evaluate the bundle against `references/context_quality_rubric.md`; a good bundle scores ≥ 7/10 on completeness, clarity, and relevance.
5. **Write the prompt header** — prepend a clear task statement to the bundle: what you need, what output format you expect, and any hard constraints.
6. **Save the package** — store the bundle using `assets/context_package_template.md` so it can be reused or updated for follow-up sessions.

# Inputs the skill needs

- Task description (what you want the AI to do)
- List of context source files or snippets (schema docs, prior reports, business definitions)
- Token budget (default: 100k tokens)

# Output

- Merged context bundle (single text file)
- Token count estimate
- Context quality score
- Ready-to-use prompt with task header (`context_package_template.md`)
