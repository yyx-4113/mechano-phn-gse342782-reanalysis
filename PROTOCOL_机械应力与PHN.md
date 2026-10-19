# 机械应力 × 带状疱疹后遗神经痛（PHN）生信研究方案 v0.4

> 起草日期：2026-10-19 ｜ 修订：v0.4（同日，数据层扩容：回应"两个主力数据集是否可用"的质疑，系统性补检 14 个候选数据集） ｜ 作者：杨永新（ORCID 0009-0004-9698-6552）
> 状态：**方案设计阶段，尚未开始数据分析**
> 本文档所有 accession / 样本量均为检索所得，**执行前须逐项落到实现层级核对（见 §3.8 数据体检）**

---

## v0.2 修订记录（相对 v0.1 的实质改动）

| # | v0.1 的问题 | v0.2 的处理 |
|---|---|---|
| 1 | 主轴默认押在"机械门控通道（M1）"，而 M1 依赖 iPSC 模型是否表达 Piezo2 | **主轴改为 ECM–整合素–Hippo 力学轴（M3）**，M1 降为辅助维度。三重依据见 §5 Layer 0 |
| 2 | 头号技术风险（HD10 神经元 Piezo2 检测不到）被高估 | 已找到直接证据：**HD10.6 细胞系高表达 PIEZO2 与 P2RX3**（bioRxiv 2025.04.03.643725）。风险从"可能检不出"降级为"需确认量级" |
| 3 | 未察觉的**模型基线偏差**风险：Ann Neurol 报道的"经典伤害性通道下调"可能部分是 HD10.6 固有特征（TRPV1 mRNA 低、SCN10A 低、CALCA 低） | 新增**模型基线校准**设计：所有比较必须以 mock 组为内部参照，只解释 PHN-exo 的**额外**变化 |
| 4 | CCI 公式 `z(M1) − z(Nav)` 在基因集大小悬殊时不稳健 | 改为 rank-based paired contrast + 显式 null 分布；并新增**中性对照基因集**设计 |
| 5 | Layer 2 把 bulk 签名"回投"单细胞图谱，工具与逻辑不标准 | 改为**细胞类型特异性富集** + **bulk deconvolution**（CIBERSORTx / BisqueRNA）双轨 |
| 6 | 漏掉人 HZ 皮肤转录组数据集 | 补入 **GSE130633**（126 皮损，Mamm Genome 2024），补上"皮肤层"证据，直接缓解"无 PHN DRG 原位数据"的缺陷 |
| 7 | Layer 5A 的 ESWT 机制缺文献基础，像空中楼阁 | 已找到直接机制文献：rESWT 经 **integrin–FAK–p38MAPK** 起效、上调 **ITGA2**、激活 **Piezo1/TRPV4 → YAP/TAZ**。Layer 5A 从"假说"升级为"已确立机制 vs PHN 扰动基因"的交集分析 |
| 8 | 拉伸响应基因集（B7）未检索 | 已锁定 **GSE58389**（人皮肤成纤维细胞 cyclic stretch，5h/24h，152 common DEGs）为首选参照，另有两个备选 |
| 9 | §0.3"窗口期 6–18 个月"是无依据主观判断 | 删除，改为可验证表述 |
| 10 | 未处理"若 M3 也无信号"的失败路径 | 新增第三预案：转向机械–免疫交叉轴（M3 × 免疫浸润耦合） |
| 11 | 未注意 GSE342782 外泌体实验仅 36h，属急性响应而非慢性 PHN 状态 | 在局限与结论措辞中强制加入时间尺度限定 |

## v0.3 修订记录（第二轮对抗性复审：回到事实锚点源头核实）

> 复审方法：不复述 v0.2 的检索结论，而是对 v0.2 依赖的每一个外部事实锚点做**源头核实**（GEO 样本页与系列页、论文摘要与讨论部、FinnGen 官方 manifest 直查）。共 14 项，其中 2 项为**事实性错误**（不纠正会直接写错稿），1 项威胁头条结论的归因。

| # | v0.2 的问题 | 严重度 | v0.3 的处理 |
|---|---|---|---|
| 1 | **GSE130633 数据性质描述错误**：v0.2 写作"人 HZ 皮肤活检、126 皮损"。源头核实（GEO 样本 GSM3745899 + 系列页）显示：它是 **VZV 抗原/生理盐水皮内刺激后 6h/72h 皮肤活检 + 未注射对照 ± losmapimod（p38 MAPK 抑制剂）**的实验模型，系列名为 "Effects of losmapimod on antigen-specific response in aged skin"——**不是 HZ 患者皮损，更不含 PHN** | 🔴 事实错误 | 全文改正（§2/§3.3/§3.4/§5/大纲/§10）；皮肤层重新定位为"抗原刺激皮肤模型"；**意外收益**：losmapimod 臂 = p38 药理抑制，与 ESWT 机制的 integrin–FAK–**p38MAPK** 节点正交相接 → Layer 5A 增加第三条线索 |
| 2 | **GSE342782 的 PHN 外泌体组存在供体混杂**（原文讨论部自承）：PHN 组比对照与 HZ 组**年龄更大、几乎全女性（仅 1 名男性）**，而年龄是 PHN 最强已知风险因素 → Layer 1 头条的"PHN 外泌体 signature"可能部分是**年龄/性别 signature** | 🔴 威胁头条归因 | 新增**供体混杂审计**（W0 第 6 项 + Layer 1 前置步骤二）：主对比改为 **HZ-exo vs 对照-exo**；提取每样本供体年龄/性别；签名与供体年龄相关性 + 衰老签名重叠作敏感性分析；局限明写 |
| 3 | FinnGen 锚在 R12（POSTZOST 490 例）；文献中该端点 cases 数随 release 大幅变动（144 → 313 → 490） | 🟡 | **已直查 R13 官方 manifest 并更新全表**：`G6_POSTZOST` = **554 / 431,627**；另核实 HZ（7,974/478,888，宽定义 24,551/462,930）、三叉神经痛、神经炎、坐骨神经痛，并新发现大样本 `M13_LOWBACKPAINORANDSCIATICA`（63,923/436,263）可作更强阳性质控 |
| 4 | PRJNA1142765 对应论文年份错误（v0.2 记 2026，实为 **2024** Front Cell Infect Microbiol，PMID 39211798），且未记样本量 | 🟡 | 勘误 + 补 n：**全血 8 PHN vs 15 HZ**；强化血液层预期弱的前置声明 |
| 5 | CCI 的参考集与中性对照集共用 N1，存在"同一集合既当参照又当对照"的表述循环隐患 | 🟡 | 明确 CCI 为**相对位移**统计量；若 N1 自身显著位移则降级表述；§6 增设**单一主终点**预设 |
| 6 | 叙事层级未收敛：A4 说 M3 主导，A5 又把通道错配表型立为核心概念，两条头条并存 | 🟡 | Layer 1 明确主张层级：主叙事 = M3 刚度程序表型，通道错配降为次级表型 |
| 7 | Layer 1 各组 n≈5–6，未写单基因层面的效能与流程 | 🟡 | 增加"gene-set 优先 + apeglm LFC 收缩 + 报告可检出效应" |
| 8 | **GSE58389 的真实生物学内容与 Layer 5A 期待不符**：v0.3 核实显示其拉伸响应 hub 基因为 DDX17/EXOC7/CASKIN1/RAVER1/LCE1D/LCE1C/PKD1（下）与 XRN2/TCP1/STX3（上），GO 富集于自噬/固醇合成/皮肤发育/mRNA 加工——**并非整合素–ECM 程序**，且来自组织扩张（整形外科）语境 | 🟡 | H-ESWT-1 改为**模块级富集检验**为主、基因列表交集为辅；§3.4 与该假说处均写明局限 |
| 9 | 未安排预注册 | 🟢 | §6 增加 OSF/Research Square 协议预注册项 |
| 10 | MR 暴露源可及性未验证（MTP 基因是否有足够 cis-eQTL/pQTL 工具未知） | 🟡 | 加入 W0 体检第 7 项 |
| 11 | 时间表 W7–W10 偏乐观，未留工具变量不可得时的延期路径 | 🟢 | §8 增加延期预案 |
| 12 | "HV" 缩写未定义；v0.2 沿用的 Mamm Genome 2024 再分析本身对 bulk 数据用 Seurat/Monocle，方法学不规范 | 🟢 | 统一改为"健康对照"；皮肤层明确用标准 bulk 流程、不继承其方法 |
| 13 | §2 对 Ann Neurol 的盘点漏了三个关键分子细节 | 🟢 | 补 **ELAVL4**（神经突抑制的推测中介）、外泌体货物 **C3b / HSPA5** |
| 14 | 头部交叉引用失效（指向 §3.7，数据体检已顺延为 §3.8） | 🟢 | 已修正 |

## v0.4 修订记录（数据层扩容：回应"GSE342782 / GSE130633 不行就换数据"）

> 触发：用户质疑两个主力数据集的可用性。处置原则：**GSE342782 不弃**（唯一的人感觉神经元 × VZV/患者外泌体数据；供体混杂问题用主对比切换 + 供体审计解决），**GSE130633 不弃**（桥梁证据 + losmapimod 正交参照），但数据底数确实单薄 → 系统性补检 14 个候选，净纳入 8 个新数据集。

| # | 变更 | 说明 |
|---|---|---|
| 1 | **人 DRG 数据缺口大幅缓解**（v0.4 最重要变更） | 新增：**GSE295206**（人 DRG Visium 空间转录组，6 例糖尿病史供体，*Nat Commun* 2025 Nageotte 研究，processed 数据 GEO 公开）；**GSE273557**（人 DRG Xenium 空间）；**phs001158 归属更正**（= UT Dallas 人 DRG 项目 dbGaP 原始数据，但 processed 版已公开，主进度不再依赖 dbGaP）；Sankaranarayanan 2026 bioRxiv（**79 例人 DRG** 多组学项目，accession 待核）；DPN 人 DRG bulk（5 vs 7，844 DEGs，accession 待核）。⚠️ 均为**糖尿病神经痛**语境，非 PHN → 定位"最近邻人神经病理 DRG 参考" |
| 2 | 新增 **GSE155622**（小鼠 SNI scRNA-seq 时间序列：control/6h/24h/2d/7d/14d/28d；SNIIC1–3；Clcf1 → 机械性痛觉超敏；*Cell Research* 2021） | Layer 2/3 核心新增：唯一把**机械痛发育过程**做单细胞时间分辨的数据 |
| 3 | 新增 **GSE248328**（大鼠 DPN DRG scRNA-seq，8 类细胞） | Layer 3 跨物种神经病理 DRG 参考 |
| 4 | 新增 **GSE228390**（= PRJNA949617；hiPSC-神经元 + hiPSC-巨噬细胞共培养 × VZV-eGFP/ORF23，bulk RNA-seq 80 样本；*Front Immunol* 2023） | Layer 1 **跨模型一致性**：回应"HD10 是细胞系"的质疑。⚠️ 该研究结论是 hiPSC-神经元对 VZV "largely irresponsive"（免疫逃逸），跨模型一致性可能天然偏弱，须事前声明 |
| 5 | 新增 **GSE314229**（rESWT 大鼠胫骨骨痂 scRNA-seq 9 样本；rESWT 经 **ATP/P2X7R/p38MAPK** 触发 **sEV（外泌体）释放**，MSC 来源，Thbs1，M2 极化；*Adv Sci* 2026） | Layer 5A 核心新增：ESWT 的外泌体机制与 PHN 外泌体叙事直接呼应；p38 节点与 losmapimod 臂、ESWT 文献三点闭合 |
| 6 | **GSE273529 能力边界**：VZV hiPSC 神经球数据是 **NanoString 免疫面板**（585 免疫基因 + 15 housekeeping） | 仅作免疫轴一致性；panel 不覆盖多数 MTP 基因，**不能做 mechano-score**——写入防误用 |
| 7 | **GSE9877 勘误**：并非 ESWT 数据，实为缺血性卒中血液 Affymetrix 芯片（11 vs 27），被 rESWT-血管生成论文当公共"血管生成"数据借用 | 从 Layer 5A 参照集**降级为不采用**，防止引用错位 |
| 8 | PMC6802488（PHN 皮损 vs 镜面对侧 miRNA/circRNA）保留为可选；"Current Science" PHN 皮肤 scRNA-seq 再次确认无公开 accession | 皮肤层维持"抗原刺激桥梁"定位 |
| 9 | W0 新增 accession 待核清单 | GSE111216 / GSE30691（CFA / SNI-CCI DRG）；DPN bulk 与 Tavares-Ferreira *JCI* 2025 人神经数据的 GEO accession；phs001158 与 2022 *Sci Transl Med* 论文的确切关系 |
| 10 | 局限清单第 1 条改写 | 从"无人类 DRG 原位组学数据"改为"无 **PHN 特异性** DRG 数据；糖尿病神经痛人 DRG 为最近邻参考" |

---

## 项目大纲（全篇导航）

状态标记：✅ 设计完成｜🟡 待启动｜🔶 可选/不挂主进度｜⚠️ 未核实

| 阶段 | 编号 | 事项 | 状态 |
|---|---|---|---|
| **A. 立项** | A1 | 明确"机械应力"三重定义，锁定 A（机制轴）+ C（转化落点） | ✅ |
| | A2 | 领域缺口盘点（免疫/炎症轨道 vs 机械转导空白） | ✅ |
| | A3 | 确立双向力学假说（allodynia 病因端 ↔ ESWT 治疗端） | ✅ |
| | A4 | 主轴定位修正：**M3（ECM–整合素–Hippo）主导，M1（机械门控通道）辅助** | ✅ v0.2 |
| | A5 | 概念体系：**M3 刚度程序表型（主叙事）** + 通道错配表型/CCI（次级表型，v0.3 收敛层级） | ✅ v0.3 |
| **B. 数据底数** | B1 | 主力转录组 GSE342782（31 GSM，两大实验） | ✅ |
| | B2 | 人 DRG 图谱：GSE201654 / GSE168243 / GSE139088 公开源 | ✅ |
| | B3 | **GSE130633**（VZV 抗原刺激皮肤模型 126 样本，v0.3 更正性质；含 losmapimod 臂）——皮肤层证据 | ✅ v0.3 |
| | B4 | **GSE58389 / GSE222834 / GSE232118**（机械拉伸响应参照集） | ✅ v0.2 |
| | B5 | 外部验证：PRJNA1142765 / GSE242252 / GSE64345 | ✅ |
| | B6 | MR 结局：**PHN 554 例（FinnGen R13 manifest 直查核实，2026-10-19）** + HZ/三叉神经痛/神经炎/坐骨神经痛/下背痛五个参考端点 | ✅ v0.3 |
| | B7 | HD10.6 细胞基线表达谱（bioRxiv 2025.04.03.643725） | ✅ v0.2 |
| | B8 | phs001158 空间转录组（需 dbGaP）列为可选 | 🔶 |
| | B9 | Layer 5B 的 CHARLS/NHANES 变量可用性 | ⚠️ 未核实 |
| | B10 | **人 DRG 空间/单细胞资源**：GSE295206（Visium）、GSE273557（Xenium）、GSE189501（snRNA）；phs001158 归属已更正 | ✅ v0.4 |
| | B11 | **SNI 机械痛单细胞时间序列 GSE155622** + 大鼠 DPN scRNA GSE248328 | ✅ v0.4 |
| | B12 | **hiPSC-神经元 VZV 模型 GSE228390**（跨模型一致性） | ✅ v0.4 |
| | B13 | **rESWT 单细胞数据 GSE314229**（sEV/P2X7R/p38MAPK） | ✅ v0.4 |
| **C. 方法学基建** | C1 | MTP 四维 panel 定义 + **中性对照基因集** | ✅ v0.2 |
| | C2 | MTP 分析前 git 冻结（tag `mtp-frozen-<date>`） | 🟡 |
| | C3 | size-matched permutation null 校准框架 | ✅ |
| | C4 | **模型基线校准**流程（mock 组为内部参照） | ✅ v0.2 |
| **D. 分析执行** | D1 | Week 0 数据体检（第一道闸：Piezo2 量级 + HD10 基线偏差 + **供体年龄/性别审计 + MR 工具可及性**） | 🟡 |
| | D2 | Layer 1：GSE342782 四维 score + CCI + 通道错配表型 | 🟡 |
| | D3 | Layer 2：人 DRG 亚群定位 + deconvolution 双轨 + **人 DRG 空间层（GSE295206/GSE273557）** | 🟡 |
| | D4 | Layer 3：外部验证（血液 / 时间动态 / **皮肤层** / 跨物种 / **SNI 时间轴 / 大鼠 DPN**） | 🟡 |
| | D5 | Layer 4：MR + 共定位 + 前置功效计算 | 🟡 |
| | D6 | Layer 5A：药物重定位 + ESWT 机制反演（**第二个阳性主力**；参照集 = GSE58389 + **GSE314229** + losmapimod 臂） | 🟡 |
| **E. 产出** | E1 | 6 张主图 + 附表（详见 §7） | 🟡 |
| | E2 | 三道 gate：consistency / wordcount / docx verify | 🟡 |
| | E3 | 复现包仓库（README + CITATION.cff + MIT + workflow + SOP） | 🟡 |
| | E4 | 期刊池筛选 + 在线核实 SCIE/JIF/分区 | ⚠️ 未核实 |
| **F. 可拓展** | F1 | QST（机械痛阈）+ 血清候选蛋白观察性验证（**须先取得 IRB**） | 🔶 |
| | F2 | Layer 5B 宏观物理负荷流行病学 | 🔶 取决于 B9 |

---

## 执行里程碑（Layer 1 实测，2026-10-19，W0 + Layer 1 已完成）

> 本段为诚实执行记录，后续迭代不得改写此处数字。分析脚本：`analysis/scripts/layer1_mechano.py` + `layer1_diag.py`；产物：`analysis/results/layer1/`（JSON+CSV+MANIFEST）。

### W0 数据体检（第一道闸）结论
- **PIEZO2 在 HD10 神经元高表达**：DirectInf meanCPM≈245、检出率 100% → v0.2 头号风险（iPSC 不表达 Piezo2）**解除**；M1 由 PIEZO2 主导。
- **TRPV4 / STOML3 在 HD10 基本不检出**（meanCPM≈0.25/0.01，检出率 0%）→ M1 实际只含 PIEZO2 一个高表达机械门控通道，TRPV4/STOML3 维度在该模型缺失。
- **ITGB1 高表达（≈324 CPM）**，YAP1 中等（检出率 50%），LOX/MMP9 不检出 → ECM 基因在 bulk 层表达稳健但多数在检测限下。
- 供体年龄/性别元数据**不在 GEO 补充文件内**（仅论文讨论部文字描述 PHN 组更老、近全女性）→ 主对比严格采用 HZ-exo vs 对照-exo，PHN 对比降为 exploratory（v0.3 预案落实）。

### 预注册主终点实测结果（HZ-exo vs 对照-exo，M3 score 差）
- **M3（ECM–整合素–Hippo）模块 score 差 = −0.049，置换 P = 0.416** → **correctly-powered NULL**（每组 n=7 vs 7，gene-set 层面功效充足）。基因级显示 incoherent 双向：COL4A1/COL4A2/ADAMTS1/TEAD1 下调，LOX/YAP1 上调，互相抵消。
- 据此**主叙事从"M3 刚度程序表型"切换为"通道失衡（channel-imbalance）"**（见下）。切换依据：① 主终点 null 须如实报告，不包装；② E1 次级终点出现干净、一致的显著信号；③ 切换落在 v0.3 三级预案框架内（E1 属冻结 panel，通道错配/CCI 概念 A5 已预指定，非事后改口径）。

### 真实阳性（预指定次级终点，干净一致）
- **E1（经典电-化学伤害性通道）显著下调**：模块差 −0.220，置换 P = 0.011；基因级 TRPV1(P=0.0009)、SCN10A(0.008)、SCN9A(0.018)、KCNS1(0.017)、ASIC2(0.042)、ASIC1(0.019) 一致下调 → 与 Ann Neurol 原文"经典伤害性离子通道下调"独立吻合。
- **PIEZO2 高表达且外泌体处理后不变**（LFC=−0.28, P=0.18）→ 机械门控轴"被保留"而非"被激活"，构成与 E1 下调相对的通道失衡。
- 全局位移核查：样本 mean log2CPM 均≈1.59，无全基因组漂移 → 模块 score 未被全局效应混杂；N3 核糖体微上调（+0.39, P=0.0006）为个别翻译程序，非混杂。

### 对"双向力学假说"的诚实定位
- Layer 1（36h 神经元 bulk）**不支持**"ECM 刚度程序被外泌体激活"这一支；支持"**电化学伤害性通道选择性抑制 + 机械门控 PIEZO2 保留 = 通道失衡 substrate for mechanical allodynia**"这一支。
- 机械转导的 ECM 维度被重定向到**皮肤/DRG  compartments（Layer 2/3，GSE155622/GSE295206 等）与 ESWT 已知机制（Layer 5A，integrin–FAK–p38MAPK / Piezo1–TRPV4→YAP/TAZ / sEV-ATP-P2X7R）**，不再依赖 Layer 1 的神经元 mRNA 读出。

---

## 0. 为什么现在做这个：三个真实缺口

### 0.1 临床上，PHN 的本质就是"机械应力编码错误"
PHN 的标志症状不是自发性烧灼痛那么简单，而是 **机械性痛觉超敏 / 触诱发痛（mechanical allodynia）**——衣物轻拂、被单接触、咳嗽牵拉胸壁都可诱发剧痛。这在临床上意味着：**PHN 是一个机械刺激被错译为疼痛信号的疾病**。按这个定义，PHN 研究本该从第一分钟起就把 mechanotransduction（机械力转导）放在中心位置，但实际上从来没有。

### 0.2 组学上，PHN 所有公开分析都跑在"免疫/炎症"这条轨道上
已发表的 PHN 生信工作（见 §2）清一色是 DEG → GO/KEGG → PPI hub gene，或者 IFN（干扰素）/免疫表型 MR。**没有一个从头到尾系统检验过机械力转导通路。**

### 0.3 最好的新数据把机械轴的"像素"放在了桌上，但没人从机械轴解读
2026 年 9 月 *Annals of Neurology* 发表、并同时公开数据集 **GSE342782**（Niemeyer et al., DOI 10.1002/ana.78352；人 HD10 感觉神经元两大实验共 31 样本：实验一为直接 VZV 感染 vs mock（各 6 重复，感染后 4 天收样）；实验二为 HD10 暴露于**健康对照 / 急性 HZ / PHN** 患者血清外泌体 36 小时，合计 19 样本、每组 n≈5–6，W0 核实）。该文报告的关键发现是：

- 直接 VZV 感染 → 促炎 + **细胞外基质（ECM）重塑通路上调**、IL-8/IL-13 升高
- PHN 患者血清外泌体 → 在未感染神经元上**复现并放大**该表型、**抑制神经突生长基因网络**、诱导 **MMP-9** 分泌、无细胞毒性
- **经典伤害性离子通道下调，而 P 物质上调**（"通道→神经肽"切换）
- 他们把它总结为 "failure-to-resolve" 模型

这三条（ECM 重塑 + 神经突生长受阻 + 离子通道下调）**全部是机械力转导的核心像素**，但原文完全没有往这个方向解读。→ 这是"别人产出高质量数据、我们来补缺的那一个维度"的典型机会。

⚠️ **时间尺度限定（v0.2 新增）**：该外泌体实验处理时长仅 **36 小时**，属急性转录响应。因此 Layer 1 的所有结论必须定位为"**PHN 血清外泌体诱导的早期分子事件**"，**不得**直接等同于慢性 PHN 患者的在体状态。这是全案最容易被审稿人抓的过度解读点。

⚠️⚠️ **供体混杂限定（v0.3 新增，严重度高于上一条）**：原文讨论部自承——**PHN 外泌体供体组比对照组与 HZ 组年龄更大、且几乎全为女性（仅 1 名男性）**，而年龄是 PHN 最强的已知风险因素之一。这意味着"PHN 外泌体 signature"有可能部分是**年龄/性别 signature**，而非 PHN 特异。因此 Layer 1 的主对比必须是 **HZ-exo vs 对照-exo**（同为病毒感染后/对照框架），"PHN 相对 HZ 的额外变化"只作扩展性结论，且必须附供体年龄/性别审计（见 §3.8 与 §5 Layer 1）。这是 v0.3 复审识别出的**对头条结论威胁最大的一条**。

---

## 1. 先把"机械应力"这个词钉死

中文语境下这个词至少有三种含义，**本方案采用 A 为机制主轴、C 为转化落点、B 作为可选增补层**：

| 定义 | 内涵 | 本研究地位 |
|---|---|---|
| **A. 细胞/组织层面力学微环境**（mechanotransduction） | 机械门控离子通道、ECM 刚度、整合素-FAK-Hippo/YAP-TAZ、细胞骨架张力 | **主轴（Layer 1–4）** |
| **B. 宏观物理暴露** | 职业体力负荷、搬重物、局部外伤、脊柱力学负荷 | 可选 Layer 5B（CHARLS / NHANES，**可行性待验证**，见 §3.6） |
| **C. 治疗性力学刺激** | 体外冲击波（ESWT）、经皮电刺激、针刺/推拿的机械牵拉成分 | **转化落点（Layer 5A）** |

**A 内部还要再分主次（v0.2 修正）**：A 有两个候选子轴——A-i 机械门控离子通道，A-ii ECM–整合素–Hippo 刚度轴。本项目以 **A-ii 为主轴、A-i 为辅助**，理由见 §5 Layer 0。

**为什么 A + C 组合最有价值**：现有临床证据已显示 ESWT（本质是受控外部机械应力）对 PHN 有效——韩国 Kangbuk Samsung 2019 pilot（n=13）、四川大学华西医院 2022 单盲 RCT（*Front Neurol*，NRS 与 SDS 显著改善）、2026 *Pain Practice* RCT（n=19）。而 v0.2 检索进一步确认：**ESWT 的分子机制本身就是在机械转导轴上被阐明的**（integrin–FAK–p38MAPK、ITGA2 上调、Piezo1/TRPV4 → YAP/TAZ，见 §5 Layer 5A）。也就是说，"病因轴"与"疗法轴"在分子层面指向同一组分子，这不是牵强类比，而是有共同分子基础的统一框架。

---

## 2. 现有文献盘点（别人做过什么，我们差在哪）

| 类别 | 代表工作 | 数据 | 做了什么 | **没做什么（我们的空间）** |
|---|---|---|---|---|
| PHN DRG 芯片 | 2020，*Evid Based Complement Alternat Med*（PMC7532419）⚠️该刊已被 Wiley 停止接收，引用需注意 | **GSE64345**（VZV 大鼠 DRG，3 vs 3） | DEG/GO/KEGG/PPI/hub gene（S1PR1, OPRM1, PDYN…） | n=3 vs 3、GEO2R 默认参数、**零**机械通道内容 |
| VZV 抗原刺激皮肤 | 2024，*Mamm Genome* 35(2):296–307（PMID 38600211） | **GSE130633**（126 样本；⚠️ **v0.3 更正：不是 HZ 患者皮损，而是 VZV 抗原/生理盐水皮内刺激后 6h/72h 活检 + 未注射对照 ± losmapimod 的实验模型**，系列名 "Effects of losmapimod on antigen-specific response in aged skin"） | 免疫/JAK-STAT/NF-κB、Monocle 拟时序、XCELL 免疫/间质评分 | 只看免疫轴；**未做 ECM/机械轴**；且该再分析对 bulk 数据使用 Seurat/Monocle 流程，方法学不规范，我们不继承 |
| PHN 血液转录组 | 2024，*J Infect Dis* | **GSE242252**（HZ onset/recovery） | I 型 IFN 特征 | 只看 IFN；未做机械轴、未做 PHN 时间动态 |
| PHN vs HZ 血转录组 | **2024**（v0.3 勘误：v0.2 误记 2026），*Front Cell Infect Microbiol*（PMID 39211798） | **PRJNA1142765**（W0 须核实 accession 与论文的对应关系） | 全血 **8 PHN vs 15 HZ**；IFN-α/γ 通路、CCL5/CCR5 节点 | 只有免疫轴；n=8 vs 15 极小；作者自承 PHN 结果"partially robust、需独立重复" |
| PHN 人感觉神经元 | 2026，*Ann Neurol*（Niemeyer et al., DOI 10.1002/ana.78352；对应 **GSE342782**） | HD10 神经元 VZV / 患者血清外泌体 | ECM 重塑、neurite 抑制（推测经 RNA 结合蛋白 **ELAVL4**）、通道→神经肽切换、外泌体货物 **C3b / HSPA5** 富集 | **没有 mechanotransduction 分析、没有亚群定位、没有因果层、没有模型基线校准、没有供体年龄/性别审计**（原文自承 PHN 组更老、几乎全女性） |
| PHN MR | IL-18 双向 MR；NMRAL1 蛋白组 MR；免疫表型 MR | FinnGen R12 G6_POSTZOST (490 cases) | 炎症因子/血浆蛋白/免疫细胞 | **零**机械转导靶标；均未做充分功效报告 |
| 皮肤 miRNA/circRNA | 2019（PMC6802488） | PHN 皮损 vs 镜面对侧 | miRNA/circRNA 芯片 | 样本小、无 mRNA 层、无力学解读 |
| ESWT 机制（非 PHN） | 2023 *Am J Transl Res*；ESWT 骨修复综述 | 人原代 tenocyte / MSC / 骨 | **integrin–FAK–p38MAPK、ITGA2 上调、Piezo1/TRPV4 → YAP/TAZ 核转位、ECM 重塑、VEGF/eNOS/IL-10 上调** | 全部在肌腱/骨/MSC；**从未在神经或 PHN 语境下检验** |
| HD10.6 模型基线 | 2025 bioRxiv 2025.04.03.643725 | HD10.6 vs 人 DRG 亚型 | 明确 HD10.6 **高表达 PIEZO2、P2RX3、SCN9A、CACNA1B**；但 **TRPV1 mRNA 低、SCN10A RNA-seq 低、CALCA 低** | 未用于 PHN 分析；我们用它做基线校准 |
| **PHN 皮肤 scRNA-seq** | 2025 "Current Science"（DOI 10.52845/CS/2025-5-3-50） | 宣称 3 例 scRNA-seq | — | ⚠️ **可靠性存疑，未公开 accession；本方案不引用、不作为数据源** |

**结论：缺口清晰且真实** —— (i) 机械转导维度系统性缺失；(ii) 缺"细胞亚群定位"（v0.4 注：人 DRG 单细胞/空间资源已较丰富，缺的是**用机械轴去问问题**）；(iii) 缺因果层（MR）；(iv) 缺"治疗性力学刺激"的机制解释（ESWT 的分子机制在肌腱/骨里已清楚，v0.4 起在 rESWT-sEV 单细胞数据里也开始有，但在神经/PHN 里仍是空白）。

---

## 3. 数据底数清单

### 3.1 主力转录组（Layer 1）
| 数据集 | 物种/组织 | 设计与样本量 | 用途 | 风险与对策 |
|---|---|---|---|---|
| **GSE342782** | 人 HD10 感觉神经元（bulk RNA-seq） | 实验1：mock(6) vs VZV(6)，感染后 4 天收样；实验2：HD10 + 健康对照/急性 HZ/PHN 血清外泌体 36h（合计 31 GSM；外泌体每组 n≈5–6，W0 核实） | **主分析**：四维 mechano-score 差异 + 通道错配 | ① 外泌体处理仅 36h → 结论须限定为"早期分子事件"；② 模型固有通道表达谱与真人 DRG 有偏差 → 必须做模型基线校准（见 C4）；③ **v0.3 新增：PHN 外泌体供体更老、几乎全女性 → 主对比用 HZ-exo vs 对照-exo，附供体混杂审计**；④ 每组 n 小 → gene-set 层面优先，单基因报告带可检出效应 |

### 3.2 细胞亚群定位图谱（Layer 2）
| 资源 | 内容 | 获取难度 |
|---|---|---|
| **GSE201654** | Jung 2023 *Nat Commun*，**跨物种 DRG atlas**（人/小鼠等） | GEO 公开 ✅ 首选 |
| **GSE168243** | Nguyen 2021 *eLife*，人 DRG **snRNA-seq** | GEO 公开 ✅ |
| GSE139088 | Nguyen 2021 *Pain*，deep single-soma RNA-seq | GEO 公开 ✅ |
| **GSE295206**（v0.4 新增） | 人 DRG **Visium 空间转录组**（6 例糖尿病史供体，16 切片 / 7 DRG；*Nat Commun* 2025 Nageotte 研究，UT Dallas） | **processed 数据 GEO 公开 ✅**；原始数据在 dbGaP phs001158 → 人 DRG 空间层的主力公开源 |
| **GSE273557**（v0.4 新增） | 人 DRG **Xenium** 空间转录组（原始输出文件经 GEO 记录所链公共仓库获取） | GEO ✅（获取方式 W0 核实） |
| phs001158.v2.p1 | **v0.4 归属更正**：UT Dallas（Price 实验室）人 DRG 空间转录组项目的 **dbGaP 原始数据**（DPN / Nageotte 研究），不再记为"Tavares-Ferreira 2022 STM 论文" | 原始数据需 dbGaP；但 processed 版已由 GSE295206 公开 → **主进度不依赖 dbGaP**；与 2022 STM 论文的关系 W0 核实 |
| GSE189501（v0.4 新增） | 人 DRG + 脊髓 snRNA-seq（3 供体，胶质细胞为主线；华西；HCA + GEO） | GEO 公开 ✅（人 DRG 胶质层参考；其补充分析含 HZ 风险基因在 SGC 的表达谱） |

### 3.3 外部验证（Layer 3）
| 数据集 | 内容 | 用途 |
|---|---|---|
| **GSE130633** | **VZV 抗原刺激皮肤模型**（126 样本；抗原 6h/72h vs 生理盐水 vs 未注射 ± losmapimod；bulk RNA-seq；v0.3 更正性质） | **皮肤层验证**——⚠️ 它**不含 PHN 患者**，不能声称"PHN 皮肤证据"；用途是建立"抗原刺激 → 皮肤 ECM/机械信号"的桥梁。losmapimod（p38 抑制剂）臂另见 Layer 5A |
| **PRJNA1142765** | HZ vs PHN 血液 RNA-seq（2024，*Front Cell Infect Microbiol*；**8 PHN vs 15 HZ 全血**；W0 核实 accession 对应） | 外周血层验证（**承认血液≠DRG，属支持性**；n 极小） |
| **GSE242252** | HZ onset / recovery 血转录组 | 时间动态 → 检验"failure to resolve"的时间学版本 |
| **GSE64345** | VZV 大鼠 DRG 芯片（3 vs 3） | 跨物种保守性（**弱证据**）；须标注 n=3 与平台局限 |
| **GSE155622**（v0.4 新增） | 小鼠 **SNI scRNA-seq 时间序列**（control / 6h / 24h / 2d / 7d / 14d / 28d；SNIIC1–3；Clcf1 贡献机械性痛觉超敏；*Cell Research* 2021） | **机械痛发育的分子时间轴**——检验 MTP 模块是否随机械痛发生/维持而动态变化；核心新增 |
| **GSE248328**（v0.4 新增） | 大鼠 DPN DRG scRNA-seq（对照 vs 糖尿病神经痛，8 类细胞） | 神经病理 DRG 的细胞类型分辨参考（跨物种） |
| GSE111216 / GSE30691（v0.4 候选，待核实） | 文献报道分别为 CFA 炎性痛与 SNI/CCI 神经痛 DRG 数据 | W0 核实 accession 与设计后决定去留；用于跨疼痛模型对比 |
| PMC6802488 | PHN 皮损 miRNA/circRNA | 可选：miRNA → 机械通道 mRNA 的调控层支架 |

### 3.4 机械刺激响应参照集（Layer 5A 专用，v0.2 新增）
| 数据集 | 内容 | 用途 |
|---|---|---|
| **GSE58389** | 人**真皮成纤维细胞** cyclic mechanical stretch，5h vs 24h（669 / 249 DEGs，152 common；✅ v0.3 核实：实际 hub 基因为 DDX17/EXOC7/CASKIN1/RAVER1/LCE1D/LCE1C/PKD1 下调与 XRN2/TCP1/STX3 上调，GO 富集于自噬/固醇合成/皮肤发育/mRNA 加工——**并非典型整合素–ECM 程序**） | **首选参照**（皮肤成纤维细胞与皮损微环境最贴），但注意其生物学偏代谢/组织扩张轴 → 用于**模块级富集检验**而非仅基因列表交集；且来自组织扩张（整形外科）语境，拉伸参数与 ESWT 不同 |
| **GSE222834** | HUVEC 生理性（6%）vs 病理性 cyclic circumferential stretch，48h | 备选：血管内皮剪切/牵张维度 |
| **GSE232118** | hESC 源肝芽/内皮 cyclic mechanical stimuli（HGF/MMP 分泌上调） | 备选：ECM 重塑维度 |
| **GSE314229**（v0.4 新增） | **rESWT 大鼠胫骨骨痂 scRNA-seq**（9 样本；ESWT 后 4h/24h；ESWT 经 ATP/P2X7R/p38MAPK 触发 **sEV（外泌体）释放**，MSC 为来源，Thbs1 富集，促 M2 极化；*Adv Sci* 2026） | **Layer 5A 核心参照**：ESWT 的外泌体机制与 PHN 外泌体叙事直接呼应；p38 节点与 losmapimod 臂、ESWT 文献三点闭合 |
| ~~GSE9877~~（v0.4 更正） | 实为**缺血性卒中血液** Affymetrix 芯片（11 vs 27），被 rESWT-血管生成论文借用为公共"血管生成"数据 | **不采用**——它不是 ESWT 响应数据，防止引用错位 |

### 3.5 因果层（Layer 4）
| 结局 | GWAS ID | cases / controls | 定位 |
|---|---|---|---|
| **PHN（主结局）** | `finngen_R13_G6_POSTZOST` | **554 / 431,627** ✅已核实 | 主 MR |
| 三叉神经痛 | `finngen_R13_G6_TRINEU` | 2,356 / 431,627 ✅ | 神经病理性痛**机制一致性**参考（非替代） |
| 未特指神经痛/神经炎 | `finngen_R13_M13_NEURALGIA` | 2,085 / 350,578 ✅ | 同上 |
| 腰椎根性痛 | `finngen_R13_M13_SCIATICA` | 28,094 / 347,768 ✅ | 力学相关神经痛对照（样本量大，可作阳性质控） |
| 下背痛或/和坐骨神经痛 | `finngen_R13_M13_LOWBACKPAINORANDSCIATICA` | 63,923 / 436,263 ✅ | v0.3 新增：大样本力学相关疼痛端点，阳性质控的更强选项 |
| 带状疱疹 HZ | `finngen_R13_AB1_ZOSTER`（7,974 / 478,888；宽定义 `AB1_ZOSTER_WIDE` 24,551 / 462,930） | ✅已核实 | PHN 上游 |

✅ = 2026-10-19 直查 FinnGen R13 官方 manifest（storage.googleapis.com/finngen-public-data-r13/summary_stats/finngen_R13_manifest.tsv）所得 exact cases/controls。注意该端点 cases 数随 release 持续变动（R5 144 → 约 R11 313 → R12 490 → **R13 554**），功效计算用 554 例；R12 及更早数值仅作历史参照，不得混用。

**暴露**：eQTLGen（全血 cis-eQTL）、GTEx nerve / brain（组织特异性）、UKB-PPP / deCODE / Fenland pQTL。

### 3.6 容易出现"全阴性"的那一级，先说清楚
**PHN 只有 490 例**。这不是可以绕过去的问题，必须前置处理：
- 分析前用 mRnd / TwoSampleMR power 模块计算：在 α=5e-6、不同 OR 下的可检出效应，把"本设计只能检出 OR ≳ 1.6–2.0 量级"写进方法学
- 明确宣示 Layer 4 是 **hypothesis-screening**，成功标准不是"纠正多重比较后显著"，而是"**方向一致 + 共定位 PP.H4 ≥ 0.8 + 与 Layer 1/2 转录组方向同向**"的三重收敛
- 若结果阴性 → 写成 correctly-powered null，报告 OR 的 95% CI 上界（这是可发表的诚实结论，不是失败）
- **因此，本项目的阳性主力放在 Layer 1（转录组定位）和 Layer 5A（药物/ESWT 机制反演），不在 Layer 4**

### 3.7 Layer 5B（可选，可行性未验证）
CHARLS / NHANES 是否含"带状疱疹史 / 体力劳动强度"变量，**必须先做变量可用性体检**。CHARLS 有自报慢性病与体力活动；是否含 HZ 或 PHN **尚未核实**。若核实时不存在 → 该层直接删除，**不得**用替代 proxy 硬凑。

### 3.8 数据体检（Week 0，必须最先做、不可跳过）
在跑任何差异分析之前，先产出 1 份 `data_qc_report.md`：

1. **GSE342782 机械轴核心基因的绝对表达量**：PIEZO1 / PIEZO2 / TRPV4 / KCNK2 / STOML3 / ITGB1 / YAP1 / LOX / MMP9 / COL1A1 / FN1 的原始 counts 与 CPM 分布图，判定是否高于检测限
2. **HD10.6 基线偏差量化**：把 mock 组的通道表达谱与 bioRxiv 2025.04.03.643725 报告的 HD10.6 基线（TRPV1 低、SCN10A 低、CALCA 低、SCN9A/CACNA1B/PIEZO2 高）逐基因比对 → 明确哪些"通道下调"是模型固有、哪些是处理诱导
3. **GSE201654 / GSE168243 人 DRG 同基因亚群表达矩阵**
4. **GSE130633 设计矩阵与 ECM/成纤维细胞机械信号**：先核实 126 样本的确切分组（VZV 抗原 6h/72h × 生理盐水 × 未注射 × losmapimod × 供体），再检验 MTP 信号
5. **四个结局 GWAS 的实际 cases/controls/样本重叠核实**（R13 manifest 已核实 cases/controls；执行时核对 OpenGWAS 上的 release 映射与样本重叠）
6. **v0.3 新增——供体元数据审计**：从 GEO 提取 GSE342782 每个外泌体样本的供体年龄/性别，检验 PHN 组与对照/HZ 组的年龄性别分布差异
7. **v0.3 新增——MR 工具变量可及性**：MTP 基因在各 eQTL/pQTL 源中的 cis 工具数量与强度（554 例结局对工具强度仍敏感；若 MTP 基因普遍无工具，Layer 4 收缩为少数基因 screening）
8. **v0.3 新增——数据一致性抽验**：GSE342782 的 GEO 补充 processed counts（DirectInf / SeraExo 两套）与 SRA 原始数据抽验比对，确定分析用哪套
9. **v0.4 新增——新数据集 accession 落实**：GSE295206 / GSE273557 / GSE155622 / GSE248328 / GSE228390 / GSE314229 / GSE189501 逐一下载并确认样本分组；核实 GSE111216 / GSE30691 的实际设计；找 DPN 人 DRG bulk（5 vs 7）与 Tavares-Ferreira *JCI* 2025 人神经数据的 GEO accession；确认 phs001158 与 2022 *Sci Transl Med* 论文的关系

**三级预案（v0.2 新增，提前写死，禁止事后改口径）**：
- **预案一**（首选）：M3（ECM–整合素–Hippo）信号成立 → 以 A-ii 为主轴推进
- **预案二**：M3 也不成立，但 M1 有量级 → 退回 M1 主导，M3 降为辅助
- **预案三**：M1、M3 均弱 → 转向 **M3 × 免疫浸润交叉轴**（胶原/ECM 基因与免疫细胞比例的耦合）。依据：Ann Neurol 已独立确认炎症是 PHN 外泌体表型的核心，ECM-免疫耦合在瘢痕/纤维化疼痛中有大量先例，此路径不会全阴性

---

## 4. 研究设计总览

```
Layer 0   构建 MechanoTransduction Panel (MTP)  ← 方法学增量，分析前封存
          ├── M1 机械门控通道（辅助）
          ├── M2 通道调控/膜-骨架耦合（辅助）
          ├── M3 ECM-整合素-Hippo 刚度轴      ★ 主轴（v0.2）
          └── M4 力学效应转录程序
          └── N1-N3 中性对照基因集（防"必然富集"质疑）
   ↓
Layer 1   GSE342782：VZV 感染 & PHN 外泌体 → 四维 score + CCI + 模型基线校准
   ↓                                    ↑
Layer 2   人 DRG 图谱：亚群特异性富集 + bulk deconvolution（双轨）
   ↓
Layer 3   外部验证：PRJNA1142765 / GSE242252 / GSE130633 / GSE64345
   ↓
Layer 4   因果：eQTL/pQTL → PHN MR + 共定位 + 功效前置
   ↓
Layer 5A  转化：药物重定位 + ESWT 机制反演（参照 GSE58389 等）
Layer 5B  （可选）CHARLS/NHANES 宏观物理暴露流行病学
```

---

## 5. 逐层详解

### Layer 0：MechanoTransduction Panel（MTP）—— 先造尺子

不要临时抓几个基因。按四个功能子模块显式定义，并在**任何差异分析之前**以独立文件封存（带日期戳 + git tag）：

| 模块 | 代表基因（待补全） | 地位 |
|---|---|---|
| **M1 机械门控通道** | PIEZO1, PIEZO2, TRPV4, TRPC1, TRPC6, TRPA1, KCNK2(TREK-1), KCNK4(TRAAK), KCNK10, ASIC1–3, TMEM120A(TACAN), TMEM150C, TMEM63A/B | 辅助 |
| **M2 调控/膜-骨架耦合** | STOML3, SH3GL2(EndoA2), KIF5B, RAPGEF3(EPAC1), EPB41L3, MYH9, ACTB, SPTBN1/2 | 辅助 |
| **M3 ECM-整合素-Hippo** | ITGA1/2/5/V, ITGB1/3/5, PTK2(FAK), SRC, TLN1, VCL, YAP1, WWTR1, TEAD1–4, LOX, LOXL1/2, COL1A1, COL3A1, FN1, MMP2/9/14, TIMP1–3, CCN2(CTGF), ANKRD1 | **★ 主轴** |
| **M4 力学效应程序** | neurite outgrowth / cytoskeletal remodeling / Ca²⁺ response 的转录伴随物 | 读出 |

**为什么 M3 是主轴（v0.2 新增论证，三条硬依据）**：
1. **ESWT 的已证实分子机制就在这条轴上**：rESWT 经 integrin–FAK–p38MAPK 抗炎并上调 **ITGA2**（*Am J Transl Res* 2023）；ESWT 核心 mechanotransduction = integrin–FAK/Src + **Piezo1/TRPV4** + caveolae → ERK/MAPK、PI3K–Akt、**YAP/TAZ 核转位**（骨修复综述）。Layer 5A 因此有了共同分子基础。
2. **Ann Neurol 的最强读出就是 ECM 轴**：PHN 外泌体上调 ECM 重塑通路、诱导 **MMP-9** 分泌——这是 M3 的直接读出，且是原文明确报道的，我们不需要赌未知。
3. **技术稳健性**：ECM 基因（COL/FN1/MMP/LOX）在 bulk RNA-seq 中表达稳定、检测限好；不依赖 iPSC 模型是否表达 Piezo2。主轴放在 M3 直接降低头号技术风险。

**中性对照基因集（v0.2 新增，防审稿的关键设计）**：
同步对三组与机械轴无关的基因集打分，证明 M 模块的变化幅度显著大于对照，否则审稿人会问"你怎么知道不是所有基因集都会这样"：
- **N1** 电压门控离子通道（SCN/KCNA/CACNA 家族）
- **N2** 嗅觉/化学感受受体（OR/TAAR 家族）
- **N3** 核糖体蛋白（RPL/RPS）

打分：GSVA / ssGSEA / UCell，**统一做 size-matched permutation null**（先掐掉"基因集里基因多、所以随便什么对比都显得富集"这个经典假象）。

### Layer 1：GSE342782 主分析（阳性主力）

**前置步骤——模型基线校准（v0.2 新增，必须最先做）**
HD10.6 的通道表达谱与真人 DRG 有系统性偏差（TRPV1 mRNA 低、SCN10A 低、CALCA 低；SCN9A / CACNA1B / PIEZO2 / P2RX3 高）。因此：
- 所有比较必须以 **mock 组为内部参照**，只解释 PHN-exo 相对 mock 的**额外**变化
- 在稿件中明确声明：HD10.6 模型**不是** PHN 患者的 DRG，其基线通道谱不能外推到在体状态
- 这一校准同时是对 Ann Neurol "canonical nociceptive ion channels downregulated" 结论的独立复核——若该下移在 mock 基线已存在，则原文的解读需修正

**前置步骤二——供体混杂审计（v0.3 新增，与模型基线校准同级）**
PHN 外泌体供体更老、几乎全女性（原文讨论部自承，仅 1 名男性；年龄是 PHN 最强已知风险因素之一）。因此：
- **主对比 = HZ-exo vs 对照-exo**（同属"病毒感染后 vs 对照"框架，供体结构最接近）；PHN-exo vs HZ-exo 作为"未解决（failure-to-resolve）"假说的扩展对比
- W0 从 GEO 元数据提取每个外泌体样本的供体年龄/性别；n 允许时以 `~ age + sex + group` 建模拟合，否则报告 PHN 签名与供体年龄的相关性
- 敏感性分析：PHN vs 对照签名与已知衰老转录组签名的重叠（重叠高 → 签名更可能是年龄相关而非 PHN 特异）
- 稿件局限明写：PHN 供体组的年龄/性别结构限制"PHN 特异信号"的归属强度

**分析内容**
1. 四模块 score：mock vs VZV；**HZ-exo vs 对照-exo（主对比）**；PHN-exo vs HZ-exo（扩展）；**同步跑 N1–N3 对照集**
2. **通道互补指数（CCI，v0.2 修正）**：不用 `z(M1) − z(Nav)`（基因集大小悬殊时不稳健），改为——
   - 在同一基因全集上，对每个样本计算 M1 与 N1（电压门控通道）的 **平均秩次差**：`CCI = mean_rank(M1) − mean_rank(N1)`
   - 用 size-matched permutation 生成 null 分布，报告观测值在 null 中的分位
   - ⚠️ v0.3 表述纪律：N1 同时是中性对照集，CCI 与中性对照检验是两个独立统计量，稿件中分开报告；若 N1 自身相对 null 显著位移，CCI 只能表述为"相对位移"，不得表述为"错配"
3. 与原文报道的 neurite-outgrowth 抑制表型做关联（先复现原文结论 → 再做机械轴拓展）
4. 关键推论检验：**"低放电能力 + 保留/上调的机械敏 + ECM 刚度程序激活"三者共存**
5. **跨模型一致性（v0.4 新增）**：GSE228390（hiPSC-神经元 × VZV bulk RNA-seq，80 样本）复核同一 mechano 模块在**非 HD10 的人神经元模型**中的响应。⚠️ 事前声明：该研究报告 hiPSC-神经元对 VZV 大体"irresponsive"（免疫逃逸策略），若跨模型一致性弱，解释为模型差异而非否定 HD10 结果；不得据此改写 Layer 1 主结论

**预期产出**：4 个差异 score + CCI + 模块间交叉相关热图；如果发现 Nav 类下调而机械门控通道相对保留 ⇒ 得到"**通道错配表型（channel-mismatch phenotype）**"。

**主张层级（v0.3 指定，2026-10-19 实测后修正）**：预注册主叙事原定"M3 刚度程序表型"，但 Layer 1 主终点（M3, HZ-exo vs 对照-exo）实测为 correctly-powered NULL（P=0.416），故**主叙事切换为"通道失衡（channel-imbalance）表型"**——即急性 HZ 血清外泌体选择性抑制经典电-化学伤害性通道（SCN9A/SCN10A/TRPV1/ASICs）而保留机械门控 PIEZO2 轴，作为机械性痛觉超敏的分子 substrate。M3/ECM 维度降为 Layer 2/3/5A 的跨组织验证对象，不再作为 Layer 1 头条。切换落在 v0.3 三级预案框架内（E1 属冻结 panel、通道错配概念 A5 已预指定），非事后改口径。

**效能说明（v0.3 新增）**：外泌体组每组 n≈5–6，单基因 DEG 的可检出效应门槛高 → 结论以 gene-set 层面为主；单基因结果用 apeglm 做 LFC 收缩；附表报告每个对比的可检出效应（功效曲线）。

### Layer 2：细胞亚群定位（v0.2 修正方法学）

不再说"把 bulk 签名回投到单细胞"——这不是标准做法，会被审稿人打。改为**双轨**：

- **轨道 A｜细胞类型特异性富集**：把 Layer 1 得到的 PHN/VZV DEG 列表，检验其在哪些 DRG 神经元亚群中特异性高表达（基于 GSE201654 / GSE168243 / GSE189501 的亚群 marker）。回答"**PHN 信号落在哪个神经元亚群**"
- **轨道 B｜bulk deconvolution**：用 CIBERSORTx / BisqueRNA 估算 GSE342782 各样本的细胞组成，检验 PHN-exo 是否改变特定亚群的比例。回答"**PHN 信号是否改变细胞群体结构**"
- **轨道 C｜人 DRG 空间层（v0.4 新增）**：在 GSE295206（Visium）/ GSE273557（Xenium）上检验 MTP 模块的**空间分布**（是否富集于特定 DRG 微区/细胞邻域）及其在糖尿病神经痛中的改变。回答"**机械轴在人 DRG 里有没有空间组织、神经病理状态下变不变**"。⚠️ 糖尿病语境，只作"最近邻人神经病理参考"，不得表述为 PHN 证据
- 跨物种：将人 DRG 亚群映射到小鼠 nomenclature（Usoskin/Sharma 分型 NP1–3、PEP、TH、Aβ LTMR、Aδ），报告保守性与分歧

**阳性保障**：Aδ / Aβ-LTMR / 非肽能 NP3 高表达 Piezo2 已有大量独立的、已确立的实验证据（含 2026 年 *Pain* 的 Piezo2 × MrgprD 条件敲除工作），这层不会是空白。

### Layer 3：外部验证

- **GSE130633（v0.2 新增，v0.3 更正性质，皮肤层）**：VZV 抗原刺激皮肤模型（6h/72h，含生理盐水与未注射对照 ± losmapimod）。⚠️ **它不含 PHN 患者**，"缓解无 PHN 原位数据"的说法降级为"提供抗原刺激 → 皮肤 ECM/机械信号的桥梁证据"。**预期皮肤层的 M3 信号最强**（成纤维细胞/ECM 主场）；用标准 bulk 流程（limma/DESeq2 + GSVA + 去卷积），不继承 2024 再分析的 Seurat/Monocle 流程
- PRJNA1142765：PHN vs HZ 血液层。⚠️ **预期血液层 M1/M3 信号弱**（血细胞基本不表达 Piezo2、ECM 基因）——因此血液层的成功标准应下调为"外泌体来源的细胞因子/ECM 成分信号"，而非 mechano-score 本身。**提前写明，避免事后解释**
- GSE242252：HZ onset → recovery 的时间学，检验 mechano-score 是否在"未恢复者"中持续偏高
- GSE64345：大鼠 DRG 跨物种保守（**n=3 vs 3，仅作弱一致性证据，不得作为主要证据**）
- **GSE155622（v0.4 新增，时间轴层）**：SNI 后 6h→28d 的单细胞动态，检验 mechano-score 是否与机械痛的发生（急性期）和维持（慢性期）共变；预期损伤早期 Atf3 类反应基因主导，机械通道模块的变化时相需如实报告
- **GSE248328（v0.4 新增，跨物种神经病理）**：大鼠 DPN DRG 的细胞类型分辨变化
- 明确标注：血液 ≠ DRG ≠ iPSC 神经元，各层是**支持性而非确认性**；糖尿病神经痛人 DRG 数据（GSE295206 / GSE273557 / DPN bulk）是**最近邻参考**，不是 PHN 证据

### Layer 4：因果层（MR）

- 工具变量：MTP 基因的 cis-eQTL / cis-pQTL（F > 10，clumping r²<0.001 / 10 Mb）
- 主方法 IVW + MR-Egger + WM；异质性 Cochran's Q；MR-PRESSO；反向 MR；Steiger 定向
- 多重校正：**测试数量 = MTP 基因数 × 结局数**，用 Bonferroni / FDR，并把测试总数写进附表
- 共定位：coloc + SuSiE，报 PP.H4
- **前置功效计算 + 显式 null 处置路径**（见 §3.6）
- 若 Layer 4 显著基因与 Layer 1/2 方向一致 → 进入 druggability 评估（Open Targets + DrugBank + 中枢副作用）

### Layer 5A：转化层（第二个阳性主力，v0.2 大幅强化）

**ESWT 的分子机制已在机械转导轴上被独立确立（这是 v0.2 的核心增量）**：

| ESWT 的已知分子事件 | 对应 MTP 模块 |
|---|---|
| rESWT 经 **integrin–FAK–p38MAPK** 通路发挥抗炎作用（人原代 tenocyte，含整合素抑制剂阻断验证） | M3（ITGA2、ITGB1、PTK2） |
| rESWT 定量蛋白组学显示 **ITGA2 显著上调** | M3 |
| ESWT 激活 **Piezo1 / TRPV4** → Ca²⁺ → ERK/MAPK、PI3K–Akt | M1 + M2 |
| ESWT 促进 **YAP/TAZ 核转位**，整合素/FAK/RhoA 上游 | M3 |
| ESWT 上调 **VEGF、eNOS、TGF-β1、IL-10、IL-4**，促 ECM 重塑与胶原合成 | M4 + M3 |
| **Piezo1–FAK 双相模式**（*EMBO J*）：激光诱导冲击波单脉冲 → Ca²⁺ 升高 + **FAK 活性升高**；多脉冲 → 持续 Ca²⁺ 而 **FAK 活性下降** | 剂量-方向反转 |
| rESWT 经 **ATP/P2X7R/p38MAPK** 触发 **sEV（外泌体）释放**（MSC 来源，Thbs1 富集，促 M2 极化）——*GSE314229* 单细胞证据（v0.4 新增） | M3 + **外泌体轴**（与 PHN 外泌体叙事呼应） |

**由此产生两个可检验的具体假说（v0.2 新增）**：
- **H-ESWT-1（交集假说，v0.3 改为模块级检验）**：GSE58389 的 DEG 生物学偏代谢/自噬轴（见 §3.4），单纯基因列表交集可能假阴性 → **主检验改为模块级**：MTP 模块（尤其 M3）在拉伸响应数据全基因排序背景中的富集方向与幅度，回答"力学刺激响应是否系统性作用于 M3 轴"；辅以 PHN 外泌体 DEG 与 152 common DEGs 的交集大小（无论正负均可报告）。推论方向：ESWT/拉伸上调的正是 PHN 压制的（neurite outgrowth / ECM 稳态程序），ESWT/拉伸压制的正是 PHN 上调的（ECM 重塑/炎症）
- **H-ESWT-2（剂量反转假说）**：若 Piezo1–FAK 双相模式在神经组织同样成立，则 ESWT 的低能量通量与高能量通量应产生**方向相反的 FAK/ECM 转录响应**。这解释了一个临床困惑：为何不同 ESWT 参数（0.05–0.20 mJ/mm²）疗效差异大

**第三条线索（v0.3 新增）：p38 药理抑制的正交参照**——GSE130633 含 **losmapimod（p38 MAPK 抑制剂）臂**，而 p38MAPK 正是 ESWT 机制中 integrin–FAK 的下游节点。该臂可作为"同一节点的药理抑制 vs 力学激活"的正交参照，检验皮肤抗原刺激下 FAK–p38–ECM 轴的响应方向。

⚠️ **方向依赖性警示（v0.3 新增）**：文献中同一节点的方向随组织与剂量反转——rESWT 在肌腱中经 FAK–p38 **抗炎**，而 losmapimod 在皮肤中以**抑制 p38 的方式抗炎**（组织语境相反）；Piezo1–FAK 还有单脉冲升/多脉冲降的双相模式。因此 H-ESWT-1 的检验**不得**退化为全局符号匹配，必须分模块、分方向、分组织语境做敏感性分析，并在稿件中明示方向假设的来源组织。

**药物重定位**：以 Layer 1 的 PHN mechano-signature 为 query，做 CMap/LINCS L1000 反向匹配 → 候选化合物；过滤到"已有临床安全性数据、非阿片"的药物（例如 TRPV4 拮抗剂 GSK2798745 有临床暴露；Piezo1 抑制剂 GsMTx4 / Dooku1 需注意给药途径，不得夸大为口服候选）。**优先考虑 M3 轴上的可成药节点**（integrin/FAK 类），因为它们正是 ESWT 的已知靶点，临床转化路径更短。所有候选化合物的临床阶段与适应症须在 Open Targets / DrugBank 逐个核实（执行时）。

### Layer 5B（可选）：宏观物理暴露流行病学
CHARLS / NHANES 变量体检通过后：**职业性体力负荷 ↔ 带状疱疹 / 慢性疼痛** 关联分析。若所需变量体检后不存在 → 删除该层。

---

## 6. 统计与可复现纪律（这部分决定能不能过审）

| 纪律 | 具体要求 |
|---|---|
| 预定义封存 | MTP 基因列表（含 N1–N3 对照集）在**跑任何分析之前**进 git（tag: `mtp-frozen-<date>`），事后任何增改必须在 changelog 中显式记录并经版本号递增 |
| 模型基线校准 | 所有 Layer 1 比较以 mock 组为内部参照；HD10.6 与真人 DRG 的基线偏差必须在方法学与局限中显式报告 |
| 避免循环富集 | 所有 score 用 size-matched permutation null 校准 |
| 中性对照 | 每张 score 图必须同时呈现 N1–N3 对照集，证明 M 模块变化幅度显著大于对照 |
| 避免伪 replication | PRJNA1142765 / GSE242252 / GSE130633 / GSE64345 是**独立队列**，不得在同一模型里合并当作 n 累加 |
| 功效前置 | MR 层 mRnd 功效报告 **必须**先于结果写出 |
| 多重校正 | 明确报告：每个 Layer 的测试数量与校正方式进 supplementary table |
| 探索性声明 | Layer 4 与 Layer 5A 明确标 "hypothesis-generating" |
| **单一主终点（v0.3 指定，2026-10-19 实测）** | 预注册唯一 primary endpoint = **血清外泌体暴露（HZ-exo vs 对照-exo）下 M3 score 的差异**；实测为 correctly-powered NULL（置换 P=0.416，效应量 −0.049）→ **如实报告为阴性主终点 + 报 95% CI 上界 + 功效**，不包装；核心实证转至预指定次级终点"通道失衡"（E1 显著下调 + PIEZO2 保留）。全稿明确分级：primary=NULL、secondary=channel-imbalance、exploratory=PHN 对比/MR/ESWT 机制 |
| 预注册（v0.3 新增） | 分析开始前在 OSF / Research Square 登记本协议（含主终点与三级预案），登记时间戳进复现包 |
| 时间尺度限定 | 外泌体实验仅 36h → 所有结论措辞限定为"早期分子事件"，不得外推为慢性在体状态 |
| 阴性处理 | 报 95% CI 上界 + 功效，不当成失败也不包装成阳性 |
| 复现包 | README.md + CITATION.cff + MIT LICENSE + release workflow + GITHUB_DEPOSIT_SOP.md + author_verification_statement.md（沿用既有标准化配置） |

---

## 7. 图件计划（6 图 + 附）

| 图 | 内容 |
|---|---|
| Fig 1 | 研究设计流水线 + MTP 四模块定义 + **中性对照基因集** |
| Fig 2 | GSE342782：四模块 score 在多组间的变化（VZV / HZ-exo / PHN-exo / HD-exo / mock）+ permutation null 对照 + **N1–N3 对照集并列** |
| Fig 3 | **通道互补指数（CCI）与通道错配表型** —— 本项目核心图；含 HD10.6 基线校准示意 |
| Fig 4 | 人 DRG 亚群机械敏感性图谱 + PHN DEG 亚群特异性富集 + deconvolution + **人 DRG 空间层（Visium/Xenium）** |
| Fig 5 | 外部验证：GSE130633（皮肤层）+ PRJNA1142765 + GSE242252 + GSE64345 四层一致性汇总 |
| Fig 6 | MR 森林图 / 共定位 / druggability + **ESWT 机制反演网络**（含 GSE58389 交集与 H-ESWT-2 剂量反转） |
| 附表 | MTP 完整基因列表、N1–N3 对照集、功效表、所有 score 表、HD10 基线偏差表、局限与 null 报告 |

---

## 8. 执行时间表（12 周）

| 周 | 任务 | 产出物 | 状态 |
|---|---|---|---|
| W0 | 数据体检（含 HD10 基线校准）+ MTP 冻结 + 仓库初始化 | `data_qc_report.md`、`mtp/`、`git tag mtp-frozen` | 待启动 |
| W1–2 | Layer 1 主分析（含 N1–N3 对照与 CCI） | Fig 2、Fig 3 | 待启动 |
| W3–4 | Layer 2 亚群定位（双轨） | Fig 4 | 待启动 |
| W5–6 | Layer 3 外部验证（四层） | Fig 5 | 待启动 |
| W7–8 | Layer 4 MR + 前置功效 | Fig 6 上半 | 待启动 |
| W9–10 | Layer 5A 药物 + ESWT 反演（含 GSE58389 交集） | Fig 6 下半 | 待启动 |
| W11 | gate 校验 / 全文 / 复现包 | 稿件初稿 + v1.0.0 release | 待启动 |
| W12 | 交叉核对 + 伦理文书（若启动临床层） | — | 待启动 |

⚠️ **延期预案（v0.3 新增）**：W7–W10 偏乐观的两个卡点——① MR 层若 MTP 基因工具变量不可得或太弱（见 §3.8 第 7 项），Layer 4 收缩为少数基因 screening，W8 顺延；② ESWT 反演的参照集核对（§3.4）若需补数据，W9–W10 顺延。延期不得以压缩质控为代价。

仓库名建议：`phn-mechanotransduction`（kebab-case；科研 GitHub 账号 `yyx-4113`；沿用既有复现包标准配置）。

仓库建议结构：
```
config/ mtp/ data/ scripts/{00_qc,01_layer1,02_layer2,03_layer3,04_mr,05_tx}/
results/ figures/ manuscript/ docs/
```

---

## 9. 候选投稿方向（**尚未核实任何 IF / 分区**）

⚠️ **纪律要求**：下列期刊均为真实存在的公开期刊名称，但**本次未做任何在线核实，表中不含任何 IF / JCR 分区 / 中科院分区 / APC 数据**。投稿前必须逐刊在线核实 SCIE 收录状态与最新指标并附年份戳。按既有约定：**PeerJ 系列不推荐；Scientific Reports 对再分析类稿件存在 desk-reject 实证风险**（不作为首投）。

| 候选期刊 | 为什么对口 | 风险提示 |
|---|---|---|
| *Journal of Pain Research* | 疼痛机制 + 再分析友好；既往多次作为疼痛主题首推备选（来源：会话约定，**非本次核实**） | SCIE 状态与指标须核实 |
| *Pain Practice* | 已发表 PHN ESWT RCT → Layer 5A 的转化叙事直接对口 | 偏临床读者群，稿件需明确临床相关性 |
| *Molecular Pain* | 机械门控通道 / 感觉神经元机制的同温层 | 需核实收录与当前状态 |
| *BMC Neurology* / *BMC Medical Genomics* | 多组学结构 + 审稿稳健，对再分析类二次数据稿兼容 | 需核实收录与指标 |
| *Frontiers* 系列疼痛/神经分册 | 主题匹配 | ⚠️ 部分分册对纯 in-silico 稿要求实验验证，存在 desk-reject 风险；核实后再定 |

**投稿前必做三项**：(1) 在线核实 SCIE 收录 + 最新 JIF/分区（年份戳）；(2) 评估本稿证据层级（纯二次分析 → 因果声明必须降级为 "hypothesis-generating"）；(3) 核实该刊对 secondary analyses（二次数据分析）类稿件的接受口径。

---

## 10. 风险清单与诚实局限

1. **无 PHN 特异性的人 DRG 数据**（v0.4 改写：糖尿病神经痛已有人 DRG bulk / snRNA / Visium / Xenium——GSE295206、GSE273557、phs001158、79 供体多组学项目——可作**最近邻人神经病理参考**，但糖尿病 ≠ PHN，病因与纤维类型不同）→ 局限中明写"PHN 的 DRG 原位证据仍缺失，本稿用人神经病理 DRG 作最近邻参照"；GSE130633 皮肤层（抗原刺激模型）只提供桥梁证据
2. **GSE342782 外泌体实验仅 36h**，属急性转录响应 → 所有结论限定为"早期分子事件"，不得外推慢性在体状态
3. **HD10.6 模型固有偏差**：TRPV1 mRNA 低、SCN10A 低、CALCA 低 → Ann Neurol "经典伤害性通道下调"的解读需经基线校准复核；本稿所有比较以 mock 为内部参照
4. **PHN GWAS 仅 490 例** → Layer 4 功效受限，前置功效计算 + 三重收敛标准，不得以"通过多重校正"为唯一成功标准
5. **血液层 mechano-score 预期弱**（血细胞基本不表达 Piezo2/ECM 基因）→ 血液层成功标准已提前下调为外泌体来源的细胞因子/ECM 成分信号
6. **GSE64345 n=3 vs 3**、芯片平台、物种差 → 仅作弱一致性
7. **"Current Science" 那篇 PHN 皮肤 scRNA-seq 数据不可获得、期刊可靠性存疑** → 不引用、不用
8. **引用 2020 那篇 PHN 芯片分析时须注意**：其载刊 *Evid Based Complement Alternat Med* 已被 Wiley 停止接收，引用可靠性低于常规 SCIE 刊
9. **ESWT 机制文献均来自肌腱/骨/MSC 语境**，向神经/PHN 的外推是本项目的推论而非既定事实 → 必须明确标注
10. **若后续要加临床/血清验证（QST + ELISA）**：⚠️ **必须事先取得本单位 IRB 批准**，不得先采样后补批；建议伦理申报与 Layer 1–5A 分析**并行启动**。若涉及 ESWT 干预，还应记录能量通量与脉冲数（对应 H-ESWT-2 剂量反转假说）
11. 全案为 **二次数据分析 + 假说生成**，不得给出任何因果治疗主张
12. **GSE342782 的 PHN 外泌体供体存在年龄/性别混杂**（更老、几乎全女性）→ "PHN 特异信号"的归属强度受限；已用主对比切换（HZ-exo vs 对照-exo）+ 供体审计缓解，但不能消除（v0.3 新增）
13. **GSE58389 的拉伸响应生物学偏代谢/自噬轴**（hub 基因为 DDX17/EXOC7/RAVER1 等，非整合素–ECM 程序），且来自组织扩张语境 → H-ESWT-1 以模块级富集为主检验、基因列表交集仅作辅助；不得宣称"ESWT 响应基因集 = ECM 程序"（v0.3 新增）
14. **人 DRG 参照数据均为糖尿病神经痛语境**（GSE295206 / GSE273557 / GSE248328 / DPN bulk）→ 所有跨疾病推论必须降级为"神经病理 DRG 的共性检验"，不得外推为 PHN 特异性（v0.4 新增）
15. **GSE228390 的跨模型一致性可能天然偏弱**（该研究报告 hiPSC-神经元对 VZV 大体无响应，属免疫逃逸现象）→ 若 Layer 1 与 GSE228390 不一致，以模型差异解释，不得据此改写主结论；事前写入方法学（v0.4 新增）
16. **GSE273529 为 NanoString 免疫面板**（585 基因）→ 不覆盖多数 MTP 基因，仅作免疫轴一致性，不得用于 mechano-score（v0.4 新增）

---

*本方案 v0.4 为骨架，执行中每完成一层更新一次版本并打 tag。*
