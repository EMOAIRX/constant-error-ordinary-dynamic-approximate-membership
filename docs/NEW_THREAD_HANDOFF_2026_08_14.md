# 新对话完整 Handoff：constant-error ordinary dynamic approximate membership

> 更新时间：2026-08-14，Asia/Shanghai。  
> 当前工作目录：本仓库根目录。  
> 本文用于直接交给一个新对话继续研究；必须保留 theorem / candidate / barrier 的区分，不得把中间结果包装成完整 closure。

---

## 0. 用户的最终目标与研究标准

用户希望研究 FOCS 2025 Kuszmaul--Liang--Zhou（KLZ）留下的 fixed-constant-error dynamic approximate membership open problem，目标是得到对社区真正有贡献、最好能够 close 的结论，而不是继续优化受限模型中的有限维小数。

用户的硬要求：

- 使用中文，严格、诚实、可读；
- 不喜欢 computer-assisted proof、浮点 optimizer 或区间证书作为主成果；
- 不接受 restricted-family 的数值最优被包装成 ordinary-model closure；
- 不希望依赖 history independence、monotonicity、locality、canonical representation 等强假设；
- 需要 matching upper/lower bound、严格更优的 ordinary construction，或真正关闭一大类方法的结构性 theorem；
- 必须明确区分：已证明 theorem、candidate/conjecture、barrier/counterexample；
- 应从真实应用和社区问题切入，而不是围绕用户旧笔记展开；
- 可以并且应当使用多个 subagents 并行探索，但最终必须由主 agent 做 hostile audit。

最终成功标准只有三类：

1. ordinary model 的 matching theorem；
2. 严格低于 fingerprint candidate rate 的合法 ordinary construction；
3. 足够广、足够自然、能显著改变社区路线选择的结构性 barrier/theorem。

---

## 1. 文献基线与社区公开问题

核心论文：Kuszmaul--Liang--Zhou，*Fingerprint Filters Are Optimal*，FOCS 2025 / arXiv:2510.18129。

KLZ ordinary 模型：

- universe (U=[u])，容量 (n)；
- 固定长度 (H)-bit persistent memory；
- 免费、random-access、read-only public random tape；
- `Initialize/Insert/Delete/Query`；
- Insert/Delete 只收到 key 与当前存储状态，不获得真实集合或 insertion handle；
- 每条 tape 上 zero false negatives；
- 对每个固定 current nonmember，FPR 对随机带至多 \(\varepsilon\)；
- 不假设 history independence、monotonicity、canonical state、locality 或 exact backing dictionary。

KLZ 已证明：当

\[
\varepsilon=o(1),\qquad u=\omega(n/\varepsilon),
\]

且支持 (omega(n)) updates 时，

\[
H\ge n\log(1/\varepsilon)+n\log e-o(n).
\]

KLZ Section 6 明确留下：

\[
\varepsilon^{-1}=\Theta(1)
\]

时的 sharp upper/lower bounds。作者猜测 entropy-encoded fingerprint multisets 仍最优，但没有证明 arbitrary-filter lower bound。

2026 相关进展：

- Blelloch--Hu--Kuszmaul--Li--Zhou，arXiv:2608.06066，给出 uniform Poisson fingerprint entropy rate 的高效动态 entropy array 实现；空间/时间是 whp 语义，不是 KLZ 每 tape fixed-(H) guarantee。
- *Resizable Retrieval*，arXiv:2606.15944，研究 resizable retrieval/filter，不闭合 constant-error sharp linear coefficient。
- *Hallucination is a Consequence of Space-Optimality*，arXiv:2602.00906，给静态 membership testing rate-distortion，不处理动态 transition closure。

文献审计：

[FOCS25_MODEL_CONSTANTS_AND_2026_FOLLOWUPS_AUDIT.md](./FOCS25_MODEL_CONSTANTS_AND_2026_FOLLOWUPS_AUDIT.md)

---

## 2. 当前研究的精确量词

必须区分三种 history：

1. **Oblivious/fixed history**：整条合法 history 在 public tape 抽取前固定；endpoint sets 与 query keys 与 tape 独立。
2. **Output-adaptive history**：后续操作依赖此前 query answers。
3. **Seed-adaptive history**：对手直接读取 random tape/hash seed 后选 keys。

目前完整上界覆盖的是：

\[
\omega(n)\le f(n),\qquad \log f(n)=o(n),
\]

且每条 history 预先固定、与 tape 独立。

自然 universe 条件：

\[
u/n\to\infty.
\]

不能把这一结果称为 output-adaptive、seed-adaptive 或 arbitrary infinite-history upper bound。

严格 adaptive 反例：

- output-adaptive 对手扫描预先准备的 nonmembers，找到第一个 YES 后立即重查同一个 key；第二次条件 FPR 为 1，且对 fingerprint construction 以 (1-o(1)) 概率能找到 YES；
- seed-adaptive 对手可直接选 top key，或选择与当前 member 同 fingerprint fiber 的 nonmember，FPR 为 1。

---

## 3. Candidate optimal rate (R_{\rm fp})

定义

\[
g(\lambda)=1-e^{-\lambda},\qquad
r(\lambda)=\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda}.
\]

候选 fingerprint rate 是曲线

\[
\bigl(g(\lambda),r(\lambda)\bigr)
\]

与 permanent-YES endpoint ((1,0)) 的 lower convex envelope：

\[
R_{\rm fp}(\varepsilon)
=
\inf_{\mu:\,\mathbb E[1-e^{-\Lambda}]\le\varepsilon}
\mathbb E\!left[
\frac{H_2(\operatorname{Pois}(\Lambda))}{\Lambda}
\right].
\]

等价的 finite mixture 形式：tracked type (i) 质量为 (	heta_i)，cell 数 (q_i=c_i n)，load

\[
\lambda_i=\theta_i/c_i,
\]

则 rate 与 rejection 为

\[
R=\sum_i c_iH_2(\operatorname{Pois}(\lambda_i)),
\qquad
1-\varepsilon=\sum_i\theta_i e^{-\lambda_i}.
\]

phase transition：

\[
\lambda_*=0.4399316012\ldots,
\qquad
\varepsilon_*=1-e^{-\lambda_*}=0.3559195261\ldots,
\]

高误差支斜率

\[
C_*=e^{\lambda_*}r(\lambda_*)
=4.4012229659\ldots.
\]

因此

\[
R_{\rm fp}(\varepsilon)=
\begin{cases}
r(-\ln(1-\varepsilon)),&\varepsilon\le\varepsilon_*,\\
C_*(1-\varepsilon),&\varepsilon\ge\varepsilon_*.
\end{cases}
\]

半误差：

\[
R_{\rm fp}(1/2)=2.20061148296\ldots.
\]

这些小数只用于定位；主 theorem 可使用 convex-envelope 的符号定义，不依赖 numerical certificate。

---

## 4. 已完整证明：oblivious subexponential-horizon sharp upper bound

### Theorem A

对每个固定 (0<\varepsilon<1) 和每个满足

\[
\log f(n)=o(n)
\]

的 horizon，在 KLZ free-random-tape、time-unrestricted 模型中，存在 fixed-worst-case-space ordinary dynamic filter，使对每条预先固定、长度至多 (f(n)) 的合法 history：

\[
H\le nR_{\rm fp}(\varepsilon)+o(n),
\]

逐 tape zero false negatives，pointwise FPR 至多 \(\varepsilon\)。

### 构造核心

- 使用 heterogeneous categorical fingerprint map；高误差支使用 frozen permanent-YES mask。
- persistent state 精确维护 light-cell multiplicity vector。
- 对每个 current cardinality (k\le n)，只编码 occupancy law (P_{n,k}) 的 information-spectrum typical family
  
  \[
  \mathcal A_{n,k}
  =\{c:-\log P_{n,k}(c)\le B_n+C\log n+t_n\}.
  \]

- 所有 (k) 共用同一个 fixed slot，另存 (O(\log n))-bit cardinality；不是把 (n+1) 个 codebooks 的大小相加。
- normal update 精确修改 count vector；若 successor 不在 typical family，则进入 absorbing `ALL-YES`。
- sticky state 不产生 false negatives；其概率直接加到 FPR，而不是被排除在 correctness 外。

参数：

\[
a_n=\log(f(n)+2)+\log(n+2),
\]

\[
t_n=n(a_n/n)^{1/4},
\qquad
\eta_n=(a_n/n)^{1/8}.
\]

则

\[
t_n=o(n),\qquad
t_n^2/n=\sqrt{na_n}=\omega(a_n),
\]

从而

\[
f(n)\operatorname{poly}(n)e^{-\Omega(\sqrt{na_n})}
=o(\eta_n).
\]

### 正确 finite-(n) FPR

若总 light mass 为 (alpha_n)，有 (M_n) 个等概率 light cells，每个概率 (p_n=\alpha_n/M_n)，则容量 (k) 的精确 FPR 是

\[
1-\alpha_n(1-\alpha_n/M_n)^k.
\]

旧公式 (1-\alpha+\alpha[1-(1-1/M)^k]) 是错误的，因为 current member 撞指定 light cell 的概率是 (alpha/M)，不是 (1/M)。这个错误已经修复。

### 完整解析 tail lemma

对 light count vector (C^{(k)}) 的 information density

\[
\imath_{n,k}(C)=-\log P_{n,k}(C),
\]

已证明 uniform tail：

\[
\Pr\!\left[
\imath_{n,k}(C)>
M_nH(\operatorname{Pois}(\alpha_nn/M_n))+C\log n+t
\right]
\le
C n^C e^{-c\min\{t^2/n,t\}}.
\]

证明包含：

- Poisson self-information 的 uniform Rényi-mgf；
- centered log-mgf 与 Bernstein；
- exact de-Poissonization，只损失 (O(\log n))；
- (alpha=1) branch；
- top branch 中 tracked total (K\) 的向上波动；
- low-load layers 使用
  
  \[
  \Pr[I>L]\le |\operatorname{supp}|2^{-L},
  \]
  
  而不是错误地声称 support size 逐点上界 self-information。

### Random tape 实现

使用每个 key 固定寻址的 (L_n)-bit tape block：

\[
L_n=\left\lceil3\log_2n+\log_2(1/\eta_n)\right\rceil.
\]

把 (2^{L_n}) 个值平均分给 (M_n) 个 light intervals，剩余映到 top；每个 light cell 概率完全相等。无 rejection-sampling 无界 local counter，也无随 history 增长的 pointer。

完整文件：

[SUBEXPONENTIAL_HORIZON_FINGERPRINT_UPPER_BOUND_AUDIT_2026_08_14.md](./SUBEXPONENTIAL_HORIZON_FINGERPRINT_UPPER_BOUND_AUDIT_2026_08_14.md)

### 安全 headline

可以称：

> Oblivious subexponential-horizon fixed-worst-case-space fingerprint upper bound.

不能称：

- adaptive robust filter；
- arbitrary infinite-history upper bound；
- self-contained charged-seed efficient implementation。

---

## 5. 已完整证明：ordinary filters 的 exact right-congruence minimax formulation

固定 tape (r) 后，一个 (K)-state filter 给 history language (Omega_n) 上的 labeled right congruence：

\[
f_r(h)=f_r(h')
\Longrightarrow
f_r(hw)=f_r(h'w)
\]

对所有两边都合法的共同 continuation (w)。

state class (C) 的最小安全 accepted set：

\[
A_C(C)=\bigcup_{h\in C}S(h).
\]

定义 rejection profile

\[
z_C(h,x)=\mathbf1[x\notin A_C([h]_C)].
\]

ordinary public-coin filter 精确等价于 index 至多 (K) 的 deterministic right congruences 的分布 (mu)，满足

\[
\forall(h,x),\qquad
\mathbb E_{C\sim\mu}z_C(h,x)\ge1-\varepsilon.
\]

minimax：

\[
V_n(K)
=\max_\mu\min_{(h,x)}\mathbb E z_C(h,x)
=\min_\pi\max_{C:\operatorname{index}(C)\le K}
\mathbb E_{(h,x)\sim\pi}z_C(h,x).
\]

所以要证明

\[
H>Rn,
\]

充要的是构造 seed-independent dual distribution (pi_n)，使每个 index (le2^{Rn}) 的 deterministic right congruence 平均 rejection 小于目标。

这一 formulation 完整覆盖：

- arbitrary history dependence；
- multiple representations；
- ghosts；
- global certificates；
- relocation；
- nonmonotonicity；
- overlapping endpoint fibers。

文件：

[RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md](./RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md)

以及 finite-horizon equivalence：

[LONG_RANGE_ONLINE_STATE_MERGING_AUDIT_2026_08_13.md](./LONG_RANGE_ONLINE_STATE_MERGING_AUDIT_2026_08_13.md)

---

## 6. 已完整证明：source-weighted simultaneous branch-width theorem

考虑 grouped-cell label-level count lattice

\[
\mathcal C_{n,q}=\{c\in\mathbb N^q:\|c\|_1\le n\}.
\]

对每个 count vector (c) 固定 canonical build history，得到 deterministic tape (r) 的 state (M_r(c))。从该 state 删除 coordinate (j) 的全部 (c_j) copies，然后 query (j)，记 rejection 为 (Z_r(c,j))。

对 state fiber 定义 coordinatewise upper envelope：

\[
A_j(m)=\max_{c:M_r(c)=m}c_j.
\]

common deletion continuation 给出：

\[
Z_r(c,j)le\mathbf1[c_j=A_j(M_r(c))].
\]

若 (C) 是任意 count-vector source，(J) 是独立 coordinate source，定义

\[
\mathsf R^+_{C,J}(\alpha)
=\inf I(C;A),
\]

其中

\[
A\ge C\quad\text{coordinatewise},
\qquad
\Pr[A_J=C_J]\ge\alpha.
\]

### Theorem B

每个 (K)-state deterministic label-level transducer 满足

\[
\log K\ge\mathsf R^+_{C,J}(\alpha_r),
\]

public-coin FPR 至多 \(\varepsilon\) 推出

\[
H\ge\mathsf R^+_{C,J}(1-\varepsilon).
\]

意义：

- 是 source-weighted，不是逐 worst fiber；
- 在一个 simultaneous persistent state 上收费；
- 自动允许 coordinate erasure / frozen masks；
- 严格强于 endpoint mutual-information accounting。

严格缺口：snapshot one-sided RDF 允许

\[
A=
\begin{cases}
1,&C\in\{0,1\},\\
C,&C\ge2,
\end{cases}
\]

但 cell ({0,1}) 不满足 Insert successor closure：同一 state 上 Insert 必须把 0 与 1 分别送到逻辑 1 与 2。

因此下一对象是

\[
\boxed{
\text{one-sided Poisson RDF}
\cap
\text{labeled successor-closed cells}.}
\]

文件：

[SUBEXP_HORIZON_WIDTH_TARGET_AND_LINEAR_SYNDROME_BARRIER_2026_08_14.md](./SUBEXP_HORIZON_WIDTH_TARGET_AND_LINEAR_SYNDROME_BARRIER_2026_08_14.md)

---

## 7. 已完整证明：linear-degree Johnson-syndrome barrier

取 random columns

\[
a_x\in\mathbb F_2^H,
\qquad H=\eta n+O(1),
\]

并定义 transition-compatible XOR transducer

\[
f(S)=\bigoplus_{x\in S}a_x.
\]

Insert/Delete 都执行 xor (a_x)，支持任意长 history。

若 layer (j/n\to\beta>0)，固定

\[
0<\vartheta<\beta/2,
\]

则存在 columns realization，使对每个 syndrome (m)、每个 (|B|\le\vartheta n)，

\[
\#\{S\in{U\choose j}:B\subseteq S,f(S)=m\}
=2^{-H}{u-|B|\choose j-|B|}(1+o(1)).
\]

证明用 pairwise independence + union bound，关键 exponent：

\[
-(\beta-2\vartheta)n\log(u/n)+O(n)=-\omega(n).
\]

因此每个 fiber 对所有严格低于 half-layer 的线性阶 inclusion statistics 都近似 uniform。

结论：任何 theorem 若只使用

- state budget/right congruence；
- 低于 half-layer 的 prescribed-coordinate sections；
- Johnson components、bounded-order moments 或 local marginals；

却不把 accepted support/FPR 与 transition width 放入同一个 inequality，就不能得到正 selectivity premium。

---

## 8. Two-choice / cuckoo 路线的严格校正

### 8.1 Stateless route collapse

若候选 tuple

\[
H(x)=(h_1(x),\ldots,h_d(x))
\]

经过固定公开函数

\[
\phi(H(x))
\]

选择 update label，则逻辑 update-label process 精确退化为一个 categorical map

\[
f=\phi\circ H.
\]

如果物理状态 exact 地维护 label multiplicities，则 rate/FPR 是 load mixture：

\[
R=\int r(\lambda)d\nu(\lambda),
\qquad
\varepsilon=\int g(\lambda)d\nu(\lambda),
\]

因此

\[
R\ge R_{\rm fp}(\varepsilon).
\]

这个 theorem 只关闭：

> public stateless routing + exact multiplicity encoding。

不能误写成关闭所有 key-recomputable routes，因为 lossy ghosts、mod residues、global quotients 并不恢复 exact count vector。

### 8.2 Canonical per-label count-only dichotomy

若单 label local state 只依赖当前 count

\[
m=\psi(c),
\]

且是 canonical right congruence，则：

- 若 (psi(0)) query NO，则 (psi(0),\ldots,psi(N)) 两两不同，等价于 exact counter；
- 若 (psi(0)) query YES，则该 label 在所有 counts 上永久 YES。

所以 independent per-label canonical summaries 只能是 exact counters + permanent-YES labels，Poisson source rate仍不低于 (R_{\rm fp})。

该结论不覆盖 multi-label coupling 与 history-dependent ghost states。

### 8.3 旧 (2.1216107112n) two-choice 数字为何无效

旧 min-rank calculation 让 query OR 两个 candidate cells，得到 support-only snapshot rate

\[
2.1216107112n<R_{\rm fp}(1/2)n.
\]

但 min-rank route 是公开可重算的；正确 query 应只 probe selected cell。旧数字同时犯了两件事：

1. 使用不必要的 two-probe query rule；
2. support-only state 无法在 Delete 时判断 last copy，因而不是合法动态 state。

真正的 two-choice 收益只能来自 state-dependent orientation；这时必须一起收费：

- query support；
- deletion route；
- last-copy certificate；
- relocation transcript；
- multiplicity/stash；
- recoverable overflow；
- fixed-memory failure semantics。

额外 benchmark：collision-free symmetric cuckoo placement 在 half error 时 support entropy约为

\[
2.978\ldots n,
\]

远高于 (R_{\rm fp})。它说明：0/1 loads 消除 last-copy 问题，但 support 太贵；允许 collisions 压低 support，又必须支付 reversible multiplicity。

文件：

[DCHOICE_INFORMATION_CONSERVATION_2026_08_14.md](./DCHOICE_INFORMATION_CONSERVATION_2026_08_14.md)

---

## 9. 已完整证明：任意 Abelian additive quotient 的 entropy-certificate theorem

考虑有限 Abelian group (Gamma)，label (a\sim\mu) 对应 (v_a\in\Gamma)。block load 为 (c) 时保存

\[
Z_c=\sum_{i=1}^c v_{A_i}.
\]

同时可保存 exact total load (c)。Insert/Delete 做群加减，因此支持任意长 key-only history，并可从 high load 恢复。

给定 (Z_c=z)，最小安全 accepted-label set：

\[
K_c(z)=\{a:\Pr[Z_{c-1}=z-v_a]>0\}.
\]

state rejection prior mass：

\[
R_c(z)=1-\mu(K_c(z)),
\qquad
\bar R_c=\mathbb ER_c(Z_c).
\]

### Theorem C

对每个 (c\ge1)，

\[
H(Z_c)-H(Z_{c-1})
\ge
\mathbb E\log_2\frac1{1-R_c(Z_c)}
\ge
\log_2\frac1{1-\bar R_c},
\]

并且

\[
H(Z_c)
\ge
c\,\mathbb E\log_2\frac1{1-R_c(Z_c)}
\ge
c\log_2\frac1{1-\bar R_c}.
\]

证明关键：

- posterior (P_{A_c|Z_c=z}) 支撑在 (K_c(z))；
- 相对 prior (mu) 的最小 KL 是 (-\log\mu(K_c(z)))；
- 群平移给
  
  \[
  I(A_c;Z_c)=H(Z_c)-H(Z_{c-1});
  \]

- independent labels 给
  
  \[
  \sum_i I(A_i;Z_c)\le H(Z_c).
  \]

定义 entropy increments

\[
\Delta_c=H(Z_c)-H(Z_{c-1}),
\]

则

\[
\Delta_1\ge\Delta_2\ge\cdots\ge0,
\qquad
\bar R_c\le1-2^{-\Delta_c}.
\]

单调性来自 data processing：加一个 independent group increment 只能降低关于旧 label 的信息。

Poisson block (C\sim\operatorname{Pois}(\lambda)) 时：

\[
\mathcal H
=H_2(\operatorname{Pois}(\lambda))
+\sum_{c\ge1}p_cH(Z_c),
\]

\[
\beta=p_0+\sum_{c\ge1}p_c\bar R_c,
\]

以及

\[
\mathcal H
\ge
H_2(\operatorname{Pois}(\lambda))
+\sum_{c\ge1}p_c c\log_2\frac1{1-\bar R_c}.
\]

### 已否决的过强命题

逐 occupancy layer 的

\[
H(Z_c)\ge C_*c\bar R_c
\]

为假。最小反例：\(c=1\)，两个均匀 labels，\(H(Z_1)=1\)、\(\bar R_1=1/2\)，而 \(C_*/2>2\)。正确 KL bound 在这个例子取等。

因此若 sharp high-error converse

\[
\mathcal H\ge C_*\lambda\beta
\]

成立，它只能来自所有 occupancy layers 的 genuine convolution compatibility，而不是单层 support certificate。

尚未发现违反 Poisson-aggregated inequality 的合法 Abelian quotient。

下一 Abelian 子问题：刻画哪些 decreasing sequences

\[
\Delta_1\ge\Delta_2\ge\cdots\ge0
\]

真正可由 finite Abelian random walk 实现，并证明一个 Mrs-Gerber/Kneser 型 entropy-growth inequality；或构造合法 profile 违反 (C_*)。

---

## 10. (u/n\to\infty) 的严格 accounting 与 endpoint barrier

文件：

[NATURAL_UNIVERSE_ALL_PIVOT_CLOSE_AUDIT_2026_08_13.md](./NATURAL_UNIVERSE_ALL_PIVOT_CLOSE_AUDIT_2026_08_13.md)

已证明：

- source falling-factorial correction 总计
  
  \[
  O(n^2/u)=o(n)
  \]
  
  只需 (u/n\to\infty)；
- suffix dependence
  
  \[
  \Delta_{V,m,q}
  \le(\log e)\frac{mq}{V-m-q+1}
  \]
  
  可由 slow diagonal 做到 (o(n))；
- 旧 (u\gg n^2) 唯一真实来源是 hard-union 逐元素 witness union bound；
- 单 parent exact accounting：
  
  \[
  I(X;F)=A+D,\qquad T\le D+\Delta;
  \]
- 任何只用 endpoint quantities ((A,D,T)) 与 chain rule 的方法，sharp closure 至多
  
  \[
  H\ge\frac{A+C}{2}-o(n);
  \]
- ordinary arbitrary-history belief-state counterexample 可实现
  
  \[
  T=D=\Theta(n),
  \]
  
  排除 universal (T\le\kappa D), (kappa<1)；
- observable parity 反例使
  
  \[
  \sum_i I(X_i;P|X_{-i})=b,
  \qquad I(X;P)=1.
  \]

结论：endpoint arithmetic/chain rule 不可能恢复 sharp all-pivot constant；必须直接处理 simultaneous replacement-response width。

---

## 11. 已知 arbitrary-history constructions 与 restricted theorems

### 11.1 Binary threshold quotient

ordinary、fixed-state、任意长 history、key-only deletion、zero overflow：

\[
H\le2.349083440193\ldots n+o(n)
\]

at half error。

构造：outer blocks + binary inner symbols；每 block 保存 exact total load (c) 与 one-count modulo (q)。当 (c<q) 时 exact；高 load 时两个 symbols 均接受；delete 可逆地恢复 low-load exactness。

restricted converse：在 commuting canonical binary group-summary class 中，(q=3) 最优。

文件：

- [ALGEBRAIC_THRESHOLD_QUOTIENT_UPPER_BOUND_2026_08_13.md](./ALGEBRAIC_THRESHOLD_QUOTIENT_UPPER_BOUND_2026_08_13.md)
- [BINARY_ABELIAN_THRESHOLD_QUOTIENT_CONVERSE_2026_08_13.md](./BINARY_ABELIAN_THRESHOLD_QUOTIENT_CONVERSE_2026_08_13.md)

### 11.2 Cross-block mod-6

\[
H\le2.346149054803\ldots n+o(n).
\]

略优于 binary threshold，但仍高于 (R_{\rm fp}(1/2)=2.20061148\ldots)。

文件：

[CROSS_BLOCK_MOD6_CONSTRUCTION_2026_08_13.md](./CROSS_BLOCK_MOD6_CONSTRUCTION_2026_08_13.md)

这些是合法 ordinary arbitrary-history upper bounds，但不是最优结论。

---

## 12. 非数值 finite-level exact theorem

文件：

[EXACT_THREE_PIVOT_PRIMAL_DUAL_THEOREM_2026_08_13.md](./EXACT_THREE_PIVOT_PRIMAL_DUAL_THEOREM_2026_08_13.md)

three-pivot relaxation 常数 (C_3) 有唯一最优点 ((p_*,q_*))，由

\[
B(q_*)=\Phi(p_*,q_*),
\]

\[
A(p_*)+A(q_*)=B(p_*)+B(q_*)
\]

唯一确定；三个 branches 等势，存在唯一严格正 KKT 权重，严格凸性给唯一全局最优。

这是完整解析、非 computer-assisted 的 matching primal-dual theorem。但

\[
C_3<3/2,
\]

所以只闭合 finite relaxation，不是社区主结果。(C_4>3/2) 仍只有 computer-assisted certificate，不应作为主方向。

---

## 13. 已严格排除或降级的路线

以下方法不能单独 close ordinary constant-error problem：

1. endpoint mutual information / posterior deficit；
2. single-path directed information；
3. 同误差 block direct sum；
4. coordinatewise certificate entropy直接求和；
5. pure-deletion saturation；
6. fixed-depth replacement gadgets；
7. fixed-degree 或低于 half-layer 的 Johnson spectrum；
8. hard-union witness union bound；
9. canonicalizing arbitrary history-dependent states；
10. support-only multiple-choice snapshot entropy；
11. “stateless route 必须保存 exact counts”；
12. 逐 occupancy layer 的 (C_*)-linear certificate inequality；
13. “存在一个 rejecting empty history就强迫 exact unary count”。

关键反例：

- **coordinate erasure**：随机带选一部分 coordinates exact 维护，其余永久 YES；说明同误差 direct sum 为假，必须先 convexify reliability allocation；
- **global ALL-YES coin/mask**：每 tape 可牺牲不同任务；
- **pure-deletion static cover**：删除-only 轨迹最多给静态率；
- **XOR syndrome**：transition compatible、状态 entropy 线性，但 accepted union 是整个 universe；
- **linear-degree syndrome fibers**：低阶 sections 看不见 transition selectivity；
- **2-state unary ghost machine**：初始 empty state NO，第一次 insert 后进入永久 YES absorbing；一个 reliable empty history只需两状态；
- **snapshot RDF merger ({0,1}\to1)**：满足 one-sided envelope，却不满足 Insert successor closure。

---

## 14. 当前最小 community-close conjecture

令 (Pi_n) 是一个与 tape 独立、长度至多 (f(n)) 的 symmetric replacement-tree history/query distribution。对 deterministic right congruence (C)：

\[
\operatorname{rej}_{\Pi_n}(C)
=\Pr_{(h,x)\sim\Pi_n}[x\notin A_C([h])].
\]

### Poisson replacement width conjecture

对每个固定 (0<\varepsilon<1)、每个 (omega(n)\le f(n)=2^{o(n)}) 和每个 (delta>0)，存在显式 (Pi_n)，使

\[
K\le2^{n(R_{\rm fp}(\varepsilon)-\delta)}
\Longrightarrow
\operatorname{rej}_{\Pi_n}(C)<1-\varepsilon-o(1)
\]

对每个 deterministic index-(K) labeled right congruence 成立。

经 minimax，这与 matching lower bound

\[
H^*_{f(n)}(n,\varepsilon)
\ge nR_{\rm fp}(\varepsilon)-o(n)
\]

等价。结合 Theorem A 才真正 close 该 horizon 下的 ordinary problem。

正确 witness 必须联合收费：

\[
\text{replacement tree branch pattern}
+
\text{transported fiber accepted support}.
\]

不能退化为：

- endpoint entropy；
- single parent chain rule；
- low-degree moments；
- 同参数 block direct sum；
- seed-dependent heavy-class histories。

---

## 15. 下一轮应优先研究的两个精确对象

### 方向 A：successor-closed causal Poisson RDF

从 Theorem B 出发，把 reproduction cells 限制为：

- one-sided (A\ge C)；
- Insert/Delete labeled successor-compatible；
- 在 stationary replacement source 中，同一 recurrent component 持续出现 return-to-zero tests；
- 允许 history-dependent ghosts 与 global reliability allocation。

目标：证明该 causal RDF 等于 (R_{\rm fp})，或构造一个合法 successor-closed cell 严格低于它。

### 方向 B：Abelian random-walk entropy profiles

对 genuine finite Abelian random walk 的 increments

\[
\Delta_c=H(Z_c)-H(Z_{c-1}),
\]

已知

\[
\Delta_1\ge\Delta_2\ge\cdots\ge0,
\qquad
\bar R_c\le1-2^{-\Delta_c}.
\]

需证明或否决 Poisson-aggregated inequality

\[
H_2(\operatorname{Pois}(\lambda))
+\sum_cp_cH(Z_c)
\stackrel{?}{\ge}
C_*\lambda\left[p_0+\sum_{c\ge1}p_c\bar R_c\right].
\]

单靠“(Delta_c) 非增”不足；必须使用 genuine convolution/sumset-growth constraints。可能需要 Mrs-Gerber、Kneser、entropy power 或 additive combinatorics 型不等式。

若该 inequality 成立，就关闭全部 finite-Abelian additive quotient 路线；若失败，反例可能直接给出优于 (R_{\rm fp}) 的 construction blueprint。

---

## 16. Subagent 状态

上一轮使用的 agents：

- `dchoice_construction`：完成 two-choice scope correction、canonical count-only dichotomy、Abelian entropy-increment theorem；刚被安排继续攻击 Poisson-aggregated Abelian inequality，但续跑因 turn abort 被中断，没有新增结果。
- `width_theorem_attack`：完成 source-weighted branch-width theorem 与 linear-degree syndrome barrier；刚被安排继续攻击 successor-closed causal Poisson RDF，但续跑因 turn abort 被中断，没有新增结果。
- `horizon_upper_audit`：完成 subexponential-horizon upper bound 的 hostile audit，已结束。

新对话如继续使用 agents，推荐：

1. 一个 agent 专攻 Abelian Poisson inequality；
2. 一个 agent 专攻 successor-closed causal RDF；
3. 一个 agent 独立寻找严格低于 (R_{\rm fp}) 的合法 construction/counterexample；
4. 主 agent 做模型量词与 ordinary API hostile audit。

---

## 17. 关键文件索引

### 总结/裁决

- [COMMUNITY_CLOSE_RESEARCH_VERDICT_2026_08_14.md](./COMMUNITY_CLOSE_RESEARCH_VERDICT_2026_08_14.md)
- [GENERAL_ORDINARY_DYNAMIC_AMQ_ROUTE_VERDICT_2026_08_13.md](./GENERAL_ORDINARY_DYNAMIC_AMQ_ROUTE_VERDICT_2026_08_13.md)
- [RESEARCH_TASTE_AND_OPEN_FRONTIER_2026_08_13.md](./RESEARCH_TASTE_AND_OPEN_FRONTIER_2026_08_13.md)

### 上界

- [SUBEXPONENTIAL_HORIZON_FINGERPRINT_UPPER_BOUND_AUDIT_2026_08_14.md](./SUBEXPONENTIAL_HORIZON_FINGERPRINT_UPPER_BOUND_AUDIT_2026_08_14.md)
- [MASKED_ENTROPY_ARRAY_LIFTING_2026_08_13.md](./MASKED_ENTROPY_ARRAY_LIFTING_2026_08_13.md)
- [VERIFIED_MAIN_THEOREM.md](./VERIFIED_MAIN_THEOREM.md)
- [UPPER_BOUND_HOSTILE_AUDIT.md](./UPPER_BOUND_HOSTILE_AUDIT.md)

### General formulation / lower target

- [RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md](./RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md)
- [LONG_RANGE_ONLINE_STATE_MERGING_AUDIT_2026_08_13.md](./LONG_RANGE_ONLINE_STATE_MERGING_AUDIT_2026_08_13.md)
- [SUBEXP_HORIZON_WIDTH_TARGET_AND_LINEAR_SYNDROME_BARRIER_2026_08_14.md](./SUBEXP_HORIZON_WIDTH_TARGET_AND_LINEAR_SYNDROME_BARRIER_2026_08_14.md)
- [NATURAL_UNIVERSE_ALL_PIVOT_CLOSE_AUDIT_2026_08_13.md](./NATURAL_UNIVERSE_ALL_PIVOT_CLOSE_AUDIT_2026_08_13.md)

### Two-choice / Abelian quotient

- [DCHOICE_INFORMATION_CONSERVATION_2026_08_14.md](./DCHOICE_INFORMATION_CONSERVATION_2026_08_14.md)
- [DCHOICE_ENTROPY_AUDIT.md](./DCHOICE_ENTROPY_AUDIT.md)
- [DELETION_ROUTING_WITH_EXCHANGEABLE_FINGERPRINTS_AUDIT_2026_08_13.md](./DELETION_ROUTING_WITH_EXCHANGEABLE_FINGERPRINTS_AUDIT_2026_08_13.md)
- [SUPPORT_ONLY_GHOST_RECYCLING_OBSTRUCTION_2026_08_13.md](./SUPPORT_ONLY_GHOST_RECYCLING_OBSTRUCTION_2026_08_13.md)

### Arbitrary-history constructions

- [ALGEBRAIC_THRESHOLD_QUOTIENT_UPPER_BOUND_2026_08_13.md](./ALGEBRAIC_THRESHOLD_QUOTIENT_UPPER_BOUND_2026_08_13.md)
- [CROSS_BLOCK_MOD6_CONSTRUCTION_2026_08_13.md](./CROSS_BLOCK_MOD6_CONSTRUCTION_2026_08_13.md)
- [BINARY_ABELIAN_THRESHOLD_QUOTIENT_CONVERSE_2026_08_13.md](./BINARY_ABELIAN_THRESHOLD_QUOTIENT_CONVERSE_2026_08_13.md)

### Finite analytic theorem

- [EXACT_THREE_PIVOT_PRIMAL_DUAL_THEOREM_2026_08_13.md](./EXACT_THREE_PIVOT_PRIMAL_DUAL_THEOREM_2026_08_13.md)

### Barriers

- [RANDOMIZED_RIGHT_CONGRUENCE_DIRECT_SUM_BARRIER_2026_08_13.md](./RANDOMIZED_RIGHT_CONGRUENCE_DIRECT_SUM_BARRIER_2026_08_13.md)
- [DEPTH2_RIGHT_CONGRUENCE_SPECTRAL_COUNTEREXAMPLE_2026_08_13.md](./DEPTH2_RIGHT_CONGRUENCE_SPECTRAL_COUNTEREXAMPLE_2026_08_13.md)
- [FINITE_DEPTH_L0_SUPPORT_BARRIER_2026_08_13.md](./FINITE_DEPTH_L0_SUPPORT_BARRIER_2026_08_13.md)
- [ORDINARY_BELIEF_STATE_COMPLEMENTARITY_NOGO_2026_08_13.md](./ORDINARY_BELIEF_STATE_COMPLEMENTARITY_NOGO_2026_08_13.md)

---

## 18. 给新对话模型的直接指令

1. 首先完整阅读本 handoff 与以下三个文件：
   - `SUBEXPONENTIAL_HORIZON_FINGERPRINT_UPPER_BOUND_AUDIT_2026_08_14.md`；
   - `SUBEXP_HORIZON_WIDTH_TARGET_AND_LINEAR_SYNDROME_BARRIER_2026_08_14.md`；
   - `DCHOICE_INFORMATION_CONSERVATION_2026_08_14.md`。
2. 不要重新研究已被 barrier 否决的 endpoint chain rule、低阶 spectrum、finite gadget 或 support-only two-choice 数值。
3. 不要声称 (R_{\rm fp}) 已经是 ordinary optimum；目前只有 matching upper candidate，没有 arbitrary-filter matching lower。
4. 优先推进：
   - successor-closed causal Poisson RDF；
   - Abelian Poisson entropy-growth inequality；
   - 或合法 counterexample construction。
5. 每个新命题都必须接受以下 hostile tests：
   - ALL-YES mixture；
   - coordinate erasure；
   - pure-deletion static cover；
   - XOR syndrome；
   - linear-degree Johnson design；
   - history-dependent ghosts；
   - global quotient；
   - key-only deletion；
   - fixed worst-case state count；
   - seed-independent history quantifier。

---

## 19. 一句话当前结论

已经严格闭合了 (R_{\rm fp}) 在 oblivious (2^{o(n)})-horizon 下的 fixed-space 上界，并得到 source-weighted branch-width 与任意 Abelian quotient 的新解析下界接口；完整 ordinary lower bound 尚未闭合，剩余核心已被压缩为“带 labeled successor closure 的 stationary causal one-sided Poisson rate-distortion”，或等价的 Poisson replacement right-congruence width theorem。
