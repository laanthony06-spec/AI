---
type: ocr-result
topic: DSP派工系统简介
tags: [OCR, DSP, 自动派工, 派工系统]
---

# DSP 派工系统简介 - OCR 原文

> 图片数量：91。OCR 结果为自动识别，可能存在错字、漏字和表格顺序错位。

## 第 001 页：自动派工系统全面介绍

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p001.jpg]]

动画
评论
自动派工系统全面介绍
DSP
2025年05月08日

## 第 002 页：DSP系统介绍

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p002.jpg]]

编辑
01
DSP系统介绍
02
自动化功能介绍
03
APS系统介绍
04
监控工具

## 第 003 页：DSP系统介绍

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p003.jpg]]

编辑Y式
动画
01
Part
DSP系统介绍

## 第 004 页：自动化系统逻辑架构

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p004.jpg]]

自动化系统逻辑架构
系统架构设计
系统架构
生产管理准备 NPW准备 生产监控
淮备层 产能支持 投产规划 Season Dummy Outside Down grade Recycle
数据分析和物
料准备） 周期管理 产线调控 Monitor Inside 实时监控
Dummy
生产调度 全局 逻辑运算 执行派工 自动报警
机制层 产品片 NPW 派工清单 设备状态 艺要求 NPW处理 协同型
应急处置
存储管控
Bullet XCDA FOUP 存储平
商密三级 Lot Purge 监控层
Confidential I

## 第 005 页：全自动化系统信息架构

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p005.jpg]]

全自动化系统信息架构
RTD（实时派工系统） AMA（自动派工管理系统）
1.Sorting（排序功能） 1.派工触发和最终核对，支持LotPre-reserve
2.WhereNext（FOUP暂存指定功能） 2.NPW管理
FAB RTD AMA
EAP MCS 派工结果
APC PMS 厂信息 搬送存储 筛选排序
派工果求
RMS FDC 生成派工需求 NPW准备 派工核对
可派工清单
工厂信息 歡送需求 搬送结果 NPW需求 设备信息 派工结果 操作结果
MES
WIP FLOW MACHINE MONITOR
商密三级 上海华1
Confidential I
HLMC

## 第 006 页：实时自动派工逻辑（RTD）

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p006.jpg]]

实时自动派工逻辑（RTD）
应用调度参考的结果，检测实时限制和执行各区域派工规则，将产品派工到设备上。
所有设备群通用逻辑，筛选掉不能派工的Lot，如：
Global Lot /Foup/Machine/Port State
RTD Filter Qtime ZoneControl/Run Path（进入Q-zone前判断下游是否断线）
InhibitCheck，NPW时效性管控等
各设备群专用逻辑，根据设备特性筛选掉不能派工Lot，如：
Local Port绑定的 Capability/Recipe
Filter Buffer空间
Real-time R2R Result
Dispatching Basic 以通用的规则定义Lot排序因素，如：
Functions Global Remain Q-time Global Rank
Sorter Breaking TargetLot等
Request T/R 这些因素对各设备适用的规则相同（标准可能有所差异）
各设备群根据设备特性单独定义的Lo排序因素，如：
Local 源/膜种可连续性
Sorter 制品温度调控
可组批性，chamber利用等
MES数据 Sorting 各设备根据Sorter的重要性，对Lot进行综合排序（部分精细到号机）
Integrated
Functions Where Next 根据Lot的下一站点信息和各stocker的存储状态，选择Lot的最佳存储位置
商密三级
Confidential I

## 第 007 页：设备自动化模式

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p007.jpg]]

设备自动化模式
AUTO Mode Description
Manual Prep[lU]+JobIn[lUi]+JobOut[U]
JobPrep[IUI]+EAP(JobIn+JobOut)
AUTO-1:
AUTO1
EQP
Job Prep[IUI+ MCs +EAP(Job In+Job Out)+MCS(WhereNext)
AUTO-2
AUTO1.5
AUTO-2:
AUTO2
AUTO-3
AUTO3
Standbyto.bandleAlarm
Confidential I HLMC

## 第 008 页：Auto 2-Lot Reserve and Queue Consume

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p008.jpg]]

Auto 2-Lot Reserve and Queue Consume
With Queue WithoutQueue
Lot Reserve
Manual Lot Reserve and send FOUPto Load Port
MES RTD
Tool Efficiency MES RTD
-Lot Sorting Load Balance Toal Efficiency
Auto20 -Load Balance
MCS -Lat Sorting
ConsumeQueues
.ToolisreadytogetaFouUP
MCS
商密三级 上海华力
ConfidentialI HLMC

## 第 009 页：Auto 3-Lot Reserve and QueueConsume

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p009.jpg]]

Auto 3-Lot Reserve and QueueConsume
With Queue WithoutQueue
Lot Reserve
TogetaFOUP Auto Lot Reserve and send FOUP to Load Port
RTD MES MES RTD
ToolEfficiency -ToolEfficiency
Load Balance huto30 +Load Balance
Lot Sorting MCS Lot Sorting
Queue Consume
MCS
AMA
商密三级 上海华力
Confidential I HLMC

## 第 010 页：实时自动派工系统触发方式（AMA）

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p010.jpg]]

实时自动派工系统触发方式（AMA）
事件触发
每当某台设备状态发生切换、某个portevent发生变化或port派工模式发生变化时，会询问RTD派工
*运算
答复
定时触发
每隔5分钟
定时
Pre-send
Pre-send功能：根据EQP在作业Lot的剩余片数，提前给机台/port派工Lot
商密三级
Confidential I 10

## 第 011 页：自动化功能介绍

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p011.jpg]]

编辑
02
Part/
自动化功能介绍

## 第 012 页：Global派工规则 QzoneControl

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p012.jpg]]

编辑
02
Part/
Global派工规则 QzoneControl
Local派工规则 NPW
搬送存储

## 第 013 页：Global派工规则

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p013.jpg]]

Global派工规则
口概述：GlobalRule指各Module通用的DSP派工逻辑，从整体控线角度出发，确定最优的调度方案。涉及Lot基本属性、Foup属
性、机台状态、工艺限定等，但与机台的具体作业方式没有关系。
Get Lot list From MES 功能名称 从MES获取可派工Lot信忘，即，符合Lot状态OK/FOUP状态OK/DSP未禁止的Recipe/Reticdeinmachine/无 功能描述 LotComment/RTDInfo
Machine/Chamber均要处于可作业状态：此外，还要检毫所有关型的constrain限定 BatchID等条件的Lot，若RuncardLot定的机台非本机台，则不能派工 NotJobPrepLowPnonty: NotinFouce
CheckMachine
Multi Lot InOne Foup 同Foup中的其他Lot正在作业/已被Reserve时，该Lot不能派，用户设定的机台不可以作业与其他Lot共用FOUP的Lot EQPUnavailable:x,ChambarState:wo
Reason Check Qzone Control 未达到是少等待时间的Lot不能派工被qzone管控下游断线或产能不足的Lo坏不能派工 MultiLotBlock
（管控Lot不自动派工） Check Loop Lot Control 制造部限定qzoneloop的Wafer/Lot/FOUPcount时满足限定条件的Lot不能派工 MinqimeNotEnough:Pathissue,Caoacit
Check MFG control 制适部根据eqp.capabilityProdutiontype.prodid.stage.recipe.tech.flow.priorityquantityqtime等信密进行生产调 IsLoopLotControi
控时，满足设定禁止作业条件的LO不派工 MFG Control
Reserve Lot 已经被Preserve的Lot不能派工
Cancel Lot JobPrepCancel/Joblncancel的lot在10min内不能派工
AMA Mark Lot auto3派工失败而被Mark的Lot在10min内不优先作业 MultiJobPrepCancal;MulfiJotinCance
Qtime Urgency 计点Lot的QtimeUrgency案急Lot优先作业 IsByAMAMarkLot
Pnority Pnonty高的Lot优先作业 QLURGENCY0/1/2/CATEGORY
Rush Lot RushLot优先作业 lotSkipCantrol PRIOR 1/2:PRIOR
Target Lot MPC设定的TargetLot优先作业 Target 0/1Nalue
Sorting Broken Lot MPC设定高等级Lot达到导待时间limit的优先 BrokenLat
（排序规则） MFG Control 设定需要在该机台优先/不优先作业产品 RunPni PreferRunPn NonPrerer
Rework Lot ReworkLot优先作业 REWORK
Sub Lot 下游等待merge的Lot优先作业 SubLat
Small Lot 作业连续少枚数后大枚数LOt优先作业 SmallLot
Remain Qtime RemainQtime小的Lot优先作业 RemQTime
Rework Lot RQPri Rework过的Lot优先作业 ReworklatRQPni
Waiting Time 等待时间长的Lot优先作业 WaitingTime
ConfidentialI HLMC

## 第 014 页：常见问题查询

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p014.jpg]]

常见问题查询
产能/断线相关Case
>卡控Capacityissue或Pathissue可以在FABScheduler→QzoneControl中查看原因
使用方式：
1.可输入LotName点击“Submit"按钮，ByLot查询下游
Qzone整体元许放货量，及断线或堆货站点
2.点击模块1的RemainWIP，可查询Qzone中各站点允许放货量
3.点击模块2的RemainWIP.可查询Qzone中某站点各机台的可
作业情况。机台Mark黄色时表示该机台不可作业。
>常见卡控Capacitylssue情况：Lot在卓站点可作业机台IDLE，却卡控该站点的产能不足
主要原因：由于Bullet/KeyLot需要提前预留产能，但Bullet/KeyLot还需要一定时间才能到达当站，故会造成机台IDLE
Qtime Urgency
用于判定Qtime紧急程度，在FABSchedulerQtimeUrgency中查看
QU=RemainQT/Remain CT QT URGEY_O
皖·A·0N358·10 0.311
RemainCT=当前站点PT+中间站点CT+结束站点23CT QT URNBNOE 2 121
存在多Qtime（大包小）时，QU取最小。
针对QTUrgency 0的计算 QT_URGENCY_3 (23)
@.当QTUrgency-RemainQT/RemainCycleTimes0.3时生效 QT URGENCY_4 (34)
@.当RemainQT/RemainProcessTime1时QU0生效 QT_URGENCYS
商密三级 上海华
15 HLMO
Confidential I

## 第 015 页：Global派工规则 Qzone Control

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p015.jpg]]

动通
02
Part/
Global派工规则 Qzone Control
Local派工规则 NPW
搬送存储

## 第 016 页：LITHO派工规则 口编辑

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p016.jpg]]

LITHO派工规则 口编辑
口概述：综合考量Reticle、R2R、DomaPath、高低能、垂直限定等因素限制Lot在机台上可作业性，并结合预排程制定出相应的
符合LITHO区域设备特性的自动派工逻辑。
功能名称 功能猫述
R2R R2R控的Lot不留作业 LotComment/RTDInfo
Doma DomaPath开启时保证整条DomaPath可以作业 R2ROVL/CDFail
Reason 高低送 Litho机台连续作业高能产品后，内部单元温魔升高触发FDC，需限定高能连续作业 No Available Doma Path
（管控Lot不自动派工） 垂古限定 限定该层与上一层作业相同机台 Too ManyHighEnergy Lot
白名单 设备的白名单lot，只能作业XXX设备 Vertical Limit
ReticleAssign Loop内的lot存在同一reticle对应多个机台的情下，连环最起始站点的lot只能assign在loop内的机台上 white list of XX机台
LoopWIPLithoEQPContral
同Reticle连续作业 Reticle相同的优先连续作业
Reticle相同的Lot中的带Qtime的个数 ReticleContinue
Reticle相同的Lot中的TargetLot的个效 GroupQTimeCount
Recipe第5码相同的优先作业 GroupTargetCount
IsSameLithoRecipe5
Recipe第5码在同一Group的优先作业 IsSameLithoRecipeGroup5
Sorting Recipe第5码相邻Group的优先作业 IsNeighbourRecipeGroups
（排序规则 Recipe连续作业 Recipe第4码和第10码相同的优先作业 IsSameLithaRecipe410
Recipe第4码和第10码在同一Group的优先作业 IsSamelithoRecipeGroup410
输出待派工Lot中同RecipeGroup的Count数：Min(Count1设定的Continuelimit） RecipeGroupLotCount
待派工lot与最近一次机台作业lot的RecipeGroup相司，且RecipeGroupCount小手对应的continuelimit值时，Recipe RacipeGroupContinue
GroupContinue指标生效
Conmuenual 1 高低能 当温度低于Lower线时高能产品优先派货、介于Lower&Upper之间正常派货、大于Upper线禁上派货 HighEnergyLat

## 第 017 页：放版指导

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p017.jpg]]

放版指导
口放版指导：MASK需要人工进行退/放操作。根据LITHOAssign结果开发放版指导界面，提示用户及时将MASK放入设备
放版指导筛选条件
produachun
KREINELKR-IN Sube RedctePw nog
MachmeE经悦用：
mseanks
AssignAeiceR-ay RUN
AssignLotk+a) 814
Care总茶 188 138
202574/5 15:50:00
2025/43166000
2025/4316:50:30 IA动
2025/4/3:16:5020 InUse
2025/4516.5090 33
025143165080
20S/4/S16500 KAT动 250A PAOO096 InUse
2028/4/510.50.00 PA000276
放版推送时间和动作 Reticle信息 RS-CW 1208 预排该Reticle的Lot信息 Reticle当前位置及状态 Assign机台信息
Q-024144-8146 PA000530F 610
MA-813A DTLOH
UTACSS 26:70
6270
4(4)
WIPDetal
sin snfam STATUS PRIORI nin remal pretool RTDREASON INTERNALP HOLDO LOTTYFE REMQT RUNCA RETICUE PART STAGE RECPE
BLKRIA02 BLKRIA02 LKRFINS LKRFIN-S BP33505 BP33508 Actve Actve 0040010 004K10 CarnerPdu Assign机台和Lo的详细信息 Producti. Producte SE451 SK-051 051222 051272 BMARK BNARK LPO112 Q0300 003031
BLKRIA02 L-KRFIN-S BP33507 Active 0040010 Phoducti S051 051022 BMARK LPO12 00300

## 第 018 页：常见问题查询

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p018.jpg]]

常见问题查询
R2R相关Case
>R2RFail：R2RFail原因都是因为匹配获取R2R配置信息时有问题，常见问题及解决方法如下
问题：1.R2RFail：R2R配置信息表中无对应信息/前层作业信息未获取到。
2.R2RFailXX状态：R2R配置信息表中R2R状态为OFF/PIRUNOFF。
解决方法：联系R2R核实对应配置信息或R2R状态。
Mask出厂相关Case
>Mask出厂安全管控：MaskTransferToFab5时会将用到该Mask的LotHold在安全站点，等待Mask回线后Release，常见问题及解决方法如下：
问题：Mask已出厂仍需下放Lot，将LotHoldRelease仍会继续Hold。
解决方法：CallMPC将MaskTransfer签核流程Close，再讲StepHold和LotHold删除且Release即可。
注意：由于报表延迟问题Close后需间隔十分钟左右再将HoldLotRelease。
预排相关Case
>LithoAssign：Litho区域根据光刻机台的Loading，将Lot提前预排到对应的机台上，常见问题及解决方法如下：
问题：DLIMIAO5机台PM前未提前管控，LOt在BAC站点仍然下放。
原因：DLIMIAO5在PM前未将PreControIFlag切至T导致LithoAssign判定结果可作业，且未打开垂直限定导致Qzone不会判断R2R。
解决方法：PM前将PreControlFlag切至T或将PMFlag切至T。
放版相关Case
>放版推送：放版和退版指导是根据自动派工的预派结果，系统会形成放版和退版指导界面，提示用户进行提前操作，以避免因光刻版未及时放入没备导致的自动派工失败。
问题：MaskTH-0888AB-312A在0102使用完成后，一直未被其他lot使用。但BP2R726在当站等待4小时放版指导未推送。
原因：BLIMIA09只剩一块版子可以推送，根据对应lot的紧急程度选择较为紧急的MASK，优先推送TB-0985AA-410A。
商密三级 上海华力
19 HLMC
ConfidentialI

## 第 019 页：ETCH派工规则

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p019.jpg]]

ETCH派工规则
口概述：结合ETCH区域Process机台作业特性，综合考量DomaPath、R2R限制Lot在机台上可作业性的各种因素等，而制定出
相应的解决方案及设定一系列逻辑规则，判断出Lo的可作业性及紧急程度，并根据各个指标对可派工的Lo进行合理的实时调度
功能猫述 Description
LotComment/RTDInfo
Port Bonding ByChamber/FlowRecipe/Capability设定只能/不能在绑定机台的 LoadPort上作业，未设置LoadPort绑定的LoadPort共通 Flowrecipe fail, ChamberNamefail,
Reason MachineCapability fail,
（管控Port作业） 对于当前各chamber的remaintimelotcount和wafercount,若存在
Port Control 对应PPID赋子reasonspecial countcontrol 任意对应chamberremaintimelotcount和wafercount数小于设定值 则待派工lot包含该chamber的PPID可被选择：否则PPID不可被选择派工， special countcontrol
PPID打分 根据chamberloading打分loading低的得分高，得分越高的越优先 PPIDScore
可作业chamber数多的优先 ChamberCount
Reason Chamber派工
(排序规则 chamber剩余作业时间少的优先派该chamber的lot ChamberRemineTime
NoNeedRecipe优先作业 不需要作业recipechange season的lot优先作业 NoNeedRecipeSeason
ReworkedLot优先作业 已经Rework过的Lot优先作业 ReworkLotRQPri
20 上海华力
Confidential I HLMC

## 第 020 页：常见问题查询

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p020.jpg]]

常见问题查询
Recipe连续作业相关Case
>问题：LotBP2Z630QT小于4h触发强派，BEASHM09同Recipe连续作业，但LotBP2Z630仍OQT。
原因：BEASHM09机台的Sorting为QTURGENCY0/1/2/3、RecipeGroupContinue、Rework、RunPri Prefer（MFGControl优先作业）、Q0Prefer等，
由于在LotBP2Z630在还未触发强派之前，有MFGControl设置的2级优先作业，待QTURGENCY3生效时QT已不足顺序作业。
解决方法：将QOPrefer指标调前可解决此问题。
管控Port派工相关Case
>问题：BP2V604/BP2V622/BP2Y101/BP2Y106到达E-ASHHD-F站点未优先派工，直至OQT。
原因：由于BEASHM22/20设定有port管控，针对A，B腔分配的剩余作业枚数低于10Pcs。因该机台多个Qtime较急的Lot为单B腔作业，单B腔Lot上机台后，其余单
腔作业Lot会卡控specialcountcontrol
解决方法：1.修改port管控设置2.将QoPrefer指标调前
SGE相关Case
>问题：BP2R815.0010在E-SIPGE-F一直卡控SGECanNotRelease直至2025/1/1110:36才有排序派上机台来不及作业OQT0.1H。
原因：产品下放后SGE机台的机况及可做业机台条件有问题导致QtimeLoop内产品无法及时消货导致。
解决方法：1.增加Lot可作业Chamber的条件2.设置优先作业
商密三级 上海华
Confidential I 21 HLMC

## 第 021 页：TF派工规则

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p021.jpg]]

TF派工规则
口概述：结合TF区域Process机台作业特性，综合考量Recipe连续、Film连续、连续上限、同条件WIP量、累计膜厚Clean、瓶颈
机台等因素设计一系列派工规则，判断Lot在机台上可作业性及紧急优先程度，并结合ALL-SGE排程等特定调度方式制定出符合
TF区域设备特性的自动派工逻辑。
Reason 功能名称 Chamber/FlowReaipe/Capability只能/不能在绑定机台的LoadPort上作业，未设量LoadPor绑定的LoadPort共通，支持正 功能描述 LotComment/RTD Info
PORT绑定
（管控LOt不自动派工） Film lean 对用户设定的并行模式机台不能司时作业两种不同的膜种 反同设定 ChamberNlame faitPlowrepe fai MachmeCaoability falil
Dif Filen Type
Recipe/Film Continue 未达到recipe/膜种连续上限时，与机台/chamber量近一次作业recipe/膜种是同一recipe/膜种的Lot优先作业 FilmConbinue:NotProcesedtCehars
根据chamberloading打分loading低的得分高，得分越高的越优先 GroupQimeCountRecpeDount FilmGroupLount
CHAMBER Sorting 可作业chamber教多的优先 PPIDScore
chamber剩余作业时间小的优先派该chamber的lot ChambarCaunt
Season Control 不需要作业recipe change season的lot优先作业 ChamberRamineTime
LastFoupFinishTime（Lot在SGE站点最早上货时间Port先ldle的机台优先 NoNeedRenpaSaason
LastFoupFinisnTime
Sorting 判断o的穿插指标 InterfudeFiag
（排序规则） 报据RemQTimeToSGE与QTimeGap?对应ratio判断RemQTimeToSGE的等级 若此lot可作业的chamber包含前一卡的idlechamber则该指标生效 RemQTimeTaSGE Categony ALLProcessChamoerHlag
判断是否为SGE的Pinunlot SGEPinnLot
ALL-SGE 判NPW生效指标 NPWFlag
Lot的Controlid存在ToolRecoveryGroup，且对应PM item strigger为T，则Group中Lot的ControlidSequence判断为 其TRGsequence TRGsequence
MFGControl设重的优先 RunPn Pnefen SGE
少枚数lot不连续 SmallLotNePrefer
Pri为1/2的高等级lot优先 N20CDPn12
商密二岁 Lot的ProcessChamberList中各Chamber打分界计之和，分值趣高越优先 TotalChamberScere 上海华力
22 HLMC
Confidential I

## 第 022 页：ALL SGEAssignment

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p022.jpg]]

ALL SGEAssignment
功能描述
SGELoop存在连环Qtime短、SGE机台产能小、产品Release情况不一致、SGE机台内部限定最多2个Foup可同时作业、来货道次设备类型多样化等诸多问题，因此开发
ALL-SGE预排功能，所有产品按照一套管控逻辑从相对安全站点开始管控放货，结合Qtime/Chamber搭配/穿插作业/SmallLot不连续/SGEPirun/NPW/高等级/优先设定
/SubLot等因素，实现SGE机台混Run，消除OQT的风险，提升机台各腔利用率，减少手动管控操作。
Homc RTD.AL
BP31247 AHAADZAHAATAAIPZLAOTE
AYSGEAO1A
PFESGEA043ZVZ2AC ATSGEAOLA
BTSGEAOISatCRUN ATSGEAOLC ATSSEAOLA
BR31806.0005 SGE机台在作业Lot信息 AISGEAOLLE
SGE机台已预排Lot信
ATSGEAOLLZATSGEAOILAATSGEADHE
BTSGEAO3SORUN ATSGEAOLLZ.ATSGEAOLLALATSGEAOLLC
FSGEAOL2ATSGEAOLUA
LOD
点击任惠预非Lot时，在此处
显示该Lot的详细信感
NoAss/gnResson
Actne BPC1028FD STN Autt AotFait
8T00074.0003 B10074009 BTSGE Acbve Active M295A01-000B M295A01000-B BPCL028FOA-D43L BPCLOZ8FDADA3LIPOMLAOOO1 此处显示所有未预 排Lo的详细倍息 STN AtOJPVtFOE SINAud PtFAle STN Autn PovtFoit
ETNARZ POHEFNC

## 第 023 页：常见问题查询

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p023.jpg]]

常见问题查询
ALL-SGE相关Case
SGECannotRelease：lot在ALL-SGEReport中卡控reason时，rule里会卡此reason，主要原因如下：
1.该lot在SGE站点无可作业腔/机台。
2.对应机台无auto3的port。
3.该lot被hold时间超过2h。
4.卡控断线
>WaitStartTimeToSGE：lot在ALL-SGEReport中已有预排结果但是该lot未到最早放货时间，主要原因如下：
1.当站多为高等级lot，导致normallot排序靠后。
2.该lot可作业机台少且可作业chamber少导致不易于穿插作业。
3.该loop内有大量长qtime的lot，短qtime的lot需等待穿插作业。
4.当站有qtime更加worse的lot，需等待其余lot先行下放，
5.机台发生岩机、PM等情况，导致loop内流通速度变慢，所以lot会在起始站点等待loop内消货再进行下放。
6.Loop内lot预排机台发生变动，计算时间会存在误差。
>SGENeedSeqRun：lot需要等待排序靠前（剩余QT，可作业腔，高等级lot.）的lot按照顺序下放，避免排序混乱。
商密三级 上海华力
ConfidentialI 24 HLMC

## 第 024 页：CMP派工规则

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p024.jpg]]

CMP派工规则
口概述：结合CMP区域Process机台作业特性，综合考量Recipe连续，R2R、PMCycle内同条件连续、TRIM机台LifeTime控货、
CCU机台错开PM等因素设计一系列派工规则，判断Lot在机台上可作业性及紧急优先程度，并结合CCU排程等特定Pirun指导方
式制定出符合CMP区域设备特性的自动派工逻辑。
功能名称 功能描述 LotComment/RTDInfo
PORT绑定功能 Chamber/FlowRecipe/Capability只能/不在级定机台的LoadPort上作业，未设重LoadPort绑定的LoadPor共通，支 ChamberName fail
持正反向设定 Flowrecipe fail
MachineCapability fait
子母批练定 TD要求有绑定关系的子母批需过同一机台作业 Waitfor Child Pilot,
Wrong Bonding Stn
（管控Lot不自动派工） Reason IAPC IAPC逻轻主要判R2R开关、JOB状态、Tool状态，PolishTime和WHITELIST四个方面内容 apctoolrun off apcnainit. apc pilot lat wrang. apc job off apcout of limit
apctodlpirun lotwrong.
Special lotnotnuncthereqp
R2R管控的Lot不照作业 R2RFail:R2R EpireDate
R2R 被设定为其他机台的specialLot不能作业 被设定为其他机台的pirunLot不能作业 Need Pilat Pilot of +CMP PiToal:
R2R会在context后面加expire time超过expiretime不作业 White listaf+WhitelistToal
Recipe Continue 与机台/chamber近一次作业recipe是同一recipe的Lot优先作业同Recipe连续作业 RecipeContinue
PMCycle内同条件连续 在设定cyde内作业过的PRODIDStage+PRODID前4码相同）对应Lot优先作业 IsPnonitizeBySpecialCyeeCentinue
CCU派工采用CMPAssign结果 CMPLotAssignRePort中Lot在机台上的排序等级 CMPAssignPnanty
（排序规则） Sorting CHAMBER Sorting 可作业chamber数多的优先 根据chamberloading打分loading低的得分高，得分越高的越优先 PPIDScore ChamberCount
chamber剩余作业时间少的优先派该chamber的lot ChamberRemineTime
Season Control 不需要作业recipechangeseason的lot优先作业 NoNeedRecipeSeason
Check RuncardLot runcardlot优先 IsRuncardLot
R2R R2R即将失效的Lot优先 IsNearExpine
商密三级 上海华力
Confidential I 25 HLMC

## 第 025 页：WET派工规则

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p025.jpg]]

WET派工规则
口概述：WET分为Chamber/Batch两种类型，因此分为两部分逻辑。WET区域派工逻辑不仅仅对WET本身使用，相对于其他
chamber机台还多了一部分WET-DIFF，WET-SGE产品的派工逻辑。
口MultiChamberWET管控逻辑 口WETBatch管控逻辑
Global功能 PPID选择 WET-DIFF管控 Global功能 PPID选择
Port绑定 PRF-SGE管控 高低温机台切换 Buffer数量 Batch填充率
商密三级 上海华力
Confidential I 28 HLMC

## 第 026 页：02 评论

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p026.jpg]]

编辑V
动画
02 评论
Part/
Global派工规则 000 Qzone Control
Local派工规则 NPW
搬送存储

## 第 027 页：华力AMHS

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p027.jpg]]

编辑
华力AMHS
口AMHS:
AMHS:AutomaticMaterialHandling System中文译作自动物料搬送系统，也称为天车系统，是业界最灵活的
集合储存（stocker），运输（搬送小车）和管控（MCS）制品在FAB设备之间搬运解决方案
主要分为两种形式:interbay半自动和intrabay全自动。
Bay1 Bay 3 Process Bay 5 Intrabaytransport 300 mm UNIFIEO AMHS
tools Bay Bay3 Process Bay5
Stocher Stocknl
OHS
SHO Interbaytransport
Stocte Stocke
OHT
Undar
Bay2 Bay4 storage
Bay6
采用interbay的半自动化AMHS intrabay全自动AMHS系统
实现制品在不同制程区域之间的传送，需 1.实现设备对设备的传送
要stocker与每条bay制程对应 2.具备ZFS(ZeroFootprintStorage)功能
商密三级 上海华力
HLMC
Confidential I

## 第 028 页：Stoker

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p028.jpg]]

Stoker
口Foup储存柜（stocker）整体构造
Stocker型号采用大福CLS-50型，本体构造主要分为四部分：
棚位：shelf，存放FOUP的棚位
堆栈机：机械手臂，抓取FOUP用
搬送口：用于FOUP进出stocker.包括与OHT相连的自动口以及手动出入口
SSS：stocker手动操作面板
自动搬送口
CLS-50仕梯
搬送至量 MAX.10kg
走行速度 MAX.120m/mln
-加减速度· MAX.0.980mls2
聚助方式 Ac Servo Motar
LM-Gulde+FrictionDrive
异降速度 MAX.80m/min
-加减速度 MAX.0.980m/s2
AC ServoMotar
SSS Timing Belit
堆栈机 手动搬送口 BrushType
棚位 STK每小时可实现120个foup自动进出，全自动化运行
商密三级 可确保数据安全及制品安全 上海华力
Confidential I HLMC

## 第 029 页：口OHB

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p029.jpg]]

OHB
口OHB
OHB:安装于小车轨道外侧用于临时存储FOUP
由于是悬空设计，增加FAB空间利用率
悬挂机台上方轨道，在小车搬送路径上可大大缩短距离，增加搬送效率
结构简单，无光电以及马达装置，故障率低
单个成本远低于stocker单个棚位
FAB6OHB
结构更为简单，可靠，可通
过改造增加purge功能，满
足制程中FOUPpurge需求
商密三级 上海华
Confidential I HLMC

## 第 030 页：六厂搬送状态

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p030.jpg]]

六厂搬送状态
动画
搬送概况 OHB&STK可储存量 评诊
>日均搬送量：123358次 Type Normal Purge Total Purge Ratio
平均搬送时间：2:17 OHB 4559 2326 6865 51%
>实际运行天车数：280台 Stocker 5647 1858 7505 33%
Total 10206 4184 14390 41%
口 PurgeOHB&STK分布
A06- -A09
BSTKP201 BSTKP202 BSTKP203BSTKP204
BSTKP104 BSTKP106 OHB:BAYA06-A09A16
BAYC11-C15C20
STK:STKP201-204.STKP104STKP106
商密 C11-C15 上海华力
42 HLMC
ConfidentialI

## 第 031 页：搬送存储作用 编辑Y式

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p031.jpg]]

搬送存储作用 编辑Y式
搬送存储主要用于缩短搬送路径，减少搬送系统负荷：加快向设备供货充分利用生产设备：调整存储类型，增
加产品品质保障。
搬送负荷 作业工艺流程 设备分布
小车分布
设备能力 存储位置 设备负荷
产能利用
设备port作业模式
port与chamber对应作业 PreSend功能
产品品质 一作业时间越快对搬送要求越高 设备作业时间 设备作业 信息 估算作业 结束时间
载具类型 工艺要求
Purge
XCDAOHB&STK 存储
商密三级 分布 存储状态
上海华力
Confidential I HLMC

## 第 032 页：搬送系统运行方式（AMA&RTD） G编辑

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p032.jpg]]

搬送系统运行方式（AMA&RTD） G编辑
RTD（自动派工系统）在搬送流程中的作用和考量因素：
当站设备 ·Lot在当站设备上作业完毕，FOUP待搬走
DSP系统 ·根据工艺需求、设备位置、OHB/Stocker空闲情况，决定Lot/FOUP存储位置
·通过MES发送搬送指令CallMCS（物料搬送系统）执行搬送动作
RTD决定存储位置的优先顺序
需要PurgeFOUP 正常FOUP
Purge OHB Purge STK OHB STK
当站设备默认位置[-n，+n]范围
下站设备默认位置[-n，+n]范围
当站设备默认位置同区域范围
下站设备默认位置同区域范围
其他任意
当OHB/Stocker存放率高于上限，则找寻下一优先级的OHB/Stocker
Purge存储位供正常Lot使用的可利用率相对低
·设备即将空闲时，AMA向RTD要货，RTD根据优先级、设备特性、存储情况
商密三级 下站设备 ·设备LoadPor空闲时，向RTD要货，RTD根据优先级、设备特性、存储情 等因素选择Lot，AMA将Lot预搬送至机台OHB 上海华力
况等因素，选择Lot对设备预约 HLMC
Confidential I

## 第 033 页：预搬送功能

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p033.jpg]]

预搬送功能
背景
对于堆货机台，产能紧张，搬送时间过长可能造成机台空机等待IDLE，导致产能LOSs，为使Lot能尽快上机台作业，对于LP
都已满机台，提前搬送Lot至机台OHB，减少搬送时间。
方法
预搬送 当设备上剩余作业量小于水位时，AMA根据RTD给出的派工清单，将顺位1的Lot添加入MES的
queue reservation list
MES发送搬送指令给MCS将Lot搬送至该设备的DefaultOHB。
Normal机台：机台名+LotCountWaterMark）
Chamber类机台：机台名+Port名+WaferCount（WaterMark），考虑port上在作业产品所用腔的剩余wafer数总和
例：CaseforMultiChamber (WaterMark:2pcs)
2pcs 20pcs P1上剩余wafer符合设定水位，但不融发
P3 P2 Lot. PPID Port 当P2剩余wafer数符合水位时，Lot1会 presend,
Lot1 AB Pre-Send到P2，随后MES会将该FOUP传
Lot3 AB P1 到EQPDefaultOHB
EQP
派工 设备LoadPort空闲时，RTD优先排货queuereservationlist中的Lot
商密三不适用场景：1.机台状态：非Auto2/3，非可作业状态
Confidern 2多个FOUP同时派工场景（如season+prod，sorter派工，batch设备派工等） 上海华力
HLMC

## 第 034 页：02 评论

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p034.jpg]]

编辅
动画
02 评论
Part/
Global派工规则 000 QzoneControl
Local派工规则 NPW
搬送存储

## 第 035 页：QZone管控简介

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p035.jpg]]

QZone管控简介
口相关术语
Qtimeduration
生产过程中在规定时间（QueueTime） step1
内完成特殊工艺区间段的作业过程。
>QZone EndRun step2 Tips:
在Q-time区间外对区间内WIP限额 step3 Otime从startstep EndRun deteoStartRur
保证区间内设备有足够WIP但不超时。 StartRUN Qtime结束站点不一 定为lo的安全装点
step4 safetyvalue翔断
EndRun
>Qzone方式 lotOverQtime时由currentPE设定action忘是hoid
QTime lot以及是否需要rewark/scan/WAT等
Minqtime：某站点作业结束后，可 step5
以继续下一站作业的最小等待时间 StartRun
step5
Maxqtime：规定时间内完成某段工
艺的最大允许时间
商密二级 上海华力
Confidential I HLMC

## 第 036 页：QZone管控简介

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p036.jpg]]

QZone管控简介
口管控内容
QZonecontrol Qtime urgency
·要求
-ot放入loop内后不会overqtime 要求
-lot在放入loop内后不会造成其他 Loop外产 品作业管控 Loop内产 品作业管控 每个lot在gtime范围内作业出loop
lotoverqtime -lot的作业不影响出货/瓶颈所需lot的作业
口考量因素
设备数量 QT时限 QT结束方式
瓶颈站点
设备状态 QT类型 Loop内WIP量
设备作业能力
设备维护计划
设备作业方式
工艺限定 Loop内WIPremainQT
商密三级 上海华力
Confidential I 48 HLMC

## 第 037 页：QZone管控简介

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p037.jpg]]

QZone管控简介
口管控类型
Branch
Main
BBBE Branch
Main
口管控难点
因素维度多，精准管控难度大 新型管控需求多，覆盖面更广
·下游机台作业时间大于qtimeduration;
·Zone中存在多道相同制程 .Wafer level qzone
·交叉qzone，考虑duration不同和连环qzone交又 ·QZone跨度大、小于4h的短Loop数量多
·Run card作业，工艺不确定性
商密三级 ·考虑zone中各站点机台的可作业情况，如机台状态 ·特殊loop:如CT-NIC、PRF-SGELoop管控 上海华力
Confidential I constraint,PMrecovertime等 49 HLMC

## 第 038 页：QZone管控简介

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p038.jpg]]

QZone管控简介
口模型架构
获取各制程信息 获取机台List
阶段 方法
机况和作业能力 判断机台与制程关系 判断机台可作业状态
数据准备 的状态、作业条件、限定信息和产能情况。 获取各制程的作业时间Process Time，各机台 获取各制程的作业时间 限定信息作业鉴件产能
IDLERUN RECYCLE BACOUP ENG LOT
MON ROU MONR BKUPTDLOE
Flow信息 Qtime信息 联取Flow信惠
获取Normal/Branch 获取Qtime信息： Norma Flow BranchFlaw
信息整合 Flow信息，根据作业顺起始/结束站点
序编码。 qtimetype. qtimelimit. 取Qtime 依据Step 获取开始站点和 获取Qtime
行顺序编码 结束站点信息 顺序编码 信惠
逻辑判断 依待定规，并按
照stepsequence进行
模型计算 根据各Lot真实QtimeflowInfo信息，按照 顺字编码
定逻辑，判断处于Qtime起始站点的Lot 将Normal Step和Branch Step进行电联按照编码
能否派工。 规则进行排序，得出Lot的真实Flow信息及滚Flow的
Qtime信息
商密三级 上海华力
Confidential I 50
HLMC

## 第 039 页：QZone管控简介

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p039.jpg]]

QZone管控简介
口管控逻辑
Constraint Qzone Exception
Result
Constraint Ozone Result Exception
主要作用 判断每个prod在每个站点机台的 判断qzone中每个站点每个机台的产能情况 忽略草些设定站点的QZone管控结
recipe可作业情况
判断内容 机台是否建Recipe 1机台产能：capability开关，EQPstate 1.白名单：制造科/PE要求设定无
2. Recipe是否被inhibit/Hold/ Communicate mode,WPH 视站点
disable 2机台需求量：QZone中的每个lot分配在该机 2.Safetyvalue判断
台上的wafer数总和
运算频率 16mn Normal12min先进工艺11min 实时
运算时间 约16min 12min 实时
与实际差 最大约18min 最大约14min
结果特别处理 Lot处于aZone起始站点，HQZone结果未计算
商密三级 出来时，该Lot不派工 海华力
Confidential I HLMC

## 第 040 页：QZone管控简介

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p040.jpg]]

QZone管控简介
口整体判断逻辑
根据不同设备群前面的Lot流通状态来估算各Lot在各种设备群的最大允许等待时间。结合各Lot余裕等待时间
和剩余加工步骤中需经过机台群的产能，管控q-zone起始站点放货情况并能根据卡Qzone的情况进行特殊处理。
获取Qzone信息 计算各Lot到每个
下游设备信息、 作业条件 step的最大允许 等待时间 平衡各个机台 loading 判断放货情况 异常特殊处理
PPID Recipe Constraint EQP/CHMBstatus 一多次分配 Queue sort 一待派TLot Wafer Balance Loop内lot 多次分配 待派工Lot 衡量overqtime可能性 待派工Lot不超qtime 待派工Lot放入loop后 不影响其他Lot作业 一堆货 一断线 下游卡Qzone
作业机台/ 依次计算目标机台产能 AIBiabReStanUSIDLEALINREOYCLE BAEKUENGLOTMONROULMON
排序 和在相应Lot的queue 管控放货 8KLRTDLOTE
下precontoifagy时ar台下可
sort范围内的作业零求
商密三级 上海华力
Confidential I 52
HLMC

## 第 041 页：QZone管控简介 口编车

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p041.jpg]]

QZone管控简介 口编车
口QZoneControl应用实例（判断处于Q-timeloop起始站点的Lot能否派工）
①获取各qzoneloop内所有要经过targetstep67对应capability的Lot，并计算每个lot的qsort值，从小至大排序；
o-tmelo0e3
Lotname qy queuesor Lotname Qty queuesor Lmeloop
Lot1 20 10 排序 Lot3 20 Target stepe7
Lot2 20 12 Lot4 20
Lot3 20 Lot5 20
Lot4 20 Lot1 20 10
Lot5 20 Lot2 20
②拿取targetcapability可作业机台/chamber及WPH，根据qsort依次计算 ③判断qzone起始站点的Lotv放入zone后是否会影响已在zone中的Lot：
target_capability各机台在相应lot的qsort范围内的作业需求和产能， Lotv进入zone后不会超qtime
WPH-15 正常lot：不会超qtime
已经超qtime的Lot：超过时间不变
Lotnam qty queuesor 作业需求 机台产能
queuesort 作业需求 机台产能 剩余产能 可放货结果
Lot3 20 20 30 10 20 30 10
Lot4 20 40 45 2（lotv) 40 30 -10 不可放货
Lot5 20 60 60 60 45 -15
Lot1 20 10 80 150 80 60 -20
Lot2 20 12 100 180 80 10 100 150 50
120 180 60

## 第 042 页：其他QZone相关附加管控功能

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p042.jpg]]

其他QZone相关附加管控功能
Loop Lot Control
特殊qzoneloop需要特殊管控方式，如CT/SAPloop需要byFOUP管控数量或部分IMPloop只管控结束站点WIP等，原qzone模型不适用。
QT2 OTA
C3 C1
Qzone管控形式：
ByBegin：管控起始站点同时在作业产品数量
ByLoop：管控起始站点（在作业WIP）至结束站点（所有WIP）总产品数量
√ByEnd：管控结束站点（所有WIP）总产品数量
WIP统计形式： LOT COUNT/WAFER COUNT/FOUP COUNT
产能计算方式：固定（与机台状态无关）／动态（随机台状态变化）
商密三级 上海华力
Confidential I HLMC

## 第 043 页：其他QZone相关附加管控功能

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p043.jpg]]

其他QZone相关附加管控功能
口Loop内lotqtime管控
1.Lot相互独立（QtimeUrgency）
Lot5在S4站点的gtime派工等级？
Lot2
Lot3
Lot4 Lot5 Lot6
$2 $3 $4 $5
QT
计算QT紧急程度：用Lot当前位置至结束站点的剩余qtime时间与估算剩余作业时间的比值作为QT紧急程度指标
QU= QTUrgency Level Description
QTUrgency0
QT Urgency_1 (0.3,1)
针对QT_Urgency_O的计算 ①.当QT_Urgency=RemainQT/RemainCycleTime≤0.3时生效 QT.Urgency.2 (1,2)
②.当RemainQT/RemainProcessTime≤1时，QU0生效 QTUrgency_3 (2.3)
（防止因CT维护值不准确，计算出的QU值偏差较大） QT Urgency_4 (3.4)
商密三级 上海华力
56 HLMC
Confidential I

## 第 044 页：其他QZone相关附加管控功能 4编辅辑

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p044.jpg]]

其他QZone相关附加管控功能 4编辅辑
2.Lot相互间影响（QO Prefer）
Lot2在S2站点的qtime派工等级？
Lot2
Lot3
Lot4
Lot5 Lot6
$2 S4 S6
估算Lotoverqtime可能性：当某Lot在容许时间范围内不允许插入一卡Lot时，将降低所有紧急程度比该Lot小的lot派工优先等级。
[RemainQTime-RemainCycleTime-Z （ProcessTime/Avail ToolCount)-GroupRemainTime]sRatio*ProcessTime
例：若所有lo在S2站点只有一个可作业机台，且STN剩余作业时间为1H
lotid Rqt-Rct PT PTEactSTN GroupRemainTime 排序 Lotid QoPreferfFlag QoPrefer等级
Lot1 27 0.5 0.5 Lot1 1001
Lot2 Lot2 1002
Lot3 3.7 Lot3 2000
Lot4 5.8 2000
商密三级 Lot5 Lot5 3000 上海华力
Confidential I 57 HLMC

## 第 045 页：Qzone异常处置机制

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p045.jpg]]

Qzone异常处置机制
断线：在Q-Time下游某个站点所有可作业机台无作业条件（Constraint/RecipeInhibit/机台不可作业/未维护WPH/Capability未打开）。
堆货：在QZoneLoop中WiP量达到了QZone算法计算的wiPLimit，qzone起始站点无法向下游放货，造成卡QZoneCapacity。
“一刀切”
卡Q-zone
QT2 Q-Zoneexception 强派
Step1 Step2 Step3 且QT2(QT3)>4H QT1=4H 强派
Tool down/堆货
是否向下游放货？ R QT,小于设定值 强派
N个
QT: QT2 QT3 Special target Lot 强派
Step1 Step2 Step3 step4
STEP1为LITHO 不强派
Tool down/堆货
是否向下游放货？ QT2/3=4H 不强派
WN
指定站点 不强派
强派 RQT1>-2H 不强派

## 第 046 页：Qzone异常处置机制

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p046.jpg]]

Qzone异常处置机制
"Safety Value"
连环qzone下游出现断线或堆货时，根据各qzone的风险程度进行特殊管控。
卡Q-zone
QT1 QT2 Q-Zone exception 强派 >Issuestep存在Exception站点：
白名单 Ozone不卡控孩lssuestep，非exception
Step1 Step2 Step3 Y>设 Y,且<设定 step依次判断
指定RQT放货 强派 指定remainqtime放货：
Tooldown/堆货 RQt<设定值：强派（忽略所有断线/堆货站
是否向下游放货？ 黑白名单
Special target Loti设定不管控 强派 RQ>=设定值不底（卡控所有断线/堆货站
QT1 QT2 QT3 >MPc设定Target：仅针对堆货
黑名单 不派 限定不可放货站点 TargetLot.强派（略所有堆货站点）
Step1 Step2 Step3 Step4 Issuestep存在限定不可放货站点：
Safety Lot不派（卡控新有lssueStep）
Tool down/堆货 Value 风险管控放货 强派
是否向下游放货？ 管控
不派

## 第 047 页：Qzone异常处置机制

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p047.jpg]]

Qzone异常处置机制
口SafetyValue定义标准
SafetyValue QT类别 QT优先级 建议处置方式 定义标准 管控级
长期停靠 无Q-time管控 Long term bank
短期停靠<=15D（待定）无Q-time管控 可短期停靠
停靠时间<=7D（待定）无Q-time管控 Q-timewindow未知，不建议长期 停靠 无风险
保留字段 无Q-time管控
保留字段 无Q-time管控
RWK-Single单一Qtime 最低 Wait RWK 异常loop：直接进入；
RWK-Multi连环Qtime 较低 Coating PR & Followed by RWK 当前loop：禁止向下放货 低风险
1.5*qtimespec;
Non-RWK-3 少量超出Q-time影响较轻微 异常loop：条件进入； 中风险
当前loop：条件向下放货
1*qtimespec;
Non-RWK-2 次之 中间层级，不要Over 异常loop：不能进入； 高风险
当前loop：条件向下放货
Non-RWK-1 最高 严格FollowQ-time，不能Over 当前loop：直接向下放货 异常loop：不能进入； 必死货
商密三级 上海华
Confidential I HLMC

## 第 048 页：Qzone异常处置机制

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p048.jpg]]

Qzone异常处置机制
Qzoneloopsafetyvalue取值
safety value取值
起始qzone safetyvalue:该lot当前step的safetyvalue
V,=CurrentStep(safety value) Vs
Te
Tooldown/地贷
中间qzone safetyvalue:所有qzone的最大safetyvalue
Vm=max(min(safetyvalue;)hj 其中： Vm
ie中间层qzone中的个step
jE中间层每个qzone Tooldoan/mn
异常qzone safetyvalue:该step 所在qzone中的最小safetyvalue
Ve=min(min(safetyvalue)) 其中： Ve
iEstep所在qzone,中的每个step
商密三级 jEstep所在的每个qzone Tooldown堆
Confidential I

## 第 049 页：Qzone异常处置机制

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p049.jpg]]

Qzone异常处置机制
口SafetyValue风险等级管控逻辑
Ym 以离Lot Current
Step量近的
IssueStep进行判断
Step1 zdaxs Step3
是否向下游放货？ Tooldown/堆货
是否可RW 条件 结论 情况
Vs=0且Vme可rework Any situation
存在可rework Vs+0且Vm/Ve可rework
loop Qzone Any situation
Vs可rework.Vm/Ne不可rework 不放 Any situation
VsVe月 Vs0 条件放贷
Vs= Ve E Vs =0 立即放贷
其中、条件放货：
不存在可rework RQT<=n%*QTimeLimit
loop qzone VsVe 且Ve≤0/1 件放货 m值的设定情况：
0.2)50,
Vm>=VsVe且 (2.4)30
Ve=0/1 (4,6)25,
VmVsVe月 Ve=0/1 不放 (8,)10 (6,8)20,

## 第 050 页：NPW自动化结构图

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p050.jpg]]

NPW自动化结构图
动通
口功能结构：涵盖所有NPW类型，并根据NPW使用流程，划分成四大功能模块
功能模块：备片（AutolnUseStart）、派工（Dispatch）recycle（AutolnUseEnd）以及downgrade（AutoRecycleEnd）
Monitor Routine PM DOWN
NPW类型 Season Idle Recipechange Recipe idle Wafercount PM/Down
Dummy eOutside Inside
Lot Start 下片
wafer下线
Check Condition 已实现auto
PreClean 自动派工 派工条件 派工等级 派工模式
InUseStart 自动备片 准备时间 准备方式 准备数量 正在开展auto
手动操作
自动派工 派工条件 派工等级 派工模式
InUseEndge 自动发recycle Reuse Recycle Downgrade 提前recycle
Clean CheckCondition 自动派工 派工条件 派工等级 派工模式
Recycle End Reassignorreclaim Downgrade 自动 Reuse Reclaim Downgrade 提前Downgrade

## 第 051 页：In Use Start--Routine monitor

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p051.jpg]]

In Use Start--Routine monitor
口 Routine monitor分批逻辑介绍
主要流程
准备Monitor 测量前值 主机台 测量后值
口逻辑介绍
> By time分批:split time =date(last monitor time)+ interval + time(initial time)-leading time
lastMonitortime Split time Schedule Monitor Time
Interval Time
Leaaing Time For Preparing
Pre-Mea SCH-CTAOC-POSTMA
Process Tool SCH-CTOSTMEA
Post-Mea
口相关参数说明
Interval：monitor频度
RemainCT：剩余各站点cycletime累加 >Monitorurgencylevel划份：
Remaindue:monitor剩余失效时间（Remaindue=lastmonitor time+interval-now) Monitorurgency=0.7时，为level0;
Monitor urgency-remain due/remain CT Monitorurgency<=1时，为level1;
商密三级 Leadingtime需要多久提前准备monitor 1<monitorurgency≤=1.5时.为level2;
Monitorurgency>1.5时.为level3.
Confidential I

## 第 052 页：In Use Start--Routine monitor

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p052.jpg]]

In Use Start--Routine monitor
Bytimeweekly分批：split time =date(now)+ time(initial time)-leading time
Monday Monday Monday
Time
Splittime
1.当前日期为指定日期时：
now>=date（now）+initialtime-leadingtime，则该monitor需要分批，否则不分批：
2.当前日期不是指定日期时：
计算当前时间所在的week，以及当前week指定的controlvalue所在的date1，以及date2（date1-7*control
interval），拿取date1&date2中小于当前日期中最大的date，作为lastsplittime。
datelastmonitortime）lastsplittime，则该monitor需要分批，否则不分批
商密三级 上海华力
Confidential I HLMC

## 第 053 页：In Use Start--Routine monitor

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p053.jpg]]

In Use Start--Routine monitor
Monitor In Use Start
口 流程图
Watch dogscan every5min
Check monitor Monitor触发判断
Get control id list
Get monitor lot list
Exist monitor End
lot?
Getmonitor source lot
Monitor准备
Send alarm Exist monitor source lot? 2.Monitor分批 1.母批筛选
In use start with split
Split success
商密三级 上海华力
Confidential I Get monitor lot list HLMC

## 第 054 页：In UseStart--Routinemonitor 问题查询

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p054.jpg]]

In UseStart--Routinemonitor 问题查询
是否到分批时间
查询上一次分批时间，推算是否到分批时间
是否有延期
配置是否正确
U配置信息
2. 底层信息是否正确：Mesprod.fabmonitoridenable=T，cansupportstandalone=T
3. 是否有指定SoucelotidMesprod.fabmonitorid.Soucelotid
机台当时状态
机台为可作业状态
Controlid当时状态
1是否有已分批的Lot
2.Controlid未正确结束，做账问题 版本号问题
ReasonValidation operationfailed 或 is not same等
AMAlog 通过NPWEPRFLOWReport文件拿取该Step的最新PLAN&Subplan版本（该
1234 是否有可用Wafer（Lotowner） 文件由于数据量过大舍弃了RecycleEnd等站点，文件中没有的可通过表
存在MonitorGroup内其他项目无法分批 mesprod.fwprocessplan拿取，name包含PLAN&Subplan，activeversion
版本号问题 为当前最新版本）
物理分批考虑是否有空Foup.等等 与Lot当前PLAN&Subplan版本对比，不同则可确定为版本问题
商密三级 上海华力
Confidential I HLMC

## 第 055 页：In Use Start 一加做&延期monitor

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p055.jpg]]

In Use Start 一加做&延期monitor
口加做&延期monitor逻辑介绍
>加做monitor:split time=applytime
系统申请 管理签核 自动备片 自动派工
Add Approve AUTO split dispateh AUTO
PE/EE
延期monitor:split time =last split time +postpone
Last Split time Schedule Monitor Split time Time
last Monitor time
Interval Time Postpone
Leading Time ForPreparing
Pre-Mea SCH-CTIFAOCFSS-FCSTMEA
Process Tool SCH-CTHOSTMEE
Post-Mea 上海华
商密三级 HLMC
Confidential I

## 第 056 页：In UseStart-复机NPW 编辑

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p056.jpg]]

In UseStart-复机NPW 编辑
TRC流程：
PM流程 Action Owner
前期准备 PE维护recoverygroup
前期准备 PE
WAITEE->PM EEtrigger PM item EE
PM 自动分批（auto） PMNPW自动备片
DSP
PM->WAIT PE
WAIT PE->WAITMFG 自动派工（auto） PE勾选is triggerPM season PE
MON PM alam 触发TRC.PMNPW自动派工 DSP
WAIT EE->DOWN PE trigger DOWN item PE
DOWN DOWN NPW自动备片 DSP
DOWN->WAITPE 异常处理
WAIT PE->WAIT MFG PE勾选istriggerPMseason PE
WAIT PE->WAIT MFG MON DOWN 触发TRC.DOWNNPW自动派工 DSP
WAIT MFG-IDLE 派工pilot DSP
商密三级 RUN Auto pi_run 上海华力
Confidential I HLMC

## 第 057 页：In Use Start 一复机NPW

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p057.jpg]]

In Use Start 一复机NPW
口复机NPW分批逻辑介绍：
>Season分批：splittime=机台切到WAIT MFG时间点
WAIT EE triggerPM/DOWN item WAIT MFG WAIT PE Time
PM&DOWN MONPM&MONDOWN
Split time
注：对于需要多卡season的设备类型，可设置按剩余片数分批。
Monitor分批：
WAIT EE triggerPM/DOWNitem ENG time WAIT PE Time
Leading time MONPM&MONDOWN
PM&DOWN
Split time Split time
注：Splittime计算：
1)存在ENG Time时:split time=ENG Time-leading time
2）不存在ENGTime，STD time不为空时：split time-PM时间点+STD time-leading time
商密三级3）不存在ENGTime，STDtime为空时：splittime=PM时间点
Confidential I 上海华力
HLMC

## 第 058 页：In UseStart 一复机NPW自动分批

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p058.jpg]]

In UseStart 一复机NPW自动分批
TRC分批逻辑：
Season分批条件：
机台存在trigger的PMitem：
2. 机台trigger的PMitem已打开autotool recovery功能；
3. 机台处于WAITMFG或MONPM/MONDOWN状态：
4. 对应control存在可用sourcelot；
注：对于需要多卡season的设备类型，可设置按剩余片数分批
Monitor分批条件：
机台存在trigger的PM item；
2. 机台trigger的PMitem已打开autotool recovery功能
3. 机台处于PM/DOWN或MONPM/MONDOWN状态：
4. 对应control存在可用sourcelot：
5.当前时间大于splittime;
Splittime计算：
1)存在ENG Time时： split time=ENG Time-leading time
2）不存在ENG Time,STD time不为空时：splittime=PM时间点+STD time-leading time
3）不存在ENGTime，STDtime为空时：splittime=PM时间点

## 第 059 页：In Use Start 一复机NPW自动派工

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p059.jpg]]

In Use Start 一复机NPW自动派工
>前/后量派工：
复机NPW优先：对于复机的NPW，派工时，RecoveryNPWFlag生效 Monitor group info:
其他sorting指标相同时，会优先派工（新增功能区分复机优先级）：
相关sorting:RecoveryNPWFlag及RecoveryNPWFlag1/2/3/4 1.SeasonA(PT:60min)
前量时效性考量：会考虑复机monitor是否存在时效性，对于存在时效性 2.MonitorB
的monitor，会根据机台的复机时间以及该monitor前面需要作业NPW的
作业时长，卡控lot派工时间点，避免monitor超时效影响复机； 3.MonitorC
相关RTDreason:Monitorqtimecontrol
4.MonitorD
后量时效性考量：会根据自身时效性（remainqtime）以及后量机台的
processtime的比值来判定派工的紧急程度，比值越小越优先。
MonitorBflow:
PM
前量
60min
8:00 12:00 13:00 14:00 主机台
Reason卡控 可派工时间段 60min
商密三级 后量
上海华力
ConfidentialI HLMC

## 第 060 页：In Use Start 一复机NPW自动派工

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p060.jpg]]

口编辑
In Use Start 一复机NPW自动派工
主机台派工：
考虑机台复机monitor的作业顺序要求： Monitorgroup info:
相关RTDreason:Need sequencerun
例：当seasonA派工后，下次派工只可以派monitorB，monitorCD 1.SeasonA
卡控不可派，reason为need sequencerun； 60min
考虑机台复机monitor相互之间的时间要求： 2MonitorB
60min
相关RTD reason:Interval time out 3.MonitorC
例：在seasonA作业完成60min后，若monitorB派工，则卡控reason 60min
为interval time out; 4.MonitorD
考虑机台非复机lot派工：
相关RTDreason:Need recovery
例：若机台处于MONPM/DOWN状态，后续待派工为非复机monitor
中的lot，其卡控reason为needrecovery：
同机台复机chamber和正常chamber之间lot排序
对于复机的NPW，派工时，RecoveryNPWFlag生效，其他sorting指标
相同时，会优先派工，相关sorting：RecoveryNPWFlag
商密三级 上海华力
Confidential I HLMC

## 第 061 页：In Use Start- 一复机NPW自动派工

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p061.jpg]]

In Use Start- 一复机NPW自动派工
TRC分批逻辑：
考虑RemonMonitor指定Lot分批（已上线）
对于SpecialDownGroup，可以添加RemonMonitor，指定不能选用的
sourceLot，再进行分批
主机台派工：
考虑机台需求多Monitor一起派工（已上线）：
同Group内可设定多个Controlid为同一Seq，同一SegMonitor会优先分
至同一FOUP，同FOUP派工时一起派工
同FOUP内RoutineMonitor派工：
考虑同FOUP内存在RoutineMonitor需求派工（已上线）
计算同FOUP内RoutineMonitor需求作业时间（包含机台剩余作业时间）
与FOUP内TRCMonitor同Group且小于当前Seq的Controlid作业时间进行
对比，若小于，即RoutineMonitor作业完成，TRCMonitor还未能开始作业
即可派工该RoutineMonitor
商密三级 上海华力
Confidential I HLMC

## 第 062 页：In UseStart -Season

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p062.jpg]]

In UseStart -Season
Season InUse Start
主要流程 机台派工
Season 翔断 Season准备 主机台
口 Season触发条件
机台触发派工
机台idle时间达到设定值
机台本次作业产品的条件与上次作业产品条件发生改变
机台作业前有换酸等
口 Season类型
Idleseason：机台或者chamberidle达到一定时间后需作业的season
Recipechange season：机台本次作业产品条件与上一次作业产品条件发生改变时需作业的season
Recipeidleseason：机台某一条件在一段时间内未作业过产品时需作业的season
Chemical season：机台换酸后需作业的season
PM&DOWNseason：机台down机或者PM后需作业的season
商密三级
Confidential I 上海华
HLMC

## 第 063 页：In Use Start-Season

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p063.jpg]]

In Use Start-Season
Season InUse Start
口AMA流程图
Watch dog
Check season Season触发判断
Get control id list
Get season lot list
Exist season
lot? Dispatch End
Get season source lot
Season准备：
Send alarm Exist season 1.母批筛选
source lot? 2.Season分批
In use start with logical split
Split success
商密三级
Confidential I Get season lot list Select target season lot 上海华力
HLMC

## 第 064 页：In Use Start--Season

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p064.jpg]]

In Use Start--Season
口母批筛选
Filterrule
Filter item
Lot ProcessingStatus=Active Description
Lot Extrastatus =WaitForlnUseStart Lot状态是active
WaferUsedCount<MaxUsedCount Lot必须是WaitForinUseStart或者WaitForlnUseEnd
Waferstatus=Normal Wafer使用次数小于最大使用次数
Wafermonitorstatus =Available Wafer状态是normal
Carrier_CarrierKind=FOUP Wafermonitorstatus必须为active
Carrier ProcessingStatus =Created Sourcelot必须在carmer
Sourcelot所在的carrier必须是created
Carrier State-Enable Sourcelot所在的carrier必须是enable
FOUPLocation=In StockerorInOHB Sourcelot所在的carrier必须是lnStocker或nOHB
Filterthe lot which available wafer count<control id wafer count Sourcelot中可用wafer数不能小于controlid所需的wafer数
Sorting rule
Sorting item Description
Lotowner=MFG lotowner=MFG的lot优先
Minavailablewafers inFOUP 可使用wafer数少的lot优先
Maxrecycle count byFOUP recycle次数多的lot优先
商密Max waiting time Max used count of FOUP 已使用次数少的lot优先
Confic Min used count ofwafer 等待时间长的lot优先
LotSlot位置小的优先

## 第 065 页：In Use Start- -Dummy

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p065.jpg]]

In Use Start- -Dummy
DummyInUseStart
主要流程 机台派工或watchdog Dummy翔断 Dummy准备 Reserve dummy
口Dummy触发条件
机台内任一dummy达到最大使用次数或当前将派工机台内dummy不足
当前无已分批的dummy
口Dummy类型
SD Dummy
FurnaceDummy
ED Dummy
Dummy
In side Dummy
ETCH Dummy
Out side Dummy
商密三级 上海华力
Confidential I HLMC

## 第 066 页：In Use Start--ETCHDummy

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p066.jpg]]

In Use Start--ETCHDummy
Dummy In Use StartETCH Dummy
口 AMA流程图
Watch dog scan every5min
Get eqp list of need dummy Dummy触发判断
End Eqp list is not
nul?
Get need to split dummy ID list
Dummy list is
not nul?
Get dummy source lot Dummy准备：
1.母批筛选
2.Season分批
Send alarm Exist dummy
source lot?
Split success
商密三级 上海华力
Confidential I End HLMC

## 第 067 页：In Use Start--ETCHDummy

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p067.jpg]]

In Use Start--ETCHDummy
口角 触发条件
lot extract status is Wait ForDummy Out
exist any one wafer used count>-itself slot max spec
no other any lot extract status is Wait For Reserve Dummy
母批筛选
Filter rule
Filter item Description
Lot_ProcessingStatus =Active Lot状态是active
Lot Extrastatus =WaitForinUseStant Lot必须是WaitForinUsestart者WaitForlnUseEnd
Wafer status - Nomal Wafer状态是nomal
Wafermonitorstatus=Available Wafermonitorstatus必须为active
Carnier CarnerKind-FOUP Sourcelot必须在camer
Camier_ProcessingStatus-Created Sourcelot所在的carmier必须是created
Carrier_State-Enable Sourcelot所在的camer必须是enable
FOUPLocation=ln StockerorInOHB Sourcelot所在的camier必须是InStocker或lnOHB
source lot available qty =dummyld need wafer count 可用wafer教大于等于dummyid所需wafer数
Sorting rule
Sorting item Description
Lotowner=MFG lotowner=MFG的lot优先
Minavailable wafers inFOUP 可使用wafer数少的lot优先
Max recycle count byFOUP recycle次数多的lot优先
Max used count of FOUP 已使用次数少的lot优先
商密 Max waiting time 等待时间长的lot优先
Conf Min used count of wafer LotSlot位置小的优先

## 第 068 页：In Use Start--FurnaceDummy

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p068.jpg]]

In Use Start--FurnaceDummy
DummyIn Use Start-Furnace Dummy
口AMA流程图
Watch dog scan every 5 min or What
Next trigger start
Get ep list of need dummy Dummy触发判断
End Eqp list is not null?
Get need to split dummy ID list
Dummy listis not
null?
Get dummy source lot Dummy准备：
1.母批筛选
2.Season分批
Send alarm Exist dummy
source lot?
Split success
商密三级
Confidential I Pass end 上海华力
HLMC

## 第 069 页：In Use Start--Dummy

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p069.jpg]]

In Use Start--Dummy
触发条件
(lot extract status is Wait For Dummy Out and exist any one waferused count -itself slot max spec)
or (Batch wafer count +monitorwafer count +SD dummy wafer count +ED dummy wafer count <spec)
no otheranylot extract status is WaitFor ReserveDummy
口母批筛选
Filter rule
Filter item
Description
Lot ProcessingStatus=Active Lot状态是active
Lot Extrastatus=WaitForlnUseStart Lot必须是WaitForinUseStart或者WaitForlnUseEnd
Wafer status =Normal Wafer状态是normal
Wafermonitorstatus=Available Wafermonitorstatus必须为active
Carrier CamierKind=FOUP Source lot必须在carrier
Carrier ProcessingStatus =Created Sourcelot所在的carier必须是created
Carrier State=Enable Sourcelot所在的carier必须是enable
FOUPLocation=InStockerorInOHB Sourcelot所在的carrier必须是InStocker或lnOHB
sourcelotavailable qty>=dummyldneedwafercount 可用wafer数大于等于dummyid所需wafer数
>Sorting rule
Sorting item Description
MinavailablewafersinFOUP 可使用wafer数少的lot优先
商密 Max recycle count by FOUP recycle次数多的lot优先
Max used count ofFOUP 已使用次数多的lot优先
Conf Max waiting time 等待时间长的lot优先

## 第 070 页：In Use End

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p070.jpg]]

In Use End
主要流程
Watchdog每5min扫描一次
获取InUseEnd站点可作业lot表
列表是否为空？ 判断可作业lot 结束
获取InUseEnd站点可作业 判断是否可以 获取InUseEnd站点可作业
reuselot信息 做reuse? recyclelot信息
InUseEnd站点做reuse InUseEnd站点做recycle
判断reuse是 发送报警 判断recycle
否成功？ 是否成功？
商密三级 结束 上海华力
HLMC
Confidential I

## 第 071 页：In Use End Reuse

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p071.jpg]]

In Use End Reuse
Reuse条件（ByWafer）
>Filter rule:
Filter item Description
Lot FULL Controlid Lot有Contrilid
Lot ProcessingStatus ="Active" Lot状态是active
Lot Extrastatus ="WaitForlnUseEnd" Lot必须在WaitForlnUseEnd站点
Switch InUseEnd ="T" 打开AMAInUseEnd功能
WaferUsedCount<MaxUsedCount Wafer未达到最大使用次数
Wafer Monitor status -"Available" Wafermonitor status必须为Available
Control status= "Used Controlstatus必领为Used
Carrier CarrierKind="FOUp" 母批必须在FOUP内
FOUPLocation= InStocker orIn OHB lot所在的carrier必须是lnStocker或inOHB
商密三级 上海华力
102 HLMC
ConfidentialI

## 第 072 页：In Use End Reuse

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p072.jpg]]

In Use End Reuse
母批筛选条件
Filter item Description
Lot ProcessingStatus ="Active" Lot状态是active
WaferUsedCount<MaxUsedCount Wafer未达到最大使用次数，多片中取最大，若母批中有
一片达到MaxUsedCount，将无法ReuseMerge回母批
Carrier CarrierKind="FOUp" LOt必须在FOUP内
FOUPLocation=inStockerorInOHB lot所在的carrier必须是InStocker或InOHB
Lot Extrastatus = "WaitForlnUseStart"/“WaitForinUseEndLot必须在WaitForlnUseStart/WaitForlnUseEnd站点
商密三级 上海华力
Confidential I HLMC

## 第 073 页：In Use End Reuse 编辑

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p073.jpg]]

In Use End Reuse 编辑
>Reuse逻辑
InUseEnd站点可作业lot
Reuse条件过
是否有母批（同
originalparentlotid product同 是否有多个 子批 子批条件过满
母批条件过滤 不满足条件 Lot自己Reuse ReuseLotD 最小子批
满足条件
子批Reusemerge回母批 子母批是香在 同一FOUP 子批Transport至母批FOUP
Reusemerge回母批
商密三级 上海华力
ConfidentialI 104
HLMC

## 第 074 页：In Use End Recycle

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p074.jpg]]

In Use End Recycle
Recycle条件（Bylot）
Filter rule:
Filter item Description
Lot ProcessingStatus=“Active" Lot状态是active
Lot ExtraStatus ="WaitForlnUseEnd" or
"WaitForlnUseStart Lot必频在WaitForinUseEnd或WaitForlnUseStart站点
Switch InUseEnd="T" 打开AMAInUseEnd功能
WaferUsedCount>=MaxUsedCount Wafer已达到最大使用次数
WaferRecycleCount<MaxRecycleCount Wafer未达到最大清洗次数
InUseStartLotQty<SettingQty 在InUseStart站点可用wafer小于设置提前发wafer
Must Process=“F"or(Must Process= "T" and Wafer 无需保证作业主机台或
UsedCount>=1) 对于配置的必须作业主机台的lot已作业过主机台
Carrier CarrierKind=“FOUp" 只判断在FOUP内的lot
FOUPLocation= InStockerorIn OHB lot所在的carrier必须是nStocker或lnQHB
商密三级 上海华力
105 HLMC
Confidential I

## 第 075 页：In Use End Recycle

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p075.jpg]]

In Use End Recycle
相关Lot筛选条件
Filter item Description
Carrier CarrierKind- "FOUp" 只判断在FOUP内的lot
Subplan like%RECYCLE%' 相关lot去除在RecycleFow中的lot
Subplanlike%DOWNGRADE% 相关lot去除在downgrade站点的lot
Subplanlike%PRE%
AND PROCESSINGSTATU='Hold 若lot在PreRule中切被Hold住，同时MaxHold
AND Max HOLDTIME>RTD CONFIG.IgnoreHoldTime time≤配置值时才将其作为相关lot考虑
>UI RTD CONFIG.IgnoreHoldTime
RTD Congtiguration
Critenia Selection Area
RTD Configuration
ID Parameter_Usage ParameterName Parametervalue ParameterValue Char ParameterValue I parameterValue Unit
681 AMAPeriodic Ciean OHB Trigger Time 0000-23:59 Matcning Peniod
682 AMAPenodic Clean OHB Tnigger Count 16 Number
701 AdvanceRecycle PreTime Hours
702 AdvanceRecycte
805 AdvanceRecycle IgnoreHoldTime 12 Hours
商密三级 106 上海华
HLMC
Confidential I

## 第 076 页：In Use EndRecycle

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p076.jpg]]

In Use EndRecycle
>Recycle逻辑
InUseEnd站点可作业
lot
Recycle条件过
是否有相关Lot
（同product同 自己Recycle
originalparentloti
、是
相关Lot筛选条
件过滤
Wait 都在inuseend 相关Lot是否 站点 是否在同 FOUP内 都在inuseend 相关Lot是否 站点 Wait
MES
子批Transport 至母批FOUP 符合Recycle 相关Lo是合 条件 符合Recycle 相关Lot是否 条件 子批与母批跳至Recycle FIOW第一站（HOLD）
显个
报错 报错 是香符合Merge 条件判定 不Hold 报错
解HoldMerge回
母批，发Recycle
商密三级 上海华力
HLMC
Confidential I

## 第 077 页：In Use End Recycle Must Process

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p077.jpg]]

In Use End Recycle Must Process
一目的：
通过ByProduct配置禁止未过主机台的lotAutoRecycle
内容：
1.若lot对应Product的MustProcess列为F’/为空，则无需新增Recycle判断，仍按原AutoRecycle逻
辑判断
2.对于表ama_npwprodmanage的MustProcess列为 T的Product所对应lot在AutoInuse
endRecycle时需新增Recycle判断：
1）所有相关lot处于Inuseend站点
2)Controlid为空或当有ControllD时Waferusecount>o;
符合其他Recycle条件 Must
Process-T
等待其余相关lot 所有相关lot处于 Inuse end站点
存在未作业过主机台lot无法 Null/Waferuse Controlid Is
Recycle
上海华力
HLMC
Recycle

## 第 078 页：InUse End 特殊NPW处理方法

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p078.jpg]]

InUse End 特殊NPW处理方法
INPW处于非正常状态
NPWHold暂无法处理：
NPW被他部门HOLD，短时间内无法处理，影响同一卡其他Lot Recycle，可以用 LongHoldReasoncodeHold异常Lot
NPW前量Fail：
NPW前量Fail，BYControlid上线AutoHandleFail功能，自动Reset前量FailLot
NPW剩余Wafer量少不足以使用：
1.设定提前Recycle水位，剩余Wafer<水位，将inusestartWafer自动跳至ineusend站点，整卡自动Recycle
2.打开AdvanceRecycle开关，系统自动计算当前可用保管量与PM+Routine用量，当保管量用量时，挑选Lot提前Recycle
口特殊NPW
量测标准片：
Recycle&Reuse时不需要Mrege，每个Lot单独进行，BYProduct上线SingleHandle功能
>NPWRecycleCount<=1实现自动处理
需求NPWFLOW，配置符合自动处理前提条件，与自动功能相互配合

## 第 079 页：In UseEnd RecycleCount<=1 NPW处理

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p079.jpg]]

In UseEnd RecycleCount<=1 NPW处理
只能使用一次： 有RecycleFLow, 无RecycleFLOw
INUSEEND 需求厂内Reclaim：
INUSEEND
RECYCLEFIOW RECYCLE END
RECYCLEEND Reclaim Flow
解决方式：MAXRecycle设定为1，上线lnuseendRecycle功能 解决方式：MAxRecycleCount设定为1，上线inuseend-Recycle
RecycleEnd-Reclaim,ReclaimEnd-Reuse功能
无RecycleFLOW, Flow中存在Dummy站点：
需求厂外Reclaim： INUSEEND
Dummy站点
Downgrade
IN USE start
厂外
解决方式：MAXRecycleCount设定为o，MAXReclaimCount设定为o, 解决方式：上线DummyAuto Skip功能
上线inuseend-Downgrade功能 上海华力
商密三级 HLMC
Confidential I

## 第 080 页：Recycle End

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p080.jpg]]

Recycle End
口主要流程
Watchdog每2min扫描一次
获取RecycleEnd站点可作业lot列表
列表是否为空？ 判断可作业lot 结束
获取RecycleEnd站点可作业 reuse lot信息 判断是否可以 做reuse? 获取RecycleEnd站点可作业
downgrade/reclaimlot信息
Recycle站点做reuse DOWNGRADE Next Step like Next Step like
RECLAIM
RecycleEnd站点做downgarde RecycleEnd站点做rectaim
判断是否成功？ 发送报警 判断是否成功？
商密三级 上海华力
Confidentia HLMC

## 第 081 页：Recycle End Reuse

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p081.jpg]]

Recycle End Reuse
口Reuse条件（Bywafer）
Filter rule:
Filter item Description
Lot ProcessingStatus - "Active" Lot自身状态是active
Lot Extrastatus="WaitForRecycleEnd" Lot自身必须在WaitForRecycleEnd站点
Switch RecycleEnd ="T" 打开AMARecycleEnd功能
Wafer Monitor State-Available Wafer处于available状态
WaferRecycleCount<MaxRecycleCount Wafer未达到最大清洗次数
Carrier CarrierKind-"FOup" 只判断在FOUP内的lot
FOUP Location = InStockerorn OHB lot所在的carrier必须是InStocker或InOHB
商密三级 上海华力
Confidential I HLMC

## 第 082 页：Recycle End Downgrade

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p082.jpg]]

Recycle End Downgrade
口Downgrade条件（ByFouP）
Filter rule:
Filter item Description
Lot ProcessingStatus -"Active" 所有相关Lot状态是active
Lot Extrastatus = "WaitForRecycleEnd" 所有相关Lot必须在WaitForRecycleEnd站点
Switch RecycleEnd = "T" 打开AMARecycleEnd功能
WaferRecycleCount>=Max RecycleCount 所有相关Wafer已达到最大清洗次数
Downgrade Step Mapping info in Downgrade站点有对应的ReassignMapping配置
FabMaintainDownGrade'is not Null
Carrier CarrierKind-"FOUp" 只判断在FOUP内的lot
FOUP Location= InStockeror In OHB lot所在的carrier必须是InStocker或lnOHB
商密三级 上海华力
HLMC
Confidential I

## 第 083 页：Auto Reassign(Downgrade)

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p083.jpg]]

Auto Reassign(Downgrade)
口主要流程
Watchdog每5min扫描一次
获取Downgrade站点可作业lot列表
判断可作业Iot列
表是否为空？
获取Downgrade站点可Reassign
lot信息
Downgrade站点做reassign
发送报警 判断是否成功
结束
商密三级 上海华力
HLMC
Confidential I

## 第 084 页：Auto Reassign(Downgrade)

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p084.jpg]]

Auto Reassign(Downgrade)
口Reassign条件（Bylot）
Filter rule:
Filter item Description
Lot ProcessingStatus ="Active" Lot自身状态是active
Lot Extrastatus="WaitForDisposal" Lot自身必须在WaitForDisposal（即Downgrade）站点
Switch Reassign ="T" 打开AMAReassign功能
Mapping info in FabMaintainDownGrade fromproduct&fromstep符合Mapping配置表
Carrier CarmierKind="FOUp" 只判断在FOUP内的lot
FOUPLocation= InStockerorin OHB lot所在的carrier必须是InStocker或lnOHB
商密三级 上海华力
ConfidentialI HLMC

## 第 085 页：Auto Reassign(Downgrade)

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p085.jpg]]

Auto Reassign(Downgrade)
口 Reassign计算
主要流程：
Compute Method:
A=to product currentwip wafer qty(Lot ProcessingStatus "Active"or“Hold")
C-the sum of to product current wip all wafers remain available recycle count
D=to productofmaxrecycle count
Result=A/B
>Result1=B*D-C
Reassignlotpriorityfordowngrade:
>Resultthe smallerthepriority
Ifresultsame,thenresult1thebiggerthepriority
商密三级 上海华力
Confidential I HLMC

## 第 086 页：IMP Monitor

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p086.jpg]]

IMP Monitor
口IMPMonitor分批逻辑
对于IMP的源种设备，在进行点检时需要更具机台作业的源种情况进行点检，所以RoutineMonitor是否分批还需要FollowIMP机
台目前打开的源种，同机台任意源种PA每天只需作业1个，所以针对PA进行分批时，需另外检查是否已分批或已作业
口涉及UI 与其他区域Routine
MonitorSourceCategory Watchdog scanevery5min Monitor分批时间计算
方式无差别
Check monitor
根据monitorppid
Check源种是香打开 后一位（无取第一位）与UI
MonitorSourceCategory对比
Get control id list
拿取该机台所有INUSE的controlID，其中中是否有符合
Check是否有%PA%B1% %PA%BIl%的controlID，若有，则不再分批；
Controlid已分批或已作业 monitortime是否存在为当前所在天，若存在，则不再分批； 拿取该机台所有符合%PA%Bll%的controlID，再看其last
%PA%BR%类似
Get monitor lot list
Existmonitor lot? End
Getmonitor source lot Monitor准备：
1.母批筛选
2.Monitor分批
商密三级 此处逻辑一致 上海华力
ConfidentialI HLMC

## 第 087 页：THKNPWAuto Handle

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p087.jpg]]

THKNPWAuto Handle
Litho涨膜Monitor自动处理
当前存在LITHOSIARCTHKWPAWafer必须涂布一层Soc才能发Recycle，但FabRoutineMonitor片数为4或6Pcs，因此导致一卡lot总有1-3PcsWafer无法投出，导致无法Recyle需求在
Wafer总数在低于4Pcs时，AMA自动投入固定Controlid的Monitor，作业完成后即能实现自动Recyle
具体逻辑，
一、设定水位
RTDConfig中设定Product及其水位，小于水位触发后续分批判断
二、选择需要处理的Wafer 存在不属于UI中的Inuse Watchdog scan every5min
筛选条件如下： Monitor暂不处理
1.PRODUCTname=RTDConfig.THKNPWLeftAvaCount配置Product 选择需要处理的Wafer
2其余条件与RoutineMonitor分批筛选条件一致 远择分批Controlid
将选出Lot按同PRODUCT小数点前Lotid相同的分为一个Group，计算每个Group总可用Wafer量，若小于设定水位，则认为这个Group的剩
余可用Wafer需要进行自动分批 选泽分批Lot
三、选择分批Controlid
Controlid=UI THKNPWAutoHandle.ControlidETHKNPWAutoHandle.Enable-T
四、选择分批Lot
1.SourceLot从上述一筛选出的Lot中进行选取
2.SourceLot排序：
①LotWaferqty=ControlidWafergty的Lot优先
②Foup内存在InUseMonitor对应Machine与当前Controlid所对应Machine相同的优先
③LotWaferqty大的优先
4)后续Sotring同RoutingMonitor选取的SourceLotSorting
口涉及UI
THKNPWAutoHandle

## 第 088 页：口编辑V

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p088.jpg]]

口编辑V
DegasMonitor
动画
DegasMonitor分批逻辑
Copper对于CUB机台MonitorDegas腔只需做同GroupName中任腔，当其中某一腔不可作业时需分批Group号一腔进行作业。MonitorAutolnUse上线自动Monitor只上线同 评论
GroupName中任一即可。
口涉及UI
DegasMonitorGroup 与其他区域Routine
Watch dog scan every 5 min Monitor分批时间计算
方式无差别
Check monitor
Check腔是否 正常分批
可作业
是否设定有
Degas Monitor End
Group
Check同
GroupMonitor对
应腔是否可作业
同GroupMonitor
分批同DegasMonitorGroup Last Monitor Time
商密三级 Monitor 上海华力
HLMC
Confidential I

## 第 089 页：DIFFMonitor

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p089.jpg]]

口编辑
DIFFMonitor
随炉Monitor
作业产品时，需要伴随作业炉管Monitor，根据UI中水位提起分批，提前量测前值，待派工时直接调用
涉及UI
AMA.FMLAutolnuseStart Watch dog scan every 5min 无需计算分批时间 Enable即要分批
老数名 描述 是否必填 是否支持 通配（*） 单位 Check monitor
ControliD 对应的monitorcontrolID
FMLNO 对应的controlID所需的片数 只计入无Batchid的数量
CarrierWater Mark 对应的controlID的foup数量 END Monitor的Foup数量 Check满足片
对应controlID是否需要自动分批 是够足够
Enable T需要自动分批 的开关，F”
F：不需要自动分批
WaitingTime 可等待的最大时间 当wafer最少的母批在sorter时， 小时 已不使 Get control id list
WEEKLY Monitor 与RoutineMonitor分
按时分批，设定方式与计算方式都和RoutineMonitor相同 Watch dog scan every 5min 批时间计算方式无差别
口涉及UI Check monitor
AMA.Furnace Monitor
Check满足片数 1.数量通过底层设定拿取
END Monitor的Foup教数量 2.只拿取无Batchid的Monitor
是够足够 3.对应机台上有正在作业的同
ControlidMonitor，无需分批
商密三级 Get control ld list 上海华力
HLMC
Confidential I

## 第 090 页：Auto Handle Fail

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p090.jpg]]

Auto Handle Fail
前量Fail的lot会自动Hold给对应PE，通过AMA自动解前量Holdlot且CancelcontrolID，即可达成控片烂账Auto处理。 前量Fail自动处理
具体逻辑
找到前量Fail的Lot 该lot处于前量站点，即inusestart作为起始站点，Inuse start后的monitorProcess站点作为结束站点，lotsteplD为起始站点至结束站
点间的任一量测Step对应的stepID（FumaceMonitorstepdescriptionLIKE%pre%，LOT即处于前量Step） Watchdogscan every5min
Holdcount=1&fwholdrelease.HoldType=EDC
Release前量Fail的Lot井卡控Lot不可派工 需求ALLReset的 Check前量Failmonitor Lot
AMAWatchDog每5分钟扫一次，对于符合条件的Lot自动执行Release动作 FurnaceMonitor还需 卡控同Foup内其他Lot Release前量Fail的Lot并卡控
符合以下卡控Lot卡控派工： Lot不可派工
lot有monitorcontrolid(fabeqpmonitorprocess）
对应controlid存在于MonitorAutolnUse表中且AutoHandleFail=T； 传给MESReset前量Fail
lot上一站点的stephistory，若存在activity=hold，holdtype为EDC，并且存在activity=release,useridAMA，卡控不可派，RTD ReleaseLot
reason为“MonitorStatusFail"
三、Reset前量Fail的Lot
口涉及UI
MonitorAutolnuse AutoHandleFail
上海华力
商密三级 HLMC
Confidential I

## 第 091 页：OverQtime原因分析

![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p091.jpg]]

OverQtime原因分析
对当前站点长时间未派工的产品Log中直询是否被
明确overqtime时间，站点和 Assign卡控不派工，并对Assign中未预排进行分
flow信息，绘制qtimeloop 分析over原因 ，通过各个Assign报表中的Reason及预排的排
序指标进行具体分析为Assign的原因
qtime放货？
进入loop后， over站点机台 是否不可作业？ 当站未按照 卡控下游断线？ 卡控下游产能？ 当站QZone 当站受其他 原因卡控不 加量加测？ Qtime内
机台临时 Down 派工机台派工 顺序是否合理 起始站点下放 时是否卡控？ 时是香卡控？ 起始站点下放 起始站点下放 时是否卡控？ 是否善要做 Seasan 站点长时间作业？ Loop中美些量烫
条件inhibit QTimeUrgencyit 算是否准确（PT的 维护是否合理） 符合强派？ 起始站点 下放到当站后 下游机台断线？ 符合强派？ 起始站点 不足？ 下游机台产能 下放到当站后 AllFoup作业模式？ SeqRun/SeqRun 确认机台
分折卡控产能原因
起始站点强派 原因是什么？ 当站不符合强 派的原因？ 原因是什么？ 起始站点强派 当站不符合强 派的原因？ 确认下家产能与实际产能是香匹配？
分析断线原因 卡控站点机合产能损失！
Prep时间，明确该时间点对应卡控贴点放货 童若LotHistory明确所在loop超站点lob constraint WPH是否维护 起始站点放货时，是香存在同时下敢？
时的可作业机台，并对该卡控站点其可作业 机台状态 ENG CONTROL
机台进行进一步童询 PM flag 机台持件影钢实际产出？
N20PM控货是否生效 Capability开关 Loop内EkistingLot存在异常变化？
Recipe/PPID状态OK
