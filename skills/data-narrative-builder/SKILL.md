---
name: data-narrative-builder
description: Build compelling data-driven narratives. Use when presenting analysis
  results, creating stakeholder reports, or transforming a set of findings into a
  story that drives a specific decision or action.
metadata:
  mind.id: ai.medrix.skill.data-narrative-builder
  mind.distribution: marketplace
  mind.market-primary: content-creation
  mind.market-categories: '["content-creation", "productivity-tools", "knowledge-learning"]'
  mind.marketplace-summary: data-narrative-builder (nimrodfisher)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Build compelling data-driven narratives. Use when presenting analysis results, creating stakeholder reports, or transforming a set of findings into a story that drives a specific decision or action.","starter_prompts":["Help me create data narrative builder. Start by asking for the audience, purpose, source material, tone, format, and constraints, then produce a polished result.","Use data narrative builder to improve the draft or assets I provide, explain the most important changes, and deliver the revised version.","Create three strong directions for data narrative builder from my brief, compare their tradeoffs, and develop the best option."]},"zh-CN":{"description":"构建有说服力的数据叙事。适用于呈现分析结果、创建利益相关者报告，或将一组发现转化为推动具体决策或行动的故事。","starter_prompts":["请帮我完成data narrative builder。先询问受众、目的、素材、语气、格式和约束，然后产出可直接使用的成品。","请用data narrative builder改进我提供的草稿或素材，说明最重要的修改，并交付修订后的版本。","请根据我的简报为data narrative builder提出三个有力方向，比较各自取舍，并完善最佳方案。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/nimrodfisher/data-analytics-skills
  mind.upstream.commit: 88498848c174ef162eba31fe5b6071faf02f8dc2
  mind.upstream.license: NOASSERTION
  mind.upstream.path: 04-data-storytelling-visualization/data-narrative-builder/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/88498848c174ef162eba31fe5b6071faf02f8dc2/04-data-storytelling-visualization/data-narrative-builder/SKILL.md"]'
license: NOASSERTION
---

# Data Narrative Builder

# When to use
- A presentation exists but feels like a data dump rather than a story
- The analysis has a clear finding but the team doesn't know how to make it compelling
- The audience is senior and will not read more than 5 slides
- A decision needs to be made and the data needs to make a clear, emotion-aware argument
- A recurring report needs to be restructured around a narrative rather than a metric list

# Process
1. **Identify the central message** — write the single most important thing the audience should know and do after seeing this. Everything else is supporting material. If there's more than one message, there are multiple presentations.
2. **Choose a narrative framework** — select the structure that fits the context. Situation–Complication–Resolution works for most problem/solution stories. Before–After–Bridge is strong for demonstrating impact. See `references/narrative_frameworks.md` for all patterns with examples.
3. **Assign an emotional arc** — map each section to an intended emotional state: establish comfort (Situation), introduce tension (Complication), offer confidence (Resolution). Tone and data emphasis should match the intended emotion at each stage.
4. **Draft each section with data woven in** — apply the pyramid principle: lead with the conclusion, then support it with evidence. Numbers must serve the narrative, not interrupt it. Round large numbers for recall; humanise by expressing impact in terms the audience cares about.
5. **Plan the visual sequence** — assign one key chart or visual to each narrative beat. The visual should reinforce the spoken or written message, not repeat it. See `references/data_writing_guide.md` for annotation and emphasis techniques.
6. **Write the opening hook and closing call to action** — the hook must earn attention in under 10 seconds (a surprising stat, a question, or a contrast). The CTA must name a specific decision, person, and deadline. Complete `assets/narrative_template.md`.

# Inputs the skill needs
- The central finding or insight to be communicated
- The audience (role, knowledge level, what they care about most)
- The desired action or decision at the end of the presentation
- All supporting data and charts already prepared
- Format and time constraints (slides, report, 5-minute presentation, 30-page doc)

# Output
- `references/narrative_frameworks.md` — SCR, BAB, hero journey, and sparklines patterns with data storytelling examples
- `references/data_writing_guide.md` — pyramid principle, number formatting, annotation, plain-language techniques
- `assets/narrative_template.md` — fill-in-the-blank narrative structure: hook, situation, complication, resolution, call to action
