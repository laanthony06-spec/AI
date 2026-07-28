# 02_Logic

> DSP 核心业务逻辑知识库。先记录从 PPT 和真实需求中学到的规则，再在具体需求中精读补充字段级细节。

## 通用逻辑文件

- `Reason.md`
- `Sorting.md`
- `Pirun.md`
- `Context.md`

## PPT 已沉淀逻辑文件

- `DispatchRules.md`：Global / Local / LITHO / ETCH / TF / CMP / WET 派工规则总览。
- `QZone.md`：QZone / QTime / Safety Value / Loop Lot Control。
- `WaferBalance.md`：QZone 中机台 loading 平衡、qsort 层级联动、按 WPH / UPH 初始化片数的逻辑。
- `WPHLoss.md`：复合机台 chamber 缺失时的 WPH 修正逻辑。
- `PM_Control.md`：QZone PM 管控、PM Start / End 修正、PM delay report、MFG Prefer 对厂 PM 判断。
- `Qsort.md`：Virtual Lot / Existing Lot 的 qsort 计算逻辑。
- `NPW.md`：Monitor / Season / Dummy / Reuse / Recycle / Downgrade / Reassign。

## 维护方式

每个逻辑文件尽量包含：

1. 定义
2. 适用场景
3. 输入
4. 判断逻辑
5. 输出
6. 常见风险
7. 对应 PPT 页码或案例来源
8. 待确认事项
