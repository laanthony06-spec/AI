# Qsort 计算逻辑

> 来源：`00.raw-materials/10.sources/images/Qsort/1.jpg` ~ `00.raw-materials/10.sources/images/Qsort/4.jpg`。  
> 注意：图片为拍照资料，以下为已读清楚部分的业务归纳；字段级公式使用前仍需回图或现行代码确认。

## 定位

Qsort 表示 Lot 到计算站点的最大允许等待时间。Lot 必须在 Qsort 时间内到达计算站点并上机台作业，否则良率可能受影响。

QZone 中 qsort category 固定为：

```text
0 / 6 / 12 / 24
```

注意：WaferBalance 中提到的 qsort 均指 Existing qsort，用于 Existing Lot 的 category 分层与 loading 继承计算；Virtual Lot qsort 是另一类计算入口，不作为 WaferBalance 中 category 计算的 qsort 来源。

## Process Time 取值原则

图片中反复强调：

- 当前站点 PT：按片数和 `Capability`。
- 其余站点 PT：按 `Recipe`，不按片数。
- Existing Lot 当前站点 `ProcessTime` 已改为按 `Capability` 的 wafer PT / step PT。

## Virtual Lot 计算

Virtual Lot 使用：

```text
Qsort = A - B
```

### A

```text
A = QTlimit
  + 连接站点的 ProcessTime
  + QTloop 起始站点的 ProcessTime
```

补充：

- 连接站点 ProcessTime 按 `Recipe`，不按片数。
- 连环 QT 需要加连接站点 PT。
- QTloop 起始站点 PT 按 Lot 片数和 `Capability`，不按 Recipe。

### B

```text
B = Target 站点至 QZone 结束站点前一站的 ProcessTime 累加
```

补充：

- ProcessTime 按 `Recipe`，不按片数。

## Existing Lot 计算

### 情况 1：Lot 在连环 QZone 起始站点作业

```text
Qsort = MAX(A, B)
```

其中：

```text
A = QTlimit 累加
  + 连接站点 PT
  + 当前站点 RemainPT
  - Target 站点至 QZone 结束站点前一站 PT 累加
```

```text
B = Target 站点前一站至当前站点 PT 累加
```

### 情况 2：Lot 在 Loop 中间站点等待作业 / 正在作业

若 Lot 所在 Loop 已 OverQT：

```text
Qsort = MAX(A, B)
```

其中：

```text
A = 当前站点至当前 QZone 结束站点前一站 PT
  + 其它 QtimeLimit
  + 连接站点 PT
  - Target 站点至 QZone 结束站点前一站 PT 累加
```

```text
B = Target 站点前一站至当前站点 PT 累加
```

若 Lot 未超 QT：

```text
Qsort = MAX(A, B)
```

其中：

```text
A = QTloop 的 QTlimit 累加
  - 已消耗 Qtime
  - Target 站点至 QZone 结束站点前一站 PT 累加
```

```text
B = Target 站点前一站至当前站点 PT 累加
```

### 情况 3：特殊当前状态

当 Existing Lot 当前状态为 `WaitForJobIn` / `JobOut`，且当前站点为 QTime 结束站时：

```text
当前站点 E_Qsort = 0
```

## 备注修订

- 2024/07/18 说明中出现过公式调整，涉及 safety value、高风险 loop、CT、merge qlimit 等内容，图片底部较模糊；需要后续用更清晰资料确认。
- 2024/07/31 说明：Existing Lot 当前站点的 `processtime` 已改为按 `capability` 的 wafer PT / step PT。

## 对其他逻辑的影响

Qsort 是以下逻辑的关键输入：

- QZone 放货判断。
- WaferBalance 的 Existing qsort category 分组。
- PM Control 原逻辑曾使用 Qsort 判断；现 PM 管控到站时间已改为 CycleTime 累计，详见 `PM_Control.md`。

## 待确认

- 公式中 `Target 站点`、`QZone 结束站点前一站` 在代码中的字段名。
- `RemainPT` 的取值来源。
- `E_Qsort` 与 qsort category 的映射关系。
- 2024/07/18 修订公式的完整内容。
