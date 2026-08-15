# 长程 online state-merging：stationary identity 与 branching-program reduction

> 日期：2026-08-13。状态：Sections 2--4 是严格有限状态归约与恒等式。裁决是：累计 directed information / transcript entropy 不能下界 persistent width；它测量可无限重复的信息耗散。完整 ordinary dynamic AMQ lower bound 精确等价于 randomized right-congruent cover branching program 的 width lower bound。本文没有证明该 width 超过 Carter；它明确隔离了所需的新组合定理。

所有 logarithms 以 2 为底。

## 1. Replacement hard process

固定容量 \(n\) 与 universe \(U\)，\(|U|=u\)。在 logical layer

\[
\Omega=\binom Un
\]

上运行 stationary replacement chain：

1. \(S_t\) uniform in \(\Omega\)；
2. \(X_t\) uniform in \(S_t\)；
3. \(Y_t\) uniform in \(U\setminus S_t\)；
4. \(S_{t+1}=S_t-X_t+Y_t\)。

写

\[
L_t=(X_t,Y_t).
\]

该 chain可逆且 uniform slice 是唯一 stationary distribution。一个 fixed-tape filter state满足

\[
M_{t+1}=\delta_R(M_t,L_t).
\tag{1}
\]

为避免 pointwise FPR 对 seed-dependent histories 的量词错误，可以从 uniform \(S_0\)、独立于 \(R\) 的 random replacement labels开始运行，再对时间作 Cesàro averaging。每个 finite history realization都独立于 \(R\)，所以可逐 history使用 pointwise FPR；有限 state space上的 subsequential Cesàro limit给出一个 stationary joint law \((R,S,M,L,S',M')\)。

## 2. Stationary one-step information balance

### Theorem 2.1（replacement entropy-production identity）

在上述任意 stationary joint law中，令

\[
\Lambda
=
I(S;M\mid M',L,R).
\tag{2}
\]

则

\[
\boxed{
\Lambda
=
I(S;L\mid M,R)
-
I(S';L\mid M',R)
\ge0.
}
\tag{3}
\]

### Proof

给定 \(L=(x,y)\)，映射

\[
S\longleftrightarrow S'=S-x+y
\]

在 compatible slices之间是 bijection，且 \(M'\) 是 \((M,L,R)\) 的确定函数。因此

\[
\begin{aligned}
\Lambda
&=
I(S;M\mid L,R)-I(S;M'\mid L,R)\\
&=
I(S;M\mid L,R)-I(S';M'\mid L,R).
\end{aligned}
\tag{4}
\]

展开两项：

\[
I(S;M\mid L,R)
=
I(S;M\mid R)
+I(S;L\mid M,R)
-I(S;L\mid R),
\tag{5}
\]

以及 successor 版本。Stationarity给

\[
I(S;M\mid R)=I(S';M'\mid R).
\tag{6}
\]

此外 \(L\) 在 \(U^{\underline2}\) 上均匀，且给定 \(S\) 或 \(S'\) 都有恰好 \(n(u-n)\) 个 compatible oriented labels。因此

\[
I(S;L\mid R)
=
I(S';L\mid R)
=
\log\frac{u(u-1)}{n(u-n)}.
\tag{7}
\]

代入即得 (3)。非负性来自 conditional mutual information。证毕。

### 解释

\(\Lambda\) 是 update 在给定当前 label 后不可逆丢失的 source information。式 (3) 表明该 loss由 label与 predecessor state之间的 conditional correlation流向 label与 successor state之间的 correlation。

这不是 state-size budget。一个固定宽度 transducer可以在每一步产生正的 \(\Lambda\)，同时从新 label继续获得信息，因而长期保持 stationary。

## 3. 为什么 directed information 不能累积为 width lower bound

令完整 transcript为

\[
Z_T=(M_0,L_0,M_1,L_1,\ldots,M_T).
\]

虽然

\[
I(S_{0:T};Z_T\mid R)
\]

有标准 causal chain rule，但一般只有

\[
I(S_{0:T};Z_T\mid R)\le O(TH),
\]

而不是 \(\le H\)。

### Counterexample 3.1（one-bit stationary dissipation）

令外部 labels携带 IID bits \(B_t\)，并令 one-bit state update为

\[
M_{t+1}=B_t.
\]

在每一步更新前，旧 bit \(M_t\) 被完全丢弃，新 bit被写入。Stationary state始终只有

\[
H=1
\]

bit，但长度 \(T\) transcript恢复 \(B_0,\ldots,B_{T-1}\)，含 \(T\) bits information。若在每次写入前加一个 fixed erase label，可使每步 reverse collapse也为一 bit。

该 machine不是 AMQ；它反驳的是任何只使用 causality、finite width 和 directed-information chain rule便声称累计量 \(\le H\) 的抽象 theorem。Replacement deletions可以充当 erase，fresh insertions可以充当 reload，所以 AMQ proof若不使用 accepted-support/FPR结构同样无法排除此行为。

## 4. 精确 branching-program / online-cover reduction

### 4.1 Replacement history tree

令 \(\mathcal T_T\) 是 depth-\(T\) 的合法 replacement history tree。一个 node \(h\) 带 logical endpoint \(S(h)\in\Omega\)。合法 label

\[
\ell=(x,y),\qquad x\in S(h),\ y\notin S(h)
\]

给出 edge

\[
h\xrightarrow{\ell}h\ell.
\]

### 4.2 Deterministic right-congruent cover

一个 width-\(K\) deterministic cover branching program由以下对象组成：

1. coloring
   \[
   c:\mathcal T_T\to[K];
   \]
2. 对每个 label \(\ell\) 的 transition map
   \[
   \Delta_\ell:[K]\to[K]
   \]
   满足
   \[
   c(h\ell)=\Delta_\ell(c(h))
   \tag{8}
   \]
   对每条合法 edge成立；
3. 每个 color的 accepted support
   \[
   A(m)\supseteq
   \bigcup_{h:c(h)=m}S(h).
   \tag{9}
   \]

式 (8) 是 history automaton 的 right-congruence condition。它允许同一 logical set有多个 colors，也允许不同 sets共享 color。

### 4.3 Randomized pointwise cover number

令 \(\mathfrak C_K(T)\) 为全部 width-\(K\) deterministic right-congruent covers。定义

\[
\chi^\rightarrow_\varepsilon(\mathcal T_T)
\]

为最小 \(K\)，使存在 \(\mathfrak C_K(T)\) 上的 distribution \(\Pi\)，满足对每个固定 node \(h\) 与每个 \(z\notin S(h)\)，

\[
\Pr_{C\sim\Pi}[z\in A_C(c_C(h))]
\le\varepsilon.
\tag{10}
\]

### Theorem 4.1（exact finite-horizon equivalence）

存在一个使用 \(H\) persistent bits、支持全部 depth-\(T\) 合法 replacement histories的 ordinary randomized one-sided filter，当且仅当

\[
\chi^\rightarrow_\varepsilon(\mathcal T_T)\le2^H.
\tag{11}
\]

### Proof

给定 filter，固定 public tape \(r\) 后，以 physical state作为 color、update algorithm作为 \(\Delta_\ell\)，并令 \(A_r(m)\) 是 query YES-set。Determinism给 (8)，zero false negatives给 (9)，pointwise FPR给 (10)。

反之，初始化抽取 \(C\sim\Pi\)，persistent memory保存当前 color；update按 \(\Delta_\ell\)，query按 \(A_C(m)\)。式 (8)--(10)分别保证 update consistency、zero false negatives和 pointwise FPR。证毕。

这一定理把 ordinary dynamic AMQ space lower bound精确归约为 randomized online cover branching-program width，而没有 HI、monotonicity、locality或 canonical representation假设。

## 5. Carter relaxation与真正缺失的 width theorem

若删除 right-congruence条件 (8)，每层可独立选择 static covers。标准 counting/entropy只给

\[
\log\chi_{\varepsilon}^{\rm static}
\ge
n\log(1/\varepsilon)-o(n)
\tag{12}
\]

for \(u/n\to\infty\)。因此任何超过 Carter 的结论必须证明 transition compatibility本身导致

\[
\log\chi^\rightarrow_\varepsilon(\mathcal T_T)
\ge
n\log(1/\varepsilon)+c_\varepsilon n-o(n)
\tag{13}
\]

for some \(T=\omega(n)\) and \(c_\varepsilon>0\)。

随机插入/删除 permutation、stationary directed information及单-layer posterior entropy都只是 (13) 的 relaxations：

- insertion/deletion permutation path没有使用 tree中未访问的 replacement branches；
- directed information可对 reusable state重复收费；
- static posterior entropy删除了 (8)。

所以真正可发表的 combinatorial theorem应直接研究 (8)--(10)，例如证明：

> 任何 pointwise-\(\varepsilon\) 的 randomized right-congruent cover若在许多 layers上接近 Carter-optimal，则某个 color的 fresh-replacement successor supports必须膨胀，迫使更多 colors或违反 (10)。

它是 online set-cover / branching-program width theorem，而不是新的 Shannon chain rule。

## 6. 已排除的长程证明接口

### 6.1 仅随机 deletion permutation：no-go

静态 random-cover encoder可用

\[
n\log(1/\varepsilon)+o(n)
\]

bits存一个包含 initial set的随机 cover，并在全部 deletions中冻结该 cover。它满足 deletion path上的 zero-FN与 pointwise FPR。因此纯删除 permutation无法证明 dynamic premium。

### 6.2 Final-state mutual information：只看静态

\[
I(S_T;M_T\mid R)
\]

有单一 \(H\)-bit budget，但 query support只迫使 Carter rate。中间 state merging可在后来被删除。

### 6.3 Full transcript / directed information：重复收费

它看见所有中间 merging，却可随 \(T\) 线性增长。Counterexample 3.1否决其由 \(H\) 一次上界。

### 6.4 Reverse entropy without full label prefix：重复收费

\[
\sum_tH(M_t\mid M_{t+1},L_t,R)
\]

可重复擦除、恢复同一个 hidden bit。加入完整 label prefix后虽然 telescopes到 \(H\)，但又成为 state entropy的恒等分解，并不强迫 support growth。

## 7. 当前裁决

严格成果是：

1. stationary replacement process中的 exact entropy-production identity (3)；
2. 长程 directed information不受 persistent \(H\) 一次上界；
3. ordinary dynamic AMQ与 randomized right-congruent cover branching-program width的 exact equivalence (11)；
4. 超过 Carter 等价于证明 transition-compatible online cover width gap (13)。

没有得到 \(c_\varepsilon>0\) 的新证明。当前最小未解对象不再是某条随机排列上的信息量，而是整个 replacement history tree上的 right-congruent cover width。任何后续 spectral、fractional-cover或communication argument都应直接证明 (13)；若只作用于单路径，它会被 static frozen cover或 reusable-memory反例击穿。
