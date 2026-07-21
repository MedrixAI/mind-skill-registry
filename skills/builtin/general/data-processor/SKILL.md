---
name: 数据处理器
description: 数据处理与分析技能。当用户需要对知识库检索结果进行数据分析、统计计算、格式转换、数据提取或生成报告时使用此技能。支持 Python 脚本执行进行高级数据处理。
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.data-processor
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
---
# Data Processor

企业级知识库数据处理与分析技能，用于处理 RAG 检索结果和执行数据分析任务。

## 核心能力

1. **数据分析**: 对检索到的文档数据进行统计分析
2. **格式转换**: JSON/CSV/Markdown 等格式相互转换
3. **数据提取**: 从非结构化文本中提取结构化信息
4. **报告生成**: 生成数据分析报告和摘要

## 使用场景

当用户请求涉及以下内容时，使用此技能：
- "分析这些数据"、"统计一下"、"计算总数/平均值"
- "转换为 JSON/CSV 格式"
- "提取关键信息"、"整理成表格"
- "生成报告"、"数据汇总"

## 可用脚本

### 1. analyze.py - 数据分析脚本

分析输入的 JSON 数据，生成统计报告。

此脚本需要业务 JSON stdin，因此使用“先读脚本、再落任务临时文件、最后执行”的两步通用 shell 流程。Skill 文件不会自动出现在 shell workspace。

1. 调用 `read_skill(skill_ref="<当前 Skill 的 canonical skill_ref>", file_path="scripts/analyze.py")`，保存返回的脚本文本。
2. 将脚本文本作为 stdin 安全写入任务临时文件；命令会输出文件路径：

```text
shell(
  command="tmp=$(mktemp /tmp/data-processor-analyze.XXXXXX.py) && cat > \"$tmp\" && printf '%s\\n' \"$tmp\"",
  stdin=<read_skill 返回的脚本文本>
)
```

3. 使用上一步 stdout 返回的路径执行脚本，把业务 JSON 放在这次调用的 stdin，并在退出时清理临时文件：

```text
shell(
  command="tmp='<上一步返回路径>'; trap 'rm -f \"$tmp\"' EXIT; python \"$tmp\"",
  stdin="{\"items\": [1, 2, 3], \"query\": \"统计分析\"}"
)
```

不要把脚本文本或业务 JSON 拼接进 `command`。`--file` 仅能指向已通过其他工具放入 shell workspace 的真实数据文件。

**输入格式**:
```json
{
  "items": [数据项数组],
  "query": "可选的查询描述"
}
```

**输出**: JSON 格式的统计结果，包含计数、求和、平均值等。

### 2. format_converter.py - 格式转换脚本

在 JSON、CSV、Markdown 表格之间转换数据。

**用法**：先用 `read_skill(skill_ref="<当前 Skill 的 canonical skill_ref>", file_path="scripts/format_converter.py")` 取得脚本文本，按 `analyze.py` 的任务临时文件流程写入，再用通用 shell 执行临时文件。格式参数写在 `command`，待转换数据写在 `stdin`。例如 JSON 转 CSV 的执行调用为 `shell(command="tmp='<返回路径>'; trap 'rm -f \"$tmp\"' EXIT; python \"$tmp\" --to csv", stdin="[{\"name\":\"A\",\"value\":1}]")`。

### 3. extract_info.py - 信息提取脚本

从文本中提取结构化信息（数字、日期、关键词等）。

**用法**：先用 `read_skill(skill_ref="<当前 Skill 的 canonical skill_ref>", file_path="scripts/extract_info.py")` 取得脚本文本并按上述流程写入任务临时文件，再调用 `shell(command="tmp='<返回路径>'; trap 'rm -f \"$tmp\"' EXIT; python \"$tmp\"", stdin="2024年销售额为100万元，同比增长15%")`。

**输出**:
```json
{
  "numbers": ["100", "15"],
  "dates": ["2024年"],
  "percentages": ["15%"],
  "amounts": ["100万元"]
}
```

## 处理流程

### 分析 RAG 检索结果

当需要分析知识库检索结果时：

1. 收集检索到的文档片段
2. 提取关键数据点
3. 使用 `analyze.py` 进行统计
4. 整理并呈现分析结果

**示例**：
```
用户: "帮我统计知识库中提到的所有产品销售数据"

步骤:
1. 使用 knowledge_search 检索相关文档
2. 整理数据为 JSON 格式
3. 调用 read_skill(skill_ref="<当前 Skill 的 canonical skill_ref>", file_path="scripts/analyze.py") 获取脚本文本
4. 用第一次 shell 调用将脚本文本通过 stdin 写入任务临时文件
5. 用第二次 shell 调用执行临时文件，并通过 stdin 传入业务数据
6. 解析输出并生成报告
```

### 数据格式转换

当用户需要特定格式输出时：

1. 整理数据为标准 JSON 格式
2. 使用 `format_converter.py` 转换
3. 返回目标格式结果

## 最佳实践

1. **数据预处理**: 调用脚本前，确保数据格式正确
2. **错误处理**: 检查脚本执行结果，处理异常情况
3. **结果验证**: 验证输出结果的合理性
4. **渐进处理**: 大数据量时分批处理

## 输出格式

分析结果示例：
```markdown
## 数据分析报告

### 基本统计
- 数据条数: 50
- 数值总和: 1,234,567
- 平均值: 24,691.34
- 最大值: 99,999
- 最小值: 100

### 分布情况
| 区间 | 数量 | 占比 |
|------|------|------|
| 0-1000 | 10 | 20% |
| 1000-10000 | 25 | 50% |
| >10000 | 15 | 30% |

### 结论
根据数据分析，XXX...
```

## 注意事项

- 脚本只在当前 Agent 已授权通用 shell 时执行
- 工作目录、超时和隔离策略由通用 shell 决定
- 输入数据大小有限制，大文件请分批处理
- 脚本输出为 JSON 格式，便于后续处理
