---
name: html-exec-briefing-memo
description: 'Generate an Executive Briefing Memo as a single-file HTML document. Decision needed + recommendation + evidence + tradeoffs, 把复杂材料压成可拍板的一页. Category: business doc / strategy. Best for: leadership & operations. Format: 一页决策 memo.'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-exec-briefing-memo
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: report
  mind.tags: '["artifact-template","report"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/exec-briefing-memo/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/exec-briefing-memo/SKILL.md"]'
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
- 决策徽章: .decision-badge (inline-flex px-4 py-2 rounded-full text-sm font-bold), 绿色=Approve, 黄色=More Evidence, 红色=Reject
- 置信度指示器: .confidence-bar (h-2 rounded-full bg-gray-200), 内层 div 宽度表示置信度百分比
- 事实证据卡: .evidence-card (bg-white border rounded-xl p-4), 每条标注来源类型标签 (sales/product/finance/customer/ops)
- 权衡对比表: .tradeoff-table (w-full border-collapse), 三列对比 Option A/B/C, 行=upside/cost/risk/reversibility
- 风险卡片: .risk-card (border-l-4 border-red-400 bg-red-50 p-4), 包含 risk + mitigation
- 行动路径: .action-path (flex gap-4), 三条路径卡片 approve/reject/more-evidence

【推荐 CDN 资源】
- 图标: Lucide (https://unpkg.com/lucide@latest/dist/umd/lucide.js)

【配色方案】
- 主色: #1e40af (Blue-800) — 权威/正式
- 中性色: #fafaf9 (Stone-50), #78716c (Stone-500)
- 强调色: #dc2626 (Red-600) — 风险/紧急; #16a34a (Green-600) — 批准/正面
- 可选深色主题: bg #1c1917, 主色 #60a5fa, 强调色 #f87171

【内容真实性】
- 必须使用用户提供的真实数据，不要编造
- 中文与英文混排时，中英文之间留半角空格

【模板: 高管决策简报 / Executive Briefing Memo】
【意图】帮助决策者在 3 分钟内理解问题并拍板。这不是会议纪要、不是周报、不是 PRD。
【适合输入】长会议记录、调研材料、战略讨论、销售反馈、产品数据、投资备忘
【布局】
1. Memo Header: 主题、owner、audience、date、decision deadline
2. Decision Needed: 一句话写清楚需要拍板的问题
3. Recommendation: 明确建议 + confidence level (高/中/低)
4. Why Now: 为什么现在需要决定，不决定的代价
5. Key Facts: 5-7 个事实证据，每条标注来源类型
6. Tradeoff Table: Option A/B/C 对比 upside/cost/risk/reversibility
7. Risks & Mitigations: 3-5 个风险 + 缓解动作
8. Decision Path: approve/reject/ask for more evidence 三种路径
9. Next Actions: owner、due date、expected artifact
10. Evidence Gaps: 缺失的关键信息

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。