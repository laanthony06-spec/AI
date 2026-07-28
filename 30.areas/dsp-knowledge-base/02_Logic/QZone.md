# QZone / QTime 管控

> 来源：自动派工系统培训 PPT，`00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p035.jpg` ~ `PPT49.jpg`、`PPT91.jpg`。

## 相关术语

### QTime duration

生产过程中在规定时间（QueueTime）内完成特殊工艺区间段的作业过程。

### QZone

在 Q-time 区间外对区间内 WIP 限额，保证区间内设备有足够 WIP，但不过时。

### Qzone 方式

- Min qtime：规定动作结束后，可以继续下一站作业的最小等待时间。
- Max qtime：规定时间内完成承接工艺的最大允许时间。

## 管控内容

PPT 中 QZone 管控内容包含：

- Loop 外产品作业管控；
- Loop 内产品作业管控；
- 每个 Lot 在 qtime 范围内作业时 loop；
- Lot 作业不影响出货 / 瓶颈后 Lot 的作业。

## 考量因素

- 瓶颈站点
- 设备数量
- 设备状态
- 设备作业能力
- 设备作业方式
- 设备维护计划
- 工艺限定
- QT 时限
- QT 类型
- QT 结束方式
- Loop 内 WIP 量
- Loop 内 WIP remain QT

## 模型结构

1. 数据准备：获取各制程作业时间 Process Time、机台状态、作业条件、限定信息和可用资源。
2. 信息整合：获取 Normal / Branch Flow 信息；获取 Qtime 信息，包括起始 / 结束站点、qtimelimit、qtimetype 等。
3. 模型计算：根据 Lot 真实 Qtime Flow 信息，按一定逻辑判断处于 Qtime 起始站点的 Lot 能否派工。

## 管控逻辑

QZone 逻辑中出现三个核心模块：

- Constraint
- Qzone Result
- Exception

其中，QZone 对下游产能与放货风险的判断会用到 WaferBalance 逻辑，用于平衡各机台 loading 并判断待派工 Lot 放入 loop 后是否会导致当前 Lot 或其他 Lot over qtime。详见 `WaferBalance.md`。

### Constraint

用于判断每个 product 在每个站点机台 recipe 的作业情况。

常见判断内容：

- 机台是否满足 Recipe；
- Recipe 是否被 inhibit / hold / disable。

### Qzone Result

用于判断 QZone 中每个站点、每个机台的产能情况。

常见判断内容：

- 机台产能；
- capability 开关；
- EQP state；
- communicate mode；
- QZone 中每个 Lot 分配在该机台上的 wafer 数总和。

### Exception

用于忽略某些设备站点的 QZone 管控。

常见判断内容：

- 白名单；
- Safety value 判断。

## Safety Value

Safety Value 用于对连续 QZone 下游出现断线或堆货时，根据各 QZone 的风险程度进行特殊管控。

PPT 中 SafetyValue 定义从 0 到 9，风险大致可分为：

- 无风险；
- 低风险；
- 中风险；
- 高风险。

具体数值含义、QT 类别、建议处置方式需在具体需求中按 PPT 原页或现行规则确认。

## Loop Lot Control

特殊 QZone loop 需要特殊管控方式。

PPT 中出现的管控形式：

- By Begin：管控起始站点同时在作业 WIP 的总产品数量；
- By Loop：管控起始站点（在作业 WIP）至结束站点（所有 WIP）的总产品数量；
- By End：管控结束站点（所有 WIP）的总产品数量。

WIP 统计形式包括：

- LOT COUNT
- WAFER COUNT
- FOUP COUNT

产能计算方式包括：

- 固定（与机台状态无关）
- 动态（随机台状态变化）

## Over Qtime 原因分析

PPT91 中 Over Qtime 原因分析涉及：

- 是否进入 loop 后 over；
- 当前站点是否 block qtime；
- QZone 是否卡控下游；
- QZone 下游产能是否足够；
- 是否需要 Season；
- Qtime 内是否有测量站点；
- constraint / 机台 state / PM flag / capability 开关 / Recipe-PPID OK / WPH 是否维护 / ENG CONTROL 等。

## 关联知识

- `WaferBalance.md`：QZone 中用于机台 loading 平衡和放货判断的核心计算逻辑。
- `Qsort.md`：Lot 到计算站点的最大允许等待时间计算逻辑。
- `WPHLoss.md`：QZone 获取 WPH 后，对复合机台 chamber 缺失造成的实际产能损失进行修正。
- `PM_Control.md`：QZone PM 管控、PM Start / End 修正、PM delay 与 MFG Prefer 对厂 PM 判断。

## Qsort

QZone 中 qsort 表示 Lot 到计算站点的最大允许等待时间。Lot 必须在 qsort 时间内到达计算站点并上机台作业，否则 Lot 良率可能受到影响。

qsort category 固定划分为：

```text
0、6、12、24
```

qsort 由 Qtime 和站点 ProcessTime 计算得到。具体计算逻辑已单独沉淀到 `Qsort.md`。若涉及 PM 管控，到站时间按 `PM_Control.md` 中的 CycleTime 累计逻辑处理，不再套用原 Qsort 判断口径。
