---
type: agent-task-queue
updated: 2026-07-12T09:20:03
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
| todo | P1 | MCP / 工具接口 | ### [Add query-first wiki mcp subcommand](https://github.com/wazootech/wiki/issues/209) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注 API、SDK、平台能力变化，以及是否会影响你的工具链选择。 关键词信号：工具调用 / MCP、自动化 / Coding Agent、RAG / Memory。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP、自动化 / Coding Agent。 相关度中等，可快速浏览。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP、自动化 / Coding Agent。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：自动化 / Coding Agent、RAG / Memory、评测 / 安全。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 分类：工具调用 / MCP | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 本简报聚焦 AI Agent、LLM Agent、多智能体、工具调用、MCP、Coding Agent、RAG / Memory、评测与安全。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 来源：GitHub issues - MCP agents | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/PPT.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/PPT.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/Testcase1.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/Testcase1.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/Testcase2.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/Testcase2.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/技术文档1.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/技术文档1.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/技术文档2.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/技术文档2.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/技术文档3.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/技术文档3.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/技术文档4.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/技术文档4.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/需求单1.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/需求单1.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/需求单2.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/需求单2.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/需求单3.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/需求单3.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/需求单4.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/需求单4.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/CMPAutoPirun/需求单5.jpg | Codex | created | [[00.raw-materials/10.sources/images/CMPAutoPirun/需求单5.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 30.areas/ai-agent-intel/inbox/2026-07-10.md | Codex | created | [[30.areas/ai-agent-intel/inbox/2026-07-10.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 30.areas/ai-agent-intel/inbox/2026-07-12.md | Codex | created | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 30.areas/semiconductor-dispatch-intel/inbox/2026-07-10.md | Codex | created | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-10.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md | Codex | created | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Memory | ### [Incoming Work-In-Progress Prediction in Semiconductor Fabrication Foundry Using Long Short-Term Memory.](https://doi.org/10.1155/2019/8729367) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | Memory | ### [Proposal: Strengthen Ralph memory handoff by requiring structured implementation learnings in `progress.md`](https://github.com/Rubiss-Projects/spec-kit-ralph/issues/27) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | Memory | - 中文导读：关注它是否提供 Agent 编排、状态管理、工具调用和生产化部署能力。 关键词信号：自动化 / Coding Agent、RAG / Memory。 相关度中等，可快速浏览。 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | Memory | - 原文摘要：<p>Schottky barriers at Si/metal interfaces; agentic HLS; probabilistic memory for edge; agentic HW design automation as repository-level code evolution; HW fingerprinting for photonic ICs; functional safety; open | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P3 | TestCase | # 四、测试重点 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | ｜ 测试内容 ｜ 测试场景 ｜ 预期结果 ｜ | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | 知识整理 | # AI / Agent 每日情报简报 - 2026-07-12 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [A review of the applications of multi-agent reinforcement learning in smart factories.](https://doi.org/10.3389/frobt.2022.1027340) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [The Architecture Decisions Behind A Production-Ready EDA AI Agent](https://semiengineering.com/the-architecture-decisions-behind-a-production-ready-eda-ai-agent/) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [allcolor/PawFlow-Agents](https://github.com/allcolor/PawFlow-Agents) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [johannalberts/supply-chain-research-agent](https://github.com/johannalberts/supply-chain-research-agent) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [💬 Tech Community AI Digest 2026-07-04](https://github.com/kakapez/agents-radar/issues/628) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [📈 AI Open Source Trends 2026-07-12](https://github.com/kakapez/agents-radar/issues/735) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 中文导读：关注它是否提供 Agent 编排、状态管理、工具调用和生产化部署能力。 相关度较高，建议优先阅读。 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 分类：Agent 框架 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：# AI Open Source Trends 2026-07-12 > Sources: GitHub Trending + GitHub Search API ｜ Generated: 2026-07-11 22:48 UTC --- # AI Open Source Trends Report (2026-07-12) --- ## 1. Today's Highlights The 2026-07-12 GitHu | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：# Tech Community AI Digest 2026-07-04 > Sources: [Dev.to](https://dev.to/) (30 articles) + [Lobste.rs](https://lobste.rs/) (14 stories) ｜ Generated: 2026-07-03 23:04 UTC --- # Dev.to + Lobste.rs AI Community Diges | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：## Problem Ralph intentionally starts each iteration in a fresh agent context. That is one of its biggest strengths: it avoids context rot, keeps work bounded, and makes long-running implementation more reliable t | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：<p>As AI infrastructure fragments into specialized tiers, CPUs are becoming the orchestration layer for agentic workloads.</p> <p>The post <a href="https://semiengineering.com/from-host-node-to-heterogeneous-rack- | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：<p>Building an AI agent that works in semiconductor and PCB design requires solving problems that generic agentic frameworks were never designed to handle. </p> <p>The post <a href="https://semiengineering.com/the | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：CrewAI is a framework for orchestrating role-playing autonomous AI agents that collaborate on complex tasks. | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：PawFlow (Platform for Agentic Workflows) Self-hosted agent runtime for real infrastructure. Run durable AI agents against your own files, tools, browsers, desktops, services, and workflows with relay-backed execut | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 来源：GitHub repositories - AI agents recently updated | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 来源：GitHub repositories - agent frameworks | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | tags: [AI, Agent, 智能体, 情报简报] | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | type: ai-agent-intel | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 优先阅读相关度高且分类为“派工规则 / WIP / AMHS / MES / AI 调度”的条目 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对明显无关的条目记录噪声来源，并更新关键词 / 来源配置 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对涉及公司内部派工逻辑的启发，单独沉淀到内部专题笔记 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 将高价值条目移动到专题笔记或建立 wiki-link | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-12.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |

## 人工追加任务

- [ ] 把 Qsort 需求单整理成通俗介绍和 TestCase。
- [ ] 把 PM_Control 需求单整理成通俗介绍和 TestCase。
- [ ] 将 X Article 里提到的 Codex + Claude Code 工作系统拆成可执行蓝图。
