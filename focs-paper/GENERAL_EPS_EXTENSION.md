# 一般固定误差 ε 的推广：对每个 ε∈(0,1) 严格超越静态基线

> 2026-08-17。把 simultaneous replacement-cover width 主定理推广到任意固定
> ε∈(0,1)，并把 ε=1/2 的 witness 常数进一步优化到 2^{-20}。
> 结论：对每个固定 ε∈(0,1) 存在显式常数 $\eta_\varepsilon=2^{-X(\varepsilon)}>0$，
> 使 $H \ge (1+\eta_\varepsilon)\, n\log_2(1/\varepsilon) - o(n)$，
> 即**在 KLZ ordinary 模型 u/n→∞ 下，对每个固定错误率都严格超越 Carter 静态
> 基线 $n\log_2(1/\varepsilon)$**。

## 1. 静态基线复核

设 $\mathbb E a_Z \le n+\varepsilon(u-n)=:a_0$（逐点 FPR ≤ ε）。$f(x)=\log\binom xn$
凹，故 $\mathbb E f(a_Z)\le f(a_0)$，与 $H(S|Z)\le\mathbb E f(a_Z)$ 结合：

$$
L_u-B_u
=\log_2\tfrac{\binom un}{\binom{a_0}n}
=n\log_2\tfrac u{a_0}-o(n)
=n\log_2\tfrac1\varepsilon-o(n)
\qquad(\tfrac u{a_0}\to\tfrac1\varepsilon).
$$

故静态基线 $H\ge n\log_2(1/\varepsilon)-o(n)$（Carter 计数，u/n→∞）。

## 2. 一般 ε 的稳定性

设 $H\le(1+\gamma)\,n\log_2(1/\varepsilon)$，$X=a_Z/u$。

恒等式 $I(S;Z)=(L_u-B_u)+J+\mathbb E d_Z\le H$ 给
$\mathbb E d_Z\le\gamma n\log_2(1/\varepsilon)+o(n)$。

凹性切线：对 $f(x)=-\log_2 x$（$f''(x)=\frac1{x^2\ln2}\ge\frac1{\ln2}$ 于 $0<x\le1$），

$$
-\log_2 X\;\ge\;-\log_2\varepsilon-\frac{X-\varepsilon}{\varepsilon\ln2}
+\frac{(X-\varepsilon)^2}{2\ln2}.
$$

又 $\log\frac{\binom un}{\binom{a_Z}n}\ge n\log_2(u/a_Z)=-n\log_2 X$ 与 $I(S;Z)\le H$ 给

$$
-n\,\mathbb E\log_2 X\le L_u-\mathbb E f(a_Z)=I(S;Z)-\mathbb E d_Z\le(1+\gamma)n\log_2\tfrac1\varepsilon,
$$

故 $\mathbb E[-\log_2 X]\le(1+\gamma)\log_2(1/\varepsilon)$。结合 $\mathbb E X\le\varepsilon+o(1)$：

$$
\boxed{\mathbb E(X-\varepsilon)^2\le 2\ln2\,\gamma\log_2\tfrac1\varepsilon+o(1).}
$$

ε=1/2 时退化回文档 (6)。

## 3. 好分支与 reservoir（一般 ε）

取窗口 $\tau=c\sqrt{\gamma\log_2(1/\varepsilon)}$，$c=3.09$（同前：四个
Markov/Chebyshev 异常质量 $(4\ln2+2)/c^2<1/2$）。

好分支：$a\ge(\varepsilon-\tau)u$、$a'\le(\varepsilon+\tau)u$、分支 KL $\le\tau^2n$。
同前（$V\subseteq A$、$V\cup i\subseteq A'$）：

$$
b=a-q-|I\cap A|\ge(\varepsilon-2\tau)u,\qquad
v\ge b\,2^{-2\tau^2}\ge(\varepsilon-\tfrac52\tau)u,
$$

$$
|C|=|A'\setminus A|\le a'-v\le\tfrac72\tau u.
$$

## 4. 覆盖容量（α 参数版）

good insertion set：$i\subseteq A'$ 且 $|i\cap(U\setminus A)|\ge\alpha q$，
其中 $|U\setminus A|\ge(1-\varepsilon-\tau)u$。超几何均值 $\ge q(1-\varepsilon-\tau)(1+o(1))$；
取 $\alpha=(1-\varepsilon)(1-\delta_n)$，$\delta_n=\max\{4\tau/(1-\varepsilon),\,n^{-1/3}\}$，
则尾部 $\Pr[|i\cap(U\setminus A)|<\alpha q]\le e^{-\Omega(\delta_n^2 q)}=o(1)$。

因 $i\cap(U\setminus A)\subseteq i\cap(A'\setminus A)=i\cap C$，每个 successor state
至多吸收（overcount 上界，不需要 C(q,αq) 因子）：

$$
\binom{|C|}{\alpha q}\binom{u-\alpha q}{q-\alpha q}
\le\Big(\frac{e\cdot\frac72\tau u}{\alpha q}\Big)^{\alpha q}\binom uq\frac{(q)_{\alpha q}}{(u)_{\alpha q}}
=\binom uq\Big(\frac{7e\tau}{2\alpha}\Big)^{\alpha q}.
$$

于是

$$
\frac Hn\ge\frac\alpha2\log_2\frac{2\alpha}{7e\tau}-o(1)
=\frac{(1-\varepsilon)(1-\delta_n)}2
\left[\log_2\frac{1-\varepsilon}{3.5e\tau}+\log_2(1-\delta_n)\right]-o(1).
$$

## 5. 自洽阈值与 witness

代入 $\tau=3.09\sqrt{\gamma\log_2(1/\varepsilon)}$，忽略 $\delta_n$ 的小损失
（计入 o(1) 的解析说明见注），矛盾条件：

$$
(1+\gamma)\log_2\tfrac1\varepsilon
<
\frac{1-\varepsilon}{2}
\Big[\log_2(1-\varepsilon)-\log_2(3.5e\cdot3.09)
-\tfrac12\log_2\gamma-\tfrac12\log_2\log_2\tfrac1\varepsilon\Big].
$$

令 $x=-\log_2\gamma$（$\log_2(3.5e\cdot3.09)=4.8775$）：

$$
x > X(\varepsilon)
:=\frac{4\log_2(1/\varepsilon)}{1-\varepsilon}
+9.755-2\log_2(1-\varepsilon)+\log_2\log_2(1/\varepsilon).
$$

| ε | 1/2 | 0.25 | 0.1 | 0.05 | 0.02 | 0.9 | 0.99 |
|---|---|---|---|---|---|---|---|
| $X(\varepsilon)$ | 19.76 | 22.25 | 26.56 | 30.21 | 35.35 | 19.76 | 22.73 |

（数值由 `verify_replacement_cover_constant.py` Part III 计算；注意 $X(\varepsilon)$
在 ε→0 时 $\sim4\log_2(1/\varepsilon)\to\infty$，在 ε→1 时
$\sim2\log_2(1/(1-\varepsilon))\to\infty$，即**不存在覆盖全区间 (0,1) 的统一绝对常数**，
只能对每个固定 ε 给 $\eta_\varepsilon=2^{-X(\varepsilon)}$，或在任意固定紧子区间
$[\varepsilon_0,1-\varepsilon_1]$ 给统一常数。）

**定理（一般 ε）**：对每个固定 $0<\varepsilon<1$ 与 $u/n\to\infty$，存在显式常数
$\eta_\varepsilon=2^{-X(\varepsilon)-2}$ 使

$$
\boxed{H\;\ge\;(1+\eta_\varepsilon)\,n\log_2\tfrac1\varepsilon-o(n),}
$$

（+2 是 δ_n 修正项的保守上界：修正项 $2\tau(\log_2\frac{1-\eps}{3.5e\tau}+2)$
在 $x=X(\eps)+2$ 处全区间最大 0.023<0.05，脚本验证）。即对每个固定错误率都严格
超越静态基线。ε=1/2 的精细 witness 为 $H\ge(1+2^{-20})n-o(n)$
（含 δ_n 修正的精确算术：X(1/2)=19.755<20，2^{-20} 处 LHS=1.0138、
margin≈0.0138，脚本 Part II 验证）。

## 6. 与 ε=1/2 版（2^{-25}）的关系

前一份笔记的 2^{-25} 用的是固定 $s_0=q/3$（α=1/3）；本笔记把 α 调到
$(1-\varepsilon)(1-\delta_n)\to1-\varepsilon$，容量指数从 q/3 提到
$(1-\varepsilon)q$，常数相应改善 2^5。ε=1/2 时 witness 从 2^{-25} 升到 2^{-20}。

## 7. 需要正式写清的三个细节（写论文时逐条展开）

1. **δ_n 损失**：$(\alpha/2)\log_2(1-\delta_n)$ 与 $\delta_n\log(1/\tau)$ 项
   需对每个 ε 显式吸收进 o(1) 或 margin（δ_n = max{4τ/(1−ε), n^{−1/3}} → 0 但
   $e^{-\Omega(\delta_n^2 q)}=o(1)$）。
2. **q = ⌊n/2⌋ 与 (u−n) 基集的 falling-factorial**：全部是 $O(n^2/u)=o(n)$ 级修正。
3. **ε 趋近 1**：$X(\varepsilon)\to\infty$（$2\log_2(1-\varepsilon)$ 项），定理在
   ε→1 时退化为平凡（RHS→0）；对 ε ≤ 1−η 可用统一常数。

## 8. 验证脚本

`verify_replacement_cover_constant.py` 的 general-ε 部分：
- Fraction 验证 §2 的切线不等式（x∈(0,1] 任意点）；
- 验证 ε∈{1/2, 1/4, 1/10} 处 X(ε) 的数值并确认 γ=2^{-30}（或 2^{-20} at ε=1/2）
  处的矛盾方向与 margin；
- 验证容量不等式 $(7e\tau/2\alpha)^{\alpha q}$ 的代数。
