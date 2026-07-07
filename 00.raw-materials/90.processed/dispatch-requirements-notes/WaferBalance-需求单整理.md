---
type: dispatch-requirement-note
source_folder: WaferBalance
topic: Wafer Balance / 晶圆均衡
tags: [自动派工, 需求单, OCR, 需求整理]
---

# WaferBalance - 需求单整理

## 资料概况

- 原始图片目录：[[00.raw-materials/10.sources/images/WaferBalance]]
- OCR 输出目录：[[00.raw-materials/90.processed/dispatch-requirements-ocr/WaferBalance]]
- 图片数量：3
- 初步主题：Wafer Balance / 晶圆均衡
- 处理状态：已 OCR，已建立初步结构化笔记
- 注意：本笔记基于 OCR 自动识别，关键需求点需回看原图确认。

## 自动识别到的关键信号

- 系统对象：EQP, Lot, Step
- 派工逻辑：Qsort, 派工
- 约束条件：Balance, Capability, QTime, WPH
- 系统接口：RTD
- 验证信息：需求

## 需求理解（初稿）

- 该组资料疑似围绕 Wafer Balance 或晶圆数量均衡展开。
- 需要重点确认：均衡对象是设备、Chamber、Recipe、产品、Monitor Wafer 还是批次内 wafer 分布。
- 对派工系统的影响：Wafer Balance 可能影响设备选择、批次组合、WPH 损失和后续站点负载均衡。

## 待澄清问题

- [ ] 需求目标是什么：提升产能、降低 Cycle Time、减少 OverQtime、降低 WPH Loss，还是提升自动化率？
- [ ] 输入数据来自哪些系统：MES、RTD、AMA、EAP、MCS、APC、PMS？
- [ ] 规则属于 Global Rule、Local Rule，还是排序 / Prefer 逻辑？
- [ ] 需要新增哪些异常原因码或查询页面？
- [ ] 验收标准是什么：测试 Case、前后对比指标、上线影响范围？

## 分页 OCR 摘录

### 第 001 张：表1.jpg

![[00.raw-materials/10.sources/images/WaferBalance/表1.jpg]]

关键 OCR 行：
- 1、将Lot的waferqty 平均分配到机台 2、计算机台作 业该Lot的时间 3、计算该机台作 业所有Lot的时间 4、计算该机合权重 5、根据权重再次计 qty 算分配Lot的wafer
- qsortcategiqsont Qty Fiow EQP UPH (by Avg) QtyAssign Step WIP Time: QtyAssign/UPH) EQPWIPTime WiIPTime) (Sum of Step eqp wip time pre qsort category neweqp wip time Weight (1) (by Weight) QtyAssign QtyAssignt(1/UPH) Step WIP Time: EQP WIPTime Time) (Sumof StepWIP eqpwip timepre gsont category neweqpwip time Weight (2) Qty Assign (by Weight) Step WIP Tim Qty Assign"(1/UP
- 某机台再分配Lotwaferqty=Lotqty× capability下所有可作业机台权重总和 0.64516129 4535147392
- 12 13 15 12 24 12 12 12 12 1162 11.62 11.62 11.62 6.91 14.5 45 11 11 11 LOtA LotA LOTA LotA LotB LotD LotD LotD LotD Lotc LOTE 20 25 13 20 20 20 20 20 20 20 20 COAT COAT COAT COAT COAT EXP EXP EXP EXP EXP EXP COT003 COT002 EXP006 EXP005 COT002 COTO01 COTO02 EXP004 EXP006 EXP005 EXP005 20 22 25 20 20 22 22 20 22 20 10 10 10 10 13 10 10 25 20 10 10 0.454545455 1136363636 0.454545455 0.454545455 0.65 0.5 0.4 0.5 0.4 0.5 1.590909091 0.454545455 1590909091 0.454545455 105 105 0.5 0.4 0.5 0.5 1590909091 0.5 050.9545455 16060652 15909091 0.4545455 15909091 155 155 0.5 04 0.5 0.5 0.628571429 Q.385964912 0.628571429 1047619048 064516129 064516129 25 22 8888888889 4535147392 1111111111 4.782608696 15.46485261 15.2173913 13.125 6.875 25 20 0.444444444 0.444444444 1136363636 0.217391304 0.760869565 0.181405896 0.702947846 0.65625 0.3125 0.65 0.444444444 Q.444444444 0.760869565 0.831405896 1353754941 1353754941 0.831405896 0.702947846 0.65625 0.3125 0.4444444 13537549 Q444144 0.7608696 D.444444444 D.44444444 1353754941 0760869565 0.702947846 1073369565 1353754941 2353754941 127585034 127585034 0.65625 0.50567161 2.62857143 0.50567161 3.12967742 3.04761905 0.97600964 Q16397838 0.464317 0.464317 5.625 45 8.888888889 1111111111 16.99751861 1721802995 2781970052 15.14860978 4.851390221 3.00248139 25 13 20 0.4442 0.444 0.1364 0.111 0.8498 1.136 0.7826 0.757 0.220
- 0,612,24 064516129 4102564103
- 某机台权重 该机台作业所有分配Lot的时间总和 0385964912 25 5384615385 15.8974359
- 1.047619048 14.61538462
- 0.385964912 25
- 该机台权重 0.64516129 22 1546485261 13
- 13.125
- 1047619048 6.875
- 0.385964912 20

<details>
<summary>展开完整 OCR</summary>

```text
1、将Lot的waferqty 平均分配到机台 2、计算机台作 业该Lot的时间 3、计算该机台作 业所有Lot的时间 4、计算该机合权重 5、根据权重再次计 qty 算分配Lot的wafer
qsortcategiqsont Qty Fiow EQP UPH (by Avg) QtyAssign Step WIP Time: QtyAssign/UPH) EQPWIPTime WiIPTime) (Sum of Step eqp wip time pre qsort category neweqp wip time Weight (1) (by Weight) QtyAssign QtyAssignt(1/UPH) Step WIP Time: EQP WIPTime Time) (Sumof StepWIP eqpwip timepre gsont category neweqpwip time Weight (2) Qty Assign (by Weight) Step WIP Tim Qty Assign"(1/UP
12 13 15 12 24 12 12 12 12 1162 11.62 11.62 11.62 6.91 14.5 45 11 11 11 LOtA LotA LOTA LotA LotB LotD LotD LotD LotD Lotc LOTE 20 25 13 20 20 20 20 20 20 20 20 COAT COAT COAT COAT COAT EXP EXP EXP EXP EXP EXP COT003 COT002 EXP006 EXP005 COT002 COTO01 COTO02 EXP004 EXP006 EXP005 EXP005 20 22 25 20 20 22 22 20 22 20 10 10 10 10 13 10 10 25 20 10 10 0.454545455 1136363636 0.454545455 0.454545455 0.65 0.5 0.4 0.5 0.4 0.5 1.590909091 0.454545455 1590909091 0.454545455 105 105 0.5 0.4 0.5 0.5 1590909091 0.5 050.9545455 16060652 15909091 0.4545455 15909091 155 155 0.5 04 0.5 0.5 0.628571429 Q.385964912 0.628571429 1047619048 064516129 064516129 25 22 8888888889 4535147392 1111111111 4.782608696 15.46485261 15.2173913 13.125 6.875 25 20 0.444444444 0.444444444 1136363636 0.217391304 0.760869565 0.181405896 0.702947846 0.65625 0.3125 0.65 0.444444444 Q.444444444 0.760869565 0.831405896 1353754941 1353754941 0.831405896 0.702947846 0.65625 0.3125 0.4444444 13537549 Q444144 0.7608696 D.444444444 D.44444444 1353754941 0760869565 0.702947846 1073369565 1353754941 2353754941 127585034 127585034 0.65625 0.50567161 2.62857143 0.50567161 3.12967742 3.04761905 0.97600964 Q16397838 0.464317 0.464317 5.625 45 8.888888889 1111111111 16.99751861 1721802995 2781970052 15.14860978 4.851390221 3.00248139 25 13 20 0.4442 0.444 0.1364 0.111 0.8498 1.136 0.7826 0.757 0.220
0,612,24 064516129 4102564103
某机台权重 该机台作业所有分配Lot的时间总和 0385964912 25 5384615385 15.8974359
1.047619048 14.61538462
0.385964912 25
该机台权重 0.64516129 22 1546485261 13
某机台再分配Lotwaferqty=Lotqty× capability下所有可作业机台权重总和 0.64516129 4535147392
13.125
1047619048 6.875
0.385964912 20
```

</details>

### 第 002 张：需求单1.jpg

![[00.raw-materials/10.sources/images/WaferBalance/需求单1.jpg]]

关键 OCR 行：
- 新增需求申请单
- 申请人员：张赛楠 功能模块（类别为3时必填）：智能派工系统（RTD/DSP）
- 不overgtime、会对loop内的wiP进行balance处理。先将loop内lot按照remain gtime划分层级Co，6，
- 12，24），将各层级按照wafer逐个分配至各机台/腔，尽量让各设备分配量均衡。但当前的waferbalance是
- 对同一层级内Lot循环分配，不同层级间没有关联，未考虑前一等级lot对下一等级lotbalance的影响，导致
- balance不合理，从而影响产能判断。
- 另外，waferbalance时，lot在机台上的初始化作业片数是由平均法得出，但实际上不同机台的作业能力
- 不一样。在进行初始化时应该依据机台作业能力进行判断，因此需对waferbalance的lot片数初始化参数作
- 同一层级内lot循环分配，不同层级间无关联，balance不合理，导致1卡lotBPoM609overgtime·
- wafer分配时增加考量不同层级联动影响，当前层级机台作业时间考量了之前层级里机台的作业时间，
- balance更加合理，避免overqtime；
- 需求内容（可添加附件）=

<details>
<summary>展开完整 OCR</summary>

```text
新增需求申请单
编号： 12-R-20220221-QC （此处由信息技术部填写）
类别（请在方框内打勾）：1软件采购 2硬件采购 3.功能开发口4.工程及服务
申请部门：制造部 系统名称（类别为3时必填）：CIM计算机集成制造系统Fab6
申请人员：张赛楠 功能模块（类别为3时必填）：智能派工系统（RTD/DSP）
申请日期：2022-02-16 希望交付期：2022-03-01-
项目简介和必要性分析： 由于设备可作业产品的情况存在差异，OzoneControl为尽量让各机台/腔获得足够的产品作业，并保证lot
不overgtime、会对loop内的wiP进行balance处理。先将loop内lot按照remain gtime划分层级Co，6，
12，24），将各层级按照wafer逐个分配至各机台/腔，尽量让各设备分配量均衡。但当前的waferbalance是
对同一层级内Lot循环分配，不同层级间没有关联，未考虑前一等级lot对下一等级lotbalance的影响，导致
balance不合理，从而影响产能判断。
另外，waferbalance时，lot在机台上的初始化作业片数是由平均法得出，但实际上不同机台的作业能力
不一样。在进行初始化时应该依据机台作业能力进行判断，因此需对waferbalance的lot片数初始化参数作
出优化。#
项目投资方案比较及效果分析：
改善前：
同一层级内lot循环分配，不同层级间无关联，balance不合理，导致1卡lotBPoM609overgtime·
改善后：+
wafer分配时增加考量不同层级联动影响，当前层级机台作业时间考量了之前层级里机台的作业时间，
balance更加合理，避免overqtime；
需求内容（可添加附件）=
1、不同gsort层级联动影响
依据lotgsornt进行category层级划分后，每次循环的balance逻辑里增加考量上一层级机台的需求作业
时间。上一层级balance结束后，把得到的各个机台需求作业时间（EQPWIPTime）作为下一层级balance前
机台的初始化作业时间，即：
当前层级里某机台作业所有分配lot的时间=sum（之前各个层级里该机台作业所有分配lot的时间）+当
前层级里该机台作业所有分配lot的时间。
说明：之前各个层级里均无此机台，则给定初始时间为0。
举例如下：
```

</details>

### 第 003 张：需求单2.jpg

![[00.raw-materials/10.sources/images/WaferBalance/需求单2.jpg]]

关键 OCR 行：
- 根据机台作业能力WPH来给定lot在该机台的初始化片数：
- Lot在某机台的初始化片数-LotQTY×（该机台WPH/所有可作业机台的WPH之和）
- 机台的初始化作业时间，即 当前层级里某机台作业所有分配lot的时间-sum（之前各个层级里该机台作业所有分配lot的时间）+当
- 前层级里该机台作业所有分配ot的时间。
- 说明：之前各个层级里均无此机台，则给定初始时间为0。
- 举例如下：
- 机台作业菜十lot
- tot分配 分配片数的时间 机台作业所有
- cateory eset 片效 LEOPWIP OPWIPOAB+
- tine Jote atx 同（PreEOP
- asse
- assign/UPH) WIP

<details>
<summary>展开完整 OCR</summary>

```text
机台的初始化作业时间，即 当前层级里某机台作业所有分配lot的时间-sum（之前各个层级里该机台作业所有分配lot的时间）+当
前层级里该机台作业所有分配ot的时间。
说明：之前各个层级里均无此机台，则给定初始时间为0。
举例如下：
机台作业菜十lot
tot分配 分配片数的时间 机台作业所有
cateory eset 片效 LEOPWIP OPWIPOAB+
tine Jote atx 同（PreEOP
asse
assign/UPH) WIP
time a
LOTA 20 COAT COT002. 20 0.5 0.5 0.5
20 COAT 25 10 0.4. 04 04
20 EXPOOS 10 1590909091 0. 15909091
LOCA 20 EXP EXP006 20 10 0.5 05 0.5.
25 EXP EXPOOS 1136363636 1590909091 15909091
691 COAT COTOO2 0.65 105 0.5 155
1162 20 COT001 0.454545455 0.4545455
1162 20 COAT COT0O2 10 04 105 0.5 155
1162 20. EXP EXP004 20 10 0.5
12 1162 EXP. EXP006 10 0.454545455 0.9545455
24 14.5 20元 EXP. EXPOOS 20 1590909091 25909091
2、参数初始化
根据机台作业能力WPH来给定lot在该机台的初始化片数：
Lot在某机台的初始化片数-LotQTY×（该机台WPH/所有可作业机台的WPH之和）
申请部门意见： 申请部门分管领导意见：
日期：
相关部门意见： 相关部门分管领导意见：
日期：
信息技术部意见： 信息技术部分管领导音见：中
```

</details>
