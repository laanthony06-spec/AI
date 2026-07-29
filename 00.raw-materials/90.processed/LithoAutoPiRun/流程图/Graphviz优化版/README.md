# LithoAutoPiRun 流程图（Graphviz 优化版）

## 设计结论

该需求同时包含两条业务链路和多个独立卡控点，不适合压缩成一张超长流程图。本目录采用“1 张端到端总览 + 8 张子流程”的结构：

| 编号 | 流程图 | 对应需求章节 |
|---|---|---|
| 00 | 端到端主流程 | RTD、AMA、Rule/Assign、Global Macro 的总体协作 |
| 01 | RTD 候选过滤与 Pilot 选择 | 一、1.1～1.4 |
| 02 | RTD Pilot 模式与物理分批选片 | 一、1.5～1.6 |
| 03 | RTD TransferFOUP 候选与任务生成 | 一、2 |
| 04 | Global Macro WaitPilotChangeFOUP 卡控总览 | 一、3.1 |
| 04B | WaitPilotChangeFOUP 解除规则 | 一、3.1 Remove 规则 |
| 05 | LithoRule / LithoAssign 卡控 | 一、3.2、一、4 |
| 06 | AMA Pilot 物理分批执行与回退 | 二、1 |
| 07 | AMA TransferFOUP 执行 | 二、2 |

## 关键规则映射

### RTD 候选过滤

- 候选 Lot 来源：FAB6、FAB8。
- 基础条件：状态、FOUP、空 RunCard、Litho/BARCO Capability，并执行跨厂去重。
- PirunLoop：向后 Fetch 20 站，截取至同 Stage 最后一道 CD；无 CD 的 Lot 被过滤。
- Loop 过滤：必须存在带 Reticle 的 Litho 站点；同 FOUP 已有 Pilot、存在 FutureHold 或 RC 时过滤。
- Specify Lot：命中 `r2r_litho_whitelist` 时转入现有 Specify 处理；其他 Lot 继续执行本次 AutoPirun 逻辑。
- 机台与 R2R：必须存在 `Pi_split_flag='Y'` 的有效机台；只保留状态合规且无 R2R Reason 的 Context；多路径 Lot 被过滤。
- AutoPirun Context：`Pi_split_flag='Y'`，且 `Pilot_CD` 或 `Pilot_OVL` 为空。
- 选择顺序：先计算 RTDRank，再计算 Context 排序指标；每个 Context 最多选择一个 Pilot。

RTDRank 依次按以下优先级计算：

1. `Min(GapToLitho)`
2. `Max(SplitCntMatched)`
3. `Max(RequiredChuckCount)`
4. `Max(BulletLot)`
5. `Min(RemainQ)`
6. `Min(KeyLot)`
7. `Min(lotid)`

Context 之间依次按 `Max(ReticleSTNRank)`、`Min(ContextCandidateCount)`、`Min(ActualSTNPilotCount)`、`Min(RTDRank)` 排序。每轮锁定首位 `Lot+Context`，移除与其 Lot 或 Context 重复的其他候选，更新指标后继续循环。

### 整批与物理分批

任一条件成立即整批设为 Pilot：

1. `BulletLot=1` 或 `KeyLot=1`
2. `CurCapability=LithoCapability` 且 `FuLL(RemainQ)`
3. `RequiredChuckCount=0`
4. `SplitCntMatched=0`
5. `componentqty<=6`

未命中整批条件时执行物理分批。`pi_splitcnt` 为空、非正数或大于 25 时使用默认值 4；若选片数超过当前可用 Wafer 数，回退为整批 Pilot。

Wafer 分组与排序：

- Group1：Wafer #1～#10；Group2：Wafer #11～#25。
- 有 Chuck 信息时按 C1/C2 分 SubGroup；否则按 Slot 奇偶分 SubGroup。
- GroupRank：G1-SG1=1、G1-SG2=2、G2-SG1=3、G2-SG2=4。
- 在 Group+SubGroup 内按 waferid 得到 WaferRank，最终按 `Min(WaferRank)`、`Min(GroupRank)` 选片。

### TransferFOUP 候选

- 生产 Pilot 条件：`priority<5`、`category='Production'`，且 OVL 或 CD 状态为 `PIRUNON`。
- 同 Carrier 存在 `extrastatus='WaitForJobPrep'` 的其他 Lot 时，标记需要 Change FOUP。
- Carrier 排序：`Min(RemainQ)`、`Min(Priority)`、`Max(componentqty)`、`Min(lotid)`。
- WatchDog 开启且位于 Trigger Time Slot 时，按 `TriggerCount/Time` 截取前 N 个 Carrier 输出 Report。

### Global Macro 卡控

- Pilot 位于 UnscheduledSorter：卡控同 FOUP 中不在 Sorter 的 Other Lot。
- Pilot 不在 UnscheduledSorter：卡控 Pilot，以及同 FOUP 中不在 Sorter 的 Other Lot。
- Pilot：`RemainQ<4h` 或触发 `Qu_0` 时解除。
- Other Lot 在 Litho：保持卡控。
- Other Lot 在 BARCO：`RemainQ<4h` 或触发 `Qu_0` 时解除。
- Other Lot 在其他站点：仅触发 `Qu_0` 时解除。

### LithoRule / LithoAssign 卡控

- `R2RAutoPirunControl`：非 Specify Lot，且 `Pi_SplitFlag='Y'`、R2R CD/OVL 状态为 `PIRUNON`、Pilot 非空时增加卡控。
- `Parent&ChildLotNeedRunSameTool`：非 Specify Lot 且 Pretool 非空时，取得 FutureMerge 关联子批/母批在当前 Layer 的最新作业机台；若待派机台不一致则卡控。
- LithoRule 使用需求中指定的业务表获取数据；LithoAssign 使用 Central 获取对应数据，判断逻辑保持一致。

### AMA 回退边界

- 六项复核：Lot 属于当前 FAB6/FAB8、状态为 `WaitForJobPrep`、RunCard 为空、Capability 合规、CarrierKind 为 FOUP、Report 选中 Wafer 仍属于该 Lot。Wafer 只校验归属，不额外校验状态、Slot 或 Chuck。
- 六项执行前复核失败：停止该 Lot、记录原因、等待下一轮；不得回退为整批 Pilot。
- 无可用空 FOUP：不执行物理分批，整批 Lot 传给 R2R。
- MES 分批接口失败：释放已预占 FOUP，整批 Lot 传给 R2R。
- MES 分批成功：生成子批并设为 Pilot，传给 R2R 后按现有顺序执行 Transfer FOUP。

### AMA TransferFOUP

- 按 Report 顺序逐条调用 MES TransferFOUP。
- 无可用空 FOUP、空 FOUP 数量为 0 或 MES 接口失败时，只在 AMALog 记录 Fail，再处理下一条。
- 需求未声明 TransferFOUP 失败后的额外回退或 FOUP 释放动作，流程图不作扩展推断。

## 解释边界

- 本套图只依据当前需求单描述建模，不把历史知识稿视为唯一事实来源。
- 需求原文中的 `FuLL(RemainQ)`、`Min(KeyLot)` 等表达按原文保留，未擅自修正业务含义。
- 图中概括节点的完整条件以本文件“关键规则映射”为准。

## 文件用途

- `.dot`：唯一可维护源文件。
- `.svg`：主要交付格式，适合插入 Word 和无损缩放。
- `.pdf`：打印与归档。
- `.png`：快速预览。

所有图均使用 Graphviz `dot` 引擎、黑白样式、从上到下布局和正交连接线。开始、结束和处理节点统一使用矩形，只有判断节点使用菱形。
