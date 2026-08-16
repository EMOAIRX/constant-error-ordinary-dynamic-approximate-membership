# Normalized-dual conditional novelty 与 finite-depth no-go

> 日期：2026-08-17。状态：Sections 1--3 是严格 information inequality；
> Section 4 的 cylinder-complete family 由随机着色和 union bound 给出。本文没有产生
> 新的 universal numerical constant，而是把超过 $1.6079$ 所需的新 invariant 精确化。

## 1. Single-step novelty lemma

固定一个 all-pivot decode step。令

- $X$ 是当前待编码 batch；
- $C$ 是 decoder 已知 context；
- $F=f(M,C)$ 是由 final physical state $M$ 导出的 step descriptor；
- $W=W(F,C)$ 决定 candidate list $\Omega(W)$，且
  $\operatorname{supp}(X\mid C,F)\subseteq\Omega(W)$。

定义 support charge 和 residual deficit

$$
A
=H(X\mid C)-\mathbb E\log_2|\Omega(W)|,
$$

$$
D
=\mathbb E\log_2|\Omega(W)|-H(X\mid C,F).
$$

则

$$
A+D=I(X;F\mid C).
$$

取 probe $P$ 满足

$$
P\perp(X,F)\mid(C,W),
$$

并令 future response statistic $Y$ 由 $(F,C,W,P)$ 决定。定义 conditional novelty

$$
V=I(X;Y\mid C,W,P).
$$

### Lemma 1

$$
\boxed{V\le D.}
$$

证明。由 conditional data processing，

$$
I(X;Y\mid C,W,P)
\le I(X;F\mid C,W,P)
=I(X;F\mid C,W).
$$

又因为 $W$ 是 $(C,F)$ 的函数，

$$
H(X\mid C,W,F)=H(X\mid C,F),
$$

而 support containment 给出

$$
H(X\mid C,W)le\mathbb E\log_2|\Omega(W)|.
$$

相减即得 $I(X;F\mid C,W)\le D$。

因此 $V$ 不是 all-pivot deficit 之外的第二份收费；它是同一个 residual information
budget 中可由未来 responses 观测到的部分。

## 2. Embedding into one pivot code

对 pivot $s$ 的 decode order $\pi_s$，令第 $k$ 步 context $C_{s,k}$ 包含公共 tape、
partition、此前已解码 batches 和协议所需 framing。取

$$
F_{s,k}=f_{s,k}(M,C_{s,k}).
$$

Chain rule 给出

$$
\sum_k I(X_{\pi_s(k)};F_{s,k}\mid C_{s,k})
\le I(X;M\mid\Theta,R)
\le H.
$$

逐步应用 Lemma 1，得到

$$
\boxed{
\sum_k(A_{s,k}+V_{s,k})\le H.
}
$$

这里每个 $A_{s,k}$ 使用现有 full-fiber batch code 的同一个 candidate list，故原
support analysis 不变：

$$
\sum_k A_{s,k}ge nF_s(x)-o(n).
$$

## 3. Normalized all-pivot dual

令 $\lambda_s\ge0$ 是任意 normalized pivot dual weights，

$$
\sum_s\lambda_s=1.
$$

对上一节的不等式加权平均，只对同一个 $H$-bit final state 收费一次：

$$
H
\ge
\sum_s\lambda_s\sum_k(A_{s,k}+V_{s,k}).
$$

对已认证的 ten-block dual，support 部分给出 $C_{10}>1.607987002861718$，因此

$$
\boxed{
H
\ge
C_{10}n+V_\lambda-o(n),
}
$$

其中

$$
V_\lambda
=\sum_s\lambda_s\sum_kV_{s,k}
\ge0.
$$

这是一条严格的加强形式，但不是自动的常数改进。要证明

$$
H\ge(1.6079+\eta)n-o(n),
$$

现在只剩一个清楚的正向目标：对 ordinary transition system 的某个合法 probe family
证明

$$
V_\lambda\ge\eta n.
$$

## 4. Finite-depth cylinder-completeness no-go

固定 $v,k,d$，$k>d$。称
$\mathcal F\subseteq\binom{[v]}k$ 是 $d$-cylinder-complete，如果对所有 disjoint
$A,J$、$|A|+|J|\le d$，

$$
\bigcup
\{T\in\mathcal F:A\subseteq T,\ T\cap J=\varnothing\}
=[v]\setminus J.
$$

### Theorem 2

令

$$
m_*
=\min_{a+b\le d}
\binom{v-a-b-1}{k-a-1}.
$$

令 $N=\binom vk$。当
$m_*/(\ln N+(d+1)\ln v)\to\infty$ 时，存在 partition

$$
\binom{[v]}k
=\mathcal F_1\sqcup\cdots\sqcup\mathcal F_K
$$

使每个 color family 都是 $d$-cylinder-complete，并且

$$
K
\ge
\frac{m_*}{16(\ln N+(d+1)\ln v)}.
$$

证明要点。随机给每个 $k$-set 着 $K$ 种颜色。固定 color、$A,J$ 和
$x\notin J$，满足

$$
A\cup\{x\}\subseteq T,
\qquad
T\cap J=\varnothing
$$

的 sets 数为

$$
\binom{v-|A|-|J|-1}{k-|A|-1}.
$$

取

$$
K
=\left\lfloor
\frac{m_*}{8(\ln N+(d+1)\ln v)}
\right\rfloor.
$$

每个 cylinder 在指定 color 中为空的概率至多
$\exp(-m_*/K)\le N^{-8}v^{-8(d+1)}$；对至多 $K\le N$ 个 colors 及
$(d+1)2^dv^{d+1}$ 个 $(A,J,x)$ constraints 作 union bound。Chernoff bound 同时给出
每个 color size 至多 $2N/K$。因此 exact-rank deficit至少
$\log_2K-1$。

令 source $X$ uniform 于整层，state $M$ 只保存 color。每个 color 的 exact-rank
deficit 至少

$$
\log_2K-O(1).
$$

但是，任何 source-independent、总共只对至多 $d$ 个 labels 作
forced-present/forced-absent section 的自适应 **local cylinder probe**，在每个 prefix
后只观察某个 $(A,J)$ cylinder 的 minimal union。Cylinder completeness 使所有
colors 的这类 transcript 完全相同，所以

$$
\boxed{I(X;Y\mid W,P)=0.}
$$

当 $d$ 固定且 $k/v\to0$ 时，

$$
\log_2K
=\log_2\binom vk
-(d+1)\log_2\frac vk
-O(\log\log N).
$$

因此 finite-depth local section responses 可以看不见几乎全部 exact rank。

## 5. Research consequence

Sections 1--3 说明 conditional response information 能合法进入 normalized all-pivot
dual，而且不会重复计费。Section 4 同时说明：不能仅从 high rank、large deficit 或
fixed-depth local shadow exposure 自动推出正的 $V_\lambda$。

所以真正可能超过 $1.6079$ 的 theorem 必须使用至少一种 extensive 结构：

1. 触及线性数量 hidden coordinates 的 recurrent probe；
2. 跨多个 physical states 的 simultaneous replacement-response width；
3. source-dependent probe，并显式扣除 probe 携带的 mutual information。

本 no-go 是 local fiber/probe theorem；随机 coloring 未被证明与一个 dynamic right
congruence 的全部 updates 相容。它没有构造 low-space arbitrary-horizon ordinary
transducer，因此没有排除 extensive-depth recurrence 路线。
