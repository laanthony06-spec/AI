---
type: dispatch-requirement-note
source_folder: Qsort
topic: Qsort / 派工排序
tags: [自动派工, 需求单, OCR, 需求整理]
---

# Qsort - 需求单整理

## 资料概况

- 原始图片目录：[[00.raw-materials/10.sources/images/Qsort]]
- OCR 输出目录：[[00.raw-materials/90.processed/dispatch-requirements-ocr/Qsort]]
- 图片数量：4
- 初步主题：Qsort / 派工排序
- 处理状态：已 OCR，已建立初步结构化笔记
- 注意：本笔记基于 OCR 自动识别，关键需求点需回看原图确认。

## 自动识别到的关键信号

- 系统对象：Lot, Recipe, Step
- 派工逻辑：Qsort
- 约束条件：Capability, QTime, QZone

## 需求理解（初稿）

- 该组资料疑似围绕 Qsort 或派工排序值计算展开。
- 需要重点确认：排序因子、权重、优先级、Tie-breaker、与 QTime / WIP / Due Date / Hot Lot 的关系。
- 对派工系统的影响：Qsort 决定候选 Lot 通过过滤后的最终派工顺序。

## 待澄清问题

- [ ] 需求目标是什么：提升产能、降低 Cycle Time、减少 OverQtime、降低 WPH Loss，还是提升自动化率？
- [ ] 输入数据来自哪些系统：MES、RTD、AMA、EAP、MCS、APC、PMS？
- [ ] 规则属于 Global Rule、Local Rule，还是排序 / Prefer 逻辑？
- [ ] 需要新增哪些异常原因码或查询页面？
- [ ] 验收标准是什么：测试 Case、前后对比指标、上线影响范围？

## 分页 OCR 摘录

### 第 001 张：1.jpg

![[00.raw-materials/10.sources/images/Qsort/1.jpg]]

关键 OCR 行：
- A=QTlimit+连接站点的Process(by到recipe且不by片数的PT，
- 片数，且bycapability不byrecipe
- B=Target站点至QZONE结束站点前一站的PT的累加和（Process
- 均By到 Recipe 不By 到片数）
- Qsort=A-B的值
- 当站的PT均需要By到片数和CAPABILITY，其余站点均需
- 要by到Recipe
- 一Virtual lot的计算方式：*
- 连环QT才需要加连接站点的PT)+QTloop起始站点的PT（byLot
- LOT13 A=6H+1站点的PT+ LOT2+
- A=6H+6H+5站点的PT+1站
- 6H 点的PTU

<details>
<summary>展开完整 OCR</summary>

```text
一Virtual lot的计算方式：*
A=QTlimit+连接站点的Process(by到recipe且不by片数的PT，
连环QT才需要加连接站点的PT)+QTloop起始站点的PT（byLot
片数，且bycapability不byrecipe
LOT13 A=6H+1站点的PT+ LOT2+
A=6H+6H+5站点的PT+1站
6H 点的PTU
LOT3+5+
6H A=6H+5 站点的 PT+ LOT3
LOT2.10
B=Target站点至QZONE结束站点前一站的PT的累加和（Process
均By到 Recipe 不By 到片数）
LOT14 B=3站点的PT+4站点 LOT24 LOT24
的PT B=7站点的 PT+8站点的
6HuPT+0站点的PT
LOT3%5元
B=7站点的PT+8站点的 LOT34
10 PT+D站点的PTH
Qsort=A-B的值
当站的PT均需要By到片数和CAPABILITY，其余站点均需
要by到Recipe
```

</details>

### 第 002 张：2.jpg

![[00.raw-materials/10.sources/images/Qsort/2.jpg]]

关键 OCR 行：
- Lot在连环QZone的起始站点作业时：
- RemainPT-Target站点至QZONE结束站点前一站的PT的累加），
- A-6H-6H+6H+5站点PT+10站点PT(byrecipe不by片数
- 6H的PT1站点的剩余作业时间（BY到片数，recipe 的
- 余站点By到Recipe不By片数
- MAX【当前站点至当前QZone结束站点前一站的PT+其它
- QtimeLimit+连接站点的PT-Target站点至QZONE结束站点前
- 2024/07/18设明zsn售+算公式-经过safetyvalue高风险loopcT判断后的mergeglimit-
- 二，ExistingLot的计算方式：
- 情况1：#
- Osort=MAX【QTlimit的累加+连接站点的PT+当前站点的
- （Target站点前一站至当前站点PT的累加）】

<details>
<summary>展开完整 OCR</summary>

```text
二，ExistingLot的计算方式：
情况1：#
Lot在连环QZone的起始站点作业时：
Osort=MAX【QTlimit的累加+连接站点的PT+当前站点的
RemainPT-Target站点至QZONE结束站点前一站的PT的累加），
（Target站点前一站至当前站点PT的累加）】
LOTL LOTI
A-6H-6H+6H+5站点PT+10站点PT(byrecipe不by片数
6H的PT1站点的剩余作业时间（BY到片数，recipe 的
ProcessTime，需验证）-13站点的PT-14站点的PT+
B-1站点的RPT累加至12站点的PT(PT除1站点其
余站点By到Recipe不By片数
10
13 OSOrt-MAXAB)
15
情况2：LOT在LoOp的中间站点等待作业/正在作业
Lot所在Loop已OverOT时：
MAX【当前站点至当前QZone结束站点前一站的PT+其它
QtimeLimit+连接站点的PT-Target站点至QZONE结束站点前
站的PT的累加），（Target站点前一站至当前站点PT的累加））
2024/07/18设明zsn售+算公式-经过safetyvalue高风险loopcT判断后的mergeglimit-
当前zone的ghint-Targer站点至merge zone结束站点前一站的PT的紧加+当剪zone的款
余step（不包结束站点）的PT的紧加
```

</details>

### 第 003 张：3.jpg

![[00.raw-materials/10.sources/images/Qsort/3.jpg]]

关键 OCR 行：
- A-3站点的PT（by到片数.Capability）-4站点的PT+5站点
- （byrecipe不by片数的PT）+
- 除3站点其余站点byrecipe不by片数的
- MAX「（QTloop的OTlimit的累加-已消耗的Qtime-Target
- 站点至QZONE结束站点前站的PT的累加），（Target站点前一
- byrecipe不by片数的PT）+
- 10 （除3站点其余站点byrecipe不by片数的PT）+
- LOTI-
- LOTI-3 的PT+6H+6H-10站点的PT-13站点的PT-14站点的PT-
- 6H B-3站点至12站点的PT累加+
- 134 Osot-MAX(AB)
- ②Lot未超QT时

<details>
<summary>展开完整 OCR</summary>

```text
LOTI-
A-3站点的PT（by到片数.Capability）-4站点的PT+5站点
LOTI-3 的PT+6H+6H-10站点的PT-13站点的PT-14站点的PT-
（byrecipe不by片数的PT）+
6H B-3站点至12站点的PT累加+
除3站点其余站点byrecipe不by片数的
134 Osot-MAX(AB)
②Lot未超QT时
MAX「（QTloop的OTlimit的累加-已消耗的Qtime-Target
站点至QZONE结束站点前站的PT的累加），（Target站点前一
站至当前站点PT的累加
LOTie
A-6H-消耗的QT+6H-6H+5站点的PT+10站点的
LOT1+3 PT-13站点的PT-14站点的PT+
byrecipe不by片数的PT）+
B-3站点至12站点的PT累加+
10 （除3站点其余站点byrecipe不by片数的PT）+
134 6H Osot-MAXAB)
情况3：#
同情况2的计算方式。
当Lot作为ExisitingLot计算时，当前状态为
```

</details>

### 第 004 张：4.jpg

![[00.raw-materials/10.sources/images/Qsort/4.jpg]]

关键 OCR 行：
- Waitforjobin/jobout,且为QTime的结束站带，则当前站点
- 的EQsort置为O.
- processtime已改为bycapability的waferPT/stepPT
- 2024/07/31说明（zsn）：existinglot当前站点的

<details>
<summary>展开完整 OCR</summary>

```text
Waitforjobin/jobout,且为QTime的结束站带，则当前站点
的EQsort置为O.
2024/07/31说明（zsn）：existinglot当前站点的
processtime已改为bycapability的waferPT/stepPT
```

</details>
