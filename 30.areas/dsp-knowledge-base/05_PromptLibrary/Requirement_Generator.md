# Requirement Generator Prompt

> 用途：把制造需求 / 业务想法转换成符合 DSP 工作方式的需求申请单草稿。

## 使用前读取

1. `README.md`
2. `PROJECT_MAP.md`
3. `01_SOP\Requirement_SOP.md`
4. `03_Template\Requirement.md`
5. 与需求相关的 `00_System\*.md`
6. 与需求相关的 `02_Logic\*.md`
7. 如涉及历史相似需求，读取 `04_Case\` 中相关 Case

## 输入

```text
需求背景：
制造/业务提出的问题：
当前逻辑：
期望逻辑：
涉及系统：RTD / AMA / MES / MCS / EAP / 其他
涉及模块：Rule / UI / Report / Sorting / Reason / Dispatch / 其他
已知表名/字段：
未知或需确认字段：
限制条件：
预期收益：
```

## 输出要求

按以下顺序输出：

1. 需求理解
2. 影响范围
3. 原逻辑
4. 新逻辑
5. 流程图草稿
6. Report / UI / Rule / DB 影响
7. 异常与边界场景
8. 待确认事项
9. 按 SOP 结构生成需求申请单草稿
10. 最终交付前使用 `DSP_Humanizer.md` 做工程化表达后处理

## 约束

- 最终需求单必须按公司 SOP，而不是自由格式。
- 不写代码、SQL、接口实现细节。
- 字段不确定时写 `【待确认】`。
- DSP 本地资料可使用真实表名、字段名和业务术语；不得主动上传互联网。
- 若需求涉及 RTD / AMA，大章节按 RTD / AMA 展开；Rule / UI / Report 作为对应章节下小节。
- Humanizer 阶段只降低 AI 感，不新增或推理需求逻辑。

## 输出模板

```text
一、需求理解

二、影响范围

三、原逻辑

四、新逻辑

五、需求流程

六、详细逻辑

七、Report / UI / Rule / DB 影响

八、异常与边界

九、待确认事项

十、需求申请单草稿
```
