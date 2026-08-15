# Algebraic threshold quotients 的完整误差相图

> 日期：2026-08-13。状态：定义、单个分支的唯一性、fixed-state rate 与端点
> 尺度已严格推导；全局 envelope 的相邻分支唯一交点目前有高精度数值证据，
> 尚缺解析证明。所有对数在公式中默认自然对数，最终 rate 除以 \(\ln2\)。

## 1. 单参数 family

令整数 \(q\ge1\) 表示 residue modulus；它对应 threshold \(L=q-1\)。每个
outer block保存总负载 \(c\) 与 binary one-count modulo \(q\)。当 \(c<q\) 时
multiset可精确恢复；当 \(c\ge q\) 时两种 query bits都必须接受。

一个 Poisson-\(\lambda\) block 对 fresh query 的 FPR 为

\[
\varepsilon_q(\lambda)
=1-e^{-\lambda}E_{q-1}(\lambda/2),
\qquad
E_r(x)=\sum_{t=0}^r\frac{x^t}{t!}.
\tag{1}
\]

local state counts为 \(d_t=\min(t+1,q)\)，所以 OGF 有闭式

\[
A_q(z)=\sum_{t\ge0}d_tz^t
=\frac{1-z^q}{(1-z)^2}.
\tag{2}
\]

对目标 \(\varepsilon\in(0,1)\)，定义 \(\lambda_q(\varepsilon)\) 为
\(\varepsilon_q(\lambda)=\varepsilon\) 的根，再定义 \(z_q(\varepsilon)\in(0,1)\)
为

\[
\lambda_q
=\frac{zA_q'(z)}{A_q(z)}
=\frac{2z}{1-z}-\frac{qz^q}{1-z^q}.
\tag{3}
\]

该分支的 fixed-state rate 是

\[
\boxed{
R_q(\varepsilon)
=\frac1{\ln2}
\left[
\frac{\ln A_q(z_q)}{\lambda_q}-\ln z_q
\right].
}
\tag{4}
\]

family envelope 为

\[
R_{\rm AT}(\varepsilon)=\min_{q\ge1}R_q(\varepsilon).
\tag{5}
\]

## 2. 已证的唯一性与光滑性

### Lemma 2.1

对每个 \(q\ge1\)，\(\varepsilon_q(\lambda)\) 在 \([0,\infty)\) 上从 \(0\)
严格增至 \(1\)。因此 \(\lambda_q(\varepsilon)\) 存在且唯一，并在
\((0,1)\) 上解析。

证明。令 \(F_q(\lambda)=e^{-\lambda}E_{q-1}(\lambda/2)\)。则

\[
F_q'(\lambda)
=e^{-\lambda}
\left[\frac12E_{q-2}(\lambda/2)-E_{q-1}(\lambda/2)\right]<0,
\]

其中 \(E_{-1}=0\)。端点显然。

### Lemma 2.2

对每个 \(q\ge1,\lambda>0\)，式 (3) 有唯一 \(z\in(0,1)\)。

证明。把

\[
p_z(t)=\frac{d_tz^t}{A_q(z)}
\]

视为 \(\mathbb N\) 上的非退化分布，则

\[
\frac{d}{d\ln z}\frac{zA_q'(z)}{A_q(z)}
=\operatorname{Var}_{p_z}(T)>0.
\]

其均值在 \(z\downarrow0\) 时趋于 \(0\)，在 \(z\uparrow1\) 时趋于无穷。
所以 saddle唯一，且隐函数定理给解析性。

## 3. 有限最优 \(q\)

固定 \(\varepsilon\)，当 \(q\to\infty\) 时

\[
\lambda_q\to\lambda_\infty
=2\ln\frac1{1-\varepsilon},
\qquad
A_q(z)\to(1-z)^{-2},
\]

故 \(R_q\to R_\infty\)，即 binary exact-multiplicity rate。数值上对每个
\(\varepsilon\in(0,1)\) 都存在有限 \(q\) 使 \(R_q<R_\infty\)，因而 minimum
由有限 \(q\) 取得。

这里仍有一个很小但明确的解析缺口：需要对全部 \(\varepsilon\) 一次性证明
某个 finite truncation严格优于极限分支。可用 \(q\to\infty\) 的首个尾项展开
处理，但尚未写成符号一致的 lemma。对任意给定 compact epsilon interval，
interval arithmetic可严格验证有限 \(q\) 取得 minimum。

## 4. 数值相图

高精度求根显示 envelope 从 \(q=3\) 开始，并依次经过
\(q=4,5,6,\ldots\)。前几个相邻切换点 \(R_q=R_{q+1}\) 是：

| \(q\to q+1\) | \(\varepsilon\) |
|---:|---:|
| 3 -> 4 | 0.691362376856073 |
| 4 -> 5 | 0.880349221320760 |
| 5 -> 6 | 0.953700123072008 |
| 6 -> 7 | 0.982253338586167 |
| 7 -> 8 | 0.993260276025918 |
| 8 -> 9 | 0.997460871581919 |
| 9 -> 10 | 0.999049924657444 |
| 10 -> 11 | 0.999646576694184 |
| 11 -> 12 | 0.999869187295275 |
| 12 -> 13 | 0.999951792936739 |

特别地，\(\varepsilon=1/2\) 落在 \(q=3\) phase，给出

\[
R_{\rm AT}(1/2)=R_3(1/2)
=2.3490834401931417\ldots.
\]

目前没有解析证明排除：非相邻分支跳跃；同一对相邻分支多次相交；或极低
epsilon处由高阶极小差异产生的隐藏 phase。80-digit计算在可信范围内均未发现
这些现象，但 double precision 在 \(\varepsilon<10^{-6}\) 时已不足以判断分支
差，因此不能把普通浮点扫描当作证明。

## 5. \(\varepsilon\downarrow0\)

对固定 \(q\ge2\)，式 (1) 给

\[
\lambda_q(\varepsilon)=2\varepsilon+O(\varepsilon^2),
\qquad
z_q(\varepsilon)=\varepsilon+O(\varepsilon^2).
\]

代入 (4)，

\[
\boxed{
R_q(\varepsilon)
=\log_2\frac1\varepsilon+\log_2e+o(1).
}
\tag{6}
\]

所有 fixed \(q\ge2\) 在主项上简并。高精度 series显示首个区分 envelope 的
项由 \(q=3\) 最小；数值上 \(q^*(\varepsilon)=3\) 一直持续到第一个切换点。
完整解析证明需要把 \(q=1,2,3\) 的展开写到首个非零差异，并对所有
\(q\ge4\) 给 uniform remainder bound。这个 uniform-in-q bound 尚未完成。

因此目前严格可说的是 (6)；

\[
q^*(\varepsilon)\to3
\]

仍应标为强数值支持的 conjecture，而不是 theorem。

## 6. \(\varepsilon\uparrow1\)

令

\[
L=\ln\frac1{1-\varepsilon}.
\]

式 (1) 可改写为

\[
1-\varepsilon
=e^{-\lambda/2}
\Pr[\operatorname{Pois}(\lambda/2)\le q-1].
\tag{7}
\]

这立即给 \(\lambda\le2L+o(L)\)。取

\[
\lambda=2L+o(L),
\qquad
q=L+\omega(\sqrt L)
\]

时 Poisson lower-tail probability趋于 \(1\)，所以约束可达。另一方面，若
\(q\le(1-\delta)L\)，Poisson large deviation在 (7) 中产生额外线性指数代价；
结合 (2)--(4) 可排除其成为 envelope optimum。由此得到尺度

\[
\boxed{
\lambda_{q^*}=2L+o(L),
\qquad
q^*=L+o(L).
}
\tag{8}
\]

将 \(z=e^{-s/\lambda}\) 代入 (2)--(4)，在 (8) 的窗口内

\[
R_{\rm AT}(\varepsilon)
=\Theta\left(\frac{\ln L}{L}\right)
=\Theta\left(
\frac{\ln\ln(1/(1-\varepsilon))}
{\ln(1/(1-\varepsilon))}
\right).
\tag{9}

要给 (9) 的 sharp leading constant，需要同时优化 central-limit/moderate-
deviation窗口

\[
q-L=\Theta(\sqrt{L\ln L})
\]

以及 saddle中的 \(1-z^q\) truncation；当前尚未闭合。数值切换点满足

\[
1-\varepsilon_{q\to q+1}\asymp e^{-q},
\]

与 (8) 一致。

## 7. 可复现的数值证书方案

要把 phase table升级为 theorem，可对每个 compact interval按以下方式生成
可机检 certificate：

1. 用 rational intervals包住 \(\varepsilon\)；
2. 对 (1) 用 alternating-free positive Taylor bounds与 directed rounding包住
   唯一 \(\lambda_q\)；
3. 由 Lemma 2.2 的单调性二分包住唯一 \(z_q\)；
4. 用 interval log bounds包住 \(R_q\) 与导数；
5. 在每个 candidate switch两侧证明 \(R_q-R_{q+1}\) 异号，并在区间内证明
   其导数不变号；
6. 同时对所有非相邻 \(r\) 证明 \(R_r\) 严格更大；
7. 对 \(q>Q\) 用 uniform tail bound比较 \(R_q\) 与 \(R_\infty\)，把无限 family
   截成有限检查。

步骤 5 和 7 是唯一需要新解析估计的部分；其余都是直接 interval arithmetic。
在没有这两个证书前，表中的小数应称为高精度数值结果，不应标成完整严格相图。
