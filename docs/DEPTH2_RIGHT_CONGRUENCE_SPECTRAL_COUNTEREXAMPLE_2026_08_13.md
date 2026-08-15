# Depth-2 right congruence 不强迫低阶 Johnson 谱泄漏

> 日期：2026-08-13。状态：定理与证明完整。本文给出一个严格反例：仅由
> single (H)-bit budget、三层 labeled insertion maps 和 right congruence，
> 不能推出任何正的 degree-1/2 posterior spectral leakage。反例不是一个
> (arepsilon<1) 的 AMQ，因为其 fiber union 为全宇宙；这精确说明后续定理
> 必须把 one-sided accepted-support/FPR 纳入假设，不能只研究 transition
> partitions。

## 1. 三层 right-congruence 模型

对 (j\in\{t,t+1,t+2\})，令

\[
\Omega_j=\binom Uj,
\qquad |U|=u.
\]

一个 depth-2 insertion congruence 包含：

- 每层的 state map (f_j:\Omega_j\to[K])；
- 对每个 label (x\in U) 的确定性 transition
  (\Delta_x:[K]\to[K])；
- 对每个 (S\in\Omega_j)、(x\notin S)，
  \[
  f_{j+1}(S\cup\{x\})=\Delta_x(f_j(S)).
  \tag{1}
  \]

式 (1) 比仅仅给三层 partitions 更强：它要求所有合法 labeled insertion
maps 同时由同一个有限状态 transducer 实现。它正是 insertion-only ordinary
history-dependent API 在这三层上的 right-congruence 条件；history-independent
构造是该模型的合法子类。

给定 state (m\)，令 posterior (P_{j,m}) 是均匀随机
(S\in\Omega_j) 条件于 (f_j(S)=m) 的分布。degree-1/2 leakage 可由

\[
p_x^{(j,m)}=\Pr_{P_{j,m}}[x\in S],
\qquad
p_{xy}^{(j,m)}=\Pr_{P_{j,m}}[x,y\in S]
\tag{2}
\]

相对 uniform-slice values (j/u) 与 (j(j-1)/(u(u-1))) 的偏差刻画。

## 2. 主反例

### Theorem 1（transition-compatible approximate 2-design fibers）

固定常数 (\eta>0)，令

\[
H=\lceil\eta n\rceil,
\qquad K=2^H,
\]

并设 (t\in[\alpha n,n-2])，其中 (\alpha>0) 固定。若

\[
\frac un\to\infty,
\tag{3}
\]

则对充分大的 (n)，存在一个 (H)-bit history-independent insertion
transducer，使：

1. 三层 (t,t+1,t+2) 满足 (1)；
2. 每层每个 state 都非空；
3. 对所有 (j\in\{t,t+1,t+2\})、(m\in\{0,1\}^H)、distinct
   (x,y\in U)，一致地有
   \[
   p_x^{(j,m)}=\frac ju+o(1/u),
   \tag{4}
   \]
   \[
   p_{xy}^{(j,m)}
   =\frac{j(j-1)}{u(u-1)}+o(1/u^2).
   \tag{5}
   \]

特别地，任意只依赖 degree at most (2) Johnson components 的 normalized
leakage functional 都趋于零，尽管 state entropy 可以达到
(H=\eta n+O(1)) 且所有 transitions 共用同一 (H)-bit budget。

### 构造

独立均匀选择 columns

\[
a_x\in\mathbb F_2^H,
\qquad x\in U.
\tag{6}
\]

定义

\[
f_j(S)=\bigoplus_{x\in S}a_x.
\tag{7}
\]

插入 (x) 时执行

\[
\Delta_x(m)=m\oplus a_x.
\tag{8}
\]

所以 (1) 对所有 layers、states 和合法 labels 精确成立。

## 3. 二阶矩证明

固定一层 (j)、一个 syndrome (m) 和一个 prescribed set
(B\subseteq U)，其中 (|B|=b\in\{0,1,2\})。令

\[
N_{j,m}(B)
=|\{S\in\Omega_j:B\subseteq S,\ f_j(S)=m\}|.
\tag{9}
\]

其期望为

\[
\mu_{j,b}
=2^{-H}\binom{u-b}{j-b}.
\tag{10}
\]

### Lemma 2（pairwise independence）

对两个 distinct nonempty sets (S,T\subseteq U)，随机变量
(f(S),f(T)\in\mathbb F_2^H) 相互独立且各自均匀。

证明。对每个 output coordinate，(f(S),f(T)) 是随机 column bits 的两个
非零线性型。由于在 (mathbb F_2) 上两个不同非零 indicator vectors 线性
无关，这两个线性型联合均匀；不同 output coordinates 独立。

因此 (9) 中的 indicators pairwise independent，并有

\[
\operatorname{Var}N_{j,m}(B)\le\mu_{j,b}.
\tag{11}
\]

取

\[
\zeta_n=
\left(
\frac{K^2u^2}{\min_{j\in\{t,t+1,t+2\}}
\binom{u-2}{j-2}}
\right)^{1/4}.
\tag{12}
\]

由 (u/n\to\infty)、(j\ge\alpha n) 和 (K=2^{O(n)})，

\[
\log\binom{u-2}{j-2}
=\Omega(n\log(u/n)),
\]

故 (\zeta_n=o(1))。Chebyshev inequality 与 union bound（对三层、(K)
个 syndromes、至多 (1+u+u^2) 个 (B)）给总失败概率至多

\[
O\left(
Ku^2\cdot
\frac1{\zeta_n^2\min\mu_{j,2}}
\right)
=O\left(
\frac{K^2u^2}
{\zeta_n^2\min\binom{u-2}{j-2}}
\right)
=O(\zeta_n^2)=o(1).
\tag{13}
\]

事实上，对每个固定常数 (d)，同一个估计还给

\[
n^d\zeta_n=o(1).
\tag{13a}
\]

这是因为
(\log\binom{u-d}{j-d}=\Omega(n\log(u/n)))，而
(\log K=O(n))；当 (u/n\to\infty) 时，前者压过任意
(O(n)+O_d(\log u)+O_d(\log n)) 项。

因此存在 columns 的 realization，使同时对所有 (j,m,B)，

\[
N_{j,m}(B)
=\mu_{j,|B|}(1\pm\zeta_n).
\tag{14}
\]

取 (B=\varnothing\) 可知每个 fiber 非空。再分别取 (B=\{x\}) 与
(B=\{x,y\})，用 (14) 的比值得

\[
p_x^{(j,m)}
=\frac{N_{j,m}(\{x\})}{N_{j,m}(\varnothing)}
=\frac{\binom{u-1}{j-1}}{\binom uj}(1+O(\zeta_n))
=\frac ju(1+O(\zeta_n)),
\tag{15}
\]

\[
p_{xy}^{(j,m)}
=\frac{j(j-1)}{u(u-1)}(1+O(\zeta_n)).
\tag{16}
\]

由 (13a)，(j\zeta_n=o(1)) 与 (j^2\zeta_n=o(1))。因此 (15)--(16)
分别给 additive (o(1/u)) 与 (o(1/u^2))，即得 theorem。

## 4. 更强的固定 degree 版本

同一证明对任意固定 (d) 成立。只需对所有
(B\subseteq U, |B|\le d) 做 union bound，并用

\[
\binom{u-d}{j-d}
\]

替代 (12) 的分母。于是：

### Corollary 3

对每个固定 (d)，可令同一个 (H=\eta n)-bit additive transducer 的
每个 fiber 在三层上同时成为 approximate (d)-design。故任何固定-depth、
固定-degree Johnson spectral inequality，都不能仅从 transition congruence 与
state budget 推出非零 leakage。

## 5. 为什么这不是 AMQ 反例

由 (14)--(15)，每个 fiber 的每个 coordinate section 非空。因此

\[
\bigcup_{S:f_j(S)=m}S=U
\tag{17}
\]

对每个 (j,m) 成立。one-sided query semantics 迫使该 state 的 accepted set
包含 (U)，即只能回答 ALL-YES。因此这个 transducer 的 FPR 为 (1)，不是
一个 (arepsilon<1) AMQ。

这不是缺陷，而是 theorem boundary：低阶 posterior moments 与 support union
是完全不同的量。一个 fiber 可以是极好的 approximate design，同时每个 key
都以极小但正的 posterior mass 出现；one-sidedness 对“正 support”收费，而
degree-(d) spectrum 只看质量。

## 6. 加入 pointwise FPR 后仍不能逐 tape 推谱泄漏

还可把上述 transducer 放进一个合法 public-coin AMQ 的 ALL-YES branch：以
概率 (\theta\le\varepsilon) 使用 syndrome/ALL-YES branch，以剩余概率使用
任意 zero-error exact dictionary，并把两种状态 padding 到相同 fixed length。
这对每条固定历史和固定非成员的 FPR 至多 (\theta)，支持普通合法
insert/delete；但在正概率 tapes 上仍有 Theorem 1 的零低阶泄漏。

这个混合结构的 exact branch 在大宇宙下空间很大，所以它不反驳目标的
(O(n))-bit AMQ lower bound。它严格反驳的是任何逐 tape 断言：

> pointwise FPR 加 right congruence 迫使每一条 tape 或每个 reachable fiber
> 出现低阶谱泄漏。

正确 theorem 必须对 random tapes 联合平均，并显式使用 accepted-support
事件的概率，而不是先固定 tape 再对 posterior 做 smooth entropy 分析。

## 7. 对 single-budget multi-layer 路线的结论

### 已否决的 theorem 形状

以下任一种假设集合都不足以给新下界：

1. 每层 partitions 至多 (2^H)；
2. 所有层只共享一次 (H)-bit state budget；
3. 每个 labeled insertion 由确定性 map (\Delta_x) 实现；
4. 观察任意固定数量相邻 layers；
5. 只测量固定 degree 的 Johnson posterior spectrum。

Theorem 1 同时满足 1--4，却让 5 的 leakage 任意小。

### 仍可能成立的 theorem 形状

必须联合一个非平滑 support quantity，例如

\[
\Pr_R[x\in W(M_R(h))]\le\varepsilon
\tag{18}
\]

对每条 fixed history (h) 和 fixed nonmember (x)，并把它与 consecutive
transition fibers 一起收费。因为 (18) 是 support-level (L_0) 约束，不能由
(L_2) mutual information、pair correlations 或有限 degree spectrum 逼近。

一个可能的正确对象是跨 tapes 的 weighted support profile

\[
\sum_R\pi_R
\mathbf 1[p_{R,m}(x)>0],
\tag{19}
\]

而不是

\[
\sum_R\pi_R p_{R,m}(x)
\quad\text{或}\quad
I(S;M_R).
\]

## 8. Paper taste

这个反例有独立 insight：它把 dynamic automata 的 right congruence 与
Johnson association scheme 的 posterior spectrum 精确分离，并说明 AMQ
下界为何是 support-sensitive 而不是普通 entropy contraction 问题。

但单独仍更适合作为一篇主论文的 barrier theorem，而非 SODA headline：

- 构造是标准 additive syndrome；
- 核心创新是识别“transition-compatible approximate designs”这一反例接口；
- 它没有给出更强 AMQ lower bound。

若后续能证明一个跨 tapes 的 (L_0)-support leakage theorem，Theorem 1 将是
必要且有说服力的 sharpness/barrier section。若没有该正面 theorem，仅报告
这个 counterexample 更像研究路线清理，而不是完整突破。
