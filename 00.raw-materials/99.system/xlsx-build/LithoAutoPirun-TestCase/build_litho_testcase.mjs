import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const buildDir = "D:/Obsidian/work/OBSidianCodex/00.raw-materials/99.system/xlsx-build/LithoAutoPirun-TestCase";
const outputDir = "D:/Obsidian/work/OBSidianCodex/outputs/019f9417-3c5f-7c43-a4be-f92f54eb74d4";
const outputPath = path.join(outputDir, "LithoAutoPirun_TestCase.xlsx");
const previewDir = path.join(buildDir, "preview");

await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(previewDir, { recursive: true });

const workbook = Workbook.create();
const functionSheet = workbook.worksheets.add("功能涉及清单");
const caseSheet = workbook.worksheets.add("LithoAutoPirun TestCase");

const palette = {
  header: "#B8CCE4",
  group: "#DCE6F1",
  subGroup: "#EEF3F8",
  white: "#FFFFFF",
  black: "#000000",
  grid: "#7F7F7F",
  positive: "#E2F0D9",
  negative: "#FCE4D6",
  boundary: "#FFF2CC",
  linkage: "#DDEBF7",
};

const baseFont = { name: "宋体", size: 10, color: palette.black };
const headerFont = { name: "宋体", size: 10, color: palette.black, bold: true };
const allBorder = { preset: "all", style: "thin", color: palette.grid };

const functionGroups = [
  ["涉及厂别", ["FAB6", "FAB8", "FAB6/FAB8 跨厂（CrossFab）"]],
  ["涉及 Macro/共通模块", [
    "istransferlot marco",
    "TransferMarco",
    "FuLL(RemainQ)",
    "Qu_0",
    "WatchDog_LithoPiLotAutoDoAdhocSorter",
    "Global Macro：WaitPilotChangeFOUP",
  ]],
  ["涉及 Report", [
    "Central_GetLithoR2RAutoPirunInfo（修改）",
    "LithoPiLotAutoDoAdhocSorter（新增）",
  ]],
  ["涉及功能模块", [
    "待判断 Lot 获取与基础过滤",
    "PirunLoop 获取与进一步过滤",
    "可作业机台与 R2R Context 判断",
    "Context 内 Lot 排序",
    "Context 间排序与循环选 Pilot",
    "整批 Pilot 判断",
    "Wafer 分组、排序与物理分批选片",
    "Merge 站点设定",
    "AdhocSorter Carrier 排序与输出",
  ]],
  ["涉及 Rule/Assign", [
    "LithoRule：R2RAutoPirunControl",
    "LithoRule：Parent&ChildLotNeedRunSameTool",
    "LithoAssign：R2RAutoPirunControl",
    "LithoAssign：Parent&ChildLotNeedRunSameTool",
  ]],
  ["涉及 AMA", [
    "整批 Lot 设置 Pilot",
    "物理分批执行前六项复核",
    "空 FOUP 预占与 MES 物理分批",
    "TransferFoup",
  ]],
  ["涉及接口/系统", [
    "R2R Pilot 接口",
    "MES 物理分批接口",
    "MES TransferFOUP 接口",
    "AMALog",
  ]],
];

const functionRows = [["类别（厂别/Macro/Report/功能模块/接口）", "类别名称"]];
const functionMerges = [];
let functionRow = 2;
for (const [category, items] of functionGroups) {
  const start = functionRow;
  for (const item of items) {
    functionRows.push([category, item]);
    functionRow += 1;
  }
  functionMerges.push([start, functionRow - 1]);
}

functionSheet.getRange(`A1:B${functionRows.length}`).values = functionRows;
for (const [start, end] of functionMerges) {
  if (end > start) functionSheet.mergeCells(`A${start}:A${end}`);
}
functionSheet.showGridLines = false;
functionSheet.freezePanes.freezeRows(1);
functionSheet.getRange(`A1:B${functionRows.length}`).format = {
  font: baseFont,
  wrapText: true,
  verticalAlignment: "center",
  borders: allBorder,
};
functionSheet.getRange("A1:B1").format = {
  fill: palette.header,
  font: headerFont,
  horizontalAlignment: "center",
  verticalAlignment: "center",
  wrapText: true,
  borders: allBorder,
  rowHeight: 34,
};
functionSheet.getRange(`A2:A${functionRows.length}`).format = {
  fill: palette.group,
  font: headerFont,
  horizontalAlignment: "center",
  verticalAlignment: "center",
  wrapText: true,
  borders: allBorder,
};
functionSheet.getRange(`B2:B${functionRows.length}`).format = {
  fill: palette.white,
  font: baseFont,
  horizontalAlignment: "left",
  verticalAlignment: "center",
  wrapText: true,
  borders: allBorder,
};
functionSheet.getRange(`A1:A${functionRows.length}`).format.columnWidth = 34;
functionSheet.getRange(`B1:B${functionRows.length}`).format.columnWidth = 62;
functionSheet.getRange(`A2:B${functionRows.length}`).format.rowHeight = 28;

const groups = [];
const addGroup = (scope, area, module, change, testContent, scenarios) => {
  groups.push({ scope, area, module, change, testContent, scenarios });
};

addGroup(
  "central",
  "Report",
  "Central_GetLithoR2RAutoPirunInfo",
  "新增 FAB6/FAB8 Lot 基础信息获取与过滤条件",
  "验证待判断 Lot 的基础过滤",
  [
    ["正向", "FAB6 Lot：processingstatus='Active'、CarrierKind='FOUP'、runcardid 为空、requiredcapability=LithoCapability。", "Lot 通过基础过滤，进入 IsTransferLot 与 PirunLoop 判断。"],
    ["正向", "FAB8 Lot：processingstatus='CrossFabTransferred'，其余条件满足，requiredcapability=L-BARCO-L；另以 L-BARCO-S 重复验证。", "两个 BARCO Capability 均被正确识别，Lot 进入后续判断。"],
    ["反向", "分别构造 processingstatus 非 Active/CrossFabTransferred、为空的 Lot。", "对应 Lot 被过滤，且 Report 计算不中断。"],
    ["反向", "CarrierKind 非 FOUP。", "Lot 被过滤。"],
    ["反向", "runcardid 非空。", "Lot 被过滤。"],
    ["反向", "requiredcapability 不属于 LithoCapability、L-BARCO-L、L-BARCO-S。", "Lot 被过滤。"],
  ],
);

addGroup(
  "central",
  "Report/Macro",
  "istransferlot marco",
  "增加跨厂信息去重条件",
  "验证 IsTransferLot 与 processingstatus 的组合过滤",
  [
    ["正向", "IsTransferLot=True，processingstatus='CrossFabTransferred'。", "Lot 保留，跨厂记录仅保留一份。"],
    ["正向", "IsTransferLot≠True，processingstatus='Active'。", "Lot 保留。"],
    ["反向", "IsTransferLot≠True，processingstatus='CrossFabTransferred'。", "Lot 被过滤，避免跨厂信息重复。"],
    ["数据处理", "同一 Lot 在取数来源中出现重复记录。", "输出按需求维度去重，不产生重复候选 Lot/Context。"],
  ],
);

addGroup(
  "central",
  "Report",
  "PirunLoop",
  "向下 Fetch 20 站并截取至同 Stage 最后一道 CD",
  "验证 PirunLoop 范围和 TransferLot 厂别修正",
  [
    ["正向", "20 站范围内存在多道 CD；准备跨 Stage 数据。", "PirunLoop 从当前站点截取到同 Stage 最后一道 CD，不包含截断后的站点。"],
    ["反向", "向下 Fetch 20 站内不存在 CD。", "Lot 被过滤。"],
    ["跨厂", "TransferLot 后续站点的原始厂别与实际目标厂别不同。", "按 TransferLot 规则修正厂别，后续 Litho 机台与配置均使用修正后的厂别。"],
    ["边界", "CD 恰好位于第 20 个 Fetch 站点。", "该 CD 被纳入 PirunLoop，并作为截断终点。"],
  ],
);

addGroup(
  "central",
  "Report",
  "PirunLoop 进一步过滤",
  "增加 Litho/Reticle、Specify、同 FOUP Pilot、FutureHold、RC 判断",
  "验证 PirunLoop 的需求限定过滤项",
  [
    ["正向", "Loop 中存在 capability=LithoCapability 且含 Reticle 的站点，且无其他排除项。", "Lot 保留。"],
    ["反向", "Loop 中无 LithoCapability 站点，或 Litho 站点无 Reticle。", "Lot 被过滤。"],
    ["正向", "Lot 命中 r2r_litho_whitelist（productid、layer、lotid）。", "沿用现有 Specify Lot 处理，不套用新增 AutoPirun 选择逻辑。"],
    ["多Lot", "同一 FOUP 中已存在从 rtd_r2r_litho_context_ovlcd/rtd_r2r_lot_history 取得的 Litho Pilot。", "当前 Lot 被过滤。"],
    ["反向", "PirunLoop 任一站点存在 FutureHold，或 Loop 中存在 RC 站点。", "对应 Lot 被过滤；无 FutureHold 且无 RC 时不误过滤。"],
  ],
);

addGroup(
  "central",
  "Report/Macro",
  "可作业机台获取/TransferMarco",
  "按机台厂别获取 Pi_split_flag、pi_splitcnt 并过滤卡控机台",
  "验证可作业机台集合",
  [
    ["跨厂", "Lot 在 Litho 站点可 Transfer；本厂和对厂均有 Litho 机台。", "同时取得对厂机台，并按各机台厂别读取 rtd_r2r_litho_add_setting。"],
    ["反向", "Lot 的所有候选机台均不存在 Pi_split_flag='Y'。", "Lot 被过滤。"],
    ["正向", "多台候选机台中部分触发 EQPStatus/LCC/Capability/Recipe/PPID/Global Reason 卡控，至少一台未卡控。", "仅筛除被卡控机台，Lot 保留未卡控且 Pi_split_flag='Y' 的机台。"],
    ["反向", "所有 Pi_split_flag='Y' 的机台均被上述任一条件卡控。", "Lot 无可作业机台并被过滤。"],
  ],
);

addGroup(
  "central",
  "Report/Rule",
  "R2R Context/多路径判断",
  "按 Lot+STN+Reticle 匹配 OVL/CD 状态和 Reason",
  "验证可用 Context 与多路径过滤",
  [
    ["正向", "OVL_Status、CD_Status 分别取 PIRUNON/ON/Fixed 的有效组合，且无 R2R Reason。", "Context 保留。"],
    ["反向", "OVL_Status 或 CD_Status 不在 PIRUNON/ON/Fixed，或存在 R2R Reason。", "Context 被过滤。"],
    ["正向", "按 Lot 统计后 ContextCount=1。", "Lot 保留并进入选 Lot。"],
    ["反向", "按 Lot 统计后 ContextCount>1。", "判定为多路径，Lot 被过滤。"],
  ],
);

addGroup(
  "central",
  "Report",
  "AutoPirun Context 筛选",
  "筛选需要自动 Pirun 的 Context",
  "验证 Pi_split_flag 与 Pilot_CD/Pilot_OVL 条件",
  [
    ["正向", "Pi_split_flag='Y'，Pilot_CD 与 Pilot_OVL 至少一个为 Null。", "Context 被识别为需要自动 Pirun。"],
    ["反向", "Pi_split_flag≠'Y'；或 Pilot_CD、Pilot_OVL 均非 Null。", "Context 不进入 AutoPirun 候选。"],
  ],
);

addGroup(
  "central",
  "Report",
  "Context 内 Lot 排序",
  "新增 RTDRank 七级排序指标",
  "验证排序指标计算及明确边界",
  [
    ["正向", "同 Context 下准备不同 GapToLitho，其余指标相同。", "GapToLitho 最小的 Lot 排在前。"],
    ["边界", "componentqty 分别小于、等于、大于 pi_splitcnt。", "小于时 SplitCntMatched=0；等于或大于时为1。"],
    ["边界", "pi_splitcnt 分别为空、0、负数、26；另设 25。", "前四种均按默认值4计算；25 保持25，不使用默认值。"],
    ["数据处理", "有 prelayer 时准备 C1/C2 各≥2片及不足2片；无 prelayer 时准备奇/偶 Slot 各≥2片及不足2片。", "满足时 RequiredChuckCount=1，否则为0；数据来源分别为 waferhistory 与 materialassociation。"],
    ["正向", "准备空扣/空 LP Lot 与普通 Lot。", "前者 BulletLot=1，普通 Lot=0；在前四项相同时 BulletLot=1 排在前。"],
    ["边界", "RemainQ 为正数、0、负数、Null。", "正数保留原值；其余均转为9999，并按 Min(RemainQ) 排序。"],
    ["正向", "quota_applyinfo 中 KeyLot=1 且 Status=CONFIRM；再准备非确认/非 KeyLot。", "仅确认 KeyLot 指标为1；排序严格按需求的 Min(KeyLot) 执行。"],
    ["数据处理", "前六项排序指标完全相同，仅 lotid 不同。", "按 Min(lotid) 稳定决胜，RTDRank 无并列漂移。"],
  ],
);

addGroup(
  "central",
  "Report",
  "Context 间排序/循环选 Pilot",
  "新增 ReticleSTNRank、ContextCandidateCount、ActualSTNPilotCount 及循环剔除",
  "验证 Context 均衡分配与每个 Context 最多一个 Pilot",
  [
    ["正向", "循环前 Context 的 STN 与 ReticleOnSTN 相同；另设不同 STN 的 Context。", "相同者 ReticleSTNRank=1，并按 Max(ReticleSTNRank) 优先。"],
    ["正向", "循环中准备与上轮第一 Context 同 Reticle+STN 组和不同组的数据。", "同组 ReticleSTNRank 更新为1，不同组为0。"],
    ["正向", "ReticleSTNRank 相同，ContextCandidateCount/ActualSTNPilotCount/RTDRank 依次制造差异。", "严格按 Min(ContextCandidateCount)、Min(ActualSTNPilotCount)、Min(RTDRank) 逐级排序。"],
    ["数据处理", "第一名固定后仍存在相同 Lot 或相同 Context 的其他组合。", "删除与已选 Lot/Context 冲突的组合，更新指标继续循环；每个 Context 最多选一个 Pilot，直至无可用项。"],
  ],
);

addGroup(
  "central",
  "Report/Macro",
  "整批 Pilot 判断",
  "五组条件按“或”关系决定 IsNeedSplit",
  "验证整批 Pilot 与物理分批分流",
  [
    ["正向", "BulletLot=1 或 KeyLot=1，其他整批条件均不成立。", "整批设为 Pilot，IsNeedSplit=F。"],
    ["正向", "CurCapability=LithoCapability 且 FuLL(RemainQ)；分别取消其中一个条件。", "两项同时成立才触发该分支；仅一项成立不因本分支整批。"],
    ["正向", "RequiredChuckCount=0，或 SplitCntMatched=0。", "任一成立即整批 Pilot。"],
    ["边界", "componentqty 分别为6和7，其余整批条件均不成立。", "6片整批 Pilot；7片进入物理分批。"],
    ["反向", "五项整批条件均不成立。", "IsNeedSplit=T，进入 Wafer 选片。"],
  ],
);

addGroup(
  "central",
  "Report",
  "物理分批 Wafer 分组与选片",
  "新增 Group/SubGroup、GroupRank、WaferRank 与 pi_splitwafer",
  "验证 Wafer 分组、排序和选片数量",
  [
    ["边界", "Waferid 使用 #1、#10、#11、#25。", "#1-#10 进入 Group1，#11-#25 进入 Group2，边界不串组。"],
    ["正向", "Lot 有 Chuck 信息，包含 C1/C2 Wafer。", "C1→SubGroup1，C2→SubGroup2，不使用 Slot 奇偶。"],
    ["正向", "Lot 无 Chuck 信息，准备奇数/偶数 Slot。", "奇数→SubGroup1，偶数→SubGroup2。"],
    ["数据处理", "准备四个 Group+SubGroup 组合。", "GroupRank 依次为 G1-SG1=1、G1-SG2=2、G2-SG1=3、G2-SG2=4。"],
    ["正向", "各 Group+SubGroup 内准备多片 Wafer，pi_splitcnt=4。", "组内按 waferid 生成 WaferRank，再按 Min(WaferRank)、Min(GroupRank) 选出前4片。"],
    ["边界", "pi_splitcnt 为空、0、负数、26；另设有效值25。", "无效配置均选默认4片；25按25片处理。"],
    ["反向", "pi_splitcnt 大于 Lot 当前可用 Wafer 数。", "不执行物理分批，改为整批 Pilot。"],
  ],
);

addGroup(
  "central",
  "Report",
  "Merge 站点/Report 输出",
  "新增 Merge 站点规则并扩充 Central Report 输出",
  "验证 Merge 站点和输出栏位",
  [
    ["正向", "PirunLoop 中存在多道非 SRC ADI。", "第一道非 SRC ADI 被设为 Merge 站点。"],
    ["正向", "无非 SRC ADI（仅有 SRC ADI 或完全无 ADI）。", "最后一道 CD 被设为 Merge 站点。"],
    ["数据处理", "选中一个整批 Pilot 和一个物理分批 Pilot。", "Central_GetLithoR2RAutoPirunInfo 输出 Lot、toolid、productid、layerid、reticleid、prereticle、pretool、custom_context_value、pi_splitwafer、IsNeedSplit、isSTNSite，值与计算一致。"],
    ["数据处理", "同一轮存在多个 Lot/Context 结果。", "Report 不重复、不漏失；每条结果与其 Lot、Context、选片一一对应。"],
  ],
);

addGroup(
  "central",
  "Report",
  "LithoPiLotAutoDoAdhocSorter",
  "新增需 TransferFOUP 的 Litho Pilot 筛选与同 Carrier Other Lot 判断",
  "验证 Report 候选 Pilot 与 Carrier 条件",
  [
    ["边界", "Pilot priority 分别为4和5，category='Production'，OVL 或 CD 为 PIRUNON。", "priority=4 入选；priority=5 不入选。"],
    ["反向", "category 非 Production；或 OVL/CD 均非 PIRUNON。", "Pilot 不进入需 TransferFOUP 清单。"],
    ["正向", "OVL_Status='PIRUNON'、CD 非 PIRUNON；再交换两者。", "两种场景均入选，符合“或”关系。"],
    ["多Lot", "Pilot 同 Carrier 存在 extrastatus='WaitForJobPrep' 的 Other Lot。", "该 Pilot 标记为需要 Change FOUP。"],
    ["反向", "同 Carrier 无 Other Lot，或 Other Lot 的 extrastatus 非 WaitForJobPrep。", "该 Pilot 不进入 Change FOUP 结果。"],
  ],
);

addGroup(
  "central",
  "Report/AMA",
  "Carrier 排序/WatchDog 输出",
  "按四级指标排序并受 Switch、Trigger Time Slot、TriggerCount/Time 控制",
  "验证 AdhocSorterJob 排序与输出数量",
  [
    ["正向", "多个 Carrier 依次在 RemainQ、Priority、componentqty、lotid 上制造差异。", "严格按 Min(RemainQ)、Min(Priority)、Max(componentqty)、Min(lotid) 排序。"],
    ["正向", "Switch='Y'，当前时间位于 Trigger Time Slot 内，候选数大于 TriggerCount/Time。", "仅排序后的前 TriggerCount/Time 个 Carrier 写入 Report。"],
    ["反向", "Switch≠'Y'，或当前时间不在 Trigger Time Slot。", "本轮不输出需处理 Carrier。"],
    ["数据处理", "触发条件满足并有多条结果。", "Report 输出 Carrier、Pilot、extrastatus、Status、RemainQ、Pieces、Prod、Priority，顺序和数据均正确。"],
  ],
);

addGroup(
  "central",
  "Global Macro",
  "WaitPilotChangeFOUP",
  "新增 Pilot/Other Lot 卡控及按站点、Qtime 的 Remove 规则",
  "验证卡控对象与解除条件",
  [
    ["反向", "WatchDog Switch≠'Y' 或当前时间不在 Trigger Time Slot。", "不新增 WaitPilotChangeFOUP 卡控。"],
    ["多Lot", "LithoPilot 位于 UnScheduleSorter；同 FOUP Other Lot 不在 AdhocSorter。", "仅 Other Lot 增加 WaitPilotChangeFOUP。"],
    ["多Lot", "LithoPilot 不在 UnScheduleSorter；同 FOUP Other Lot 也不在 AdhocSorter。", "LithoPilot 与 Other Lot 均增加 WaitPilotChangeFOUP。"],
    ["反向", "Other Lot 位于 Litho 站点，RemainQ<4H 或触发 Qu_0。", "按需求 Litho 站点不能 Remove，卡控继续保留。"],
    ["边界", "Other Lot 位于 BARCO，RemainQ 分别为3.9H和4H，且未触发 Qu_0。", "3.9H Remove；4H 不因 RemainQ Remove。触发 Qu_0 时均 Remove。"],
    ["反向", "Other Lot 位于非 Litho/BARCO，分别仅 RemainQ<4H、触发 Qu_0。", "仅 RemainQ<4H 不 Remove；触发 Qu_0 才 Remove。"],
    ["边界", "LithoPilot 不在 Sorter，RemainQ 分别为3.9H和4H，另设 Qu_0。", "3.9H 或 Qu_0 时 Remove；4H 且无 Qu_0 时不 Remove。"],
  ],
);

addGroup(
  "central",
  "LithoRule",
  "R2RAutoPirunControl",
  "保留并明确 AutoPirun Pilot 卡控条件",
  "验证 Rule 卡控条件的与关系及 Specify 例外",
  [
    ["正向", "非 Specify Lot，Pi_SplitFlag='Y'，R2R CD/OVL Status 均为 PIRUNON，Pilot 非 Null。", "卡控 Reason=R2RAutoPirunControl。"],
    ["反向", "命中 Specify 白名单，其他条件均满足。", "不按 R2RAutoPirunControl 卡控。"],
    ["反向", "非 Specify，但分别令 Pi_SplitFlag≠'Y'、CD 或 OVL 非 PIRUNON、Pilot 为 Null。", "任一条件不满足均不产生该 Reason。"],
  ],
);

addGroup(
  "central",
  "LithoRule",
  "Parent&ChildLotNeedRunSameTool",
  "新增子母批同机台卡控",
  "验证 pretool、FutureMerge、最新历史与机台比对",
  [
    ["反向", "按 Prod/layer 关系未取得 pretool，或 pretool 为空。", "不进入新增子母批机台比对，按原逻辑处理。"],
    ["正向", "通过 r2r_litho_context_relation 的 pre_layer→curr_layer，再从 OVL 取得非空 pretool。", "正确识别为需后续判断的 Lot。"],
    ["数据处理", "FutureMerge 关联的子/母批在当前 layer 有多条 r2r_lot_history，完成时间相同且记录ID不同。", "先按实际作业完成时间降序、再按记录ID降序，取得唯一最新 toolid。"],
    ["正向", "非 Specify Lot，待判断机台与最新子/母批 toolid 不一致。", "卡控 Reason=Parent&ChildLotNeedRunSameTool。"],
    ["反向", "非 Specify Lot，机台与最新 toolid 一致。", "不产生新增 Reason，按原逻辑处理。"],
    ["反向", "Specify Lot，机台与子/母批 toolid 不一致。", "不按新增子母批逻辑卡控。"],
  ],
);

addGroup(
  "Local/central",
  "LithoAssign",
  "R2RAutoPirunControl/Parent&ChildLotNeedRunSameTool",
  "LithoAssign 增加与 LithoRule 一致的两类卡控，子母批数据改由 Central 提供",
  "验证 Assign 与 Rule 的判定一致性",
  [
    ["联动", "使用同一非 Specify Lot 和 R2R 状态分别执行 LithoRule、LithoAssign。", "R2RAutoPirunControl 的卡控结果与 Reason 一致。"],
    ["联动", "Central 返回 pretool、FutureMerge 子/母批最新 toolid，分别测试同机台和不同机台。", "LithoAssign 的 Parent&ChildLotNeedRunSameTool 结果与 LithoRule 一致。"],
    ["反向", "不满足新增两类卡控条件的普通 Lot。", "LithoAssign 原有逻辑结果不受影响。"],
  ],
);

addGroup(
  "Local",
  "AMA/Report/R2R",
  "设置 Pilot/物理分批执行前复核",
  "AMA 按 Central Report 分流，并在物理分批前执行六项复核",
  "验证整批分流、六项复核范围及失败行为",
  [
    ["联动", "Central Report 返回 IsNeedSplit=F。", "AMA 不调用 MES 物理分批，直接将整批 Lot 传给 R2R。"],
    ["正向", "IsNeedSplit=T；Lot 属于当前执行厂 FAB6/FAB8、WaitForJobPrep、runcardid 为空、Capability 合法、CarrierKind='FOUP'、所选 Wafer 均属于该 Lot。", "六项复核通过，进入空 FOUP 预占。"],
    ["反向", "分别构造 Lot 不属于当前执行厂、状态非 WaitForJobPrep。", "停止处理该 Lot，记录对应失败原因，等待下一轮重新计算，不回退整批 Pilot。"],
    ["反向", "分别构造 runcardid 非空、Capability 非 Litho/L-BARCO-L/L-BARCO-S、CarrierKind 非 FOUP。", "任一项失败即停止并记录准确原因，不预占 FOUP、不调用 MES、不回退整批 Pilot。"],
    ["反向", "Report 的 pi_splitwafer 中至少一片不属于该 Lot。", "Wafer 归属复核失败，停止并记录原因，不回退整批 Pilot。"],
    ["正向", "所选 Wafer 属于该 Lot，但 Wafer 状态、Slot 或 Chuck 与 Report 不一致。", "仅按归属关系复核，不因状态/Slot/Chuck 额外阻断。"],
  ],
);

addGroup(
  "Local",
  "AMA/MES/R2R",
  "空 FOUP 与 MES 物理分批",
  "六项复核通过后预占空 FOUP、调用 MES，并按结果回退",
  "验证物理分批成功和两类回退",
  [
    ["联动", "六项复核通过，成功预占空 FOUP，MES 物理分批成功。", "指定 pi_splitwafer 被分为子批 Pilot，子批传给 R2R；母批保留未选 Wafer。"],
    ["异常处理", "六项复核通过，但没有可用空 FOUP。", "不调用 MES 物理分批，整批 Lot 传给 R2R。"],
    ["异常处理", "已预占空 FOUP，但 MES 物理分批接口 Fail。", "立即释放预占 FOUP，并将整批 Lot 传给 R2R。"],
    ["数据处理", "Report 指定多片 pi_splitwafer，MES 返回成功。", "仅指定 Wafer 进入子批，无多分、漏分；R2R 收到的 Pilot 为新子批。"],
  ],
);

addGroup(
  "Local",
  "AMA/MES/AMALog",
  "TransferFoup",
  "AMA 按 LithoPiLotAutoDoAdhocSorter 顺序调用 MES TransferFOUP",
  "验证 TransferFOUP 成功及失败日志",
  [
    ["联动", "Report 有排序结果，空 FOUP 可用，MES TransferFOUP 成功。", "按 Report 顺序将 Pilot 导入空 FOUP，处理顺序不变。"],
    ["异常处理", "拿取可用空 FOUP 失败。", "不调用后续无效操作，并在 AMALog 记录 Fail 信息。"],
    ["边界", "返回的可用空 FOUP 数量为0。", "在 AMALog 记录 Fail 信息。"],
    ["异常处理", "MES TransferFOUP 接口失败。", "在 AMALog 记录接口 Fail 信息，Lot/Carrier/Pilot 可追溯。"],
  ],
);

addGroup(
  "Local/central",
  "Report/Rule/AMA/接口",
  "LithoAutoPirun 端到端联动",
  "串联 Report 选择、Rule/Assign 卡控、AMA 分批/换 FOUP、MES/R2R 结果",
  "验证需求明确涉及的跨模块闭环",
  [
    ["联动", "Central 选出 IsNeedSplit=T 的 Pilot，六项复核和 MES 分批均成功。", "Report→AMA→MES→R2R 数据一致；子批 Pilot 生效，原 Lot 不被错误重复处理。"],
    ["联动", "Central 选出 IsNeedSplit=F 的整批 Pilot。", "AMA 直接把整批 Lot 传给 R2R；Rule/Assign 按 Pilot 状态执行对应卡控。"],
    ["多Lot", "同 FOUP 存在 Pilot 与 WaitForJobPrep Other Lot，Pilot 需要 TransferFOUP。", "Report2 排序输出、WaitPilotChangeFOUP 卡控、AMA TransferFoup 和卡控解除规则衔接一致。"],
    ["跨厂", "FAB6 Lot 可 Transfer 到 FAB8 Litho 机台，并完成 Pilot 选择与后续执行。", "厂别修正、对厂配置/机台、Central 输出及本厂 AMA 复核边界一致，不出现重复 Lot 或错误跨厂执行。"],
    ["数据处理", "同一轮含整批、物理分批、TransferFOUP、Specify 与普通未命中 Lot。", "仅需求命中的对象被处理；Report 栏位、排序、Reason、AMA 调用与日志无重复、无漏失，Specify 与原有逻辑保持不变。"],
  ],
);

const headers = [
  "No",
  "所属（Local/central）",
  "Area（功能模块 Report/Rule/AMA）",
  "涉及 Macro/共通模块",
  "逻辑变动内容",
  "类别（正向/反向/特殊符号处理）",
  "测试内容",
  "测试情景",
  "预期结果",
  "测试结果",
  "测试日期",
  "测试owner",
];

const caseRows = [headers];
const groupRanges = [];
let currentRow = 2;
for (let index = 0; index < groups.length; index += 1) {
  const group = groups[index];
  const start = currentRow;
  for (const scenario of group.scenarios) {
    caseRows.push([
      index + 1,
      group.scope,
      group.area,
      group.module,
      group.change,
      scenario[0],
      group.testContent,
      scenario[1],
      scenario[2],
      "Pass/Fail",
      "XXXX",
      "XXXX",
    ]);
    currentRow += 1;
  }
  groupRanges.push([start, currentRow - 1]);
}

const lastRow = caseRows.length;
caseSheet.getRange(`A1:L${lastRow}`).values = caseRows;
caseSheet.showGridLines = false;
caseSheet.freezePanes.freezeRows(1);
caseSheet.freezePanes.freezeColumns(2);

for (const [start, end] of groupRanges) {
  for (const col of ["A", "B", "C", "D", "E", "G"]) {
    if (end > start) caseSheet.mergeCells(`${col}${start}:${col}${end}`);
  }
}

caseSheet.getRange(`A1:L${lastRow}`).format = {
  font: baseFont,
  wrapText: true,
  verticalAlignment: "center",
  borders: allBorder,
};
caseSheet.getRange("A1:L1").format = {
  fill: palette.header,
  font: headerFont,
  horizontalAlignment: "center",
  verticalAlignment: "center",
  wrapText: true,
  borders: allBorder,
  rowHeight: 48,
};
caseSheet.getRange(`A2:G${lastRow}`).format.verticalAlignment = "center";
caseSheet.getRange(`A2:D${lastRow}`).format.horizontalAlignment = "center";
caseSheet.getRange(`F2:F${lastRow}`).format.horizontalAlignment = "center";
caseSheet.getRange(`J2:L${lastRow}`).format.horizontalAlignment = "center";
caseSheet.getRange(`E2:E${lastRow}`).format.horizontalAlignment = "left";
caseSheet.getRange(`G2:I${lastRow}`).format.horizontalAlignment = "left";
caseSheet.getRange(`A2:L${lastRow}`).format.rowHeight = 68;

const widths = {
  A: 6,
  B: 14,
  C: 19,
  D: 26,
  E: 30,
  F: 17,
  G: 30,
  H: 52,
  I: 50,
  J: 11,
  K: 12,
  L: 12,
};
for (const [col, width] of Object.entries(widths)) {
  caseSheet.getRange(`${col}1:${col}${lastRow}`).format.columnWidth = width;
}

for (let index = 0; index < groupRanges.length; index += 1) {
  const [start, end] = groupRanges[index];
  if (index % 2 === 1) {
    caseSheet.getRange(`A${start}:L${end}`).format.fill = palette.subGroup;
  }
  caseSheet.getRange(`A${start}:A${end}`).format.fill = palette.group;
  caseSheet.getRange(`A${start}:A${end}`).format.font = headerFont;
}

caseSheet.getRange(`J2:J${lastRow}`).dataValidation = {
  rule: { type: "list", values: ["Pass/Fail", "Pass", "Fail", "Blocked", "Not Run"] },
};
caseSheet.getRange(`F2:F${lastRow}`).conditionalFormats.add("containsText", {
  text: "边界",
  format: { fill: palette.boundary, font: { color: palette.black } },
});
caseSheet.getRange(`F2:F${lastRow}`).conditionalFormats.add("containsText", {
  text: "联动",
  format: { fill: palette.linkage, font: { color: palette.black } },
});

const xlsx = await SpreadsheetFile.exportXlsx(workbook);
await xlsx.save(outputPath);

const functionPreview = await workbook.render({
  sheetName: "功能涉及清单",
  autoCrop: "all",
  scale: 1,
  format: "png",
});
await fs.writeFile(path.join(previewDir, "01_功能涉及清单.png"), new Uint8Array(await functionPreview.arrayBuffer()));

const chunkSize = 24;
let chunkIndex = 1;
for (let start = 1; start <= lastRow; start += chunkSize) {
  const end = Math.min(lastRow, start + chunkSize - 1);
  const preview = await workbook.render({
    sheetName: "LithoAutoPirun TestCase",
    range: `A${start}:L${end}`,
    scale: 0.65,
    format: "png",
  });
  await fs.writeFile(
    path.join(previewDir, `02_TestCase_${String(chunkIndex).padStart(2, "0")}_R${start}-R${end}.png`),
    new Uint8Array(await preview.arrayBuffer()),
  );
  chunkIndex += 1;
}

const workbookSummary = await workbook.inspect({
  kind: "sheet",
  include: "id,name",
  maxChars: 4000,
});
const functionInspect = await workbook.inspect({
  kind: "region",
  sheetId: "功能涉及清单",
  range: `A1:B${functionRows.length}`,
  maxChars: 6000,
  tableMaxRows: 12,
  tableMaxCols: 2,
  tableMaxCellChars: 120,
});
const caseInspect = await workbook.inspect({
  kind: "region",
  sheetId: "LithoAutoPirun TestCase",
  range: `A1:L${Math.min(lastRow, 18)}`,
  maxChars: 9000,
  tableMaxRows: 18,
  tableMaxCols: 12,
  tableMaxCellChars: 120,
});
const formulaErrors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 },
  summary: "final formula error scan",
  maxChars: 4000,
});

console.log(JSON.stringify({
  outputPath,
  functionRowCount: functionRows.length,
  testGroupCount: groups.length,
  testScenarioCount: lastRow - 1,
  workbookSummary,
  functionInspect,
  caseInspect,
  formulaErrors,
}, null, 2));
