# Test Case SOP

> 来源：`00.raw-materials/10.sources/images/TestCase_SOP/TestCase要求\1.jpg`、`2.jpg`，以及 `00.raw-materials/10.sources/images/TestCase_SOP/TestCase示例\case1.jpg` ~ `case5.jpg`。

## 功能涉及清单

编写 Test Case 前，先列出本需求涉及范围，避免漏测：

- 涉及厂别：单厂 / 跨厂。
- 涉及 Macro：Macro1 / Macro2 / Macro3 等。
- 涉及 Report：Report1 / Report2 / Report3 / Report4 等。
- 涉及功能模块：功能模块1 / 2 / 3 / 4 等。
- 涉及 AMA Rule：AMA MainJobName。
- 涉及接口：接口1 / 2 / 3 等。

## 测试用例分类

- Normal：正常路径。
- Boundary：边界条件。
- Exception：异常输入 / 异常状态。
- Recovery：异常恢复。
- Regression：回归测试。

## 公司模板字段

图片示例中的测试用例表字段为：

- `No`
- `所属(Local/Central)`
- `Area(功能模块 Report/Rule/AMA)`
- `涉及 Macro / 共通模块`
- `逻辑变动内容`
- `类别（正向 / 反向 / 特殊符号处理）`
- `测试内容`
- `测试情景`
- `预期结果`
- `测试结果`
- `测试日期`
- `测试 owner`

## 每条测试用例字段

- Case ID
- 测试目的
- 前置条件
- 输入数据
- 操作步骤
- 预期结果
- 涉及系统
- 备注 / 待确认

## 测试大类与标准

### 单点模块测试

- 正 / 反向测试：每个判断指标正确，生效符合预期。
- 特殊符号处理：特殊符号、空值、NULL、默认值应正确处理。
- 边界值处理：大于、小于、等于、空值、极值、比较关系都要覆盖。
- 数据处理：合并、去重、过滤、格式、上下游一致性，不应误删或重复。
- Branch / 主环 Branch 交互：Normal、Branch、Adhoc、RC、RRC、Rework、OCAP 等 Lot 场景要覆盖。
- MultiLot：同 FOUP 多 Lot、Batch 特殊处理。
- 厂别判定：单厂 / 跨厂、Lot 同时存在多厂别时的站点信息。
- CrossFab 中间态：CrossFabTransferred、Cross 途中、跨厂参数归属。
- 产品客制化：配置命中、产品不支持 recipe、空值或大小写影响。
- 对比验证：改动前后数据差异应符合需求。

### 功能模块联动测试

- 正 / 反向测试：参数输出正确，非改动指标不受影响。
- 对比验证：Rule、接口、AMA、Report 输出均符合预期。
- 性能测试：若修改影响整段功能或大批量数据，需要验证性能影响。

### 全场景完整性测试

- 对修改模块涉及的功能与场景做一次梳理，并测试验证结果。

### 他系统配套管控

- 与 R2R / MES / MCS 等相关逻辑对齐。

### 跨组 / 科室 / 部门联合验证

- 涉及多方功能时，视需求情况联合用户协同测试。

## 编写原则

- 每条用例只验证一个核心判断。
- 预期结果必须可验证。
- 涉及未知字段写 `【待确认】`。
- RTD / AMA 同时受影响时，测试用例需分别覆盖。
- 不写“功能正常”这类不可验证结论；要写清楚输入、命中条件、输出字段或系统行为。
- 一个逻辑点通常至少拆成正向、反向、边界 / 特殊值三类。
- 涉及 Flow 类型时，需考虑 Normal、Runcard、Branch / Rework 等组合。
