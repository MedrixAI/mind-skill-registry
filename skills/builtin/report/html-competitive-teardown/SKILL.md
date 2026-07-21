---
name: html-competitive-teardown
description: 'Generate a Competitive Teardown report as a single-file HTML document. 定位图 + 功能矩阵 + 价格对比 + 机会窗口, 把竞品资料转成产品决策报告. Category: business doc / strategy. Best for: product & strategy. Format: 战略长页面.'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-competitive-teardown
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: report
  mind.tags: '["artifact-template","report"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/competitive-teardown/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/competitive-teardown/SKILL.md"]'
---
你是世界级的视觉设计师 + 资深前端工程师。请输出一份**自包含的单文件 HTML**，要求：

【内容驱动数量】
- 模板只定义可用版面/风格/配色/字体/组件库，不定义 section 的数量
- 输出数量完全由用户内容的实际长度和信息结构决定，必须完整覆盖每一个要点

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
- 定位象限图: 用 CSS Grid 2×2 + SVG 坐标轴绘制，坐标轴标签必须来自用户内容
- 竞品卡片: .competitor-card (bg-white shadow-md rounded-2xl p-6 border-l-4), 包含 target user / core promise / pricing / strength / weakness
- 功能矩阵: 横向表格 .feature-matrix, sticky 首列, 用 ✓ / △ / — 图标, 小屏可转为 stacked cards
- 机会窗口卡片: .opportunity-card (bg-gradient-to-r from-blue-50 to-white), 包含 why now / target segment / first move / risk
- 行动建议时间线: .action-timeline (flex flex-col gap-4), 30天 / 90天 / 180天 分段

【推荐 CDN 资源】
- 图表: Chart.js (https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js)
- 图标: Lucide (https://unpkg.com/lucide@latest/dist/umd/lucide.js)

【配色方案】
- 主色: #2563eb (Blue-600) — 战略/专业
- 中性色: #f8fafc (Slate-50), #64748b (Slate-500)
- 强调色: #f59e0b (Amber-500) — 机会/信号
- 可选深色主题: bg #0f172a, 主色 #38bdf8, 强调色 #fbbf24

【内容真实性】
- 必须使用用户提供的真实数据，不要编造
- 中文与英文混排时，中英文之间留半角空格

【模板: 竞品拆解 / Competitive Teardown】
【意图】把多个竞品的杂乱资料转成一份可决策的产品战略报告，帮团队回答"我们和它们到底差在哪里，下一步该怎么打?"
【适合输入】竞品官网/定价页/changelog/用户评论/销售反馈，2-6 个竞品最合适
【布局】
1. Header: 市场 / 产品类别 / 报告日期 / 结论一句话
2. Executive Takeaway: 3 条最重要判断，每条包含 "so what"
3. Positioning Map: CSS 2×2 象限图，坐标轴来自用户内容
4. Competitor Cards: 每个竞品一张卡
5. Feature Matrix: 横向对比表，行=关键能力，列=竞品+"Us/Opportunity"
6. Pricing/Packaging Read: 价格层级、免费试用、限制项
7. UX/Messaging Notes: 4-6 条可观察细节
8. Opportunity Windows: 3 个机会窗口
9. Recommended Moves: 30天/90天/180天行动建议
10. Evidence Gaps: 列出缺失信息

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。