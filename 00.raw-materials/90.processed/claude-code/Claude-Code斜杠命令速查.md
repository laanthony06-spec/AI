---
type: distilled-knowledge
source: "[[00.raw-materials/10.sources/web-clips/claude-code/2026-07-05_Claude-Code斜杠命令推文.md]]"
topic: Claude Code 斜杠命令
status: draft
created: 2026-07-05
tags: [Claude-Code, 斜杠命令, AI编程, 工作流, 速查]
---

# Claude Code 斜杠命令速查

> 这是一份基于推文内容整理的 Claude Code Slash Commands 速查笔记。  
> 命令是否可用以当前环境中的 `/help` 为准。

## 一句话总结

Claude Code 的 `/` 斜杠命令不是用来“写 Prompt”的，而是用来**控制会话、权限、上下文、模型、诊断和工作流**。

## 最小必记组合

| 场景 | 命令 | 用途 |
|---|---|---|
| 不知道能做什么 | `/help` 或 `/` | 查看当前可用命令 |
| 新项目开始 | `/init` | 初始化项目，生成 CLAUDE.md |
| 大改前 | `/plan` | 先规划，避免直接乱改 |
| 切换模型 | `/model` | 根据任务复杂度选择模型 |
| 控制权限 | `/permissions` | 管理工具权限和风险边界 |
| 改完验收 | `/diff` | 查看实际改动 |
| 上下文太长 | `/compact` | 压缩上下文 |
| 看状态 | `/status` | 查看模型、账号、连接状态 |
| 接着旧任务 | `/resume` | 恢复之前会话 |
| 出问题 | `/doctor` | 诊断安装和环境问题 |

## 推荐工作流

### 1. 新项目开工

```text
/init
/memory
/permissions
/status
```

目的：

- 生成项目长期上下文。
- 明确项目规则。
- 检查权限和连接状态。

### 2. 复杂任务开始前

```text
/plan
/model
/permissions
```

目的：

- 先让 Claude 输出方案。
- 决定是否需要更强模型。
- 避免在权限不清楚时直接执行危险操作。

### 3. 改完代码后

```text
/diff
/simplify
/recap
```

目的：

- 看 Claude 实际改了哪些文件。
- 检查是否能进一步简化。
- 留下会话总结，方便后续接续。

### 4. 长会话维护

```text
/compact
/focus
/clear
```

目的：

- 避免上下文过长导致跑偏。
- 降低历史噪声。
- 新任务开启干净上下文。

### 5. 排障

```text
/status
/doctor
/debug
/feedback
```

目的：

- 先看状态。
- 再诊断安装、账号、权限、MCP、插件等问题。
- 必要时提交反馈。

## 命令分类

### 开工类

- `/init`
- `/plan`
- `/model`
- `/memory`
- `/permissions`

### 代码验收类

- `/diff`
- `/simplify`
- `/review`
- `/recap`

### 上下文管理类

- `/compact`
- `/clear`
- `/focus`
- `/resume`

### 排障类

- `/status`
- `/doctor`
- `/debug`
- `/feedback`

### 扩展能力类

- `/skills`
- `/plugin`
- `/mcp`
- `/hooks`
- `/sandbox`

### 会话管理类

- `/rename`
- `/export`
- `/insights`
- `/tasks`
- `/exit`
- `/quit`

## 最值得养成的 5 个习惯

1. **新项目先 `/init`**  
   先建立项目说明和长期上下文，再让 Claude 改代码。

2. **大改前先 `/plan`**  
   先审方案，再决定是否执行。

3. **改完必须 `/diff`**  
   不要只相信 Claude 的总结，要看真实文件改动。

4. **长会话及时 `/compact`**  
   上下文不是越长越好，关键是干净。

5. **异常先 `/doctor`**  
   账号、权限、MCP、插件、安装问题，先诊断再重装。

## 风险提醒

- `/permissions` 不要一口气放开所有权限，尤其是删除文件、安装依赖、执行脚本。
- `/compact` 可能丢失细节，关键约束建议先写入项目文档。
- `/plan` 只是规划，不代表方案一定正确。
- `/diff` 是验收入口，但最终仍需人工 Review 和测试。
- 斜杠命令需要放在消息开头，例如 `/model`，不要写成“请你 /model”。

## 关联笔记

- 原始推文归档：[[00.raw-materials/10.sources/web-clips/claude-code/2026-07-05_Claude-Code斜杠命令推文.md]]
- 可扩展为专题：Claude Code 使用规范（待建立）
