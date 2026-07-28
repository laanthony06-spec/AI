---
type: workflow
tags: [Codex, Graphviz, DOT, 流程图, SVG, PDF]
updated: 2026-07-28
---

# Codex + Graphviz 流程图工作流

## 职责分工

- Codex：理解业务规则、提取节点与分支、生成和修改 `.dot`、执行渲染命令、检查结果并迭代。
- Graphviz `dot`：负责分层布局、减少连线交叉，并输出 SVG、PNG 或 PDF。

标准链路：

```text
业务描述 / 原流程图截图
          ↓
        Codex
  提取节点与分支关系
          ↓
生成并维护 Graphviz DOT
          ↓
运行 dot 自动排版
          ↓
输出 SVG + PDF
          ↓
检查并优化布局
```

`.dot` 是唯一源文件，`.svg` 是主要交付文件，PDF 用于打印或正式归档。

## 推荐目录

```text
flowchart-project/
├─ requirements/
│  └─ lithopilot.md
├─ diagrams/
│  ├─ lithopilot.dot
│  ├─ lithopilot.svg
│  └─ lithopilot.pdf
└─ scripts/
   └─ render.ps1
```

如果流程图属于本库现有需求项目，业务说明仍放在项目案例目录，DOT 与导出文件放在对应项目的 `03_Assets` 或专用 `diagrams` 子目录。

## 环境检查

```powershell
dot -V
```

Windows 未安装时可执行：

```powershell
winget install Graphviz.Graphviz
```

安装属于环境变更，应由用户确认后执行。

## DOT 排版规范

- 使用 `dot` 排版引擎。
- `rankdir=TB`，主流程从上到下。
- `splines=ortho`，使用正交连接线。
- 黑线、黑字、白底，不使用阴影、渐变或装饰色。
- 椭圆表示开始和结束，矩形表示处理，菱形表示判断。
- 判断分支统一标记“是”和“否”。
- 与 `splines=ortho` 同用时，分支文字优先写成 `xlabel="是"` / `xlabel="否"`，避免 Graphviz 的正交边标签警告。
- 单个节点文字尽量不超过 20 个字。
- 合并重复结果节点。
- 不得为了压缩画布而缩小字体。
- 判断超过 4 层或单图过长时，拆为主流程和子流程。

## 生成任务模板

```text
读取需求说明，将业务规则转换为 Graphviz DOT。

要求：
1. 使用 dot 引擎，rankdir=TB，splines=ortho
2. 黑白样式
3. 椭圆表示起止，矩形表示处理，菱形表示判断
4. 判断分支只标“是”和“否”
5. 节点文字不超过 20 个字
6. 合并重复结果节点
7. 避免连接线交叉
8. 超过 4 层判断时拆分主流程和子流程

生成后输出 SVG 和 PDF。若 Graphviz 报警或版面拥挤，修改 DOT 后重新渲染，最多迭代 3 次。
```

## 渲染命令

```powershell
dot -Tsvg diagrams/lithopilot.dot -o diagrams/lithopilot.svg
dot -Tpdf diagrams/lithopilot.dot -o diagrams/lithopilot.pdf
```

通用 PowerShell 脚本：

`00.raw-materials/99.system/scripts/render_graphviz.ps1`

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File "00.raw-materials/99.system/scripts/render_graphviz.ps1" `
  -InputPath "diagrams/lithopilot.dot"
```

## 验证与迭代

每次修改 DOT 后检查：

1. Graphviz 命令是否成功，是否存在语法警告。
2. SVG、PDF 是否生成。
3. 节点是否拥挤或超出画布。
4. 连接线是否交叉，左右分支是否失衡。
5. 判断节点文字是否过长。
6. 是否存在可以合并的重复终点。
7. 是否需要拆分子流程。

最多迭代 3 次；仍无法清晰展示时，应先调整业务分层，而不是继续压缩图形。

## 项目规则模板

若某个独立仓库需要长期固定这些规则，可将“DOT 排版规范、渲染命令、验证与迭代”写入该仓库的 `AGENTS.md`。本库暂不启用全局 Graphviz 强制规则，避免影响不需要 DOT 的任务。
