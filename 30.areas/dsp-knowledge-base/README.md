---
type: area
aliases: [DSP Knowledge Base, DSP 知识库]
tags: [DSP, RTD, AMA, 自动派工, KnowledgeBase]
updated: 2026-07-28
---

# DSP 业务知识库

本区承接原 `D:\Codex\projects\DSP_Workspace` 中可长期复用的内容，用于支撑 DSP 需求分析、RTD / AMA 逻辑设计、需求单、流程图、TestCase、Review 和案例复盘。

快速工作入口：[[30.areas/dsp-knowledge-base/Dashboard.md]]

## 内容地图

| 模块 | 入口 | 用途 |
|---|---|---|
| 系统边界 | [[30.areas/dsp-knowledge-base/00_System/README.md]] | RTD、AMA、MES、MCS / AMHS、EAP |
| SOP | [[30.areas/dsp-knowledge-base/01_SOP/README.md]] | TestCase、流程图规范；需求单完整 SOP 统一链接到需求单工程 |
| 业务逻辑 | [[30.areas/dsp-knowledge-base/02_Logic/README.md]] | 派工规则、QZone、WaferBalance、WPHLoss、PM Control、Qsort、NPW |
| 模板 | [[30.areas/requirement-writing/01_SOP/需求单模板.md]] | 统一需求模板；输入、TestCase、Review 模板继续保存在 DSP 区 |
| 案例 | [[30.areas/dsp-knowledge-base/04_Case/README.md]] | 案例模板与 STNLoadingBalance 案例 |
| Prompt | [[30.areas/dsp-knowledge-base/05_PromptLibrary/README.md]] | 生成、审查、流程图、风险检查与自然化 |
| Workflow | [[30.areas/dsp-knowledge-base/06_Workflow/README.md]] | 需求到交付、TestCase 和案例沉淀流程 |
| Review | [[30.areas/dsp-knowledge-base/07_ReviewAssistant/README.md]] | RTD、AMA、Report / DB、TestCase 检查清单 |
| 经验 | [[30.areas/dsp-knowledge-base/08_Experience/经验沉淀.md]] | 跨案例方法、升级记录 |
| 参考笔记 | [[30.areas/dsp-knowledge-base/09_Reference/PPT学习索引_v0.1.md]] | PPT 索引、WaferBalance 示例、图片学习归纳 |

## 关键主题

- 系统：[[30.areas/dsp-knowledge-base/00_System/RTD.md]]、[[30.areas/dsp-knowledge-base/00_System/AMA.md]]、[[30.areas/dsp-knowledge-base/00_System/MES.md]]、[[30.areas/dsp-knowledge-base/00_System/MCS.md]]
- 派工：[[30.areas/dsp-knowledge-base/02_Logic/DispatchRules.md]]、[[30.areas/dsp-knowledge-base/02_Logic/Sorting.md]]、[[30.areas/dsp-knowledge-base/02_Logic/Pirun.md]]
- Loading：[[30.areas/dsp-knowledge-base/02_Logic/WaferBalance.md]]、[[30.areas/dsp-knowledge-base/02_Logic/WPHLoss.md]]、[[30.areas/dsp-knowledge-base/02_Logic/PM_Control.md]]
- 约束：[[30.areas/dsp-knowledge-base/02_Logic/QZone.md]]、[[30.areas/dsp-knowledge-base/02_Logic/Qsort.md]]、[[30.areas/dsp-knowledge-base/02_Logic/NPW.md]]

## 证据与加工资料

- 91 页 DSP 培训资料：[[00.raw-materials/20.metadata/DSP派工系统简介-资料卡.md]]
- DSP PPT 结构化笔记：[[00.raw-materials/90.processed/dsp-dispatch-system-intro-notes/DSP派工系统简介-内容结构化.md]]
- 自动派工需求单 OCR 索引：[[00.raw-materials/90.processed/dispatch-requirements-notes/自动派工需求单图片-OCR索引.md]]
- 派工规则 TestCase：[[30.areas/agent-knowledge-ops/03.testcases/派工规则TestCase库.md]]

## 使用原则

- 本区是可执行知识，不替代正式需求单、系统代码或生产数据。
- 标为 `【待确认】` 的内容不得当作已确认事实。
- 字段名、数据源、计算公式和异常处理在交付前必须回查 Evidence。
- 新案例优先写入 `04_Case`，可复用规则再回写 `02_Logic`、`05_PromptLibrary` 或 `07_ReviewAssistant`。
