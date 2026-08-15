# KLZ all-pivot profile minimax：三 pivot 的严格改进与连续前沿

> 日期：2026-08-13。状态：本文严格定义 finite-`b` all-pivot minimax，并证明
> 只使用三个 pivots 已经把 endpoint 常数严格提高到一个二维凸变分常数
> `C_3>C_end`。`C_3=1.485506...` 与完整 finite-`b` 数值只是定位证据；定理
> 表述使用闭式变分和凸 dual，不依赖浮点数。完整 all-pivot 连续极限尚未解析
> 求解。

所有 logarithms 以 2 为底。本文件只研究已经由 full-fiber batch theorem给出的
profile functional，不重复其数据结构 lifting。

## 1. Finite-`b` 精确 minimax

固定 `delta in (0,1/2]`，定义

\[
\Phi_\delta(a,c)
=(1-\delta a)
\log\frac{1-\delta a}{\delta(c-a)},
\qquad 0\le a<c\le1.
\tag{1}
\]

当 `a=c` 时取下半连续延拓 `+infinity`。正式 filter proof使用
`c-a+gamma_b`，其中 `gamma_b=O(4^-b)`；先对每个 finite `b` 优化，再令
`gamma_b->0`，得到式 (1)。

令

\[
0=x_0\le x_1\le\cdots\le x_b=1.
\tag{2}
\]

端点归一化没有损失：`x_0` 减小会降低所有 right intervals 的左端，并由
`partial_a Phi>=0` 使 pivot `0` 更困难；`x_b` 增大会由
`partial_c Phi<0` 使 pivot `b` 更困难。故 infimum 可在式 (2) 的端点取得。

对 pivot `s in {0,...,b}`，KLZ decode order给

\[
F_{b,s}(x)
=\frac1b\left[
\sum_{k=1}^{s}\Phi_\delta(x_{k-1},x_b)
+\sum_{k=s+1}^{b}\Phi_\delta(x_s,x_k)
\right].
\tag{3}
\]

完整离散变分是

\[
\boxed{
C_b(\delta)
=\inf_{x\text{ satisfies }(2)}
\max_{0\le s\le b}F_{b,s}(x).
}
\tag{4}
\]

因此已证 batch theorem实际给

\[
H/n\ge C_b(\delta)-o_b(1)-o_n(1)
\tag{5}
\]

对每个 admissible `b=b(n)->infinity`。Endpoint theorem只保留 `s=0,b`，
没有使用式 (4) 的内部 constraints。

## 2. Half-error 的简化

以下固定 `delta=1/2`。令

\[
A(x)=\Phi(0,x)=\log\frac2x,
\qquad
B(x)=\Phi(x,1)
=\left(1-\frac x2\right)
\log\frac{2-x}{1-x}.
\tag{6}
\]

变量代换

\[
y=1-\frac x2\in[1/2,1]
\tag{7}
\]

把 kernel 写成

\[
\Phi(a,c)=y_a\log\frac{y_a}{y_a-y_c}.
\tag{8}
\]

这是 `u log(u/v)` 的 perspective与 affine map 的复合，所以
`Phi(a,c)` 在域 `a<c` 上联合凸。`A` 与 `B` 也凸；`A` 严格递减，`B` 严格
递增。

Endpoint constant 是

\[
C_{\rm end}
=\min_{0<x<1}\max\{A(x),B(x)\},
\tag{9}
\]

其唯一 optimizer `x_*` 满足 `A(x_*)=B(x_*)`。已有 interval certificate可把
它包在 `1.434406...` 附近；本文只用其唯一性。

## 3. 三 pivot reduction

取偶数 `b=2h`，只保留 pivots `0,h,b`。定义 shared interior averages

\[
p_b=\frac1{h-1}\sum_{i=1}^{h-1}x_i,
\qquad
q_b=\frac1{h-1}\sum_{i=h+1}^{b-1}x_i.
\tag{10}
\]

单调 profile给 `p_b<=x_h<=q_b`。在三个 pivot sums中丢掉至多常数个非负
boundary terms，再分别使用 Jensen 和 `partial_a Phi>=0`，得到

\[
F_{b,0}(x)
\ge\frac{h-1}{b}[A(p_b)+A(q_b)],
\tag{11}
\]

\[
F_{b,b}(x)
\ge\frac{h-1}{b}[B(p_b)+B(q_b)],
\tag{12}
\]

以及

\[
F_{b,h}(x)
\ge\frac{h-1}{b}[B(p_b)+\Phi(p_b,q_b)].
\tag{13}
\]

例如式 (13) 的左半段对 `B(x_1),...,B(x_(h-1))` 使用 Jensen；右半段对
`Phi(x_h,x_(h+1)),...,Phi(x_h,x_(b-1))` 使用 Jensen，再用
`x_h>=p_b` 与 `partial_a Phi>=0`。

定义二维闭式常数

\[
\boxed{
C_3=
\inf_{0<p<q<1}
\max\left\{
\frac{A(p)+A(q)}2,
\frac{B(p)+B(q)}2,
\frac{B(p)+\Phi(p,q)}2
\right\}.
}
\tag{14}
\]

由式 (11)--(13)，

\[
\liminf_{b\to\infty}C_b(1/2)\ge C_3.
\tag{15}
\]

故 full-fiber batch theorem立即加强为

\[
\boxed{H\ge C_3 n-o(n).}
\tag{16}
\]

这已经是 all-pivot 信息的严格使用；不需要先解完整连续控制问题。

## 4. 为什么 `C_3` 严格超过 endpoint 常数

### Theorem 4.1

\[
\boxed{C_3>C_{\rm end}.}
\tag{17}
\]

**证明。** 反设存在 `p_j<q_j` 使式 (14) 的 objective趋于
`C_end`。前两个 branches 的最大值至少为

\[
\max\left\{
\frac{A(p_j)+A(q_j)}2,
\frac{B(p_j)+B(q_j)}2
\right\}
\ge C_{\rm end},
\tag{18}
\]

因为分别对凸函数使用 Jensen，右侧进一步至少为
`max{A((p_j+q_j)/2),B((p_j+q_j)/2)}>=C_end`。

取等的极限要求两次 Jensen gap趋零，并且平均点趋于 endpoint问题的唯一 optimizer
`x_*`。`A` 严格凸，所以必有

\[
p_j-q_j\longrightarrow0,
\qquad p_j,q_j\longrightarrow x_*.
\tag{19}
\]

但

\[
\Phi(p_j,q_j)
=\left(1-\frac{p_j}2\right)
\log\frac{2-p_j}{q_j-p_j}
\longrightarrow+\infty,
\tag{20}
\]

使第三个 branch发散，矛盾。由于 objective在远离 diagonal 和 boundary的 compact
子集上连续，式 (17) 是严格正 gap，而不只是 infimum未取得。证毕。

因此式 (16)--(17) 是一个不依赖 decimal approximation 的严格
`>1.434406...` theorem：右侧常数由闭式二维凸变分定义。

## 5. Convex dual 与唯一 optimizer

记式 (14) 的三个 branches 为 `f_0,f_1,f_m`。它们都是凸函数，且 objective
在 boundary `p=0`、`q=1` 或 diagonal `p=q` 附近不能取最优。数值定位显示唯一
interior optimizer由

\[
f_0(p,q)=f_1(p,q)=f_m(p,q)
\tag{21}
\]

决定，等价于

\[
A(p)+A(q)=B(p)+B(q),
\qquad
B(q)=\Phi(p,q).
\tag{22}

在该解处存在 `lambda_0,lambda_1,lambda_m>0`，总和为一，并满足

\[
\lambda_0\nabla f_0
+\lambda_1\nabla f_1
+\lambda_m\nabla f_m=0.
\tag{23}

于是对任意 `p<q`，凸性给

\[
\max_i f_i(p,q)
\ge\sum_i\lambda_i f_i(p,q)
\ge\sum_i\lambda_i f_i(p_*,q_*)
=C_3.
\tag{24}

式 (22)--(24) 是一个 closed analytic dual certificate。投稿版可通过单调性证明
式 (22) 有唯一解，再以有理 interval arithmetic认证 `p_*,q_*` 和正 multipliers。

高精度定位值为

\[
p_*=0.5961558880945\ldots,
\qquad
q_*=0.8557291936266\ldots,
\tag{25}
\]

\[
C_3=1.4855061257315\ldots,
\tag{26}
\]

对应 KKT weights约为

\[
(\lambda_0,\lambda_1,\lambda_m)
=(0.38785292,0.41067342,0.20147366).
\tag{27}
\]

式 (25)--(27) 目前只用于复现和寻找 interval boxes；主定理是式 (14)、(16)、
(17) 与 convex dual (24)，不把这些 floating-point digits当作证明。

## 6. 完整 all-pivot 的连续极限

把离散 profile视为 nondecreasing path `x:[0,1]->[0,1]`，端点为 `0,1`。对
continuity points，式 (3) 的 Riemann limit是

\[
\mathcal F_t[x]
=\int_0^t B(x(r))\,dr
+\int_t^1\Phi(x(t),x(r))\,dr.
\tag{28}
\]

候选连续值为

\[
\boxed{
C_\infty
=\inf_{x\text{ nondecreasing},\ x(0)=0,x(1)=1}
\sup_{0\le t\le1}\mathcal F_t[x].
}
\tag{29}
\]

有限计算显示 optimizer倾向于 equalize全部 pivots。若 `x` 光滑且所有 constraints
active，形式上应满足 `mathcal F_t[x]=C_infty`。对 `t` 求导得到一个
Volterra/Bellman型方程；但 differentiation穿过 `r=t` 的 logarithmic singularity
需要先证明 `x'(t)>0` 及足够 regularity，当前不能把形式 Euler equation当定理。

式 (29) 的严谨化还需处理：

1. monotone paths 的 jumps；
2. `Phi(a,c)` 在 diagonal 的 log singularity仍可积；
3. finite-`b` regularizer `gamma_b` 与 Riemann limit的交换；
4. `lim C_b=C_infty` 的 recovery sequence与 lower semicontinuity。

因此本文不宣称已经求出完整 all-pivot极限。

## 7. 数值形状审计

epigraph SLSQP 对 finite `b` 给出以下定位值：

| `b` | numerical `C_b(1/2)` |
|---:|---:|
| 4 | 1.3887226127 |
| 8 | 1.5110343682 |
| 16 | 1.5920581731 |
| 32 | 1.6429888502 |

所有 pivots在数值 optimizer上近乎 active。`b=4` 低于 endpoint asymptotic常数并不
矛盾：endpoint Jensen proof有 `(b-1)/b` loss，而且原 filter theorem要求
`b->infinity`。这些数值提示 `C_infty` 很可能显著高于 `C_3`，但 optimizer、solver
误差和 `gamma_b` 尚未 interval-certified，不能据此给 theorem constant。

复现脚本是 `scripts/explore_all_pivot_profile.py`。它是 explorer，不是 verifier。

## 8. 研究裁决

已经严格闭合：

1. all-pivot finite minimax (4)；
2. 三 pivot二维凸 reduction (14)--(16)；
3. `C_3>C_end` 的解析 strict-gap theorem；
4. 用 positive KKT mixture表达的 global convex dual接口。

这把 ordinary half-error lower bound从 endpoint常数严格提高到一个闭式
`C_3`；高精度定位约为 `1.485506n`，但正式定理无需依赖这个小数。

尚未闭合：完整 Bellman optimizer、`lim C_b` 的存在性与精确值、以及一个可引用的
decimal interval certificate。下一步最有价值的是为式 (22)--(24) 写纯有理 interval
verifier，然后用四分或 dyadic pivots建立一串可解析收敛的 lower bounds，而不是
直接对式 (29) 猜微分方程。

