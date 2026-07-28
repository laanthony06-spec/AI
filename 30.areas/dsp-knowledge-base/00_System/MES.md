# MES

## 定位

MES（Manufacturing Execution System）用于承载制造执行相关数据与状态，是 DSP 逻辑的重要数据来源和结果影响对象之一。

## 常见关注点

- Lot 状态：`【待确认】`
- Step / Route / Recipe：`【待确认】`
- Hold / Active / Transfer 等状态：`【待确认】`
- 与 RTD / AMA 的交互字段：`【待确认】`

## 撰写要求

需求单中涉及 MES 时，应说明：

1. 从 MES 获取什么信息。
2. 这些信息用于什么判断。
3. 判断后是否回写或影响 MES 状态。
4. 异常情况下如何处理。

