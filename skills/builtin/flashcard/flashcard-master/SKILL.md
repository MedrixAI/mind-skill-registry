---
name: flashcard-master
description: 将知识库内容生成高质量交互式 HTML 闪卡（Flashcard）。采用 genai-rag 两阶段模式：先提取核心概念（Extraction），再转化为问答对（Transformation），生成可在浏览器直接使用的翻转闪卡页面。适用于：知识复习、考试备考、概念记忆等学习场景。
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.flashcard-master
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: flashcard
  mind.tags: '["artifact-template","flashcard"]'
  mind.runtime-default: 'true'
---
# Flashcard Master — 交互式 HTML 闪卡生成器

将知识库内容转化为精美的交互式 HTML 闪卡，支持翻转动画和学习进度追踪。

## 工作流程（genai-rag 两阶段模式）

### Phase 1: 内容提取（Extraction）

使用 `list_knowledge_chunks` 获取知识库所有文档的解析文本块。

**提取策略**：
- 识别文档中的核心概念、定义、公式、重要事实
- 过滤冗余内容，保留信息密度高的片段
- 按主题分组，确保覆盖全面

**提取目标**（根据用户指定的数量）：
- 每个概念/定义 → 1 张闪卡
- 每个重要事实/数据 → 1 张闪卡
- 每个流程/步骤 → 1 张闪卡（问：流程是什么？答：步骤列表）

### Phase 2: 转化生成（Transformation）

将提取的内容转化为问答对格式：

**问题（Front）设计原则**：
- 简洁明确，一个问题只问一件事
- 使用"什么是...？"、"...的作用是？"、"如何...？"等句式
- 避免过于宽泛的问题

**答案（Back）设计原则**：
- 简洁完整，通常 1-3 句话
- 包含关键词和核心要点
- 如有数字/公式，精确呈现

### Phase 3: HTML 生成

生成完整的交互式 HTML 闪卡页面，包含：

**功能特性**：
- 点击/空格键翻转卡片（CSS 3D 翻转动画）
- 左右箭头键或按钮切换卡片
- 进度显示（当前第 X 张 / 共 Y 张）
- 学习模式：标记"已掌握"/"需复习"
- 随机打乱顺序按钮
- 键盘快捷键提示

**视觉设计**：
- 卡片正面：深色背景 + 白色问题文字（突出问题）
- 卡片背面：浅色背景 + 深色答案文字
- 流畅的 3D 翻转动画（0.6s ease）
- 进度条显示学习进度
- 响应式设计，支持移动端

**技术规范**：
- 完整自包含 HTML（`<!DOCTYPE html>` 开头）
- 通过 CDN 引入 Tailwind v3 Play
- 中文字体：Noto Sans SC
- 所有闪卡数据内嵌在 JavaScript 数组中
- 无需后端，可离线使用

### Phase 4: 提交结果

生成完整 HTML 后，调用 `submit_html` 提交。

## 示例闪卡结构

```javascript
const flashcards = [
  {
    front: "什么是向量数据库？",
    back: "向量数据库是专门存储和检索高维向量的数据库，支持基于语义相似度的近似最近邻（ANN）搜索，常用于 RAG 系统中存储文档嵌入向量。"
  },
  {
    front: "RAG 的全称是什么？",
    back: "Retrieval-Augmented Generation（检索增强生成）。通过在生成前检索相关文档，为 LLM 提供上下文，减少幻觉并提升回答准确性。"
  }
];
```

## 质量标准

- 内容必须来自知识库，不编造
- 问题清晰，答案准确简洁
- 闪卡数量符合用户要求（默认 20 张）
- 交互流畅，视觉美观
- 颜色对比度 ≥ 4.5（无障碍）
