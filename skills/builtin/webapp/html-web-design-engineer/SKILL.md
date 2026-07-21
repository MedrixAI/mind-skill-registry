---
name: html-web-design-engineer
description: Mindar-adapted web design engineer for polished, source-grounded, interactive single-file HTML web apps.
license: MIT
compatibility: Requires submit_html and read_skill support for bundled style recipes.
allowed-tools:
- knowledge_search
- read_skill
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-web-design-engineer
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: webapp
  mind.tags: '["artifact-template","webapp"]'
  mind.runtime-default: 'true'
  mind.runtime-capabilities: '["webapp:style-recipes"]'
  mind.upstream.repo: https://github.com/ConardLi/garden-skills
  mind.upstream.commit: fbd6453c984e2a150c9553efe3075e1f62338df8
  mind.upstream.path: skills/web-design-engineer/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/ConardLi/garden-skills/fbd6453c984e2a150c9553efe3075e1f62338df8/skills/web-design-engineer/SKILL.md"]'
---
# HTML Web Design Engineer

Use this skill for Studio Web App artifacts: dashboards, explorers, calculators, learning modules, prototypes, and other browser-rendered interactive applications.

This is a Mindar production adaptation inspired by ConardLi/garden-skills `web-design-engineer`. Keep the design-engineering quality bar, but follow Mindar's asynchronous artifact contract.

## Operating Contract

- Produce one complete, self-contained HTML document.
- Finish by calling `submit_html` exactly once.
- Do not wait for user confirmation, create local project files, or split output into multiple files.
- Use the knowledge base, selected full markdown, and `knowledge_search` results as the primary factual source.
- Web search is not available in this artifact worker. If a brand, product, logo, screenshot, metric, or current fact is missing from the sources, use an honest placeholder or omit it. Never fabricate.
- Do not include the full HTML in `final_answer`.

## Mindar HTML Constraints

- Start with `<!DOCTYPE html>` and end with `</html>`.
- External images are forbidden. Use inline SVG, CSS shapes, gradients, tables, charts, or data URIs only when appropriate.
- External fonts are forbidden. Use system stacks such as `"Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", "Segoe UI", Arial, sans-serif`; code uses `Consolas, "SFMono-Regular", ui-monospace, monospace`.
- Allowed external script/style origins are the platform allowlist: `https://cdn.tailwindcss.com`, `https://cdn.jsdelivr.net`, and `https://unpkg.com`.
- Avoid Google Fonts, `@font-face`, relative script URLs, remote background images, and remote `<img>` URLs.

## Internal Workflow

Before writing HTML, silently form a compact design brief:

- Audience and job-to-be-done.
- App type from Studio params: dashboard, learning, explorer, calculator, prototype, or custom.
- Style recipe: if Studio params include `style_recipe`, read exactly one file at `references/style-recipes/<style_recipe>.md` with `read_skill(skill_ref="<当前 Skill 的 canonical skill_ref>", file_path=...)`. Do not read the recipe index or multiple recipe files. Mindar ships the 25 official Garden recipe IDs: `apple-hig`, `muji-kenya-hara`, `aesop`, `dieter-rams-braun`, `monocle-magazine`, `pentagram`, `vignelli-swiss-helvetica`, `bloomberg-terminal`, `tufte-dataink`, `nyt-the-daily`, `linear`, `vercel-mesh`, `raycast`, `notion-pre-ai`, `field-io`, `active-theory`, `resn-storytelling`, `are-na`, `bloomberg-businessweek-turley`, `balenciaga-post-2017`, `mailchimp-freddie`, `stripe-press`, `headspace-meditation`, `y2k-retrofuturism`, and `mid-century-modern`.
- Information architecture: primary views, data groupings, navigation, and source-backed claims.
- Interaction map: filters, tabs, toggles, sliders, search, stepper, drilldown, hover/focus/active states, empty/loading/error states where useful.
- Design system: palette, typography scale, spacing rhythm, radius, border, shadow, motion, and chart language.
- Quality risks: missing data, likely overflow, mobile constraints, chart readability, and unsupported assets.

Then build directly. Checkpoints from the upstream Garden skill become internal self-checks, not user pauses.

## Design Quality Rules

- Make the artifact feel like a real product surface, not a decorated article.
- Avoid generic AI defaults: purple-pink-blue gradient hero backgrounds, endless rounded cards, left-border accent cards, emoji icons, fake testimonials, fake logos, and invented metrics.
- Choose one coherent visual direction and commit to it. Do not mix unrelated design references on the same page.
- Use a controlled palette: one primary accent, two or three neutrals, and at most one warning/success scale when the content requires it.
- Use dense but breathable information layouts for dashboards and operational tools; use editorial rhythm only when the request is learning, narrative, or longform.
- Prefer real controls over decorative labels: tabs for views, segmented controls for modes, toggles for binary options, sliders/inputs for numeric settings, and icon buttons for tools.
- Provide visible interaction feedback: hover, focus, selected, disabled, and active states.
- Keep text within containers at mobile and desktop widths. Prefer wrapping, responsive grids, and stable min/max dimensions over fixed desktop-only layouts.
- Charts must have stable containers, readable labels, and a source-grounded takeaway. If data is insufficient, show clearly labeled placeholder structures instead of fake numbers.

## Recommended Style Mapping

If Studio passes `style_recipe`, use it as the single Garden recipe source of truth. If `style_recipe` is absent, Mindar backend normally infers one from `visual_style`:

- `data_modern`: `bloomberg-terminal` for dense dashboards, otherwise `tufte-dataink`.
- `technical`: `vercel-mesh` for immersive explorers/prototypes, otherwise `linear`.
- `editorial`: `stripe-press` for learning/docs, otherwise `monocle-magazine`.
- `minimal`: `muji-kenya-hara`.
- `playful`: `mailchimp-freddie`.
- `modern`: `linear`.

Translate `visual_style` into a practical design direction:

- `data_modern`: restrained data product, high information density, compact metrics, tables, filters, and chart annotations.
- `technical`: precise developer/tooling UI, strong grid, code or system motifs, compact command-like controls.
- `editorial`: magazine-like learning or narrative module with strong hierarchy and calm reading rhythm.
- `minimal`: quiet utilitarian layout, few colors, high whitespace discipline, crisp borders, no decorative clutter.
- `playful`: approachable product surface with warmer colors, clear affordances, small motion, and friendly but professional copy.
- `modern`: polished product UI with balanced hierarchy, useful controls, and restrained motion.

If Studio params include `custom_visual_style`, treat it as an additional source-aware visual direction layered on top of the single loaded recipe or backend-inferred recipe. Never interpret `custom_visual_style` as a file path.

## Required Web App Features

For interactive Studio Web App requests, include at least three meaningful interactions when the source material supports them, such as:

- Search or filtering.
- Tabs or view switching.
- Expand/collapse detail panels.
- Sortable or selectable table rows.
- Scenario input or slider-driven recalculation.
- Theme/density toggle when it adds value.
- Keyboard-accessible buttons and focus states.

Do not add interactions that merely animate without helping the user understand or manipulate the source content.

## Pre-Submit Self-Check

Before calling `submit_html`, revise against this checklist:

- The page is visibly useful on first paint without relying on delayed JavaScript.
- The app reflects Studio params and selected language.
- Content is grounded in sources or clearly marked as placeholder.
- No external fonts, external images, relative scripts, or non-HTTPS assets.
- Desktop and mobile layouts avoid overlap, clipping, and unreadable chart labels.
- Buttons, tabs, filters, sliders, and toggles have accessible labels and visible focus states.
- The design has a coherent system and avoids generic AI cliches.
- The final response path is `submit_html`, not `final_answer` with HTML.
