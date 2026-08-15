# Three-pivot convex converse 的精确 primal--dual 定理

> 日期：2026-08-13。状态：完全解析，不依赖数值 optimizer、网格或 interval
> verifier。本文精确刻画 two-block/three-pivot 常数及唯一等号结构；不声称把该
> 方法推广到了 four-block 或连续 all-pivot 极限。

所有对数以 2 为底。定义

\[
A(x)=\log\frac2x,
\qquad
B(x)=\left(1-\frac x2\right)\log\frac{2-x}{1-x},
\]

以及

\[
\Phi(a,c)=\left(1-\frac a2\right)
\log\frac{2-a}{c-a},\qquad 0<a<c<1.
\]

three-pivot constant 是

\[
C_3=\inf_{0<p<q<1}\max\{f_0(p,q),f_1(p,q),f_2(p,q)\},
\tag{1}
\]

其中

\[
f_0=\frac{A(p)+A(q)}2,
\quad
f_1=\frac{B(p)+\Phi(p,q)}2,
\quad
f_2=\frac{B(p)+B(q)}2.
\tag{2}
\]

## Theorem

存在唯一一对 ((p_*,q_*)\)、(0<p_*<q_*<1)，满足

\[
\boxed{
B(q_*)=\Phi(p_*,q_*),
\qquad
A(p_*)+A(q_*)=B(p_*)+B(q_*).
}
\tag{3}
\]

而且 ((p_*,q_*)\) 是式 (1) 的唯一 minimizer，三个 branches全部等势，

\[
\boxed{
C_3=f_0(p_*,q_*)=f_1(p_*,q_*)=f_2(p_*,q_*).
}
\tag{4}
\]

此外，存在唯一的正权向量

\[
(\lambda_0,\lambda_1,\lambda_2)\in(0,1)^3,
\qquad\sum_i\lambda_i=1,
\tag{5}
\]

使

\[
\lambda_0\nabla f_0(p_*,q_*)
+\lambda_1\nabla f_1(p_*,q_*)
+\lambda_2\nabla f_2(p_*,q_*)=0.
\tag{6}
\]

式 (3)、(5)、(6) 是 matching analytic primal--dual certificate；它完全定义
(C_3)，无需给出其十进制展开。

## Proof

令

\[
H(x)=A(x)-B(x).
\]

(A) 严格递减，(B) 严格递增，故 (H) 严格递减；又
(H(0+)=+\infty\)、(H(1-)=-\infty\)。因此存在唯一 (x_0\in(0,1))
满足 (H(x_0)=0)。

固定 (p\in(0,1))，考虑

\[
K_p(q)=\Phi(p,q)-B(q),\qquad p<q<1.
\]

当 (q\downarrow p) 时，(K_p(q)\to+\infty)；当 (q\uparrow1) 时，
(\Phi(p,q)\to B(p)<\infty\)，而 (B(q)\to+\infty)，所以
(K_p(q)\to-\infty\)。又

\[
\partial_qK_p(q)=\partial_c\Phi(p,q)-B'(q)<0.
\]

故存在唯一 (q=Q(p)\in(p,1)) 满足

\[
B(Q(p))=\Phi(p,Q(p)).
\tag{7}
\]

由于 (partial_p\Phi\ge0)，隐函数单调性给 (Q'(p)\ge0)。定义

\[
D(p)=H(p)+H(Q(p)).
\]

(H) 严格递减且 (Q) 非降，所以 (D) 严格递减。当 (p\downarrow0) 时，
式 (7) 的极限是 (A(Q(0+))=B(Q(0+)))，故 (Q(0+)=x_0)，从而
(D(p)\to+\infty)。另一方面，(Q(x_0)>x_0)，故

\[
D(x_0)=H(x_0)+H(Q(x_0))<0.
\]

所以存在唯一 (p_*\in(0,x_0)) 满足 (D(p_*)=0)。置
(q_*=Q(p_*))。这证明式 (3) 的存在唯一性；并且
(p_*<x_0<q_*)。式 (3) 立即给三个 branches等势。

下面构造正 dual。记 (g_i=\nabla f_i(p_*,q_*)\)。由导数符号，

\[
g_0\in(-\infty,0)^2,
\qquad
g_1\in(0,\infty)\times(-\infty,0),
\qquad
g_2\in(0,\infty)^2.
\tag{8}
\]

并且

\[
\frac{(g_0)_2}{(g_0)_1}=\frac{p_*}{q_*}<1,
\qquad
\frac{(g_2)_2}{(g_2)_1}
=\frac{B'(q_*)}{B'(p_*)}>1,
\tag{9}
\]

因为 (A'(x)=-1/(x\ln2))，而严格凸函数 (B) 的导数严格增加。
式 (9) 说明由 (g_0) 和 (g_2) 的正锥包含整个开西北象限：当正系数之比
连续变化时，所得向量方向从负水平轴连续扫到正竖直轴。由式 (8)，
(-g_1) 位于该象限。因此存在唯一 (alpha,\beta>0) 使

\[
\alpha g_0+\beta g_2=-g_1.
\]

归一化 ((\alpha,1,\beta)) 即得式 (5)--(6)。

最后令

\[
L=\lambda_0f_0+\lambda_1f_1+\lambda_2f_2.
\]

三个 (f_i) 都是凸函数，而 (lambda_0>0) 且 (f_0) 严格凸，所以
(L) 严格凸。式 (6) 表明 ((p_*,q_*)) 是 (L) 的唯一全局 minimizer。
对任意 (0<p<q<1)，

\[
\max_i f_i(p,q)
\ge L(p,q)
\ge L(p_*,q_*)
=C_3.
\]

而 ((p_*,q_*)) 处三个 branches均等于 (C_3)，故达到下界。若另一点也
达到 (C_3)，上述两重不等式都必须取等，特别地 (L) 也在该点取最小值，
与严格凸性矛盾。这证明唯一性。\(\square\)

## 边界

该定理给出了一个真正的 exact finite-level optimum，但 (C_3<3/2)，所以它
不能替代 four-block 的 (>3/2) 目标。four-block 的五个相邻等势方程形成耦合的
离散 logarithmic-potential system；目前尚未证明其唯一解、全部正 dual weights
或无数值的 closed form。连续 all-pivot 极限还额外包含 diagonal logarithmic
correction，因此也不能从本定理直接连续化。
