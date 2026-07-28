# Requirement to Test Case Excel Workflow

> 用途：在需求单业务口径确认后，单独生成可执行的 Test Case Excel。

## 交付边界

- Test Case 不写入需求单正文。
- 需求单只需达到“规则可以被测试”的完整度。
- Test Case 是需求单之后的独立工作项。
- 最终交付为 `.xlsx`，保存到 `00.raw-materials/90.processed/testcase-deliverables/`。
- Excel 中记录依据的需求单名称、版本和确认日期。

## 输入

- 已确认业务口径的需求单
- 流程图
- Report 字段说明
- UI / Rule / DB 修改点
- 待确认事项的最终结论

## 流程

```text
读取需求单
↓
拆解核心逻辑
↓
提取输入字段 / 输出字段
↓
识别判断条件
↓
识别边界和异常
↓
生成 Normal / Boundary / Exception / Recovery / Regression
↓
补充 DB Validation
↓
生成独立 Test Case Excel
↓
检查需求条款与 Case 覆盖关系
```

## Excel 输出

主工作表建议命名为 `TestCase`，字段按 [[30.areas/dsp-knowledge-base/01_SOP/TestCase_SOP.md]] 执行。文件命名：

```text
项目名_TestCase_vX.Y.xlsx
```

## 检查重点

- 每条新逻辑至少对应一条 Normal Case。
- 每个判断条件至少有正反两类 Case。
- 每个待确认边界形成测试条件。
- Report 字段需要 DB Validation。
- Priority / Timeline / qsort / PM / WPH 等数值规则必须有边界 Case。
- 不得把 Test Case 表格回填到需求单 Word。
