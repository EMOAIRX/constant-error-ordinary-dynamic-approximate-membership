# Permanent-YES mask 在 half error 不改善 binary canonical optimum

> 日期：2026-08-13。状态：解析定理。对任意 threshold order \(q\ge2\)、任意
> binary bias \(p\in[0,1]\) 和任意 permanent-YES mask，若总 rejection 至少
> \(1/2\)，则 mask 后的 effective load 不超过相同 \((q,p)\) 的 unmasked
> half-error root。因此结合 biased-binary unmasked theorem，全类最优仍唯一是
> \(q=3,p=1/2\)，rate 为 \(2.349083440193\ldots\) bits/key。

本文只讨论 exact-load、binary deterministic canonical threshold quotients 的
blockwise fixed-state rate。它不外推到 multisymbol、cross-load merge 或
history-dependent summaries。

## 1. 参数消元

固定 \(q\ge2\) 与 bias \(p\in[0,1]\)，写 \(r=1-p\)。条件于 tracked query
所在 block 有 \(c<q\) 个 members，query symbol 缺席的概率是

\[
a_c=p r^c+r p^c,
\qquad a_0=1.
\tag{1}
\]

load \(c\ge q\) 时 threshold quotient 全部回答 `YES`。因此 tracked query 在
Poisson mean load \(\lambda\) 下的 rejection 是

\[
\boxed{
J_{q,p}(\lambda)
=e^{-\lambda}\sum_{c=0}^{q-1}
\frac{\lambda^c}{c!}a_c.
}
\tag{2}

令 public mask 以概率 \(\beta\) 跟踪 key，其他 keys 永久回答 `YES`。总 rejection
为 \(\beta J_{q,p}(\lambda)\)。为了恰好达到 half error，最省 tracked mass 的
校准是

\[
\beta=\frac1{2J_{q,p}(\lambda)},
\tag{3}
\]

其可行条件恰为

\[
J_{q,p}(\lambda)\ge\frac12.
\tag{4}

因为 tracked block mean 满足 \(\lambda=\beta n/B\)，所以

\[
\frac Bn=\frac\beta\lambda
=\frac1{2\lambda J_{q,p}(\lambda)}.
\]

定义 effective load

\[
\boxed{
\mu(\lambda)=2\lambda J_{q,p}(\lambda).
}
\tag{5}

则 fixed-state rate 正是相同 order-\(q\) OGF 在 block density \(1/\mu\) 下的
rate，记为 \(R_q(\mu)\)。已知 \(R_q(\mu)\) 严格随 \(\mu\) 下降。因此 mask 是否
有益，完全等价于式 (5) 能否超过 unmasked half-error root。

## 2. 两个基础单调性

### Lemma 2.1（\(J_{q,p}\) 严格下降）

对任意非退化参数，\(J_{q,p}(\lambda)\) 严格随 \(\lambda>0\) 下降，并存在唯一
正根 \(\lambda_{q,p}\) 满足

\[
J_{q,p}(\lambda_{q,p})=\frac12.
\tag{6}

**证明。** 令 \(C_\lambda\sim\operatorname{Pois}(\lambda)\)，并把

\[
f(c)=a_c\mathbf1\{c<q\}.
\]

序列 \(a_c=p r^c+r p^c\) 非增，且 truncation 后最终为零，所以 \(f\) 非增且
非恒定。Poisson variables 可按 \(C_{\lambda'}=C_\lambda+Z\) coupling，其中
\(Z\) 为独立正均值 Poisson，得到 expectation 严格下降。又
\(J(0)=1\)、\(J(\lambda)\to0\)，故唯一根存在。\(\square\)

### Lemma 2.2（可行域位于 \(2\ln2\) 以下）

若 \(J_{q,p}(\lambda)\ge1/2\)，则

\[
\lambda\le2\ln2<2.
\tag{7}

**证明。** 去掉 threshold truncation 得

\[
J_{q,p}(\lambda)
\le U_p(\lambda)
:=p e^{-\lambda p}+r e^{-\lambda r}.
\tag{8}

对 \(0\le\lambda\le2\)，函数 \(U_p(\lambda)\) 关于 \(p\) 在 \(1/2\) 取得
最大值，故

\[
U_p(\lambda)\le e^{-\lambda/2}.
\tag{9}

为完整起见，令左侧关于 \(p\) 的函数为 \(F_\lambda(p)\)，则

\[
F_\lambda''(p)
=\lambda e^{-\lambda p}(\lambda p-2)
+\lambda e^{-\lambda r}(\lambda r-2)\le0.
\]

它关于 \(p=1/2\) 对称，故式 (9) 成立。

还需排除 \(\lambda>2\) 才能无循环地使用式 (9)。对固定 \(p\)，
\(U_p(\lambda)\) 随 \(\lambda\) 下降；而式 (9) 在 \(\lambda=2\) 给

\[
U_p(2)\le e^{-1}<\frac12.
\]

所以 \(\lambda\ge2\) 不可能满足式 (4)。现在 \(\lambda<2\)，由

\[
\frac12\le J_{q,p}(\lambda)\le e^{-\lambda/2}
\]

立即得到式 (7)。\(\square\)

## 3. 核心导数不等式

### Theorem 3.1（\(\lambda J\) 在可行域严格递增）

对所有 \(q\ge2\)、\(p\in[0,1]\)，在

\[
\{\lambda>0:J_{q,p}(\lambda)\ge1/2\}
\]

上，函数

\[
F(\lambda)=\lambda J_{q,p}(\lambda)
\]

严格递增。

**证明。** 记

\[
T=\sum_{c=1}^{q-1}\frac{\lambda^c}{c!}a_c.
\]

由式 (2) 直接求导：

\[
e^\lambda F'(\lambda)
=\sum_{c=0}^{q-1}
\frac{\lambda^c}{c!}a_c(c+1-\lambda).
\tag{10}

Lemma 2.2 给 \(\lambda\le2\ln2<2\)。所以对所有 \(c\ge1\)，

\[
c+1-\lambda\ge2-\lambda>0.
\]

分离 \(c=0\) 项，并使用可行性

\[
e^{-\lambda}(1+T)=J_{q,p}(\lambda)\ge\frac12,
\qquad
T\ge\frac{e^\lambda}{2}-1,
\tag{11}

得到

\[
\begin{aligned}
e^\lambda F'(\lambda)
&\ge1-\lambda+(2-\lambda)T\\
&\ge1-\lambda+(2-\lambda)
\left(\frac{e^\lambda}{2}-1\right)\\
&=\frac{(2-\lambda)e^\lambda}{2}-1.
\end{aligned}
\tag{12}

最后证明式 (12) 的右侧在 \([0,2\ln2]\) 非负。令

\[
h(\lambda)=\lambda+\ln(2-\lambda)-\ln2.
\]

则

\[
h'(\lambda)=\frac{1-\lambda}{2-\lambda}.
\]

所以 \(h\) 在 \([0,1]\) 上增加，在 \([1,2\ln2]\) 上下降。两个端点满足

\[
h(0)=0,
\qquad
h(2\ln2)
=\ln\bigl(2(2-2\ln2)\bigr)>0.
\]

故 \(h(\lambda)>0\) 对所有 \(0<\lambda\le2\ln2\) 成立，等价于

\[
(2-\lambda)e^\lambda>2.
\]

代回式 (12) 得 \(F'(\lambda)>0\)。\(\square\)

这个证明没有使用 \(q\) 或 \(p\) 的特殊数值；threshold truncation 和 arbitrary
bias 都被式 (11) 吸收。

## 4. Mask 不改善同一 \((q,p)\)

### Corollary 4.1（effective-load domination）

对任意满足式 (4) 的 \(\lambda\)，

\[
\boxed{
\mu(\lambda)
=2\lambda J_{q,p}(\lambda)
\le\lambda_{q,p}.
}
\tag{13}

等号当且仅当 \(\lambda=\lambda_{q,p}\)，此时

\[
J_{q,p}(\lambda)=\frac12,
\qquad \beta=1.
\]

**证明。** Lemma 2.1 给可行域
\(0<\lambda\le\lambda_{q,p}\)。Theorem 3.1 给

\[
\lambda J_{q,p}(\lambda)
\le
\lambda_{q,p}J_{q,p}(\lambda_{q,p})
=\frac{\lambda_{q,p}}2.
\]

乘以 2 即得式 (13)。严格性来自 Theorem 3.1。\(\square\)

因为 \(R_q(\mu)\) 严格下降，式 (13) 立刻给

\[
R_q(\mu(\lambda))
\ge R_q(\lambda_{q,p}).
\tag{14}

所以对每个固定 \((q,p)\)，任何非平凡 permanent-YES mask 都严格增加空间率。

## 5. 与 binary unmasked theorem 合并

已有 biased-binary theorem 证明，在所有 exact-load deterministic canonical
binary summaries、任意 finite threshold \(q\ge2\)、任意 bias \(p\in[0,1]\)
中，unmasked half-error rate 的唯一最优非退化参数是

\[
q=3,
\qquad p=\frac12,
\]

其值为

\[
R_3(\lambda_{3,1/2})
=2.349083440193141\ldots\text{ bits/key}.
\tag{15}

结合式 (14)，得到：

### Theorem 5.1（masked biased-binary sharp optimum）

在下列 class 中：

- public permanent-YES mask；
- tracked keys 使用任意 biased binary hash；
- exact-load deterministic canonical key-only quotient；
- minimal one-sided query；
- blockwise fixed-state enumerative coding；

half-error 的唯一非退化最优参数是

\[
\boxed{
\beta=1,
\qquad q=3,
\qquad p=\frac12,
}
\]

且最优率仍为式 (15)。换言之，在 \(\varepsilon=1/2\) 时，permanent-YES mask
不仅不能改善 \(2.349083\)，任何真正丢弃正质量 keys 的 mask 都严格更差。

## 6. 模型边界

本定理关闭了 binary canonical family 中一个真实缺口：此前 high-error endpoint
的 mask 有用，不能仅凭直觉断言 half error 时也无用。这里的结论来自特定的
half-error 可行域和式 (12)，不是一般 error 的单调性。

它没有覆盖：

1. 不同 block types 的全局 heterogeneous mixture；若允许各类型承担不同份额的
   rejection，需要额外的 convex-envelope argument。
2. multisymbol quotients；其 absence coefficients 和 OGF 都不同。
3. cross-load merge、cross-block encoding 或 history-dependent multiple states。
4. 非 permanent 的 adaptive mask 或随 history 改变 tracked status 的结构。

特别地，Theorem 5.1 仍是 restricted converse，不能升级成 ordinary dynamic AMQ
的全局 \(2.349083n\) 下界。
