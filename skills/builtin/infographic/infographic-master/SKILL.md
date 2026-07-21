---
name: infographic-master
description: 将知识库内容生成精美的单页信息图（Infographic）HTML。Tailwind v3 Play CDN + Chart.js + Heroicons CDN，单文件自包含可双击打开。适用于：年终总结、数据洞察、流程概览、对比分析等可视化场景。
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.infographic-master
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: infographic
  mind.tags: '["artifact-template","infographic"]'
  mind.runtime-default: 'true'
---
# Infographic Master — 信息图生成器

把知识库内容转化为一张高密度、易读、可分享的单页信息图。

## 工作流程

### Phase 1: 内容收集
使用 `list_knowledge_chunks` 获取知识库的文本块，重点抽取：
- 核心观点 / 结论（Hero 大标题区）
- 关键数字 / 占比（KPI 卡片、Donut/Bar 图）
- 步骤 / 阶段 / 时间线（Timeline、Flow）
- 对比项（双栏对比、矩阵）
- 引用 / 来源（页脚 References）

### Phase 2: 视觉规划
依据 `params.style` 选定布局：
- `modern`：大标题 + 4-6 个 KPI 卡 + 1-2 张主图 + 流程时间线
- `minimal`：简洁双色，多空白，仅 1 张主图 + 关键句
- `data_dense`：多张图并列，KPI 网格，密集信息
- `timeline`：以时间线为主轴串联所有要点
- `comparison`：左右双栏 / 矩阵对比

### Phase 3: HTML 生成
输出完整自包含的单页 HTML：

**头部 CDN**：
```html
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700;900&family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
```

**视觉规范**：
- 1 个主色 + 2 个中性色 + 1 个强调色，杜绝纯黑纯白
- 8px 基线网格，标题/正文层级清晰
- 颜色对比度 ≥ 4.5（WCAG AA）
- 中文优先 Noto Sans SC，英文优先 Inter
- 大标题字重 700+，营造海报感

**内容真实性**：
- 所有数字 / 引用必须出自知识库；如材料缺数字，用文字概述代替图表
- 不允许出现编造的统计数字

### Phase 4: 提交
调用 `submit_html` 提交完整 HTML。
