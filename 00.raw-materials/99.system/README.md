---
type: system-guide
tags: [自动化, 构建, 缓存, 系统目录]
updated: 2026-07-28
---

# 99.system

本目录只保存可再生的系统文件，不作为业务知识入口。

| 目录 | 用途 |
|---|---|
| `.venv/` | Python 虚拟环境 |
| `scripts/` | OCR、知识提纯、Agent Knowledge Ops 等自动化脚本 |
| `cache/` | 运行日志和临时状态 |
| `docx-build/` | Word 构建、LibreOffice Profile、渲染 QA、差异比较 |
| `xlsx-build/` | Excel 构建过程 |
| `archive/` | 内容整合过程中保留的旧副本 |

日常阅读和 Obsidian 检索时可以忽略本目录。

## LibreOffice 命令行

- 安装位置：`C:\Program Files\LibreOffice\program\soffice.exe`
- 自动化入口：`C:\Program Files\LibreOffice\program\soffice.com`
- `soffice.exe` 是 GUI 启动器，自动化任务中可能保持进程；无界面转换统一使用 `soffice.com`。
- 安全渲染脚本：`scripts/render_docx_safe.ps1`

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File "00.raw-materials/99.system/scripts/render_docx_safe.ps1" `
  -InputPath "path/to/input.docx"
```
