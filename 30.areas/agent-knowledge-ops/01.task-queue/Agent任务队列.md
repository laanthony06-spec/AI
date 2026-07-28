---
type: agent-task-queue
updated: 2026-07-28T22:03:35
tags: [Agent, Dispatch, 任务队列, 自动化]
---

# Agent Dispatch 任务队列

> 这是 Dispatch 中枢：把简报、Hooks、Memory、Evidence、TestCase 中出现的事项，整理成可执行任务。当前默认人工确认后再执行。
>
> 2026-07-28：按用户要求关闭当前全部 38 条自动生成任务；人工追加任务保持不变。

## 字段说明

- 推荐执行者：建议由哪个 Agent / 人类角色处理。
- 触发来源：brief、note_scan、hook created / modified 等。
- Evidence：任务依据，优先指向原始资料或 processed 笔记。
- 输出位置：完成后建议写到哪里。

## 任务列表

| 状态 | 优先级 | 分类 | 任务 | 推荐执行者 | 触发来源 | Evidence | 输出位置 | 下一步 |
|---|---|---|---|---|---|---|---|---|
| cancelled | P1 | MCP / 工具接口 | ### [Proposal: Security audit for MCP servers used by AutoGen agents](https://github.com/microsoft/autogen/issues/7924) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | ### [[Feature]: Develop MCP Server for AI-Native Kmesh Service Mesh Management](https://github.com/kmesh-net/kmesh/issues/1800) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | ### [[i18n] Thai Translation: Features Part 2b - MCP, Memory, Personality](https://github.com/NousResearch/hermes-agent/issues/15003) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP、多智能体、自动化 / Coding Agent、RAG / Memory。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP、自动化 / Coding Agent、RAG / Memory。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP、评测 / 安全。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | - 分类：工具调用 / MCP | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | - 原文摘要：## Security certification for MCP servers AutoGen agents increasingly use MCP (Model Context Protocol) servers as tools. These servers execute arbitrary code. How do we verify they are safe? We built **Sentinel**  | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | - 原文摘要：## 📄 user-guide/features/mcp.md --- sidebar_position: 4 title: "MCP (Model Context Protocol)" description: "Connect Hermes Agent to external tool servers via MCP - and control exactly which MCP tools Hermes loads" | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | - 原文摘要：### **Description:** Build a Model Context Protocol (MCP) server that exposes Kmesh's capabilities as callable tools for AI agents (Claude, Cursor, GitHub Copilot). The MCP server acts as a middle layer between AI | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | - 原文摘要：All BROAD queries returned items already in `_seen.txt` or zero results. **Queries run (5):** - Claude Code new features updates 2026 - Claude API tool use agents anthropic 2026 - MCP model context protocol new se | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | - 本简报聚焦 AI Agent、LLM Agent、多智能体、工具调用、MCP、Coding Agent、RAG / Memory、评测与安全。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P1 | MCP / 工具接口 | - 来源：GitHub issues - MCP agents | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| cancelled | P2 | Hooks | 处理 Hook 事件：created 30.areas/semiconductor-dispatch-intel/inbox/2026-07-26.md | Codex | created | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-26.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| cancelled | P2 | Hooks | 处理 Hook 事件：created 30.areas/semiconductor-dispatch-intel/inbox/2026-07-27.md | Codex | created | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-27.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| cancelled | P2 | Memory | ### [Incoming Work-In-Progress Prediction in Semiconductor Fabrication Foundry Using Long Short-Term Memory.](https://doi.org/10.1155/2019/8729367) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-27.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| cancelled | P2 | Memory | ### [[Proposal Update] Speculative Routing Predictor (SRP) v2.0: Full Production Engineering Blueprints for MoE Memory Bottleneck Mitigation](https://github.com/deepseek-ai/DeepSeek-V3/issues/1492) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-27.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| cancelled | P2 | Memory | - 中文导读：关注它是否提供 Agent 编排、状态管理、工具调用和生产化部署能力。 关键词信号：多智能体、RAG / Memory。 相关度中等，可快速浏览。 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| cancelled | P2 | Memory | - 原文摘要：# AI Agent Radar 日报 · 2026-07-25 ## 今日摘要 共排名 312 个项目，展示前 10 个，收录 1 条资讯。 ## 今日新发现 1. [Fmarzochi/EGC](https://github.com/Fmarzochi/EGC) — EGC gives every AI coding agent the same brain\. Shared memory, skills, and l | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| cancelled | P2 | Telemetry | - 原文摘要：<p>Integrating real-time voltage telemetry and functional monitoring for deeper insights.</p> <p>The post <a href="https://semiengineering.com/enhancing-system-observability/">Enhancing System Observability</a> ap | Codex | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-27.md]] | `30.areas/agent-knowledge-ops/04.telemetry/` | 人工确认后执行 |
| cancelled | P3 | TestCase | # 四、测试重点 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| cancelled | P3 | TestCase | ｜ 测试内容 ｜ 测试场景 ｜ 预期结果 ｜ | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | # AI / Agent 每日情报简报 - 2026-07-25 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | ### [A review of the applications of multi-agent reinforcement learning in smart factories.](https://doi.org/10.3389/frobt.2022.1027340) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | ### [AI Agent Radar 日报 · 2026-07-25](https://github.com/apiiskan/ai-agent-radar/issues/6) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | ### [johannalberts/supply-chain-research-agent](https://github.com/johannalberts/supply-chain-research-agent) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | ### [syed-fouzaan/Support-Ticket-Triage-Agent](https://github.com/syed-fouzaan/Support-Ticket-Triage-Agent) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | ### [🔍 Tool candidates for 2026-07-25 — 245 new](https://github.com/duolaAmengweb3/agentstore/issues/94) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | - 分类：Agent 框架 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | - 原文摘要：### 20 candidates need your review Auto-onboarded trusted sources this run: **0** For each candidate below: - ✅ **Onboard**: reply with `/onboard ` — bot will create a PR - ❌ **Skip**: no action needed, candidates | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | - 来源：GitHub repositories - AI agents recently updated | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | tags: [AI, Agent, 智能体, 情报简报] | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | type: ai-agent-intel | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-25.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | 优先阅读相关度高且分类为“派工规则 / WIP / AMHS / MES / AI 调度”的条目 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | 对明显无关的条目记录噪声来源，并更新关键词 / 来源配置 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | 对涉及公司内部派工逻辑的启发，单独沉淀到内部专题笔记 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| cancelled | P3 | 知识整理 | 将高价值条目移动到专题笔记或建立 wiki-link | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |

## 人工追加任务

- [ ] 把 Qsort 需求单整理成通俗介绍和 TestCase。
- [ ] 把 PM_Control 需求单整理成通俗介绍和 TestCase。
- [ ] 将 X Article 里提到的 Codex + Claude Code 工作系统拆成可执行蓝图。
