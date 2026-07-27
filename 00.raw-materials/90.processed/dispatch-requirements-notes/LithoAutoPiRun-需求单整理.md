---
type: dispatch-requirement-note
source_folder: LithoAutoPiRun
topic: 自动派工需求
tags: [自动派工, 需求单, OCR, 需求整理]
---

# LithoAutoPiRun - 需求单整理

## 资料概况

- 原始图片目录：[[00.raw-materials/10.sources/images/LithoAutoPiRun]]
- OCR 输出目录：[[00.raw-materials/90.processed/dispatch-requirements-ocr/LithoAutoPiRun]]
- 图片数量：8
- 初步主题：自动派工需求
- 处理状态：已 OCR，已建立初步结构化笔记
- 注意：本笔记基于 OCR 自动识别，关键需求点需回看原图确认。

## 自动识别到的关键信号

- 系统对象：EQP, FOUP, Lot, Port, Recipe, Step, Tool
- 派工逻辑：Rule, 排序, 派工, 规则
- 约束条件：Capability, Hold, QTime
- 系统接口：AMA, MES, RTD
- 验证信息：结果, 需求

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

![[00.raw-materials/10.sources/images/LithoAutoPiRun/1.jpg]]

关键 OCR 行：
- 申请人员：温洁奇 功能模快（类别为3时必填）=智能派工系统（RTD/DSP）
- 当前LithoAutoSplitPinn 为逻辑分批，分出的Pilot与母批在同Foup，跨厂场景下会因同FoUP Lot
- Transfer限制，导致Pilot无法及时Pinun对产线WiP流通造成景影响。另外因AutoPirun只针对满足分批条件
- 的Lot自动设置为Pilot进行Pirun，不满足条件的Lot会被一直卡控，导致产线许多LotOverQtime。因此需
- 将LithoAutoSplitPinn为由逻辑分批修改为物理分批，并优化Pilot选择逻辑。
- 将LithoAutoSplitPinun为由逻辑分批修改力物理分批，并优化Pilot选择逻辑。
- 减少LotoverQtime风险
- 需求内容（可添加附件）：
- 方案逻辑：
- RTD新增逻辑
- 1修改Report：Central GetLithoR2RAutoPinuninfo 中的Pilot 选择逻辑，2增加 Report：
- LithoPLotAutoDoAdhocSorter：3Rule和Assign中增加子母批作业同一机台逻辑

<details>
<summary>展开完整 OCR</summary>

```text
新增需火中请单
编号： （比处由信息技术部填写）
类别（请在方框内打勾）：口1软件采购 2硬件采购 3.功能开发4.工程及服务
申请部门：制造部 系统名称（类别内3时必填）：CIM计算机集成制造系统Fab6
（科））
申请人员：温洁奇 功能模快（类别为3时必填）=智能派工系统（RTD/DSP）
申请日期：2026-07-24 希望交付期：2026-0729
项目简介和必要性分析：
当前LithoAutoSplitPinn 为逻辑分批，分出的Pilot与母批在同Foup，跨厂场景下会因同FoUP Lot
Transfer限制，导致Pilot无法及时Pinun对产线WiP流通造成景影响。另外因AutoPirun只针对满足分批条件
的Lot自动设置为Pilot进行Pirun，不满足条件的Lot会被一直卡控，导致产线许多LotOverQtime。因此需
将LithoAutoSplitPinn为由逻辑分批修改为物理分批，并优化Pilot选择逻辑。
项目投资方案比较及效果分析折：
改善方案：
将LithoAutoSplitPinun为由逻辑分批修改力物理分批，并优化Pilot选择逻辑。
效果分析：
减少LotoverQtime风险
需求内容（可添加附件）：
方案逻辑：
RTD新增逻辑
1修改Report：Central GetLithoR2RAutoPinuninfo 中的Pilot 选择逻辑，2增加 Report：
LithoPLotAutoDoAdhocSorter：3Rule和Assign中增加子母批作业同一机台逻辑
IReport:Central CetLithoR2RAutoPirunlnfo
对选1ot和选片逻辑进行修改。
11Lot获取
从FAB6和FAB8 两厂获取待判断Lot，并进行初步过滤。
L1ILot基础信息获取
通过表fwlot获取appid，pnority，processngstatus，componentqty栏位信息；
通过表fablotext获取requiredcapabilityruncardid，reticleid位信息
```

</details>

### 第 002 张：2.jpg

![[00.raw-materials/10.sources/images/LithoAutoPiRun/2.jpg]]

关键 OCR 行：
- 通过fabnqtimeprocess获取RemainQ栏位信息
- 从UIRTDConfig LITHOLotAssignment-LithoAssignCapability 中获取LithoCapability。
- 112基础过滤条件
- K1）基本条件过滤：筛选出满足processingstatus-Active orCrossFabTransfered，camerkind-FOUP
- runcardid 为空，requiredcapability In (LithoCapability,L-BARCO-L,L-BARCO S)的Lot
- CrossFabTransfered）的Lot（IsTransferLot指标经istransferlotmarco判断得到
- 获取Lot后续站点信息并进一步判断是否符合AutoPinun条件。
- 对通过11筛选的Lot，向下Fetch20站，获取每个站点的productname、planname、stage、capability
- 1.2.2其他过滤条件
- （2）Specify判断：判断lot是否在r2r litho whitelist（匹配productid、layer、lotid）中，若在则过滤Lot。
- （3）同FoupPilot判断：从表rntdr2rlitho contextov/cd和rtd r2rlothistory获取LithoPilot，判断同
- （4）FutureHold 判断：从表fabfutureaction获取PinunLoop中每个站点的FutureAction信息，判断Loop

<details>
<summary>展开完整 OCR</summary>

```text
通过表fablotcarierext获取camierkind栏位信息
通过fabnqtimeprocess获取RemainQ栏位信息
从UIRTDConfig LITHOLotAssignment-LithoAssignCapability 中获取LithoCapability。
112基础过滤条件
对章取的Lot执行以下过滤：
K1）基本条件过滤：筛选出满足processingstatus-Active orCrossFabTransfered，camerkind-FOUP
runcardid 为空，requiredcapability In (LithoCapability,L-BARCO-L,L-BARCO S)的Lot
（2）跨厂信息去重：筛选出满足 IsTransferLot-True 或CIsTransferLot#True 且processingStatus
CrossFabTransfered）的Lot（IsTransferLot指标经istransferlotmarco判断得到
12获取Pirun站点并对lot进一步过滤
获取Lot后续站点信息并进一步判断是否符合AutoPinun条件。
12.1PirunLoop信息获取
对通过11筛选的Lot，向下Fetch20站，获取每个站点的productname、planname、stage、capability
Lot当前站点到最后一道CD站点即为一段PinunLoop。若lotFetch站点中无CD站点，则过滤该Lot
1.2.2其他过滤条件
点。若无则过滤Lot。
（2）Specify判断：判断lot是否在r2r litho whitelist（匹配productid、layer、lotid）中，若在则过滤Lot。
（3）同FoupPilot判断：从表rntdr2rlitho contextov/cd和rtd r2rlothistory获取LithoPilot，判断同
Foup中是否有LithoPilot，若有则过滤Lot。
（4）FutureHold 判断：从表fabfutureaction获取PinunLoop中每个站点的FutureAction信息，判断Loop
中是否存在FutureHold，若有则过滤Lot。
（5）RC判断：判断 PirunLoop中是否存在RC站点，若有则过滤Lot。
1.3R2R条件断
获取1ot在可作业机台的R2R状态，并判断1o是否存在多路径
13.1可作业机台获取
```

</details>

### 第 003 张：3.jpg

![[00.raw-materials/10.sources/images/LithoAutoPiRun/3.jpg]]

关键 OCR 行：
- 拿取12 中Lot的Litho 站点，经TransferMarco判断后，若Lot 在Litho 站点能 Transfer则同时章取
- By机台别从表rtd r2r litho add setting中获取 Lot 在机台的 Pi split flag 和pi splitcnt。若Lot不存
- 将剩余lot在Litho站点的机台经过EQPStatus、LCC、Capabiity、Recipe、PPID、Global Reason判断，
- 13.2多路径判断
- By Lot-STN+Reticle维度从表 rtd 2rlitho context ovi 和 rtd r2r litho context cd 匹配R2R 状态，并
- 1L.4选Lot规则
- By Context为Lot排序并挑选最优Lot
- 获取13过滤后的Lot及Context信息，栏位包括Lot、STN、Reticle.Prod、Layer、Recipe、Pretool
- .4.2Context内Lot排序
- 获取lot的排序指标
- （2）判断Lot的片数是否大于等于Pisplitcnt（黑认为4），若是则SplitCntMatched-1，否则为0；
- （3）若Lot存在prelayer，则从表2r litho waferhistory 中获取每片Wafer的Chuck 信息；否则从表

<details>
<summary>展开完整 OCR</summary>

```text
拿取12 中Lot的Litho 站点，经TransferMarco判断后，若Lot 在Litho 站点能 Transfer则同时章取
对厂Litho机台。
By机台别从表rtd r2r litho add setting中获取 Lot 在机台的 Pi split flag 和pi splitcnt。若Lot不存
在Pi splitflagT的机台，则过滤Lot
将剩余lot在Litho站点的机台经过EQPStatus、LCC、Capabiity、Recipe、PPID、Global Reason判断，
若存在卡控则筛除对应机台。
13.2多路径判断
By Lot-STN+Reticle维度从表 rtd 2rlitho context ovi 和 rtd r2r litho context cd 匹配R2R 状态，并
半断是否存在 R2R Reason。筛选出满足：OVL Status InPirunON ONFixed)CD Status In(PinunON ON
Fixed）且无R2RReason的Context(ByLot-STN+Reticle)
ByLot统计Context数量，若ContextCount>1且存在OVL Status In(ON.Fixed)且CDStatusIn(ON,Fi区xed)
的Context，则认为Lot存在多路径，过滤该Lot。
1L.4选Lot规则
By Context为Lot排序并挑选最优Lot
L.4.1AutoPirunContext筛选
获取13过滤后的Lot及Context信息，栏位包括Lot、STN、Reticle.Prod、Layer、Recipe、Pretool
Prereticle.Custom ContextValueCD StatusOVL Status.Pilot CD.Pilot OVL.Pi splitflag.Pi splitcnt.
筛选出满足Pi splitflag-Y且（PilotCD为Null或PilotOVL为Null的Context，即为需要自动Pirun的
.4.2Context内Lot排序
获取lot的排序指标
（1）计算Lot当前站点距 Litho 站点的剩余 Step 数量，记为GapToLitho：
（2）判断Lot的片数是否大于等于Pisplitcnt（黑认为4），若是则SplitCntMatched-1，否则为0；
（3）若Lot存在prelayer，则从表2r litho waferhistory 中获取每片Wafer的Chuck 信息；否则从表
fsmaterialassociation 中获取Wafer的 Slot信息。判断Lot是否满足包合C1C2（或Slot奇偶）各大于等于
两片，若是则RequiredChuckCount-1，否则为0，
（4>判断Lot是否为空机空LpLot，若是则BulletLot-1，否则为os
（5若LotRemainQ有值且大于0，贝指标RemanQ力lot剩余Qtime，否则为9909
```

</details>

### 第 004 张：4.jpg

![[00.raw-materials/10.sources/images/LithoAutoPiRun/4.jpg]]

关键 OCR 行：
- 按以下优先级对Lot排序，并记为力RTDRank：
- 1.42Context之间排序
- 均衡分配，需要对Context进行排序。
- Context排序指标：
- 的STN-ReticleOnSTN，则ReticleSINRank-1，循环中，若Context与上轮排序第一的Context属于同一组，
- 最终按以下优先级对 Lot-Context排序
- @Min(RTDRank)
- 将排序第一的Lot-Context固定，作为已选Pilot的Context，并去除lotContext与已选Context相同的其
- 15Pilot选片逻辑
- 判断Lot是否要整批设为Pilo，不满足的需要选片进行物理分批。
- （6）若Lot在表guota applyinf。中且Keylot=lStatus-CONFIRM，则指标KeyLot-1，否则为0。
- DMin(GapToLitho)

<details>
<summary>展开完整 OCR</summary>

```text
（6）若Lot在表guota applyinf。中且Keylot=lStatus-CONFIRM，则指标KeyLot-1，否则为0。
按以下优先级对Lot排序，并记为力RTDRank：
DMin(GapToLitho)
@Max(SplitCntMatched)
?Max (RequredChuckCount)
@Max(BulletLot)
5Min(RemainQ)
@Min(KeyLot)
1.42Context之间排序
Lot存在多个Pirun Context时，为实现使用同一Reticle的Lot尽量分配到同一机台，不同Reticle的lot
均衡分配，需要对Context进行排序。
Context排序指标：
（1）ByReticle-STN给Context分组，获取Reticle当前所在机台信息ReticleOnSTN，循环前，若Context
的STN-ReticleOnSTN，则ReticleSINRank-1，循环中，若Context与上轮排序第一的Context属于同一组，
则ReticleSTNRank-1，否则为0。
（2》统计Contetx内当前可选Lot的数量，记作ContextCandidateCount。
（3）BySTN统计已选择Pilot的Contetx数量，记作ActualSTNPilotCount
最终按以下优先级对 Lot-Context排序
D Max(ReticleSTNRank)
Min(ContextCandidateCount)
3)Min(ActualSTNPilotCount)
@Min(RTDRank)
L4.3Context循环挑选Pilot
将排序第一的Lot-Context固定，作为已选Pilot的Context，并去除lotContext与已选Context相同的其
他LotContext，在更新ReticleSTNRank、ContextCandidateCount、ActualSTNPilotCount指标后，进入下一轮
循环，直至无可用Context或无可用Lot后，结束循环。
15Pilot选片逻辑
判断Lot是否要整批设为Pilo，不满足的需要选片进行物理分批。
```

</details>

### 第 005 张：5.jpg

![[00.raw-materials/10.sources/images/LithoAutoPiRun/5.jpg]]

关键 OCR 行：
- 2）Lot 的CurCapability-LithoCapabilityEFullRemainQ
- 1.5.2物理分批选片逻辑
- 不满足151场景时，Pilot需要物理分批，FlagIsNeedSplit生效T并进行选片，规则如下
- 1521Wafer分组
- 将Lot的Wafer分为以下层级：
- （1Group 层：按Wafend编号，Wafend#1-#1o 的 Wafer 划入Group1Wafend#11-#25的Wafer
- （2）SubGroup 层：若Lot有 Chuck 信息，则 Chuckl （C1）的 Wafer一SubGroupl，Chuck2（C2）
- 的 Wafer一SubGroup2：否则按 SlotMap，奇数 slot 的 WaferSubGroupl偶数 Slot 的Wafer一
- 15.22Wafer排序与选择
- 在 Group +SubGroup 内按 waferid 排序并编号，记为WaferRank。按以下优先级排序：
- MN(WaferRank);@ MIN(GroupRank)
- 选择规则：

<details>
<summary>展开完整 OCR</summary>

```text
1.5.1整批设为Pilot场景
（1bLot生效BulletLot-1或KeyLot-1
2）Lot 的CurCapability-LithoCapabilityEFullRemainQ
（3Lot的指标RequiredChuckCount-0
4Lot的指标SplitCntMatched-0：
5Lot的片数componentqty<-6
1.5.2物理分批选片逻辑
不满足151场景时，Pilot需要物理分批，FlagIsNeedSplit生效T并进行选片，规则如下
1521Wafer分组
将Lot的Wafer分为以下层级：
（1Group 层：按Wafend编号，Wafend#1-#1o 的 Wafer 划入Group1Wafend#11-#25的Wafer
划入Group2。
（2）SubGroup 层：若Lot有 Chuck 信息，则 Chuckl （C1）的 Wafer一SubGroupl，Chuck2（C2）
的 Wafer一SubGroup2：否则按 SlotMap，奇数 slot 的 WaferSubGroupl偶数 Slot 的Wafer一
SubGroup2.
(3)GroupRank 贝值：Groupl-SubGroupl-1:Group1-SubGroup2-2;Group2-SubGroup1-3:Group2
SubGroup2-4.
15.22Wafer排序与选择
在 Group +SubGroup 内按 waferid 排序并编号，记为WaferRank。按以下优先级排序：
MN(WaferRank);@ MIN(GroupRank)
选择规则：
若Context对应的pisplitcnt 有值，则按排序顺序挑选pisplitcnt片Wafer 作为pisplitwafer否则
按排序顺序挑选4片Wafer作为pisplitwafer
将pisplitwafer分批后设为Pilot。
L53Merge站点设定
若Lot有ADI站点不包含 SRC，则lot需物理分批时，将第一道ADI设为Merge站点，否则将
最后道CD 设力Merge站点·
L6输出Report
以上全部计算结果存入Report：Central GetLithoR2RAutoPinunInfo，供AMA 读取热行。
```

</details>

### 第 006 张：6.jpg

![[00.raw-materials/10.sources/images/LithoAutoPiRun/6.jpg]]

关键 OCR 行：
- pi splitwafer,IsNeedSplit,isSTNSite
- 获取需要TransferFoup的LithoPilot，判断逻辑如下：
- 212筛选判断：
- 2.2TransferFOUP翔判断
- 2.3Carrier排序规则
- 对于需TransferFOUP的LithoPilot进行排序，拿取LithoPilot的RemainQ、Priority、componentqty指标
- 并按照Mim(RemainQ）、Min(Priority）、Max（componentqty）排序，根据排序建立AdhocSorterJob。
- 从 AMATriggerConfig-WatchDog LithoPiLotAutoDoAdhocSorter 拿取 Switch、 Tnigger Time Slot
- TriggerCountTime栏位信息，当Switch-Y且当前时间在TnggerTimeSlot范围内时，将前TniggerCountTime
- 个需物理分批的Carnier结果存入Report：LithoPiLotAutoDoAdhocSorter中，栏位包括：Camer、Pilotextrastatus、
- Report 栏位包括：Lot、toolid、productidlayend、reticleid、prereticle、pretool、custom contextvalue
- 2新增ReportLithoPiLotAutoDoAdhocSorter

<details>
<summary>展开完整 OCR</summary>

```text
Report 栏位包括：Lot、toolid、productidlayend、reticleid、prereticle、pretool、custom contextvalue
pi splitwafer,IsNeedSplit,isSTNSite
2新增ReportLithoPiLotAutoDoAdhocSorter
获取需要TransferFoup的Pilot。
2.1LithoPilot拿取
获取需要TransferFoup的LithoPilot，判断逻辑如下：
2.11数据获取：
从2r litho contextovl获取ovlstatus pilot栏位信息：从r2r litho contextcd获取cd status、pilot栏位
信息：从fwlot中获取appid、lottype、priority栏位信息；从fabcategorymap中获取lottype、category栏位信
212筛选判断：
筛选出满足priority5category-Production且（ovlstatus-PIRUNON 或cd status-“PIRUNON）
的Pilot，即为需要TransferFoup的LithoPilot。
2.2TransferFOUP翔判断
拿取2.1中LithoPilot的Carnier信息，By Carnier 从fuwlot中获取所有Lot，筛选出Lotextrastatus均为
WaitForJobPrep的Carrier。
若LithoPilot同Caier中存在其他Lot时，则该Pilot需要ChangeFoup。
2.3Carrier排序规则
对于需TransferFOUP的LithoPilot进行排序，拿取LithoPilot的RemainQ、Priority、componentqty指标
并按照Mim(RemainQ）、Min(Priority）、Max（componentqty）排序，根据排序建立AdhocSorterJob。
2.4输出Report
从 AMATriggerConfig-WatchDog LithoPiLotAutoDoAdhocSorter 拿取 Switch、 Tnigger Time Slot
TriggerCountTime栏位信息，当Switch-Y且当前时间在TnggerTimeSlot范围内时，将前TniggerCountTime
个需物理分批的Carnier结果存入Report：LithoPiLotAutoDoAdhocSorter中，栏位包括：Camer、Pilotextrastatus、
StatusRemainOPieces.Prod,Priority
3.Rule中新增卡控罗辑
在GlobalMacro中新增对需导FoupLithoPilot的卡控：在LithoRule中增加子母批Run相同机台的卡控
3.1ClobalMacro新增卡控逻箱
```

</details>

### 第 007 张：7.jpg

![[00.raw-materials/10.sources/images/LithoAutoPiRun/7.jpg]]

关键 OCR 行：
- 不在 AdhocSoter站点的Other Lot需要卡控Reason WaitPilotChangeFOUP。Remove规则：当Other Lot在
- 3.2LithoRale新增卡控逻辑
- 3221判断lot是否有Pretool
- curlayer从r2rlitho_contextov获取pretool，当lot存在pretoo不为空时，则需要后续判断。
- productid，layend获取最新一笔子批母批在待判断lot当前layer的作业机台toolid。
- 3223判断是否需卡控
- 通过2rlitho whitelist判断（匹配productid、layend、lotid）lot是否为SpecifyLot，针对非SpecifyLot，
- 若待判断lot的机台与子批/母批作业机台toolid不一致，则卡控Reason：Parent&ChildLotNeedRunSameTool
- 否则按原逻辑判断
- 4LithoAssign新增卡控逻辑
- LithoAssign增加子母批Run相同机台的卡控，并保有原R2RAutoPinunControl逻辑。
- 拿取21中的LithoPilot，当 WatchDog LithoPiLotAutoDoAdhocSorte中的Switch-Y且当前时间在

<details>
<summary>展开完整 OCR</summary>

```text
拿取21中的LithoPilot，当 WatchDog LithoPiLotAutoDoAdhocSorte中的Switch-Y且当前时间在
IniggerTime Slot范围内时，满足以下两种场景的lot需卡控Reason：
（1）若LithoPilot在AdhocSoter站点（adhocplanname包合“UnScheduleSorter，则LithoPilot同Foup
不在 AdhocSoter站点的Other Lot需要卡控Reason WaitPilotChangeFOUP。Remove规则：当Other Lot在
Litho站点时，不能Remove：当OtherLot在Barco站点时，RemainQ-4H或触发QuO时，Remove卡控，当
OtherLot在非Litho/Barco站点时，仅触发Qu o时，Remove卡控
2）若LithoPilot不在AdhocSoter站点，则LithoPilot和同Foup不在AdhocSoter站点的OtherLot者都需
要卡控Reason WaitPilotChangeFOUPRemove规贝：OtherLotFollow（D，LithoPilot 的RemainQ-4H或触
发Qu0时、Remove卡控
3.2LithoRale新增卡控逻辑
3.2.1R2RAutoPirunControl控
针对非SpecifyLot，若Pi SplitFlag-Y且R2RCDOVLStatus-PIRUNONPilot为Null，则卡控
ReasonR2RAutoPirunControl，否则不卡控
3.2.2Parent&ChildLotNeedRunSameTool卡控
3221判断lot是否有Pretool
从表2rlitho context relation中获取productid、cur layer、pre layer栏位信息，从r2rltho_contextovi中
获取productid、layerid、pretool栏位信息；
ByProdlayer从2r litho contextrelation（匹配productid、pre layer）获取curlayer，再通过Prod
curlayer从r2rlitho_contextov获取pretool，当lot存在pretoo不为空时，则需要后续判断。
3222获取子母批作业机台
通过表fabfutureaction拿取和lot有FutureMerge关系的子批母批lot，从表2rlothistory中（匹配Lotid、
productid，layend获取最新一笔子批母批在待判断lot当前layer的作业机台toolid。
3223判断是否需卡控
通过2rlitho whitelist判断（匹配productid、layend、lotid）lot是否为SpecifyLot，针对非SpecifyLot，
若待判断lot的机台与子批/母批作业机台toolid不一致，则卡控Reason：Parent&ChildLotNeedRunSameTool
否则按原逻辑判断
4LithoAssign新增卡控逻辑
LithoAssign增加子母批Run相同机台的卡控，并保有原R2RAutoPinunControl逻辑。
```

</details>

### 第 008 张：8.jpg

![[00.raw-materials/10.sources/images/LithoAutoPiRun/8.jpg]]

关键 OCR 行：
- 逻辑与LithoRule中一致，pretool获取和子批母批作业机台获取改为Central。
- ANLA新增逻辑
- pretool, custom context value, pi splitwaferIsNeedSplitisSTNSite.
- 当IsNeedSplit-T时，给MES物理接口，将pisplitwafer从Lot中分出，若未拿到可用空Foup或call分
- 获取Repont：LithoPLotAutoDoAdhocSorter栏位信息，并按顺序给MES打TransferFOUP接口，将Pilot
- 导到空FOUP中，若拿取可用的空Foup失收或空Foup数量为o，则在AMALog中记录Fail信息。
- 4.1R2RAutoPirunControl卡控
- 针对非SpecifyLot，若Pi SplitFlag-Y且R2R CD/OVL Status-PIRUNON且Pilot力Null，则卡控
- ReasonR2RAutoPinunControl，否则不卡控
- 4.2Parent&ChildLotNeedRunSameTool卡控
- 根据Report Central GetLithoR2RAutoPinuninfo 热行物理分批，并将 Pilot给到 R2R，根据Report：
- LithoPiLotAutoDoAdhocSorter热行TransferFoup

<details>
<summary>展开完整 OCR</summary>

```text
4.1R2RAutoPirunControl卡控
针对非SpecifyLot，若Pi SplitFlag-Y且R2R CD/OVL Status-PIRUNON且Pilot力Null，则卡控
ReasonR2RAutoPinunControl，否则不卡控
4.2Parent&ChildLotNeedRunSameTool卡控
逻辑与LithoRule中一致，pretool获取和子批母批作业机台获取改为Central。
ANLA新增逻辑
根据Report Central GetLithoR2RAutoPinuninfo 热行物理分批，并将 Pilot给到 R2R，根据Report：
LithoPiLotAutoDoAdhocSorter热行TransferFoup
获取Report Central GetLithoR2RAutoPirunInfo栏位信息Lottoolid.productid layenid.reticleid.prereticle.
pretool, custom context value, pi splitwaferIsNeedSplitisSTNSite.
L1整批设为Pilot
当IsNeedSplit-F时，直接将整批Lot传给R2R。
1.2物理分批Pilot
当IsNeedSplit-T时，给MES物理接口，将pisplitwafer从Lot中分出，若未拿到可用空Foup或call分
批接口Fai，则将整批Lot传给R2R，否则将分出的子批pilot传给R2R。
2.TransferFoup
获取Repont：LithoPLotAutoDoAdhocSorter栏位信息，并按顺序给MES打TransferFOUP接口，将Pilot
导到空FOUP中，若拿取可用的空Foup失收或空Foup数量为o，则在AMALog中记录Fail信息。
申请部门意见： 申请部门分管领导意见：
日期： 日期：
相关部门意见： 相关部门分管领导意见：
日期： 日期：
信息技术部意见： 信息技术部分管领导意见
日期： 日期：
```

</details>
