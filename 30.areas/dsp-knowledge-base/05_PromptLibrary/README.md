# 05_PromptLibrary

> DSP 高频 Prompt 库。目标是减少每次重新描述任务的成本。

## 推荐使用顺序

| 场景 | 使用文件 |
| --- | --- |
| 生成需求单 | `Requirement_Generator.md` |
| Review 需求单 | `Requirement_Reviewer.md` |
| 生成测试用例 | `TestCase_Generator.md` |
| 生成流程图 | `FlowChart_Generator.md` |
| 检查上线风险 | `Risk_Checker.md` |
| 降低需求单 AI 感 | `DSP_Humanizer.md` |
| 查看总览 | `Prompts.md` |

## 使用原则

- 先读项目知识，再使用 Prompt。
- Prompt 是工作流入口，不替代业务确认。
- 不确定字段统一写 `【待确认】`。
- 本地 DSP 工作可使用用户明确提供的真实表名、字段名、系统术语。
- `DSP_Humanizer.md` 只做表达后处理，不新增逻辑、不补待确认字段。
