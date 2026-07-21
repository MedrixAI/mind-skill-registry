---
name: html-frame-flowchart-sticky
description: 'Generate a Sticky Flowchart Frame as a single-file HTML document. SVG 曲线连接 + 便利贴节点 + 光标交互, 像白板 brainstorm Category: video / animation frames. Best for: operations & management. Format: 1920×1080 (16:9).'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-frame-flowchart-sticky
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: deck
  mind.tags: '["artifact-template","deck"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/frame-flowchart-sticky/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/frame-flowchart-sticky/SKILL.md"]'
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

【模板: 便利贴流程图帧 (Sticky Flowchart)】
【意图】把一个流程 / 系统 / 工作流画成"白板 + 便利贴"的样子, 适合 onboarding 视频、运营流程说明、系统架构讲解。Inspired by hyperframes flowchart。

【画布】1920×1080。背景: 米黄白板纸 `#f4ede1` 或冷灰白板 `#f0f2f4`; 加非常浅的 hex grid `rgba(0,0,0,0.04)` 让它有白板感。

【节点 (Sticky Notes)】
- 每节点 = 一张 240×180px 便利贴, 4 套颜色随机分配: 黄 `#fcd34d` / 桃 `#fca5a5` / 薄荷 `#a7f3d0` / 天 `#a5b4fc`。
- 便利贴有轻微旋转 `transform: rotate(±2deg)` 不一致, 投影 `drop-shadow(0 6px 14px rgba(0,0,0,0.12))`, 顶部胶带 `linear-gradient(...)` 装饰。
- 节点内容: 1 个 emoji 或单线 SVG icon + 大字标题 (16-20px) + 一行描述 (12px)。
- 节点字体: `Kalam` / `Caveat` / `Patrick Hand` 手写感字体 (中文用 `霞鹜文楷` 或 `LXGW WenKai Screen`)。

【连接线 (SVG)】
- 用 `<path>` Bezier 曲线连接节点, stroke `#2a2a2a`, width 2.5, `stroke-linecap: round`, `stroke-dasharray: 0` (实线) 或 `8 6` (虚线 = 条件分支)。
- 箭头终端用 `marker-end`, 黑色三角小箭头。
- 复杂节点可有循环或分支: 同一节点连出 2 条 (分叉) 或 2 条进入一节点 (合并)。

【可选交互】
- 顶部 caption (sans, 12px uppercase): "FLOW · MIGRATION · 2026"。
- 鼠标 hover 节点: 抬起阴影 + scale 1.05, 用 CSS transition。
- 一个"光标"装饰 (`<svg>` arrow + name tag), 浮在某节点旁, 模拟 figma 协作光标。

【设计细节】
- 至少 5 个节点, 最多 12 个。
- 节点排布不要全部居中对齐, 要有一点白板风的"随手贴"感, 但保证连接线清晰不交叉。
- 严禁: 全屏深色背景、霓虹色、企业 dashboard 风格。
- 字体不能用 Inter / 衬线, 必须手写感。
- 单文件 HTML, 不要外部图标库 (用 inline SVG)。
- 必须用用户的真实流程内容; 节点文字直接来自用户输入。

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
