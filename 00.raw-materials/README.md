---
type: raw-materials-guide
tags: [原始资料, 资料管理, Obsidian]
---

# 原始资料库

本目录用于集中存放和处理未经整理或半整理的原始资料。当前已优化为五个主要文件夹，降低目录层级噪声，同时保留图片、视频、文档、PPT、PDF、表格、音频、网页、数据集、压缩包等类型分类。

## 五个一级文件夹

| 文件夹 | 用途 |
|---|---|
| `00.inbox/` | 临时收件箱。无法立即判断分类的资料先放这里 |
| `10.sources/` | 所有原始资料，按类型继续分二级目录 |
| `20.metadata/` | 资料卡、登记表、索引、重命名映射等元数据 |
| `90.processed/` | OCR、结构化整理、知识提取、周报等加工后知识 |
| `99.system/` | 自动化脚本、运行日志、Python 虚拟环境等系统文件 |

## 原始资料分类

`10.sources/` 下按资料类型分类：

| 二级目录 | 用途 |
|---|---|
| `10.sources/images/` | 图片、截图、扫描图、PPT 导出图片 |
| `10.sources/videos/` | 视频、录屏、培训录像 |
| `10.sources/documents/` | Word、Markdown、TXT 等文档 |
| `10.sources/presentations/` | PPT、Keynote、演示文件 |
| `10.sources/pdfs/` | PDF、论文、白皮书、手册 |
| `10.sources/spreadsheets/` | Excel、CSV、报表 |
| `10.sources/audio/` | 录音、会议音频 |
| `10.sources/web-clips/` | 网页剪藏、网页导出、HTML |
| `10.sources/datasets/` | 数据集、日志样本、仿真数据 |
| `10.sources/archives/` | ZIP、RAR、7z 等压缩包 |
| `10.sources/sensitive/` | 敏感资料，仅本地保存，谨慎同步 |

## 当前重点资料

- DSP 派工系统简介资料卡：[[00.raw-materials/20.metadata/DSP派工系统简介-资料卡.md]]
- 自动派工需求单 OCR 索引：[[00.raw-materials/90.processed/dispatch-requirements-notes/自动派工需求单图片-OCR索引.md]]
- 最新每周知识提纯：[[00.raw-materials/90.processed/weekly-knowledge-distill/最新每周知识提纯.md]]
- Codex 知识迁移清单：[[00.raw-materials/20.metadata/2026-07-28_Codex知识迁移清单.md]]
- 需求单最新交付物：`00.raw-materials/90.processed/requirement-writing-deliverables/`

## 推荐命名规范

```text
YYYY-MM-DD_主题_来源_版本.扩展名
```

PPT 导出图片建议使用页码补零：

```text
DSP派工系统简介_p001.png
DSP派工系统简介_p002.png
DSP派工系统简介_p003.png
```

## 资料处理流程

1. 新资料先放入 `00.inbox/` 或 `10.sources/` 对应类型目录。
2. 重要资料在 `20.metadata/` 中建立资料卡。
3. 图片、PPT 截图、需求单等进入 OCR 流程。
4. OCR、结构化整理和知识提取结果放入 `90.processed/`。
5. 自动化脚本、日志和虚拟环境放入 `99.system/`，日常阅读时可忽略。

## 每周知识提纯自动化

计划任务名称：

```text
Obsidian Raw Materials Weekly Knowledge Distill
```

默认每周一 **09:00** 运行。

手动运行：

```powershell
cd "D:\Obsidian\work\OBSidianCodex"
powershell -NoProfile -ExecutionPolicy Bypass -File "00.raw-materials/99.system/scripts/run_weekly_knowledge_distill.ps1"
```

自动化会：

- 扫描 `00.inbox/`、`10.sources/`、`20.metadata/`
- 刷新图片需求单 OCR 与整理笔记
- 生成原始资料清单 JSON / CSV
- 从 OCR、Markdown、TXT、CSV、JSON 等资料中提炼知识
- 判断 `90.processed/` 中已有知识是否还有优化空间

输出位置：

- `90.processed/weekly-knowledge-distill/`
- `90.processed/inventory/`

## 敏感资料提醒

涉及公司内部系统、产线、设备、客户、派工规则、截图、日志的数据，建议放入：

```text
10.sources/sensitive/
```

并在相关资料卡中标注敏感级别。
