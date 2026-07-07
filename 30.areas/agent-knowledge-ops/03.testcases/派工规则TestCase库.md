---
type: testcase-index
tags: [自动派工, TestCase, DSP, RTD]
---

# 派工规则 TestCase 库

目标：把派工规则从“描述性知识”转成“可验证案例”。

## 为什么要做

自动派工逻辑经常包含多层约束，例如 QTime、QZone、WPH、Capability、Recipe、PM、Hot Lot。只靠文字说明容易漏掉边界条件。TestCase 可以帮助我们确认：

- 输入数据是否完整；
- 规则判断是否稳定；
- 改版前后结果是否符合预期；
- 是否会引入 OverQtime、WPH Loss 或负载失衡。

## 当前 TestCase 集合

- [[30.areas/agent-knowledge-ops/03.testcases/WaferBalance-TestCases.md]]

## 标准模板

```markdown
## TC-编号：标题

### 目标

### 输入

| Lot | Qty | qsort category | Step | 可作业 EQP | WPH / UPH | remain QTime |
|---|---:|---:|---|---|---|---|

### 前置状态

| EQP | Pre EQP WIP Time | 状态 |
|---|---:|---|

### 执行规则

### 期望结果

### 验收标准

### 证据来源
```

## 后续要补

- [ ] Qsort TestCase
- [ ] PM_Control TestCase
- [ ] WPHLoss TestCase
- [ ] TestCase_SOP 示例规范化

