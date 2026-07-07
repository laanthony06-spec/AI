---
type: dispatch-requirement-note
source_folder: WPHLoss
topic: WPH Loss / 产能损失
tags: [自动派工, 需求单, OCR, 需求整理]
---

# WPHLoss - 需求单整理

## 资料概况

- 原始图片目录：[[00.raw-materials/10.sources/images/WPHLoss]]
- OCR 输出目录：[[00.raw-materials/90.processed/dispatch-requirements-ocr/WPHLoss]]
- 图片数量：4
- 初步主题：WPH Loss / 产能损失
- 处理状态：已 OCR，已建立初步结构化笔记
- 注意：本笔记基于 OCR 自动识别，关键需求点需回看原图确认。

## 自动识别到的关键信号

- 系统对象：Chamber, EQP, Lot, Machine, Recipe, Step
- 派工逻辑：派工
- 约束条件：Capability, Loss, PM, QZone, WPH
- 系统接口：RTD
- 验证信息：需求

## 需求理解（初稿）

- 该组资料疑似围绕 WPH Loss 或产能损失分析展开。
- 需要重点确认：Loss 的定义、计算窗口、归因规则、是否用于派工排序或异常提醒。
- 对派工系统的影响：WPH Loss 可作为派工策略评估指标，也可反馈到瓶颈机台优先级或设备选择逻辑。

## 待澄清问题

- [ ] 需求目标是什么：提升产能、降低 Cycle Time、减少 OverQtime、降低 WPH Loss，还是提升自动化率？
- [ ] 输入数据来自哪些系统：MES、RTD、AMA、EAP、MCS、APC、PMS？
- [ ] 规则属于 Global Rule、Local Rule，还是排序 / Prefer 逻辑？
- [ ] 需要新增哪些异常原因码或查询页面？
- [ ] 验收标准是什么：测试 Case、前后对比指标、上线影响范围？

## 分页 OCR 摘录

### 第 001 张：1.jpg

![[00.raw-materials/10.sources/images/WPHLoss/1.jpg]]

关键 OCR 行：
- 申请人员：万艳艳 功能模块（类别为3时必填）：智能派工系统（RTD/DSP）
- 复合机台（如BMCUBA01-1234CDEF），每组腔的产能LOSS不同，如CUBA01-12LOSS：15%，CUBA01-
- 34LoSS:25%，CUBA01-CDLOSS:50%，CUBA01-EFLOSS:50%，按目前的WPH设定，每个腔无法
- 按实际的LOSS设定WPH。因此产线需求复合机台上线WPHLoss功能，按腔体/count设定Loss比例，因
- 此QZone需要新增WPHLoss的判断。
- QZone新增WPHLoss的判断逻辑，根据WPHLoss重新计算WPH值。
- 1.Metal设备WPH按实际产能维护，Q-timeLoop放货量管控，减少>OverQ-time5-6Lot/月：
- 2.减少人为管控风险，节省人力18H/每月（60个腔每20天PM一次，人为管控0.2H一次）
- 需求内容（可添加附件）：
- QZone拿取机台WPH时新增WPHLoss的逻辑：
- （一）.原QZone拿取机台WPH时Bycapability.machinename，recipe拿取表vwdspcapabilitywph
- 对应的wph.isengcontrolengpriority信息，现需要多拿出ProcessGroup，WPHLossControl栏

<details>
<summary>展开完整 OCR</summary>

```text
甲请部门：利造部 系统名称（类别为3时必填）：CIM计算机集成制造系统Fab6
（二科））
申请人员：万艳艳 功能模块（类别为3时必填）：智能派工系统（RTD/DSP）
申请日期：2024-05-15 希望交付期：2023-06-15
项目简介和必要性分折：
复合机台（如BMCUBA01-1234CDEF），每组腔的产能LOSS不同，如CUBA01-12LOSS：15%，CUBA01-
34LoSS:25%，CUBA01-CDLOSS:50%，CUBA01-EFLOSS:50%，按目前的WPH设定，每个腔无法
按实际的LOSS设定WPH。因此产线需求复合机台上线WPHLoss功能，按腔体/count设定Loss比例，因
此QZone需要新增WPHLoss的判断。
项目投资方案比较及效果分析：
改善方案：
QZone新增WPHLoss的判断逻辑，根据WPHLoss重新计算WPH值。
效果分析：
1.Metal设备WPH按实际产能维护，Q-timeLoop放货量管控，减少>OverQ-time5-6Lot/月：
2.减少人为管控风险，节省人力18H/每月（60个腔每20天PM一次，人为管控0.2H一次）
需求内容（可添加附件）：
QZone拿取机台WPH时新增WPHLoss的逻辑：
（一）.原QZone拿取机台WPH时Bycapability.machinename，recipe拿取表vwdspcapabilitywph
对应的wph.isengcontrolengpriority信息，现需要多拿出ProcessGroup，WPHLossControl栏
位。
（）.在拿完WPH后新增逻辑判断LotWPHLoss逻辑：
```

</details>

### 第 002 张：2.jpg

![[00.raw-materials/10.sources/images/WPHLoss/2.jpg]]

关键 OCR 行：
- 1拿取Lot的以下信息Lotidcapability stepsegstn可作业的机台
- /chamben.recipe.wph.ProcessGroup,wPHLossControlppid.chamberflow取stn中
- 空值），且WPHLossControl均-Y时需要对Lot的该主机台EQPID进行后WPHLoSs的计
- 2.1判断WPHLOSS的具体逻辑如下
- 取缺少的chamber个数及对应的Loss值，再重新计算机台的WPH信息。
- 21.1拿取需要判断的Lot信息并进行数据处理：
- a 对需要判断WPHLoss 的Lot及机台拿取以下信息：Lot,stepseg，Capability
- 行，再按拆分成多行（原QZone中不同PPID间用：分隔，不同chamber
- 212判断Lot在机台的上缺少的chamber个数信息
- a掌取维护表tb dspwphloss中的维护信息：
- 前的部分作为主机台EQPID若stn中无则 EQPID=STN
- 2.ByLotstepseg.EQPID分组，当同一组中的可作业机台 stn对应的ProcessGroup相同 不力

<details>
<summary>展开完整 OCR</summary>

```text
1拿取Lot的以下信息Lotidcapability stepsegstn可作业的机台
/chamben.recipe.wph.ProcessGroup,wPHLossControlppid.chamberflow取stn中
前的部分作为主机台EQPID若stn中无则 EQPID=STN
2.ByLotstepseg.EQPID分组，当同一组中的可作业机台 stn对应的ProcessGroup相同 不力
空值），且WPHLossControl均-Y时需要对Lot的该主机台EQPID进行后WPHLoSs的计
算，反之不需要。
2.1判断WPHLOSS的具体逻辑如下
根据lot在机台chamberflow中不同的chamber信息与机台总的chamber信息比较，拿
取缺少的chamber个数及对应的Loss值，再重新计算机台的WPH信息。
21.1拿取需要判断的Lot信息并进行数据处理：
a 对需要判断WPHLoss 的Lot及机台拿取以下信息：Lot,stepseg，Capability
EQPID，ProcessGroup，ChamberFlow并对数据进行去重
b对Lot的chamberflow进行拆分，掌chamberflow中每一个chamber的信息：，
ByLotstepseg EQPID分组，拿取机台可用的chamberflow，先按：拆分成多
行，再按拆分成多行（原QZone中不同PPID间用：分隔，不同chamber
间用，分隔，因此按该分隔符拆分），注意数据去重，使机台chamberlow中的
每个不同的chamber为行信息（例：chamberilow为 STN1.STN2 STN1,STN3
理后为三行信息：STN1STN2STN3）
212判断Lot在机台的上缺少的chamber个数信息
a掌取维护表tb dspwphloss中的维护信息：
```

</details>

### 第 003 张：3.jpg

![[00.raw-materials/10.sources/images/WPHLoss/3.jpg]]

关键 OCR 行：
- 对需要判断WPHLoss的Lot,By CapablltyProcessGroup,EQPID,chamber与表
- mfgcim.tb dsp wphloss 中的 apability，ProcessGroup,Machine,sTN进行匹配
- 2.13判断Lot在该机台的WPHLOSS信息：
- a 计算每个SubegpStateGroup的WPHLoss
- By Capability.ProcessGroup,EQPID,SubegpStateGroup. CountGap与表
- tb dsp wphloss 的 Capability ProcessGroup Machine,subegpstateGroup,Court
- 匹配，拿取对应的LOSS信息，当串不到时默认LOSS=O+
- b.计算机台的最终WPHLOsS值：
- 取机台不同SubeqpStateGroup中的Max(Loss）做为Lot在该机台对应的wPHLoss
- 表mfgcim.tbdsp.wphloss.中数据示例：
- Capability Machine STN SUBEORSTATE GROUP SAMEGURNRCOURE Count, LOsS
- .根据机台的WPHLOSS情况对原MVPH进行处理：

<details>
<summary>展开完整 OCR</summary>

```text
对需要判断WPHLoss的Lot,By CapablltyProcessGroup,EQPID,chamber与表
mfgcim.tb dsp wphloss 中的 apability，ProcessGroup,Machine,sTN进行匹配
拿取SubegpstateGroup（同类型chamber的分组信息），SameGroupCount（同
组中的chamber个数信息
b.计算缺少的chamber个数：
对Lot按SubegpStateGroup进行分组，并累计处于同一SubegpstateGroup中可作
业chamber个数，记为ActualCount；
By SubegpstateGroup计算SameGroupCount-ActualCount的值，记为CountGap
值，并将该值赋给对应的SubeqpStateGroup
2.13判断Lot在该机台的WPHLOSS信息：
a 计算每个SubegpStateGroup的WPHLoss
By Capability.ProcessGroup,EQPID,SubegpStateGroup. CountGap与表
tb dsp wphloss 的 Capability ProcessGroup Machine,subegpstateGroup,Court
匹配，拿取对应的LOSS信息，当串不到时默认LOSS=O+
b.计算机台的最终WPHLOsS值：
取机台不同SubeqpStateGroup中的Max(Loss）做为Lot在该机台对应的wPHLoss
表mfgcim.tbdsp.wphloss.中数据示例：
Capability Machine STN SUBEORSTATE GROUP SAMEGURNRCOURE Count, LOsS
M-RFCUS-C Groupi, BMCUBAG4 BMCUEAOAL1 200
M-RFCUS-C Groupt, BMCUBAG4 BMCUBADA 2 40%
MRFCUS-C Groupa BMCUBAG4 BMKUEADAC
M-RFCUS-C Groupi BMCUBA94 BMRUBAOA D 50%
.根据机台的WPHLOSS情况对原MVPH进行处理：
```

</details>

### 第 004 张：4.jpg

![[00.raw-materials/10.sources/images/WPHLoss/4.jpg]]

关键 OCR 行：
- （1）已知此机台每个Chamber或机台的TotalSTNWPH，即Lot在该机台实际维护WPH之
- 则为该机台腔WPH之和，注：细化到Capability&Recipe层面）
- (2）对应该产品在该机台实际WPH，即ActualSTNWPH=TotalSTNWPH（1-WPHLOsS）。
- （3）通过计算出的ActualSTNWPH，对产品每个可作业腔计算实际WPH占比，并计算该腔
- 或整机的WPH。
- ①若WPH维护整机，则WPH=ActualSTNWPH
- ②若WPH维护腔，产品在实际每个可作业腔占比Chamber Ratio=该腔
- WPH/Z该产品可作业腔WPH，每个腔WPH即ChamberWPH=ChamberRatio*ActualSTN
- WPH
- 申请部门意见： 申请部门分管领导意见：
- 日期：4 日期：3
- 相关部门意见： 相关部门分管领导意见：

<details>
<summary>展开完整 OCR</summary>

```text
（1）已知此机台每个Chamber或机台的TotalSTNWPH，即Lot在该机台实际维护WPH之
则为该机台腔WPH之和，注：细化到Capability&Recipe层面）
(2）对应该产品在该机台实际WPH，即ActualSTNWPH=TotalSTNWPH（1-WPHLOsS）。
（3）通过计算出的ActualSTNWPH，对产品每个可作业腔计算实际WPH占比，并计算该腔
或整机的WPH。
①若WPH维护整机，则WPH=ActualSTNWPH
②若WPH维护腔，产品在实际每个可作业腔占比Chamber Ratio=该腔
WPH/Z该产品可作业腔WPH，每个腔WPH即ChamberWPH=ChamberRatio*ActualSTN
WPH
申请部门意见： 申请部门分管领导意见：
日期：4 日期：3
相关部门意见： 相关部门分管领导意见：
日期：3 日期：2
信息技术部意见： 信息技术部分管领导意见：
日期：# 日期：3
附件名称：#
```

</details>
