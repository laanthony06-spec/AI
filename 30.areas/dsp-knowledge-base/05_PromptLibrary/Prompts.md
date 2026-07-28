# Prompt Library v1.1

> v1.1 已将高频 Prompt 拆分为独立文件。本文保留为总览索引。

## v1.1 独立 Prompt

| 场景 | 文件 |
| --- | --- |
| 需求单生成 | `Requirement_Generator.md` |
| 需求单 Review | `Requirement_Reviewer.md` |
| 测试用例生成 | `TestCase_Generator.md` |
| 流程图生成 | `FlowChart_Generator.md` |
| 风险检查 | `Risk_Checker.md` |

---

## v0.1 Prompt 摘要

## 1. Requirement Generator

输入：

```text
背景：
需求：
限制：
预期：
涉及系统：
已知字段：
未知字段：
```

输出：

```text
需求申请单
流程图
修改点
影响分析
待确认事项
```

## 2. Test Case Generator

输入：

```text
Requirement：
测试范围：
重点风险：
```

输出：

```text
Normal
Boundary
Exception
Recovery
Regression
```

## 3. Review Assistant

输入：

```text
待 Review 文档：
涉及系统：
重点关注：
```

输出：

```text
完整性检查
逻辑漏洞
异常流程遗漏
Boundary 遗漏
待确认事项
修改建议
```

## 4. Flow Chart Generator

输入：

```text
逻辑说明：
判断条件：
异常分支：
输出结果：
```

输出：

```text
文本流程图
Mermaid 流程图
正文对应关系
```

## 5. Logic Explain

输入：

```text
逻辑片段：
目标读者：
```

输出：

```text
业务解释
输入
判断
输出
风险
待确认
```

## 6. Requirement Optimize

输入：

```text
初版需求单：
SOP：
用户修改意见：
```

输出：

```text
优化后需求单
修改说明
待确认事项
```

## 7. Risk Check

输入：

```text
需求内容：
涉及系统：
上线范围：
```

输出：

```text
业务风险
系统风险
测试风险
上线风险
回滚关注点
```

## 8. AMA Design

输入：

```text
业务目标：
执行频率：
数据来源：
判断条件：
执行动作：
```

输出：

```text
AMA 逻辑设计
异常处理
输出结果
测试重点
```

## 9. RTD Design

输入：

```text
业务目标：
候选对象：
筛选条件：
排序条件：
输出结果：
```

输出：

```text
RTD 逻辑设计
Rule / UI / Report 影响
Reason / Sorting / Dispatch
测试重点
```

## 10. FAQ Builder

输入：

```text
知识文件：
案例：
```

输出：

```text
常见问题
标准答案
待确认问题
```

## 11. Case Builder

输入：

```text
已完成需求：
测试结果：
上线结果：
踩坑：
```

输出：

```text
脱敏 Case
可复用经验
Review 重点
上线注意事项
```

## 12. Change Impact Analyzer

输入：

```text
修改点：
涉及系统：
上下游：
```

输出：

```text
影响范围
受影响逻辑
需回归模块
需确认事项
```
