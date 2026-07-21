---
name: brand-guidelines
description: Applies Anthropic's official brand colors and typography to any sort
  of artifact that may benefit from having Anthropic's look-and-feel. Use it when
  brand colors or style guidelines, visual formatting, or company design standards
  apply.
license: Complete terms in LICENSE.txt
metadata:
  mind.id: ai.medrix.skill.brand-guidelines
  mind.distribution: marketplace
  mind.market-primary: content-creation
  mind.market-categories: '["content-creation"]'
  mind.marketplace-summary: brand-guidelines
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Applies Anthropic''s official brand colors and typography to any sort of artifact that may benefit from having Anthropic''s look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.","starter_prompts":["Help me create brand guidelines. Start by asking for the audience, purpose, source material, tone, format, and constraints, then produce a polished result.","Use brand guidelines to improve the draft or assets I provide, explain the most important changes, and deliver the revised version.","Create three strong directions for brand guidelines from my brief, compare their tradeoffs, and develop the best option."]},"zh-CN":{"description":"将 Anthropic 官方品牌颜色和字体应用于需要统一品牌观感的各类作品。适用于品牌色、视觉规范、格式设计或企业设计标准相关任务。","starter_prompts":["请帮我完成brand guidelines。先询问受众、目的、素材、语气、格式和约束，然后产出可直接使用的成品。","请用brand guidelines改进我提供的草稿或素材，说明最重要的修改，并交付修订后的版本。","请根据我的简报为brand guidelines提出三个有力方向，比较各自取舍，并完善最佳方案。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/anthropics/skills
  mind.upstream.commit: 9d2f1ae187231d8199c64b5b762e1bdf2244733d
  mind.upstream.path: skills/brand-guidelines/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.license: Apache-2.0
  mind.upstream.evidence-urls: '["https://github.com/anthropics/skills/blob/9d2f1ae187231d8199c64b5b762e1bdf2244733d/skills/brand-guidelines/LICENSE.txt",
    "https://raw.githubusercontent.com/anthropics/skills/9d2f1ae187231d8199c64b5b762e1bdf2244733d/skills/brand-guidelines/SKILL.md"]'
---

# Anthropic Brand Styling

## Overview

To access Anthropic's official brand identity and style resources, use this skill.

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

## Brand Guidelines

### Colors

**Main Colors:**

- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**

- Orange: `#d97757` - Primary accent
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography

- **Headings**: Poppins (with Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- **Note**: Fonts should be pre-installed in your environment for best results

## Features

### Smart Font Application

- Applies Poppins font to headings (24pt and larger)
- Applies Lora font to body text
- Automatically falls back to Arial/Georgia if custom fonts unavailable
- Preserves readability across all systems

### Text Styling

- Headings (24pt+): Poppins font
- Body text: Lora font
- Smart color selection based on background
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use accent colors
- Cycles through orange, blue, and green accents
- Maintains visual interest while staying on-brand

## Technical Details

### Font Management

- Uses system-installed Poppins and Lora fonts when available
- Provides automatic fallback to Arial (headings) and Georgia (body)
- No font installation required - works with existing system fonts
- For best results, pre-install Poppins and Lora fonts in your environment

### Color Application

- Uses RGB color values for precise brand matching
- Applied via python-pptx's RGBColor class
- Maintains color fidelity across different systems
