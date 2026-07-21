---
name: html-frame-glitch-title
description: 'Generate a Glitch Title Frame as a single-file HTML document. 数字故障 / 像散偏移 / 数据腐败标题, 适合视频转场 / cyberpunk hero Category: video / animation frames. Format: 1920×1080 (16:9).'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-frame-glitch-title
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: deck
  mind.tags: '["artifact-template","deck"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/frame-glitch-title/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/frame-glitch-title/SKILL.md"]'
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

【模板: 故障艺术标题帧 (Glitch Title)】
【意图】单帧 hero / 视频转场 / cyberpunk 风格标题。Inspired by hyperframes glitch。

【画布】1920×1080, 背景 `#070708` 近黑或 CRT 暗灰 `#0d0e10`; 加 56px 网格 (透明 5%) + scanlines 横线 (透明 8%, 2px 间隔)。

【主标题】
- 居中, 6-9vw, weight 800/900, 字体 `Space Grotesk Bold` / `Inter Tight Black` / `JetBrains Mono Bold`。
- 颜色: 主层 `#f5f5f7`; 后面套 2 层伪影:
  - cyan `#00f0ff` translate(`-3px`, `1px`)。
  - magenta `#ff2bd6` translate(`3px`, `-1px`)。
- 整层加 clip-path 切片 5-8 段, 每段 `@keyframes` 随机 translateX -10px → 10px, 持续 80-160ms, 错峰播放, 营造 "data corruption" 像散。
- 每隔 1.5s 触发一次"重故障" — 整个标题被 horizontal smear 1 frame, 用 `filter: url(#displacementFilter)` 或简单 CSS 平移。

【附加层】
- 顶部一行 caption (uppercase mono, 11px, opacity 0.6): `>> SIGNAL_LOST · CH-04 · 14:32:08`。
- 标题下面 1 行副标 (24-28px, mono, opacity 0.7), 偶发被 ` ̶▒̶` 字符替换 (假乱码)。
- 角落随机点缀 `█▓▒░` ASCII 噪点 chunks。
- 底部 timecode (mono, opacity 0.4)。
- 整画面叠 noise grain 层 `background-image: url("data:image/svg+xml,...turbulence...")`, opacity 6%, mix-blend-mode overlay。

【SVG 滤镜 (可选)】
- 定义 `<filter id="rgbShift">` 用 `feColorMatrix` + `feOffset` + `feMerge` 把 R/G/B 三通道偏移; 整层 `filter: url(#rgbShift)` 在故障瞬间应用。

【设计细节】
- 颜色仅用: 黑 / 白 / cyan / magenta / 一点 amber 警告色; 严禁全彩虹。
- 字体: 西文 `Space Grotesk` 或 `JetBrains Mono` Bold; 中文 `Noto Sans Mono CJK SC` 或 `Noto Sans SC` Bold。
- 严禁 lorem ipsum; 必须用用户的标题 + 副标。
- 动效用 `@keyframes`, 可被 `prefers-reduced-motion` 关闭 (退回静态 chromatic split)。
- 单文件 HTML。

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
