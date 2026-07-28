# PM Control / PM 提前回线判断

> 来源：`00.raw-materials/10.sources/images/PM_Control/PM管控1.jpg` ~ `PM管控4.jpg`、`Prefer考量PM管控1.jpg`、`Prefer考量PM管控2.jpg`、`STNPMTimeControl内容示例.jpg`。  
> 作用范围：QZone PM 管控、MFG Prefer / 断线对厂机台选择、PM delay report。

## 定位

PM Control 用于判断 Lot 在 QZone 或对厂选机台时，是否会因为目标机台 PM / 借机管控导致无法按时作业。

原逻辑主要比较：

```text
Lot Qsort > PM Start
```

问题是长 Loop 场景会过早管控，导致可按时回线的机台产能被浪费。现逻辑中，PM 管控判断的到站时间改用 CycleTime 累计，替代原逻辑的 Qsort 判断；同时引入 `PMQzoneControl`、PM Start / End 修正、PM buffer 等判断，使 PM 管控更接近 Lot 实际到站风险。

## 主要业务问题

- 长 Loop 中仅用 `Qsort` 与 `PM Start` 比较，可能提前管控过早。
- 对于可按时回线的 PM 机台，过早管控会损失瓶颈机台产能。
- PM 机台前后若存在 Merge 站点，子母批 / 同组 Lot 可能因部分 Lot 被管控而无法继续流通。
- 多台同类型机台同时 PM 时，PM delay report 对同一 Lot 的延期时长可能重复计算。
- MFG Prefer / 断线选对厂机台时若不考虑 PM，Lot 可能到对厂后无法作业或卡在 QZone。

## STNPMTimeControlInfo / STNPMTimeControl

PM 管控依赖 `STNPMTimeControlInfo` 或 UI `STNPMTimeControl` 中的机台 PM 信息。

截图中出现的字段包括：

- `MachineID_New`
- `PlanStartTime`
- `PlanEndTime`
- `PMFlag`
- `StdMonPM`
- `PirunStdTime`
- `PMQzoneControl`
- `ActualPMTimeDuration`
- `NewPMStartTime`
- `STNSTATE`
- `CreateTime`
- `UpdateTime`

UI `STNPMTimeControl` 维护项包括：

- `Machine`：管控站点机台信息，支持模糊匹配。
- `Min PM Time`：最小 PM 时长限定。
- `Max PM Time`：最大 PM 时长限定。
- `PM Start Ratio`：提前管控 StartTime 占 PM 时长的比例。
- `PM End Ratio`：管控 PM End 占 PM 时长的比例。
- `Mon Ratio`：管控 `Mon + Pirun` 时长的比例。
- `Time Control`：该条设定是否受时间范围限制。
- `Start Time`：设定生效起始时间。
- `End Time`：设定生效结束时间。

若 UI 中无匹配 PM time duration 设定，则从默认配置取得默认 Ratio。

## PM Start / PM End 修正

基础时长：

```text
PMTimeDuration = PlanEndTime - PlanStartTime
```

当 `PMQzoneControl = Y` 时：

```text
PMStartTime = PlanStartTime - PMTimeDuration × PMStartRatio
PMEndTime   = PlanEndTime + PMTimeDuration × PMEndRatio + (StdMonPM + PirunStdTime) × (1 + MonRatio)
```

当 `PMQzoneControl != Y` 时：

```text
PMStartTime = PlanStartTime
PMEndTime   = PlanEndTime + PirunStdTime + StdMonPM
```

截图中对厂场景出现过以当前时间为基准的写法，其中 `$End` 表示当前时间：

```text
PMStartTime = PlanStartTime - $End
PMEndTime   = PlanEndTime - $End
```

含义是将计划 PM Start / End 转换为“距离当前时间还剩多久”的相对时间，用于与 Lot 到站累计时间或 CycleTime 类指标比较。

## QZone 中的 PM 管控判断

开关打开时，Lot STN List 取得符合 `STNPMTimeControlInfo` 的 `MachineID_New`，并判断主机台 / 腔当前状态。

仅对可做业状态继续判断，例如：

- `e10state = Standby`
- `Productive`
- `Eqpstate IN (MON-R, BACKUP, TD_LOT, ENG_LOT, MON_ROU, RECYCLE)`

新逻辑按 PM / 借机场景分开考虑：

- 借机：考虑借机时间段。
- PM 且 `PMQzoneControl = Y`：考虑 PM 时间段及 PM 开始后的整体时长。

若 Lot 预计到达或作业窗口落入 PM / 借机管控区间，则：

```text
IsNewPMAutoControl = T
```

否则：

```text
IsNewPMAutoControl = F
```

## 到站时间：CycleTime 累计

2025/05/07 修订说明：PM 管控判断中，Lot 到站时间使用 CycleTime 累计，替代原逻辑中的 Qsort。

原则：

- Lot Fetch Step 时计算 Lot 到每一站的到达时间。
- Process 站点使用 CycleTime。
- 非 Process 站点使用 ProcessTime。
- 每站 CT / PT 逐站累加后，记为 `CumulatedCycleTimeToStep`。
- PM / 借机管控判断使用 `CumulatedCycleTimeToStep` 与 PM 控制区间比较。

因此，PM 管控中的“到站时间”不再按 Qsort 理解。

## Merge Lot / 子母批优化

PM 站点前后若存在 Merge 站点，可能出现同一分批 Lot 中部分 Lot 可流通、部分 Lot 被 PM 管控，最终造成 Merge 后无法流通和 Over 风险。

优化方向：

- QZone Lot 分支抱团结果中，先确认同子母批 Lot 在同一分支。
- 对存在 Future Merge 站点的多 Lot 作为同一 Group。
- 针对同 Group 的 Lot 判断先后顺序。
- 若同 Group 中任一 Lot 受 PM 影响不可作业，其余 Lot 也需同步判断，避免后续 Merge 卡住。

## PM delay report 优化

当同类型多机台同时 PM 时，同一 Lot 在同一站点可能在多个延期机台上被重复计算延期时长。

优化原则：

- 对需要延期判断的机台，计算延期时长时排除已计算过的同站点 Over Lot。
- 同一 Lot / 同一站点 / 多机台 Over 时，避免重复累计 PM delay。

## MFG Prefer / 断线对厂 PM 判断

MFG Prefer / DownTime 场景在检查对厂可作业机台时，也要考虑 PM 管控。

原因：

- Lot 被选到对厂后，可能因对厂机台 PM 无法作业。
- Lot 可能在对厂后被 QZone 卡控。

新增判断位置：

- `MFGPrefer`
- 断线场景的 `TargetFabCondition`

关键步骤：

1. Lot Fetch Step 时计算 Lot 到每一站的 `ArriveTime`，记为 `CumulatedCycleTimeToStep`。
2. 获取对厂机台信息。
3. 按 `Machine` / `MainTool` 获取 `PreControlFlag`。
4. 从 `PreControlException` 获取例外设定。
5. 获取 `STNPMTimeControlInfo` 中的 PM / 借机时间。
6. 判断 `CumulatedCycleTimeToStep` 是否落入 PM / 借机区间。

若机台处于 PM 管控区间：

```text
IsNewPMAutoControlSTN = T
```

若 Machine 和 MainTool 任一存在 `IsNewPMAutoControlSTN = T`，则认为该 Machine 不可作业。

TargetFabCondition 中：

```text
若 IsPreControlException != T
且 (PreControlFlag = T 或 (PreControlFlag != T 且 IsNewPMAutoControlSTN = T))
则机台不可作业，剔除机台；
反之保留。
```

## 风险点

- PM 管控到站时间使用 CycleTime 累计，不应再套用原 Qsort 判断口径。
- `PMQzoneControl = Y` 时必须修正 PM Start / End。
- PM / 借机处理方式不同，不应套同一公式。
- Machine 与 MainTool 都要判断，不能只判断腔或只判断主机台。
- Merge Lot 需按 Group 联动判断，避免单 Lot 判断通过但 Merge 后卡住。
- Delay report 需避免同 Lot 同站点多机台重复计时。

## 待确认

- `STNPMTimeControlInfo` 与 UI `STNPMTimeControl` 的字段映射。
- `PreControlException` 的完整字段和优先级。
