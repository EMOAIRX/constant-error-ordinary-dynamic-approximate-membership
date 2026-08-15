# Masked binary canonical quotients 的 high-error matching converse

> 日期：2026-08-13。状态：解析证明。本文刻画一个自然的 exchangeable
> masked、load-preserving binary canonical quotient 类；结论不是 arbitrary
> dynamic AMQ lower bound。

所有对数以 2 为底。令

\[
\delta=1-\varepsilon\downarrow0
\]

表示固定 nonmember 必须获得的拒绝概率。

## 1. 模型

公共随机带把每个 key 独立分到有限个 tracked types
\(i=1,\ldots,r\) 或一个永久 YES type。type \(i\) 的概率质量为
\(\beta_i\)。在 type \(i\) 内：

- outer hash 均匀映到 \(B_i\) 个 blocks；
- inner binary symbol 的 bias 为 \(p_i\)；
- 每个 block 使用显式保持 exact load 的 deterministic canonical binary
  summary；
- query 采用 minimal one-sided rule。

由 lattice normal form，每个非退化、每层状态数一致有界的 type 都等价于
one-count modulo 某个整数 \(q_i\ge2\)。允许参数 \(q_i,p_i,\beta_i,B_i\)
依赖目标 \(\delta\)。全局 fixed state 对所有 types 作联合 enumerative coding，
并覆盖最坏情况下 total tracked load 至多 \(n\) 的全部 formal states。

记

\[
b_i=\frac{B_i}{n},
\qquad
\lambda_i=\frac{\beta_i n}{B_i}=\frac{\beta_i}{b_i}.
\tag{1}
\]

这里 \(\lambda_i\) 只控制一个固定 history 上的 probabilistic block load；
fixed-state enumeration 仍必须覆盖全部 \(n\) 个 live keys 都落入 tracked
types 的情况。

## 2. 每个 type 的拒绝效率至多 \(2/e\)

对 order-\(q\)、bias-\(p\) quotient，条件于 query 属于该 type，其 Poisson
拒绝概率为

\[
J_{q,p}(\lambda)
=e^{-\lambda}\sum_{c=0}^{q-1}\frac{\lambda^c}{c!}
\left[p(1-p)^c+(1-p)p^c\right].
\tag{2}
\]

去掉 threshold truncation 只能增加拒绝概率，因此

\[
J_{q,p}(\lambda)
\le
p e^{-\lambda p}+(1-p)e^{-\lambda(1-p)}.
\tag{3}
\]

### Lemma 2.1（universal efficiency bound）

对所有 \(\lambda>0\)、\(p\in[0,1]\) 和 \(q\ge2\)，

\[
\boxed{\lambda J_{q,p}(\lambda)\le\frac2e.}
\tag{4}
\]

**证明。** 令

\[
a=\lambda p,\qquad b=\lambda(1-p).
\]

由式 (3)，

\[
\lambda J_{q,p}(\lambda)
\le
a e^{-a}+b e^{-b}.
\]

函数 \(x e^{-x}\) 在 \(x\ge0\) 上的最大值为 \(1/e\)，故右侧至多
\(2/e\)。等号要求 \(a=b=1\)，即 \(\lambda=2,p=1/2\)，并且 threshold
truncation 渐近消失。 \(\square\)

type \(i\) 对总 pointwise rejection 的贡献为

\[
\delta_i=\beta_iJ_{q_i,p_i}(\lambda_i)
=b_i\lambda_iJ_{q_i,p_i}(\lambda_i).
\]

所以 Lemma 2.1 给出

\[
\delta=\sum_i\delta_i
\le\frac2e\sum_i b_i.
\tag{5}
\]

令 \(b=\sum_i b_i\)，则

\[
\boxed{b\ge\frac e2\,\delta.}
\tag{6}
\]

这个 bound 允许不同模数、不同 biases 和不同 conditional loads 的任意有限
混合；mixture 不能超过单 type 的最佳 rejection-per-block efficiency。

## 3. Fixed-state 极点下界

order-\(q_i\) binary quotient 的 local state OGF 是

\[
A_{q_i}(z)=\frac{1-z^{q_i}}{(1-z)^2}
=\frac{1+z+\cdots+z^{q_i-1}}{1-z}.
\tag{7}
\]

因此对每个 \(0<z<1\)，

\[
A_{q_i}(z)\ge\frac1{1-z}.
\tag{8}
\]

联合 enumerative state rate 为

\[
S
=\min_{0<z<1}
\left\{
\sum_i b_i\log_2 A_{q_i}(z)-\log_2z
\right\}.
\tag{9}
\]

由式 (8)，

\[
S\ge
\min_{0<z<1}
\left\{
b\log_2\frac1{1-z}-\log_2z
\right\}.
\tag{10}
\]

右侧在 \(z=1/(1+b)\) 取到最小值，等于

\[
\Psi(b)
=(1+b)\log_2(1+b)-b\log_2b.
\tag{11}
\]

\(\Psi\) 严格递增，并且

\[
\Psi(b)=b\log_2\frac1b+O(b)
\qquad(b\downarrow0).
\tag{12}
\]

结合式 (6)，得到

\[
S\ge
\Psi\!\left(\frac e2\delta\right)
=\left(\frac e2-o(1)\right)
\delta\log_2\frac1\delta.
\tag{13}
\]

这里不需要假设 \(q_i\) 一致有界：式 (8) 对所有 \(q_i\ge2\) uniform 成立。
若 types 数随 \(\delta\) 变化，只要每个有限 \(n\) 的构造使用有限个 types，
同一推导逐点成立。

## 4. Matching theorem

### Theorem 4.1

在 Section 1 的全部 exchangeable masked、显式保持 exact load 的 deterministic
canonical binary quotient filters 中，

\[
\boxed{
R_{\rm class}(1-\delta)
=
\left(\frac e2+o(1)\right)
\delta\log_2\frac1\delta.
}
\tag{14}
\]

**证明。** 下界是式 (13)。上界由 masked threshold construction 得到：取
uniform inner bits，令 \(q\) 先足够大，再令 \(\delta\downarrow0\)。其

\[
M_q=\max_{\lambda>0}\lambda
e^{-\lambda}\sum_{c=0}^{q-1}\frac{(\lambda/2)^c}{c!}
\uparrow
\max_{\lambda>0}\lambda e^{-\lambda/2}
=\frac2e.
\]

同时 fixed-state rate 为

\[
S_q(b)=b\log_2(1/b)+b\log_2q+O_q(b),
\qquad
b=\delta/M_q.
\]

先固定 \(q\)，再令 \(\delta\to0\)，最后令 \(q\to\infty\)，给出 matching
upper bound。 \(\square\)

## 5. 结论意义与边界

式 (14) 把此前的 factor-two upper bound 升级为 natural class 内的 sharp
theorem。它说明 \(e/2\) 来自两个不可同时突破的结构限制：

1. 一个 binary tracked block 对 pointwise rejection 的效率至多 \(2/e\)；
2. 每个 load-preserving reversible quotient 至少有一个 simple-pole family
   的 reachable states，迫使 \(b\log(1/b)\) fixed-state cost。

该 converse 覆盖：

- 任意 public exchangeable permanent-YES mask；
- 任意有限 mixture of tracked block types；
- 每个 type 任意 bias、modulus 和 conditional load；
- 由 lattice normal form 包含的所有 load-preserving deterministic canonical
  binary summaries；
- worst-case total tracked load \(n\) 的联合 enumerative coding。

它不覆盖：

- \(K>2\) inner alphabets；
- 跨 load merging 的 lattices；
- history-dependent/multiple representations；
- randomized local transitions；
- 跨 blocks 的非canonical global state；
- arbitrary ordinary dynamic AMQs。

因此安全表述是“masked load-preserving canonical binary class 的精确
high-error rate”，不能写成所有 dynamic filters 的最优高误差率。
