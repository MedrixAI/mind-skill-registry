---
name: web-artifacts-builder
description: Suite of tools for creating elaborate, multi-component claude.ai HTML
  artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui).
  Use for complex artifacts requiring state management, routing, or shadcn/ui components
  - not for simple single-file HTML/JSX artifacts.
license: Apache-2.0
metadata:
  mind.id: ai.medrix.skill.web-artifacts-builder
  mind.distribution: marketplace
  mind.market-primary: development-tools
  mind.market-categories: '["development-tools"]'
  mind.marketplace-summary: web-artifacts-builder
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.","starter_prompts":["Help me with web artifacts builder. Start by asking for the repository or system context, environment, constraints, and acceptance criteria, then implement or configure the solution.","Use web artifacts builder to diagnose the issue I provide, identify the root cause, make the smallest safe fix, and explain how to verify it.","Review my current web artifacts builder approach for correctness, security, and maintainability, then return prioritized improvements and validation steps."]},"zh-CN":{"description":"使用 React、Tailwind CSS 和 shadcn/ui 创建复杂的多组件 HTML Artifact。适用于需要状态管理、路由或组件库的复杂作品。","starter_prompts":["请帮我完成web artifacts builder。先询问仓库或系统上下文、运行环境、约束和验收标准，然后实施或配置解决方案。","请使用web artifacts builder诊断我提供的问题，定位根因，完成最小且安全的修复，并说明如何验证。","请从正确性、安全性和可维护性角度审查我当前的web artifacts builder方案，并给出按优先级排序的改进和验证步骤。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/anthropics/skills
  mind.upstream.commit: 9d2f1ae187231d8199c64b5b762e1bdf2244733d
  mind.upstream.license: Apache-2.0
  mind.upstream.path: skills/web-artifacts-builder/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://github.com/anthropics/skills/blob/9d2f1ae187231d8199c64b5b762e1bdf2244733d/skills/web-artifacts-builder/LICENSE.txt",
    "https://raw.githubusercontent.com/anthropics/skills/9d2f1ae187231d8199c64b5b762e1bdf2244733d/skills/web-artifacts-builder/SKILL.md"]'
---

# Web Artifacts Builder

To build powerful frontend claude.ai artifacts, follow these steps:
1. Initialize the frontend repo using `scripts/init-artifact.sh`
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file using `scripts/bundle-artifact.sh`
4. Display artifact to user
5. (Optional) Test the artifact

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design & Style Guidelines

VERY IMPORTANT: To avoid what is often referred to as "AI slop", avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

This creates a fully configured project with:
- ✅ React + TypeScript (via Vite)
- ✅ Tailwind CSS 3.4.1 with shadcn/ui theming system
- ✅ Path aliases (`@/`) configured
- ✅ 40+ shadcn/ui components pre-installed
- ✅ All Radix UI dependencies included
- ✅ Parcel configured for bundling (via .parcelrc)
- ✅ Node 18+ compatibility (auto-detects and pins Vite version)

### Step 2: Develop Your Artifact

To build the artifact, edit the generated files. See **Common Development Tasks** below for guidance.

### Step 3: Bundle to Single HTML File

To bundle the React app into a single HTML artifact:
```bash
bash scripts/bundle-artifact.sh
```

This creates `bundle.html` - a self-contained artifact with all JavaScript, CSS, and dependencies inlined. This file can be directly shared in Claude conversations as an artifact.

**Requirements**: Your project must have an `index.html` in the root directory.

**What the script does**:
- Installs bundling dependencies (parcel, @parcel/config-default, parcel-resolver-tspaths, html-inline)
- Creates `.parcelrc` config with path alias support
- Builds with Parcel (no source maps)
- Inlines all assets into single HTML using html-inline

### Step 4: Share Artifact with User

Finally, share the bundled HTML file in conversation with the user so they can view it as an artifact.

### Step 5: Testing/Visualizing the Artifact (Optional)

Note: This is a completely optional step. Only perform if necessary or requested.

To test/visualize the artifact, use available tools (including other Skills or built-in tools like Playwright or Puppeteer). In general, avoid testing the artifact upfront as it adds latency between the request and when the finished artifact can be seen. Test later, after presenting the artifact, if requested or if issues arise.

## Reference

- **shadcn/ui components**: https://ui.shadcn.com/docs/components