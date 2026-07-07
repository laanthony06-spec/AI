---
type: knowledge-note
topic: WaferBalance
tags: [自动派工, WaferBalance, QZone, QTime, WPH, RTD, DSP]
source:
  - "[[00.raw-materials/10.sources/images/WaferBalance/需求单1.jpg]]"
  - "[[00.raw-materials/10.sources/images/WaferBalance/需求单2.jpg]]"
  - "[[00.raw-materials/10.sources/images/WaferBalance/表1.jpg]]"
  - "[[00.raw-materials/90.processed/dispatch-requirements-notes/WaferBalance-需求单整理.md]]"
---

# WaferBalance 逻辑通俗介绍

## 1. 一句话说明

**WaferBalance 是 QZoneControl / RTD 派工中的一种“分配均衡”逻辑：在多个 Lot、多个机台 / Chamber 都可能作业时，把 Lot 的 wafer 数量尽量合理地分到各个可作业机台上，既避免某些机台吃太多活，也避免高 QTime 风险的 Lot 因分配不合理而 OverQtime。**

更直白一点：

> 它不是简单地把 wafer 平均分给机台，而是要看每台机台的处理能力、当前已经分到多少工作量、不同 qsort 层级之间的前后影响，然后再决定每个 Lot 应该更偏向哪台机台。

## 2. 为什么需要 WaferBalance？

在晶圆厂自动派工中，一个 Lot 到达某个 Step 时，可能有多台机台 / Chamber 可以作业。

如果只看“这台机台能不能做”，还不够。系统还要考虑：

- 这台机台当前或即将承接多少 Lot？
- 这台机台的 WPH / UPH 是否更高？
- 该 Lot 的 QTime 风险是否更紧急？
- 如果把某些 Lot 都倾向同一台机台，会不会造成局部拥堵？
- 会不会导致后面的 Lot OverQtime？

所以 WaferBalance 要解决的问题是：

> 在可作业机台集合中，如何把 wafer 数量和作业时间分得更合理，让各机台负载更均衡，同时保护 QTime 风险。

## 3. 业务背景：它和 QZone / QTime 的关系

资料中提到，`QZoneControl` 会对 loop 内的 WIP 进行 balance 处理，目的包括：

- 尽量让各机台 / Chamber 获得足够产品作业；
- 保证 Lot 不 Over QTime；
- 在 QTime loop 内对 WIP 做合理释放和分配；
- 支持产能判断。

这里的一个关键输入是 `remain qtime`。

系统会先把 loop 内 Lot 按照剩余 QTime 分成不同层级，例如：

```text
0、6、12、24
```

可以理解为不同风险层：

| qsort / category 层级 | 通俗理解 |
|---|---|
| 越小 / 越紧急 | QTime 风险越高，越需要优先考虑 |
| 越大 / 越宽松 | QTime 风险相对低，可以排在后面考虑 |

因此 WaferBalance 不是对所有 Lot 一锅端平均分，而是：

```text
先处理更紧急层级
再处理次紧急层级
再处理更宽松层级
```

## 4. 旧逻辑的问题

需求单中明确提到两个问题。

### 问题一：不同 qsort 层级之间没有联动

旧逻辑大致是：

```text
第 1 层 qsort 做一次 balance
第 2 层 qsort 再单独做一次 balance
第 3 层 qsort 再单独做一次 balance
```

问题在于：  
**每一层都像是重新开始算，没有把上一层已经分配给各机台的工作量带进来。**

这会导致一个现象：

- 第 1 层已经把很多 Lot 分给机台 A；
- 第 2 层计算时却不知道机台 A 已经很忙；
- 于是第 2 层可能继续把 Lot 分给机台 A；
- 最后机台 A 实际负载很高，但系统中每一层看起来都“挺均衡”。

这就是典型的“局部均衡，全局不均衡”。

需求单中提到，这种不合理 balance 可能导致：

- 产能判断不准确；
- 某些 Lot Over QTime；
- 例子中出现了 `Lot BPOM609 over qtime`。

### 问题二：初始化 wafer 数量用平均法，忽略机台能力差异

旧逻辑中，Lot 在各机台上的初始化作业片数由平均法得出。

例如一个 Lot 有 20 片，有 2 台机台可做，就可能先粗略分成：

```text
机台 A：10 片
机台 B：10 片
```

但实际情况可能是：

```text
机台 A WPH = 20
机台 B WPH = 25
```

机台 B 明显更快。  
如果还按 10 / 10 平均分，就没有利用机台能力差异。

所以新需求要求：

> 初始化时就要根据机台作业能力 WPH 判断，而不是简单平均。

## 5. 新逻辑的核心改进

新 WaferBalance 主要做了两件事。

### 改进一：不同 qsort 层级联动

新逻辑会把上一层级已经计算出的机台作业时间，作为下一层级的初始负载。

也就是说：

```text
第 1 层 balance 后，得到每台机台的 EQP WIP Time
第 2 层 balance 时，把第 1 层的 EQP WIP Time 带入
第 3 层 balance 时，把第 1 + 第 2 层的 EQP WIP Time 带入
```

需求单中的描述可以理解为：

```text
当前层级某机台作业所有分配 Lot 的时间
= 之前各层级中该机台作业所有分配 Lot 的时间
  + 当前层级里该机台作业所有分配 Lot 的时间
```

如果之前层级没有该机台，则初始时间为 0。

这个改进让系统不再“每层从零开始”，而是逐层累积机台负载。

### 改进二：初始化片数按 WPH 加权

新逻辑要求根据机台作业能力 `WPH` 给定 Lot 在某机台的初始化片数。

公式是：

```text
Lot 在某机台的初始化片数
= Lot QTY ×（该机台 WPH / 所有可作业机台 WPH 之和）
```

举个简单例子：

```text
Lot QTY = 20
机台 A WPH = 20
机台 B WPH = 25

WPH 总和 = 20 + 25 = 45

机台 A 初始化片数 = 20 × 20 / 45 ≈ 8.89
机台 B 初始化片数 = 20 × 25 / 45 ≈ 11.11
```

这样，处理能力更强的机台会自然分到更多 wafer。

这比简单平均的：

```text
A = 10
B = 10
```

更贴近真实产能。

## 6. 关键字段怎么理解？

| 字段 | 通俗解释 |
|---|---|
| `Lot` | 待派工批次 |
| `Qty / Lot QTY` | Lot 中 wafer 数量 |
| `Step` | 当前工艺站点 |
| `EQP` | 可作业机台 |
| `UPH / WPH` | 机台单位时间处理能力 |
| `Qty Assign` | 当前计算中分配给某机台的 wafer 数 |
| `Step WIP Time` | 某 Lot 分给某机台后预计占用的时间，通常约等于 `Qty Assign / UPH` |
| `EQP WIP Time` | 某台机台累计被分配的作业时间 |
| `Pre EQP WIP Time` | 前面 qsort 层级已占用的机台时间 |
| `Current EQP WIP Time` | 当前层级新增的机台时间 |
| `New EQP WIP Time` | 累加之后的机台总时间 |
| `Weight` | 机台权重，通常负载越低，权重越高 |
| `qsort category` | 按 QTime 风险划分的 Lot 层级 |

## 7. 算法流程：用人话走一遍

可以把 WaferBalance 想象成“给多个窗口分客户”。

窗口就是机台，客户就是 Lot，客户手里的单据数量就是 wafer 数。

### Step 1：找出每个 Lot 可以去哪几台机台

先根据 Capability、Recipe、Step、设备状态等条件，得到可作业机台集合。

例如：

```text
LotA 可去 COT002、COT003、EXP005、EXP006
LotB 可去 EXP005
LotC 可去 COT002
```

### Step 2：按 qsort / remain QTime 分层

先处理最紧急的 Lot，再处理后面的 Lot。

例如：

```text
category 6：LotA、LotB
category 12：LotC、LotD
category 24：LotE
```

### Step 3：初始化每个 Lot 在各机台上的片数

旧逻辑：平均分。  
新逻辑：按 WPH 加权分。

```text
初始化片数 = Lot QTY × 该机台 WPH / 所有可作业机台 WPH 总和
```

### Step 4：计算机台作业时间

每个 Lot 分给某机台后，会占用该机台一段时间：

```text
Step WIP Time = Qty Assign / UPH
```

机台总时间就是它承接的所有 Lot 时间相加：

```text
EQP WIP Time = Sum(Step WIP Time)
```

### Step 5：带入前一层级的机台负载

这是新逻辑最关键的点。

```text
New EQP WIP Time
= Pre EQP WIP Time + Current EQP WIP Time
```

也就是：

> 上一层已经给这台机台分了多少活，下一层必须知道。

### Step 6：根据机台负载计算权重

资料中的表格给出思路：

```text
某机台权重 = 1 / 该机台作业所有分配 Lot 的时间总和
```

通俗理解：

- 机台越忙，总时间越大，权重越小；
- 机台越空，总时间越小，权重越大。

### Step 7：按权重再次分配 wafer

再分配时：

```text
某机台再分配 Lot wafer qty
= Lot qty ×（该机台权重 / capability 下所有可作业机台权重总和）
```

这样，系统会倾向把更多 wafer 分给“更有余量”的机台。

## 8. 旧逻辑 vs 新逻辑

| 对比项 | 旧逻辑 | 新逻辑 |
|---|---|---|
| qsort 层级关系 | 各层级独立 balance | 层级之间联动，后一层继承前一层机台负载 |
| 初始化 wafer 数 | 平均分 | 按 WPH / UPH 加权 |
| 机台负载判断 | 只看当前层级 | 看历史层级累计 + 当前层级 |
| 均衡效果 | 容易局部均衡、全局不均衡 | 更接近真实机台负载 |
| QTime 风险 | 可能因误判导致 OverQtime | 更有利于避免 OverQtime |
| 产能判断 | 可能偏乐观或偏差 | 更贴近实际可承载能力 |

## 9. 一个小例子

假设某个 Lot 有 20 片，可以去两台机台：

```text
机台 A：WPH = 20
机台 B：WPH = 25
```

### 平均法

```text
A 分 10 片
B 分 10 片
```

看起来公平，但 B 比 A 快，这样并不合理。

### WPH 加权法

```text
A 分 20 × 20 / 45 ≈ 8.89 片
B 分 20 × 25 / 45 ≈ 11.11 片
```

B 能力强，因此多分一点。

如果上一层级已经让 B 承接了很多 Lot，那么下一层级再算时，B 的 `Pre EQP WIP Time` 会变大，权重会下降，系统就不会继续盲目把 Lot 往 B 上堆。

这就是“能力”和“当前负载”一起看。

## 10. 对自动派工系统的意义

WaferBalance 这类逻辑，本质上是在做一件事：

> 把“能不能做”升级为“谁更适合做”。

对 DSP / RTD 派工系统来说，它的价值包括：

- 避免只看 Capability 导致某些机台过载；
- 避免只看平均分导致高 WPH 机台能力浪费；
- 避免 qsort 层级之间互相割裂；
- 提升 QZone 内 WIP 分配合理性；
- 降低 OverQtime 风险；
- 提高产能判断准确性；
- 让派工结果更接近真实生产能力。

## 11. 实施时要注意的点

### 1. WPH / UPH 数据要可信

如果机台 WPH 配置不准，加权分配就会被带偏。

需要确认：

- WPH 是按 Tool、Chamber、Recipe、Product 还是 Step 维护？
- WPH 是否会随 Recipe、产品、批量变化？
- WPH 缺失时是否有默认值？

### 2. qsort 层级顺序必须稳定

既然后一层要继承前一层负载，那么层级处理顺序必须明确。

例如：

```text
先处理 0 / 6，再处理 12，再处理 24
```

不能顺序不稳定，否则结果可能不可复现。

### 3. 小数片数如何处理

公式会得到小数，例如 8.89 片。

系统需要定义：

- 保留小数只用于计算？
- 最后是否取整？
- 取整后总片数如何保持等于 Lot QTY？
- 是否存在最小分配单位？

### 4. Chamber 级别还是 Tool 级别

需求中提到“机台 / 腔”。需要确认 WaferBalance 的粒度：

- 是按 EQP 分？
- 还是按 Chamber 分？
- 如果一个 Tool 多 Chamber，WPH 和负载如何汇总？

### 5. 与强派 / Hot Lot / QTime 急迫度的关系

WaferBalance 是均衡逻辑，但生产中经常存在优先级更高的约束。

需要明确：

- Hot Lot 是否绕过 balance？
- QTime 极高风险 Lot 是否强制优先？
- WaferBalance 是 Filter、Sorting，还是 Prefer 逻辑的一部分？

## 12. 我对这份需求的理解

这份 WaferBalance 需求的核心不是“新增一个分片公式”这么简单，而是要把派工系统从一种较粗糙的局部均衡，升级为更贴近真实产能的全局均衡：

1. **从平均分配升级为能力加权分配**：不同机台 WPH 不同，不能一视同仁。
2. **从单层独立计算升级为跨 qsort 层级联动**：前面紧急 Lot 已经占用的机台时间，会影响后面 Lot 的 balance。
3. **从 wafer 数均衡升级为作业时间均衡**：真正要均衡的是机台负载时间，而不仅是片数。
4. **从表面均衡升级为 QTime 风险友好**：最终目标是减少不合理分配导致的 OverQtime。

如果把它放进 DSP / RTD 派工知识体系里，可以归类为：

```text
QZoneControl 下的 WIP / QTime 风险均衡逻辑
→ 通过 WPH 加权和跨 qsort 层级累计负载
→ 改善 Wafer 分配和机台负载判断
→ 避免 OverQtime 与产能误判
```

## 13. 后续可继续补充

- [ ] 用真实生产案例补充一版“旧逻辑 vs 新逻辑”的数值对比。
- [ ] 明确 qsort category 与 remain QTime 的对应关系。
- [ ] 明确 WPH 来源表和维护责任。
- [ ] 明确小数片数的取整规则。
- [ ] 明确最终逻辑在 RTD 中属于 Filter、Sorting 还是 Prefer。
- [ ] 建立测试 Case：验证跨层级继承 `Pre EQP WIP Time` 是否正确。

