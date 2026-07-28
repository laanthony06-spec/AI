# STNLoadingBalance 需求单 v0.8 优化建议

> 基于 `STNLoadingBalance需求单_优化稿_v0.7修改后.docx`、内容提取稿及用户确认记录整理。  
> 本轮已按建议执行，生成 v0.8 优化版。

## 1. 字段名统一

当前文档中存在 `WIPLoading_Avg / WIPLoading_avg`、`PriorWIPLoading / PriorityWIPLoading`、`PriorWIPloading_Avg / PriorityWIPLoading_avg` 等混用风险。

按用户确认，正式字段统一为：

```text
WIPLoading_Avg
PriorWIPLoading
PriorWIPloading_Avg
```

v0.8 已统一为上述字段名。

## 2. Timeline 表达改为“可配置层级”

当前层级为：

```text
0、2、6、12、24
```

但需求本质是层级可配置，后续可能增加到 6 个或 8 个层级。

v0.8 已调整为：

```text
系统按配置的 Timeline 层级执行 Loading 计算。当前配置层级为 0、2、6、12、24；后续新增层级时，计算逻辑按配置自动扩展。
```

## 3. PM_RemainTime 定义补清楚

原稿中 PM_RemainTime 容易被理解为每个 Lot / 每次 Balance 重复累加。

用户已确认：

```text
PM_RemainTime = Lot 到站前，机台因 PM / 借机不能提供作业的时长。
```

同一机台、同一 PM 计划、同一 Timeline 层级下，`PM_RemainTime` 相同。

v0.8 已按该定义改写。

## 4. Priority Loading 无数据时输出 0

原稿中保留了“0 或空值【待确认】”。

用户已确认输出：

```text
0
```

v0.8 已删除待确认表述。

## 5. EqpLotSummary 字段含义补充

v0.8 已补充：

| 字段 | 含义 |
| --- | --- |
| `PiecesPreStation` | Lot 分配到该机台的片数 |
| `LoadingPreStation` | 机台作业 Lot 分配片数所需时间，等于 `PiecesPreStation / UPH` |
| `LotAttInfoSite` | Lot 当前所在厂 |
| `CurrentInfoSite` | Lot 在该站实际作业厂 |
| `EqpSite` | 机台所在厂 |

## 6. 语言风格优化

v0.8 已按工程化规则处理：

- 删除“本需求旨在 / 通过……从而……”类表达。
- 将长解释压缩为变更说明。
- 保留表名、字段名、判断条件和输出结果。
- 保留必要 NOTE，不新增未确认逻辑。

## 7. 仍建议后续确认

以下内容本轮未擅自补充：

- `MFGControl` 的具体判断规则。
- `Important Lot` CSV 配置的维护位置、字段格式和生效范围。
- `PW Lot 后续 50 站` 的配置来源和默认值。
- `WPHLoss` 在本需求中的具体复用方式是否完全沿用既有逻辑。
