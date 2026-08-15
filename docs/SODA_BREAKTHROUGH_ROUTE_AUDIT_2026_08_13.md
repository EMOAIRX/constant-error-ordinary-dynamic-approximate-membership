# 常数误差动态 Membership：SODA 突破路线最终审计

> 日期：2026-08-13。状态：路线收敛报告。当前没有 SODA 级新定理；本文严格区分已证工具、已否决猜想与唯一主攻缺口。

## 0. 结论先行

广泛探索后，只剩一个值得集中资源的普通模型问题：

> 在 KLZ/FOCS 2025 的一般 history-dependent dynamic filter 模型中，证明一个 batch joint branch--support inequality；它必须同时给 hit-pattern 的相关性和条件 location/support 代价收费，并允许 frozen masks、共享 rejection certificates 和任意全局物理状态。

若该 inequality 给出显式线性 gap，它可以替换 KLZ Lemma 4.5，并通过现有 obfuscating tree 与 reconstructible-set 技术提升到一般模型。若它失败，一个可张量化反例将揭示超越 fingerprints 的普通动态 filter 机制，也具有 SODA 价值。

bounded churn、逐 cell rate--distortion、exact multiplicities、普通 direct sum 和单独联合编码 hit vector 均不足以承担主结果。

## 1. 唯一主模型

固定完整随机带 `r` 后，filter 是任意确定性 finite-state transducer：

- 物理状态空间 `M_r`，大小至多 `2^H`；
- query accepted set `A_r(m)`；
- 对每个 labeled Insert/Delete 的任意全局转移；
- 状态可含 routing、ghosts、relocation、epoch、历史摘要和共享证书。

对每条预先固定且与随机带独立的合法历史、每个时刻和固定当前非成员 `z`，

\[
\Pr_r[z\in A_r(M_r(h))]\le\varepsilon,
\]

而成员在每条随机带上均无 false negative。

主定理不得假设：

- history independence 或 canonical state；
- actual accepted-set monotonicity；
- exact multiplicity recovery；
- cell locality 或可加 memory decomposition；
- singleton witnesses、union preservation；
- 删除时免费的 insertion-time placement/orientation。

## 2. 最新文献边界

### 2.1 KLZ25 真正留下的问题

固定常数 `epsilon`，确定一般动态 filter 的一阶最优率

\[
\operatorname{OPT}_{\rm dyn}(\varepsilon)
=\liminf_n\frac{H^*(n,\varepsilon)}n
\]

仍是开放问题。不能预设答案一定是 uniform Poisson fingerprint rate。

### 2.2 2026 entropy arrays 已经解决什么

Blelloch--Hu--Kuszmaul--Li--Zhou, FOCS 2026, Theorem 8.2 已给 uniform single-hash fingerprint multiset：

\[
H\le
n\frac{H_2(\operatorname{Pois}(\delta))}{\delta}+o(n),
\qquad
\delta=-\ln(1-\varepsilon),
\]

并支持 `O(1)` 时间操作，空间和时间为 whp 保证，`U=poly(n)`。它不证明 arbitrary-filter converse，也不是 KLZ 固定最坏 `H`-bit 的同步无限执行保证。

所以“动态编码 uniform fingerprint counters”已经不是突破；一般 lower bound、fixed-memory 模型差异和非 uniform/shared-certificate 结构仍开放。

## 3. KLZ 原证明在常数误差下的精确能力

保留 Proposition 4.3 至 Lemma 5.3 中全部常数，只得到

\[
H\ge n\left[
\log_2\frac1\varepsilon
+(1-\varepsilon)\log_2e
-2h_2(\varepsilon)
\right]-o(n).
\tag{1}
\]

在 `epsilon=1/2`，括号为 `-0.2786524796...`，所以动态 protocol 无非平凡结论；一 bit/key 来自静态 Carter lower bound。

相对小误差目标，线性损失为

\[
2h_2(\varepsilon)+\varepsilon\log_2 e.
\]

来源是：

1. 逐 key 发送 hit bit；
2. hit/miss branch 与 location code 混合；
3. factorial saving 只发生在 miss branch。

obfuscation 与 reconstructible-set reduction 在固定误差、大宇宙下只损失 `o(n)`。因此必须替换单字母发送 lemma，而不是重做 KLZ Sections 4--5。

## 4. 已证的一般工具：fiber transport

固定随机带 `r`。对物理状态 `m`，令

\[
\mathcal F_r(m)
=\{S:\text{某条合法历史以逻辑集合 }S\text{ 到达 }m\}.
\]

由 one-sidedness，

\[
\bigcup_{S\in\mathcal F_r(m)}S\subseteq A_r(m).
\tag{2}
\]

若同一个 labeled update word `w` 对子族 `G subset F_r(m)` 中每个集合均合法，则固定 tape 后所有隐藏世界执行 `w` 到达同一后继状态 `m_w`，且

\[
\bigcup_{S\in\mathcal G}\Phi_w(S)
\subseteq A_r(m_w).
\tag{3}
\]

这是 sound 的 common-legal-continuation fiber transport lemma。它允许完整 history dependence、全局相关状态和 certificate sharing；但单独不推出线性 bits。

## 5. 唯一主攻 lemma：joint branch--support inequality

考虑 KLZ 一个 hidden batch

\[
X=(X_1,\ldots,X_q)
\]

以及两个 nested reconstructible sets。令 `Z` 是完整 hit vector。给定 `Z=z` 后，令 `N_z` 为与同一个完整物理 transcript、one-sidedness、无放回 distinctness 和 fiber transport 相容的整个 ordered batch 数量。

正确的通信量是

\[
\mathsf{BS}_q
=H(Z)+\mathbb E_Z\log N_Z.
\tag{4}
\]

需要证明存在显式 `J(epsilon)>0`，使任意普通 filter 的 KLZ batch 都满足

\[
\boxed{
H(Z)+\mathbb E\log N_Z
\le q\log|U_k|-qJ(\varepsilon)+o(q).
}
\tag{5}
\]

并使所得一般动态下界严格改善现有 arbitrary-filter bound。最高目标才是证明相应 multi-letter variational value等于某个 fingerprint rate。

式 (5) 不能只使用 hit marginals。独立 Bernoulli hits 使 `H(Z)` 可达 `q h_2(epsilon)`；全局 frozen mask 可使 `H(Z)` 很小，却把 hit-side support 放大。真正要证明的是二者不可同时过小。

## 6. 等价的 transition-covering 语言

固定 tape 的状态分区不是任意静态 coloring，而是对所有共同合法 update labels 闭合的 right congruence。式 (5) 可等价表述为：

> 满足 pointwise FPR 的 public-coin transition-constrained fiber covering，其随机 deletion language 的条件熵不能超过某个显式界。

这一定义自动覆盖：

- frozen masks；
- global ALL-YES coins；
- 少量共享 rejection certificates；
- fingerprints/paintboxes；
- arbitrary routing 与 history summaries。

普通 graph entropy 不够；必须保留 transition consistency 和 multi-letter deletion trie。

## 7. 已被否决或降级的路线

### 7.1 exact-count 两选择

`epsilon=1/2` 时乐观 exact-count rate 为 `2.8304000127` bits/key，高于现有 fingerprint benchmark。查询两个候选位置的 FPR 代价压过负载异质性收益。

### 7.2 support-only/sticky ghosts

静态 support entropy 虽有数值优势，但 `Insert(x), Delete(x), Query(x)` 使永久 ghost 对固定已删除 key 以概率一返回 YES。

### 7.3 逐 cell deletion rate--distortion

它暗含 memory、update 和 query 可局部分解，不适用于 arbitrary automata。

### 7.4 普通 static + incremental direct sum

错误。shared rejection certificate 可同时服务 survivors 和 newcomers。见 [BOUNDED_CHURN_DIRECT_SUM_CONJECTURE.md](./BOUNDED_CHURN_DIRECT_SUM_CONJECTURE.md)。

### 7.5 Dummy + Lovett--Porat

dummy simulation 只转移已经针对 fresh, pairwise-distinct insertions 证明的 lower bound。Lovett--Porat 原 hard distribution 允许重复 labels，其 path closure 不能直接搬到 fresh API。此前 `m/n to infinity` 下的 `1.1 alpha n` 和 `alpha>10/11` 结论已经撤回。

### 7.6 只联合编码 hit vector

不足。marginal FPR 允许 hits 独立；共享证书又允许 hits 完全相关。必须与条件 support 联合优化。

### 7.7 bounded churn 作为主论文

black-box overlay theorem

\[
F_0\le F_T
\le F_0+O\!\left(T\log\frac{em}{T}\right)
\]

是正确的，但只够 note/warmup。当前没有匹配 linear curve。

在 `m=2n, epsilon=1/2`，静态率是 `0.6225562489...n`，而 frozen balanced mask 用 `n+O(1)` bits 支持任意长 churn。因此任何随着 `T` 无界线性增长的 dense 公式都错误。

## 8. 下一阶段的严格执行顺序

1. 在 HI + monotone warmup 中使用 acceptance layers 与 first-acceptance word，证明固定 chain 的 rook-polynomial identity，并精确定义 falling-factorial batch functional；不先碰 obfuscating tree。
2. 将 optimizer 与四类 hostile laws 比较：independent hits、all-or-none coin、fixed-size frozen mask、overlapping shared witnesses。
3. 证明 global-certificate extremality，或找到严格更优且可张量化的 law。
4. 只有 finite-block functional 严格改善 single-letter KLZ 后，才把 inequality 移植到 Section 4 obfuscation。
5. 检查它只使用 reconstructible inclusion、public partition exchangeability 和 fiber transport；随后用 Section 5 去掉 actual monotonicity。
6. 最终再比较所得 rate 与 uniform/nonuniform fingerprint upper bounds，不能预设 optimizer。

具体 formulation 与已证计数恒等式见 [ACCEPTANCE_LAYER_BATCH_ROUTE.md](./ACCEPTANCE_LAYER_BATCH_ROUTE.md)。Acceptance forest 单独是 no-go；必须与 layer sizes、conditional physical state 和 KLZ 双向 pivot 联合使用。

一条次级路线是严格化 Lovett--Porat Section 3.5 的递归常数。原文只正式证明
`C(1/2)>=1.1`，`1.13` 是未给参数证书的 computer-search remark。即使把递归变成可认证的
变分或动态规划，若极限改进仍停留在约 `1.13` 且没有新的结构定理，这更像已有证明的常数精炼，不能替代 joint branch--support 主线。

## 9. SODA 成功标准

最小主结果必须在完整 KLZ 模型中给出某个常数误差区间的显式线性改进：

\[
H\ge n\bigl(L_{\rm known}(\varepsilon)+\Delta(\varepsilon)\bigr)-o(n),
\qquad \Delta(\varepsilon)>0.
\]

更强结果是求出 transition-constrained multi-letter rate并给 matching construction；或证明它等于正确的 fingerprint benchmark。

同样足够重要的反向结果是：构造合规的普通 dynamic automaton，严格低于所有 fingerprint-multiset rates。

以下不够：

- 只证明 fiber transport；
- 只解 exact-count/fingerprint subclass；
- 只给 finite-state 数值；
- 只重算 KLZ constants；
- 只提出 variational formulation；
- 在 bounded churn/WHI/dense 特例中给 separation，却声称普通模型突破。

## 10. 当前诚实判断

现在还没有完整突破。真正的进展是已经找到一个没有强假设、可被明确证伪、并能直接接入社区主问题的最小核心 lemma。

研究资源应集中在 joint branch--support functional。若不能在 HI/monotone warmup 中先得到严格 gap，就应停止 lower-bound lifting，转而从 optimizer 寻找新构造，而不是继续添加模型假设。

## 参考文件

- [普通动态 Membership 的 SODA 突破前沿](./ORDINARY_DYNAMIC_FILTER_SODA_FRONTIER_2026_08_13.md)
- [KLZ 固定误差常数审计](./KLZ_FIXED_EPSILON_CONSTANT_AUDIT.md)
- [FOCS 2026 entropy-array Theorem 8.2 审计](./ENTROPY_ARRAYS_THEOREM_8_2_AUDIT.md)
- [更正后的 bounded-churn stability](./BOUNDED_CHURN_STABILITY_THEOREM.md)
- [bounded-churn direct-sum 反例](./BOUNDED_CHURN_DIRECT_SUM_CONJECTURE.md)
