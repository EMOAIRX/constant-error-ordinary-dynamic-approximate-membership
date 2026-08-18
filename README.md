# Constant-error ordinary dynamic approximate membership

本仓库研究 Kuszmaul--Liang--Zhou（FOCS 2025）留下的 fixed-constant-error
ordinary dynamic approximate membership 问题。

## 原始模型：当前主结论

原始模型指：容量 $n$、$u/n\to\infty$、任意长合法 Insert/Delete 历史、固定最坏
持久空间、免费公共随机带、zero false negatives，以及对每条固定历史和每个固定当前
非成员的 pointwise FPR 至多固定 $\varepsilon\in(0,1)$。

令

$$
\beta=1-\varepsilon,
\qquad
\ell=\log_2(1/\varepsilon),
\qquad
\sigma=\min\{\varepsilon,\beta\},
\qquad
B_0=4\ln2+1.
$$

对 $0<t\le\sigma/4$ 定义

$$
\rho_\varepsilon(t)
=\varepsilon+t-(\varepsilon-t)2^{-2t^2},
\qquad
\alpha_\varepsilon(t)=\beta-t,
$$

$$
\Psi_\varepsilon(t)
=\frac{\alpha_\varepsilon(t)}2
\log_2\frac{\alpha_\varepsilon(t)}{e\rho_\varepsilon(t)}.
$$

方程

$$
\Psi_\varepsilon(t)=\ell+\frac{t^2}{B_0}
$$

在 $(0,\sigma/4)$ 中有唯一解 $t^*_\varepsilon$。令

$$
\Gamma_\varepsilon
=\frac{(t^*_\varepsilon)^2}{B_0\ell}>0.
$$

则当前下界是

$$
\boxed{
H^*_\varepsilon(n,u)
\ge
(1+\Gamma_\varepsilon)n\log_2(1/\varepsilon)-o(n).
}
$$

这是一个统一的 fixed-$\varepsilon$ 定理；$\varepsilon=1/2$ 只是同一解析方程的直接
代入。定理不选择 $2^{-20}$、$2^{-48}$ 或任何其它 dyadic witness，也不使用数值求根。
$B_0$ 正好来自统一阈值证明中的两次 accepted-size 偏差和一次 posterior-KL 偏差，
而 $\rho_\varepsilon(t)$ 是 support thickness 直接给出的、未经线性松弛的
successor-reservoir density 上界。

在半误差下，当前真正可比较的一对无条件界是

$$
\boxed{
(1+\Gamma_{1/2})n-o(n)
\le
H^*_{1/2}(n,u)
\le
2.34614905664\,n+o(n).
}
$$

| 方向 | 结论 | 来源 | 状态 |
|---|---:|---|---|
| 下界 | $H\ge(1+\Gamma_\varepsilon)n\log_2(1/\varepsilon)-o(n)$ | 本仓库：canonical fixed-$\varepsilon$ replacement-cover theorem | 无条件；只假设 $u/n\to\infty$，允许 arbitrary history dependence |
| 上界（$\varepsilon=1/2$） | $H\le2.34614905664n+o(n)$ | 本仓库：cross-block mod-$6$ additive quotient | 无条件；任意长历史、无 overflow、固定最坏空间 |

- [统一 fixed-$\varepsilon$ 下界与完整证明](./docs/CANONICAL_FIXED_EPSILON_REPLACEMENT_COVER_2026_08_18.md)
- [simultaneous replacement-cover 基础定理](./docs/SIMULTANEOUS_REPLACEMENT_COVER_WIDTH_LOWER_BOUND_2026_08_17.md)
- [当前上界定理](./docs/CROSS_BLOCK_MOD6_CONSTRUCTION_2026_08_13.md)
- [独立 hostile audit](./docs/TWO_SUBBLOCK_MODULUS_INDEPENDENT_AUDIT_2026_08_13.md)

因此，原始 ordinary 模型在每个固定错误率下都严格超过 Carter 静态基线；目前仍未
确定下界增益的最佳值，也没有证明半误差上界 $2.34614905664$ 最优。

## 改变条件后的下界

下表中的行不能互相替换；每个常数只在同一行写明的条件下成立。

| 模型或额外条件 | 半误差下界 | 来源 | 准确地位 |
|---|---:|---|---|
| 原始 ordinary 模型，$u/n\to\infty$ | $H\ge(1+\Gamma_\varepsilon)n\log_2(1/\varepsilon)-o(n)$ | 本仓库：canonical fixed-$\varepsilon$ replacement-cover theorem | 一般、无条件；每个固定 $\varepsilon\in(0,1)$，允许 arbitrary history dependence |
| ordinary 模型，$u/n^2\to\infty$，且支持确定的 $f(n)/n\to\infty$ 操作 horizon | $H\ge C_{\mathrm{AP}}n-o(n)$，其中 $C_{\mathrm{AP}}>1.607987002861718\ldots$ | 本仓库：continuous full-fiber all-pivot converse | 在所列强宇宙/时域量词内不假设 BSSI、monotonicity 等结构；$C_{\mathrm{AP}}$ 是完整 finite hierarchy 的严格极限，不是新挑选的有限 block 常数 |
| ordinary 模型，$u/n^2\to\infty$ | $H\ge1.198n-o(n)$ | 本仓库：multicut prefix-union theorem | 一般、无条件；证明只用 fresh insertions，因此也适用于 incremental filters |
| ordinary 模型，$u/n\to\infty$，再假设 BSSI | $H\ge1.434406361243753\ldots n-o(n)$ | 本仓库 | 条件定理；尚未证明所有低空间 ordinary filters 都满足 BSSI |
| history-dependent monotone 子类，$u/n\to\infty$ | $H\ge1.1992732344471508\ldots n-o(n)$ | 本仓库对 KLZ Proposition 4.3 的固定误差审计与 AND 推论 | 不是 ordinary nonmonotone 下界 |
| Lovett--Porat 原模型，$\varepsilon=1/2$，$n/u\to0$ | $H\ge1.1n-o(n)$ | 外部文献：Lovett--Porat 2010/2013 | 原 hard distribution 允许重复 labels；不能不加说明地当作 KLZ fresh-distinct API 定理 |
| dense universe：$u=2n$ | $H\ge0.6225562489\ldots n-o(n)$ | 外部静态 finite-universe covering bound（ChainedFilter/Carter-type counting） | 该 dense-universe regime 的一般下界；本仓库有 $H\le n$ 的任意长历史构造 |

相关文件：

- [Natural-universe simultaneous replacement theorem](./docs/SIMULTANEOUS_REPLACEMENT_COVER_WIDTH_LOWER_BOUND_2026_08_17.md)
- [Natural-universe theorem hostile audit](./docs/SIMULTANEOUS_REPLACEMENT_COVER_WIDTH_HOSTILE_AUDIT_2026_08_17.md)
- [Continuous all-pivot variational limit](./docs/CONTINUOUS_ALL_PIVOT_VARIATIONAL_LIMIT_2026_08_17.md)
- [$1.6079$ finite all-pivot predecessor](./docs/EQUAL_BLOCK_ALL_PIVOT_CONVERSE_2026_08_13.md)
- [$1.6079$ lifting closure audit](./docs/ALL_PIVOT_16079_CLOSURE_AUDIT_2026_08_16.md)
- [$1.198$ multicut theorem](./docs/MULTICUT_PREFIX_UNION_LOWER_BOUND_2026_08_16.md)
- [$1.198$ hostile audit](./docs/MULTICUT_PREFIX_UNION_HOSTILE_AUDIT_2026_08_16.md)
- [BSSI natural-universe theorem](./docs/BOUNDED_SOURCE_SECTION_INFLUENCE_NATURAL_UNIVERSE_LOWER_BOUND_2026_08_15.md)
- [Monotone amplification audit](./docs/AMPLIFICATION_FRONTIER_HOSTILE_AUDIT_2026_08_13.md)
- [Dense-universe $n$-bit construction](./docs/TRANSITION_COMPATIBLE_COVERING_CONSTRUCTION_AUDIT_2026_08_13.md)

## 改变空间或历史量词后的上界

| 模型或资源语义 | 半误差上界 | 来源 | 不能被误写成什么 |
|---|---:|---|---|
| 原始 ordinary、任意长历史、固定最坏空间 | $2.34614905664n+o(n)$ | 本仓库：cross-block mod-$6$ quotient | 尚未证明最优；numerical optimum 约为 $2.3461490548$ |
| 与随机带独立的 oblivious history，长度 $f(n)$ 且 $\log f(n)=o(n)$，固定预分配空间 | $2.20061148296052\ldots n+o(n)$ | 本仓库：heterogeneous fingerprint information-spectrum coder | 不是 adaptive 或任意无限历史上界 |
| polynomial universe、current-state whp space/time、uniform fingerprints | $2.28790401364596\ldots n+o(n)$ | 外部文献：Blelloch--Hu--Kuszmaul--Li--Zhou 2026 | 不是 KLZ fixed-worst-case $H$-bit 上界 |
| 同一 whp-resource 语义，加入 permanent-YES thinning | $2.20061148296052\ldots n+o(n)$ | 本仓库对上述 2026 entropy array 的 lifting | 仍继承 whp 资源量词 |
| incremental/insertion-only | $(1/\ln2)n=1.442695040888\ldots n$ | 外部经典 Bloom filter | 不支持 ordinary deletion |
| uniform exact fingerprint multiplicities、全部 compositions、任意长历史 | $2.384499842479\ldots n+o(n)$ | 标准 fingerprint construction；常数在本仓库审计 | 只是 benchmark，已被 $2.34614905664$ ordinary quotient 改进 |
| dense universe：$u=2n$、任意长历史 | $n$ | 本仓库：balanced frozen mask | 不适用于 $u/n\to\infty$ |

- [Subexponential-horizon fixed-space theorem](./docs/SUBEXPONENTIAL_HORIZON_FINGERPRINT_UPPER_BOUND_AUDIT_2026_08_14.md)
- [Heterogeneous fingerprint class theorem](./docs/VERIFIED_MAIN_THEOREM.md)
- [2026 entropy-array audit](./docs/ENTROPY_ARRAYS_THEOREM_8_2_AUDIT.md)
- [Permanent-YES thinning lifting](./docs/MASKED_ENTROPY_ARRAY_LIFTING_2026_08_13.md)

## 已由外部文献解决的相邻 regime

Kuszmaul--Liang--Zhou（FOCS 2025）解决的是 small-error regime，而不是这里的
固定半误差问题。在

$$
\varepsilon=o(1),
\qquad
u=\omega(n/\varepsilon),
$$

并支持 $\omega(n)$ 次合法 updates 时，KLZ 证明 arbitrary dynamic filters 的
matching lower bound；结合文献中的 fingerprint upper bound，small-error regime
的 first-order optimum 为

$$
\boxed{H^*=n\log_2(1/\varepsilon)+n\log_2 e+o(n).}
$$

KLZ 明确把 $\varepsilon^{-1}=\Theta(1)$ 的 tight upper/lower bounds 留作开放
问题。2026 年 Blelloch--Hu--Kuszmaul--Li--Zhou 解决了 uniform fingerprint
multiset 的高效动态熵编码上界，但没有给出 constant-error arbitrary-filter 下界。

- [KLZ 模型、常数与 2026 follow-up 审计](./docs/FOCS25_MODEL_CONSTANTS_AND_2026_FOLLOWUPS_AUDIT.md)
- [文献与模型边界总审计](./docs/LITERATURE_FRONTIER_AUDIT.md)

## 不是当前定理的数字

- $1.13$ 是 Lovett--Porat 文中的 computer-search remark，不是已认证定理。
- $2^{-20}$ 与 $2^{-48}$ 都只是早期 proof witnesses，已经被统一的
  $\Gamma_\varepsilon$ 定理取代；它们不再作为当前下界陈述。
- $C_{\mathrm{AP}}>1.607987\ldots$ 现在是 $u/n^2\to\infty$ 且
  $f(n)/n\to\infty$ 下的最强 all-pivot 定理；它仍不是原始
  $u/n\to\infty$ 条件下的下界。
- $2.200611\ldots$ 不能写成任意长历史 fixed-worst-case 上界。
- $2.287904\ldots$ 不能写成每张随机带都满足的固定空间上界。
- $2.34614905664$ 是当前严格上界，不是 ordinary 模型的最优值或下界。
- $2.345979662\ldots$ 是两层 Pair hierarchy 的数值侦察；尚无独立 theorem package，
  不列入主区间。

## Research frontier：continuous all-pivot 与自然宇宙

完整 finite Jensen hierarchy 现在已经解析闭合。令

$$
C_{\mathrm{AP}}
=
\inf_{x\uparrow}
\sup_{0\le t\le1}\mathcal F_t[x].
$$

则连续 value-space game 的 infimum attained，并且对每个有限 $q$，

$$
C_q<C_{\mathrm{AP}},
\qquad
\lim_{q\to\infty}C_q=C_{\mathrm{AP}}.
$$

严格 gap 来自 diagonal logarithmic singularity：任何让有限 Jensen reduction
取等的 block-flat profile，都会被 block 内部的 pivot 以无穷代价识别。因此这不是
增加到 $20$ 或 $50$ blocks 后的数值爬升，而是整个 all-pivot hierarchy 的精确
variational limit。结合旧的 $C_{10}$ 证书，严格得到

$$
C_{\mathrm{AP}}>C_{10}
\ge1.607987002861718\ldots .
$$

two-stage partition conditioning、full-fiber common-suffix transport、exact batch code
和全部 fixed finite pivots 的统一误差已经重新审计。在

$$
\frac{u}{n^2}\to\infty,
\qquad
\frac{f(n)}n\to\infty
$$

时，先对每个固定 $q$ 应用 finite theorem，再在 $n\to\infty$ 后取
$q\to\infty$，得到 ordinary、history-dependent、nonmonotone dynamic filter 的
下界 $H\ge C_{\mathrm{AP}}n-o(n)$。这里没有 BSSI、monotonicity 或
canonical-state 假设，也没有使用 growing-depth tree。

- [Continuous value game and exact lifting](./docs/CONTINUOUS_ALL_PIVOT_VARIATIONAL_LIMIT_2026_08_17.md)
- [Finite $C_{10}$ theorem](./docs/EQUAL_BLOCK_ALL_PIVOT_CONVERSE_2026_08_13.md)
- [Finite lifting closure audit](./docs/ALL_PIVOT_16079_CLOSURE_AUDIT_2026_08_16.md)

强宇宙条件已经通过 simultaneous replacement-cover width theorem 降到原始的
$u/n\to\infty$。当前的
[canonical fixed-$\varepsilon$ theorem](./docs/CANONICAL_FIXED_EPSILON_REPLACEMENT_COVER_2026_08_18.md)
进一步去掉了 dyadic witness、任意 good-mass 门槛、线性 reservoir 松弛和重复 tolerance
损失，但还没有接近 $C_{\mathrm{AP}}$。新证明不再要求一个 hard-union witness
同时避开全部 suffix；它对
每个 replacement branch 分别做 posterior pruning，并用一次 KL chain rule 统一收费。
这正是消除旧 $n^2/u$ collision 门槛的关键。

- [Natural-universe replacement-cover theorem](./docs/SIMULTANEOUS_REPLACEMENT_COVER_WIDTH_LOWER_BOUND_2026_08_17.md)

本轮进一步得到一个不重复计费的精确接口。对 normalized ten-pivot dual，可写成

$$
H\ge C_{10}n+V_\lambda-o(n),
$$

其中 $V_\lambda$ 是条件于已有 full-fiber candidate list 后，future response 对 hidden
batches 携带的 conditional mutual information。任何 $V_\lambda\ge\eta n$ 的一般定理
都会把该 finite $C_{10}$ branch 提高 $\eta$；它并不能自动加到新的
$C_{\mathrm{AP}}$ 上。cylinder-complete fibers 还证明 fixed-depth local probes 可以有
$V_\lambda=0$，即使 exact rank 几乎是线性的。因此下一步必须是 linear-depth
recurrent response 或跨 state 的 transversality theorem，而不是再加一个 marginal rank。

- [Normalized-dual conditional novelty theorem](./docs/NORMALIZED_DUAL_CONDITIONAL_NOVELTY_2026_08_17.md)
- [Future-visible double-charge barrier](./docs/ALL_PIVOT_FUTURE_VISIBLE_DOUBLE_CHARGE_BARRIER_2026_08_17.md)

若 attained optimizer 具有 positive all-active density，并满足已推导的 endpoint
regular-variation law，则对应 tail Volterra equation 的 normalized 正解至多一个；
这是由严格正 kernel 的 maximum principle 推出的解析唯一性。仅有 interior Dini
regularity 还不够，必须保证两个正解之比在 endpoint 有有限正极限。该解的 numerical
location 约为 $1.7156$，但这个小数仍不是 theorem。已经严格证明的还包括 endpoint
density 的唯一 regular-variation 指数 $1$ 与不可消除的 $v\log v$ boundary layer。

- [Continuous variational-limit theorem](./docs/CONTINUOUS_ALL_PIVOT_VARIATIONAL_LIMIT_2026_08_17.md)
- [Continuous endpoint boundary theorem](./docs/CONTINUOUS_ALL_PIVOT_ENDPOINT_BOUNDARY_2026_08_17.md)
- [Finite analytic structure and thick-fiber upper barrier](./docs/CONTINUOUS_OPTIMALITY_AND_THICK_FIBER_UPPER_BARRIER_2026_08_17.md)

本项目不会把增加到 $20$ blocks、$50$ blocks 的纯数值爬升当作突破。下一步真正需要
的是以下任一项：

1. 超越当前 canonical replacement-cover balance，并尽量向 $C_{\mathrm{AP}}$ 靠近。
   下一次改进必须加强 posterior replacement width 或改变 hard transition，而不是再挑选
   一个数值 witness；
2. 给出 matching lower/upper bound，从而确定某个明确模型的最优一阶常数；
3. 证明 all-active regularity 和 matching adjoint potential，从而解析识别
   $C_{\mathrm{AP}}$；
4. 证明覆盖 transport/posterior 方法的结构性 barrier theorem。

## 仓库导航

- [详细结果分类与来源](./docs/README.md)
- `docs/`：定理、审计、反例、barrier 与研究笔记。
- `scripts/`：精确证书验证器与探索程序。

运行主要验证器：

```bash
bash scripts/run_theorem_verifiers.sh
python3 scripts/verify_multicut_half_error.py
python3 scripts/verify_hierarchical_pair_quotient_uniform_audit.py
```

探索性数值不视为定理；只有有限参数陈述和 hostile audit 都闭合后才进入上述表格。
