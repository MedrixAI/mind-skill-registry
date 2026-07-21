---
name: html-data-report
description: 'Generate a Data Visualization Report as a single-file HTML document. 把 CSV/Excel/JSON 数据转成漂亮的可视化报告页 Category: data visualization / report. Best for: finance & business. Format: 桌面长页面.'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-data-report
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: report
  mind.tags: '["artifact-template","report"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/data-report/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/data-report/SKILL.md"]'
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
- KPI 卡片: .kpi-card (bg-white rounded-2xl shadow-sm p-6 border), 大号数值 + 同比变化 (↑↓ + 百分比) + 微型趋势线 (canvas height=40px)
- 图表容器: .chart-box (bg-white rounded-2xl shadow-sm p-6 border), 固定高度 div (height:280-320px) 包裹 canvas, Chart.js 使用 responsive:true + maintainAspectRatio:false
- 数据表格: .data-table (w-full border-collapse), sticky header, zebra stripe (even:bg-gray-50), hover:bg-blue-50
- 洞察卡片: .insight-card (flex gap-3 p-4 bg-blue-50 rounded-xl), emoji 开头 + 文字描述
- 方法论折叠: details/summary (bg-gray-50 rounded-xl p-4), 点击展开
- 标签: .tag (inline-flex px-2 py-0.5 rounded-full text-xs font-medium bg-gray-100)

【推荐 CDN 资源】
- 图表: Chart.js (https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js) — 默认推荐
- 图表备选: ECharts (https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js) — 中文场景或需要更丰富图表类型时使用
- 图标: Lucide (https://unpkg.com/lucide@latest/dist/umd/lucide.js)

【配色方案】
- 主色: #2563eb (Blue-600) — 数据/专业
- 中性色: #f9fafb (Gray-50), #6b7280 (Gray-500)
- 强调色: #10b981 (Emerald-500) — 正向指标; #ef4444 (Red-500) — 负向指标
- 图表调色板: ['#2563eb','#10b981','#f59e0b','#ef4444','#8b5cf6','#ec4899','#06b6d4']

【内容真实性】
- 必须使用用户提供的真实数据，不要编造
- 中文与英文混排时，中英文之间留半角空格

【模板: 数据可视化报告】
- 头部: 报告标题 + 时间区间 + 数据来源说明。
- KPI 卡片网格: 3-5 个最重要指标, 每个卡片显示数值 + 同比变化 + 微型趋势线。
- 主图表区: 至少 2 个图表 (柱状 / 折线 / 饼 / 散点), 使用 Chart.js 或 ECharts (jsdelivr CDN 引入), 数据从用户输入解析得到。
- **图表容器必须有固定高度**: 每个 `<canvas>` 外层包一个 `<div style="position:relative;height:NNNpx">` (KPI 迷你图 ~40px, 主图表 ~240–280px)。Chart.js 用 `responsive:true, maintainAspectRatio:false` 时若父容器没有显式高度, 会陷入 ResizeObserver 死循环, 图表无限增高直至卡死浏览器。**绝对不要**直接给 canvas 写 `height=` 属性当布局, 那个只是初始值。
- 数据表格: 用户原始数据节选, 使用 `<table>` + 现代化样式 (zebra stripe, hover, sticky header)。
- 洞察块: 3-5 条文字洞察, 用 emoji 开头, 像产品周报。
- 底部"方法论"折叠区。
- 配色克制专业: 主色 1 + 中性色阶, 图表用调色板。
- **必须解析用户提供的实际数据**, 不要捏造。

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。

## anti-slop（用可执行量，禁用氛围词）
- 禁用 premium / magazine-grade / rich / futuristic / professional / 高级感 / 精美 等氛围词；改写为可执行量，例如"头部标题 + 3–5 KPI 卡（含微型趋势线）+ ≥2 图表（固定高度容器）+ 数据表 + 3–5 洞察块 + 底部方法论折叠"。
- 不编造内容；中英文混排留半角空格。

---
> 共享基线（CDN allowlist / 设计 token / 硬性技术要求 / 响应式 / 无障碍）见 `skills/enhancements/base.md`，运行时由全局 system prompt 注入、由 `htmlassets.ValidateHTML` 强制；本 skill 仅定义版面/组件/场景差量。
