---
type: template
template_for: web-clip-x-tweet
created: 2026-07-07
tags: [WebClipper, X, 模板, 原始资料]
---

# X 推文剪藏模板

```yaml
---
type: web-clip
platform: X
source_author:
source_handle:
source_url:
source_title:
published:
captured: {{date}}
language: zh-CN
tags: [X]
status: source-record
copyright_note: 仅保存来源信息、短摘录、结构化摘要与可落地观察；不保存未经授权全文。
---
```

## 使用位置

建议保存到：

```text
00.raw-materials/10.sources/web-clips/x-tweets/
```

## 正文结构

```markdown
# {{title}}

## 来源

- 平台：X / Twitter
- 作者：
- 原文链接：
- 发布时间：
- 读取方式：

## 合规短摘录

> 保留不超过 25 个词的短摘录。

## 结构化摘要

用自己的话概括原文，不逐字搬运长文。

## 可借鉴点

1.
2.
3.

## 待确认

- [ ] 是否需要进一步读取链接文章？
- [ ] 是否需要生成 SOP？
- [ ] 是否需要加入任务队列？
```
