# Litho Auto Split Pirun Pilot 动态挑选排序规则 v1.0

> 适用于多 Context、多候选 Lot 的 Pilot 自动挑选。每条输入数据为一个`Lot + Context`组合。

## 1. 核心原则

1. 候选 Lot 必须先通过 Auto Split Pirun 基础过滤和可作业检查。
2. 一个 Lot 只能成为一个 Context 的 Pilot；一个 Context 只能选择一个 Pilot。
3. 同一 Reticle 优先连续使用同一 STN，减少计划内 STN 切换；系统不使用 Reticle 当前物理位置。
4. 所有未选择 Context 都参与排序。非 AnchorSTN Context 只降低优先级，不过滤、不删除。
5. 每选中一个`Lot + Context`后，删除同 Lot 行和同 Context 行，保留其他行并重新计算、重新排序。
6. 机台均衡只使用实际 Pilot 数，不使用预计分配数。

## 2. 数据定义与候选范围

### 2.1 ContextKey

```text
ContextKey = STN|Reticle|Prod|Recipe|PreReticle|PreStn|Custom_Value
```

`STN`就是 Eqp，也是 Context 的固定字段。同一 Context 的所有候选 Lot 必须使用相同 STN，排序不能把 Context 改派到其他 STN。

### 2.2 唯一性

```text
LotContextUniqueKey = LotID|STN|Reticle
```

| 情形 | 处理 |
| --- | --- |
| `LotContextUniqueKey`和`ContextKey`均相同 | 合并重复记录 |
| 相同`LotContextUniqueKey`对应不同`ContextKey` | 记录`ContextMappingConflict`，不参与自动选择 |
| 同一 Lot 出现在多个 Context | 允许参与排序，但最终只能被一个 Context 选中 |

### 2.3 候选范围

进入循环前完成以下处理：

| 检查项 | 要求 |
| --- | --- |
| Pirun Loop RC / Future Hold | 排除 |
| Lot Status | 必须为 Active |
| Specify Lot | 排除 |
| CSN、PPID、Recipe、Capa、Global、R2R Context | 必须通过可作业判断 |
| 已被其他 Context 配置为有效 Pilot 的 Lot | 排除 |
| 已存在有效 Pilot 的 Context | 不再参与本轮选择 |

## 3. 排序规则

### 3.1 同 Context 内 Lot 排序：RTDRank

| 顺序 | 字段 | 方向 | 定义 |
| ---: | --- | :---: | --- |
| 1 | `DistanceToLitho` | ASC | 距离 LITHO 站点越近越优先 |
| 2 | `SplitCntMatched` | DESC | `LotWaferCount >= pi_splitcnt`时为 1 |
| 3 | `ChuckMatched` | DESC | `Chuck1 >= 2 AND Chuck2 >= 2`时为 1 |
| 4 | `EmptyEqpPort` | DESC | 空机空 Port Lot 为 1 |
| 5 | `HasPositiveRemainQtime` | DESC | `RemainQtime > 0`时为 1 |
| 6 | `RemainQtimeSort` | ASC | 仅比较正值，越小越优先；空值最后 |
| 7 | `IsKeyLot` | ASC | Key Lot 为 1，因此可参与但不优先 |

```text
RTDRank = DENSE_RANK() OVER (
    PARTITION BY ContextKey
    ORDER BY
        DistanceToLitho ASC,
        SplitCntMatched DESC,
        ChuckMatched DESC,
        EmptyEqpPort DESC,
        HasPositiveRemainQtime DESC,
        RemainQtimeSort ASC NULLS LAST,
        IsKeyLot ASC
)
```

RTDRank 只表示同一 Context 内的 Lot 优先级。Lot 状态、RemainQtime、空机空 Port 等业务字段变化时重新计算；使用固定快照时可在任务开始时计算一次。

### 3.2 ReticleAnchorSTN

`ReticleAnchorSTN`表示某块 Reticle 当前计划优先连续处理的 STN。系统拿不到 Reticle 当前物理位置，因此初始 Anchor 和后续切换均按以下顺序确定：

| 顺序 | 字段 | 方向 |
| ---: | --- | :---: |
| 1 | `RemainingReticleSTNContextCount` | DESC |
| 2 | `ActualSTNPilotCount` | ASC |
| 3 | `BestSTNRTDRankScore` | ASC |
| 4 | `STN` | ASC |

AnchorSTN 上仍有未选择 Context 时保持不变；没有剩余 Context 时，才从同一 Reticle 的其他 STN 中选择下一 AnchorSTN。

### 3.3 动态指标

| 指标 | 定义 |
| --- | --- |
| `ContextCandidateCount` | 当前 Context 剩余的不同 Lot 数 |
| `RemainingReticleSTNContextCount` | 当前`Reticle + STN`下尚未选出 Pilot 且仍有候选 Lot 的 Context 数 |
| `ReticleSTNRank` | Context.STN 等于 ReticleAnchorSTN 时为 0，否则为 1 |
| `ActualSTNPilotCount` | 本轮开始前有效 Pilot Context 数 + 本轮实际已选 Pilot Context 数 |
| `BestRemainingRTDRank` | 当前 Context 剩余候选 Lot 中最小的 RTDRank |
| `BestSTNRTDRankScore` | 当前`Reticle + STN`下各剩余 Context 的`BestRemainingRTDRank`平均值 |
| `LotContextCount` | 当前同一 Lot 可匹配的不同 Context 数 |
| `OtherContextOnlyCandidateCount` | 除当前 Context 外，只剩该 Lot 一个候选的 Context 数 |

`ReticleSTNRank`只影响排序：非 AnchorSTN Context 始终保留在排序集合中。

### 3.4 ContextOrder

所有尚未选出 Pilot、仍有候选 Lot 且满足可执行条件的 Context 参加排序：

排序顺序：`ReticleSTNRank ASC` → `ContextCandidateCount ASC` → `RemainingReticleSTNContextCount DESC` → `ActualSTNPilotCount ASC` → `BestRemainingRTDRank ASC` → `ContextKey ASC`。

### 3.5 当前 Context 的 Lot 排序

取`ContextOrder = 1`后，对该 Context 的剩余 Lot 排序：

排序顺序：`RTDRank ASC` → `OtherContextOnlyCandidateCount ASC` → `LotContextCount ASC` → `LotID ASC`。

先遵循 RTDRank；同级时避免占用其他 Context 的唯一候选，再优先选择适用 Context 较少的 Lot，最后按 LotID 保证结果稳定。

## 4. 动态循环

| 步骤 | 处理 |
| ---: | --- |
| 1 | 初始化`SelectedLots`、`SelectedContexts`、`ActualSTNPilotCount`和各 Reticle 的 AnchorSTN |
| 2 | 重新计算 RTDRank、动态指标和 ReticleSTNRank |
| 3 | 更新 AnchorSTN：仍有剩余 Context 则保持，否则按 Anchor 规则切换 |
| 4 | 对全部未选 Context 生成 ContextOrder，取第一名 |
| 5 | 对该 Context 的 Lot 排序，取第一名作为 Pilot |
| 6 | 写入 SelectedLots、SelectedContexts，并将对应 STN 的 ActualSTNPilotCount 加 1 |
| 7 | 删除所有同 Lot 行和同 Context 行；其他未选择行全部保留 |
| 8 | 返回步骤 2，直到没有可选 Context |

## 5. 完整示例

### 5.1 示例条件

| 项目 | 值 |
| --- | --- |
| Context / Reticle / STN | 9 个 / 3 块 / E1、E2、E3 |
| 候选记录 | 24 条`Lot + Context` |
| `pi_splitcnt` | 4 |
| 初始有效 Pilot 数 | E1=0，E2=1，E3=0 |
| Reticle 当前位置 | 无法取得，不参与排序 |
| 共享 Lot | L04、L06、L11、L13 |

### 5.2 Context 数据

| Context | STN | Reticle | Prod | Recipe | PreReticle | PreStn | Custom_Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | E1 | RET-A | P-A | RCP-01 | PRE-A | BARC-A | CV-01 |
| C02 | E1 | RET-A | P-B | RCP-01 | PRE-A | BARC-A | CV-02 |
| C03 | E2 | RET-A | P-C | RCP-02 | PRE-A | BARC-B | CV-03 |
| C04 | E1 | RET-B | P-D | RCP-03 | PRE-B | BARC-A | CV-01 |
| C05 | E2 | RET-B | P-E | RCP-03 | PRE-B | BARC-B | CV-02 |
| C06 | E2 | RET-B | P-F | RCP-04 | PRE-B | BARC-B | CV-03 |
| C07 | E1 | RET-C | P-G | RCP-05 | PRE-C | BARC-C | CV-01 |
| C08 | E2 | RET-C | P-H | RCP-05 | PRE-C | BARC-C | CV-02 |
| C09 | E3 | RET-C | P-I | RCP-06 | PRE-C | BARC-D | CV-03 |

### 5.3 候选 Lot 与初始 RTDRank

| Context | STN | Lot | Distance | Wafer | Chuck1/2 | EmptyPort | RemainQtime | KeyLot | RTDRank |
| --- | --- | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| C01 | E1 | L01 | 1 | 25 | 3/3 | 0 | 40 | 0 | 2 |
| C01 | E1 | L02 | 1 | 25 | 3/3 | 0 | 20 | 1 | 1 |
| C01 | E1 | L03 | 2 | 25 | 4/4 | 1 | 10 | 0 | 3 |
| C02 | E1 | L04 | 1 | 25 | 3/3 | 0 | 30 | 0 | 1 |
| C02 | E1 | L05 | 1 | 6 | 1/2 | 1 | 5 | 0 | 2 |
| C03 | E2 | L06 | 1 | 25 | 2/2 | 0 | 60 | 0 | 2 |
| C03 | E2 | L07 | 1 | 25 | 3/3 | 1 | 10 | 0 | 1 |
| C03 | E2 | L08 | 2 | 25 | 3/3 | 1 | 5 | 0 | 3 |
| C04 | E1 | L04 | 1 | 25 | 3/3 | 0 | 30 | 0 | 2 |
| C04 | E1 | L09 | 1 | 25 | 3/3 | 0 | 15 | 0 | 1 |
| C04 | E1 | L10 | 2 | 25 | 3/3 | 1 | 5 | 0 | 3 |
| C05 | E2 | L06 | 1 | 25 | 2/2 | 0 | 60 | 0 | 2 |
| C05 | E2 | L11 | 1 | 25 | 2/2 | 1 | 30 | 0 | 1 |
| C06 | E2 | L12 | 1 | 25 | 3/3 | 0 | 50 | 0 | 2 |
| C06 | E2 | L13 | 1 | 25 | 3/3 | 0 | 15 | 0 | 1 |
| C06 | E2 | L14 | 2 | 25 | 3/3 | 1 | 5 | 0 | 3 |
| C07 | E1 | L11 | 1 | 25 | 2/2 | 1 | 30 | 0 | 2 |
| C07 | E1 | L15 | 1 | 25 | 2/2 | 1 | 20 | 1 | 1 |
| C07 | E1 | L16 | 2 | 25 | 4/4 | 1 | 5 | 0 | 3 |
| C08 | E2 | L17 | 1 | 25 | 3/3 | 0 | 20 | 0 | 1 |
| C08 | E2 | L18 | 1 | 3 | 1/1 | 1 | 5 | 0 | 2 |
| C09 | E3 | L13 | 1 | 25 | 3/3 | 0 | 15 | 0 | 2 |
| C09 | E3 | L19 | 1 | 25 | 3/3 | 0 | 10 | 0 | 1 |
| C09 | E3 | L20 | 2 | 25 | 4/4 | 1 | 5 | 0 | 3 |

### 5.4 初始 AnchorSTN 与 ReticleSTNRank

| Reticle | 各 STN 剩余 Context | 初始 AnchorSTN | 选择依据 |
| --- | --- | --- | --- |
| RET-A | E1:2；E2:1 | E1 | E1 的 Context 更多 |
| RET-B | E1:1；E2:2 | E2 | E2 的 Context 更多 |
| RET-C | E1:1；E2:1；E3:1 | E1 | 数量相同；E1、E3 实际 Pilot 数较少，再按 STN 升序 |

| Reticle | `ReticleSTNRank = 0` | `ReticleSTNRank = 1` |
| --- | --- | --- |
| RET-A | C01、C02@E1 | C03@E2 |
| RET-B | C05、C06@E2 | C04@E1 |
| RET-C | C07@E1 | C08@E2、C09@E3 |

Rank 1 Context 仍参与排序且数据保留；只有同 Lot 或同 Context 命中删除规则时才删除。

### 5.5 动态挑选过程

| 步骤 | Context | AnchorSTN | 候选数 | Pilot Lot | RTDRank | 共享行变化 | 选择后实际 Pilot 数 |
| ---: | --- | --- | ---: | --- | ---: | --- | --- |
| 1 | C02 | RET-A→E1 | 2 | L04 | 1 | 删除 C04-L04 | E1=1，E2=1，E3=0 |
| 2 | C05 | RET-B→E2 | 2 | L11 | 1 | 删除 C07-L11 | E1=1，E2=2，E3=0 |
| 3 | C07 | RET-C→E1 | 2 | L15 | 1 | 无 | E1=2，E2=2，E3=0 |
| 4 | C09 | RET-C→E3 | 3 | L19 | 1 | C09-L13 随 Context 删除 | E1=2，E2=2，E3=1 |
| 5 | C01 | RET-A→E1 | 3 | L02 | 1 | 无 | E1=3，E2=2，E3=1 |
| 6 | C06 | RET-B→E2 | 3 | L13 | 1 | 无 | E1=3，E2=3，E3=1 |
| 7 | C04 | RET-B→E1 | 2 | L09 | 1 | L04 已删除 | E1=4，E2=3，E3=1 |
| 8 | C08 | RET-C→E2 | 2 | L17 | 1 | 无 | E1=4，E2=4，E3=1 |
| 9 | C03 | RET-A→E2 | 3 | L07 | 1 | 无 | E1=4，E2=5，E3=1 |

步骤 3 后，RET-C 在 E1 已无剩余 Context。E2、E3 均剩 1 个 Context，但 E3 的实际 Pilot 数更少，因此下一 AnchorSTN 为 E3，C09 的 ReticleSTNRank 从 1 更新为 0。

### 5.6 最终结果

| Reticle | Context | STN | Pilot Lot | RTDRank |
| --- | --- | --- | --- | ---: |
| RET-A | C01 | E1 | L02 | 1 |
| RET-A | C02 | E1 | L04 | 1 |
| RET-A | C03 | E2 | L07 | 1 |
| RET-B | C04 | E1 | L09 | 1 |
| RET-B | C05 | E2 | L11 | 1 |
| RET-B | C06 | E2 | L13 | 1 |
| RET-C | C07 | E1 | L15 | 1 |
| RET-C | C08 | E2 | L17 | 1 |
| RET-C | C09 | E3 | L19 | 1 |

| Reticle | 计划 STN 顺序 | 计划内切换次数 |
| --- | --- | ---: |
| RET-A | E1 → E2 | 1 |
| RET-B | E2 → E1 | 1 |
| RET-C | E1 → E3 → E2 | 2 |

切换次数不包含 Reticle 未知初始位置到首个 AnchorSTN 的搬送。

## 6. 无 Pilot Context 修复

循环结束后，如 Context 因共享 Lot 被占用而无 Pilot，可执行一次换 Lot 修复。仅当替换能增加获得 Pilot 的 Context 总数，且新 Lot 仍满足基础条件时才调整。

| Context | 原候选 | 原结果 | 修复后 |
| --- | --- | --- | --- |
| C01 | L01、L02 | C01→L01 | C01→L02 |
| C02 | L01 | 无 Pilot | C02→L01 |

调整后重新校验 AnchorSTN、Lot 唯一性和 RTDRank。

## 7. 异常与边界

| 情形 | 处理 |
| --- | --- |
| Context 无候选 Lot | 记录`NoEligiblePilot`，不绕过过滤条件 |
| AnchorSTN 上无有效 Context | 按剩余 Context 重新选择 AnchorSTN |
| Context、Lot 或 Anchor 相关状态变化 | 停止下放，更新指标后重新排序 |
| Lot 被并发任务选中 | 通过原子占用或唯一性校验；失败方移除该 Lot 后重排 |
| Lot Status、Hold、FOUP、Wafer、R2R 状态变化 | 标记为不可选并重排，保留记录 |
| 所有排序条件相同 | 按 ContextKey、LotID 升序保证结果稳定 |

## 8. 排序总览

| 层级 | 排序顺序 |
| --- | --- |
| AnchorSTN | `RemainingReticleSTNContextCount DESC` → `ActualSTNPilotCount ASC` → `BestSTNRTDRankScore ASC` → `STN ASC` |
| ContextOrder | `ReticleSTNRank ASC` → `ContextCandidateCount ASC` → `RemainingReticleSTNContextCount DESC` → `ActualSTNPilotCount ASC` → `BestRemainingRTDRank ASC` → `ContextKey ASC` |
| 当前 Context 的 Lot | `RTDRank ASC` → `OtherContextOnlyCandidateCount ASC` → `LotContextCount ASC` → `LotID ASC` |

每轮只删除同 Lot 和同 Context 行；其他未选择行保留并参与下一轮排序。
