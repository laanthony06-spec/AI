# OBSidianCodex 项目运行规则

## LibreOffice

- LibreOffice 安装目录：`C:\Program Files\LibreOffice\program\`。
- 命令行和无界面任务必须调用 `C:\Program Files\LibreOffice\program\soffice.com`。
- 不要直接调用 `soffice.exe`；该 GUI 启动器在自动化环境中可能保持进程并导致任务阻塞。
- 每次无界面转换使用独立的 `-env:UserInstallation=file:///...` 临时 Profile。
- DOCX 渲染优先使用 `00.raw-materials/99.system/scripts/render_docx_safe.ps1`。

## 需求申请单首选模板

- 后续需求单 Word 默认参考个人模板 `$artifact-template-word`。
- 模板参考文件：`00.raw-materials/90.processed/LithoAutoPiRun/LithoAutoPiRun_需求申请单_最终版_流程图更新.docx`。
- 只继承公司申请表版式和大框架，不继承申请人、日期、系统名称、Litho 业务逻辑、表名、字段或版本结论。
- 大框架包括：标题与编号、基础信息、项目简介和必要性分析、改善方案与效果分析、详细需求内容、按系统拆分的变更逻辑、必要流程图、审批意见区。
- 业务内容以本次需求声明、现场证据和确认结论为准；历史知识稿只作为对照基线。
- Test Case 不写入需求单正文，应在需求确认后单独输出 Excel。

## 流程图连接线

- 流程图任务遵循 `30.areas/dsp-knowledge-base/06_Workflow/Codex_Graphviz_Flowchart_Workflow.md`。
- Graphviz DOT 的每条边必须显式使用 `:n`、`:s`、`:w`、`:e` 固定锚点，禁止依赖自动或自由连接点。
- 主流程上下节点保持同一垂直中心轴；判断节点默认“是”从底部 `:s` 向下，“否”从左侧或右侧 `:w/:e` 引出。
- 侧向分支应与判断节点保持同一 rank，并使用 `constraint=false`，保证首段水平且进入矩形侧边正中心。
- 多分支只有在渲染结果确实共用同一目标锚点时才可合并；若 Graphviz 自动错开入点，必须拆分为含义明确的分支结果或子流程，禁止接受箭头偏移、穿越文字或使用自由汇合点。
- 所有连接线使用 `splines=ortho`，并在渲染后检查箭头是否准确接触节点边框。
