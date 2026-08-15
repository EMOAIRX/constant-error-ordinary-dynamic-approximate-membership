# Exact global cardinality 不改善固定 binary lattice 的渐近局部失真

> 日期：2026-08-13。状态：fixed-lattice compensation lemma 已证明。它补上
> cross-load classification 的一个重要边界：即使额外用 (O(\log n)) bits 保存
> exact current cardinality，并允许 query 联合读取全部 block states，对每个固定
> binary lattice，最坏容量快照的渐近 rejection 仍与 local minimal rule 相同。
> Section 6 给出 generator/index 随 (n) 发散时的局部极限闭合；Section 7
> 单独处理 inner bias 趋于 0 或 1。两者合起来覆盖任意 bias 序列。

## 1. 为什么 global size 可能有帮助

设 block (j) 保存 binary composition (X_j\in\mathbb N^2) 的 coset

\[
M_j=[X_j]_L,
\qquad L\le\mathbb Z^2.
\tag{1}
\]

若 query 只看 (M_j)，只要 coset 中存在一个包含 query symbol 的 composition，
zero false negatives 就强迫 `YES`。但若还保存

\[
N=\sum_j|X_j|,
\tag{2}
\]

这个 local witness 可能具有不同 load；除非其他 blocks 能作相反 load change，
它不一定与 exact (N) 相容。因此 local ALL-YES 或 local rejection formula
本身不足以处理 global-size side information。

下面证明：对固定 lattice、固定正 inner bias 和线性数量的 blocks，这种额外
辨识只发生在 (o(1)) 概率事件上。

## 2. 模型

固定：

- lattice (L\le\mathbb Z^2)，不随 (n) 改变；
- (p_0,p_1>0)，(p_0+p_1=1)；
- (B=B_n)，且 (n/B\to\lambda\in(0,\infty))。

对任意预先固定的 (n)-element set (S)，公共 hashes 将每个 key 独立送到

\[
(j,i)\in[B]\times\{0,1\}
\]

且概率为 (p_i/B)。于是 (X_j=(X_{j,0},X_{j,1}))。固定非成员 query 的
outer block 记为 (J)，query symbol 记为 (I)。

在 ordinary finite-universe key API 中，还假设

\[
\frac{|U_n|}{n}\to\infty.
\tag{2a}
\]

这是 state-counting 所需的 reachability 条件：abstract label vectors 只有在相应
hash fibers 中确实存在足够多 distinct keys 时才是合法 histories。Section 5.1
给出精确 richness lemma。若直接采用 abstract full-simplex label model，则无需
式 (2a)。

令 (Q_{\rm loc}) 是只根据 (M_J) 的 minimal one-sided rule；令
(Q_{\rm glob}) 是根据

\[
(M_1,\ldots,M_B,N)
\]

的 minimal one-sided rule。显然

\[
Q_{\rm glob}=\mathrm{YES}\Longrightarrow Q_{\rm loc}=\mathrm{YES},
\tag{3}
\]

即 global side information 只能增加 rejection。

## 3. Donor lemma

### Lemma 3.1（单 witness 的补偿）

设目标 block 的真实 composition 为 (x)，且 local rule 接受 symbol (i)。则
存在 (y\in\mathbb N^2)，满足

\[
y_i>0,
\qquad \ell:=y-x\in L.
\tag{4}
\]

写 coordinatewise positive/negative parts

\[
\ell=\ell^+-\ell^-.
\]

若另一个 block 的真实 composition 恰为 (\ell^+)，则把 target 从 (x)
改为 (y=x+\ell)，同时把 donor 从 (\ell^+) 改为 (\ell^-)。两个 local
cosets 都不改变，因为 (\pm\ell\in L)，而总 load change 为

\[
|\ell|_1^{\rm signed}+(|-\ell|)_1^{\rm signed}=0.
\]

这里更直接地写就是

\[
(|y|-|x|)+(|\ell^-|-|\ell^+|)=0.
\tag{5}
\]

因此修改后的 global composition tuple 与 exact (N) 相容且包含 query
symbol，global minimal rule 也必须接受。

若 (\ell=0)，target 本身已经给出同 load witness，无需 donor。

在 abstract composition model 中这已经完成 indistinguishability。对 ordinary
key API，还要把修改后的 counts 实现成 distinct universe keys，并让 query key
本身占据 target 的一个 symbol-(i) 位置。对 fixed witness，所需备用 key 数只是
常数；Lemma 5.3 证明在式 (2a) 下，对所有 fixed witnesses 同时存在这些 fresh
keys。因此后续使用 Lemma 3.1 时都隐含这一 realization event。

### Lemma 3.2（有限 witness 集同时拥有 donors）

固定有限集合 (D\subset\mathbb N^2)。以 (Z_d) 表示 composition 恰为
(d\in D) 的非目标 blocks 数。则存在常数 (c_D>0)，使

\[
\Pr\left[\min_{d\in D}Z_d<c_D B\right]
\le |D|e^{-\Omega(n)}.
\tag{6}
\]

**证明。** 对 fixed (d=(d_0,d_1))，标准 multinomial occupancy 极限给

\[
\frac1B\mathbb E Z_d
\longrightarrow
\pi_d
=e^{-\lambda}\frac{(\lambda p_0)^{d_0}}{d_0!}
\frac{(\lambda p_1)^{d_1}}{d_1!}>0.
\tag{7}
\]

也可直接由有限 (n) multinomial 公式得到。改变一个 member key 的 hash pair
至多改变原、目标两个 blocks 的 indicators，所以 (Z_d) 是 bounded-difference
常数至多 2 的函数。McDiarmid 给

\[
\Pr[Z_d\le \mathbb EZ_d/2]\le e^{-\Omega(n)}.
\tag{8}
\]

对有限 (D) union bound 即得。

删除 query 的目标 block 最多损失一个 donor，不影响线性下界。

## 4. Global-local equivalence theorem

### Theorem 4.1

在 Section 2 的 fixed-lattice 模型中，

\[
\Pr[Q_{\rm loc}=\mathrm{YES},\ Q_{\rm glob}=\mathrm{NO}]=o(1).
\tag{9}
\]

因此 global 与 local minimal rules 的 rejection probabilities 相差 (o(1))。
该结论对每个预先固定的 (S) 和 fixed nonmember 都成立；概率只取公共 hashes。

**证明。** 固定截断 (C)。只有有限多个 target compositions 满足
(|x|\le C)，也只有两个 query symbols。对每个 local-YES pair ((x,i))
任选一个 witness (y(x,i))，令

\[
D_C=\{(y(x,i)-x)^+:|x|\le C,\ i\in\{0,1\}\}.
\tag{10}
\]

这是只依赖于 (L,C) 的有限集合。在 Lemma 3.2 的 high-probability event 上，
每个所需 donor composition 都存在于非目标 block。由 Lemma 3.1，所有
load 至多 (C) 的 local-YES queries 也都是 global-YES。因此

\[
\Pr[Q_{\rm loc}=\mathrm{YES},Q_{\rm glob}=\mathrm{NO}]
\le \Pr[|X_J|>C]+e^{-\Omega(n)}.
\tag{11}
\]

目标 occupancy ( |X_J|\sim\operatorname{Bin}(n,1/B))，在
(n/B\to\lambda) 下 tight，并收敛到 (\operatorname{Pois}(\lambda))。先令
(n\to\infty)，再令 (C\to\infty)，右侧趋于零。

证明不需要 query history independent；这里只固定当前集合并使用 pointwise
public-hash probability，正好匹配 ordinary AMQ 的固定历史量词。

## 5. 对 cross-load binary classification 的推论

对每个固定 (L\le\mathbb Z^2)，额外保存 exact global (N) 只需
(O(\log n)=o(n)) bits，并且不改变 fixed-state 一阶 OGF rate。Theorem 4.1
又说明它不改变最坏容量 (N=n) 时的一阶 query rejection。

因此 corrected binary lattice classification 的 half-error sharp optimum

\[
q=3,\qquad p=\frac12,\qquad
R=2.349083440193141\ldots
\tag{12}
\]

可以从 block-local query 扩展到：

> 每个 block 使用同一个固定 deterministic canonical binary lattice quotient，
> query 可以联合读取全部 block cosets 与 exact global cardinality。

这尤其修复下列潜在反例：

- rank-two quotient 的 local ALL-YES witness 改变 load；
- same-sign rank-one quotient 通过增加两种 symbols 产生 witness；
- coordinate lattice 通过增加 (a) 个被周期化的 symbol 产生 witness；
- oblique lattice 的 support witness 改变 (a-b) 的 load。

在所有情形中，另一个随机 donor block以相反 lattice relation 精确补偿 load。

### 5.1 Ordinary key API 的 fiber-richness lemma

令整个 universe 的 public labels 为独立样本

\[
(g(x),h(x))\in[B]\times\{0,1\},
\qquad\Pr[(j,i)]=p_i/B.
\]

对整数 (C\ge1)，称 block (j) 对 symbol set (T\subseteq\{0,1\}) 是
(C,T)-rich，若每个 (i\in T) 的 fiber

\[
\{x\in U:g(x)=j,h(x)=i\}
\]

至少含 (C) 个 keys。

### Lemma 5.1（linear-density blocks 中几乎全部 rich）

若 (B=\Theta(n))、(|U|/n\to\infty)，并且对 (i\in T) 有
(p_i\ge\eta>0)，则对每个 fixed (C)，以 (1-o(1)) 概率至少

\[
B-o(B)
\tag{12a}
\]

个 blocks 是 ((C,T))-rich。

**证明。** 对 fixed block/symbol，fiber size 是

\[
Y_{j,i}\sim\operatorname{Bin}(|U|,p_i/B),
\qquad
\mathbb EY_{j,i}\ge\eta |U|/B\to\infty.
\]

所以 (\Pr[Y_{j,i}<C]=o(1))，均匀于 (i\in T)。不 rich blocks 数的期望
是 (o(B))；Markov 即给式 (12a)。不需要 union bound 保证每一个 block rich。

### Lemma 5.2（sparse outer blocks 中有 \(\omega(n)\) 个 usable fibers）

若 (B/n\to\infty)、(|U|/n\to\infty) 且某 symbol (i) 的
(p_i\ge\eta>0)，令

\[
M_i=|\{j:\exists x\in U,\ (g(x),h(x))=(j,i)\}|.
\]

则以 (1-o(1)) 概率

\[
M_i=\Omega(\min\{B,p_i|U|\})=\omega(n).
\tag{12b}
\]

**证明。** occupancy 公式给

\[
\mathbb EM_i
=B\left[1-\left(1-\frac{p_i}{B}\right)^{|U|}\right]
=\Theta(\min\{B,p_i|U|\}).
\]

(M_i) 是 (|U|) 个 independent labels 的 1-Lipschitz 函数；bounded
differences 或标准 balls-into-bins concentration 给
(M_i=\Omega(\mathbb EM_i)) whp。式 (2a) 与 (B/n\to\infty) 使右侧为
(\omega(n))。

### Lemma 5.3（fresh-key realization）

固定任意预先选择的 current set (S)、非成员 query (x\notin S)、有限个
block-symbol labels，以及每个 label 所需的 fixed multiplicity。若
(B=\Theta(n))、(|U|/n\to\infty)，且所用 symbols 的 probabilities 一致大于
正常数，则以 (1-o(1)) 概率，每个所需 label 的

\[
U\setminus(S\cup\{x\})
\]

fiber 都含足够多 distinct keys。

**证明。** 对 (U\setminus(S\cup\{x\})) 中的 keys，public labels 仍独立；每个
fixed label 的 fiber mean 至少

\[
\eta\frac{|U|-n-1}{B}\to\infty.
\]

其小于任意 fixed multiplicity 的概率为 (o(1))。对有限 labels union bound。

应用于 Lemma 3.1 时，target 的 symbol-(i) witness 位置先指定为 query key
(x)；只对剩余 (y_i-1) 个 symbol-(i) 位置和其他 coordinates调用 fresh keys。
donor 的新 representative (\ell^-) 同理。这样构造出的 alternative set 与原集合
大小相同、没有重复 key、具有完全相同的全部 lattice cosets与 exact (N)，并且
确实包含 query key，而不只是包含某个同 label 的抽象 symbol。

donor block 本身由 current-set occupancies 选择，可能不是预先固定的 label。
这不造成适应性漏洞：Lemma 3.2 给 (\Theta(B)) 个 candidate donors，而
Lemma 5.1 对 unused universe keys 给出至多 (o(B)) 个不 rich blocks；两者所用
keys 不相交、labels 独立。因此 whp 至少一个 candidate donor 同时拥有实现
(\ell^-)-representative 所需的 fresh fibers。

### 如何修正 OGF 计数

在 Section 6 的 interior-bias truncation 中，只对 Lemma 5.1 给出的

\[
B'=B-o(B)
\]

rich blocks 使用 (A_{\infty,C})。每个 local state 的 minimum-load
representative 每个 coordinate 至多 (C)，故可由这些 blocks 中的 distinct
universe keys 实现。其余 blocks 固定为空。因此 ordinary key histories 真正
包含

\[
[z^{\le n}]A_{\infty,C}(z)^{B'}
\tag{12c}
\]

个状态；因 (B'/n\to B/n)，一阶 saddle rate 不变。

endpoint bias 的 Section 7 只使用 common-symbol unary representatives；对 fixed
(C)，Lemma 5.1 取 (T=\{\mathrm{common}\}) 即可。sparse-block Section 8 不再
虚构全部 (B) 个 fibers，而改用 Lemma 5.2 的 (M_i) 个实际 usable blocks。

这些 richness statements 是对 public tape 的 high-probability events。fixed
worst-case memory 长度 (H_n) 不得随 tape 改变；所以存在典型 rich tapes 时，
同一个 (H_n)-bit state space 必须容纳该 tape 上全部可实现 histories，足以推出
上述计数下界。query/FPR 部分则始终固定任意 current set 与 nonmember，只对
public tape 取概率；没有把 pointwise guarantee 偷换成随机输入平均保证。

如果 (|U|/n) 不发散，上述结论一般不成立：当 (B\gg|U|) 时绝大多数 outer
labels 没有 key preimage，abstract (A^B) 会严重 overcount。此时本文只给
abstract full-simplex label model theorem，不能宣称 ordinary finite-universe
key-API lower bound。

## 6. Growing lattices 的离散局部极限

Theorem 4.1 先固定 (L) 再令 (n\to\infty)。对任意 subgroup 序列
(L_n\le\mathbb Z^2)，逐个枚举整数 vectors 并作 diagonal subsequence，可假设
每个 fixed (d\in\mathbb Z^2) 的 membership 最终稳定。定义

\[
L_\infty=\{d:d\in L_n\text{ eventually}\}.
\tag{13}
\]

它对加法、取负闭合，故仍是 subgroup。对每个 fixed (C)，充分大 (n) 时

\[
L_n\cap[-2C,2C]^2=L_\infty\cap[-2C,2C]^2.
\tag{14}
\]

因此所有负载至多 (C) 的 compositions 在 (L_n) 与 (L_\infty) 下具有完全
相同的 equivalence relation。若

\[
A_{L_n}(z)=\sum_{c\ge0}d_{n,c}z^c,
\qquad
A_{L_\infty}(z)=\sum_{c\ge0}d_{\infty,c}z^c,
\]

则

\[
d_{n,c}=d_{\infty,c},\qquad 0\le c\le C
\tag{15}
\]

最终成立。最小负载是否等于 (c) 只涉及两个负载不超过 (c) 的
representatives，其差落在式 (14) 的 bounded box 内。

这给出完整 compactness trichotomy：

1. (L_\infty=0)：所有 fixed-load layers 最终 exact；
2. (\operatorname{rank}L_\infty=1)：bounded-load local limit 是 fixed
   rank-one quotient，即使每个 (L_n) 可能 rank two；
3. (\operatorname{rank}L_\infty=2)：(L_\infty) 有有限 index；包含它的
   supergroups 只有有限多个，再取 subsequence 可令 (L_n) 本身固定。

### Theorem 6.1（uniform interior-bias closure）

固定 (\eta>0)。允许 (L_n) 任意依赖 (n)，但令 inner bias

\[
p_n\in[\eta,1-\eta],
\]

且 (p_n) 在所取 subsequence 上收敛。若保存全部 block cosets 和 exact global
cardinality，query 可联合读取它们，且 half-error rejection 渐近至少 (1/2)，
则 fixed-state rate 的下极限至少为

\[
2.349083440193141\ldots .
\tag{16}
\]

**证明。** 反设有更低 rate 的序列，取上述局部收敛 subsequence。固定 (C)。
对每个负载至多 (C) 的 (L_\infty)-local-YES pair 选择一个 fixed witness
difference (\ell\in L_\infty)。充分大 (n) 时 (\ell\in L_n)。因为 bias 一致
远离端点，所需 donor composition (\ell^+) 的 block probability 一致为正常数；
Lemma 3.2 的 donor argument 对每个 fixed (C) 仍成立。因此

\[
\limsup_n J_{\rm global}(L_n,p_n,\lambda)
\le J_{\rm local}(L_\infty,p_\infty,\lambda)
+\Pr[\operatorname{Pois}(\lambda)>C].
\tag{17}
\]

令 (C\to\infty)，局部极限也必须有 rejection 至少 (1/2)。

另一方面，式 (15) 说明对 finite polynomial

\[
A_{\infty,C}(z)=\sum_{c=0}^Cd_{\infty,c}z^c,
\]

充分大 (n) 时 (A_{L_n}) 逐系数支配它。由 Lemma 5.1，可以从实际 universe
中选出 (B_n'=B_n-o(B_n)) 个 ((C,\{0,1\}))-rich blocks；以下只在这些
blocks 上变化，其余固定为空。这里必须按整个容量类
(N=0,\ldots,n) 计数：即使 exact (N) 作为单独字段保存，总物理状态数也是各
cardinality slices 之和。每个 local-state tuple 的 minimum-load representatives
给出其中一个 slice，故总状态数不小于
([z^{\le n}]A_{\infty,C}(z)^{B_n'})。由于 (B_n'/n\to1/\lambda)，
positive-coefficient type counting
给 state rate 下界 (\mathcal R_{A_{\infty,C}}(\lambda))。令
(C\to\infty)，由单调收敛得到

\[
\liminf_n R_n\ge\mathcal R_{A_{L_\infty}}(\lambda).
\tag{18}
\]

更形式化地，先取 (C>\lambda+1)，使 truncated polynomial 的 tilted mean 可以
跨过 (\lambda)；固定一个 rational type 逼近其 saddle distribution，multinomial
type class给出对应指数下界。随后让 type approximation误差趋零，再令
(C\to\infty)。这避免把 infinite-series coefficient asymptotic 当作黑箱交换极限。

若 (L_\infty=0)，half-error exact-composition rate 至少
(2.384499842478516\ldots)。rank one 时，corrected classification 分别用
coordinate lower bound、same-sign ALL-YES、或 oblique-to-threshold domination。
rank two 为 ALL-YES。最后 biased-threshold sharp theorem 给式 (16)。

## 7. Vanishing bias endpoint

Theorem 6.1 的 donor proof 在 (p_n\to0) 时不统一，因为含 symbol 1 的 fixed
composition 可能不再出现线性多个。但 endpoint 反而可以用一维 order 完全关闭。

### Lemma 7.1（half rejection 强迫 bounded load）

设 (p_n=\Pr[\text{symbol }1]\to0)，且 (n/B_n\to\lambda) 沿 subsequence
存在于 ((0,\infty])。固定 nonmember 的 query symbol 以概率 (1-o(1)) 为 0，
其目标 block 中 symbol-0 members 数收敛到
(\operatorname{Pois}(\lambda))；若 (\lambda=\infty)，按相同公式理解空概率
趋于零。

只要真实目标 block 含 symbol 0，zero false negatives 就强迫任何 global query
rule 回答 `YES`。因此不依赖 summary 结构，

\[
J_n\le
\Pr[\text{query symbol}=0,\ X_{J,0}=0]
+\Pr[\text{query symbol}=1]
=e^{-\lambda}+o(1).
\tag{19}
\]

若 (\liminf J_n\ge1/2)，必有

\[
\lambda\le\ln2.
\tag{20}
\]

### Lemma 7.2（common increment 的 order 必须发散）

定义

\[
a_n=\min\{a\ge1:(a,0)\in L_n\}\in\mathbb N\cup\{\infty\}.
\tag{21}
\]

若 (a_n) 在某 subsequence 上有界，再取 subsequence 可令 (a_n=a) 固定。
由于 (p_n\to0) 且 (n/B_n\to\lambda>0)，composition 恰为 ((a,0)) 的 blocks
有 (\Theta(B_n)) 个，失败概率 (e^{-\Omega(n)})。

对任意 target composition (x)，把它改为 (x+(a,0)) 会保持 target coset 并使
其包含 common symbol；同时把一个 ((a,0)) donor 改为空，保持 donor coset 与
exact global cardinality。因此除 donor failure 外，每个 common-symbol query 都
必须 `YES`。rare-symbol query 的概率为 (p_n=o(1))，故 (J_n=o(1))，与 half
rejection 矛盾。所以

\[
a_n\to\infty.
\tag{22}
\]

若式 (20) 中 (\lambda=0)，下面的 rate bound只会更大；donor 数论证不需用于
该情形。

### Lemma 7.3（发散 order 强迫 unary state rate）

对 (0\le c<a_n)，cosets

\[
[(c,0)]_{L_n}
\tag{23}
\]

两两不同，否则其差给出小于 (a_n) 的正 x-axis relation。该 coset 的最小逻辑
负载 (w_c) 至多为 (c)。所以对任意 fixed (C) 和充分大 (n)，local
minimal-weight OGF 满足 pointwise

\[
A_{L_n}(z)
\ge\sum_{c=0}^Cz^{w_c}
\ge\sum_{c=0}^Cz^c,
\qquad0<z<1.
\tag{24}
\]

按所有 cardinality slices 的总状态计数，finite-polynomial type bound 后令
(C\to\infty)，得到

\[
\liminf R_n
\ge\mathcal R_{(1-z)^{-1}}(\lambda).
\tag{25}
\]

式 (5)--(6) 的单调性与 (\lambda\le\ln2) 给

\[
\liminf R_n
\ge\mathcal R_{(1-z)^{-1}}(\ln2)
=2.384499842478516\ldots
>2.349083440193141\ldots.
\tag{26}
\]

(p_n\to1) 交换 symbols 后相同。

### Theorem 7.4（arbitrary-bias uniform closure）

在 Theorem 6.1 的模型中删除 interior-bias 假设，允许任意
(p_n\in[0,1])。若 half-error rejection 渐近至少 (1/2)，则仍有

\[
\boxed{\liminf R_n\ge2.349083440193141\ldots.}
\tag{27}
\]

**证明。** 任意反例序列取 subsequence 使 (p_n\to p_\infty)。若
(p_\infty\in(0,1))，选取某个 (\eta>0) 后应用 Theorem 6.1。若端点为 0 或 1，
应用 Lemmas 7.1--7.3，甚至得到严格更强的式 (26)。因此不存在反例 subsequence。

这个结论允许 (L_n) 的 rank、generator、finite index 与 bias 同时随 (n) 改变；
它仍只覆盖每个 block 使用同一个 deterministic canonical binary lattice quotient
并按全部 block cosets 编码的 class，不覆盖 history-dependent representations、
随机 transition kernels 或跨 blocks 的额外 noncanonical quotient。

## 8. Outer block density 也不需要预先固定

前面先取 (n/B_n\to\lambda\in(0,\infty))。对 arbitrary (B_n)，任意
subsequence 又可取 extended-real subsequence

\[
\lambda_n:=n/B_n\to\lambda\in[0,\infty].
\]

两个边界都不能产生低 rate 的 half-error 反例。

### Lemma 8.1（dense-block boundary）

对任意 summary，zero false negatives 给出 universal rejection upper bound：

\[
J_n
\le p_n\left(1-\frac{p_n}{B_n}\right)^n
+(1-p_n)\left(1-\frac{1-p_n}{B_n}\right)^n.
\tag{28}
\]

右侧只是 query symbol 在真实 target block 中缺席的概率；若它真实出现，任何
filter 都必须接受。若 (\lambda_n\to\infty)，则式 (28) 对
(p_n\in[0,1]) 一致趋于零。一个直接界是把 (u=\lambda_np_n) 分成
(u\le\lambda_n/2) 与其对称区域，并使用

\[
p_ne^{-\lambda_np_n}\le\frac1{e\lambda_n},
\]

另一个 common-symbol 项至多 (e^{-\lambda_n/2})；交换 symbols 后覆盖另一半。
因此 half rejection 不可能。

### Lemma 8.2（sparse-block boundary）

若 (\lambda_n\to0) 且 rejection 渐近至少 (1/2)，则 local
OGF 必须至少有一个 empty 之外、最小负载为 1 的 state：

\[
A_{L_n}(z)\succeq1+z.
\tag{29}
\]

**证明。** 取概率较大的 common symbol (i_n)，其概率至少 (1/2)。若
(e_{i_n}\in L_n)，则可从任意包含 symbol (i_n) 的 donor block 删除一个该
symbol，并向 query target 插入它；两个 cosets 与 exact (N) 都不变。因此除
“当前集合没有 common symbol”或 query 本身是另一个 symbol 外，common query
都必须接受。

若 common-symbol probability 严格高于 (1/2+o(1))，这已使 rejection 严格小于
(1/2)。在临界 (p_{i_n}=1/2+o(1)) 中，要达到 half rejection，另一个 symbol
的 singleton 必须与 empty state 不同；否则同一 relocation argument 使两个
query symbols 都接受。故无论哪种情形，half rejection 都强迫至少一个
(e_i\notin L_n)，且该 distinguishable symbol 的概率对充分大 (n) 至少为
(1/3)，即式 (29)。这里 donor key 以 (1-e^{-\Omega(n)}) 概率存在；
outer target 与 donor 重合的概率在 (B_n/n\to\infty) 下为 (o(1))。

由式 (29) 与 Lemma 5.2，选择对应 distinguishable symbol 的
(M_n=\omega(n)) 个实际非空 fibers；每个至少提供一个 distinct universe key。
这些 usable blocks 的 state tuples、容量至多 (n) 的数量至少为

\[
\sum_{k=0}^n{M_n\choose k}.
\tag{30}
\]

因为 (M_n/n\to\infty)，

\[
\frac1n\log_2{M_n\choose n}
\ge\log_2\frac{M_n}{n}
\to\infty.
\tag{31}
\]

这里使用标准不等式 ({M\choose n}\ge(M/n)^n)，并只需充分大 (n) 时
(M_n\ge n)。

所以 sparse-block boundary 的 rate 不只是大于 (2.34908)，而是发散。

式 (30) 仍按所有 cardinality slices 计数；若 exact (N) 被加入状态，各 slices
本来就物理可区分。若从未保存 exact (N)，删除这份 side information只会使
query 更弱；本文的 lower-bound class可以先给原结构附加 (O(\log n)) bits 的
exact (N)，一阶 rate 不变。

### Theorem 8.3（完整的 varying-parameter binary canonical theorem）

假设 ordinary universe 满足 (|U_n|/n\to\infty)，并允许下列全部参数随
(n) 改变：

\[
B_n,\qquad p_n,\qquad L_n\le\mathbb Z^2.
\]

每个 block 使用同一个预先固定、且不依赖 public tape 的 deterministic canonical
binary quotient (L_n)；持久状态
是全部 block cosets，可附加 exact global cardinality；query 可读取全局状态；
updates 是 key-only、任意长且 zero-FN。若对容量至多 (n) 的每条固定历史和
固定非成员保持 FPR 至多 (1/2+o(1))，则 fixed worst-case memory 满足

\[
\boxed{
H_n\ge
2.349083440193141\ldots\,n-o(n).
}
\tag{32}
\]

**证明。** 任取一个假设违反式 (32) 的 subsequence。再取
(\lambda_n=n/B_n) 的 extended-real convergent subsequence。若极限为
(\infty)，Lemma 8.1 排除 half rejection；若为 0，Lemma 8.2 给发散 rate；
若为有限正数，再取 (p_n) 的 convergent subsequence，使用 Theorem 6.1
（interior limit）或 Theorem 7.4（endpoint limit）。三种情形均矛盾。

因此 binary sharp converse 现在同时删除了：

- exact local load；
- fixed lattice 参数；
- fixed inner bias；
- 预设的线性 outer block density；
- query 只能读取目标 block；

但仍保留最关键的结构假设：

- 每个 block summary 是当前 binary multiset 的 deterministic canonical 函数；
- quotient lattice 不能在看到 public tape 的 fiber occupancies 后适应性选择；
- block states 是同一个 lattice quotient 的 product，除 exact (N) 外没有
  cross-block noncanonical compression；
- 不覆盖 history-dependent 或 randomized representations。
