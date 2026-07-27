---
type: dispatch-requirement-note
source_folder: CMPAutoPirun
topic: PM 管控 / 设备保养约束
tags: [自动派工, 需求单, OCR, 需求整理]
---

# CMPAutoPirun - 需求单整理

## 资料概况

- 原始图片目录：[[00.raw-materials/10.sources/images/CMPAutoPirun]]
- OCR 输出目录：[[00.raw-materials/90.processed/dispatch-requirements-ocr/CMPAutoPirun]]
- 图片数量：12
- 初步主题：PM 管控 / 设备保养约束
- 处理状态：已 OCR，已建立初步结构化笔记
- 注意：本笔记基于 OCR 自动识别，关键需求点需回看原图确认。

## 自动识别到的关键信号

- 系统对象：Chamber, EQP, Lot, Machine, Port, Step, Tool
- 派工逻辑：Rule
- 约束条件：Capability, Idle, Loss, PM, QTime, WPH
- 系统接口：AMA, APC, EAP, MES, RTD
- 验证信息：测试, 结果, 需求

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

### 第 001 张：PPT.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/PPT.jpg]]

关键 OCR 行：
- AMA系统根据lot作业条件，机台loading情况进行自动分批Pi-Run，提升效率。
- Q02 项目方案： AMA系统根据Q-timeRisk等指标选定需要Pi-RunLot，分配到Loading最低并且
- 子批A.1作为Pi-Runlot将 AMA自动选择Alot同时分 A1可Run Pi-RunLot E3
- CMPR2RPi-RunLot自动分批功能
- Q01 项目描述：当CMP在堆货的时候，PE手动Pi-Run效率低，客 容易导致lotoverQ-time，现需
- Lifetime充足机台，然后对选定Pi-RunLot进行自动分批，同时将Pi-RunLot
- 信息发送给R2R系统
- LOT EQP
- E1
- E2 没有Q-timelot
- 有Q-timelot
- A.1相关信息发送给R2R系统 A.1

<details>
<summary>展开完整 OCR</summary>

```text
CMPR2RPi-RunLot自动分批功能
Q01 项目描述：当CMP在堆货的时候，PE手动Pi-Run效率低，客 容易导致lotoverQ-time，现需
AMA系统根据lot作业条件，机台loading情况进行自动分批Pi-Run，提升效率。
Q02 项目方案： AMA系统根据Q-timeRisk等指标选定需要Pi-RunLot，分配到Loading最低并且
Lifetime充足机台，然后对选定Pi-RunLot进行自动分批，同时将Pi-RunLot
信息发送给R2R系统
LOT EQP
E1
E2 没有Q-timelot
有Q-timelot
子批A.1作为Pi-Runlot将 AMA自动选择Alot同时分 A1可Run Pi-RunLot E3
A.1相关信息发送给R2R系统 A.1
R2ROn机台
E4
R2ROff机台
R2R
03 项目效益：减少overQ-timelot数量，同时提升机台生产效率3%以上。
商密二级 上海华力
ConfidentialⅡ HLMC
```

</details>

### 第 002 张：Testcase1.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/Testcase1.jpg]]

关键 OCR 行：
- 用户测试 I测
- 测试内容 预期结果 测试日期
- By处理过后的tool name（by到side）从tb machineselfcapa表中串取机台边 成功串取到所有机台边的selfcapability并按
- ity 对应的selfcapability，从R2R表中串取mergestep，qty以及count 此分group，设置groupidx，每个group的 2025/12/4
- 正确拿取初始符合条件的Lot信息 2025/12/4
- ot 获取overq或者超lifetime频度的lot，同selfcapability下多个lot生效时 QTimeWorse和LifeTimeWorse有一个为T的，
- 优先选取除无Qtimelot外Remaing最短的lot，给needpirunflag：2 则赋给该记录needpirunflag为2
- 获取有展路宽需求的lot，需要管控的selefcapability且在原逻辑判断中不存 首先计算QWIP以及LimitWIP，根据公式进行比 2025/12/4
- 在overa风险或超lifetime频度风险的lot，从对应selfcapability选取 较，得出正确的Switch，对于Switch为true
- loading最高的机台（assignedstn）中拿取除无Qtimelot外RemainQ最长的 的，且QTimeWorse和LifeTimeWorse同时为F
- owner own
- picountconfig取最小值

<details>
<summary>展开完整 OCR</summary>

```text
用户测试 I测
测试内容 预期结果 测试日期
owner own
By处理过后的tool name（by到side）从tb machineselfcapa表中串取机台边 成功串取到所有机台边的selfcapability并按
ity 对应的selfcapability，从R2R表中串取mergestep，qty以及count 此分group，设置groupidx，每个group的 2025/12/4
picountconfig取最小值
首先通过sysId串取lot当前的各项信息，筛选lot状态，选取片数大于5片的
lot
正确拿取初始符合条件的Lot信息 2025/12/4
doublecheck，比对CMPLotAssignment表里记录的lot信息是否是实时的，选
取实时信息
邓怀骏
ot 获取overq或者超lifetime频度的lot，同selfcapability下多个lot生效时 QTimeWorse和LifeTimeWorse有一个为T的，
优先选取除无Qtimelot外Remaing最短的lot，给needpirunflag：2 则赋给该记录needpirunflag为2
获取有展路宽需求的lot，需要管控的selefcapability且在原逻辑判断中不存 首先计算QWIP以及LimitWIP，根据公式进行比 2025/12/4
在overa风险或超lifetime频度风险的lot，从对应selfcapability选取 较，得出正确的Switch，对于Switch为true
loading最高的机台（assignedstn）中拿取除无Qtimelot外RemainQ最长的 的，且QTimeWorse和LifeTimeWorse同时为F
lot分子批进行Pirun，给needpirunflag：1 的，赋给该记录needpirunflag为1
```

</details>

### 第 003 张：Testcase2.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/Testcase2.jpg]]

关键 OCR 行：
- 筛选掉不可pi的机台：机况不符合条件的，边上有正在pilot的，pi上该lot
- 天，1天后可再次选取该lot，stn同样不参与循环，直至stnside上不存在 不重复，即已选的机台边不参与接下来的判断。
- 后会超出lifetime频度的。在此基础上选择ReasoncodeCMP里含有APC-JOB 正确选取可pi的机台边
- OFF的。
- t可pi
- 在上述拿取到的机台中选取loading最低的机台作为分批该Lot选定的机台（当 2025/12/4
- 机台loading相同时，选取lifetime频度低的机台）循环选取，每次循环记
- 录lot和对应pi的机台，lot不参与接下来的分子批pirun，时间间隔设置为1 能够正确选取1ot要pi的机台边，并且机台边
- pilot为止。
- 正确分批，保证1ot片数大于要分子批的片数，
- lot 根据R2RIAPC表中配置的分批片数进行分子批pirun 2025/12/4
- 输出componentinfo

<details>
<summary>展开完整 OCR</summary>

```text
筛选掉不可pi的机台：机况不符合条件的，边上有正在pilot的，pi上该lot
后会超出lifetime频度的。在此基础上选择ReasoncodeCMP里含有APC-JOB 正确选取可pi的机台边
OFF的。
t可pi
在上述拿取到的机台中选取loading最低的机台作为分批该Lot选定的机台（当 2025/12/4
机台loading相同时，选取lifetime频度低的机台）循环选取，每次循环记
录lot和对应pi的机台，lot不参与接下来的分子批pirun，时间间隔设置为1 能够正确选取1ot要pi的机台边，并且机台边
天，1天后可再次选取该lot，stn同样不参与循环，直至stnside上不存在 不重复，即已选的机台边不参与接下来的判断。
pilot为止。
正确分批，保证1ot片数大于要分子批的片数，
lot 根据R2RIAPC表中配置的分批片数进行分子批pirun 2025/12/4
输出componentinfo
```

</details>

### 第 004 张：技术文档1.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/技术文档1.jpg]]

关键 OCR 行：
- AMA 详细设计说明书
- CMP R2R AutoPirun
- 版本历史
- 20201201

<details>
<summary>展开完整 OCR</summary>

```text
AMA 详细设计说明书
CMP R2R AutoPirun
版本历史
20201201
```

</details>

### 第 005 张：技术文档2.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/技术文档2.jpg]]

关键 OCR 行：
- 用户需求
- 11 背景
- 12 需求描述
- 样式
- 上海 华力商级
- HuMo confidental
- 目录
- 版本历史
- 详细设计
- 21 UI设计
- 22 功能设计

<details>
<summary>展开完整 OCR</summary>

```text
样式
上海 华力商级
HuMo confidental
目录
版本历史
用户需求
11 背景
12 需求描述
详细设计
21 UI设计
22 功能设计
```

</details>

### 第 006 张：技术文档3.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/技术文档3.jpg]]

关键 OCR 行：
- 1用户需求
- -1.1背景
- 当CaP在堆货的时候，PE 手动Pi-Run效率低，容易导致 lot overO-time，现需AMA
- 系统根据lot作业条件，机台loading情况进行自动分批Pi-Run，提升效率。
- 1.2需求描述
- AMA需求流程图
- AMA End
- 实现功能：AMA 系统根据o-time Risk 等指标选定需要Pi-Run Lot，分配到 Loading
- （一）在AMATigxCOnfi中增加开关，描述如下
- AdDu 正文 标题1 标题2 标题3 标颖4 标额5 标题 副标题
- 样式
- Select Pllot

<details>
<summary>展开完整 OCR</summary>

```text
AdDu 正文 标题1 标题2 标题3 标颖4 标额5 标题 副标题
样式
1用户需求
-1.1背景
当CaP在堆货的时候，PE 手动Pi-Run效率低，容易导致 lot overO-time，现需AMA
系统根据lot作业条件，机台loading情况进行自动分批Pi-Run，提升效率。
1.2需求描述
AMA需求流程图
Select Pllot
And STN
AMA End
R2R
实现功能：AMA 系统根据o-time Risk 等指标选定需要Pi-Run Lot，分配到 Loading
最低并且Lifetime充足机台，然后对选定 Pi-Run Lot 进行自动分批，同时将Pi-Run
Lot 信息发送给 R2R 系统。
2详细设计
2.1UI设计
（一）在AMATigxCOnfi中增加开关，描述如下
Punction NameCMPAutosplitirunlott
SwitchYe
```

</details>

### 第 007 张：技术文档4.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/技术文档4.jpg]]

关键 OCR 行：
- TriggerTimeslot=00:00-23:59-
- （）在RTD.CMP1OWWIP中设置下拉选项：
- 配。Lowwip用来判断原Lowwip逻辑，Highaip用于新增选择Pirunlot判断逻辑。
- PirunLot和STN选取逻辑：
- 无Qtimelot外Remaina最短的lot，给needplinunflaa：2，获取有展路宽需求的lot，需
- 要管控的selefcapability且在原逻辑判断中不存在overe风险或超lifetime频度风险的
- lot，从对应selfcapabilitx选取loading最高的机台中拿取除无Qtimelot外Remaino最
- 选好Lot后首先筛选掉不可pi的机台机况不符合条件的，边上有pilot的，pi上该
- lot后会超出lifetime频度的。在此基础上选择ReasoncodelCuP符合条件的。在上述拿取
- WatchDog定时Call R2R接口逻辑：
- 若用户配置满足，且AMATxiggexsuitch中开关打开，则5分钟执行一次xatchDog，选
- 正文 标题2 标题4 标题5 副标题

<details>
<summary>展开完整 OCR</summary>

```text
正文 标题2 标题4 标题5 副标题
样式
上海华力 华力商海级
HiMdcontidential
TriggerTimeslot=00:00-23:59-
Trigger Count/Time=5+
（）在RTD.CMP1OWWIP中设置下拉选项：
Controltype栏位设置下拉选项，选项内包含Lowwie/Highwi（必填项，不支持模糊匹
配。Lowwip用来判断原Lowwip逻辑，Highaip用于新增选择Pirunlot判断逻辑。
2.2功能设计
PirunLot和STN选取逻辑：
首先通过ssId串取1ot当前的各项信息，筛选1ot状态，选取片数大于5片的1ot。
获取overg或者超lifetime频度的lot，同selfcapabilit下多个lot生效时优先选取除
无Qtimelot外Remaina最短的lot，给needplinunflaa：2，获取有展路宽需求的lot，需
要管控的selefcapability且在原逻辑判断中不存在overe风险或超lifetime频度风险的
lot，从对应selfcapabilitx选取loading最高的机台中拿取除无Qtimelot外Remaino最
长的lot分子批进行Pirun给needpirunflag：1按MAx（nsedpirunflag）优先选取pilot。
选好Lot后首先筛选掉不可pi的机台机况不符合条件的，边上有pilot的，pi上该
lot后会超出lifetime频度的。在此基础上选择ReasoncodelCuP符合条件的。在上述拿取
到的机台中选取loading最低的机台作为分批该Lot选定的机台（当机台loading相同时，
选取1ifetime频度低的机台），循环选取，每次循环记录1ot和对应pi的机台。
WatchDog定时Call R2R接口逻辑：
若用户配置满足，且AMATxiggexsuitch中开关打开，则5分钟执行一次xatchDog，选
取Pilot及机台，并且给Lot找空Eoue，进行物理分批把分出来的子批Lot信息传给R2R
系统。
```

</details>

### 第 008 张：需求单1.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/需求单1.jpg]]

关键 OCR 行：
- UI：RTD.CMPIOWWIP修改
- Capability SelfCapability Ratio Controltype
- Contxoltype：设置下拉选项，选项内包含Lowaip/Highwip（必填项，不支持模糊匹配）Lowip用来判断
- 原Lowwip逻辑，Highwp用于新增选择Piunlou判断逻辑。
- 原有配置Contzoltzpe-认为 Lowwie，原cMP Lowwip逻辑中需求匹配 Controltype-Lowip 的
- 新增AMAJob：CMPAutosplitPirunLot每5分钟触发一次，此Job 开关配置在UI:TriggerConfig中，
- 二、AMA新增选取pirunlot逻辑
- 通过享取CMPASE品最新一版的结果 根据以下逻辑选取需进行Pi的lot并进行自动分批。
- 1、设定需自动分批seltcapability取
- 必填项，不支持模糊匹配必填项，支持模糊匹配必填项，不支持模糊匹配，必填项，不支持模糊匹配
- 新增配置参数：
- HLRS O60..

<details>
<summary>展开完整 OCR</summary>

```text
UI：RTD.CMPIOWWIP修改
Capability SelfCapability Ratio Controltype
必填项，不支持模糊匹配必填项，支持模糊匹配必填项，不支持模糊匹配，必填项，不支持模糊匹配
新增配置参数：
HLRS O60..
华力商密级
HL Cofdental
Contxoltype：设置下拉选项，选项内包含Lowaip/Highwip（必填项，不支持模糊匹配）Lowip用来判断
原Lowwip逻辑，Highwp用于新增选择Piunlou判断逻辑。
原有配置Contzoltzpe-认为 Lowwie，原cMP Lowwip逻辑中需求匹配 Controltype-Lowip 的
配置进行计算lowip界限
新增AMAJob：CMPAutosplitPirunLot每5分钟触发一次，此Job 开关配置在UI:TriggerConfig中，
functionname-ucMPAutoSplitPirunlLotuswitch-时且当前触发的时间符合设定的时间范围，可执行
此Jobo
二、AMA新增选取pirunlot逻辑
通过享取CMPASE品最新一版的结果 根据以下逻辑选取需进行Pi的lot并进行自动分批。
1、设定需自动分批seltcapability取
拿取R2R表中维护的tech prod、stage、count（该elfaapa下分子批的数量）gtx（该lot分子批
的片数等数据信息。
通过专中维护
```

</details>

### 第 009 张：需求单2.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/需求单2.jpg]]

关键 OCR 行：
- selfcapabilitx，对于串取到的selfcapabilitx需进行下述判断，未串取到的selfcapabilix则无需进行后
- 续判断。 注：R2R中 By tech、prod、stagegtx维护，需处理成by selfcapa 的gtx作为符合此条件Lot 的分
- 掌取OM 最新版的信果优配R中seapab要信息 满足以下两种
- CPAasin中已存在overa风险或超lifetime频度风险（该部分判断逻辑follow原CMPLotAssign判断逻
- 辑：64-R-20250901）的1ot给needpirunelag：2，同selfcapabilitx下多个1ot生效时优先选取除无Qtimelot
- 2-2.展路宽需求的10t
- 拿取R2R表中维护的tech prodstage count（该elfcapa 下分子批的数量）gt（该lot分子批
- 的片数等数据信息。
- 通过R2R表中维护tech、prod、stage等数据从表MECCIMtb selfcapa rule未同步成csy中串取
- 批数量，若存在多条Count指标则取小
- 选取Pirun lot
- 情况的任一需进行自动分批piot

<details>
<summary>展开完整 OCR</summary>

```text
拿取R2R表中维护的tech prodstage count（该elfcapa 下分子批的数量）gt（该lot分子批
的片数等数据信息。
通过R2R表中维护tech、prod、stage等数据从表MECCIMtb selfcapa rule未同步成csy中串取
selfcapabilitx，对于串取到的selfcapabilitx需进行下述判断，未串取到的selfcapabilix则无需进行后
续判断。 注：R2R中 By tech、prod、stagegtx维护，需处理成by selfcapa 的gtx作为符合此条件Lot 的分
批数量，若存在多条Count指标则取小
选取Pirun lot
掌取OM 最新版的信果优配R中seapab要信息 满足以下两种
情况的任一需进行自动分批piot
2-.存在Overo&超lifetime风险的lot
CPAasin中已存在overa风险或超lifetime频度风险（该部分判断逻辑follow原CMPLotAssign判断逻
辑：64-R-20250901）的1ot给needpirunelag：2，同selfcapabilitx下多个1ot生效时优先选取除无Qtimelot
外Remaing最短的lot。
HLRS 00603.
2-2.展路宽需求的10t
```

</details>

### 第 010 张：需求单3.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/需求单3.jpg]]

关键 OCR 行：
- 2-2.展路宽需求的1ot+
- 只针对设定有pilot atx对应的selfsapabilitz判断loading是否到达pirun水位，判断逻辑如下
- selfcapabilitix对应的QwIP>LimitWipLimitwip-（SunSidewph*Min（QTimelimit）ratio）C该部逻
- 反之，则管控不生效（Switch=“F·在上述需要管控的selefcapabilitx且在原逻辑判断中不存在oxexa
- 风险或超lifetine频度风险的lot时需求分别从对应selfcapabilitx选取1oading最高的机台中拿取除无
- Qtimelot外Remaing最长的lot分子批进行Pirm 对于此类lot给needpirunflag：1
- 3、选取需求Pirun的机台
- 对以上选取的pilot选取urun 机台时需无视掉LowwipControl且 APclJOB OFF 为PE 需求Pirun 的
- reasoneE 由于cMP机台特性，机台Idle时需要作业season为避免连续pirun产生idleloss，所以需求同
- 3-1.选取机台逻辑如下：
- 选取完需要Pixun的1ot后，通过Assign中结果章取Lot对应的sTN信息，从该Lot可顶排的所有机台
- 台：DReasoncode:APC JOB OFF"@ ReasoncodeAPC JOB OFFAssienOtherSTN “APC JOB OFF

<details>
<summary>展开完整 OCR</summary>

```text
2-2.展路宽需求的1ot+
只针对设定有pilot atx对应的selfsapabilitz判断loading是否到达pirun水位，判断逻辑如下
selfcapabilitix对应的QwIP>LimitWipLimitwip-（SunSidewph*Min（QTimelimit）ratio）C该部逻
辑与CMPLowip管控类似，ratio拿取上述UI中sontroltxRe-Hghwip的值）贝管控生效《Switch=（T）
反之，则管控不生效（Switch=“F·在上述需要管控的selefcapabilitx且在原逻辑判断中不存在oxexa
风险或超lifetine频度风险的lot时需求分别从对应selfcapabilitx选取1oading最高的机台中拿取除无
Qtimelot外Remaing最长的lot分子批进行Pirm 对于此类lot给needpirunflag：1
反之，不满足上述两种情况的lot给needeiunfla：o.needpirunflag2>1>0
置信息需存在mergestep。
3、选取需求Pirun的机台
对以上选取的pilot选取urun 机台时需无视掉LowwipControl且 APclJOB OFF 为PE 需求Pirun 的
reasoneE 由于cMP机台特性，机台Idle时需要作业season为避免连续pirun产生idleloss，所以需求同
个机台只能分一个子批进行piun。
3-1.选取机台逻辑如下：
选取完需要Pixun的1ot后，通过Assign中结果章取Lot对应的sTN信息，从该Lot可顶排的所有机台
中无视掉Reason：LowwipControl，在机台剩余的Reasoncode中存在以下三类情形的机台中进行选取Piun机
台：DReasoncode:APC JOB OFF"@ ReasoncodeAPC JOB OFFAssienOtherSTN “APC JOB OFF
Assienotherside"
在上述章取到的机台中选取 oading最低的机台作为分挑该Lot选定的机台当机台loading相同时，选
取lifetime频度低的机台）对此Lot选定的机台需判断pi该机台后不存在超lifetine频度风险，此外，若
该机台已存在piot则需按照上达逻辑重新选择机台，若未拿取到满足以上条件的机台，则按照上述选取piot
```

</details>

### 第 011 张：需求单4.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/需求单4.jpg]]

关键 OCR 行：
- 取lifetime频度低的机台）。对此Lot选定的机台需判断pi该机台后不存在超lifetime频度风险，此外，若
- 该机台已存在pi1ot则需按照上述逻辑重新选择机台，若未拿取到满足以上条件的机台，则按照上述选取pilot
- 逻辑重新章取新的pilot并选择所需pirun的机台·
- 3-2特殊判断逻辑：
- O超lifetime频度风险：Byequipmentid、dhanberid metertpe串取表mesprod.fabcnpwafercount
- &表mesprod.fweapequipment&表mesprodlxsiteeapusagemetet享取value.afercount等信息，其中metertype
- 所此处需增加special判断：如果边在Ripconfia中ParapterName MPlLowieMachinedouble 对应value
- 3/5- HLRS-0060-3.
- 华力商饭
- HLConfidentialll
- 由于CMP机台边对应类型的Curtent(value）值为对应Chanber对应类型中Current（value)的最大值，所
- 以对于同一个边拿取到的两个腔的cuent(value）需取最大值，例如机台MAB边的当前value值拿取M机台

<details>
<summary>展开完整 OCR</summary>

```text
取lifetime频度低的机台）。对此Lot选定的机台需判断pi该机台后不存在超lifetime频度风险，此外，若
该机台已存在pi1ot则需按照上述逻辑重新选择机台，若未拿取到满足以上条件的机台，则按照上述选取pilot
逻辑重新章取新的pilot并选择所需pirun的机台·
3-2特殊判断逻辑：
3/5- HLRS-0060-3.
华力商饭
HLConfidentialll
O超lifetime频度风险：Byequipmentid、dhanberid metertpe串取表mesprod.fabcnpwafercount
&表mesprod.fweapequipment&表mesprodlxsiteeapusagemetet享取value.afercount等信息，其中metertype
由于CMP机台边对应类型的Curtent(value）值为对应Chanber对应类型中Current（value)的最大值，所
以对于同一个边拿取到的两个腔的cuent(value）需取最大值，例如机台MAB边的当前value值拿取M机台
A边和B边当前值中的最大的值记为MAB边的currentvalue）
拿取Charber对应的wafexcount即为该Chanber对应的最大警戒值max value,机台边对应的最大警戒值
axyalue为边对应Chamber中对应的Min（maxvalue）值
By 边将预排至该机台的 lot 循环计算Nelifetine值，NevKlifetine）待计算 lot 的tx+
Current（yalue），若计算出的Ne（lifetime>该边的Min（max yalue）则认为有超lifetime频度风险
需注意：对于C-CCCCU-C.m，部分边（BCCcUA05/06/09）跑卡货仅需消耗正常边的一半1ifetime值，
所此处需增加special判断：如果边在Ripconfia中ParapterName MPlLowieMachinedouble 对应value
```

</details>

### 第 012 张：需求单5.jpg

![[00.raw-materials/10.sources/images/CMPAutoPirun/需求单5.jpg]]

关键 OCR 行：
- 所以此处需增加 special判断：如果边在RTDConfig中ParanterNane-fCMPILowwipMachinedouble 对应value
- ②机台loading判断逻辑：当前机台下分配的ip数量（OMPLatassisnment中存的totalwip）
- AMAsplit子批逻辑
- 按照以上逻辑选定好1ot后在选定的机台split对应表中配置片数的子批进行Pun，根据匹配信息从R2R
- 表中章取ergestep设置futureneree.直该lotstn不再参与后续pirun逻辑选择·
- 下次Assign时需章取上一版report结果对所分子批井行卡控判断，该子批需在其余所有可作业atn&side
- 以上算一次完整R2RPirun lot选取byselfcapability为groupAMA循环选择Pirun lot进行分批，直至达
- 需注意：对于C-CCCCU-C.T，部分边（BCCCUA05/06/09）跑卡货仅需消耗正常边的半1ifetine值
- 多个边By设定值中，Nelifetime待计算lot的ot/2+Curedtvalue)
- 卡控reason R2RPirunlot 直将该子批 mark 蓝色子批在Rule whatNextMultiChamber cMe rule 和
- Rule WhatNextcMe rule中需renove 掉Reason:LowwieControll
- 到该selfcapa设置的选取上限或已不存在可选择的lot&stn。

<details>
<summary>展开完整 OCR</summary>

```text
需注意：对于C-CCCCU-C.T，部分边（BCCCUA05/06/09）跑卡货仅需消耗正常边的半1ifetine值
所以此处需增加 special判断：如果边在RTDConfig中ParanterNane-fCMPILowwipMachinedouble 对应value
多个边By设定值中，Nelifetime待计算lot的ot/2+Curedtvalue)
②机台loading判断逻辑：当前机台下分配的ip数量（OMPLatassisnment中存的totalwip）
AMAsplit子批逻辑
按照以上逻辑选定好1ot后在选定的机台split对应表中配置片数的子批进行Pun，根据匹配信息从R2R
表中章取ergestep设置futureneree.直该lotstn不再参与后续pirun逻辑选择·
下次Assign时需章取上一版report结果对所分子批井行卡控判断，该子批需在其余所有可作业atn&side
卡控reason R2RPirunlot 直将该子批 mark 蓝色子批在Rule whatNextMultiChamber cMe rule 和
Rule WhatNextcMe rule中需renove 掉Reason:LowwieControll
以上算一次完整R2RPirun lot选取byselfcapability为groupAMA循环选择Pirun lot进行分批，直至达
到该selfcapa设置的选取上限或已不存在可选择的lot&stn。
注意：每个lot仅可被选择一次，下次筛选时需去除该lot，每个机台仅可分一个子批，下次选择可作业机
台时需剔除掉该stn直至该stn不存在pilot才可重新选择
45
HLRS-0060-3
```

</details>
