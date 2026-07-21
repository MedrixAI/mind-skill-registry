---
name: theme-factory
description: Toolkit for styling artifacts with a theme. These artifacts can be slides,
  docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts
  that you can apply to any artifact that has been creating, or can generate a new
  theme on-the-fly.
license: Complete terms in LICENSE.txt
metadata:
  mind.id: ai.medrix.skill.theme-factory
  mind.distribution: marketplace
  mind.market-primary: content-creation
  mind.market-categories: '["content-creation"]'
  mind.marketplace-summary: theme-factory
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.","starter_prompts":["Help me create theme factory. Start by asking for the audience, purpose, source material, tone, format, and constraints, then produce a polished result.","Use theme factory to improve the draft or assets I provide, explain the most important changes, and deliver the revised version.","Create three strong directions for theme factory from my brief, compare their tradeoffs, and develop the best option."]},"zh-CN":{"description":"为幻灯片、文档、报告和 HTML 落地页等作品应用主题样式。提供预设颜色和字体，也可即时生成新主题。","starter_prompts":["请帮我完成theme factory。先询问受众、目的、素材、语气、格式和约束，然后产出可直接使用的成品。","请用theme factory改进我提供的草稿或素材，说明最重要的修改，并交付修订后的版本。","请根据我的简报为theme factory提出三个有力方向，比较各自取舍，并完善最佳方案。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/anthropics/skills
  mind.upstream.commit: 9d2f1ae187231d8199c64b5b762e1bdf2244733d
  mind.upstream.path: skills/theme-factory/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.license: Apache-2.0
  mind.upstream.evidence-urls: '["https://github.com/anthropics/skills/blob/9d2f1ae187231d8199c64b5b762e1bdf2244733d/skills/theme-factory/LICENSE.txt",
    "https://raw.githubusercontent.com/anthropics/skills/9d2f1ae187231d8199c64b5b762e1bdf2244733d/skills/theme-factory/SKILL.md"]'
---

# Theme Factory Skill

This skill provides a curated collection of professional font and color themes themes, each with carefully selected color palettes and font pairings. Once a theme is chosen, it can be applied to any artifact.

## Purpose

To apply consistent, professional styling to presentation slide decks, use this skill. Each theme includes:
- A cohesive color palette with hex codes
- Complementary font pairings for headers and body text
- A distinct visual identity suitable for different contexts and audiences

## Usage Instructions

To apply styling to a slide deck or other artifact:

1. **Show the theme showcase**: Display the `theme-showcase.pdf` file to allow users to see all available themes visually. Do not make any modifications to it; simply show the file for viewing.
2. **Ask for their choice**: Ask which theme to apply to the deck
3. **Wait for selection**: Get explicit confirmation about the chosen theme
4. **Apply the theme**: Once a theme has been chosen, apply the selected theme's colors and fonts to the deck/artifact

## Themes Available

The following 10 themes are available, each showcased in `theme-showcase.pdf`:

1. **Ocean Depths** - Professional and calming maritime theme
2. **Sunset Boulevard** - Warm and vibrant sunset colors
3. **Forest Canopy** - Natural and grounded earth tones
4. **Modern Minimalist** - Clean and contemporary grayscale
5. **Golden Hour** - Rich and warm autumnal palette
6. **Arctic Frost** - Cool and crisp winter-inspired theme
7. **Desert Rose** - Soft and sophisticated dusty tones
8. **Tech Innovation** - Bold and modern tech aesthetic
9. **Botanical Garden** - Fresh and organic garden colors
10. **Midnight Galaxy** - Dramatic and cosmic deep tones

## Theme Details

Each theme is defined in the `themes/` directory with complete specifications including:
- Cohesive color palette with hex codes
- Complementary font pairings for headers and body text
- Distinct visual identity suitable for different contexts and audiences

## Application Process

After a preferred theme is selected:
1. Read the corresponding theme file from the `themes/` directory
2. Apply the specified colors and fonts consistently throughout the deck
3. Ensure proper contrast and readability
4. Maintain the theme's visual identity across all slides

## Create your Own Theme
To handle cases where none of the existing themes work for an artifact, create a custom theme. Based on provided inputs, generate a new theme similar to the ones above. Give the theme a similar name describing what the font/color combinations represent. Use any basic description provided to choose appropriate colors/fonts. After generating the theme, show it for review and verification. Following that, apply the theme as described above.
