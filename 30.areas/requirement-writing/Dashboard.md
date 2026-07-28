---
type: dashboard
tags: [需求单, SOP, Review]
---

# 需求单工程 Dashboard

Word 需求单默认使用个人模板 `$artifact-template-word`，参考现有“新增需求申请单”表格框架。模板控制版式与章节骨架，业务事实仍按本次需求重新确认。

## 开始一个需求

1. 用 [[30.areas/dsp-knowledge-base/03_Template/Requirement_Input_Form.md]] 收集输入。
2. 按 [[30.areas/requirement-writing/01_SOP/需求事实来源与变更基线规则.md]] 声明本次新增、修改、删除、保持不变和不调整范围。
3. 查阅相关系统、历史需求和知识稿，将其作为对照证据，不自动覆盖本次需求。
4. 对新旧口径建立冲突清单，并确认哪些差异属于本次有意变更。
5. 按 [[30.areas/requirement-writing/01_SOP/需求单SOP提炼.md]] 形成结构。
6. 使用统一模板：[[30.areas/requirement-writing/01_SOP/需求单模板.md]]。
7. 用 [[30.areas/dsp-knowledge-base/07_ReviewAssistant/Requirement_Review_Checklist.md]] 做完整性检查。
8. 用 [[30.areas/requirement-writing/01_SOP/需求单工程化降AI风格规则.md]] 做最终语言收口。
9. 仅将已经确认的新规则回写 DSP 知识库和案例库。

项目与版本总入口：[[30.areas/requirement-writing/02_Cases/README.md]]

## 最新案例

- 项目与版本总览：[[30.areas/requirement-writing/02_Cases/README.md]]
- STNLoadingBalance：[[30.areas/requirement-writing/02_Cases/STNLoadingBalance/STNLoadingBalance需求单_优化稿_v1.1.md]]
- LoadingCandidateLot 分析：[[30.areas/requirement-writing/02_Cases/STNLoadingBalance/STNLoadingBalance_LoadingCandidateLot需求内容分析_v0.1.md]]
- Litho 物理分批：[[30.areas/requirement-writing/02_Cases/LithoAutoSplitPirun/LithoAutoSplitPirun物理分批及选Pilot逻辑优化需求单_v0.5.md]]
- Pilot 动态排序：[[30.areas/requirement-writing/02_Cases/LithoAutoSplitPirun/LithoAutoSplitPirun_Pilot动态挑选排序规则_最终版_v1.0.md]]
- CMP Auto Pirun：[[30.areas/requirement-writing/02_Cases/CMPAutoPirun/README.md]]

## 质量关口

- 是否区分“当前实际逻辑、历史文档逻辑、本次目标逻辑”。
- 新稿与旧稿的冲突是否已经分类，不能仅凭版本号判断对错。
- 字段、表名、接口、异常处理是否有 Evidence。
- 原逻辑、变更逻辑、影响范围、测试重点是否分开表达。
- 是否保留待确认项，且没有把推断写成事实。
- Word / PPT 与 Markdown 的版本是否一致；不一致时明确标注。
