# Case_STNLoadingBalance_v0.1

> 状态：工作中案例。来源于 STNLoadingBalance 需求单优化过程。

## 背景

当前 LoadingBalance 以 SelfCapability 作为均衡对象，无法充分体现同一机台组内不同机台的实际负荷差异。

## 为什么改

不同产品 / Lot 的 release 机台、可作业机台、跨厂条件、PM 状态、QZone 管控等存在差异，导致机台组维度 Loading 与真实机台负荷存在偏差。

## 原逻辑

- 以 SelfCapability 维度计算 Loading。
- 机台组来源为 WIP 可作业机台并集。

## 新逻辑

- 改为机台维度计算 Loading。
- 按 Timeline 层级执行 WaferBalance。
- 分别计算：
  - FAB6 / FAB8 单厂 `WIPLoading`
  - 两厂 `WIPLoading_avg`
  - FAB6 / FAB8 Priority `PriorityWIPLoading`
  - 两厂 `PriorityWIPLoading_avg`

## 容易遗漏

- Priority Loading 不是从全量 Loading 按比例拆分，而是筛选 `isprioritylot = T` 后单独执行 WaferBalance。
- WaferBalance 第一次 Balance 应按可作业机台 WPH 比例分配 Lot Qty，不是平分。
- `EqpLoadingSummary` 需要明确唯一维度。
- PM 时间是否重复累计必须明确。
- WPHLoss 若沿用旧逻辑，需写清楚“沿用”。
- Timeline 层级 `0、2、6、12、24` 需确认是否固定。

## Review 重点

- Report 字段含义。
- 单厂 vs 两厂平均逻辑边界。
- Priority 单独计算边界。
- PM_RemainTime 累计方式。
- WPH 缺失处理。

## 可复用经验

复杂 Loading 类需求应先明确：

```text
输入 Lot 范围
输入机台范围
计算层级
继承关系
输出唯一维度
空值 / 缺失值处理
```
