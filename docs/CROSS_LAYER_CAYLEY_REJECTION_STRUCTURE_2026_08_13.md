# Cayley quotient 的跨层 rejection 结构

> 日期：2026-08-13。状态：本文中的事件嵌套、几何衰减和 weighted-class
> identity 都是解析定理。它们严格排除了此前 entropy relaxation 的显式假
> profile，但与 entropy--distortion inequality 联合后仍不足以推出
> (2.349083\ldots) 的全 (K) converse。

## 1. 模型

令 (X_1,X_2,\ldots,A) 独立均匀于 ([K])，并令

\[
S_c=v_{X_1}+\cdots+v_{X_c}\in G,
\qquad V=\{v_1,\ldots,v_K\}\subseteq G,
\]

其中 (G) 是 finite Abelian group。minimal one-sided query 在 load (c)
接受 symbol (a) 当且仅当

\[
S_c-v_a\in(c-1)V.
\]

写 rejection event 为

\[
E_c(a)=\{S_c-v_a\notin(c-1)V\},
\qquad \rho_c=\Pr[E_c(A)].
\]

## 2. 跨层事件嵌套

### Theorem 2.1（pathwise deletion projection）

对每个固定 (a) 和每条 symbol sequence，

\[
E_{c+1}(a)
\subseteq E_c(a)\cap\{X_{c+1}\ne a\}.
\tag{1}
\]

因此

\[
\boxed{
\rho_{c+1}\le\left(1-\frac1K\right)\rho_c,
}
\tag{2}
\]

并由 (rho_0=1) 得

\[
\boxed{
\rho_c\le\left(1-\frac1K\right)^c.
}
\tag{3}

**证明。** 若 (X_{c+1}=a)，则
(S_{c+1}-v_a=S_c\in cV)，所以 (a) 必被接受。若 (a) 在第 (c) 层
已被接受，则存在 (t\in(c-1)V) 使 (S_c-v_a=t)。于是

\[
S_{c+1}-v_a=t+v_{X_{c+1}}\in cV,
\]

故在第 (c+1) 层仍被接受。这证明式 (1)。因为 (X_{c+1}) 独立于
((X_1,\ldots,X_c,A))，取概率即得式 (2)，迭代得式 (3)。证毕。

式 (3) 比“query symbol 没在真实 composition 中出现”更强，因为式 (2)
给出逐层 hazard constraint，而不仅是每层独立 upper bound。composition-
injective walk 对所有未饱和 layers 取等号。

### Corollary 2.2（显式 formal obstruction 被排除）

此前 entropy relaxation 允许 binary profile

\[
(\rho_0,\rho_1,\rho_2,\ldots)=(1,1/2,1/2,0,\ldots).
\]

Theorem 2.1 强迫

\[
\rho_2\le\frac12\rho_1=\frac14,
\]

所以该 profile 不可能来自任何 finite-Abelian Cayley quotient。这里不需要
binary lattice 的完整分类。

## 3. Composition classes 的精确 identity

固定 load (c)。令

\[
\mathcal C_{K,c}=\{m\in\mathbb N^K:|m|=c\}
\]

为 composition space，并按 syndrome 划分 equivalence classes

\[
m\sim_c m'
\iff
\sum_i m_iv_i=\sum_i m_i'v_i.
\]

对一个 class (C)，定义其 support union

\[
U(C)=\bigcup_{m\in C}\operatorname{supp}(m).
\]

令 multinomial weight

\[
w_c(m)=\frac{c!}{K^c\prod_i m_i!},
\qquad W_c(C)=\sum_{m\in C}w_c(m).
\]

### Theorem 3.1（weighted class-union formula）

load-(c) rejection 恰为

\[
\boxed{
\rho_c
=1-\frac1K
\sum_{C\in\mathcal C_{K,c}/\sim_c}
W_c(C)|U(C)|.
}
\tag{4}

等价地，若

\[
a_c=\left(1-\frac1K\right)^c
\]

是 exact-composition absence probability，则 quotient 相对 exact composition
损失的 rejection 恰为

\[
\boxed{
a_c-\rho_c
=\frac1K\sum_C\sum_{m\in C}w_c(m)
|U(C)\setminus\operatorname{supp}(m)|.
}
\tag{5}

**证明。** 给定 syndrome class (C)，zero false negatives 强迫接受
(U(C)) 中的每个 symbol，而 minimal rule 不接受其余 symbols。因此 conditional
acceptance probability 是 (|U(C)|/K)。按 class probability (W_c(C))
平均即得式 (4)。若知道 exact composition (m)，acceptance probability 是
(|\operatorname{supp}(m)|/K)。对 multinomial composition 平均，rejection
是 (a_c)。两者相减即得式 (5)。证毕。

式 (5) 把“跨层 congruence 导致的 query distortion”精确变成 weighted
clustering cost：合并 compositions 只有在它们 supports 高度重叠时才便宜。
同时这些 partitions 不能逐层任意选择；它们必须全部由同一个 lattice
(L\le A_{K-1}) 的 cosets 给出。

## 4. 与 entropy--distortion inequality 的联合边界

令 (d_c=|cV|)。已有联合熵界给出

\[
d_c\ge
\left\lceil
\exp\sum_{i=1}^c
[\log K-\phi_K(K(1-\rho_i))]
\right\rceil,
\tag{6}
\]

其中 (phi_K) 是穿过 ((j,\log j)) 的 concave piecewise-linear envelope。
Theorem 2.1 再加入

\[
0\le\rho_{c+1}\le(1-1/K)\rho_c.
\tag{7}
\]

这是目前无需分类 (L) 就能证明的最强通用 scalar relaxation。它确实排除
固定 (rho_c\approx1/2) 很多层而 entropy 缓慢增长的旧假 profile。

但是式 (6)--(7) 仍不足以证明 binary (q=3) 全局最优。原因是它们仍允许
把每一步的 mutual-information lower bound 和 geometric rejection ceiling
几乎同时取等号，却没有支付同一个 lattice 在所有 layers 上产生这些
partitions 的代价。数值变分会产生低于 (2.349083\ldots) 的形式 profiles；
它们尚未发现真实 ((G,V)) realization。

## 5. 自然真实子类的反例搜索

对 product-modulus lattice

\[
G=\mathbb Z_{q_1}\times\cdots\times\mathbb Z_{q_{K-1}},
\qquad
V=\{0,e_1,\ldots,e_{K-1}\},
\]

可以精确枚举全部 reachable syndromes、式 (4) 的 rejection 以及 OGF rate。
在 ternary (2\le q_1\le q_2\le15) 的枚举中，最佳为

\[
(q_1,q_2)=(3,4),
\]

其 profile 是

\[
d=(1,3,6,9,11,12,12,\ldots),
\]

\[
\rho=(1,2/3,4/9,22/81,\ldots),
\]

并给出

\[
R=2.3525841337\ldots>2.3490834402\ldots.
\]

这与更广的小循环群枚举一致，但有限枚举不是全 lattice converse。

## 6. 准确剩余命题

要闭合 (K>2) sharp converse，需要一个真正使用同一 lattice 的 theorem，形式
应类似：若式 (4) 的 clustering cost 在若干低 layers 很小，则相应 class
partitions 必须在这些 layers 近 composition-injective；于是

\[
d_c\gtrsim {c+K-1\choose K-1}.
\]

反之，若 (d_c) 明显低于 composition count，则式 (5) 必须给出足够大的
rejection loss。所需的是一个 **weighted lattice-coset clustering inequality**，
不是单独的 Kneser sumset bound或单层 additive-energy bound。

目前最强的严格结论是 Theorems 2.1 与 3.1：前者控制跨层 hazard，后者精确刻画
每层 quotient distortion。它们把开放部分缩小为同一个 lattice 对多层 weighted
composition partitions 的兼容性，但尚未推出 (R\ge2.349083\ldots)。
