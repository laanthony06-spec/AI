# NPW 自动化

> 来源：自动派工系统培训 PPT，`00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p050.jpg` ~ `PPT90.jpg`。

## NPW 类型

PPT 中 NPW 类型包括：

- Monitor
- Season
- Dummy

## 功能模块

NPW 自动化按流程可分为：

- 备片 / AutoInUseStart
- 派工 / Dispatch
- Recycle / AutoInUseEnd
- Downgrade / AutoRecycleEnd

## Monitor

Routine monitor 的主要流程包括：

1. 准备 Monitor；
2. 监测前值；
3. 主机台；
4. 测量后值。

分批逻辑示例：

- By time 分批：`split time = date(last monitor time) + interval + time(initial time) - leading time`
- By time weekly 分批：`split time = date(now) + time(initial time) - leading time`

常见参数：

- interval
- remain CT
- remain due
- monitor urgency
- leading time

## Season

Season In Use Start 的主要流程：

1. 机台派工；
2. Season 判断；
3. Season 准备；
4. 主机台。

触发条件包括：

- 机台触发派工；
- 机台 idle 时间达到设定值；
- 机台本次作业产品条件与上次作业产品条件发生改变；
- 机台作业前有换线等。

Season 类型包括：

- Idle season
- Recipe change season
- Recipe idle season
- Chemical season
- PM&DOWN season

## Dummy

Dummy 类型包括：

- Furnace Dummy
  - SD Dummy
  - ED Dummy
- ETCH Dummy
  - Inside Dummy
  - Outside Dummy

Dummy In Use Start 触发条件示例：

- 机台内在 dummy 达到最大使用次数，或当前控派工机台内 dummy 不足；
- 当前无分批的 dummy。

## In Use End

In Use End 用于处理可 reuse / recycle 的 lot 信息。

主要流程包括：

1. Watchdog 每 5 分钟扫描一次；
2. 获取 InUseEnd 站点可作业 lot 列表；
3. 判断是否有可作业 lot；
4. 判断是否可以做 reuse；
5. 判断是否可以做 recycle；
6. 成功或失败后结束 / 告警。

## Reuse

Reuse 条件中出现的字段 / 条件包括：

- Lot_ProcessingStatus = Active
- Lot_Extrastatus = WaitForInUseEnd
- Switch_InUseEnd = T
- Wafer UsedCount < Max UsedCount
- Wafer Monitor status = Available
- Control status = Used
- Carrier_CarrierKind = FOUP
- FOUP Location = InStocker or In OHB

## Recycle

Recycle 条件中出现的字段 / 条件包括：

- Lot_ProcessingStatus = Active
- Lot_Extrastatus = WaitForInUseEnd or WaitForInUseStart
- Switch_InUseEnd = T
- Wafer UsedCount >= Max UsedCount
- Wafer RecycleCount < MaxRecycleCount
- InUseStart Lot Qty < Setting Qty
- Carrier_CarrierKind = FOUP
- FOUP Location = InStocker or In OHB

## Downgrade / Reassign

Downgrade / Reassign 相关条件中出现：

- Switch_RecycleEnd = T
- Switch_Reassign = T
- FabMaintainDownGrade
- Reassign Mapping
- Carrier_CarrierKind = FOUP
- FOUP Location = InStocker or In OHB

## Auto Handle Fail

Auto Handle Fail 用于处理前置 Fail 场景。PPT 中提到：

- 前置 Fail Lot 会自动 Hold 给对应 PE；
- AMA 自动检索前置 Fail Lot 并进行 Release / Cancel control ID 等动作；
- 相关 UI：MonitorAutoInuse_Auto Handle Fail。

