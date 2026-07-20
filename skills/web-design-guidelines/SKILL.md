---
name: web-design-guidelines
description: Review UI code for Web Interface Guidelines compliance. Use when asked
  to "review my UI", "check accessibility", "audit design", "review UX", or "check
  my site against best practices".
metadata:
  author: vercel
  version: 1.0.0
  argument-hint: <file-or-pattern>
  mind.id: ai.medrix.skill.web-design-guidelines
  mind.distribution: marketplace
  mind.market-primary: content-creation
  mind.market-categories: '["content-creation"]'
  mind.marketplace-summary: web-design-guidelines
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Review UI code for Web Interface Guidelines compliance. Use when asked to \"review my UI\", \"check accessibility\", \"audit design\", \"review UX\", or \"check my site against best practices\".","starter_prompts":["Help me create web design guidelines. Start by asking for the audience, purpose, source material, tone, format, and constraints, then produce a polished result.","Use web design guidelines to improve the draft or assets I provide, explain the most important changes, and deliver the revised version.","Create three strong directions for web design guidelines from my brief, compare their tradeoffs, and develop the best option."]},"zh-CN":{"description":"按照 Web Interface Guidelines 审查 UI 代码。适用于 UI 审查、可访问性检查、设计或 UX 审计以及最佳实践检查。","starter_prompts":["请帮我完成web design guidelines。先询问受众、目的、素材、语气、格式和约束，然后产出可直接使用的成品。","请用web design guidelines改进我提供的草稿或素材，说明最重要的修改，并交付修订后的版本。","请根据我的简报为web design guidelines提出三个有力方向，比较各自取舍，并完善最佳方案。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/vercel-labs/agent-skills
  mind.upstream.commit: f8a72b9603728bb92a217a879b7e62e43ad76c81
  mind.upstream.license: NOASSERTION
  mind.upstream.path: skills/web-design-guidelines/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/vercel-labs/agent-skills/f8a72b9603728bb92a217a879b7e62e43ad76c81/skills/web-design-guidelines/SKILL.md"]'
license: NOASSERTION
---

# Web Interface Guidelines

Review files for compliance with Web Interface Guidelines.

## How It Works

1. Fetch the latest guidelines from the source URL below
2. Read the specified files (or prompt user for files/pattern)
3. Check against all rules in the fetched guidelines
4. Output findings in the terse `file:line` format

## Guidelines Source

Fetch fresh guidelines before each review:

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

Use WebFetch to retrieve the latest rules. The fetched content contains all the rules and output format instructions.

## Usage

When a user provides a file or pattern argument:
1. Fetch guidelines from the source URL above
2. Read the specified files
3. Apply all rules from the fetched guidelines
4. Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.
