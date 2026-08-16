# Operational support completion 与 avalanche-or-information 下界

> 日期：2026-08-16。状态：一般 finite-parameter 定理。本文用一个
> infinitesimal support-completion argument 把 source posterior 与完整
> operational fiber 对齐。结论不需 source-cover equality、BSSI、
> history independence 或 monotone queries；大 operational section avalanche
> 必须由同一个 state 的 excess information 或 suffix-source information
> 支付。它给出一个新的一般下界，但尚未单独证明 unrestricted
> ordinary model 的新 universal constant。

所有对数以 2 为底。

## 1. Setup

固定有限 universe `U`、`u=|U|`、load `t` 与 exact operation time `q0`。
令 `Theta` 是与 filter tape `R` 一起公开的 source context。在给定
`Theta` 后，抽取一条与 `R` 独立的合法 parent history `H0`，使其
endpoint

\[
S=S(H_0),\qquad |S|=t,
\]

并记 parent physical state 为

\[
M=M_R(H_0).
\]

对每个 realized `(R,M)=(r,m)`，定义完整 operational endpoint fiber

\[
\mathcal O_r(m,t,q_0)
=\{T:\text{存在长度 }q_0\text{ 的合法 history 以 }T
\text{ 结束且到达 }m\},
\tag{1}
\]

及其 union

\[
W=W_r(m,t,q_0)=\bigcup_{T\in\mathcal O_r(m,t,q_0)}T,
\qquad w=|W|.
\tag{2}
\]

这是完整 operational fiber，不只是 source 可见 endpoints。

从 parent 开始执行一个随机 self-contained suffix `Omega`。记其所有
distinct insertion labels 为 `J(Omega)`。所谓 self-contained，是指 suffix
中每个 deletion 都匹配 suffix 内更早的 insertion；因此对任意

\[
T\cap J(\Omega)=\varnothing,
\]

该 suffix 从 `T` 出发都合法，且不会删除 `T` 的原有 members。
定义 section union

\[
W[J]
=\bigcup\{T\in\mathcal O_r(m,t,q_0):T\cap J=\varnothing\},
\qquad w_J=|W[J]|.
\tag{3}
\]

因为 actual suffix 合法，`S cap J(Omega)=emptyset`，所以 `w_J>=t`。

## 2. Infinitesimal support completion

固定

\[
Z=(\Theta,R,M)=(\theta,r,m).
\]

令 `P` 是 actual conditional joint law of `(S,Omega)`。它的 endpoint
support 可能只覆盖 (1) 的很小一部分。取任意 full-support law `Q`，
使对每个 actual suffix word `omega` 和每个

\[
T\in\mathcal O_r(m,t,q_0),
\qquad T\cap J(\omega)=\varnothing,
\]

都有 `Q(T,omega)>0`。所有 alphabet 在固定有限参数与 horizon
下有限，故这样的 `Q` 存在。

对 `eta in (0,1)` 定义

\[
P_\eta=(1-\eta)P+\eta Q.
\tag{4}
\]

这个任意小的 doping 有一个不连续的 support 效果：给定任意
`omega`，`S_eta | Omega_eta=omega` 的 support 恰好覆盖完整
operational section，所以

\[
H(S_\eta\mid Z,\Omega_\eta=\omega)
\le\log\binom{w_{J(\omega)}}t.
\tag{5}
\]

同时 Shannon entropy 和 mutual information 在有限 alphabet 上连续。因此
`eta -> 0` 时，doping 的 entropy 代价趋于零，但它已经把
source-invisible operational ghosts 加入了 conditional support。

这个极限步骤是本文的核心。它不声称 rare witnesses 有可观的
posterior mass；相反，它允许该 mass 趋于零，并把由此产生的
full-union thinness 记入 entropy deficit。

## 3. Operational avalanche-or-information theorem

### Theorem 3.1

在 Section 1 的任意 ordinary deterministic-tape transducer 与任意
self-contained random suffix 下，

\[
\boxed{
t\,\mathbb E
\log\frac{w}{w_{J(\Omega)}}
\le
\mathbb E\!\left[
\log\binom wt-H(S\mid\Theta,R,M)
\right]
+I(S;\Omega\mid\Theta,R,M).
}
\tag{6}
\]

这里 `w` 是由 `(Theta,R,M)` 决定的随机 cardinality。

若进一步 `S | Theta` 在一个大小为 `v` 的 ambient set 的
`t`-subsets 上均匀，定义

\[
\mathsf A
=\log\binom vt-\mathbb E\log\binom wt,
\qquad
\mathsf J
=I(S;\Omega\mid\Theta,R,M),
\tag{7}
\]

则

\[
\boxed{
t\,\mathbb E
\log\frac{w}{w_{J(\Omega)}}
\le
I(S;M\mid\Theta,R)-\mathsf A+\mathsf J
\le H-\mathsf A+\mathsf J.
}
\tag{8}
\]

#### Proof

固定 `Z=(theta,r,m)` 并对 (4) 使用 (5)：

\[
\begin{aligned}
\log\binom wt
-\mathbb E_{P_\eta}\log\binom{w_J}t
&\le
\log\binom wt-H(S_\eta\mid Z,\Omega_\eta)\\
&=
\log\binom wt-H(S_\eta\mid Z)
+I(S_\eta;\Omega_\eta\mid Z).
\end{aligned}
\tag{9}
\]

对 `t<=w_J<=w` 有

\[
\log\frac{\binom wt}{\binom{w_J}t}
=\sum_{i=0}^{t-1}\log\frac{w-i}{w_J-i}
\ge t\log\frac w{w_J}.
\tag{10}
\]

把 (10) 代入 (9)，再令 `eta -> 0`。有限 alphabet 上的连续性给出

\[
t\,\mathbb E_P\log\frac w{w_J}
\le
\log\binom wt-H(S\mid Z)+I(S;\Omega\mid Z).
\tag{11}
\]

对 `Z` 平均得到 (6)。在 (7) 的 uniform source 下，

\[
\begin{aligned}
\mathbb E\!\left[
\log\binom wt-H(S\mid\Theta,R,M)
\right]
&=I(S;M\mid\Theta,R)-\mathsf A,
\end{aligned}
\tag{12}
\]

而 `I(S;M|Theta,R)<=H`，故得 (8)。`Q` 只用于每个固定
finite instance 的极限证明；定理中没有修改真实 filter 或 source。
\(\square\)

## 4. 对真实 successor transport 的推论

令 `M+` 是执行 `Omega` 后的 physical state，`W+` 是相应时间与
load 的完整 operational union。对每个

\[
T\in\mathcal O_R(M,t,q_0),
\qquad T\cap J(\Omega)=\varnothing,
\]

suffix 从 `T` 出发合法，且 fixed-tape determinism 使它到达同一个
`M+`。Zero false negatives 给出

\[
W[J(\Omega)]\subseteq W^+.
\tag{13}
\]

定义真实 operational transport loss

\[
L=|W\setminus W^+|.
\tag{14}
\]

由 (13)，`w-L=|W cap W+|>=w_J`。因此 Theorem 3.1 立即给出：

### Corollary 4.1

\[
\boxed{
t\,\mathbb E\log\frac w{w-L}
\le H-\mathsf A+\mathsf J.
}
\tag{15}
\]

从而

\[
\boxed{
\mathbb E\frac Lw
\le
\frac{\ln2}{t}(H-\mathsf A+\mathsf J),
}
\tag{16}
\]

且对每个 `theta in (0,1)`，

\[
\boxed{
\Pr[L\ge\theta w]
\le
\frac{H-\mathsf A+\mathsf J}
{t\log(1/(1-\theta))}.
}
\tag{17}
\]

等价地，若一个 suffix experiment 满足

\[
\Pr[L\ge\theta w]\ge\tau,
\]

则得到直接的状态下界

\[
\boxed{
H\ge
\mathsf A
+t\tau\log\frac1{1-\theta}
-\mathsf J.
}
\tag{18}
\]

这是 avalanche 产生的真正 dynamic premium；它不是将同一个
posterior deficit 错接到 future hidden batch。

## 5. 与 pointwise FPR 的合法组合

对每条固定 source history，先对原 filter tape 使用 pointwise FPR，
再对 source 平均，得

\[
\mathbb E w
\le t+\varepsilon(u-t).
\tag{19}
\]

对 uniform `t`-set source，`a -> log binom(a,t)` 的凹性给出

\[
\mathsf A
\ge
\log\binom ut
-\log\binom{t+\varepsilon(u-t)}t.
\tag{20}
\]

所以 (18) 进一步给出完全一般的 finite-parameter 下界

\[
\boxed{
H\ge
\log\frac{\binom ut}
{\binom{t+\varepsilon(u-t)}t}
+t\tau\log\frac1{1-\theta}
-\mathsf J.
}
\tag{21}
\]

当 `u/t -> infinity` 且 `mathsf J=o(t)` 时，

\[
\boxed{
H\ge
t\left[
\log\frac1\varepsilon
+\tau\log\frac1{1-\theta}
\right]-o(t).
}
\tag{22}
\]

因此在极其一般的 ordinary model 中，常数概率的常数比例
operational avalanche 不是一个免费的反例机制；它会直接把下界
推过 Carter rate。

## 6. One-label implication preorder

对任意 nonempty family `C subseteq binom(U,t)` 定义

\[
x\preceq y
\quad\Longleftrightarrow\quad
\forall T\in\mathcal C,
\quad x\in T\Longrightarrow y\in T.
\tag{23}
\]

这是一个 preorder。对 one-label loop

\[
\tau_y=(\operatorname{Insert}(y),\operatorname{Delete}(y)),
\]

一步 section loss 恰为 principal down-set

\[
D(y)=W(\mathcal C)\setminus W(\mathcal C[\{y\}])
=\{x:x\preceq y\}.
\tag{24}
\]

其中 `C[{y}]` 表示 `C` 中所有不含 `y` 的 members。

对每个 `x in W(C)`，其 principal up-set

\[
\uparrow x=\{y:x\preceq y\}
\]

包含于任意一个包含 `x` 的 witness `T`，所以

\[
|\uparrow x|\le t.
\tag{25}
\]

双计数给出

\[
\boxed{
\sum_{y\in U}|D(y)|
=\sum_{x\in W(\mathcal C)}|\uparrow x|
\le t|W(\mathcal C)|.
}
\tag{26}
\]

式 (26) 精确解释了 birthday barrier：单纯对随机 label 平均只能得到
`t|W|/u` 级的 one-step influence。当 suffix 含 `Theta(n)` 个 labels
时，cardinality-only 方法自然产生 `n^2/u` 尺度。Theorem 3.1
增加的关键信息是：若这个粗界真的通过 rare/shared witnesses 达到，
则相应 full-union thinness 必须出现在 `H - A` 中。

## 7. 它解决了什么，还缺什么

已解决的是一个先前明确的缺口：

- source witnesses 不需要覆盖 operational union；
- source-invisible successor ghosts 可以通过 infinitesimal doping 进入 support；
- rare-witness 或 shared-witness avalanche 不需要 bounded influence；
- 费用是同一 parent state 的 exact excess information，不是错位的
  future-batch deficit。

尚未解决的是跨多个 replacement cuts 的 single-budget 组合。式 (8)
允许每个 cut 最多使用一次 `H - A`；若机械地对线性多个
cuts 重复付费，仍然会被 parity/DTC 和 mutable-memory 反例击穿。

因此剩余的最小主定理现在可以更窄地表述为：

\[
\text{small avalanche at many recurrent cuts}
\quad\Longrightarrow\quad
\text{large joint replacement-response width}.
\]

不再需要把 source-to-operational completeness 作为独立假设。
