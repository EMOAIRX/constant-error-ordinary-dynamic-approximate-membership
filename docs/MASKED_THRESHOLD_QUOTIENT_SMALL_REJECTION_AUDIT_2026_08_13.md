# Masked threshold quotient 的 small-rejection 上界

> 日期：2026-08-13。状态：构造语义与一阶渐近已核查。本文修正了一个关键
> 计费错误：公共 mask 不会把 worst-case tracked capacity 从 \(n\) 降到
> \(\beta n\)。修正后，前导 factor-two 改进仍然成立，但理由来自 threshold
> quotient 在高 block load 下的状态饱和。

以下写

\[
\delta=1-\varepsilon
\]

为每个固定 nonmember 必须得到的最小拒绝概率。关心
\(\delta\downarrow0\)。

## 1. 构造

公共随机带提供相互独立的：

- mask \(m:U\to\{0,1\}\)，其中
  \(\Pr[m(x)=1]=\beta\)；
- outer hash \(g:U\to[B]\)；
- uniform inner bit \(h:U\to\{0,1\}\)。

若 \(m(x)=0\)，称 \(x\) 为 untracked。它不改变持久状态，query 永远回答
YES。若 \(m(x)=1\)，则按 order-\(q\) threshold quotient 更新 block
\(g(x)\)：保存 block load 与 inner-one-count modulo \(q\)。query 在 load
\(c<q\) 时按精确 binary multiset 回答，在 \(c\ge q\) 时回答 YES。

成员若 untracked 则直接接受；若 tracked，则由 threshold quotient 的 zero-FN
保证接受。因此整个结构 zero-FN。Insert/Delete 只加减被更新 key 的公开
mask、block 与 bit label，支持 key-only deletion 和任意长合法历史。

## 2. 精确 pointwise rejection

固定任意合法历史的当前集合 \(S\)，令 \(s=|S|\le n\)，并固定
\(x\notin S\)。query 被拒绝首先要求 \(m(x)=1\)，概率为 \(\beta\)。
条件于此，

\[
C=|\{y\in S:m(y)=1,\ g(y)=g(x)\}|
\sim\operatorname{Bin}\left(s,\frac{\beta}{B}\right).
\]

条件于 \(C=t<q\)，query bit 在全部 \(t\) 个 member bits 中缺席的概率为
\(2^{-t}\)；\(C\ge q\) 时拒绝概率为零。因此有限 \(n\) 的精确式是

\[
\Pr[\mathrm{NO}]
=\beta\sum_{t=0}^{q-1}
\binom st
\left(\frac{\beta}{B}\right)^t
\left(1-\frac{\beta}{B}\right)^{s-t}2^{-t}.
\tag{1}
\]

右侧随 \(s\) 非增，所以只需在 \(s=n\) 校准。若

\[
\lambda=\frac{\beta n}{B},
\]

则 Poisson 极限为

\[
\Pr[\mathrm{NO}]
\longrightarrow
\beta F_q(\lambda),
\qquad
F_q(\lambda)
=e^{-\lambda}\sum_{t=0}^{q-1}\frac{(\lambda/2)^t}{t!}.
\tag{2}
\]

这是对每条固定 history、每个固定 nonmember、关于公共随机带的 pointwise
保证，不是平均 query distribution 保证。

## 3. Fixed-state 计费的关键修正

不能把 tracked capacity 写成 \(\beta n\)。对每条固定公共 tape，存在合法
key sequence 使全部 \(n\) 个 live keys 都满足 \(m(x)=1\)。fixed persistent
memory 必须覆盖这条 history；否则结构存在 tape-dependent overflow。

所以状态 rank 必须枚举

\[
\sum_{j=1}^B c_j\le n,
\]

而不是 \(\sum_jc_j\le\beta n\)。order-\(q\) local OGF 是

\[
A_q(z)=\frac{1-z^q}{(1-z)^2}.
\tag{3}
\]

令

\[
b=\frac Bn=\frac{\beta}{\lambda}.
\]

正确的一阶 fixed-state rate 是

\[
\boxed{
S_q(b)
=\min_{0<z<1}
\left\{
b\log_2A_q(z)-\log_2z
\right\},
}
\tag{4}
\]

其 saddle 满足

\[
\frac{zA_q'(z)}{A_q(z)}=\frac1b.
\tag{5}
\]

特别地，saddle mean 是 \(n/B=1/b=\lambda/\beta\)，不是 conditional
probabilistic load \(\lambda\)。前者来自 worst-case state enumeration，后者
只用于固定 history 上的 FPR；混淆两者会得到错误空间公式。

## 4. 为什么修正后 factor two 仍成立

对每个固定 \(q\)，当 \(b\downarrow0\) 时式 (5) 的 saddle \(z\uparrow1\)。
对 fixed \(q\)，由

\[
A_q(z)=\frac{1-z^q}{(1-z)^2}
\sim\frac q{1-z}
\]

和式 (5) 可得

\[
1-z=b+O_q(b^2).
\]

代回式 (4)：

\[
S_q(b)
=b\log_2\frac1b+b\log_2q+O_q(b).
\tag{6}
\]

定义

\[
M_q=\max_{\lambda>0}\lambda F_q(\lambda).
\tag{7}
\]

在式 (2) 取等号 \(\delta=\beta F_q(\lambda)\) 时，

\[
b=\frac{\beta}{\lambda}
=\frac{\delta}{\lambda F_q(\lambda)}.
\]

所以固定 \(q\) 最优选择式 (7) 的 maximizer，得到

\[
S_q
=\frac{\delta}{M_q}\log_2\frac1\delta+O_q(\delta).
\tag{8}
\]

由于 \(F_q(\lambda)\uparrow e^{-\lambda/2}\)，

\[
M_q\uparrow
\max_{\lambda>0}\lambda e^{-\lambda/2}
=\frac2e,
\tag{9}
\]

且唯一极限 maximizer 是 \(\lambda=2\)。先固定足够大的 \(q\)，再令
\(\delta\to0\)，最后对 \(q\) 作对角选择，式 (8)--(9) 给出

\[
\boxed{
\limsup_{\delta\downarrow0}
\frac{R_{\rm masked}(\delta)}
{\delta\log_2(1/\delta)}
\le\frac e2.
}
\tag{10}
\]

等价地，

\[
R_{\rm masked}(\delta)
\le
\left(\frac{e}{2\ln2}+o(1)\right)
\delta\ln\frac1\delta.
\tag{11}
\]

如果此前 exact heterogeneous fingerprint benchmark 的前导系数确为
\(e/\ln2\)，式 (11) 在前导项上严格改善 factor two。这个 benchmark 比较仍应
单独核对文献和模型；式 (10) 本身不依赖该比较。特别地，这不是相对于所有
static AMQ 的 factor-two 改进。高误差 finite-universe/static covering 的最优
率可能只有 \(O(\delta)\)，不能把某个 fingerprint benchmark 误称为一般静态
信息论下界。

## 5. 有限 \(n\) 与无限历史

对给定 \(\delta,q,\beta,\lambda\)，先固定这些常数，再取
\(B=\lceil\beta n/\lambda'\rceil\)，其中 \(\lambda'<\lambda\) 且
\(\lambda-\lambda'=o(1)\) 选择得足以吸收 rounding 与 Binomial--Poisson
误差。由式 (1) 对 \(s\) 的单调性，可令 \(n\) 足够大时最坏 rejection 至少为
\(\delta\)。这只改变 \(o(n)\) 空间。持久 rank 覆盖全部 total tracked loads
至多 \(n\)，
所以：

- 不依赖 tracked count concentration；
- 不限制 history 长度；
- 不需要 union bound over time；
- 不存在 overflow/failure state；
- high-load churn 通过 modulo-\(q\) 逆更新在降回低层后自动恢复。

公共 mask 与 hashes 是免费只读随机带的一部分，不是 instance-specific seed，
因而无需计入 persistent bits。式 (1) 使用的标准量词是：先固定一个不依赖该
随机带的合法 history 与固定 nonmember，再对随机带取概率。若 adversary 先读
完整公共 tape，再选择 keys，则它可以专门选择 untracked query，FPR 保证失败；
本构造不提供这种 stronger public-coin-adaptive guarantee。state-capacity
论证则是 pathwise 的，确实覆盖所有 tapes 与 histories；不能用这一点反推更强
的 FPR 量词。

对 endpoint 渐近可避免任何 \(q=q(n)\) 的 uniform local-limit 问题：给定目标
精度 \(\eta>0\)，先固定有限 \(q=q(\eta)\) 使
\(M_q\ge2/e-\eta\)，再令 \(\delta\to0\)，最后令 \(\eta\to0\)。对每个阶段
\(q\) 都是常数，式 (6) 的 \(O_q(b)\) 与有限-\(n\) saddle asymptotic 均合法。
若要在单一 joint limit 中显式写 \(q(\delta)\)，还需给 uniform error bound；
本文不依赖该写法。

## 6. 参数形状

有限 \(\delta\) 时不应直接取很大的 \(q\)。修正公式的粗数值优化显示：

- \(\delta=1/2\) 回到 \(q=3,\beta=1\)，rate \(2.34908\ldots\)；
- \(\delta=0.1\) 仍约由 \(q=3\) 最优；
- \(\delta=0.01\) 与 \(0.001\) 附近 \(q=4\) 已更好；
- 只有在真正的 \(\delta\to0\) 极限中，最优 \(q\) 才缓慢发散。

因此“渐近取 \(q\to\infty\)”与“现实参数由 \(q=4/5\) 最优”并不矛盾。

## 7. 结论边界

严格成立的是新的 ordinary fixed-state upper-bound family 及式 (10)。尚未建立：

- 对任意 ordinary dynamic AMQ 的 matching lower bound；
- 在 masked-threshold family 内的完整有限-\(\delta\) phase diagram；
- biased inner symbols 是否能改善 \(M_q\)；
- 与所有已有 high-error AMQ constructions 的完整 priority audit；
- time-efficient rank/unrank implementation。

最重要的 conceptual point 是：永久 mask **没有**缩小 worst-case capacity。
空间下降来自 high-load threshold quotient 把每个 block 的 local states 饱和到
\(q\)，从而让 \(B=\Theta(\delta n)\) 个 blocks 仍能用 fixed memory 覆盖最多
\(n\) 个 tracked keys。
