# Litho Auto Split Pirun 物理分批及选 Pilot 逻辑优化需求单 v0.5

> 本版记录 2026-07-23 当轮用户确认口径，并补充多 Context、多 Lot 场景下的 Pilot 挑选逻辑。它是该轮需求的参考基线，不是后续新需求的唯一事实来源；新需求与本版不一致时，应先判断是否属于有意变更并重新确认。原始需求 `1.jpg～8.jpg` 中未在本版说明的已上线逻辑仅作为历史对照。

## 版本变更记录

| 版本 | 日期 | 变更内容 |
| --- | --- | --- |
| v0.5 | 2026-07-23 | 增加 Context 组成及唯一性校验；补充同 Reticle 优先同机台、不同 Reticle 组间机台均衡及完整 Pilot 挑选步骤。 |
| v0.4 | 2026-07-23 | 按用户确认稿更新 Auto Split 触发条件、选 Lot 优先级、整卡 Pilot 场景、物理分批、Auto Pirun 卡控、子母批派工及 TransferFoup 逻辑。 |

## 基础信息

| 字段 | 内容 |
| --- | --- |
| 编号 | 由信息技术部填写 |
| 类别 | □1. 软件采购　□2. 硬件采购　☑3. 功能开发　□4. 工程及服务 |
| 申请部门 | 制造部 |
| 系统名称 | CIM 计算机集成制造系统 Fab6（二科） |
| 申请人员 | 温浩奇 |
| 功能模块 | 智能派工系统（RTD/DSP/AMA） |
| 申请日期 | 【待填写】 |
| 希望交付期 | 【待填写】 |
| 需求项目 | Litho Auto Split Pirun 物理分批及选 Pilot 逻辑优化 |
| 涉及范围 | FAB6 / FAB8、RTD、LithoAssign、LithoRule、AMA、MES Split、TransferFoup |
| 需求类型 | 已上线功能逻辑优化 |

## 项目简介和必要性分析

### 项目背景

现有 Litho Auto Split Pirun 功能已上线运行。RTD 根据 Lot 的 R2R（Run-to-Run）状态、作业条件和 Context 选择 Pilot，生成 `Central_GetLithoR2RAutoPirunInfo` Report，由 AMA 调用 MES 分批接口，并将 Pilot Lot 传给 R2R。

本次调整按用户确认稿统一以下业务口径：

1. Auto Split Pirun 仅检查 BARC 与 LITHO（IMM）主机台当站 Lot。
2. 明确候选 Lot 的过滤条件、可作业机台判断及 Context 选 Pilot 的优先级。
3. 区分整卡 Pilot 与物理分批场景；Auto Split 分出的子批执行物理分批。
4. R2R 已配置 Pilot 与其他 Lot 共用 FOUP 时，按条件自动执行 `TransferFoup`。
5. 补充 Auto Pirun 派工管控、子母批同机台卡控、Sorter 等待及 Reticle 位置处理规则。

### 需求目标

1. 从 BARC 与 LITHO（IMM）主机台当站 Lot 中自动选择 Pilot。
2. 按确认后的固定优先级为每个 Context 选择 Pilot，避免同一 Lot 同时成为多个 Context 的 Pilot。
3. 多个 Context 同时选 Pilot 时，相同 Reticle 的 Lot 尽量选择到同一机台。
4. 在满足同 Reticle 同机台的前提下，避免各 Context 的 Pilot 全部集中到同一机台。
5. 满足整卡条件时，将当前 Lot 全部 Wafer 设为 Pilot；其余场景执行物理分批。
6. Auto Split 分出的 Pilot 子批进入独立 FOUP。
7. R2R 已配置 Pilot 与其他 Lot 共用 FOUP 时，自动执行 `TransferFoup`，减少人工拆分 FOUP。
8. 保证同 FOUP 其他 Lot、子母批派工及 Auto Pirun 管控符合现场作业要求。

### 术语说明

- **Pirun / Pilot**：Pilot Run，用于 R2R 前置验证的 Lot 或 Wafer。
- **Auto Split**：R2R Context 开启的自动选 Pilot 及自动分批功能。
- **Context**：R2R 中用于区分产品、Layer、Recipe 或机台条件的控制组合。
- **RemainQtime**：Lot 当前剩余 Queue Time。
- **整卡 Pilot**：当前 Lot 的全部 Wafer 均作为 Pilot，不执行分批。
- **物理分批**：从原 Lot 分出指定 Wafer 生成 Pilot 子 Lot，并将子 Lot 导入另一只 FOUP。
- **TransferFoup**：将已存在的 Pilot Lot 从共用 FOUP 转入其他 FOUP，不生成新 Lot。
- **Pretool**：R2R 中用于垂直限定 Layer 同机台作业的机台信息；`Pretool ≠ "NA"`表示需要执行同机台卡控。

## 项目投资方案比较及效果分析

### 改善方案

1. RTD 获取 BARC 与 LITHO（IMM）主机台当站 Lot，执行候选过滤、可作业机台判断、Context 排序及 Pilot 选择。
2. RTD 以 `STN / Reticle / Prod / Recipe / PreReticle / PreStn / Custom_Value`组成 Context，并校验同一 `Lot + STN + Reticle`只对应一个 Context。
3. Context 内按 6 项业务规则对候选 Lot 排序；跨 Context 先按 Reticle 归组，再依次执行同 Reticle 机台聚合和机台均衡。
4. RTD 根据 Lot 位置、RemainQtime、Lot 片数、Chuck 数量及特殊 Lot 属性，输出整卡 Pilot 或物理分批结果。
5. AMA 对需要分批的 Lot 调用 MES 物理分批接口；接口未成功时，原 Lot 整卡设为 Pilot。
6. 对 R2R 已配置的 Pilot，若同 FOUP 内存在其他 Lot，则按本版适用范围执行 `TransferFoup`。
7. LithoAssign / LithoRule 按 Auto Pirun、子母批同机台及 BARC 强派规则执行派工卡控。

### 效果分析

1. 减少人工选 Pilot、人工拆分 FOUP 及手动维护 R2R Pilot 的操作。
2. 通过整卡 Pilot 与物理分批条件区分，降低不满足分批条件时的处理等待。
3. 通过同 FOUP 其他 Lot 卡控及子母批派工约束，避免 Pilot 搬送期间其他 Lot 被错误派工。
4. OQT、人工工时及自动化率的量化收益由制造补充。

## 需求流程图

### Auto Split 选 Pilot 及分批流程

```text
开始
  ↓
获取 BARC 与 LITHO（IMM）主机台当站 Lot
  ↓
过滤 Pirun Loop RC、Pirun Loop Future Hold、非 Active、Specify Lot
  ↓
按 CSN、PPID、Recipe、Capa、Global 卡控及 R2R Context 判断可作业机台
  ↓
同一 Lot 是否存在多路径？
  ├─ 是：不自动作为 Pilot；如需使用，由用户在 R2R 中手动设置
  └─ 否：生成 ContextKey，并校验 Lot + STN + Reticle 唯一性
           ↓
是否存在 Context 映射冲突？
  ├─ 是：冲突记录不参与自动选择，输出 ContextMappingConflict
  └─ 否：按 Reticle 对 Context 归组
           ↓
优先处理可选机台较少的 Reticle 组
  ↓
初始化各机台已有 Pilot Context 数，并计算每个机台可覆盖的未完成 Context 数
  ↓
选择同 Reticle 已分配数与本轮可覆盖数合计最大的机台
  ↓
合计值相同时，选择全部有效 Pilot Context 数较少的机台
  ↓
仍相同时，选择 Context 内候选 Lot 综合排序更优的机台
  ↓
每个 Context 从目标机台可作业 Lot 中选择排名第一的 Lot
  ↓
已选 Lot 从其他 Context 候选池移除，剩余 Context 重新计算
  ↓
是否满足任一整卡 Pilot 条件？
  ├─ 是：当前 Lot 全部 Wafer 设为 Pilot
  └─ 否：执行物理分批
           ↓
物理分批接口是否成功？
  ├─ 是：新 Pilot 子 Lot 导入另一只 FOUP
  └─ 否：原 Lot 整卡设为 Pilot
           ↓
结束
```

### 已配置 Pilot 的 TransferFoup 流程

```text
开始
  ↓
R2R Status = PirunON，且 Context 已配置 Pilot
  ↓
是否属于 Production 且等级 < 5 的 Pilot？
  ├─ 否：不执行本需求新增的 TransferFoup 逻辑
  └─ 是：检查 Pilot 所在 FOUP
           ↓
同 FOUP 内是否存在其他 Lot？
  ├─ 否：不执行 TransferFoup
  └─ 是：卡控同 FOUP 其他 Lot，不允许派工
           ↓
Pilot 在 Sorter 站点等待导 FOUP，不自动 Cancel
  ↓
执行 TransferFoup（不区分 Auto Split 开关状态）
  ↓
结束
```

# 一、RTD 部分更改逻辑

## 1. Auto Split 触发场景

### 1.1 候选 Lot 范围

Auto Split Pirun 仅检查 BARC 与 LITHO（IMM）主机台当站 Lot，不将 Pirun Loop 中间站 Lot 纳入自动候选。

候选 Lot 继续从 FAB6、FAB8 获取，沿用现有数据来源：

1. 通过 `fwlot`获取 `appid`、`priority`、`processingstatus`、`componentqty`，用于 Lot 基础信息和片数判断。
2. 通过 `fablotext`获取 `requiredcapability`、`runcardid`、`reticleid`，用于 Capability 和作业条件判断。
3. 通过 `fablotcarrierext`获取 `carrierkind`，用于 FOUP 类型判断。
4. 通过 `fabinqtimeprocess`获取 `RemainQtime`，用于 Qtime 判断和排序。
5. 通过 `fabfutureaction`获取 Future Action 信息，用于 Future Hold 判断。
6. 通过 `RTDConfig_LITHOLotAssignment-LithoAssignCapability`获取 Litho Capability 配置。
7. 通过 R2R Context 相关表获取 R2R Status、Pilot、Pretool 和 Auto Split 开关。

### 1.2 候选过滤条件

候选 Lot 必须满足：

```text
processingstatus = 'Active'
```

同时删除以下 Lot：

1. Pirun Loop 中存在 RC 站点的 Lot。
2. Pirun Loop 中存在 Future Hold 的 Lot。
3. Specify Lot。

### 1.3 可作业机台判断

可作业机台按以下条件判断：

1. CSN；
2. PPID；
3. Recipe；
4. Capa；
5. Global 卡控；
6. R2R Context：`R2R Status = PirunON`且 Auto Split 开关开启。

任一条件不满足时，过滤对应机台。Lot 在相关机台均无可作业条件时，不进入 Auto Split Pirun 候选。

### 1.4 多路径 Lot

同一 Lot 存在多条可作业路径时，不自动将该 Lot 设为 Pilot。若用户需要该 Lot 执行其他 Context 的 Pirun，需在 R2R 系统中手动设置 Pilot。

## 2. 选 Lot 逻辑

### 2.1 Context 组成及唯一性

Context 由以下 7 个字段组成：

```text
ContextKey = STN|Reticle|Prod|Recipe|PreReticle|PreStn|Custom_Value
```

生成 Context 时，字段按系统标准值进行匹配，字段顺序固定，不允许交换。各字段去除首尾空格，空值统一按`<EMPTY>`参与组合，避免因连接方式产生重复或碰撞。相同字段组合只保留一个 ContextKey。

同一 Lot 在相同 STN、相同 Reticle 下只能对应一个 Context：

```text
LotContextUniqueKey = LotID|STN|Reticle
```

唯一性检查按以下规则处理：

1. 相同 `LotContextUniqueKey`重复出现，且对应的 ContextKey 完全相同：合并重复记录，只保留一条候选。
2. 相同 `LotContextUniqueKey`对应多个不同 ContextKey：判定为 Context 映射冲突，相关记录不参与本轮自动选 Pilot，并记录`ContextMappingConflict`。
3. `Reticle`为空或`NA`时，不与其他空 Reticle Context 合并为同一 Reticle 组；该 Context 按独立组参与机台均衡。

### 2.2 跨 Context Pilot 卡控

Lot 已设置为 Context A 的 R2R Pilot 时，不允许再被选择为 Context B 的 R2R Pilot。Context A 清除该 Pilot 配置后，该 Lot 才可参与其他 Context 的 Pilot 选择。

本轮选择过程中，同一 Lot 也只允许分配给一个 Context。Lot 被某个 Context 选中后，立即从其他 Context 的候选池中移除；受影响的 Context 重新计算候选 Lot 和目标机台。

### 2.3 Lot 片数基础判断

1. `Lot wafer count ≤ 6`时，将该 Lot 的全部 Wafer 设为 Pilot，不执行分批。
2. `Lot wafer count > 6`时，按 Auto Split 设置的分批片数执行后续判断；未设置分批片数时，默认 Pilot 片数为 4 片。

### 2.4 Context 内候选 Lot 排序

同一 Context 的候选 Lot 按以下顺序比较；前一项相同时，再比较后一项：

1. 距离 LITHO 站点最近的 Lot 优先。
2. Lot 总片数大于或等于设置的分批片数时优先。
3. `Chuck1`与`Chuck2`的 Wafer 数量均大于或等于 2 片时优先。
4. 空机空 Port Lot 优先。
5. `RemainQtime > 0`的候选 Lot 中，`RemainQtime`最小的优先。
6. Key Lot 可参与选择，但不优先。

排序条件可统一表示为：

```text
CandidateSortKey =
1. DistanceToLitho ASC
2. SplitCntMatched DESC
3. ChuckMatched DESC
4. EmptyEqpPort DESC
5. HasPositiveRemainQtime DESC，RemainQtime ASC
6. IsKeyLot ASC
7. StableOrder ASC
```

其中，`HasPositiveRemainQtime = 1`表示`RemainQtime > 0`；仅在该值为 1 时比较 RemainQtime 大小。`IsKeyLot = 1`表示 Key Lot，因此非 Key Lot 排在 Key Lot 前面。

空机空 Port Lot 或 Key Lot 被选中后，均按整卡 Pilot 处理。

为保证结果稳定，6 项条件完全相同时，沿用候选数据的现有稳定顺序；若现有逻辑无稳定顺序，则以 LotID 升序作为最终 Tie-breaker。Tie-breaker 只用于保证重复计算结果一致，不改变上述业务优先级。

### 2.5 多 Context 的 Reticle 归组

完成 Context 内排序后，按 Reticle 对尚未选出 Pilot 的 Context 归组：

```text
ReticleGroup = 相同 Reticle 的 Context 集合
```

不同 Prod、Recipe、PreReticle、PreStn 或 Custom_Value 的 Context，只要 Reticle 相同，仍属于同一 ReticleGroup；各 Context 的候选 Lot 和可作业机台保持独立。

ReticleGroup 按以下顺序处理：

1. 可选机台数量较少的 ReticleGroup 优先。
2. 可选机台数量相同时，包含 Context 数量较多的 ReticleGroup 优先。
3. 前两项均相同时，按 Reticle 的现有稳定顺序处理；若无稳定顺序，则按 Reticle ID 升序处理。

该顺序用于优先处理机台选择受限的 ReticleGroup，减少后续无可选机台的情况。

### 2.6 同 Reticle 优先选择同一机台

针对当前 ReticleGroup，系统对每台可作业机台计算`ReticleCoverageCount`：

```text
ReticleCoverageCount
= 当前机台至少存在一个可作业候选 Lot 的未完成 Context 数量
```

同时计算：

```text
ReticleAssignedContextCount
= 当前机台已配置或本轮已选中的同 Reticle Pilot Context 数量

ReticleCohesionScore
= ReticleAssignedContextCount + ReticleCoverageCount
```

已有有效 Pilot 的 Context 不再重复选择 Pilot，但需要计入`ReticleAssignedContextCount`和机台总分配数，使本轮新选 Pilot 同时考虑现有结果。

机台选择按以下顺序比较：

1. `ReticleCohesionScore`较大的机台优先，使新选 Pilot 尽量与该机台已有的同 Reticle Pilot 汇合；当前 Reticle 尚无已选 Pilot 时，该值等同于比较`ReticleCoverageCount`。
2. `ReticleCohesionScore`相同时，比较`EqpAssignedContextCount`，当前全部有效 Pilot Context 数量较少的机台优先。
3. 前两项相同时，比较`CandidateRankScore`。对机台可覆盖的每个 Context，取该机台下最优候选 Lot 的 Context 内名次，再计算平均名次；平均值较小的机台优先。
4. 以上条件仍相同时，沿用机台现有稳定顺序；若无稳定顺序，则按 EqpID 升序处理。

确定目标机台后，当前机台可覆盖的每个 Context，从该机台可作业的候选 Lot 中选择 2.4 节排名第一的 Lot 作为 Pilot。

若没有任何一台机台可以覆盖同一 ReticleGroup 的全部 Context，则先选择`ReticleCohesionScore`最大的机台完成可覆盖 Context；剩余 Context 更新已分配数和覆盖数后继续选择，直至全部 Context 完成或无候选 Lot。

### 2.7 在同 Reticle 约束下执行机台均衡

`EqpAssignedContextCount`表示当前机台全部有效 Pilot Context 的数量。计算开始时，以当前有效的已配置 Pilot 初始化；本轮每成功选择一个 Context 的 Pilot 后立即加 1。

机台均衡只在`ReticleCohesionScore`相同的机台之间生效，不得为了均衡而拆开原本可以选择到同一机台的同 Reticle Context。处理不同 ReticleGroup 时，继续使用已更新的`EqpAssignedContextCount`，使后续 ReticleGroup 优先选择当前分配数量较少的机台。

优先关系固定为：

```text
同 Reticle Cohesion 最大化
    > 机台有效 Pilot Context 数量最小化
    > CandidateRankScore 最小化
    > 稳定 Tie-breaker
```

### 2.8 完整挑选步骤

1. 获取全部待处理 Context、候选 Lot 及每个 Lot 的可作业机台。
2. 按 2.1 节生成 ContextKey，合并重复记录并拦截 Context 映射冲突。
3. 删除已被其他 Context 配置为 Pilot 的 Lot，并执行候选过滤及可作业机台判断。
4. 读取当前有效的已配置 Pilot，初始化每台机台的`EqpAssignedContextCount`及每个 Reticle 在各机台的`ReticleAssignedContextCount`。
5. 在每个 Context 内按 2.4 节生成候选 Lot 排名。
6. 按 Reticle 建立 ReticleGroup，并按 2.5 节确定组处理顺序。
7. 对当前 ReticleGroup 计算各机台的`ReticleCoverageCount`和`ReticleCohesionScore`。
8. 按“Cohesion 最大、机台有效 Pilot Context 数最小、CandidateRankScore 最小、稳定 Tie-breaker”选择目标机台。
9. 每个被覆盖的 Context 从目标机台候选中选择排名第一的 Lot。
10. 每选中一个 Lot，立即登记“Context—Pilot Lot—TargetEqp”结果；该 Lot 从其他 Context 候选池移除，并更新两个 AssignedContextCount。
11. 若候选池因 Lot 被占用而变化，受影响的 Context 重新执行步骤 7～10。
12. 当前 ReticleGroup 仍有未完成 Context 时，继续选择下一台机台；当前组完成后处理下一 ReticleGroup。
13. Context 无可用候选 Lot 时，不为该 Context 自动设置 Pilot，记录`NoEligiblePilot`及过滤原因。

### 2.9 示例

| ReticleGroup | Context | 可选机台 | Context 内首选 Lot |
| --- | --- | --- | --- |
| R1 | C1 | E1 | L1 |
| R1 | C2 | E1、E2 | L2 |
| R2 | C3 | E1、E2 | L3 |

处理结果：

1. R1 组中，E1 可同时覆盖 C1、C2，`ReticleCoverageCount = 2`；E2 只能覆盖 C2，覆盖数为 1。因此 C1、C2 均选择到 E1。
2. 完成 R1 后，E1 的`EqpAssignedContextCount = 2`，E2 为 0。
3. R2 组中，E1、E2 对 C3 的覆盖数相同，均为 1；此时按机台均衡选择 E2。
4. 最终结果为：相同 Reticle R1 的两个 Context 集中到 E1，不同 Reticle R2 的 Context 分配到 E2，满足两条约束的先后关系。

## 3. 整卡 Pilot 与物理分批判断

### 3.1 整卡 Pilot 场景

选中的 Lot 满足以下任一条件时，不执行物理分批，将当前 Lot 的全部 Wafer 设为 Pilot：

1. Lot 为空机空 Port Lot 或 Key Lot。
2. Lot 位于 LITHO（IMM）当站，且存在 Qtime。
3. `Chuck1`或`Chuck2`的 Wafer 数量不满足大于或等于 2 片的条件。
4. Lot 总片数小于设置的 `pi_splitcnt`。
5. `Lot wafer count ≤ 6`。
6. 物理分批接口未成功。

### 3.2 物理分批场景

Lot 不满足 3.1 节任一整卡 Pilot 条件时，执行物理分批。

Lot 总片数大于 6 片时，Pilot 片数按以下规则确定：

```text
IF pi_splitcnt 有值
THEN Pilot 片数 = pi_splitcnt；
ELSE Pilot 片数 = 4。
```

Wafer 按现有 `Chuck1 / Chuck2`分组及 `WaferRank / GroupRank`排序逻辑选择；本次只增加两个 Chuck 的 Wafer 数量均需大于或等于 2 片的前置条件。

### 3.3 LITHO（IMM）与 BARC 当站处理

1. LITHO（IMM）当站 Lot 存在 Qtime 时，整卡设为 Pilot；不存在 Qtime 时，按 3.1 节判断是否执行物理分批。
2. BARC 当站 Lot 按 3.1 节判断；不满足整卡 Pilot 条件时执行物理分批。

## 4. Auto Pirun 派工管控

### 4.1 L-BARCO* 站点强派

在 `L-BARCO*`站点设置 `R2R Auto Pirun Control`派工管控。当 Lot 位于`L-BARCO*`站点，且`RemainQtime < 强派时间`时，强派前 Remove Auto Pirun 派工管控，再执行强派。

### 4.2 LITHO（IMM）当站卡控

当 `R2R Status = PirunON`且 Auto Split 开关开启时，LITHO（IMM）当站符合条件的 Lot 需执行 `R2R Auto Pirun Control`，直至选出 Pilot。

`RC Specify` Lot 不执行该卡控。

### 4.3 Context 已存在 Pilot

当 `R2R Status = PirunON`、Auto Split 开关开启且 Context 已存在 Pilot 时，不再执行 `R2R Auto Pirun Control`，后续按现有 R2R 逻辑判断。

## 5. 子母批派工卡控

### 5.1 垂直限定 Layer

对于垂直限定 Layer，即 R2R 中 `Pretool ≠ "NA"`的场景：

1. 子母批中的一个 Lot 已在主机台作业时，其他同源 Lot 需派往相同机台。
2. 子批、母批需要分开派往不同机台时，由 PE 在 R2R 中设置白名单放行。
3. 子母批中任一 Lot 存在 Specify 时，不执行同机台卡控。

### 5.2 两只 FOUP、两条可作业路径

子母批位于两只 FOUP，且两条路径均可作业时，同 Layer、同 Lot Source 的 Lot 不应同时派往两台机台。

光刻不存在同一时间在多台机台内作业的场景，因此本次按 5.1 节规则卡控，不新增独立派工逻辑。

## 6. Reticle 位置卡控

Auto Split 选择及处理过程中，不再卡控 Reticle 的位置。

## 7. Report 调整

原 Report `Central_GetLithoR2RAutoPirunInfo`继续供 AMA 读取。现有栏位包括：

```text
toolid、toolname、productid、layerid、reticleid、prereticle、pretool、
custom_context_value、prelayer、pilot、STNSite
```

为支持本次逻辑，Report 需能够提供以下业务信息：

1. 原 Lot。
2. Pilot Wafer 清单。
3. 处理模式：`PhysicalSplit / WholeLotPilot`。
4. 整卡 Pilot 原因。
5. Lot 当前所在位置：LITHO（IMM）/ BARC。
6. `RemainQtime`。
7. Context、Pretool 及目标站点信息。
8. `ContextKey`及组成字段。
9. `ReticleGroup`。
10. `TargetEqp`。
11. Context 内候选 Lot 排名及最终`CandidateRank`。
12. 选中机台时的`ReticleAssignedContextCount`、`ReticleCoverageCount`、`ReticleCohesionScore`和`EqpAssignedContextCount`。
13. `SelectReason`：记录同 Reticle 聚合、机台均衡、`CandidateRankScore`及 Tie-breaker 的命中结果。

> 【待 IT 确认】上述信息复用现有栏位还是新增 Report 栏位，以及正式栏位名。

# 二、AMA 部分更改逻辑

## 1. 执行频率及数据获取

AMA Job 执行频率继续沿用现有配置，不在本次需求中调整。

AMA 读取 `Central_GetLithoR2RAutoPirunInfo`，根据 RTD 输出的处理模式执行物理分批或整卡 Pilot。

## 2. Auto Split 物理分批

### 2.1 物理分批前提

Auto Split Pirun 分出的 Pilot 子批需要执行物理分批。

### 2.2 PhysicalSplit

当 RTD 输出 `PhysicalSplit`时，AMA 调用 MES 物理分批接口：

1. 从原 Lot 分出 Report 指定的 Pilot Wafer。
2. 生成新的 Pilot 子 Lot。
3. 将新 Pilot 子 Lot 导入另一只 FOUP，使其与原 Lot 不共用 FOUP。
4. 分批成功后，将新 Pilot 子 Lot 传给 R2R。

> 【待 IT 确认】MES 物理分批接口名称、参数、目标 FOUP 分配方式及成功返回栏位。

### 2.3 物理分批接口未成功

物理分批接口未成功时：

1. 当前 Lot 不再执行物理分批。
2. 将原 Lot 的全部 Wafer 整卡设为 Pilot。
3. 记录物理分批接口失败原因及整卡处理结果。

### 2.4 WholeLotPilot

当 RTD 输出 `WholeLotPilot`时，AMA 不调用 MES 分批接口，直接将原 Lot 作为 Pilot 传给 R2R。

## 3. 已配置 Pilot 的 TransferFoup

### 3.1 触发条件及适用范围

R2R 表中的 Pirun Lot，以及 Context 中 `R2R Status = PirunON`时所配置的 Pilot，满足以下条件时自动执行 `TransferFoup`：

1. Pilot 所在 FOUP 内存在其他 Lot。
2. Pilot 为 Production，且等级 `< 5`。

符合以上条件时，不区分 Auto Split 开关是否开启，均执行 `TransferFoup`。

`TransferFoup`只搬送已存在的 Pilot Lot，不生成新 Lot。

### 3.2 同 FOUP 其他 Lot 卡控

执行 `TransferFoup`前，同 FOUP 内其他 Lot 需执行派工卡控，不允许派工。完成 Pilot 导 FOUP 后，再按现有逻辑处理同 FOUP 其他 Lot。

### 3.3 Sorter 等待处理

Pilot 在 Sorter 站点等待导 FOUP，不执行自动 Cancel。

本次不新增自动 `Cancel Sorter`接口。该 Lot 已为 Pilot，Qtime 紧急风险较低。

## 4. 子母批派工

物理分批完成后，新 Pilot 子 Lot 与原 Lot 按 RTD 章节 5 的规则执行派工卡控：垂直限定 Layer 默认保持同机台；确需分开派往不同机台时，由 PE 在 R2R 中设置白名单放行；任一 Lot 存在 Specify 时，不执行同机台卡控。

## 5. Log 及追溯信息

AMA Log 至少记录以下业务信息：

1. `SourceLot`：原 Lot。
2. `PilotLot`：物理分批生成的 Pilot 子 Lot；整卡或 TransferFoup 场景记录原 Pilot Lot。
3. `SourceFOUP`：原 FOUP。
4. `TargetFOUP`：新 Pilot 子 Lot 或 TransferFoup 后的 FOUP。
5. `ActionType`：`PhysicalSplit / WholeLotPilot / TransferFoup`。
6. `PilotWaferList`：Pilot Wafer 清单；整卡场景记录全部 Wafer。
7. `Result`：`Success / Fail / Fallback`。
8. `FailReason`：MES 物理分批接口或 TransferFoup 返回的失败原因。

# 三、原逻辑与现逻辑对比

## 1. 候选 Lot 范围

原逻辑：候选范围包含 Pirun Loop 内的相关 Lot。

现逻辑：仅检查 BARC 与 LITHO（IMM）主机台当站 Lot；Lot Status 必须为 Active，并过滤 Pirun Loop RC、Pirun Loop Future Hold 及 Specify Lot。

修改原因：按用户确认稿收敛自动选择范围及过滤口径。

## 2. Pilot 排序

原逻辑：按已上线指标选择 Pilot，特殊 Lot 及 Qtime 的排序口径未按本次顺序统一。

现逻辑：Context 由`STN / Reticle / Prod / Recipe / PreReticle / PreStn / Custom_Value`组成，同一`Lot + STN + Reticle`只允许对应一个 Context。Context 内按“距离 LITHO 最近、片数满足分批片数、Chuck1 / Chuck2 均不少于 2 片、空机空 Port、最小正 RemainQtime、Key Lot 不优先”的顺序比较。多个 Context 同时选 Pilot 时，先使相同 Reticle 的 Context 尽量选择到同一机台，再在覆盖数相同的机台间选择本轮已分配 Context 数较少的机台。

修改原因：统一 Context 内候选 Lot 排序，并补充跨 Context 的 Reticle 聚合和机台均衡逻辑。

## 3. 整卡 Pilot 与物理分批

原逻辑：按原 Auto Split 逻辑生成 Pilot 子批。

现逻辑：空机空 Port / Key Lot、LITHO 当站有 Qtime、任一 Chuck 少于 2 片、Lot 片数不足 `pi_splitcnt`、Lot 片数不大于 6 或物理分批接口未成功时，整卡设为 Pilot；其余场景执行物理分批。`pi_splitcnt`未设置时默认 4 片。

修改原因：明确不能或不需要物理分批时的统一处理方式。

## 4. TransferFoup

原逻辑：R2R 已配置 Pilot 与其他 Lot 共用 FOUP 时，主要依赖人工处理。

现逻辑：Production 且等级 `< 5`的 Pilot，在 `R2R Status = PirunON`且同 FOUP 内存在其他 Lot 时自动执行 `TransferFoup`，不区分 Auto Split 开关；导 FOUP 前卡控同 FOUP 其他 Lot，Pilot 在 Sorter 等待期间不自动 Cancel。

修改原因：减少人工拆分 FOUP，并避免导 FOUP 期间其他 Lot 被派工。

## 5. 子母批派工

原逻辑：子母批分开后，未按本次确认稿统一同机台及例外规则。

现逻辑：垂直限定 Layer 默认保持同机台；需异机台作业时由 PE 设置白名单；任一 Lot 存在 Specify 时不执行同机台卡控。

修改原因：避免同 Layer、同 Lot Source 的子母批同时派往不同机台。

## 6. Reticle 位置

原逻辑：Auto Split 处理过程中存在 Reticle 位置卡控。

现逻辑：Auto Split 时不再卡控 Reticle 位置。

修改原因：按用户确认稿调整 Auto Split 判断条件。

# 四、Test Case 派生参考（不进入需求单交付）

> 本节用于后续基于需求单单独生成 Test Case Excel。正式需求单 Word 不包含本节测试用例明细。

| 场景 | 输入条件 | 预期结果 |
| --- | --- | --- |
| 候选范围 | Lot 位于 BARC 与 LITHO（IMM）之间的 Pirun Loop 中间站 | 不进入自动候选 |
| Lot Status | `processingstatus ≠ Active` | 不进入自动候选 |
| Pirun Loop RC | Lot 的 Pirun Loop 中存在 RC 站点 | 不进入自动候选 |
| Future Hold | Lot 的 Pirun Loop 中存在 Future Hold | 不进入自动候选 |
| Specify Lot | Lot 为 Specify Lot | 不进入自动候选 |
| 多路径 Lot | 同一 Lot 存在多条可作业路径 | 不自动设为 Pilot；如需使用，由用户在 R2R 中手动设置 |
| 跨 Context Pilot | Lot 已设置为 Context A 的 R2R Pilot | 不允许再被 Context B 选择 |
| Context 重复记录 | 相同`Lot + STN + Reticle`重复出现，且 ContextKey 相同 | 合并重复记录，只保留一条候选 |
| Context 映射冲突 | 相同`Lot + STN + Reticle`对应多个不同 ContextKey | 不参与本轮自动选择，记录`ContextMappingConflict` |
| 同 Reticle 有共同机台 | R1 的 C1、C2 均可在 E1 作业 | C1、C2 优先选择到 E1 |
| 已有同 Reticle Pilot | R1 已有 Pilot 在 E1，新 Context 在 E1、E2 均可作业 | 优先比较`ReticleCohesionScore`，新 Pilot 尽量继续选择 E1 |
| 同 Reticle 无共同机台 | R1 的多个 Context 无法由单一机台全部覆盖 | 先选覆盖 Context 数最多的机台，再为剩余 Context 重新选机台 |
| Cohesion 相同 | E1、E2 对当前 ReticleGroup 的`ReticleCohesionScore`相同 | 选择`EqpAssignedContextCount`较小的机台 |
| 不同 Reticle 机台均衡 | R1 已向 E1 分配多个 Context，R2 在 E1、E2 均可作业 | R2 优先选择 E2，避免 Pilot 全部集中到 E1 |
| 同一 Lot 被多 Context 候选 | Lot 已被其中一个 Context 选中 | 从其他 Context 候选池移除，并重新计算目标机台和 Pilot |
| Reticle 为空或 NA | 多个 Context 的 Reticle 均为空或 NA | 不合并为同一 ReticleGroup，各 Context 独立参与机台均衡 |
| 小批量 Lot | `Lot wafer count ≤ 6` | 全部 Wafer 设为 Pilot，不执行分批 |
| 默认分批片数 | `Lot wafer count > 6`且未设置`pi_splitcnt` | 默认按 4 片执行分批判断 |
| LITHO 当站有 Qtime | LITHO（IMM）当站 Lot 存在 Qtime | 整卡设为 Pilot |
| Chuck 不满足 | `Chuck1 < 2`或`Chuck2 < 2` | 整卡设为 Pilot |
| Lot 片数不足 | Lot 总片数小于`pi_splitcnt` | 整卡设为 Pilot |
| 空机空 Port Lot | Lot 被选中 | 整卡设为 Pilot |
| Key Lot | Lot 可参与选择但不优先，且最终被选中 | 整卡设为 Pilot |
| 物理分批 | Lot 不满足任一整卡 Pilot 条件 | 执行物理分批，新 Pilot 子 Lot 导入另一只 FOUP |
| 物理分批接口未成功 | MES 物理分批接口返回未成功 | 原 Lot 整卡设为 Pilot，并记录失败原因 |
| L-BARCO* 强派 | `RemainQtime < 强派时间` | Remove Auto Pirun 派工管控后执行强派 |
| LITHO 当站卡控 | `R2R Status = PirunON`且 Auto Split 开启，Context 尚无 Pilot | 执行`R2R Auto Pirun Control`直至选出 Pilot |
| RC Specify | Lot 为 RC Specify | 不执行`R2R Auto Pirun Control` |
| Context 已有 Pilot | `R2R Status = PirunON`、Auto Split 开启且 Context 已存在 Pilot | 不再执行`R2R Auto Pirun Control`，按现有 R2R 逻辑处理 |
| TransferFoup | Production、等级 `< 5`的 Pilot 与其他 Lot 共用 FOUP | 卡控同 FOUP 其他 Lot，并执行 TransferFoup；不区分 Auto Split 开关 |
| Sorter 等待 | Pilot 在 Sorter 站点等待导 FOUP | 不自动 Cancel |
| 垂直限定 Layer | `Pretool ≠ "NA"`，一个同源 Lot 已在主机台作业 | 其他同源 Lot 派往相同机台 |
| PE 白名单 | 子母批需分别派往不同机台 | PE 在 R2R 中设置白名单后放行 |
| Specify 例外 | 子母批任一 Lot 存在 Specify | 不执行同机台卡控 |
| Reticle 位置 | Auto Split 选择及处理 Pilot | 不再卡控 Reticle 位置 |

# 五、待确认事项

| 序号 | 待确认项 | 确认方 | 影响范围 |
| --- | --- | --- | --- |
| 1 | `Production`及“等级 `< 5`”在系统中的正式字段名和数据来源 | IT / R2R | TransferFoup 适用范围 |
| 2 | MES 物理分批接口名称、参数、目标 FOUP 分配方式及成功返回栏位 | IT / MES | 物理分批 |
| 3 | Report 新增或复用栏位及正式栏位名 | IT / RTD / AMA | RTD 与 AMA 数据交互 |
| 4 | 同 FOUP 其他 Lot 使用的正式派工卡控 Reason 名称及解除时点 | IT / LithoAssign | TransferFoup 前后卡控 |
| 5 | 效果分析的 OQT、人工工时及自动化率量化数据 | 制造 | 收益评估 |

# 六、本次不调整内容

1. 原有 `ON / Fixed`在“其他可用站点”中的判断逻辑。
2. 原有 Chuck 分组及组内 `WaferRank / GroupRank`排序逻辑，除本版明确调整的默认片数和两个 Chuck 的最小数量外。
3. AMA Job 执行频率及现有基础校验。
4. 不新增自动 `Cancel Sorter`接口。

# 七、审批意见区

| 审批项 | 意见 / 日期 |
| --- | --- |
| 申请部门意见 |  |
| 申请部门分管领导意见 |  |
| 相关部门意见 |  |
| 相关部门分管领导意见 |  |
| 信息技术部意见 |  |
| 信息技术部分管领导意见 |  |
| 附件名称 |  |
