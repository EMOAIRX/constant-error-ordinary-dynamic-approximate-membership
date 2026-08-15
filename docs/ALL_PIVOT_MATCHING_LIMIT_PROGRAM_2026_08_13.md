# All-pivot 层级的 matching-limit 问题

> 日期：2026-08-13。状态：研究中的精确闭环目标。本文只记录严格离散恒等式、
> 候选连续对象与必须补齐的奇异极限步骤；不把形式积分方程写成定理。

固定 half error，并定义

\[
\Phi(a,c)=\left(1-\frac a2\right)\log_2\frac{2-a}{c-a},
\qquad B(a)=\Phi(a,1).
\]

## 1. 真正需要关闭的问题

宏观层级已经给出

\[
C_m=\inf_{0<z_1\le\cdots\le z_m<1}
\max_{0\le r\le m}G_r(z),
\qquad C_{km}\ge C_m.
\]

有限层级的常数证书不能确定 ordinary dynamic AMQ 的 tight rate。下一步有意义的
目标是证明存在一个显式常数 `C_*` 与 profile family，使

\[
\lim_{j\to\infty}C_{2^j}=C_*,
\]

并同时给出：

1. 对所有 profile 的 converse `liminf C_m>=C_*`；
2. 一个显式 recovery profile，证明 `limsup C_m<=C_*`。

这将关闭 all-pivot/full-fiber 方法本身的极限，但仍不自动等于数据结构的最优率。

## 2. 严格的离散相邻等势恒等式

数值最优点上全部 branches 等势。若这一 interior KKT 结构成立，置 `z_0=0`，则
相邻 branches 相等精确等价于

\[
B(z_r)+\sum_{j=r+1}^{m}\Phi(z_r,z_j)
=\sum_{j=r}^{m}\Phi(z_{r-1},z_j),
\qquad 1\le r\le m.
\tag{1}
\]

式 (1) 是后续渐近分析的可靠起点。它保留最近邻项
`Phi(z_(r-1),z_r)`；该项随 mesh 缩小按 `log m` 增长，不能在连续化时直接删除。

令

\[
y_r=1-z_r/2,\qquad y_{m+1}=1/2,
\]

并令 `N=m-r+1`。将式 (1) 指数化可写成精确乘积恒等式

\[
\left[
\frac{y_r^N}{\prod_{j=r+1}^{m+1}(y_r-y_j)}
\right]^{y_r}
=
\left[
\frac{y_{r-1}^N}{\prod_{j=r}^{m}(y_{r-1}-y_j)}
\right]^{y_{r-1}}.
\tag{2}
\]

它显示极限问题本质上是一个带移动端点的离散 logarithmic-potential 平衡，而不是
常规光滑 ODE。

## 3. 候选连续平衡与危险之处

若经验分布弱收敛到密度 `rho`，branch 等势的无歧义候选 tail equation 是

\[
\int_a^1[\Phi(a,c)-B(c)]\rho(c)\,dc=0,
\qquad 0<a<1.
\tag{3}
\]

但式 (3) 目前不是定理。式 (1) 中最近邻 logarithmic singularity 与其余
`1/(c-a)` 型和式可能留下有限 lattice correction。必须直接从式 (2) 做
Euler--Maclaurin/Stirling 型展开，不能先假设普通 Riemann convergence。

即便额外假设 `rho` 连续且具有足够的 logarithmic modulus，形式微分也必须包含
cutoff 边界项：

\[
\begin{aligned}
0={}&(2-a)\int_a^1\frac{\rho(c)-\rho(a)}{c-a}\,dc\\
&-(2-a)\rho(a)\ln\frac{2-a}{1-a}\\
&-\int_a^1\left[\ln\frac{2-a}{c-a}+1\right]\rho(c)\,dc.
\end{aligned}
\tag{4}
\]

漏掉第二行会得到错误方程。正式证明应优先使用 tail form (3) 或离散乘积式 (2)。

## 4. 闭合所需的四个 lemma

1. **Compactness。** 有界 branch energy 强迫端点与 gap 的定量控制，并给经验测度
   的紧性。
2. **Singular liminf。** 对式 (2) 的 logarithmic potential 建立带 diagonal
   correction 的下半连续性。
3. **Uniqueness。** 证明修正后的连续平衡有唯一概率测度，并求出其 rate `C_*`。
4. **Recovery。** 从该测度的 quantiles 构造离散 profile，显式控制最近邻项，得到
   `limsup C_m<=C_*`。

在这四步完成前，`C_32,C_64,...` 只能作为定位证据。继续认证更大的固定 `m`
不会关闭问题。

## 5. 与真正 AMQ tight rate 的边界

即使上述四步全部完成，得到的也是 full-fiber all-pivot converse 的 exact value。
要把它升级为 ordinary AMQ 的 tight theorem，还需要二者之一：

- 构造达到 `C_*` 的 ordinary dynamic filter；
- 证明新的结构定理，说明任意 filter 的状态 fibers 都足以实现 matching converse，
  并将当前 `u/n^2->infinity` transport 条件降到自然的 `u/n->infinity`。

因此本项目的成功判据不是更大的有限小数，而是“matching variational theorem”或
“transport-or-information dichotomy”。
