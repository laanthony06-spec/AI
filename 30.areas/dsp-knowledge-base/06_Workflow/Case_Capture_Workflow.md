# Case Capture Workflow

> 用途：需求完成后沉淀为案例，避免经验散落在单次对话中。

## 触发时机

- 需求单完成后。
- Test Case 完成后。
- 上线后发现问题时。
- 用户指出 Codex 理解错误并完成纠正后。

## Case 文件位置

```text
04_Case\CaseXXX_需求简名.md
```

## Case 必填内容

```text
背景：
为什么改：
原逻辑：
新逻辑：
关键字段：
容易误解：
Review 重点：
测试重点：
上线注意：
可复用经验：
```

## 可复用经验判断

如果经验可跨需求复用，再提炼到：

```text
02_Logic\
07_ReviewAssistant\
05_PromptLibrary\
```

