---
type: agent-task-queue
updated: 2026-07-28T22:03:35
tags: [Agent, Dispatch, 任务队列, 自动化]
---

# Agent Dispatch 任务队列

> 这是 Dispatch 中枢：把简报、Hooks、Memory、Evidence、TestCase 中出现的事项整理成可执行任务。当前默认人工确认后再执行。

## 自动任务

| 状态 | 优先级 | 分类 | 任务 | 推荐执行者 | 触发来源 | Evidence | 输出位置 | 下一步 |
|---|---|---|---|---|---|---|---|---|
| — | — | — | 当前没有自动生成的待办任务 | — | — | — | — | 新任务将在后续刷新时加入 |

## 已关闭自动任务

- 2026-07-28 按用户要求关闭 38 条自动生成任务。
- 状态统一为 `cancelled`，没有标记为已完成。
- 明细保存在 [[00.raw-materials/90.processed/agent-knowledge-ops/agent-dispatch-queue.json]]。

## 人工追加任务

- [ ] 把 Qsort 需求单整理成通俗介绍和 TestCase。
- [ ] 把 PM_Control 需求单整理成通俗介绍和 TestCase。
- [ ] 将 X Article 里提到的 Codex + Claude Code 工作系统拆成可执行蓝图。
