---
type: agent-task-queue
updated: 2026-08-01T17:21:12
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
| todo | P1 | MCP / 工具接口 | ### [Autonomous AI Shopping Assistant Playground with Real-Time MCP Tool Call Inspector](https://github.com/abhisek2004/62Days-CodeSprint-WebDev-Challenge/issues/320) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [Exercise: Integrate MCP with Copilot](https://github.com/Potato061/mcp-exer/issues/1) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [GENAI - MCP Registry](https://github.com/constructorfabric/gears-rust/issues/4329) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [M2.5: MCP adapter (thin, over the core)](https://github.com/mandaloriat/fenix-spoon/issues/49) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [Phase 17: MCP Execution Fabric Integration — Governed interoperability without replacing Gummy architecture](https://github.com/bohselecta/gummy-os/issues/36) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [Server instructions from initialize response not passed to model](https://github.com/anthropics/claude-ai-mcp/issues/93) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [YogevBokobza/health-mcp](https://github.com/YogevBokobza/health-mcp) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [bug: MCP tool handlers return errors as "Error: ..." strings instead of structured error responses](https://github.com/nunchi-labs/sdk/issues/479) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [feat(registry): unify agent tools behind an AgentCore Gateway (managed MCP aggregation + dual-sided auth, any substrate)](https://github.com/aws-samples/sample-autonomous-cloud-coding-agents/issues/641) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [feat: implement Dockerized Auditing Daemon & MCP Server Support (Phase 17)](https://github.com/jmrenouard/MySQLTuner-perl/issues/62) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [feat: implement Dockerized Auditing Daemon & MCP Server Support (Phase 17)](https://github.com/major/MySQLTuner-perl/issues/954) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [security: .cursor/ directory not in .gitignore — AI IDE config (including future MCP credentials) can be accidentally committed](https://github.com/nunchi-labs/sdk/issues/810) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | MCP / 工具接口 | ### [test(mcp): add tests for MCP server behavior against an empty database](https://github.com/AbdulmalikAlayande/sorokeep/issues/468) | Codex（先本地只读） | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/05.mcp-server/` | 人工确认后执行 |
| todo | P1 | 知识整理 | 需求目标是什么：提升产能、降低 Cycle Time、减少 OverQtime、降低 WPH Loss，还是提升自动化率？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P2 | Memory | ### [Incoming Work-In-Progress Prediction in Semiconductor Fabrication Foundry Using Long Short-Term Memory.](https://doi.org/10.1155/2019/8729367) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | Memory | ### [UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams](https://arxiv.org/abs/2607.26017v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `30.areas/agent-knowledge-ops/06.memory/` | 人工确认后执行 |
| todo | P2 | 知识整理 | - 将LithoAutoSplitPinn为由逻辑分批修改为物理分批，并优化Pilot选择逻辑。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P2 | 知识整理 | - 将LithoAutoSplitPinun为由逻辑分批修改力物理分批，并优化Pilot选择逻辑。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P2 | 知识整理 | 将LithoAutoSplitPinn为由逻辑分批修改为物理分批，并优化Pilot选择逻辑。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P2 | 知识整理 | 将LithoAutoSplitPinun为由逻辑分批修改力物理分批，并优化Pilot选择逻辑。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | TestCase | - 验证信息：结果, 需求 | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | TestCase | 验收标准是什么：测试 Case、前后对比指标、上线影响范围？ | Codex | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `30.areas/agent-knowledge-ops/03.testcases/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [A review of the applications of multi-agent reinforcement learning in smart factories.](https://doi.org/10.3389/frobt.2022.1027340) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [AI Agent Orchestration For ASIC Autonomy](https://semiengineering.com/ai-agent-orchestration-for-asic-autonomy/) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Agentic AI in medicine: architectures, applications, evaluation, and challenges for clinical translation](https://arxiv.org/abs/2607.25489v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [AnjanaMadhushanaj/Heart_Agent_App](https://github.com/AnjanaMadhushanaj/Heart_Agent_App) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Dylanperry04/ai-triage-agentic-system](https://github.com/Dylanperry04/ai-triage-agentic-system) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs](https://arxiv.org/abs/2607.25853v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents](https://arxiv.org/abs/2607.25485v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks](https://arxiv.org/abs/2607.25877v1) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [Upstream update: microsoft-agent-framework](https://github.com/managedcode/dotnet-skills/issues/1163) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [WaniyaKhan211/Agentic_AI_Essay_Writer](https://github.com/WaniyaKhan211/Agentic_AI_Essay_Writer) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [bhakti857/AgenticCommercePlatform](https://github.com/bhakti857/AgenticCommercePlatform) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [johannalberts/supply-chain-research-agent](https://github.com/johannalberts/supply-chain-research-agent) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [mohamedalaaabdella-maker/Agentic-RAG-System](https://github.com/mohamedalaaabdella-maker/Agentic-RAG-System) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | ### [yusheng-g/openagent-go](https://github.com/yusheng-g/openagent-go) | Codex + 人工复核 | brief_or_note_scan | [[30.areas/ai-agent-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 处理状态：已 OCR，已建立初步结构化笔记 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 对于堆货机台，产能紧张，搬送时间过长可能造成机台空机等待IDLE，导致产能LOSs，为使Lot能尽快上机台作业，对于LP | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 对通过11筛选的Lot，向下Fetch20站，获取每个站点的productname、planname、stage、capability | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 将Lot的Wafer分为以下层级： | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 将剩余lot在Litho站点的机台经过EQPStatus、LCC、Capabiity、Recipe、PPID、Global Reason判断， | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 将排序第一的Lot-Context固定，作为已选Pilot的Context，并去除lotContext与已选Context相同的其 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 申请人员：张赛楠 功能模块（类别为3时必填）：智能派工系统（RTD/DSP） | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | - 申请人员：温洁奇 功能模快（类别为3时必填）=智能派工系统（RTD/DSP） | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 优先人工复核 OCR 标注为关键的需求单页面。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 优先阅读相关度高且分类为“派工规则 / WIP / AMHS / MES / AI 调度”的条目 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对仍含待办的 processed 笔记补充结论和下一步行动。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对厂Litho机台。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对敏感资料补充敏感级别和访问限制说明。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对明显无关的条目记录噪声来源，并更新关键词 / 来源配置 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对涉及公司内部派工逻辑的启发，单独沉淀到内部专题笔记 | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对章取的Lot执行以下过滤： | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对选1ot和选片逻辑进行修改。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对通过11筛选的Lot，向下Fetch20站，获取每个站点的productname、planname、stage、capability | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 对长笔记拆成“索引页 + 专题页”。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 将剩余lot在Litho站点的机台经过EQPStatus、LCC、Capabiity、Recipe、PPID、Global Reason判断， | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 将排序第一的Lot-Context固定，作为已选Pilot的Context，并去除lotContext与已选Context相同的其 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 将高价值条目移动到专题笔记或建立 wiki-link | Codex + 人工复核 | brief_or_note_scan | [[30.areas/semiconductor-dispatch-intel/inbox/2026-07-29.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 将高价值需求拆解为：背景、目标、输入、规则、输出、异常、验收标准。 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/weekly-knowledge-distill/2026-07-27-每周原始资料知识提纯.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 申请人员：温洁奇 功能模快（类别为3时必填）=智能派工系统（RTD/DSP） | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 申请日期：2026-07-24 希望交付期：2026-0729 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 申请部门：制造部 系统名称（类别内3时必填）：CIM计算机集成制造系统Fab6 | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 规则属于 Global Rule、Local Rule，还是排序 / Prefer 逻辑？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 输入数据来自哪些系统：MES、RTD、AMA、EAP、MCS、APC、PMS？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |
| todo | P3 | 知识整理 | 需要新增哪些异常原因码或查询页面？ | Codex + 人工复核 | brief_or_note_scan | [[00.raw-materials/90.processed/dispatch-requirements-notes/LithoAutoPiRun-需求单整理.md]] | `00.raw-materials/90.processed/agent-knowledge-ops/` | 人工确认后执行 |

## 已关闭自动任务

- 已关闭：0 条。
- 明细保存在 [[00.raw-materials/90.processed/agent-knowledge-ops/agent-dispatch-queue.json]]。

## 人工追加任务

- [ ] 把 Qsort 需求单整理成通俗介绍和 TestCase。
- [ ] 把 PM_Control 需求单整理成通俗介绍和 TestCase。
- [ ] 将 X Article 里提到的 Codex + Claude Code 工作系统拆成可执行蓝图。
