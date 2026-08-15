# Four-state relational binary transducer：饱和前三层后的无限尾刚性

> 日期：2026-08-13。状态：Sections 1--4 是解析定理；Section 5 给出尚未闭合的
> 最小 tradeoff 问题。模型允许 arbitrary history dependence、multiple
> representations、nontransitive fibers 和不可逆 updates，但要求 exact load、
> binary label-oblivious local transitions、每层至多四个 reachable states，以及
> public mixture 与 IID binary labels 独立。

## 1. 精确模型

固定 public seed 后，令 \(Q_c\) 是 load \(c\) 的 reachable physical states，且

\[
|Q_c|\le 4\qquad(c\ge0).
\tag{1}
\]

对 \(b\in\{0,1\}\)，insert/delete maps

\[
I_b:Q_c\to Q_{c+1},\qquad D_b:Q_c\to Q_{c-1}
\tag{2}
\]

只读取当前 local state 与 operation label。它们只需在 hidden composition 中操作
合法时正确；不要求 \(D_bI_b=\mathrm{id}\)。令

\[
R_{c,k}\subseteq Q_c
\tag{3}
\]

为 one-count 为 \(k\) 的所有合法 histories 可到达的 states。同一
\(R_{c,k}\) 可含多个 states，不同 \(R_{c,k}\) 可重叠。

对每条 fixed key history，fresh query label 与 operation labels IID uniform。
one-sidedness 给 load-\(c\) rejection ceiling \(2^{-c}\)。假设每条 load-2 和
load-3 history分别达到

\[
\rho_2=\frac14,\qquad \rho_3=\frac18.
\tag{4}
\]

这里 equality 是逐 fixed history 的 public-coin equality，不是只对某个随机
history distribution 平均。

## 2. Load 3 已被强迫为 exact composition

### Lemma 2.1

在式 (1)--(4) 下，存在恰好四个 states \(q_{3,0},\ldots,q_{3,3}\)，且

\[
\boxed{R_{3,k}=\{q_{3,k}\}\qquad(0\le k\le3).}
\tag{5}
\]

### 证明

先固定一条 deterministic tape。load-2 equality 强迫每个表示 pure-zero
composition 的 state拒绝 query 1，每个表示 pure-one composition 的 state拒绝
query 0；表示 mixed composition 的 state必须接受两种 labels。因此 pure-zero、
mixed、pure-one 三类 state两两不相交。这里不需要 \(|Q_2|\le3\)，允许第四个
state作为额外 representation。

load-3 equality同样强迫表示 \(k=0\) 的每个 state拒绝 1，表示 \(k=3\) 的每个
state拒绝 0。故它们彼此不相交，也不能与 mixed compositions \(k=1,2\) 共享。
而 \(k=1\) 与 \(k=2\) 也不能共享 state：若共享，从共同 state删除一个 label
0 是两边都合法的，determinism 会产生同一个 load-2 successor；但 successors
分别具有 one-count 1 和 2，即 mixed 与 pure-one，上一段已证明它们不能共享。

所以四个 composition fibers两两不相交且均非空。由 \(|Q_3|\le4\)，每个 fiber
恰为一个 singleton，且没有额外 representation，得到式 (5)。

public mixture的处理合法：每条 tape的 rejection都不超过 ceiling；平均取等强迫
几乎每条 tape取等。对可数 fixed histories取 probability-one intersection 后，
上述论证可逐 tape同时执行。\(\square\)

## 3. Load 4 不可能保留 rejection

### Lemma 3.1

在式 (5) 下，load 4 的唯一可能 relational fibers 是 modulo-four classes：

\[
R_{4,0}=R_{4,4}=\{q_{4,0}\},
\qquad
R_{4,k}=\{q_{4,k}\}\quad(1\le k\le3).
\tag{6}
\]

特别地，所有 load-4 states接受两种 query labels，故

\[
\boxed{\rho_4=0.}
\tag{7}
\]

### 证明

若同一 load-4 state兼容不同 one-counts \(k<\ell\)，且这对不是
\(\{0,4\}\)，则两 compositions有一个共同出现的 label。删除该 label后，同一
deterministic transition必须落入两个不同的 load-3 states，与式 (5) 矛盾。
所以唯一允许的 collision pair是 disjoint-support endpoints \(\{0,4\}\)。

五个 compositions由至多四个 states覆盖，因此 endpoints必须共享，三个 mixed
compositions各自占据一个 singleton state。任何 extra representation都会超过四
state budget。endpoint state兼容两种 labels；mixed states本身也兼容两种 labels，
故全部 ALL-YES。共同删除始终合法，因为证明只删除两个 hidden compositions都
实际含有的同一 label。\(\square\)

## 4. 整个 infinite tail 是 modulo four

### Theorem 4.1

对所有 \(c\ge3\)，存在四个 states \(q_{c,0},\ldots,q_{c,3}\)，使

\[
\boxed{R_{c,k}=\{q_{c,k\bmod4}\}\qquad(0\le k\le c).}
\tag{8}
\]

因此 reachable transition system 与 canonical one-count modulo-four quotient
等价，并且

\[
\boxed{\rho_c=0\qquad(c\ge4).}
\tag{9}
\]

### 证明

Sections 2--3 给出 \(c=3,4\)。归纳假设式 (8) 对 \(c-1\ge4\) 成立。mixed
compositions \(k=1,\ldots,c-1\) 包含全部四个 residues。若两个不同 residues
共享 state，共同删除 label 0 后会落入上一层不同 residue states，矛盾。因此
mixed compositions已经占满四个 states，且每个只能位于其 residue state。

对 pure-zero composition删除 label 0；其 successor必须是上一层 residue-zero
state，而四个 top states中只有 mixed residue-zero state具有这个 successor，故
pure zero也位于该 state。对 pure-one composition对称地删除 label 1。归纳完成。
每个 residue state在 \(c\ge4\) 时都兼容一个包含 0 的 composition和一个包含 1
的 composition，故 query必须 ALL-YES。\(\square\)

### Corollary 4.2（half-error rate）

令 \(d_c=|Q_c|\)。式 (4)--(9) 至少强迫

\[
d_c\ge \min(c+1,4),
\qquad
\rho_c\le 2^{-c}\mathbf 1\{c<4\}.
\tag{10}
\]

第一项在 \(c=0,1,2\) 只是非空 composition classes的 one-sided separation，
在 \(c\ge3\) 由前述 rigidity取等。更准确地，load 2 equality把 pure-zero、
mixed、pure-one fibers分开，故 \(d_2\ge3\)；若两个 load-1 compositions共享
state，再共同插入 label 0，就会在 load 2得到 pure-zero/mixed overlap，故
\(d_1\ge2\)。这一步使用 future insertion compatibility，而不只使用 load-1
query语义。若低层存在额外 representations，\(d_c\) 只会更大。因此 local OGF
逐系数不小于

\[
A_4(z)=\frac{1-z^4}{(1-z)^2}.
\]

在 homogeneous Poisson outer-block product及 minimal one-sided query下，逐层
rejection不超过 canonical modulo-four，
故可用平均 load不超过其 root

\[
\lambda_4=1.375441246548\ldots.
\]

fixed-state rate对 OGF逐系数单调、对可用平均 load单调下降，于是

\[
R\ge R_4(1/2)
=2.360295858677\ldots
>2.349083440193\ldots=R_3(1/2).
\tag{11}
\]

所以指定的 four-state saturated-prefix方向不仅没有 positive tail，也不可能在
空间率上击败 canonical modulo-three。

### 与既有 flat-tail theorem 的关系

`FLAT_TAIL_HISTORY_DEPENDENT_RIGIDITY_2026_08_13.md` 的 \(q=4\) 情形已经证明：
若低层 state counts还满足 \(|Q_c|\le c+1\) 且 loads \(0,1,2,3\) 全部饱和，
则结论 (8)--(9) 成立。Theorem 4.1 补的是一个窄但真实的量词差异：这里只假设
每层统一上界四，允许 loads 1、2 有额外 states；load-2/load-3 equality仍足以在
第三层把这些自由度压掉。

## 5. 第一个尚未解决的命题

以上严格否决

\[
\rho_2=\frac14,\qquad
\rho_3=\frac18,\qquad
\rho_4>0
\tag{12}
\]

以及任何更远的 positive tail。它没有解决牺牲低层 rejection 后的 frontier。
最小未证问题可表述为：

> 对每层至多四 states 的 everlasting relational transducer，刻画所有逐 fixed
> history可实现的 public-coin sequence \((\rho_2,\rho_3,\rho_4,\ldots)\)，并证明
> 在 Poisson weights \(a_c=e^{-\lambda}\lambda^c/c!\) 下
> \(\sum_c a_c\rho_c\) 的 sharp upper envelope。

不能把 finite-depth equality points当作答案。一个 load-3/4 endpoint cover即使
满足局部共同删除约束，也可能在重复 insert-delete loops 中累积 ghosts；要成为
构造，必须给出全部 layers上的 transition maps并验证任意长 histories。反过来，
现有 saturated-prefix induction在 \(\rho_2\) 或 \(\rho_3\) 有 slack 时立即失去
singleton predecessor states，也不能证明一个未经验证的全局 tradeoff。

最自然但尚未证明的下一 lemma 是 four-state leave-one-out inequality，例如某个
对所有 fixed four-key histories成立、并在 modulo-four endpoint取等的

\[
\alpha\rho_2+\beta\rho_3+\gamma\rho_4
\le C.
\tag{13}
\]

系数不能从三状态的 \(\rho_2+\rho_3\le1/4\) 直接类推：第四个 state允许新的
nontransitive overlap，原三状态 pigeonhole proof不再成立。必须先证明式 (11)
对 full infinite right congruence有效，再做 OGF/rate优化。

## 6. 论文价值裁决

Theorem 4.1 是可靠的 restricted-class rigidity lemma，但不是独立主结果：核心
机制已被一般 flat-tail theorem覆盖，新增价值只是删除低层最小 state-count假设。
真正可能成为主结果的是 Section 5 的 sharp weighted tradeoff，或一个合法的
nonflat infinite-tail construction。当前没有这样的 theorem或 counterexample，
所以不能声称 four-state方向已经给出优于 canonical mod-3/mod-4 的结果。
