# 有限深度 (L_0)-support 方法不能证明动态线性 gap

> 日期：2026-08-13。状态：主定理与证明完整。结论覆盖跨 random tapes 的
> pointwise support matrix、所有 labeled insertion maps、single fixed memory
> budget、global masks 与 ALL-YES mixtures。它给出一个严格 barrier：任何只
> 观察常数个 consecutive insertion layers 的 rectangle covering、nonnegative
> rank、fooling set 或 Johnson-support 方法，最多恢复静态 AMQ 下界，不能证明
> 额外的 (Omega(n)) 动态空间。

## 1. 局部动态模型

固定起始容量 (t) 和深度 (d)。算法在第 (t) 层接收一个已经初始化好的
state，代表任意 (t)-set (S\subseteq U)；随后必须支持最多 (d) 次 fresh
distinct insertions。对每条固定起始集合、固定 inserted suffix 和固定当前
非成员 (z)，要求 pointwise FPR 至多 (\varepsilon)。

这是 ordinary incremental filter 的一个合法局部子问题。每层 partitions 与
所有 labeled insertion maps 必须由同一个 fixed-length state block 实现。

## 2. Static-to-depth-(d) extension theorem

### Theorem 1（exact suffix logging）

设 (\mathcal D_0) 是任意 public-coin static one-sided AMQ，表示任意
(t)-set，使用 (H_0) bits，并满足：对每个固定 (t)-set (S) 与固定
(z\notin S)，

\[
\Pr_R[z\in A_R(E_R(S))]\le\varepsilon.
\tag{1}
\]

则存在 depth-(d) history-dependent insertion transducer，使用

\[
\boxed{
H_d
\le H_0+
\left\lceil
\log_2\sum_{i=0}^d\binom ui
\right\rceil
}
\tag{2}
\]

bits，并具有相同的 zero-FN 与 pointwise FPR (\varepsilon)。它同时满足所有
labeled insertion right-congruence equations。

### 构造

第 (t) 层 state 是

\[
(m_0,\varnothing),
\qquad m_0=E_R(S).
\]

执行 suffix insertions 后，令 (Y\subseteq U) 是 suffix 中已经插入的 key
集合，(|Y|\le d)。state 为

\[
(m_0,Y).
\tag{3}
\]

对 fresh label (x\notin S\cup Y)，transition 定义为

\[
\Delta_x(m_0,Y)=(m_0,Y\cup\{x\}).
\tag{4}
\]

query accepted set 为

\[
A_R(m_0,Y)=A_R(m_0)\cup Y.
\tag{5}
\]

### 正确性

当前真实集合是 (S\cup Y)。由 static one-sidedness，
(S\subseteq A_R(m_0))，而 (Y) 在式 (5) 中被显式接受，故无 false
negative。

固定任意当前非成员 (z\notin S\cup Y)。因为 (z\notin Y)，

\[
z\in A_R(m_0,Y)
\quad\Longleftrightarrow\quad
z\in A_R(m_0).
\]

由 (1)，其概率至多 (\varepsilon)。这里 suffix 可任意依赖固定历史，但在
random tape 之前固定；不需要不同 keys 或不同时间的错误独立。

式 (4) 对每个 physical state 与每个 label 是确定性 map，因此任意两个在第
(t+i) 层碰撞的 histories，继续执行相同合法 insert label 后仍碰撞。也就是
完整的 labeled right congruence，而不只是每层独立 static covering。

状态数至多

\[
2^{H_0}\sum_{i=0}^d\binom ui,
\]

即得 (2)。所有层共享同一个 state block；没有逐层重复收费 (H_0)。

## 3. Depth 2 的明确形式

取 (d=2)，则

\[
H_2
\le H_0+log_2\left(1+u+\binom u2\right)+1
\le H_0+2\log_2u+2.
\tag{6}
\]

因此只要

\[
\log u=o(n),
\tag{7}
\]

depth-2 transition compatibility 的最优空间率与静态率相同到 (o(n))。例如
任何 polynomial universe (u=n^{O(1)}) 都满足 (7)。

更一般地，固定 (d) 时

\[
H_d\le H_0+d\log_2u+O_d(1)=H_0+o(n).
\tag{8}
\]

甚至对增长深度，只要

\[
d\log u=o(n),
\tag{9}
\]

仍不能产生一阶动态 gap。

## 4. Support matrix 表述

对 fixed history (h)、tape (R)、state (m=M_R(h)) 与 key (x)，令

\[
\mathbf A_{h,R,x}
=\mathbf1[x\in W_R(m)],
\tag{10}
\]

其中 (W_R(m)) 是同-state endpoint fiber union。one-sidedness 给

\[
S(h)\subseteq W_R(m)\subseteq A_R(m).
\tag{11}
\]

所以 pointwise FPR 强迫

\[
\mathbb E_R\mathbf A_{h,R,x}\le\varepsilon
\qquad(x\notin S(h)).
\tag{12}
\]

在 Theorem 1 的构造中，第 (t+i) 层 fiber union 恰满足

\[
W_R(m_0,Y)=W_R(m_0,\varnothing)\cup Y.
\tag{13}
\]

因此整个 depth-(d) support tensor 只是一个 static support row 加上可由
state 精确恢复的 (d)-sparse correction。它满足：

- 跨 tapes 的逐 ((h,x)) 边际 (12)；
- 所有 label transitions；
- 任意 global correlation；
- single fixed state budget；
- 每层任意 history dependence。

任何只对该有限 tensor 使用 rectangle covering、nonnegative rank 或 fooling
set 的 universal lower bound，都必须接受这个 extension，因而其值不能超过

\[
H_0+d\log u+O(d).
\tag{14}
\]

优化 (\mathcal D_0) 后，有限深度方法至多得到 static optimum 加
(d\log u+O(d))。

## 5. 覆盖 hostile laws

### 5.1 Global frozen mask

若 static base 的 accepted set 是一个 public frozen mask 加真实 keys，式 (5)
保持同一 mask；所有时间和 keys 的 false positives 可以完全相关。证明不按 key
直和，因此不受影响。

### 5.2 ALL-YES mixture

static base 可在概率 (\theta\le\varepsilon) 的 tapes 上 ALL-YES，在其余 tapes
精确或使用其他 filter。extension 在 ALL-YES branch 仍 ALL-YES，并保留原
pointwise marginal。故任何排除这种全局 mixture 的矩阵假设都不是 ordinary
模型 theorem。

### 5.3 Duplicate physical masks

不同 (Y) 可以产生相同 query mask，也可以因 suffix metadata 而保留不同
physical states。Theorem 1 允许 duplicate masks；因此只计不同 accepted sets
而不计 transition metadata 的 lower bound 不完整。

## 6. 为什么这不反驳真正的动态下界

construction 只支持从已经得到 static encoding 的第 (t) 层开始的 (d) 次
insertions。它没有解释如何从空集在线走过前 (t) 次 insertion 并得到
(m_0=E_R(S))。若要求完整长度 (n) 的 incremental execution，记录整个
suffix 需要约

\[
n\log(u/n)
\]

bits，不再可忽略。

因此 Lovett--Porat 的线性动态 gap 与 KLZ 的长 obfuscation proof 没有被
反驳。真正的 dynamic information 恰来自**深度增长到线性规模的在线压缩**，
不是任意固定 number of adjacent layers 的 transition consistency。

## 7. 研究结论

### 已严格否决

不存在仅使用以下输入便证明额外 (\Omega(n)) 动态 gap 的方法：

1. 三个或任意固定数量 consecutive layers；
2. 每层至多 (2^H) states；
3. 所有 labeled insertion maps；
4. 跨 tapes 的 pointwise (L_0)-support marginals；
5. arbitrary rectangles、global masks 和 ALL-YES mixtures；
6. single (H)-bit budget。

因为 Theorem 1 对任意 static filter 给出满足全部条件的 (H_0+o(n)) extension。

### 正确的下一目标

要证明新动态 gap，depth 必须增长到至少

\[
\Omega(n/\log u)
\]

才可能排除 exact suffix logging。相应数学对象不是 depth-2 matrix，而是长程
online state-merging/direct-product theorem：证明同一个 (H)-bit state 不能在
线性多次 insertion 中持续吸收 fresh key identities，同时保持所有
pointwise support marginals。

这也给 single-budget multi-layer 路线一个明确设计标准：层数必须随 (n)
增长；任何固定五层或十层变分即使数值上给出 (1.16)，若没有额外结构阻止
suffix logging，都不能成为 ordinary dynamic theorem。

