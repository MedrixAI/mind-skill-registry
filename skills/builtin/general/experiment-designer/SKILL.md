---
name: experiment-designer
description: 帮助用户设计科学实验。当用户需要设计实验、检验假设或确定对照组时使用此技能。
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.experiment-designer
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
---
# Experiment Designer

Guide users through rigorous experimental design.

## When to Use This Skill

- "Design an experiment to test [hypothesis]"
- "How do I measure [variable]"
- "What controls do I need for [experiment]"
- "Help plan my study design"

## Workflow (6 Steps)

### Step 1 — Hypothesis Clarification
- Null hypothesis (H0): default assumption
- Alternative hypothesis (H1): what you are testing
- Variables: independent, dependent, confounding

### Step 2 — Experimental Approach
- Design type: observational / experimental / quasi-experimental
- Between-subjects vs. within-subjects
- Randomization strategy
- Blinding (single / double)

### Step 3 — Sample Size & Power
- Desired effect size
- Significance level (α = 0.05 typical)
- Power (1−β = 0.80 typical)
- Use `claw_task` for power analysis calculations

### Step 4 — Controls & Validity
- Positive control: known effect for comparison
- Negative control: no expected effect
- Internal validity: confounders to control
- External validity: generalizability

### Step 5 — Data Collection Plan
- Measurements: how to measure the dependent variable
- Frequency: pre/post-test, repeated measures
- Recording: suggest CSV structure

### Step 6 — Analysis Plan
- Primary statistical test (t-test / ANOVA / regression)
- Assumptions (normality, homoscedasticity, independence)
- Multiple comparison correction (Bonferroni / FDR)

## Output Template

```markdown
## Experimental Design: [Study Title]

### Research Question
[Question]

### Hypotheses
- H0: [null]
- H1: [alternative]

### Variables
- Independent: [variable] (levels: [A, B, C])
- Dependent: [variable] (measurement: [unit])
- Confounds: [list] (control: [how])

### Design
- Type: [between/within/mixed]
- Groups: [N] groups, n=[size] per group
- Randomization: [strategy]
- Blinding: [type]

### Procedure
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Data Analysis
- Primary test: [statistical test]
- Software: R / Python (via claw_task)
- α = 0.05

### Expected Outcomes
- If H1 supported: [pattern]
- If H0 not rejected: [implications]

### Limitations
- [Limitation 1]
- [Limitation 2]
```

## Best Practices
- Consult domain-specific methodologies in user's KB.
- Suggest pilot studies for novel designs.
- Remind about ethical considerations (IRB if human subjects).
- Encourage pre-registration for confirmatory studies.
