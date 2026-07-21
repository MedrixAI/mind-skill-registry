---
name: html-video-hyperframes
description: 'Generate a Hyperframes Video as a single-file HTML document. Hyperframes / Remotion 兼容的连续帧动画, 可自动播放 Category: video / animation frames. Format: 1920×1080 (16:9).'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-video-hyperframes
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: video
  mind.tags: '["artifact-template","video"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/video-hyperframes/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/video-hyperframes/SKILL.md"]'
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

【模板: Hyperframes 视频帧】
- 输出 N 个连续 `<section class="frame">`, 每个 `w-[1920px] h-[1080px]`; N 由【用户内容】信息密度决定 (短脚本 6-10 帧起步, 长脚本应更多, 每帧只承载一个镜头/概念)。
- 每帧表达一个镜头/概念: 文字 + 视觉构图 (中央构图 / 黄金分割 / 三分法)。
- 每帧底部隐藏标记 `<!-- frame:N duration:3000 transition:fade -->` 供后续 Remotion / Hyperframes 渲染脚本读取。
- 顶部加一段 JavaScript 自动播放: 每 3 秒切换到下一帧, 也支持点击 / 方向键控制; 角落显示进度条。
- 第 1 帧是 hook (一个数据 / 一个反常识 / 一个问题), 第 2-N 是论证, 最后是结论 + CTA。
- 字号巨大 (text-9xl), 一句话即可, 不要堆砌。
- 配色统一一套电影感 (深色背景 + 1 个霓虹强调色)。
- 输出最后包含一段简短注释 `<!-- HYPERFRAMES_META: ... -->`, 包含每帧 duration / transition / sceneSummary 的 JSON 元数据, 用于后续转 Remotion。

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
