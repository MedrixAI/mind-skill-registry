---
name: statistical-consultant
description: 帮助用户选择和解读统计分析。当用户问"该用什么检验"、"如何分析数据"或"解读这些结果"时使用此技能。
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.statistical-consultant
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
---
# Statistical Consultant

Guide users through statistical analysis decisions and interpretation.

## When to Use This Skill

- "What statistical test should I use?"
- "How do I analyze [describe data]"
- "Interpret these p-values"
- "Is my result significant?"
- "Check assumptions for [test]"

## Workflow (6 Steps)

### Step 1 — Understand the Data
- Data type: continuous / categorical / ordinal / count
- Sample size per group
- Number of groups; independent or paired
- Research question: difference / association / prediction

### Step 2 — Test Selection Decision Tree

**Comparing groups:**
- 2 independent, continuous → independent t-test
- 2 paired, continuous → paired t-test
- 3+ independent, continuous → one-way ANOVA
- 3+ groups, multiple IVs → factorial ANOVA
- 2 categorical → chi-square

**Associations:**
- 2 continuous → Pearson (normal) or Spearman (non-normal)
- Predict continuous outcome → linear regression
- Predict binary outcome → logistic regression

**Non-parametric alternatives:**
- Mann-Whitney U (vs. t-test)
- Wilcoxon signed-rank (vs. paired t-test)
- Kruskal-Wallis (vs. ANOVA)

### Step 3 — Check Assumptions
For parametric tests:
- Normality: Shapiro-Wilk, Q-Q plot
- Homogeneity of variance: Levene's test
- Independence: by design
- Sample size: n > 30 per group (rule of thumb)

Use `data_analysis` SQL to check:
```sql
SELECT group_var, COUNT(*) as n,
       AVG(outcome) as mean, STDDEV(outcome) as sd
FROM data GROUP BY group_var;
```

### Step 4 — Execute Analysis
Basic stats via `data_analysis` (DuckDB SQL). Complex analyses (ANOVA, regression) via `claw_task`:

```python
import pandas as pd
import scipy.stats as stats
df = pd.read_csv('data.csv')
t_stat, p_value = stats.ttest_ind(
    df[df['group']=='A']['outcome'],
    df[df['group']=='B']['outcome'])
print(f"t={t_stat:.3f}, p={p_value:.4f}")
```

### Step 5 — Interpret Results
- p < 0.05: statistically significant (reject H0)
- Effect size: Cohen's d (small=0.2, medium=0.5, large=0.8)
- Confidence intervals: range of plausible values
- Statistical vs. practical significance

### Step 6 — Report

## Output Template

```markdown
## Statistical Analysis Results

### Test Performed
[Test name], testing [hypothesis]

### Assumptions
- Normality: [passed/failed, evidence]
- Homogeneity: [passed/failed, evidence]

### Results
- Test statistic: [value]
- df: [value]
- p-value: [value]
- Effect size: [d/r²/η²] = [value]
- 95% CI: [lower, upper]

### Interpretation
[Plain-language explanation]

### Recommendations
[Next steps, additional analyses]
```

## Best Practices
- Always check assumptions before running a test.
- Report effect sizes, not just p-values.
- Correct for multiple comparisons (Bonferroni / FDR).
- Use two-tailed tests unless a strong directional hypothesis exists.
- Visualize data before analyzing (histograms, boxplots).
