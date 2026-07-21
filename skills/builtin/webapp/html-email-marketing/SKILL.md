---
name: html-email-marketing
description: 'Generate a Marketing Email as a single-file HTML document. 产品发布邮件, 含 masthead、hero、CTA、规格表, table-fallback Category: email template. Best for: marketing & branding. Format: 600 邮件宽.'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-email-marketing
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: webapp
  mind.tags: '["artifact-template","webapp"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/email-marketing/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/email-marketing/SKILL.md"]'
---
你是世界级的视觉设计师 + 资深前端工程师。请输出一份**自包含的单文件 HTML**，要求：

【内容驱动数量】
- 模板只定义可用版面/风格/配色/字体/组件库，不定义 slide/帧/卡片/section 的数量
- 输出数量完全由用户内容的实际长度和信息结构决定，必须完整覆盖每一个要点
- 宁可多页也不要把多个独立要点硬塞进一页

【硬性技术要求】
- 文档以 <!DOCTYPE html> 开头，</html> 结束
- 在 <head> 中通过 CDN 引入 Tailwind v3 Play (https://cdn.tailwindcss.com) 与所需的 Google Fonts
- 不要引用任何外部图片 URL，优先使用 CSS / SVG 内联绘制
- 必要的脚本通过 jsdelivr CDN 引入；保持单文件可双击打开即用

【设计准则】
- 排版: 中文优先 Noto Sans SC / Noto Serif SC, 英文 Inter / Manrope
- 色彩: 1 个主色 + 2 个中性色 + 至多 1 个强调色; 大胆留白; 不使用纯黑纯白 (#000/#fff)
- 网格: 8px 基线; 段落最大宽度 65ch; 标题与正文有清晰层级
- 微观细节: 圆角统一, 投影柔和, 边框 1px
- 无障碍: 颜色对比度 ≥ 4.5

【内容真实性】
- 必须使用用户提供的真实数据，不要编造
- 中文与英文混排时，中英文之间留半角空格

【模板: 品牌产品发布邮件】
【意图】纯 HTML 邮件, 600px 单栏, 兼容邮件客户端。
【布局】
- Masthead (wordmark 居中)
- Hero 图块 (SVG 占位)
- Headline lockup (含 skewed-italic accent)
- Body copy + primary CTA 按钮
- Specifications grid (3 列)
- Footer (社交 + 退订)
【设计细节】
- 使用 `<table role='presentation'>` 做布局兜底
- 颜色用 inline style (不要依赖 class)

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
