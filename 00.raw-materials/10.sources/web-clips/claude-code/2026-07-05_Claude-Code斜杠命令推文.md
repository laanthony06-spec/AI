---
type: web-clip
source_type: tweet
topic: Claude Code 斜杠命令
status: archived
created: 2026-07-05
tags: [Claude-Code, 斜杠命令, AI编程, 工具使用, 原始资料]
processed_note: "[[00.raw-materials/90.processed/claude-code/Claude-Code斜杠命令速查.md]]"
---

# Claude Code 斜杠命令推文归档

> 来源：用户手动粘贴的推文内容  
> 说明：以下为原始推文内容整理归档。命令是否在当前 Claude Code 版本中可用，仍需以 `/help` 或当前环境实际显示为准。

## 原文核心内容

这篇推文介绍了 Claude Code 中的 `/` 斜杠命令，强调这些命令不是让 Claude “更聪明”，而是用于控制当前 Claude Code 会话，例如：

- 切换模型
- 查看状态
- 初始化项目
- 进入 Plan mode
- 查看代码改动
- 压缩上下文
- 管理权限
- 恢复历史会话
- 诊断安装问题

## 新手优先记住的 10 个命令

```markdown
/help           查看帮助和可用命令
/init           初始化项目，生成 CLAUDE.md
/model          切换模型
/plan           先规划，再动手
/permissions    管理工具权限
/diff           查看本次改了什么
/compact        压缩上下文
/status         查看版本、模型、账号、连接状态
/resume         恢复之前的会话
/doctor         诊断安装和环境问题
```

推文建议的使用顺序：

```text
开工前 /init
大改前 /plan
改完后 /diff
上下文长了 /compact
出问题 /doctor
```

## 高频核心命令

- `/help`：查看帮助和可用命令。
- `/model`：切换 Claude Code 使用的模型。
- `/ide`：管理 IDE 集成状态。
- `/permissions`：管理工具权限。
- `/plan`：进入 Plan mode，大改前先规划。
- `/review`：审查 PR。
- `/compact`：压缩上下文，释放 token 空间。
- `/status`：查看 Claude Code 当前状态。
- `/usage`：查看会话成本、计划用量和统计。
- `/fast`：开启或关闭 Fast mode。

## 配置、账号与系统命令

- `/login`：登录 Anthropic 账号。
- `/logout`：退出登录。
- `/memory`：编辑 memory / CLAUDE.md 相关文件。
- `/hooks`：查看 hooks 配置。
- `/init`：初始化项目，并生成 CLAUDE.md。
- `/mobile`：显示 Claude 手机 App 下载二维码。
- `/debug`：为当前会话开启调试日志并辅助排查。
- `/doctor`：诊断 Claude Code 安装和设置。
- `/feedback`：提交反馈或报告问题。
- `/exit` 或 `/quit`：退出 Claude Code。

## 工作流与代码质量命令

- `/diff`：查看当前未提交改动和每轮改动差异。
- `/simplify`：审查代码复用、质量和效率问题。
- `/rewind`：回到之前某个代码或对话状态。
- `/recap`：生成当前会话摘要。
- `/focus`：切换 Focus 视图，只看关键内容。
- `/skills`：列出可用 Skills。
- `/plugin`：管理 Claude Code 插件。
- `/mcp`：管理 MCP servers。
- `/powerup`：互动引导了解 Claude Code 能力。
- `/sandbox`：查看或配置沙箱模式。

## 会话与终端管理命令

- `/clear`：开启新的空上下文会话。
- `/resume`：恢复之前的对话。
- `/rename`：重命名当前会话。
- `/export`：导出当前会话。
- `/insights`：生成 Claude Code 会话分析报告。
- `/tasks`：查看和管理后台任务。
- `/tui`：设置终端 UI 渲染方式。
- `/theme`：切换主题。
- `/terminal-setup`：配置终端快捷键集成。
- `/keybindings`：打开或创建快捷键配置文件。

## 按场景记忆

### 第一次进项目

```text
/init
/memory
/permissions
/status
```

### 准备做复杂任务

```text
/plan
/model
/permissions
```

### Claude 改完代码后

```text
/diff
/simplify
/recap
```

### 上下文太长

```text
/compact
/focus
/clear
```

### 出问题了

```text
/status
/doctor
/debug
/feedback
```

### 想接着上次做

```text
/resume
/rename
/export
```

## 推文强调的使用习惯

1. 进入项目后先 `/init`。
2. 大改前先 `/plan`，不要让 Claude 直接动手。
3. 改完后必须 `/diff`，看它实际改了什么。
4. 上下文长了就 `/compact`。
5. 异常先 `/doctor`。

## 注意事项

- 不同用户看到的命令可能不同，取决于平台、账号、版本、插件、MCP 环境。
- 最准确的方法是输入 `/` 或 `/help` 查看当前环境支持的命令。
- 斜杠命令需要放在消息开头。
- `/plan`、`/diff`、`/compact`、`/permissions` 都不是万能按钮，仍需人工判断和验收。

