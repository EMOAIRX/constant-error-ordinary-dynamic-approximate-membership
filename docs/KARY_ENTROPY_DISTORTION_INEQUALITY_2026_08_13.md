# 多符号 Abelian quotient 的联合熵--拒绝不等式

> 日期：2026-08-13。状态：核心不等式为解析定理；其后的数值 relaxation
> 只用于审计 sharp converse 是否已经闭合。结论是：该不等式第一次把
> sumset growth 与 query distortion 联合起来，但它单独仍不足以证明
> `2.349083...` 的全 (K) converse。

## 1. 模型

令 (X_1,X_2,\ldots) 独立且均匀分布于 alphabet ([K])，并把 symbols
映为有限 Abelian 群 (G) 中的不同 elements

\[
V=\{v_1,\ldots,v_K\}.
\]

定义 random-walk syndrome

\[
S_c=v_{X_1}+\cdots+v_{X_c},
\qquad d_c=|cV|.
\tag{1}
\]

给定 state (s\in cV)，minimal one-sided query 必须接受的 symbol set 是

\[
P_c(s)=\{a\in[K]:s-v_a\in(c-1)V\}.
\tag{2}
\]

令 fresh uniform query 被拒绝的平均概率为

\[
\rho_c
=1-\frac1K\mathbb E|P_c(S_c)|.
\tag{3}
\]

这正是 Poisson FPR 公式中 occupancy-(c) layer 的 rejection。

## 2. 核心定理

### Theorem 2.1（entropy--distortion increment）

对每个 (c\ge1)，

\[
\boxed{
H(S_c)-H(S_{c-1})
\ge \log K-\mathbb E\log |P_c(S_c)|
\ge-\log(1-\rho_c).
}
\tag{4}
\]

这里 logarithm 的底任意，但必须一致。因此

\[
\boxed{
\log d_c
\ge H(S_c)
\ge\sum_{i=1}^c-\log(1-\rho_i),
}
\tag{5}
\]

即

\[
\boxed{
d_c\ge\prod_{i=1}^c(1-\rho_i)^{-1}.
}
\tag{6}

**证明。** 因为 (S_c=S_{c-1}+v_{X_c})，

\[
H(S_c)-H(S_{c-1})
=I(X_c;S_c)
=H(X_c)-H(X_c\mid S_c).
\]

条件于 (S_c=s)，symbol (X_c) 的 posterior support 包含于
(P_c(s))，所以

\[
H(X_c\mid S_c=s)\le\log|P_c(s)|.
\]

取期望得到式 (4) 的第一项。再由 Jensen 与式 (3)，

\[
\mathbb E\log |P_c(S_c)|
\le\log\mathbb E|P_c(S_c)|
=\log(K(1-\rho_c)),
\]

得到第二项。对 (c) telescoping，并用 (H(S_0)=0) 和
(H(S_c)\le\log|cV|)，即得式 (5)--(6)。证毕。

这个证明没有分别极值化 (|cV|) 与 (rho_c)。它直接使用 posterior
ambiguity，所以避开了单独使用 Cauchy--Davenport 的根本缺口。

## 3. 整数 posterior 的严格加强

Jensen 在 (|P_c(S_c)|) 非常小的时候会损失。定义 (phi_K:[1,K]\to
[0,\log K]) 为穿过整数点

\[
(j,\log j),\qquad j=1,\ldots,K
\]

的分段线性函数。因为随机变量 (M\in\{1,\ldots,K\}) 在给定均值时使
(\mathbb E\log M) 最大的分布只支撑于相邻两个整数，得到

\[
\mathbb E\log|P_c(S_c)|
\le \phi_K(K(1-\rho_c)).
\]

因此有更强的

\[
\boxed{
H(S_c)-H(S_{c-1})
\ge \log K-\phi_K(K(1-\rho_c)).
}
\tag{7}

及

\[
\boxed{
d_c\ge
\left\lceil
\exp\left(
\sum_{i=1}^c
[\log K-\phi_K(K(1-\rho_i))]
\right)
\right\rceil.
}
\tag{8}

式 (7) 在 posterior size 恒定时取等号；它把 support cardinality 的整数性
纳入了联合界。

## 4. Binary threshold 的 sharp sanity check

对 order-(3) binary quotient，

\[
(\rho_1,\rho_2,\rho_3,\ldots)
=\left(\frac12,\frac14,0,\ldots\right).
\]

式 (6) 给

\[
d_1\ge2,
\qquad d_2\ge\frac83,
\]

结合 (d_c\in\mathbb N) 得 (d_1\ge2,d_2\ge3)。以后增量为零，且
sumsets 不能缩小，所以得到 profile

\[
(d_0,d_1,d_2,d_3,\ldots)\ge(1,2,3,3,\ldots),
\]

正好由 (G=\mathbb Z_3,V=\{0,1\}) 取等号。因此该不等式在已知 binary
optimizer 上没有常数损失。

## 5. 为什么它尚未给出全 (K) converse

half-error 的 Poisson rejection constraint 是

\[
e^{-\lambda}\sum_{c\ge0}\frac{\lambda^c}{c!}\rho_c=\frac12,
\qquad \rho_0=1.
\tag{9}

若只保留式 (8)、

\[
0\le\rho_c\le1,\qquad d_c\in\mathbb N,
\]

再把 tail (d_c) 乐观地冻结，所得 relaxation 仍允许不存在于任何真实
sumset walk 的 profiles。例如它允许许多连续 layers 维持接近 (1/2) 的
rejection，同时只按 mutual-information 下界缓慢增加 (d_c)。随机搜索已经
找到 relaxation rate 严格低于 (2.349083) 的形式 profile；这不是 filter
反例，而证明式 (8) 单独不足以闭合 converse。

这里甚至有一个完全显式的 obstruction，不需要随机搜索。取 (K=2)，形式上令

\[
\rho_0=1,
\qquad \rho_1=\rho_2=\frac12,
\qquad \rho_c=0\quad(c\ge3).
\tag{10}
\]

式 (6) 只强迫

\[
(d_0,d_1,d_2,d_3,\ldots)
\ge(1,2,4,4,\ldots).
\tag{11}
\]

把式 (11) 当作可达 profile，half-error root 与 fixed-state saddle 分别为

\[
\lambda=1.568119992393\ldots,
\qquad z=0.464608569227\ldots,
\]

并给出

\[
R_{\rm formal}=2.269435990153\ldots
<2.349083440193\ldots.
\tag{12}
\]

但它不可能来自 binary canonical quotient：binary lattice classification
说明每个 quotient 都是 modulo-(q)，其 rejection profile 必为

\[
\rho_c=2^{-c}\mathbf 1\{c<q\}.
\]

特别地，
(rho_2) 只能是 (1/4) 或 (0)，不可能是 (1/2)。所以式 (10)--(12)
精确定位了 relaxation 丢掉的信息：同一个 quotient 的跨层 right-congruence
兼容性，而不是某个小的数值 slack。

缺失的约束至少包括：

1. (P_c(s)) 来自同一个 Cayley sumset chain，而不是任意 posterior channel；
2. support nesting (cV+V=(c+1)V) 对各 syndrome 的 representation graph
   施加局部 degree 约束；
3. 当高 rejection 在多层持续时，Pluennecke/Kneser 型增长应比 Shannon
   entropy 下界更快；
4. equality/stability：式 (4) 近等号要求 posterior 在 (P_c(s)) 上近均匀，
   同时 (S_c) 近似均匀于 (cV)，这应迫使接近 subgroup/coset 的结构。

所以正确的下一条 lemma 不是另一个纯 cardinality 界，而是式 (4) 的稳定版：
持续的小 mutual information 必须迫使 (V) 接近 subgroup coset；但 coset
情形在第一层以后 rejection 立即归零。这个 dichotomy 才可能给出 sharp
(K>2) converse。

## 6. 研究结论

本文件给出一个可独立使用的新结构工具：

> 在任意 uniform finite-Abelian local quotient 中，每层 query rejection
> 强迫至少 (-\log(1-\rho_c)) 的 syndrome entropy growth。

它解释了为什么“保持较长时间的 query 分辨率”一定要支付 sumset state growth，
并在 binary optimum 上 sharp。它还没有证明 (K>2) 全局不优于 binary；把它
误称为 matching converse 会越过现有证据。
