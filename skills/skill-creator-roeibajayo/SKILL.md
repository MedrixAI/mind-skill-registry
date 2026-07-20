---
name: skill-creator-roeibajayo
description: Design and create Claude Skills using progressive disclosure principles.
  Use when user request to build new or update skills, or when realizing a new skill
  is needed, based on repeated context or domain expertise.
metadata:
  mind.id: ai.medrix.skill.skill-creator-roeibajayo
  mind.distribution: marketplace
  mind.market-primary: content-creation
  mind.market-categories: '["content-creation", "knowledge-learning"]'
  mind.marketplace-summary: skill-creator (roeibajayo)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Design and create Claude Skills using progressive disclosure principles. Use when user request to build new or update skills, or when realizing a new skill is needed, based on repeated context or domain expertise.","starter_prompts":["Help me create skill creator roeibajayo. Start by asking for the audience, purpose, source material, tone, format, and constraints, then produce a polished result.","Use skill creator roeibajayo to improve the draft or assets I provide, explain the most important changes, and deliver the revised version.","Create three strong directions for skill creator roeibajayo from my brief, compare their tradeoffs, and develop the best option."]},"zh-CN":{"description":"使用渐进式披露原则设计和创建 Claude Skill。适用于用户要求新建或更新 Skill，或从重复上下文和领域知识中识别新 Skill。","starter_prompts":["请帮我完成skill creator roeibajayo。先询问受众、目的、素材、语气、格式和约束，然后产出可直接使用的成品。","请用skill creator roeibajayo改进我提供的草稿或素材，说明最重要的修改，并交付修订后的版本。","请根据我的简报为skill creator roeibajayo提出三个有力方向，比较各自取舍，并完善最佳方案。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/roeibajayo/polygent-tools
  mind.upstream.commit: 77e9813d4ee8d88028f461d4fce479cb1b2f8f55
  mind.upstream.license: NOASSERTION
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.path: .claude/skills/skill-creator/SKILL.md
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/roeibajayo/polygent-tools/77e9813d4ee8d88028f461d4fce479cb1b2f8f55/.claude/skills/skill-creator/SKILL.md"]'
license: NOASSERTION
---

# Skill Creator

Principles and patterns for designing effective Claude Skills.

## Quick Start

Creating a minimal skill:

1. Create directory: `.claude/skills/my-skill/`
2. Create `SKILL.md` with frontmatter (name, description) and body
3. Test in conversation
4. Add references/ as content grows

## When to Create a Skill

Create a skill when you notice:

- **Repeating context** across conversations (same schema, patterns, rules)
- **Domain expertise** needed repeatedly (API integration, framework conventions)
- **Project-specific knowledge** that Claude should know automatically

Example: "I keep explaining this database schema" → Create a database-schema skill.

## Skill Architecture

Skills are directories with this structure:

```
my-skill/
├── SKILL.md          # Required: Instructions + metadata
├── references/       # Optional: Detailed documentation
├── scripts/          # Optional: Executable operations
└── assets/           # Optional: Templates, images, files
```

**SKILL.md** - Core instructions with YAML frontmatter (name, description) + markdown body

**references/** - Detailed docs loaded only when Claude needs them (schemas, API docs, guides)

**scripts/** - Deterministic operations Claude can execute without generating code (validation, generation)

**assets/** - Files used directly in output without loading into context (templates, images)

## Progressive Disclosure

Skills load in 3 levels:

**Level 1: Metadata** (~100 tokens, always loaded) - YAML frontmatter determines skill triggering

**Level 2: Instructions** (<5k tokens, when triggered) - SKILL.md body with core patterns and links

**Level 3: Resources** (unlimited, as needed) - references/ scripts/ assets/ loaded only when used

**Key principle**: Keep Levels 1 & 2 lean. Move details to Level 3.

## Development Process

1. **Recognize** - Notice repeated context or domain needs
2. **Gather** - Collect 3-5 concrete examples of skill usage
3. **Plan** - Decide what goes in SKILL.md vs references/ vs scripts/
4. **Structure** - Create directory with SKILL.md and needed subdirectories
5. **Write** - Craft description, then SKILL.md body following patterns
6. **Enhance** - Add references, scripts, assets as needed
7. **Iterate** - Test in conversations, refine based on actual usage

## Writing Effective Content

**Descriptions**: Include "Use when..." triggers, <200 chars optimal.
Format: [Domain] + [Operations] + [Trigger keywords]

**SKILL.md Body**: Target ~50 lines, max ~150. Structure: Quick Start + Core Patterns (3-5) + Links. Use imperative voice, concrete examples.

**References**: Detailed docs with no size limit. Use descriptive filenames.

## Common Patterns

**Succeeds**: Domain expertise, concrete examples, keyword-rich descriptions, clear triggers, scripts for deterministic tasks

**Fails**: Generic descriptions, bloated SKILL.md, second person voice, missing triggers, vague content

See [skill-examples.md](references/skill-examples.md) for detailed patterns.

## Reference Documentation

For detailed guidance:

- [anthropic-resources.md](references/anthropic-resources.md) - Official Anthropic best practices
- [writing-guide.md](references/writing-guide.md) - Voice, structure, and code examples

## Notes

- Skills are iterative - start minimal, refine through real usage
- Description drives discovery - invest time in crafting it
- Test in actual conversations to validate effectiveness
- Progressive disclosure is key - resist urge to front-load everything
