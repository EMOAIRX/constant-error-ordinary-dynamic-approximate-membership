# Three-pivot batch converse：从 1.4344 到解析二维变分

> 日期：2026-08-13。状态：解析 theorem candidate。三-pivot reduction 与
> `C_3>C_end` 的严格 separation 已闭合。一个单调矩形覆盖还给出可复核的
> `C_3>1.48` 证书；浮点极值约为 `1.485506`，但不把后者写成认证常数。

所有对数以 2 为底。固定 `delta=1/2`，定义

\[
\Phi(a,c)=(1-a/2)\log_2\frac{1-a/2}{(c-a)/2},
\qquad 0\le a<c\le1.
\tag{1}
\]

沿用 full-fiber joint-batch converse。对任意非降 profile

\[
0\le x_0\le x_1\le\cdots\le x_b\le1,
\tag{2}
\]

KLZ pivot `s` 给

\[
P_s(x)=\frac1b\left[
\sum_{k=1}^s\Phi(x_{k-1},x_b)
+\sum_{k=s+1}^b\Phi(x_s,x_k)
\right].
\tag{3}
\]

忽略 finite-`b` 的 `gamma_b->0` 正则与 `o(1)` 后，filter rate 至少为
`max_s P_s(x)`。

## 1. 两端 pivot 回顾

令

\[
A(x)=\Phi(0,x)=\log_2\frac2x,
\qquad
B(x)=\Phi(x,1)=(1-x/2)\log_2\frac{2-x}{1-x}.
\tag{4}
\]

由 `s=0,b`，分别 Jensen 后得到

\[
H/n\ge\min_x\max\{A(x),B(x)\}-o(1)
=1.434406361243753\ldots-o(1).
\tag{5}
\]

## 2. 加入一个中间 pivot

不妨先取 `b=2s`；一般 `b` 舍去一个 batch。为了避免 endpoint 与 cut 的 index
错位，使用共同的内部坐标

\[
I=\{1,\ldots,s-1\},
\qquad J=\{s+1,\ldots,b-1\}.
\tag{5a}
\]

令

\[
p=\frac1{s-1}\sum_{i\in I}x_i,
\qquad
q=\frac1{s-1}\sum_{j\in J}x_j,
\qquad c=x_s.
\tag{5b}
\]

由 profile 单调性，`p<=c<=q`。从每个 pivot sum 中丢掉至多两个非负 batch
terms 后，损失因子是 `(s-1)/b=1/2-o(1)`。两个 endpoint pivots 分别给

\[
P_0\ge\frac12[A(p)+A(q)]-o(1),
\tag{6}
\]

\[
P_b\ge\frac12[B(p)+B(q)]-o(1).
\tag{7}
\]

中间 pivot 的左半部分为 `Phi(x_i,1)=B(x_i)`，对 `I` 中坐标 Jensen 得

\[
\frac2b\sum_{i<s}\Phi(x_i,1)\ge B(p)-o(1).
\tag{8}
\]

右半部分为 `Phi(c,x_k)`。因为 `c>=p`，`Phi(a,z)` 对 `a` 非降；对固定
`a`，函数 `z -> Phi(a,z)` 严格凸。因此对 `J` 中坐标使用 Jensen，得到

\[
\frac2b\sum_{k>s}\Phi(c,x_k)
\ge\Phi(c,q)-o(1)
\ge\Phi(p,q)-o(1).
\tag{9}
\]

因此严格的三-pivot constant target 是

\[
\boxed{
C_3=inf_{0<p\le q<1}
\max\left\{
\frac{A(p)+A(q)}2,
\frac{B(p)+B(q)}2,
\frac{B(p)+\Phi(p,q)}2
\right\}.
}
\tag{10}
\]

式 (10) 本身已经给出比 endpoint theorem 严格更强的一般 ordinary nonmonotone
结论；下一节证明这个 separation 不依赖浮点计算。

## 3. 严格证明 `C_3>C_end`

记

\[
C_{\rm end}=\min_x\max\{A(x),B(x)\}.
\tag{10a}
\]

`A` 严格凸且递减，`B` 严格凸且递增；它们在唯一一点 `x_*` 相交，并在那里
达到 endpoint minimax。

首先由 Jensen，式 (10) 的前两项满足

\[
\max\left\{
\frac{A(p)+A(q)}2,
\frac{B(p)+B(q)}2
\right\}
\ge
\max\left\{A\left(\frac{p+q}2\right),
B\left(\frac{p+q}2\right)\right\}
\ge C_{\rm end}.
\tag{10b}
\]

假设反面存在 `(p_j,q_j)` 使式 (10) 的最大值趋于 `C_end`。由端点发散性，
可取收敛子列。式 (10b) 与 endpoint minimizer 的唯一性强迫

\[
(p_j+q_j)/2\longrightarrow x_*.
\tag{10c}
\]

又因为 `A,B` 严格凸，Jensen gap 趋零强迫

\[
q_j-p_j\longrightarrow0,
\qquad p_j,q_j\longrightarrow x_*.
\tag{10d}
\]

但是

\[
\Phi(p_j,q_j)
=(1-p_j/2)\log_2\frac{2-p_j}{q_j-p_j}
\longrightarrow\infty,
\tag{10e}
\]

使式 (10) 的第三项发散，矛盾。因此

\[
\boxed{C_3>C_{\rm end}=1.434406361243753\ldots.}
\tag{10f}
\]

这个证明给出严格的常数 gap，但没有给 gap 的方便闭式小数。正式 theorem 可以
直接以二维变分 `C_3` 陈述；若摘要需要十进制值，再附 interval-arithmetic certificate。

## 4. 一个显式认证常数：`C_3>1.48`

式 (10) 中三项记为 `F_1,F_2,F_3`。在任意矩形

\[
R=[p_-,p_+]\times[q_-,q_+]
\tag{11}
\]

与可行域 `0<p<=q<1` 的交上，单调性给严格下界

\[
F_1\ge\frac{A(p_+)+A(q_+)}2,
\tag{12}
\]

\[
F_2\ge\frac{B(p_-)+B(q_-)}2,
\tag{13}
\]

以及

\[
F_3\ge\frac{B(p_-)+\Phi(p_-,q_+)}2.
\tag{14}
\]

第三式使用 `B` 对 `p` 递增、`Phi` 对第一变量递增且对第二变量递减。因而定义

\[
L(R)=\max\left\{
\frac{A(p_+)+A(q_+)}2,
\frac{B(p_-)+B(q_-)}2,
\frac{B(p_-)+\Phi(p_-,q_+)}2
\right\},
\tag{15}
\]

则整个 `R` 上目标至少为 `L(R)`。

边界 `p<=0.05` 由第一项给出至少 `3.1609...`，边界 `q>=0.95` 由第二项给出
至少 `1.6529...`。在中间 `[0.05,0.95]^2` 上，每次沿较长边二分，并丢弃
`p_->=q_+` 的空可行矩形。对 `T=1.48`，directed-rounding verifier 访问 51 个
矩形后全部由式 (15) 排除，没有未决叶。因此得到认证形式

\[
\boxed{C_3>1.48.}
\tag{16}
\]

独立 verifier 是
`scripts/verify_three_pivot_148.py`。它只使用 Python 标准库 `decimal`，精度 90 digits，
以 130 digits 计算 correctly-rounded-nearest `ln` 后加入显式 `10^-110` 误差半径，
再对 `ln 2` 分母取上界、对正数乘除保持向下舍入。

## 5. 数值形状

直接搜索显示 optimizer 约为

\[
p\approx0.596156,
\qquad q\approx0.855729,
\tag{11}
\]

且

\[
\frac{A(p)+A(q)}2
\approx
\frac{B(p)+B(q)}2
\approx1.48550613,
\tag{12}
\]

第三项也在数值精度内取同一值。这提示三个 pivot constraints 在 optimizer 处
同时 active。这个浮点值不是证明；认证声明仍只使用式 (16)。

## 6. 一个潜在简化

如果能证明第三项在 endpoint 两项的 minimax optimizer 附近从不成为更小的逃逸
方向，则式 (10) 可先降为二点 moment problem

\[
\inf_{p\le q}
\max\left\{
\frac{A(p)+A(q)}2,
\frac{B(p)+B(q)}2
\right\}.
\tag{13}
\]

但式 (13) 允许 `p=q`，会退回 endpoint constant；因此中间 pivot 不可丢。
cut variable `c=x_s` 满足

\[
p\le c\le q,
\tag{14}
\]

由于 `Phi(a,q)` 对 `a` 非降，`Phi(c,q)>=Phi(p,q)`，所以 adversary 的最坏选择
确实可将 `c` 压到 `p`；二维式 (10) 是合法下界，不需保留三维变量。

## 7. 当前裁决

- 全 pivot 离散 minimax 是正确的研究对象。
- 有限深度数值从 `b=8` 的约 `1.512` 上升到 `b=20` 的约 `1.612`，显示显著余量。
- 二维 reduction 的 cut/average 接口和 strict separation 已闭合。
- 可立即陈述的解析改进是 `H>=C_3 n-o(n)`、`C_3>C_end`，以及认证常数
  `H>1.48n-o(n)`。
- `C_3≈1.485506` 仍需更精细 interval certificate 后才能作为认证小数。
