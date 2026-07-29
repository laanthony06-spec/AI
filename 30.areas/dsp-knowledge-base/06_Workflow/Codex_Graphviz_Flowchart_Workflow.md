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
- 开始、结束和处理节点统一使用矩形，菱形仅用于判断。
- 判断分支统一标记“是”和“否”。
- 与 `splines=ortho` 同用时，分支文字优先写成 `xlabel="是"` / `xlabel="否"`，避免 Graphviz 的正交边标签警告。
- 单个节点文字尽量不超过 20 个字。
- 优先合并重复结果节点，但仅限渲染后所有分支确实共用同一目标锚点；若 Graphviz 自动错开入点，则拆为含义明确的分支结果或子流程。
- 不得为了压缩画布而缩小字体。
- 判断超过 4 层或单图过长时，拆为主流程和子流程。

## 四、连接线与锚点规范

所有连接线必须使用节点的标准几何锚点，禁止连接到边框上的任意位置。Graphviz DOT 中必须显式使用 `:n`、`:s`、`:w`、`:e`，分别对应 top、bottom、left、right；不得依赖自动端口。

### 矩形节点

- 上方入线连接到上边正中心 `:n`。
- 下方出线连接到下边正中心 `:s`。
- 左右分支连接到对应侧边正中心 `:w` / `:e`。
- 线段必须与矩形边框垂直相交。

### 菱形判断节点

- 上方入线只能连接顶部顶点 `:n`。
- 向下分支只能从底部顶点 `:s` 发出。
- 左分支只能从左侧顶点 `:w` 发出。
- 右分支只能从右侧顶点 `:e` 发出。
- 禁止从菱形斜边中部或靠近顶点的位置引出线段。
- 主流程“是”默认从底部 `:s` 垂直向下；“否”从左侧或右侧 `:w/:e` 水平引出。

### 连接线

- 所有连接线使用水平或垂直的正交折线，不使用斜线、曲线或自由弯折。
- 连接线首段与节点边界垂直，不得贴着节点边缘倾斜进入或离开。
- 相邻上下节点保持同一垂直中心轴，使用 `source:s -> target:n`。
- 分支汇入矩形时，连接到对应边正中心；多个分支汇入同一矩形时，必须使用同一个目标锚点。
- 侧向分支的目标节点应与判断节点处于同一 rank；推荐用 `{ rank=same; decision; no_node; }` 配合 `constraint=false`，使首段保持水平。
- 固定端口语法不是最终验收依据；必须检查 SVG 或 PNG 中的实际几何位置。
- Graphviz 若将多条入线在目标边框上自动摊开，或使箭头进入文字区，不得保留该汇合；应改为含义明确的分支结果节点或拆分子流程，不得加入自由、隐形汇合点规避。
- 箭头尖端必须准确接触节点边框，不得进入节点内部或与边框留有间隙。
- “是/否”使用 `xlabel` 放在线段旁，不得为标签改变锚点或偏移线段。

DOT 示例：

```dot
start:s -> process:n;
process:s -> decision:n;
decision:s -> yes_node:n [xlabel="是"];
{ rank=same; decision; no_node; }
decision:e -> no_node:w [xlabel="否", constraint=false];
```

### 强制禁止项

- 禁止连接线从菱形斜边发出。
- 禁止连接线偏离矩形中心。
- 禁止箭头连接到节点圆角、边角附近或文字区域。
- 禁止为了避让文字而改变节点锚点。
- 禁止同一条主流程中的上下节点出现中心轴偏移。
- 禁止使用自由连接点，必须使用 `:n/:s/:w/:e` 四个固定锚点。

## 生成任务模板

```text
读取需求说明，将业务规则转换为 Graphviz DOT。

要求：
1. 使用 dot 引擎，rankdir=TB，splines=ortho
2. 黑白样式
3. 开始、结束和处理节点统一使用矩形，菱形仅用于判断
4. 判断分支只标“是”和“否”
5. 节点文字不超过 20 个字
6. 在渲染结果保持同一目标锚点的前提下合并重复结果节点
7. 避免连接线交叉
8. 超过 4 层判断时拆分主流程和子流程
9. 每条边显式使用 :n/:s/:w/:e 固定锚点
10. 主流程“是”从菱形底部向下，“否”从左侧或右侧引出
11. 侧向分支使用同层约束，首段保持水平
12. 若 Graphviz 将共享入点摊开，拆分结果节点或子流程

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
6. 是否存在可以安全合并且不会导致入点偏移的重复终点。
7. 是否需要拆分子流程。
8. 每条边是否显式使用固定锚点。
9. 菱形分支是否只从四个顶点发出。
10. 主流程上下节点是否共用垂直中心轴。
11. 多分支汇入是否在渲染结果中实际使用同一个目标锚点。
12. 侧向分支是否同层、首段水平，并进入目标矩形侧边正中心。
13. 是否存在箭头进入节点内部、穿过文字或与边框留有间隙。

最多迭代 3 次；仍无法清晰展示时，应先调整业务分层，而不是继续压缩图形。

## 项目规则模板

若某个独立仓库需要长期固定这些规则，可将“DOT 排版规范、渲染命令、验证与迭代”写入该仓库的 `AGENTS.md`。本库已在根目录 `AGENTS.md` 启用上述固定锚点和渲染验收规则。
