# Operational support completion theorem：hostile audit

> 日期：2026-08-16。审计对象：
> `OPERATIONAL_SUPPORT_COMPLETION_AVALANCHE_LOWER_BOUND_2026_08_16.md`。
> 裁决：support-completion 极限与 avalanche lower bound 成立；
> 它是一般 structural theorem，不是 unrestricted constant 已解。

## 1. Support 补全不要求可观 posterior mass

Doping law `Q` 只需对每个 operationally compatible pair `(T,omega)` 给正
mass。在混合权重 `eta>0` 下，这使 conditional support 恰好变成
完整 section。证明随后在每个固定有限 instance 上令 `eta->0`。

因为 finite-alphabet entropy 连续，

\[
H(P_\eta)\to H(P),
\qquad
I_{P_\eta}(S;\Omega)\to I_P(S;\Omega).
\]

所以没有把 free support 误当成 free entropy。Rare witnesses 对 union 的影响
保留在

\[
\log\binom wt-H(S\mid R,M)
\]

中。

## 2. Operational fiber 的量词

Fiber 必须固定：

- tape；
- physical state；
- logical load；
- exact operation time。

否则一个 witness history 接上 suffix 后可能超出 horizon，或落在不同的
decoder fiber。主文的定义保留了这四项。

## 3. Common-suffix direction

对 `T cap J(omega)=emptyset`，self-contained suffix 对 `T` 合法，且不会
删除 `T` 的原有 keys。Fixed-tape determinism 使所有这些 worlds
到达 actual successor state。因此

\[
W[J]\subseteq W^+.
\]

所以

\[
|W\cap W^+|\ge |W[J]|,
\]

且真实 transport log-loss 不超过 section log-loss。方向没有反。

## 4. Suffix distribution 不需要 uniform

Theorem 3.1 不假设 `Omega` 与 source 独立或均匀。任意 dependence 都保留为

\[
\mathsf J=I(S;\Omega\mid\Theta,R,M).
\]

这避免了旧 SUC-only 尝试中把 `G_ell` endpoint worlds 与尚未插入的
future batch `X_k` 做错误 chain-rule 对齐。只有在具体 hard source 中
另外证明 `mathsf J=o(n)` 后，才能忽略这一项。

## 5. Pointwise FPR 的使用顺序

Theorem 3.1 本身完全不使用 FPR。Corollary (20)--(22) 先固定一条
concrete source history 和一个 concrete nonmember，再对原 tape `R`
使用 pointwise FPR，最后才对 source 平均。证明没有在条件于
`(R,M)` 后重用 FPR。

## 6. Hostile examples

### ALL-YES branch

若 full fiber 是所有 `t`-sets，则 `W=U`，且 section union 至少是
`U setminus J`。产生的小 log-loss 由 suffix-source dependence 与 exact
finite-population correction 支付。定理不会错误排除 ALL-YES tapes。

### Exact dictionary

Operational fiber 为 singleton `\{S\}`，而合法 insertion labels 与 `S` 不交。
所以 `W[J]=W=S`，avalanche 项为零。大 exact-state cost 不会被重复
收费。

### Rare-witness poisoning

大量 fringe keys 可以只有极低 source mass 的 witnesses。Doping 使它们进入
section support，但当 suffix 杀死这些 witnesses 时，

\[
\log\binom wt-H(S\mid R,M)
\]

正好记录 posterior 在完整 union 内的 thinness。这是本定理要捕捉的
主要例子。

### Source-invisible ghosts

即使 actual source conditional support 中没有任何 witness 包含 ghost key，
`Q` 仍覆盖完整 operational fiber。因此主定理不再需要 BSSI 中的
source-cover equality。

### Global parity / DTC

定理是 single-cut inequality。它不对不同 leave-one-out contexts 的右侧求和。
因此 parity state 在多个 parents 之间重用一 bit 不会与定理矛盾。

## 7. One-label preorder 检查

若 `x preceq y` 且 `y preceq z`，则每个包含 `x` 的 family member
先包含 `y`，再包含 `z`，故关系可传递。对任意 `x in W`，选一个
witness `T` 包含 `x`；所有 `y` with `x preceq y` 都属于 `T`，
所以 `|up x|<=t`。式 (26) 只是这个 incidence matrix 的两种求和
顺序，无 independence 假设。

## 8. 最终裁决

`scripts/verify_operational_support_completion_small.py` 额外穷举了
`u=4,t=2` 下的 665 组 operational-family/source-subfamily pairs，并对
均匀合法 one-label suffix 检查 (6)。最小 slack 为零。这是对
support 量词和 mutual-information 符号的 finite sanity check，不代替
Theorem 3.1 的一般证明。

可以声明：

1. 完整 operational-fiber section loss 有一个不需 source-cover 的 exact
   avalanche-or-information upper bound；
2. 常数概率的常数比例 avalanche 给出超过 Carter 的直接下界；
3. source-invisible ghosts 不再是该 single-cut interface 的缺口。

不能声明：

1. 所有 low-space filters 都有大 avalanche；
2. 小 avalanche 在多个 recurrent cuts 上自动产生 joint width；
3. unrestricted ordinary model 已在 `u/n->infinity` 下得到 `1.4344n`
   或任何新 universal constant。

剩余的核心已经从

\[
\text{source cover} + \text{bounded influence}
\]

缩小为

\[
\text{small recurrent avalanche}
\Longrightarrow
\text{joint replacement-response width}.
\]
