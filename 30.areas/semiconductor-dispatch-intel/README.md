# 半导体自动派工信息收集系统

本目录用于收集与你岗位相关的外部情报：半导体制造自动派工、晶圆厂调度、MES、AMHS、APC、APS、WIP、Cycle Time、瓶颈设备、AI Scheduling、数字孪生等。

## 目录说明

- `Dashboard.md`：中文情报看板。
- `config/sources.yml`：平台、关键词、RSS、论文、专利配置。
- `.env.example`：密钥模板。复制为 `.env` 后填写。
- `scripts/collect_intel.py`：采集脚本。
- `scripts/run_collect.ps1`：每日自动运行脚本。
- `inbox/`：每日 Markdown 情报简报。
- `cache/`：去重缓存、原始 JSON、运行日志。

## 快速开始

```powershell
cd "30.areas/semiconductor-dispatch-intel"
.\.venv\Scripts\python.exe scripts\collect_intel.py
```

运行后会生成：

```text
inbox/YYYY-MM-DD.md
```

## 已配置平台

- RSS：行业媒体、arXiv、Google Scholar 等。
- GitHub：已支持公开仓库、issues / PR 搜索。
- Reddit：使用公开 RSS，不强制需要密钥。
- X / Twitter：已预留接口，需要 `X_BEARER_TOKEN` 后启用。
- 论文源：arXiv、Semantic Scholar、Europe PMC。
- 专利源：当前使用 Google Patents 监控入口；结构化采集需额外 API。

## 自动分类

采集结果会自动分类为：

- 派工规则
- WIP
- AMHS
- MES
- AI 调度
- 论文
- 专利
- 厂商动态

## 每日自动运行

已注册 Windows 计划任务：

```text
Obsidian Semiconductor Dispatch Intel Daily
```

默认每天 **08:00** 运行：

```powershell
scripts/run_collect.ps1
```

查看任务：

```powershell
Get-ScheduledTask -TaskName "Obsidian Semiconductor Dispatch Intel Daily"
```

运行日志：

```text
cache/last_run.log
```

## Dashboard

入口：[[30.areas/semiconductor-dispatch-intel/Dashboard.md]]

## 你可能还需要提供的密钥

- `X_BEARER_TOKEN`：启用 X / Twitter 采集。
- `SEMANTIC_SCHOLAR_API_KEY`：降低 Semantic Scholar 限流概率。
- `PATENTSVIEW_API_KEY`：后续接入结构化专利采集。

## 建议工作流

1. 每天查看 `inbox/YYYY-MM-DD.md`。
2. 优先处理相关度高、分类为“派工规则 / WIP / AMHS / MES / AI 调度”的条目。
3. 把高价值条目移动或链接到专题笔记。
4. 根据噪声调整 `config/sources.yml` 中的关键词和来源。
