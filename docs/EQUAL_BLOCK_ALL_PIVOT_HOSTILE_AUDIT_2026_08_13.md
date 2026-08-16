# Ordinary dynamic AMQ 的 all-pivot 工作：敌对审计与研究前沿

> **2026-08-16 更新。** 本文 Section 2 找到的 two-sigma-field 缺口后来已由
> [Batch perspective 与 prefix-mass lemma](./BATCH_PERSPECTIVE_AND_PREFIX_MASS_LEMMA_2026_08_13.md)
> 的两阶段条件化修复。统一 transport、decoder side information、finite-$b$ 误差和
> 端点放松的最终复核见
> [all-pivot closure audit](./ALL_PIVOT_16079_CLOSURE_AUDIT_2026_08_16.md)。因此
> $1.6079$ 现在可在 $u/n^2\to\infty$、$f(n)/n\to\infty$ 下作为 ordinary 定理引用；
> 本文其余“尚未闭合”的文字保留为历史审计记录。

> 日期：2026-08-13。审计对象主要是
> `EQUAL_BLOCK_ALL_PIVOT_CONVERSE_2026_08_13.md` 及其依赖的 full-fiber
> lifting、batch code 和 KLZ obfuscation interface。本文区分已经严格成立的
> 数值/凸优化层、尚未写成自包含证明的 lifting 层，以及下一步真正值得研究的结构问题。

所有对数以 2 为底。

## 1. 裁决

当前最强声明是：在 ordinary KLZ dynamic approximate-membership 模型中，若

\[
\varepsilon=\frac12,
\qquad \frac{u}{n^2}\to\infty,
\qquad \frac{f(n)}n\to\infty,
\]

则

\[
H>1.6079n-o(n).
\tag{1}
\]

审计结论是：

1. `q=10` 的有限维凸优化和纯有理 dual certificate 是可靠的；两份独立 verifier
   分别严格认证 `C_10>1.6079` 和 `C_10>1.60`。数值优化不是风险所在。
2. all-pivot 的宏观分块 reduction 在获得正确的 full-fiber batch functional 后是
   可成立的。端点正规化和 `10 | b` 目前写得不完整，但都可修补。
3. 第一个实际未闭合点是 prefix-mass lemma 的条件化：当前文字把完整 public side
   information 放入条件场，同时又把随机 partition 的剩余 assignment 当作随机。
   这两个条件不能同时成立。
4. 该问题看起来是可修补的 sigma-field 错位，而不是已知反例。因此最准确的状态不是
   “式 (1) 已完全证明”，也不是“式 (1) 已被推翻”，而是：**conditional theorem，
   尚缺一个自包含的 two-stage conditioning lemma 及其与 batch code 的正式拼接。**

在这项修补完成前，`1.6079n` 不应作为无条件 theorem 引用。

## 2. 第一个断点：不能在同一条件场下既固定 partition 又平均 partition

`BATCH_PERSPECTIVE_AND_PREFIX_MASS_LEMMA_2026_08_13.md` 定义条件场
`P_ell` 时包含了“decoder 在发送 `X_k` 前已有的 public side information”。但 KLZ
协议中 partition

\[
\pi=(U_1,\ldots,U_b)
\]

本身就是 Alice 和 Bob 共享的 public randomness。若 `P_ell` 包含完整 public side
information，则条件于 `P_ell` 后 `U_k` 已经固定，不能再写

\[
\mathbb E[|W(G_\ell)\cap U_k|\mid\mathcal P_\ell]
\le
L_k+\frac{V-L_k}{u-L}|W(G_\ell)|
\tag{2}
\]

并把未暴露元素到 `U_k` 的 assignment 解释为均匀有限总体抽样。于是当前文字尚未
证明 block-local prefix bound

\[
\frac{\mathbb E|W(G_\ell)\cap U_k|}{V}
\le \delta x_\ell+o(4^{-b}).
\tag{3}
\]

式 (3) 是 batch functional 的输入，因此这是 proof chain 中第一个应当修复的点。

### 最小修补：两个不同的 sigma-field

应明确分成两次条件化。

**Partition-removal 条件场。** 定义

\[
\mathcal A_\ell
=\sigma(R,\text{tree shape},\text{cut 前实际执行的 operations 和 labels}),
\tag{4}
\]

并明确不把完整 `pi` 放入 `A_ell`。因为 full fiber 的定义不引用 partition，给定
`A_ell` 后，物理状态、load、time 以及 `W(G_ell)` 都已固定。另一方面，除已暴露
labels 外，剩余 universe 元素到各 blocks 的 assignment 仍具有交换性，故 (2) 可在
`A_ell` 下证明。

**Batch-code 条件场。** 另定义

\[
\mathcal B_\ell
=\sigma(\pi,R,\text{所有在 }X_k\text{ 之前生成且不依赖 }X_k\text{ 的变量}).
\tag{5}
\]

给定 `B_ell` 后，`U_k` 和

\[
G=W(G_\ell)\cap U_k
\]

固定，而 hidden batch `X_k` 仍在 `U_k` 中均匀无放回。这正是 batch perspective
lemma 所需的 hypergeometric 条件。

最后分别在两个条件场下证明相应结论，再取全期望。不能把 (4) 和 (5) 合并成一个
“包含全部 public information”的条件场。

### 修补后仍需逐项证明的内容

修补不是只改一句定义。正式 lemma 至少要写清：

1. `A_ell` 给定后 `W(G_ell)` 的 measurability；
2. 条件于 cut exposure 后，partition completion 的精确有限总体分布；
3. `B_ell` 给定后 `X_k` 与 prefix state 的条件独立性；
4. 从 (2) 的条件估计到 (3) 的全期望估计；
5. 所有误差对 `ell<k<=r` 和所选全部 pivots 一致。

这五项闭合后，当前没有发现阻止 prefix-mass interface 成立的结构性反例。

## 3. 其余可修补问题

### 3.1 Profile 端点

full-fiber construction 实际只给

\[
0\le x_0\le x_1\le\cdots\le x_b\le1,
\tag{6}
\]

而 all-pivot 稿直接写成 `x_0=0,x_b=1`。这不是无条件的“正规化等式”，但可以作为
合法放松：`Phi(a,c)` 对第一变量非降、对第二变量递减。因此把 `x_0` 降到 0、把
`x_b` 升到 1，只会降低每个 pivot functional，仍给有效但更弱的下界。正式证明应
逐类检查 `s=0`、`0<s<b`、`s=b` 的受影响 terms，并在 finite regularizer
`gamma_b` 下重复单调性论证。

### 3.2 Horizon 的量词

“支持 `omega(n)` 次操作”必须解释为：存在确定函数 `f(n)`，`f(n)/n->infinity`，
算法对每条从空集出发、所有 prefix load 不超过 `n`、长度不超过 `f(n)` 的合法更新
序列都满足保证。若只表示“存在一条超线性长序列”，则 lower bound 不成立。

带 exact-time 坐标的 full fiber 应只遍历保证域内的 histories：

\[
W_R(m,t,q)=\bigcup\{S(h):h\text{ 从空集出发且合法},\ |h|=q\le f(n),
\ |S(h)|=t,\ M_R(h)=m\}.
\tag{7}
\]

若 witness history 与真实 prefix 同长度，则拼接同一 suffix 后仍与真实执行同长度，
不需要额外预留两倍 horizon。

### 3.3 参数与整除

令

\[
T_n=\min\{\log_4(u/n^2),\log_4(f(n)/n),\log_4n\}.
\]

为使用十等块，应直接取

\[
b=10\left\lfloor
\frac{\lfloor\sqrt{T_n}/4\rfloor}{10}
\right\rfloor,
\qquad M=4^b.
\tag{8}
\]

此时 `b->infinity`、`10 | b`，且

\[
Q\le\frac{nM^{b+1}}b=o(f(n)).
\tag{9}
\]

所有 DFS prefixes、相关 suffixes 和替代 witness histories 都在同一确定性上界内。

### 3.4 Exact batch code 的正式接口

当前 enumerative identity 的思想正确，但投稿版需要把 code 写成一个单独 lemma。
给定 decoder 已知的 `G,D`，发送 hit pattern、hit values 和 `D` 中的 ordered distinct
miss tuple，总长度为

\[
\log(V)_{\underline m}
+\log\frac{(d)_{\underline Q}}{(V-g)_{\underline Q}}+O(1).
\tag{10}
\]

需要明示在每个 KLZ decode step 中 Bob 确实已经知道相应的 `F_r,G_ell`，因而可以
枚举 partition-free full fibers并知道 `G,D,g,d`；`D` 可以依赖 hidden batch，
但它在该 step 的 parent states 给定后对 decoder 可见。还应使用 prefix-free 或
arithmetic/enumerative coding明确处理随机长度，而不是只写“精确计数给出”。

## 4. 已经可靠的部分

### 4.1 Full-fiber 的基本定义

固定 tape、state、load 和 exact time 后，full-fiber union 不引用 KLZ partition，且

\[
S(h)\subseteq W_R(M_R(h),t,q)\subseteq A_R(M_R(h)).
\tag{11}
\]

第二个 inclusion 只用 zero false negatives，没有使用 history independence、accepted-
set monotonicity、locality 或 canonical state。

### 4.2 Common-suffix transport 的确定性核心

KLZ 的相关 suffix 是 self-contained。它的 deletions 只删除 suffix 自己先前插入的
keys。因此若 endpoint witness `T_x` 不包含 suffix 的任何 insertion label，则替代
witness history可以合法拼接该 suffix，并到达与真实 prefix 相同的 successor physical
state。当前没有发现这一步隐藏使用 monotonicity。

### 4.3 KLZ coupling 的适用对象

Claim 4.7 比较的是完整 operational histories 的条件分布，而不仅是 current key set。
因此带 exact-time 坐标的 functional

\[
\sigma\mapsto |W_R(M_R(\sigma),t(\sigma),|\sigma|)|
\]

可以进入同一 distributional coupling。这里不需要把 `F_k` 与 `G_k` 当成相同 state。

### 4.4 All-pivot convex layer

一旦获得统一的 pivot functional

\[
\frac Hn\ge F_{b,s}(x)-o(1)
\]

并完成端点放松，固定 `q` 的等块 Jensen reduction 是有限维凸问题。`Phi` 的联合凸性、
第一变量单调性和 block-boundary 的 `O(q/b)` 损失均与所用方向一致。

`scripts/verify_ten_block_160_certificate.py` 严格输出

\[
C_{10}\ge1.607987002861718\ldots>1.6079,
\]

独立脚本 `scripts/verify_ten_block_pivot_160_dual.py` 输出更接近驻点的全局下界
`1.607987004845738...>1.60`。两者都使用有理区间和凸性推广，不依赖局部 optimizer。

## 5. 这个工作已经解决了什么，又没有解决什么

如果 Section 2 的 two-stage conditioning 被完整证明，则现有 package 的真实贡献是：

1. 在 ordinary、history-dependent、non-monotone dynamic AMQ 中建立 partition-free
   full-fiber lifting；
2. 给出对任意 hit correlation 有效的 joint batch code；
3. 从 KLZ 的全部 pivots 提取一个可系统加深的凸 converse hierarchy；
4. 在 `epsilon=1/2`、`u/n^2->infinity` 下得到认证常数 `1.6079`。

它没有解决：

1. KLZ 在一般 `u/n->infinity` regime 的 constant-error tight rate；
2. fingerprint filters 是否在 ordinary 模型下最优；
3. 与当前约 `2.349083n` ordinary everlasting upper bound 的大常数缺口；
4. all-pivot 连续极限的严格识别；
5. time-efficient matching construction。

因此这项工作的价值主要来自 lifting/interface，而不是 `1.6079` 这个小数本身。

## 6. Taste 判断：下一步不应继续做什么

继续认证 `C_20,C_50`，或直接猜连续 Bellman 方程，不是当前最好的研究投入。

原因是：

1. finite-pivot hierarchy只记录 full-fiber union 的一阶大小，不记录 posterior
   thickness；即使求出极限，也很可能停在约 `1.7n`，仍远低于 upper bound；
2. hard-union transport 在 `u>>n^2` 的 birthday scale 基本 tight，不能靠更好的
   witness union bound解除；
3. exact-posterior arithmetic code只会恢复 chain rule，单 pivot 不产生新的 dynamic
   premium；
4. 常数个 parents 允许 product-rectangle posterior，普适 two-parent direct-sum 没有
   正 gap。

这些都是方法边界，不是数值精度问题。

## 7. 值得深入的核心问题

### 7.1 Growing-parent transition-compatibility dichotomy

令 `X_1,...,X_s` 是 KLZ hidden batches，`M_final` 是同一个最终 `H`-bit state；各
parent state由 `M_final` 与已解码 side information确定。对第 `i` 个 parent posterior
定义相对于其 union 的 entropy deficit `D_i`，并定义 suffix pruning/rank saving
`K_i`。

单 parent 只能得到

\[
K_i\le D_i+o(n).
\tag{12}
\]

真正需要研究的是：当 parent 数随 `n` 增长且它们必须来自同一 online transition
system 时，能否证明

\[
\sum_i D_i
\le
I(X_{1:s};M_{\rm final}\mid R,\Theta)
+\operatorname{TC}(X_{1:s}\mid M_{\rm final},R,\Theta)
+o(n),
\tag{13}
\]

并进一步由 transition compatibility 强迫一个 `Omega(n)` 的非矩形度/overlap term。

这里不能把“hidden batches 先验独立”误当成结论；product-rectangle fibers会使条件
total correlation 为零。正面定理必须真正使用 growing depth、共同 final state 和
online update compatibility。

### 7.2 一个清晰的可证伪分叉

这个问题应同时沿正反两面推进。

**正面目标。** 证明 growing-parent overlap theorem，使同一 fiber deficit 不能在多个
pivots 中重复支付。若定量足够强，可把 full-fiber theorem 从 `u>>n^2` 推到
`u>>n`，并产生超出 Carter static baseline 的动态下界。

**反面目标。** 构造一个 ordinary right-congruent transducer，其多个 parent
posteriors 近似 product rectangles 或共享 transversal，使 (13) 的额外 gap 为 `o(n)`。
这会证明 posterior-overlap 路线本身不能关闭 KLZ 问题，并把研究重心转到新的
upper-bound congruence。

两种结果都有社区价值：前者给出新的 lower-bound mechanism，后者关闭一条目前看似
最有希望但可能虚假的路线。

### 7.3 为什么这个问题比“继续优化常数”更好

它同时覆盖三个社区真正关心的障碍：

1. ordinary history dependence 允许同一 state 表示许多 operational worlds；
2. non-monotonicity 允许 suffix 破坏 hard union，但这种破坏与 posterior information
   有精确 tradeoff；
3. dynamic lower bound 必须证明信息不能被多个时间切片重复使用，而不是把静态 Carter
   bound重新计算多次。

因此核心对象不是某个特定 Bloom/cuckoo construction，而是 randomized right-
congruence cover 在长 online history 下的非矩形度。这是一个简单、普适且可证伪的
理论问题。

## 8. 建议的论文路线

### Paper A：先把现有结果做成可靠 theorem

最低可接受 package 是：

1. 自包含的 two-stage partition-removal/batch-conditioning lemma；
2. exact-time full-fiber suffix transport lemma；
3. uniform-in-pivot first-moment interface；
4. exact batch enumerative code；
5. all-pivot macro-block hierarchy与 `C_10>1.6079` 证书；
6. 明确声明 `u/n^2->infinity`、universal horizon 和非 tight 性。

若这些部分写得干净，这是一篇有实质技术内容的 lower-bound 论文；卖点应是
partition-free lifting 和 all-pivot hierarchy，而不是宣称解决 constant-error最优率。

### Paper B：真正改变前沿的结果

主定理应采取二选一形式：

1. **Overlap theorem：** 对 growing KLZ parents 证明线性 transition-compatibility
   deficit，并据此在 `u/n->infinity` 下给出新的 arbitrary-filter lower bound；或
2. **Barrier theorem：** 构造满足 ordinary semantics 的 shared-transversal/product-
   posterior transducer，证明任何只使用 parent supports、posterior deficits和共同
   final-state mutual information的方法至多达到某个显式 bound。

前者若常数显著并覆盖一般 universe regime，有 FOCS/SODA 级潜力；后者若抽象得足够
普适，也可能成为一篇有价值的 limitation/barrier paper。

## 9. 立即执行的研究顺序

1. 先形式化 Section 2 的 two-stage sigma-field lemma，并做一个 `b=2` 手工 coupling
   验证；若这一步失败，停止引用 `1.6079`。
2. 把 exact batch code 写成完全独立的 source-coding lemma，逐 pivot检查 decoder
   side information。
3. 将所有 `o(4^{-b})` 写成显式 uniform bounds，再完成端点与 `10 | b` 修补。
4. 冻结现有 constant hierarchy，不再投入更高维数值证书。
5. 对 growing-parent 问题先做反例搜索：product rectangles、shared transversals、
   frozen masks、global coins和有限深度 suffix logging。
6. 只有这些反例都失败后，才尝试证明 transition-induced total correlation 的线性
   下界。

这个顺序把最便宜的 falsification 放在最前面，也把“完成现有论文”和“追求真正突破”
分成两个不会互相污染的目标。
