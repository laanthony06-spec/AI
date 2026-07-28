# STNLoadingBalance 需求单优化稿 v1.1

> 基于 `STNLoadingBalance需求单_优化稿_v0.7修改后.docx` 整理。  
> 已合并用户确认口径：Timeline 可配置、正式字段名、PM_RemainTime 定义、Priority 无数据输出 0、EqpLotSummary 字段含义。  
> 当前范围：包含 `EqpLoadingSummary / EqpLotSummary Report 输出修改` 与 `LoadingCandidateLot 修改` 两部分。  
> v1.1 更新：5 项待确认事项全部闭环（PW 50 站代码写死、CreateTime 取 Report Job 开始时间、IsCandidateChecked 含义明确、MFGControl 沿用既有逻辑、Important Lot CSV 配置确认）。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 编号 | （此处由信息技术部填写） |
| 类别 | □1. 软件采购　□2. 硬件采购　☑3. 功能开发　□4. 工程及服务 |
| 申请部门 | 制造部 |
| 系统名称 | CIM 计算机集成制造系统 Fab6（二科） |
| 申请人员 | 温浩奇 |
| 功能模块 | 智能派工系统（RTD/DSP） |
| 申请日期 | 2026-05-19 |
| 希望交付期 | 2026-xx-xx |

## 项目简介和必要性分析

### 项目背景

当前 LoadingBalance 以 SelfCapability 作为 Loading 均衡对象，可作业机台来源为 WIP 对应可作业机台并集。

### 存在问题

不同产品、不同 Lot 的 release 条件、可作业机台、跨厂可作业条件、PM 状态、QZone 管控存在差异。若仍按 SelfCapability 整体计算 Loading，机台组内部负荷差异无法展开，结果容易与实际机台负荷不一致。

### 修改内容

将 LoadingBalance 计算粒度由 SelfCapability 调整为 STN / 机台维度。

STNLoadingBalance 按配置的 Timeline 层级计算每台机台 Loading。当前配置层级为：

```text
0、2、6、12、24
```

后续若配置新增层级，计算逻辑需按配置层级自动扩展。

本次需求分为两部分：

1. `EqpLoadingSummary / EqpLotSummary Report 输出修改`：计算并输出 STN 维度 Loading 结果。
2. `LoadingCandidateLot 修改`：使用 STN 维度 Loading 结果识别低 Loading 机台，并按 Timeline / Priority / Loading 缺口选择可 Transfer Lot。

### 输出目标

需输出：

- FAB6 单厂 Loading：`WIPLoading`
- FAB8 单厂 Loading：`WIPLoading`
- 两厂平均 Loading：`WIPLoading_Avg`
- FAB6 Priority Lot 单厂 Loading：`PriorWIPLoading`
- FAB8 Priority Lot 单厂 Loading：`PriorWIPLoading`
- 两厂 Priority Lot 平均 Loading：`PriorWIPLoading_Avg`

NOTE: Priority Loading 不从全量 Loading 拆分。需筛选 `isprioritylot = T` 的 Lot 后单独执行 WaferBalance。

## 项目投资方案比较及效果分析

### 改善方案

本次修改范围为 RTD/DSP Loading 计算逻辑。

主要修改点：

1. 重新整理 FAB6 / FAB8 WIP 获取与站点展开逻辑。
2. 按 Lot 当前站点至第一个安全站点范围保留候选站点。
3. 结合 QZone、Loop Lot Control、LCC / PCC / MCC / T2T / DOMA / MES Pirun / CPK 等规则判断可作业机台。
4. 结合 ArriveTime、PM / 借机管控、WPH / WPHLoss 计算机台可提供的作业能力。
5. 按 STN / 机台维度执行 WaferBalance，输出单厂 Loading、两厂平均 Loading、Priority Loading。
6. 输出 `EqpLoadingSummary` 与 `EqpLotSummary`，供后续 Over Loading / Under Loading 及选 Lot 逻辑使用。
7. 修改 `LoadingCandidateLot` 逻辑，按 STN 维度 Loading 结果挑选可补低 Loading 机台的 Transfer Candidate Lot。

### 效果分析

LoadingBalance 由机台组维度调整为机台维度。

预期效果：

1. Loading 结果更接近现场可作业机台负荷。
2. 减少 SelfCapability 内 release 差异造成的误判。
3. 为 Over Loading / Under Loading 判断提供机台级数据。
4. 支持跨厂 WIP balance 后续选 Lot 判断。
5. LoadingCandidateLot 可基于 STN 维度缺口逐机台、逐 Timeline 选择 Lot，减少只看机台组 Loading 造成的选 Lot 偏差。

## 需求流程图

```text
开始
↓
获取并筛选 FAB6 / FAB8 WIP
↓
修正 Transfer Lot 唯一信息
↓
按 NPW / PW 获取站点信息
↓
识别 Key Lot / Target Lot / Important Lot
↓
获取 SelfCapability / SelfCapabilityGroup
↓
截取当前站点至第一个安全站点
↓
执行 QZone / Loop Lot Control 站点筛选
↓
判断可作业机台，获取 PM / WPH 信息
↓
执行 MFGControl 判断
↓
按配置 Timeline 层级执行单厂 WaferBalance
↓
筛选 isprioritylot = T，执行 Priority 单厂 WaferBalance
↓
按配置 Timeline 层级执行两厂平均 WaferBalance
↓
筛选 isprioritylot = T，执行 Priority 平均 WaferBalance
↓
输出 EqpLoadingSummary / EqpLotSummary
↓
读取 LoadingSettingINFO 中 isBySTN=True 的配置
↓
从 EqpLoadingSummary / EqpLotSummary 获取机台维度 Loading 与 Lot 分配关系
↓
判断低 Loading STN，计算 T_BUFFER / T_BUFFER_Pri
↓
获取可 Transfer Candidate Lot，并执行当站状态再过滤
↓
按 STN + Timeline 循环挑选 Lot
↓
试算选中 Lot 对相关机台 Loading 的影响
↓
输出 LoadingCandidateLot 结果
↓
结束
```

# 一、RTD 部分更改逻辑

## 1. EqpLoadingSummary / EqpLotSummary 逻辑修改

### 1.1 修改目标

原 `EqpLoadingSummary` 按 SelfCapability 维度计算 Loading。本次修改后，Loading 需改为按 STN / 机台维度计算。

### 1.2 EqpLoadingSummary 输出字段

`EqpLoadingSummary` 用于保存机台维度 Loading 结果。

建议字段：

| 字段 | 含义 |
| --- | --- |
| `EqpSite` | 机台所在厂 |
| `SelfCapability` | 机台对应 SelfCapability |
| `STN` | 机台 |
| `Timeline` | Timeline 层级 |
| `WIPLoading` | 单厂 Loading |
| `WIPLoading_Avg` | 两厂平均 Loading |
| `PriorWIPLoading` | Priority Lot 单厂 Loading |
| `PriorWIPLoading_Avg` | 两厂 Priority Lot 平均 Loading |
| `CreateTime` | 整个 Report Job 开始时间 |

### 1.3 EqpLotSummary 输出字段

`EqpLotSummary` 用于保存 Lot 与机台分配关系及中间计算结果。

建议字段：

| 字段 | 含义 |
| --- | --- |
| `Lot` | Lot |
| `CurStep_FullSeq` | Lot 当前站点 FullSeq |
| `Full_StepSeq` | 参与计算站点 FullSeq |
| `Timeline` | Timeline 层级 |
| `SelfCapabilityGroup` | SelfCapabilityGroup |
| `STN` | 分配机台 |
| `Pieces` | Lot 总片数 |
| `IsPriorityLot` | 是否 Priority Lot |
| `LotAttInfoSite` | Lot 当前所在厂 |
| `CurrentInfoSite` | Lot 在该站实际作业厂 |
| `EqpSite` | 机台所在厂 |
| `PiecesPreStation` | Lot 分配到该机台的片数 |
| `UPH` | 机台每小时作业片数 |
| `LoadingPreStation` | 机台作业 Lot 分配片数所需时间，等于 `PiecesPreStation / UPH` |
| `CreateTime` | 整个 Report Job 开始时间 |

## 2. WIP 获取逻辑

### 2.1 基础数据来源

需从 FAB6 / FAB8 获取 Lot 基础数据。

| 数据来源 | 主要用途 |
| --- | --- |
| `fwlot` | 获取 Lot 基础信息 |
| `fwwipstep` | 获取 `Stepseq`、`Stage` 等站点信息 |
| `fwproduct` / `fabproductext` | 获取 `Producttype` |
| `fabcategorymap` | 根据 `lottype` 获取 `Producttype` |
| `fwprocessplan` / `fabprocessplanext` | 获取 `Technology` |
| `fablotext` | 获取 Lot 的 Capability（STNFAM）及状态信息 |
| `RTDConfig` | 获取 N20 `internalpriority` 配置 |
| `fablotcarrierext` | 获取 carrier 基础信息 |
| `fabeapseasonprocess` | 获取 `controlid`，rename 为 `seasoncontrolid` |
| `fabeapmonitorprocess` | 获取 `controlid`，rename 为 `monitorcontrolid` |
| `fabeapmonitorgroup` / `fabeapmonitorgroup_N2M` | 获取 `toid` |
| `FabeapTRCGroupitem` / `FabeapTRCGroup` | 获取 `groupid` |
| `FabEapDummylotProcess` | 获取 `dummyid` |

### 2.2 Producttype 修正规则

当 Lot 在 `fwproduct` 中的 `Producttype` 为 `Production` 或 `Engineer` 时，优先使用 `fabcategorymap` 中的 `Producttype`。

当 Lot 满足 `RTDConfig` 中 N20 `internalpriority` 配置时，将该 Engineer Lot 视为 Production Lot。

### 2.3 Season / Monitor / Dummy 标识

Season 判断：

```text
从 fabeapseasonprocess 获取 controlid，rename 为 seasoncontrolid
从 fabeapmonitorgroup / fabeapmonitorgroup_N2M 获取 toid
从 FabeapTRCGroupitem / FabeapTRCGroup 获取 groupid
当 Lot 有 toid 或 groupid 时，seasonflag = True
```

Monitor 判断：

```text
Null(STNFAM) and Full(monitorcontrolid)
=> Monitorflag = True
```

Dummy 判断：

```text
Full(dummyid)
=> dummyflag = True
```

### 2.4 WIP 筛选条件

系统筛选满足以下条件的 WIP：

```text
(
  (priority < 8 and processingstatus = Active)
  or
  (priority < 5 and processingstatus = CrossFabTransferred)
)
and carrierkind = FOUP
and !(Full(dummyflag) or Full(seasonflag))
```

### 2.5 Transfer Lot 唯一性处理

获取 FAB6 / FAB8 两厂 Lot 后，通过 `Macro:GetCrossFabLotList` 判断 Lot 是否为 Transfer Lot。

保留规则：

```text
(!IsTransferlot and LotStatus != CrossFabTransferred)
or IsTransferlot
```

含义：

1. 非 Transfer Lot：保留 `LotStatus != CrossFabTransferred` 的记录。
2. Transfer Lot：保留 Transfer Lot 对应准确记录。

## 3. Important Lot 定义

### 3.1 Key Lot

从 `quota_applyinfo` 判断 Lot 的 key lot 指标。

### 3.2 Target Lot

数据来源：

- 从 `tb_special_targetlot` 获取 `lotid`、`TargetStepseq`。
- 从 `quota_applyinfo` 获取 `lotid`、`dept`、`TargetStepsequence`。

Target Lot 生效条件：

```text
(Lot = lotid and FullStepSeq <= TargetStepseq)
or
(Lot = lotid and dept != support and FullStepSeq <= TargetStepsequence)
```

### 3.3 Important Lot

满足配置的 Lot 记为 Important Lot。配置文件为 `ImportantLotConfig.csv`，与 RTDConfig 同目录维护。

配置维度：

```text
keylot
Targetlot
ProductionType
ProdName
Tech
LotType
Recipe
Priority
InternalPriority
MPCPriority
```

Lot 命中配置时：

```text
isprioritylot = T
```

## 4. 站点信息获取逻辑

### 4.1 NPW / PW 站点获取范围

| Lot 类型 | 判断条件 | 站点获取范围 |
| --- | --- | --- |
| NPW Lot | `!(category = Production or category = Engineer)` | 当前站 |
| PW Lot | `(category = Production or category = Engineer)` 且排除 5-9 Lot | 后续 50 站，50 为代码写死 |

PW Lot 需额外去除等级为 5-9 的 Lot：

```text
(category = Production or category = Engineer)
and !(priority = 5 and internalpriority = 9)
```

### 4.2 NPW Lot 站点信息

NPW Lot 从 `npwepr` 获取：

```text
CurStepSeq
FullStepSeq
StepIndex
capability
stage
product
LotAttInfoSite
CurrentInfoSite
```

从 `fablotext` 获取：

```text
recipe
Pieces
```

从 `FabeqpCapability` 按 Capability 获取：

```text
STN
EqpSite
```

### 4.3 NPW Lot 主机台 / 前量机台修正

数据来源：

- 从 `FabEapMonitorProcess` by Lot 和 `controlid` 获取 `eqpname`、`state`。
- 从 `FabEQPMonitorid` by `Controlid` 获取主机台 `stepseq`。
- 从 `FabEqpMonitorProcessN2M` 获取前量机台 `PreStn`。

处理逻辑：

1. 若 `state = inuse` 且 `lot CurStepSeq = stepseq`，机台替换为 `eqpname`。
2. 若 `state != inuse`，保留 Capability 获取的机台。
3. 若 `state = inuse` 且 `lot CurStepSeq != stepseq`，机台替换为 `PreStn`。

### 4.4 Specialization 指定机台修正

从 `FabFutureAction` 获取 Lot 的 Specialization 指定机台信息。

若存在 Specialization 指定机台，使用指定机台；否则保留主机台 / 前量机台 / Capability 判断后的机台。

### 4.5 PW Lot 站点信息

PW Lot Fetch 后续 50 站（50 为代码写死，不做参数化），并获取：

```text
CurStepSeq
FullStepSeq
StepIndex
product
stage
recipe
capability
Stn
ArriveTime（CT 累加）
LotAttInfoSite
CurrentInfoSite
EqpSite
```

若 Lot 为 `isTransferlot`，需修正站点厂别信息。

## 5. SelfCapability / SelfCapabilityGroup 获取

### 5.1 数据来源

| 数据来源 | 获取字段 |
| --- | --- |
| `tb_product_list` | `tech`、`productname` |
| `tb_selfcapa_rule` | `stagename`、`capability`、`recipe`、`selfcapability` |
| `UI SelfCapabilityGroupLimit` | `SelfCapability`、`SelfCapabilityGroup` |

### 5.2 匹配逻辑

1. By product，从 `tb_product_list` 获取 Lot 所属 `tech`。
2. 根据 Lot 各站点的 `capability`、`stage`、`product`、`recipe`、`tech`，从 `tb_selfcapa_rule` 获取 `SelfCapability`。
3. By `SelfCapability`，从 UI `SelfCapabilityGroupLimit` 获取 `SelfCapabilityGroup`。

## 6. 安全站点判断逻辑

获取 Lot 安全站点，并仅保留从当前站点到第一个安全站点之间的站点，包含当前站点和安全站点。

安全站点包括：

1. SafetyValue 安全站点。
2. 自定义安全站点。

### 6.1 SafetyValue 安全站点

满足以下任一条件，视为安全站点：

```text
3 <= safety value
or qtime type 均为 start
or qtime type 为空
```

### 6.2 自定义安全站点

设定值来源：

```text
RTDConfig-Global-APMSafetyValue
```

满足以下任一组条件，视为自定义安全站点：

```text
情形一：
safety value = 设定值
and 存在 qtimetype = End（只看 MAX qtime）
and 必须存在 qtime type = START
and 所有 END qtime 对应的 Min(qlimit) >= 设定时间

情形二：
safety value = 设定值
and Qtimetype 全为空

情形三：
safety value = 设定值
and Qtimetype 全为 Start
```

## 7. QZone 与 Loop Lot Control 判断

Lot 经 QZone Control 与 Loop Lot Control 判断后，按以下规则筛选站点。

### 7.1 QZone Control

若 Lot 在某站点卡控 QZone Control，则筛除该站点及其之后的所有站点。

例外：

```text
保留 issue 站点
```

### 7.2 Loop Lot Control

若 Lot 在某站点卡控 Loop Lot Control，则筛除该站点及其之后的所有站点。

例外：

```text
保留结束站点
```

## 8. 可作业机台判断

### 8.1 YE Skip 判断

从 `FabSsnfcSkip` 获取配置：

```text
baselineSubid
eqpCapability
planid
productid
scanLotid
stageid
stepseq
skipLotid
```

匹配规则：

| 条件 | 结果 |
| --- | --- |
| 匹配 `scanLotid` | `ScanFlag = T` |
| 匹配 `skipLotid` | `SkipFlag = T` |
| Lot 最后一位匹配 `baselineSubid` | `baselineFlag = T` |

跳站判断：

```text
ScanFlag = F and SkipFlag = T
or
ScanFlag = F and SkipFlag = F and baselineFlag = T
```

命中时去除 Lot 可跳站的站点。

### 8.2 RC / 非 RC 对厂机台获取

当 `FullStepseq` 包含 RC：

1. 通过 `FabRunCard`、`FabRCDstepinfo` 获取 RC 指定机台。
2. 通过 `FabeqpCapability` 用 Capability 获取 Lot 在对厂站点的机台。
3. 若存在 RC 指定机台，使用 RC 指定机台；否则使用 Capability 获取的机台。
4. 检查机台 capability、Recipe、PPID。

当 `FullStepseq` 不包含 RC：

1. 从 `FabFutureAction` 获取 Specialization 指定机台。
2. 通过 `FabeqpCapability` 获取 Lot 在对厂站点的机台。
3. 若存在 Specialization 指定机台，使用 Specialization 指定机台；否则使用 Capability 获取的机台。
4. 检查机台 capability、Recipe、PPID。

输出：

```text
AvailStnList
AvailPPidList
AvailChamberList
```

### 8.3 可作业条件判断

RC 与非 RC Lot 合并后，经过以下逻辑判断：

```text
LCC
PCC
MCC
T2T
DOMA
MES Pirun
CPK
```

NOTE: 若存在单厂 LCC 结果，直接使用单厂 LCC 结果；否则跑 ParaLCC 逻辑。

最终得到 Lot 在站点本厂和对厂的可作业机台：

```text
AvailableStnChamberList
```

## 9. Timeline 获取

### 9.1 数据来源

从 `restructedQtime` 获取：

```text
part
part_revision
route
route_revision
gatestepbeginsequence
c_gateendsequence
c_queuelimithours_nopt
```

根据 Lot 的 `product`、`productversion`、`plan`、`planversion` 取得对应记录。

### 9.2 Timeline 计算逻辑

根据 Lot 的 `CurIndex` 与各站点 `FullStepIndex`，得到 Lot 到每一站的 Timeline。

满足以下条件时，取对应 `c_queuelimithours_nopt` 作为 Lot 在该站点的 Timeline：

```text
(
  CurIndex > gatestepbeginsequence
  or
  (
    CurIndex <= gatestepbeginsequence
    and extrastatus != Wait For Job Prep
  )
)
and FullStepIndex <= c_gateendsequence
```

若 Lot 在该站点满足：

```text
Fullstepseq = CurStepseq
```

则该站点 Timeline 取：

```text
0
```

否则取原 Timeline。

NOTE: STNLoadingBalance 按配置 Timeline 层级计算。当前配置为 `0、2、6、12、24`，后续新增层级时按配置自动扩展。

## 10. PM 管控判断

本需求不修改既有 PM / 借机管控逻辑。Loading 计算中判断机台是否可参与该 Lot 作业时，沿用既有 PM 管控结果。

### 10.1 到站时间口径

PM 管控判断中的 Lot 到站时间使用 `ArriveTime`，其来源为 CycleTime 累计结果，不再使用原 Qsort 判断口径。

计算原则：

1. Lot Fetch Step 时，计算 Lot 到每一站的预计到站时间。
2. Process 站点使用 CycleTime。
3. 非 Process 站点使用 ProcessTime。
4. 每站 CT / PT 逐站累加后，作为该站点的 `ArriveTime`。
5. PM / 借机管控判断使用该 `ArriveTime` 与 PM / 借机管控区间比较。

### 10.2 PM 时间区间

从 `STNPMTimeControlInfo` / `STNPMTimeControl` 获取机台 PM / 借机相关信息。

主要使用信息包括：

- `MachineID_New`
- `PlanStartTime`
- `PlanEndTime`
- `PMFlag`
- `StdMonPM`
- `PirunStdTime`
- `PMQzoneControl`
- `ActualPMTimeDuration`

当 `PMQzoneControl = Y` 时，PM Start / End 需按既有逻辑修正：

```text
PMTimeDuration = PlanEndTime - PlanStartTime

PMStartTime = PlanStartTime - PMTimeDuration × PMStartRatio
PMEndTime   = PlanEndTime + PMTimeDuration × PMEndRatio + (StdMonPM + PirunStdTime) × (1 + MonRatio)
```

当 `PMQzoneControl != Y` 时：

```text
PMStartTime = PlanStartTime
PMEndTime   = PlanEndTime + PirunStdTime + StdMonPM
```

若使用相对当前时间判断，`$End` 表示当前时间：

```text
PMStartTime = PlanStartTime - $End
PMEndTime   = PlanEndTime - $End
```

### 10.3 机台保留判断

系统根据 Lot `ArriveTime` 与 PM / 借机管控区间判断机台是否可参与该 Lot 作业。

判断原则：

1. 借机场景按借机时间段判断。
2. PM 场景按修正后的 `PMStartTime` / `PMEndTime` 判断。
3. Machine / MainTool 均需判断，任一被 PM 管控影响时，按既有规则处理。
4. 若既有 PM 管控结果判定机台不可作业，则该机台不参与该 Lot 在该站点的 Loading 计算。
5. 若机台保留参与 Loading 计算，但 Lot 到站前存在 PM / 借机不可作业时间，则计算 `PM_RemainTime`。

### 10.4 PM_RemainTime 定义

`PM_RemainTime` 定义：

```text
Lot 到站前，机台因 PM / 借机不能提供作业的时长。
```

同一机台、同一 PM 计划、同一 Timeline 层级下：

```text
PM_RemainTime 相同
```

后续 Balance 计算机台累计作业时间时，需纳入该机台在当前 Timeline 层级下的 `PM_RemainTime`。

## 11. WPH 获取

根据机台厂别，从 `vw_dsp_capabilitywph` 中按以下优先级获取 Lot 在各站点机台的 WPH：

1. `capability + recipe + productname`
2. `capability + recipe`
3. `capability + productname`
4. `capability`

### 11.1 WPHLoss 原逻辑沿用

本需求不修改 WPHLoss 既有逻辑，Loading 计算使用 WPH 时需沿用原 WPHLoss 修正结果。

原逻辑简述如下：

1. WPHLoss 用于修正复合机台 / chamber 缺失造成的实际产能损失。
2. 按 `Lot / stepseq / EQPID` 分组判断是否需要计算 WPHLoss。
3. 同组内可作业 `STN` 具备相同且非空的 `ProcessGroup`，且 `WPHLossControl = Y` 时，计算 WPHLoss；否则沿用原 WPH。
4. 若 `STN` 包含 `-`，取 `-` 前的部分作为主机台 `EQPID`；否则 `EQPID = STN`。
5. 对需要计算 WPHLoss 的 Lot，拆分并去重 `chamberflow`，得到该 Lot 在该机台可用 chamber 清单。
6. 按 `Capability / ProcessGroup / Machine / SubeqpStateGroup / Count` 回表 `tb_dsp_wphloss` 匹配 Loss；未匹配到维护值时，`Loss = 0`。
7. 同一机台涉及多个 `SubeqpStateGroup` 时，最终 `WPHLoss` 取各分组 Loss 的最大值。
8. 实际 WPH 修正公式：

```text
Actual STN WPH = Total STN WPH × (1 - WPHLoss)
```

后续 WaferBalance 中使用的 WPH 均为修正后的实际 WPH。第一次 Balance 按 WPH 比例分配 Lot 片数时，也使用该修正后 WPH。

## 12. MFGControl 判断

Lot 在两厂的可作业机台需经过 MFGControl 判断。

MFGControl 完全沿用既有逻辑，不新增判断条件。如后续需修改 MFGControl，需另开需求单说明。

## 13. 机台单厂 Loading 计算

### 13.1 计算范围

单厂 Loading 计算时：

```text
FAB6 Lot 仅使用 FAB6 可作业机台
FAB8 Lot 仅使用 FAB8 可作业机台
```

单厂 Loading 只反映各厂自身可作业机台的负荷情况。

### 13.2 Timeline 层级

系统按配置的 Timeline 层级执行 Loading 计算。当前配置层级为：

```text
0、2、6、12、24
```

后续若配置新增层级，计算逻辑按配置层级自动扩展。

### 13.3 单厂 WaferBalance 计算

系统按 `SelfCapabilityGroup_STN` 获取所有 Lot，并按 Timeline 层级划分后，使用 WaferBalance 方法计算机台 Loading。

每一层级 Balance 时，需考虑：

1. 上一层级机台已累计的需求作业时间。
2. 当前 Timeline 层级下机台因 PM / 借机无法提供作业能力的时间，即 `PM_RemainTime`。

继承规则：

```text
上一层级 Balance 结束后，
各机台累计作业时间作为下一层级 Balance 前的初始化作业时间。

若某机台在之前层级中均未出现，
初始化时间 = 0。
```

### 13.4 WaferBalance 基础规则

WaferBalance 计算遵循以下原则：

1. 第一次 Balance 按可作业机台 WPH 比例分配 Lot Qty。
2. `Step WIP Time = Qty Assign / WPH`。
3. 第一次权重：

```text
Weight(1) = 1 / New EQP WIP Time(1)
```

4. 第二次及以后按上一轮 Weight 分配 Lot Qty。
5. 第二次及以后权重：

```text
Weight(n) = (1 / New EQP WIP Time(n)) × Weight(n-1)
```

6. Balance 共执行 5 次。

### 13.5 PM_RemainTime 对 Balance 的影响

Balance 计算机台累计作业时间时，需纳入 `PM_RemainTime`：

```text
New EQP WIP Time
= Pre EQP WIP Time
+ Step WIP Time
+ PM_RemainTime
```

其中：

```text
PM_RemainTime = Lot 到站前，机台因 PM / 借机不能提供作业的时长
```

同一机台、同一 PM 计划、同一 Timeline 层级下，`PM_RemainTime` 相同。

### 13.6 Priority 单厂 Loading 计算

完成全量单厂 Loading 计算的同时，系统需筛选 `isprioritylot = T` 的 Lot，额外单独执行一次 WaferBalance，计算 Priority Lot 维度单厂 Loading。

计算范围：

```text
FAB6 PriorWIPLoading：
仅使用 FAB6 Lot 中 isprioritylot = T 的 Lot
且仅使用 FAB6 可作业机台。

FAB8 PriorWIPLoading：
仅使用 FAB8 Lot 中 isprioritylot = T 的 Lot
且仅使用 FAB8 可作业机台。
```

计算方法与全量单厂 Loading 一致：

1. 按配置 Timeline 层级计算。
2. 使用 WaferBalance 方法执行 5 次 Balance。
3. 继承上一 Timeline 层级的机台累计作业时间。
4. 计算时考虑机台 `PM_RemainTime`。
5. 输出每台机台在各 Timeline 层级下的 `PriorWIPLoading`。

若某厂、某 `SelfCapabilityGroup_STN`、某 Timeline 层级下不存在 `isprioritylot = T` 的 Lot：

```text
PriorWIPLoading = 0
```

## 14. 机台平均 Loading 计算

### 14.1 计算范围

平均 Loading 计算时：

```text
FAB6 Lot 使用 FAB6 + FAB8 两厂可作业机台
FAB8 Lot 使用 FAB6 + FAB8 两厂可作业机台
```

即两厂 Lot 与两厂可作业机台一起参与 WaferBalance，用于计算两厂合并视角下的平均 Loading。

### 14.2 计算方法

平均 Loading 与单厂 Loading 使用相同 WaferBalance 方法，区别仅在于 Lot 与可作业机台范围。

| 计算类型 | Lot 范围 | 可作业机台范围 | 输出结果 |
| --- | --- | --- | --- |
| FAB6 单厂 Loading | FAB6 全量 Lot | FAB6 可作业机台 | `WIPLoading` |
| FAB8 单厂 Loading | FAB8 全量 Lot | FAB8 可作业机台 | `WIPLoading` |
| 平均 Loading | FAB6 + FAB8 全量 Lot | FAB6 + FAB8 可作业机台 | `WIPLoading_Avg` |
| FAB6 Priority 单厂 Loading | FAB6 `isprioritylot = T` Lot | FAB6 可作业机台 | `PriorWIPLoading` |
| FAB8 Priority 单厂 Loading | FAB8 `isprioritylot = T` Lot | FAB8 可作业机台 | `PriorWIPLoading` |
| Priority 平均 Loading | FAB6 + FAB8 `isprioritylot = T` Lot | FAB6 + FAB8 可作业机台 | `PriorWIPLoading_Avg` |

### 14.3 Priority 平均 Loading 计算

平均 Loading 计算完成后，系统需筛选两厂 `isprioritylot = T` 的 Lot，额外单独执行一次两厂合并 WaferBalance，得到 `PriorWIPLoading_Avg`。

计算范围：

```text
Lot 范围：FAB6 + FAB8 中 isprioritylot = T 的 Lot
机台范围：FAB6 + FAB8 两厂可作业机台
```

计算方法与全量平均 Loading 一致，仅使用 Priority Lot 参与计算。

若某 `SelfCapabilityGroup_STN`、某 Timeline 层级下不存在 `isprioritylot = T` 的 Lot：

```text
PriorWIPLoading_Avg = 0
```

## 15. 输出结果说明

最终结果需支持：

1. 查看 FAB6 每台机台在不同 Timeline 下的单厂 Loading。
2. 查看 FAB8 每台机台在不同 Timeline 下的单厂 Loading。
3. 查看同一机台在两厂合并视角下的平均 Loading。
4. 查看 FAB6 / FAB8 每台机台在不同 Timeline 下的 Priority Lot 单厂 Loading。
5. 查看同一机台在两厂合并视角下的 Priority Lot 平均 Loading。
6. 供后续 Over Loading / Under Loading 判断及选 Lot 逻辑使用。

## 16. LoadingCandidateLot 修改

### 16.1 修改目标

`LoadingCandidateLot` 需引用本次新增的 STN 维度 Loading 结果，识别低 Loading 机台，并选择可转移到对厂低 Loading 机台作业的 Lot。

本章节不重新定义 Loading 计算逻辑，Loading 来源以前述 `EqpLoadingSummary` / `EqpLotSummary` 输出为准。

修改后逻辑需支持：

1. 从 UI 配置中识别 STN 维度 Loading 控制条件。
2. 按 STN / Timeline 判断低 Loading 机台。
3. 计算每个低 Loading STN 需要接收的 WIP 量。
4. 获取可 Transfer Candidate Lot。
5. 按 Timeline、Priority、Loading 缺口、可作业低 Loading STN 数量、RTD Rank 选择 Lot。
6. 每次选中 Lot 前先试算 Loading 影响，确认不会造成其他机台 Loading 不满足。
7. 选中 Lot 后，更新该 Lot Timeline 及之后相关机台的 Loading。

### 16.2 配置与数据来源

#### 16.2.1 UI 配置来源

从 UI `LoadingSettingINFO` 获取：

```text
isBySTN = True
```

的配置。

主要使用配置：

| 配置 | 用途 |
| --- | --- |
| `STN` | 指定机台 |
| `QTLimit` | Loading 判断使用的 Timeline 上限 |
| `SelfCapabilityGroup` | 机台所属 SelfCapabilityGroup |
| `LotAttribute` | Lot 属性配置 |
| `TargetFABS` | 目标厂别 |
| `LoadingGap` | 与两厂平均 Loading 的 Gap 控制 |
| `FAB_LoadingSpec` | 单厂 Loading Spec 控制 |
| `TransferLotCountLimit` | Transfer Lot 数量限制 |

配置匹配原则：

1. 筛选 `SelfCapabilityGroup` 中 `Timeline <= QLimit` 的机台和 Timeline。
2. 每个 Timeline 使用最近的 `QLimit` 配置。
3. 若同一 STN 命中多个配置，例如多 SelfCapabilityGroup 情况，需处理到唯一配置后再参与后续判断。

#### 16.2.2 Loading 数据来源

从 `EqpLoadingSummarybyEqp` 获取 STN 维度 Loading 信息。

正式字段统一如下：

| 字段 | 含义 |
| --- | --- |
| `WIPLoading` | 当前 STN 单厂 Loading |
| `WIPLoading_Avg` | 当前 STN 两厂平均 Loading |
| `PriorWIPLoading` | 当前 STN Priority Lot 单厂 Loading |
| `PriorWIPLoading_Avg` | 当前 STN Priority Lot 两厂平均 Loading |

历史字段对照：

```text
WIPLoading_allFab = WIPLoading_Avg
PriWIPLoading_allFab = PriorWIPLoading_Avg
PriWIPLoading = PriorWIPLoading
```

文档后续统一使用正式字段名。

#### 16.2.3 Lot 数据来源

从 `EqpLotSummaryByEqp` 按 `FULL_STEPSEQ / LOT` 取得 Lot 与机台 Loading 分配关系。

从 `LoadingMidLog` 取得低 Loading 机台相关 Lot 信息，主要包括：

```text
IsTransferCandidate
Fab
Fab_t
IsPriorityLot
RTDRank
TransferLotCountLimit
```

Candidate Lot 获取逻辑需与前述 Loading 计算中的 Lot 获取逻辑保持一致，并额外执行：

1. Transfer 检查。
2. TargetFab 检查。
3. 对厂 `AvailableSTNChamberList` 检查。
4. `AvailableSTNChamberList` 需包含当前低 Loading STN。

### 16.3 低 Loading STN 判断

#### 16.3.1 ReceiveLoading 判断

当 STN 满足以下任一条件时，视为可接收 Loading 的低 Loading 机台：

```text
IF (
    Full(LoadingGap)
    AND MAX(0, WIPLoading_Avg - LoadingGap) >= WIPLoading
)
OR
(
    FULL(FAB_LoadingSpec)
    AND WIPLoading <= FAB_LoadingSpec
)
THEN ReceiveLoading
```

命中 `ReceiveLoading` 的 STN 进入 `ReceiveSTNList`。

#### 16.3.2 T_BUFFER 计算

`T_BUFFER` 与 `t_buffer` 为同一字段，正式统一为：

```text
T_BUFFER
```

含义：

```text
当前 Timeline、当前 STN 需要接收的 WIP 量
```

计算逻辑：

```text
IF FULL(LoadingGap) AND WIPLoading < WIPLoading_Avg
THEN WIPLoading_Avg - WIPLoading
ELSE IF FULL(FAB_LoadingSpec) AND WIPLoading < FAB_LoadingSpec
THEN FAB_LoadingSpec - WIPLoading
ELSE 0.0
```

#### 16.3.3 Priority T_BUFFER 计算

Priority Loading 缺口使用 `PriorWIPLoading` / `PriorWIPLoading_Avg` 计算。

```text
IF FULL(LoadingGap) AND PriorWIPLoading < PriorWIPLoading_Avg
THEN PriorWIPLoading_Avg - PriorWIPLoading
ELSE IF FULL(FAB_LoadingSpec) AND PriorWIPLoading < FAB_LoadingSpec
THEN FAB_LoadingSpec - PriorWIPLoading
ELSE 0.0
```

输出可记为：

```text
T_BUFFER_Pri
```

用于表示当前 Timeline、当前 STN 需要接收的 Priority WIP 量。

### 16.4 Candidate Lot 再过滤

为避免 Report 与当前 Lot 状态存在时间差，系统在选 Lot 前需对当站 Lot 再过滤。

满足以下任一条件时，Lot 不参与本轮 Candidate Lot 选择：

```text
CURSTEP_FULLSEQ_Cur != CURSTEP_FULLSEQ
OR LOTRUNCARD != LOTRUNCARD_Cur
OR (
  (
    EXTRASTATUS = 'WaitForJobIn'
    OR EXTRASTATUS = 'WaitForJobOut'
    OR EXTRASTATUS = 'WaitForTransport'
  )
  AND IsNPWLot = TRUE
)
OR (
  EXTRASTATUS = 'WaitForJobPrep'
  AND !IsNPWLot
)
OR In(LOTSTATE, 'Hold', 'CrossFabTransferred')
```

### 16.5 Candidate Lot 基础条件

Lot 需满足以下条件后，方可作为 `LoadingCandidateLot`：

1. `IsTransferCandidate = TRUE`。
2. Lot 通过 Transfer 检查。
3. Lot 通过 TargetFab 检查。
4. Lot 在对厂存在可作业 STN。
5. Lot 的对厂 `AvailableSTNChamberList` 包含当前低 Loading STN。
6. Lot 未被本轮选中过。

其中 `IsCandidateChecked` 表示该 Lot 通过 Transfer / TargetFab / AvailableSTN 检查，且选中后不会导致其他机台 Loading 降至低 Loading 水平以下。

### 16.6 ReceiveSTNCnt

`ReceiveSTNCnt` 表示该 Lot 在对厂可匹配的低 Loading STN 数量。

用途：

```text
Candidate Lot 排序
```

排序原则：

```text
ReceiveSTNCnt 越小越优先
```

原因：

可匹配低 Loading STN 越少，Lot 可选择空间越小，应优先处理。

### 16.7 Candidate Lot 选择循环

#### 16.7.1 第一重循环：按 STN + Timeline 检查

系统按低 Loading STN 与 Timeline 执行第一重循环。

排序原则：

```text
By Timeline 小
By T_BUFFER_Pri 大
By T_BUFFER 大
By Fab / Timeline / STN / T_BUFFER_Pri / T_BUFFER 编号
```

说明：

1. 循环按照机台和 Timeline 从小到大执行。
2. 当前 Timeline 的 Candidate Lot 范围不能只包含本 Timeline 的 Lot，也需包含本 Timeline 之前的 Lot。
3. 例如 12 小时 Loading 包含 6 小时 Loading，因此检查 12 小时层级时，6 小时内到站的 Lot 也会影响该层级 Loading。
4. 选 Lot 时仍优先选择与当前 Timeline 更接近的 Lot。

#### 16.7.2 第二重循环：每个 STN + Timeline 一次选一个 Lot

在每个 STN + Timeline 下，每次只选择一个 Lot。

原因：

一次选择多个 Lot 时，多个 Lot 同时更新 Loading 会导致影响难以判断；逐 Lot 选择可保证每次选择后均能重新计算 Loading。

#### 16.7.3 退出条件

满足以下任一条件时，退出当前选择循环：

```text
IsPriorityCheckFinished = TRUE
OR IsCheckFinished = TRUE
OR transfercnt 达到 TransferLotCountLimit
OR 从近到远检查超过 100 个 lot
```

其中：

```text
IsPriorityCheckFinished = T_BUFFER_Pri <= 0
IsCheckFinished         = T_BUFFER <= 0
```

`TransferLotCountLimit` 按 `SelfCapabilityGroup` 计数。

`从近到远检查超过 100 个 lot` 固定使用 100，不做参数化。

### 16.8 Candidate Lot 排序

Candidate Lot 基础筛选条件：

```text
!IsToDispatch
AND IsCandidateChecked
AND Timeline_checking >= Timeline
AND STN = STN_checking
```

若 Priority Loading 尚未满足，则优先保留 Priority Lot：

```text
(!IsPriorityCheckFinished AND IsPriorityLot)
OR IsPriorityCheckFinished
```

排序逻辑：

```text
MIN(Timeline_checking - Timeline)
MIN(ReceiveSTNCnt)

IF IsPriorityCheckFinished = FALSE
THEN:
    PIECES >= T_BUFFER_Pri
    MIN ABS(PIECES - T_BUFFER_Pri)

IF IsPriorityCheckFinished = TRUE
THEN:
    PIECES >= T_BUFFER
    MIN ABS(PIECES - T_BUFFER)

MIN RTDRank
```

解释：

1. 优先选择与当前检查 Timeline 最接近的 Lot。
2. 优先选择可匹配低 Loading STN 数量较少的 Lot。
3. Priority Loading 未满足时，优先选择片数更接近 `T_BUFFER_Pri` 的 Priority Lot。
4. Priority Loading 已满足后，选择片数更接近普通 `T_BUFFER` 的 Lot。
5. 最后按 `RTDRank` 排序。

### 16.9 选中 Lot 后的片数更新

当 Lot 被选中后，更新该 Lot 在各 STN 上的分配片数：

```text
IF IsSelectedLot AND STN_checking == STN
THEN Real(PIECES)
ELSE IF IsSelectedLot AND STN_checking != STN
THEN 0.0
ELSE PiecesPerStation
```

含义：

1. 被选中的 Lot 只分配给当前低 Loading STN。
2. 被选中的 Lot 在其他 STN 上的分配片数改为 0。
3. 未被选中的 Lot 保持原 `PiecesPerStation`。

### 16.10 试算与 Loading 更新

#### 16.10.1 更新对象

Lot 被选中后，系统需拿取该 Lot 的所有相关机台，从 `LotSummary` 获取相关机台 Loading 信息，并重新计算：

```text
WIPLoading
PriorWIPLoading
```

#### 16.10.2 更新范围

Loading update 需包含该 Lot Timeline 之后的所有相关机台。

例如：

```text
Lot Timeline = 10
```

则选中该 Lot 后，需更新：

```text
所有 Timeline >= 10 的相关机台 Loading
```

`IsToDispatch` 只有该 Lot 当前 Timeline 是更新的，因此需要增加本次是否需要更新后续 Timeline Loading 的全局标识，避免只更新当前 Timeline 后，后续判断仍使用旧 Loading。

#### 16.10.3 试算检查范围

试算时只检查：

```text
timeline <= timeline_checking
```

原因：

后续更大的 Timeline 仍会在后续循环中继续调整；当前选择需优先保证当前及更近 Timeline 的 Loading 满足。

#### 16.10.4 是否可 Transfer 判断

选中 Lot 前，需试算该 Lot 从其他机台转移到当前低 Loading STN 后，对其他机台 Loading 的影响。

检查原则：

1. 检查对象为其他机器，不包含当前低 Loading STN。
2. 当前低 Loading STN 因接收 Lot，Loading 必然增加，不作为减少风险检查对象。
3. 其他候选机台因该 Lot 被移走，Loading 会减少，需确认减少后仍满足 `FAB_LoadingSpec` 或 `WIPLoading_Avg` 相关要求。
4. 若试算 OK，则该 Lot 可作为 Transfer Candidate。
5. 若试算不 OK，则继续检查下一 Candidate Lot。

#### 16.10.5 Priority / Normal Lot 检查规则

若当前正在检查 Priority Loading：

```text
选中条件：Priority Loading OK
```

若 Lot 为 Priority Lot，但当前检查普通 Loading：

```text
选中条件：Priority Loading OK 且普通 Loading OK
```

若 Lot 为普通 Lot：

```text
选中条件：普通 Loading OK
```

### 16.11 输出结果

`LoadingCandidateLot` 最终需输出可用于后续 Dispatch / Transfer 判断的 Candidate Lot。

建议保留以下信息：

| 字段 | 含义 |
| --- | --- |
| `Lot` | 候选 Lot |
| `STN` | 目标低 Loading 机台 |
| `Timeline` | 当前检查 Timeline |
| `Fab` | Lot 当前厂别 |
| `TargetFab` | 目标厂别 |
| `IsPriorityLot` | 是否 Priority Lot |
| `T_BUFFER` | 当前 STN 普通 Loading 需接收 WIP 量 |
| `T_BUFFER_Pri` | 当前 STN Priority Loading 需接收 WIP 量 |
| `ReceiveSTNCnt` | Lot 可匹配低 Loading STN 数量 |
| `RTDRank` | RTD 排序结果 |
| `IsToDispatch` | 是否选中为本轮 Dispatch / Transfer Candidate |

# 二、原逻辑与现逻辑对比

## 1. 原逻辑

原 LoadingBalance 以 SelfCapability 作为 Loading 均衡对象，机台组拿取方式为 WIP 可作业机台并集。计算结果主要体现机台组整体负荷，无法准确体现 SelfCapability 内每台机台的负荷差异。

原 LoadingCandidateLot 主要基于既有 Loading 维度判断低 Loading 与 Candidate Lot，无法直接使用 STN 维度 Loading 结果判断某一台机台是否需要接收 WIP，也无法逐 STN / Timeline 试算选 Lot 后对其他机台 Loading 的影响。

## 2. 现逻辑

现逻辑改为以 STN / 机台维度计算 Loading：

1. 获取 Lot 在各站点的可作业机台。
2. 按配置 Timeline 层级划分 Lot。
3. 使用 WaferBalance 方法计算每台机台的单厂 Loading。
4. 筛选 `isprioritylot = T` 的 Lot，额外单独计算 Priority Lot 单厂 Loading。
5. 使用两厂 Lot 和两厂可作业机台计算平均 Loading。
6. 筛选两厂 `isprioritylot = T` 的 Lot，额外单独计算 Priority Lot 平均 Loading。
7. 输出 `EqpLoadingSummary` 与 `EqpLotSummary`。

同时修改 `LoadingCandidateLot`：

1. 从 `EqpLoadingSummarybyEqp` 获取 STN 维度 Loading。
2. 按 `LoadingSettingINFO` 中 `isBySTN=True` 的配置判断低 Loading STN。
3. 使用 `T_BUFFER` 表示当前 STN / Timeline 需要接收的 WIP 量。
4. 按 STN + Timeline 循环挑选可 Transfer Candidate Lot。
5. Candidate Lot 选择前需执行当前状态再过滤、Transfer 检查、TargetFab 检查、AvailableSTN 检查。
6. 每次只选择一个 Lot，选中前需试算对其他相关机台 Loading 的影响。
7. 选中后更新该 Lot Timeline 及之后相关机台的 `WIPLoading` / `PriorWIPLoading`。

## 3. 修改原因

不同 Lot、不同产品在 release 机台、跨厂可作业条件、PM 状态、QZone 管控上存在差异。按 SelfCapability 整体计算 Loading 会导致部分机台结果与实际不一致。改为机台维度后，可更准确反映每台机台负荷，为后续 transfer 选 Lot 提供基础。

LoadingCandidateLot 同步改为 STN 维度后，可避免只看机台组整体 Loading 导致低 Loading 机台无法被准确补偿的问题。通过逐 Lot 试算，可降低选中 Lot 后造成其他机台 Loading 不满足的风险。

# 三、已确认事项

以下事项已于 v1.1 确认闭环：

1. `MFGControl` 完全沿用既有逻辑，不新增判断条件。
2. `Important Lot` 配置文件为 `ImportantLotConfig.csv`，与 RTDConfig 同目录维护，字段格式见 3.3 节。
3. `PW Lot 后续 50 站` 的 50 为代码写死，不做参数化。
4. `EqpLoadingSummary` 与 `EqpLotSummary` 的 `CreateTime` 取整个 Report Job 开始时间。
5. `IsCandidateChecked` 表示该 Lot 通过 Transfer / TargetFab / AvailableSTN 检查，且选中后不会导致其他机台 Loading 降至低 Loading 水平以下。

# 四、审批意见区

| 审批项 | 意见 / 日期 |
| --- | --- |
| 申请部门意见 |  |
| 申请部门分管领导意见 |  |
| 相关部门意见 |  |
| 相关部门分管领导意见 |  |
| 信息技术部意见 |  |
| 信息技术部分管领导意见 |  |
| 附件名称 |  |
