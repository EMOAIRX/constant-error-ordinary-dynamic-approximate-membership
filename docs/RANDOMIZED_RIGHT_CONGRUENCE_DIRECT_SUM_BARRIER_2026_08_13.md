# Randomized right congruence 的 direct-sum barrier

> 日期：2026-08-13。状态：本文给出普通 public-tape dynamic AMQ 的精确
> right-congruence formulation、一个任意维解析反例，以及能够恢复可加性的
> 充分条件。反例支持任意长 insert/delete histories，不是 finite-horizon 或
> 小规模枚举现象。

## 1. Causal / zero-error formulation

令 \(\mathcal L\) 是全部合法 update histories 的 prefix language，
\(S(h)\) 是 history \(h\) 的当前集合。固定公共随机带 \(r\) 后，任意
\(H\)-bit filter 定义一个有限指数的 labeled right congruence

\[
h\equiv_r h'
\Longrightarrow
h\circ w\equiv_r h'\circ w
\tag{1}
\]

其中式 (1) 只对两边都合法的 labeled continuation \(w\) 使用。一个 class
\(C\) 的 minimal one-sided reproduction 是

\[
A_r(C)=\bigcup_{h\in C}S(h).
\tag{2}
\]

随机 filter 是这些至多 \(2^H\) classes 的 right congruences 的分布
\(\mu\)，并满足

\[
\forall h,\ \forall x\notin S(h),\qquad
\Pr_{r\sim\mu}[x\in A_r([h]_r)]\le\varepsilon.
\tag{3}

成员属于式 (2)，所以 zero false negatives 在每条 tape 上成立。反之，任意
满足 (1)--(3) 的 randomized right-congruence cover 都给出一个允许无界计算
时间的普通 fixed-memory dynamic AMQ。

这可以看作 zero-error one-sided distortion 的 causal covering number。与普通
rate--distortion 的关键差别是：

1. zero-FN 对每条 tape 成立，而不是平均 distortion；
2. (3) 是每个固定 history--query pair 的边缘约束；
3. 代价是每条 tape 的最大 class 数，而不是 mutual information；
4. 所有 blocks 可以共享同一个免费随机 certificate。

## 2. 一般解析反例

### Theorem 2.1（coordinate-erasure right congruence）

取 \(k\) 个互不相交的一键 blocks。block \(i\) 的 logical state 是
\(s_i\in\{0,1\}\)，支持合法的 `Insert(i)`、`Delete(i)` 和 `Query(i)`。
令 \(m\in\{0,\ldots,k\}\)，并设

\[
\varepsilon=1-\frac mk.
\]

则存在支持任意长合法历史的 public-tape filter，只有

\[
\boxed{2^m\text{ persistent states}}
\tag{4}
\]

且对每个固定当前非成员的 FPR 恰为 \(\varepsilon\)。

**构造。** 公共随机带均匀选择 \(m\)-subset \(C\subseteq[k]\)。persistent
state 只保存 \((s_i)_{i\in C}\)。对 \(i\in C\)，updates 与 query 都精确；
对 \(i\notin C\)，updates 被忽略且 query 永远 YES。固定 \(C\) 后，两个
histories 等价当且仅当它们在 \(C\) 上的当前 bit vector 相同。这是一个
\(2^m\)-class labeled right congruence，因而支持任意 history。

若 \(s_i=0\)，恰在 \(i\notin C\) 时发生 false positive，所以

\[
\Pr[i\notin C]=1-m/k=\varepsilon.
\]

若 \(s_i=1\)，无论 \(i\) 是否在 \(C\) 中都回答 YES。证毕。

### Corollary 2.2（同参数 block direct sum 为假）

对单个 one-bit block 和任意 \(\varepsilon<1\)，至少需要两个 states。因为
若只有一个 state，该 state 可由成员 endpoint 到达，zero-FN 强迫它回答 YES；
空 endpoint 也处于同一 state，故 FPR 为一。因此

\[
\mathsf{RC}_\varepsilon(\mathcal L_{\rm bit})=2.
\tag{5}
\]

但在 \(k\) blocks、\(\varepsilon=1/2\) 时，Theorem 2.1 给

\[
\mathsf{RC}_{1/2}(\mathcal L_{\rm bit}^{\times k})
\le2^{k/2}
<2^k
=\mathsf{RC}_{1/2}(\mathcal L_{\rm bit})^k.
\tag{6}

所以不存在

\[
\log\mathsf{RC}_\varepsilon(\mathcal L_1\times\cdots\times\mathcal L_k)
\ge
\sum_i\log\mathsf{RC}_\varepsilon(\mathcal L_i)
\tag{7}

这样的 ordinary-public-tape direct sum。gap 是 \(\Theta(k)\) bits 或状态数上的
指数因子，不是 rounding artifact。

该构造正是 balanced frozen mask 的最小动态版本。它说明随机带可以决定本条
tape 完全放弃哪些 blocks；同一个 certificate 同时服务这些 blocks 的所有时刻、
所有 updates 和所有 queries。

## 3. 为什么常见 tensorization theorem 不适用

### 3.1 Shannon / nonanticipatory rate--distortion

经典 rate--distortion 及 nonanticipatory RDF 在 independent product source、
separable average distortion 和 mutual-information/directed-information objective
下有加性定理。这里 objective 是 worst-case state alphabet，zero-FN 是 per-tape
硬约束，而 FPR 只是 public-tape 上的 pointwise marginal。把它换成 directed
information 会得到一个合法 relaxation，但会丢掉 fixed-state covering 的主要
困难，也不能按时间求和：同一 \(H\)-bit state 可以在 updates 后覆盖旧信息。

### 3.2 Zero-error graph entropy

若 deterministic code classes 必须是 confusability graph 的 independent sets，
Korner graph entropy 和相应 fractional covering quantities在合适的 OR products
下具有加性或乘法性质。Approximate membership 的 classes 不是 independent
sets：同一 class 可以合并冲突 endpoints，只是在产生的 directed false-positive
pairs 上由随机混合满足边缘上界 (3)。此外 classes 必须同时是 labeled right
congruence classes。因此普通 graph-entropy product theorem没有覆盖当前优化域。

### 3.3 Pairwise collision inequalities

对每个固定 predecessor，one-sidedness确实给 successor collision probability
至多 \(\varepsilon\)。但 Theorem 2.1 中所有未保存 coordinates 的 collisions
由同一个随机 \(C\) 完全相关。故 collision entropy、ghost entropy或 deletion
certificate 不能逐 block或逐时间相加。

## 4. 能恢复可加性的条件

以下条件足以恢复 direct sum，但都比普通 KLZ public-tape模型强。

### 4.1 Cartesian right congruences

若每条 tape 上的 congruence 被要求分解为

\[
\equiv_r=\equiv_{r,1}\times\cdots\times\equiv_{r,k},
\]

且 persistent representation 是这些 block states 的 Cartesian product，则
class 数逐 tape 相乘，log-space逐 block相加。这是最直接但也最强的 locality
假设。

### 4.2 Independent local tapes 与 conditional FPR

要求 \(R=(R_1,\ldots,R_k)\) 独立，并对每个固定 \(r_{-i}\)、outside history和
block-\(i\) nonmember 都有

\[
\Pr_{R_i}[\mathrm{FP}_i\mid R_{-i}=r_{-i}]\le\varepsilon.
\tag{8}

式 (8) 禁止一条 global tape 牺牲整个 block。但若要从 (8) 得到 state-count
乘法，仍需 rectangular fibers、local decodability或等价的 product-representation
条件；单独的 conditional FPR 只能给每个 slice 的 lower bound，不能把 slices
相乘。

### 4.3 Exact error \(\varepsilon=0\)

若所有 queries 必须精确，则不同 logical product states必须由查询区分。在完整
product API 下 endpoint representations不能共享同一物理 state，得到普通 exact
state-count direct sum。这个论证在任意正误差下立即被 coordinate erasure破坏。

### 4.4 Reliability-budget formulation

对普通 pointwise FPR，一个可能成立的定理必须允许在 tapes之间分配 reliability。
任何 per-block rate curve都至少要先与点

\[
(\varepsilon,R)=(1,0)
\]

取 lower convex envelope。Theorem 2.1 实现的正是“以总 reliability
\(1-\varepsilon\)选择 blocks精确维护”的 time sharing。因此未经这一步
convexification 的 direct-sum势函数不可能正确。

## 5. 对 ordinary dynamic AMQ 下界的含义

这个反例没有否决所有 batch lower bound。它否决的是依赖以下形式的证明：

\[
\text{每个 block 的 pointwise FPR}\le\varepsilon
\quad\Longrightarrow\quad
\text{每个 block 独立支付同一正成本}.
\]

一个可能正确的普通模型 theorem必须把 shared certificate 当作优化变量，而不是
误差项。可考虑的量是：对 tape \(r\) 定义每个 block 的 reliability
\(\alpha_i(r)\)，满足

\[
\mathbb E_r\alpha_i(r)\ge1-\varepsilon,
\]

再证明单条 tape 的 state cost 至少为某个联合势

\[
\Phi(\alpha_1(r),\ldots,\alpha_k(r)).
\]

只有当 \(\Phi\) 对 reliability allocation 有合适的凸性，平均后才会产生全局
下界。coordinate-erasure 构造要求任何候选 \(\Phi\) 在
\(\alpha_i\in\{0,1\}\) 的极点上 sharp；逐 block certificate entropy求和不满足
这一压力测试。

## 6. 裁决

普通 public-tape dynamic AMQ 不具有同误差参数的 block direct sum，即使 blocks
是最简单的一键全动态系统、history任意长、且每条 tape 本身是完全 canonical 的
right congruence。

因此更可行的解析路线不是证明 naive tensorization，而是求一个
**reliability-allocation / fractional right-congruence covering theorem**。它必须
先精确包含 coordinate erasure，再利用单个大 block 内的 transition constraints
证明 reliability成本严格超过静态 covering成本。有限实例
\(U=4,n=2,q=3\) 的 transition premium 可以作为这种势函数的 seed，但不能直接
按 blocks相加。
