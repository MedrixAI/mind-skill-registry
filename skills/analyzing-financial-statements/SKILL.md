---
name: analyzing-financial-statements
description: This skill calculates key financial ratios and metrics from financial
  statement data for investment analysis
metadata:
  mind.id: ai.medrix.skill.analyzing-financial-statements
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools", "business-operations"]'
  mind.marketplace-summary: analyzing-financial-statements (anthropics)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"This skill calculates key financial ratios and metrics from financial statement data for investment analysis","starter_prompts":["Help me use analyzing financial statements for my task. Start by asking for the goal, inputs, deadline, constraints, and desired output, then complete the workflow.","Apply analyzing financial statements to the material I provide, identify missing or inefficient steps, and produce a clearer, more reliable result.","Review my existing approach with analyzing financial statements and turn it into a practical checklist or plan with priorities, owners, and validation steps."]},"zh-CN":{"description":"根据财务报表数据计算关键财务比率和指标，用于投资分析。","starter_prompts":["请帮我用analyzing financial statements完成任务。先询问目标、输入、截止时间、约束和所需输出，然后完成整个流程。","请对我提供的材料应用analyzing financial statements，找出缺失或低效步骤，并产出更清晰、更可靠的结果。","请使用analyzing financial statements审查我现有的方法，并将其整理为包含优先级、负责人和验证步骤的实用清单或计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/anthropics/claude-cookbooks
  mind.upstream.commit: 67ce644d33e5933f0bcc0b6eb4113df41bbf3a8f
  mind.upstream.license: MIT
  mind.upstream.path: skills/custom_skills/analyzing-financial-statements/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://github.com/anthropics/claude-cookbooks/blob/67ce644d33e5933f0bcc0b6eb4113df41bbf3a8f/LICENSE",
    "https://raw.githubusercontent.com/anthropics/claude-cookbooks/67ce644d33e5933f0bcc0b6eb4113df41bbf3a8f/skills/custom_skills/analyzing-financial-statements/SKILL.md"]'
license: MIT
---

# Financial Ratio Calculator Skill

This skill provides comprehensive financial ratio analysis for evaluating company performance, profitability, liquidity, and valuation.

## Capabilities

Calculate and interpret:
- **Profitability Ratios**: ROE, ROA, Gross Margin, Operating Margin, Net Margin
- **Liquidity Ratios**: Current Ratio, Quick Ratio, Cash Ratio
- **Leverage Ratios**: Debt-to-Equity, Interest Coverage, Debt Service Coverage
- **Efficiency Ratios**: Asset Turnover, Inventory Turnover, Receivables Turnover
- **Valuation Ratios**: P/E, P/B, P/S, EV/EBITDA, PEG
- **Per-Share Metrics**: EPS, Book Value per Share, Dividend per Share

## How to Use

1. **Input Data**: Provide financial statement data (income statement, balance sheet, cash flow)
2. **Select Ratios**: Specify which ratios to calculate or use "all" for comprehensive analysis
3. **Interpretation**: The skill will calculate ratios and provide industry-standard interpretations

## Input Format

Financial data can be provided as:
- CSV with financial line items
- JSON with structured financial statements
- Text description of key financial figures
- Excel files with financial statements

## Output Format

Results include:
- Calculated ratios with values
- Industry benchmark comparisons (when available)
- Trend analysis (if multiple periods provided)
- Interpretation and insights
- Excel report with formatted results

## Example Usage

"Calculate key financial ratios for this company based on the attached financial statements"

"What's the P/E ratio if the stock price is $50 and annual earnings are $2.50 per share?"

"Analyze the liquidity position using the balance sheet data"

## Scripts

- `calculate_ratios.py`: Main calculation engine for all financial ratios
- `interpret_ratios.py`: Provides interpretation and benchmarking

## Best Practices

1. Always validate data completeness before calculations
2. Handle missing values appropriately (use industry averages or exclude)
3. Consider industry context when interpreting ratios
4. Include period comparisons for trend analysis
5. Flag unusual or concerning ratios

## Limitations

- Requires accurate financial data
- Industry benchmarks are general guidelines
- Some ratios may not apply to all industries
- Historical data doesn't guarantee future performance
