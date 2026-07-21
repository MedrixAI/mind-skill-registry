# Mind Skill Registry

Mind 官方 Builtin 与 Marketplace skill 的唯一维护仓库。这里保存 skill 内容、附带文件、运行分类、Marketplace 分类、license 和第三方来源信息。

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

[`skill-catalog.html`](skill-catalog.html) 是 Builtin 与 Marketplace Skill 的可交互清单。下载或克隆仓库后可直接打开，支持发布类型、分类、来源筛选、关键词搜索、Marketplace 展示语言切换和 starter prompts 预览，并提供对应 GitHub 来源链接。

任何 Skill 增删改都必须在同一变更中刷新该 HTML。具体命令见 [`CLAUDE.md`](CLAUDE.md#26-interactive-and-cross-repository-catalog-maintenance)。

## 发布链路

Registry 合并不等于上线：

```text
本仓库 PR 合并
  -> Mind Webadmin「Skills / 来源同步」
  -> Mind Webadmin「Skills / 更新队列」检查并批准
  -> Builtin: unlisted + tenant 无需订阅即可 available
     Marketplace: listed + tenant subscription 后 available
  -> Agent 按 all / selected / none activation policy 使用
```

Webadmin 入口：`https://admin.mind.medrixai.com`。

发布时记录合并后的完整 commit SHA，在更新队列中核对 candidate SHA 和数量后再
批准。同步只生成待发布项；批准后才会进入对应的数据库运行 lane。

官方 source 使用 `source_type=github_repo`、`branch=main`、
`sub_path=skills`、`trust_profile=official_registry` 和
`auto_update=review`。Builtin 批准后进入 tenant 可用集但保持 unlisted 且无需
subscription；Marketplace 批准后才进入可发现、可订阅状态。两者仍需进入具体
Agent 的 `all` 或 `selected` activation policy 才能由该 Agent `read_skill`；
`available` 不等于对所有 Agent 自动激活。不存在 filesystem
`directory/dir_path` source 或 mind-api repo-local Skill 回退。

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
└── skills/
    ├── builtin/<runtime-category|general>/.../<slug>/
    └── marketplace/<market-primary>/.../<slug>/
        ├── SKILL.md
        ├── LICENSE / LICENSE.txt
        ├── scripts/          # 可选
        ├── references/       # 可选
        └── assets/           # 可选
```

扫描器递归查找 `SKILL.md`，发现后的目录就是 package root，其下文件属于同一个 skill。`builtin`、`marketplace`、category 和更深的中间目录只用于组织；同步后的 `source`、运行分类和能力完全由 frontmatter 决定。package 之间不能互相嵌套。

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

当前发布基线（2026-07-21）：

| 项目 | 覆盖 |
|---|---:|
| Builtin Skill | 95 |
| Marketplace Skill | 94 |
| 含 `mind.presentation` | 93 / 94 Marketplace |

同日生产迁移验收：官方 source `74d694f9-be91-4498-a921-a0d1a80fa80a`
在候选 commit `02a469a7ce27a065a22842a803c0fa58d4ec5160` 生成的 184 个候选已全部
批准，更新队列为 0；95 个 Builtin 均 approved+enabled+unlisted，94 个
Marketplace 均 approved+enabled+listed。后续 docs-only commit 可让 source
provenance 前移而不改变 package digest 或产生候选；实时状态仍以 Webadmin/数据库
为准。`skill-catalog.html` 只表达当前 Git package inventory，不伪装成实时审批面板。

维护任一 Skill 时必须继续满足 presentation 合同，并重新生成
`skill-catalog.html`。Catalog 的语言选择只影响离线目录展示；线上 Marketplace
仍根据用户 UI locale 解析 description 与 starter prompts。

## 本地校验

```bash
python3 -m pip install pyyaml  # 仅缺少依赖时
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_skills.py
PYTHONDONTWRITEBYTECODE=1 python3 tests/test_validate.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_skill_catalog.py --check
git diff --check
```

Validator 会检查 frontmatter、lane/目录关系、稳定身份唯一性、运行分类/默认项/能力、Marketplace 分类关系，并计算 package digest。脚本文件允许作为 bundled file 存在，validator 会输出 `INFO`；脚本仍必须按 `policies/review-policy.yaml` 完成安全审查。

## 重要边界

- `mind.id` 是已发布 skill 的稳定身份，更新或移动目录时不能更换。
- `mind.distribution` 只决定 Builtin/Marketplace 的发布与 tenant availability lane；
  不替代 Agent activation policy，也不需要额外 frontmatter 字段表达 activation。
- `mind.presentation` 只负责 Marketplace 展示和 chat starter prompts，不替代 Agent discovery 使用的顶层 `description`。
- 本仓库是公开仓库，禁止提交 secrets、cookie、token、私钥、客户数据或生产凭据。
- 第三方内容必须固定 upstream commit，并记录 license 和来源证据。
- 从 Git 删除 package 不会自动下架线上旧 skill；必须先在 Webadmin 下架。
- Skill 内容、canonical summary 和 presentation 在本仓库维护；展示图、精选、推荐、
  排序和上下架在 Webadmin 维护。若 Webadmin 临时覆盖官方 summary/presentation，
  需要回写 Registry，避免下次同步产生漂移。

## License

仓库根目录 Apache-2.0 license 只覆盖 Registry tooling/schema。每个 skill package 记录自己的 license；第三方 package 按需携带 `NOTICE` / `MODIFICATIONS.md`。
