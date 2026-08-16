# Hierarchical $\operatorname{Pair}_Q$：symbol-symmetry failure

## Verdict

**FAIL.** 原拟议的

$$
H\le2.3074n+o(n)
$$

不成立。旧递推只跟踪了“每层都进入 left child、base query symbol 固定为 $1$”的
distinguished query，却把它误当成全部 $32$ 个 inner labels 的共同 profile。
父层没有保存 child exact load，因此固定 load 下存在的 child symbol swap 不能一般地
提升为 independent-of-load finite-syndrome automorphism。

## 1. Fixed-load recursion

审计从 minimum reachable load $\mu(s)$ 重新推导 parent minimum load。若左 child
实际 slack 为 $E_L$，保存的 allocation residue 强迫删除其中
$E_L\bmod Q$ 的 residue part，只允许整 $Q$ 跨 fiber 平移；右 child 的 zero increment
吸收其余 load。因此

$$
E'=Q\lfloor E_L/Q\rfloor+E_R.
$$

包含 query 的 left witness 必须补足 child gap $G_L$；先用现有 residue slack，剩余部分
向上取整到 $Q$ 的倍数，得到

$$
G'=Q\left\lceil\frac{(G_L-(E_L\bmod Q))_+}{Q}\right\rceil.
$$

所以 `reject iff E' < G'` 的方向正确。脚本的

$$
\binom c{a}
\times(\text{left path count})
\times(\text{right path count})
$$

恰为 fixed-load labeled sequence multiplicity，没有把 state-uniform 与 path-uniform
混淆。

## 2. Exact load-$1$ counterexample

最终 $Q=1$ 层把两个 child 的 zero increments 合并为同一个 finite-group increment。
因此 $32$ 个 labeled symbols 中，$30$ 个 increments 的 multiplicity 是 $1$，一个
increment 的 multiplicity 是 $2$。

在 load $1$ 时，若 stored symbol 的 increment class 大小为 $m$，该 state 的 minimal
one-sided union 含 $m$ 个 labels。对 uniform stored label 和 uniform query label，
acceptance probability 是

$$
\frac{30\cdot1^2+1\cdot2^2}{32^2}
=\frac{34}{1024}.
$$

所以正确 uniform-query rejection 是

$$
\boxed{\rho_1=1-\frac{34}{1024}=\frac{495}{512}.}
$$

旧 distinguished-query verifier 给出 $31/32=496/512$。这一个 exact layer 已经
否定“全部 symbols 对称”的归纳，无需依赖最终 numerical optimum。

Base type 本身也暴露了丢失的信息。相对于 minimum reachable load，query symbol $1$
的 gap 在 residue $0$ 时为 $3$、其余为 $0$；query symbol $0$ 的 gap 恒为 $1$。
两者单层 rejection marginal 相同，但 joint $(G,E)$ law 不同，后续 pairing 可以放大
该差异。

## 3. OGF and $Q=1$

每层保留一个 zero increment，所以 finite syndrome 从 minimum load 起连续可达。
对每对 child syndromes，$Q$ 个 allocation residues 的 minimum-load offsets 恰为
$0,1,\ldots,Q-1$。这严格给出

$$
A_{\operatorname{Pair}_Q(T)}(z)=A_T(z)^2(1-z^Q).
$$

$Q=1$ 不是除零或虚构 constraint；它表示不保存 allocation residue。此时

$$
E'=E_L+E_R,
\qquad
G'=G_L\ \text{or}\ G_R
$$

按 query 所在 child 继承 gap，仍是合法的 total-load pooling operation。

## 4. Correct uniform-query recursion

`scripts/verify_hierarchical_pair_quotient_uniform_audit.py` 对每个 load 保存所有 query
labels 的 integer-total $(G,E)$ multiplicities。Pair 层必须同时加入：

- left queries：
  $$
  G'=Q\left\lceil\frac{(G_L-(E_L\bmod Q))_+}{Q}\right\rceil;
  $$
- right queries：
  $$
  G'=G_R.
  $$

两类共享

$$
E'=Q\lfloor E_L/Q\rfloor+E_R.
$$

证书核对 $\rho_1=495/512$，并严格认证在旧测试点 $\lambda=20.9$ 时，正确 uniform
rejection 已经小于 $1/2$。因此旧 rate test 即使 OGF coefficient bound 本身正确，也
没有满足 half-error calibration。

## 5. What survives

- OGF 恒等式和 key-only additive updates 仍正确；失败只在 query calibration。
- 两层 $(6,8)$ 的正确 uniform-query numerical rate 约为 $2.345979662$，略优于单层
  mod-$6$，但目前没有把这个微小差异提升为新的主结果。
- 更深 binary hierarchy 的数值变化很小或反而恶化；继续增加层数不构成用户要求的
  本质突破。
- 本审计是一个 proof barrier，不是新的 ordinary lower bound 或 matching theorem。
