---
type: insight-note
source: [[00.raw-materials/10.sources/web-clips/x-tweets/2026-06-30_WorkBuddy_intro_part1_XiaohuiAI666.md]]
created: 2026-07-05
tags: [AI-Agent, Agent架构, WorkBuddy, Obsidian自动化, 自动派工]
status: candidate-actions
---

# WorkBuddy 对 Agent Knowledge Ops 的架构借鉴

## 一句话结论

这篇 WorkBuddy 长文最值得吸收的是：**把 AI 从聊天窗口变成可控的任务执行系统**。它的权限、记忆、任务、远程触发、专家模块，正好可以补强本仓库的 Agent Knowledge Ops 架构。

## 可落地设计

### 1. 权限分层：Ask / Plan / Craft

建议在本仓库内形成三种执行模式：

| 模式 | 在本仓库中的定义 | 是否改文件 |
|---|---|---|
| Ask | 只分析资料、回答问题、提出建议 | 否 |
| Plan | 生成执行计划、列出将修改的文件，等待确认 | 否 |
| Craft | 在已授权范围内自动 OCR、整理、归档、更新 Dashboard | 是 |

### 2. Memory 治理

当前已经有 Memory 目录：

- [[30.areas/agent-knowledge-ops/06.memory/系统约定记忆.md]]
- [[30.areas/agent-knowledge-ops/06.memory/任务执行记忆.md]]
- [[30.areas/agent-knowledge-ops/06.memory/错误与修复记录.md]]
- [[30.areas/agent-knowledge-ops/06.memory/高价值来源记录.md]]

建议新增规则：

- 记忆条目不求多，优先保留可复用规则。
- 每周自动检查过期记忆。
- Memory 分为“全局记忆”和“项目记忆”，避免不同项目互相污染。

### 3. 专家团拆分

可将自动派工知识系统拆分为以下专家角色：

| 专家 | 负责内容 |
|---|---|
| 派工规则专家 | DSP 规则、优先级、约束、异常处理 |
| WIP 专家 | WIP balance、queue time、lot aging、瓶颈站点 |
| AMHS 专家 | 搬送约束、FOUP / Stocker / OHT 影响 |
| MES 集成专家 | MES event、lot state、recipe、route、hold/release |
| AI Scheduling 专家 | Agent、RL、优化算法、仿真、自动调参 |

### 4. 远程触发任务

后续可以设计“远程触发语句”：

- 处理今天新增原始资料。
- 总结本周 AI Agent 简报。
- 从需求单中提取派工规则。
- 为 WaferBalance 生成 TestCase。
- 检查 Dashboard 是否有过期内容。

## 建议加入任务队列

- [ ] 在 Agent任务队列中加入 Ask / Plan / Craft 权限字段。
- [ ] 为 Memory 增加每周清理任务。
- [ ] 建立 5 类半导体自动派工专家模板。
- [ ] 增加“远程触发语句库”。
- [ ] 把 WorkBuddy 作为 AI Agent 产品研究样本纳入高价值来源记录。

## Evidence

- 原始剪藏：[[00.raw-materials/10.sources/web-clips/x-tweets/2026-06-30_WorkBuddy_intro_part1_XiaohuiAI666.md]]
- 原始链接：[X 推文](https://x.com/XiaohuiAI666/status/2071830585216291050)
