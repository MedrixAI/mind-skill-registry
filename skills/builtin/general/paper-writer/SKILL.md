---
name: paper-writer
description: 引导用户完成学术论文写作工作流。当用户需要写论文、起草手稿或组织论文结构时使用此技能。
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.paper-writer
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
---
# Paper Writer

Structured workflow for writing academic papers section by section.

## When to Use This Skill

- User requests "write a paper on [topic]"
- User asks to "draft [section]" (abstract, intro, methods, etc.)
- User wants to "structure my manuscript"
- User says "turn my findings into a paper"

## Workflow (7 Steps)

### Step 1 — Clarify Paper Type & Venue
- Type: research article / review / short communication / letter
- Target venue: journal or conference (look up formatting guidelines)
- Word/page limit
- Required sections (IMRaD or custom)

### Step 2 — Generate Outline
Produce a structured outline:
```
Title: [working title]
Abstract (250 words): Background / Objective / Methods / Results / Conclusion
1. Introduction
   1.1 Background & Context
   1.2 Literature Review (→ literature-reviewer skill)
   1.3 Research Gap
   1.4 Objectives
2. Methods
   2.1 Study Design (→ experiment-designer skill if needed)
   2.2 Participants/Materials
   2.3 Procedures
   2.4 Statistical Analysis
3. Results
   3.1 Descriptive Statistics
   3.2 Main Findings (figures/tables)
   3.3 Secondary Analyses
4. Discussion
   4.1 Interpretation
   4.2 Comparison with Prior Work
   4.3 Limitations
   4.4 Implications
5. Conclusion
References
```

### Step 3 — Write Section by Section
- **Introduction**: Use `knowledge_search` for background; state the gap clearly.
- **Methods**: Specific enough for replication; past tense.
- **Results**: Facts only, no interpretation; use `data_analysis` for stats.
- **Discussion**: Interpret findings, compare with literature via `knowledge_search`.

### Step 4 — Citation Management
- Use `skill_search(query="citation-generator")` to obtain the tenant-visible canonical ref, then call `read_skill(skill_ref="<canonical skill_ref returned by skill_search>")` for consistent formatting.
- Build reference list incrementally; do not add citations in a separate pass.

### Step 5 — Figure/Table Planning
- Describe what each figure should show.
- Generate via `claw_task` with Python/matplotlib.
- Write standalone captions (→ figure-caption-writer skill).

### Step 6 — Generate Artifact
Use `write_artifact`:
- `kind: "report"` for full paper content (Markdown/HTML).
- `kind: "ppt"` for a conference presentation version.
- Set `source_refs` to relevant KB documents.

### Step 7 — Review Checklist
- [ ] All claims cited inline
- [ ] Figures/tables referenced in text
- [ ] Methods detailed enough for replication
- [ ] Limitations acknowledged
- [ ] Conclusion matches results
- [ ] Reference formatting consistent

## Output Template

```markdown
## [Section Name]

[Content with inline citations like (Author, Year)]

**Figures to Generate**:
- Figure 1: [Description] → claw_task with matplotlib code
```

## Best Practices
- Write Methods before Results (clarifies what was measured).
- Results = facts, Discussion = interpretation.
- Avoid overinterpreting null results.
- Use past tense for your study, present tense for established facts.
- Follow target venue's formatting guidelines.
