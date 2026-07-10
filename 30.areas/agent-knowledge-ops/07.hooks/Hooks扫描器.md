---
type: hooks-scanner
updated: 2026-07-10T20:21:50
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
| created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/1.jpg]] | 318258 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/2.jpg]] | 376360 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/3.jpg]] | 400809 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/4.jpg]] | 375383 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/5.jpg]] | 372808 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/6.jpg]] | 384837 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/7.jpg]] | 348292 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/8.jpg]] | 408379 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/9.jpg]] | 823820 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.2.docx]] | 43050 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.2.md]] | 9465 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.docx]] | 132111 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.md]] | 11418 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/90.processed/dispatch-requirements-notes/render_LithoAutoSplitPirun_v0.2_manual/litho_physical_split_v02.docx]] | 43050 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[00.raw-materials/90.processed/dispatch-requirements-notes/render_LithoAutoSplitPirun_v0.2_manual/test.docx]] | 36580 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | 64075 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |
| created | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-09.md]] | 17248 | 检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase |

## 触发规则草案

| 事件 | 自动生成任务 |
|---|---|
| `00.inbox` 新增文件 | 分类原始资料，必要时移动到 `10.sources` |
| `10.sources/images` 新增图片 | OCR 并建立资料卡 / 需求单整理 |
| AI 简报新增 | 抽取可借鉴 Agent 应用 |
| 半导体派工简报新增 | 抽取派工相关条目 |
| processed 笔记修改 | 更新 Evidence 和 Telemetry |
