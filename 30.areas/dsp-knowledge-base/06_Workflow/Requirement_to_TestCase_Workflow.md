# Requirement to TestCase Workflow

> 用途：从需求单生成可执行测试用例。

## 输入

- 需求单最终稿
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
输出测试用例
```

## 检查重点

- 每条新逻辑至少对应一条 Normal Case。
- 每个判断条件至少有正反两类 Case。
- 每个待确认边界形成测试条件。
- Report 字段需要 DB Validation。
- Priority / Timeline / qsort / PM / WPH 等数值规则必须有边界 Case。

