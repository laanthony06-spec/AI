# Litho Auto Split Pirun 物理分批优化需求单 v0.2

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 编号 | 由信息技术部填写 |
| 类别 | ☑3. 功能开发 |
| 申请部门 | 制造部 |
| 系统名称 | CIM 计算机集成制造系统 Fab6（二科） |
| 申请人员 | 温浩奇 |
| 功能模块 | 智能派工系统（RTD/DSP/AMA） |
| 申请日期 | 2026-07-09（待确认） |
| 希望交付期 | 待确认 |
| 需求项目 | R2R Auto Split Pirun 物理分批功能优化 |
| 涉及范围 | FAB6 / FAB8、RTD Report、AMA 分批接口、MES Split 逻辑、R2R Pilot 传参 |
| 需求类型 | 逻辑优化 |

## 项目简介和必要性分析

### 项目背景

当前 Litho Auto Split Pirun 已由 RTD 选择符合条件的 Lot，并输出 Report 给 AMA 执行分批；AMA 将分出的子 Lot 作为 Pilot 传给 R2R。

现有分批为逻辑分批：MES 中拆出子 Lot，但晶圆仍在同一 FOUP 内。现场需要 Pilot 晶圆实际拆出并形成独立 FOUP，保证 R2R Pilot 状态与 FOUP 物理状态一致。

### 存在问题

1. 逻辑分批后，子 Lot 已在 MES 中生成，但晶圆仍在原 FOUP 内，未形成独立 FOUP。
2. R2R 接收到的 Pilot 子 Lot 与现场 FOUP 实体状态不一致，后续搬送、派工及作业确认存在异常风险。
3. 若候选 Pilot Lot 所在 FOUP 内已有带 SortJobid 的 Lot，继续选该 FOUP 内 Lot 作为 Pilot，可能与既有 SortJob 任务冲突。

### 需求目标

1. AMA AutoSplitPirun 执行分批时，由逻辑分批调整为物理分批。
2. 物理分批后，新分出的子 Lot 形成独立 FOUP。
3. 新分出的子 Lot 作为 Pilot 传给 R2R，保持与原逻辑的 Pilot 传参对象一致。
4. RTD 选择 Pilot 时，增加同 FOUP SortJobid 判断；若同 FOUP 内存在 SortJobid 不为空的 Lot，则该候选 Lot 不选作 Pilot。

## 项目投资方案比较及效果分析

### 改善方案

1. RTD 在 Pilot 选择前增加 SameFoupSortJob 判断。
2. AMA 分批方式由逻辑分批改为物理分批。
3. MES 物理分批成功后返回新子 Lot 及独立 FOUP 信息。
4. AMA 将新子 Lot 作为 Pilot 传给 R2R。
5. 分批失败时记录 MES 返回原因；FutureMerge 失败沿用既有 AutoHold 逻辑。

### 效果分析

1. Pilot 子 Lot 与独立 FOUP 对应，减少 R2R 状态与现场实体状态不一致问题。
2. 降低同 FOUP 内 SortJob 任务与 AutoSplitPirun 分批任务冲突风险。
3. 减少逻辑分批后仍需人工处理实体 FOUP 拆分的等待。
4. 降低 Pilot 未及时形成独立 FOUP、后续无法按预期派工导致的 OQT 风险。

## 需求流程图

```text
RTD 获取 AutoSplitPirun 候选 Lot
  ↓
取得候选 Lot 所在 FOUP 及同 FOUP 内 Lot
  ↓
判断同 FOUP 内是否存在 SortJobid 不为空的 Lot
  ├─ 是：候选 Lot 不选作 Pilot
  └─ 否：继续进入原 Pilot 选择逻辑
  ↓
RTD 输出 Report 给 AMA
  ↓
AMA 执行分批前校验
  ↓
调用 MES 物理分批
  ↓
判断是否生成新子 Lot 及独立 FOUP
  ├─ 是：新子 Lot 作为 Pilot 传给 R2R
  └─ 否：不传 Pilot，记录失败原因
```

# 一、RTD 部分更改逻辑

## 1. 同 FOUP SortJobid 判断

### 1.1 数据获取

RTD 在候选 Lot 进入 Pilot 选择前，增加同 FOUP Lot 信息获取。

| 数据项 | 获取方式 | 说明 |
| --- | --- | --- |
| 候选 Lot 所在 FOUP | 通过候选 Lot 当前 Carrier / FOUP 信息获取 | 用于定位同 FOUP 范围 |
| 同 FOUP Lot 清单 | 根据候选 Lot 所在 FOUP 获取该 FOUP 内全部 Lot | 用于检查是否已有 SortJob 任务 |
| SortJobid | 获取同 FOUP 内各 Lot 的 SortJobid | 数据来源表及字段名待 IT 确认 |

### 1.2 判断逻辑

新增 `SameFoupHasSortJobFlag`：

```text
若候选 Lot 所在 FOUP 内存在任意 Lot 的 SortJobid 不为空，
则 SameFoupHasSortJobFlag = T；
否则 SameFoupHasSortJobFlag = F。
```

### 1.3 Pilot 选择逻辑

在候选 Lot 进入 Pilot 选择前增加过滤：

```text
若 SameFoupHasSortJobFlag = T，则该候选 Lot 不允许作为 Pilot；
若 SameFoupHasSortJobFlag = F，则继续进入原 Pilot 选择逻辑。
```

该逻辑为过滤逻辑，不作为排序降级逻辑。即同 FOUP 内存在 SortJobid 时，该候选 Lot 直接剔除。

### 1.4 示例

| FOUP | 候选 Lot | 同 FOUP Lot | SortJobid | 判断结果 |
| --- | --- | --- | --- | --- |
| F001 | LOTA | LOTA | 空 | 继续判断 |
| F001 | LOTA | LOTB | SJ001 | LOTA 不选作 Pilot |
| F002 | LOTC | LOTC | 空 | 继续判断 |
| F002 | LOTC | LOTD | 空 | LOTC 可参与 Pilot 选择 |

## 2. Report 输出

原 Report `Central_GetLithoR2RAutoPirunInfo` 继续供 AMA 读取执行。

建议新增以下追溯字段：

| 栏位 | 说明 |
| --- | --- |
| SameFoupHasSortJobFlag | 同 FOUP 内是否存在 SortJobid 不为空的 Lot |
| SameFoupSortJobLot | 同 FOUP 内带 SortJobid 的 Lot |
| SameFoupSortJobid | 同 FOUP 内存在的 SortJobid |

正常情况下，`SameFoupHasSortJobFlag = T` 的候选 Lot 不输出给 AMA。上述字段用于 Report 追溯或异常排查。

# 二、AMA 部分更改逻辑

## 1. 分批方式调整

### 1.1 原分批方式

原 AMA 分批为逻辑分批：

```text
MES 中拆出子 Lot；
晶圆仍在原 FOUP 内；
分出的子 Lot 作为 Pilot 传给 R2R。
```

### 1.2 新分批方式

AMA 分批调整为物理分批：

```text
MES 中拆出子 Lot；
Pilot 晶圆实际从原 FOUP 中拆出；
新分出的子 Lot 形成独立 FOUP；
新子 Lot 作为 Pilot 传给 R2R。
```

## 2. 分批前校验

AMA 读取 RTD Report 后，执行 MES 物理分批前保留既有校验：

1. Lot 厂别校验：Lot 属于 FAB6 或 FAB8。
2. Lot 状态校验：Lot 当前状态为 `WaitForJobPrep`，且当前站点 `runcardid` 为空。
3. Capability 校验：Lot 当前 Capability 为 `LithoCapability` 或 Barc 对应 Capability。
4. Carrier 类型校验：`CarrierKind = FOUP`。
5. Wafer 校验：Report 中选中的 Wafer 存在于该 Lot 中。

校验不通过时，不调用物理分批。

## 3. 物理分批执行

AMA 调用 MES 分批逻辑时，需指定本次 AutoSplitPirun 为物理分批。

接口名称、参数名及参数值待 IT 确认。需求语义如下：

| 参数语义 | 说明 |
| --- | --- |
| SplitMode | 分批模式，取值为 Physical / 物理分批 |
| SourceLot | 原 Lot |
| SplitWaferList | RTD Report 选出的 Pilot Wafer |
| TargetCarrierRequired | 是否要求独立 FOUP，取值为 True |
| RequestSource | 请求来源，标识为 AMA AutoSplitPirun |

若不新增 UI 开关，AutoSplitPirun 默认执行物理分批；若需保留逻辑分批 / 物理分批切换，需另行确认配置项。

## 4. 物理分批结果校验

MES 返回成功后，AMA 校验以下结果：

1. MES 返回新子 LotID。
2. 新子 Lot 对应 Wafer 与 Report 选定 Wafer 一致。
3. 新子 Lot 已绑定独立 FOUP。
4. 新子 Lot 与原 Lot 不在同一 FOUP。
5. 新子 Lot 状态满足 R2R Pilot 传参要求。

若 MES 返回成功但新子 Lot 未形成独立 FOUP，则本次 AutoSplitPirun 视为物理分批异常，不传 Pilot 给 R2R，并记录异常原因。

## 5. Pilot 传给 R2R

物理分批成功后，AMA 将 MES 返回的新子 Lot 作为 Pilot 传给 R2R。

```text
若 MES 物理分批成功，且新子 Lot 已形成独立 FOUP，
则 AMA 将新子 LotID 作为 Pilot 传给 R2R；
否则不传 Pilot，并记录失败原因。
```

R2R 侧接收对象保持原逻辑：仍接收分批后的子 Lot 作为 Pilot。

## 6. 分批失败处理

### 6.1 FutureMerge 失败

若 MES 返回分批失败，且失败原因包含 `FutureMerge`，沿用既有 AutoHold 逻辑：

```text
R2R Auto Split Execute Fail, Because Of FutureMerge
```

### 6.2 非 FutureMerge 失败

物理分批失败且失败原因不包含 FutureMerge 时：

1. AMA 不传 Pilot 给 R2R。
2. AMA 记录 MES 返回失败原因。
3. 是否自动 Hold Lot 待制造 / IT 确认。

建议失败原因保留原始返回信息，便于区分 FOUP 不足、Carrier 异常、MES Split 失败、AMHS 搬送异常等场景。

## 7. AMA 日志 / Report 记录

建议 AMA 记录以下栏位：

| 栏位 | 说明 |
| --- | --- |
| SourceLot | 原 Lot |
| ChildLot | 物理分批后新子 Lot |
| SourceFOUP | 原 FOUP |
| ChildFOUP | 新子 Lot 所在独立 FOUP |
| SplitMode | Physical |
| SplitWaferList | 本次分出的 Pilot Wafer |
| SplitResult | Success / Fail |
| FailReason | MES 返回失败原因 |
| R2RSendFlag | 是否已传给 R2R |

# 三、待确认事项

| 序号 | 待确认项 | 影响范围 |
| --- | --- | --- |
| 1 | SortJobid 的具体数据来源、表名、字段名 | RTD 同 FOUP SortJobid 判断 |
| 2 | 同 FOUP Lot 清单获取方式及 Carrier / FOUP 关系表 | RTD Pilot 过滤 |
| 3 | MES 物理分批接口名称、参数名及成功返回字段 | AMA 物理分批 |
| 4 | 物理分批是否需要新增 UI 开关，或 AutoSplitPirun 默认全部执行物理分批 | AMA 配置 |
| 5 | 非 FutureMerge 的物理分批失败是否需要 AutoHold | 异常处理 |
| 6 | 物理分批失败时是否需要通知工程部 / 制造部 | 异常闭环 |

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
