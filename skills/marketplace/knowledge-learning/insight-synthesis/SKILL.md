---
name: insight-synthesis
description: Transform data findings into compelling insights. Use when converting
  analysis results into actionable insights, connecting findings to business impact,
  or preparing insights for stakeholder communication.
metadata:
  mind.id: ai.medrix.skill.insight-synthesis
  mind.distribution: marketplace
  mind.market-primary: knowledge-learning
  mind.market-categories: '["knowledge-learning"]'
  mind.marketplace-summary: insight-synthesis (nimrodfisher)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Transform data findings into compelling insights. Use when converting analysis results into actionable insights, connecting findings to business impact, or preparing insights for stakeholder communication.","starter_prompts":["Help me with insight synthesis. Start by asking for the question, sources or material, required depth, constraints, and output format, then complete the analysis.","Use insight synthesis to synthesize the sources I provide, distinguish evidence from assumptions, identify gaps or contradictions, and produce clear conclusions.","Critically review my current understanding with insight synthesis, challenge weak reasoning, and turn the findings into an actionable learning or research plan."]},"zh-CN":{"description":"将数据发现转化为有说服力的洞察。适用于把分析结果变成可执行洞察、连接发现与商业影响，或准备利益相关者沟通材料。","starter_prompts":["请帮我完成insight synthesis。先询问研究问题、来源或材料、所需深度、约束和输出格式，然后完成分析。","请使用insight synthesis综合我提供的来源，区分证据与假设，识别缺口或矛盾，并形成清晰结论。","请使用insight synthesis批判性审查我当前的理解，挑战薄弱推理，并将发现转化为可执行的学习或研究计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/nimrodfisher/data-analytics-skills
  mind.upstream.commit: 88498848c174ef162eba31fe5b6071faf02f8dc2
  mind.upstream.license: NOASSERTION
  mind.upstream.path: 04-data-storytelling-visualization/insight-synthesis/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/88498848c174ef162eba31fe5b6071faf02f8dc2/04-data-storytelling-visualization/insight-synthesis/SKILL.md"]'
license: NOASSERTION
---

# Insight Synthesis

# When to use
- An analysis has produced many statistics but no clear "so what"
- The team has findings but is struggling to prioritise which ones to act on
- Stakeholders are asking "what does this mean for us?" rather than "what did you find?"
- Multiple analyses need to be synthesised into a unified set of recommendations
- Preparing an insight briefing for a team that doesn't have time to review the full analysis

# Process
1. **List all findings** — enumerate every statistically meaningful finding: trends, comparisons, correlations, anomalies, surprises. Write each as a factual statement. Don't interpret yet.
2. **Apply So What → Why → Now What to each finding** — convert each fact into an insight by answering: So what (why does this matter to the business?), Why (what is the most likely explanation?), Now what (what specific action should follow?). See `references/insight_framework.md`.
3. **Quantify business impact** — for each insight, estimate the financial, customer, or operational magnitude. An insight without a number is an observation. Use order-of-magnitude estimates if precise data is not available.
4. **Prioritise by impact × confidence × actionability** — score each insight on these three dimensions (1–3 scale). Insights that score high on all three are the ones to lead with. Deprioritise insights that are high-impact but low-confidence until validated.
5. **Group and resolve conflicts** — cluster related insights and check for contradictions. If two findings point in opposite directions, document the tension and state what additional data would resolve it.
6. **Produce the insight brief** — present the top 3–5 insights in priority order, each with the finding, So What / Why / Now What, business impact, and confidence level. Use `assets/insight_brief_template.md`.

# Inputs the skill needs
- All analysis findings (statistics, charts, model outputs, anomalies)
- Business context: current goals, OKRs, strategic priorities
- Audience who will act on the insights (role and decision authority)
- Confidence levels for the findings (based on sample size, method, data quality)
- Known constraints on action (budget, timeline, team capacity)

# Output
- `references/insight_framework.md` — So What / Why / Now What pattern, insight quality rubric, prioritisation matrix
- `references/prioritization_guide.md` — scoring insights by impact, confidence, and actionability; how to present trade-offs
- `assets/insight_brief_template.md` — structured brief: top insights in priority order, each with impact, explanation, recommendation, and confidence level
