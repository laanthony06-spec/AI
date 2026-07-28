# WaferBalance

> 来源：`00.raw-materials/10.sources/images/WaferBalance/需求单1.jpg`、`需求单2.jpg`、`表1.jpg`，并结合用户在 2026-06-27、2026-06-28 的确认修正。

## 定位

WaferBalance 是 QZoneControl 中用于 loop 内 WIP balance 的逻辑，用于评估待派工 Lot 放入 loop 后，下游机台产能与 loading 是否仍可支撑 Lot 在 Existing qsort 时间内到达计算站点并上机台作业。

它不是简单平均分配，也不是只做一次权重分配，而是：

```text
第一次 Balance：按可作业机台 WPH 比例分配 Lot wafer qty
后续 Balance：根据上一轮权重重新分配
共执行 5 次 Balance
```

## Qsort / category

WaferBalance 中提到的 qsort 均指 Existing qsort，不是 Virtual Lot qsort。

Existing qsort 表示 Existing Lot 到计算站点的最大允许等待时间。Lot 必须在 Existing qsort 时间内到达计算站点并上机台作业，否则良率可能受到影响。

QZone 中 qsort category 固定划分为：

```text
0、6、12、24
```

按 category 从小到大处理：

```text
0 → 6 → 12 → 24
```

后一 category 继承前一 category 的机台累计作业时间；因为前一 category 已经包含更前面 category 的累计结果，所以只需要继承上一 category。

## 第一次 Balance：按 WPH 比例分配

第一次 Balance 时，将 Lot 的 wafer qty 按该 Lot 所有可作业机台的 WPH 比例分配。

```text
Qty Assign(1, EQP)
= Lot Qty × WPH(EQP) / sum(该 Lot 所有可作业机台 WPH)
```

UPH / WPH 表示机台每小时能作业几片 Wafer。第一次按 WPH 比例分配后，再用 WPH / UPH 换算作业时间。

```text
Step WIP Time = Qty Assign / WPH
```

这样做的含义是：第一次 Balance 会先让同一 Lot 在各可作业机台上的初始作业时间尽量接近，再基于机台累计作业时间计算 Weight。

## category 内机台累计时间

同一 category 内，同一机台可能分配到多个 Lot，因此需要汇总：

```text
Current EQP WIP Time = sum(当前 category 内该机台所有 Step WIP Time)
```

再加上前一 category 继承来的机台累计时间：

```text
New EQP WIP Time = Pre EQP WIP Time + Current EQP WIP Time
```

其中：

```text
category 0 的 Pre EQP WIP Time = 0
category 6 的 Pre EQP WIP Time = category 0 的 New EQP WIP Time
category 12 的 Pre EQP WIP Time = category 6 的 New EQP WIP Time
category 24 的 Pre EQP WIP Time = category 12 的 New EQP WIP Time
```

## 权重计算

第一次 Balance 的权重：

```text
Weight(1) = 1 / New EQP WIP Time(1)
```

第二次及以后，每次权重都要乘以上一次权重：

```text
Weight(n) = (1 / New EQP WIP Time(n)) × Weight(n-1)
```

其中：

```text
n = 2、3、4、5
```

含义：

- 机台累计作业时间越长，`1 / New EQP WIP Time` 越小；
- 机台累计作业时间越短，`1 / New EQP WIP Time` 越大；
- 上一轮权重会继续影响下一轮分配。

## 第二次及以后：按上一轮权重分配

第二次 Balance 起，Lot wafer qty 按上一轮权重分配：

```text
Qty Assign(n)
= Lot Qty ×（Weight(n-1, 该机台) / sum(Weight(n-1, 该 Lot 所有可作业机台))）
```

分配完成后，重新计算：

```text
Step WIP Time
Current EQP WIP Time
New EQP WIP Time
Weight(n)
```

## 5 次 Balance 顺序

迭代单位是“全部 category 跑完一遍”，不是单个 category 内重复 5 次。

```text
第 1 次：category 0 → 6 → 12 → 24，第一次按 WPH 比例分配，计算 Weight(1)
第 2 次：category 0 → 6 → 12 → 24，按 Weight(1) 分配，计算 Weight(2)
第 3 次：category 0 → 6 → 12 → 24，按 Weight(2) 分配，计算 Weight(3)
第 4 次：category 0 → 6 → 12 → 24，按 Weight(3) 分配，计算 Weight(4)
第 5 次：category 0 → 6 → 12 → 24，按 Weight(4) 分配，计算 Weight(5)
```

其中：

```text
Weight(n) = (1 / New EQP WIP Time(n)) × Weight(n-1)
```

## 字段理解

| 字段 | 含义 |
| --- | --- |
| category | qsort 分层后的层级，固定为 0、6、12、24 |
| qsort | WaferBalance 中指 Existing qsort，即 Existing Lot 到计算站点的最大允许等待时间 |
| Lot | Lot 名称 |
| Qty | Lot wafer qty |
| Step | 作业 step |
| EQP | 可作业机台 |
| UPH / WPH | 机台每小时可作业 wafer 数 |
| Qty Assign | 分配到该机台的 wafer qty |
| Step WIP Time | 当前 Lot 分配量在该机台的作业时间 |
| EQP WIP Time | 该机台当前 category 内累计作业时间 |
| Pre EQP WIP Time | 前一 category 继承来的机台累计作业时间 |
| New EQP WIP Time | 继承后该机台新的累计作业时间 |
| Weight | 机台权重 |
| Qty Assign by Weight | 按上一轮权重重新分配后的 wafer qty |

## 最终放货判断

WaferBalance 只是 QZone 放货判断中的 loading / 产能平衡环节。

最终是否允许放货，还需要结合：

- queue sort；
- 机台 IdleLoss；
- 机台 PM 时间；
- 机台 Loading；
- Existing qsort / Qtime；
- QZone 下游产能；
- Safety Value / Exception 等特殊管控逻辑。

## 待补充

- capability 下“所有可作业机台”的取值范围；
- IdleLoss、PM 时间、Loading 与 WaferBalance 结果如何共同参与最终放货判断。

## 关联知识

- `Qsort.md`：Existing qsort / qsort category 的计算来源；WaferBalance 使用 Existing qsort。
- `WPHLoss.md`：进入 WaferBalance 前，机台 WPH 可能已按 chamber loss 修正。
- `PM_Control.md`：最终放货判断需结合机台 PM / 借机时间段。
