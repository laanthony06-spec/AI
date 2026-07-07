---
type: web-clip
platform: X
source_author: 程序员小灰
source_handle: XiaohuiAI666
source_url: https://x.com/XiaohuiAI666/status/2071830585216291050
source_title: WorkBuddy 保姆级入门教程（上篇）
published: 2026-06-30 13:37
captured: 2026-07-05
language: zh-CN
tags: [X, AI-Agent, WorkBuddy, 桌面AI工作台, AgentKnowledgeOps]
status: structured-summary
copyright_note: 仅保存结构化摘要与少量短摘录，不保存全文。
---

# WorkBuddy 保姆级入门教程（上篇）

> 短摘录：WorkBuddy 保姆级入门教程（上篇）

## 来源

- 平台：X / Twitter
- 作者：程序员小灰（@XiaohuiAI666）
- 链接：[原推文](https://x.com/XiaohuiAI666/status/2071830585216291050)
- 发布时间：2026-06-30 13:37
- 读取方式：Chrome 页面读取

## 内容摘要

这篇长文介绍腾讯桌面 AI 工作台 **WorkBuddy** 的基本概念、安装配置、任务模式、权限分层、记忆机制、远程助理和专家模块。它的核心价值不只是“聊天”，而是让 AI Agent 能够围绕本地文件、办公任务、代码、资料整理等场景进行任务拆解、计划、执行与交付。

## 结构化要点

### 1. 产品定位

- WorkBuddy 是桌面 AI 工作台。
- 面向日常办公、文件处理、代码、设计、资料总结等场景。
- 强调从“回答问题”升级为“执行任务”。

### 2. 安装与基础设置

- 支持 Windows / Mac。
- 需要关注工作空间路径，避免默认路径占满系统盘。
- 支持自定义模型，重点是 **OpenAI compatible API**。

### 3. 任务模式

- 用户通过“新建任务”描述目标。
- AI 自动拆解步骤并执行。
- 和普通聊天相比，任务模式更接近可交付工作流。

### 4. 权限分层

| 模式 | 含义 | 适用场景 |
|---|---|---|
| Ask | 只给建议，不直接执行 | 咨询、思路讨论 |
| Plan | 先制定计划，用户确认后执行 | 大多数日常任务 |
| Craft | 更自动化地执行完整流程 | 批量文件处理、代码、重复性工作 |

### 5. Memory 记忆机制

- 记忆让 AI Agent 逐渐理解用户偏好、项目背景和输出要求。
- 建议定期清理记忆，避免记忆过多分散模型注意力。
- 当前局限：项目级隔离不足，多个项目共享记忆时可能串上下文。

### 6. 助理功能

- 手机端可远程触发电脑上的 WorkBuddy 执行任务。
- 适用于通勤、会议、离开电脑时远程发起任务。
- 前提是电脑和 WorkBuddy 保持运行。

### 7. 专家模块

- 专家不是简单 Prompt，而是领域认知框架、工具链和输出模板的组合。
- 可用于财务、代码、法律、产品、数据分析、内容创作等领域。
- 支持通过问答引导创建专属专家团。

## 对本仓库的可借鉴点

1. **Ask / Plan / Craft 权限模型**：可映射到 Obsidian 自动化任务的只读分析、计划确认、自动执行三级模式。
2. **Memory 小而精**：Agent 记忆应控制数量，强调高价值、可复用、定期清理。
3. **任务优先于聊天**：将“问答”转为“资料读取 → Evidence → 规则提炼 → TestCase → Dashboard 更新”。
4. **专家团机制**：可以建立派工规则专家、WIP 专家、AMHS 专家、MES 集成专家、AI Scheduling 专家。
5. **远程触发**：后续可考虑通过手机、飞书、微信或快捷指令触发 Obsidian 知识整理任务。

## 关联笔记

- [[30.areas/agent-knowledge-ops/Dashboard.md]]
- [[30.areas/agent-knowledge-ops/06.memory/系统约定记忆.md]]
- [[30.areas/agent-knowledge-ops/01.task-queue/Agent任务队列.md]]
