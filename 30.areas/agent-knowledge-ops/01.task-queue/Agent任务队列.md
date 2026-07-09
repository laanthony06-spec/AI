---
type: agent-task-queue
updated: 2026-07-09T21:44:32
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
| todo | P1 | MCP / 工具接口 | ### [Docs Feedback modules/ROOT/pages/index.adoc (ref: main)](https://github.com/neo4j/docs-mcp/issues/19) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [Expose the auditor as an MCP server so AI assistants can run audits directly](https://github.com/asish-singh/agent-readiness-auditor/issues/1) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [feat: Blawby MCP agent surface](https://github.com/Blawby/blawby-ai-chatbot/issues/579) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注 API、SDK、平台能力变化，以及是否会影响你的工具链选择。 关键词信号：工具调用 / MCP、RAG / Memory。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP。 相关度中等，可快速浏览。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。 关键词信号：工具调用 / MCP。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 中文导读：关注它是否提供 Agent 编排、状态管理、工具调用和生产化部署能力。 关键词信号：工具调用 / MCP。 相关度较高，建议优先阅读。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 分类：工具调用 / MCP | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 原文摘要：# feat: Blawby MCP agent surface > **Full plan:** [`docs/plans/2026-05-15-002-feat-blawby-mcp-agent-surface-plan.md`](docs/plans/2026-05-15-002-feat-blawby-mcp-agent-surface-plan.md) (commit pending) > **Origin re | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 本简报聚焦 AI Agent、LLM Agent、多智能体、工具调用、MCP、Coding Agent、RAG / Memory、评测与安全。 | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | - 来源：GitHub issues - MCP agents | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | TestCase | ![[00.raw-materials/10.sources/images/TestCase_SOP/TestCase示例/case1.jpg]] | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P1 | TestCase | ![[00.raw-materials/10.sources/images/TestCase_SOP/TestCase示例/case2.jpg]] | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P1 | TestCase | # TestCase_SOP/TestCase示例 - 需求单整理 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P1 | TestCase | - OCR 输出目录：[[00.raw-materials/90.processed/dispatch-requirements-ocr/TestCase_SOP__TestCase示例]] | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P1 | TestCase | - 初步主题：TestCase / SOP / 验证规范 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P1 | TestCase | - 原始图片目录：[[00.raw-materials/10.sources/images/TestCase_SOP/TestCase示例]] | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P1 | TestCase | source_folder: TestCase_SOP/TestCase示例 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P1 | TestCase | topic: TestCase / SOP / 验证规范 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P1 | 知识整理 | 需求目标是什么：提升产能、降低 Cycle Time、减少 OverQtime、降低 WPH Loss，还是提升自动化率？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P2 | Memory | ### [Incoming Work-In-Progress Prediction in Semiconductor Fabrication Foundry Using Long Short-Term Memory.](https://doi.org/10.1155/2019/8729367) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | Memory | - 中文导读：关注它是否提供 Agent 编排、状态管理、工具调用和生产化部署能力。 关键词信号：RAG / Memory、评测 / 安全。 相关度中等，可快速浏览。 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | 知识整理 | ## 待澄清问题 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | TestCase | (Local/central) 所属 Report/Rule/AMA) Area(功能模块 涉及Iacro/共通模块 逻辑变动内容 类别（正向/方 向/特殊符号处 理） 测试内容 1增加四列栏位：N2OHB临界值（N2OHBUseRatio）N2STK临界值 （N2STKUseRatio）SpecialN2OHB临界值（SpecialN2OHBRatio) 测试情景 特殊处理当不配置时给个默认值，不会出现无 预期结果 测试结 Pass/ | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | - (Local/central) 所属 Report/Rule/AMA) Area(功能模块 涉及Iacro/共通模块 逻辑变动内容 类别（正向/方 向/特殊符号处 理） 测试内容 1增加四列栏位：N2OHB临界值（N2OHBUseRatio）N2STK临界值 （N2STKUseRatio）SpecialN2OHB临界值（SpecialN2OHBRatio) 测试情景 特殊处理当不配置时给个默认值，不会出现无 预期结果 测试结 Pas | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | - No 所尾（Local/central） Repor/Rale/AMA) Arex(功配换快 适猫变动内容 类别（正尚/方向/特殊符号处理） 测试结果 则试日期 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | - 当EqptypeinOHBP lotOHB/STK判断逻辑验证 STKP则为XCDAIsXCDAPurgeOHB/ （USEDTargetFab）计算实时的loading | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | - 特殊符号处理 UlWhereNext修改栏位 SpecialN2STK临界值（SpecialN2STKRatio）null值测试.从UI拿取配 法比较情况，可正确从UI中拿取配置信息 Pass/Fail Pass/Fail XXXX XXXX | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | - 验证信息：Case, Test, 测试, 结果, 需求 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | 1.OHB/STKname以及位置与利用率ratio数据验证 Pass/ail XXXX | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | No 所尾（Local/central） Repor/Rale/AMA) Arex(功配换快 适猫变动内容 类别（正尚/方向/特殊符号处理） 测试结果 则试日期 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | 当EqptypeinOHBP lotOHB/STK判断逻辑验证 STKP则为XCDAIsXCDAPurgeOHB/ （USEDTargetFab）计算实时的loading | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | 正向 存储位loading公式 1.利用率公式验证：储位loading公式 -(usedcapacity+used+USEDTargetFab/(availcapacity+usedcapacity) 1利用率loading公式更新！考虑到了 (systime-creattime）内的transfer数量 （USEDTargetFab）计算实时的loading Pass/Fall Pass/Fail Pass/Fail XXXX | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | 特殊符号处理 UlWhereNext修改栏位 SpecialN2STK临界值（SpecialN2STKRatio）null值测试.从UI拿取配 法比较情况，可正确从UI中拿取配置信息 Pass/Fail Pass/Fail XXXX XXXX | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | 验收标准是什么：测试 Case、前后对比指标、上线影响范围？ | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | 知识整理 | # AI / Agent 每日情报简报 - 2026-07-07 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [A review of the applications of multi-agent reinforcement learning in smart factories.](https://doi.org/10.3389/frobt.2022.1027340) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Agent-based dynamic scheduling for semiconductor wafer fab](https://www.semanticscholar.org/paper/db062b192daf596c3fa49d24b5c3ed2dcb9299dc) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Mdhu8768/awesome-ai-agents](https://github.com/Mdhu8768/awesome-ai-agents) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [johannalberts/supply-chain-research-agent](https://github.com/johannalberts/supply-chain-research-agent) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [💬 Tech Community AI Digest 2026-07-07](https://github.com/ys578/agents-radar/issues/133) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [💬 技术社区 AI 动态日报 2026-07-07](https://github.com/ys578/agents-radar/issues/132) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 分类：Agent 框架 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：# 技术社区 AI 动态日报 2026-07-07 > 数据来源: [Dev.to](https://dev.to/) (30 篇) + [Lobste.rs](https://lobste.rs/) (4 条) ｜ 生成时间: 2026-07-07 11:21 UTC --- 好的，这是为您生成的《技术社区 AI 动态日报》。 --- ### 技术社区 AI 动态日报 ｜ 2026-07-07 #### 1. 今日速览  | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：## Problem Today the audit requires a terminal and an npx command. But the people most curious about agent readiness are increasingly working *inside* AI assistants (Claude, ChatGPT, IDE agents). For them, the too | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：> Do not include confidential information, personal data, sensitive data, or other regulated data. With refereence to Linear [DEVSURF-1281](https://linear.app/neo4j/issue/DEVSURF-1281/doc-changes-for-legal-require | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：Explore a curated list of AI agent frameworks, tools, and resources for building autonomous and semi-autonomous systems | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 原文摘要：Extracts every question from RFP/DDQ questionnaires (Word/PDF/Excel) into structured, retrieval-ready JSON — dual-leg LLM extraction with reconciliation, atomic decomposition and granularity views. .NET 10 + Micro | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 来源：GitHub repositories - agent frameworks | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | tags: [AI, Agent, 智能体, 情报简报] | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | type: ai-agent-intel | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 优先阅读相关度高且分类为“派工规则 / WIP / AMHS / MES / AI 调度”的条目 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对明显无关的条目记录噪声来源，并更新关键词 / 来源配置 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对涉及公司内部派工逻辑的启发，单独沉淀到内部专题笔记 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 将高价值条目移动到专题笔记或建立 wiki-link | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-07.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 规则属于 Global Rule、Local Rule，还是排序 / Prefer 逻辑？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 输入数据来自哪些系统：MES、RTD、AMA、EAP、MCS、APC、PMS？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 需要新增哪些异常原因码或查询页面？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/TestCase_SOP__TestCase示例-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |

## 人工追加任务

- [ ] 把 Qsort 需求单整理成通俗介绍和 TestCase。
- [ ] 把 PM_Control 需求单整理成通俗介绍和 TestCase。
- [ ] 将 X Article 里提到的 Codex + Claude Code 工作系统拆成可执行蓝图。
