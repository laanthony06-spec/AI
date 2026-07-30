import fs from "node:fs/promises";
import {
  FileBlob,
  SpreadsheetFile,
  Workbook,
} from "@oai/artifact-tool";

const workspace = "D:/Obsidian/work/OBSidianCodex";
const outputDir = `${workspace}/outputs/019fb28d-c1bc-70b1-8b53-c1618dca15fb`;
const outputFile = `${outputDir}/Reticle_AB版分仓逻辑_TestCase.xlsx`;

const cases = [
  ["TC-RAB-001","Central","RTD/DSP · 共通逻辑","AB Group 判定","R1｜14码 ReticleID 的 AB 版识别","正向","验证标准 A/B 版被识别为同一 AB Group","准备 RETICLE000001A 与 RETICLE000001B：两者长度均为14，前13码 RETICLE000001 相同，第14码不同。","两块 Reticle 被识别为同一 AB Group，并参与后续冲突判断。","Not Run",null,"","需求：Mask AB版判定"],
  ["TC-RAB-002","Central","RTD/DSP · 共通逻辑","AB Group 判定","R1｜14码 ReticleID 的 AB 版识别","反向","验证完全相同的 ReticleID 不构成 A/B 对版","比较 RETICLE000001A 与 RETICLE000001A。","第14码未发生差异，不作为两块 A/B 对版；不得仅因前13码相同即判定冲突。","Not Run",null,"",""],
  ["TC-RAB-003","Central","RTD/DSP · 共通逻辑","AB Group 判定","R1｜14码 ReticleID 的 AB 版识别","反向","验证不同前13码不属于同一 AB Group","比较 RETICLE000001A 与 RETICLE000002B。","前13码不同，两块 Reticle 不属于同一 AB Group。","Not Run",null,"",""],
  ["TC-RAB-004","Central","RTD/DSP · 共通逻辑","AB Group 判定","R1｜非14码 SpecialReticle 排除","边界","验证13码 ReticleID 不参与 AB 判定","准备 RETICLE000001（13码），并与 RETICLE000001A 同时进入判定。","13码对象被视为 SpecialReticle，不参与 AB Group/冲突标记。","Not Run",null,"",""],
  ["TC-RAB-005","Central","RTD/DSP · 共通逻辑","AB Group 判定","R1｜非14码 SpecialReticle 排除","边界","验证15码 ReticleID 不参与 AB 判定","准备 RETICLE000001AB（15码），并与标准14码 Reticle 同时进入判定。","15码对象被视为 SpecialReticle，不参与 AB Group/冲突标记。","Not Run",null,"",""],
  ["TC-RAB-006","Central","RTD/DSP · 共通逻辑","AB Group 判定","R1｜混合 ReticleID 数据处理","数据处理","验证普通 Reticle 与 SpecialReticle 混合时判定准确","输入 RETICLE000001A、RETICLE000001B、RETICLE000001、RETICLE000001AB。","仅两条14码且前13码相同、第14码不同的记录形成 AB Group；SpecialReticle 被跳过且流程不中断。","Not Run",null,"",""],

  ["TC-RAB-007","Central","RTD/DSP · Report","Target Stocker 取得","R2｜候选 Stocker 过滤","正向","验证 RTLSTK_BARE 正常候选","Target 记录满足 eqpkind='Stocker'、processtype='Stocker'、stockertype='RETICLE'、constructtype='Normal'、TYPE='RTLSTK_BARE'，且 name 不等于当前 ReticleLocation。","该机台进入 Target Stocker 候选集合。","Not Run",null,"","数据源：设备与 Location 相关表"],
  ["TC-RAB-008","Central","RTD/DSP · Report","Target Stocker 取得","R2｜候选 Stocker 过滤","正向","验证 XCDA/NOXCDA 两类正常候选","分别准备 TYPE='RTLSTK_XCDA' 与 TYPE='RTLSTK_NOXCDA'，其余过滤条件均满足。","两类机台均进入 Target Stocker 候选集合。","Not Run",null,"","参数化执行两次"],
  ["TC-RAB-009","Central","RTD/DSP · Report","Target Stocker 取得","R2｜排除当前所在 Stocker","反向","验证当前 ReticleLocation 不可作为 Target","候选机台全部字段有效，但 name=待传出 Reticle 当前 ReticleLocation。","该机台被排除，不允许原 Stocker 被选为 Target。","Not Run",null,"",""],
  ["TC-RAB-010","Central","RTD/DSP · Report","Target Stocker 取得","R2｜候选 Stocker 过滤","反向","验证 eqpkind 条件","设置 eqpkind!='Stocker'，其余条件满足。","该记录不进入 Target Stocker 候选集合。","Not Run",null,"",""],
  ["TC-RAB-011","Central","RTD/DSP · Report","Target Stocker 取得","R2｜候选 Stocker 过滤","反向","验证 processtype 条件","设置 processtype!='Stocker'，其余条件满足。","该记录不进入 Target Stocker 候选集合。","Not Run",null,"",""],
  ["TC-RAB-012","Central","RTD/DSP · Report","Target Stocker 取得","R2｜候选 Stocker 过滤","反向","验证 stockertype 条件","设置 stockertype!='RETICLE'，其余条件满足。","该记录不进入 Target Stocker 候选集合。","Not Run",null,"",""],
  ["TC-RAB-013","Central","RTD/DSP · Report","Target Stocker 取得","R2｜候选 Stocker 过滤","反向","验证 constructtype 条件","设置 constructtype!='Normal'，其余条件满足。","该记录不进入 Target Stocker 候选集合。","Not Run",null,"",""],
  ["TC-RAB-014","Central","RTD/DSP · Report","Target Stocker 取得","R2｜候选 Stocker 过滤","反向","验证 TYPE 白名单","设置 TYPE 为非 RTLSTK_BARE/RTLSTK_XCDA/RTLSTK_NOXCDA 的值，其余条件满足。","该记录不进入 Target Stocker 候选集合。","Not Run",null,"",""],
  ["TC-RAB-015","Central","RTD/DSP · Report","Target Stocker 取得","R2｜多候选取得与去重","数据处理","验证多个合法 Target 均可取得且不重复","准备 STK_RSP_02、STK_BRS_01 两个合法候选，并使设备扩展表 Join 产生重复行。","输出包含两个合法 Target，每个 Stocker 仅保留一个候选对象。","Not Run",null,"","去重为防止多表 Join 放大"],
  ["TC-RAB-016","Central","RTD/DSP · Report","Target Stocker 取得","R2｜无合法候选处理","边界","验证没有合法 Target 时流程安全结束","所有机台至少有一个过滤条件不满足，或唯一合法记录为当前 Stocker。","Target 集合为空；不产生错误的 TransportOut 目的地或异常中断。","Not Run",null,"",""],

  ["TC-RAB-017","Central","RTD/DSP · Report","Target Reticle 汇总","R3｜Target 内既有 Reticle 取得","正向","验证库存 Reticle 被纳入 Target 内容","在 fwinvmaterialpropertyext/fwinvdurableserialized/fwinvlocation 关联数据中，使 wname=STK_RSP_02，id=RETICLE000001B。","RETICLE000001B 被纳入 STK_RSP_02 的既有 Reticle 集合。","Not Run",null,"",""],
  ["TC-RAB-018","Central","RTD/DSP · Report","Target Reticle 汇总","R3｜正搬入 Reticle 取得","正向","验证预约搬入 Reticle 被纳入 Target 内容","fwinvslotcontainer/Ext 中 requesteddeviceid=STK_RSP_02，reservedreticleid=RETICLE000001B。","RETICLE000001B 被纳入 STK_RSP_02 的正搬入 Reticle 集合。","Not Run",null,"",""],
  ["TC-RAB-019","Central","RTD/DSP · Report","Target Reticle 汇总","R3｜正搬入 Reticle 过滤","反向","验证其他 Target 的预约记录不被误用","存在 reservedreticleid=RETICLE000001B，但 requesteddeviceid=STK_BRS_01；当前判断对象为 STK_RSP_02。","该预约记录不计入 STK_RSP_02 的 Reticle 集合。","Not Run",null,"",""],
  ["TC-RAB-020","Central","RTD/DSP · Report","Target Reticle 汇总","R3｜既有与正搬入数据合并","数据处理","验证两类 Reticle 合并后共同参与判断","STK_RSP_02 既有 RETICLE000002A，同时有 reservedreticleid=RETICLE000001B 正搬入。","Target Reticle 集合同时包含两条记录，后续按合并后的完整集合计算 ExistMaskA&B。","Not Run",null,"",""],
  ["TC-RAB-021","Central","RTD/DSP · Report","Target Reticle 汇总","R3｜重复数据处理","数据处理","验证同一 Reticle 多次 Join/重复出现不影响结果","同一 id/reservedreticleid 在查询结果中重复两次以上。","汇总结果按 Reticle 唯一标识处理；冲突 Flag 正确且不因重复数据产生额外搬送。","Not Run",null,"",""],
  ["TC-RAB-022","Central","RTD/DSP · Report","Target Reticle 汇总","R3｜空 Target 内容","边界","验证 Target 既无库存也无预约搬入","既有 Reticle 查询与正搬入查询均无记录。","Target Reticle 集合为空，后续 ExistMaskA&B 判为 F。","Not Run",null,"",""],

  ["TC-RAB-023","Central","RTD/DSP · Report","ExistMaskA&B","R4｜AB 冲突 Flag","正向","验证 Target 已存在对版时 Flag=T","传出 RETICLE000001A；Target 既有 RETICLE000001B。","Target 标记 ExistMaskA&B=T。","Not Run",null,"",""],
  ["TC-RAB-024","Central","RTD/DSP · Report","ExistMaskA&B","R4｜AB 冲突 Flag","正向","验证 Target 正搬入对版时 Flag=T","传出 RETICLE000001A；Target 无既有对版，但预约搬入 RETICLE000001B。","Target 标记 ExistMaskA&B=T，避免并发搬入造成 A/B 同仓。","Not Run",null,"",""],
  ["TC-RAB-025","Central","RTD/DSP · Report","ExistMaskA&B","R4｜AB 冲突 Flag","反向","验证 Target 只有同一 ID 时不误判对版","传出 RETICLE000001A；Target 查询结果仅含 RETICLE000001A。","因第14码相同，不构成 A/B 对版，ExistMaskA&B=F。","Not Run",null,"",""],
  ["TC-RAB-026","Central","RTD/DSP · Report","ExistMaskA&B","R4｜AB 冲突 Flag","反向","验证不同 Group 不误判","传出 RETICLE000001A；Target 含 RETICLE000002B。","前13码不同，ExistMaskA&B=F。","Not Run",null,"",""],
  ["TC-RAB-027","Central","RTD/DSP · Report","ExistMaskA&B","R4｜AB 冲突 Flag","边界","验证 SpecialReticle 不参与冲突 Flag","传出标准14码 Reticle；Target 仅含13码或15码、前缀相似的 SpecialReticle。","SpecialReticle 被排除，ExistMaskA&B=F。","Not Run",null,"",""],
  ["TC-RAB-028","Central","RTD/DSP · Report","ExistMaskA&B","R4｜混合内容 Flag","数据处理","验证 Target 含多块 Reticle 时任一对版即可置 T","Target 同时含多个无关 Reticle 与一块 RETICLE000001B；传出 RETICLE000001A。","只要完整集合中存在同 AB Group 的对版，ExistMaskA&B=T。","Not Run",null,"",""],

  ["TC-RAB-029","Central","RTD/DSP · Report","Target Stocker 排序","R5｜ExistMaskA&B 排序指标","正向","验证 F 候选优先于 T 候选","两个 Target 原排序中 STK_RSP_02 在前且 Flag=T，STK_BRS_01 在后且 Flag=F。","新增排序后 STK_BRS_01 排在 STK_RSP_02 前并优先被选中。","Not Run",null,"",""],
  ["TC-RAB-030","Central","RTD/DSP · Report","Target Stocker 排序","R5｜F 组内保持原排序","回归","验证多个 F 候选沿用原排序指标","准备三个 ExistMaskA&B=F 的 Target，原有水位/距离/优先级排序结果明确。","三个 F 候选之间仍按原排序顺序选择，新指标不破坏原有组内排序。","Not Run",null,"",""],
  ["TC-RAB-031","Central","RTD/DSP · Report","Target Stocker 排序","R5｜全部候选冲突时回退","边界","验证所有 Target 均为 T 时流程不中断","所有合法 Target 均存在或正搬入对应 AB 版，均标记 T。","没有 F 候选时不应报错或空指针；暂按原排序继续选择/给出无可避让结果，最终规则以业务确认为准。","Not Run",null,"","待确认：需求仅明确 F 优先，未明确全 T 策略"],
  ["TC-RAB-032","Central","RTD/DSP · Report","Target Stocker 排序","R5｜预约状态参与最终排序","联动","验证最终选择前能识别已产生的搬入预约","初次候选取得后，STK_RSP_02 新增 reservedreticleid=对应 B 版；执行最终 Target 选择。","最终判断将 STK_RSP_02 标记 T，并优先选择仍为 F 的其他 Target。","Not Run",null,"","执行时需控制预约数据生成时点"],

  ["TC-RAB-033","Central","RTD/DSP · Balance","ReticleStockerBalance","R6｜保留原超水位触发","回归","验证超水位且无 AB Group 时原逻辑不变","RSP/BRS Stocker Reticle 数量超过设定水位，但内部不存在同一 AB Group。","按原超水位规则和原排序挑选 Reticle 执行 TransportOut。","Not Run",null,"",""],
  ["TC-RAB-034","Central","RTD/DSP · Balance","ReticleStockerBalance","R6｜AB 同仓主动触发 Balance","正向","验证未超水位也会因 A/B 同仓主动搬出","分别在 RSP 与 BRS Stocker 中准备 RETICLE000001A/B，数量未超过设定水位。","检测到同一 AB Group 后主动触发 ReticleBalance，并产生其中一块 Reticle 的 TransportOut。","Not Run",null,"","RSP、BRS 各执行一次"],
  ["TC-RAB-035","Central","RTD/DSP · Balance","ReticleStockerBalance","R6｜主动触发条件反向验证","反向","验证未超水位且无 AB Group 时不新增搬送","Stocker 数量未超水位，只有不同 Group Reticle 或单块 Reticle。","不因本次新增逻辑触发 ReticleBalance/TransportOut。","Not Run",null,"",""],
  ["TC-RAB-036","Central","RTD/DSP · Balance","ReticleStockerBalance","R6｜AB Group 内挑选","正向","验证 TransportOut 对象必须来自冲突 Group","Stocker 内有 RETICLE000001A/B 及多块其他 Reticle；原排序中其他 Reticle 更靠前。","主动 Balance 的候选被限制为发生冲突的 AB Group，并按原排序从该 Group 选出一块 TransportOut。","Not Run",null,"",""],
  ["TC-RAB-037","Central","RTD/DSP · Balance","ReticleStockerBalance","R6｜多个 AB Group 的处理","边界","验证多个冲突 Group 时仍使用原排序指标","同一 Stocker 同时存在 000001A/B 与 000002A/B 两个 AB Group，并设置原排序先后。","系统在冲突 Group 候选范围内按原排序挑选 TransportOut 对象，不随机选择或挑到无关 Reticle。","Not Run",null,"","每次 Balance 搬送数量沿用原设计"],
  ["TC-RAB-038","Central","RTD/DSP · Balance","ReticleStockerBalance","R6｜重复查询数据不触发误搬","数据处理","验证同一 ID 的重复行不被当成 A/B 两版","查询结果因 Join 出现两条 RETICLE000001A，但仓内实际只有一块。","不判为 AB Group，不触发新增主动 Balance。","Not Run",null,"",""],
  ["TC-RAB-039","Central","RTD/DSP · Balance","ReticleStockerBalance","R6｜SpecialReticle 回归","回归","验证多个相似 SpecialReticle 不触发主动 Balance","Stocker 内放入13码/15码、前缀相似的 SpecialReticle，数量未超水位。","SpecialReticle 不参与 AB 判定，不触发新增主动 Balance。","Not Run",null,"",""],
  ["TC-RAB-040","Central","RTD/DSP · Balance","ReticleStockerBalance","R6｜搬出后的再次扫描","联动","验证冲突解除后不会重复触发","A/B 同仓触发一次并成功搬出其中一块；下一周期重新执行 Balance。","原 Stocker 已无同一 AB Group 时不再因该 Group 重复触发主动搬送。","Not Run",null,"",""],
  ["TC-RAB-041","Central","RTD/DSP · Balance/Report","ReticleStockerBalance","R6｜主动 Balance 端到端分仓","联动","验证主动搬出与 Target 避让形成闭环","当前 STK_RSP_01 同仓 A/B；Target1 Flag=T、Target2 Flag=F；触发主动 Balance。","从冲突 Group 选一块 TransportOut，并优先送往 Flag=F 的 Target2；搬送后源仓与目标仓均不形成 A/B 同仓。","Not Run",null,"","核心业务验收用例"],

  ["TC-RAB-042","Central","RTD/DSP · WhereNext","ReticleWhereNext","R7｜WhereNext 新增 AB 排序","正向","验证既有对版影响 ReticleWhereNext 选仓","本地 ReticleWhereNext 的 Target1 已有 B 版、Target2 无对版；传出 A 版，其他原排序条件相同。","Target1 Flag=T、Target2 Flag=F；ReticleWhereNext 优先选择 Target2。","Not Run",null,"",""],
  ["TC-RAB-043","Central","RTD/DSP · WhereNext","ReticleWhereNext","R7｜WhereNext 识别正搬入对版","联动","验证预约搬入信息参与 ReticleWhereNext","Target1 无既有 B 版但有 B 版 reservedreticleid 正搬入；Target2 无冲突。","ReticleWhereNext 将 Target1 标记 T，优先选择 Target2。","Not Run",null,"",""],
  ["TC-RAB-044","Central","RTD/DSP · WhereNext","ReticleWhereNext","R7｜WhereNext 原排序回归","回归","验证所有候选均无 AB 冲突时原结果不变","多个 Target 均为 ExistMaskA&B=F，记录变更前原排序与选中结果。","变更后仍按原指标排序，最终 Target 与变更前一致。","Not Run",null,"",""],

  ["TC-RAB-045","Central","RTD/DSP · CentralWhereNext","CentralReticleWhereNext","R8｜CentralWhereNext 新增 AB 排序","正向","验证既有对版影响 CentralReticleWhereNext 选仓","Central 计算中 Target1 已有 B 版、Target2 无对版；传出 A 版，其他条件一致。","Target1 Flag=T、Target2 Flag=F；CentralReticleWhereNext 优先选择 Target2。","Not Run",null,"",""],
  ["TC-RAB-046","Central","RTD/DSP · CentralWhereNext","CentralReticleWhereNext","R8｜CentralWhereNext 识别正搬入对版","联动","验证预约搬入信息参与 CentralReticleWhereNext","Target1 无既有 B 版但有 B 版 reservedreticleid 正搬入；Target2 无冲突。","CentralReticleWhereNext 将 Target1 标记 T，优先选择 Target2。","Not Run",null,"",""],
  ["TC-RAB-047","Central","RTD/DSP · 三功能联动","Balance/WhereNext/CentralWhereNext","R8｜三功能判定一致性","联动","验证相同输入在三项功能中的 Flag 与选仓一致","固定同一传出 Reticle、Target 列表、既有/正搬入 Reticle 和原排序条件，依次执行三项功能。","三项功能对每个 Target 的 ExistMaskA&B 标记一致；在相同原排序条件下最终选择一致。","Not Run",null,"",""],
  ["TC-RAB-048","Central","RTD/DSP · 三功能回归","Balance/WhereNext/CentralWhereNext","R8｜非 AB 业务回归","回归","验证非14码和无对版场景不改变原业务","使用 SpecialReticle、无对版普通 Reticle 及原有常规选仓数据，记录改造前结果并执行改造后版本。","除新增 AB 避让场景外，触发条件、原排序、Target 结果及 TransportOut 行为与改造前一致。","Not Run",null,"","发布前回归"],
];

await fs.mkdir(outputDir, { recursive: true });

const workbook = Workbook.create();
const summary = workbook.worksheets.add("测试概览");
const sheet = workbook.worksheets.add("TestCase");

summary.showGridLines = false;
sheet.showGridLines = false;

// ===== 测试概览 =====
summary.getRange("A1:H1").merge();
summary.getRange("A1").values = [["Reticle Mask A/B 分仓逻辑 — 测试概览"]];
summary.getRange("A1:H1").format = {
  fill: "#1F4E78",
  font: { bold: true, color: "#FFFFFF", size: 18 },
  horizontalAlignment: "left",
  verticalAlignment: "center",
};
summary.getRange("A1:H1").format.rowHeight = 36;

summary.getRange("A3:H4").values = [
  ["系统名称","CIM 计算机集成制造系统 Fab6（二科）","功能模块","智能派工系统（RTD/DSP）","申请部门","制造部","需求日期",new Date(2026,5,23)],
  ["测试范围","ReticleStockerBalance、ReticleWhereNext、CentralReticleWhereNext","核心目标","避免 Mask A/B 版放在同一 Stocker","用例版本","V1.0","编制日期",new Date(2026,6,30)],
];
summary.getRange("A3:H4").format = {
  wrapText: true,
  verticalAlignment: "center",
  borders: { preset: "all", style: "thin", color: "#B4C6E7" },
};
for (const address of ["A3","C3","E3","G3","A4","C4","E4","G4"]) {
  summary.getRange(address).format = {
    fill: "#D9EAF7",
    font: { bold: true, color: "#1F1F1F" },
    verticalAlignment: "center",
  };
}
summary.getRange("H3:H4").format.numberFormat = "yyyy-mm-dd";

summary.getRange("A6:H6").merge();
summary.getRange("A6").values = [["执行状态"]];
summary.getRange("A6:H6").format = {
  fill: "#D9EAF7",
  font: { bold: true, color: "#1F4E78", size: 12 },
  borders: { preset: "outside", style: "thin", color: "#9FBAD0" },
  verticalAlignment: "center",
};
summary.getRange("A7:H8").values = [
  ["总用例数",null,"待执行",null,"Pass",null,"Fail / Blocked",null],
  [null,null,null,null,null,null,null,null],
];
summary.getRange("A7:B7").merge();
summary.getRange("C7:D7").merge();
summary.getRange("E7:F7").merge();
summary.getRange("G7:H7").merge();
summary.getRange("A8:B8").merge();
summary.getRange("C8:D8").merge();
summary.getRange("E8:F8").merge();
summary.getRange("G8:H8").merge();
summary.getRange("A8").formulas = [["=COUNTA('TestCase'!$A$5:$A$52)"]];
summary.getRange("C8").formulas = [["=COUNTIF('TestCase'!$J$5:$J$52,\"Not Run\")"]];
summary.getRange("E8").formulas = [["=COUNTIF('TestCase'!$J$5:$J$52,\"Pass\")"]];
summary.getRange("G8").formulas = [["=COUNTIF('TestCase'!$J$5:$J$52,\"Fail\")+COUNTIF('TestCase'!$J$5:$J$52,\"Blocked\")"]];
summary.getRange("A7:H8").format = {
  horizontalAlignment: "center",
  verticalAlignment: "center",
  borders: { preset: "all", style: "thin", color: "#B4C6E7" },
};
summary.getRange("A7:H7").format.font = { bold: true, color: "#44546A" };
summary.getRange("A8:B8").format = { fill: "#D9EAF7", font: { bold: true, color: "#1F4E78", size: 18 }, horizontalAlignment: "center", verticalAlignment: "center" };
summary.getRange("C8:D8").format = { fill: "#E7E6E6", font: { bold: true, color: "#595959", size: 18 }, horizontalAlignment: "center", verticalAlignment: "center" };
summary.getRange("E8:F8").format = { fill: "#C6EFCE", font: { bold: true, color: "#006100", size: 18 }, horizontalAlignment: "center", verticalAlignment: "center" };
summary.getRange("G8:H8").format = { fill: "#FFC7CE", font: { bold: true, color: "#9C0006", size: 18 }, horizontalAlignment: "center", verticalAlignment: "center" };

summary.getRange("A10:E10").values = [["需求编号","需求点","覆盖说明","用例数","状态"]];
summary.getRange("A11:C18").values = [
  ["R1","Mask AB 版判定","14码、非14码、混合数据"],
  ["R2","Target Stocker 取得","设备属性白名单与当前仓排除"],
  ["R3","Target Reticle 汇总","既有库存、预约搬入、空集与去重"],
  ["R4","ExistMaskA&B Flag","T/F、SpecialReticle、混合内容"],
  ["R5","Target 排序","F 优先、组内原排序、全 T 边界"],
  ["R6","ReticleStockerBalance","水位触发、主动 Balance、端到端"],
  ["R7","ReticleWhereNext","既有/预约冲突与回归"],
  ["R8","Central 与三功能一致性","Central 选仓、联动、非 AB 回归"],
];
const reqRowRanges = [[5,10],[11,20],[21,26],[27,32],[33,36],[37,45],[46,48],[49,52]];
for (let row = 11; row <= 18; row += 1) {
  const [startRow, endRow] = reqRowRanges[row - 11];
  summary.getRange(`D${row}`).formulas = [[`=COUNTA('TestCase'!$A$${startRow}:$A$${endRow})`]];
  summary.getRange(`E${row}`).formulas = [[`=IF(D${row}>0,"已覆盖","缺失")`]];
}
summary.getRange("A10:E18").format = {
  wrapText: true,
  verticalAlignment: "center",
  borders: { preset: "all", style: "thin", color: "#D9E2F3" },
};
summary.getRange("A10:E10").format = {
  fill: "#2F75B5",
  font: { bold: true, color: "#FFFFFF" },
  horizontalAlignment: "center",
  verticalAlignment: "center",
};
summary.getRange("D11:E18").format.horizontalAlignment = "center";
summary.getRange("E11:E18").conditionalFormats.add("containsText", {
  text: "已覆盖",
  format: { fill: "#C6EFCE", font: { color: "#006100", bold: true } },
});
summary.getRange("E11:E18").conditionalFormats.add("containsText", {
  text: "缺失",
  format: { fill: "#FFC7CE", font: { color: "#9C0006", bold: true } },
});

summary.getRange("G10:H10").values = [["用例类别","用例数"]];
summary.getRange("G11:G16").values = [["正向"],["反向"],["边界"],["数据处理"],["联动"],["回归"]];
for (let row = 11; row <= 16; row += 1) {
  summary.getRange(`H${row}`).formulas = [[`=COUNTIF('TestCase'!$F$5:$F$52,G${row})`]];
}
summary.getRange("G10:H16").format = {
  borders: { preset: "all", style: "thin", color: "#D9E2F3" },
  verticalAlignment: "center",
};
summary.getRange("G10:H10").format = {
  fill: "#2F75B5",
  font: { bold: true, color: "#FFFFFF" },
  horizontalAlignment: "center",
  verticalAlignment: "center",
};
summary.getRange("H11:H16").format.horizontalAlignment = "center";

summary.getRange("A20:H20").merge();
summary.getRange("A20").values = [["测试数据建议"]];
summary.getRange("A20:H20").format = {
  fill: "#D9EAF7",
  font: { bold: true, color: "#1F4E78", size: 12 },
  borders: { preset: "outside", style: "thin", color: "#9FBAD0" },
};
summary.getRange("A21:H24").values = [
  ["标准 Prefix（13码）","RETICLE000001","A版（14码）","RETICLE000001A","B版（14码）","RETICLE000001B","不同 Group","RETICLE000002A"],
  ["SpecialReticle（13码）","RETICLE000001","SpecialReticle（15码）","RETICLE000001AB","当前 Stocker","STK_RSP_01","候选 Stocker","STK_RSP_02 / STK_BRS_01"],
  ["合法 TYPE 1","RTLSTK_BARE","合法 TYPE 2","RTLSTK_XCDA","合法 TYPE 3","RTLSTK_NOXCDA","constructtype","Normal"],
  ["状态字段","测试前锁定一致快照","预约字段","requesteddeviceid / reservedreticleid","Flag","ExistMaskA&B=T/F","结果状态","Not Run / Pass / Fail / Blocked"],
];
summary.getRange("A21:H24").format = {
  wrapText: true,
  verticalAlignment: "center",
  borders: { preset: "all", style: "thin", color: "#D9E2F3" },
};
for (const col of ["A","C","E","G"]) {
  summary.getRange(`${col}21:${col}24`).format = { fill: "#F2F6FA", font: { bold: true, color: "#44546A" }, verticalAlignment: "center", wrapText: true };
}

summary.getRange("A26:H26").merge();
summary.getRange("A26").values = [["需求解读与待确认项"]];
summary.getRange("A26:H26").format = {
  fill: "#FFF2CC",
  font: { bold: true, color: "#7F6000", size: 12 },
  borders: { preset: "outside", style: "thin", color: "#D6B656" },
};
const notes = [
  "1. 需求单 2.4 写“统计 Target Stocker 所有 Reticle（2.1和2.2的 Reticle）”，与分项编号存在歧义；本 Test Case 按“Target 内既有 Reticle（2.2）+ 正搬入 Reticle（2.3）”合并判定。",
  "2. 需求明确 ExistMaskA&B=F 放在排序第一位，但未明确所有候选均为 T 时的处理。本 Test Case 暂按“不中断并沿用原排序”验证，执行前请业务/开发确认。",
  "3. 需求未给出性能阈值与批量规模，因此当前覆盖功能、边界、数据处理、联动和回归；若需性能验收，应另行补充 Stocker/Reticle 数量与响应时间指标。",
  "4. 测试前需准备可控的既有库存与搬入预约数据，并记录改造前原排序结果，便于核对新增指标只改变 AB 冲突场景。",
];
for (let i = 0; i < notes.length; i += 1) {
  const row = 27 + i;
  summary.getRange(`A${row}:H${row}`).merge();
  summary.getRange(`A${row}`).values = [[notes[i]]];
}
summary.getRange("A27:H30").format = {
  wrapText: true,
  verticalAlignment: "center",
  fill: "#FFFBEB",
  borders: { preset: "all", style: "thin", color: "#E6D9A2" },
};

summary.getRange("A32:H32").merge();
summary.getRange("A32").values = [["来源：需求申请单图片 d5815a88eaff0f8c87c24be4c8b66a7d.jpg、d144bb67c4170cb1860c9659645454bc.jpg；项目现有 TestCase 样式作为版式参考。"]];
summary.getRange("A32:H32").format = {
  wrapText: true,
  font: { italic: true, color: "#666666", size: 9 },
  verticalAlignment: "center",
};

const summaryWidths = [18,29,21,29,20,29,18,32];
for (let i = 0; i < summaryWidths.length; i += 1) {
  summary.getRangeByIndexes(0, i, 32, 1).format.columnWidth = summaryWidths[i];
}
summary.getRange("A3:H4").format.rowHeight = 36;
summary.getRange("A7:H7").format.rowHeight = 24;
summary.getRange("A8:H8").format.rowHeight = 34;
summary.getRange("A10:H18").format.rowHeight = 30;
summary.getRange("A21:H24").format.rowHeight = 34;
summary.getRange("A27:H30").format.rowHeight = 38;
summary.getRange("A32:H32").format.rowHeight = 30;
summary.freezePanes.freezeRows(1);

// ===== TestCase =====
sheet.getRange("A1:M1").merge();
sheet.getRange("A1").values = [["Reticle Mask A/B 分仓逻辑 TestCase"]];
sheet.getRange("A1:M1").format = {
  font: { bold: true, color: "#1F1F1F", size: 18 },
  horizontalAlignment: "left",
  verticalAlignment: "center",
};
sheet.getRange("A1:M1").format.rowHeight = 34;

sheet.getRange("A2:M2").merge();
sheet.getRange("A2").values = [["来源：2026-06-23 需求申请单；范围：ReticleStockerBalance、ReticleWhereNext、CentralReticleWhereNext 的 Mask A/B 不同仓逻辑"]];
sheet.getRange("A2:M2").format = {
  font: { color: "#595959", size: 10 },
  verticalAlignment: "center",
};
sheet.getRange("A2:M2").format.rowHeight = 24;

sheet.getRange("A4:M4").values = [[
  "No",
  "所属（Local/Central）",
  "Area（功能模块 Report/Balance）",
  "涉及 Macro / 共通模块",
  "逻辑变动内容",
  "类别（正向/反向/边界/联动/回归）",
  "测试内容",
  "测试情景",
  "预期结果",
  "测试结果",
  "测试日期",
  "测试 owner",
  "备注",
]];
sheet.getRange(`A5:M${4 + cases.length}`).values = cases;

const table = sheet.tables.add(`A4:M${4 + cases.length}`, true, "ReticleABTestCases");
table.style = "TableStyleMedium2";
table.showBandedRows = true;
table.showFilterButton = true;

sheet.getRange("A4:M4").format = {
  fill: "#1F4E78",
  font: { bold: true, color: "#FFFFFF", size: 10 },
  wrapText: true,
  horizontalAlignment: "left",
  verticalAlignment: "center",
  borders: { preset: "all", style: "thin", color: "#B4C6E7" },
};
sheet.getRange("A4:M4").format.rowHeight = 42;
sheet.getRange(`A5:M${4 + cases.length}`).format = {
  font: { color: "#1F1F1F", size: 9 },
  wrapText: true,
  verticalAlignment: "center",
  borders: { preset: "all", style: "thin", color: "#D9E2F3" },
};
sheet.getRange(`A5:F${4 + cases.length}`).format.horizontalAlignment = "left";
sheet.getRange(`J5:L${4 + cases.length}`).format.horizontalAlignment = "center";
sheet.getRange(`A5:M${4 + cases.length}`).format.rowHeight = 58;
sheet.getRange(`K5:K${4 + cases.length}`).format.numberFormat = "yyyy-mm-dd";

const testWidths = [16,16,24,24,28,18,28,58,58,14,14,15,30];
for (let i = 0; i < testWidths.length; i += 1) {
  sheet.getRangeByIndexes(0, i, 4 + cases.length, 1).format.columnWidth = testWidths[i];
}

sheet.getRange(`J5:J${4 + cases.length}`).dataValidation = {
  rule: { type: "list", values: ["Not Run","Pass","Fail","Blocked"] },
};
sheet.getRange(`J5:J${4 + cases.length}`).conditionalFormats.add("containsText", {
  text: "Not Run",
  format: { fill: "#E7E6E6", font: { color: "#595959" } },
});
sheet.getRange(`J5:J${4 + cases.length}`).conditionalFormats.add("containsText", {
  text: "Pass",
  format: { fill: "#C6EFCE", font: { color: "#006100", bold: true } },
});
sheet.getRange(`J5:J${4 + cases.length}`).conditionalFormats.add("containsText", {
  text: "Fail",
  format: { fill: "#FFC7CE", font: { color: "#9C0006", bold: true } },
});
sheet.getRange(`J5:J${4 + cases.length}`).conditionalFormats.add("containsText", {
  text: "Blocked",
  format: { fill: "#FCE4D6", font: { color: "#C65911", bold: true } },
});
sheet.getRange(`F5:F${4 + cases.length}`).conditionalFormats.add("containsText", {
  text: "边界",
  format: { fill: "#FFF2CC", font: { color: "#7F6000" } },
});
sheet.getRange(`F5:F${4 + cases.length}`).conditionalFormats.add("containsText", {
  text: "联动",
  format: { fill: "#DDEBF7", font: { color: "#1F4E78" } },
});
sheet.getRange(`M5:M${4 + cases.length}`).conditionalFormats.add("containsText", {
  text: "待确认",
  format: { fill: "#FFF2CC", font: { color: "#7F6000", bold: true } },
});

sheet.freezePanes.freezeRows(4);
sheet.freezePanes.freezeColumns(1);

// ===== 校验与导出 =====
const summaryCheck = await workbook.inspect({
  kind: "table",
  range: "测试概览!A1:H18",
  include: "values,formulas",
  tableMaxRows: 18,
  tableMaxCols: 8,
  maxChars: 12000,
});
console.log("SUMMARY_CHECK");
console.log(summaryCheck.ndjson);

const caseCheck = await workbook.inspect({
  kind: "table",
  range: "TestCase!A1:M12",
  include: "values,formulas",
  tableMaxRows: 12,
  tableMaxCols: 13,
  maxChars: 12000,
});
console.log("CASE_CHECK");
console.log(caseCheck.ndjson);

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
});
console.log("FORMULA_ERROR_SCAN");
console.log(errors.ndjson);

for (const [sheetName, range, fileName] of [
  ["测试概览", "A1:H32", "preview_测试概览.png"],
  ["TestCase", "A1:M28", "preview_TestCase_1.png"],
  ["TestCase", "A29:M52", "preview_TestCase_2.png"],
]) {
  const preview = await workbook.render({
    sheetName,
    range,
    scale: 1,
    format: "png",
  });
  await fs.writeFile(`${outputDir}/${fileName}`, new Uint8Array(await preview.arrayBuffer()));
}

const exported = await SpreadsheetFile.exportXlsx(workbook);
await exported.save(outputFile);

const persisted = await SpreadsheetFile.importXlsx(await FileBlob.load(outputFile));
const finalCheck = await persisted.inspect({
  kind: "workbook,sheet,table",
  maxChars: 5000,
  tableMaxRows: 3,
  tableMaxCols: 13,
  tableMaxCellChars: 80,
});
console.log("FINAL_WORKBOOK_CHECK");
console.log(finalCheck.ndjson);
console.log(`OUTPUT ${outputFile}`);
