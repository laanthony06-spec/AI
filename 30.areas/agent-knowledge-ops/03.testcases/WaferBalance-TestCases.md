---
type: dispatch-testcase
topic: WaferBalance
tags: [WaferBalance, TestCase, QZone, QTime, WPH]
source:
  - "[[00.raw-materials/10.sources/images/WaferBalance/需求单1.jpg]]"
  - "[[00.raw-materials/10.sources/images/WaferBalance/需求单2.jpg]]"
  - "[[00.raw-materials/10.sources/images/WaferBalance/表1.jpg]]"
  - "[[00.raw-materials/90.processed/dispatch-requirements-notes/WaferBalance逻辑通俗介绍.md]]"
---

# WaferBalance TestCases

## TC-WB-001：初始化片数按 WPH 加权，而不是平均分

### 目标

验证 WaferBalance 初始化 wafer 数时，会根据机台作业能力 WPH 分配，而不是简单平均。

### 输入

| Lot | Qty | Step | 可作业 EQP | WPH |
|---|---:|---|---|---|
| LotA | 20 | COAT | COT002, COT003 | COT002=20, COT003=25 |

### 执行规则

```text
Lot 在某机台的初始化片数
= Lot QTY ×（该机台 WPH / 所有可作业机台 WPH 之和）
```

### 期望结果

| EQP | 计算 |
|---|---|
| COT002 | 20 × 20 / 45 ≈ 8.89 |
| COT003 | 20 × 25 / 45 ≈ 11.11 |

### 验收标准

- COT003 的初始化片数应大于 COT002。
- 不应出现 COT002=10、COT003=10 的简单平均分配。

### 证据来源

- [[00.raw-materials/10.sources/images/WaferBalance/需求单2.jpg]]
- [[00.raw-materials/10.sources/images/WaferBalance/表1.jpg]]

---

## TC-WB-002：后一 qsort 层级继承前一层级的机台负载

### 目标

验证不同 qsort category 之间存在联动；后一层级 balance 时，必须把前面层级已产生的 `EQP WIP Time` 作为 `Pre EQP WIP Time`。

### 输入

| qsort category | Lot | EQP | Current EQP WIP Time |
|---:|---|---|---:|
| 6 | LotA | COT002 | 0.5 |
| 6 | LotA | COT003 | 0.4 |
| 12 | LotC | COT002 | 0.65 |

### 前置状态

category 6 已经完成 balance：

| EQP | Pre EQP WIP Time |
|---|---:|
| COT002 | 0.5 |
| COT003 | 0.4 |

### 执行规则

```text
New EQP WIP Time
= Pre EQP WIP Time + Current EQP WIP Time
```

### 期望结果

category 12 计算 COT002 时，不应从 0 开始，而应：

```text
New COT002 WIP Time = 0.5 + 0.65 = 1.15
```

### 验收标准

- 后一层级不能忽略前一层级的机台占用时间。
- 如果前一层级没有该机台，则初始时间为 0。

### 证据来源

- [[00.raw-materials/10.sources/images/WaferBalance/需求单1.jpg]]
- [[00.raw-materials/10.sources/images/WaferBalance/需求单2.jpg]]

---

## TC-WB-003：机台越忙，权重越低

### 目标

验证 WaferBalance 的权重计算方向正确：机台累计作业时间越大，分配权重越低。

### 输入

| EQP | New EQP WIP Time |
|---|---:|
| EQP_A | 0.5 |
| EQP_B | 1.5 |

### 执行规则

```text
机台权重 ≈ 1 / 该机台作业所有分配 Lot 的时间总和
```

### 期望结果

| EQP | 预期权重关系 |
|---|---|
| EQP_A | 权重较高 |
| EQP_B | 权重较低 |

### 验收标准

- EQP_A 应分到更多后续 wafer。
- EQP_B 不应继续被过度分配。

### 证据来源

- [[00.raw-materials/10.sources/images/WaferBalance/表1.jpg]]

