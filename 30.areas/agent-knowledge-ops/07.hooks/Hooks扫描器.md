---
type: hooks-scanner
updated: 2026-07-23T22:27:51
tags: [Agent, Hooks, 自动触发]
---

# Hooks 扫描器

## 作用

扫描关键目录的新增、修改、删除事件，并把事件转成可进入 Dispatch 队列的候选任务。当前版本只生成任务，不自动修改业务资料。

## 监听目录

- `00.raw-materials/00.inbox`
- `00.raw-materials/10.sources/images`
- `00.raw-materials/20.metadata`
- `00.raw-materials/90.processed/dispatch-requirements-notes`
- `00.raw-materials/90.processed/weekly-knowledge-distill`
- `30.areas/ai-agent-intel/inbox`
- `30.areas/semiconductor-dispatch-intel/inbox`

## 本次扫描结果

| 事件 | 文件 | 大小 | 建议动作 |
|---|---|---:|---|
| created | [[30.areas/ai-agent-intel/inbox/2026-07-22.md]] | 99985 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-22.md]] | 28730 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |

## 触发规则草案

| 事件 | 自动生成任务 |
|---|---|
| `00.inbox` 新增文件 | 分类原始资料，必要时移动到 `10.sources` |
| `10.sources/images` 新增图片 | OCR 并建立资料卡 / 需求单整理 |
| AI 简报新增 | 抽取可借鉴 Agent 应用 |
| 半导体派工简报新增 | 抽取派工相关条目 |
| processed 笔记修改 | 更新 Evidence 和 Telemetry |
