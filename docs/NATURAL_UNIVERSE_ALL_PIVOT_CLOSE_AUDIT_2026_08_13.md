# `u/n -> infinity` 下的 all-pivot converse：可闭合部分与严格 barrier

> 日期：2026-08-13。状态：Sections 1--3 是严格 finite-parameter lemmas；
> Sections 4--5 给出 ordinary arbitrary-history transducer 中的线性 barrier。
> 结论是否定性的 close：without-replacement / collision accounting 已不再需要
> `u >> n^2`，但仅靠 posterior support、entropy deficit、suffix debit 和
> multi-parent chain rule，不能恢复原 hard-union all-pivot constant。缺失对象必须是
> simultaneous replacement-branch width，而不是另一种 endpoint code。

所有 logarithms 以 2 为底。

## 1. Birthday scale 的精确定位

令每个 KLZ block 大小为 `V=u/b`、hidden batch 大小为 `m=n/b`。两个常见
finite-population corrections 是：

### Source falling factorial

\[
b\left[m\log V-\log(V)_{\underline m}\right]
\le (\log e)\frac{bm(m-1)}{2(V-m+1)}
=O\left(\frac{n^2}{u}\right).
\tag{1}
\]

相对于线性主项，式 (1) 只要求

\[
u/n\to\infty,
\]

因为 `(n^2/u)/n=n/u=o(1)`。所以 source entropy 本身从未内生地要求
`u/n^2 -> infinity`。

### Suffix/source dependence

若 suffix 从 batch complement 中无放回抽取 `q` 个 distinct insert labels，则

\[
\Delta_{V,m,q}
=\log\frac{\binom Vq}{\binom{V-m}q}
\le(\log e)\frac{mq}{V-m-q+1}.
\tag{2}
\]

对 `b` 个 batches，若 `q=o(V)` 且参数 `b=b(n)` 足够慢，累计 correction为
`o(n)`。由于 KLZ suffix length形如 `n 4^{O(b^2)}`，只要 `u/n->infinity`，可以
对任意发散比值 `u/n` 作 diagonal choice，使

\[
4^{O(b^2)}=o(u/n),
\]

同时保持 `b->infinity` 和 operation horizon约束。

因此旧 proof 中真正使用 `u >> n^2` 的唯一不可忽略位置，是对每个 hard-union
element选择一个 witness 后作 union bound：一个 size-`n` witness 与随机 suffix
冲突概率约 `nq/u`，再对 `Theta(u)` 个 union elements收费，产生 `Theta(nq)` 的
绝对 loss。这个 loss不是 without-replacement approximation造成的。

## 2. 单 parent 的 debit-compatible identity

令 `X` 均匀于 `[V]^{underline m}`，`F` 是任意 parent observable。给定 `F=f`，
posterior coordinate union大小为 `w_f`；随机 suffix insertion set `I` 从实际
`X` 的 complement中无放回抽取。删去所有与 `I` 相交的 posterior tuples后，
surviving coordinate union大小为 `w_(f,I)`。

定义

\[
A=\mathbb E\log\frac{(V)_{\underline m}}{(w_F)_{\underline m}},
\]

\[
D=\mathbb E\left[
\log(w_F)_{\underline m}-H(X\mid F)
\right],
\]

以及 suffix debit

\[
T=\mathbb E\log
\frac{(w_F)_{\underline m}}{(w_{F,I})_{\underline m}}.
\]

则 exact chain rule 与 posterior pruning给

\[
\boxed{I(X;F)=A+D,}
\tag{3}
\]

\[
\boxed{T\le D+\Delta_{V,m,q}.}
\tag{4}
\]

相加后得到真正 debit-compatible 的单 parent inequality

\[
\boxed{
\mathbb E\log\frac{(V)_{\underline m}}
{(w_{F,I})_{\underline m}}
\le I(X;F)+\Delta_{V,m,q}.
}
\tag{5}

式 (5) 已经一次性吸收：static support saving、posterior thinness和suffix
conflict。它不需要 hard-union witness union bound，也不需要 `u >> n^2`。

## 3. 为什么任意 endpoint code 仍只能到 midpoint

设一个 ideal hard-support all-pivot branch给出总 converse常数

\[
C=A+K,
\]

其中 `A` 是 static/support contribution，`K` 是理想 dynamic rank saving。
任何 lossless posterior-aware second-stage code至少使用

\[
H(X\mid F)=S-A-D
\]

bits。若 hard rank code在无冲突时长度为 `S-A-K`，suffix debit `T` 使它变成

\[
S-A-K+T.
\]

losslessness强迫

\[
K\le D+T+o(n).
\tag{6}
\]

结合式 (4)，最多得到

\[
K\le2D+o(n).
\]

另一方面 state message给

\[
H\ge A+D,
\]

而 hard-rank protocol给

\[
H\ge C-T\ge C-D-o(n).
\]

因此该接口的 sharp closure是

\[
\boxed{
H\ge\max\{A+D,C-D\}-o(n)
\ge\frac{A+C}{2}-o(n).
}
\tag{7}

这不是选择了不好的 code。式 (6) 是 Shannon lower bound；式 (4) 是 exact
posterior pruning inequality。要超过式 (7)，必须加入一个普通 endpoint code中没有
的 operational invariant。

在 half error、large universe下 `A=1`。即使使用 certified
`C_10>1.6079`，这个 closure也只有

\[
H>1.30395n-o(n).
\]

这里的 `1.30395` 只是该抽象会计系统允许的形式值，不是已经证明的 ordinary-AMQ
lower bound：还需要把各 parent posterior与同一个 KLZ final-state decode order严格
对齐。本文使用它刻画方法天花板，不把它列为新定理常数。

## 4. Barrier I：`T<=kappa D` 不可能有 universal `kappa<1`

取一个 block universe `V`，`|V|=2m`，固定 `a in V`，令

\[
X\sim\binom Vm,
\qquad M=\mathbf1[a\in X].
\]

条件于 `M=1`，posterior family为所有包含 `a` 的 `m`-sets，coordinate union仍为
整个 `V`。其 within-union deficit恰为

\[
D_1
=\log\binom{2m}{m}-\log\binom{2m-1}{m-1}
=1.
\tag{8}
\]

从实际 `X` 的 complement均匀取 `Y`，执行合法 self-contained suffix

\[
\tau_Y=(Insert(Y),Delete(Y)).
\]

在 belief-state transducer中，这个 suffix将 posterior section到不含 `Y` 的
worlds；coordinate union从 `V` 降为 `V\setminus\{Y\}`。所以 hard ambient debit为

\[
T_1
=\log\binom{2m}{m}-\log\binom{2m-1}{m}
=1=D_1.
\tag{9}
\]

将这个 gadget在 disjoint blocks上 tensorize，得到线性规模

\[
T=D=Theta(n).
\]

任意 family section都可由 ordinary key-only belief transitions实现；再以概率
`1/2` 运行 exact branch、概率 `1/2` 运行该 lossy branch并 padding到固定状态块，
得到支持任意长合法 history、zero false negatives且 pointwise FPR至多 `1/2` 的
ordinary randomized AMQ。

故：

> 在 ordinary semantics下，不存在 universal常数 `kappa<1` 使所有 active
> posterior sections满足 `T<=kappa D+o(n)`。

这个构造不是低空间 upper bound；它是 proof-interface反例。它说明 strict debit
coefficient不能只由 ordinary update legality和one-sided query推出。

## 5. Barrier II：future-response quotient 也不能自动 telescope parents

令 `X_1,...,X_b` 独立；每个 `X_i` 取四点 block中的一条 edge，并把六条 edges
分成两个各含三条、且 coordinate union都为四点的 color classes。令

\[
P=c(X_1)\oplus\cdots\oplus c(X_b).
\tag{10}
\]

source physical state保存一 bit `P`，其 represented family是所有满足式 (10) 的
edge tuples。给该 state增加一个固定 source-nonmember probe `z`，query规定

\[
Query(z)=YES
\quad\Longleftrightarrow\quad
z\text{ 属于当前 belief-family union，或 }P=1,
\]

其他 keys使用 belief-family union rule。Belief transitions支持任意长合法 updates；
在 source endpoint，`z` 不属于任何 represented world，所以其响应恰为 `P`；若
`z` 后来成为member，union项自动保证 zero false negatives。与 exact branch作
half-half public-coin mixture后，所有 fixed history/nonmember的FPR至多 `1/2`。

由于 `z` 的响应直接区分 `P=0,1`，这一个 bit不会在 future-response quotient中被
消去。可是给定其他 batches，

\[
I(X_i;P\mid X_{-i})=1
\]

for every `i`，而

\[
I(X_{1:b};P)=1.
\]

所以

\[
\sum_i I(X_i;P\mid X_{-i})=b
\gg1=I(X;P).
\tag{11}

因此：

> 即使先商掉 query-silent fields，使用不同 leave-one-out parent contexts 的
> response information仍不能未加权 telescope到 final-state source information。

对每个固定 decode permutation，普通 chain rule当然仍只收费一次；失败的是从多个
pivots各挑有利 parent后相加。All-pivot的 normalized convex dual避免了这类显式重复
收费，但它并不能消除 Section 3 的同一-parent `D/T` midpoint。

## 6. Close verdict

### 已经严格关闭

1. `u >> n^2` 不是 without-replacement/source-entropy的必要条件；式 (1)--(2)
   在 `u/n->infinity` 下给 `o(n)` correction。
2. 单 parent suffix conflict可由式 (5) 精确吸收到 mutual information中，不再需要
   hard-union witness union bound。
3. 任何只使用 `(A,D,T)` 和普通 multi-parent chain rule的 endpoint protocol，其
   最强普适 closure是 midpoint (7)。
4. `T<=kappa D` with `kappa<1` 被 ordinary tensor belief transducer严格反驳。
5. 未加权 multi-parent telescope即使经过 future-response quotient仍被 observable
   parity反例严格反驳。

### 没有关闭

这些 barriers不否决一个真正使用 small state-space width的 lower bound。反例的完整
belief transition space很大；这正指出旧接口漏看的量：大量 counterfactual
replacement branches是否能同时在一个小 physical state space中实现。

所以恢复 `C_10`，更不用说匹配大宇宙 upper bound，所需的最小新 theorem必须是：

> **Simultaneous replacement-response width theorem.** 若一个 source cell在
> dual-active的许多 KLZ parents上同时实现近-midpoint的 posterior thinness与suffix
> debit，则这些 parents的 fresh replacement response tables必须占据
> `2^{Omega(n)}` 个 future-distinct physical states，除非相应 branches支付
> `Omega(n)` 的 false-positive list penalty。

这个 theorem会直接使用 worst-case state-space width `2^H`，而不是只使用某个 source
distribution下的 `I(X;M)`。没有这种 width项，debit-compatible endpoint code无法恢复
sharp constant；这一点已经由 Sections 3--5 严格关闭。
