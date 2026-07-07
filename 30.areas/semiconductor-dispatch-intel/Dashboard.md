---
type: dashboard
tags: [半导体, 自动派工, 情报看板]
---

# 半导体自动派工情报看板

> 目标：持续跟踪半导体制造自动派工、晶圆厂调度、WIP 控制、AMHS、MES、AI Scheduling、Cycle Time 改善等信息，并沉淀为可复用的岗位知识。

## 快速入口

- 最新情报简报目录：[[30.areas/semiconductor-dispatch-intel/inbox]]
- 情报源与关键词配置：[[30.areas/semiconductor-dispatch-intel/config/sources.yml]]
- 系统说明文档：[[30.areas/semiconductor-dispatch-intel/README.md]]
- 采集脚本：[[30.areas/semiconductor-dispatch-intel/scripts/collect_intel.py]]
- 最近运行日志：[[30.areas/semiconductor-dispatch-intel/cache/last_run.log]]

## 今日处理流程

- [x] 打开最新的每日情报简报
- [ ] 优先阅读“相关度”较高的条目
- [ ] 标记与本厂派工场景相关的内容
- [ ] 将高价值信息整理到专题笔记
- [ ] 根据噪声情况调整关键词或信息源

## 重点关注方向

### 1. 派工规则 / Dispatch Rule

- Lot Priority / 批次优先级
- Bottleneck Tool / 瓶颈设备
- Re-entrant Flow / 重入式流程
- Setup Time / 换线时间
- Tool Qualification / 设备资格
- Recipe Constraint / 工艺配方约束

需要沉淀的问题：

- 哪些 Dispatch Rule 能降低 Cycle Time？
- 如何在 Due Date、Hot Lot、Tool Utilization 之间做权衡？
- 哪些规则适合 Lithography、Etch、CVD、PVD、CMP、Metrology 等不同站点？

### 2. WIP 与 Cycle Time

- WIP Level / 在制品水平
- Queue Time / 排队时间
- Cycle Time / 制造周期
- Throughput / 产出
- Bottleneck Prediction / 瓶颈预测
- Line Balance / 产线平衡

需要沉淀的问题：

- WIP 增加时，哪些站点最先形成瓶颈？
- 派工策略如何影响 Cycle Time 分布？
- 如何识别隐性瓶颈和临时瓶颈？

### 3. AMHS 与搬送派工

- AMHS / Automated Material Handling System
- OHT / Overhead Hoist Transport
- Stocker / 暂存库
- Vehicle Dispatching / 搬送车派工
- Transport Time / 搬送时间
- Load Port / 上下料口

需要沉淀的问题：

- AMHS 派工如何与机台派工联动？
- Stocker 策略如何影响批次等待时间？
- OHT 拥堵是否会改变最优机台选择？

### 4. MES、APS 与工厂系统

- MES / Manufacturing Execution System
- APS / Advanced Planning and Scheduling
- APC / Advanced Process Control
- EAP / Equipment Automation Program
- Lot Tracking / 批次追踪
- Recipe Management / 配方管理

需要沉淀的问题：

- 自动派工需要从 MES 获取哪些实时状态？
- 派工结果如何回写 MES？
- APS 的计划约束如何传递给实时派工系统？

### 5. AI Scheduling 与优化算法

- Reinforcement Learning / 强化学习
- Machine Learning / 机器学习
- Optimization / 优化算法
- Genetic Algorithm / 遗传算法
- Simulation / 仿真
- Digital Twin / 数字孪生

需要沉淀的问题：

- AI Scheduling 相比规则派工的收益在哪里？
- 哪些场景适合用强化学习，哪些场景仍适合规则系统？
- 如何用仿真验证派工策略，而不影响真实产线？

## 信息源状态

| 平台 | 当前状态 | 说明 |
|---|---|---|
| RSS | 已启用 | 行业媒体、arXiv、Google Scholar 等 |
| GitHub | 已启用 | 使用本地 GitHub Token，提高搜索额度 |
| Reddit | 已启用 | 当前使用公开 RSS，不依赖 API 密钥 |
| X / Twitter | 已预留，默认关闭 | 需要填写 `X_BEARER_TOKEN` 后启用 |
| 论文源 | 已启用 | arXiv、Semantic Scholar、Europe PMC；Semantic Scholar 可能限流 |
| 专利源 | 已启用基础入口 | 当前为 Google Patents 监控链接；结构化采集需专利 API |

## 最近情报简报

```dataview
TABLE date AS 日期, file.mtime AS 修改时间
FROM "30.areas/semiconductor-dispatch-intel/inbox"
WHERE type = "semiconductor-dispatch-intel"
SORT date DESC
LIMIT 14
```

## 高价值条目处理模板

```markdown
## 情报摘录：标题

- 来源：
- 链接：
- 日期：
- 分类：派工规则 / WIP / AMHS / MES / AI Scheduling / 论文 / 专利 / 厂商动态
- 相关场景：
- 关键观点：
- 对当前工作的启发：
- 后续行动：
```

## 手动运行采集

```powershell
cd "30.areas/semiconductor-dispatch-intel"
.\.venv\Scripts\python.exe scripts\collect_intel.py
```

## 自动运行设置

Windows 计划任务名称：

```text
Obsidian Semiconductor Dispatch Intel Daily
```

默认每天 **08:00** 自动采集。

查看任务状态：

```powershell
Get-ScheduledTask -TaskName "Obsidian Semiconductor Dispatch Intel Daily"
```

## 待完善事项

- [ ] 填写并启用 X / Twitter Bearer Token
- [ ] 申请 Semantic Scholar API Key，降低论文源限流概率
- [ ] 如需要结构化专利采集，补充 PatentsView 或其他专利数据库 API Key
- [ ] 根据实际岗位关注点继续优化关键词
- [ ] 建立专题笔记：派工规则、WIP 控制、AMHS、MES、AI Scheduling
