# DSP Workspace v1.1 升级报告

## 升级目标

将 DSP Workspace 从“知识库骨架”升级为“可执行工作流工作台”，重点支持：

- DSP 需求分析
- Requirement 生成
- Test Case 生成
- 流程图生成
- Review 检查
- Case 沉淀

## 本次新增

### Prompt Library

- `05_PromptLibrary\Requirement_Generator.md`
- `05_PromptLibrary\Requirement_Reviewer.md`
- `05_PromptLibrary\TestCase_Generator.md`
- `05_PromptLibrary\FlowChart_Generator.md`
- `05_PromptLibrary\Risk_Checker.md`

### Workflow

- `06_Workflow\DSP_Requirement_Writer_Workflow.md`
- `06_Workflow\Requirement_to_TestCase_Workflow.md`
- `06_Workflow\Case_Capture_Workflow.md`

### Review Assistant

- `07_ReviewAssistant\Requirement_Review_Checklist.md`
- `07_ReviewAssistant\RTD_Impact_Checklist.md`
- `07_ReviewAssistant\AMA_Impact_Checklist.md`
- `07_ReviewAssistant\Report_DB_Checklist.md`
- `07_ReviewAssistant\TestCase_Review_Checklist.md`

### Template / Case

- `03_Template\Requirement_Input_Form.md`
- `04_Case\Case_STNLoadingBalance_v0.1.md`

## 使用建议

处理新 DSP 需求时，从以下文件开始：

```text
06_Workflow\DSP_Requirement_Writer_Workflow.md
05_PromptLibrary\Requirement_Generator.md
07_ReviewAssistant\Requirement_Review_Checklist.md
```

生成测试用例时读取：

```text
06_Workflow\Requirement_to_TestCase_Workflow.md
05_PromptLibrary\TestCase_Generator.md
07_ReviewAssistant\TestCase_Review_Checklist.md
```

完成需求后读取：

```text
06_Workflow\Case_Capture_Workflow.md
04_Case\Case_Template.md
```

## 健康检查

- 目录结构：已存在。
- Prompt Library：已从单一总览扩展为独立高频 Prompt。
- Workflow：已新增主工作流和 Case 沉淀流程。
- Review Assistant：已新增分场景 Checklist。
- Case Library：已新增 STNLoadingBalance 工作中案例。
- 外部 Skill：本次未安装。原因是当前更需要固化本地 DSP SOP / Case / Workflow；外部 Skill 可后续按需评估。

## 下一步建议

1. 用 STNLoadingBalance 跑一次完整链路：Requirement → Test Case → Review。
2. 将 WaferBalance 示例沉淀为正式 Case。
3. 待 2~3 个真实需求稳定后，再考虑把 `DSP Requirement Writer` 封装为 Codex Skill。

