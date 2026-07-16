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
