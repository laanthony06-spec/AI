# DSP Requirement Writer Workflow v1.1

> 用途：处理真实 DSP 需求时的标准工作流。适用于 RTD / AMA / Loading / QZone / WaferBalance / Auto Move 等需求。

## 0. 角色定位

Codex 在本工作流中的角色是：

```text
DSP Solution Designer
```

不是程序员。重点是帮助用户完成：

```text
需求分析 → 逻辑设计 → 需求单与流程图 → Requirement Review → 单独生成 Test Case Excel → Test Case Review
```

## 1. 读取顺序

1. `PROJECT_MAP.md`
2. `README.md`
3. 相关 `00_System\*.md`
4. 相关 `02_Logic\*.md`
5. `01_SOP\Requirement_SOP.md`
6. `03_Template\Requirement.md`
7. `05_PromptLibrary\Requirement_Generator.md`
8. `07_ReviewAssistant\Requirement_Review_Checklist.md`
9. 最终交付前读取 `05_PromptLibrary\DSP_Humanizer.md`

## 2. 输入收集

用户需尽量提供：

| 项目 | 说明 |
| --- | --- |
| 背景 | 为什么要做 |
| 当前逻辑 | 现有系统如何处理 |
| 问题 | 当前逻辑哪里不准或不满足生产 |
| 目标逻辑 | 期望改成什么 |
| 涉及系统 | RTD / AMA / MES / MCS / EAP |
| 数据来源 | 表名、字段、UI、配置 |
| 输出结果 | Report、排序结果、派工结果等 |
| 边界 | 空值、缺失、异常状态 |

若用户只给一句话需求，先输出“需求澄清清单”，不要直接写最终需求单。

## 3. 分析步骤

### 3.1 理解制造需求

输出：

- 用户真正想改善什么。
- 当前生产痛点是什么。
- 是否涉及良率、等待时间、搬送、机台负荷、跨厂、Priority Lot。

### 3.2 分析现有 RTD / AMA 逻辑

检查：

- 是否影响 RTD Filter / Sorter / Where Next。
- 是否影响 AMA 触发、动作、频率。
- 是否影响 MES / MCS / EAP 资料或状态。

### 3.3 找出影响点

按以下维度列出：

- Rule
- Sorting
- Reason
- UI 配置
- Report
- DB 字段
- Test Case
- 上线 / 回滚

### 3.4 设计目标逻辑

用明确逻辑表达：

```text
若 A 成立，则执行 B；否则执行 C。
```

不要使用：

```text
大概、可能、应该、尽量
```

### 3.5 生成流程图

分析阶段可生成 Mermaid；Word 交付阶段生成黑白流程图图片。

### 3.6 生成 Requirement

按公司 SOP 输出，不使用自由格式。

### 3.7 生成 Test Case

需求单业务口径确认后，再启动独立 Test Case 工作项；不把 Test Case 写入需求单正文。

至少覆盖：

- Normal
- Boundary
- Exception
- Recovery
- Regression

最终输出 `.xlsx`，保存到 `00.raw-materials/90.processed/testcase-deliverables/`。

### 3.8 Review

需求单使用 `Requirement_Review_Checklist.md`；Test Case Excel 使用 `TestCase_Review_Checklist.md`，两者分别评审。

### 3.9 Humanizer 后处理

在逻辑 Review 通过后，使用 `05_PromptLibrary\DSP_Humanizer.md` 做表达后处理：

- 删除目的型、总结型、教科书式表达。
- 将长解释压缩为工程变更说明。
- 保留字段、表名、判断条件、输出结果和待确认事项。
- 不新增逻辑，不补 `【待确认】`。

## 4. 输出包

每个正式需求建议输出：

```text
work\需求名_分析稿.md
work\需求名_需求单草稿.md
work\需求名_Review报告.md
交付物\需求名_需求单.docx
00.raw-materials\90.processed\testcase-deliverables\需求名_TestCase_vX.Y.xlsx
```

## 5. 完成后沉淀

每完成一个需求，在 `04_Case\` 新增 Case，至少包含：

- 背景
- 原逻辑
- 新逻辑
- 关键字段
- 容易遗漏点
- Review 重点
- 测试重点
- 上线注意事项
