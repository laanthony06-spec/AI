# AMA

> 来源：自动派工系统培训 PPT，`00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p005.jpg`、`PPT8.jpg`、`PPT9.jpg`、`PPT10.jpg`、`PPT50.jpg` ~ `PPT90.jpg`。

## 定位

AMA（自动派工管理系统）用于自动化任务和派工前后处理，主要负责派工触发、机台 / port reserve、NPW 管理、Pre-send、Monitor / Season / Dummy / Reuse / Recycle / Downgrade / Reassign 等自动处理。

## 触发方式

### 事件触发

当某台设备状态发生切换、某个 port event 发生变化、或 port 派工模式发生变化时，会询问 RTD 派工。

### 定时触发

PPT 中示例为每隔 5 分钟触发一次，用于周期性检查和自动处理。

### Pre-send

Pre-send 功能会根据 EQP 在作业 Lot 的剩余片数，提前给机台 / port 派工 Lot。

## 典型功能

- Lot Reserve
- Queue Consume
- NPW 准备
- Pre-send
- Monitor In Use Start
- Season In Use Start
- Dummy In Use Start
- In Use End
- Reuse
- Recycle
- Downgrade
- Reassign
- Auto Handle Fail

## NPW 自动化结构

NPW 类型包括：

- Monitor
- Season
- Dummy

NPW 功能模块包括：

- 备片 / AutoInUseStart
- 派工 / Dispatch
- Recycle / AutoInUseEnd
- Downgrade / AutoRecycleEnd

## 写 AMA 需求时必须说明

- 触发方式：事件触发 / 定时触发 / Pre-send / 其他；
- 执行频率；
- 数据获取；
- 条件判断；
- 自动动作；
- 是否调用 RTD；
- 是否发送 alarm；
- 输出结果；
- 异常处理。

## 与 RTD 的边界

- AMA 负责自动化流程编排和触发，例如 reserve、split、dispatch、reuse、recycle、downgrade、reassign。
- RTD 负责被调用时的实时派工判断、筛选、排序和 Where Next。
- 如果一个需求同时影响 AMA 和 RTD，应分别写 AMA 章节和 RTD 章节。

