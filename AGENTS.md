# OBSidianCodex 项目运行规则

## LibreOffice

- LibreOffice 安装目录：`C:\Program Files\LibreOffice\program\`。
- 命令行和无界面任务必须调用 `C:\Program Files\LibreOffice\program\soffice.com`。
- 不要直接调用 `soffice.exe`；该 GUI 启动器在自动化环境中可能保持进程并导致任务阻塞。
- 每次无界面转换使用独立的 `-env:UserInstallation=file:///...` 临时 Profile。
- DOCX 渲染优先使用 `00.raw-materials/99.system/scripts/render_docx_safe.ps1`。

