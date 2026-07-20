# Mind Skill Registry

Mind 官方 Marketplace skill 的维护仓库。这里保存 skill 内容、附带文件、分类、license 和第三方来源信息。

## 日常协作方式

推荐直接在本仓库目录中使用 Claude Code 或 Codex：

```bash
git clone https://github.com/MedrixAI/mind-skill-registry.git
cd mind-skill-registry
```

然后告诉 agent 要新增或更新什么 skill。Agent 的完整规则在 [`CLAUDE.md`](CLAUDE.md)；Codex 会先读取 [`AGENTS.md`](AGENTS.md)，再按 `CLAUDE.md` 工作。

示例：

```text
请新增一个 <skill-name>，作用是……。
按照仓库 CLAUDE.md 完成内容、分类、license 和校验，先给我检查 diff，不要 push。
```

确认 diff 后，由 agent commit、push 并创建 PR。PR 通过 CI 和所需审核后合并到 `main`。

## Skill 全景目录

[`skill-catalog.html`](skill-catalog.html) 是 Builtin 与 Marketplace Skill 的可交互清单。下载或克隆仓库后可直接打开，支持发布类型、分类、来源筛选和关键词搜索，并提供对应 GitHub 来源链接。

任何 Marketplace Skill 增删改都必须在同一变更中刷新该 HTML。具体命令和 Builtin 快照更新方式见 [`CLAUDE.md`](CLAUDE.md#26-interactive-and-cross-repository-catalog-maintenance)。

## 发布链路

Registry 合并不等于上线：

```text
本仓库 PR 合并
  -> Mind Webadmin「Skills / 来源同步」
  -> Mind Webadmin「Skills / 更新队列」检查并批准
  -> Marketplace 上线
```

Webadmin 入口：`https://admin.mind.medrixai.com`。

发布时记录合并后的完整 commit SHA，在更新队列中核对 candidate SHA 和数量后再批准。同步只生成待发布项；批准后才会进入 Marketplace。

## 仓库结构

```text
mind-skill-registry/
├── CLAUDE.md                 # Agent 完整维护规范
├── AGENTS.md                 # Codex 兼容入口，指向 CLAUDE.md
├── categories.yaml           # Marketplace 7 类 taxonomy
├── skill-catalog.html        # Builtin / Marketplace 可交互清单
├── schemas/skill.schema.json # SKILL.md frontmatter schema
├── policies/                 # trust 和 review policy
├── scripts/generate_skill_catalog.py
├── scripts/validate_skills.py
├── tests/test_validate.py
└── skills/<slug>/            # 一个目录一个 skill package
    ├── SKILL.md
    ├── LICENSE / LICENSE.txt
    ├── scripts/              # 可选
    ├── references/           # 可选
    └── assets/               # 可选
```

扫描器递归查找 `SKILL.md`，发现后的目录就是 package root，其下文件属于同一个 skill。当前 package 使用 `skills/<slug>/` 平铺结构。

## Marketplace 分类

新内容只使用 `categories.yaml` 中的 canonical slug：

| Slug | 中文 | 旧别名 |
|---|---|---|
| `general` | 通用 | — |
| `development-tools` | 开发工具 | `code` |
| `content-creation` | 内容创作 | `writing`, `image`, `slides`, `video`, `web` |
| `data-analysis` | 数据分析 | `data` |
| `productivity-tools` | 效率工具 | — |
| `business-operations` | 商业运营 | — |
| `knowledge-learning` | 知识与学习 | `learning` |

具体 frontmatter、稳定 `mind.id`、第三方 vendoring 和分类规则由 `CLAUDE.md` 说明。

## Marketplace 本地化与输入提示

Skill 可通过 JSON string 类型的 `metadata.mind.presentation` 配置多语言
Marketplace 描述和多条可直接发送的 starter prompts。`default_locale` 的描述必须
与顶层 canonical `description` 一致；加号激活 Skill 时默认使用当前语言的第一条
prompt。locale entry 一旦选中，其 prompts 独立生效；缺省或空数组表示该语言没有
prompts，不会继承默认语言。完整 shape、限制和示例见 [`CLAUDE.md`](CLAUDE.md#85-marketplace-presentation)。

## 本地校验

```bash
python3 -m pip install pyyaml  # 仅缺少依赖时
python3 scripts/validate_skills.py
python3 tests/test_validate.py
python3 scripts/generate_skill_catalog.py --check
git diff --check
```

Validator 会检查 frontmatter、`mind.*` 字段、分类关系并计算 package digest。脚本文件允许作为 bundled file 存在，validator 会输出 `INFO`；脚本仍必须按 `policies/review-policy.yaml` 完成安全审查。

## 重要边界

- `mind.id` 是已发布 skill 的稳定身份，更新或移动目录时不能更换。
- `mind.presentation` 只负责 Marketplace 展示和 chat starter prompts，不替代 Agent discovery 使用的顶层 `description`。
- 本仓库是公开仓库，禁止提交 secrets、cookie、token、私钥、客户数据或生产凭据。
- 第三方内容必须固定 upstream commit，并记录 license 和来源证据。
- 从 Git 删除 package 不会自动下架线上旧 skill；必须先在 Webadmin 下架。
- Skill 内容在本仓库维护；摘要、展示图、精选、推荐、排序和下架在 Webadmin 维护。

## License

仓库根目录 Apache-2.0 license 只覆盖 Registry tooling/schema。每个 skill package 记录自己的 license；第三方 package 按需携带 `NOTICE` / `MODIFICATIONS.md`。
