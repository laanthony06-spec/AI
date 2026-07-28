# Test Case Generator Prompt

> 用途：基于需求单生成测试用例，覆盖 Normal / Boundary / Exception / Recovery / Regression。

## 交付边界

- 需求单业务口径确认后再生成 Test Case。
- Test Case 不写入需求单正文。
- 最终直接生成 Excel `.xlsx`，Markdown 表格只用于必要的中间检查。
- 文件保存到 `00.raw-materials/90.processed/testcase-deliverables/`。

## 输入

```text
需求单：
涉及系统：
核心逻辑：
关键字段：
边界条件：
上线风险：
```

## 输出结构

| Test ID | 类型 | Purpose | Pre-condition | Input | Expected Result | DB Validation | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 类型要求

### Normal

- 主流程正常输入。
- 常见业务路径。
- 输出结果应与需求核心目标一致。

### Boundary

- 时间边界。
- 数量边界。
- Priority / Timeline / qsort category 边界。
- 空值、最大值、最小值。

### Exception

- 字段缺失。
- WPH / UPH 取不到。
- Lot 无可作业机台。
- 配置缺失。
- 机台 PM / Down / Hold 等异常。

### Recovery

- 配置修正后重新计算。
- 异常数据恢复后重新执行。
- Report 重算 / 补算。

### Regression

- 不影响原 Reason。
- 不影响原 Sorting。
- 不影响现有 AMA / RTD / MES / MCS / EAP 流程。

## 输出要求

- 输出文件名：`项目名_TestCase_vX.Y.xlsx`。
- Excel 主工作表名称：`TestCase`。
- Excel 中记录依据的需求单名称、版本和确认日期。
- 每个测试用例必须能对应需求单中的具体逻辑段落。
- 不确定字段写 `【待确认】`。
- 如果需求单缺少可测试条件，先列出“需求缺口”。
- 不得把生成的 Test Case 表格写回需求单 Word。
