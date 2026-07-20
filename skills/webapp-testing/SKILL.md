---
name: webapp-testing
description: Toolkit for interacting with and testing local web applications using
  Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing
  browser screenshots, and viewing browser logs.
license: Apache-2.0
metadata:
  mind.id: ai.medrix.skill.webapp-testing
  mind.distribution: marketplace
  mind.market-primary: development-tools
  mind.market-categories: '["development-tools"]'
  mind.marketplace-summary: webapp-testing
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.","starter_prompts":["Help me with webapp testing. Start by asking for the repository or system context, environment, constraints, and acceptance criteria, then implement or configure the solution.","Use webapp testing to diagnose the issue I provide, identify the root cause, make the smallest safe fix, and explain how to verify it.","Review my current webapp testing approach for correctness, security, and maintainability, then return prioritized improvements and validation steps."]},"zh-CN":{"description":"使用 Playwright 与本地 Web 应用交互和测试，支持验证前端功能、调试 UI 行为、截图和查看浏览器日志。","starter_prompts":["请帮我完成webapp testing。先询问仓库或系统上下文、运行环境、约束和验收标准，然后实施或配置解决方案。","请使用webapp testing诊断我提供的问题，定位根因，完成最小且安全的修复，并说明如何验证。","请从正确性、安全性和可维护性角度审查我当前的webapp testing方案，并给出按优先级排序的改进和验证步骤。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/anthropics/skills
  mind.upstream.commit: 9d2f1ae187231d8199c64b5b762e1bdf2244733d
  mind.upstream.license: Apache-2.0
  mind.upstream.path: skills/webapp-testing/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://github.com/anthropics/skills/blob/9d2f1ae187231d8199c64b5b762e1bdf2244733d/skills/webapp-testing/LICENSE.txt",
    "https://raw.githubusercontent.com/anthropics/skills/9d2f1ae187231d8199c64b5b762e1bdf2244733d/skills/webapp-testing/SKILL.md"]'
---

# Web Application Testing

To test local web applications, write native Python Playwright scripts.

**Helper Scripts Available**:
- `scripts/with_server.py` - Manages server lifecycle (supports multiple servers)

**Always run scripts with `--help` first** to see usage. DO NOT read the source until you try running the script first and find that a customized solution is abslutely necessary. These scripts can be very large and thus pollute your context window. They exist to be called directly as black-box scripts rather than ingested into your context window.

## Decision Tree: Choosing Your Approach

```
User task → Is it static HTML?
    ├─ Yes → Read HTML file directly to identify selectors
    │         ├─ Success → Write Playwright script using selectors
    │         └─ Fails/Incomplete → Treat as dynamic (below)
    │
    └─ No (dynamic webapp) → Is the server already running?
        ├─ No → Run: python scripts/with_server.py --help
        │        Then use the helper + write simplified Playwright script
        │
        └─ Yes → Reconnaissance-then-action:
            1. Navigate and wait for networkidle
            2. Take screenshot or inspect DOM
            3. Identify selectors from rendered state
            4. Execute actions with discovered selectors
```

## Example: Using with_server.py

To start a server, run `--help` first, then use the helper:

**Single server:**
```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

**Multiple servers (e.g., backend + frontend):**
```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_automation.py
```

To create an automation script, include only Playwright logic (servers are managed automatically):
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True) # Always launch chromium in headless mode
    page = browser.new_page()
    page.goto('http://localhost:5173') # Server already running and ready
    page.wait_for_load_state('networkidle') # CRITICAL: Wait for JS to execute
    # ... your automation logic
    browser.close()
```

## Reconnaissance-Then-Action Pattern

1. **Inspect rendered DOM**:
   ```python
   page.screenshot(path='/tmp/inspect.png', full_page=True)
   content = page.content()
   page.locator('button').all()
   ```

2. **Identify selectors** from inspection results

3. **Execute actions** using discovered selectors

## Common Pitfall

❌ **Don't** inspect the DOM before waiting for `networkidle` on dynamic apps
✅ **Do** wait for `page.wait_for_load_state('networkidle')` before inspection

## Best Practices

- **Use bundled scripts as black boxes** - To accomplish a task, consider whether one of the scripts available in `scripts/` can help. These scripts handle common, complex workflows reliably without cluttering the context window. Use `--help` to see usage, then invoke directly. 
- Use `sync_playwright()` for synchronous scripts
- Always close the browser when done
- Use descriptive selectors: `text=`, `role=`, CSS selectors, or IDs
- Add appropriate waits: `page.wait_for_selector()` or `page.wait_for_timeout()`

## Reference Files

- **examples/** - Examples showing common patterns:
  - `element_discovery.py` - Discovering buttons, links, and inputs on a page
  - `static_html_automation.py` - Using file:// URLs for local HTML
  - `console_logging.py` - Capturing console logs during automation