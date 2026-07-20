---
name: applying-brand-guidelines
description: This skill applies consistent corporate branding and styling to all generated
  documents including colors, fonts, layouts, and messaging
metadata:
  mind.id: ai.medrix.skill.applying-brand-guidelines
  mind.distribution: marketplace
  mind.market-primary: business-operations
  mind.market-categories: '["business-operations"]'
  mind.marketplace-summary: applying-brand-guidelines (anthropics)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"This skill applies consistent corporate branding and styling to all generated documents including colors, fonts, layouts, and messaging","starter_prompts":["Help me with applying brand guidelines. Start by asking for the business goal, stakeholders, available inputs, constraints, and desired decision or deliverable, then complete the workflow.","Apply applying brand guidelines to the material I provide, identify the most important findings, risks, and evidence gaps, and produce a decision-ready result.","Review my existing applying brand guidelines work, correct weak assumptions or missing details, and return an improved version with clear next actions."]},"zh-CN":{"description":"为生成的文档统一应用企业品牌规范，包括颜色、字体、版式和信息表达。","starter_prompts":["请帮我完成applying brand guidelines。先询问业务目标、利益相关者、现有输入、约束以及需要支持的决策或交付物，然后完成整个流程。","请对我提供的材料开展applying brand guidelines，找出最重要的发现、风险和证据缺口，并输出可用于决策的结果。","请审查我现有的applying brand guidelines成果，修正薄弱假设和遗漏细节，并给出改进版本及明确的后续行动。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/anthropics/claude-cookbooks
  mind.upstream.commit: 67ce644d33e5933f0bcc0b6eb4113df41bbf3a8f
  mind.upstream.license: MIT
  mind.upstream.path: skills/custom_skills/applying-brand-guidelines/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://github.com/anthropics/claude-cookbooks/blob/67ce644d33e5933f0bcc0b6eb4113df41bbf3a8f/LICENSE",
    "https://raw.githubusercontent.com/anthropics/claude-cookbooks/67ce644d33e5933f0bcc0b6eb4113df41bbf3a8f/skills/custom_skills/applying-brand-guidelines/SKILL.md"]'
license: MIT
---

# Corporate Brand Guidelines Skill

This skill ensures all generated documents adhere to corporate brand standards for consistent, professional communication.

## Brand Identity

### Company: Acme Corporation
**Tagline**: "Innovation Through Excellence"
**Industry**: Technology Solutions

## Visual Standards

### Color Palette

**Primary Colors**:
- **Acme Blue**: #0066CC (RGB: 0, 102, 204) - Headers, primary buttons
- **Acme Navy**: #003366 (RGB: 0, 51, 102) - Text, accents
- **White**: #FFFFFF - Backgrounds, reverse text

**Secondary Colors**:
- **Success Green**: #28A745 (RGB: 40, 167, 69) - Positive metrics
- **Warning Amber**: #FFC107 (RGB: 255, 193, 7) - Cautions
- **Error Red**: #DC3545 (RGB: 220, 53, 69) - Negative values
- **Neutral Gray**: #6C757D (RGB: 108, 117, 125) - Secondary text

### Typography

**Primary Font Family**: Segoe UI, system-ui, -apple-system, sans-serif

**Font Hierarchy**:
- **H1**: 32pt, Bold, Acme Blue
- **H2**: 24pt, Semibold, Acme Navy
- **H3**: 18pt, Semibold, Acme Navy
- **Body**: 11pt, Regular, Acme Navy
- **Caption**: 9pt, Regular, Neutral Gray

### Logo Usage

- Position: Top-left corner on first page/slide
- Size: 120px width (maintain aspect ratio)
- Clear space: Minimum 20px padding on all sides
- Never distort, rotate, or apply effects

## Document Standards

### PowerPoint Presentations

**Slide Templates**:
1. **Title Slide**: Company logo, presentation title, date, presenter
2. **Section Divider**: Section title with blue background
3. **Content Slide**: Title bar with blue background, white content area
4. **Data Slide**: For charts/graphs, maintain color palette

**Layout Rules**:
- Margins: 0.5 inches all sides
- Title position: Top 15% of slide
- Bullet indentation: 0.25 inches per level
- Maximum 6 bullet points per slide
- Charts use brand colors exclusively

### Excel Spreadsheets

**Formatting Standards**:
- **Headers**: Row 1, Bold, White text on Acme Blue background
- **Subheaders**: Bold, Acme Navy text
- **Data cells**: Regular, Acme Navy text
- **Borders**: Thin, Neutral Gray
- **Alternating rows**: Light gray (#F8F9FA) for readability

**Chart Defaults**:
- Primary series: Acme Blue
- Secondary series: Success Green
- Gridlines: Neutral Gray, 0.5pt
- No 3D effects or gradients

### PDF Documents

**Page Layout**:
- **Header**: Company logo left, document title center, page number right
- **Footer**: Copyright notice left, date center, classification right
- **Margins**: 1 inch all sides
- **Line spacing**: 1.15
- **Paragraph spacing**: 12pt after

**Section Formatting**:
- Main headings: Acme Blue, 16pt, bold
- Subheadings: Acme Navy, 14pt, semibold
- Body text: Acme Navy, 11pt, regular

## Content Guidelines

### Tone of Voice

- **Professional**: Formal but approachable
- **Clear**: Avoid jargon, use simple language
- **Active**: Use active voice, action-oriented
- **Positive**: Focus on solutions and benefits

### Standard Phrases

**Opening Statements**:
- "At Acme Corporation, we..."
- "Our commitment to innovation..."
- "Delivering excellence through..."

**Closing Statements**:
- "Thank you for your continued partnership."
- "We look forward to serving your needs."
- "Together, we achieve excellence."

### Data Presentation

**Numbers**:
- Use comma separators for thousands
- Currency: $X,XXX.XX format
- Percentages: XX.X% (one decimal)
- Dates: Month DD, YYYY

**Tables**:
- Headers in brand blue
- Alternating row colors
- Right-align numbers
- Left-align text

## Quality Standards

### Before Finalizing

Always ensure:
1. Logo is properly placed and sized
2. All colors match brand palette exactly
3. Fonts are consistent throughout
4. No typos or grammatical errors
5. Data is accurately presented
6. Professional tone maintained

### Prohibited Elements

Never use:
- Clip art or stock photos without approval
- Comic Sans, Papyrus, or decorative fonts
- Rainbow colors or gradients
- Animations or transitions (unless specified)
- Competitor branding or references

## Application Instructions

When creating any document:
1. Start with brand colors and fonts
2. Apply appropriate template structure
3. Include logo on first page/slide
4. Use consistent formatting throughout
5. Review against brand standards
6. Ensure professional appearance

## Scripts

- `apply_brand.py`: Automatically applies brand formatting to documents
- `validate_brand.py`: Checks documents for brand compliance

## Notes

- These guidelines apply to all external communications
- Internal documents may use simplified formatting
- Special projects may have exceptions (request approval)
- Brand guidelines updated quarterly - check for latest version
