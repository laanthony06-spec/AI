---
type: knowledge-extraction
topic: DSP派工系统简介
tags: [DSP, 自动派工, 派工规则, QZone, AMHS, NPW, MES]
---

# DSP 派工系统简介 - 派工系统知识提取

## 一句话理解

DSP 派工系统围绕 RTD（实时派工）与 AMA（自动派工管理）展开：RTD 负责在实时约束下筛选、排序、推荐 Lot 与机台；AMA 负责派工触发、最终核对、NPW 自动化、搬送存储等管理流程，并与 MES、EAP、MCS、APC、PMS 等系统协同。

## 系统边界与角色

- **RTD / Real-Time Dispatching**：执行实时派工逻辑，处理 Lot、FOUP、Machine、Port、Recipe、Capability、QTime、QZone 等约束。
- **AMA / Auto Move or Auto Dispatch Management**：承担派工触发、结果核对、Lot Pre-reserve、NPW 管理等自动化功能。
- **MES**：提供 Lot 状态、工艺路线、Recipe、Hold、Comment、RTDInfo 等生产执行数据。
- **EAP / MCS / AMHS**：承接设备自动化与搬送任务，影响 FOUP 到机台 Load Port 的到达效率。
- **APC / PMS**：提供过程控制、设备状态、PM / Clean / R2R 等约束信息。

## 核心派工链路

```text
触发事件 / 定时扫描
  → 获取可派工 Lot 与设备状态
  → Global Rule 过滤
  → Local Rule 过滤
  → QZone / QTime / Capacity 检查
  → 排序与优先级计算
  → Reserve / Pre-reserve
  → 搬送与 Load Port 上料
  → 异常原因回写与查询
```

## Global 派工规则

参考页：p010、p063、p006、p012、p013、p014、p015、p016、p018、p020、p021、p022、p023、p026 等

Global Rule 是跨 Module 通用的派工过滤逻辑，关注整体控线角度，而非单一设备作业方式。典型检查包括：

- Lot 状态是否 OK
- FOUP 状态是否 OK
- Recipe 是否被 DSP 禁止
- Reticle 是否在机台或可用
- Machine / Chamber 是否处于可作业状态
- 是否存在 Constraint、BatchID、Runcard 指定机台、Multi Lot in One FOUP 等限制
- 是否被 QZone、Capacity、Path issue、下游断线或堆货限制

## Local 派工规则

参考页：p017、p019、p024、p025、p062

Local Rule 根据不同 Module 的设备特性与工艺限制设计。OCR 中出现的典型区域包括：

- **LITHO**：Reticle、R2R、DomaPath、高低能、垂直限定、放版指导。
- **ETCH**：DomaPath、R2R、Recipe 连续作业、Lot 可作业性与紧急程度。
- **TF**：Recipe 连续、Film 连续、连续上限、同条件 WIP、累计膜厚 Clean、瓶颈机台、ALL-SGE。
- **CMP**：Recipe 连续、R2R、PM Cycle 内同条件连续、TRIM LifeTime、CCU 错开 PM。
- **WET**：Chamber / Batch 两类逻辑，以及 WET-DIFF、WET-SGE 相关派工。

## QZone / QTime 管控

参考页：p006、p012、p013、p014、p015、p016、p018、p020、p021、p022、p023、p026 等

QZone 管控用于判断 Q-Time loop 起始站点的 Lot 是否可以继续放货，核心是防止下游断线、堆货或 QTime 风险扩大。

关键概念：

- **QTime Duration**：允许等待时间窗口。
- **QTime Urgency**：Lot 剩余 QTime 风险等级。
- **Remain WIP / WIP Limit**：QZone 中各站点或能力组允许的放货量。
- **Path issue / Capacity issue**：下游路径断线或产能不足导致的卡控。
- **Safety Value**：连环 QZone 出现断线或堆货时的风险分级与特殊管控。

## AMHS 与搬送存储

参考页：p004、p005、p007、p008、p009、p027、p028、p029、p030、p031、p032、p033 等

AMHS 相关内容包括 Stocker、OHB、MCS、搬送路径、预搬送等。搬送存储的目标不是单纯移动 FOUP，而是配合派工减少设备空等、缩短搬送路径、降低搬送系统负荷并提升设备利用率。

需要特别关注：

- Stocker / OHB 的临时存储能力
- FOUP 从当前站点到下游设备的搬送时间
- Load Port 可用性
- 堆货机台或瓶颈机台的预搬送策略
- AMHS 派工与机台派工之间的联动

## NPW 自动化

参考页：p050、p051、p052、p053、p054、p055、p056、p057、p058、p060、p061、p065 等

NPW 自动化覆盖 Routine Monitor、复机 NPW、Season、Dummy、Reuse、Recycle、Downgrade、Auto Reassign、IMP Monitor、THK NPW Auto Handle 等场景。

可以抽象为四类问题：

1. **何时分批**：By time、weekly、apply time、WAIT MFG、PM / TRC 流程等触发条件。
2. **如何筛选母批 / 子批**：按 Filter rule、产品、设备、状态、使用次数、Recipe、Monitor group 过滤。
3. **如何派工或复用**：Reserve、Reuse、Recycle、Downgrade、Auto Reassign。
4. **失败如何处理**：Auto Handle Fail、自动 Hold、Cancel Control ID、异常原因追踪。

## OverQtime 原因分析

参考页：p001、p002、p003、p011

OverQtime 分析关注长时间未派工产品在日志中的卡控原因，重点查明：

- 是否被 Assign 卡控不派工
- 是否未进入预排
- 是否受 QZone / QTime / Capability / Recipe / 设备状态限制
- 具体 OverQtime 时间、站点和卡控原因

## 可沉淀为派工系统设计原则

- 派工系统不是简单排序，而是“可作业性过滤 + 风险管控 + 优先级排序 + 搬送协同”。
- Global Rule 解决共性约束，Local Rule 解决 Module / Tool 特有约束。
- QZone 是控线与局部最优之间的关键平衡器。
- AMHS 决定派工结果能否及时落地，尤其影响瓶颈机台空等。
- NPW 自动化需要把生产、设备、工艺、监控片生命周期联动起来。
- 异常查询能力与派工能力同等重要；没有 reason trace，派工系统难以维护。

## 后续建议建立的专题笔记

- [[DSP 派工系统]]
- [[RTD 实时派工逻辑]]
- [[AMA 自动派工管理]]
- [[QZone 管控模型]]
- [[AMHS 与派工联动]]
- [[NPW 自动化管理]]
- [[OverQtime 原因分析]]