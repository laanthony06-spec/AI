---
type: agent-knowledge-ops
tags: [Agent, KnowledgeOps, 自动化, Obsidian]
---

# Agent Knowledge Ops

这是一个把 **每日简报 → Dispatch 任务队列 → Evidence 证据层 → TestCase → Telemetry → MCP → Memory → Hooks** 串起来的工作区。

它的目标不是“让 Agent 自己乱跑”，而是让 Agent 像一个可靠的研究助理：

- 知道该看哪里；
- 知道任务从哪里来；
- 知道结论有什么证据；
- 知道哪些规则可以测试；
- 知道自己之前做过什么；
- 知道哪些自动化正在健康运行。

## 模块入口

| 模块 | 入口 | 作用 |
|---|---|---|
| Dispatch 任务队列 | [[30.areas/agent-knowledge-ops/01.task-queue/Agent任务队列.md]] | 汇总简报、Hooks、Memory、Evidence 中的可执行任务 |
| Evidence 证据层 | [[30.areas/agent-knowledge-ops/02.evidence/Evidence索引.md]] | 给知识结论绑定原图、OCR、需求单、笔记来源 |
| 派工规则 TestCase 库 | [[30.areas/agent-knowledge-ops/03.testcases/派工规则TestCase库.md]] | 把派工规则转为可验证案例 |
| Agent Telemetry 看板 | [[30.areas/agent-knowledge-ops/04.telemetry/Agent自动化运行看板.md]] | 检查每日 / 每周自动化是否健康 |
| Obsidian 只读 MCP 原型 | [[30.areas/agent-knowledge-ops/05.mcp-server/Obsidian只读MCP服务说明.md]] | 为后续 Agent 结构化读取知识库做准备 |
| Agent Memory | [[30.areas/agent-knowledge-ops/06.memory/系统约定记忆.md]] | 记录系统约定、任务执行、错误修复、高价值来源 |
| Hooks 扫描器 | [[30.areas/agent-knowledge-ops/07.hooks/Hooks扫描器.md]] | 扫描新增/修改文件，生成候选任务 |

## 手动刷新

```powershell
cd "D:\Obsidian\work\OBSidianCodex"
powershell -NoProfile -ExecutionPolicy Bypass -File "00.raw-materials/99.system/scripts/run_agent_knowledge_ops.ps1"
```

## 自动刷新

计划任务：

```text
Obsidian Agent Knowledge Ops Refresh
```

默认每天 **09:20** 运行。

## 当前边界

- Hooks 只扫描并生成任务，不自动移动/删除/修改业务资料。
- MCP 原型只读，默认 stdio，不开放网络端口。
- Dispatch 队列默认需要人工确认后执行。
- 敏感资料默认不外发。

