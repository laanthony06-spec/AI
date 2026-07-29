---
type: agent-task-queue
updated: 2026-07-29T20:02:24
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
| todo | P1 | MCP / 工具接口 | ### [Add support for `2026-07-28` MCP Specification](https://github.com/reshaprio/reshapr/issues/285) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [Exercise: Integrate MCP with Copilot](https://github.com/ReehanaaAbdulRazak/skills-integrate-mcp-with-copilot/issues/1) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [Publish blog draft: Building an authenticated MCP server with Routecraft and Clerk](https://github.com/routecraftjs/routecraft/issues/506) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [feat: MCP tool validation and compatibility checking](https://github.com/Apicurio/apicurio-registry/issues/8427) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [极致IT MCP入门到实战67集完整版 少走99%的弯路 精品教程](https://github.com/dsfgfdg12345/DeepSeek-/issues/19) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | 知识整理 | 需求目标是什么：提升产能、降低 Cycle Time、减少 OverQtime、降低 WPH Loss，还是提升自动化率？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P2 | Hooks | 处理 Hook 事件：modified 00.raw-materials/20.metadata/2026-07-28_内容整合清单.md | Codex | modified | [[00.raw-materials/20.metadata/2026-07-28_内容整合清单.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Hooks | 处理 Hook 事件：modified 00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md | Codex | modified | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `30.areas/agent-knowledge-ops/07.hooks/` | 判断是否需要 OCR、整理、Evidence 或 TestCase |
| todo | P2 | Memory | ### [Show HN: CMEM – Persistent Memory for AI Coding Agents](https://cmem.ai) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | 知识整理 | - 将LithoAutoSplitPinn为由逻辑分批修改为物理分批，并优化Pilot选择逻辑。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P2 | 知识整理 | - 将LithoAutoSplitPinun为由逻辑分批修改力物理分批，并优化Pilot选择逻辑。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P2 | 知识整理 | 将LithoAutoSplitPinn为由逻辑分批修改为物理分批，并优化Pilot选择逻辑。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P2 | 知识整理 | 将LithoAutoSplitPinun为由逻辑分批修改力物理分批，并优化Pilot选择逻辑。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | TestCase | - 验证信息：结果, 需求 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | 验收标准是什么：测试 Case、前后对比指标、上线影响范围？ | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [A Self-Calibrating Agentic AI Framework for Autonomous Edge Resource Allocation](https://arxiv.org/abs/2607.22400v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [AgentAbstain: Do LLM Agents Know When Not to Act?](https://arxiv.org/abs/2607.10059) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Agentic CPU-GPU Scheduling for Heterogeneous AI Workloads](https://arxiv.org/abs/2607.22242v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture](https://arxiv.org/abs/2607.22445v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Feature Request: Support AGENTS.md.](https://github.com/anthropics/claude-code/issues/6235) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation](https://arxiv.org/abs/2607.22375v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [IDSTune: A Multi-Agent Collaborative Framework for Integrated Database System Tuning](https://arxiv.org/abs/2607.22031v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Is drift on websites still a problem for ai browser agents?](https://www.reddit.com/r/AI_Agents/comments/1v7x4w8/is_drift_on_websites_still_a_problem_for_ai/) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Nanbeige4.2-3B: Unlocking Agentic Capabilities in a Compact Mode](https://arxiv.org/abs/2607.22083v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Reliability-Contagion Feasibility in LLM Multi-Agent Networks](https://arxiv.org/abs/2607.21912v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Show HN: Rules that stop AI coding agents from breaking working code](https://github.com/avenna01-ceo/claude-code-survival-kr) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents](https://arxiv.org/abs/2607.22520v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [The state of AI agents, in numbers](https://www.getreadyforagents.com/statistics/) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Towards Trustworthy and Cost-Efficient Data Integration: From Naïve RAG to Agentic RAG](https://arxiv.org/abs/2607.22319v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Void8478/AgentFlow](https://github.com/Void8478/AgentFlow) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [dhruvb2028/AI-Research-Agent](https://github.com/dhruvb2028/AI-Research-Agent) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [junghakim2023/AI_AGENT_stock_agent](https://github.com/junghakim2023/AI_AGENT_stock_agent) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [📅 Daily Trending: AI Agents · LLMs · Governance — 2026-07-27](https://github.com/princeruhulofficial/github-trending/issues/18) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-27.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 处理状态：已 OCR，已建立初步结构化笔记 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 对于堆货机台，产能紧张，搬送时间过长可能造成机台空机等待IDLE，导致产能LOSs，为使Lot能尽快上机台作业，对于LP | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 对通过11筛选的Lot，向下Fetch20站，获取每个站点的productname、planname、stage、capability | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 将Lot的Wafer分为以下层级： | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 将剩余lot在Litho站点的机台经过EQPStatus、LCC、Capabiity、Recipe、PPID、Global Reason判断， | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 将排序第一的Lot-Context固定，作为已选Pilot的Context，并去除lotContext与已选Context相同的其 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 申请人员：张赛楠 功能模块（类别为3时必填）：智能派工系统（RTD/DSP） | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 申请人员：温洁奇 功能模快（类别为3时必填）=智能派工系统（RTD/DSP） | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 优先人工复核 OCR 标注为关键的需求单页面。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对仍含待办的 processed 笔记补充结论和下一步行动。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对厂Litho机台。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对敏感资料补充敏感级别和访问限制说明。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对章取的Lot执行以下过滤： | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对选1ot和选片逻辑进行修改。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对通过11筛选的Lot，向下Fetch20站，获取每个站点的productname、planname、stage、capability | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对长笔记拆成“索引页 + 专题页”。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 将剩余lot在Litho站点的机台经过EQPStatus、LCC、Capabiity、Recipe、PPID、Global Reason判断， | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 将排序第一的Lot-Context固定，作为已选Pilot的Context，并去除lotContext与已选Context相同的其 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 将高价值需求拆解为：背景、目标、输入、规则、输出、异常、验收标准。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 申请人员：温洁奇 功能模快（类别为3时必填）=智能派工系统（RTD/DSP） | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 申请日期：2026-07-24 希望交付期：2026-0729 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 申请部门：制造部 系统名称（类别内3时必填）：CIM计算机集成制造系统Fab6 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 规则属于 Global Rule、Local Rule，还是排序 / Prefer 逻辑？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 输入数据来自哪些系统：MES、RTD、AMA、EAP、MCS、APC、PMS？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 需要新增哪些异常原因码或查询页面？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |

## 已关闭自动任务

- 已关闭：7 条。
- 明细保存在 [[00.raw-materials/90.processed/agent-knowledge-ops/agent-dispatch-queue.json]]。

## 人工追加任务

- [ ] 把 Qsort 需求单整理成通俗介绍和 TestCase。
- [ ] 把 PM_Control 需求单整理成通俗介绍和 TestCase。
- [ ] 将 X Article 里提到的 Codex + Claude Code 工作系统拆成可执行蓝图。
