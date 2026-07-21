---
name: html-deck-simple
description: 'Generate a Simple Deck as a single-file HTML document. 通用 horizontal-swipe HTML deck, 不要 magazine 调 Category: slide deck / presentation. Best for: product & startup. Format: 16:9.'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-deck-simple
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: deck
  mind.tags: '["artifact-template","deck"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/deck-simple/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/deck-simple/SKILL.md"]'
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

【组件库】
- 幻灯片容器: .slide (w-full h-screen flex items-center justify-center snap-center), 16:9 比例
- 进度条: .progress-bar (fixed top-0 left-0 h-1 bg-blue-600 transition-width)
- 导航按钮: .nav-btn (absolute bottom-8 w-12 h-12 rounded-full bg-white/80 shadow-lg flex items-center justify-center hover:bg-white)
- 页码指示器: .page-indicator (fixed bottom-8 right-8 text-sm text-gray-400)
- 标题幻灯片: .title-slide (text-center), 大标题 text-6xl/7xl font-bold
- 内容幻灯片: .content-slide (max-w-4xl mx-auto), 左文右图或上图下文布局
- 图标装饰: 使用 Lucide 内联 SVG 或 CSS 绘制图标

【推荐 CDN 资源】
- 图表: Chart.js (https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js)
- 图标: Lucide (https://unpkg.com/lucide@latest/dist/umd/lucide.js)
- 动画: Motion One (https://cdn.jsdelivr.net/npm/motion@11.12.0/dist/motion.min.js) — 用于幻灯片切换动画

【配色方案】
- 主色: #2563eb (Blue-600) — 现代/专业
- 中性色: #f8fafc (Slate-50), #475569 (Slate-600)
- 强调色: #f59e0b (Amber-500) — 高亮/CTA
- 幻灯片背景: 白色或极浅灰, 文字用深灰而非纯黑

【内容真实性】
- 必须使用用户提供的真实数据，不要编造
- 中文与英文混排时，中英文之间留半角空格

【模板: Simple Deck】
【意图】干净通用的 horizontal-swipe deck (pitch / overview / study)。
【布局】
- Cover + N 个 content 页 + 收尾 (N 由【用户内容】长度决定, 完整覆盖每个要点; 短内容 6-10 起步, 长内容应更多)
- 每页一个核心信息 + 1 张图 / 1 个图表
- 顶部 progress bar
【设计细节】
- 键盘 ← / → 切换 + hash 同步

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
