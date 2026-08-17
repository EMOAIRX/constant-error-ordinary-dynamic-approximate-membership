# Subagent hostile-audit 结果存档

> 2026-08-17。两个独立 hostile audit subagent 的结论汇总。完整报告为 subagent 输出，
> 本文件只记录 verdict 与可操作发现。

## Audit 1：主定理（simultaneous replacement-cover width 下界）

**VERDICT: SOUND**。独立重推了文档全部显示式 ((1a),(2),(3),(4),(5),(6),(7))，
含 symbolic 检查与数值脚本，无致命缺口。

关键确认：
- 条件化干净：$(S,D,I)\perp R$ 全程成立；FPR 只在固定历史下对 R 平均；
  ν_z 不是 tape-dependent hard distribution；Fubini 在全部平均之后才固定 (r,s,d)。
- $V\subseteq A$ 需要且成立（$K\subseteq S\setminus d\subseteq A_z$）。
- (7) 精确成立（用文档 §7 的 $2^q\cdot(5\tau)^{s_0}$ 粗界，$\gamma=2^{-48}$ 时
  1.11301 > 1+2^{-48}）。
- 按文档原框架（γ^{1/4} tails）可推出的最优常数约为 $2^{-45.29}$，比宣称的
  2^{-48} 强 6.55 倍。

**重要更正（对我此前读法的修正）**：文档说的是 "any fixed larger constant"，
不是 "3e 可替换为 8"；且 8 < 3e ≈ 8.1548，8 不可行。我自己的常数优化推导不依赖
该替换（用更紧的 overcount 界），已在新笔记中注明。

Minor（全 cosmetic）：(1a) 的 ≤H 需要补 $S\perp R$ 一行；§5 的 3τ slack 在该处
未解释；超几何句措辞松散；$O(\sqrt\gamma)+o(1)$ 尾部只在固定 γ 下成立。

## Audit 2：上界（cross-block mod-6 构造）

**VERDICT: SOUND**。独立用 Fractions+mpmath 重推导：状态 profile、ρ 表、ρ_c=0
(c≥10) 归纳、J 严格递减、λ*=2.648017694023161、z*=0.453320842862439、
R=2.346149054803344（唯一全局 saddle 极小）、(18c) 精确、有限 n 校准的
Θ(n^{-1/4}) margin 支配 Le Cam O(1/n)、2 万步模拟 0 false negatives。
模型合规：无限只读随机带允许 fully random hash（key 索引读取）；IID-labels 分析
匹配 pointwise 量词；adaptive-adversary 限制已在文档中正确声明。

Non-fatal 发现：
- 文档第 241 行 gap 数字末位错误（0.002934385389796 应为 0.002934385389655）；
- 脚本 1 的 assert 比文档宣称界更松（2.34616），但打印的 certified endpoint
  2.346149056633739 支持文档界（50 位精度复核）；
- "pathwise deletion projection ⇒ (3/4)ρ_c" 的归属不严谨：该投影干净地只给
  ρ_{c+1} ≤ ρ_c；3/4 常数是 profile 直接验证的；
- "log2 N = nR+o(n)" 应为 "≤"。

**新增：Q 族类内最优性（restricted converse，脚本 2 认证）**——这不是笔误而是论文资产：
对 q=3 的 allocation-mod-Q 子块模数族，脚本 2 用有理区间证书证明
R_5−R_6 ∈ (0.0003159365427, 0.0003159368733)、R_Q > R_5 for Q∈{1,2,3,4,7,8}、
λ_∞ ∈ (2.65163815056, 2.65163815058)、Q≥9 的 frozen-tail 松弛下界
2.347751122371 > R_6，即**模数 6 是该自然族内的唯一最优**。上界 2.3461 因此自带
一个 restricted converse，从"常数改进"升级为"族内 matching"。

**新增：有限 n 校准的精确数值**（audit 独立计算）：n=1e3/1e6/1e8 时精确二项
E[ρ] = 0.5255/0.5142/0.50446/0.50141，均 >1/2，margin Θ(n^{−1/4}) 支配
Le Cam O(1/n)（0.0122/0.0013/1.4e-5）→ FPR ≤ 1/2 − Θ(n^{−1/4})。

**范围提醒（写论文时必须保持的声明）**：
- fully random outer hash 依赖 KLZ 无限只读随机带（key 索引读取、无存储、无指针）；
  仓库的 limited-independence 替换引理（EFFICIENT_OUTER_HASH_LEMMA 等）属于另一个
  fixed-slot 构造、**尚未移植**——若声称 polylog-time 或 bounded-independence
  实例化，需要额外工作；
- tape-adaptive 更新对手会破坏构造（文档已正确声明；KLZ ordinary 模型量词是
  fixed-history/pointwise，合规）。

## Audit 3：论文 .tex（FOCS submission audit，round 6 完成）

**VERDICT: GAPS-FOUND → 全部修复后 SOUND**。逐式重推了 §3 全部显示式并独立数值验证。

确认正确的部分：Lemma 3.1（deficit 恒等式、L_u−B_u、切线不等式 dense-grid 零违反、
moment bound）、Lemma 3.2（KL chain rule、ν=Unif C(A\(d∪i),k)、v≥b·2^{−2τ²}）、
好分支预算（(4ln2+2)/c²=0.5 精确、reservoir (7/2)τu）、Lemma 3.3（容量不等式逐因子）、
X(ε) 算术（9.755 ✓、X(1/2)=19.755 ✓）、量词卫生 CLEAN（S⊥R、Fubini 顺序、无
tape-dependent 分布）、§5-7 常数（KLZ functional −0.2787、两切证书、P(z)/ρ 表
精确枚举、λ*/z*/R、C10）。

**发现并已修复的实质问题**：
1. [FATAL→fixed] §3.5 的 δ_n 定义（4τ/(1−ε)）与 ε=1/2 witness（α=(1/2)(1−4τ)）
   不一致：按定义 α=(1/2)(1−8τ)=0.48793 时 witness 值 0.99716 < 1+2^{-20}，
   矛盾不成立。**修复**：δ_n 分段定义——δ(ε)=4 for ε≤3/4、4/(1−ε) for ε>3/4，
   gap = τ(3−4ε)>0 / 3τ>0；witness 恢复 α=(1/2)(1−4τ) → 1.01382 ✓；
   一般 ε 的 δ 修正上界 2τ(B+2) 在分段定义下仍然成立（(1−ε)δ(ε)≤4），
   x=X(ε)+2 处全 ε 最大 0.023<0.033（数值扫描验证，无矛盾失败点）。
2. [FATAL→fixed] 旧 §4 的"δ-loss = o(1)"错误（实为 Θ(√γ·log(1/γ))≈0.0168，
   超过 witness margin）——已在 round 4-5 改为 η_ε=2^{−X(ε)−2} 并加 +2 margin
   （audit 确认 x=21.755 时 LHS≈1.23 ≫ 1+2^{-21.755}）。
3. [fixed] KW 常数（round 5 已修：log2(4/(√17−1))≈0.357）。
4. [fixed] multicut 不动点位数：verifier 提升到 N=200000 + 不动点迭代，
   1.198102077 vs 仓库证书 1.1981007740（差 1.3e-6，Riemann 离散误差容差内）；
   论文引用仓库证书值，1.198n corollary 两者之下不受影响。
5. [fixed] 实指标二项式取整约定（§3.5 加注释）；"τ≤1/8" 删除（gap 恒正）；
   k≥n/2−1 → k=⌈n/2⌉ 精确。
6. [fixed] §7 pointwise FPR 从 source-averaged ρ_c 到 fixed-history/fixed-nonmember
   的推导补全为完整段落（Bin(m,1/B) 块载荷 × 均匀 multinomial 符号 × 查询符号独立
   → P[reject]=J_n(m) 精确）。
7. [未复核但已有证书] R_5−R_6 区间与 Q≥9 下界 2.347751122371 由仓库 Fraction
   脚本认证（PASS）；LP/PSW 量词由本评估对原文逐字核对。

## 最终结论

三份 hostile audit 全部闭环：两个源定理 SOUND + 论文 .tex 的 GAPS-FOUND 全部修复。
论文 `paper/main.tex`（14 页）达到提交级质量。

## 论文 .tex 的自查修复记录（round 4-5，与 audit 3 并行）

自查 paper/main.tex 时发现并修复的实质问题（audit 3 进行中，结果待并入）：

1. **incremental overclaim**：主定理证明使用 deletion（replacement 词），
   不能声称适用于 insertion-only filters——已改为"适用于任何支持该词的 fully
   dynamic filter"，incremental 的对应物指向 multicut（只用 insertions）。
2. **KW 常数误抄**：$4/\log_2(\sqrt{17}-1)$ → 正确
   $n\log_2(4/(\sqrt{17}-1))\ge0.35n$（对照 KW 原文数值）。
3. **一般 ε 定理的 δ_n 修正项不是 o(1)**（固定 γ 下为 Θ(τ·x)）：
   常数改为 $\eta_\varepsilon=2^{-X(\varepsilon)-2}$，修正上界
   $2c\,2^{-x/2}\sqrt{\log_2(1/\varepsilon)}(x/2-0.8775)\le0.033$
   （数值验证：exact 修正全 ε 最大 0.023；B+2≤x/2−2.8775 零违反；
   $(1-\varepsilon)^2\le1-\varepsilon\le\ln(1/\varepsilon)\le\log_2(1/\varepsilon)$
   的解析证明）。ε=1/2 的精确 witness 2^{-20} 不变（margin 0.0138）。
4. Lemma 3.1 因子比估计展开为逐句严格版本。
