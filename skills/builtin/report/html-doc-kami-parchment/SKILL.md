---
name: html-doc-kami-parchment
description: 'Generate a Kami Parchment Document as a single-file HTML document. 暖羊皮纸底 (#f5f4ed) + 墨蓝单色 accent (#1B365D) + 单一衬线字体, 编辑级排印 Category: document / documentation. Best for: personal & lifestyle. Format: A4 / Letter 长页.'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-doc-kami-parchment
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: report
  mind.tags: '["artifact-template","report"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/doc-kami-parchment/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/doc-kami-parchment/SKILL.md"]'
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

【模板: Kami 羊皮纸文档】
【意图】严肃排版文档: one-pager / 长报告 / 信函 / 简历 / 财报 / changelog / portfolio。Inspired by tw93/kami。强调"写得像被排过版的纸", 不是 dashboard, 不是网页。

【硬性视觉签名 — 不许改】
- **画布**: 暖羊皮纸 `#f5f4ed` (永远不用纯白 `#fff`)。次级背景 `#efeee5`。
- **墨色**: 主文字 `#1f1d18` (近黑暖灰, 不用纯黑 `#000`)。次文字 `#6b665b`。
- **唯一色彩**: 墨蓝 `#1B365D` ——所有 accent (链接、tag 描边、重点数字、引用左 rule) 只能用这一个色, 严禁多色。
- **字体**: 一种语言一种衬线, 全文不混用:
  - 英文: `Charter` (fallback: `Source Serif Pro`, `Iowan Old Style`)
  - 中文: `TsangerJinKai02 W04` (fallback: `Noto Serif SC`)
  - 日文: `YuMincho` (fallback: `Noto Serif JP`)
  - Body 400, Heading 500 (不要 700/800/900)。
- **行高**: 标题 1.1–1.3, 紧凑正文 1.4–1.45, 阅读型正文 1.5–1.55。
- **绝不**: drop-shadow / blur / 圆角 ≥ 8px / 渐变 / 霓虹色 / rgba (用 solid hex)。
- **细节**: tag 用 solid hex 背景方块 (因为 WeasyPrint 不渲染 rgba 好); 单线几何 icon; 边缘 1px hairline `#d4d1c5` rule, 长度受控不到边。

【可选文档类型 — 按用户内容判断】
- **One-Pager** — 顶 logotype (Charter italic) + 标题 + lede + 3 列要点 + 底脚 metadata。
- **Long Doc** — 封面页 (大标题 + 副标 + 作者 + 日期) → 目录 (kicker + page no.) → 章节 (folio 顶角 + section rule + body) → 注释脚注 + 文末 colophon。
- **Letter** — 抬头地址 + 日期 + 收件人 + 正文 (左对齐, 段间空 1.5em) + 署名 + 签名占位线。
- **Portfolio** — 项目 hero (大标题 + sub) + 1 张全幅图 (用 CSS 块绘制占位) + 项目描述 + 角色 / 时间 / stack 元数据 row。
- **Resume** — 顶部姓名 (大字) + tagline 一行 + contact row + 主要 section: experience (公司 / 时间 / 职位 / bullets) + skills + education。
- **Slides** — keynote 风, 页数由【用户内容】决定 (短内容 6 页起步, 长内容应更多), 每页满铺羊皮纸, 大标题 + lede + 角标 page no., 简洁到只有"被印出来"的感觉。
- **Equity Report** — 公司名 + ticker + Q × 年份 + key metrics row (revenue / margin / yoy) + body 分析 + 图表 (SVG 单色折线)。
- **Changelog** — 版本号 (Charter italic 大字) + 日期 + 改动列表 (Added / Changed / Fixed), 单 rule 分隔。

【设计准则】
- "Composed pages, not dashboards." 不要堆 KPI 卡, 不要堆 emoji 图标, 不要 hero gradient。
- "Ring or whisper only, no hard drop shadows." 阴影只能是 `0 0 0 1px #d4d1c5` 这种 hairline 描边。
- 文字层级靠**衬线对比 + 字号 + 留白**, 不靠颜色。
- 单文件 HTML, 用 Tailwind CDN; 全文中英混排时加盘古之白; 不要外链图片, 占位用 paper-tint 色块 + 1px ink 描边。

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
