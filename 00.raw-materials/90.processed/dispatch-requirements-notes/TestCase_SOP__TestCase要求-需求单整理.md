---
type: dispatch-requirement-note
source_folder: TestCase_SOP/TestCase要求
topic: TestCase / SOP / 验证规范
tags: [自动派工, 需求单, OCR, 需求整理]
---

# TestCase_SOP/TestCase要求 - 需求单整理

## 资料概况

- 原始图片目录：[[00.raw-materials/10.sources/images/TestCase_SOP/TestCase要求]]
- OCR 输出目录：[[00.raw-materials/90.processed/dispatch-requirements-ocr/TestCase_SOP__TestCase要求]]
- 图片数量：2
- 初步主题：TestCase / SOP / 验证规范
- 处理状态：已 OCR，已建立初步结构化笔记
- 注意：本笔记基于 OCR 自动识别，关键需求点需回看原图确认。

## 自动识别到的关键信号

- 系统对象：FOUP, Lot, Port, Recipe
- 派工逻辑：Rule
- 约束条件：Capability
- 系统接口：AMA, MCS, MES
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

### 第 001 张：1.jpg

![[00.raw-materials/10.sources/images/TestCase_SOP/TestCase要求/1.jpg]]

关键 OCR 行：
- 15 AMAMainJobName1
- 16 涉及AMARule AMAMainJobName2
- AMAMainJobName3
- 功能沙及清单模版 lotesnattribute维度功能滋及清单 测试模板 iotcsnattribute雄度TestCase
- 类别（厂别/Macro/Report/功能模块/接口） 类别名称
- 涉及厂别
- 跨厂
- 涉及Macro Macro2 Macro1
- Macro3
- Report1
- 涉及Report Report2
- Report3

<details>
<summary>展开完整 OCR</summary>

```text
类别（厂别/Macro/Report/功能模块/接口） 类别名称
涉及厂别
跨厂
涉及Macro Macro2 Macro1
Macro3
Report1
涉及Report Report2
Report3
10 Report4
功能模块1
12 涉及功能模块 功能模块2
13 功能模块3
14 功能模块4
15 AMAMainJobName1
16 涉及AMARule AMAMainJobName2
AMAMainJobName3
接口1
19 涉及接口 接口2
20 接口3
21
38
30
40
42
43
功能沙及清单模版 lotesnattribute维度功能滋及清单 测试模板 iotcsnattribute雄度TestCase
```

</details>

### 第 002 张：2.jpg

![[00.raw-materials/10.sources/images/TestCase_SOP/TestCase要求/2.jpg]]

关键 OCR 行：
- 测试大类 必测类别 测试标准
- 正/反向测试 各个判断指标的正确，生效符合预期（正向&反向均需测试）
- 每个判断的输出数据是否存在重复
- 数据处理 各个数据的格式，确保单数据的前后一致性，逻辑上下层一致性，避免出现数值/时间格式不一致 过滤删选时，避免误删除数据
- 符合判定的Capability多道次的处理例多IMI垂直限定，DIFF排程多炉管站点
- 13 单点模块测试 Normal与Branch/连环Branch场曼交互 对同一站点多数据的处理：例多Reticle.多前层信息等数据整合的处理 涉及Normal/Branch(Adhoc/RC/RRC/Rework/OCAP）Lo的处理：站点拿取正确，比大小准确、可做业机台正等
- MultiLot 同FOUP多Lot判断的处理，对于Batch时的特殊处理
- 厂别判定 涉及到厂别的判定，每个站点的厂别判断正确
- 产品客制化 产品客制化导致的问题处理，例：产品本身不支持recipe包含，空值比大小响
- 对比验证 改动前后数据差异对比符合需求的处理
- 正/反向测试 参数输出正确（正向&反向均需测试）
- Rule可执行成功且结果满足预期（各单厂/跨厂

<details>
<summary>展开完整 OCR</summary>

```text
测试大类 必测类别 测试标准
正/反向测试 各个判断指标的正确，生效符合预期（正向&反向均需测试）
针对特殊符号的处理准确，特别注意通配/空的处理
边缘值处理 空值的处理，避免输出&循环的数据影响
比大小时，避免产生空值与其他值的比较
比大小注意或或或
每个判断的输出数据是否存在重复
主线和支路的参数整合保证数据整合正确且不重复&不丢失
数据处理 各个数据的格式，确保单数据的前后一致性，逻辑上下层一致性，避免出现数值/时间格式不一致 过滤删选时，避免误删除数据
符合判定的Capability多道次的处理例多IMI垂直限定，DIFF排程多炉管站点
13 单点模块测试 Normal与Branch/连环Branch场曼交互 对同一站点多数据的处理：例多Reticle.多前层信息等数据整合的处理 涉及Normal/Branch(Adhoc/RC/RRC/Rework/OCAP）Lo的处理：站点拿取正确，比大小准确、可做业机台正等
14 (RC/PlanRework/AdhocRework/AdhocSorter/OCAP) 连环Branch的站点判定：Rework进RC.RC进RRC连环RC
Branch至Nomal的站点判定
MultiLot 同FOUP多Lot判断的处理，对于Batch时的特殊处理
厂别判定 涉及到厂别的判定，每个站点的厂别判断正确
Lot同时存在多厂别，拿取当前Lot所在厂别的准确信息及后续站点信息
LotCross时（Lot在两厂的状态均为CrossFabTransfered）中间态Lot所属厂别正确
CrossFab中间态 Lot在Cross途中，Lot厂别全取正确
Cross中的Lot各个Lot属性的参数指标拿取正确，例：RemainQ，LotType，各排程对应指标等相关
产品客制化 产品客制化导致的问题处理，例：产品本身不支持recipe包含，空值比大小响
对比验证 改动前后数据差异对比符合需求的处理
正/反向测试 参数输出正确（正向&反向均需测试）
非改动的其他指标不受影响
Rule可执行成功且结果满足预期（各单厂/跨厂
接口数据正确且能打通并反馈结果
功能模块联动测试 对比验证 AMA脚本正确执行输出结果正确（各单厂/跨厂）
报表数据输出完整且正确（各单厂/跨厂）
改动前后的数据对比符合预期（各单厂/跨厂）
性能测试 验证修改模块对整个功能性能影响，如存在较大影响及时商议并改善
所有涉及场景完整性测试 对修改模块涉及功能&场景进行 梳理并测试验证结果
他系统配套管控 涉及多方功能，视需求情况联合用户协同测试 与R2R/MES/MCS等相关逻辑对齐
跨组/科室/部门联合验证
功能涉及清单模版 lotcsnattribute维度功能涉及清单 测试模板 lotcsnattribute维度TestCase
```

</details>
