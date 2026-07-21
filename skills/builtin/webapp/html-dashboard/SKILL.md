---
name: html-dashboard
description: 'Generate a Admin Dashboard as a single-file HTML document. 固定侧栏 + 顶栏 + KPI 网格 + 1-2 张图 Category: dashboard / analytics panel. Best for: operations & management. Format: 桌面 1440.'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-dashboard
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: webapp
  mind.tags: '["artifact-template","webapp"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/dashboard/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/dashboard/SKILL.md"]'
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
- KPI 卡片: .kpi-card (bg-white rounded-2xl shadow-sm p-6 border border-gray-100), 大号数字 + 趋势箭头 ↑↓ + 副标题
- 图表容器: .chart-container (bg-white rounded-2xl shadow-sm p-6 border border-gray-100), 固定高度 320px, Canvas 内图表
- 导航侧栏: .sidebar (fixed left-0 top-0 h-full w-64 bg-gray-900 text-white), 折叠时 w-16
- 顶栏: .topbar (sticky top-0 h-16 bg-white border-b flex items-center px-6)
- 活动列表: .activity-list (divide-y), 每行 avatar + 描述 + 时间戳
- 状态标签: .status-badge (px-2 py-0.5 rounded-full text-xs font-medium), 绿=active, 黄=pending, 灰=inactive

【推荐 CDN 资源】
- 图表: Chart.js (https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js)
- 图标: Lucide (https://unpkg.com/lucide@latest/dist/umd/lucide.js)

【配色方案】
- 主色: #4f46e5 (Indigo-600) — 专业/后台
- 中性色: #f9fafb (Gray-50), #6b7280 (Gray-500)
- 强调色: #10b981 (Emerald-500) — 正向指标; #ef4444 (Red-500) — 告警
- 侧栏: bg-gray-900, text-gray-100

【内容真实性】
- 必须使用用户提供的真实数据，不要编造
- 中文与英文混排时，中英文之间留半角空格

【模板: 管理后台 Dashboard】
【意图】标准 admin/analytics 仪表板单页。
【布局】
- Fixed left sidebar (logo + 导航 + 用户 footer)
- Top bar (search + 通知 + avatar)
- Main: KPI cards 网格 (3-5 个)
- 1-2 张主图表 (折线 / 柱 / 区域)
- 底部 recent activity 列表

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
