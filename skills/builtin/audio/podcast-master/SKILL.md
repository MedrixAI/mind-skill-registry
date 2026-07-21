---
name: podcast-master
description: 为知识库内容生成 NotebookLM 风格的双主播播客脚本（Host A / Host B 对话）。仅当 audio_overview 生成失败时由 agent 兜底使用；优先路径为 Go handler 直接调用 LLM 产 JSON 脚本再走 MiniMax TTS。该 skill 输出严格 JSON，不输出 HTML。
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.podcast-master
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: audio
  mind.tags: '["artifact-template","audio"]'
---
# Podcast Master — 双主播播客脚本

把知识库内容转化为高质量的双人播客对话脚本。

## 工作流程

### Phase 1: 内容收集
使用 `list_knowledge_chunks` 获取知识库的文本块。

### Phase 2: 编剧拆解
按"开场（hook）→ 主体（layer-by-layer）→ 收尾（takeaway/CTA）"三段式拆解，定下：
- 主播 A：发起话题、提问、串场、收尾
- 主播 B：深入解读、举例、提供专家视角
- A、B 严格交替，第一段为 A 的开场，最后一段为 A 的总结

### Phase 3: 输出 JSON
严格按照下面 schema 输出，不要包裹 markdown 代码块：

```json
{
  "title": "本期播客标题（≤30字）",
  "segments": [
    {"speaker": "A", "text": "...", "emotion": "happy"},
    {"speaker": "B", "text": "...", "emotion": "neutral"}
  ]
}
```

## 硬性要求
- 每段 text 单行 60-150 个汉字（约 5-12 秒），便于 TTS 自然停顿
- emotion 仅能取：neutral / happy / sad / angry / surprised / fearful / disgusted（默认 neutral）
- 内容必须基于知识库材料，不编造；可适当口语化补充连接词
- 标题与对话自然契合，避免老套的"今天我们要讲……"
