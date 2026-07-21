---
name: daily-briefing
description: Start your day with a prioritized sales briefing. Works standalone when
  you tell me your meetings and priorities, supercharged when you connect your calendar,
  CRM, and email. Trigger with "morning briefing", "daily brief", "what's on my plate
  today", "prep my day", or "start my day".
metadata:
  mind.id: ai.medrix.skill.daily-briefing
  mind.distribution: marketplace
  mind.market-primary: business-operations
  mind.market-categories: '["business-operations"]'
  mind.marketplace-summary: daily-briefing (anthropics)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Start your day with a prioritized sales briefing. Works standalone when you tell me your meetings and priorities, supercharged when you connect your calendar, CRM, and email. Trigger with \"morning briefing\", \"daily brief\", \"what''s on my plate today\", \"prep my day\", or \"start my day\".","starter_prompts":["Help me with daily briefing. Start by asking for the business goal, stakeholders, available inputs, constraints, and desired decision or deliverable, then complete the workflow.","Apply daily briefing to the material I provide, identify the most important findings, risks, and evidence gaps, and produce a decision-ready result.","Review my existing daily briefing work, correct weak assumptions or missing details, and return an improved version with clear next actions."]},"zh-CN":{"description":"生成按优先级排序的每日销售简报。用户提供会议和重点即可独立使用，连接日历、CRM 与邮件后效果更佳。","starter_prompts":["请帮我完成daily briefing。先询问业务目标、利益相关者、现有输入、约束以及需要支持的决策或交付物，然后完成整个流程。","请对我提供的材料开展daily briefing，找出最重要的发现、风险和证据缺口，并输出可用于决策的结果。","请审查我现有的daily briefing成果，修正薄弱假设和遗漏细节，并给出改进版本及明确的后续行动。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/anthropics/knowledge-work-plugins
  mind.upstream.commit: 47caa757e4730eb8daf7d335470f692d4a68b59e
  mind.upstream.path: sales/skills/daily-briefing/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.license: Apache-2.0
  mind.upstream.evidence-urls: '["https://github.com/anthropics/knowledge-work-plugins/blob/47caa757e4730eb8daf7d335470f692d4a68b59e/sales/LICENSE",
    "https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/47caa757e4730eb8daf7d335470f692d4a68b59e/sales/skills/daily-briefing/SKILL.md"]'
license: Apache-2.0
---

# Daily Sales Briefing

Get a clear view of what matters most today. This skill works with whatever you tell me, and gets richer when you connect your tools.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                      DAILY BRIEFING                              │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone)                                       │
│  ✓ You tell me: today's meetings, key deals, priorities         │
│  ✓ I organize: prioritized action plan for your day             │
│  ✓ Output: scannable 2-minute briefing                          │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                      │
│  + Calendar: auto-pull today's meetings with attendees          │
│  + CRM: pipeline alerts, tasks, deal health                     │
│  + Email: unread from key accounts, waiting on replies          │
│  + Enrichment: overnight signals on your accounts               │
└─────────────────────────────────────────────────────────────────┘
```

---

## Getting Started

When you run this skill, I'll ask for what I need:

**If no calendar connected:**
> "What meetings do you have today? (Just paste your calendar or list them)"

**If no CRM connected:**
> "What deals are you focused on this week? Any that need attention?"

**If you have connectors:**
I'll pull everything automatically and just show you the briefing.

---

## Connectors (Optional)

Connect your tools to supercharge this skill:

| Connector | What It Adds |
|-----------|--------------|
| **Calendar** | Today's meetings with attendees, times, and context |
| **CRM** | Open pipeline, deals closing soon, overdue tasks, stale deals |
| **Email** | Unread from opportunity contacts, emails waiting on replies |
| **Enrichment** | Overnight signals: funding, hiring, news on your accounts |

> **No connectors?** No problem. Tell me your meetings and deals, and I'll create your briefing.

---

## Output Format

```markdown
# Daily Briefing | [Day, Month Date]

---

## #1 Priority

**[Most important thing to do today]**
[Why it matters and what to do about it]

---

## Today's Numbers

| Open Pipeline | Closing This Month | Meetings Today | Action Items |
|---------------|-------------------|----------------|--------------|
| $[X] | $[X] | [N] | [N] |

---

## Today's Meetings

### [Time] — [Company] ([Meeting Type])
**Attendees:** [Names]
**Context:** [One-line: deal status, last touch, what's at stake]
**Prep:** [Quick action before this meeting]

### [Time] — [Company] ([Meeting Type])
**Attendees:** [Names]
**Context:** [One-line context]
**Prep:** [Quick action]

*Run `call-prep [company]` for detailed meeting prep*

---

## Pipeline Alerts

### Needs Attention
| Deal | Stage | Amount | Alert | Action |
|------|-------|--------|-------|--------|
| [Deal] | [Stage] | $[X] | [Why flagged] | [What to do] |

### Closing This Week
| Deal | Close Date | Amount | Confidence | Blocker |
|------|------------|--------|------------|---------|
| [Deal] | [Date] | $[X] | [H/M/L] | [If any] |

---

## Email Priorities

### Needs Response
| From | Subject | Received |
|------|---------|----------|
| [Name @ Company] | [Subject] | [Time] |

### Waiting On Reply
| To | Subject | Sent | Days Waiting |
|----|---------|------|--------------|
| [Name @ Company] | [Subject] | [Date] | [N] |

---

## Suggested Actions

1. **[Action]** — [Why now]
2. **[Action]** — [Why now]
3. **[Action]** — [Why now]

---

*Run `call-prep [company]` before your meetings*
*Run `call-follow-up` after each call*
```

---

## Execution Flow

### Step 1: Gather Context

**If connectors available:**
```
1. Calendar → Get today's events
   - Filter to external meetings (non-company attendees)
   - Pull: time, title, attendees, description

2. CRM → Query your pipeline
   - Open opportunities owned by you
   - Flag: closing this week, no activity 7+ days, slipped dates
   - Get: overdue tasks, upcoming tasks

3. Email → Check priority messages
   - Unread from opportunity contact domains
   - Sent messages with no reply (3+ days)

4. Enrichment → Check signals (if available)
   - Funding, hiring, news on open accounts
```

**If no connectors:**
```
Ask user:
1. "What meetings do you have today?"
2. "What deals are you focused on? Any closing soon or needing attention?"
3. "Anything urgent I should know about?"

Work with whatever they provide.
```

### Step 2: Prioritize

```
Priority ranking:
1. URGENT: Deal closing today/tomorrow not yet won
2. HIGH: Meeting today with high-value opportunity
3. HIGH: Unread email from decision-maker
4. MEDIUM: Deal closing this week
5. MEDIUM: Stale deal (7+ days no activity)
6. LOW: Tasks due this week

Select #1 Priority:
- If meeting with >$50K deal today → prep that
- If deal closing today → focus on close
- If urgent email from buyer → respond first
- Else → highest-value stale deal
```

### Step 3: Generate Briefing

```
Assemble sections based on available data:

1. #1 Priority — Always include (even if simple)
2. Today's Numbers — If CRM connected, otherwise skip
3. Today's Meetings — From calendar or user input
4. Pipeline Alerts — If CRM connected
5. Email Priorities — If email connected
6. Suggested Actions — Always include top 3 actions
```

---

## Quick Mode

Say "quick brief" or "tldr my day" for abbreviated version:

```markdown
# Quick Brief | [Date]

**#1:** [Priority action]

**Meetings:** [N] — [Company 1], [Company 2], [Company 3]

**Alerts:**
- [Alert 1]
- [Alert 2]

**Do Now:** [Single most important action]
```

---

## End of Day Mode

Say "wrap up my day" or "end of day summary" after your last meeting:

```markdown
# End of Day | [Date]

**Completed:**
- [Meeting 1] — [Outcome]
- [Meeting 2] — [Outcome]

**Pipeline Changes:**
- [Deal] moved to [Stage]

**Tomorrow's Focus:**
- [Priority 1]
- [Priority 2]

**Open Loops:**
- [ ] [Unfinished item needing follow-up]
```

---

## Tips

1. **Connect your calendar first** — Biggest time saver
2. **Add CRM second** — Unlocks pipeline alerts
3. **Even without connectors** — Just tell me your meetings and I'll help prioritize

---

## Related Skills

- **call-prep** — Deep prep for any specific meeting
- **call-follow-up** — Process notes after calls
- **account-research** — Research a company before first meeting
