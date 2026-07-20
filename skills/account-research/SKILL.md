---
name: account-research
description: Research a company or person and get actionable sales intel. Works standalone
  with web search, supercharged when you connect enrichment tools or your CRM. Trigger
  with "research [company]", "look up [person]", "intel on [prospect]", "who is [name]
  at [company]", or "tell me about [company]".
metadata:
  mind.id: ai.medrix.skill.account-research
  mind.distribution: marketplace
  mind.market-primary: business-operations
  mind.market-categories: '["business-operations"]'
  mind.marketplace-summary: account-research (anthropics)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Research a company or person and get actionable sales intel. Works standalone with web search, supercharged when you connect enrichment tools or your CRM. Trigger with \"research [company]\", \"look up [person]\", \"intel on [prospect]\", \"who is [name] at [company]\", or \"tell me about [company]\".","starter_prompts":["Help me with account research. Start by asking for the business goal, stakeholders, available inputs, constraints, and desired decision or deliverable, then complete the workflow.","Apply account research to the material I provide, identify the most important findings, risks, and evidence gaps, and produce a decision-ready result.","Review my existing account research work, correct weak assumptions or missing details, and return an improved version with clear next actions."]},"zh-CN":{"description":"研究公司或个人并获得可执行的销售情报。可独立结合网页搜索使用，连接企业信息增强工具或 CRM 后效果更佳。适用于公司研究、联系人查询和潜在客户情报。","starter_prompts":["请帮我完成account research。先询问业务目标、利益相关者、现有输入、约束以及需要支持的决策或交付物，然后完成整个流程。","请对我提供的材料开展account research，找出最重要的发现、风险和证据缺口，并输出可用于决策的结果。","请审查我现有的account research成果，修正薄弱假设和遗漏细节，并给出改进版本及明确的后续行动。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/anthropics/knowledge-work-plugins
  mind.upstream.commit: 47caa757e4730eb8daf7d335470f692d4a68b59e
  mind.upstream.path: sales/skills/account-research/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.license: Apache-2.0
  mind.upstream.evidence-urls: '["https://github.com/anthropics/knowledge-work-plugins/blob/47caa757e4730eb8daf7d335470f692d4a68b59e/LICENSE",
    "https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/47caa757e4730eb8daf7d335470f692d4a68b59e/sales/skills/account-research/SKILL.md"]'
license: Apache-2.0
---

# Account Research

Get a complete picture of any company or person before outreach. This skill always works with web search, and gets significantly better with enrichment and CRM data.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     ACCOUNT RESEARCH                             │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone via web search)                        │
│  ✓ Company overview: what they do, size, industry               │
│  ✓ Recent news: funding, leadership changes, announcements      │
│  ✓ Hiring signals: open roles, growth indicators                │
│  ✓ Key people: leadership team from LinkedIn                    │
│  ✓ Product/service: what they sell, who they serve              │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                      │
│  + Enrichment: verified emails, phone, tech stack, org chart    │
│  + CRM: prior relationship, past opportunities, contacts        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Getting Started

Just tell me who to research:

- "Research Stripe"
- "Look up the CTO at Notion"
- "Intel on acme.com"
- "Who is Sarah Chen at TechCorp?"
- "Tell me about [company] before my call"

I'll run web searches immediately. If you have enrichment or CRM connected, I'll pull that data too.

---

## Connectors (Optional)

Connect your tools to supercharge this skill:

| Connector | What It Adds |
|-----------|--------------|
| **Enrichment** | Verified emails, phone numbers, tech stack, org chart, funding details |
| **CRM** | Prior relationship history, past opportunities, existing contacts, notes |

> **No connectors?** No problem. Web search provides solid research for any company or person.

---

## Output Format

```markdown
# Research: [Company or Person Name]

**Generated:** [Date]
**Sources:** Web Search [+ Enrichment] [+ CRM]

---

## Quick Take

[2-3 sentences: Who they are, why they might need you, best angle for outreach]

---

## Company Profile

| Field | Value |
|-------|-------|
| **Company** | [Name] |
| **Website** | [URL] |
| **Industry** | [Industry] |
| **Size** | [Employee count] |
| **Headquarters** | [Location] |
| **Founded** | [Year] |
| **Funding** | [Stage + amount if known] |
| **Revenue** | [Estimate if available] |

### What They Do
[1-2 sentence description of their business, product, and customers]

### Recent News
- **[Headline]** — [Date] — [Why it matters for your outreach]
- **[Headline]** — [Date] — [Why it matters]

### Hiring Signals
- [X] open roles in [Department]
- Notable: [Relevant roles like Engineering, Sales, AI/ML]
- Growth indicator: [Hiring velocity interpretation]

---

## Key People

### [Name] — [Title]
| Field | Detail |
|-------|--------|
| **LinkedIn** | [URL] |
| **Background** | [Prior companies, education] |
| **Tenure** | [Time at company] |
| **Email** | [If enrichment connected] |

**Talking Points:**
- [Personal hook based on background]
- [Professional hook based on role]

[Repeat for relevant contacts]

---

## Tech Stack [If Enrichment Connected]

| Category | Tools |
|----------|-------|
| **Cloud** | [AWS, GCP, Azure, etc.] |
| **Data** | [Snowflake, Databricks, etc.] |
| **CRM** | [e.g. Salesforce, HubSpot] |
| **Other** | [Relevant tools] |

**Integration Opportunity:** [How your product fits with their stack]

---

## Prior Relationship [If CRM Connected]

| Field | Detail |
|-------|--------|
| **Status** | [New / Prior prospect / Customer / Churned] |
| **Last Contact** | [Date and type] |
| **Previous Opps** | [Won/Lost and why] |
| **Known Contacts** | [Names already in CRM] |

**History:** [Summary of past relationship]

---

## Qualification Signals

### Positive Signals
- ✅ [Signal and evidence]
- ✅ [Signal and evidence]

### Potential Concerns
- ⚠️ [Concern and what to watch for]

### Unknown (Ask in Discovery)
- ❓ [Gap in understanding]

---

## Recommended Approach

**Best Entry Point:** [Person and why]

**Opening Hook:** [What to lead with based on research]

**Discovery Questions:**
1. [Question about their situation]
2. [Question about pain points]
3. [Question about decision process]

---

## Sources
- [Source 1](URL)
- [Source 2](URL)
```

---

## Execution Flow

### Step 1: Parse Request

```
Identify what to research:
- "Research Stripe" → Company research
- "Look up John Smith at Acme" → Person + company
- "Who is the CTO at Notion" → Role-based search
- "Intel on acme.com" → Domain-based lookup
```

### Step 2: Web Search (Always)

```
Run these searches:
1. "[Company name]" → Homepage, about page
2. "[Company name] news" → Recent announcements
3. "[Company name] funding" → Investment history
4. "[Company name] careers" → Hiring signals
5. "[Person name] [Company] LinkedIn" → Profile info
6. "[Company name] product" → What they sell
7. "[Company name] customers" → Who they serve
```

**Extract:**
- Company description and positioning
- Recent news (last 90 days)
- Leadership team
- Open job postings
- Technology mentions
- Customer base

### Step 3: Enrichment (If Connected)

```
If enrichment tools available:
1. Enrich company → Firmographics, funding, tech stack
2. Search people → Org chart, contact list
3. Enrich person → Email, phone, background
4. Get signals → Intent data, hiring velocity
```

**Enrichment adds:**
- Verified contact info
- Complete org chart
- Precise employee count
- Detailed tech stack
- Funding history with investors

### Step 4: CRM Check (If Connected)

```
If CRM available:
1. Search for account by domain
2. Get related contacts
3. Get opportunity history
4. Get activity timeline
```

**CRM adds:**
- Prior relationship context
- What happened before (won/lost deals)
- Who we've talked to
- Notes and history

### Step 5: Synthesize

```
1. Combine all sources
2. Prioritize enrichment data over web (more accurate)
3. Add CRM context if exists
4. Identify qualification signals
5. Generate talking points
6. Recommend approach
```

---

## Research Variations

### Company Research
Focus on: Business overview, news, hiring, leadership

### Person Research
Focus on: Background, role, LinkedIn activity, talking points

### Competitor Research
Focus on: Product comparison, positioning, win/loss patterns

### Pre-Meeting Research
Focus on: Attendee backgrounds, recent news, relationship history

---

## Tips for Better Research

1. **Include the domain** — "research acme.com" is more precise
2. **Specify the person** — "look up Jane Smith, VP Sales at Acme"
3. **State your goal** — "research Stripe before my demo call"
4. **Ask for specifics** — "what's their tech stack?" after initial research

---

## Related Skills

- **call-prep** — Full meeting prep with this research plus context
- **draft-outreach** — Write personalized message based on research
- **prospecting** — Qualify and prioritize research targets
