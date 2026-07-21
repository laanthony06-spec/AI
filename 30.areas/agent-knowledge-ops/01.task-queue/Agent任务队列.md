---
type: agent-task-queue
updated: 2026-07-21T20:05:04
tags: [Agent, Dispatch, 任务队列, 自动化]
---

# Agent Dispatch 任务队列

> 这是 Dispatch 中枢：把简报、Hooks、Memory、Evidence、TestCase 中出现的事项，整理成可执行任务。当前默认人工确认后再执行。

## 字段说明

- 推荐执行者：建议由哪个 Agent / 人类角色处理。
- 触发来源：brief、note_scan、hook created / modified 等。
- Evidence：任务依据，优先指向原始资料或 processed 笔记。
- 输出位置：完成后建议写到哪里。

## 任务列表

| 状态 | 优先级 | 分类 | 任务 | 推荐执行者 | 触发来源 | Evidence | 输出位置 | 下一步 |
|---|---|---|---|---|---|---|---|---|
| todo | P1 | MCP / 工具接口 | ### [Volcano Model Context Protocol (MCP) Server for Ecosystem-Wide AI Operations](https://github.com/volcano-sh/volcano/issues/5667) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [feat: MCP Server — expose UI Foundations knowledge to AI agents](https://github.com/tbielich/ui-foundations/issues/75) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP、RAG / Memory、评测 / 安全。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它是否提供 Agent 编排、状态管理、工具调用和生产化部署能力。 关键词信号：工具调用 / MCP、自动化 / Coding Agent、RAG / Memory。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它是否提供 Agent 编排、状态管理、工具调用和生产化部署能力。 关键词信号：工具调用 / MCP。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 分类：工具调用 / MCP | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 原文摘要：## Summary Build a Model Context Protocol (MCP) server that exposes UI Foundations design system knowledge, rules, components, patterns, and tokens to AI agents. ## Scope (Phase 1) - **Resources**: manifest, agent | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 原文摘要：Full-Stack Developer with commercial experience building enterprise microservices (Java · Spring Boot · Angular) at Aibron, and a growing focus on AI engineering — RAG pipelines, vector databases, MCP-based agent  | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 原文摘要：Modular, agentic framework and MCP platform you self-host. Build and run your own AI agents, connect Claude/ChatGPT/Cursor as a native MCP connector, self-host your apps, and share over encrypted P2P — on hardware | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 本简报聚焦 AI Agent、LLM Agent、多智能体、工具调用、MCP、Coding Agent、RAG / Memory、评测与安全。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 来源：GitHub issues - MCP agents | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P2 | Hooks | 处理 Hook 事件：created 30.areas/ai-agent-intel/inbox/2026-07-16.md | Codex | created | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md | Codex | created | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Memory | ### [Incoming Work-In-Progress Prediction in Semiconductor Fabrication Foundry Using Long Short-Term Memory.](https://doi.org/10.1155/2019/8729367) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | Memory | ### [New Nonvolatile Memory Winners Emerge](https://semiengineering.com/new-nonvolatile-memory-winners-emerge/) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | Memory | ### [[Proposal Update] Speculative Routing Predictor (SRP) v2.0: Full Production Engineering Blueprints for MoE Memory Bottleneck Mitigation](https://github.com/deepseek-ai/DeepSeek-V3/issues/1492) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | Memory | - 中文导读：关注它是否提供 Agent 编排、状态管理、工具调用和生产化部署能力。 关键词信号：RAG / Memory。 相关度中等，可快速浏览。 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | Memory | - 原文摘要：<p>RRAM, MRAM have promising futures, while FeRAM lurks, and UltraRAM plans a debut. </p> <p>The post <a href="https://semiengineering.com/new-nonvolatile-memory-winners-emerge/">New Nonvolatile Memory Winners Eme | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P3 | TestCase | # 四、测试重点 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | ｜ 测试内容 ｜ 测试场景 ｜ 预期结果 ｜ | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | 安全预检 | - 中文导读：关注它是否提供 Agent 编排、状态管理、工具调用和生产化部署能力。 关键词信号：自动化 / Coding Agent、评测 / 安全。 相关度中等，可快速浏览。 | 人工确认 + Codex | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | # AI / Agent 每日情报简报 - 2026-07-16 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [A review of the applications of multi-agent reinforcement learning in smart factories.](https://doi.org/10.3389/frobt.2022.1027340) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [johannalberts/supply-chain-research-agent](https://github.com/johannalberts/supply-chain-research-agent) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [linny006/agent-eval-harness](https://github.com/linny006/agent-eval-harness) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 分类：Agent 框架 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：## 1. Description / Problem Statement When distributed batch workloads (such as PyTorch training, Spark jobs, or Ray clusters) fail, stall, or hang in queues, operators must manually investigate cluster state. Thi | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：A multi-tenant Enterprise Policy RAG Platform built with FastAPI, PostgreSQL + pgvector, Redis, LangGraph, and LlamaIndex. Supports secure, citation-backed policy search with Notion/Google integration, agent orche | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：Live, open-source benchmark for comparing AI coding agents on real GitHub issues | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：🏗️ AI-powered blueprint generator for codebases with autonomous multi-agent CI/CD workflow | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 来源：GitHub repositories - AI agents recently updated | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 来源：GitHub repositories - agent frameworks | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | tags: [AI, Agent, 智能体, 情报简报] | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | type: ai-agent-intel | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 优先阅读相关度高且分类为“派工规则 / WIP / AMHS / MES / AI 调度”的条目 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对明显无关的条目记录噪声来源，并更新关键词 / 来源配置 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对涉及公司内部派工逻辑的启发，单独沉淀到内部专题笔记 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 将高价值条目移动到专题笔记或建立 wiki-link | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-16.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |

## 人工追加任务

- [ ] 把 Qsort 需求单整理成通俗介绍和 TestCase。
- [ ] 把 PM_Control 需求单整理成通俗介绍和 TestCase。
- [ ] 将 X Article 里提到的 Codex + Claude Code 工作系统拆成可执行蓝图。
