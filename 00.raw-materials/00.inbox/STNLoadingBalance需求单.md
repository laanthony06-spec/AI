

## STNLoadingBalance

### 首页基础信息

标题：新增需求申请单

编号：______（此处由信息技术部填写）

类别（请在方框内打勾）：

- □1. 软件采购
- □2. 硬件采购
- ☑3. 功能开发
- □4. 工程及服务

申请部门：制造部

系统名称（类别为 3 时必填）：CIM 计算机集成制造系统 Fab6（二科）

申请人员：温浩奇

功能模块（类别为 3 时必填）：智能派工系统（RTD/DSP）

申请日期：2026-05-19

希望交付期：2026-xx-xx

### 项目简介和必要性分析

当前 LoadingBalance 功能以整个机台组（SelfCapability）作为 Loading 均衡对象，机台组量取方式为 WIP 可作业机台并集。实际生产中因各产品 release 机台情况不同，导致部分机台组 Loading 计算结果与实际相差较大，因此需对 Loading 功能进行优化，改为机台维度的 loading 计算，实现每个机台的负载均衡。

### 项目投资方案比较及效果分析

改善方案：

细化到机台维度计算 Loading，实现每个机台的负载均衡。

效果分析：

优化 LoadingBalance，更加符合跨厂 WIP 之间的 Balance 需求。

### 需求内容（可添加附件）

## 一、STN 维度 Loading 计算及 Report 输出修改

原 LoadingBalance 按 SelfCapability 维度计算 Loading。本次修改后，Loading 需改为按 STN 维度计算。

### 1. Report 输出字段

#### 1.1 EqpLoadingSummarybyEqp 输出字段

EqpLoadingSummarybyEqp 用于保存机台维度 Loading 结果。

| 字段 | 含义 |
| --- | --- |
| EqpSite | 机台厂别 |
| SelfCapabilityGroup | 机台所属 SelfCapabilityGroup |
| STN | 机台名称 |
| Timeline | 到站点 Qtimelimit 累加值 |
| WIPLoading | 机台单厂 Loading |
| WIPLoading_Avg | 机台两厂平均 Loading |
| PriorWIPLoading | 仅 PriorityLot 的机台单厂 Loading |
| PriorWIPLoading_Avg | 仅 PriorityLot 的机台两厂平均 Loading |
| CreateTime | Job 开始时间 |

#### 1.2 EqpLotSummarybyEqp 输出字段

EqpLotSummarybyEqp 用于输出 Lot 与机台 Loading 分配关系的计算结果。

| 字段 | 含义 |
| --- | --- |
| Lot | Lot 名称 |
| CurStep_FullSeq | Lot 当前站点 StepSeq |
| Full_StepSeq | 每一站的 StepSeq |
| Timeline | 到站点 Qtimelimit 累加值 |
| SelfCapabilityGroup | 站点所属 SelfCapabilityGroup |
| STN | 机台名称 |
| Pieces | Lot 片数 |
| IsPriorityLot | 是否为 Important Lot |
| LotAttInfoSite | 当前所在厂别 |
| CurrentInfoSite | 该站点实际作业厂别 |
| EqpSite | 机台厂别 |
| PiecesPreStation | Lot 分配到机台的片数 |
| UPH | 机台每小时作业片数 |
| LoadingPreStation | 机台作业 Lot 分配片数所需时间 |
| CreateTime | Job 开始时间 |

### 2. WIP 与基础参数准备

#### 2.1 WIP 获取逻辑

##### 2.1.1 基础数据来源

从 FAB6 / FAB8 获取 Lot 以及基础信息。

| 数据来源                                        | 主要用途                                                             |
| ------------------------------------------- | ---------------------------------------------------------------- |
| fwlot                                       | 获取 Lot、prodname、planname、priority、internal_priority、pieces 等基础信息 |
| fablotext                                   | 获取 Capability、status、extrastatus、LotAttInfoSite 等信息              |
| fwripstep                                   | 获取 Stepseq、Stage 等站点信息                                           |
| fabproductext / fabcategorymap              | 获取 Producttype 等信息                                               |
| tb_product_list                             | 获取 tech 等信息                                                      |
| fablotcarrierext                            | 获取 carrierkind、carrierstate 等信息                                  |
| fabeapseasonprocess                         | 获取 controlid 信息，记为 seasoncontrolid                               |
| fabeapmonitorprocess                        | 获取 controlid 信息，记为 monitorcontrolid                              |
| fabeapmonitorgroup / fabeapmonitorgroup_N2M | 获取 toid 信息                                                       |
| FabeapTRCGroupitem / FabeapTRCGroup         | 获取 groupid 信息                                                    |
| FabEapDummyLotProcess                       | 获取 dummyid 信息                                                    |
| RTDConfig-Global-N2OInternalPriority        | 获取 N2O internalpriority 配置                                       |

#### 2.1.2 Producttype 修正

当 Lot 在 fwproductext 中的 Producttype 为 Production 或 Engineer 时，优先使用fabcategorymap 中的 Producttype。

若 Engineer Lot 的 Internalpriority 满足 N2O internalpriority 配置，则视为 Production Lot。

#### 2.1.3 Season / Monitor / Dummy Flag 判断

Season Flag：

当 Lot 的 toid 或 groupid 有值时，seasonflag = T，否则为 F。

Monitor Flag：

当 lot Null(Capability) and Full(monitorcontrolid) 时，monitorflag = T，否则为 F。

Dummy Flag：

当 lot Full(dummyid) 时，dummyflag = T，否则为 F。

#### 2.1.4 WIP 筛选条件

选满足以下条件的 WIP：

```text
(
  priority < 8
  and processingstatus = Active
)
or
(
  priority < 5
  and processingstatus = CrossFabTransferred
)
and carrierkind = FOUP
and !(Full(dummyflag) or Full(seasonflag))
```

#### 2.1.5 WIP 去重处理

筛选 FAB6 / FAB8 Lot 后，通过 Macro:GetCrossFabLotList 判断 Lot 是否为 Transfer Lot 以及 CurrentInfoSite。

筛选满足以下条件的 lot：

```text
(!IsTransferlot and LotStatus != CrossFabTransferred)
or IsTransferlot
```

### 2.2 Important Lot 识别逻辑

#### 2.2.1 数据获取

从 `quota_applyinfo` 获取 `lotid`、`Keylot`、`dept`、`targetstepsequence`、`Status` 信息。

从 `tb_special_targetlot` 获取 `lotid`、`TargetStepseq` 信息。

#### 2.2.2 Key Lot / Target Lot 判断

Keylot：

```text
Lotname = lotid
且 KeyLot = 1
且 Status = CONFIRM
```

Targetlot：

```text
Lot = lotid
且 FullStepSeq <= TargetStepseq
或
(
  Lot = lotid
  且 dept != support
  且 FullStepSeq <= TargetStepsequence
  且 Status = CONFIRM
)

```


#### 2.2.3 Important Lot 判断（Isprioritylot）

从配置文件获取：

- keylot
- Targetlot
- ProductionType
- ProdName
- Tech
- LotType
- Recipe
- Priority
- InternalPriority
- MPCPriority

匹配上配置的 lot 即为 Importantlot，Isprioritylot 指标生效为 T。

### 2.3 Lot 站点与机台信息获取

#### 2.3.1 NPW / PW 站点获取范围

| Lot 类型 | 判断条件 | 站点获取范围 |
| --- | --- | --- |
| NPW Lot | !(category = Production or category = Engineer) | 当前站点 |
| PW Lot | category = Production or category = Engineer | 后续 50 站，50 为可设定参数 |

后续判断中 PW Lot 需额外去除等级为 5-9 的 Lot：

```text
!(priority = 5 and internalpriority = 9)
```

#### 2.3.2 NPW Lot 站点信息

NPW Lot 从 `npwepr`、`fablotext`、`FabeqpCapability` 得到：

- CurStepSeq
- FullStepSeq
- StepIndex
- capability
- recipe
- stage
- product
- Pieces
- STN
- LotAttInfoSite
- CurrentInfoSite
- EqpSite

##### （1）主机台 / 前置机台修正

从表 `FabEapMonitorProcess` by Lot 和 controlid 获取：

- eqpname
- state

从表 `FabEQPMonitorid` by Controlid 获取主机台 `stepseq`。

从表 `FabEqpMonitorProcessN2M` 获取前置机台 `PreStn`。

判断逻辑：

a. 若 `state = inuse` 且 lot `CurStepSeq = stepseq`，机台替换为 `eqpname`。

b. 若 `state != inuse`，保留 Capability 获取的机台。

c. 若 `state = inuse` 且 lot `CurStepSeq != stepseq`，机台替换为 `PreStn`。

##### （2）Specialization 指定机台修正

从 `FabFutureAction` 获取 Lot 的 Specialization 指定机台信息。

若存在 Specialization 指定机台，使用指定机台；否则保留 eqpname 主机台 / 前置机台 / Capability 判断后的机台。

#### 2.3.3 PW Lot 站点信息

PW Lot 经 `TransferlotFetchMacro Fetch` 后续 50 站，并获取：

- CurStepSeq
- FullStepSeq
- StepIndex
- product
- stage
- recipe
- capability
- Stn
- ArriveTime（CT 累加）
- LotAttInfoSite
- CurrentInfoSite
- EqpSite

需考量 Specialization 指定机台逻辑。

另若 Lot 为 `isTransferlot`，需修正站点厂别信息。

### 2.4 SelfCapabilityGroup 获取

首先 by product 从表 `tb_product_list` 中获取 Lot 所属的 tech。
再根据 lot 各站点的：
- capability
- stage
- product
- recipe
- tech

从表 `tb_selfcapa_rule` 中获取 SelfCapability 信息。

最后 by SelfCapability 从 `SelfCapabilityGroupLimit` 得到 lot 各站点的 SelfCapabilityGroup。

### 3. 站点筛选与可作业机台判断

#### 3.1 安全站点判断逻辑

获取 Lot 安全站点，仅保留从当前站点到第一个安全站点之间的站点，包含当前站点和安全站点。

安全站点包括：

1. SafetyValue 安全站点
2. APM 自定义安全站点

##### 3.1.1 SafetyValue 安全站点

满足以下任一条件，视为安全站点：

```text
3 <= safety value
or qtime type 均为 start
or qtime type 为空
```

##### 3.1.2 自定义安全站点

设定值获取：

```text
RTDConfig-Global-APMSafetyValue
```

满足以下任一条件，视为自定义安全站点：

条件一：

```text
safety value = 设定值
and 存在 qtimetype = End（只看 MAX qtime）
and 必须存在 qtime type = START
and 所有 END qtime 对应的 Min(qlimit) >= 设定时间
```

条件二：

```text
safety value = 设定值
and Qtimetype 全为空
```

条件三：

```text
safety value = 设定值
and Qtimetype 全为 Start
```

#### 3.2 QZone 与 Loop Lot Control 判断

Lot 经 QZone Control 与 Loop Lot Control 判断后，按以下规则筛选站点。

##### 3.2.1 QZone Control

若 Lot 在某站点卡控 QZone Control，则筛除该站点及其之后的所有站点。（保留 issue 站点）

##### 3.2.2 Loop Lot Control

若 Lot 在某站点卡控 Loop Lot Control，则筛除该站点及其之后的所有站点。（保留结束站点）

#### 3.3 可作业机台判断

##### 3.3.1 YE Skip 判断

从表 `FabSsnfcSkip` 获取配置：

- baselineSubid
- eqpCapability
- planid
- productid
- scanLotid
- stageid
- stepseq
- skipLotid

匹配规则：

- 若 lot 信息匹配上 scanLotid，则 `ScanFlag = T`，否则为 F。
- 若 lot 信息匹配上 skipLotid，则 `SkipFlag = T`，否则为 F。
- 若 lot 最后一位匹配 baselineSubid，则 `baselineFlag = T`，否则为 F。

跳站判断：

```text
lot 满足
(
  ScanFlag = F
  and SkipFlag = T
)
or
(
  ScanFlag = F
  and SkipFlag = F
  and baselineFlag = T
)
时，认为 Lot 在该站点可 skip，去除 Skip 站点。
```

##### 3.3.2 RC / 非 RC 对厂机台获取

若 FullStepseq 包含 RC，则：
通过 `FabRunCard`、`FabRCDstepinfo` 获取 RC 指定机台。

通过 `FabeqpCapability` by Capability 获取 Lot 在对厂站点的机台。

若存在 RC 指定机台，使用 RC 指定机台；否则使用 Capability 获取的机台。

当 FullStepseq 不包含 RC：

通过 `FabFutureAction` 获取 Specialization 指定机台。

通过 `FabeqpCapability` 获取 Lot 在对厂站点的机台。

若存在 Specialization 指定机台，则使用 Specialization 指定机台；否则使用 Capability 获取的机台。

##### 3.3.3 可作业条件判断

将 lot 在本厂和对厂机台经过：

- LCC
- PCC
- MCC
- T2T
- DOMA
- MES Pirun
- CFK

逻辑判断，得到两厂的 `AvailableStnChamberList`。

注：若存在单厂 LCC 结果，直接使用单厂 LCC 结果；否则走 ParaLCC 逻辑。

### 4. Timeline / PM / WPH 参数获取

#### 4.1 Timeline 获取

##### 4.1.1 数据来源

从 `restructedQtime` 获取：

- part
- part_revision
- route
- route_revision
- gatestepbeginsequence
- c_gateendsequence
- c_queuelimithours_nopt

信息。

根据 Lot 的：

- product
- productrevision
- plan
- planversion

串取相应的：

- gatestepbeginsequence
- c_gateendsequence
- c_queuelimithours_nopt

##### 4.1.2 Timeline 计算逻辑

根据 Lot 的 CurIndex 与各站点 FullStepIndex，得到 Lot 到每一站的 Timeline。

满足以下条件时，取对应 `c_queuelimithours_nopt` 作为 Lot 在该站点的 Timeline：

```text
CurIndex > gatestepbeginsequence
or
(
  CurIndex = gatestepbeginsequence
  and extrastatus != Wait For Job Prep
)
and FullStepIndex <= c_gateendsequence
```

若 Lot 在该站点满足：

```text
Fullstepseq = CurStepseq
```

则该站点 Timeline 取 0，否则取原 Timeline。

#### 4.2 PM 管控判断

Follow Qzone PM 管控判断，用 ArriveTime（CT 累加）判断 Lot 是否落入管控区间。

##### 4.2.2 PM 时间区间

从 `STNPMTimeControlInfo` 获取机台 PM / 借机相关信息，包括：

- MachineID_New
- PlanStartTime
- PlanEndTime
- PMFlag
- StdMonPM
- PirunStdTime
- PMQzoneControl
- ActualPMTimeDuration

当 `PMQzoneControl = Y` 时，PM Start / End 需按既有逻辑修正：

```text
PMTimeDuration = PlanEndTime - PlanStartTime
PMStartTime = PlanStartTime - PMTimeDuration * PMStartRatio
PMEndTime = PlanEndTime + PMTimeDuration * PMEndRatio + (StdMonPM + PirunStdTime) * (1 + MonRatio)
```

使用相对当前时间判断，`$End` 表示当前时间：

```text
PMStartTime = PlanStartTime - $End
PMEndTime = PlanEndTime - $End
```

##### 4.2.3 机台保留判断

根据 Lot ArriveTime 与 PM / 借机管控区间判断机台是否可参与该 Lot 作业。

判断逻辑：

1. 借机场景按借机时间段判断。
2. PM 场景按修正后的 PMStartTime / PMEndTime 判断。
3. Machine / MainTool 均需判断，任一满足 PM 管控，则认为机台受 PM 管控影响。

受 PM 管控的机台认为不可作业。

##### 4.2.4 PM_RemainTime 判断

`PM_RemainTime`：Lot 到站前，机台因 PM / 借机不能提供作业的时长。

若机台当前状态为 PM / MON_PM，则该机台所有 lot 都需考量 `PM_RemainTime`，且：

```text
PM_RemainTime = PlanEndTime - $End
```

若机台当前状态不为 PM / MON_PM，则根据机台的 PlanStartTime 判断 lot 是否考量 `PM_RemainTime`。

```text
ArriveTime > PlanStartTime - $End
```

的 lot 需考量 `PM_RemainTime`，且：

```text
PM_RemainTime = PlanEndTime - PlanStartTime
```

后续 Balance 计算机台累计作业时间时，需考量 `PM_RemainTime`。

#### 4.3 WPH 获取

根据机台厂别，从 `vw_dsp_capabilitywph` 中按以下优先级获取 Lot 在各站点机台的 WPH：

1. capability + recipe + productname
2. capability + recipe
3. capability + productname
4. capability

##### 4.3.1 WPHLoss 考量

参考原 WPHLoss 逻辑，Loading 计算使用 WPH 时使用 WPHLoss 修正结果。

原逻辑框架如下：

按 Lot、stepseq、EQPID 分组判断是否需要计算 WPHLoss。

同组内可作业 STN 具备相同且非空的 ProcessGroup，且 `WPHLossControl = Y` 时，计算 WPHLoss；否则沿用原 WPH。

对需要计算 WPHLoss 的 Lot，拆分并去重 chamberflow，得到该 Lot 在该机台可用 chamber list。

By Capability、ProcessGroup、Machine、SubeqpStateGroup、Count 从表 `tb_dsp_wphloss` 匹配 WPHLoss；未匹配到时，WPHLoss = 0。

同一机台涉及多个 SubeqpStateGroup 时，最终 WPHLoss 取各分组 Loss 的最大值。

WPH 计算公式：

```text
Actual STN WPH = Total STN WPH × (1 - WPHLoss)
```

#### 4.4 MFGControl 判断

Lot 在两厂的可作业机台需经过 MFGControl Macro 判断（不考虑 WaittingTime、Remain 等动态变化）。

### 5. STN 维度 Loading 计算

#### 5.1 机台单厂 Loading 计算

##### 5.1.1 计算范围

单厂 Loading 计算时：

- `Currentinfosite` 为 FAB6 的 Lot，只获取 FAB6 可作业机台。
- `Currentinfosite` 为 FAB8 的 Lot，只获取 FAB8 可作业机台。
- 单厂 Loading 只反映各厂自身可作业机台的 loading 情况。

##### 5.1.2 Timeline 层级

Lot 按 Timeline 层级进行 Loading 计算。

当前层级为：

```text
0, 6, 12, 24
```

视计算情况可调整。

##### 5.1.3 单厂 WaferBalance 计算

获取单厂所有 Lot，并按 Timeline 层级划分后，使用 WaferBalance 方法计算机台 Loading。

每一层级 Balance 时，需考虑：

1. 上一层级机台已累计的需求作业时间。
2. 机台因 PM / 借机无法提供作业能力的时间，即 `PM_RemainTime`。

##### 5.1.4 WaferBalance 基础逻辑

WaferBalance 计算逻辑如下：

1. Step WIP Time

首先 lot 按可作业机台 WPH 比例分配 Lot Qty。得到每个机台的：

```text
Step WIP Time = Qty Assign / WPH
```

2. New EQP WIP Time

累计机台分配到的 Step WIP Time 以及 Pre EQP WIP Time 和 PM_RemainTime 得到 New EQP WIP Time。

3. 权重计算：

```text
Weight(n) = Weight(n-1) / New EQP WIP Time(n)
```

4. 全部 Time 层级计算一遍后，进入下一次 Balance，共 Balance 5 次。

##### 5.1.5 Loading 计算结果

计算 lot 分配到每个可作业机台的作业时间后，by STN、Timeline 累加所有 lot 分配到机台的作业时间，最终 STN 在每个 Timeline 的 loading 为小于等于该 Timeline 的 loading 之和。

##### 5.1.6 Priority 单厂 Loading 计算

筛选 `isprioritylot = T` 的 Lot，额外单独执行一次 WaferBalance，计算 Priority Lot 维度单厂 Loading。

计算方法与单厂 Loading 一致。

#### 5.2 机台平均 Loading 计算

##### 5.2.1 计算范围

平均 Loading 计算时：

- Lot 使用 FAB6 及 FAB8 两厂可作业机台。
- 即两厂 Lot 与两厂可作业机台一起参与 WaferBalance，得到两厂的平均 Loading。

##### 5.2.2 计算方法

平均 Loading 与单厂 Loading 使用相同 WaferBalance 方法，区别仅在于 Lot 与可作业机台范围。
##### 5.2.3 Priority 平均 Loading 计算

筛选两厂 `isprioritylot = T` 的 Lot，额外单独执行一次两厂的 WaferBalance，得到 `PriorWIPLoading_Avg`。

计算范围：

- Lot 范围：FAB6 和 FAB8 中 `isprioritylot = T` 的 Lot
- 机台范围：FAB6 和 FAB8 两厂可作业机台

计算方法与平均 Loading 一致，仅使用 Priority Lot 参与计算。

### 6. Loading 输出结果汇总

| 计算类型                 | Lot 范围                  | 可作业机台范围           | 输出结果                |
| -------------------- | ----------------------- | ----------------- | ------------------- |
| FAB 单厂 Loading       | FAB6 Lot                | FAB6 可作业机台        | WIPLoading          |
| FAB 单厂 Loading       | FAB8 Lot                | FAB8 可作业机台        | WIPLoading          |
| 平均 Loading           | FAB6 + FAB8 Lot         | FAB6 + FAB8 可作业机台 | WIPLoading_Avg      |
| FAB6 PriorityLoading | FAB6 prioritylot        | FAB6 可作业机台        | PriorWIPLoading     |
| FAB8 PriorityLoading | FAB8 prioritylot        | FAB8 可作业机台        | PriorWIPLoading     |
| Priority 平均 Loading  | FAB6 + FAB8 prioritylot | FAB6 + FAB8 可作业机台 | PriorWIPLoading_Avg |

## 二、LoadingCandidateLot 修改

LoadingCandidateLot 根据 STN 维度 Loading 结果，判断低 Loading 机台，并从对厂选择可转移到该低 Loading 机台作业的 Lot。

### 1. Candidate Lot WIP 获取与 Transfer 标识

WIP 获取范围与第一部分 Loading 计算范围保持一致。由于后续会串取 `EqpLotSummarybyEqp` 判断 Lot 与机台 Loading 分配关系，可不重复执行站点筛除相关逻辑。

需额外进行以下判断：

1. 通过 `TransferCondition` 检查 Lot 是否可 Transfer。
2. 通过 `TargetFabCondition` 检查 Lot 是否符合目标厂别要求。
3. 若 Lot 可 Transfer，则标记：

```text
IsTransferCandidate = TRUE
```

同时获取：

- Lot 在对厂的可作业机台
- `SelfCapabilityGroupLimit` 中对应 `SelfCapabilityGroup` 的 `TransferLotCountLimit`
- `Transferlotsortingitem` 中对应 `SelfCapabilityGroup` 的排序指标，并记为 `RTDRank`

---

### 2. ReceiveLoading STN 判断

本节用于根据 `EqpLoadingSummarybyEqp` 的 STN 维度 Loading 结果，结合 UI 配置判断哪些 STN 可接收对厂 Lot。

#### 2.1 配置与 Loading 数据来源

从 UI：`LoadingSettingINFO` 获取以下配置：

- SelfCapabilityGroup
- QTLimit
- TransferType
- LotAttribute
- LoadingGap
- FAB_LoadingSpec
- FromSite
- TargetSite

从 `EqpLoadingSummarybyEqp` 获取 STN 维度 Loading 结果：

- Site
- SelfCapabilityGroup
- STN
- Timeline
- WIPLoading
- WIPLoading_Avg
- PriorWIPLoading
- PriorWIPLoading_Avg

#### 2.2 按 Timeline 匹配 Loading 配置

每笔 `STN + Timeline` 记录，需先按 `SelfCapabilityGroup` 找到对应 Loading 配置。若同一 Timeline 可匹配到多笔 QTLimit 配置，则保留最接近当前 Timeline 的一笔。

`EqpLoadingSummarybyEqp` 中每笔 `STN + Timeline` 记录，先通过 `SelfCapabilityGroup` 匹配 `LoadingSettingINFO` 中满足以下条件的配置：

```
Timeline <= QTLimit
```

若同一 `STN + Timeline + SelfCapabilityGroup` 匹配到多笔 `QTLimit` 配置，则取满足条件下 `QTLimit` 最小的一笔配置。

若同一 STN 同时归属多个 `SelfCapabilityGroup`，则每个 `SelfCapabilityGroup` 分别执行上述匹配逻辑，并各保留一笔配置。

#### 2.3 低 Loading STN 判断

匹配配置后，按 `LotAttribute` 区分普通 Loading 与 Priority Loading，分别判断 STN 是否低于配置水位。

每笔 `STN + Timeline` 按已匹配到的配置判断是否为低 Loading 机台。

当 `LotAttribute = Normal` 时，满足以下任一条件，则该 STN 视为 `ReceiveLoading`：

```
Full(LoadingGap)
AND WIPLoading <= MAX(0, WIPLoading_Avg - LoadingGap)
```

或

```
Full(FAB_LoadingSpec)
AND WIPLoading <= FAB_LoadingSpec
```

当 `LotAttribute = Important` 时，满足以下任一条件，则该 STN 视为 `ReceiveLoading`：

```
Full(LoadingGap)
AND PriorWIPLoading <= MAX(0, PriorWIPLoading_Avg - LoadingGap)
```

或

```
Full(FAB_LoadingSpec)
AND PriorWIPLoading <= FAB_LoadingSpec
```

若同一 `STN + Timeline + LotAttribute` 下，不同 `SelfCapabilityGroup` 配置均判断为低 Loading，则仅保留水位最小的一笔配置，供后续接收量计算使用。

水位取值如下：

- 使用 `LoadingGap` 判断时：
  - Normal：`WIPLoading_Avg - LoadingGap`
  - Important：`PriorWIPLoading_Avg - LoadingGap`
- 使用 `FAB_LoadingSpec` 判断时，水位为 `FAB_LoadingSpec`。

#### 2.4 T_BUFFER / T_BUFFER_Pri 接收量计算

接收量用于表示低 Loading STN 在当前 Timeline 下还能接收多少 WIP。`LoadingGap` 场景下，水位只用于判断是否低 Loading，接收量仍按平均 Loading 计算。

对判断为 `ReceiveLoading` 的 STN，取该 STN 最大的低 Loading Timeline，并计算该 Timeline 下各 Timeline 需要接收的 WIP 量。

当 `LotAttribute = Normal` 时，计算 `T_BUFFER`：

```text
IF Full(LoadingGap)
THEN WIPLoading_Avg - WIPLoading

ELSE IF Full(FAB_LoadingSpec)
THEN FAB_LoadingSpec - WIPLoading

ELSE 0.0
```

当 `LotAttribute = Important` 时，计算 `T_BUFFER_Pri`：

```
IF Full(LoadingGap)
THEN PriorWIPLoading_Avg - PriorWIPLoading

ELSE IF Full(FAB_LoadingSpec)
THEN FAB_LoadingSpec - PriorWIPLoading

ELSE 0.0
```

说明：

- 使用 `LoadingGap` 判断低 Loading 时，水位仅用于判断 STN 是否低 Loading。
- 接收量仍按平均 Loading 与当前 Loading 的差值计算。
- 使用 `FAB_LoadingSpec` 判断低 Loading 时，接收量按 `FAB_LoadingSpec` 与当前 Loading 的差值计算。

---

### 3. Candidate Lot 准备

本节用于从可 Transfer WIP 中筛选可参与当前低 Loading STN 选择的 Candidate Lot，并准备排序和模拟计算所需信息。

#### 3.1 Candidate Lot 入选条件

Lot 需满足以下条件后，认为是 LoadingCandidateLot：

1. `IsTransferCandidate = TRUE`
2. Lot 在对厂存在可作业机台。
3. Lot 对厂可作业机台中包含当前低 Loading STN。
4. Lot 未在本轮循环中判断过：

```
IsCandidateChecked = FALSE
```

#### 3.2 Lot 原始 Loading 分配关系获取

通过 `LOT + FULL_STEPSEQ` 从 `EqpLotSummarybyEqp` 获取 Lot 分配到各机台的 Loading 信息，用于后续判断与 Loading 更新。

#### 3.3 ReceiveSTNCnt

`ReceiveSTNCnt` 表示该 Lot 在对厂可匹配的低 Loading STN 数量。

排序原则：

```
ReceiveSTNCnt 越小越优先
```

原因：

可匹配低 Loading STN 越少，Lot 可选择空间越小，应优先处理。

### 4. Candidate Lot 循环选择逻辑

Candidate Lot 按 `STN + Timeline` 分层循环选择。每次只选择一个 Lot，完成模拟计算和 Loading 更新后，再继续下一轮选择。

#### 4.1 第一重循环：STN + Timeline 处理顺序

低 Loading 的 `STN + Timeline` 先按以下规则排序，再按排序结果逐一进入选 Lot 判断。

排序规则：

```text
MIN(Timeline)
MAX(T_BUFFER_Pri)
MAX(T_BUFFER)
```

说明：

1. 优先处理 Timeline 较小的低 Loading STN。
2. 同一 Timeline 下，优先处理 `T_BUFFER_Pri` 较大的 STN。
3. `T_BUFFER_Pri` 相同或已处理完成后，再处理 `T_BUFFER` 较大的 STN。
4. 当前 Timeline 的 Candidate Lot 范围不仅包含本 Timeline 的 Lot，也包含本 Timeline 之前可到站的 Lot。
5. 选 Lot 时优先选择与当前 Timeline 更接近的 Lot。

#### 4.2 第二重循环：逐 Lot 选择与更新

在每个 `STN + Timeline` 下，每次只选择一个 Lot。

Lot 选中后，立即模拟计算并更新相关 Loading，再重新进入下一轮选择。

#### 4.3 Candidate Lot 基础筛选

当前 `STN + Timeline` 下，Candidate Lot 需满足以下条件：

```
!IsToDispatch
AND !IsCandidateChecked
AND STN = STN_checking
AND Timeline <= Timeline_checking
```

说明：

- `STN = STN_checking`：Lot 对厂可作业机台需包含当前低 Loading STN。
- `Timeline <= Timeline_checking`：当前检查 Timeline 可选择本 Timeline 及之前的 Lot。
- `!IsToDispatch`：Lot 未被本轮选择过。
- `!IsCandidateChecked`：Lot 尚未在本轮选择中判断过。

#### 4.4 Priority Lot 优先选择规则

若当前 `T_BUFFER_Pri > 0`，表示 Priority Loading 仍需接收 Lot，本轮仅保留 Priority Lot 参与排序：

```
IsPriorityLot = TRUE
```

若当前 `T_BUFFER_Pri <= 0`，则 Priority 检查完成，后续可选择 Normal Lot 或 Priority Lot 参与普通 Loading 计算。

#### 4.5 Candidate Lot 排序

Candidate Lot 按以下顺序排序：

```
MIN(Timeline_checking - Timeline)
MIN(ReceiveSTNCnt)
```

若当前 Priority Loading 未完成：

```
PIECES >= T_BUFFER_Pri
MIN ABS(PIECES - T_BUFFER_Pri)
```

若当前 Priority Loading 已完成：

```
PIECES >= T_BUFFER
MIN ABS(PIECES - T_BUFFER)
```

最后按：

```
MIN RTDRank
```

排序说明：

1. 优先选择与当前检查 Timeline 更接近的 Lot。
2. 优先选择可匹配低 Loading STN 数量较少的 Lot。
3. Priority Loading 未完成时，优先选择片数更接近 `T_BUFFER_Pri` 的 Priority Lot。
4. Priority Loading 已完成后，优先选择片数更接近 `T_BUFFER` 的 Lot。
5. 最后按 `RTDRank` 排序。

#### 4.6 选中 Lot 后的片数分配

Lot 被选中后，仅将该 Lot 分配给当前低 Loading STN。

片数更新规则：

```
IF IsSelectedLot AND STN_checking = STN
THEN Real(PIECES)

ELSE IF IsSelectedLot AND STN_checking != STN
THEN 0.0

ELSE PiecesPreStation
```

说明：

1. 被选中的 Lot，只保留当前低 Loading STN 的分配片数。
2. 被选中的 Lot，在其他 STN 上的分配片数改为 0。
3. 未被选中的 Lot，保持原 `PiecesPreStation`。

#### 4.7 Transfer 后 Loading 模拟计算

Lot 选中前，需先模拟计算该 Lot 转移到当前低 Loading STN 后，对相关机台 Loading 的影响。

检查该 Lot 从其他机台移出后，相关机台 Loading 是否仍满足配置要求。

模拟计算检查范围：

```
timeline <= timeline_checking
```

说明：

当前选择只检查当前及更近 Timeline 的 Loading 是否满足要求；更大的 Timeline 会在后续循环中继续处理。

#### 4.8 Loading 检查通过条件

若当前正在检查 Priority Loading：

```
Priority Loading OK
```

若当前处理普通 Loading，且 Lot 为 Priority Lot：

```
Priority Loading OK
AND Normal Loading OK
```

若当前处理普通 Loading，且 Lot 为 Normal Lot：

```
Normal Loading OK
```

说明：

- Priority Lot 会同时影响 Priority Loading 和普通 Loading。
- Normal Lot 只影响普通 Loading。

#### 4.9 Loading 更新

模拟计算通过后，将该 Lot 标记为本轮 Transfer Candidate，并同步更新当前 Timeline 及后续 Timeline 的相关机台 Loading。

若模拟计算不通过，则继续检查下一 Candidate Lot。

更新内容：

```
WIPLoading
PriorWIPLoading
```

更新范围：

```
该 Lot 当前 Timeline 及之后的所有相关机台
```

例如：

```
Lot Timeline = 10
```

则需更新：

```
所有 Timeline >= 10 的相关机台 Loading
```

说明：

`IsToDispatch` 只表示该 Lot 当前 Timeline 已被选中。为避免后续 Timeline 仍使用旧 Loading，需同步更新该 Lot 后续 Timeline 相关机台的 Loading。

#### 4.10 当前 STN + Timeline 结束条件

满足以下任一条件时，退出当前 `STN + Timeline` 的选 Lot 循环：

```
T_BUFFER_Pri <= 0
OR T_BUFFER <= 0
OR transfercnt 达到 TransferLotCountLimit
```

其中：

- `T_BUFFER_Pri <= 0`：Priority 需接收量已满足。
- `T_BUFFER <= 0`：普通 Loading 需接收量已满足。
- `TransferLotCountLimit` 按 `SelfCapabilityGroup` 计数。

退出后，进入下一个 `STN + Timeline`。

### 5. OQT 风险检查

检查当站需Transfer的CandidateLot在传到对厂后是否有OQT风险，无风险的lot生成Transfer 结果。

## 三、Test Case

### 2. LoadingCandidateLot 修改

| 测试内容 | 测试场景 | 预期结果 |
| --- | --- | --- |
| WIP 获取范围 | WIP 获取范围与 STN Loading 计算范围一致；Lot 需可串取 `EqpLotSummarybyEqp` 信息 | 正确取得可参与 Transfer 判断的 WIP；缺少站点筛除相关判断不影响后续通过 `EqpLotSummarybyEqp` 判断 |
| Transfer Lot 标识 | Lot 满足 `TransferCondition`，且满足 `TargetFabCondition` | `IsTransferCandidate = TRUE` |
| 不可 Transfer Lot 标识 | Lot 不满足 `TransferCondition`，或不满足 `TargetFabCondition` | Lot 不进入 LoadingCandidateLot 后续选择 |
| Transfer 相关信息获取 | Lot 可 Transfer 时，获取对厂可作业机台、`SelfCapabilityGroupLimit` 中 `TransferLotCountLimit`、`TransferLotSortingItem` 中排序指标 | 正确取得 Lot 可匹配的 STN、Transfer 数量限制及 `RTDRank` |
| Loading 配置匹配 | `EqpLoadingSummarybyEqp` 中 STN + Timeline 通过 `SelfCapabilityGroup` 匹配 `LoadingSettingINFO`，且 `Timeline <= QTLimit` | 正确匹配到可用 Loading 配置 |
| 多 QTLimit 配置处理 | 同一 `SelfCapabilityGroup` 下存在多笔满足 `Timeline <= QTLimit` 的配置 | 取满足条件下 `QTLimit` 最小的一笔配置 |
| 多 SelfCapabilityGroup 配置处理 | 同一 STN 同时归属多个 `SelfCapabilityGroup` | 每个 `SelfCapabilityGroup` 分别匹配配置，并各保留一笔 |
| 无 Loading 配置 | STN + Timeline 未匹配到 `LoadingSettingINFO` 配置 | 不作为 ReceiveLoading STN |
| Normal 低 Loading 判断-LoadingGap | `LotAttribute = Normal`，`LoadingGap` 有值，且 `WIPLoading <= MAX(0, WIPLoading_Avg - LoadingGap)` | STN 判断为 `ReceiveLoading` |
| Normal 低 Loading 判断-FAB_LoadingSpec | `LotAttribute = Normal`，`FAB_LoadingSpec` 有值，且 `WIPLoading <= FAB_LoadingSpec` | STN 判断为 `ReceiveLoading` |
| Important 低 Loading 判断-LoadingGap | `LotAttribute = Important`，`LoadingGap` 有值，且 `PriorWIPLoading <= MAX(0, PriorWIPLoading_Avg - LoadingGap)` | STN 判断为 `ReceiveLoading` |
| Important 低 Loading 判断-FAB_LoadingSpec | `LotAttribute = Important`，`FAB_LoadingSpec` 有值，且 `PriorWIPLoading <= FAB_LoadingSpec` | STN 判断为 `ReceiveLoading` |
| 多配置均满足低 Loading | 相同 `LotAttribute` 下，不同 `SelfCapabilityGroup` 配置均满足低 Loading 条件 | STN 视为 ReceiveLoading；取水位最小的一笔配置用于后续接收量计算 |
| T_BUFFER 计算-LoadingGap | ReceiveLoading STN 使用 `LoadingGap` 判断低 Loading | 水位仅用于判断是否低 Loading；`T_BUFFER = WIPLoading_Avg - WIPLoading`，`T_BUFFER_Pri = PriorWIPLoading_Avg - PriorWIPLoading` |
| T_BUFFER 计算-FAB_LoadingSpec | ReceiveLoading STN 使用 `FAB_LoadingSpec` 判断低 Loading | `T_BUFFER = FAB_LoadingSpec - WIPLoading`，`T_BUFFER_Pri = FAB_LoadingSpec - PriorWIPLoading` |
| 第一重循环排序 | 存在多个低 Loading 的 `STN + Timeline` | 按 `MIN(Timeline)`、`MAX(T_BUFFER_Pri)`、`MAX(T_BUFFER)` 顺序处理 |
| Candidate Lot 基础筛选 | Lot 满足 `!IsToDispatch`、`IsCandidateChecked`、`STN = STN_checking`、`Timeline <= Timeline_checking` | Lot 可进入当前 `STN + Timeline` 的 Candidate Lot 排序 |
| Candidate Lot 基础筛除 | Lot 已被选择、未完成检查、STN 不一致，或 Timeline 晚于当前检查 Timeline | Lot 不参与当前 `STN + Timeline` 选择 |
| Priority Lot 优先选择 | 当前 `T_BUFFER_Pri > 0` | 仅保留 `IsPriorityLot = TRUE` 的 Lot 参与本轮选择 |
| Priority 检查完成后选择 | 当前 `T_BUFFER_Pri <= 0` | Priority Lot 与 Normal Lot 均可参与普通 Loading 选择 |
| Candidate Lot 排序 | 多个 Candidate Lot 同时满足选择条件 | 按 `MIN(Timeline_checking - Timeline)`、`MIN(ReceiveSTNCnt)`、片数接近接收量、`MIN RTDRank` 排序 |
| Candidate Lot 片数匹配-Priority | 当前 Priority Loading 未完成 | 优先选择 `PIECES >= T_BUFFER_Pri` 且 `ABS(PIECES - T_BUFFER_Pri)` 最小的 Priority Lot |
| Candidate Lot 片数匹配-Normal | 当前 Priority Loading 已完成 | 优先选择 `PIECES >= T_BUFFER` 且 `ABS(PIECES - T_BUFFER)` 最小的 Lot |
| 选中 Lot 片数分配 | Lot 被选中，且 `STN_checking = STN` | 该 Lot 在当前低 Loading STN 的 `PiecesPreStation = Real(PIECES)` |
| 选中 Lot 其他 STN 片数 | Lot 被选中，且 `STN_checking != STN` | 该 Lot 在其他 STN 的 `PiecesPreStation = 0.0` |
| 未选中 Lot 片数 | Lot 未被选中 | 保持原 `PiecesPreStation` |
| Transfer 后 Loading 模拟计算范围 | Lot 转移到当前低 Loading STN 后进行 Loading 检查 | 仅检查 `timeline <= timeline_checking` 的相关机台 Loading |
| 其他机台 Loading 检查 | Lot 从其他机台移出后，其他相关机台 Loading 下降 | 其他机台仍需满足 `FAB_LoadingSpec` 或平均 Loading 相关要求；当前接收 STN 不作为减少风险检查对象 |
| Priority Loading 检查条件 | 当前正在检查 Priority Loading | Priority Loading OK 时，该 Lot 可作为本轮 Transfer Candidate |
| Priority Lot 普通 Loading 检查 | 当前检查普通 Loading，且 Lot 为 Priority Lot | 需同时满足 Priority Loading OK 与 Normal Loading OK |
| Normal Lot 普通 Loading 检查 | 当前检查普通 Loading，且 Lot 为 Normal Lot | 满足 Normal Loading OK 即可 |
| 模拟计算通过 | Lot Transfer 后 Loading 检查通过 | 标记为本轮 Transfer Candidate，并更新相关 Loading |
| 模拟计算不通过 | Lot Transfer 后 Loading 检查不通过 | 不选择该 Lot，继续检查下一 Candidate Lot |
| Loading 更新范围 | Lot 被选中，当前 Timeline = N | 更新该 Lot 当前 Timeline 及之后所有相关机台 Loading，即所有 `Timeline >= N` 的相关机台 |
| IsToDispatch 与后续 Timeline 更新 | Lot 当前 Timeline 已被选中，但后续 Timeline 仍存在相关 Loading | `IsToDispatch` 仅代表当前 Timeline 已选中；后续 Timeline 需同步使用更新后的 Loading |
| 当前 STN + Timeline 结束条件 | `T_BUFFER_Pri <= 0`，或 `T_BUFFER <= 0`，或 `transfercnt` 达到 `TransferLotCountLimit` | 退出当前 `STN + Timeline` 选 Lot 循环，进入下一个 `STN + Timeline` |
| TransferLotCountLimit 计数 | 同一 `SelfCapabilityGroup` 下连续选择 Transfer Lot | `transfercnt` 按 `SelfCapabilityGroup` 计数，达到限制后不再为该组继续选择 |
| OQT 风险检查 | Candidate Lot 传到对厂后存在 OQT 风险 | 不输出 Transfer 结果 |
| OQT 无风险 | Candidate Lot 传到对厂后无 OQT 风险 | 生成 Transfer 结果 |
