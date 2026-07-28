# WPHLoss

> 来源：`00.raw-materials/10.sources/images/WPHLoss/1.jpg` ~ `00.raw-materials/10.sources/images/WPHLoss/4.jpg`。  
> 作用范围：QZone 获取机台 WPH 后，对复合机台 / chamber 缺失造成的实际产能损失进行修正。

## 定位

WPHLoss 是 QZone 中用于修正机台实际 WPH 的逻辑。它解决的问题是：复合机台不同 chamber 缺失时，产能损失比例不同，若仍使用原始 WPH，会高估下游产能，导致 Q-time Loop 放货过多，增加 Over Q-time 风险。

示例：

```text
BMCUBA01-1234CDEF
CUBA01-12 Loss = 15%
CUBA01-34 Loss = 25%
CUBA01-CD Loss = 50%
CUBA01-EF Loss = 50%
```

## 输入信息

QZone 原本按 `capability / machinename / recipe` 从 `vw_dsp_capabilitywph` 取得：

- `wph`
- `isengcontrol`
- `engpriority`

WPHLoss 需求中新增或额外关注：

- `ProcessGroup`
- `WPHLossControl`
- `Lotid`
- `capability`
- `stepseq`
- `stn`
- `recipe`
- `ppid`
- `chamberflow`

其中：

- 若 `stn` 包含 `-`，取 `-` 前的部分作为主机台 `EQPID`。
- 若 `stn` 不包含 `-`，则 `EQPID = STN`。

## 是否需要计算 WPHLoss

按 `Lot / stepseq / EQPID` 分组判断。

同组内若可作业 `STN` 具备相同且非空的 `ProcessGroup`，并且 `WPHLossControl = Y`，则该 Lot 在该主机台需要计算 WPHLoss。

否则不做 WPHLoss 修正，沿用原 WPH。

## chamberflow 拆分逻辑

对需要计算 WPHLoss 的 Lot，取得：

- `Lot`
- `stepseq`
- `Capability`
- `EQPID`
- `ProcessGroup`
- `ChamberFlow`

并去重。

`chamberflow` 拆分规则：

1. 先按 `;` 拆分不同 PPID 的 chamber group。
2. 再按 `,` 拆分单个 chamber。
3. 去重后得到该 Lot 在该机台的可用 chamber 清单。

示例：

```text
STN1,STN2;STN1,STN3
```

拆分后得到：

```text
STN1
STN2
STN3
```

## 缺失 chamber 数计算

从 `mfgcim.tb_dsp_wphloss` 取得维护信息。

匹配字段：

- `Capability`
- `ProcessGroup`
- `Machine`
- `STN`

取得：

- `SubeqpStateGroup`：同类型 chamber 分组。
- `SameGroupCount`：该分组应有 chamber 数。

对 Lot 当前可用 chamber 按 `SubeqpStateGroup` 统计：

```text
ActualCount = 当前 Lot 在该 SubeqpStateGroup 的可用 chamber 数
CountGap = SameGroupCount - ActualCount
```

## Loss 计算

按以下字段回表 `tb_dsp_wphloss` 匹配 Loss：

- `Capability`
- `ProcessGroup`
- `Machine`
- `SubeqpStateGroup`
- `Count`

其中 `Count = CountGap`。

若未匹配到维护值，则默认：

```text
Loss = 0
```

若一个 Lot 在同一机台涉及多个 `SubeqpStateGroup`，最终取：

```text
WPHLoss = Max(各 SubeqpStateGroup Loss)
```

## WPH 修正

先确定机台总 WPH：

```text
Total STN WPH = sum(ChamberWPH) 或 STN WPH
```

- 若 WPH 按整机维护，则 `Total STN WPH` 为整机 WPH。
- 若 WPH 按 chamber 维护，则 `Total STN WPH` 为各 chamber WPH 加总。
- 维护粒度可细到 `Capability & Recipe`。

计算实际机台 WPH：

```text
Actual STN WPH = Total STN WPH × (1 - WPHLoss)
```

若 WPH 按整机维护：

```text
WPH = Actual STN WPH
```

若 WPH 按 chamber 维护：

```text
Chamber Ratio = 该 chamber WPH / sum(该产品可作业 chamber WPH)
Chamber WPH = Chamber Ratio × Actual STN WPH
```

## 对 QZone / WaferBalance 的影响

WPHLoss 发生在 QZone 获取 WPH 后、后续产能判断前。

因此，后续使用 WPH 的逻辑都应使用修正后的实际 WPH，包括：

- QZone 下游产能评估。
- WaferBalance 第一次 Balance 按 WPH 比例分配 Lot qty。
- 后续 Loading / Over Q-time 风险判断。

## 风险点

- `ProcessGroup` 为空或同组不一致时，不应误触发 WPHLoss。
- `chamberflow` 中 `;` 和 `,` 的拆分、去重必须正确。
- 缺失 Loss 维护时应默认 `0`，避免空值影响计算。
- 多 `SubeqpStateGroup` 时取最大 Loss，而不是累加。
- 整机 WPH 与 chamber WPH 的修正方式不同。

## 待确认

- `tb_dsp_wphloss` 的完整字段定义、主键和生效/失效规则。
- `vw_dsp_capabilitywph` 中 `ProcessGroup`、`WPHLossControl` 的来源。
- WPHLoss 与 Engineer Control / Priority 的先后关系。
