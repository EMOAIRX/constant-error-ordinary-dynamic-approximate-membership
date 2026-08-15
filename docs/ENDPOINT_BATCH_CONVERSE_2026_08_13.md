# Endpoint batch converse：ordinary dynamic filters 的 1.4344n 下界

> 日期：2026-08-13。状态：修正版 theorem。旧稿的逐区间 cross-average
> reduction 方向错误；这里改为在两个 endpoint sums 共享的内部 profile
> coordinates 上分别应用 Jensen，得到严格 min--max 变分。严格 batch lemma 见
> `BATCH_PERSPECTIVE_AND_PREFIX_MASS_LEMMA_2026_08_13.md`。

所有对数以 2 为底。

## 1. 模型与主定理

考虑容量 `n`、有限宇宙 `U`（`u=|U|`）上的 ordinary one-sided dynamic
approximate-membership filter：

- persistent state 始终是一个固定 `H`-bit block；
- 可读取免费无限 public random tape；
- key-only `Insert/Delete/Query`，只要求合法更新；
- zero false negatives；
- 对每条固定合法 history 和每个固定当前 nonmember，FPR 至多固定
  `delta in (0,1/2]`；
- 允许任意 history dependence、non-monotone accepted sets、ghosts、relocation 和
  global certificates。

假设 filter 支持 `f(n)=omega(n)` 次操作，并且

\[
u/n^2\longrightarrow\infty.
\tag{1}
\]

定义

\[
\boxed{
C(\delta)=\min_{0<x<1}\max\{A_\delta(x),B_\delta(x)\},
}
\tag{2}
\]

其中

\[
A_\delta(x)=\log\frac1{\delta x},
\qquad
B_\delta(x)=(1-\delta x)
\log\frac{1-\delta x}{\delta(1-x)}.
\tag{2a}
\]

### Theorem 1（endpoint batch converse）

在上述模型中，

\[
\boxed{H\ge C(\delta)n-o(n).}
\tag{3}
\]

当 `delta=1/2` 时，一维目标在

\[
x_*=0.739998185722401\ldots
\tag{4}
\]

取得唯一极小值，并且

\[
\boxed{
H\ge1.434406361243753\ldots n-o(n).
}
\tag{5}
\]

这个常数：

- 显著超过 Lovett--Porat 正式的 `1.1n` 和其未认证递归约 `1.13n`；
- 超过逐 key full-fiber lifting 加 AND amplification 的
  `1.19927323445n`；
- 距 `log_2 e=1.442695...` 只差约 `0.008289` bits/key；
- 仍低于现有 ordinary everlasting quotient upper bound
  `2.349083...n`，没有数值矛盾。

## 2. Full-fiber 接口

固定 filter tape `R`，对物理状态 `m`、当前 load `t` 和操作数 `q` 定义

\[
W_R(m,t,q)=
\bigcup\{S(h): |h|=q,\ |S(h)|=t,\ M_R(h)=m\}.
\tag{6}
\]

union 遍历从空集出发的全部合法 histories。则

\[
S(h)\subseteq W_R(M_R(h),t,q)\subseteq A_R(M_R(h)),
\tag{7}
\]

并且对每条固定 history

\[
\mathbb E_R|W_R(M_R(h),t,q)|
\le t+\delta(u-t).
\tag{8}
\]

与 KLZ Section 5 的 conforming reconstructible set 不同，`W` 不依赖 public
partition。对 self-contained common suffix，它只会因为 witness endpoint 已含某个
未来 insertion label 而失去 union elements。`u/n^2 -> infinity` 允许选择 KLZ
深度参数 `b->infinity` 足够慢，使全部 transport loss 在归一化后为
`o(4^{-b})`。

因此存在一个 corrected nondecreasing profile

\[
0\le x_0\le x_1\le\cdots\le x_b\le1,
\tag{9}
\]

使 KLZ endpoint states 满足以下两个 partition-safe first moments。令
`V=u/b`、`m=n/b`，对一次 `Send(X_k,F_r,G_ell)` 定义

\[
G=W(G_\ell)\cap U_k,
\qquad
D=(W(F_r)\setminus W(G_\ell))\cap U_k.
\tag{10}
\]

则一致地有

\[
\frac{\mathbb E|G|}{V}
\le \delta x_\ell+o(1),
\tag{11}
\]

\[
\frac{\mathbb E|D|}{V}
\le \delta(x_r-x_\ell)+o(1).
\tag{12}
\]

式 (11) 不是只用全局 FPR 得到的 `<=delta`。它使用 full-fiber profile 的实际
累计质量。式 (12) 是 common-suffix transport、obfuscation coupling 和
partition-free removing-`U_k` 的组合。

## 3. Exact batch code

固定 `G` 后，hidden batch

\[
X=(X_1,\ldots,X_m)\in U_k^{\underline m}
\]

仍均匀无放回。这里 `G` 来自 `G_ell`，其 operational history 在插入 hidden
future batch `X_k` 之前结束。`D` 可以依赖 `X`；下面的 code 不需要它们独立。

令

\[
Z_i=\mathbf1[X_i\in G],
\qquad
Q=\sum_i(1-Z_i),
\qquad g=|G|,\ d=|D|.
\tag{13}
\]

Alice 联合编码整个 `Z` 以及所有 hit values，再把 miss values 作为 `D` 中的
ordered distinct tuple 编码。精确计数给

\[
\boxed{
\mathcal C_k
\le
\log(V)_{\underline m}
+\mathbb E\log
\frac{(d)_{\underline Q}}{(V-g)_{\underline Q}}
+O(1).
}
\tag{14}
\]

证明要点是：给定 hit pattern 和 hit values 后，未揭示的 `Q` 个坐标恰有
`(V-g)_{underline Q}` 种可能。这个 identity 自动处理 frozen masks、shared
certificates 和任意 hit correlation；没有使用
`H(Z_1,...,Z_m) >= m h(delta)` 之类的假命题。

由 falling-factorial ratio、log perspective 的联合凹性，以及 conditional
hypergeometric variance，

\[
\mathcal C_k
\le
\log(V)_{\underline m}
+m\alpha\log\frac{\mathbb E d/V}{\alpha}
+o(m),
\tag{15}
\]

其中

\[
\alpha=\mathbb E Q/m=1-\mathbb E g/V.
\tag{16}
\]

将 (11)--(12) 代入，并注意函数
`alpha -> alpha log(c/alpha)` 在当前可行区间的最坏值位于
`alpha=1-delta x_ell`，得到

\[
\boxed{
\mathcal C_k
\le
\log(V)_{\underline m}
-m\Phi_\delta(x_\ell,x_r)+o(m),
}
\tag{17}
\]

其中

\[
\boxed{
\Phi_\delta(a,b)
=(1-\delta a)
\log\frac{1-\delta a}{\delta(b-a)}.
}
\tag{18}
\]

若 profile difference 为零，合法 transcript 迫使相应 miss mass 为零；式 (18)
按下半连续延拓解释为 `+infinity`，只会加强下界。

正式的 finite-`b` 证明不直接使用这个延拓。由 first-moment interface 保留统一
正则项 `gamma_b=O(4^{-b})`，把 denominator 写成

\[
\delta(x_r-x_\ell+\gamma_b).
\tag{18a}
\]

下面先对每个有限 `b` 的正则化函数使用 Jensen，最后才令
`b->infinity`、`gamma_b->0`。这统一覆盖零 profile difference。

## 4. 两个 endpoint pivots 已经足够

KLZ protocol 对每个 pivot `s in {0,...,b}` 都可解码全部 batches。本文不需要解
完整的 `(b+1)`-pivot 变分，只取两个端点。

### Pivot `s=0`

第 `k` 批使用 `(ell,r)=(0,k)`，故 source entropy 减 communication 后给

\[
H\ge \frac nb\sum_{k=1}^b
\Phi_{\delta,\gamma_b}(x_0,x_k)-o(n).
\tag{19}
\]

### Pivot `s=b`

第 `k` 批使用 `(ell,r)=(k-1,b)`，故

\[
H\ge \frac nb\sum_{k=1}^b
\Phi_{\delta,\gamma_b}(x_{k-1},x_b)-o(n).
\tag{20}
\]

下面两条单调性给出 endpoint reduction：

\[
\partial_a\Phi_\delta(a,b)\ge0,
\qquad
\partial_b\Phi_\delta(a,b)<0.
\tag{21}
\]

第一式令 `r=(1-delta a)/(delta(b-a))` 后化为
`delta(r-ln r-1)>=0`；这里 `r>=1`，因为 `b<=1`。第二式直接由 denominator
对 `b` 的单调性得到。因此，

\[
\Phi_{\delta,\gamma_b}(x_0,x_k)
\ge A_{\delta,\gamma_b}(x_k),
\qquad
\Phi_{\delta,\gamma_b}(x_i,x_b)
\ge B_{\delta,\gamma_b}(x_i),
\tag{22}
\]

其中可以取

\[
A_{\delta,\gamma}(x)=\log\frac1{\delta(x+\gamma)},
\qquad
B_{\delta,\gamma}(x)=(1-\delta x)
\log\frac{1-\delta x}{\delta(1-x+\gamma)}.
\tag{22a}
\]

prefix-mass 中另一个 `o(4^{-b})` 可通过把 `gamma_b` 增大常数倍吸收；由于
`alpha log(c/alpha)` 在当前可行域对 `alpha` 递减，这个吸收方向给通信上界。

丢掉 (19) 中 `k=b` 的一个非负 endpoint term，以及 (20) 中 `i=0` 的一个
非负 endpoint term。剩余两个 sums 都在完全相同的内部坐标
`x_1,...,x_{b-1}` 上求和：

\[
\frac Hn\ge
\frac1b\sum_{i=1}^{b-1}A_{\delta,\gamma_b}(x_i)-o(1),
\qquad
\frac Hn\ge
\frac1b\sum_{i=1}^{b-1}B_{\delta,\gamma_b}(x_i)-o(1).
\tag{23}
\]

函数 `A_{delta,gamma}` 严格凸，因为

\[
A_{\delta,\gamma}''(x)=\frac1{(x+\gamma)^2\ln2}>0.
\tag{24}
\]

函数 `B_{delta,gamma}` 凸。令
`y=1-delta x`、`z=1-x+gamma`，直接求导得

\[
B_{\delta,\gamma}''(x)
=\frac{(y-\delta z)^2}{y z^2\ln2}
=\frac{(1-\delta-\delta\gamma)^2}
{(1-\delta x)(1-x+\gamma)^2\ln2}\ge0.
\tag{25}
\]

令内部坐标平均值为

\[
\bar x=\frac1{b-1}\sum_{i=1}^{b-1}x_i.
\]

分别对 (23) 的两个正则化 sums 使用 Jensen，并用
相同因子 `(b-1)/b`，得到

\[
\frac Hn\ge\frac{b-1}{b}A_{\delta,\gamma_b}(\bar x)-o(1),
\qquad
\frac Hn\ge\frac{b-1}{b}B_{\delta,\gamma_b}(\bar x)-o(1).
\tag{26}
\]

定义

\[
C_{\delta,\gamma}
=\min_{0\le x\le1}
\max\{A_{\delta,\gamma}(x),B_{\delta,\gamma}(x)\}.
\tag{26a}
\]

于是无需假设 `A,B` 在 profile 平均点上一致有界，便直接得到

\[
\frac Hn\ge\frac{b-1}{b}C_{\delta,\gamma_b}-o(1).
\tag{26b}
\]

在任意 compact interior 上两函数一致收敛到 `A_delta,B_delta`。另一方面，
当 `gamma->0` 时，靠近 `0` 有 `A_{delta,gamma}->infinity`，靠近 `1` 有
`B_{delta,gamma}->infinity`；故所有极小点一致停留在某个 compact interior。
因此 `C_{delta,gamma}->C(delta)`。令 `b->infinity`、`gamma_b->0`，得到

\[
\frac Hn\ge
\max\{A_\delta(\bar x),B_\delta(\bar x)\}-o(1)
\ge C(\delta)-o(1),
\tag{27}
\]

即 Theorem 1。这个 argument 允许 profile 有任意 jumps；旧稿错误的逐区间
cross-average 已完全删除。

## 5. 一维极值

`A_delta` 严格递减。另一方面，令

\[
r=\frac{1-\delta x}{\delta(1-x)}>1.
\]

直接求导得

\[
B_\delta'(x)=\frac\delta{\ln2}(r-\ln r-1)>0.
\tag{28}
\]

所以 min--max 的唯一极小点是 `A_delta(x)=B_delta(x)` 的交点。对
`delta=1/2`，高精度求根给 (4)，共同函数值为 (5)。

正式数值 theorem 可用 interval arithmetic 给 `x_*` 和 `C(1/2)` 的有理包络；
数值不是证明主不等式所必需。

## 6. Hostile tests

### Frozen fixed-density mask

令 public tape 选择一个固定密度 mask，使许多 hit indicators 完全相关。式 (14)
联合发送 pattern 与 hit values，不逐坐标收费，所以仍成立。mask 的 block-local
质量只进入 `E g`；极端相关性不会击穿 perspective bound。

### Global ALL-YES coin

一个全局 coin 可同时改变全部 hit bits。证明从不下界 hit-vector entropy，也不把
memory 按 coin branch 平均。所有 first moments 都在原联合实验中计算，因此
fixed worst-case `H` 语义保持。

### Rare witnesses

full-fiber union 可以被大量 degree-one rare witnesses 污染。这个问题由 transport
loss 显式支付，并正是条件 `u >> n^2` 的来源。证明不把 union degree 当成 endpoint
概率，也没有用 incidence-weighted entropy 替代 union mass。

### Exact dictionary

full fiber 等于 exact current set。候选 difference 足够大以完成 code；所得下界远
低于 exact-set representation，不产生假超界。

### Exact fingerprint count vector 与 threshold quotient

`2.384499842n` exact count-vector 和 `2.349083440n` everlasting threshold quotient
都满足 (3)。本文没有推出超过已知 upper bound 的 `2.442695n`；那个错误值来自
把 partition-dependent reconstructible difference 当成 fixed set，而这里已由
full fiber 修复。

## 7. 为什么这个结论有论文价值

这个 theorem package 的核心不是将旧常数从 `1.199` 调到 `1.434`，而是三个可复用
结构：

1. **partition-free full-fiber transport** 修复 arbitrary non-monotone lifting；
2. **exact batch branch--support identity** 对任意 correlated hit pattern成立；
3. **endpoint-pivot symmetrization** 将 transition-constrained profile 压缩成一个
   显式一维变分，而不猜 fingerprint extremality。

剩余 gap 也很清楚。式 (5) 仍只利用 full-fiber union 的一阶 profile；若要逼近
`2.2--2.35` 的 ordinary upper bounds，必须加入 fiber thickness、core/transversal
profile 或更强的多 pivot extremal inequality。有限深度的全-pivot 数值实验显示
还有明显余量，但解析极限与可认证误差尚未证明，因此不进入本文定理或数值声明。
