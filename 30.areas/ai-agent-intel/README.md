---
type: intel-system
tags: [AI, Agent, 智能体, 情报系统]
---

# AI / Agent 每日情报系统

这个目录用于每日收集 AI Agent、LLM Agent、多智能体、MCP、工具调用、Coding Agent、RAG / Memory、Agent 安全评测等信息。

## 目录

- `config/sources.json`：关键词和来源配置
- `.env.example`：密钥模板
- `scripts/collect_ai_agent_intel.py`：采集脚本
- `scripts/run_collect.ps1`：手动 / 定时运行入口
- `inbox/`：每日简报
- `cache/`：原始 JSON 和运行日志

## 当前来源

- GitHub：公开仓库、issues
- RSS：arXiv、Hacker News、Reddit RSS
- X / Twitter：已预留接口，需要 Bearer Token 后启用

## 手动运行

```powershell
cd "D:\Obsidian\work\OBSidianCodex"
powershell -NoProfile -ExecutionPolicy Bypass -File "30.areas/ai-agent-intel/scripts/run_collect.ps1"
```

## 每日自动任务

计划任务名称：

```text
Obsidian AI Agent Intel Daily
```

默认每天 **08:40** 运行。

## 需要你提供的密钥

### 推荐：GitHub Token

不填也能搜索公开内容，但速率较低。

在 `.env` 中填写：

```env
GITHUB_TOKEN=
```

### 可选但重要：X / Twitter Bearer Token

如果要采集 X，需要填写：

```env
X_BEARER_TOKEN=
```

然后把 `config/sources.json` 中：

```json
"x": {
  "enabled": false
}
```

改为：

```json
"x": {
  "enabled": true
}
```

## 最新简报

每日输出到：

```text
inbox/YYYY-MM-DD.md
```

