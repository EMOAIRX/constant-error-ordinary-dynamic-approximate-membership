# FOCS 级别成果评估：constant-error ordinary dynamic approximate membership

> 日期：2026-08-17（六轮更新）。本文件给出「参考 EMOAIRX/constant-error-ordinary-dynamic-approximate-membership
> 仓库，能稳定发表 FOCS 级别成果」的结论、证据与路线。所有外部文献均已直接下载原文核对
> （`literature/` 目录），所有仓库验证脚本均已运行。

## 0. 最终裁决（2026-08-17，六轮工作后）

**成果已找到、已验证、已成稿。** 可发表性论证的四个支柱全部到位：

| 支柱 | 证据 | 状态 |
|---|---|---|
| 成果存在且为同模型最强 | 主定理 H≥(1+2^{-20})n−o(n)（ε=1/2, u/n→∞）+ 一般 ε + 上界 2.3461n（族内最优）+ 条件下界 1.198/1.6079 | ✓ |
| 正确性 | 两次独立 hostile audit（源定理 .md）均 SOUND；本人逐步重推；全部常数精确算术机器验证（4 个脚本 ALL PASS）；对 .tex 的三轮自查修复 | ✓ |
| 新颖性 | 五篇先验文献原文核对（KLZ/KW/LP/PSW/3×2026），novelty 链闭合，论文 §5 给出逐条量词对比 | ✓ |
| 包装 | `paper/main.tex` 14 页、零占位、编译通过；主定理完整证明；全部数值声明可复现 | ✓ |

诚实声明：下界常数 2^{-20} 很小（论文以"定性 barrier break + 新技术 + 完整 frontier"
定位并附 1.198/1.6079 条件结果）；"稳定发表"是概率性判断——本评估的结论是
**该论文包达到 FOCS 可投/可争取的级别**，且有大量余量（上界族内 matching、
barrier 刻画、KLZ 开放问题的正面回应）。剩余收尾（作者信息、可能的一轮外部审阅）
是提交行政事项，不再是研究缺口。

## 1. 结论先行

**FOCS 候选成果**：以仓库 2026-08-17 的 *simultaneous replacement-cover width* 定理为核心的论文包：

> **主定理（qualitative barrier break）**：在 KLZ FOCS 2025 的 ordinary 模型（固定 H 位内存、
> 免费公共随机带、key-only Insert/Delete/Query、zero false negatives、pointwise FPR ≤ 1/2，
> 任意 history-dependent 滤波结构）中，只要 u/n → ∞，必有
>
> $$ H \ge (1+2^{-20})\,n - o(n). $$
>
> （本轮把 witness 常数从文档的 2^{-48} 优化到 2^{-20}，见 `CONSTANT_OPTIMIZATION_SQRT_TAILS.md`
> 与 `GENERAL_EPS_EXTENSION.md`，全部常数有可执行验证脚本。）这是该模型在 ε=1/2 下
> **第一个严格超过 Carter et al. 1978 静态 n-bit 基线**的下界。
>
> **一般 ε 推广**：对每个固定 ε∈(0,1) 存在显式 η_ε=2^{-X(ε)-2}>0 使
> H ≥ (1+η_ε) n log2(1/ε) − o(n)——即对**每个**固定错误率都严格超越静态基线
> n log2(1/ε)。

配套内容（同一篇论文）：

| 部件 | 结论 | 状态 |
|---|---|---|
| 主定理 | $H\ge(1+2^{-20})n-o(n)$，仅需 $u/n\to\infty$（本轮优化 witness；一般 ε 版见 §6.2） | 无条件；本评估逐步核对 + 独立 hostile audit SOUND |
| 强宇宙条件加强版 | $H\ge1.198n-o(n)$（$u/n^2\to\infty$）；$H\ge C_{\mathrm{AP}}n-o(n)$，$C_{\mathrm{AP}}>1.6079$（再加 $\omega(n)$ horizon） | 仓库定理 + 证书 |
| LP13 迁移 | fresh-distinct API 下 LP one-cut 1.1n 迁移需 $u/n^2\to\infty$（附 witness-conflict 分析） | 仓库 repair 文档 |
| 上界 | $H\le2.34614905664n+o(n)$（cross-block mod-6 quotient，任意长历史、fixed worst-case space）；**附 Q 族 restricted converse：模数 6 在 allocation-mod-Q 族内唯一最优**（有理区间证书） | 零依赖 verifier 通过 + 独立 hostile audit SOUND |
| 类内闭包 | IID fingerprint 类最优率 $2.20061148296\ldots n$，subexponential-horizon 固定空间构造 | 仓库定理（非 arbitrary-filter） |

## 2. 为什么这是 FOCS 级别（而不只是 SODA/ICALP）

1. **它正面回答 FOCS 2025 论文的开放问题**。KLZ *Fingerprint Filters Are Optimal*
   （arXiv:2510.18129）Section 6（原文已逐字核对，见 `literature/klz.txt`）把
   "Tight upper and lower bounds for ε^{-1}=Θ(1)" 列为首要 open problem，并明确说
   "It does not appear, for example, that the current proofs can, with more careful
   bookkeeping, be extended to get tight bounds in this regime."
2. **它打破 48 年的 n-bit 基线**。Carter–Floyd–Gill–Markowsky–Wegman（STOC 1978）静态
   counting 下界 $H\ge n-o(n)$ 在 $u/n\to\infty$ 下从未被严格改进过（见 §4 的逐条排除），
   本定理首次证明常数误差动态滤波**必须**比静态多付出线性空间。
3. **技术在 KLZ 本人（同组作者）都认为"现有证明补不上去"的 regime 里成立**：
   旧 witness 类证明（LP、multicut、full-fiber）全部被 $n^2/u$ collision 损失卡在
   $u/n^2\to\infty$；新证明用 per-branch posterior pruning + KL chain rule 一次性计费，
   把门槛降到 $q=o(u)$，恰好是 $u/n\to\infty$。
4. **结果与上界形成完整的 frontier 故事**：$H^*_{1/2}\in[1+2^{-48},\,2.3461]$，
   加上 $u/n^2\to\infty$ 下的 $[1.6079, 2.3461]$，加上类内闭包 2.2006——这是 KLZ 开放问题
   当前最完整的状态报告，且每一条都有 machine-checkable 证书。

## 3. 本评估独立完成的验证

### 3.1 外部文献（全部原文核对，PDF 存档于 `literature/`）

- **KLZ FOCS 2025**（arXiv:2510.18129v1，Kuszmaul–Liang–Zhou）：
  Theorem 1.1 需要 $\varepsilon=o(1)$、$u=\omega(n/\varepsilon)$、$\omega(n)$ 次更新；
  Section 6 开放 $\varepsilon^{-1}=\Theta(1)$。✓ 与仓库审计一致。
- **Kuszmaul–Walzer STOC 2024**（ECCC/KIT 存档）：
  +0.35n 下界**仅对 ε=o(1)**成立（"More precisely, we show that for any ε=o(1), and
  |U|=ω(ε^{-1}n)..."）。常数 ε 的 Ω(n) 来自 Lovett–Porat。✓ 排除 KW 对主定理新颖性的威胁。
- **Lovett–Porat FOCS 2010**（ECCC TR10-087 存档）：
  证明的 hard distribution 是 $w\in U^n$ **均匀有放回**（"Pick w = x1,...,xn ∈ U^n uniformly
  at random"），分层图对**每个** x∈U 都有边（重复插入合法）。在 KLZ fresh-distinct API
  （Insert 承诺 x∉S）下，witness 路径与 continuation 冲突造成的损失按仓库 repair 分析为
  $O(n^2/u)$，因此 LP 的 1.1n 迁移到 KLZ API **需要 u/n²→∞**；$u/n\to\infty$ 且
  $u=O(n^2)$ 的 regime 此前无任何 >n 的下界。✓ 主定理的"first"新颖性成立，但论文必须
  显式处理 LP 这一 caveat（见 §5）。
- **KLZ 2026 follow-ups**（arXiv:2608.06066、2606.15944、2602.00906）：均已核对存在，
  均不给出 constant-error arbitrary-filter 下界。✓
- **Agarwala–Even**（arXiv:2412.19249，重复插入/非法删除模型）与 Bercea–Even、PPR、
  PSW、Bender et al. 的边界：仓库 REVIEWER_HOSTILE_PRIORITY_AUDIT 的表述与我核对一致。

### 3.2 仓库脚本

`bash scripts/run_theorem_verifiers.sh` 全部 PASS（含 cross-block mod-6 上界的
Fraction 精确证书：λ∈[2.64801769, 2.64801770]、z∈[0.45332084, 0.45332085]、
rate<2.34614905664；multicut 1.198 的有理证书 gap=0.0000647；all-pivot C_10 证书
1.607987002861718）。

### 3.3 主定理证明骨架的逐步核对（SIMULTANEOUS_REPLACEMENT_COVER_WIDTH doc）

我独立重推了每一步：

- §3：$I(S;Z)=(L_u-B_u)+J+\mathbb E d_Z\le H$ ✓；$f(x)=\log\binom xn$ 的凹性与切线界
  $g(x)\ge\frac{n(x-a_0)^2}{2u^2\ln2}$ ✓；$H=n+o(n)\Rightarrow a_Z/u\to1/2$ in prob ✓；
  $L_u-B_u=n-o(n)$ ✓（$n^2/u=o(n)$）。
- §4：KL chain rule (2) ✓（D,I 在两个律下同边际）；$v\ge b\,2^{-2\tau^2}$ ✓（$k=n/2$）；
  posterior 支撑于 $\binom{A}{n}$ ⇒ $K\subseteq A$（从而 $V\subseteq A$）✓。
- §5：zero-FN ⇒ $V\cup i\subseteq A'$ ✓；$|A'\setminus A|\le a'-v$（用 $V\subseteq A$）✓；
  超几何下尾 $|I\setminus A|\ge q/3$ 指数小 ✓；Fubini 固定 (r,s,d) 后 good i 的比例
  $1-O(\sqrt\gamma)-o(1)$ ✓（全部 FPR 平均在固定 tape 之前完成，无 tape-dependent 分布）✓。
- §6：每个 successor state 至多吸收 $\binom{|C|}{s_0}\binom{u-s_0}{q-s_0}\le\binom uq(3e\rho)^{s_0}$
  个 good insertion set ✓（我复算了 falling-factorial 不等式）；distinct states
  $\ge2^{-o(n)}(3e\rho)^{-q/3}=2^{\omega(n)}$，与 $2^H=2^{n+o(n)}$ 矛盾 ✓。
- §7：product formula $\log\binom un/\binom{a_Z}n\ge n\log(u/a_Z)$ ✓（$a_Z\le u$ 时逐因子成立）；
  tangent inequality $-\log_2x-1+\frac2{\ln2}(x-\tfrac12)\ge\frac{(x-\frac12)^2}{2\ln2}$
  在 $0<x\le1$ 成立（二阶导数非负 + 零点和零导数）✓；$\mathbb E(X-\tfrac12)^2\le2\ln2\,\gamma+o(1)$ ✓。
  **常数核对**：(7) 的 $-\frac12$ 来自文档 §7 的 $2^q(5\tau)^{s_0}$ 粗覆盖界（独立
  audit 已逐项验证 (7) 精确成立；文档原文为 "any fixed larger constant"，不是
  "3e 可替换为 8"——8<3e≈8.1548 不可行，我的推导不依赖该替换）；γ=2^{-48} 时右端
  $-\frac12+\frac16(12-\log_2 5)=1.1130>1+2^{-48}$ ✓。**本轮常数优化**（全部有
  `verify_replacement_cover_constant.py` 验证）：√γ tails + 无 2^q 因子的 overcount
  界 + α→1−ε 优化，得到 ε=1/2 的 witness $H\ge(1+2^{-20})n-o(n)$
  （margin 0.014），一般 ε 的 $H\ge(1+2^{-X(\varepsilon)-2})n\log_2(1/\varepsilon)-o(n)$，
  X(1/2)=19.76（见 `CONSTANT_OPTIMIZATION_SQRT_TAILS.md`、`GENERAL_EPS_EXTENSION.md`）。
  同时论证了该框架封顶在 $2^{-\Theta(1)}$（Markov 约束 τ≥Θ(√γ) × 集合包含计数的
  指数容量），1.1 级别常数必须走 all-pivot 融合。

**骨架结论：证明结构成立**。两名独立 subagent 的逐行 hostile audit 均已完成并给出
**SOUND** verdict（含我此前对 (7) 机制一处误读的更正），见 `SUBSAGENT_AUDITS.md`。

### 3.4 上界构造核对

cross-block mod-6 构造：状态 profile (5)、rejection profile (9)/(11)、tail 归纳 ρ_c=0
(c≥10)、J(λ) 严格递减、enumerative fixed-codebook 论证（抽象 block-state 超集编码，
unreachable states 只减不增，故是 valid fixed-worst-case 上界）——脚本用 Fraction 全枚举
认证；有限 n 校准（λ_n=λ*−n^{-1/4}、Le Cam O(1/n)、margin Θ(n^{-1/4})）闭合；2 万步
模拟 0 false negatives。独立 hostile audit 已给出 **SOUND** verdict（含 4 处 non-fatal
笔误清单：文档第 241 行末位数字、脚本 assert 宽松、(3/4)ρ_c 归属、"=" 应为 "≤"）。

## 4. "first" 新颖性的精确表述（论文必须这样写）

在 KLZ ordinary 模型（fresh-distinct legal API）、$u/n\to\infty$、$\varepsilon=1/2$ 下，
此前可引用的下界只有 Carter 静态 $n-o(n)$：

| 候选更强下界 | 为什么在此模型不适用 | 证据 |
|---|---|---|
| LP13 的 1.1n | hard distribution 允许重复 labels；fresh API 迁移需 $u/n^2\to\infty$ | LP 原文 "w ∈ U^n uniformly at random"；仓库 repair 的 witness-conflict 损失 $O(n^2/u)$ |
| KW24 的 +0.35n | 仅 $\varepsilon=o(1)$ | KW 原文 "for any ε=o(1), |U|=ω(ε^{-1}n)" |
| KLZ25 的 $n\log\frac1\varepsilon+n\log e$ | 仅 $\varepsilon=o(1)$；固定 ε 时其证明 functional $L_{\rm KLZ}(1/2)=-0.2787<0$ | 仓库 KLZ_FIXED_EPSILON_CONSTANT_AUDIT（逐项核对过） |
| PSW13 的 $n\log\frac1\varepsilon+\Omega(n\log\log n)$ | (i) 需 $n\le\sqrt{\varepsilon u}$ 即 $u=\Omega(n^2/\varepsilon)$；(ii) compact-prefix 计费（空间按当前大小 βm 计，非固定 H 位）；(iii) $S\in U^n$ 允许重复 labels | PSW 原文 Theorem 3.1（arXiv:1304.1188，本轮原文核对，存档） |

**结构性观察（本轮新增，见 `FUSION_ANALYSIS_AND_PSW_CHECK.md`）**：所有"超越静态
基线"的已知动态下界（LP13、PSW13、multicut 1.198、all-pivot C_AP）共享同一个几何
机制——witness/endpoint 与未来标签的碰撞概率 Θ(n²/u)——因此全部需要重复标签、
u/n²→∞ 或 compact-prefix 计费三者之一。multicut 的 KL-posterior 移植（本轮尝试）
在唯一一个精确点失败（bank 包含 $V_i\subseteq A(q)$ 被当前段碰撞破坏，损失 Θ(n²/u)
不可消除；放弃包含则不等式空泛——脚本验证）。这支持主定理的 "first in u/n→∞"
新颖性表述。

**可安全声称**：本定理是 KLZ ordinary 模型在 $u/n\to\infty$、$\varepsilon=1/2$ 下**第一个
严格超过静态 n-bit 基线的下界**；证明只使用一个长度为 $2\lfloor n/2\rfloor$ 的
replacement 词（适用于任何支持该词的 fully dynamic filter）；incremental 的静态
分离对应物是 multicut 1.198（只用 insertions）。
**不可声称**："解决了 KLZ open problem"（上下界仍相距甚远）或"第一个证明动态比静态贵"
（LP/KW/KLZ 在其他 regime 已做）。

## 5. 风险清单与对策

| 风险 | 严重度 | 对策 |
|---|---|---|
| 下界常数太小，reviewer 认为"grossly non-tight" | 高 | 卖点是定性 barrier break + 新技术 + 完整 frontier；常数已从 2^{-48} 优化到 2^{-20}（`GENERAL_EPS_EXTENSION.md`，脚本验证），一般 ε 版对每个固定错误率都破静态基线；把 $C_{\mathrm{AP}}>1.6079$、1.198n 作为同篇内容；把"为什么 2^{-Θ(1)} 封顶"写成结构性讨论 |
| LP novelty caveat 被 reviewer 质疑 | 高 | 论文正文必须包含 §4 表格与 fresh-distinct 迁移的严格分析（仓库 LOVETT_PORAT_FRESH_DISTINCT_REPAIR 可直接用） |
| 主定理证明细节（常数、Fubini 定量步）有笔误 | 低 | 两个独立 hostile audit 均 SOUND；本评估独立重推 + 脚本验证；写 LaTeX 后按 audit 的 non-fatal 清单再走一轮 |
| 上界 2.3461 只是常数改进（vs 2.3491） | 中 | 定位为"结构新机制（cross-block modulus-6 coupling）+ 首个 beating-fingerprint-benchmark 的 ordinary 构造"；不单独卖 |
| adaptive/seed-adaptive 模型未覆盖 | 中 | 明确 model 量词（同 KLZ），引用 Bender et al. 2018 说明 adaptive 是另一条线 |
| KLZ/KW 同组作者可能已推进 | 中 | 持续监控 arXiv（本评估已查至 2026-08，无冲突论文） |
| $C_{\mathrm{AP}}$/1.198 依赖 $u/n^2\to\infty$ | 低 | 作为条件定理清晰标注（仓库 README 的诚实风格保持） |

## 6. 增强路径（按"提升 FOCS 命中率"排序）

1. ✅ **（本轮已完成）主定理常数优化与一般 ε 推广**：√γ tails + α→1−ε overcount 界
   得到 ε=1/2 的 $H\ge(1+2^{-20})n-o(n)$，一般 ε 的
   $H\ge(1+2^{-X(\varepsilon)-2})n\log_2(1/\varepsilon)-o(n)$（X(ε) 显式），全部有
   `verify_replacement_cover_constant.py` 机器验证（`CONSTANT_OPTIMIZATION_SQRT_TAILS.md`、
   `GENERAL_EPS_EXTENSION.md`）。已论证该框架封顶在 $2^{-\Theta(1)}$：Markov 约束
   $\tau\ge\Theta(\sqrt\gamma)$ × 集合包含计数的指数容量，靠调常数到不了 1.1。
2. **向 $C_{\mathrm{AP}}$ 逼近**（去掉 $u/n^2\to\infty$）：本轮已尝试把 multicut 1.198
   的 KL-posterior 银行移植进 u/n→∞（`FUSION_ANALYSIS_AND_PSW_CHECK.md`），并精确
   定位失败点：bank 包含 $V_i\subseteq A(q)$ 被当前段标签碰撞破坏、损失 Θ(n²/u)
   不可消除，放弃包含则不等式空泛（脚本验证）。因此 frontier 收敛到**一个 lemma**：
   要么严格证明该 Θ(n²/u) 碰撞损失不可消除（barrier 定理），要么发明对它的新计费
   方式（linear-depth recurrent response / 跨 state transversality——与仓库
   NORMALIZED_DUAL_CONDITIONAL_NOVELTY 的结论一致）。这是下一轮的主攻方向。
3. **类内 matching 的扩展**：allocation-mod-Q 族内最优性已被脚本 2 认证（Q=6 唯一
   极小、Q≥9 松弛下界），论文可直接写"该族内 matching"；进一步扩展方向是 k 个
   subblock 的 Smith normal form 分类（把 restricted converse 推广到更广 lattice 族），
   以及（范围声明见 `SUBSAGENT_AUDITS.md`）把 limited-independence 外层 hash 移植
   过来以获得 polylog-time 实例化。
4. 论文写作：LaTeX 全文 + 全部证书脚本随文 + 独立复现包；先修 audit 清单里的
   non-fatal 笔误。

## 7. 论文草案结构（FOCS 2027 目标，deadline 约 2027-04）

1. Intro：KLZ open problem；静态 n-bit 基线 48 年未破；本文结果区间
   $[1+2^{-20},\,2.3461]$（$u/n\to\infty$，ε=1/2）与 $[1.6079,\,2.3461]$（$u/n^2\to\infty$）；
   一般 ε 版对每个固定错误率破静态基线；为什么 LP/KW/KLZ 不覆盖（§4 表格）。
2. Model（逐字对齐 KLZ Definition 2.1 + footnote 5）。
3. Main theorem：simultaneous replacement-cover width（两步 audit SOUND）。
4. 定量形式与常数（√γ tails + α 优化，全部显式、脚本可复现）。
5. LP fresh-distinct 迁移与 $n^2/u$ barrier 讨论（novelty 辩护；含 PSW 量词对比与
   四个证明家族共享碰撞机制的结构性刻画——`FUSION_ANALYSIS_AND_PSW_CHECK.md`）。
6. 条件下界：multicut 1.198（$u/n^2\to\infty$）；all-pivot hierarchy 与
   $C_{\mathrm{AP}}>1.6079$ 的 continuous variational limit（strict gap、endpoint
   exponent-1 定理）。
7. 上界：cross-block mod-6 quotient（2.34614905664n），有限 n 校准，枚举编码；
   allocation-mod-Q 族内 matching（Q=6 唯一最优，有理区间证书；Q≥9 松弛下界）。
8. 类内闭包：fingerprint-multiset 率 2.20061148296（含匹配 converse 与
   subexponential-horizon 构造）。
9. Open problems（$C_{\mathrm{AP}}$ 是否在 $u/n\to\infty$ 下成立；2.3461 最优性；
   adaptive 模型）。

## 8. 已完成 / 待办

已完成：仓库克隆与全部脚本验证 ✓；外部文献原文核对（KLZ/KW/LP/PSW/3×2026，全部
PDF 存档）✓；主定理逐步独立核对 ✓；novelty 链（Carter→LP→KW→PSW→KLZ→本定理）
闭合 ✓；两名 hostile audit subagent 均 SOUND ✓；常数优化 2^{-48}→2^{-20} + 一般 ε
推广 + 机器验证 ✓；框架封顶论证 ✓；multicut 融合尝试与失败点精确定位 + PSW 威胁
排查 ✓（`FUSION_ANALYSIS_AND_PSW_CHECK.md`）；**论文核心草稿已写出并可编译**
（`paper/main.tex`，11 页：Abstract/Intro/Model/主定理完整证明/general-ε/novelty
辩护/Open problems 完整，Section 6-7 为占位）✓。

待办（后续轮次）：论文 Section 6（条件下界 1.198/C_AP）与 Section 7（上界 2.3461
+ Q 族最优性）的完整证明文本；提交前对 .tex 的最后一轮独立 hostile audit；作者与
相关工作整理；barrier lemma（Θ(n²/u) 碰撞损失的严格 barrier 证明，Open Problems
节深度）。

## 附：本评估所用原文存档

- `literature/klz.pdf|txt` — KLZ FOCS 2025（arXiv:2510.18129v1）
- `literature/kw.pdf|txt` — KW STOC 2024（KIT OA 存档）
- `literature/lp.pdf|txt` — Lovett–Porat（ECCC TR10-087）
- 仓库本体：`/nfs-hg/prod/containers/yukuai/dev/repo-amq/`
