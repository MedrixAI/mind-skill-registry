---
name: customer-review-aggregator
description: Aggregate and analyze customer reviews from G2, Capterra, Trustpilot,
  App Store, and other platforms. Performs sentiment analysis, identifies pain points,
  extracts feature feedback, generates marketing claims, and compares competitor reviews.
  Use when users need review analysis, competitive intelligence, or customer feedback
  insights.
metadata:
  mind.id: ai.medrix.skill.customer-review-aggregator
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools", "business-operations", "knowledge-learning"]'
  mind.marketplace-summary: customer-review-aggregator (OneWave-AI)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Aggregate and analyze customer reviews from G2, Capterra, Trustpilot, App Store, and other platforms. Performs sentiment analysis, identifies pain points, extracts feature feedback, generates marketing claims, and compares competitor reviews. Use when users need review analysis, competitive intelligence, or customer feedback insights.","starter_prompts":["Help me use customer review aggregator for my task. Start by asking for the goal, inputs, deadline, constraints, and desired output, then complete the workflow.","Apply customer review aggregator to the material I provide, identify missing or inefficient steps, and produce a clearer, more reliable result.","Review my existing approach with customer review aggregator and turn it into a practical checklist or plan with priorities, owners, and validation steps."]},"zh-CN":{"description":"汇总并分析多个平台的客户评论，执行情感分析、识别痛点、提取功能反馈、生成营销论据并比较竞品评论。适用于评论分析、竞争情报和客户反馈洞察。","starter_prompts":["请帮我用customer review aggregator完成任务。先询问目标、输入、截止时间、约束和所需输出，然后完成整个流程。","请对我提供的材料应用customer review aggregator，找出缺失或低效步骤，并产出更清晰、更可靠的结果。","请使用customer review aggregator审查我现有的方法，并将其整理为包含优先级、负责人和验证步骤的实用清单或计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/OneWave-AI/claude-skills
  mind.upstream.commit: 4d09aaeeb87dc07701d8bcbd199d81b58c31c6ad
  mind.upstream.path: customer-review-aggregator/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://github.com/OneWave-AI/claude-skills/blob/4d09aaeeb87dc07701d8bcbd199d81b58c31c6ad/LICENSE",
    "https://raw.githubusercontent.com/OneWave-AI/claude-skills/4d09aaeeb87dc07701d8bcbd199d81b58c31c6ad/customer-review-aggregator/SKILL.md"]'
license: MIT
---

# Customer Review Aggregator & Analyzer

Pull reviews from multiple platforms and extract actionable insights with sentiment analysis, pain-point detection, marketing-claim extraction, and competitor comparison.

## Contents

- `references/sources.md` - supported platforms and sentiment dimensions
- `references/intake-prompts.md` - scope and data-collection prompts, example use cases
- `references/output-templates.md` - report templates for every analysis type

## Workflow

1. Define scope. Present the scope prompt from `references/intake-prompts.md` to capture product, platforms, competitors, analysis focus, and time period.
2. Gather review data. Offer the three data-collection methods (paste, CSV upload, URLs via WebFetch) from `references/intake-prompts.md` and collect the reviews.
3. Analyze sentiment. Score overall sentiment and feature-level sentiment using the dimensions in `references/sources.md`.
4. Identify pain points. Cluster negative feedback by theme, rank by frequency, and assign impact plus a recommendation.
5. Extract marketing claims. Derive evidence-backed claims from positive reviews, each with supporting quotes, a confidence level, and a use case.
6. Compare competitors. When competitors are provided, build the side-by-side comparison and surface weaknesses to exploit.
7. Analyze feature requests. Rank requested features by mention count, urgency, and competitor coverage.
8. Assemble the report. Populate the full analysis report and offer deliverable formats.

For all output formats and tables, see `references/output-templates.md`.
