---
name: report-master
description: Generate structured, source-grounded research and business reports as Word-aware HTML. Reports include sections, citations, editable tables, optional data-driven visual blocks, and an embedded ReportDocument JSON model for downstream DOCX export.
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.report-master
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: report
  mind.tags: '["artifact-template","report"]'
  mind.runtime-default: 'true'
---
# Report Master

Turn knowledge-base material into a readable, evidence-grounded report that works in two places:

1. HTML preview/editing in Mindar.
2. Native DOCX export with editable Word tables.

## Hard Rules

- Submit a complete standalone HTML document with `submit_html`.
- Do not use `<img>`, external image URLs, base64 image payloads, or `background-image: url(...)`.
- Do not load Tailwind CDN, Google Fonts, external stylesheets, remote scripts, or any other network dependency. Use self-contained CSS and deterministic system-font fallbacks.
- Do not fabricate facts, metrics, dates, benchmarks, citations, charts, or tables.
- If source evidence is thin, say so clearly and use a caveat or qualitative table instead of making a chart.
- Keep the report text-driven and printable. Use clear headings, concise paragraphs, tables, citations, and action-oriented sections.
- Use the requested output language. If no language is clear, default to business English for US/EU knowledge workers.

## Default Audience Contract

When the user does not choose options, generate a smart default report for US/EU knowledge workers who care about knowledge management and office productivity.

Default shape:

- Executive summary.
- Evidence-backed key findings.
- Confidence, assumptions, and limits.
- Tables where they improve scanning or later editing.
- Balanced source-grounded visuals only when data supports them.
- Next actions.
- GDPR/privacy sensitivity where relevant.
- References/source appendix.

## Report Types

Use the selected report type when provided. If the type is `auto`, infer the best one from source material and user intent.

- Executive brief: decision-ready summary, risks, and next actions.
- Consulting analysis: findings, options, tradeoffs, and recommendations.
- Product/Ops memo: operational context, product/ops decisions, execution plan.
- Market/competitive report: landscape, competitors, market signals, gaps.
- Research synthesis: evidence synthesis, source contrast, limits.
- Learning/study guide: concepts, study notes, review checklist.
- Finance/FP&A readout: KPI readout, variance, assumptions, actions.
- Legal/compliance memo: issues, evidence, risk, mitigation checklist.
- HR/L&D brief: people insights, learning needs, rollout plan.
- Personal knowledge digest: clean digest for personal knowledge workflows.

## Word-Aware HTML Contract

The HTML is the preview, but it must carry enough structure for native DOCX export.

### Required JSON Model

Embed this script near the end of `<body>`:

```html
<script id="report-document" type="application/json">
{
  "title": "Report title",
  "audience": "US/EU knowledge workers",
  "language": "en",
  "sections": [
    {
      "id": "section-01-summary",
      "title": "Executive summary",
      "summary": "Short section summary",
      "blocks": [
        {
          "id": "block-0001",
          "type": "paragraph",
          "text": "Source-grounded summary statement.",
          "citation_ids": ["ref-1"]
        },
        {
          "id": "block-0002",
          "type": "table",
          "title": "Evidence table",
          "headers": ["Finding", "Evidence"],
          "rows": [["Finding A", "Evidence A"]],
          "citation_ids": ["ref-1"]
        }
      ]
    }
  ],
  "blocks": [],
  "references": [{"id": "ref-1", "title": "Source title"}]
}
</script>
```

Every value in top-level `blocks` and `sections[].blocks` must be a complete JSON object matching the block schema. Never use strings, type names, IDs, or references such as `"blocks":["chart","table"]`; place each complete block object directly in the array. For KPI strips, use `items` with `label` and `value`. For chart data that must remain editable in Word, use `headers` and `rows` and keep the matching visible HTML table.

Supported block types:

- `heading`
- `paragraph`
- `list`
- `table`
- `kpi_strip`
- `chart`
- `callout`
- `caption`
- `source_note`
- `reference_list`
- `page_break`
- `timeline`
- `risk_matrix`
- `decision_matrix`
- `action_items`

`references` remains accepted as a compatibility alias for `reference_list`.

The JSON and the visible HTML must describe the same claims, tables, chart data, citations, and references.

For editable DOCX reports, every semantic block except `page_break` and `section_break`
must have a stable unique `id`, and its single visible HTML projection must carry the
same value in `data-report-block-id`. Do not reuse an ID or place the same ID on nested
elements. These IDs are the save-time contract that maps online edits back to Word.

```html
<h2 data-report-block-id="block-0001">Executive summary</h2>
<p data-report-block-id="block-0002">Editable report content.</p>
```

### Tables

Use native HTML tables for any data that should be editable after DOCX export.

```html
<table data-report-table data-citation-ids="1,2">
  <caption>Quarterly productivity signals</caption>
  <thead>
    <tr><th>Metric</th><th>Q1</th><th>Q2</th><th>Source</th></tr>
  </thead>
  <tbody>
    <tr><td>Time saved</td><td>12%</td><td>18%</td><td>[1]</td></tr>
  </tbody>
</table>
```

### Formulas

Use KaTeX-compatible LaTeX as the formula source. Never show raw LaTeX as the visual formula and never distribute equation tokens across table cells or spaced text.

- Display formula: use an `equation` ReportDocument block with `formula`, and project it once as `<div data-report-block-id="..." data-report-math="display" data-latex="...">...</div>`.
- Inline formula: use `ReportInline.formula`, and project it as `<span data-report-math="inline" data-latex="...">...</span>` inside the owning paragraph.
- HTML-escape the `data-latex` attribute. Keep a readable LaTeX fallback as the element text; the report renderer replaces it with static MathML.
- Use LaTeX commands for fractions, roots, scripts, Greek symbols, sums, integrals, matrices, vectors, and norms. Do not fake them with Unicode spacing.

```html
<p data-report-block-id="block-0003">
  The objective <span data-report-math="inline" data-latex="J(\theta)">J(\theta)</span> is minimized subject to the constraints below.
</p>
<div
  data-report-block-id="block-0004"
  data-report-math="display"
  data-latex="\min_{x} \sum_{i=1}^{n} \lVert A_i x-b_i \rVert_2^2"
>\min_{x} \sum_{i=1}^{n} \lVert A_i x-b_i \rVert_2^2</div>
```

### Charts

Charts are allowed only when source data supports them. Every chart must have an adjacent canonical table with the exact same data.

Required chart attributes:

- `data-report-chart`
- `data-chart-type`, for example `bar`
- `data-chart-data`, JSON-encoded data
- `data-citation-ids`

Stable preview:

- Prefer inline SVG/CSS for bar charts, KPI strips, timelines, risk matrices, and decision matrices.
- Chart.js/ECharts may be included only as progressive enhancement. They must not be the sole representation of the data.
- If a script fails, the report must still show readable SVG/CSS and a canonical data table.

Example:

```html
<figure
  data-report-chart
  data-chart-type="bar"
  data-chart-data='{"labels":["Search","Writing","Review"],"values":[32,24,18]}'
  data-citation-ids="1,3"
>
  <figcaption>Workflow time recovered by activity</figcaption>
  <svg role="img" aria-label="Bar chart showing workflow time recovered by activity"></svg>
</figure>
<table data-report-table data-citation-ids="1,3">
  <caption>Chart data: workflow time recovered by activity</caption>
  <thead><tr><th>Activity</th><th>Hours recovered</th><th>Source</th></tr></thead>
  <tbody>
    <tr><td>Search</td><td>32</td><td>[1]</td></tr>
    <tr><td>Writing</td><td>24</td><td>[3]</td></tr>
    <tr><td>Review</td><td>18</td><td>[3]</td></tr>
  </tbody>
</table>
```

## Components To Use When Appropriate

- KPI strip: 3-5 source-backed numbers with citations and caveats.
- Bar chart: categorical comparisons with source-backed numeric values.
- Timeline: events, phases, decisions, or implementation sequence.
- Risk matrix: risk, likelihood, impact, mitigation, owner/source.
- Decision matrix: option, criteria, score/fit, tradeoffs, recommendation.
- Action items: next action, owner/role, timing, dependency, confidence.
- References: numbered source list matching inline `[n]` citations.

## Research Workflow

1. Scan the knowledge base with `list_knowledge_chunks`.
2. Search for evidence per section with `knowledge_search` / `grep_chunks`.
3. Build an outline before writing. Use the requested section count when present.
4. Use tables/charts only where they clarify real evidence.
5. Write the final HTML and embed the ReportDocument JSON.
6. Submit with `submit_html`.

## Depth Guidance

- `brief`: 4-5 sections, short executive wording, high signal.
- `standard`: 5-7 sections, balanced analysis and tables.
- `deep`: 7-9 sections, more evidence, method notes, matrices, references.

## Layout Guidance

- Use a single-column reading layout with a comfortable measure.
- Include a table of contents for longer reports.
- Make sections printable with physical A4 dimensions, explicit page margins, and `box-sizing: border-box`. Never use a fixed 820px print width that exceeds the A4 content box.
- Keep section headings with the first following paragraph so headings are not stranded at the bottom of a page.
- Keep captions/source notes with the immediately adjacent chart or table. Keep short callouts, KPI strips, and compact matrices intact.
- Allow long tables to span pages. Use semantic `<thead>` so print renderers can repeat headers, and avoid splitting ordinary body rows where possible.
- Do not apply `break-inside: avoid` to every table, long paragraph, reference list, or entire section; doing so creates large empty areas.
- Reference lists may flow naturally across pages and must not carry private retrieval IDs such as `[2-source-...]` in visible content.
- Keep colors restrained and accessible. Avoid decorative visual noise.
- Do not add in-page feature explanations or UI controls.

## Template Contract

- When `report_template_id` or `report_template_label` is provided, align the report's hierarchy and content shape with that template without changing source facts.
- When `reference_document_name` or the compatibility field `reference_docx_name` is provided, treat it as the sole design authority. Do not blend in a built-in template. Match its hierarchy and page rhythm in the Word-aware HTML; the server applies the actual DOCX/DOTX/PDF styles, page setup, headers, and footers during export. Never expose its storage URI in visible HTML.
- For `linkedin_insight`, `instagram_carousel`, `x_thread`, `wechat_article`, `product_announcement`, and `community_update`, generate platform-native social content rather than a conventional research report. Use the platform's natural sequence (post, carousel slides, thread, or article), a strong hook, concise evidence-backed copy, and a clear discussion prompt or call to action while retaining the structured ReportDocument and citation contracts.

## Anti-Slop

- Avoid vague praise words. Make claims specific and sourced.
- Mark inference as inference.
- Keep citations near claims.
- Do not pad the report to hit a length target.
- If a requested visualization cannot be supported by the sources, explain the evidence gap.
