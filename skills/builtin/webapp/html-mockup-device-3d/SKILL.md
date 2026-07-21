---
name: html-mockup-device-3d
description: 'Generate a Device 3D Showcase as a single-file HTML document. iPhone + MacBook 仿 GLTF 静态展架, 屏幕内嵌真实 HTML 内容, 玻璃镜头折射, 360° 转盘构图 Best for: product & startup. Format: 1920×1080 (16:9).'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-mockup-device-3d
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: webapp
  mind.tags: '["artifact-template","webapp"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/mockup-device-3d/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/mockup-device-3d/SKILL.md"]'
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

【模板: 设备 3D 展架 (Device 3D Showcase / HTML-in-Canvas)】
【意图】产品发布、App 演示、设计稿展示。把用户提供的 UI 内容真实渲染到 iPhone / MacBook "屏幕"里, 周围用 CSS 3D transform 模拟 GLTF 模型的玻璃 / 高光 / 折射。Inspired by hyperframes vfx-iphone-device。

【硬性构图】
- **画布**: 1920×1080, 暖灰渐变背景 `radial-gradient(#1a1a1f → #0a0a0f)`, 底部反射地面 (mirror gradient)。
- **iPhone 15 Pro 模型**: 左侧 / 中部, `transform: rotateY(-12deg) rotateX(4deg) translateZ(40px)`; 边框钛金属银 `#a8a8ad` (实心 4px) + 屏幕圆角 56px; 屏幕内嵌 iframe-like div, 真实渲染用户的 HTML 内容 (mobile viewport 375×812)。
- **MacBook Pro 14"** (可选第二台): 右侧, 略小, `rotateY(8deg)`; 上盖屏幕嵌入桌面 viewport 内容 (1440×900 缩放); 底座键盘 + trackpad 用 CSS 阴影线条绘制 (不画键帽细节)。
- **玻璃 / 镜头光斑**: 顶部加 2-3 个 `radial-gradient(ellipse, rgba(255,255,255,0.4) 0%, transparent 60%)` 的椭圆 highlight, 模拟 morphing glass lens。
- **地面反射**: 设备下方 `transform: scaleY(-1)` + `mask-image: linear-gradient(to bottom, rgba(0,0,0,0.4), transparent 70%)`。

【屏幕内容来源】
- 用户提供的是文本/数据 → 自动渲染为一个 mock app 界面 (顶部 status bar + 标题 + body + 底部 tab bar 或 home indicator)。
- 用户提供的是 HTML → 原样嵌入屏幕 div 内 (注意缩放 transform 让它适配屏幕宽高)。
- 屏幕内 UI 用 Tailwind, 字号要按 mobile 真实尺寸 (text-sm / text-base, 不要 text-9xl)。

【可选附加元素】
- 右下角 "product slug" 角标: 大 logo + 一行 tagline + 副标 hairline。
- 顶部一行 caption (英文 sans, 字号小, 透明 0.6): 产品 codename / 日期 / 版本。
- 加 8s 自动 CSS 转盘: `@keyframes turntable` rotateY -12 ↔ 12, ease-in-out infinite alternate; 可被 `prefers-reduced-motion` 关闭。

【设计细节】
- **绝不**: 用外部 mockup 图片 URL (任何 unsplash / dribbble link), 全部用 CSS / SVG 绘制设备。
- 字体: 设备外的 caption / logo 用 `Inter Tight` / `SF Pro` 风格; 设备内根据用户内容自适应。
- 背景可选 4 套调色: charcoal / pearl / midnight blue / mocha; 不要彩虹渐变。
- 单文件 HTML; iframe 不要用 srcdoc 嵌套 (容易出问题), 用 `<div class="screen">` + Tailwind 渲染内容。
- 必须用用户真实数据填充屏幕内容, 严禁 lorem ipsum 或 "Your text here"。

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
