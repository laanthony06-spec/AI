---
type: audit-report
source: [[00.raw-materials/90.processed/agent-knowledge-ops/2026-06-16_AI时代Obsidian工作台搭建SOP.md]]
created: 2026-07-07
tags: [Obsidian, SOP检查, AgentKnowledgeOps, Vault治理]
status: action-required
---

# Obsidian 工作台 SOP 符合性检查

## 检查结论

当前 vault 已经具备 **原始资料归档、自动 OCR / 知识提纯、AI / 半导体情报采集、Agent Knowledge Ops 看板** 等核心能力。  
主要缺口集中在：**Git / GitHub 备份、Obsidian 插件生态、附件规则、Web Clipper / 飞书 / 发布工作流、安全扫描**。

## 已具备能力

| 模块 | 状态 | 说明 |
|---|---|---|
| 本地 Obsidian vault | 已具备 | 当前路径稳定：`D:\Obsidian\work\OBSidianCodex` |
| 原始资料区 | 已具备 | `00.raw-materials` 已拆分为 sources / metadata / processed / system |
| 领域知识区 | 已具备 | `30.areas` 已包含 Agent、AI 情报、半导体派工情报 |
| 自动化任务 | 已具备 | 4 个 Windows 计划任务均为 Ready |
| Agent Knowledge Ops | 已具备 | Dashboard、Evidence、Memory、Hooks、Task Queue 已存在 |
| X 推文剪藏 | 部分具备 | 已有 `x-tweets` 文件夹与结构化记录 |
| 原始资料提纯 | 已具备 | 已有 weekly knowledge distill 与 OCR 产物 |
| 敏感配置局部忽略 | 部分具备 | 子目录 `.gitignore` 已忽略部分 `.env` |

## 需要增加 / 修复的项目

### P0：Git / GitHub 备份能力需要补齐

检查发现：

- 系统命令中未找到 `git`
- vault 根目录没有 `.gitignore`
- `.git` 目录存在但未发现有效 `.git/config`

建议：

- [ ] 安装 Git for Windows
- [ ] 确认 `git` 能在 PowerShell 中运行
- [ ] 初始化或修复当前 vault 的 Git 仓库
- [ ] 连接 GitHub Private 仓库
- [ ] 在根目录创建 `.gitignore`

建议根目录 `.gitignore` 至少包含：

```gitignore
.env
**/.env
**/.venv/
**/__pycache__/
**/*.pyc
*.log
.obsidian/workspace.json
.obsidian/workspace-mobile.json
```

### P0：敏感信息保护需要升级为全局规则

当前 `.env` 存在于：

- `30.areas/ai-agent-intel/.env`
- `30.areas/semiconductor-dispatch-intel/.env`

虽然子目录有 `.gitignore`，但根目录缺少全局 `.gitignore`，未来如果 Git 初始化位置变化，仍有误提交风险。

建议：

- [ ] 建立根目录 `.gitignore`
- [ ] 建立敏感信息扫描脚本
- [ ] 在 Agent Knowledge Ops 中加入“提交前检查密钥”的任务

### P1：Obsidian 插件生态需要补齐

当前启用的社区插件只有：

- `realclaudian`

SOP 推荐但当前未检测到的插件：

- [ ] Obsidian Git
- [ ] Custom Attachment Location
- [ ] Advanced Tables
- [ ] Excalidraw
- [ ] Terminal
- [ ] Obsidian Web Clipper 浏览器扩展

建议优先级：

1. Obsidian Git
2. Custom Attachment Location
3. Advanced Tables
4. Excalidraw
5. Terminal
6. Web Clipper

### P1：附件与图片规则需要标准化

当前已有大量图片、OCR 和原始资料，但尚未检测到统一附件插件配置。

建议：

- [ ] 新增统一附件命名规则
- [ ] 新增文章级 assets 目录规范
- [ ] 对新剪藏、新文章、新 SOP 自动套用附件路径规则

推荐规则：

```text
新附件位置：./assets/${noteFileName}
生成附件文件名：file-${date:{momentJsFormat:'YYYYMMDDHHmmssSSS'}}
引用路径：assets/${noteFileName}/${generatedAttachmentFileName}
```

### P1：Web Clipper 模板需要建立

当前已有 X 推文剪藏目录：

- `00.raw-materials/10.sources/web-clips/x-tweets`

但建议进一步建立统一模板。

建议模板字段：

```yaml
type: web-clip
platform:
source_author:
source_handle:
source_url:
source_title:
published:
captured:
language: zh-CN
tags:
status:
copyright_note:
```

### P2：飞书 CLI 工作流尚未接入

SOP 中建议用飞书负责协作，Obsidian 负责归档和再加工。当前未检测到飞书 CLI 工作流。

建议：

- [ ] 检查是否需要飞书 CLI
- [ ] 如需要，建立“飞书文档进入 Obsidian”的 SOP
- [ ] 建立“Obsidian 笔记发到飞书”的 SOP
- [ ] 明确飞书凭证不得入库

### P2：公众号 / X Article 发布工作流尚未形成

当前已能读取和保存 X 推文，但尚未形成从 Obsidian 到公众号 / X Article 草稿的正式流程。

建议：

- [ ] 建立公众号草稿发布 SOP
- [ ] 建立 X Article 草稿发布 SOP
- [ ] 加入“最终发布必须人工确认”规则
- [ ] 不保存公众号 / X 凭证

### P2：SOP Dashboard 入口需要补充

建议把本 SOP 和本检查报告加入 Agent Knowledge Ops Dashboard。

待加入：

- [[00.raw-materials/90.processed/agent-knowledge-ops/2026-06-16_AI时代Obsidian工作台搭建SOP.md]]
- [[00.raw-materials/90.processed/agent-knowledge-ops/2026-07-07_Obsidian工作台SOP符合性检查.md]]

## 自动化任务检查

| 任务 | 状态 |
|---|---|
| Obsidian Agent Knowledge Ops Refresh | Ready |
| Obsidian AI Agent Intel Daily | Ready |
| Obsidian Semiconductor Dispatch Intel Daily | Ready |
| Obsidian Raw Materials Weekly Knowledge Distill | Ready |

## 推荐下一步执行顺序

1. 安装 / 修复 Git，并连接 GitHub Private 仓库。
2. 增加根目录 `.gitignore`，优先保护 `.env`、`.venv`、日志、workspace 状态文件。
3. 安装 Obsidian Git 插件，并按 SOP 配置自动备份。
4. 安装 Custom Attachment Location，统一图片路径。
5. 安装 Advanced Tables、Excalidraw、Terminal。
6. 建立 Web Clipper 模板。
7. 建立敏感信息扫描任务。
8. 如有团队协作需求，再接入飞书 CLI。
9. 如有对外发布需求，再接入公众号 / X Article 草稿工作流。

## 总体评分

| 维度 | 评分 | 说明 |
|---|---:|---|
| 本地知识结构 | 8/10 | 已较成熟 |
| 自动化采集与提纯 | 8/10 | 已有多条自动任务 |
| GitHub 备份 | 2/10 | 当前 Git 不可用，需要优先补齐 |
| 插件工作台 | 3/10 | 社区插件较少 |
| 安全边界 | 5/10 | 子目录有保护，根目录缺全局规则 |
| 发布 / 协作流 | 3/10 | 尚未正式接入飞书、公众号、X Article |

## 一句话建议

优先补齐 **GitHub 备份 + 全局 .gitignore + Obsidian Git 插件 + 图片附件规则**。这四项补齐后，你的 Obsidian AI 工作台就会从“能运行”升级为“更安全、可恢复、可长期维护”。
