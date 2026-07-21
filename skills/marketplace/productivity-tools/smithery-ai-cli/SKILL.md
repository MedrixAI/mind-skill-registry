---
name: smithery-ai-cli
description: Find, connect, and use MCP tools and skills via the Smithery CLI. Use
  when the user searches for new tools or skills, wants to discover integrations,
  connect to an MCP, install a skill, or wants to interact with an external service
  (email, Slack, Discord, GitHub, Jira, Notion, databases, cloud APIs, monitoring,
  etc.).
metadata:
  openclaw:
    requires:
      bins:
      - smithery
    homepage: https://smithery.ai
  mind.id: ai.medrix.skill.smithery-ai-cli
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools"]'
  mind.marketplace-summary: smithery-ai/cli
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Find, connect, and use MCP tools and skills via the Smithery CLI. Use when the user searches for new tools or skills, wants to discover integrations, connect to an MCP, install a skill, or wants to interact with an external service (email, Slack, Discord, GitHub, Jira, Notion, databases, cloud APIs, monitoring, etc.).","starter_prompts":["Help me use smithery ai cli for my task. Start by asking for the goal, inputs, deadline, constraints, and desired output, then complete the workflow.","Apply smithery ai cli to the material I provide, identify missing or inefficient steps, and produce a clearer, more reliable result.","Review my existing approach with smithery ai cli and turn it into a practical checklist or plan with priorities, owners, and validation steps."]},"zh-CN":{"description":"通过 Smithery CLI 查找、连接并使用 MCP 工具和 Skill。适用于发现集成、连接 MCP、安装 Skill，或与各类外部服务交互。","starter_prompts":["请帮我用smithery ai cli完成任务。先询问目标、输入、截止时间、约束和所需输出，然后完成整个流程。","请对我提供的材料应用smithery ai cli，找出缺失或低效步骤，并产出更清晰、更可靠的结果。","请使用smithery ai cli审查我现有的方法，并将其整理为包含优先级、负责人和验证步骤的实用清单或计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/smithery-ai/cli
  mind.upstream.commit: 407ac3b33944a585357379bc213fdf1ee55464d7
  mind.upstream.license: AGPL-3.0-only
  mind.upstream.path: skills/smithery-ai-cli/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://github.com/smithery-ai/cli/blob/407ac3b33944a585357379bc213fdf1ee55464d7/LICENSE",
    "https://raw.githubusercontent.com/smithery-ai/cli/407ac3b33944a585357379bc213fdf1ee55464d7/skills/smithery-ai-cli/SKILL.md"]'
license: AGPL-3.0-only
---

# Smithery

The marketplace for AI agents. Connect to 100K+ tools and skills instantly.

Use `smithery --help` and `<command> --help` for flags, arguments, and full examples.
This skill focuses on concepts and canonical workflows.

## Quick Start

```bash
# 1. Install
npm install -g @smithery/cli

# 2. Authenticate (requires human to confirm in browser)
smithery auth login

# 3. Search for MCP servers
smithery mcp search "github"

# 4. Connect to a server (URL or qualified name both work)
smithery mcp add "https://github.run.tools" --id github

# 5. Browse tools (tree view — drill into groups by passing the prefix)
smithery tool list github
smithery tool list github issues.

# 6. Inspect tool input/output JSON schema
smithery tool get github issues.create

# 7. Call a tool
smithery tool call github issues.create '{"repo": "owner/repo", "title": "Bug"}'
```

## Core Concepts

### [Namespaces](https://smithery.ai/docs/concepts/namespaces.md)

A namespace is the workspace boundary for Smithery resources. Servers, connections, and skills all live in a namespace.
Use one namespace per app/environment (for example, `my-app-dev`, `my-app-prod`), then set it as your active context.
Canonical flow:

```bash
smithery namespace list
smithery namespace create my-app-prod
smithery namespace use my-app-prod
```

For namespace-specific flags and overrides, run `smithery namespace --help` and `smithery mcp --help`.

### [Connect (MCP Connections)](https://smithery.ai/docs/use/connect.md)

A connection is a managed, long-lived MCP session.
Smithery Connect handles OAuth flow, credential storage, token refresh, and session lifecycle.
Connection status model:
- `connected`: ready to list/call tools
- `auth_required`: human must open authorization URL
- `error`: inspect details and retry/fix config

Canonical flow (single user-scoped connection):

```bash
smithery mcp add https://github.run.tools \
  --id user-123-github \
  --metadata '{"userId":"user-123"}'

smithery mcp list --metadata '{"userId":"user-123"}'
smithery tool list user-123-github
```

If CLI shows `auth_required`, tell your human to open the URL and then retry.

### [Token Scoping](https://smithery.ai/docs/use/token-scoping.md)

Service tokens are restricted credentials for browser/mobile/agent usage.
Never pass a full API key to untrusted code.
Policy mental model:
- A token policy is one or more constraints
- In the CLI, pass one JSON object per `--policy` flag
- Fields inside one constraint are AND-ed (more fields = narrower)
- Lists and multiple constraints are OR-ed (more entries = wider)

Canonical user-scoped token:

```bash
smithery auth token --policy '{
  "namespaces": "my-app",
  "resources": "connections",
  "operations": ["read", "execute"],
  "metadata": { "userId": "user-123" },
  "ttl": "1h"
}'
```

### Request-level Tool Restrictions (`rpcReqMatch`, experimental)

Use `rpcReqMatch` to restrict specific MCP JSON-RPC requests (regex by request path).
Important: connection IDs are not in the JSON-RPC body, so combine:
- `metadata` for connection-level restriction
- `rpcReqMatch` for method/tool restriction

Canonical combined restriction:

```bash
smithery auth token --policy '{
  "resources": "connections",
  "operations": "execute",
  "metadata": { "connectionId": "my-github" },
  "rpcReqMatch": {
    "method": "tools/call",
    "params.name": "^issues\\."
  },
  "ttl": "30m"
}'
```

### Piped Output

When output is piped, Smithery commands emit JSONL (one JSON object per line):

```bash
smithery tool list github --flat --limit 1000 | grep label
```
