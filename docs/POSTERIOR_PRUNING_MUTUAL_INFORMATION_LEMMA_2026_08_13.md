# Posterior pruning 与 mutual information 的精确抵消

> 日期：2026-08-13。状态：抽象有限参数 lemma。它说明 support shrinkage 与
> posterior thickness deficit 使用的是同一份 mutual-information 预算。本文尚未
> 证明 KLZ multi-parent pivot 中所有 parent deficits 的 chain rule。

所有对数以 2 为底。

## 1. 实验

令 `X` 在 `[V]` 的 ordered distinct `m`-tuples 上均匀：

\[
X\sim [V]^{\underline m}.
\]

令 `F` 是任意与 `X` 相关的随机变量。给定 `F=f`，记 posterior 为 `mu_f`，其
coordinate union 为

\[
W_f=\bigcup_{x\in\operatorname{supp}\mu_f}\{x_1,\ldots,x_m\},
\qquad w_f=|W_f|.
\]

再给定实际 `X`，从 `[V]\setminus\{X_1,...,X_m\}` 中均匀抽取一个 `q`-set `I`。
在 posterior support 中删除所有与 `I` 相交的 tuples，所得 coordinate union记为
`W_(f,I)`，大小为 `w_(f,I)`。实际 `X` 总能 survive，所以 `w_(f,I)>=m`。

## 2. 精确 lemma

### Lemma 2.1

若 `V-m-q+1>0`，则

\[
\boxed{
\mathbb E\log
\frac{(V)_{\underline m}}{(w_{F,I})_{\underline m}}
\le
I(X;F)+\Delta_{V,m,q},
}
\tag{1}
\]

其中

\[
\Delta_{V,m,q}
=\log\frac{\binom Vq}{\binom{V-m}q}
\le(\log e)\frac{mq}{V-m-q+1}.
\tag{2}
\]

### 证明

对每个 `f` 定义 posterior thickness deficit

\[
D_f=\log(w_f)_{\underline m}-H(X\mid F=f)\ge0.
\tag{3}
\]

互信息有精确分解

\[
\begin{aligned}
I(X;F)
&=\log(V)_{\underline m}-\mathbb EH(X\mid F=f)\\
&=\mathbb E\left[
\log\frac{(V)_{\underline m}}{(w_f)_{\underline m}}+D_f
\right].
\end{aligned}
\tag{4}

另一方面，给定 `(F=f,I=i)`，surviving posterior 支持在
`W_(f,i)^{\underline m}`，所以

\[
H(X\mid F=f,I=i)\le\log(w_{f,i})_{\underline m}.
\tag{5}

由 posterior pruning 的 entropy identity，

\[
\begin{aligned}
\mathbb E_{I\mid F=f}
\log\frac{(w_f)_{\underline m}}{(w_{f,I})_{\underline m}}
&\le
\log(w_f)_{\underline m}
-H(X\mid F=f,I)\\
&=D_f+I(X;I\mid F=f).
\end{aligned}
\tag{6}

对 `f` 平均，并将式 (6) 与式 (4) 相加，得到

\[
\mathbb E\log
\frac{(V)_{\underline m}}{(w_{F,I})_{\underline m}}
\le I(X;F)+I(X;I\mid F).
\tag{7}

最后，条件于 `X`，`I` 在一个大小为 `V-m` 的集合中均匀，因此

\[
H(I\mid X,F)=H(I\mid X)=\log\binom{V-m}q,
\]

而 `H(I|F)<=log binom(V,q)`。所以

\[
I(X;I\mid F)
\le\log\frac{\binom Vq}{\binom{V-m}q}
=\Delta_{V,m,q}.
\]

再用 `log_2(1+x)<=log_2(e)x` 得到式 (2)。证毕。

## 3. 含 side information 的条件版本

若给定 side information `C` 后，`X` 仍均匀分布在同一个
`[V]^{underline m}` 上，则逐 `C=c` 使用 Lemma 2.1 并平均得到

\[
\boxed{
\mathbb E\log
\frac{(V)_{\underline m}}{(w_{F,I,C})_{\underline m}}
\le I(X;F\mid C)+\Delta_{V,m,q}.
}
\tag{8}

这正是 multi-parent communication 应使用的形式。

## 4. 对 KLZ lifting 的意义与剩余缺口

式 (8) 说明：

- large posterior union 给出的静态 support saving；
- suffix pruning 缩小 union带来的额外 rank saving；
- thin fiber 的 posterior entropy deficit；

三者不是独立预算。前两项之和已经由同一个 `I(X;F|C)` 支付，误差只有
`Delta_(V,m,q)`。在 `V/m=u/n->infinity` 且 `q=o(V)` 的适当参数区间，累计误差
可以是 `o(n)`。

但 KLZ all-pivot batch code 的 difference support来自 parent `G_ell` 经 suffix
transport到 child `F_r`。式 (8) 直接收费的是同一个 posterior变量 `F` 的 support
pruning。要将它用于 ordinary AMQ，还必须证明下列 multi-parent chain rule：

\[
\sum_k \operatorname{ParentDeficit}(G_{\ell_k}\mid D_k)
\le I(X;M_{final}\mid R,\Theta)+o(n),
\tag{9}
\]

或者改写 batch decoder，使每个 pruning support直接来自对应 `F_(r_k)` posterior，
从而逐项使用

\[
\sum_k I(X_k;F_{r_k}\mid R,\Theta,D_k)\le H.
\]

式 (9) 目前不是定理。若对同一 parent deficit重复使用多个 pivots，它会再次造成
重复收费。因此 Lemma 2.1 解决了单 batch 的精确抵消，但没有自动给出
`u/n->infinity` 下的 all-pivot常数。
