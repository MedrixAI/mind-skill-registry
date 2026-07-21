---
name: html-vfx-text-cursor
description: 'Generate a VFX Text Cursor as a single-file HTML document. 光标拖光 + 彩色像散射线 + 定向光斑, 适合视频片头逐字揭示金句 Category: video / animation frames. Format: 1920×1080 (16:9).'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-vfx-text-cursor
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: video
  mind.tags: '["artifact-template","video"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/vfx-text-cursor/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/vfx-text-cursor/SKILL.md"]'
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

【模板: VFX 文字光标 (Text Cursor)】
【意图】视频开场/Hero 帧 —— 光标在画布上"打字", 文字逐字浮现, 后面拖着彩色像散尾迹 + 定向光斑。Inspired by hyperframes vfx-text-cursor。

【画布】1920×1080, 背景 `#06070a` 暗哑黑 或 `#0a0d12` (有暖偏蓝); 加微妙 vignette。

【内容】
- 一句金句 (中英不限), 居中, 字号 6-8vw, weight 700, 字体 `Inter Tight` / `Source Sans 3` / `Noto Sans SC`。
- 逐字揭示, 每个字符 80ms 间隔; 当前字符后面跟着一个 cursor `▍` (或细 vertical bar)。
- 已揭示文字默认白色 `#f5f5f7`, opacity 1; 即将揭示位置加 chromatic ghost: 一份 `text-shadow: 2px 0 #ff3b6f, -2px 0 #00d4ff` 在 reveal 瞬间, 200ms 内收敛回正常。
- 光标本身: 16px 宽矩形, 颜色 = accent (取 1: hot pink `#ff3b6f` / cyan `#00d4ff` / amber `#ffb547`), 闪烁 `@keyframes` 1.0s 周期; 后面拖一条 60-120px 的 motion blur trail (径向渐变到透明)。

【光斑 / 射线】
- 在打字位置附近随机生成 3-5 道**定向光斑** (light leak): 用 `linear-gradient(45deg, transparent, accent20, transparent)` 的细长矩形 + `mix-blend-mode: screen`, 不规则角度。
- 当文字打完, 整段文字加 0.5s shimmer sweep (光带横扫)。

【字段】
- 顶部 caption (uppercase letterspace 0.18em, 11px, opacity 0.5): "FRAME 01 · OPENING"。
- 文字底下副标 (24-28px, opacity 0.6): 来源 / 章节。
- 右下角 timecode (`00:03:21` mono)。

【设计细节】
- **绝不**: 多色彩虹 chromatic (只用 1 个 hot pink + cyan 这种二元像散, 不要 R/G/B 全色)。
- 字体: 西文 `Inter Tight` Bold; 中文 `Noto Sans SC` Bold; 严禁衬线。
- 动效用 `@keyframes` + JS 计时器 (`setTimeout` 逐字), 可被 `prefers-reduced-motion` 关闭 (直接显示所有字)。
- 必须用用户提供的金句; 不要捏造。
- 单文件 HTML, 不要外链字体以外的资源。

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
