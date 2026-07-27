---
type: dispatch-requirement-note
source_folder: LithoAutoPirun优化
topic: 自动派工需求
tags: [自动派工, 需求单, OCR, 需求整理]
---

# LithoAutoPirun优化 - 需求单整理

## 资料概况

- 原始图片目录：[[00.raw-materials/10.sources/images/LithoAutoPirun优化]]
- OCR 输出目录：[[00.raw-materials/90.processed/dispatch-requirements-ocr/LithoAutoPirun优化]]
- 图片数量：9
- 初步主题：自动派工需求
- 处理状态：已 OCR，已建立初步结构化笔记
- 注意：本笔记基于 OCR 自动识别，关键需求点需回看原图确认。

## 自动识别到的关键信号

- 系统对象：EQP, FOUP, Lot, Port, Recipe, Step, Tool
- 派工逻辑：Prefer, Rule, Sorting, 排序, 派工, 规则
- 约束条件：Capability, Hold, QTime
- 系统接口：AMA, MES, RTD
- 验证信息：原因, 结果, 需求

## 需求理解（初稿）

- 该组资料与自动派工需求有关，需进一步人工复核 OCR 结果。
- 建议从输入、处理逻辑、输出、异常、验收标准五个角度补全需求。

## 待澄清问题

- [ ] 需求目标是什么：提升产能、降低 Cycle Time、减少 OverQtime、降低 WPH Loss，还是提升自动化率？
- [ ] 输入数据来自哪些系统：MES、RTD、AMA、EAP、MCS、APC、PMS？
- [ ] 规则属于 Global Rule、Local Rule，还是排序 / Prefer 逻辑？
- [ ] 需要新增哪些异常原因码或查询页面？
- [ ] 验收标准是什么：测试 Case、前后对比指标、上线影响范围？

## 分页 OCR 摘录

### 第 001 张：1.jpg

![[00.raw-materials/10.sources/images/LithoAutoPirun优化/1.jpg]]

关键 OCR 行：
- 申请人员：温洁奇 功能模块（类别为3时必填）：智能派工系统（RTD/DSP）
- 长，容易造成lotOQT。现需根据lot的R2R状态，作业条件由系统自动选择pilot，不限制pilot自动分批站
- 优化AutoSplit逻辑，选择状态仅为piunon且在光刻有作业条件的lot反馈给R2R，自动分批不再卡控
- reticle位置，pilot在purun loop中优先派工。
- 需求内容（可添加附件）：
- 方案逻辑：
- RTD新增逻辑
- 实现 AutoSplitPurun 的全部判定逻辑，并输出 Pilot 选择结果的Repont 供AMA 执行分批。另外对
- LithoRule和LithoAssign涉及AutoSplitPunun 的逻辑同步进行修改。
- 从FAB6 和FAB8 两厂获取待判断 Lot，并进行初步过滤。
- 通过表fablotext获取reguredcapabilityruncardidretcled栏位信息，
- 申请部门：制造部 系统名称类别为3时必填）：CIM计算机集成制造系统Fab6

<details>
<summary>展开完整 OCR</summary>

```text
申请部门：制造部 系统名称类别为3时必填）：CIM计算机集成制造系统Fab6
申请人员：温洁奇 功能模块（类别为3时必填）：智能派工系统（RTD/DSP）
申请日期：2026-02-11 希望交付期：
顶目简介和必要性分析
当前LithoPurun需要PE设置Pilot，在pilot的Mask放入机台后才会自动分批，purun流程花费时间较
长，容易造成lotOQT。现需根据lot的R2R状态，作业条件由系统自动选择pilot，不限制pilot自动分批站
点，实现lot在Barc站点AutoSplitPinum·
项目投资方案比较及效果分折：
改善方案：
优化AutoSplit逻辑，选择状态仅为piunon且在光刻有作业条件的lot反馈给R2R，自动分批不再卡控
reticle位置，pilot在purun loop中优先派工。
效果分析：
R2RAutoPinunOtimeBuffer从最低6小时变至24小时
需求内容（可添加附件）：
方案逻辑：
RTD新增逻辑
实现 AutoSplitPurun 的全部判定逻辑，并输出 Pilot 选择结果的Repont 供AMA 执行分批。另外对
LithoRule和LithoAssign涉及AutoSplitPunun 的逻辑同步进行修改。
LReport部分
涉及生成Report：Central GetLithoR2RAutoPirunInfo
L1Lot获取
从FAB6 和FAB8 两厂获取待判断 Lot，并进行初步过滤。
L.1.ILot基础信息获取
通过表fwlot获取appid、priontyprocessingstatus、componentgty位信息
通过表fablotext获取reguredcapabilityruncardidretcled栏位信息，
通过表fablotcanerext获取camerknd栏位信息：
```

</details>

### 第 002 张：2.jpg

![[00.raw-materials/10.sources/images/LithoAutoPirun优化/2.jpg]]

关键 OCR 行：
- 通过fabinqtimeprocess天取Remaino栏位信息。
- 从 UIRTDConfig-LITHOLotAssignment LithoAssignCapability 中获取 LithoCapability
- 1.1.2基础过滤条件，
- （2）基本条件过滤：筛选出满足samierkind-TFOUP、runcardid 为空、RemainQ0或Remano为空、
- reguiredcapability E LithoCapability,L-BARCO-LL-BARCO-S) 的 Lot
- （IsTransferLot指标经istransferlotmarco判断得到）
- 1.13其他过滤条件
- 拿取112的lot并过滤满足以下条件的lot
- imtemalpnonity-BulletLot intemalpriority BulletLot pnonity  BulletLot intemalpniority 在 RTDConfig 中
- （3）去除同 FOUP 已存在 Litho Pilot 的 LotLithoPilot 从表 rtd r2r litho context ovl/cd 和
- 获取Lot后续站点信息并进一步判断是否符合AutoSplitPiun条件。
- 对通过1.1筛选的Lot，向下Fetch20站，获取每个站点的productmame、planname、stage、capability、

<details>
<summary>展开完整 OCR</summary>

```text
通过fabinqtimeprocess天取Remaino栏位信息。
从 UIRTDConfig-LITHOLotAssignment LithoAssignCapability 中获取 LithoCapability
1.1.2基础过滤条件，
对掌取的Lot执行以下三步过滤：?
（1）状态过滤：筛选出满足(priority 8且processimgstatus=Active）或（priority5且
（2）基本条件过滤：筛选出满足samierkind-TFOUP、runcardid 为空、RemainQ0或Remano为空、
reguiredcapability E LithoCapability,L-BARCO-LL-BARCO-S) 的 Lot
（3）跨厂lot去重：筛选出满足IsTransferLot-True 或(IsTransferLotTrue 且 processmgStatus#
CrossFabTransfered的Lot。
（IsTransferLot指标经istransferlotmarco判断得到）
1.13其他过滤条件
拿取112的lot并过滤满足以下条件的lot
（1）去除Bullet LotBullet LP：即空机或空PortLot，空机 lot定义：prionity一BulletLotpriority，
imtemalpnonity-BulletLot intemalpriority BulletLot pnonity  BulletLot intemalpniority 在 RTDConfig 中
BulletLot PnoAndInterpno的ParameterValue Char栏位获取空PontLot定义：mpcpnionity-mpcpriority config的lot
即为空portlot。mpcpriorityconfig从tbmpgprionity.config拿取，即freepont-Y时的mpspriority。
（2）去除R2R白名单Lot：通过表2rlithowhitelist 获取白名单lot。
（3）去除同 FOUP 已存在 Litho Pilot 的 LotLithoPilot 从表 rtd r2r litho context ovl/cd 和
ntd 2r lot histony获取。+
12Pirun站点获取
获取Lot后续站点信息并进一步判断是否符合AutoSplitPiun条件。
L2.1Fetch站点信息获取
对通过1.1筛选的Lot，向下Fetch20站，获取每个站点的productmame、planname、stage、capability、
stepseg、tecipeid、STN 信息eTransterlot需修正厂广另D
L22PirunLoop判断
Lo般Pinn的站点力BARCLthoOVLCDADI对121的Kt进以下过滤
1）CD站点判断：截取到最后道CD站点若LoOP中无CD站点：过Lo+
```

</details>

### 第 003 张：3.jpg

![[00.raw-materials/10.sources/images/LithoAutoPirun优化/3.jpg]]

关键 OCR 行：
- (2）Ltho站点划断：半断 Loop 中是否存在 capabilityLithoCapabilty 且合有 Reticle 信息的站点。
- <3） FutureHold 半断：从表fabfutureacuion获取Loop中每个站点的FutureActon信息，判断Loop 中
- （4）RC判断：判断Loop 中是否存在 RC站点，若有则过滤Lot。
- 1.3AntoSplir条件力断
- 获取lot的R2R状态并进行AutoSplit条件的判断。
- 对12 的Lot，拿取其 Litho 站点：判断逻辑为（IsLithoStep And (Curstep Full Segl-Full StepSea or
- 经TIransferMarco判断后，若Lot 在Litho 站点能 Transfer则同时拿取对广Litho 机台信息。
- 将 Lot 在litho 站点的机台List 进行折分，By 机台厂别以表rtd r2r litho add setting 中获取Lot在机
- 将剩余lot 在 Litho站点的机台经 EQPStatus、LCC、Capabiity、Recipe、PPID、Global Reason 的判断
- （followLithoassign逻辑），若存在卡控则筛除对应机台。
- 从表rtd2r litho contextovl和 ntd r2r litho_contextcd匹配 R2R状态，并判断是否存在R2R
- Reason。筛选同时满足以下条件的Lot：

<details>
<summary>展开完整 OCR</summary>

```text
(2）Ltho站点划断：半断 Loop 中是否存在 capabilityLithoCapabilty 且合有 Reticle 信息的站点。
若无贝过滤Lot。
<3） FutureHold 半断：从表fabfutureacuion获取Loop中每个站点的FutureActon信息，判断Loop 中
是否存在FutureHold，若有过滤Lot。
（4）RC判断：判断Loop 中是否存在 RC站点，若有则过滤Lot。
1.2.3Merge站点设定
若Lot有ADI站点（不包合 SRC则lot被选为分批Iot时，将第道ADI设力Merge站点，否
则将最后一道CD 设为Merge 站点。
1.3AntoSplir条件力断
获取lot的R2R状态并进行AutoSplit条件的判断。
13.1机台及Lot卡控断
对12 的Lot，拿取其 Litho 站点：判断逻辑为（IsLithoStep And (Curstep Full Segl-Full StepSea or
ExtralStatus-Waitfor JobPrep OR Wait For Transport And Null(tuackinTime))
经TIransferMarco判断后，若Lot 在Litho 站点能 Transfer则同时拿取对广Litho 机台信息。
将 Lot 在litho 站点的机台List 进行折分，By 机台厂别以表rtd r2r litho add setting 中获取Lot在机
台的 spltflag 和 pisplitct若Lot不存在Pusplit flag一T的机台，则过滤Lot。
将剩余lot 在 Litho站点的机台经 EQPStatus、LCC、Capabiity、Recipe、PPID、Global Reason 的判断
（followLithoassign逻辑），若存在卡控则筛除对应机台。
L32R2R状态四配
从表rtd2r litho contextovl和 ntd r2r litho_contextcd匹配 R2R状态，并判断是否存在R2R
Reason。筛选同时满足以下条件的Lot：
( OVL Status E PinnON,ON.Fixed:
(2)CD Status E (PinunON.ON.Fixed;
(3)R2RReason力空。
此时Lot.STNOVL Status、CD Status 为一行信息
L3.3AutoSplit条件力断
串取 Lot 的 Chuck 和 Slot 信息 从表ntd rr ltho gontext relauon 联取 Prelaver信息若 Lot 存在
elaye，以表2r ltho waferhistory 中联取每片 Wafe 的 Chuck 信息，百u从表matenalassocatuon 中
```

</details>

### 第 004 张：4.jpg

![[00.raw-materials/10.sources/images/LithoAutoPirun优化/4.jpg]]

关键 OCR 行：
- prelayet，则从表r2r litho waferhistory中获取每片Wafer的Chuck信息，否则从表fsmaterialassociation中
- 获取Wafer 的 Slot 信息。若Lot 包含 Chuckl 和Chuck2，或 Slot 包含奇偶号，则 ChuckOrSlotidSatisty
- 存在CD站点？ （不清是条件）
- （不满足条件）
- （不满足条件
- TRUE.N
- 按LotSTN维度计算以下 Flag：
- ChuckOrSlotidSatisf-TRUE，则为 TRUE，否贝内 FALSE。
- CanAutoSplitFlag CD若CD StatusPuunoNE pusplitflag二Y且Pilot为空目
- ChuckOrSlotidSatisfy-TRUE，则为 TRUE百贝 FALSE。
- TRUE：否则为FALSE。J
- 按Lot 维度汇总（各STN 的 Flag取OR）筛选 CanAutoSplitFlag OVLTRUE 或

<details>
<summary>展开完整 OCR</summary>

```text
prelayet，则从表r2r litho waferhistory中获取每片Wafer的Chuck信息，否则从表fsmaterialassociation中
获取Wafer 的 Slot 信息。若Lot 包含 Chuckl 和Chuck2，或 Slot 包含奇偶号，则 ChuckOrSlotidSatisty
TRUE.N
按LotSTN维度计算以下 Flag：
ChuckOrSlotidSatisf-TRUE，则为 TRUE，否贝内 FALSE。
CanAutoSplitFlag CD若CD StatusPuunoNE pusplitflag二Y且Pilot为空目
ChuckOrSlotidSatisfy-TRUE，则为 TRUE百贝 FALSE。
TRUE：否则为FALSE。J
按Lot 维度汇总（各STN 的 Flag取OR）筛选 CanAutoSplitFlag OVLTRUE 或
CanAutoSplitFlag CD-TRUE) 月 HaveOtherAvailableSTN-FALSE 的 Lote
存在CD站点？ （不清是条件）
存在uho站？
（不满足条件）
（不满足条件
中在RCO？ （不满足养件）
HONON
```

</details>

### 第 005 张：5.jpg

![[00.raw-materials/10.sources/images/LithoAutoPirun优化/5.jpg]]

关键 OCR 行：
- （限足所有条件）
- 1.4Lot与Context排序
- 对Lot 排序及并byContetx循环排选最优SplitLot。
- L4.1Context统计与Lot排序
- 判断 Lot 是否为 STRMSTRLot（是否在表ystrmstr lot中）：若是 STRMSTRLot且RemainQ
- 8，则记NonPreferFlag-Ture，反之为Flase·
- 按以下优先级对Lot排序：
- ?NonPreferflag-Flase优先 STRMSTRLot优先
- eutureHold?
- 群在RC装忧？
- OVL/CD状态黑足？
- PUONON/Fd) （不满件）

<details>
<summary>展开完整 OCR</summary>

```text
eutureHold?
群在RC装忧？
OVL/CD状态黑足？
PUONON/Fd) （不满件）
Paot为空？
Chuck/sota?
商有位微可用益可分批）
进入AutoSpli颜选Lot
（限足所有条件）
1.4Lot与Context排序
对Lot 排序及并byContetx循环排选最优SplitLot。
L4.1Context统计与Lot排序
获取Lot当前站点距Litho 站点的乘余Step数量，记为GapIoLitho（值越小越优）。
判断 Lot 是否为 STRMSTRLot（是否在表ystrmstr lot中）：若是 STRMSTRLot且RemainQ
8，则记NonPreferFlag-Ture，反之为Flase·
按以下优先级对Lot排序：
DMIN(GapToLitho) 距Litho站点越近越优先
RemainO越少越优先无Remain赋值9999）
?NonPreferflag-Flase优先 STRMSTRLot优先
L4.2Context均衡分配（fullSTNindex）
```

</details>

### 第 006 张：6.jpg

![[00.raw-materials/10.sources/images/LithoAutoPirun优化/6.jpg]]

关键 OCR 行：
- (1）按Ltho 机台 name分组并编号，记为 Index2：组内排序编号记为Index；统计机台总数量记为
- (3）Lot+Context按fullSTNindex排序
- 按排序后的Context依次选择SplitLot，每轮循环结束后去除已选的Context和Lot，继卖下一轮挑选，
- 15Pilot选片逻辑
- 从SplitLot中按规则选择Wafer 作为Pilota
- 1.5.1Wafer分组
- 拿取 14中选定的Context 及 SplitLot，将 Split Lot 的 Wafer 分为以下层级：+
- （1）Group层：按 Wafend编号，Wafenid#1-#10 的Wafer 划入Groupl，Wafenid#11-#25的Wafer
- （2）SubGroup层：若Lot有Chuck信息，则 Chuck1（C1）的Wafer一SubGroupl，Chuck2（C2）
- 的 Wafer一SubGroup2；否则按SlotMap，奇数 Slot的 Wafer一SubGroupl，偶数 Slot的Wafer一
- L5.2Wafer排序与选择+
- 在 Group +SubGroup 内按 wafernd排序并编号，记为 WaferRank·按以下优先级排序：

<details>
<summary>展开完整 OCR</summary>

```text
为避免不同Context的lot被集中分配到同一机台：
(1）按Ltho 机台 name分组并编号，记为 Index2：组内排序编号记为Index；统计机台总数量记为
Index3
(2）计算公式：fulSTNindex-(Index-DxIndex3+Index2
(3）Lot+Context按fullSTNindex排序
L4.3按Context循环挑选
按排序后的Context依次选择SplitLot，每轮循环结束后去除已选的Context和Lot，继卖下一轮挑选，
直至无可用Context或无可用Lot。
15Pilot选片逻辑
从SplitLot中按规则选择Wafer 作为Pilota
1.5.1Wafer分组
拿取 14中选定的Context 及 SplitLot，将 Split Lot 的 Wafer 分为以下层级：+
（1）Group层：按 Wafend编号，Wafenid#1-#10 的Wafer 划入Groupl，Wafenid#11-#25的Wafer
划入Group2。
（2）SubGroup层：若Lot有Chuck信息，则 Chuck1（C1）的Wafer一SubGroupl，Chuck2（C2）
的 Wafer一SubGroup2；否则按SlotMap，奇数 Slot的 Wafer一SubGroupl，偶数 Slot的Wafer一
SubGroup2。-
(3）GroupRank 值：Group1-SubGroupl-1:Group1-SubGroup2-2;Group2-SubGroup1-3；Group2
SubGroup2=4。-
L5.2Wafer排序与选择+
在 Group +SubGroup 内按 wafernd排序并编号，记为 WaferRank·按以下优先级排序：
MINWaferRank);@MN(GroupRank)+
选择规则：
（1）若Context对应的pisplitcmt有值，则按排序顺序排选puspltcnt片Wafer 作为pusplituaferi
（2）若pisplitcm无值且Wafer总数6，则安排序顺序兆选6片Wafer作为Pspwae+
（3>否则无需挑选，直接特SpltLot整体作力Pilota
流程图：
```

</details>

### 第 007 张：7.jpg

![[00.raw-materials/10.sources/images/LithoAutoPirun优化/7.jpg]]

关键 OCR 行：
- 以上全部计算结果存入Report：Central GetLithoR2RAutoPirunInfo，供AMA 读取执行。
- 2.Assign和Rule相关逻辑
- 在LithoAssign/LithoRule中增加Pilot相关逻辑的修改，以及新增Pilot加速的Global Sorting
- 针对Pi SplitFlag-Y 且R2RCDOVL Status-PinunON 且无Pilot 的场景，修改 Pilot 的选取规则。
- 当无Pilot时，取排序第一的 Lot 作为 Pilote+
- 2.12现逻辑
- 在 RTD Global Sorting 中新增 Piulot 加速逻辑
- 1.6Report输出
- Report栏位包括：toolid、toolname productidlavenid、retucleidprereticleprotool custom context value
- prelaver pilot, STNSite.
- 2.1LithoAssign/RuleLithoRule修改
- 2.1.1原罗辑+

<details>
<summary>展开完整 OCR</summary>

```text
1.6Report输出
以上全部计算结果存入Report：Central GetLithoR2RAutoPirunInfo，供AMA 读取执行。
Report栏位包括：toolid、toolname productidlavenid、retucleidprereticleprotool custom context value
prelaver pilot, STNSite.
2.Assign和Rule相关逻辑
在LithoAssign/LithoRule中增加Pilot相关逻辑的修改，以及新增Pilot加速的Global Sorting
2.1LithoAssign/RuleLithoRule修改
针对Pi SplitFlag-Y 且R2RCDOVL Status-PinunON 且无Pilot 的场景，修改 Pilot 的选取规则。
2.1.1原罗辑+
当无Pilot时，取排序第一的 Lot 作为 Pilote+
2.12现逻辑
当无Pilot时，增加划断：LithoAssign和LithoRule中，针对Pi SpltFlag-Y且R2RCD/OVL
Status-PIRUNON，对lot卡控ReasonR2RAutoPirunControl，待AutoSpltPinun功能确定Pilot。
22Pilot加速Clobal Sorting
在 RTD Global Sorting 中新增 Piulot 加速逻辑
```

</details>

### 第 008 张：8.jpg

![[00.raw-materials/10.sources/images/LithoAutoPirun优化/8.jpg]]

关键 OCR 行：
- Global Sortung判断：若当前Lot的lotid 等于上述任未源的 pilot值，则生效 Pilot-l：反之按原逻
- CDPilot加速逻辑与OVL一致：
- 数据来源：从表rtd rarlot history 和fiuwipstephistory中获取近三天历史数据居·获取lotud productid
- 逻辑判断。
- AMA新增逻辑
- AMA根据Repont结果向MEScall分批接口并将分出的Pilot传给R2R
- AMA读取Report后、执行分批接口前，需核对以下条件：
- <5）Wafer校验：确Repont中选中的Wafer确实存在于该Lot中。
- 检查后的lot根据repont结果分出对应Wafer作为Pilot。
- 2.2.1OVLPilot加速
- 数据来源从表nd r2rlitho context ovi中获取 layerid、olstatus、pilot等栏位，筛选出oxlstatus
- PirunON对应的pilot

<details>
<summary>展开完整 OCR</summary>

```text
2.2.1OVLPilot加速
数据来源从表nd r2rlitho context ovi中获取 layerid、olstatus、pilot等栏位，筛选出oxlstatus
PirunON对应的pilot
数据来源：从表nd r2rlothistory 和fwwipstephistory中获取近天历史数居，获取 lotid
productud、plot、process subrype、stagename 栏位。从表fiwlot、fablotext中获取lot当前stage筛选出
process subtrype-Litho 且 pilot-OVLY且当前stage-stagename的pilot
Global Sortung判断：若当前Lot的lotid 等于上述任未源的 pilot值，则生效 Pilot-l：反之按原逻
辑断。
2.2.2CDPilot加速
CDPilot加速逻辑与OVL一致：
数据来源：从表ntd r2r ltho context cd 中获取 layerid、cd status、pilot等栏位，筛选出：cd status
PinunON对应的pilot。
数据来源：从表rtd rarlot history 和fiuwipstephistory中获取近三天历史数据居·获取lotud productid
pilot、process subtrype、stagename栏位从表fiwlot、tablotext 中获取lot 当前 stage筛选出：
process subtrype Litho且pilot-CD/ Y且当前 Stage-stagename的pilot
Global Sonting 半断：若当前Lot 的lotid 等于上述任来源的pilot 值，则生效Pilot-1，反之按原
逻辑判断。
AMA新增逻辑
AMA根据Repont结果向MEScall分批接口并将分出的Pilot传给R2R
工分批检查
AMA读取Report后、执行分批接口前，需核对以下条件：
（1）Lot厂别校验：确认分批Lot属于本厂（FAB6或FAB8）。
（2）Lot状态校验：确认Lot当前状态为WaitForJobPrep 且当前站点runcardid 为空。
（4）Camier类型校验：确认CanerKind-FOUP
<5）Wafer校验：确Repont中选中的Wafer确实存在于该Lot中。
检查后的lot根据repont结果分出对应Wafer作为Pilot。
2向R2R传
```

</details>

### 第 009 张：9.jpg

![[00.raw-materials/10.sources/images/LithoAutoPirun优化/9.jpg]]

关键 OCR 行：
- 2当该ot被系统选中plot目扶行分批动作时若执行失败 则AMA汽行自动分批失败的lothold住hodconnentR2RAutoSpltExeauteFail
- 需求内容 BeausefxxXXX（报告技行自动分批失败原因）
- 住具他正常lot仍可板AMA当作pilot热行分批
- 4当同stagenane存在不同的lotname但tname前码相同时，当作一个etE，当该t组内有ot被设定大plot时其他lot环不手被AMA选为pilot
- 生产影响 当分批失败时会触发AMAH需二程部及时处理
- 工程响 兰影批封会触发AMAHOd需工程及时处
- 需末项目 R2RAutOSOltPin能优化
- 方适免cossFABot行分批失败故不优先已设定futuremerge、Elot物理位置不处于同一FAB的lot当作plot
- 2大是免同一ot组下含有多前层的lot，故不优先将lotname前码相同的不同lot再次设定大eilot
- 兰行自动分批选时不优先选择带futuremerge巨子三批不在同一FAB的当作piot
- s当同context下，当站三有执行自动分批失败的lot并巨又到站同至的带有tremege的et时不再将该lot排选为自动分批的lot，也不多效lothold
- 效益型

<details>
<summary>展开完整 OCR</summary>

```text
需末项目 R2RAutOSOltPin能优化
方适免cossFABot行分批失败故不优先已设定futuremerge、Elot物理位置不处于同一FAB的lot当作plot
2大是免同一ot组下含有多前层的lot，故不优先将lotname前码相同的不同lot再次设定大eilot
兰行自动分批选时不优先选择带futuremerge巨子三批不在同一FAB的当作piot
2当该ot被系统选中plot目扶行分批动作时若执行失败 则AMA汽行自动分批失败的lothold住hodconnentR2RAutoSpltExeauteFail
需求内容 BeausefxxXXX（报告技行自动分批失败原因）
s当同context下，当站三有执行自动分批失败的lot并巨又到站同至的带有tremege的et时不再将该lot排选为自动分批的lot，也不多效lothold
住具他正常lot仍可板AMA当作pilot热行分批
4当同stagenane存在不同的lotname但tname前码相同时，当作一个etE，当该t组内有ot被设定大plot时其他lot环不手被AMA选为pilot
效益型
计算方式制造或工程 当同一FouP存在多前层的情兄时ot过货完前t多的proces站点，需是老费近倍的时间我是个ot多用个FoUPquota
部培写，尽量教字化
涉及制造科科室可多选六区 及制造科主任 评信者 浅及工程部风险 邹天飞季
选择DSP组别 DSPTEDSTEE
风险等级
预期影响 影响描述 风险评估等级
生产影响 当分批失败时会触发AMAH需二程部及时处理
工程响 兰影批封会触发AMAHOd需工程及时处
系统影响
综合风险等级
```

</details>
