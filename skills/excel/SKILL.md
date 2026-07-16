---
name: excel
description: Advanced Excel and spreadsheet analytics techniques
version: 2.0.0
sasmp_version: 2.0.0
bonded_agent: 01-data-analytics-foundations
bond_type: SECONDARY_BOND
config:
  atomic: true
  retry_enabled: true
  max_retries: 3
  backoff_strategy: exponential
parameters:
  skill_level:
    type: string
    required: true
    enum:
    - beginner
    - intermediate
    - advanced
    default: beginner
  focus_area:
    type: string
    required: false
    enum:
    - formulas
    - pivots
    - power_query
    - charts
    - all
    default: all
observability:
  logging_level: info
  metrics:
  - formula_complexity
  - pivot_usage
  - automation_level
metadata:
  mind.id: ai.medrix.skill.excel
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools"]'
  mind.marketplace-summary: excel (pluginagentmarketplace)
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/pluginagentmarketplace/custom-plugin-data-analyst
  mind.upstream.commit: 2150f932b448b967c6ae19f79b1611d712d4097c
  mind.upstream.license: NOASSERTION
  mind.upstream.path: skills/excel/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://github.com/pluginagentmarketplace/custom-plugin-data-analyst/blob/2150f932b448b967c6ae19f79b1611d712d4097c/LICENSE",
    "https://raw.githubusercontent.com/pluginagentmarketplace/custom-plugin-data-analyst/2150f932b448b967c6ae19f79b1611d712d4097c/skills/excel/SKILL.md"]'
license: NOASSERTION
---

# Excel Analytics Skill

## Overview
Master advanced Excel techniques for professional data analysis and reporting.

## Topics Covered
- Pivot tables and advanced filtering
- VLOOKUP, XLOOKUP, INDEX-MATCH
- Power Query and data transformation
- Excel formulas for analysis
- Charts and conditional formatting

## Learning Outcomes
- Master advanced Excel functions
- Build dynamic pivot tables
- Create automated reports
- Transform data with Power Query

## Error Handling

| Error Type | Cause | Recovery |
|------------|-------|----------|
| #REF! error | Broken cell reference | Check and update references |
| #N/A error | Lookup not found | Use IFERROR wrapper |
| Slow calculation | Too many formulas | Convert to values, optimize |
| File corruption | Crash during save | Enable AutoRecover, use cloud backup |

## Related Skills
- foundations (for core concepts)
- visualization (for chart design)
- reporting (for automated delivery)
