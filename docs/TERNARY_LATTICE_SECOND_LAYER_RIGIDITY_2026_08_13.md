# Ternary load-preserving lattice quotient 的第二层刚性

> 日期：2026-08-13。状态：第二层分类为解析定理；HNF 搜索只是后续证据。
> 本结果处理任意有限指数子格 (L\le A_2)，允许低层 lossy。它没有完成
> 全部 occupancy layers 的 rate converse。

## 1. 二维格模型

把 ternary composition ((m_0,m_1,m_2)) 在 fixed load 下表示为
((m_1,m_2)\in\mathbb Z^2)。任意 canonical、load-preserving、key-only
summary 都由有限指数子格 (L\le\mathbb Z^2) 给出：

\[
(m_1,m_2)\sim(m_1',m_2')
\iff
(m_1-m_1',m_2-m_2')\in L.
\]

假设三个 singleton symbols 不被合并，否则第一层 rejection 已严格下降，且可
单独视为更小 alphabet 的退化 quotient。令

\[
d_c=|T_c/L|,
\qquad
T_c=\{(x,y)\in\mathbb N^2:x+y\le c\}.
\]

## 2. 第二层五点定理

### Theorem 2.1

对任何上述 quotient，load two 的 state count 与 rejection pair 只能是

\[
\boxed{
(d_2,\rho_2)\in
\left\{
(3,0),
(4,2/9),
(5,8/27),
(5,10/27),
(6,4/9)
\right\}.
}
\tag{1}

所有五种 pair 都可由有限 Abelian quotient 实现。

**证明。** 记三个 group increments 为 (a,b,c)。load-two reachable states
来自六个 unordered pair sums

\[
2a,2b,2c,a+b,a+c,b+c.
\tag{2}
\]

因为 (a,b,c) 两两不同，translation cancellation 给出以下限制。

1. 两个 mixed sums 若共享一个 endpoint，例如 (a+b=a+c)，则 (b=c)，
   不可能。因此 mixed--mixed collision 只能在两条 disjoint edges 间发生；
   三个 vertices 时不存在 disjoint edges，所以三个 mixed sums 两两不同。
2. pure sums 若发生多个 collisions，会由相减与 cancellation 产生进一步
   forced collisions；同理，pure--mixed collision 一旦固定，其在三角形上的
   translates 决定整个 collision component。
3. 因而式 (2) 的 quotient partition，在交换 (a,b,c) 后只能属于五类：
   六项全不同；恰合并一个 pure--pure pair；恰合并一个 pure--mixed pair；
   两个或更多由同一 order relation 强迫的 pure collisions；以及 quotient
   已只有三个 states。

下面直接按 collision class 的 support-union cost 计算 rejection。三个 pure
compositions (2e_i) 的 multinomial probability 各为 (1/9)，三个 mixed
compositions (e_i+e_j) 的 probability 各为 (2/9)。若无 collision，fresh
symbol 缺席的概率为

\[
3\cdot\frac19\cdot\frac23
+3\cdot\frac29\cdot\frac13
=\frac49.
\]

一个 pure--pure merge 把两个 singleton supports 合成 size two，增加 accepted
mass (2/27)，给 (10/27)。一个 pure--mixed merge 若两 supports 相交，
增加 accepted mass (4/27)，给 (8/27)。若 lattice relation 强迫三个
pure compositions 合并，损失为 (2/9)，给 (2/9)。当六项压到三个 reachable states 时，
每个 class 的 support union 覆盖所有与之相容的 symbols，直接给 rejection zero。
这些恰对应式 (1)。

为避免把普通 set partition 错当 lattice partition，需要核对上述 forced-
collision closure。可等价选 (a=0)，把任一 equality 写成

\[
u(b-a)+v(c-a)=0,
\qquad |u|+|v|\le2,
\]

并在 (A_2/L) 中逐项消元；除上述五类外，其余形式 partition 要么强迫
(a=b,b=c) 或 (a=c)，要么 closure 后落入已有类别。证毕。

> 正式投稿版本应把最后的有限消元列成一张 relation table。式 (1) 不依赖
> 数值 HNF 搜索，但当前文字证明仍偏压缩。

## 3. 结构意义

式 (1) 给出真正的 weighted coset-clustering rigidity：第二层不能沿一条连续
space--distortion 曲线移动。尤其：

- 若保留最大的 rejection (4/9)，必须保存全部六个 compositions；
- 把第二层减少一个 state，至少损失 (2/27) rejection；
- 若只剩四个 states，rejection 至多 (2/9)；
- 极强压缩到三个 states 时第二层完全失去拒绝能力。

这比 entropy inequality 和 hazard ceiling 严格更强，因为后两者允许许多式 (1)
之外的 ((d_2,\rho_2))。

## 4. HNF 全格搜索审计

任意 finite-index (L\le\mathbb Z^2) 可写成 Hermite normal form。对每个指数
([\mathbb Z^2:L]\le400) 的全部 HNF，精确枚举：

1. 每层 reachable cosets (T_c/L)；
2. multinomial random walk；
3. minimal one-sided rejection；
4. local-state OGF 与 half-error saddle rate。

搜索到的最佳 genuine ternary quotient 为指数 (12) 的一族，profile

\[
d=(1,3,6,9,11,12,12,\ldots),
\]

\[
\rho=(1,2/3,4/9,22/81,31/243,31/729,0,\ldots),
\]

其 rate 是

\[
R=2.352584133736\ldots.
\]

它仍严格高于 binary (q=3) 的 (2.349083440193\ldots)。

搜索过程中曾出现 (2.20945) 的 apparent counterexample；hostile audit 发现
HNF reduction 对负坐标使用了错误的 quotient/remainder convention，导致 query
inverse step 落入错误 coset。修正后该候选消失。这个失败候选不得引用为构造。

## 5. 尚未闭合的部分

Theorem 2.1 只控制第二层。仅用 geometric hazard

\[
\rho_{c+1}\le\frac23\rho_c
\]

并乐观冻结 (d_c=d_2)，仍会允许不存在于真实 lattice 的低 rate profile。
因此要证明 ternary 全局不优于 binary，至少还需一个多层 extension：短 relation
一旦在 (T_2) 或 (T_3) 产生 collision，其 translates 在全部后续 triangles
(T_c) 中同时造成多少 state saving 与 weighted support-union loss。

准确目标可以表述为：对每个二维有限指数 lattice (L)，由最短非零向量及其
translate packing 推出

\[
\sum_c \pi_\lambda(c)\rho_c
\quad\text{与}\quad
\sum_c d_cz^c
\]

的联合下界。第二层五点定理提供了该多层 stability theorem 的第一个离散基例，
但尚未推出完整 (R\ge2.349083\ldots)。
