---
type: structured-source-note
topic: DSP派工系统简介
tags: [DSP, 自动派工, 结构化整理, RTD, AMA, QZone, NPW, AMHS]
---

# DSP 派工系统简介 - 内容结构化

## 资料概况

- 原始图片数量：91 页
- 资料形式：PPT 图片 OCR
- 主题：DSP 自动派工系统、RTD、AMA、Global / Local 派工规则、AMHS、QZone、NPW 自动化
- 重要提醒：本笔记基于 OCR 自动整理，涉及生产系统细节时应回看原图确认。

## 总体目录

- 01 DSP 系统与自动化架构：第 001–010 页
- 02 自动化派工规则：第 011–025 页
- 03 AMHS 与搬送存储：第 026–033 页
- 04 QZone 管控：第 034–049 页
- 05 NPW 自动化处理：第 050–090 页
- 06 OverQtime 原因分析：第 091–091 页

## 01 DSP 系统与自动化架构

### 第 001 页：自动派工系统全面介绍

- 分类：综合
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p001.jpg]]
- 关键 OCR 行：
  - 自动派工系统全面介绍

### 第 002 页：DSP系统介绍

- 分类：综合
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p002.jpg]]
- 关键 OCR 行：
  - 编辑
  - 01
  - DSP系统介绍
  - 02
  - 自动化功能介绍
  - 03

### 第 003 页：DSP系统介绍

- 分类：综合
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p003.jpg]]
- 关键 OCR 行：
  - 编辑Y式
  - 动画
  - 01
  - Part
  - DSP系统介绍

### 第 004 页：自动化系统逻辑架构

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p004.jpg]]
- 关键 OCR 行：
  - 生产管理准备 NPW准备 生产监控
  - 淮备层 产能支持 投产规划 Season Dummy Outside Down grade Recycle
  - 生产调度 全局 逻辑运算 执行派工 自动报警
  - 机制层 产品片 NPW 派工清单 设备状态 艺要求 NPW处理 协同型
  - 存储管控

### 第 005 页：全自动化系统信息架构

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p005.jpg]]
- 关键 OCR 行：
  - RTD（实时派工系统） AMA（自动派工管理系统）
  - 1.Sorting（排序功能） 1.派工触发和最终核对，支持LotPre-reserve
  - 2.WhereNext（FOUP暂存指定功能） 2.NPW管理
  - FAB RTD AMA
  - EAP MCS 派工结果
  - APC PMS 厂信息 搬送存储 筛选排序

### 第 006 页：实时自动派工逻辑（RTD）

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p006.jpg]]
- 关键 OCR 行：
  - 实时自动派工逻辑（RTD）
  - 应用调度参考的结果，检测实时限制和执行各区域派工规则，将产品派工到设备上。
  - 所有设备群通用逻辑，筛选掉不能派工的Lot，如：
  - RTD Filter Qtime ZoneControl/Run Path（进入Q-zone前判断下游是否断线）
  - InhibitCheck，NPW时效性管控等
  - 各设备群专用逻辑，根据设备特性筛选掉不能派工Lot，如：

### 第 007 页：设备自动化模式

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p007.jpg]]
- 关键 OCR 行：
  - 设备自动化模式
  - AUTO Mode Description
  - Manual Prep[lU]+JobIn[lUi]+JobOut[U]
  - JobPrep[IUI]+EAP(JobIn+JobOut)
  - AUTO-1:
  - AUTO1

### 第 008 页：Auto 2-Lot Reserve and Queue Consume

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p008.jpg]]
- 关键 OCR 行：
  - Auto 2-Lot Reserve and Queue Consume
  - Lot Reserve
  - Manual Lot Reserve and send FOUPto Load Port
  - MES RTD
  - Tool Efficiency MES RTD

### 第 009 页：Auto 3-Lot Reserve and QueueConsume

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p009.jpg]]
- 关键 OCR 行：
  - Auto 3-Lot Reserve and QueueConsume
  - Lot Reserve
  - TogetaFOUP Auto Lot Reserve and send FOUP to Load Port
  - RTD MES MES RTD
  - AMA

### 第 010 页：实时自动派工系统触发方式（AMA）

- 分类：DSP / RTD / AMA
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p010.jpg]]
- 关键 OCR 行：
  - 实时自动派工系统触发方式（AMA）
  - 每当某台设备状态发生切换、某个portevent发生变化或port派工模式发生变化时，会询问RTD派工
  - Pre-send功能：根据EQP在作业Lot的剩余片数，提前给机台/port派工Lot

## 02 自动化派工规则

### 第 011 页：自动化功能介绍

- 分类：综合
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p011.jpg]]
- 关键 OCR 行：
  - 编辑
  - 02
  - Part/
  - 自动化功能介绍

### 第 012 页：Global派工规则 QzoneControl

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p012.jpg]]
- 关键 OCR 行：
  - Global派工规则 QzoneControl
  - Local派工规则 NPW

### 第 013 页：Global派工规则

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p013.jpg]]
- 关键 OCR 行：
  - Global派工规则
  - 口概述：GlobalRule指各Module通用的DSP派工逻辑，从整体控线角度出发，确定最优的调度方案。涉及Lot基本属性、Foup属
  - Get Lot list From MES 功能名称 从MES获取可派工Lot信忘，即，符合Lot状态OK/FOUP状态OK/DSP未禁止的Recipe/Reticdeinmachine/无 功能描述 LotComment/RTDInfo
  - Machine/Chamber均要处于可作业状态：此外，还要检毫所有关型的constrain限定 BatchID等条件的Lot，若RuncardLot定的机台非本机台，则不能派工 NotJobPrepLowPnonty: NotinFouce
  - Multi Lot InOne Foup 同Foup中的其他Lot正在作业/已被Reserve时，该Lot不能派，用户设定的机台不可以作业与其他Lot共用FOUP的Lot EQPUnavailable:x,ChambarState:wo
  - Reason Check Qzone Control 未达到是少等待时间的Lot不能派工被qzone管控下游断线或产能不足的Lo坏不能派工 MultiLotBlock

### 第 014 页：常见问题查询

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p014.jpg]]
- 关键 OCR 行：
  - 产能/断线相关Case
  - >卡控Capacityissue或Pathissue可以在FABScheduler→QzoneControl中查看原因
  - Qzone整体元许放货量，及断线或堆货站点
  - 2.点击模块1的RemainWIP，可查询Qzone中各站点允许放货量
  - 3.点击模块2的RemainWIP.可查询Qzone中某站点各机台的可
  - Qtime Urgency

### 第 015 页：Global派工规则 Qzone Control

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p015.jpg]]
- 关键 OCR 行：
  - Global派工规则 Qzone Control
  - Local派工规则 NPW

### 第 016 页：LITHO派工规则 口编辑

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p016.jpg]]
- 关键 OCR 行：
  - LITHO派工规则 口编辑
  - 口概述：综合考量Reticle、R2R、DomaPath、高低能、垂直限定等因素限制Lot在机台上可作业性，并结合预排程制定出相应的
  - 符合LITHO区域设备特性的自动派工逻辑。
  - R2R R2R控的Lot不留作业 LotComment/RTDInfo
  - Doma DomaPath开启时保证整条DomaPath可以作业 R2ROVL/CDFail
  - （管控Lot不自动派工） 垂古限定 限定该层与上一层作业相同机台 Too ManyHighEnergy Lot

### 第 017 页：放版指导

- 分类：Local 派工规则
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p017.jpg]]
- 关键 OCR 行：
  - 放版指导筛选条件
  - sin snfam STATUS PRIORI nin remal pretool RTDREASON INTERNALP HOLDO LOTTYFE REMQT RUNCA RETICUE PART STAGE RECPE

### 第 018 页：常见问题查询

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p018.jpg]]
- 关键 OCR 行：
  - R2R相关Case
  - >R2RFail：R2RFail原因都是因为匹配获取R2R配置信息时有问题，常见问题及解决方法如下
  - 问题：1.R2RFail：R2R配置信息表中无对应信息/前层作业信息未获取到。
  - 2.R2RFailXX状态：R2R配置信息表中R2R状态为OFF/PIRUNOFF。
  - 解决方法：联系R2R核实对应配置信息或R2R状态。
  - >Mask出厂安全管控：MaskTransferToFab5时会将用到该Mask的LotHold在安全站点，等待Mask回线后Release，常见问题及解决方法如下：

### 第 019 页：ETCH派工规则

- 分类：Local 派工规则
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p019.jpg]]
- 关键 OCR 行：
  - ETCH派工规则
  - 口概述：结合ETCH区域Process机台作业特性，综合考量DomaPath、R2R限制Lot在机台上可作业性的各种因素等，而制定出
  - 相应的解决方案及设定一系列逻辑规则，判断出Lo的可作业性及紧急程度，并根据各个指标对可派工的Lo进行合理的实时调度
  - LotComment/RTDInfo
  - Port Bonding ByChamber/FlowRecipe/Capability设定只能/不能在绑定机台的 LoadPort上作业，未设置LoadPort绑定的LoadPort共通 Flowrecipe fail, ChamberNamefail,
  - Reason MachineCapability fail,

### 第 020 页：常见问题查询

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p020.jpg]]
- 关键 OCR 行：
  - Recipe连续作业相关Case
  - >问题：LotBP2Z630QT小于4h触发强派，BEASHM09同Recipe连续作业，但LotBP2Z630仍OQT。
  - 原因：BEASHM09机台的Sorting为QTURGENCY0/1/2/3、RecipeGroupContinue、Rework、RunPri Prefer（MFGControl优先作业）、Q0Prefer等，
  - 管控Port派工相关Case
  - >问题：BP2V604/BP2V622/BP2Y101/BP2Y106到达E-ASHHD-F站点未优先派工，直至OQT。
  - 原因：由于BEASHM22/20设定有port管控，针对A，B腔分配的剩余作业枚数低于10Pcs。因该机台多个Qtime较急的Lot为单B腔作业，单B腔Lot上机台后，其余单

### 第 021 页：TF派工规则

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p021.jpg]]
- 关键 OCR 行：
  - TF派工规则
  - 口概述：结合TF区域Process机台作业特性，综合考量Recipe连续、Film连续、连续上限、同条件WIP量、累计膜厚Clean、瓶颈
  - 机台等因素设计一系列派工规则，判断Lot在机台上可作业性及紧急优先程度，并结合ALL-SGE排程等特定调度方式制定出符合
  - TF区域设备特性的自动派工逻辑。
  - Reason 功能名称 Chamber/FlowReaipe/Capability只能/不能在绑定机台的LoadPort上作业，未设量LoadPor绑定的LoadPort共通，支持正 功能描述 LotComment/RTD Info
  - （管控LOt不自动派工） Film lean 对用户设定的并行模式机台不能司时作业两种不同的膜种 反同设定 ChamberNlame faitPlowrepe fai MachmeCaoability falil

### 第 022 页：ALL SGEAssignment

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p022.jpg]]
- 关键 OCR 行：
  - 功能描述
  - SGELoop存在连环Qtime短、SGE机台产能小、产品Release情况不一致、SGE机台内部限定最多2个Foup可同时作业、来货道次设备类型多样化等诸多问题，因此开发
  - ALL-SGE预排功能，所有产品按照一套管控逻辑从相对安全站点开始管控放货，结合Qtime/Chamber搭配/穿插作业/SmallLot不连续/SGEPirun/NPW/高等级/优先设定
  - /SubLot等因素，实现SGE机台混Run，消除OQT的风险，提升机台各腔利用率，减少手动管控操作。
  - Homc RTD.AL

### 第 023 页：常见问题查询

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p023.jpg]]
- 关键 OCR 行：
  - SGECannotRelease：lot在ALL-SGEReport中卡控reason时，rule里会卡此reason，主要原因如下：
  - 4.卡控断线
  - 1.当站多为高等级lot，导致normallot排序靠后。
  - 3.该loop内有大量长qtime的lot，短qtime的lot需等待穿插作业。
  - 4.当站有qtime更加worse的lot，需等待其余lot先行下放，
  - >SGENeedSeqRun：lot需要等待排序靠前（剩余QT，可作业腔，高等级lot.）的lot按照顺序下放，避免排序混乱。

### 第 024 页：CMP派工规则

- 分类：Local 派工规则
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p024.jpg]]
- 关键 OCR 行：
  - CMP派工规则
  - 口概述：结合CMP区域Process机台作业特性，综合考量Recipe连续，R2R、PMCycle内同条件连续、TRIM机台LifeTime控货、
  - CCU机台错开PM等因素设计一系列派工规则，判断Lot在机台上可作业性及紧急优先程度，并结合CCU排程等特定Pirun指导方
  - 式制定出符合CMP区域设备特性的自动派工逻辑。
  - 功能名称 功能描述 LotComment/RTDInfo
  - PORT绑定功能 Chamber/FlowRecipe/Capability只能/不在级定机台的LoadPort上作业，未设重LoadPort绑定的LoadPor共通，支 ChamberName fail

### 第 025 页：WET派工规则

- 分类：Local 派工规则
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p025.jpg]]
- 关键 OCR 行：
  - WET派工规则
  - 口概述：WET分为Chamber/Batch两种类型，因此分为两部分逻辑。WET区域派工逻辑不仅仅对WET本身使用，相对于其他
  - chamber机台还多了一部分WET-DIFF，WET-SGE产品的派工逻辑。
  - 口MultiChamberWET管控逻辑 口WETBatch管控逻辑
  - Global功能 PPID选择 WET-DIFF管控 Global功能 PPID选择
  - Port绑定 PRF-SGE管控 高低温机台切换 Buffer数量 Batch填充率

## 03 AMHS 与搬送存储

### 第 026 页：02 评论

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p026.jpg]]
- 关键 OCR 行：
  - Global派工规则 000 Qzone Control
  - Local派工规则 NPW

### 第 027 页：华力AMHS

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p027.jpg]]
- 关键 OCR 行：
  - 华力AMHS
  - 口AMHS:
  - AMHS:AutomaticMaterialHandling System中文译作自动物料搬送系统，也称为天车系统，是业界最灵活的
  - 集合储存（stocker），运输（搬送小车）和管控（MCS）制品在FAB设备之间搬运解决方案
  - Bay1 Bay 3 Process Bay 5 Intrabaytransport 300 mm UNIFIEO AMHS
  - 采用interbay的半自动化AMHS intrabay全自动AMHS系统

### 第 028 页：Stoker

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p028.jpg]]
- 关键 OCR 行：
  - 口Foup储存柜（stocker）整体构造
  - Stocker型号采用大福CLS-50型，本体构造主要分为四部分：
  - 搬送口：用于FOUP进出stocker.包括与OHT相连的自动口以及手动出入口
  - SSS：stocker手动操作面板

### 第 029 页：口OHB

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p029.jpg]]
- 关键 OCR 行：
  - OHB
  - 口OHB
  - OHB:安装于小车轨道外侧用于临时存储FOUP
  - 单个成本远低于stocker单个棚位
  - FAB6OHB

### 第 030 页：六厂搬送状态

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p030.jpg]]
- 关键 OCR 行：
  - 搬送概况 OHB&STK可储存量 评诊
  - 平均搬送时间：2:17 OHB 4559 2326 6865 51%
  - >实际运行天车数：280台 Stocker 5647 1858 7505 33%
  - 口 PurgeOHB&STK分布
  - BSTKP104 BSTKP106 OHB:BAYA06-A09A16

### 第 031 页：搬送存储作用 编辑Y式

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p031.jpg]]
- 关键 OCR 行：
  - XCDAOHB&STK 存储

### 第 032 页：搬送系统运行方式（AMA&RTD） G编辑

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p032.jpg]]
- 关键 OCR 行：
  - 搬送系统运行方式（AMA&RTD） G编辑
  - RTD（自动派工系统）在搬送流程中的作用和考量因素：
  - DSP系统 ·根据工艺需求、设备位置、OHB/Stocker空闲情况，决定Lot/FOUP存储位置
  - RTD决定存储位置的优先顺序
  - Purge OHB Purge STK OHB STK
  - 当OHB/Stocker存放率高于上限，则找寻下一优先级的OHB/Stocker

### 第 033 页：预搬送功能

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p033.jpg]]
- 关键 OCR 行：
  - 对于堆货机台，产能紧张，搬送时间过长可能造成机台空机等待IDLE，导致产能LOSs，为使Lot能尽快上机台作业，对于LP
  - 都已满机台，提前搬送Lot至机台OHB，减少搬送时间。
  - 预搬送 当设备上剩余作业量小于水位时，AMA根据RTD给出的派工清单，将顺位1的Lot添加入MES的
  - MES发送搬送指令给MCS将Lot搬送至该设备的DefaultOHB。
  - Lot3 AB P1 到EQPDefaultOHB
  - 派工 设备LoadPort空闲时，RTD优先排货queuereservationlist中的Lot

## 04 QZone 管控

### 第 034 页：02 评论

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p034.jpg]]
- 关键 OCR 行：
  - Global派工规则 000 QzoneControl
  - Local派工规则 NPW

### 第 035 页：QZone管控简介

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p035.jpg]]
- 关键 OCR 行：
  - QZone管控简介
  - Qtimeduration
  - >QZone EndRun step2 Tips:
  - 保证区间内设备有足够WIP但不超时。 StartRUN Qtime结束站点不一 定为lo的安全装点
  - step4 safetyvalue翔断
  - >Qzone方式 lotOverQtime时由currentPE设定action忘是hoid

### 第 036 页：QZone管控简介

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p036.jpg]]
- 关键 OCR 行：
  - QZone管控简介
  - 口管控内容
  - QZonecontrol Qtime urgency
  - -ot放入loop内后不会overqtime 要求
  - -lot在放入loop内后不会造成其他 Loop外产 品作业管控 Loop内产 品作业管控 每个lot在gtime范围内作业出loop
  - lotoverqtime -lot的作业不影响出货/瓶颈所需lot的作业

### 第 037 页：QZone管控简介

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p037.jpg]]
- 关键 OCR 行：
  - QZone管控简介
  - 口管控类型
  - 口管控难点
  - 因素维度多，精准管控难度大 新型管控需求多，覆盖面更广
  - ·下游机台作业时间大于qtimeduration;
  - ·Zone中存在多道相同制程 .Wafer level qzone

### 第 038 页：QZone管控简介

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p038.jpg]]
- 关键 OCR 行：
  - QZone管控简介
  - IDLERUN RECYCLE BACOUP ENG LOT
  - Flow信息 Qtime信息 联取Flow信惠
  - 获取Normal/Branch 获取Qtime信息： Norma Flow BranchFlaw
  - 序编码。 qtimetype. qtimelimit. 取Qtime 依据Step 获取开始站点和 获取Qtime
  - 模型计算 根据各Lot真实QtimeflowInfo信息，按照 顺字编码

### 第 039 页：QZone管控简介

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p039.jpg]]
- 关键 OCR 行：
  - QZone管控简介
  - 口管控逻辑
  - Constraint Qzone Exception
  - 主要作用 判断每个prod在每个站点机台的 判断qzone中每个站点每个机台的产能情况 忽略草些设定站点的QZone管控结
  - recipe可作业情况
  - 判断内容 机台是否建Recipe 1机台产能：capability开关，EQPstate 1.白名单：制造科/PE要求设定无

### 第 040 页：QZone管控简介

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p040.jpg]]
- 关键 OCR 行：
  - QZone管控简介
  - 和剩余加工步骤中需经过机台群的产能，管控q-zone起始站点放货情况并能根据卡Qzone的情况进行特殊处理。
  - 获取Qzone信息 计算各Lot到每个
  - PPID Recipe Constraint EQP/CHMBstatus 一多次分配 Queue sort 一待派TLot Wafer Balance Loop内lot 多次分配 待派工Lot 衡量overqtime可能性 待派工Lot不超qtime 待派工Lot放入loop后 不影响其他Lot作业 一堆货 一断线 下游卡Qzone
  - 排序 和在相应Lot的queue 管控放货 8KLRTDLOTE

### 第 041 页：QZone管控简介 口编车

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p041.jpg]]
- 关键 OCR 行：
  - QZone管控简介 口编车
  - 口QZoneControl应用实例（判断处于Q-timeloop起始站点的Lot能否派工）
  - ①获取各qzoneloop内所有要经过targetstep67对应capability的Lot，并计算每个lot的qsort值，从小至大排序；
  - Lot1 20 10 排序 Lot3 20 Target stepe7
  - ②拿取targetcapability可作业机台/chamber及WPH，根据qsort依次计算 ③判断qzone起始站点的Lotv放入zone后是否会影响已在zone中的Lot：
  - target_capability各机台在相应lot的qsort范围内的作业需求和产能， Lotv进入zone后不会超qtime

### 第 042 页：其他QZone相关附加管控功能

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p042.jpg]]
- 关键 OCR 行：
  - 其他QZone相关附加管控功能
  - 特殊qzoneloop需要特殊管控方式，如CT/SAPloop需要byFOUP管控数量或部分IMPloop只管控结束站点WIP等，原qzone模型不适用。
  - Qzone管控形式：
  - ByBegin：管控起始站点同时在作业产品数量
  - ByLoop：管控起始站点（在作业WIP）至结束站点（所有WIP）总产品数量
  - √ByEnd：管控结束站点（所有WIP）总产品数量

### 第 043 页：其他QZone相关附加管控功能

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p043.jpg]]
- 关键 OCR 行：
  - 其他QZone相关附加管控功能
  - 口Loop内lotqtime管控
  - 1.Lot相互独立（QtimeUrgency）
  - Lot5在S4站点的gtime派工等级？
  - 计算QT紧急程度：用Lot当前位置至结束站点的剩余qtime时间与估算剩余作业时间的比值作为QT紧急程度指标

### 第 044 页：其他QZone相关附加管控功能 4编辅辑

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p044.jpg]]
- 关键 OCR 行：
  - 其他QZone相关附加管控功能 4编辅辑
  - Lot2在S2站点的qtime派工等级？
  - 估算Lotoverqtime可能性：当某Lot在容许时间范围内不允许插入一卡Lot时，将降低所有紧急程度比该Lot小的lot派工优先等级。
  - [RemainQTime-RemainCycleTime-Z （ProcessTime/Avail ToolCount)-GroupRemainTime]sRatio*ProcessTime
  - lotid Rqt-Rct PT PTEactSTN GroupRemainTime 排序 Lotid QoPreferfFlag QoPrefer等级

### 第 045 页：Qzone异常处置机制

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p045.jpg]]
- 关键 OCR 行：
  - Qzone异常处置机制
  - 断线：在Q-Time下游某个站点所有可作业机台无作业条件（Constraint/RecipeInhibit/机台不可作业/未维护WPH/Capability未打开）。
  - 堆货：在QZoneLoop中WiP量达到了QZone算法计算的wiPLimit，qzone起始站点无法向下游放货，造成卡QZoneCapacity。
  - Tool down/堆货
  - Tool down/堆货

### 第 046 页：Qzone异常处置机制

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p046.jpg]]
- 关键 OCR 行：
  - Qzone异常处置机制
  - 连环qzone下游出现断线或堆货时，根据各qzone的风险程度进行特殊管控。
  - 指定RQT放货 强派 指定remainqtime放货：
  - Tooldown/堆货 RQt<设定值：强派（忽略所有断线/堆货站
  - Special target Loti设定不管控 强派 RQ>=设定值不底（卡控所有断线/堆货站
  - QT1 QT2 QT3 >MPc设定Target：仅针对堆货

### 第 047 页：Qzone异常处置机制

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p047.jpg]]
- 关键 OCR 行：
  - Qzone异常处置机制
  - 口SafetyValue定义标准
  - SafetyValue QT类别 QT优先级 建议处置方式 定义标准 管控级
  - 长期停靠 无Q-time管控 Long term bank
  - 短期停靠<=15D（待定）无Q-time管控 可短期停靠
  - 停靠时间<=7D（待定）无Q-time管控 Q-timewindow未知，不建议长期 停靠 无风险

### 第 048 页：Qzone异常处置机制

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p048.jpg]]
- 关键 OCR 行：
  - Qzone异常处置机制
  - Qzoneloopsafetyvalue取值
  - 起始qzone safetyvalue:该lot当前step的safetyvalue
  - 中间qzone safetyvalue:所有qzone的最大safetyvalue
  - Vm=max(min(safetyvalue;)hj 其中： Vm
  - ie中间层qzone中的个step

### 第 049 页：Qzone异常处置机制

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p049.jpg]]
- 关键 OCR 行：
  - Qzone异常处置机制
  - 口SafetyValue风险等级管控逻辑
  - 是否向下游放货？ Tooldown/堆货
  - loop Qzone Any situation
  - 不存在可rework RQT<=n%*QTimeLimit
  - loop qzone VsVe 且Ve≤0/1 件放货 m值的设定情况：

## 05 NPW 自动化处理

### 第 050 页：NPW自动化结构图

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p050.jpg]]
- 关键 OCR 行：
  - NPW自动化结构图
  - 口功能结构：涵盖所有NPW类型，并根据NPW使用流程，划分成四大功能模块
  - 功能模块：备片（AutolnUseStart）、派工（Dispatch）recycle（AutolnUseEnd）以及downgrade（AutoRecycleEnd）
  - NPW类型 Season Idle Recipechange Recipe idle Wafercount PM/Down
  - PreClean 自动派工 派工条件 派工等级 派工模式
  - 自动派工 派工条件 派工等级 派工模式

### 第 051 页：In Use Start--Routine monitor

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p051.jpg]]
- 关键 OCR 行：
  - 主要流程

### 第 052 页：In Use Start--Routine monitor

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p052.jpg]]
- 关键 OCR 行：
  - In Use Start--Routine monitor
  - Bytimeweekly分批：split time =date(now)+ time(initial time)-leading time
  - Monday Monday Monday
  - Time
  - Splittime
  - 1.当前日期为指定日期时：

### 第 053 页：In Use Start--Routine monitor

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p053.jpg]]
- 关键 OCR 行：
  - Send alarm Exist monitor source lot? 2.Monitor分批 1.母批筛选

### 第 054 页：In UseStart--Routinemonitor 问题查询

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p054.jpg]]
- 关键 OCR 行：
  - AMAlog 通过NPWEPRFLOWReport文件拿取该Step的最新PLAN&Subplan版本（该
  - 1234 是否有可用Wafer（Lotowner） 文件由于数据量过大舍弃了RecycleEnd等站点，文件中没有的可通过表

### 第 055 页：In Use Start 一加做&延期monitor

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p055.jpg]]
- 关键 OCR 行：
  - 系统申请 管理签核 自动备片 自动派工

### 第 056 页：In UseStart-复机NPW 编辑

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p056.jpg]]
- 关键 OCR 行：
  - In UseStart-复机NPW 编辑
  - PM 自动分批（auto） PMNPW自动备片
  - WAIT PE->WAITMFG 自动派工（auto） PE勾选is triggerPM season PE
  - MON PM alam 触发TRC.PMNPW自动派工 DSP
  - DOWN DOWN NPW自动备片 DSP
  - WAIT PE->WAIT MFG MON DOWN 触发TRC.DOWNNPW自动派工 DSP

### 第 057 页：In Use Start 一复机NPW

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p057.jpg]]
- 关键 OCR 行：
  - In Use Start 一复机NPW
  - 口复机NPW分批逻辑介绍：

### 第 058 页：In UseStart 一复机NPW自动分批

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p058.jpg]]
- 关键 OCR 行：
  - In UseStart 一复机NPW自动分批

### 第 059 页：In Use Start 一复机NPW自动派工

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p059.jpg]]
- 关键 OCR 行：
  - In Use Start 一复机NPW自动派工
  - >前/后量派工：
  - 复机NPW优先：对于复机的NPW，派工时，RecoveryNPWFlag生效 Monitor group info:
  - 其他sorting指标相同时，会优先派工（新增功能区分复机优先级）：
  - 相关sorting:RecoveryNPWFlag及RecoveryNPWFlag1/2/3/4 1.SeasonA(PT:60min)
  - 的monitor，会根据机台的复机时间以及该monitor前面需要作业NPW的

### 第 060 页：In Use Start 一复机NPW自动派工

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p060.jpg]]
- 关键 OCR 行：
  - In Use Start 一复机NPW自动派工
  - 主机台派工：
  - 相关RTDreason:Need sequencerun
  - 例：当seasonA派工后，下次派工只可以派monitorB，monitorCD 1.SeasonA
  - 相关RTD reason:Interval time out 3.MonitorC
  - 例：在seasonA作业完成60min后，若monitorB派工，则卡控reason 60min

### 第 061 页：In Use Start- 一复机NPW自动派工

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p061.jpg]]
- 关键 OCR 行：
  - In Use Start- 一复机NPW自动派工
  - 主机台派工：
  - 考虑机台需求多Monitor一起派工（已上线）：
  - 至同一FOUP，同FOUP派工时一起派工
  - 同FOUP内RoutineMonitor派工：
  - 考虑同FOUP内存在RoutineMonitor需求派工（已上线）

### 第 062 页：In UseStart -Season

- 分类：Local 派工规则
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p062.jpg]]
- 关键 OCR 行：
  - 主要流程 机台派工
  - 口 Season触发条件
  - 机台触发派工
  - Recipechange season：机台本次作业产品条件与上一次作业产品条件发生改变时需作业的season
  - Recipeidleseason：机台某一条件在一段时间内未作业过产品时需作业的season

### 第 063 页：In Use Start-Season

- 分类：DSP / RTD / AMA
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p063.jpg]]
- 关键 OCR 行：
  - 口AMA流程图
  - Send alarm Exist season 1.母批筛选

### 第 064 页：In Use Start--Season

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p064.jpg]]
- 关键 OCR 行：
  - 口母批筛选
  - Filterrule
  - Filter item
  - FOUPLocation=In StockerorInOHB Sourcelot所在的carrier必须是lnStocker或nOHB
  - Filterthe lot which available wafer count<control id wafer count Sourcelot中可用wafer数不能小于controlid所需的wafer数
  - Sorting rule

### 第 065 页：In Use Start- -Dummy

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p065.jpg]]
- 关键 OCR 行：
  - 主要流程 机台派工或watchdog Dummy翔断 Dummy准备 Reserve dummy
  - 口Dummy触发条件
  - 机台内任一dummy达到最大使用次数或当前将派工机台内dummy不足

### 第 066 页：In Use Start--ETCHDummy

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p066.jpg]]
- 关键 OCR 行：
  - 口 AMA流程图
  - 1.母批筛选

### 第 067 页：In Use Start--ETCHDummy

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p067.jpg]]
- 关键 OCR 行：
  - 口角 触发条件
  - no other any lot extract status is Wait For Reserve Dummy
  - 母批筛选
  - Filter rule
  - Filter item Description
  - FOUPLocation=ln StockerorInOHB Sourcelot所在的camier必须是InStocker或lnOHB

### 第 068 页：In Use Start--FurnaceDummy

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p068.jpg]]
- 关键 OCR 行：
  - 口AMA流程图
  - 1.母批筛选

### 第 069 页：In Use Start--Dummy

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p069.jpg]]
- 关键 OCR 行：
  - 触发条件
  - no otheranylot extract status is WaitFor ReserveDummy
  - 口母批筛选
  - Filter rule
  - Filter item
  - FOUPLocation=InStockerorInOHB Sourcelot所在的carrier必须是InStocker或lnOHB

### 第 070 页：In Use End

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p070.jpg]]
- 关键 OCR 行：
  - 主要流程
  - reuselot信息 做reuse? recyclelot信息
  - InUseEnd站点做reuse InUseEnd站点做recycle
  - 判断reuse是 发送报警 判断recycle

### 第 071 页：In Use End Reuse

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p071.jpg]]
- 关键 OCR 行：
  - In Use End Reuse
  - Reuse条件（ByWafer）
  - >Filter rule:
  - Filter item Description
  - Switch InUseEnd ="T" 打开AMAInUseEnd功能
  - FOUPLocation= InStocker orIn OHB lot所在的carrier必须是lnStocker或inOHB

### 第 072 页：In Use End Reuse

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p072.jpg]]
- 关键 OCR 行：
  - In Use End Reuse
  - 母批筛选条件
  - Filter item Description
  - 一片达到MaxUsedCount，将无法ReuseMerge回母批
  - FOUPLocation=inStockerorInOHB lot所在的carrier必须是InStocker或InOHB

### 第 073 页：In Use End Reuse 编辑

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p073.jpg]]
- 关键 OCR 行：
  - In Use End Reuse 编辑
  - >Reuse逻辑
  - Reuse条件过
  - 母批条件过滤 不满足条件 Lot自己Reuse ReuseLotD 最小子批
  - 子批Reusemerge回母批 子母批是香在 同一FOUP 子批Transport至母批FOUP
  - Reusemerge回母批

### 第 074 页：In Use End Recycle

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p074.jpg]]
- 关键 OCR 行：
  - In Use End Recycle
  - Recycle条件（Bylot）
  - Filter rule:
  - Filter item Description
  - Switch InUseEnd="T" 打开AMAInUseEnd功能
  - WaferRecycleCount<MaxRecycleCount Wafer未达到最大清洗次数

### 第 075 页：In Use End Recycle

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p075.jpg]]
- 关键 OCR 行：
  - In Use End Recycle
  - 相关Lot筛选条件
  - Filter item Description
  - Subplan like%RECYCLE%' 相关lot去除在RecycleFow中的lot
  - Subplanlike%DOWNGRADE% 相关lot去除在downgrade站点的lot
  - AND PROCESSINGSTATU='Hold 若lot在PreRule中切被Hold住，同时MaxHold

### 第 076 页：In Use EndRecycle

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p076.jpg]]
- 关键 OCR 行：
  - In Use EndRecycle
  - >Recycle逻辑
  - Recycle条件过
  - （同product同 自己Recycle
  - 相关Lot筛选条
  - 子批Transport 至母批FOUP 符合Recycle 相关Lo是合 条件 符合Recycle 相关Lot是否 条件 子批与母批跳至Recycle FIOW第一站（HOLD）

### 第 077 页：In Use End Recycle Must Process

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p077.jpg]]
- 关键 OCR 行：
  - In Use End Recycle Must Process
  - 通过ByProduct配置禁止未过主机台的lotAutoRecycle
  - 1.若lot对应Product的MustProcess列为F’/为空，则无需新增Recycle判断，仍按原AutoRecycle逻
  - 2.对于表ama_npwprodmanage的MustProcess列为 T的Product所对应lot在AutoInuse
  - endRecycle时需新增Recycle判断：
  - 符合其他Recycle条件 Must

### 第 078 页：InUse End 特殊NPW处理方法

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p078.jpg]]
- 关键 OCR 行：
  - InUse End 特殊NPW处理方法
  - INPW处于非正常状态
  - NPWHold暂无法处理：
  - NPW被他部门HOLD，短时间内无法处理，影响同一卡其他Lot Recycle，可以用 LongHoldReasoncodeHold异常Lot
  - NPW前量Fail：
  - NPW前量Fail，BYControlid上线AutoHandleFail功能，自动Reset前量FailLot

### 第 079 页：In UseEnd RecycleCount<=1 NPW处理

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p079.jpg]]
- 关键 OCR 行：
  - In UseEnd RecycleCount<=1 NPW处理
  - 只能使用一次： 有RecycleFLow, 无RecycleFLOw
  - RECYCLEFIOW RECYCLE END
  - RECYCLEEND Reclaim Flow
  - 解决方式：MAXRecycle设定为1，上线lnuseendRecycle功能 解决方式：MAxRecycleCount设定为1，上线inuseend-Recycle
  - RecycleEnd-Reclaim,ReclaimEnd-Reuse功能

### 第 080 页：Recycle End

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p080.jpg]]
- 关键 OCR 行：
  - Recycle End
  - 口主要流程
  - 获取RecycleEnd站点可作业lot列表
  - 获取RecycleEnd站点可作业 reuse lot信息 判断是否可以 做reuse? 获取RecycleEnd站点可作业
  - downgrade/reclaimlot信息
  - Recycle站点做reuse DOWNGRADE Next Step like Next Step like

### 第 081 页：Recycle End Reuse

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p081.jpg]]
- 关键 OCR 行：
  - Recycle End Reuse
  - 口Reuse条件（Bywafer）
  - Filter rule:
  - Filter item Description
  - Lot Extrastatus="WaitForRecycleEnd" Lot自身必须在WaitForRecycleEnd站点
  - Switch RecycleEnd ="T" 打开AMARecycleEnd功能

### 第 082 页：Recycle End Downgrade

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p082.jpg]]
- 关键 OCR 行：
  - Recycle End Downgrade
  - 口Downgrade条件（ByFouP）
  - Filter rule:
  - Filter item Description
  - Lot Extrastatus = "WaitForRecycleEnd" 所有相关Lot必须在WaitForRecycleEnd站点
  - Switch RecycleEnd = "T" 打开AMARecycleEnd功能

### 第 083 页：Auto Reassign(Downgrade)

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p083.jpg]]
- 关键 OCR 行：
  - Auto Reassign(Downgrade)
  - 口主要流程
  - 获取Downgrade站点可作业lot列表
  - 获取Downgrade站点可Reassign
  - Downgrade站点做reassign

### 第 084 页：Auto Reassign(Downgrade)

- 分类：AMHS / 搬送
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p084.jpg]]
- 关键 OCR 行：
  - Auto Reassign(Downgrade)
  - Filter rule:
  - Filter item Description
  - Lot Extrastatus="WaitForDisposal" Lot自身必须在WaitForDisposal（即Downgrade）站点
  - Switch Reassign ="T" 打开AMAReassign功能
  - Mapping info in FabMaintainDownGrade fromproduct&fromstep符合Mapping配置表

### 第 085 页：Auto Reassign(Downgrade)

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p085.jpg]]
- 关键 OCR 行：
  - Auto Reassign(Downgrade)
  - 主要流程：
  - C-the sum of to product current wip all wafers remain available recycle count
  - D=to productofmaxrecycle count
  - Reassignlotpriorityfordowngrade:

### 第 086 页：IMP Monitor

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p086.jpg]]
- 关键 OCR 行：
  - 1.母批筛选

### 第 087 页：THKNPWAuto Handle

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p087.jpg]]
- 关键 OCR 行：
  - THKNPWAuto Handle
  - 当前存在LITHOSIARCTHKWPAWafer必须涂布一层Soc才能发Recycle，但FabRoutineMonitor片数为4或6Pcs，因此导致一卡lot总有1-3PcsWafer无法投出，导致无法Recyle需求在
  - Wafer总数在低于4Pcs时，AMA自动投入固定Controlid的Monitor，作业完成后即能实现自动Recyle
  - RTDConfig中设定Product及其水位，小于水位触发后续分批判断
  - 筛选条件如下： Monitor暂不处理
  - 1.PRODUCTname=RTDConfig.THKNPWLeftAvaCount配置Product 选择需要处理的Wafer

### 第 088 页：口编辑V

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p088.jpg]]
- 关键 OCR 行：
  - 口编辑V
  - DegasMonitor
  - 动画
  - DegasMonitor分批逻辑
  - Copper对于CUB机台MonitorDegas腔只需做同GroupName中任腔，当其中某一腔不可作业时需分批Group号一腔进行作业。MonitorAutolnUse上线自动Monitor只上线同 评论
  - GroupName中任一即可。

### 第 089 页：DIFFMonitor

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p089.jpg]]
- 关键 OCR 行：
  - 作业产品时，需要伴随作业炉管Monitor，根据UI中水位提起分批，提前量测前值，待派工时直接调用
  - AMA.FMLAutolnuseStart Watch dog scan every 5min 无需计算分批时间 Enable即要分批
  - AMA.Furnace Monitor

### 第 090 页：Auto Handle Fail

- 分类：NPW 自动化
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p090.jpg]]
- 关键 OCR 行：
  - 前量Fail的lot会自动Hold给对应PE，通过AMA自动解前量Holdlot且CancelcontrolID，即可达成控片烂账Auto处理。 前量Fail自动处理
  - Release前量Fail的Lot井卡控Lot不可派工 需求ALLReset的 Check前量Failmonitor Lot
  - AMAWatchDog每5分钟扫一次，对于符合条件的Lot自动执行Release动作 FurnaceMonitor还需 卡控同Foup内其他Lot Release前量Fail的Lot并卡控
  - 符合以下卡控Lot卡控派工： Lot不可派工
  - lot上一站点的stephistory，若存在activity=hold，holdtype为EDC，并且存在activity=release,useridAMA，卡控不可派，RTD ReleaseLot

## 06 OverQtime 原因分析

### 第 091 页：OverQtime原因分析

- 分类：QZone / QTime
- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p091.jpg]]
- 关键 OCR 行：
  - OverQtime原因分析
  - 对当前站点长时间未派工的产品Log中直询是否被
  - 明确overqtime时间，站点和 Assign卡控不派工，并对Assign中未预排进行分
  - flow信息，绘制qtimeloop 分析over原因 ，通过各个Assign报表中的Reason及预排的排
  - qtime放货？
  - 进入loop后， over站点机台 是否不可作业？ 当站未按照 卡控下游断线？ 卡控下游产能？ 当站QZone 当站受其他 原因卡控不 加量加测？ Qtime内
