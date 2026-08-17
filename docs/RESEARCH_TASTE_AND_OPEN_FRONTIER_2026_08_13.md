# Ordinary dynamic AMQ：现有工作的缺口与下一步研究判断

> 日期：2026-08-13。本文是研究决策文档，不把猜想写成定理。讨论的主模型是
> zero-FN、public-tape、key-only updates、pointwise FPR，允许 arbitrary history
> dependence、multiple representations、ghosts 和 global certificates。

> 2026-08-17 update：本文提出的 simultaneous successor-width 目标已经由
> [replacement-cover theorem](./SIMULTANEOUS_REPLACEMENT_COVER_WIDTH_LOWER_BOUND_2026_08_17.md)
> 实现，原始 natural-universe 模型现在有
> $H\ge(1+2^{-48})n-o(n)$。本文关于有限 gadget、重复计费和 upper-bound taste 的
> barrier 判断仍保留；Section 1.3 的“尚未超过 Carter”已被新定理取代。

## 1. 结论先行

当前工作不是“没有贡献”，但三个不同层次必须分开。

1. **可闭合的 lower-bound paper。** 在 `u/n^2 -> infinity`、half error 下，
   full-fiber all-pivot hierarchy 给出认证常数
   \[
   H>1.6079n-o(n).
   \]
   十块凸优化和有理 dual 已可靠；two-sigma-field prefix lemma 已写入当前稿，仍需
   一次从 KLZ 原始 sampling 到全部 measurability/统一误差的逐行审计。这个结果有
   方法价值，但没有解决自然 `u/n -> infinity` regime，也离上界很远。

2. **可形成独立 upper-bound paper。** 若采用 KLZ lower bound 实际使用的
   seed-independent、预先给定的超线性操作窗口（例如任意长度至多 `n^c` 的固定
   history），masked fingerprint multiset 可以严格达到
   \[
   H\le2.200611482960522\,n+o(n)
   \]
   at `epsilon=1/2`。这是真正的 fixed preallocation、ordinary key API、逐 tape
   zero-FN、pointwise FPR 上界，不只是 expected-space benchmark。它不适用于无限
   history 或 seed-adaptive history。单独的 typical-set coding 不新；可投稿的包是
   generalized IID fingerprint class 的 matching converse、heavy endpoint、解析 phase
   transition 和动态 fixed-slot implementation。

3. **真正的核心 open problem。** 在 natural `u/n -> infinity` regime，对 arbitrary
   ordinary filters 证明超过 Carter，或给出低于现有构造的新 right-congruent cover。
   继续叠加 posterior deficits、directed information 或 finite gadgets不会解决它。
   所需的新对象必须看见同一 state 上所有未访问 replacement branches 的联合行为。

因此研究优先级应是：先固定一个可提交成果，再把高风险主线集中到 branching
compatibility；不再继续优化 `C_20,C_50` 或构造单层形式 profile。

## 2. 当前严格状态

### 2.1 已经可靠

- ordinary filter 与 randomized right-congruent cover 的 exact finite-parameter
  characterization；
- `q=10` all-pivot convex certificate：`C_10>1.6079`；
- `U=4,n=2` 的 transition dual：三状态最优 depth-3 FPR 为 `29/45`，而四状态
  frozen mask 达到 half error；
- coordinate-erasure、cover-and-tombstone、reusable-memory 和 XOR checksum
  barriers；
- binary canonical lattice classification，以及 saturated-prefix flat-tail rigidity；
- finite-horizon masked fingerprint rate及其解析 phase constants。

### 2.2 仍需谨慎表述

all-pivot稿现在显式分开两个条件场：先在不含完整 partition 的条件场中做
removing-partition，再加入 partition 证明 hidden batch 的 hypergeometric law。
这个修补方向正确，但正式引用 `1.6079` 前仍应检查：

- transcript 对相容 balanced partitions 的 likelihood 是否严格常数；
- 重复 labels、已暴露 labels 与 rightmost batch 的条件独立；
- difference first moment 与 batch decoder side information 的拼接；
- 所有 `ell,k,r` 上误差的一致性；
- 从实际 `x_0>=0,x_b<=1` 到 `x_0=0,x_b=1` 的单调放松。

数值证书不是风险所在；风险只在 lifting 层。

## 3. 已被关闭的路线

### 3.1 Multi-parent posterior 不能作为主 invariant

对 independent blocks，普通 total correlation 公式是错的。正确恒等式为

\[
\sum_i I(X_i;M\mid X_{-i})
=I(X;M)+\operatorname{DTC}(X\mid M).
\]

但 XOR checksum 使 DTC 本身达到线性放大：同一个 query-silent `L`-bit parity
可被任意多个 leave-one-out parents 各恢复一次，而 query 行为完全不变。这个机制
能嵌入 ordinary arbitrary-history transducer。因此任何 posterior invariant 若不先
商掉 future-query-equivalent states，都会给冗余 memory 错误收费。

### 3.2 All-pivot 与 transition dual 不能直接相加

all-pivot dual 已经通过归一化权重对 final state 收费一次。finite transition dual 的
额外代价主要存在于中间或 counterfactual histories。把两者独立相加会再次把 reusable
memory 当成不可复用 memory。

合法的合成必须改变同一个 cell 的可行域：给定 union profile、section thickness 和
transition table，证明该 cell family 至少需要更多 colors。它不能是“两条 lower
bounds 求和”。

### 3.3 Midpoint barrier 是真实的

把 posterior support cost 记为 `A`，within-union deficit 记为 `D`，理想 hard-rank
saving 记为 `C`，transport debit 记为 `T`。现有信息最多给

\[
H\ge A+D,\qquad H\ge C-D-o(n),
\]

因而对未知 `D` 最坏化只能得到

\[
H\ge(A+C)/2-o(n).
\]

要超过这个 barrier，必须证明 `D` 与 `T` 的 complementarity，或 source posterior
在 full operational fiber 中具有 transition-compatible thickness。重新排列 Shannon
chain rule不会做到这一点。

### 3.4 有限深度不能给渐近动态 premium

任意 static cover 可以显式保存短 replacement transcript，从而在
`T=o(n/log n)` 深度保持 static 一阶空间率。因此常数深度 gadget、局部 Johnson
不等式或小规模 LP不能直接张量化成线性 asymptotic theorem。

## 4. 最值得研究的下界对象

先把 deterministic machine 商到 future-response quotient `Q_bar`：两个 states 若对
所有 update continuation 及其后 query 给相同响应，则视为同一 behavior。对 parent
`i` 预先固定一族 tape-independent、此前未访问的 replacement probes `P_i`，定义

\[
T_i(q)=\text{从 }q\text{ 出发在全部 }P_i\text{ 上得到的 response table}.
\]

最小的单-parent命题应是

\[
K_i\le I(X_i;T_i(\bar Q_i)\mid C_i,R,P_i)+L_i+o(m),
\]

其中 `K_i` 是 hard pruning saving，`L_i` 是 probes 因 false positives 或 ALL-YES
branches 产生的精确 list penalty。它通过了 XOR、coordinate erasure、frozen mask
和 cover-and-tombstone 的第一轮压力测试，但尚未证明。

真正困难的是 joint single-budget lemma：能否选择共同 decode order，使

\[
\sum_i I(X_i;T_i(\bar Q_i)\mid C_i,R,P_{1:s})\le H.
\]

若成立，并能用 pointwise FPR 控制 `sum L_i`，就得到新的 asymptotic lower-bound
mechanism。若失败，应构造一个 future-minimal right congruence 反例；这本身也是有
价值的 barrier theorem。

### 更组合化的等价目标

对一条 tape、一个 color `m`，考察所有合法 replacement labels的 successor-support
向量

\[
\bigl(A(Delta_ell(m))\bigr)_ell.
\]

需要证明：一个接近 Carter-optimal 的 thick cell不可能在指数多个 replacement
branches上同时保持小 accepted support，除非 successor colors的数目发生指数膨胀。
这个定理必须满足：

- 在 coordinate erasure 极点上 sharp；
- 允许 reliability 在 public tapes之间作极端分配；
- 使用 `Omega(n/log n)` 深度或指数多个并行 branches；
- 对 multiple representations 和 holonomy 有效；
- 全程只使用一次 width `2^H` budget。

这才是 symmetric transition dual 的渐近版本。有限 `U=4,n=2` 五轨道证书可以提示
需要哪些 orbit，但不能直接 tensorize。

## 5. 构造侧的 taste 判断

### 5.1 四状态 flat-tail 已不是 open breakthrough

已有 flat-tail rigidity theorem：若 load `0,1,2,3` 达到 maximal rejection，且从
load 3 起每层至多四 states，则任意 history-dependent、multiple-representation
infinite transducer 都被强迫为 one-count modulo 4；所以 `rho_c=0` for `c>=4`。

因此“保持 `rho_2=1/4,rho_3=1/8` 再让 `rho_4>0`”已经被关闭。继续枚举四状态
tail没有价值。剩余的真正问题只有：

- 牺牲低层 rejection 换取高层 rejection 的完整 weighted tradeoff；
- non-flat state counts；
- cross-block global quotient。

这些结论仍是 restricted local class，不能作为 arbitrary AMQ 主结果。

### 5.2 Dense random-linear global quotient 大概率是 barrier，不是新上界

固定指数 `q` 的群 quotient满足 `q(e_i-e_j)` 落入 kernel。一旦某 coordinate 的
occupancy 至少 `q`，质量可沿 kernel搬到 query coordinate，minimal query趋于
ALL-YES。若令特征和群大小随 `n` 增长来避免短 kernel relation，则一个 query有指数
多个包含它的 alternative compositions；随机线性 map 要避免这些 collisions，群大小
必须接近全部 composition 数，基本退回 exact enumerative rate。

这值得整理成一个 random-linear quotient no-go theorem，但当前还需严格处理
alternative differences 的依赖、projective directions 与 reachable syndrome count。
除非找到高度结构化、非随机且禁止全局质量搬运的 kernel，否则不应把这条路线当作
最可能的新 construction。

## 6. 可立即形成的上界定理

令 permanent-YES 质量为 `1-alpha`，tracked cells 数为

\[
q=\frac{\alpha n}{\lambda}+o(n),
\]

每个 tracked cell 的 key probability为 `lambda/n`。对固定 current set
`|S|=k<=n`，normal-state rejection为

\[
\alpha(1-\lambda/n)^k,
\]

故最坏点在 `k=n`。极限约束是

\[
\alpha e^{-\lambda}\ge1-\varepsilon.
\]

Poisson multiset entropy的空间率为

\[
R(\alpha,\lambda)=\frac{\alpha}{\lambda}
H_2(\operatorname{Pois}(\lambda)).
\]

消去 `alpha=(1-epsilon)e^lambda` 后，优化

\[
(1-\varepsilon)
\min_{0<\lambda\le-\ln(1-\varepsilon)}
e^\lambda\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda}.
\]

全局唯一 interior minimizer是

\[
\lambda_*=0.439931601244785\ldots,
\qquad
\varepsilon_*=1-e^{-\lambda_*}=0.355919526120782\ldots.
\]

因此 `epsilon=1/2` 时

\[
\alpha=0.776300509451189\ldots,
\qquad
R=2.200611482960522\ldots.
\]

有限 `n` 下使用 `eta_n=1/log n` 的 error margin。两级有限独立 hash、条件
multinomial fixed-slot code、block totals、hash seeds、padding与 scratch space 全部计入
后仍为 `nR+o(n)` 固定预分配空间。对每条 seed-independent、长度至多 `n^c` 的
history，所有 block-time overflow 的概率可压到 `n^{-d}`；进入 sticky ALL-YES 后
依然逐 tape zero-FN，且该概率直接计入 pointwise FPR。

这个 theorem 的主要 nonclaim 是：不覆盖无限或 seed-adaptive histories，也不证明
arbitrary filters 的 matching lower bound。

## 7. 建议的研究组合与判停条件

### Paper A：先完成可交付结果

合并：generalized fingerprint class converse、heavy endpoint、phase theorem、finite
horizon fixed-slot dynamic construction。投稿前必须把与 2026 entropy-array工作的区别
写成 exact coefficient、heterogeneous optimum 与 fixed preallocation quantifiers，而不
声称首次 entropy-code fingerprints。

### Paper B：all-pivot lower bound

只在 two-sigma-field lifting 全部逐行闭合后提交。主叙事应是 full-fiber lifting 与
all-pivot convex hierarchy，不是 `1.6079` 这个小数。若 lifting不能自包含闭合，停止
继续认证更深 `q`。

### 高风险主线：branch-response width theorem

第一阶段只证明单-parent response-table inequality，或给 future-minimal反例。第二阶段
才研究 joint single-budget。以下任一情况触发判停并转向 barrier paper：

- response tables仍能被 XOR/secret-sharing式复用；
- coordinate erasure不能作为 equality case；
- theorem只检查实际 source paths而不检查未访问 branches；
- 证明只适用于 `o(n/log n)` replacement depth；
- 需要 canonical、locality或 history independence。

## 8. 最终判断

好的 taste 不是继续寻找一个看起来更大的常数，而是把问题拆成可验证的三层：

1. 当前 `1.6079` lifting 能否成为无条件 theorem；
2. `2.200611` 是否在明确有限窗口语义下形成最强构造与 class-wide converse；
3. arbitrary ordinary optimum 是否需要一个真正新的 branch-response width invariant。

其中第 2 项最接近完整论文，第 1 项最接近新的 lower-bound paper，第 3 项最可能产生
社区级突破，也最可能以一个严格 barrier theorem结束。Posterior entropy、有限局部
gadget和 flat-tail 枚举已经完成了它们能完成的工作，不应再作为主线。
