---
type: agent-task-queue
updated: 2026-07-10T20:21:50
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
| todo | P1 | MCP / 工具接口 | ### [Refusal training for LLM agents against disguised MCP attacks](https://github.com/johnhalloran321/mcp_safety_training) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP、评测 / 安全。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它是否提供 Agent 编排、状态管理、工具调用和生产化部署能力。 关键词信号：工具调用 / MCP、评测 / 安全。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：建议提取问题定义、方法、实验指标和可复用模型结构。 关键词信号：工具调用 / MCP、多智能体。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 分类：工具调用 / MCP | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 原文摘要：Article URL: https://github.com/johnhalloran321/mcp_safety_training Comments URL: https://news.ycombinator.com/item?id=48834106 Points: 1 # Comments: 0 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 本简报聚焦 AI Agent、LLM Agent、多智能体、工具调用、MCP、Coding Agent、RAG / Memory、评测与安全。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/LithoAutoPirun优化/1.jpg | Codex | created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/1.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/LithoAutoPirun优化/2.jpg | Codex | created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/2.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/LithoAutoPirun优化/3.jpg | Codex | created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/3.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/LithoAutoPirun优化/4.jpg | Codex | created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/4.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/LithoAutoPirun优化/5.jpg | Codex | created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/5.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/LithoAutoPirun优化/6.jpg | Codex | created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/6.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/LithoAutoPirun优化/7.jpg | Codex | created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/7.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/LithoAutoPirun优化/8.jpg | Codex | created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/8.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/10.sources/images/LithoAutoPirun优化/9.jpg | Codex | created | [[00.raw-materials/10.sources/images/LithoAutoPirun优化/9.jpg]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.2.docx | Codex | created | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.2.docx]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.2.md | Codex | created | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.2.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.docx | Codex | created | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.docx]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.md | Codex | created | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/90.processed/dispatch-requirements-notes/render_LithoAutoSplitPirun_v0.2_manual/litho_physical_split_v02.docx | Codex | created | [[00.raw-materials/90.processed/dispatch-requirements-notes/render_LithoAutoSplitPirun_v0.2_manual/litho_physical_split_v02.docx]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 00.raw-materials/90.processed/dispatch-requirements-notes/render_LithoAutoSplitPirun_v0.2_manual/test.docx | Codex | created | [[00.raw-materials/90.processed/dispatch-requirements-notes/render_LithoAutoSplitPirun_v0.2_manual/test.docx]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 30.areas/ai-agent-intel/inbox/2026-07-09.md | Codex | created | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：created 30.areas/semiconductor-dispatch-intel/inbox/2026-07-09.md | Codex | created | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Memory | ### [A hierarchical memory architecture overcomes context limits in long-horizon multi-agent computational modeling](https://arxiv.org/abs/2607.07666v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | Memory | ### [Incoming Work-In-Progress Prediction in Semiconductor Fabrication Foundry Using Long Short-Term Memory.](https://doi.org/10.1155/2019/8729367) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | Memory | - 中文导读：建议提取问题定义、方法、实验指标和可复用模型结构。 关键词信号：多智能体、RAG / Memory、评测 / 安全。 相关度较高，建议优先阅读。 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P3 | TestCase | # 四、测试重点 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | ｜ 测试内容 ｜ 测试场景 ｜ 预期结果 ｜ | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoSplitPirun物理分批优化需求单_v0.3.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | 安全预检 | - 中文导读：建议提取问题定义、方法、实验指标和可复用模型结构。 关键词信号：评测 / 安全。 相关度较高，建议优先阅读。 | 人工确认 + Codex | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | # AI / Agent 每日情报简报 - 2026-07-09 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [A review of the applications of multi-agent reinforcement learning in smart factories.](https://doi.org/10.3389/frobt.2022.1027340) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Agent-Exploitation Affordances: From Basic to Complex Representation Patterns](https://arxiv.org/abs/2607.07475v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents](https://arxiv.org/abs/2607.07321v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Physics-Audited Agentic Discovery in Scientific Machine Learning](https://arxiv.org/abs/2607.07379v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Show HN: microide, a 100% vibecoded IDE that LLM agents can drive](https://pablojimenezmateo.github.io/microide/) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [johannalberts/supply-chain-research-agent](https://github.com/johannalberts/supply-chain-research-agent) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 分类：Agent 框架 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：I want to be very upfront: this IDE's code is 100% generated by LLMs supervised by me, I am not hiding this fact. This submission was written by a human. microide's focus is performance and privacy, I was very tir | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：In agentic scientific machine learning (SciML), large language model (LLM) agents can discover surrogate models and select one by an automated score, typically an error metric. A low error, however, does not estab | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：Large language models (LLMs) demonstrate remarkable reasoning capabilities, yet their stateless architecture fundamentally limits deployment in long-horizon research workflows requiring multi-session continuity an | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：Tool utilization enables Large Language Model (LLM) agents to interact with the real world and resolve complex tasks. However, existing agent frameworks predominantly rely on static toolsets composed of granular a | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 来源：Hacker News - LLM agent | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 来源：arXiv cs.AI agent search | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | tags: [AI, Agent, 智能体, 情报简报] | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | type: ai-agent-intel | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 优先阅读相关度高且分类为“派工规则 / WIP / AMHS / MES / AI 调度”的条目 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对明显无关的条目记录噪声来源，并更新关键词 / 来源配置 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对涉及公司内部派工逻辑的启发，单独沉淀到内部专题笔记 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 将高价值条目移动到专题笔记或建立 wiki-link | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-09.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |

## 人工追加任务

- [ ] 把 Qsort 需求单整理成通俗介绍和 TestCase。
- [ ] 把 PM_Control 需求单整理成通俗介绍和 TestCase。
- [ ] 将 X Article 里提到的 Codex + Claude Code 工作系统拆成可执行蓝图。
