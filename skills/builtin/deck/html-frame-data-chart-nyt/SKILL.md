---
name: html-frame-data-chart-nyt
description: 'Generate a NYT-Style Data Chart Frame as a single-file HTML document. NYT-newsroom 排版 + 错峰揭示动画 + 编辑级图表 (折线/柱/范围带) Category: video / animation frames. Format: 1920×1080 (16:9).'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-frame-data-chart-nyt
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: deck
  mind.tags: '["artifact-template","deck"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/frame-data-chart-nyt/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/frame-data-chart-nyt/SKILL.md"]'
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

【模板: NYT 风数据图表帧】
【意图】把一段数据 (CSV / JSON / 一句结论) 做成《纽约时报》专栏感的单帧/动画图表, 适合视频片段或推特卡。Inspired by hyperframes data-chart。

【画布】1920×1080, 暖白底 `#f7f5ee` 或墨黑底 `#0e0e0e` 二选一; 文字色和背景相反。

【布局】
- **顶部 kicker** (11px uppercase letterspace 0.14em, 颜色 = accent 红 `#a91d1d` 或 mint `#5fb38a`): 数据来源 + 类目, 如 "GLOBAL · WEEKLY ACTIVE USERS · 2018–2026"。
- **大字标题** (Cheltenham / Playfair / Source Serif Pro, 5.6vw, italic 副标可选): 一句结论。**结论必须从用户数据中提炼**, 不是描述图。
- **图表区** (占画布 55-65%):
  - 折线: 1-2 条线, 主线 ink 实心 2.5px, 次线 dashed 1.5px; 数据点用 6px 实心圆; 关键点旁标注 `2024 · 412M` 黑色 mono 小字。
  - 柱状: 全部 ink 单色或加 1 道 accent 高亮柱; 柱顶大数字; 柱底类目斜体 (Cheltenham italic)。
  - 范围带 (range band): 浅灰填充 `#e6e2d2` 包络 + 中线 ink。
- **底部 source + footnote** (10px mono, opacity 0.6): "Source: 用户数据 · Chart by html-anything"。
- **错峰揭示动画**: 标题 fade-in (0s), kicker (200ms), 折线 stroke-dashoffset 1.2s ease-out (400ms), 数据标签依次 100ms 间隔。可被 `prefers-reduced-motion` 关闭。

【设计细节】
- **绝不**: 使用 chart.js / d3 库 (除非 jsdelivr CDN 引入); 推荐手写 SVG, 不超过 80 行 inline。
- 字体: 标题 `Source Serif Pro` 或 `Cheltenham` (无则用 `Playfair Display`); body `IBM Plex Sans` 或 `Inter`; 数据标签 `IBM Plex Mono`。
- 1 个主色 (ink) + 1 个 accent (NYT red `#a91d1d` / 编辑 mint `#5fb38a` / 暖橙 `#d97757` 三选一)。
- Y 轴刻度仅 hairline + 3-4 个 tick, 标签在轴外侧 mono 字。
- 严禁 grid 全屏铺线、阴影、3D 立体柱; 严禁 emoji。
- 必须用用户提供的数据。如果输入是文本结论, 自动估算合理坐标 (但要标注 "schematic"); 如果是 CSV/JSON, 直接绘制。
- 单文件 HTML; 数据点旁注释格式: `<text class="annot">2024 · 412M</text>`。

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
