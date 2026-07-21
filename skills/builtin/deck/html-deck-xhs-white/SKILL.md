---
name: html-deck-xhs-white
description: 'Generate a White Editorial Deck as a single-file HTML document. 纯白 + 顶部彩虹 bar + 渐变文字 + 马卡龙软卡片 + 黑底 pill Category: slide deck / presentation. Best for: marketing & branding. Format: 16:9 / 3:4.'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-deck-xhs-white
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: deck
  mind.tags: '["artifact-template","deck"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/deck-xhs-white/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/deck-xhs-white/SKILL.md"]'
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

【模板: 白底杂志风 Deck】
【意图】可同时发小红书图文与横版 PPT 双用的白底杂志风。
【布局】
- 纯白背景 + 顶部 10 色彩虹 bar
- 80-110px display 标题 + 紫→蓝→绿→橙→粉渐变文字
- 马卡龙软卡片组 (粉 / 紫 / 蓝 / 绿 / 橙)
- 黑底白字 .focus pill + 引用大块

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
