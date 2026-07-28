# RTD

> 来源：自动派工系统培训 PPT，`00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p005.jpg`、`PPT6.jpg`、`PPT13.jpg`、`PPT16.jpg`、`PPT19.jpg`、`PPT21.jpg`、`PPT24.jpg`、`PPT32.jpg` 等。

## 定位

RTD（实时派工系统 / Real Time Dispatch）用于根据实时状态进行派工决策。它应用调度参考结果，检测实时限制并执行各区域派工规则，将产品派工到设备上。

RTD 的核心关注是：

- 当前 Lot 是否可派；
- 可派到哪些 Machine / Port / Chamber；
- 按什么规则筛选和排序；
- 派工结果、Reason、RTD Info 如何输出；
- Where Next 时 Lot / FOUP 应该搬送到哪里。

## 基本功能链路

PPT 中 RTD Basic Functions 包含：

1. Global Filter
2. Local Filter
3. Global Sorter
4. Local Sorter
5. Sorting
6. Where Next

## Global Filter

所有设备共通逻辑，筛选掉不能派工的 Lot。常见因素：

- Lot / Foup / Machine / Port State
- Qtime Zone Control / Run Path
- Inhibit Check
- NPW 时效性管控

## Local Filter

各设备群专用逻辑，根据设备特性筛选不能派工的 Lot。常见因素：

- Port 绑定的 Capability / Recipe
- Buffer 空间
- R2R Result

## Global Sorter

通用规则定义 Lot 排序因素，例如：

- Remain Q-time
- Global Rank
- Breaking
- Target Lot
- Request T/R

## Local Sorter

各设备群根据设备特性单独定义 Lot 排序因素，例如：

- 源 / 目标中可连续性
- 制品温度调整
- 可组批性
- Chamber 利用率

## Sorting

各设备根据 Sorter 的重要性对 Lot 进行综合排序，部分排序结果可用于导出。

## Where Next

Where Next 根据 Lot 的下一站点信息和 Stocker 的存储状态，选择 Lot 的最佳存储位置。

## 区域派工规则

PPT 中出现的区域派工规则包括：

- Global 派工规则
- LITHO 派工规则
- ETCH 派工规则
- TF 派工规则
- CMP 派工规则
- WET 派工规则

各区域规则通常会结合区域 Process 机台作业特性，设计 Reason / Sorting / Local Rule。

## 与 AMA 的边界

- RTD 偏实时派工决策：当设备请求派工、Load Port 空闲或 Where Next 需要决策时，RTD 根据实时状态、规则和优先级选择 Lot / FOUP / 存储位置。
- AMA 偏自动化任务和周期 / 事件触发：负责 Lot Reserve、NPW 准备、Pre-send、Monitor / Season / Dummy / Reuse / Recycle 等自动处理流程。

## 与 MCS / MES 的交互

- RTD 可通过 MES 发送搬送指令 Call MCS 执行搬送。
- RTD 在搬送流程中可根据工艺需求、设备位置、OHB / Stocker 空闲情况，决定 Lot / FOUP 存储位置。
- 具体字段和接口以实际需求为准。

