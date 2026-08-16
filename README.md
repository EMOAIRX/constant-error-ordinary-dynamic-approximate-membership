# Constant-error ordinary dynamic approximate membership

本仓库研究 Kuszmaul--Liang--Zhou（FOCS 2025）留下的 fixed-constant-error
ordinary dynamic approximate membership 问题。

## 原始模型：当前真正可比较的一对界

这里的原始模型指：容量 $n$、$u/n\to\infty$、任意长合法
Insert/Delete 历史、固定最坏持久空间、免费公共随机带、zero false negatives，
以及对每条固定历史和每个固定当前非成员的 pointwise FPR 至多 $1/2$。

若 $H^*_{1/2}(n,u)$ 表示这个模型的最优空间，则当前可引用的区间是

$$
\boxed{
n-o(n)
\le
H^*_{1/2}(n,u)
\le
2.349083440193\ldots\,n+o(n).
}
$$

| 方向 | 结论 | 来源 | 状态 |
|---|---:|---|---|
| 下界 | $H\ge n-o(n)$ | 外部文献：Carter 型静态 accepted-set 计数下界 | 无条件；目前自然宇宙下的一般下界 |
| 上界 | $H\le2.349083440193\ldots n+o(n)$ | 本仓库：order-$3$ algebraic threshold quotient | 无条件；任意长历史、无 overflow、固定最坏空间 |

- [本仓库上界定理](./docs/VERIFIED_ALGEBRAIC_THRESHOLD_QUOTIENT_2026_08_13.md)
- [上界 hostile audit](./docs/ALGEBRAIC_THRESHOLD_QUOTIENT_HOSTILE_AUDIT_2026_08_13.md)
- [精确 right-congruence 变分刻画](./docs/RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md)

因此，仓库目前没有在仅假设 $u/n\to\infty$ 时证明一般下界系数严格大于 $1$，
也没有证明 $2.349083\ldots$ 最优。

## 改变条件后的下界

下表中的行不能互相替换；每个常数只在同一行写明的条件下成立。

| 模型或额外条件 | 半误差下界 | 来源 | 准确地位 |
|---|---:|---|---|
| 原始 ordinary 模型，$u/n\to\infty$ | $H\ge n-o(n)$ | 外部文献：Carter 静态基线 | 一般、无条件 |
| ordinary 模型，$u/n^2\to\infty$ | $H\ge1.198n-o(n)$ | 本仓库：multicut prefix-union theorem | 一般、无条件；证明只用 fresh insertions，因此也适用于 incremental filters |
| ordinary 模型，$u/n\to\infty$，再假设 BSSI | $H\ge1.434406361243753\ldots n-o(n)$ | 本仓库 | 条件定理；尚未证明所有低空间 ordinary filters 都满足 BSSI |
| history-dependent monotone 子类，$u/n\to\infty$ | $H\ge1.1992732344471508\ldots n-o(n)$ | 本仓库对 KLZ Proposition 4.3 的固定误差审计与 AND 推论 | 不是 ordinary nonmonotone 下界 |
| Lovett--Porat 原模型，$\varepsilon=1/2$，$n/u\to0$ | $H\ge1.1n-o(n)$ | 外部文献：Lovett--Porat 2010/2013 | 原 hard distribution 允许重复 labels；不能不加说明地当作 KLZ fresh-distinct API 定理 |
| dense universe：$u=2n$ | $H\ge0.6225562489\ldots n-o(n)$ | 外部静态 finite-universe covering bound（ChainedFilter/Carter-type counting） | 目前也是一般 dynamic 模型唯一无条件下界；本仓库有 $H\le n$ 的任意长历史构造 |

相关文件：

- [$1.198$ multicut theorem](./docs/MULTICUT_PREFIX_UNION_LOWER_BOUND_2026_08_16.md)
- [$1.198$ hostile audit](./docs/MULTICUT_PREFIX_UNION_HOSTILE_AUDIT_2026_08_16.md)
- [BSSI natural-universe theorem](./docs/BOUNDED_SOURCE_SECTION_INFLUENCE_NATURAL_UNIVERSE_LOWER_BOUND_2026_08_15.md)
- [Monotone amplification audit](./docs/AMPLIFICATION_FRONTIER_HOSTILE_AUDIT_2026_08_13.md)
- [Dense-universe $n$-bit construction](./docs/TRANSITION_COMPATIBLE_COVERING_CONSTRUCTION_AUDIT_2026_08_13.md)

## 改变空间或历史量词后的上界

| 模型或资源语义 | 半误差上界 | 来源 | 不能被误写成什么 |
|---|---:|---|---|
| 原始 ordinary、任意长历史、固定最坏空间 | $2.349083440193\ldots n+o(n)$ | 本仓库 | 尚未证明最优 |
| 与随机带独立的 oblivious history，长度 $f(n)$ 且 $\log f(n)=o(n)$，固定预分配空间 | $2.20061148296052\ldots n+o(n)$ | 本仓库：heterogeneous fingerprint information-spectrum coder | 不是 adaptive 或任意无限历史上界 |
| polynomial universe、current-state whp space/time、uniform fingerprints | $2.28790401364596\ldots n+o(n)$ | 外部文献：Blelloch--Hu--Kuszmaul--Li--Zhou 2026 | 不是 KLZ fixed-worst-case $H$-bit 上界 |
| 同一 whp-resource 语义，加入 permanent-YES thinning | $2.20061148296052\ldots n+o(n)$ | 本仓库对上述 2026 entropy array 的 lifting | 仍继承 whp 资源量词 |
| incremental/insertion-only | $(1/\ln2)n=1.442695040888\ldots n$ | 外部经典 Bloom filter | 不支持 ordinary deletion |
| uniform exact fingerprint multiplicities、全部 compositions、任意长历史 | $2.384499842479\ldots n+o(n)$ | 标准 fingerprint construction；常数在本仓库审计 | 只是 benchmark，已被 $2.349083\ldots$ ordinary quotient 改进 |
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
\boxed{
H^*
=
n\log_2(1/\varepsilon)+n\log_2 e+o(n).
}
$$

KLZ 明确把 $\varepsilon^{-1}=\Theta(1)$ 的 tight upper/lower bounds 留作开放
问题。2026 年 Blelloch--Hu--Kuszmaul--Li--Zhou 解决了 uniform fingerprint
multiset 的高效动态熵编码上界，但没有给出 constant-error arbitrary-filter 下界。

- [KLZ 模型、常数与 2026 follow-up 审计](./docs/FOCS25_MODEL_CONSTANTS_AND_2026_FOLLOWUPS_AUDIT.md)
- [文献与模型边界总审计](./docs/LITERATURE_FRONTIER_AUDIT.md)

## 不是当前定理的数字

- $1.13$ 是 Lovett--Porat 文中的 computer-search remark，不是已认证定理。
- 旧的 $1.6079$ all-pivot 数值依赖尚未闭合的 lifting/interface，不列入当前可信
  frontier。
- $2.200611\ldots$ 不能写成任意长历史 fixed-worst-case 上界。
- $2.287904\ldots$ 不能写成每张随机带都满足的固定空间上界。
- $2.349083\ldots$ 是上界，不是 ordinary 模型的最优值或下界。

## 仓库导航

- [详细结果分类与来源](./docs/README.md)
- `docs/`：定理、审计、反例、barrier 与研究笔记。
- `scripts/`：精确证书验证器与探索程序。

运行主要验证器：

```bash
bash scripts/run_theorem_verifiers.sh
python3 scripts/verify_multicut_half_error.py
```

探索性数值不视为定理；只有有限参数陈述和 hostile audit 都闭合后才进入上述表格。
