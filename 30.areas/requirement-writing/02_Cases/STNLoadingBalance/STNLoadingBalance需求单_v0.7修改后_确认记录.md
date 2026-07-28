# STNLoadingBalance v0.7 修改后确认记录

> 用途：记录用户对需求单阅读阶段提出的口径确认，后续优化正式需求单时以本文件为准。

## 2026-06-28 确认

### 1. Timeline 层级

当前 STNLoadingBalance 使用以下五个 Timeline 层级：

```text
0、2、6、12、24
```

但需求应表达为“层级可配置 / 可扩展”，不能写成永久固定只有五层。

后续可能增加到：

```text
6 个层级 / 8 个层级 / 更多层级
```

正式需求单建议表达：

```text
系统按配置的 Timeline 层级执行 Loading 计算。当前配置层级为 0、2、6、12、24；后续若配置新增层级，计算逻辑需按配置层级自动扩展。
```

### 2. 正式输出字段名

正式需求单统一使用以下字段名：

```text
WIPLoading_Avg
PriorWIPLoading
PriorWIPloading_Avg
```

不再混用以下写法：

```text
WIPLoading_avg
PriorityWIPLoading
PriorityWIPLoading_avg
PriorWIPLoading_Avg
```

后续优化需求单时，应统一替换为正式字段名。

## 2026-06-29 确认

### 3. PM_RemainTime 含义

`PM_RemainTime` 的实际含义：

```text
Lot 到站前，机台因 PM / 借机不能提供作业的时长。
```

因此，同一机台、同一 PM 计划、同一 Timeline 层级下：

```text
PM_RemainTime 相同
```

正式需求单中不应描述为“每个 Lot / 每次 Balance 重复累加”。建议表达为：

```text
Balance 计算机台累计作业时间时，需纳入该机台在当前 Timeline 层级下的 PM_RemainTime。
PM_RemainTime 表示 Lot 到站前该机台因 PM / 借机无法提供作业的时长。
同一机台、同一 PM 计划、同一 Timeline 层级下 PM_RemainTime 相同。
```

### 4. Priority Loading 无数据时输出

当某厂 / 某 SelfCapabilityGroup_STN / 某 Timeline 层级下不存在 `isprioritylot = T` 的 Lot 时：

```text
PriorWIPLoading = 0
```

当两厂合并视角下某 SelfCapabilityGroup_STN / 某 Timeline 层级不存在 `isprioritylot = T` 的 Lot 时：

```text
PriorWIPloading_Avg = 0
```

正式需求单中不再保留“0 或空值【待确认】”。

### 5. EqpLotSummary 字段含义

| 字段 | 含义 |
| --- | --- |
| `PiecesPreStation` | Lot 分配到该机台的片数 |
| `LoadingPreStation` | 机台作业 Lot 分配到该机台片数所需的时间，等于 `PiecesPreStation / UPH` |
| `LotAttInfoSite` | Lot 当前所在厂 |
| `CurrentInfoSite` | Lot 在这一站要在哪一个厂作业，即实际作业厂 |
| `EqpSite` | 机台所在厂 |
