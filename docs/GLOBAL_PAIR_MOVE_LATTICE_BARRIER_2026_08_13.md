# Pair-move global lattices 精确退化为 occupancy filters

> 日期：2026-08-13。状态：结构分类和 half-error asymptotic converse均为解析
> 定理。它覆盖由 relations \(e_i-e_j\) 生成的全部global load-preserving
> lattices，不覆盖higher-support circuits。

## 1. 模型与应用意义

令global fingerprint occupancy为

\[
x\in\mathbb N^M,\qquad |x|\le n,
\]

并保存exact total load与lattice coset \([x]_L\)，其中

\[
L=\langle e_i-e_j:\{i,j\}\in E\rangle_{\mathbb Z}
\le A_{M-1}.
\tag{1}
\]

这种kernel包含最局部、最容易实现的跨coordinate共享：沿graph edge搬运一个
单位质量不改变state。它涵盖hash buckets合并、pairwise equality checks和以
connected regions共享counter的global sketches。

下面证明，这类cross-block耦合没有产生新的filter：它严格退化为在graph
connected components上的ordinary exact-load occupancy filter，并在half error下
至少需要 \(2.384499842479\ldots n-o(n)\) bits。

## 2. Fixed-load fibers 的完整分类

令graph \(([M],E)\) 的connected components为
\(C_1,\ldots,C_r\)，并定义component loads

\[
X_a=\sum_{i\in C_a}x_i.
\tag{2}
\]

### Theorem 2.1（component-load normal form）

对任意 \(x,y\in\mathbb N^M\) 且 \(|x|=|y|\)，

\[
x-y\in L
\iff
\sum_{i\in C_a}x_i=\sum_{i\in C_a}y_i
\quad\forall a\in[r].
\tag{3}

所以quotient state恰好是 \((X_1,\ldots,X_r)\)。minimal one-sided query对
coordinate \(i\in C_a\) 回答

\[
\mathrm{YES}\iff X_a>0.
\tag{4}

**证明。** 每个generator \(e_i-e_j\) 保持每个component的total，给出必要性。
反过来，在一个connected component内，任意zero-sum integer vector都可沿
spanning tree写成edge differences的整数线性组合；逐component相加给充分性。
若 \(X_a>0\)，component内已有某coordinate为正，并可沿path把一个单位搬到
任意 \(i\in C_a\)，故fiber含 \(y_i>0\)。若 \(X_a=0\)，非负性强迫整个component
为零。式 (4)随即由minimal rule得到。\(square\)

### Corollary 2.2（exact state count）

load恰为 \(c\) 的reachable states数为

\[
d_c={c+r-1\choose r-1},
\tag{5}
\]

load至多 \(n\) 的全部states数为

\[
N(n,r)={n+r\choose r}.
\tag{6}

因此fixed worst-case memory满足

\[
H\ge\log_2{n+r\choose r}.
\tag{7}
\]

式 (7) 在 abstract full-simplex coordinate API 中是精确的。对 ordinary
distinct-key API，固定 hash tape 未必使全部 component-load vectors 可达；所以
下文的 asymptotic converse额外假设 \(M=\Theta(n)\) 与 \(|U|/M\to\infty\)，并使用下面的
bounded-richness lift。

### Lemma 2.3（ordinary key API 的 component-richness lift）

固定常数 \(L\)。存在正概率的 fingerprint-map realization，使全部 \(r\) 个
非空 components 中除 \(o(n)\) 个外，每个都含至少 \(L\) 个 distinct universe
keys。于是所有

\[
y\in\{0,\ldots,L\}^{r-o(n)},\qquad |y|\le n,
\tag{7a}
\]

都是可达 component-load states，故

\[
H\ge
\log_2[z^{\le n}](1+z+\cdots+z^L)^{r-o(n)}.
\tag{7b}
\]

**证明。** 每个非空 component 至少含一个 fingerprint coordinate，所以质量
\(w_a\ge1/M\)。它所含 universe keys数为
\(\operatorname{Bin}(|U|,w_a)\)，其均值至少 \(|U|/M\to\infty\)。
所以它少于 \(L\) 个 keys 的概率为 \(o(1)\)。坏 components数的期望为
\(o(n)\)，Markov给所需 realization。每个 rich component独立提供 \(L\) 个
distinct keys，从而实现式 (7a)。fixed memory必须覆盖这张正概率 tape，得到
式 (7b)。\(\square\)

对固定 \(L\)，令 \(n\to\infty\)，再令 \(L\to\infty\)，式 (7b) 的 saddle
exponent单调收敛到 stars-and-bars rate。

## 3. Rejection 的 sharp optimization

令public fingerprint coordinate均匀于 \([M]\)。component \(C_a\) 的mass为

\[
w_a=|C_a|/M,\qquad \sum_aw_a=1.
\tag{8}

对 \(n\) 个fixed members和fixed nonmember，Theorem 2.1给exact rejection

\[
D_n(w)=\sum_{a=1}^r w_a(1-w_a)^n.
\tag{9}

令 \(r/n\to\beta\)。写 \(t_a=nw_a\)，则

\[
D_n(w)=\frac1n\sum_a t_a(1-t_a/n)^n.
\tag{10}

### Lemma 3.1（asymptotic concave envelope）

若 \(r\le n+1\)，则先放松为 \(\sum_aw_a\le1\)，并逐项使用
\(w(1-w)^n\) 在 \(w=1/(n+1)\) 的全局最大值，得到

\[
\max_{w\in\Delta_{r-1}}D_n(w)
\le\frac r{n+1}\left(\frac n{n+1}\right)^n.
\tag{10a}
\]

若 \(\beta>1\)，则

\[
\limsup_{n\to\infty}\max_{w\in\Delta_{r-1}}D_n(w)
\le e^{-1/\beta}.
\tag{11}

equal component masses \(w_a=1/r\)达到等号，所以式 (11) sharp。

**证明。** 定义 \(g(t)=te^{-t}\)，以及

\[
h(t)=
\begin{cases}
te^{-t},&0\le t\le1,\\
e^{-1},&t\ge1.
\end{cases}
\tag{12}
\]

由于 \(g''(t)=(t-2)e^{-t}\le0\) 在 \([0,1]\) 上成立，且
\(g'(1)=0\)，\(h\) 是concave majorant of \(g\)。标准uniform truncation处理
\((1-t/n)^n\le e^{-t}\) 与可能的large \(t\)，于是Jensen给

\[
\limsup D_n
\le \beta h(1/\beta)
=e^{-1/\beta},
\]

其中 \(1/\beta<1\)。uniform weights直接给
\((1-1/r)^n\to e^{-1/\beta}\)。\(\square\)

这里concave envelope很重要：函数 \(te^{-t}\) 在整个正半轴并不concave，不能
未经处理直接使用Jensen。

## 4. Half-error barrier

若FPR至多 \(1/2\)，rejection至少 \(1/2\)。式 (10a) 排除
\(r/n\le1+o(1)\)，因为其右侧至多 (e^{-1}+o(1)<1/2)。所以只需考虑
\(r/n\to\beta>1\) 的 subsequences；由Lemma 3.1，

\[
e^{-1/\beta}\ge\frac12,
\qquad
\beta\ge\frac1{\ln2}.
\tag{13}

而

\[
\frac1n\log_2{n+\beta n\choose\beta n}
\longrightarrow
s(\beta):=(1+\beta)\log_2(1+\beta)-\beta\log_2\beta,
\tag{14}
\]

且 \(s\) 严格递增。因此：

### Theorem 4.1（pair-move half-error converse）

在 \(M=\Theta(n)\)、\(|U|/M\to\infty\) 下，任意由未缩放 unit relations \(e_i-e_j\) 生成的
pair-move global lattice filter若满足zero false negatives、pointwise
FPR至多 \(1/2\) 和fixed worst-case memory，则

\[
\boxed{
H\ge s(1/\ln2)n-o(n)
=2.384499842479\ldots n-o(n).
}
\tag{15}

equal-size connected components以普通occupancy query达到这个class内的
rejection/state tradeoff，因此常数对该restricted class是sharp的。

## 5. 研究裁决

unit pair moves不是击败 \(2.349083440193n\) 的机制。它们把coordinates收缩成
supercoordinates，却没有保留任何component内部support信息；为了达到half
rejection，supercoordinates数量被迫回到 \(n/\ln2\)，状态数正是完整weak
composition benchmark。

结合random-linear barrier，当前cross-block additive路线的两端都已关闭：

- 大量short pair relations：退化为supercoordinate occupancies；
- 无结构的random long relations：constant rejection迫使near-injective simplex
  image。

本文不覆盖 scaled relations \(q(e_i-e_j)\)、\(q>1\)：它们还保留 component
内部 residues，不能归约为单一 component load。唯一尚未覆盖且真正可能有新意的
中间区间，包括这类 scaled pair relations，以及由bounded-support
\(3\)-way或更高circuits生成、但不含 unit pair moves的designed lattices。下一步需要
研究其circuit hypergraph如何同时控制reachable-state saving与fiber support-union
膨胀；不能把pair-move定理或random-matrix定理直接外推到这个区间。
