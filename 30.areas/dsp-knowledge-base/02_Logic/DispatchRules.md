# 派工规则总览

> 来源：自动派工系统培训 PPT，`00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p013.jpg` ~ `PPT25.jpg`。

## Global 派工规则

Global Rule 指各 Module 通用的 DSP 派工逻辑，从整体控线角度出发，确定最优调度方案。

它考虑：

- Lot 基本属性；
- Foup 属性；
- 机台状态；
- 工艺限定；
- 与具体机台作业方式无关的通用约束。

## 常见 Global Reason / Sorting

PPT 中出现的功能包括：

- Get Lot list From MES
- Check Machine
- Multi Lot In One Foup
- Check Qzone Control
- Check Loop Lot Control
- Check MFG control
- Reserve Lot
- Cancel Lot
- AMA Mark Lot
- Qtime Urgency
- Priority
- Rush Lot
- Target Lot
- Broken Lot
- MFG Control
- Rework Lot
- Sub Lot
- Small Lot
- Remain Qtime
- Rework Lot RQ Pri
- Waiting Time

## LITHO 派工规则

LITHO 规则综合考虑：

- Reticle
- R2R
- DomaPath
- 高低能
- 垂直限定

目标是限制 Lot 在机台上的可作业性，并结合预排程制定符合 LITHO 区域设备特性的自动派工逻辑。

## ETCH 派工规则

ETCH 规则结合 ETCH 区域 Process 机台作业特性，综合考虑：

- DomaPath
- R2R
- 限制 Lot 在机台上可作业性的各种因素。

目标是判断 Lot 的可作业性和紧急程度，并制定符合 ETCH 区域特性的自动派工逻辑。

## TF 派工规则

TF 规则结合 TF 区域 Process 机台作业特性，综合考虑：

- Recipe 连续
- Film 连续
- 连续上限
- 同条件 WIP 量
- 累计膜厚 Clean
- 瓶颈机台等因素。

## CMP 派工规则

CMP 规则综合考虑：

- Recipe 连续
- R2R
- PM Cycle
- 向条件连续
- TRIM 机台 LifeTime 控货
- CCU 机台合并开 PM 等因素。

## WET 派工规则

WET 分为 Chamber / Batch 两种类型，因此分为两部分逻辑。

WET 区域派工逻辑不仅对 WET 本身使用，也迁移了部分 WET-DIFF、WET-SGE 产品的派工逻辑。

### Multi Chamber WET 管控逻辑

- Global 功能
- PPID 选择
- WET-DIFF 管控
- Port 绑定
- PRF-SGE 管控
- 高低温机台切换

### WET Batch 管控逻辑

- Global 功能
- PPID 选择
- Buffer 数量
- Batch 填充率

