# Ordinary dynamic AMQ 的 right-congruence 全局变分

> 日期：2026-08-13。状态：有限参数下的 automaton / LP characterization 是
> exact theorem；binary canonical block class 的 matching theorem 已由现有
> lattice classification 与数值证书给出。对 arbitrary history-dependent
> transducer，缺失的是一个明确的 minimax dual witness，不是 Shannon chain
> rule。

所有对数以 2 为底。

## 1. History unfolding 与 fiber representation

固定有限 universe `U` 和容量 `n`。令 \(\Omega_n\) 是从空集出发的全部合法
`Insert/Delete` histories，\(S(h)\) 是 history \(h\) 的 endpoint。若 update
label \(o\) 对 \(S(h)\) 合法，就有 partial edge

\[
h\xrightarrow{o}ho.
\tag{1}
\]

固定 public tape \(r\) 后，一个 \(K\)-state deterministic filter 是

\[
f_r:\Omega_n\to Q_r,\qquad |Q_r|\le K,
\tag{2}
\]

以及每个 update label 的 deterministic map \(\Delta_{r,o}\)，满足

\[
f_r(ho)=\Delta_{r,o}(f_r(h)).
\tag{3}
\]

因此 \(f_r\) 的 kernel 是 labeled right congruence：若 \(f_r(h)=f_r(h')\)，
则每个对两边都合法的共同 continuation \(w\) 满足

\[
f_r(hw)=f_r(h'w).
\tag{4}
\]

等价地，对物理 state \(q\) 定义 endpoint fiber

\[
\mathcal F_r(q)=\{S(h):f_r(h)=q\}.
\tag{5}
\]

这些 fibers 是 logical update graph 在一个 deterministic state action 中的
relational representation。同一 endpoint 可以出现在多个 fibers，不同
endpoints 也可以出现在同一 fiber；loops 可以在同一 logical endpoint 上产生
holonomy。因此它一般不是 endpoint graph 的 quotient。

更精确地，令 \(\mathsf{Upd}_n\) 为 partial update path category：objects 是
容量至多 \(n\) 的 logical sets，morphisms 是合法 labeled update words，composition
是 concatenation。一个 \(K\)-state **overlapping relational action** 是：

- 一个共同 ambient set \(Q\)，\(|Q|\le K\)；
- 每个 object \(S\) 的非空 reachable subset \(R_S\subseteq Q\)，不同
  \(R_S\) 允许重叠；
- 每个 key-label operation \(o\) 的同一个 global map
  \(\Delta_o:Q\to Q\)，且每条合法边 \(S\xrightarrow{o}T\) 满足
  \(\Delta_o(R_S)\subseteq R_T\)；
- 一个初态 \(q_0\in R_\varnothing\)，且 \(R_S\) 只保留从 \(q_0\) 经某条
  endpoint 为 \(S\) 的合法 path 实际可达的 states。

这与 history right congruence完全等价。它不是通常的
\(\mathsf{Upd}_n\to\mathsf{Set}\) functor，因为各 object fibers并不 disjoint，
同一 \(q\) 可以同时属于多个 \(R_S\)。若 fibers disjoint且每条 edge action是
bijection，才退化为带 monodromy/holonomy 的 permutation cover；若进一步存在被
所有 labeled actions保持的 single-valued section，才可 canonicalize 成 endpoint
quotient。

state \(q\) 的 minimal one-sided accepted set 是

\[
A_r(q)=\bigcup_{T\in\mathcal F_r(q)}T.
\tag{6}
\]

取更大的 accepted set 只会增加 false positives，所以 converse 中可无损地
使用式 (6)。

## 2. Exact public-coin characterization

令 test set

\[
\mathcal T_n=\{(h,x):h\in\Omega_n,\ x\notin S(h)\}.
\tag{7}
\]

对一个 deterministic right congruence \(C\) 定义 rejection profile

\[
z_C(h,x)
=\mathbf 1\{x\notin A_C([h]_C)\}.
\tag{8}
\]

记 \(\mathscr C_{n,K}\) 为全部 index 至多 \(K\) 的 labeled right
congruences，并使用式 (6) 的 minimal query rule。

### Theorem 2.1（fractional right-congruence characterization）

存在一个使用至多 \(\lceil\log K\rceil\) bits、zero false negatives、支持任意
长合法 history、且 pointwise FPR 至多 \(\varepsilon\) 的 ordinary public-tape
dynamic AMQ，当且仅当存在 \(\mathscr C_{n,K}\) 上的概率分布 \(\mu\)，使

\[
\forall(h,x)\in\mathcal T_n,
\qquad
\mathbb E_{C\sim\mu}z_C(h,x)\ge1-\varepsilon.
\tag{9}
\]

**证明。** 固定 filter tape 得到式 (2)--(4) 的 right congruence。zero-FN
强迫 accepted set 包含式 (6)，而 minimal 化不会恶化 error，故 public tape 的
law 给出 \(\mu\) 与式 (9)。反向，public tape 先采样 \(C\)，persistent state
保存当前 congruence class，updates 沿 quotient transition，query 使用式 (6)。
右同余保证 transition well-defined，式 (6) 保证 zero-FN，式 (9) 给 pointwise
FPR。\(\square\)

这一定理同时覆盖 history dependence、multiple representations、ghosts、global
random masks、non-monotonicity 和 cross-block state sharing。

## 3. Minimax / rate-distortion form

定义 \(K\)-state可达到的 worst-test rejection

\[
V_n(K)
=\max_{\mu\in\Delta(\mathscr C_{n,K})}
  \min_{a\in\mathcal T_n}\mathbb E_{C\sim\mu}z_C(a).
\tag{10}
\]

虽然 histories 无限，固定 \(U,n,K\) 时 labeled transition tables、initial
states和 query tables只有有限多个；无效 machines 可通过 product
\((S,q)\) reachability 删除。因此这是一个有限 LP。LP duality 给

\[
\boxed{
V_n(K)
=\min_{\pi\in\Delta(\mathcal T_n)}
  \max_{C\in\mathscr C_{n,K}}
  \mathbb E_{a\sim\pi}z_C(a).
}
\tag{11}
\]

式 (11) 是 ordinary dynamic AMQ 正确的全局 rate-distortion / graph-entropy
替代物。最优 fixed-state complexity 恰为

\[
H_n(\varepsilon)
=\left\lceil
\log\min\{K:V_n(K)\ge1-\varepsilon\}
\right\rceil.
\tag{12}
\]

这里 distortion 是 support-union 产生的 one-sided false positive，code cells
被额外限制为 right-congruence classes，代价是每条 tape 的 maximum index，而
不是 average mutual information。

### 一个可直接用于下界的 dual lemma

要证明 \(H_n(1/2)>Rn\)，充分且必要的是找到一个与 tape 无关的
history-query distribution \(\pi_n\)，使每个 index 至多 \(2^{Rn}\) 的
deterministic right congruence 都满足

\[
\mathbb E_{a\sim\pi_n}z_C(a)<\frac12.
\tag{13}
\]

因此 arbitrary-transducer matching converse 的最小缺口可以准确表述为：构造
并分析式 (13) 的 symmetric dual witness。它必须直接处理 relational fibers，
不能先把它们 canonicalize。

## 4. 为什么普通 Myhill--Nerode 与 graph entropy 不够

对每个 key \(x\)，成员 histories

\[
L_x=\{h:x\in S(h)\}
\tag{14}
\]

必须包含在该 tape 的 accepted history language 中。但后者可以任意扩大；固定
tape 甚至可以对所有 histories 回答 YES。于是不存在一个 tape-by-tape 的固定
confusability graph，使每个 state class 都必须是 independent set。错误约束只在
不同 tapes 的 convex mixture 后逐 test成立。

同样，final-state mutual information虽然有 chain rule，却看不到 deletion 中间的
ghost distortion；完整 transcript看得见，却可因 mutable memory反复复用而远大于
persistent \(H\)。因此式 (11) 的 L-infinity state-index minimax 不能被普通
Shannon RDF替代。

coordinate-erasure filter进一步强迫任何局部势先对 reliability allocation 作
convexification：一条 tape 可以精确维护一部分 coordinates并永久放弃其余
coordinates。逐 block使用相同 \(\varepsilon\) 的 direct sum 因而为假。

## 5. Algebraic quotient 达到的 matching restricted theorem

考虑以下 restricted class：uniform outer blocks、uniform binary inner symbols、
每个 block显式保持 load；local representation由一个 single-valued canonical
map \(\phi:\mathbb N^2\to Q\) 给出，两个 insertion actions commute，deletion
是相应 inverse，query采用 minimal one-sided rule；global state枚举全部 block
states且总 load 至多 \(n\)。

canonical kernel 是 cancellative additive congruence。exact load 迫使其
same-load kernel 位于

\[
\{t(1,-1):t\in\mathbb Z\}.
\tag{15}
\]

该 kernel 的 subgroup必为 \(q\mathbb Z(1,-1)\)。所以每个非退化 local
machine都等价于保存 one-count modulo \(q\)：load \(c<q\) 时精确，load
\(c\ge q\) 时两个 symbols 都被接受，local OGF为

\[
A_q(z)=\frac{1-z^q}{(1-z)^2}.
\tag{16}
\]

在 half error 下，pointwise FPR校准与 full-state enumeration给 rate

\[
R_q=\min_{0<z<1}
\left\{\frac1{\lambda_q}\log A_q(z)-\log z\right\},
\tag{17}
\]

其中

\[
1-e^{-\lambda_q}\sum_{t=0}^{q-1}
\frac{(\lambda_q/2)^t}{t!}=\frac12.
\tag{18}
\]

现有解析分类与 interval certificate证明 \(q=3\) 对所有整数 \(q\ge2\) 唯一
最优，并达到

\[
\boxed{R_3=2.349083440193\ldots\text{ bits/key}.}
\tag{19}
\]

所以已经存在一个真正 matching 的 restricted theorem：不是只在一族人为
thresholds中比较，而是覆盖全部 commuting canonical binary group summaries。

## 6. 从 restricted theorem 到 arbitrary filters 缺什么

arbitrary filter 的 fibers \(R_x\subseteq Q\) 只给 co-representation relation

\[
xCy\iff R_x\cap R_y\ne\varnothing.
\tag{20}
\]

共同 insert/delete continuations使 \(C\) 具有局部 translation/cancellation，
但 \(C\) 不必 transitive。即使updates严格可逆，logical loops仍可产生任意
permutation holonomy。因此不能把式 (20) 替换成 lattice kernel；这种替换既会
虚增 forced-YES support，又会虚减 state count。

把式 (19) 升级成 arbitrary-transducer converse有两个等价的可靠入口：

1. **直接 dual route：** 对 \(R<2.349083\ldots\) 构造式 (13) 的
   \(\pi_n\)，并对所有 nontransitive relational fibers证明平均 rejection
   小于 \(1/2\)。
2. **stability route：** 证明任何在式 (11) 中接近最优的 congruence mixture
   都存在一个 transition-compatible canonical section；丢弃 \(o(n)\) bits与
   \(o(1)\) rejection后，其 fibers可由 commuting lattice quotient描述。

第二条所需的不是单纯的 overlap transitivity，而是
**transition-compatible principal-fiber / trivial-holonomy lemma**。仅有 pairwise
overlap transitivity仍不能保证所有 logical worlds共享同一 representative，也
不能保证 representatives在每个 labeled update下闭合。

这就是当前最小缺参：一个控制 nonprincipal overlap 和 holonomy 的全局量。它应
同时满足：单 tape 的 state-index下界、对 public-tape reliability allocation 的
凸性，以及在 modulo-3 quotient上取等。普通 entropy deficit、pairwise collision
或有限深度 support rank 均不具备这三项。

## 7. 裁决

1. 式 (10)--(12) 给出了 arbitrary ordinary dynamic AMQ 的精确全局变分，既是
   lower-bound定义也是 upper-bound定义。
2. binary commuting canonical class 已有由 order-3 algebraic quotient达到的
   sharp matching theorem，常数为 \(2.349083440193\ldots\)。
3. 当前没有把该常数推广到 arbitrary transducer。唯一诚实的全局证明目标是
   式 (13) 的 dual witness，或等价的 approximate canonicalization theorem。
4. 任何声称只靠 Myhill--Nerode、普通 graph entropy、Shannon chain rule 或
   naive block direct sum完成桥梁的证明，都遗漏了 shared public certificate、
   nontransitive fibers与 reusable memory中的至少一项。
