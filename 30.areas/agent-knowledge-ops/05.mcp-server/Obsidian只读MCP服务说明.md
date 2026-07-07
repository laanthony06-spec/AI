---
type: mcp-prototype-doc
tags: [MCP, Obsidian, Agent, 只读服务]
---

# Obsidian 只读 MCP 服务说明

## 当前实现状态

已建立一个**只读 JSON-RPC 原型服务**：

```text
00.raw-materials/99.system/scripts/obsidian_readonly_mcp.py
```

它不是最终生产版 MCP Server，而是一个安全原型：

- 只读；
- 只能访问当前 vault 内文件；
- 只支持 `.md`、`.txt`、`.json`、`.csv`、`.yml`、`.yaml`；
- 默认通过 stdio 通信，不开启网络端口；
- 不允许写入、删除、移动文件。

## 支持的方法

### list_notes

列出指定目录下的文本资料。

```json
{"id":1,"method":"list_notes","params":{"prefix":"30.areas","limit":20}}
```

### read_note

读取指定文件。

```json
{"id":2,"method":"read_note","params":{"path":"30.areas/agent-knowledge-ops/Dashboard.md"}}
```

### search_notes

全文搜索。

```json
{"id":3,"method":"search_notes","params":{"query":"WaferBalance QTime","limit":10}}
```

## 手动测试

```powershell
cd "D:\Obsidian\work\OBSidianCodex"
echo {"id":1,"method":"search_notes","params":{"query":"WaferBalance","limit":5}} | python "00.raw-materials/99.system/scripts/obsidian_readonly_mcp.py"
```

## 后续升级方向

- [ ] 接入正式 MCP SDK。
- [ ] 增加资源列表：briefs、raw materials、processed notes、testcases。
- [ ] 增加权限配置：只读目录白名单。
- [ ] 增加 Evidence 查询接口。
- [ ] 增加 TestCase 查询接口。

## 需要你确认

如果后续要让外部 Agent 或其他客户端连接，需要确认：

- 是否允许本地端口服务；
- 哪些目录允许读取；
- 是否允许读取敏感目录 `10.sources/sensitive/`；
- 是否需要 Token 或本机访问控制。

