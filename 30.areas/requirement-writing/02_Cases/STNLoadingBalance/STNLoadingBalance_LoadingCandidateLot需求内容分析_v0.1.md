# STNLoadingBalance - LoadingCandidateLot 修改需求内容分析 v0.1

来源：`STNLoadingBalance图片内容提取稿_v0.1.md` 中第二部分零散逻辑  
范围：仅整理 `LoadingCandidateLot 修改`，不改第一部分 `EqpLoadingSummary / EqpLotSummary Report 输出修改`

---

## 1. 对整体需求的理解

本需求分为两部分：

1. `EqpLoadingSummary / EqpLotSummary Report 输出修改`
   - 这一部分是已写好的核心 Loading 计算逻辑。
   - 目标是将原本按 `SelfCapability` 维度计算的 Loading，改为按 `STN` 机台维度计算。
   - 输出 `EqpLoadingSummary` 和 `EqpLotSummary`，供后续 LoadingCandidateLot 选 Lot 使用。

2. `LoadingCandidateLot 修改`
   - 这一部分不是重新计算 Loading，而是使用第一部分产出的机台维度 Loading 结果，找出低 Loading 机台，并选择合适的 Lot 作为 Transfer / Dispatch candidate。
   - 核心目标是：在满足 transfer、target fab、可作业机台、timeline、priority loading、normal loading 等条件下，优先挑选能够改善对厂低 Loading 的 Lot。

---

## 2. LoadingCandidateLot 修改目标

原 LoadingCandidateLot 逻辑主要基于既有 Loading 维度判断候选 Lot。本次改为引用 STN 维度的 Loading 结果：

- 从 `EqpLoadingSummarybyEqp` 取得机台维度 Loading。
- 从 `EqpLotSummaryByEqp` / `LoadingMidLog` 取得 Lot 与机台 Loading 分配关系。
- 根据 UI 配置、Loading Gap / Fab Loading Spec、Priority Loading、Timeline 等条件，判断哪些 STN 属于低 Loading 机台。
- 对低 Loading STN 逐个挑选可 transfer 的 Lot。
- 每挑选一个 Lot 后，需要试算该 Lot 对相关机台后续 Timeline Loading 的影响，确认不会造成其他机台 Loading 不满足后，才可选中。

一句话：

> LoadingCandidateLot 需从“找低 Loading 机台”升级为“基于 STN 维度 Loading，逐机台、逐 Timeline、逐 Lot 试算后选择可 Transfer Lot”。

---

## 3. 数据输入

### 3.1 配置来源

从 UI 表 `LoadingSettingINFO` 获取 `isBySTN=True` 的配置。

需使用的配置维度包括：

```text
STN
QTLimit
SelfCapabilityGroup
LotAttribute
TargetFABS
LoadingGap
Fab_LoadingSpec
TransferLotCountLimit
```

规则：

- 筛选 `SelfCapabilityGroup` 中 `Timeline <= QLimit` 的机台与 Timeline。
- 每个 Timeline 使用最近的 QLimit 配置。
- 若同一 STN 命中多个配置，例如多个 SelfCapabilityGroup，需要处理到唯一配置。

### 3.2 Loading 来源

从 `EqpLoadingSummarybyEqp` 获取 STN 维度 Loading 信息：

```text
STN
SITE / Fab
Timeline
WIPLoading
WIPLoading_allFab / WIPLoading_Avg
PriorWIPLoading
PriorWIPLoading_allFab / PriorWIPLoading_Avg
```

字段命名需以后续正式口径统一。

### 3.3 Lot 来源

从 `EqpLotSummaryByEqp BY FULL_STEPSEQ \ LOT` 取得 Lot 与机台分配关系。

从 `LoadingMidLog` 取得低 Loading 机台相关 Lot 信息，包括：

```text
IsTransferCandidate
Fab
Fab_t
IsPriorityLot
RTDRank
TransferLotCountLimit
```

同时需沿用第一部分 Loading 计算中的 Lot 获取逻辑，包括：

- Transfer 检查
- TargetFab 检查
- 对厂 `AvailableSTNChamberList` 判断
- `AvailableSTNChamberList` 需包含低 Loading STN / Receive STN

---

## 4. 低 Loading STN 判断

### 4.1 ReceiveLoading / Reserveeqp 判断

当 STN 满足以下任一条件时，视为可接收 Loading 的低 Loading 机台：

```text
IF (
    Full(LoadingGap)
    AND MAX(0, WIPLoading_Avg - LoadingGap) >= WIPLoading
)
OR
(
    FULL(Fab_LoadingSpec)
    AND WIPLoading <= Fab_LoadingSpec
)
THEN ReceiveLoading
```

理解：

- 若配置了 `LoadingGap`，则用两厂平均 Loading 与当前 STN Loading 的差异判断是否低 Loading。
- 若配置了 `Fab_LoadingSpec`，则用当前 STN Loading 是否低于 Spec 判断。
- 满足条件的 STN 进入 `ReceiveSTNList`。

### 4.2 LackLoading / t_buffer 计算

普通 Loading 缺口计算：

```text
IF FULL(LoadingGap) AND WIPLoading < WIPLoading_allFab
THEN WIPLoading_allFab - WIPLoading
ELSE IF FULL(FAB_LoadingSpec) AND WIPLoading < FAB_LoadingSpec
THEN FAB_LoadingSpec - WIPLoading
ELSE 0.0
```

另有一段 `T_BUFFER` 逻辑：

```text
IF FULL(LoadingGap)
THEN WIPLoading_allFab - LoadingGap - WIPLoading
ELSE IF FULL(FAB_LoadingSpec)
THEN FAB_LoadingSpec - WIPLoading
ELSE WIPLoading_allFab - WIPLoading
```

这两段疑似分别用于：

- `T_BUFFER`：原始缺口 / 排序或中间判断。
- `t_buffer`：实际可补 Loading 缺口，负值归 0。

需确认两者最终字段含义是否都保留。

### 4.3 Priority Loading 缺口计算

Priority Loading 缺口计算：

```text
IF FULL(LoadingGap) AND PriWIPLoading < PriWIPLoading_allFab
THEN PriWIPLoading_allFab - PriWIPLoading
ELSE IF FULL(FAB_LoadingSpec) AND PriWIPLoading < PriFAB_LoadingSpec
THEN FAB_LoadingSpec - PriWIPLoading
ELSE 0.0
```

输出可理解为：

```text
LackLoadingPri / Pri_t_buffer
```

---

## 5. Candidate Lot 过滤

### 5.1 当站 Lot 再过滤

为避免 Report 与当前 Lot 状态存在时间差，需要对当站 Lot 再过滤。

满足以下任一条件的 Lot 需过滤：

```text
CURSTEP_FULLSEQ_Cur != CURSTEP_FULLSEQ
OR LOTRUNCARD != LOTRUNCARD_Cur
OR (
  (EXTRASTATUS = 'WaitForJobIn'
   OR EXTRASTATUS = 'WaitForJobOut'
   OR EXTRASTATUS = 'WaitForTransport')
  AND IsNPWLot = TRUE
)
OR (
  EXTRASTATUS = 'WaitForJobPrep'
  AND !IsNPWLot
)
OR In(LOTSTATE, 'Hold', 'CrossFabTransferred')
```

### 5.2 Transfer Candidate 判断

Candidate Lot 需满足：

- `IsTransferCandidate = TRUE`
- Lot 在对厂存在可作业 STN。
- Lot 的对厂 `AvailableSTNChamberList` 包含当前低 Loading STN。
- 通过 TargetFab 检查。
- 通过 Transfer 检查。

### 5.3 ReceiveSTNCnt

`ReceiveSTNCnt` 表示该 Lot 在对厂可匹配的低 Loading STN 数量。

该字段用于排序：

- 可作业低 Loading STN 越少，越优先。
- 原因：可选机台少的 Lot 更难匹配，应优先处理。

---

## 6. Candidate Lot 选择循环

### 6.1 第一重循环：按 STN + Timeline 检查

第一重循环按低 Loading 机台与 Timeline 执行。

排序建议：

```text
By Timeline 小
By LackLoadingPri 大
By LackLoading 大
By Fab / Timeline / STN / LackLoadingPri / LackLoading 编号
```

注意：

- 第一重循环虽然按当前 `Timeline_checking` 检查，但不能只看本 Timeline 下的 Lot。
- 因为例如 12 小时 Loading 包含 6 小时 Loading，所以当前 Timeline 的候选范围应包含本 Timeline 及之前 Timeline 的 Lot。
- 但挑 Lot 时仍应优先选择与当前 Timeline 更接近的 Lot。

### 6.2 第二重循环：每个 STN + Timeline 一次选一个 Lot

第二重循环用于在当前 STN + Timeline 下挑 Lot。

原则：

- 每个 capa / STN / Timeline 每次只选一个 Lot。
- 不一次选多个 Lot，避免难以判断多个 Lot 同时变更对 Loading 的影响。

### 6.3 退出条件

满足以下任一条件时退出：

```text
IsPriorityCheckFinished = TRUE
OR IsCheckFinished = TRUE
OR transfercnt 达到 TransferLotCountLimit
OR 从近到远检查超过 100 个 lot
```

其中：

```text
IsPriorityCheckFinished = LackLoadingPri <= 0
IsCheckFinished         = LackLoading <= 0
```

---

## 7. Candidate Lot 排序

候选 Lot 需满足基础条件：

```text
!IsToDispatch
AND IsCandidateChecked
AND Timeline_checking >= Timeline
AND STN = STN_checking
```

若当前尚未完成 Priority Loading 检查，则优先只保留 Priority Lot：

```text
(!IsPriorityCheckFinished AND IsPriorityLot)
OR IsPriorityCheckFinished
```

排序逻辑：

```text
MIN(Timeline_checking - Timeline)
MIN(receiveSTNCnt)

IF IsPriorityCheckFinished = FALSE
THEN:
    PIECES >= LackLoadingPri
    MIN ABS(PIECES - LackLoadingPri)

IF IsPriorityCheckFinished = TRUE
THEN:
    PIECES >= LackLoading
    MIN ABS(PIECES - LackLoading)

MIN RTDRank
```

解释：

1. 优先选择与当前检查 Timeline 最接近的 Lot。
2. 优先选择可接收 STN 数较少的 Lot。
3. 若 Priority Loading 未满足，优先选择片数更接近 `LackLoadingPri` 的 Priority Lot。
4. 若 Priority Loading 已满足，选择片数更接近普通 `LackLoading` 的 Lot。
5. 最后按 RTD Rank 排序。

---

## 8. 选中 Lot 后的片数更新

挑到 Lot 后，更新分配到机台的片数：

```text
IF IsSelectedLot AND STN_checking == STN
THEN Real(PIECES)
ELSE IF IsSelectedLot AND STN_checking != STN
THEN 0.0
ELSE PiecesPerStation
```

理解：

- 选中的 Lot 只分配给当前低 Loading STN。
- 该 Lot 在其他 STN 上的分配片数改为 0。
- 非选中 Lot 保持原 `PiecesPerStation`。

---

## 9. 试算与 Loading 更新

### 9.1 更新范围

选中 Lot 后，需拿取 `IsSelectedLot` 的所有机台，从 `lotsummary` 获取该 Lot 影响到的机台 Loading 信息，并重新计算：

```text
WIPLoading
PriorWIPLoading
```

只有该 Lot 的 Timeline 之后的所有相关机台 Loading 受影响。

例如：

```text
lot timeline = 10
```

则选中后影响：

```text
所有 timeline >= 10 的 loading
```

### 9.2 检查范围

试算时只检查：

```text
timeline <= timeline_checking
```

原因：

- 后续更大的 Timeline 仍有机会通过之后循环继续调整。
- 当前应优先保证更近 Timeline 的 Loading 满足。

### 9.3 是否可 Transfer 判断

试算时需检查：去掉该 Lot 后，其他候选机台在相关 Timeline 的 Loading 是否仍满足 Spec 或 `WIPLoading_allFab`。

注意：

- 检查对象应为其他机器，不包含当前 Receive STN。
- 因为无论怎么选，Receive STN 都是增加 Loading；真正需要防止的是其他候选机台因该 Lot 被拿走后 Loading 下降过多。

### 9.4 Priority / Normal Lot 检查差异

若当前是 Priority Loading 检查：

- 选中条件需要 Priority Loading OK。

若 Lot 是 Priority Lot，但当前检查的是普通 Loading：

- 选中条件需要 Priority Loading 和普通 Loading 都 OK。

若 Lot 是普通 Lot：

- 选中条件为普通 Loading OK。

---

## 10. 全局更新标识

图片最后说明：

因为 Loading update 需要包含该 Lot Timeline 之后的所有相关机台。

但 `IsToDispatch` 只对该 Lot 当前 Timeline 生效。

因此需要新增或总结一个全局变量，用于表示此次选中 Lot 后是否需要更新后续 Timeline 相关机台 Loading。

建议需求中表达为：

> 当 Lot 被选中为 Transfer Candidate 后，需建立本次选择的 Loading Update 标识，并基于该 Lot 的 Timeline，更新所有相关机台在该 Timeline 及之后层级的 WIPLoading / PriorWIPLoading，避免仅更新当前 Timeline 导致后续判断使用旧 Loading。

---

## 11. 建议写入需求单的内容结构

建议 `LoadingCandidateLot 修改` 章节按以下结构撰写：

```text
2. LoadingCandidateLot 修改

2.1 修改范围
2.2 配置与数据来源
2.3 低 Loading STN 判断
2.4 Candidate Lot 获取与过滤
2.5 Candidate Lot 排序与选择
2.6 选中 Lot 后 Loading 试算
2.7 Loading 更新范围
2.8 输出结果
2.9 待确认事项
```

---

## 12. 待确认事项

1. `WIPLoading_allFab` 与 `WIPLoading_Avg` 是否为同一字段，正式名称需统一。
   是同一字段，统一为WIPLoading_Avg
2. `PriWIPLoading_allFab`、`PriorWIPLoading_Avg`、`PriWIPLoading`、`PriorWIPLoading` 命名需统一。
 PriWIPLoading_allFab和PriorWIPLoading_Avg是同一字段，统一为PriorWIPLoading_Avg，PriWIPLoading和PriorWIPLoading是同一字段，统一为PriorWIPLoading
3. `T_BUFFER` 与 `t_buffer` 是否都需要输出，还是一个为中间计算、一个为最终字段。
T_BUFFER 与 t_buffer是同一字段，表示Timeline、STN需接收的WIP量
4. `FAB_LoadingSpec` 与 `Fab_LoadingSpc` 是否为同一配置。
  是同一配置，统一为FAB_LoadingSpec
5. `从近到远检查超过 100 个 lot` 是否需要做成参数。
 无需
6. `TransferLotCountLimit` 是按 STN 计数、按 Fab 计数，还是本轮总计数。
 安照SelfCapabilityGroup计数
7. `IsCandidateChecked` 的具体含义需确认，是通过 Transfer / TargetFab / AvailableSTN 检查后的标识，还是还有额外条件。
未确认
8. 最后图片中 “istodispatch 只有这个 lot 当前 timeline 是需断的” 文字疑似不清，需确认准确含义。
istodispatch 只有这个 lot 当前 timeline 是更新的