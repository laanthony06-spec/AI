# Litho Auto Split Pirun 物理分批优化需求单 v0.3

> 本需求单仅描述本次新增 / 修改逻辑，不重复原 Litho Auto Split Pirun 全量逻辑。  
> 既有 FutureMerge Pilot 过滤、同母批同 Stage Pilot 唯一性判断逻辑继续沿用。

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 编号 | 由信息技术部填写 |
| 类别 | ☑3. 功能开发 |
| 申请部门 | 制造部 |
| 系统名称 | CIM 计算机集成制造系统 Fab6（二科） |
| 申请人员 | 温浩奇 |
| 功能模块 | 智能派工系统（RTD/DSP/AMA） |
| 申请日期 | 2026-07-10 |
| 希望交付期 | 待确认 |
| 需求项目 | R2R Auto Split Pirun 物理分批功能优化 |
| 涉及范围 | FAB6 / FAB8、RTD Report、Litho Auto Split Pirun、AMA 分批接口、MES Split |
| 需求类型 | 逻辑优化 |

## 项目简介和必要性分析

当前 Litho Auto Split Pirun 由 RTD 选择符合条件的 Lot，并输出 Report 给 AMA 执行分批；AMA 分批成功后，将分出的子 Lot 作为 Pilot 传给 R2R。

现行分批方式为逻辑分批，MES 中会生成子 Lot，但晶圆仍在原 FOUP 内，未形成独立 FOUP。现场希望 Pilot Lot 与实际 FOUP 状态保持一致，因此本次将 AMA AutoSplitPirun 分批方式由逻辑分批调整为物理分批。

同时，为避免候选 Pilot 所在 FOUP 内已有 SortJob 任务时继续触发 AutoSplitPirun，RTD 需新增同 FOUP SortJobid 判断。若候选 Lot 所在 FOUP 内任意 Lot 存在 SortJobid，则该候选 Lot 不允许作为 Pilot。

## 项目投资方案比较及效果分析

### 改善方案

1. RTD 在 Pilot 选择前新增同 FOUP SortJobid 判断。
2. 同 FOUP 内任意 Lot 存在 SortJobid 时，该 FOUP 内候选 Lot 不选作 Pilot。
3. AMA AutoSplitPirun 分批方式由逻辑分批改为物理分批。
4. 物理分批成功后，新分出的子 Lot 形成独立 FOUP，并作为 Pilot 传给 R2R。
5. 物理分批失败时，AMA 不传 Pilot，不执行 Hold，仅记录 MES 返回失败原因。

### 效果分析

1. Pilot 子 Lot 与独立 FOUP 对应，减少 MES Lot 状态与现场 FOUP 实体状态不一致问题。
2. 避免同 FOUP 内既有 SortJob 任务与 AutoSplitPirun 分批任务冲突。
3. 减少逻辑分批后仍需人工处理实体 FOUP 拆分的等待。
4. 降低 Pilot 未及时形成独立 FOUP，导致后续无法按预期 Pirun 的风险。

## 需求流程图

```text
RTD 获取 AutoSplitPirun 候选 Lot
  ↓
取得候选 Lot 所在 FOUP
  ↓
取得同 FOUP 内全部 Lot
  ↓
判断同 FOUP 内是否存在 SortJobid
  ├─ 是：该候选 Lot 不选作 Pilot
  └─ 否：继续原 Pilot 选择逻辑
  ↓
RTD 输出 Report 给 AMA
  ↓
AMA 读取 Report 并执行分批前校验
  ↓
调用 MES 物理分批
  ↓
物理分批是否成功？
  ├─ 否：不传 Pilot，不 Hold，记录失败原因
  └─ 是：校验新子 Lot 与独立 FOUP
          ↓
       新子 Lot 作为 Pilot 传给 R2R
```

# 一、RTD 部分修改逻辑

## 1. 同 FOUP SortJobid 判断

### 1.1 目的

避免候选 Pilot 所在 FOUP 内已有 SortJob 任务时，仍选择该 FOUP 内 Lot 作为 AutoSplitPirun Pilot。

### 1.2 数据获取

RTD 在候选 Lot 进入 Pilot 选择前，增加同 FOUP Lot 信息获取。

| 数据项 | 获取方式 | 说明 |
| --- | --- | --- |
| 候选 Lot 所在 FOUP | 通过候选 Lot 当前 Carrier / FOUP 信息获取 | 用于定位同 FOUP 范围 |
| 同 FOUP Lot 清单 | 根据候选 Lot 所在 FOUP 获取 FOUP 内全部 Lot | 用于检查是否已有 SortJob 任务 |
| SortJobid | 获取同 FOUP 内各 Lot 的 SortJobid | 数据来源表及字段名待 IT 确认 |

### 1.3 判断逻辑

新增判断结果 `SameFoupHasSortJobFlag`：

```text
IF 候选 Lot 所在 FOUP 内存在任意 Lot 的 SortJobid 不为空
THEN SameFoupHasSortJobFlag = T
ELSE SameFoupHasSortJobFlag = F
```

说明：

1. 判断范围为候选 Lot 当前所在 FOUP。
2. 同 FOUP 内包含候选 Lot 自身及其他 Lot。
3. 只要同 FOUP 内任意 Lot 的 SortJobid 不为空，即视为该 FOUP 已存在 SortJob 任务。

### 1.4 Pilot 选择规则

在候选 Lot 进入既有 Pilot 选择逻辑前增加过滤：

```text
IF SameFoupHasSortJobFlag = T
THEN 该候选 Lot 不允许作为 Pilot
ELSE 继续原 Pilot 选择逻辑
```

该逻辑为过滤逻辑，不作为排序降级逻辑。

即：

- `SameFoupHasSortJobFlag = T`：直接过滤，不选作 Pilot。
- `SameFoupHasSortJobFlag = F`：继续执行既有 FutureMerge、同母批同 Stage Pilot 唯一性等判断。

### 1.5 示例

| FOUP | 候选 Lot | 同 FOUP Lot | SortJobid | 判断结果 |
| --- | --- | --- | --- | --- |
| F001 | LOTA | LOTA | 空 | 继续原 Pilot 判断 |
| F001 | LOTA | LOTB | SJ001 | LOTA 不选作 Pilot |
| F002 | LOTC | LOTC | 空 | 继续原 Pilot 判断 |
| F002 | LOTC | LOTD | 空 | LOTC 可进入原 Pilot 选择逻辑 |

## 2. Report 输出

原 Report `Central_GetLithoR2RAutoPirunInfo` 继续供 AMA 读取执行。

正常情况下，`SameFoupHasSortJobFlag = T` 的候选 Lot 不输出给 AMA。为便于追溯，建议 Report 或 RTD Log 增加以下字段：

| 字段 | 说明 |
| --- | --- |
| SameFoupHasSortJobFlag | 同 FOUP 内是否存在 SortJobid 不为空的 Lot |
| SameFoupSortJobLot | 同 FOUP 内带 SortJobid 的 Lot |
| SameFoupSortJobid | 同 FOUP 内存在的 SortJobid |

字段是否输出到正式 Report，或仅记录在 RTD Log，由 IT 评估。

# 二、AMA 部分修改逻辑

## 1. 分批方式调整

### 1.1 原逻辑

AutoSplitPirun 现行分批方式为逻辑分批：

```text
MES 中生成子 Lot；
晶圆仍在原 FOUP 内；
分出的子 Lot 作为 Pilot 传给 R2R。
```

### 1.2 新逻辑

AutoSplitPirun 分批方式调整为物理分批：

```text
MES 中生成子 Lot；
Pilot 晶圆实际从原 FOUP 中拆出；
新子 Lot 绑定独立 FOUP；
新子 Lot 作为 Pilot 传给 R2R。
```

本需求上线后，AutoSplitPirun 默认全部使用物理分批，不再使用原逻辑分批。

## 2. 分批前校验

AMA 读取 RTD Report 后，调用 MES 物理分批前保留既有校验：

1. Lot 厂别校验：Lot 属于 FAB6 或 FAB8。
2. Lot 状态校验：Lot 当前状态为 `WaitForJobPrep`，且当前站点 `runcardid` 为空。
3. Capability 校验：Lot 当前 Capability 为 `LithoCapability` 或 Barc 对应 Capability。
4. Carrier 类型校验：`CarrierKind = FOUP`。
5. Wafer 校验：Report 中选中的 Wafer 存在于该 Lot 中。

校验不通过时，不调用 MES 物理分批。

## 3. 物理分批执行

AMA 调用 MES Split 接口时，需将本次 AutoSplitPirun 标识为物理分批。

接口名称、参数名及参数值待 IT 确认。需求语义如下：

| 参数语义 | 说明 |
| --- | --- |
| SplitMode | 分批模式，取值为 Physical / 物理分批 |
| SourceLot | 原 Lot |
| SplitWaferList | RTD Report 选出的 Pilot Wafer |
| TargetCarrierRequired | 要求新子 Lot 形成独立 FOUP |
| RequestSource | 请求来源，标识为 AMA AutoSplitPirun |

说明：

1. 本需求不新增 UI 开关。
2. AutoSplitPirun 后续统一使用物理分批。
3. 若 MES 接口需指定目标 Carrier 或由 MES 自动分配 FOUP，具体方式由 IT 与 MES 确认。

## 4. 物理分批结果校验

MES 返回成功后，AMA 需校验以下结果：

1. MES 返回新子 LotID。
2. 新子 Lot 对应 Wafer 与 Report 选定 Wafer 一致。
3. 新子 Lot 已绑定独立 FOUP。
4. 新子 Lot 与原 Lot 不在同一 FOUP。
5. 新子 Lot 状态满足 R2R Pilot 传参要求。

若 MES 返回成功但新子 Lot 未形成独立 FOUP，则本次 AutoSplitPirun 视为物理分批异常：

```text
不传 Pilot 给 R2R；
不执行 Hold；
记录异常原因。
```

## 5. Pilot 传给 R2R

物理分批成功后，AMA 将 MES 返回的新子 Lot 作为 Pilot 传给 R2R。

```text
IF MES 物理分批成功
AND 新子 Lot 已形成独立 FOUP
THEN AMA 将新子 LotID 作为 Pilot 传给 R2R
ELSE 不传 Pilot，记录失败原因
```

R2R 接收对象保持原逻辑，仍接收分批后的子 Lot 作为 Pilot。

## 6. 分批失败处理

若 MES 物理分批失败：

1. AMA 不传 Pilot 给 R2R。
2. AMA 不执行 Hold。
3. AMA 记录 MES 返回失败原因。

失败原因建议保留 MES 原始返回信息，便于区分 FOUP 不足、Carrier 异常、Split 接口失败、AMHS 搬送异常等场景。

说明：

1. 本需求上线后，AutoSplitPirun 使用物理分批。
2. 物理分批失败统一不执行 Hold。
3. 若 MES 返回原因包含 `FutureMerge`，同样不执行 Hold，仅记录失败原因。

## 7. AMA Log / 追溯信息

建议 AMA 记录以下信息：

| 字段 | 说明 |
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

# 三、影响范围

| 项目 | 影响说明 |
| --- | --- |
| RTD Pilot 选择 | 增加同 FOUP SortJobid 过滤逻辑 |
| RTD Report / Log | 建议增加 SameFoupSortJob 相关追溯字段 |
| AMA 分批逻辑 | AutoSplitPirun 由逻辑分批改为物理分批 |
| MES Split 接口 | 需支持 / 调用物理分批参数 |
| R2R Pilot 传参 | 传参对象仍为分批后的子 Lot |
| 分批失败处理 | 物理分批失败不执行 Hold，仅记录失败原因 |

# 四、测试重点

| 测试内容 | 测试场景 | 预期结果 |
| --- | --- | --- |
| 同 FOUP SortJobid 判断 | 候选 Lot 所在 FOUP 内任意 Lot 的 SortJobid 不为空 | 候选 Lot 不选作 Pilot |
| 同 FOUP 无 SortJobid | 候选 Lot 所在 FOUP 内所有 Lot 的 SortJobid 均为空 | 候选 Lot 继续进入原 Pilot 选择逻辑 |
| SortJobid 数据为空值处理 | SortJobid 为 NULL / 空字符串 | 按空值处理，不触发过滤 |
| 物理分批成功 | MES 返回新子 Lot，且新子 Lot 形成独立 FOUP | AMA 将新子 Lot 作为 Pilot 传给 R2R |
| 物理分批失败 | MES 返回物理分批失败 | AMA 不传 Pilot，不 Hold，记录失败原因 |
| FutureMerge 返回原因 | MES 返回失败原因包含 FutureMerge | 本次物理分批失败处理不执行 Hold，仅记录失败原因 |
| 独立 FOUP 校验 | MES 返回成功但新子 Lot 未绑定独立 FOUP | 不传 Pilot，不 Hold，记录异常原因 |
| 原逻辑回归 | FutureMerge 过滤、同母批同 Stage Pilot 唯一性逻辑 | 既有判断结果不受影响 |

# 五、待确认事项

| 序号 | 待确认项 | 影响范围 |
| --- | --- | --- |
| 1 | SortJobid 的具体数据来源、表名、字段名 | RTD 同 FOUP SortJobid 判断 |
| 2 | 同 FOUP Lot 清单获取方式及 Carrier / FOUP 关系表 | RTD Pilot 过滤 |
| 3 | MES 物理分批接口名称、参数名及成功返回字段 | AMA 物理分批 |
| 4 | MES 物理分批时，目标 FOUP 由 MES 自动分配还是 AMA 指定 | 物理分批执行 |
| 5 | 新子 Lot 状态满足 R2R Pilot 传参要求的判定字段 | AMA 结果校验 |

# 六、审批意见区

| 审批项 | 意见 / 日期 |
| --- | --- |
| 申请部门意见 |  |
| 申请部门分管领导意见 |  |
| 相关部门意见 |  |
| 相关部门分管领导意见 |  |
| 信息技术部意见 |  |
| 信息技术部分管领导意见 |  |
| 附件名称 |  |
