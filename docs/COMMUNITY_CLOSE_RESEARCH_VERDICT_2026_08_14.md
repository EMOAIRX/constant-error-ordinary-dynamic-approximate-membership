# Constant-error dynamic approximate membership：从应用到当前最小闭合问题

> 日期：2026-08-14。本文只陈述已经完成严格证明的结果，并把尚未证明的主命题明确标为 conjecture。所有对数以 2 为底。

## 1. 为什么这个问题值得做

缓存去重、LSM-tree 层级索引、网络黑名单、数据库 semi-join、分布式存储中的 object existence test，都需要维护一个不断插入和删除的集合，同时允许少量 false positives。静态 Bloom filter 的核心代价约为

\[
n\log(1/\varepsilon),
\]

但 deletion 使问题发生本质变化：结构必须知道某个 fingerprint、bucket 或局部证书是否仍由其他真实 key 支撑。若清除过早，会产生 false negative；若永不清除，ghost 会在长期 churn 中积累。KLZ 在 \(\varepsilon=o(1)\) 时证明 fingerprint filters 最优，而 fixed constant error 仍是公开问题。

本文研究的 ordinary 模型是：固定 \(H\)-bit persistent memory、免费只读 public random tape、key-only `Insert/Delete/Query`、逐 tape zero false negatives，以及对每条预先固定且与随机带独立的合法 history、每个固定 current nonmember 的 pointwise FPR。

我们把首个自然且可严格控制的 horizon 取为

\[
\omega(n)\le f(n),\qquad \log f(n)=o(n),
\]

并假设 \(u/n\to\infty\)。这个量词不等于 output-adaptive 或 seed-adaptive robustness。

## 2. 候选最优率

令

\[
g(\lambda)=1-e^{-\lambda},\qquad
r(\lambda)=\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda}.
\]

定义

\[
R_{\rm fp}(\varepsilon)
=\operatorname{lce}_{\lambda\in(0,\infty]}
\{(g(\lambda),r(\lambda))\}(\varepsilon),
\]

其中允许与 permanent-YES endpoint \((1,0)\) 取下凸包。它同时优化 heterogeneous fingerprint loads 与 frozen reliability allocation。在 \(\varepsilon=1/2\) 时，

\[
R_{\rm fp}(1/2)=2.20061148296\ldots.
\]

## 3. 已闭合的上界

### Theorem A（oblivious subexponential-horizon upper bound）

对每个固定 \(0<\varepsilon<1\) 和每个满足 \(\log f(n)=o(n)\) 的 horizon，存在 ordinary one-sided dynamic filter，使对每条预先固定、与 public tape 独立、长度至多 \(f(n)\) 的合法 history，

\[
H\le nR_{\rm fp}(\varepsilon)+o(n),
\]

并且逐 tape zero false negatives、pointwise FPR 至多 \(\varepsilon\)。

证明使用一个全局 occupancy information-spectrum slot。normal states 精确编码 heterogeneous fingerprint count vector 的统一 typical family；任何离开 typical family 的更新进入 absorbing ALL-YES state。Poisson self-information 的解析 Bernstein 尾界给

\[
\Pr[\text{某个固定 endpoint atypical}]
\le \operatorname{poly}(n)e^{-\Omega(t_n^2/n)},
\]

取

\[
a_n=\log(f(n)+2)+\log(n+2),\qquad
t_n=n(a_n/n)^{1/4},
\]

即可使整条 history 的 sticky probability 为 \(o(1)\)，而 \(t_n=o(n)\)。该概率直接计入 FPR，不被当作 correctness 之外的 failure event。

完整证明见
[SUBEXPONENTIAL_HORIZON_FINGERPRINT_UPPER_BOUND_AUDIT_2026_08_14.md](./SUBEXPONENTIAL_HORIZON_FINGERPRINT_UPPER_BOUND_AUDIT_2026_08_14.md)。

这个 theorem 不覆盖 output-adaptive、seed-adaptive 或无限 history。扫描候选直到首次 YES 再重查同一 nonmember，已经给出 output-adaptive conditional FPR 为 1 的严格反例。

## 4. 一般模型的精确优化对象

固定 public tape 后，任意 ordinary filter 都诱导 history language 上的有限指数 labeled right congruence。一个 state class 的最小安全 accepted set，是该 class 中所有 endpoint sets 的 union。于是随机 filter 精确等价于 index 至多 \(2^H\) 的 deterministic right congruences 的 public-coin mixture。

若 \(z_C(h,x)\) 表示 congruence \(C\) 在 test \((h,x)\) 上拒绝 nonmember，则有限 LP minimax 给

\[
V_n(K)
=\min_{\pi}\max_{C:\operatorname{index}(C)\le K}
\mathbb E_{(h,x)\sim\pi}z_C(h,x).
\]

因此 matching lower bound 的充要形式，是构造一个与 tape 独立的 history-query distribution \(\pi_n\)，使每个低指数 right congruence 的平均 rejection 都不足 \(1-\varepsilon\)。这不是 Shannon mutual information 或普通 graph entropy 可以替代的目标。

完整 characterization 见
[RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md](./RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md)。

## 5. 新的严格下界接口

### Theorem B（source-weighted upper-envelope branch width）

在 grouped-cell label-level count lattice 中，令 \(C\) 是任意 count-vector source，\(J\) 是随机 coordinate。从 canonical state 删除 coordinate \(J\) 的全部当前 copies 后查询，令平均 rejection reliability 为 \(\alpha\)。定义 one-sided RDF

\[
\mathsf R^+_{C,J}(\alpha)
=\inf I(C;A),
\]

其中

\[
A\ge C\quad\text{coordinatewise},\qquad
\Pr[A_J=C_J]\ge\alpha.
\]

则任何 \(K\)-state deterministic transducer 满足

\[
\log K\ge \mathsf R^+_{C,J}(\alpha),
\]

而 public-coin pointwise FPR 至多 \(\varepsilon\) 推出

\[
H\ge \mathsf R^+_{C,J}(1-\varepsilon).
\]

证明对每个 state fiber 取 coordinatewise upper envelope。若删除 \(c_j\) 次后能够拒绝 \(j\)，同 fiber 就不可能含有更大的第 \(j\) 个 count，否则共同 continuation 会让同一 successor 同时需要 YES 与 NO。

这个 theorem 在一个 simultaneous state 上收费，并自动允许 coordinate erasure；它严格强于此前的 endpoint mutual-information accounting。

但它仍不是主问题 closure。reproduction 把 counts \(\{0,1\}\) 合并为 \(A=1\)、其余 exact，满足 snapshot RDF，却不可能是 insertion-successor-compatible right congruence。真正需要的是

\[
\text{one-sided Poisson RDF}
\cap
\text{labeled successor-closed cells}.
\]

证明与反例见
[SUBEXP_HORIZON_WIDTH_TARGET_AND_LINEAR_SYNDROME_BARRIER_2026_08_14.md](./SUBEXP_HORIZON_WIDTH_TARGET_AND_LINEAR_SYNDROME_BARRIER_2026_08_14.md)。

## 6. 对 multi-label additive quotients 的解析推进

考虑有限 Abelian group \(\Gamma\)，label \(a\) 对应向量 \(v_a\)，block 内 \(c\) 个 iid labels 的 syndrome 为

\[
Z_c=\sum_{i=1}^c v_{A_i}.
\]

令 \(R_c(z)\) 是 state \(z\) 能够安全拒绝的 fresh-label prior mass，\(\bar R_c=\mathbb E R_c(Z_c)\)。

### Theorem C（Abelian entropy increment pays for zero certificates）

对每个 \(c\ge1\)，

\[
H(Z_c)-H(Z_{c-1})
\ge
\mathbb E\log\frac1{1-R_c(Z_c)}
\ge
\log\frac1{1-\bar R_c},
\]

并且

\[
H(Z_c)\ge c\log\frac1{1-\bar R_c}.
\]

第一步来自 posterior support 相对 prior 的 KL divergence；第二步来自 Jensen；最后一步来自 independent labels 的 information tensorization。若

\[
\Delta_c=H(Z_c)-H(Z_{c-1}),
\]

则 data processing 还给出

\[
\Delta_1\ge\Delta_2\ge\cdots\ge0,
\qquad
\bar R_c\le1-2^{-\Delta_c}.
\]

这一定理覆盖任意 group size、任意 label distribution 和任意 Abelian vectors，不依赖 binary、\(q=3\) 或数值枚举。

完整证明见
[DCHOICE_INFORMATION_CONSERVATION_2026_08_14.md](./DCHOICE_INFORMATION_CONSERVATION_2026_08_14.md)。

它同时严格否决了一个过强但诱人的路线：逐 load 的

\[
H(Z_c)\ge C_*c\bar R_c
\]

为假；\(c=1\)、两个均匀 labels 已给出反例。若 Abelian quotient 最终满足 sharp fingerprint converse，常数只能来自所有 Poisson occupancy layers 之间的 convolution compatibility，而不是单层 support entropy。

## 7. 已经关闭的证明路线

以下方法不能单独得到 matching ordinary lower bound：

1. endpoint mutual information 或 posterior deficit；
2. 单路径 directed information；
3. 同误差参数的 block direct sum；
4. pure-deletion saturation；
5. fixed-depth replacement gadgets；
6. 低阶 Johnson spectrum。

最后一项已有线性加强：random XOR syndrome fibers 对所有严格低于 half-layer 的 \(\Theta(n)\)-degree inclusion statistics都可与 uniform slice 渐近一致。因此任何不把 accepted support/FPR 与 transition width 放进同一个 inequality 的 section/spectral theorem 都会失败。

## 8. 当前最小主命题

### Conjecture（Poisson replacement width）

对每个固定 \(0<\varepsilon<1\) 和 \(\omega(n)\le f(n)=2^{o(n)}\)，存在显式、symmetric、与 tape 独立的 replacement-history/query distribution \(\Pi_n\)，使

\[
K\le2^{n(R_{\rm fp}(\varepsilon)-\delta)}
\Longrightarrow
\operatorname{rej}_{\Pi_n}(C)<1-\varepsilon-o(1)
\]

对每个 deterministic index-\(K\) labeled right congruence 成立。

经 LP minimax，这与

\[
H^*_{f(n)}(n,\varepsilon)
\ge nR_{\rm fp}(\varepsilon)-o(n)
\]

等价。结合 Theorem A 才会真正 close constant-error ordinary problem。

## 9. 研究裁决

目前已经得到的不是完整 ordinary-model closure，而是四项可独立验证的实质进展：

1. \(R_{\rm fp}\) 在任意 oblivious subexponential horizon 下的 fixed-worst-case-space 完整解析上界；
2. ordinary filters 的 exact right-congruence minimax formulation；
3. 一个允许 reliability allocation 的 source-weighted simultaneous branch-width theorem；
4. 任意 Abelian additive quotient 的 entropy-increment/zero-certificate theorem，以及线性阶谱路线的严格 barrier。

最有希望的下一步不是继续优化有限常数或小群，而是二选一：

- 证明 Poisson 加权的 successor-closed causal RDF 恰为 \(R_{\rm fp}\)；
- 构造一个合法 successor-closed cell 或 Abelian random-walk entropy profile，严格违反该 inequality，从而导出低于 \(R_{\rm fp}\) 的 ordinary construction。

这两种结果都会改变社区对 constant-error dynamic filters 的理解。当前材料足以形成一篇“sharp upper bound + exact variational formulation + broad barriers”的理论论文骨架，但在没有解决上述二选一之前，不能声称已经关闭 FOCS 2025 留下的完整 lower-bound open problem。
