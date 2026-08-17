# 研究结果、条件与来源索引

本页把仓库中的可引用结论按模型分开。标签含义：

- **外部文献**：原论文已经证明；本仓库只做核对或常数计算。
- **本仓库定理**：仓库给出了证明和 hostile audit。
- **条件定理**：额外结构假设尚未对全部 ordinary filters 证明。
- **类内最优**：只在 fingerprint、canonical quotient 等受限类内 matching。
- **结构定理**：严格成立，但没有单独产生新的 universal 数值常数。

## 1. 原始 constant-error ordinary 模型

模型：$u/n\to\infty$、$\varepsilon=1/2$、arbitrary history dependence、任意长
合法 Insert/Delete、fixed worst-case persistent memory、free public tape、zero
false negatives、pointwise FPR。

$$
(1+2^{-48})n-o(n)
\le
H^*_{1/2}(n,u)
\le
2.34614905664n+o(n).
$$

这里 $2^{-48}$ 是 theorem package 给出的保守解析 witness，尚未优化。

| 结论 | 来源 | 文件 |
|---|---|---|
| $H\ge(1+2^{-48})n-o(n)$ | **本仓库定理**：simultaneous replacement-cover width；一般 ordinary 模型、只需 $u/n\to\infty$ | [natural-universe theorem](./SIMULTANEOUS_REPLACEMENT_COVER_WIDTH_LOWER_BOUND_2026_08_17.md) |
| $H\ge n-o(n)$ | **外部文献**：Carter static accepted-set baseline；已被上一行动态下界严格改进 | [KLZ fixed-error audit](./KLZ_FIXED_EPSILON_CONSTANT_AUDIT.md) |
| $H\le2.34614905664n+o(n)$ | **本仓库定理**：cross-block mod-$6$ additive quotient | [theorem](./CROSS_BLOCK_MOD6_CONSTRUCTION_2026_08_13.md), [audit](./TWO_SUBBLOCK_MODULUS_INDEPENDENT_AUDIT_2026_08_13.md) |
| $H\le2.349083440193\ldots n+o(n)$ | **本仓库旧定理**：order-$3$ algebraic threshold quotient；已被上一行改进 | [baseline](./VERIFIED_ALGEBRAIC_THRESHOLD_QUOTIENT_2026_08_13.md) |
| finite-parameter optimum 的 randomized right-congruence minimax characterization | **本仓库结构定理**；尚无显式渐近常数 | [right-congruence variational theorem](./RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md) |

新下界的独立量词、常数和反例审计见
[replacement-cover hostile audit](./SIMULTANEOUS_REPLACEMENT_COVER_WIDTH_HOSTILE_AUDIT_2026_08_17.md)。

## 2. 下界：条件改变后

| 条件 | 半误差结论 | 类型 | 文件或来源 |
|---|---:|---|---|
| $u/n\to\infty$，ordinary | $H\ge(1+2^{-48})n-o(n)$ | **本仓库定理**；无附加结构假设 | [simultaneous replacement-cover theorem](./SIMULTANEOUS_REPLACEMENT_COVER_WIDTH_LOWER_BOUND_2026_08_17.md) |
| $u/n^2\to\infty$，$f(n)/n\to\infty$，ordinary | $H\ge C_{\mathrm{AP}}n-o(n)$，$C_{\mathrm{AP}}>1.607987002861718\ldots$ | **本仓库定理**；在所列强宇宙/时域量词内不假设 BSSI、monotonicity 等结构；continuous hierarchy 的严格极限 | [continuous theorem](./CONTINUOUS_ALL_PIVOT_VARIATIONAL_LIMIT_2026_08_17.md), [finite predecessor](./EQUAL_BLOCK_ALL_PIVOT_CONVERSE_2026_08_13.md) |
| $u/n^2\to\infty$，ordinary | $H\ge1.198n-o(n)$ | **本仓库定理**，无额外结构假设 | [multicut theorem](./MULTICUT_PREFIX_UNION_LOWER_BOUND_2026_08_16.md), [audit](./MULTICUT_PREFIX_UNION_HOSTILE_AUDIT_2026_08_16.md) |
| $u/n\to\infty$，BSSI | $H\ge1.434406361243753\ldots n-o(n)$ | **本仓库条件定理** | [theorem](./BOUNDED_SOURCE_SECTION_INFLUENCE_NATURAL_UNIVERSE_LOWER_BOUND_2026_08_15.md), [audit](./BOUNDED_SOURCE_SECTION_INFLUENCE_HOSTILE_AUDIT_2026_08_15.md) |
| $u/n\to\infty$，history-dependent monotone | $H\ge1.1992732344471508\ldots n-o(n)$ | **本仓库对 KLZ 的受限子类推论** | [amplification audit](./AMPLIFICATION_FRONTIER_HOSTILE_AUDIT_2026_08_13.md) |
| Lovett--Porat 旧 dynamic/incremental 模型，$n/u\to0$ | $H\ge1.1n-o(n)$ | **外部文献**；其 hard distribution 允许 repeated labels | [LP comparison audit](./AMPLIFICATION_FRONTIER_HOSTILE_AUDIT_2026_08_13.md#7-%E4%B8%8E-lovett--porat-%E7%9A%84%E7%BB%9F%E4%B8%80%E6%AF%94%E8%BE%83) |
| $u=2n$，一般 dynamic | $H\ge0.6225562489\ldots n-o(n)$ | **外部静态 bound**（ChainedFilter/Carter-type counting），动态下界未改进 | [finite-universe audit](./LITERATURE_FRONTIER_AUDIT.md) |

### $1.198$ 的准确含义

该证明只运行一条 $n$ 次 fresh-distinct insertion history，所以任何 fully dynamic
filter 都必须满足；它同时也是 incremental 下界。当前 canonical-witness transport
需要 $u/n^2\to\infty$，因此不能写成 $u/n\to\infty$ 定理。

### BSSI 的准确含义

BSSI 允许 history dependence、multiple representations、nonmonotone queries、
ghosts 与 holonomy；它额外排除 fresh suffix label 一次摧毁无界 source-section
union mass 的机制。该条件尚未从低空间 ordinary semantics 推出。

## 3. 上界：空间和历史量词

| 条件 | 半误差结论 | 类型 | 文件或来源 |
|---|---:|---|---|
| 任意长 history，fixed worst-case space | $2.34614905664n+o(n)$ | **本仓库定理** | [cross-block quotient](./CROSS_BLOCK_MOD6_CONSTRUCTION_2026_08_13.md), [audit](./TWO_SUBBLOCK_MODULUS_INDEPENDENT_AUDIT_2026_08_13.md) |
| oblivious fixed history，$\log f(n)=o(n)$，fixed preallocation | $2.20061148296052\ldots n+o(n)$ | **本仓库定理** | [subexponential-horizon theorem](./SUBEXPONENTIAL_HORIZON_FINGERPRINT_UPPER_BOUND_AUDIT_2026_08_14.md) |
| polynomial seed-independent history，polylog time | $2.20061148296052\ldots n+o(n)$ | **本仓库定理**；exact IID fingerprint class 内 matching | [verified fingerprint theorem](./VERIFIED_MAIN_THEOREM.md) |
| current-state whp space/time，uniform Poisson fingerprints | $2.28790401364596\ldots n+o(n)$ | **外部文献**：Blelloch--Hu--Kuszmaul--Li--Zhou 2026 | [Theorem 8.2 audit](./ENTROPY_ARRAYS_THEOREM_8_2_AUDIT.md) |
| 同一 whp-resource 语义，heterogeneous thinning | $2.20061148296052\ldots n+o(n)$ | **本仓库对外部 entropy array 的 lifting** | [lifting theorem](./MASKED_ENTROPY_ARRAY_LIFTING_2026_08_13.md) |
| incremental only | $(1/\ln2)n$ | **外部经典 Bloom filter** | 标准 one-hash Bloom calculation |
| uniform exact multiplicity，all compositions | $2.384499842479\ldots n+o(n)$ | 标准 fingerprint benchmark；常数由本仓库核对 | [frozen-mask/count-vector audit](./FROZEN_MASK_DYNAMIC_CHAIN_AUDIT_2026_08_13.md) |
| $u=2n$，任意长 history | $n$ | **本仓库定理**：balanced frozen mask | [construction audit](./TRANSITION_COMPATIBLE_COVERING_CONSTRUCTION_AUDIT_2026_08_13.md) |

### $2.200611\ldots$ 的类内最优性

本仓库求出了 generalized IID fingerprint-multiset class 的 lower convex envelope：

$$
R_{\rm FM}(\varepsilon)
=
\operatorname{lce}_{\lambda\in(0,\infty]}
\left(
1-e^{-\lambda},
\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda}
\right)(\varepsilon).
$$

在 $\varepsilon=1/2$ 时为 $2.20061148296052\ldots$。这是 fingerprint class 内的
matching converse，不是 arbitrary ordinary filter 下界。

## 4. 外部文献已经闭合的 regime

### Small error fixed-capacity dynamic filters

Kuszmaul--Liang--Zhou（FOCS 2025）在

$$
\varepsilon=o(1),
\qquad
u=\omega(n/\varepsilon),
$$

并支持 $\omega(n)$ 次合法 updates 时，KLZ 证明 matching lower bound；结合已有
fingerprint upper bound，文献中的 first-order optimum 为

$$
H^*
=
n\log_2(1/\varepsilon)+n\log_2 e+o(n).
$$

这是 **外部文献已经闭合的 first-order regime**：KLZ 下界适用于 arbitrary
dynamic filters，matching 上界来自 fingerprint constructions；它不覆盖 constant
error。见 [FOCS25 model audit](./FOCS25_MODEL_CONSTANTS_AND_2026_FOLLOWUPS_AUDIT.md)。

### Unknown-size incremental filters

Pagh--Segev--Wieder（FOCS 2013）研究的是不知道最终大小且要求每个 prefix 都紧凑的
incremental filter，得到额外 $\Omega(n\log\log n)$ 项。它不是 fixed-capacity
constant-error ordinary 模型。见 [literature audit](./LITERATURE_FRONTIER_AUDIT.md)。

### Dynamic uniform fingerprint coding

Blelloch--Hu--Kuszmaul--Li--Zhou（2026）在 polynomial universe、word RAM、whp
resource 语义下实现 uniform Poisson fingerprint entropy rate和 $O(1)$ operations。
它解决了 KLZ 提出的 uniform-multiset efficient coding 子问题，但不解决 arbitrary-
filter constant-error lower bound。

## 5. 主定理依赖与一般 structural theorems

以下先列新下界闭合的 replacement-width 接口，再列仍只提供结构会计的通用定理：

- [Simultaneous replacement-cover width](./SIMULTANEOUS_REPLACEMENT_COVER_WIDTH_LOWER_BOUND_2026_08_17.md)：把此前缺失的 extensive replacement-width 接口闭合为原始模型下的显式严格 gap；它已列入 Section 1，不只是结构 lemma。
- [Full-fiber transport-information dichotomy](./FULL_FIBER_TRANSPORT_INFORMATION_DICHOTOMY_2026_08_13.md)：在 $u/n\to\infty$ 下把 union destruction 记为 entropy deficit。
- [Operational avalanche-or-information theorem](./OPERATIONAL_SUPPORT_COMPLETION_AVALANCHE_LOWER_BOUND_2026_08_16.md)：常数概率、常数比例 avalanche 产生显式 dynamic premium。
- [Joint transportable-section rank-volume theorem](./JOINT_REPLACEMENT_RANK_VOLUME_LOWER_BOUND_2026_08_16.md)：jointly 编码 replacement labels 与 survivors，得到非负 rank premium。
- [Exact right-congruence minimax](./RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md)：给出有限参数最优空间的精确 LP/minimax characterization。
- [Normalized-dual conditional novelty](./NORMALIZED_DUAL_CONDITIONAL_NOVELTY_2026_08_17.md)：把 future-response information 合法嵌入 all-pivot dual；finite-depth cylinder theorem 同时给出 sharp local no-go。
- [Continuous all-pivot variational limit](./CONTINUOUS_ALL_PIVOT_VARIATIONAL_LIMIT_2026_08_17.md)：证明 finite hierarchy 严格收敛到 attained constant $C_{\mathrm{AP}}$，且 $C_q<C_{\mathrm{AP}}$ 对每个有限 $q$ 成立。
- [Continuous all-pivot endpoint boundary](./CONTINUOUS_ALL_PIVOT_ENDPOINT_BOUNDARY_2026_08_17.md)：证明 endpoint exponent 必为 $1$，并求出 $v\log v$ boundary layer；$1.7156$ 仍只是 numerical location。
- [Continuous optimality and thick-fiber upper barrier](./CONTINUOUS_OPTIMALITY_AND_THICK_FIBER_UPPER_BARRIER_2026_08_17.md)：证明 finite minimizer 唯一、adjacent-difference Jacobian 是 nonsingular $M$-matrix，并排除 complete thick fibers 加 tight unions 的 matching-upper 路线。

其中 continuous all-pivot theorem 已作为严格的 symbolic coefficient lower bound
列入 Section 2；它仍受 $u/n^2\to\infty$ 限制。其余结构结果不能单独填进
Section 1 的原始模型区间。

## 6. 已关闭的错误组合方式

- [Multi-parent excess-information counterexample](./MULTIPARENT_EXCESS_INFORMATION_COUNTEREXAMPLE_2026_08_13.md)：同一 parity/checksum 可在多个 parents 中重复产生 raw deficit。
- [Reverse-entropy telescoping audit](./REVERSE_ENTROPY_TELESCOPING_AUDIT_2026_08_13.md)：若不条件于完整 label prefix，同一 bit 可反复擦除、恢复和收费。
- [Ordinary belief-state complementarity no-go](./ORDINARY_BELIEF_STATE_COMPLEMENTARITY_NOGO_2026_08_13.md)：单 fiber rank 与 transport 没有普适正 gap。
- [Rank-$1$ residual-shadow barrier](./JOINT_REPLACEMENT_RANK_VOLUME_LOWER_BOUND_2026_08_16.md)：极薄 covering design 仍可让所有 rank-$1$ sections 看起来完整。
- [Future-visible double-charge barrier](./ALL_PIVOT_FUTURE_VISIBLE_DOUBLE_CHARGE_BARRIER_2026_08_17.md)：exact bucket counts 同时实现 all-pivot deficit、exact rank 和 deletion 后 response distinctions，三者不能裸加。
- [Pair hierarchy symmetry failure](./HIERARCHICAL_PAIR_QUOTIENT_SYMMETRY_FAILURE_2026_08_17.md)：单个 distinguished query 的 $(G,E)$ profile 不能冒充 uniform inner-label FPR。

因此，raw per-cut deficits、marginal union sizes、posterior TC 或两个独立上界不能在
没有 joint-intersection/transversality theorem 时直接相加。

## 7. 不应继续引用为当前 frontier 的旧数字

| 数字 | 原因 |
|---:|---|
| $1.13$ | Lovett--Porat computer-search remark，不是正式证书 |
| $C_{\mathrm{AP}}$ under only $u/n\to\infty$ | $C_{\mathrm{AP}}$ 的 lifting 仍需要 $u/n^2\to\infty$ 和确定的超线性 horizon；新 replacement-cover theorem 只给 $1+2^{-48}$，尚未把 $C_{\mathrm{AP}}$ 推到自然宇宙 |
| $1.199273$ ordinary | 只证明于 monotone 子类；ordinary nonmonotone lifting 有 partition-dependence gap |
| $2.200611$ arbitrary infinite history | 当前只在受限 horizon 或 whp-resource 语义成立 |
| $2.287904$ fixed-worst-case | 外部 entropy-array theorem 给的是 whp space/time |
| $2.349083$ current upper | 已被 cross-block mod-$6$ 的严格 $2.34614905664$ 改进 |
| $2.346149$ optimum | 目前只是可实现上界；matching lower bound 仅在某些 restricted quotient classes 内成立 |
| $2.345979662$ theorem | 目前只是两层 Pair hierarchy 数值侦察，尚无独立 theorem package |
| $1.7156$ as a proved decimal | $C_{\mathrm{AP}}$ 的 variational limit 已闭合，但该小数仍只是 all-active equation 的 numerical location；尚未证明 decimal enclosure |

Kuszmaul--Walzer 2024 的精确线性余项暂不在本页列小数：KLZ arXiv v1 中展示的
公式含一个 $1/2$ 因子时数值约为 $0.1785n$，但相邻文字写“约 $0.35n$”。在核到
KW24 primary source 前，不把这个存在 factor-two 冲突的二手常数当作可靠表项。

## 8. 外部来源

- Carter et al., *Exact and Approximate Membership Testers*, STOC 1978, [DOI](https://doi.org/10.1145/800133.804332).
- Bloom, *Space/Time Trade-offs in Hash Coding with Allowable Errors*, CACM 1970, [DOI](https://doi.org/10.1145/362686.362692).
- Lovett--Porat, *A Space Lower Bound for Dynamic Approximate Membership Data Structures*, FOCS 2010 / SICOMP 2013, [DOI](https://doi.org/10.1137/120867044).
- Pagh--Segev--Wieder, *How to Approximate a Set Without Knowing Its Size in Advance*, FOCS 2013, [arXiv](https://arxiv.org/abs/1304.1188).
- Kuszmaul--Liang--Zhou, *Fingerprint Filters Are Optimal*, FOCS 2025, [arXiv](https://arxiv.org/abs/2510.18129).
- Blelloch--Hu--Kuszmaul--Li--Zhou, *Dynamic Entropy-Encoded Arrays in $O(1)$ Time with Nearly Optimal Space*, 2026, [arXiv](https://arxiv.org/abs/2608.06066).
- Li et al., *ChainedFilter*, SIGMOD 2024, [arXiv](https://arxiv.org/abs/2308.13632).

## 9. Verification policy

`../scripts/` 中既有定理证书，也有探索程序。只有同时具备 finite statement、误差
量词说明和 hostile audit 的结果，才列入 Sections 1--4。
