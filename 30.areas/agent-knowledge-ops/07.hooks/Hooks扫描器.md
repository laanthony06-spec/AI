---
type: hooks-scanner
updated: 2026-07-28T19:23:21
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
| created | [[00.raw-materials/90.processed/dispatch-requirements-notes/CMPAutoPirun-需求单整理.md]] | 26280 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | 23901 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPirun优化-需求单整理.md]] | 23497 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| modified | [[00.raw-materials/90.processed/dispatch-requirements-notes/PM_Control-需求单整理.md]] | 26932 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| modified | [[00.raw-materials/90.processed/dispatch-requirements-notes/Qsort-需求单整理.md]] | 6992 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| modified | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | 27533 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| modified | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase要求-需求单整理.md]] | 6866 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| modified | [[00.raw-materials/90.processed/dispatch-requirements-notes/WaferBalance-需求单整理.md]] | 12380 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| modified | [[00.raw-materials/90.processed/dispatch-requirements-notes/WPHLoss-需求单整理.md]] | 10834 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| modified | [[00.raw-materials/90.processed/dispatch-requirements-notes/自动派工需求单图片-OCR索引.md]] | 2077 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | 31883 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| modified | [[00.raw-materials/90.processed/weekly-knowledge-distill/最新每周知识提纯.md]] | 283 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | 102776 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |

## 触发规则草案

| 事件 | 自动生成任务 |
|---|---|
| `00.inbox` 新增文件 | 分类原始资料，必要时移动到 `10.sources` |
| `10.sources/images` 新增图片 | OCR 并建立资料卡 / 需求单整理 |
| AI 简报新增 | 抽取可借鉴 Agent 应用 |
| 半导体派工简报新增 | 抽取派工相关条目 |
| processed 笔记修改 | 更新 Evidence 和 Telemetry |
