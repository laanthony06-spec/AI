---
type: dispatch-requirement-note
source_folder: TestCase_SOP/TestCase示例
topic: TestCase / SOP / 验证规范
tags: [自动派工, 需求单, OCR, 需求整理]
---

# TestCase_SOP/TestCase示例 - 需求单整理

## 资料概况

- 原始图片目录：[[00.raw-materials/10.sources/images/TestCase_SOP/TestCase示例]]
- OCR 输出目录：[[00.raw-materials/90.processed/dispatch-requirements-ocr/TestCase_SOP__TestCase示例]]
- 图片数量：5
- 初步主题：TestCase / SOP / 验证规范
- 处理状态：已 OCR，已建立初步结构化笔记
- 注意：本笔记基于 OCR 自动识别，关键需求点需回看原图确认。

## 自动识别到的关键信号

- 系统对象：EQP, FOUP, Lot, Port
- 派工逻辑：Rule, Sorting
- 约束条件：Capability
- 系统接口：AMA, MES, RTD
- 验证信息：Case, Test, 测试, 结果, 需求

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

### 第 001 张：case1.jpg

![[00.raw-materials/10.sources/images/TestCase_SOP/TestCase示例/case1.jpg]]

关键 OCR 行：
- No 所尾（Local/central） Repor/Rale/AMA) Arex(功配换快 适猫变动内容 类别（正尚/方向/特殊符号处理） 测试结果 则试日期
- carriarcontaignsall+hite
- (Foup内全然总学trantfe购 Pass 2026/4/2
- intarniercontancnsall=Falie (Foup内感有营装hransfer又有 Puss 2026/4/2
- 有需ktanstelot?
- Pass 2026/4/2
- QUOGlobaiPnETE Pass 2026/4/2
- 正间 CutaGlobaiRani 2026/42
- 202642
- QUsorting(QUo/1/2/3/categon) Pa 2125/42
- Cu2aGletaiRaE
- 反网 2025/4/2

<details>
<summary>展开完整 OCR</summary>

```text
No 所尾（Local/central） Repor/Rale/AMA) Arex(功配换快 适猫变动内容 类别（正尚/方向/特殊符号处理） 测试结果 则试日期
carriarcontaignsall+hite
(Foup内全然总学trantfe购 Pass 2026/4/2
intarniercontancnsall=Falie (Foup内感有营装hransfer又有 Puss 2026/4/2
有需ktanstelot?
Pass 2026/4/2
QUOGlobaiPnETE Pass 2026/4/2
正间 CutaGlobaiRani 2026/42
202642
QUsorting(QUo/1/2/3/categon) Pa 2125/42
Cu2aGletaiRaE
反网 2025/4/2
正间 2026/4/2
qUSaGobaiRaniaR 202542
CUCategory
20254/2
Keytot CeytotaGlobalRankts 212542
202542
SubLot SublataGlobalRanknee
15
正间 202542
Rework Lot 2026/42
200542
RCLat
202542
IintemalPn ntemalPnadlobaiRanist 201254/2
WaitTume WaitimeaGbaRanis 22642
2025/4/2
STRMSTRPHOr 2025/4/2
2025/472
Rusih Lor 202542
2026/42
TarpeRinitb 2026/4/2
Sheet2
```

</details>

### 第 002 张：case2.jpg

![[00.raw-materials/10.sources/images/TestCase_SOP/TestCase示例/case2.jpg]]

关键 OCR 行：
- (Local/central) 所属 Report/Rule/AMA) Area(功能模块 涉及Iacro/共通模块 逻辑变动内容 类别（正向/方 向/特殊符号处 理） 测试内容 1增加四列栏位：N2OHB临界值（N2OHBUseRatio）N2STK临界值 （N2STKUseRatio）SpecialN2OHB临界值（SpecialN2OHBRatio) 测试情景 特殊处理当不配置时给个默认值，不会出现无 预期结果 测试结 Pass/Fall 测试日 XXXX owner 测试
- 特殊符号处理 UlWhereNext修改栏位 SpecialN2STK临界值（SpecialN2STKRatio）null值测试.从UI拿取配 法比较情况，可正确从UI中拿取配置信息 Pass/Fail Pass/Fail XXXX XXXX
- 2.存储位status（表mesprod.fweqpcurrentstate拿取status栏位） Pass/Fail XXXX
- 3.OHB、STK存储位类型判断，获得机台附近STKOHB以及所在 location判断
- 4.判断capabilty状态：只取对应的开关打开的Capability（lsengenable CapabilityName Pass/Fail XXXX
- 当EqptypeinOHBP lotOHB/STK判断逻辑验证 STKP则为XCDAIsXCDAPurgeOHB/ （USEDTargetFab）计算实时的loading
- 正向 获取两厂所有的机台相关信息 Eqptypein OHBN IsN2PurgeSTK. STKN则为 reticle存储位以及是否overloading U中拿取各种存储位的位置信息，判断是否为
- Normal(isNormaloHB/IsNormalSTK) 3.成功拿到状态正带的capability
- 6.overloading判定修改 4.overloading判断，可以计算report时间差
- 拿到参数requesteddeviceid然后去重计数得到的结果即report结果计算 Rule里重新计算的，可得到实时指令数量
- 后还需要去对厂储位的数量个数） 5非Reticle储位状态判断，成功拿到符合条
- 在原基础上塔加了USEDTargetFab(UESDTargetFab是又从fablotcaext 拿到参数requesteddeviceid然后去重计数得到的结果，即report结果计算 Pass/Fail XXXX

<details>
<summary>展开完整 OCR</summary>

```text
(Local/central) 所属 Report/Rule/AMA) Area(功能模块 涉及Iacro/共通模块 逻辑变动内容 类别（正向/方 向/特殊符号处 理） 测试内容 1增加四列栏位：N2OHB临界值（N2OHBUseRatio）N2STK临界值 （N2STKUseRatio）SpecialN2OHB临界值（SpecialN2OHBRatio) 测试情景 特殊处理当不配置时给个默认值，不会出现无 预期结果 测试结 Pass/Fall 测试日 XXXX owner 测试
特殊符号处理 UlWhereNext修改栏位 SpecialN2STK临界值（SpecialN2STKRatio）null值测试.从UI拿取配 法比较情况，可正确从UI中拿取配置信息 Pass/Fail Pass/Fail XXXX XXXX
正向 存储位loading公式 1.利用率公式验证：储位loading公式 -(usedcapacity+used+USEDTargetFab/(availcapacity+usedcapacity) 1利用率loading公式更新！考虑到了 (systime-creattime）内的transfer数量 （USEDTargetFab）计算实时的loading Pass/Fall Pass/Fail Pass/Fail XXXX
1.OHB/STKname以及位置与利用率ratio数据验证 Pass/ail XXXX
2.存储位status（表mesprod.fweqpcurrentstate拿取status栏位） Pass/Fail XXXX
3.OHB、STK存储位类型判断，获得机台附近STKOHB以及所在 location判断
Pass/Fail XXXX
4.判断capabilty状态：只取对应的开关打开的Capability（lsengenable CapabilityName Pass/Fail XXXX
T"andisptenable) 1利用率loading公式更新，考虑到了
5.区分STK为LOTSTK还是ReticleSTK (systime-creattime)内的transfer数量
当EqptypeinOHBP lotOHB/STK判断逻辑验证 STKP则为XCDAIsXCDAPurgeOHB/ （USEDTargetFab）计算实时的loading
EqptypeinCOHBPN' IsXCDAPurgeSTK) STKPN则为N20SN2PUrgeOHB 2.得到两厂所有OHB/STK的利用率，得到两厂 所有机台以及Defaulstk等信息，并能正确从 Pass/Fail XXXX
正向 获取两厂所有的机台相关信息 Eqptypein OHBN IsN2PurgeSTK. STKN则为 reticle存储位以及是否overloading U中拿取各种存储位的位置信息，判断是否为
Normal(isNormaloHB/IsNormalSTK) 3.成功拿到状态正带的capability
6.overloading判定修改 4.overloading判断，可以计算report时间差
无orderlimit则overloading-F 5min内自的地又接受指令的数量，
USED+USEDTargetFab+CurDeviceCountOrderLimit-T 在原基础上增加了USEDTargetFabUESDTargetFab是又从fablotcaext UESDTargetFab是在report计算出后又在 Pass/Fail XXXX
拿到参数requesteddeviceid然后去重计数得到的结果即report结果计算 Rule里重新计算的，可得到实时指令数量
后还需要去对厂储位的数量个数） 5非Reticle储位状态判断，成功拿到符合条
7.overloading判定修改 件的储位，并且标志位isAvailableCheck=T
无orderlimit则overloading=F
USED+USED TargetFab+CurDeviceCount-OrderLimit-T
在原基础上塔加了USEDTargetFab(UESDTargetFab是又从fablotcaext 拿到参数requesteddeviceid然后去重计数得到的结果，即report结果计算 Pass/Fail XXXX
后还需要去对厂储位的数量个数）
正向 MES-RTD通讯测试 2与MES联调测试使用MESCallRTD得到回复 3.RTD传参检查，通讯栏位传参检查 1.打MES接口，看是否能正常通讯 可以正确接受MES传参，正常进行通讯 Pass/Fall Pass/Fail XXXX XXXX
1.选择存储位时要考虑WereNextsTkConstrain中csn逻辑，按照Trackable Pass/Fall
正向 和Non-Trackable优先选择配置非黑名单的存储位 成功从UI中拿取信息，根据U配置的黑名单 将黑名单的OHB和STK都加上对应的flag。选 Pass/Fail XXXX
若未考虑CSN逻辑，那么可以选到黑名单的目的地 取目的地时去除黑名单目的地 不从UI拿取Csn配置，自的地选择可以选择到
反向
黑名单目的地
成功从UIWhereNextXCDA基十FOUP身
上配置栏位SPECIALPURGEFLAG
SORTINGMODECARRIERTYPE
CARRIERMODELNUMBERSTATE
CREATETIME STARTCREATETIME END
正向 空FOUP若符合Ul:wherenextXCDA配置，是否搬进XCDApurge储位 FUNCTIONMODE判断逻辑）确定空FOUP是 否满足配置，空FOUP类型满足UI配置时，代
表有purge需求，根据eqptype确认搬送目的 Pass/Fail XXXX
centralwherenextTestcase 地类型进行搬送
```

</details>

### 第 003 张：case3.jpg

![[00.raw-materials/10.sources/images/TestCase_SOP/TestCase示例/case3.jpg]]

关键 OCR 行：
- (Local/central) 所属 Report/Rule/AMA) Area功能模块 涉及Iacro/共通模块 逻辑变动内容 类别（正向/方 向/特殊符号处 特殊符号处理 理） Ul:WhereNext修改栏位 测试内容 SpecialN2STK临界值（SpecialN2STKRatio），null值测试，从U拿取配 1.增加四列栏位，N2OHB临界值（N2OHBUseRatio）N2STK临界值 （N2STKUseRatio）SpecialN2OHB临界值（SpecialN2OHBRatio） 测试情景 法比较情况：可正确从UI中拿取配置信息 待殊处理当不配置时给个默认值，不会出现无 预期结果 测试结 Pass/Fail Pass/Fail Pass/Fail 测试日 XXX XXXX XX owner 测试
- 2.存储位status（表mesprod.fweqpcurrentstate拿取status栏位） 1.OHB/STKname以及位置与利用率ratio数据验证 Pass/Fail XXX
- location判断 3.OHB、STK存储位类型判断，获得机台附近STK,OHB以及所在 Pas5/Fail X0X
- CapabilityName 4.判断capabilty状态：只取对应的开关打开的Capability（lsengenable= Pass/Fail XXX
- lotOHB/STK判断逻辑验证： 当Eqptypein （OHBPSTKP）则为XCDA（IsXCDAPurgeOHB/ （USEDTargetFab）计算实时的loading
- IsN2PurgeSTK), U中拿取各种存储位的位登信息，判断是否为
- 正向 获取两厂所有的机台相关信息 Eqptypein（OHBN"STKN）则为 Normal(lsNormalOHB/IsNormalSTK): reticle存储位以及是否overloading 3.成功拿到状态正常的capability
- 6.overloading判定修改： 4.overloading判断，可以计算repor时间差
- USED+USED_TargetFab+CurDeviceCount>=OrderLimit=T 无orderlimit则overloading=F 在原基础上增加了USEDTargetFab（UESDTargetFab是又从fablotcaext 5min内目的地又接受指令的数量 UESDTargetFab是在report计算出后又在 Pass/Fail XOCCX
- 拿到参数requesteddeviceid然后去重计数得到的结果，即report结果计算 Rule里重新计算的，可得到实时指令教量 5.非Reticle储位优态判断，成功拿到待合条
- 拿到参数requesteddeviceid然后去重计数得到的结果，即report结果计算
- 1打MES接口，看是否能正常通讯 Pass/Fail

<details>
<summary>展开完整 OCR</summary>

```text
No
(Local/central) 所属 Report/Rule/AMA) Area功能模块 涉及Iacro/共通模块 逻辑变动内容 类别（正向/方 向/特殊符号处 特殊符号处理 理） Ul:WhereNext修改栏位 测试内容 SpecialN2STK临界值（SpecialN2STKRatio），null值测试，从U拿取配 1.增加四列栏位，N2OHB临界值（N2OHBUseRatio）N2STK临界值 （N2STKUseRatio）SpecialN2OHB临界值（SpecialN2OHBRatio） 测试情景 法比较情况：可正确从UI中拿取配置信息 待殊处理当不配置时给个默认值，不会出现无 预期结果 测试结 Pass/Fail Pass/Fail Pass/Fail 测试日 XXX XXXX XX owner 测试
1.利用率loading公式更新，考虑到了 Pass/Fail XXXX
正向 存储位loading公式 1.利用率公式验证：储位loading公式 =(usedcapacity+used+USED_TargetFab/(availcapacity+usedcapacity) (systime-creattime）内的transfer教量 （USEDTargetFab）计算实时的loading Pass/Fail Pass/Fail XX XXXX
2.存储位status（表mesprod.fweqpcurrentstate拿取status栏位） 1.OHB/STKname以及位置与利用率ratio数据验证 Pass/Fail XXX
Pass/Fail XXX
location判断 3.OHB、STK存储位类型判断，获得机台附近STK,OHB以及所在 Pas5/Fail X0X
CapabilityName 4.判断capabilty状态：只取对应的开关打开的Capability（lsengenable= Pass/Fail XXX
5.区分STK为LOTSTK还是ReticleSTK： "Tandisptenable"T) 1利用率loading公式更新，考虑到了 (systime-creattime）内的transfer教显
lotOHB/STK判断逻辑验证： 当Eqptypein （OHBPSTKP）则为XCDA（IsXCDAPurgeOHB/ （USEDTargetFab）计算实时的loading
Eqptypein（OHBPN，STKPN）则为N2(IsN2PurgeOHB/ IsXCDAPurgeSTK） 2.得到两厂所有OHB/STK的利用速得到两厂 所有机台以及DefaulStk等信息，并能正确从 Pass/Fail
IsN2PurgeSTK), U中拿取各种存储位的位登信息，判断是否为
正向 获取两厂所有的机台相关信息 Eqptypein（OHBN"STKN）则为 Normal(lsNormalOHB/IsNormalSTK): reticle存储位以及是否overloading 3.成功拿到状态正常的capability
6.overloading判定修改： 4.overloading判断，可以计算repor时间差
USED+USED_TargetFab+CurDeviceCount>=OrderLimit=T 无orderlimit则overloading=F 在原基础上增加了USEDTargetFab（UESDTargetFab是又从fablotcaext 5min内目的地又接受指令的数量 UESDTargetFab是在report计算出后又在 Pass/Fail XOCCX
拿到参数requesteddeviceid然后去重计数得到的结果，即report结果计算 Rule里重新计算的，可得到实时指令教量 5.非Reticle储位优态判断，成功拿到待合条
后还需要去对厂储位的数量个数） 件的储位，并旦标志位sAvailableCheck-T
7.overloading判定修改：
无orderlimit则overloading=F
USED+USEDTargetFab+CurDeviceCount>=OrderLimit=T
在原基础上增加了USEDTargetFab（UESDTargetFab是又从fablotcaext Pass/Fail
拿到参数requesteddeviceid然后去重计数得到的结果，即report结果计算
后还需要去对厂储位的数量个数）
1打MES接口，看是否能正常通讯 Pass/Fail
正向 MES-RTD通讯测试 2.与MES联调测试，使用MESCallRTD得到回复 可以正确接受MES传参，正常进行通讯 Pass/Fail
3.RTD传参检查，通讯栏位传参检查 Pass/Fail
正向 和Non-Trackable优先选择配置非黑名单的存储位 1.选择存储位时要考虑WereNextSTKConstrain中csn返得，按照Trackable 成功从U中拿取信息，根据U配漫的黑名单 将黑名单的OHB和STK多加上对应的flag，选 Pass/Fail
取自的她时去除黑名单自的吧
反向 若未考虑CSN逻辑，那么可以选到黑名单的目的地 黑名单日的她 不从U拿取csn配售，自的地举可以远
成动XUI:WhereNexXCDA十FOUP
上配置（栏位SPECIALPURGEFLAG
SORTINGMODECARRIERTYPE
CARRIERMODELNUMBER STATE
CREATETIME START CREATETIME END
FUNCTIONMODE邦断连确空FOUP是
正向 空FOUP若符合Ul：wherenextXCDA配置，是否搬进XCDApurge储位 表有purge需求，根据eqpbype确认多送日的 香满足配置，空FOUP类型满定U配营时，代 Pans/Fail AELT
地类型进行搬送：
```

</details>

### 第 004 张：case4.jpg

![[00.raw-materials/10.sources/images/TestCase_SOP/TestCase示例/case4.jpg]]

关键 OCR 行：
- No (Local/central) 所属 Report/Rule/AMA) Area功能模快 涉及acro/ 共通模块 逻辑变动内容 类别（正向/方向 （特殊符号处理） 测试内容 测试情景
- 15 16 Local Report ParaLCCResult 新增lotcsnattribute维 度逻辑判断 正向 5、当Lotcsnattribute维度为Key1.csn设置Key1 csnattribute维度 2lotA为Runcardflowlot，当Lotcsnattnbute维意为Key1，对应stn B设置了 csnattribute维度 3、lotA为Branchflow(Rework）lot，当Lotcsnattribute维度为Key1，对应sti 1csnattribute维度
- 17 1、lotA为Namalflowlot，兰Lotcsnattnbute维度为NonKey，对应stnB设置
- 功能步及清单模版 lotcsnattribute维度功能步及清单 测试模板 lotcsnattribute维度TestCase
- 1lotA为Normalflowlot，当Lotcsnattribute维度为空，对应stn B设置了Csn 维度)
- 特殊符号处理 1.当Lotcsnattribute维度为空，STNcsn未设置csnattribute维 2lotA为Runcardflowlot，当Lotcsnattribute维度为空，对应stn B设置了Csi
- 3lotA为Branchflow(Rework）lot，当Lotcsnattribute维度为空：对应stn 维度）
- csnattribute维度）
- 1lotA为Normalflowlot，当Lotcsnattribute维度为空，对应stnB设置了Csn
- 特殊符号处理 2、当Lotcsnattribute维度为空，csn设置csnattribute维度 2lotA为Runcardflowlot，当Lotcsnattribute维度为空，对应stnB设置了Csr
- 3.lotA为Branchflow(Rework）lot，当Lotcsnattribute维度为空，对应stn
- csnattribute维度

<details>
<summary>展开完整 OCR</summary>

```text
No (Local/central) 所属 Report/Rule/AMA) Area功能模快 涉及acro/ 共通模块 逻辑变动内容 类别（正向/方向 （特殊符号处理） 测试内容 测试情景
1lotA为Normalflowlot，当Lotcsnattribute维度为空，对应stn B设置了Csn 维度)
特殊符号处理 1.当Lotcsnattribute维度为空，STNcsn未设置csnattribute维 2lotA为Runcardflowlot，当Lotcsnattribute维度为空，对应stn B设置了Csi
3lotA为Branchflow(Rework）lot，当Lotcsnattribute维度为空：对应stn 维度）
csnattribute维度）
1lotA为Normalflowlot，当Lotcsnattribute维度为空，对应stnB设置了Csn
特殊符号处理 2、当Lotcsnattribute维度为空，csn设置csnattribute维度 2lotA为Runcardflowlot，当Lotcsnattribute维度为空，对应stnB设置了Csr
3.lotA为Branchflow(Rework）lot，当Lotcsnattribute维度为空，对应stn
csnattribute维度
1lotA为Normalflowlot，当Lotcsnattribute维度为NonKey，对应stnB设置
正向 3.当Lotcsnattribute维度为NonKey，csn设置NonKey 2、lotA为Runcardflowiot，当Lotcsnattribute维度为NonKey，对应stn B设置 NonKeycsnattribute维度
csnattribute维度 3、lotA为Branchflow(Rework）lot，Lotcsnattribute维度为NonKey，对 NonKeycsnattribute维度
(STNcsn设置NanKeycsnattribute维）
10 1，lotA为Nomalflowlot，当Lot.csnattribute维度为Key1，对应stnB设置了K
csnattribute维营
反向 4,当Lotcsnattribute维度为NonKey，csn设非NonKey 2、lotA为Runeardflowlat，当Lotcsnattrbute维度为Key2，对应stnB设置了 维度
12 csnattribute维度或者csn未设置csnattribute维度 3、lotA为Branchflowlot，当Lotcsnattribute维度为Key1，对应stnB设置了K
csnattribute维度
13 4、lotA为Branchflowlot，当Lotcsnattnbute维度为Key2，对应stnB设置了k
csnattrbute维度)
14 1，lotA为Nomalflowlot，当Lotcsnattnibute准为Key1对应stnB设置了C
15 16 Local Report ParaLCCResult 新增lotcsnattribute维 度逻辑判断 正向 5、当Lotcsnattribute维度为Key1.csn设置Key1 csnattribute维度 2lotA为Runcardflowlot，当Lotcsnattnbute维意为Key1，对应stn B设置了 csnattribute维度 3、lotA为Branchflow(Rework）lot，当Lotcsnattribute维度为Key1，对应sti 1csnattribute维度
Key1csnattibute
17 1、lotA为Namalflowlot，兰Lotcsnattnbute维度为NonKey，对应stnB设置
Non Keycsnattribute维
18 反向 6、当Lotcsnattribute维度为Key1，csn设置非Key1 2lotA为Runcardflowlot，当Lotcsnattribute维度为Key2，对应stnB设置了 维度）
19 csnattribute维度或者csn未设置csnattribute维度 3、lotA为Branchtlowlot，当Lotcsnattnbute维度为Key2,对应stnB设置了Ke
4、lotA为Branchflowlot.当Lotesnattnbute维度为NonKey，对应stn B设置 csnattnbute维
20 置NonKey csnattnbute维度
21 1、lotA为Nomalflowlot，当Lotcsnattribute准度为Key2，对应stnB设置了Cs
22 正向 7、当Lotcsnattribute维度为Key2.csn设置Key2 2、lotA为Runcardflowlot当Lotcsnattribute维度为Key2，对应stnB设置了C csnattribute准度）
csnattribute维度 csnattribute维度）
23 3lotA为Branchtlow（Rework）lot，当Lotcsnattribute维度为Key2对应stn
Key12csnattribute维度） 1、lotA为Normalflowlot，当Lotcsnattribute维度为NonKey，对应stn B设置
NonKeycsnattnbute维度） lotA为Runcardflowlot当lotcsnattrbute维度为Key1对应stnB设置了k
功能步及清单模版 lotcsnattribute维度功能步及清单 测试模板 lotcsnattribute维度TestCase
```

</details>

### 第 005 张：case5.jpg

![[00.raw-materials/10.sources/images/TestCase_SOP/TestCase示例/case5.jpg]]

关键 OCR 行：
- 测试内容 测试情景 预期结果 测试结 测试日 测试
- 当Lotcsnattribute维度为空，STNcsn未设置csnattribute维 2lotA为Runcardflowlot，当Lotcsnattribute维度为空，对应stnB设置了Csn(STNcsn未设置csnattribute 维度) lotA在stnBCsn结果生效 Pass/Fail
- 3、lotA为Branchflow（Rework）lot当Lotcsnattribute维度为空对应stn B设置了Csn（sTNcsn未设置 维度） lotA在stnBCsn结果生效 Pass/Fail XX
- 1、lotA为Normalflowlot当Lotcsnattribute维度为空对应stnB设置了Csn(STNesn设置csnattribute维 csnattribute维度 lotA在stnBCsn结果生效 Pass/Fail XXXX
- 2lotA为Runcardflowlot，当Lotcsnattribute维度为空，对应stn B设置了Csn (STNcsn设置csnattribute维 lotA在stnBCsn结果不生效 Pass/Fail XXXX
- 当Lotcsnattribute维度为空，csn设置csnattribute维度 3lotA为Branchflow（Rework）lot当Lotcsnattribute维度为空对应stn B设置了csn（STNcsn设置 度) lotA在stnBcsn结果不生效 Pass/Fail
- csnattribute维度） 1lotA为Normal flowlot，当Lotcsnattribute维度为NonKey对应stn B设置了NonKeycsn（STNcsn设置 lotA在stnBcsn结果不生效 Pass/Fail XOX
- 2、lotA为Runcardflowlot当Lotcsnattribute维度为NonKey对应stn B设置了NonKeyCsn(sTN csn设置 NonKeyCsnattribute维度） lotA在stnBc5n结果生效 Pass/Fall XOX
- csnattribute维度 NonKeycsnattribute维度） lotA在stnBcsn结果生效 Pass/Fail
- lotA在stnBcsn结果生效
- csnattribute维度 lotA在stnBcsn结果不生效 Pass/Fail
- 4、当Lotcsnattribute维度为NonKey，csn设置非NonKey 2lotA为Runcardflowlot，当Lotcsnattribute维度为Key2对应stn B设置了Key2csn(sTN csn设置Key2 维度） lotA在stnBcsn结果不生效 Pass/Fail XOOX

<details>
<summary>展开完整 OCR</summary>

```text
测试内容 测试情景 预期结果 测试结 测试日 测试
1、lotA为Nomalflowlot，当Lotcsnattribute维度为空对应stn B设置了Csn(STNcsn未设置csnattribute owner
当Lotcsnattribute维度为空，STNcsn未设置csnattribute维 2lotA为Runcardflowlot，当Lotcsnattribute维度为空，对应stnB设置了Csn(STNcsn未设置csnattribute 维度) lotA在stnBCsn结果生效 Pass/Fail
3、lotA为Branchflow（Rework）lot当Lotcsnattribute维度为空对应stn B设置了Csn（sTNcsn未设置 维度） lotA在stnBCsn结果生效 Pass/Fail XX
1、lotA为Normalflowlot当Lotcsnattribute维度为空对应stnB设置了Csn(STNesn设置csnattribute维 csnattribute维度 lotA在stnBCsn结果生效 Pass/Fail XXXX
2lotA为Runcardflowlot，当Lotcsnattribute维度为空，对应stn B设置了Csn (STNcsn设置csnattribute维 lotA在stnBCsn结果不生效 Pass/Fail XXXX
当Lotcsnattribute维度为空，csn设置csnattribute维度 3lotA为Branchflow（Rework）lot当Lotcsnattribute维度为空对应stn B设置了csn（STNcsn设置 度) lotA在stnBcsn结果不生效 Pass/Fail
csnattribute维度） 1lotA为Normal flowlot，当Lotcsnattribute维度为NonKey对应stn B设置了NonKeycsn（STNcsn设置 lotA在stnBcsn结果不生效 Pass/Fail XOX
2、lotA为Runcardflowlot当Lotcsnattribute维度为NonKey对应stn B设置了NonKeyCsn(sTN csn设置 NonKeyCsnattribute维度） lotA在stnBc5n结果生效 Pass/Fall XOX
3当Lotcsnattribute维度为NonKey，csn设置NonKey
csnattribute维度 NonKeycsnattribute维度） lotA在stnBcsn结果生效 Pass/Fail
3.lotA为Branchflow（Rework）lot当Lotcsnattribute维度为NonKey对应str B设置了NonkeyCsn (STNcsn设置NonKeyCsnattribute维度） Pass/Fall
lotA在stnBcsn结果生效
1.lotA为Normalflowlot，当Lotcsnattribute维度为Key1对应stnB设置了Key1Csn（STN csn设置Key1
csnattribute维度 lotA在stnBcsn结果不生效 Pass/Fail
4、当Lotcsnattribute维度为NonKey，csn设置非NonKey 2lotA为Runcardflowlot，当Lotcsnattribute维度为Key2对应stn B设置了Key2csn(sTN csn设置Key2 维度） lotA在stnBcsn结果不生效 Pass/Fail XOOX
csnattribute维度或者csn未设置csnattribute维度 3、lotA为Branchflowlot当Lotcsnattribute维度为Key1对应stn B设置了Key1csn(sTN csn设置 lotA在stnBcsn结果不生效 Pass/Fail
csnattribute维度
4、lotA为Branchflow lot，当Lotcsnattribute维度为Key2对应stn B设置了Key2Csn(sTNcsn设置 lotA在stnBcsn结果不生效 Pass/Fail X0X
1.lotA为Normalflowlot，当Lotcsnattribute维度为Key1对应stn B设置了Csn(sTN csn设置Key1 csnattribute维度
csnattribute维度） lotA在stnBcsn结果生效 Pass/Fail
5.当Lotcsnattribute维度为Key1,csn设置Key1 2lotA为Runcardflowlot，当Lotcsnattribute维度为Key1对应stn B设置了Csn(sTNcsn设置Key lotA在stnBcsn结果生效 Pass/Fail
csnattribute维度 3.lotA为Branchflow（Rework）lot当Lotcsnattribute维度为Key1对应stnB设置了Csn(sTN csn设置 1csnattribute维度） lotA在stnBcsn结果生效 Pass/Fail X0X
1lotA为Normal flowlot，当Lotcsnattribute维度为NonKey对应stn B设置了NonKeyCsh(STN csn设置 Key1csnattribute维度）
lotA在stnBesn结果不生钱 Pass/Fail X0X
2、lotA为Runcardflowlot，当Lotcsnattribute维度为Key2.对应stnB设置了Key2Csn（STNcsn设置Key2 NonKeycsnattribute维度）
lotA在stnBcsn结果下生效 Pass/Fail
6.当Lotcsnattribute维度为Key1，csn设置非Key1 Csnattribute维度或者csn未设置csnattribute维度 3.lotA为Branchflowlot当Lotcsnattribute维度为Key2,对应stn B设置了Key2csn(STNcsn设置Key2 维度） lotA在stnBcsn结果不生效 Pass/Fail
csnattribute维度） 4.lotA为Branchflow lot当Lotcsnattribute维度为NonKey对应stn B设置了NonKeyCsn (sTNcsn设 lotA在stnBcsn结果不生效 Pass/Fail
1lotA为Normalflowlot，当Lotcsnattribute维度为Key2对应stn B设置了Csn（STNcsn设置Key2 置NonKeycsnattribute维度 lotA在stnBcsn精果生效 Pass/Fail XXXX
7.当Lotcsnattribute维度为Key2，csn设置Key2 2lotA为Runcardflowlot，当Lotcsnattribute维度为Key2.对应stn B设置了CsnSTNcsn设置Key2 csnattribute维度 lotA在stnBesn洁果生效 Pass/Fail
csnattribute维度 3.lotA为Branchflow（Rework）lot，当Lotcsnattribute维度为Key2对应stn B设置了Csh（STNcsn设置 csnattribute维度） lotA在stnBcsn特果生效 Pass/Fail XXXX
Key12csnattribute维度） 1lotA为Normal flowlot，当Lotcsnattribute维度为NonKey对应stn B设置了NonKeyCsn(STNcsn设置 lotA在stnBcsn洁果下生效 Pass/Fail LEY
2lotA为Runcardflowlot当lotcsnattribute维度Key1对应stn B设置了Key1Csn(sTNcsn设置kev1 NonKeycsnattribute维康)
度功能步及清单 测试模板 lotcsnattribute维度TestCase
```

</details>
