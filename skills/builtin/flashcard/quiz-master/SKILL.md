---
name: quiz-master
description: 为知识库内容生成高质量选择题（quiz）。优先路径是 Go handler 单次调用 LLM 输出 JSON 题库；该 skill 仅当 agent 兜底时使用，输出严格 JSON 而非 HTML。
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.quiz-master
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: flashcard
  mind.tags: '["artifact-template","flashcard"]'
---
# Quiz Master — 选择题生成器

为知识库内容生成可自测的选择题题库。

## 输出 JSON 结构（严格）

不要包裹 markdown 代码块，直接输出 JSON 对象：

```json
{
  "questions": [
    {
      "type": "single",
      "question": "题干文字",
      "options": ["选项A","选项B","选项C","选项D"],
      "correct_index": [0],
      "explanation": "为什么选这个的简要说明",
      "source": "引用的文件名或 chunk 编号（可选）",
      "difficulty": "easy|medium|hard"
    }
  ]
}
```

## 出题原则

- 数量按用户 `count` 参数（默认 10，上限 30）
- 题型：single（单选，correct_index 长度 1）/ multiple（多选，长度 ≥ 2）/ mixed
- 难度：easy（基础事实）/ medium（核心概念应用）/ hard（细节辨析与综合）
- 选项 4 个为佳；选项之间互不重复且互斥（多选除外）
- correct_index 是基于 0 的下标
- 题目和答案必须能在知识库材料中找到依据，不编造

## 质量准则

- 干扰项要"看似正确但有具体出错的点"，避免明显错误
- 题干清晰，单题只考一个知识点
- 解释要点出关键词，便于复习
