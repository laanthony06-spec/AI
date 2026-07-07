---
type: dispatch-requirement-note
source_folder: PM_Control
topic: PM 管控 / 设备保养约束
tags: [自动派工, 需求单, OCR, 需求整理]
---

# PM_Control - 需求单整理

## 资料概况

- 原始图片目录：[[00.raw-materials/10.sources/images/PM_Control]]
- OCR 输出目录：[[00.raw-materials/90.processed/dispatch-requirements-ocr/PM_Control]]
- 图片数量：7
- 初步主题：PM 管控 / 设备保养约束
- 处理状态：已 OCR，已建立初步结构化笔记
- 注意：本笔记基于 OCR 自动识别，关键需求点需回看原图确认。

## 自动识别到的关键信号

- 系统对象：Lot, Machine, Step, Tool
- 派工逻辑：Prefer, Qsort, 排序, 派工
- 约束条件：Down, Idle, PM, QTime, QZone
- 系统接口：EAP, MCS, MES, PMS, RTD
- 验证信息：结果, 需求

## 需求理解（初稿）

- 该组资料疑似围绕 PM（Preventive Maintenance）对自动派工的影响展开。
- 需要重点确认：PM 前后是否允许派工、Prefer 是否考虑 PM、PM 造成的机台可用性变化如何进入排序或过滤逻辑。
- 对派工系统的影响：PM 约束通常应进入 Tool 可作业性过滤、Prefer 计算或 WPH / Capacity 评估。

## 待澄清问题

- [ ] 需求目标是什么：提升产能、降低 Cycle Time、减少 OverQtime、降低 WPH Loss，还是提升自动化率？
- [ ] 输入数据来自哪些系统：MES、RTD、AMA、EAP、MCS、APC、PMS？
- [ ] 规则属于 Global Rule、Local Rule，还是排序 / Prefer 逻辑？
- [ ] 需要新增哪些异常原因码或查询页面？
- [ ] 验收标准是什么：测试 Case、前后对比指标、上线影响范围？

## 分页 OCR 摘录

### 第 001 张：PM管控1.jpg

![[00.raw-materials/10.sources/images/PM_Control/PM管控1.jpg]]

关键 OCR 行：
- 申请人员：马婉 功能模块（类别为3时必填）=智能派工系统（RTD/DSP）
- 现优化的PM管控模式，评估Loop内产品分配至其他可做业机台后是否需延期，在Qzone放货时对
- PM/借机机台提前控货。现有模式PM控货以Qsort对比PM Start 时间卡控，借机则以借机时间段进行控
- 因PM只以PMStart控货针对Loop较长则会导致管控较早，对于按时复机回线的瓶颈机台造成产能损
- 失：PM机台Loop中存在Merge 站点，若其中子/母批任产品已流通其他卡控，则会造成无法Merge继续
- 流通至PM后站点：PM延期报表中，若存在同类型多机台同时PM时，对于延期时间长度判断同一Lot在
- 每个延期机台均进行延期，造成PM机台延期时长计算差异化。
- 基于以上待优化情况，需对当前PMQzone管控模式进行重新改善，保证机台PM 前产品正常流通。
- 对于PM按照复机成功率评估按照不同模式管控，其中可正常回线的机台通过时间段的管控模式可更好
- 的管控产品放货情况，风险较高的PM机台则按照当前情况（清空LOOp）较为安全。
- 编号： （此处由信息技术部填写）
- 类别（请在方框内打勾）：口1.软件采购 □2.硬件采购 3.功能开发□4.工程及服务

<details>
<summary>展开完整 OCR</summary>

```text
编号： （此处由信息技术部填写）
类别（请在方框内打勾）：口1.软件采购 □2.硬件采购 3.功能开发□4.工程及服务
申请部门：制造部 系统名称（类别为3时必填）：CIM计算机集成制造系统Fab6
（科）
申请人员：马婉 功能模块（类别为3时必填）=智能派工系统（RTD/DSP）
申请日期：2025-04-07 希望交付期：2025-04-18
项目简介和必要性分析：
现优化的PM管控模式，评估Loop内产品分配至其他可做业机台后是否需延期，在Qzone放货时对
PM/借机机台提前控货。现有模式PM控货以Qsort对比PM Start 时间卡控，借机则以借机时间段进行控
货。
因PM只以PMStart控货针对Loop较长则会导致管控较早，对于按时复机回线的瓶颈机台造成产能损
失：PM机台Loop中存在Merge 站点，若其中子/母批任产品已流通其他卡控，则会造成无法Merge继续
流通至PM后站点：PM延期报表中，若存在同类型多机台同时PM时，对于延期时间长度判断同一Lot在
每个延期机台均进行延期，造成PM机台延期时长计算差异化。
基于以上待优化情况，需对当前PMQzone管控模式进行重新改善，保证机台PM 前产品正常流通。
项目投资方案比较及效果分析：
对于PM按照复机成功率评估按照不同模式管控，其中可正常回线的机台通过时间段的管控模式可更好
的管控产品放货情况，风险较高的PM机台则按照当前情况（清空LOOp）较为安全。
```

</details>

### 第 002 张：PM管控2.jpg

![[00.raw-materials/10.sources/images/PM_Control/PM管控2.jpg]]

关键 OCR 行：
- 需求内容（可添加附件 样式
- PMQzone管控优化
- 现逻辑：PM机台状态为可做业状态，LotQSontPMStart则判定该Lot对应的此机台PMFlag为Y
- 修改逻辑：对于PM机台新增判定指标PMOzoneControl，该指标力Y的情况下考量机台PM时间
- 段和Buffer情况，基于该时间段评估产品可放货情况其中PMBuffer的考量参照原一刀切PM管控方式
- 对于PM时间长度新增Bufer计算，重新预估PMStart&End时间
- 1.1PMQzone 管控中PM Start&End 计算
- 原逻辑中需可做业机台PM时间管控进行优化
- 开关打开时LotSTNList，拿取符合其SINPMControllnfo报表中的MachineIDNew，并判定其机台/腔
- （）对于MachineIDNew的PMStartTime<-当前时间则对应的PMStartTIme取当前时间（此判定考量
- 机台已在设定PM区间段内评估对应的PM周期相应进行延长
- （2）对借机/PM进行不同时间的者量，借机者量借机的时间段，PM考量PM开始时间之后的整个时间长

<details>
<summary>展开完整 OCR</summary>

```text
需求内容（可添加附件 样式
PMQzone管控优化
现逻辑：PM机台状态为可做业状态，LotQSontPMStart则判定该Lot对应的此机台PMFlag为Y
修改逻辑：对于PM机台新增判定指标PMOzoneControl，该指标力Y的情况下考量机台PM时间
段和Buffer情况，基于该时间段评估产品可放货情况其中PMBuffer的考量参照原一刀切PM管控方式
对于PM时间长度新增Bufer计算，重新预估PMStart&End时间
1.1PMQzone 管控中PM Start&End 计算
原逻辑中需可做业机台PM时间管控进行优化
开关打开时LotSTNList，拿取符合其SINPMControllnfo报表中的MachineIDNew，并判定其机台/腔
当前状态情况，如机台/腔为可做业状态（e1Ostate-Standby orProductive，orEgpstateIN(MON-R
BACKUPTD LOTENG LOT,MON ROURECYCLE）只取MaChIneID NeW 对应的机台状态为可做业
状态的进行后续判定。
（）对于MachineIDNew的PMStartTime<-当前时间则对应的PMStartTIme取当前时间（此判定考量
机台已在设定PM区间段内评估对应的PM周期相应进行延长
（2）对借机/PM进行不同时间的者量，借机者量借机的时间段，PM考量PM开始时间之后的整个时间长
度.Qzone中VItual&Existing）STN判定，（PMSTN=NAndPMStartTime-当前时间<-LotQsorn<-PM
Start Time 当前时间+ActualPMTimeDuration And LotSTN-MachinelD New）or（PM STN- Y AndLot
Qsort>-PM StartTime-当前时间And LotSIN-MachinelD New）则Is NewPMAuto Control=T反之
Is NewPMAuto Control-"F 对于PM和借机的处理方式不一致）
现修改逻辑：#
开关打开时LotSTNList，拿取符合其STNPMTimeContrallnfo报表中的MachinelDNew，并判定其机
台/腔当前状态情况，如机台/腔为可做业状态(e10state-StandbyorProductive，orEgpstateIN（MoN-R
BACKUP.TDLOTENGLOT，MON ROU，RECYCLE，只取MachineIDNew对应的机台状态为可做业
状态的进行后续判定。
对借机/PM 进行不同时间的考量，借机或PM 且 PMzoneContro-Y考量时间段，PM且
PMOzoneControl！二Y”考量PM开始时间之后的整个时间长度，
Ozone 中(Virtual&Existing)STN判定，（(PMSTN-"N or(PM STN-AndPMOzoneContro-
STN-Y  And Lot Osort>-PM Stan Time-当前时间 And LotSIN-MachinelDNew)则 Is New PM Auto
Control"T反之 Is New Pm Auto ControlF CPM EndTime-PMStartTime 当前时间+
ActualPMTimeDuration)
其中新增PMSTN=Y机台同修工翔断
```

</details>

### 第 003 张：PM管控3.jpg

![[00.raw-materials/10.sources/images/PM_Control/PM管控3.jpg]]

关键 OCR 行：
- (1)UINameSTNPMTimeControl
- MachineMin PM Time MaxPMTime FMStart Ratio. PM Ernd Reio Mon Ratio Tine Control Sonme Endtime
- MinPMTime：最小PM时长限定（必填项，数值大于等于O）
- MaxPMTime：最大PM时长限定（必填项，数值大于等于O
- PMStartRatio需提前管控StatTime 占PM时长的比例Ce填项，-o）
- PMEndRatio:管控PMEnd占PM时长的比例（必填项，-O）
- 四配符合可做业机台设定中每个需PM机台及对应PM时间长度，拿取其设定Ratio并进行后续判定
- 对于UI无符合PMTimeDuration设定PM StarRatio&PMEndRatio&MonRatio指标则通过设定默认值
- 拿取RTDConfig 中QzoneLoop-Default EMCSPM Start/End Time ratio control.
- U STNPMimeControl 匹配 PM STN-Y的机台并计算机台 PM Time Duration PlanEndTime
- PlanStartTime。匹配关系排序：对于Mchine去掉通配后MAX(Machine）字符长度，MaxUpdatetime进行匹
- 计算修正后的PMStartTime&PMEnd Time：

<details>
<summary>展开完整 OCR</summary>

```text
(1)UINameSTNPMTimeControl
MachineMin PM Time MaxPMTime FMStart Ratio. PM Ernd Reio Mon Ratio Tine Control Sonme Endtime
Machine设定管控站点机台信息必填项，可模糊四配
MinPMTime：最小PM时长限定（必填项，数值大于等于O）
MaxPMTime：最大PM时长限定（必填项，数值大于等于O
PMStartRatio需提前管控StatTime 占PM时长的比例Ce填项，-o）
PMEndRatio:管控PMEnd占PM时长的比例（必填项，-O）
MonRatio：管控Mon+Pirun 时长的比例（必填项，>=o）
TimeControl：该条设定是否受时间的限定（选填项，下拉选择Y/N）
StartTime：管控该条设定生效起始时间（选填项，时间格式）
>EndTime：管控该条设定生效结时间（选填项，时间格式）+
四配符合可做业机台设定中每个需PM机台及对应PM时间长度，拿取其设定Ratio并进行后续判定
对于UI无符合PMTimeDuration设定PM StarRatio&PMEndRatio&MonRatio指标则通过设定默认值
拿取RTDConfig 中QzoneLoop-Default EMCSPM Start/End Time ratio control.
U STNPMimeControl 匹配 PM STN-Y的机台并计算机台 PM Time Duration PlanEndTime
PlanStartTime。匹配关系排序：对于Mchine去掉通配后MAX(Machine）字符长度，MaxUpdatetime进行匹
配各Ratio，取第条。如不满足UI中的匹配则按照默认Ratio。
计算修正后的PMStartTime&PMEnd Time：
IF Machine PMOzoneControl-Y"则 PM Start Time-PlanstartTime-PM Time DurationPM Time
StartRatio 当前时i间,PM End Time-PlanEndTimetPM TimeDuration*PM Time End Ratio+(pirunstdtime
+stdmonpm）*（1+MonRatio）当前时间
ElsePM StartTime-PlanStartTime-当前时间,PM End Time-PlanEndTime+pirunstatimetstdmonpm
当前时间
12PM机台站点前MergeLot子母批判定优化
因现出现PM站点前/后分批作业产品存在Merge站点，对于此分批Lot存在部分流通、部分被管控无
法作业，因PM机台影响Merge导致无法流通，造成Over风险。
OzoneLot分10支跑结果，首先确保同子母批Lot在同一支分支，需在分支前对Lot进行排序尽量保
证LO在同一分支进行后续运算。
OzoneNewPMAuto Control模块新增MergeLot判断优化：判是Lot 是否存在Futune Merge 站点，
对于存在FutureMerge 站点的多Lot 作为同一Group。针对此 Group 的Lot 判定Lot先后顺序：Existing
以当前站点Vinual则以最近的Begin站点作大最优先到达PMMachne的Lot按照选择Lot评估同Group
```

</details>

### 第 004 张：PM管控4.jpg

![[00.raw-materials/10.sources/images/PM_Control/PM管控4.jpg]]

关键 OCR 行：
- 中其他Lot相同站点PM Machine可作业情况Virtual Lot 最近Begin站点若同时存在多LotPMMachine
- ：STNPMControl 优化
- PM延期报表中存在同类型多机台同时PM时，对于延期时间长度判断同一Lot在每个延期机台均进行
- 延期，造成PM机台延期时长计算差异化。需对存在同一Lot同一站点在多机台Over时长延期的计算模块
- 对需进行延期判定的机台，在延期时长判断时者量排除已计算过的同站点OverLot。
- 2025/05/07修改逻辑：
- 因单机机台BWPRFD15连环Qtime（8--36中间小段Loop6H-24H机台处在结束站点--8宿环），机台
- PM时长18H，产线控货提前9H即可，按照Qsort指标导致管控过早，因此修正以CycleTime进行判断。
- （原Qsort比大小判断的地方全都改成Cycletime）
- 作业情况：同Group任一Lot判定机台可作业，其余Lot均判定可作业
- 进行优化一
- 申请部门意见： 申请分管领导意见：

<details>
<summary>展开完整 OCR</summary>

```text
中其他Lot相同站点PM Machine可作业情况Virtual Lot 最近Begin站点若同时存在多LotPMMachine
作业情况：同Group任一Lot判定机台可作业，其余Lot均判定可作业
：STNPMControl 优化
PM延期报表中存在同类型多机台同时PM时，对于延期时间长度判断同一Lot在每个延期机台均进行
延期，造成PM机台延期时长计算差异化。需对存在同一Lot同一站点在多机台Over时长延期的计算模块
进行优化一
对需进行延期判定的机台，在延期时长判断时者量排除已计算过的同站点OverLot。
2025/05/07修改逻辑：
因单机机台BWPRFD15连环Qtime（8--36中间小段Loop6H-24H机台处在结束站点--8宿环），机台
PM时长18H，产线控货提前9H即可，按照Qsort指标导致管控过早，因此修正以CycleTime进行判断。
（原Qsort比大小判断的地方全都改成Cycletime）
申请部门意见： 申请分管领导意见：
日期：
相关部门意见： 相关部份分管领导意见：
日期： 日期
信息技术部意见： 信息技术部阶管领导意见：
日期： 日期
附件名称：
```

</details>

### 第 005 张：Prefer考量PM管控1.jpg

![[00.raw-materials/10.sources/images/PM_Control/Prefer考量PM管控1.jpg]]

关键 OCR 行：
- 目前MFGPrefer/断线场景判断对厂可作业机台时未考量PM管控，导致LOT去对厂后可能存在无法作
- 业也不能回原厂的情况，或LOT在被判断到对厂作业后因机台PM管控而卡控Qzone无法作业，因此需在
- MFGPrefer/断线场景对厂可作业机台检查逻辑中增加PM管控的判定。
- 在MFGPrefer/断线场景对厂可作业机台检查逻辑中增加PM管控的判定。
- 降低因对厂机台PM管控导致lot无法作业最终QverOtime的风险
- 需求内容（可添加附件）：
- 方案逻辑：#
- MFGPrefex/断线场景新增逻辑
- 在MFGPrefer和断线场景的 TargetFabCondition判断中考量机台PM管控，可FollowQzone PM管控判
- MFGPrefer/DownTime场景LotFetchStep时计算Lot到每一站的AnriveTime(每一站CT/PT累加，Process
- 2.获取机台PM管控信息+
- 在Lot获取到对厂机台后，判断机台的PM管控信息

<details>
<summary>展开完整 OCR</summary>

```text
项目简介和必要性分析：
目前MFGPrefer/断线场景判断对厂可作业机台时未考量PM管控，导致LOT去对厂后可能存在无法作
业也不能回原厂的情况，或LOT在被判断到对厂作业后因机台PM管控而卡控Qzone无法作业，因此需在
MFGPrefer/断线场景对厂可作业机台检查逻辑中增加PM管控的判定。
项目投资方案比较及效果分析：
改善方案：
在MFGPrefer/断线场景对厂可作业机台检查逻辑中增加PM管控的判定。
效果分析
降低因对厂机台PM管控导致lot无法作业最终QverOtime的风险
需求内容（可添加附件）：
方案逻辑：#
MFGPrefex/断线场景新增逻辑
在MFGPrefer和断线场景的 TargetFabCondition判断中考量机台PM管控，可FollowQzone PM管控判
断。先
1.1ot到站时间计算
MFGPrefer/DownTime场景LotFetchStep时计算Lot到每一站的AnriveTime(每一站CT/PT累加，Process
站点用CycleTime，非Process站点用ProcessTime）.记作CumulatedcycleTimeToStep。
2.获取机台PM管控信息+
在Lot获取到对厂机台后，判断机台的PM管控信息
2.1PreControlFlag获取+
将Lot的对厂机台拆分，记为Machine整机或腔），取Machine前八位，记作MainTool。
FabEgpEquipmentCaExt中串取PreControlFlag。 从表FabEapEquipmentCaExt获取PreControlFlag栏位，分别用Machine 和 MainTool从
2.2IsPreControlException获取
从Ul-PreControlException 中获取MachineName QOtimeDuration(h）、Operation、IsSafetyStepNeedFollow栏
位分别用Machine和MainTool判断FlagIsPreControlException;
3.机台PM管控判断
判断机台是否处于PM/借机管控区间。
3.1获取机台PM/借机时间
By TargetFab从 STNPMTimeControllnfo 中获取 MachineID New Planstarttime Planendtime PMFlag
StdMonPM、PirunStdTimePMOzoneControl栏位。
筛选出机台状态良好的 MachineIDNew（StnstateFlag-T），即满足：elOstate=Standby or Productive，or
EgpstateIN(MON-R,BACKUPTD LOTENG LOT,MON ROU,RECYCLE)。
```

</details>

### 第 006 张：Prefer考量PM管控2.jpg

![[00.raw-materials/10.sources/images/PM_Control/Prefer考量PM管控2.jpg]]

关键 OCR 行：
- 分别用 Machine 和 MainTool 从 SINPMTimeControllnfo 串取 Planstarttime Planendtime.PMFlag
- StdMonPM、PirunStdTime PMQzoneControl信息，并计算 PMTimeDuration PMStratTime.PMEndTime.
- PMTimeDuratron-Planendtime-Planstarttimet
- PMStratTime-Planstarttume-SEnd.
- PMEndTime-Planendtuime-SEnd-
- 3.2机台PM/借机管控判断-
- 3.2.1更新PMStratTime/PMEndTime
- 若机台 PMOzoneControl-Y，则从 STNPMTimeComfigCfg 中匹配获取 PMStratRatio、PMEndRatio
- MonRatio.未匹配上从RTDConfigQzoneLoopDefaultEMCS PM Star/End Timeratio control获取默认值，
- 并更新PMStratTime和PMEndTime·
- PMSuatTime-PMStratTime-PMTimeDuration*PMStratRatio-
- PMEndTime-PMEndTime +PMTimeDuration*PMEndRatio+(StdMonPM-PirunStdTime)'(l+MonRatuo)

<details>
<summary>展开完整 OCR</summary>

```text
分别用 Machine 和 MainTool 从 SINPMTimeControllnfo 串取 Planstarttime Planendtime.PMFlag
StdMonPM、PirunStdTime PMQzoneControl信息，并计算 PMTimeDuration PMStratTime.PMEndTime.
PMTimeDuratron-Planendtime-Planstarttimet
PMStratTime-Planstarttume-SEnd.
PMEndTime-Planendtuime-SEnd-
3.2机台PM/借机管控判断-
3.2.1更新PMStratTime/PMEndTime
筛选出有Planstarttime的Machine/MainTool,
若机台 PMOzoneControl-Y，则从 STNPMTimeComfigCfg 中匹配获取 PMStratRatio、PMEndRatio
MonRatio.未匹配上从RTDConfigQzoneLoopDefaultEMCS PM Star/End Timeratio control获取默认值，
并更新PMStratTime和PMEndTime·
PMSuatTime-PMStratTime-PMTimeDuration*PMStratRatio-
PMEndTime-PMEndTime +PMTimeDuration*PMEndRatio+(StdMonPM-PirunStdTime)'(l+MonRatuo)
否则不更新PMStratTime和PMEndTime。
32.1判断机台是否处于PM借机时间段，
对借机PM 进行不同时间的考量，借机或（PM 且 PMOzoneControl-Y）考量时间段，PM 且
PMOzoneControl！-Y考量PM开始时间之后的整个时间长度。
PMFlag-T且(PMQzoneControl！-Y且CumulatedcycleTimeToStep-PMStratTime)或PMQzoneControl
-Y且CumulatedcycleTimeToStep-PMStratTimeCumulatedcycleTimeToStep-PMEndTime))-
PMFlag-F且CumulatedcycleTimeToStepPMStratTime 且CumulatedcycleTimeToStep<PMEndTime)
）且StnstateFlag-T时
认为机台处于在管控区间段，给 Elag IsNewPMAutoControlSTN-T，Machine 和 MainTool任意存在
IaNewPMAutoControlSIN-T,贝为Machine 的IsNewPMAutoControlsTN-T
3.3TargetFabCondition增加判断
IsNePMAutoControlSTN-T则认力机台不可作业，去除机台，反之保留
申请部门意见， 中请部门分管领导意见：
日期：
相关部门意见： 管领导意贝
```

</details>

### 第 007 张：STNPMTimeControl内容示例.jpg

![[00.raw-materials/10.sources/images/PM_Control/STNPMTimeControl内容示例.jpg]]

关键 OCR 行：
- GroupKey MACHINEID New PLANSTARTIIME PLANENDTIME ActualPMTimeDuration NewPMStartTime STNSTATE CreateTimrUpdateTirPMFag STDMONPM PIRUNSTDTIME PMOZONECONTROL
- 3BOCCWA02 06/24/2026154959 06/25/20260149.59 13/06/24/20261549:59 MONPM 06/24/20220260624 TRUE ON
- 24BEOXET40A 29BEPYEC36A 23BEOXET31F 25BEOXET49_B 26BEOXET51E 27/BEOXET52E 28BEOXET53_B 12BEMTEL09 15BEMTEL17.A 21BEOXET16_B 13BEMTEL09C 16BEMTEL18B 18BEOXEC05.A 19BEOXEL37A 20BEOXET13E 22BEOXET31B 14BEMTEL09D 17BEMTEL26A 10BEBVEL01 11BEBVEL01A 9BDASNT20 6BCCCWE08.B 8BDASNK10 4BCCCWA03 5BCCCWA09 BCCOXA12 06/23/202609:00:00 06/24/202610:00:00 06/24/202610:00:00 06/24/202610:00:00 06/23/202610:00:00 06/23/202610:00:00 06/24/202608:00:00 06/23/202613:00:00 06/24/202609:00:00 06/24/202609:00:00 06/24/202610:00:00 06/23/202609.18:42 06/24/202609.29:30 06/23/202609:00:00 06/24/202610:30:00 06/23/202609:00:00 06/24/20261146:00 03/20/2028084546 06/24/202611-1052 06/24/20261000:00 06/24/202610:00:00 06/24/202602:00:00 06/24/202610:00:00 06/24/202608:0000 06/24/20261114.50 06/24/202607:13:01 06/24/20260100:00 06/24/20260100:00 06/25/20260000:00 06/25/202602:00:00 06/24/202602:00:00 06/24/20260200:00 06/24/20262200:00 06/25/202613:00:00 06/25/202601:00:00 06/25/202601:00:00 06/25/202602:0000 06/24/2026011842 06/25/20260129:30 06/24/202601:00:00 06/25/202602:3000 06/26/20260200:00 06/25/202600:00:00 06/24/202618.00:00 06/24/202620:00:00 06/25/202602:00:00 06/25/202602:00:00 06/24/20261646:00 06/24/2026165552 06/24/20262213:01 06/24/20261659:50 03/20/202814:3046 10.7506/24/2026111450 11.7506/24/2026111052 9.2503/20/2028084546 9.506/24/2026114600 2206/24/2026071301 1306/24/202610:00.00 6106/24/20260200:00 1206/24/202610.00.00 3206/24/20261000.00 52.06/24/202610:00:00 6406/23/202613:0000 5606/23/20260900.00 2406/24/2026100000 3206/24/202610:00.00 4806/23/202610.00:00 5206/23/20261000:00 2206/24/202608:00.00 5206/24/20261003.24 3606/24/202608:00:00 5206/24/202609.0000 4406/24/202610:00.00 4406/23/2026091842 4406/24/202609:2930 5206/23/2026090000 3806/24/202610:30:00 5206/23/20260900:00 RUN RUN RUN PM IDLE DOWN MONDOWN PM MONDOWN PM PM PM WAIT PE PM WAIT PE PM MONDOWN PM PM IDLE MONPM WAIT PE PM MONDOWN MON PM WAIT EE 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 FALSE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE 35 45 10 28 28 20 20 20 28 16 15N 15N OY 12N ON ON ON ON 8N 8N 8N 8N 4N 8N 8Y 8N 8N 8N 8Y 8Y 8Y 8N 8N 8N
- STNPMTimeControllnfo
- 1ATHKOS01 B 06/21/202616:00:00 06/24/202616:00:00 8606/21/202616:00:00 MONDOWN 06/24/20220260624 TRUE OY
- 2BOCCUE11 D 06/24/20261332:26 06/24/202618:0226 806/24/202613.3226 RUN 06/24/20220260624 TRUE 25

<details>
<summary>展开完整 OCR</summary>

```text
GroupKey MACHINEID New PLANSTARTIIME PLANENDTIME ActualPMTimeDuration NewPMStartTime STNSTATE CreateTimrUpdateTirPMFag STDMONPM PIRUNSTDTIME PMOZONECONTROL
1ATHKOS01 B 06/21/202616:00:00 06/24/202616:00:00 8606/21/202616:00:00 MONDOWN 06/24/20220260624 TRUE OY
2BOCCUE11 D 06/24/20261332:26 06/24/202618:0226 806/24/202613.3226 RUN 06/24/20220260624 TRUE 25
3BOCCWA02 06/24/2026154959 06/25/20260149.59 13/06/24/20261549:59 MONPM 06/24/20220260624 TRUE ON
24BEOXET40A 29BEPYEC36A 23BEOXET31F 25BEOXET49_B 26BEOXET51E 27/BEOXET52E 28BEOXET53_B 12BEMTEL09 15BEMTEL17.A 21BEOXET16_B 13BEMTEL09C 16BEMTEL18B 18BEOXEC05.A 19BEOXEL37A 20BEOXET13E 22BEOXET31B 14BEMTEL09D 17BEMTEL26A 10BEBVEL01 11BEBVEL01A 9BDASNT20 6BCCCWE08.B 8BDASNK10 4BCCCWA03 5BCCCWA09 BCCOXA12 06/23/202609:00:00 06/24/202610:00:00 06/24/202610:00:00 06/24/202610:00:00 06/23/202610:00:00 06/23/202610:00:00 06/24/202608:00:00 06/23/202613:00:00 06/24/202609:00:00 06/24/202609:00:00 06/24/202610:00:00 06/23/202609.18:42 06/24/202609.29:30 06/23/202609:00:00 06/24/202610:30:00 06/23/202609:00:00 06/24/20261146:00 03/20/2028084546 06/24/202611-1052 06/24/20261000:00 06/24/202610:00:00 06/24/202602:00:00 06/24/202610:00:00 06/24/202608:0000 06/24/20261114.50 06/24/202607:13:01 06/24/20260100:00 06/24/20260100:00 06/25/20260000:00 06/25/202602:00:00 06/24/202602:00:00 06/24/20260200:00 06/24/20262200:00 06/25/202613:00:00 06/25/202601:00:00 06/25/202601:00:00 06/25/202602:0000 06/24/2026011842 06/25/20260129:30 06/24/202601:00:00 06/25/202602:3000 06/26/20260200:00 06/25/202600:00:00 06/24/202618.00:00 06/24/202620:00:00 06/25/202602:00:00 06/25/202602:00:00 06/24/20261646:00 06/24/2026165552 06/24/20262213:01 06/24/20261659:50 03/20/202814:3046 10.7506/24/2026111450 11.7506/24/2026111052 9.2503/20/2028084546 9.506/24/2026114600 2206/24/2026071301 1306/24/202610:00.00 6106/24/20260200:00 1206/24/202610.00.00 3206/24/20261000.00 52.06/24/202610:00:00 6406/23/202613:0000 5606/23/20260900.00 2406/24/2026100000 3206/24/202610:00.00 4806/23/202610.00:00 5206/23/20261000:00 2206/24/202608:00.00 5206/24/20261003.24 3606/24/202608:00:00 5206/24/202609.0000 4406/24/202610:00.00 4406/23/2026091842 4406/24/202609:2930 5206/23/2026090000 3806/24/202610:30:00 5206/23/20260900:00 RUN RUN RUN PM IDLE DOWN MONDOWN PM MONDOWN PM PM PM WAIT PE PM WAIT PE PM MONDOWN PM PM IDLE MONPM WAIT PE PM MONDOWN MON PM WAIT EE 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 06/24/20220260624 FALSE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE 35 45 10 28 28 20 20 20 28 16 15N 15N OY 12N ON ON ON ON 8N 8N 8N 8N 4N 8N 8Y 8N 8N 8N 8Y 8Y 8Y 8N 8N 8N
STNPMTimeControllnfo
```

</details>
