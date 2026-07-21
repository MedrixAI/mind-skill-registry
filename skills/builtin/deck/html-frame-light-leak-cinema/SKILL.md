---
name: html-frame-light-leak-cinema
description: 'Generate a Light-Leak Cinematic Frame as a single-file HTML document. 胶片漏光 + 颗粒噪点 + 16:9 letterbox + 衬线大字, 电影感开场 / 章节卡 Category: video / animation frames. Format: 2.39:1 letterbox (1920×800) 或 16:9 (1920×1080).'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-frame-light-leak-cinema
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: deck
  mind.tags: '["artifact-template","deck"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/frame-light-leak-cinema/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/frame-light-leak-cinema/SKILL.md"]'
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

【模板: 胶片漏光电影帧】
【意图】纪录片 / 个人短片 / 视频章节卡的开场单帧 —— 暖橙漏光 + 35mm 颗粒 + 衬线大字, 古典胶片质感。Inspired by hyperframes light-leak。

【画布】
- **2.39:1 letterbox** (推荐): 1920×800, 上下黑边各 140px (`#000`)。
- 或 16:9: 1920×1080, 无 letterbox。

【背景】
- 底层: 深暖色 (深红棕 `#1a0d08` / 墨绿 `#0a1410` / 蓝紫 `#0d0e1a`) 或场景描绘 (CSS gradient 模拟天空 / 室内 / 室外)。
- **胶片漏光 (Light Leak)**: 2-3 个大 `radial-gradient(ellipse at top right, #ffb547 0%, transparent 50%)` + 1 个底部 `linear-gradient(to top, #d97757 0%, transparent 30%)`; 颜色取暖橙 / 桃 / 玫红 / 暗黄, **不要冷蓝**。
- **35mm Grain**: 全屏覆盖 SVG turbulence noise 图层, opacity 14%, `mix-blend-mode: overlay`; 也可用 `background-image: url("data:image/svg+xml,...feTurbulence...")`。
- 可选: 1 道 `feDisplacementMap` 模拟胶片摆动 (慎用)。

【文字】
- 中央或左下: 大字衬线 (Source Serif Pro / Playfair Display / EB Garamond) 5-8vw, weight 500 italic; 颜色暖白 `#f5e9d6` 或 cream。
- 副标 (24-28px) 一行, opacity 0.7, 同样衬线。
- 角落 caption (uppercase letterspace 0.18em, 10-11px, mono, opacity 0.5): "REEL 03 · CH I · 1985"。
- 底部 timecode + 拍摄地 + 日期 (mono, opacity 0.4)。

【可选附加】
- "胶片划痕": 几条 1-2px 竖向白线, opacity 0.2, 不规则间距 (用 `box-shadow` 多重 inset 或多个 `<div>`)。
- "胶片齿孔": letterbox 黑边内, 等距小白方块 (CSS repeating-linear-gradient)。
- 入场动效: 整画面从 underexposed (brightness 0.3) → normal, 800ms 内; 漏光位置缓慢漂移 12s 一个周期。

【设计细节】
- 颜色绝不超过 4 个色相 (深背景 + 2 个暖漏光色 + 文字 cream)。
- 严禁: 蓝紫漏光 (违反胶片质感)、emoji、霓虹色、几何 dashboard 装饰。
- 中文: `Noto Serif SC` italic 不存在 → 用 `Noto Serif SC` regular + 字距加大。
- 必须用用户提供的标题; 自动估算合理"年份 / 章节 / 地点" 元数据 (但来源用户内容)。
- 单文件 HTML, 用 `prefers-reduced-motion` 关动效。

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
