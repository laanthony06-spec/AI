# MCS / AMHS

> 来源：自动派工系统培训 PPT，`00.raw-materials/10.sources/images/dsp-dispatch-system-intro/DSP派工系统简介_p027.jpg` ~ `PPT33.jpg`。

## 定位

AMHS（Automatic Material Handling System，自动物料搬送系统）也称天车系统，是用于 WIP 搬送、运输和存储的自动化系统。

MCS 是搬送控制相关系统，用于执行具体搬送动作。

## 搬送形式

PPT 中 AMHS 主要包括：

- interbay 半自动：实现制品在不同制程区域之间的传送，需要 stocker 与每一条 bay 制程对应。
- intrabay 全自动：实现设备对设备的传送，并具备 ZFS（Zero Footprint Storage）功能。

## 存储对象

PPT 中出现的存储相关对象：

- Stocker / Foup 储存柜
- OHB
- Purge OHB
- Purge STK

## 搬送存储作用

搬送存储主要用于：

- 缩短搬送路径；
- 减少搬送系统负荷；
- 加快向设备供货；
- 充分利用生产设备；
- 调整存储类型；
- 提高产品品质保障。

## 与 RTD / AMA 的关系

- RTD 在 Where Next 或搬送流程中决定 Lot / FOUP 存储位置。
- AMA 可在设备 Load Port 空闲时请求 RTD，RTD 根据优先级、设备特性、存储情况等因素选择 Lot，并派到机台 OHB。
- RTD 可通过 MES 发送搬送指令 Call MCS 执行搬送动作。

