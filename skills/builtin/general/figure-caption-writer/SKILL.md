---
name: figure-caption-writer
description: 撰写可发表级别的图表标题。当用户需要为可视化或表格生成标题时使用此技能。
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.figure-caption-writer
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
---
# Figure Caption Writer

Generate publication-quality captions for figures and tables.

## When to Use This Skill

- "Write a caption for this figure"
- "Generate a table caption"
- "Describe this visualization"
- User creates figures via `write_artifact` or `claw_task`

## Caption Structure

### For Figures
```
Figure X. [Brief descriptive title]. [Detailed description: what is shown, how, sample sizes, statistical info]. [Legend explanation if needed]. [Abbreviations if used].
```

**Example:**
```
Figure 1. Effect of treatment on cell viability over time. Mean cell viability (±SEM) measured at 24h, 48h, and 72h post-treatment for control (blue) and drug-treated (red) groups (n=3 biological replicates, 3 technical replicates each). **p<0.05, ***p<0.001 by two-way ANOVA with Bonferroni post-hoc test. Error bars represent standard error of the mean.
```

### For Tables
```
Table X. [Descriptive title]. [Column/row explanations if needed]. [Statistical notes, significance markers].
```

**Example:**
```
Table 1. Demographic characteristics of study participants. Values are mean ± SD for continuous variables and n (%) for categorical variables. *p<0.05 by independent t-test (continuous) or chi-square (categorical).
```

## Workflow

1. Identify figure/table number and type (bar, line, scatter, heatmap, table).
2. Ask what data it shows (variables, groups, time points).
3. Ask for statistical info (n, test, significance).
4. Draft caption following the structure above.
5. Confirm abbreviations are defined.

## Best Practices
- **Self-contained**: reader should understand without the main text.
- **Specific**: include n, units, statistical tests.
- **Legend**: explain symbols, colors, abbreviations.
- **Statistics**: note significance levels and error bar meaning.
- **Tense**: use present tense ("shows", "represents").

## Output
Provide caption text ready to paste into the manuscript.
