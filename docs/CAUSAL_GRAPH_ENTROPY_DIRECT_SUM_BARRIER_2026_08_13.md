# Ordinary dynamic AMQ 的 causal graph entropy：chain rule 与 direct-sum barrier

> 日期：2026-08-13。结论：history automaton 上的 public-coin right-congruence
> formulation 是严格的；最终状态 mutual information 有标准 direct sum；完整
> transcript directed information 也有 causal chain rule。但二者都不能把
> (U=4,n=2) 的三状态 transition gadget 张量成 (H\ge n)：前者看不见中间
> deletion/ghost distortion，后者对可复用内存重复收费。本文给出显式反例，说明
> 缺失的必须是 simultaneous-live 或 irreversible-information lemma，而不是普通
> Shannon chain rule。

## 1. History automaton 与 randomized right congruence

令 Ω 是所有容量至多 (n) 的合法 key-update histories，
(S(h)\subseteq U) 是 endpoint set。对合法 operation (o)，history automaton
有 partial edge

\[
h\xrightarrow{o}ho.
\tag{1}
\]

固定 public tape (r) 后，一个 (K=2^H)-state deterministic filter 是 map

\[
f_r:\Omega\to[K]
\tag{2}
\]

与 labeled maps δ_{r,o}，满足

\[
f_r(ho)=\delta_{r,o}(f_r(h)).
\tag{3}
\]

所以 kernel relation

\[
h\equiv_r h'\iff f_r(h)=f_r(h')
\tag{4}
\]

是 history automaton 的 right congruence：若同一个 (o) 对两 histories 都合法，
(h\equiv_r h') 强迫 (ho\equiv_r h'o)。它不必由 endpoint sets上的
equivalence relation诱导，同一 endpoint可有多个 classes。

每个 class (m) 的 minimal one-sided accepted set 是

\[
A_r(m)=\bigcup\{S(h):f_r(h)=m\}.
\tag{5}
\]

public-coin AMQ 是 right congruences ≡_r 的 mixture，并满足对每个 fixed
history (h) 和 fixed (x\notin S(h))，

\[
\Pr_R[x\in A_R(f_R(h))]\le\varepsilon.
\tag{6}
\]

式 (1)--(6) 是不假设 canonical、history independence、locality或 monotonicity
的精确 formulation。

## 2. 两个确实成立的 information chain rules

### 2.1 Final-state chain rule

令 (X_1,\ldots,X_k) 是 independent block histories，按任意固定 interleaving
喂给同一个 transducer；令 (M) 是最终 (H)-bit state，且 public tape (R)
独立于 inputs。总有

\[
\begin{aligned}
H
&\ge H(M\mid R)\\
&\ge I(X_1,\ldots,X_k;M\mid R)\\
&=\sum_{i=1}^k I(X_i;M\mid R,X_{<i}).
\end{aligned}
\tag{7}
\]

这是真正只对 persistent memory 收费一次的 direct sum。若能证明每一项条件
mutual information 都至少为某个常数 (c)，便得到 (H\ge ck)。

### 2.2 Transcript directed-information chain rule

设 (M_t) 是每次 operation 后的 state，(Y_t) 是 operation/query response；
完整 transcript记为 (Z=(M_0,Y_0,M_1,Y_1,\ldots))。标准 chain rule 给

\[
I(X_{1:k};Z\mid R)
=\sum_t I(X_{1:k};Z_t\mid R,Z_{<t}),
\tag{8}
\]

也可以按 blocks重排成 directed-information summands。式 (8) 能看见中间 ghost
queries和 deletion traces。

但是

\[
I(X_{1:k};Z\mid R)
\not\le H.
\tag{9}
\]

一个 (H)-bit mutable state 可以先编码一个 block、输出或被观察、擦除，再编码
下一个 block；完整 transcript可包含 (kH) bits。用式 (8) 直接下界 (H) 是
重复收费。

## 3. 显式 reusable-memory 反例

下面的 one-bit transducer足以否决任何“独立 history gadgets 的 causal
information逐块相加，从而下界 persistent bits”的无条件定理。

每个 block (i) 提供一个 independent bit (X_i\sim\operatorname{Bern}(1/2))，
并有三步操作：

1. `Load(i,X_i)`：state (M\leftarrow X_i)；
2. `Probe(i)`：输出当前 state；
3. `Clear(i)`：state (M\leftarrow0)。

对 (i=1,\ldots,k) 顺序执行。全部 transitions deterministic、key-only label
形式可编码进一个 finite history automaton，且 persistent state始终只有一 bit。
但 transcript probes 恢复整个 (X_{1:k})，所以

\[
I(X_{1:k};Z)=k,
\qquad
H(M_{\rm final})=0,
\qquad
H=1.
\tag{10}
\]

因此任何把“每个 gadget 的中间 query distortion”定义成 directed information
并声称其 sum ≤ persistent (H) 的 theorem 都是假的。deletion正好扮演
`Clear`：它允许旧 block information 合法消失。

这个反例不是 AMQ upper bound，但它反驳的是拟议 chain rule 本身；只要 theorem
仅使用 causality、right congruence和 independent sequential blocks，它就已满足
全部结构假设。

## 4. 为什么 U=4 gadget 不能直接进入式 (7)

有限 (U=4,n=2) theorem 说：如果 deterministic tape 只有三个 total states，
则五轨道 history-query分布下 average FP至少 (29/45)。形式上它给一个
cardinality-constrained distortion function

\[
D_3\ge29/45.
\tag{11}
\]

它没有给出如下 Shannon rate-distortion inequality：

\[
I(X;M\mid R,W)\ge1
\quad\text{whenever conditional pointwise FPR}\le1/2,
\tag{12}
\]

其中 (W) 是其他 blocks和先前 histories形成的 arbitrary side information。
条件化 (W=w) 后，单块诱导 machine仍可访问全部 (2^H) 个 residual global
states，而不是三个 states；所以 (11) 对式 (7) 的每个 conditional summand没有
任何适用性。

更根本地，有限 dual 的关键质量放在中间 histories (I_aD_a) 与
(I_aD_aI_b) 的 ghost queries。final state (M) 可以在 gadget结束后擦除这些
信息，所以 final mutual information式 (7) 不负责支付 finite transition premium。

由此得到严格结论：

> 仅凭三状态 finite gadget 与普通 Shannon chain rule，不能推出 independent
> (k)-block shared-state transducer 需要 (k\log_2 4) 或 (k) bits。

这不是尚未找到证明，而是 proof interface不成立。

## 5. 单块 causal graph entropy 的正确与错误定义

对 history source (P_X) 和 distortion tests Τ，可定义 final-state functional

\[
R_{\rm final}(D)
=\inf I(X;M\mid R),
\tag{13}
\]

infimum取遍 randomized right congruence encoders及满足平均 distortion (D) 的
queries。该 functional obeys ordinary source-coding direct sum，但它只约束 final
state tests。

也可定义 transcript functional

\[
R_{\rm causal}(D)
=\inf I(X;Z\mid R),
\tag{14}
\]

它能表达所有中间 tests，并对 independent sources tensorize；但式 (9)--(10)
说明它下界的是 total information throughput / communication，不是 reusable
persistent memory。

因此不存在一个同时无条件满足以下三项的 Shannon functional：

1. 看见任意时刻 deletion/ghost distortion；
2. 对 sequential independent gadgets作 additive direct sum；
3. 始终由 persistent memory (H) 上界一次。

reusable-memory反例证明这三项不可兼得。

## 6. Simultaneous-live blocks：唯一可行的 direct-sum入口

若在任何 probe 之前先加载 (k) 个 independent blocks，并要求它们同时保持 live，
不允许在最终联合测试前删除/擦除，则 final state必须同时承载它们。此时式 (7)
是正确入口。为了从中得到 (H\ge k)，仍需一个 **side-information robust
single-block lemma**：

\[
I(X_i;M\mid R,X_{<i})\ge1-o(1).
\tag{15}
\]

pointwise FPR本身通常只能给 Carter-type static rate-distortion下界；(U=4)
dynamic premium依赖中间 deletions，不能在 simultaneous-live final test 中自动
保留。因此式 (15) 不能由 (29/45) certificate推出。

另一种可能是证明 **information irreversibility**：虽然 deletion可改变 state，
某个 support-sensitive potential Ψ 不能下降，或下降必永久增加未来 FPR。若有

\[
\Psi(M_{t+1})-\Psi(M_t)
\ge\text{new block charge}-\text{FPR dissipation},
\tag{16}
\]

跨 blocks求和后可能避免 transcript重复收费。但 additive-syndrome、frozen-mask
以及 history-dependent ghost states都说明普通 Shannon entropy不是这样的 Ψ。

## 7. 对 Johnson replacement graph 的精确 formulation

在 (U=[2n]) 的容量层，vertices是 (n)-sets；directed replacement label
((a,b)) 在 (a\in S,b\notin S) 时把

\[
S\mapsto S-a+b.
\tag{17}
\]

ordinary transducer实际作用在 histories的 covering graph，而不是直接给
Johnson vertices着色：同一个 (S) 可有多个 representations。每条 tape的
right congruence quotient是 history covering graph 的 deterministic automaton
quotient；投影到 (J(2n,n)) 后一般只是多值 cover，不是 graph quotient或 equitable
partition。

所以 association-scheme谱只直接作用于 endpoint distributions。要收费
history multiplicity，至少需要 lifted vertices ((S,m)) 与 transition flows；
这会得到 constrained graph entropy / hidden-state rate-distortion问题，而不是
Johnson graph本身的 quotient entropy。

## 8. 严格裁决

已经证明：

1. public-coin ordinary dynamic AMQ 精确等价于 history automaton right
   congruences 的 mixture，并带 support-union distortion式 (5)--(6)；
2. final-state mutual information有一次性 chain rule式 (7)；
3. transcript directed information有 causal chain rule式 (8)，但不受 (H)
   一次上界；
4. one-bit reusable transducer严格否决 sequential-gadget causal direct sum；
5. (U=4) 的 cardinality dual不蕴含 side-information robust mutual-information
   lemma，因此不能推出 (U=2n) 下 (H\ge n-o(n))。

尚可能成立、且足够有含金量的正面定理只有两类：

1. simultaneous-live Johnson blocks 的 side-information robust graph-entropy
   inequality；
2. support-sensitive、对合法 deletion近似不可逆的全局势函数。

在证明其中之一前，把 finite (U=4) transition premium张量化成线性 ordinary
dynamic AMQ下界是不严谨的。
