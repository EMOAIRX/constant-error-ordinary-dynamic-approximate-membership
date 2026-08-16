# Continuous all-pivot limit：endpoint boundary theorem

> 日期：2026-08-17。状态：本文证明 candidate continuous optimizer 的 endpoint
> 正则变化指数和下一阶 logarithmic boundary layer。它没有把 numerical candidate
> $1.7156\ldots$ 提升为 theorem constant。

所有 logarithms 在积分方程中取自然对数；这只删除一个共同正因子。

## 1. All-active tail equation

Half error kernel 为

$$
\Phi(a,c)
=\left(1-\frac a2\right)
\log_2\frac{2-a}{c-a},
$$

$$
B(c)=\Phi(c,1).
$$

若 continuous all-pivot optimizer 由无原子的 value-density $\rho(c)$ 描述，且所有
pivots 等势，则比较 pivot $a$ 与 endpoint pivot 得到必要 tail equation

$$
\boxed{
\int_a^1[\Phi(a,c)-B(c)]\rho(c)\,dc=0,
\qquad0<a<1.
}
$$

令

$$
u=1-a,
\qquad
v=1-c,
\qquad
r(v)=\rho(1-v).
$$

删除共同因子 $1/(2\ln2)$ 后，方程变为

$$
\boxed{
\int_0^u
\left[
(1+u)\ln\frac{1+u}{u-v}
-(1+v)\ln\frac{1+v}{v}
\right]r(v)\,dv=0.
}
$$

## 2. Unique regular-variation exponent

假设 endpoint density 正则变化：

$$
r(v)\sim Kv^{\alpha-1},
\qquad K>0, \alpha>0.
$$

代入 $v=ut$，leading kernel 是

$$
\ln\frac{t}{1-t}.
$$

其系数必须为零：

$$
H(\alpha)
=\int_0^1t^{\alpha-1}\ln\frac{t}{1-t}\,dt
=\frac{\psi(\alpha)+\gamma}{\alpha}=0.
$$

这里 $\psi$ 是 digamma，$\gamma$ 是 Euler constant。因为 $\psi$ 严格递增，且

$$
\psi(1)=-\gamma,
$$

唯一可能是

$$
\boxed{\alpha=1.}
$$

所以 candidate density 不能在 $c\uparrow1$ 时按幂次爆炸或消失；它必须趋于有限正
极限 $r_0$，真正的修正出现在下一阶。

## 3. The unavoidable $v\ln v$ layer

写

$$
r(v)=r_0[1+A v\ln v+Bv+o(v)].
$$

再次令 $v=ut$。Kernel 展开为

$$
\ln\frac{t}{1-t}
+u\left[(1-t)(1-\ln u)-\ln(1-t)+t\ln t\right]
+O(u^2|\ln u|).
$$

$u^2\ln u$ 系数使用

$$
\int_0^1t\ln\frac{t}{1-t}\,dt=\frac12
$$

后强迫

$$
A=1.
$$

常数阶再使用

$$
\int_0^1
t\ln t\ln\frac{t}{1-t}\,dt
=\frac{\pi^2}{12}-\frac34,
$$

得到

$$
B=-\left(1+\frac{\pi^2}{6}\right).
$$

因此

$$
\boxed{
r(v)
=r_0\left[
1+v\ln v
-\left(1+\frac{\pi^2}{6}\right)v
+o(v)
\right].
}
$$

特别地，$r'(v)$ logarithmically diverges。任何直接假设普通 $C^1$ endpoint density
并对 all-pivot functional 写光滑 ODE 的路线都遗漏了真实 boundary correction。

## 4. Correct continuous dual template

候选 dual measure 应允许 endpoint atoms：

$$
\lambda
=\alpha_0\delta_0+\alpha_1\delta_1+w(t)\,dt,
\qquad
\alpha_0+\alpha_1+\int_0^1w(t)\,dt=1.
$$

对 monotone profile $x$，weighted energy 可交换积分写成

$$
\begin{aligned}
L_\lambda[x]
=\int_0^1\Bigg[
&\alpha_0A(x(r))
+\left(\alpha_1+\int_r^1w(t)\,dt\right)B(x(r))\\
&+\int_0^r w(t)\Phi(x(t),x(r))\,dt
\Bigg]dr.
\end{aligned}
$$

若找到 all-active $x_*$ 和非负 $\lambda$，使 $x_*$ 全局最小化这个 convex energy，
则

$$
\sup_t\mathcal F_t[x]
\ge L_\lambda[x]
\ge L_\lambda[x_*]
$$

给出 matching continuous converse。

但 $\partial_1\Phi$ 与 $\partial_2\Phi$ 的 stationarity terms 各自 logarithmically
divergent。它们只能在共同 cutoff 下作为 finite part 合并。安全证明必须先对
$\Phi_\gamma$ 建立 dual，再联合令 $\gamma\downarrow0$；不能把两个 singular
integrals 分别当作普通 Lebesgue integrals。

## 5. Numerical location and theorem boundary

对 tail equation 作 product-integration discretization，稳定指向

$$
C_\infty^{\rm num}\approx1.7156.
$$

该数字与 finite-pivot values 从下方缓慢上升的现象一致；$v\ln v$ endpoint layer
也解释了收敛为何慢。它目前只是 numerical location，不是 certified lower bound、
upper bound 或 AMQ optimum。

关闭 full-fiber all-pivot 方法本身仍需：

1. equicoercive $\Gamma$-limit；
2. singular liminf 与 recovery sequence；
3. 联立求解 primal tail equation 和 nonnegative dual measure；
4. 对 finite-part stationarity 的严格认证。

这条路线的价值在于解析关闭整个 all-pivot hierarchy，而不是继续增加固定 block 数。
