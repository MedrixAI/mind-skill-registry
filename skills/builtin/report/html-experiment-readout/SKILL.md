---
name: html-experiment-readout
description: 'Generate an Experiment Readout as a single-file HTML document. 假设 + 指标 + 结果 + 解释 + 决策, 把 A/B 或产品实验转成行动建议. Category: data / product. Best for: product & growth. Format: 产品实验报告.'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-experiment-readout
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: report
  mind.tags: '["artifact-template","report"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/experiment-readout/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/experiment-readout/SKILL.md"]'
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
- 排版: 中文优先 Noto Sans SC / Noto Serif SC, 英文 Inter / Manrope, 数字 Tabular Nums
- 色彩: 1 个主色 + 2 个中性色 + 至多 1 个强调色; 大胆留白; 不使用纯黑纯白 (#000/#fff)
- 网格: 8px 基线; 段落最大宽度 65ch; 标题与正文有清晰层级
- 微观细节: 圆角统一, 投影柔和, 边框 1px
- 无障碍: 颜色对比度 ≥ 4.5

【组件库】
- 决策徽章: .decision-badge (text-2xl font-bold px-6 py-3 rounded-2xl), 🟢 SHIP / 🟡 ITERATE / 🔵 EXTEND / 🔴 STOP
- 指标增量卡: .metric-delta (bg-gradient-to-br rounded-2xl p-6 text-white), 大字显示 primary metric lift + 绝对 delta + 置信度
- 指标对比表: .metric-table (w-full), Control vs Variant, primary + secondary + guardrail 指标
- 置信度指示: .confidence-indicator (inline-flex items-center gap-2), 用 pill 标签显示 "Statistically Significant" / "Directional" / "Inconclusive"
- 实验设置卡: .setup-card (bg-gray-50 rounded-xl p-4), audience / variant / duration / sample size
- 后续实验卡: .followup-card (border rounded-xl p-4 hover:shadow-md), hypothesis + expected impact + effort (用 S/M/L 标签)

【推荐 CDN 资源】
- 图表: Chart.js (https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js) — 用于 lift 柱状图、时间序列趋势
- 图标: Lucide (https://unpkg.com/lucide@latest/dist/umd/lucide.js)

【配色方案】
- 主色: #6366f1 (Indigo-500) — 数据/分析
- 中性色: #fafafa (Neutral-50), #737373 (Neutral-500)
- 强调色: #22c55e (Green-500) — 正向; #ef4444 (Red-500) — 负向; #f59e0b (Amber-500) — 方向性
- 可选深色主题: bg #0a0a0a, 主色 #818cf8, 强调色 #4ade80

【内容真实性】
- 必须使用用户提供的真实数据，不要编造
- 中文与英文混排时，中英文之间留半角空格

【模板: 实验复盘 / Experiment Readout】
【意图】回答"这个实验说明了什么，下一步应该上线、停止、继续跑，还是重新设计?"
【适合输入】A/B test、增长实验、定价实验、onboarding 改版、功能灰度、邮件实验
【布局】
1. Header: 实验名称、owner、日期、实验状态、decision badge
2. Hypothesis: 原始假设，改写成可验证句式
3. Setup: audience、variant、duration、sample size、primary metric、guardrail metrics
4. Result Snapshot: primary metric lift + 绝对 delta + sample + confidence / caveat
5. Metric Table: Control vs Variant, primary + secondary + guardrail
6. Chart: Lift 柱状图或时间序列趋势 (Chart.js)
7. Interpretation: 解释结果为什么发生，区分 signal/noise/unknown
8. Decision: Ship / Iterate / Extend / Stop 四选一 + 理由
9. Follow-up Experiments: 2-4 个下一步实验
10. Instrumentation Notes: 数据缺口、埋点问题、样本偏差

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。