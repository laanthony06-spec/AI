---
type: checklist
created: 2026-07-07
tags: [Obsidian, 插件, 工作台, SOP]
status: action-required
---

# Obsidian 插件安装清单

## 安装路径

Obsidian 左下角设置 → 第三方插件 → 浏览。

## 推荐优先级

### P0：备份与安全

- [ ] **Obsidian Git**
  - 用途：自动 commit / sync 到 GitHub。
  - 前置条件：电脑已安装 Git for Windows。
  - 推荐配置见：[[00.raw-materials/90.processed/agent-knowledge-ops/2026-06-16_AI时代Obsidian工作台搭建SOP.md]]

### P1：附件与写作效率

- [ ] **Custom Attachment Location**
  - 用途：让图片跟随文章进入对应 assets 文件夹。
  - 推荐附件位置：`./assets/${noteFileName}`

- [ ] **Advanced Tables**
  - 用途：更方便地编辑 Markdown 表格。
  - 适合：需求字段表、TestCase、选题表、发布记录。

- [ ] **Excalidraw**
  - 用途：画流程图、派工流程、Agent 工作流。

### P2：Agent 与剪藏

- [ ] **Terminal**
  - 用途：在 Obsidian 内打开命令行，配合 Codex / Claude Code。

- [ ] **Obsidian Web Clipper**（Chrome 扩展）
  - 用途：从网页剪藏资料到本地 vault。
  - 推荐模板：[[00.raw-materials/20.metadata/WebClipper模板-X推文.md]]

## 安装后检查

- [ ] `.obsidian/community-plugins.json` 中能看到对应插件 ID。
- [ ] 插件已 Enable。
- [ ] 不把任何 Token / Cookie / AppSecret 写入插件说明笔记。
- [ ] 安装后运行一次敏感扫描：[[00.raw-materials/90.processed/agent-knowledge-ops/sensitive-scan-report.md]]
