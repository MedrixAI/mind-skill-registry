---
name: literature-reviewer
description: 系统化的文献检索、筛选、分析与综合。当用户需要进行文献综述、系统评价、meta分析、总结某主题的研究进展或识别研究空白时使用此技能。
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.literature-reviewer
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
---
# Literature Reviewer

Conduct systematic literature reviews: structured search, screening, extraction, appraisal, and synthesis.

## When to Use
- "Literature review on [topic]" / "summarize research on [topic]"
- "Systematic review" or "meta-analysis"
- "What do recent papers say about [topic]"
- "Identify research gaps in [field]"

## Workflow (7 Steps)

### Step 1 — Define the Question (PICO)
Clarify scope using Population, Intervention, Comparison, Outcome.
Example: "In adults with type 2 diabetes (P), does metformin (I) vs placebo (C) reduce cardiovascular events (O)?"
Output: a one-sentence research question.

### Step 2 — Search Strategy
- KB: `knowledge_search` with semantic phrasing; `grep_chunks` with alternation, e.g. `metformin|cardiovascular|CVD`.
- Web (if KB thin): `web_search` targeting PubMed, Scholar, Cochrane.
- Record every query and date range used.

### Step 3 — Screen & Select
Define inclusion (design, date range, language, min sample) and exclusion (editorials, non-peer-reviewed, duplicates) criteria. For each hit, read the abstract via `list_knowledge_chunks` and tag include / exclude / uncertain. Cite each retained study inline.

### Step 4 — Extract Data
Per included study capture: design, N, population, intervention, outcomes, main results (effect size + CI), author-noted limitations. Read full text with `list_knowledge_chunks`. Record in the extraction table below.

### Step 5 — Appraise Quality
- RCTs: Cochrane RoB 2.0 (randomization, blinding, attrition, selective reporting).
- Observational: Newcastle-Ottawa (selection, comparability, outcome).
Assign High / Moderate / Low to each study.

### Step 6 — Synthesize
Group findings by subtopic. Compare and contrast across studies. Note agreements, conflicts, and the strength of evidence. Quantitative pooling only if designs/outcomes are comparable.

### Step 7 — Report & Identify Gaps
Write the structured review (template below), state research gaps and future directions, and compile the reference list.

## Recommended Tools
`knowledge_search`, `grep_chunks`, `list_knowledge_chunks`, `get_document_info`, `web_search`, `web_fetch`, `write_artifact`, `todo_write`, `thinking`.

## Output Template
```markdown
## Literature Review: [Topic]

### Background
[Context and importance, with inline citations]

### Methods
- Search sources: [KB / PubMed / ...]
- Date range: [...]
- Inclusion/exclusion: [...]
- Studies included: [N]

### Extraction Summary
| Study | Design | N | Key Finding | Effect Size (95% CI) | Quality |
|-------|--------|---|-------------|----------------------|---------|
| ...   | ...    | ..| ...         | ...                  | ...     |

### Key Findings
#### Subtopic 1
[Synthesis with inline citations]

### Research Gaps
[Gaps and future directions]

### Conclusion
[Current state of evidence]

---
**References**
1. [Citation]
```

## Best Practices
- Never cite a paper you have not read in full via `list_knowledge_chunks`.
- Distinguish primary studies from reviews.
- Flag conflicting evidence explicitly rather than averaging it away.
- Prefer recent, higher-quality, larger-N studies when weighting conclusions.
