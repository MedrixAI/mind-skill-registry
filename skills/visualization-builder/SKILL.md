---
name: visualization-builder
description: Create effective, publication-ready data visualizations. Use when choosing
  chart types, designing presentation visuals, building dashboard charts, or applying
  visual design best practices to data output.
metadata:
  mind.id: ai.medrix.skill.visualization-builder
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools"]'
  mind.marketplace-summary: visualization-builder (nimrodfisher)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Create effective, publication-ready data visualizations. Use when choosing chart types, designing presentation visuals, building dashboard charts, or applying visual design best practices to data output.","starter_prompts":["Help me use visualization builder for my task. Start by asking for the goal, inputs, deadline, constraints, and desired output, then complete the workflow.","Apply visualization builder to the material I provide, identify missing or inefficient steps, and produce a clearer, more reliable result.","Review my existing approach with visualization builder and turn it into a practical checklist or plan with priorities, owners, and validation steps."]},"zh-CN":{"description":"创建有效且可发表的数据可视化。适用于选择图表类型、设计演示视觉、构建仪表盘图表或优化数据输出。","starter_prompts":["请帮我用visualization builder完成任务。先询问目标、输入、截止时间、约束和所需输出，然后完成整个流程。","请对我提供的材料应用visualization builder，找出缺失或低效步骤，并产出更清晰、更可靠的结果。","请使用visualization builder审查我现有的方法，并将其整理为包含优先级、负责人和验证步骤的实用清单或计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/nimrodfisher/data-analytics-skills
  mind.upstream.commit: 88498848c174ef162eba31fe5b6071faf02f8dc2
  mind.upstream.license: NOASSERTION
  mind.upstream.path: 04-data-storytelling-visualization/visualization-builder/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/88498848c174ef162eba31fe5b6071faf02f8dc2/04-data-storytelling-visualization/visualization-builder/SKILL.md"]'
license: NOASSERTION
---

# Visualization Builder

# When to use
- Choosing the right chart type for a specific analytical message
- A chart exists but is cluttered, misleading, or failing to make the point
- Building a chart for an executive presentation that must work without verbal explanation
- Producing consistent, branded visualisations across a report or dashboard
- Creating accessible charts that work for colorblind viewers or screen readers

# Process
1. **Identify the message type** — classify the chart's purpose: comparison (bar), trend over time (line), composition / part-of-whole (stacked bar, pie only for 2–3 categories), distribution (histogram, box plot), or relationship (scatter). The message type determines the chart type. See `references/chart_selection_guide.md`.
2. **Select and load the data** — confirm the data is at the right grain for the chart. Aggregations (e.g., groupby month) should happen before plotting, not inside the chart library.
3. **Build the base chart** — use `scripts/chart_builder.py` with pre-set professional styling (whitegrid, sans-serif, accessible color palette). Set axes, ticks, and scale deliberately — default settings are often wrong.
4. **Apply visual hierarchy** — make the most important data element visually dominant (bolder line, darker bar, distinct color). De-emphasise secondary series. Remove every element that doesn't contribute to the message (gridlines at 0.2 alpha, no top/right spines). See `references/visual_design_principles.md`.
5. **Annotate for the reader** — add a descriptive title that states the finding ("Mobile churn is 2× desktop"), not the variable names ("Churn by device type"). Annotate key data points, thresholds, and reference lines directly on the chart. Add a data source and date.
6. **Export and validate** — export at 300 DPI for print or 150 DPI for web. View the chart at the intended display size. Check: is the key message legible in under 5 seconds? Does it work in greyscale? Complete `assets/viz_spec_template.md` if the chart is part of a larger deliverable.

# Inputs the skill needs
- The data to be visualised (at the correct aggregation grain)
- The single key message the chart must communicate
- The audience (technical or executive) and the display context (presentation slide, report, dashboard, email)
- Brand colors or style guidelines if applicable
- Any accessibility requirements (colorblind palette, alt text)

# Output
- `scripts/chart_builder.py` — creates professional matplotlib/seaborn charts with pre-set styling, annotation helpers, and export settings
- `references/chart_selection_guide.md` — which chart type for which message; common chart mistakes and how to fix them
- `references/visual_design_principles.md` — color, typography, hierarchy, annotation, and accessibility principles
- `assets/viz_spec_template.md` — spec template for a chart: message, data source, chart type, annotations, export requirements
