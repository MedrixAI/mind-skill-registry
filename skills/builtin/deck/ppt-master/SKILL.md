---
name: ppt-master
description: 将知识库内容生成高质量 HTML 演示文稿（幻灯片）。采用 Strategist + Executor 两阶段模式：先分析内容结构和受众，选择最合适的视觉风格，再生成完整的单文件 HTML 幻灯片。目标：生成媲美 NotebookLM 的精美专业演示文稿。
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.ppt-master
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: deck
  mind.tags: '["artifact-template","deck"]'
  mind.runtime-default: 'true'
---
# PPT Master — 高质量 HTML 演示文稿生成器

将知识库内容转化为**视觉精美、专业级**的 HTML 幻灯片演示文稿，风格参考 NotebookLM Studio。

## 核心设计原则

**必须达到的视觉标准**：
- 每张幻灯片都有强烈的视觉冲击力，不是简单的文字堆砌
- 使用渐变背景、卡片布局、图标、数据可视化等视觉元素
- 配色专业统一：深色主题（深蓝/深灰）或浅色主题（白底蓝色调）
- 中文字体使用 Noto Sans SC，英文使用 Inter 或 Manrope
- 每页有明确的视觉层次：大标题 → 副标题 → 内容卡片

## 工作流程

### Phase 1: 内容收集

使用 `list_knowledge_chunks` 工具获取知识库中所有文档的解析文本块。

收集完成后分析：
- 内容主题和核心概念（3-5个）
- 关键数据和统计数字
- 内容类型（技术/商业/学术/医学/教学）
- 目标受众

### Phase 2: 策略规划

1. **先做内部选型，不要把选型暴露给用户**：
   - 通读 full markdown，判断内容意图、受众、证据形态、数据密度和叙事节奏。
   - 从下方"主题系统"中选择 1 个最合适的主题和 1 套固定调色板；不要混用主题，不要临时编造颜色。
   - 最终 HTML 不出现主题选择器、切换按钮或导出 PPTX 按钮。
2. **页数规划**：页数由内容驱动；短内容 8-12 页，标准内容 12-18 页，资料很长时可超过 18 页。每页只承载一个中心论点或一个信息结构。
3. **版式规划**：为每一页指定一个命名版式（见"版式池"），连续 3 页不得使用同一种版式；数据页、解释页、对比页、章节页交替出现。
4. **内容结构**：封面 → 目录/路线图 → 章节 opener → 内容页若干 → 证据/风险/对比 → 总结/下一步。

## 主题系统（根据 full markdown 智能选择）

**主题 = 固定调色板 + 字体层级 + 版式偏好，不是随意换色。必须只选一种。**

1. **Swiss Analysis（默认通用 / 研究 / 产品 / 管理汇报）**
   - 适用：结构化分析、产品说明、医学/行业综述、知识总结。
   - 调色板：paper `#fafaf8`，ink `#0a0a0a`，accent `#002FA7`，muted `#6b7280`，rule `#d9d9d2`。
   - 风格：16 列网格、强标题、1px hairline、直角或 6px 以下圆角，克制留白。

2. **Pitch Board（商业 / 融资 / 增长 / 市场）**
   - 适用：市场规模、机会、用户痛点、方案、竞争、traction、路线图、ask。
   - 调色板：bg `#0b1020`，panel `#111827`，ink `#f8fafc`，accent `#38bdf8`，positive `#34d399`。
   - 风格：深色大标题、强 KPI、市场地图、before/after、roadmap；每页有明确商业结论。

3. **Tech Talk（技术 / 代码 / 架构 / 工程复盘）**
   - 适用：API、架构、部署、性能、安全、工程决策、源码分析。
   - 调色板：bg `#0d1117`，panel `#161b22`，ink `#e6edf3`，accent `#58a6ff`，mono `#7ee787`。
   - 风格：代码块、系统图、命令行片段、依赖图、before/after 性能对比；避免营销化文案。

4. **Course Module（教学 / 培训 / 课程）**
   - 适用：课程材料、学习总结、概念教学、训练营、课堂讲解。
   - 调色板：paper `#fff8ed`，ink `#1f2937`，accent `#ea580c`，support `#2563eb`，soft `#fed7aa`。
   - 风格：学习目标、概念卡、例题/自测、步骤拆解、回顾页；难点逐层递进。

5. **Editorial Keynote（叙事 / 观点 / 趋势 / 临床综述）**
   - 适用：研究综述、临床 review、趋势观察、观点型材料。
   - 调色板：paper `#f5f1e8`，ink `#1c1917`，accent `#9f1239`，muted `#78716c`，rule `#d6d3c7`。
   - 风格：大引言、章节 opener、叙事型时间线、证据脚注、强留白；像被编辑过的演讲稿。

6. **Data Room（数据密集 / 指标 / 对比 / 实验）**
   - 适用：实验结果、benchmark、财务/经营指标、表格密集资料。
   - 调色板：paper `#f8fafc`，ink `#0f172a`，accent `#2563eb`，green `#16a34a`，red `#dc2626`。
   - 风格：KPI ledger、图表、数据表、注释、方法论；所有图形比例必须来自真实数据。

7. **Minimal / Quiet（极简 / 哲学 / 高管简报）**
   - 适用：安静叙事、战略观点、创始人信、哲学/文化主题和低噪声高管简报。
   - 调色板：bg `#ffffff`，ink `#111111`，accent `#111111`，soft `#f2f2f2`，muted `#9a9a9a`。
   - 风格：12 列网格、超大留白、单一小型 accent、强字重层级；无多余卡片和渐变。

8. **Dark Investor（暗色投资 / 种子轮 / 增长故事）**
   - 适用：融资、投资人更新、增长复盘、商业模式和路线图。
   - 调色板：bg `#0e0e10`，panel `#1a1a1d`，ink `#f5f5f5`，accent `#635bff`，mint `#00c896`，muted `#a1a1aa`。
   - 风格：暗画布、超大数字、blurple 高光、traction 图、市场机会和 ask 强收束；每页结论可被单独截屏。

9. **Gradient / Aurora（现代 SaaS / 产品发布 / 开发者工具）**
   - 适用：产品发布、SaaS、开发者工具、新功能演示、路线图和生态叙事。
   - 调色板：bg `#0b0f1a`，panel `#111827`，ink `#ffffff`，accent `#7c3aed`，sky `#0ea5e9`，cyan `#22d3ee`。
   - 风格：极光渐变背景、细网格、玻璃态面板、产品机制图、before/after 和 launch timeline；控制发光面积，保证正文清晰。

10. **Retro / Vintage（复古 / 品牌故事 / 历史回顾）**
   - 适用：品牌传承、历史复盘、文化叙事、人物/组织故事和怀旧主题。
   - 调色板：bg `#ede4d3`，ink `#3a2e1f`，accent `#c04b2c`，olive `#6b5b3e`，muted `#9a8c70`。
   - 风格：旧纸底色、slab serif 标题、半调点纹、徽章编号、时间线；避免过度装饰影响阅读。

11. **Elegant / Luxury（优雅 / 奢华 / 酒店时尚）**
   - 适用：高端品牌、时尚、酒店、艺术、私享活动和精品服务介绍。
   - 调色板：bg `#0f0f0f`，panel `#1a1a1a`，ink `#f5e6c8`，accent `#b8860b`，muted `#8c7a5b`。
   - 风格：黑色画布、金色细线、serif 大标题、大量留白、少量高对比图形；禁止卡片堆叠。

12. **Creative / Illustrated（创意 / 插画 / Agency）**
   - 适用：创意提案、品牌 campaign、工作坊、轻量课程、团队活动和面向大众的科普。
   - 调色板：bg `#fffdf7`，ink `#1f2933`，accent `#2d6a4f`，blue `#3a86ff`，yellow `#ffbe0b`，coral `#ff6b6b`。
   - 风格：内联 SVG 插画、贴纸式编号、手绘箭头、活泼版面；仍保持 16:9 网格和严格不重叠。

**主题选择规则（内部执行，不输出给用户）**：
- 通用研究/产品/管理：Swiss Analysis；商业融资：Pitch Board 或 Dark Investor；技术/代码：Tech Talk；教学：Course Module。
- 医学/趋势/观点叙事：Editorial Keynote；数据/实验/财务指标：Data Room；极简高管观点：Minimal / Quiet。
- 产品发布/SaaS/dev-tool：Gradient / Aurora；品牌历史：Retro / Vintage；高端品牌：Elegant / Luxury；大众传播或创意提案：Creative / Illustrated。
- 一份 deck 只选一种主题和一套调色板；不要在 HTML 中加入主题选择器、主题切换按钮或 Export PPTX / 导出 PPTX 按钮。

## 版式池（命名可复用，按内容语义选择）

- **P01 Cover Signal**：主题色满版/大标题/副标题/来源数量/日期。
- **P02 Agenda Map**：目录或路线图，4-7 个章节锚点，点击可跳转。
- **P03 Chapter Opener**：章节编号 + 一句话结论 + 大留白。
- **P04 Big Claim**：一个核心判断，占据画面 60% 以上，配 2-3 条证据。
- **P05 KPI Ledger**：3-5 个大数字，单位、口径、来源说明齐全。
- **P06 Evidence Cards**：3-6 张证据卡，每张含结论、依据、限制。
- **P07 Mechanism Diagram**：流程/机制/因果链，用 CSS/SVG 节点与箭头。
- **P08 Before After**：左右对比，适合方案前后、版本差异、策略取舍。
- **P09 Timeline**：水平或垂直时间线，适合历史、流程、研究进展。
- **P10 Matrix**：2x2、三列表、风险-收益矩阵或优先级矩阵。
- **P11 Code/System Sheet**：技术主题专用，架构图 + 代码/配置片段 + 注释。
- **P12 Course Step**：教学主题专用，目标 → 概念 → 示例 → 自测。
- **P13 Quote Pull**：Editorial 专用，大引言 + 解释 + 来源脚注。
- **P14 Data Chart**：固定高度 Chart.js/SVG 图表 + 结论标题 + 口径说明。
- **P15 Risk & Mitigation**：风险、影响、缓解动作三栏。
- **P16 Closing Actions**：3-5 个结论或下一步，带 owner/优先级/时间。

## 严谨结构规则

- 每页必须有一个"页标题 = 结论句"，不要只写名词标题。
- 每页正文不超过 5 个 bullet；每个 bullet 不超过 18 个中文字符或 14 个英文词。长解释拆到备注/脚注或下一页。
- 图表页必须写清口径、时间范围、样本或来源；没有真实数值时使用结构图，不要伪造图表。
- 目录锚点和上一页/下一页按钮必须可点击；键盘 ← / → / Space 必须可用；首屏无脚本也能看到第一页。
- 16:9 画布内所有元素不得重叠；固定页脚显示 `N / Total`；不要生成 Export PPTX / 导出 PPTX 按钮。
- 第一张 `.slide` 在静态 HTML 中必须直接带 `active` 类，且 CSS 必须让 `.slide.active` 可见；不要只依赖 `DOMContentLoaded` 或脚本再激活第一页。
- 每张 `.slide` 固定 1280×720 或等比例 16:9，内容过多时拆页，不缩小到不可读；标题、图表、页脚不得被 `overflow:hidden` 裁掉。
- 需要滚动的长表格只能放在局部表格容器内，整张幻灯片本身不滚动；导出截图必须和前端预览一致。

### Phase 3: HTML 生成

生成完整的单文件 HTML，**严格遵循以下视觉规范**：

#### 必须包含的视觉元素

**封面页（第1页）**：
- 全屏渐变背景（深色为主）
- 大号主标题（font-size: 3-4rem，白色或亮色）
- 副标题（font-size: 1.2-1.5rem，半透明白色）
- 装饰性几何图形（SVG圆形、线条等）
- 底部信息栏（日期、来源数量等）

**目录页（第2页）**：
- 编号列表，每项有图标或色块
- 悬停效果

**内容页**：根据内容类型选择以下布局之一：

1. **KPI卡片布局**（适合数据/统计）：
```
3列卡片，每卡片：大数字 + 单位 + 说明文字
卡片有渐变背景或彩色左边框
```

2. **左图右文布局**（适合概念解释）：
```
左侧：SVG图标或数据图表（占40%）
右侧：标题 + 3-4个要点（每点有彩色圆点）
```

3. **时间线布局**（适合历史/流程）：
```
水平或垂直时间线，节点有圆圈+年份+描述
```

4. **对比布局**（适合比较分析）：
```
两列对比，各有标题+要点，中间有分隔线
```

5. **流程图布局**（适合步骤/机制）：
```
横向箭头流程，每步有图标+标题+简短说明
```

**总结页（最后页）**：
- 关键要点回顾（3-5条，带图标）
- 行动号召或结论

#### CSS 规范

```css
/* 必须使用的字体 */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700;900&family=Inter:wght@400;500;600;700;800&display=swap');

/* 幻灯片容器 */
.slide {
  width: 1280px;
  height: 720px;
  position: relative;
  overflow: hidden;
  font-family: 'Noto Sans SC', 'Inter', sans-serif;
}

.slide:not(.active) {
  opacity: 0;
  pointer-events: none;
}

.slide.active {
  opacity: 1;
  pointer-events: auto;
}

/* 卡片样式 */
.card {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 12px;
  padding: 24px;
  backdrop-filter: blur(10px);
}

/* 强调数字 */
.stat-number {
  font-size: 3rem;
  font-weight: 900;
  background: linear-gradient(135deg, #60a5fa, #34d399);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

#### JavaScript 规范

```javascript
// 幻灯片切换（必须实现）
let current = 0;
const slides = document.querySelectorAll('.slide');

function goTo(n) {
  slides[current].classList.remove('active');
  current = (n + slides.length) % slides.length;
  slides[current].classList.add('active');
  updateProgress();
}

document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' || e.key === ' ') goTo(current + 1);
  if (e.key === 'ArrowLeft') goTo(current - 1);
});

// 顶部进度条
function updateProgress() {
  document.getElementById('progress').style.width = 
    ((current + 1) / slides.length * 100) + '%';
}
```

#### 数据可视化

- **柱状图/折线图**：使用 Chart.js（CDN: `https://cdn.jsdelivr.net/npm/chart.js`）
- **流程图**：使用纯 CSS + SVG 箭头，不依赖外部库
- **图标**：使用内联 SVG，不引用外部图片

### Phase 4: 提交

生成完整 HTML 后调用 `submit_html` 提交。

## 质量检查清单

生成前自检：
- [ ] 封面有渐变背景和大号标题？
- [ ] 每页都有视觉元素（图标/图表/卡片），不是纯文字？
- [ ] 配色统一，有主色调和强调色？
- [ ] 数据用图表或大数字卡片展示，不是文字描述？
- [ ] 字体正确（Noto Sans SC + Inter）？
- [ ] 键盘导航和进度条已实现？
- [ ] 内容来自知识库，无编造？

## 技术要求

- HTML 完整自包含（`<!DOCTYPE html>` 开头，`</html>` 结尾）
- 通过 CDN 引入 Google Fonts 和 Chart.js
- 不引用外部图片，使用 CSS/SVG 内联
- 支持键盘 ← / → / Space 切换幻灯片
- 顶部进度条显示当前位置
- 16:9 比例（1280×720px）
- 颜色对比度 ≥ 4.5（无障碍）

## anti-slop（用可执行量，禁用氛围词）
- 禁用 premium / magazine-grade / rich / futuristic / professional / 高级感 / 精美 等氛围词；改写为可执行量，例如"封面渐变 + 3 张 KPI 卡 + 1 个机制图（4 节点）+ 1 个对比表 + 顶部进度条 + 键盘导航"。
- 不编造内容；中英文混排留半角空格。

---
> 共享基线（CDN allowlist / 设计 token / 硬性技术要求 / 响应式 / 无障碍）见 `skills/enhancements/base.md`，运行时由全局 system prompt 注入、由 `htmlassets.ValidateHTML` 强制；本 skill 仅定义版面/组件/场景差量。
