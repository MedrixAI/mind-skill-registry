---
name: skill-discovery
description: Discover agent skills on GitHub. Use when user asks to find new skills,
  search for skills, explore skill repositories, or wants to see trending/popular
  skills.
metadata:
  mind.id: ai.medrix.skill.skill-discovery
  mind.distribution: marketplace
  mind.market-primary: general
  mind.market-categories: '["general"]'
  mind.marketplace-summary: skill-discovery
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Discover agent skills on GitHub. Use when user asks to find new skills, search for skills, explore skill repositories, or wants to see trending/popular skills.","starter_prompts":["Help me with skill discovery. Start by asking for the goal, relevant files or context, constraints, and desired output, then complete the workflow.","Apply skill discovery to the material I provide, explain the key findings or changes, and produce a polished result I can use directly.","Review my current work with skill discovery, identify gaps and risks, and return an improved version with clear next steps."]},"zh-CN":{"description":"在 GitHub 上发现 Agent Skill。适用于查找新 Skill、搜索 Skill、浏览 Skill 仓库，或查看热门和流行 Skill。","starter_prompts":["请帮我完成skill discovery。先询问目标、相关文件或上下文、约束和所需输出，然后完成整个流程。","请对我提供的材料应用skill discovery，说明关键发现或修改，并产出可直接使用的结果。","请使用skill discovery审查我当前的成果，识别缺口和风险，并返回改进版本及明确的后续步骤。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/dejanr/dotfiles
  mind.upstream.commit: c1164c1b0da9a7100d7d64a653285fc3b4c616e1
  mind.upstream.license: NOASSERTION
  mind.upstream.path: modules/home/cli/pi-mono/skills/skill-discovery/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/dejanr/dotfiles/c1164c1b0da9a7100d7d64a653285fc3b4c616e1/modules/home/cli/pi-mono/skills/skill-discovery/SKILL.md"]'
license: NOASSERTION
---

# Skill Discovery

Find agent skills on GitHub using `gh` CLI. Skills work across multiple harnesses (Claude Code, Codex, Gemini CLI, Pi, etc.) as they follow the same SKILL.md format.

## Workflow

1. Search repos by topic to find skill collections
2. For awesome lists: fetch README and extract skill links
3. For skill repos: list directories containing SKILL.md
4. Build searchable catalog at `/tmp/skills-catalog.md`
5. Search/filter based on user query

## Find skill repos

```bash
gh search repos --topic=claude-skills --sort=stars --limit=30 --json fullName,description
gh search repos --topic=codex-skills --sort=stars --limit=20 --json fullName,description
gh search repos --topic=gemini-skills --sort=stars --limit=20 --json fullName,description
gh search repos --topic=skill-md --sort=stars --limit=20 --json fullName,description
gh search repos --topic=agent-skills --sort=stars --limit=20 --json fullName,description
gh search repos --topic=claude-code-skills --sort=stars --limit=20 --json fullName,description
gh search repos --topic=gemini-cli-skills --sort=stars --limit=20 --json fullName,description
```

## Find repos with SKILL.md files

Search GitHub code for actual SKILL.md files (finds repos not tagged with topics):

```bash
# Find repos containing SKILL.md files, then fetch stars via GraphQL (single query)
repos=$(gh search code "filename:SKILL.md" --limit=50 --json repository | jq -r '.[].repository.nameWithOwner' | sort -u)

# Build GraphQL query to get stars for all repos at once
query="{ "
i=0
for repo in $repos; do
  owner="${repo%/*}"
  name="${repo#*/}"
  query+="r$i: repository(owner: \"$owner\", name: \"$name\") { nameWithOwner stargazerCount description } "
  ((i++))
done
query+="}"

gh api graphql -f query="$query" --jq '.data | to_entries[] | "\(.value.nameWithOwner) ★\(.value.stargazerCount) - \(.value.description // "no desc")"' | sort -t'★' -k2 -rn
```

## Build catalog from awesome lists

For repos with "awesome" in name, fetch README:

```bash
gh api "repos/<owner>/<repo>/contents/README.md" --jq '.content' | base64 -d >> /tmp/skills-catalog.md
```

## List skills in a collection repo

For repos with skills directories:

```bash
# Find skills directory (skills/, scientific-skills/, etc.)
gh api repos/<owner>/<repo>/contents --jq '.[].name'

# List individual skills
gh api repos/<owner>/<repo>/contents/<skills-dir> --jq '.[].name'
```

## Search catalog

```bash
grep -i "<keyword>" /tmp/skills-catalog.md -B2 -A1
```

## View skill contents

```bash
gh api repos/<owner>/<repo>/contents/<path>/SKILL.md --jq '.content' | base64 -d
```

## Install skill

Skills are managed via Nix — `~/.pi/agent/skills/` is a read-only Nix store symlink.
Install into the dotfiles source, then rebuild to activate.

```bash
gh repo clone <owner>/<repo> /tmp/<repo>
cp -r /tmp/<repo>/skills/<skill-name> ~/.dotfiles/modules/home/cli/pi-mono/skills/
```

After copying, remind the user to rebuild (`sudo nixos-rebuild switch --flake ~/.dotfiles#` or `nix run nix-darwin -- switch --flake ~/.dotfiles#`) to activate the new skill.

## Output

Show matching skills as table: | Repository | Description |

After results, offer:

1. View a specific skill's SKILL.md
2. Install a skill to `~/.pi/agent/skills/`
3. Search for different keywords
