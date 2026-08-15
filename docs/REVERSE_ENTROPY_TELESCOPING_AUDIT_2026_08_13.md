# Random deletion trajectories 的 reverse entropy：精确恒等式与 no-go

> 日期：2026-08-13。状态：严格信息论恒等式与反例。结论是：逐步 reverse
> entropy
> \(H(M_{j-1}\mid M_j,X_j,R)\) 一般不 telescoping，也不受单个 \(H\)-bit
> memory预算控制；它可在线性多步中反复收费同一个隐藏 bit。正确 telescoping
> 对象必须加入 delete-label uncertainty，或等价地使用 directed information
> correction。修正后总量至多 \(H\)，但 frozen-mask / reversible-cover 压力测试
> 表明它本身不强迫 accepted shadows变小，因此仍不足以推出
> \(2.349083n\) ordinary converse。

## 1. 模型与记号

固定 arbitrary public-tape dynamic filter。令 \(R\) 为 tape，\(M_0\) 为某条
initial insertion history 后的 state。随后删除一个随机 ordered sequence

\[
X_1,\ldots,X_T,
\]

并令

\[
M_j=D_{R,X_j}(M_{j-1}),
\qquad 1\le j\le T.
\tag{1}

\]

删除序列可以由随机当前 set permutation产生，因而 \(X_j\) 与 state trajectory
高度相关。只要求给定 \((R,M_{j-1},X_j)\) 后 successor \(M_j\) 确定。

写

\[
X_{\le j}=(X_1,\ldots,X_j),
\qquad X_{>j}=(X_{j+1},\ldots,X_T).
\]

所有熵均以 bits计。

## 2. 单步 reverse indegree identity

### Lemma 2.1

对每一步，

\[
\boxed{
H(M_{j-1}\mid M_j,X_j,R)
=H(M_{j-1}\mid X_j,R)-H(M_j\mid X_j,R).
}
\tag{2}

**证明。** 给定 \((X_j,R)\)，\(M_j\) 是 \(M_{j-1}\) 的确定函数，所以

\[
H(M_{j-1},M_j\mid X_j,R)=H(M_{j-1}\mid X_j,R).
\]

再按另一顺序展开 joint entropy 即得。\(\square\)

式 (2) 是 delete map在当前 distribution 下的 entropy loss，也可由 expected
log reverse indegree上界：

\[
H(M_{j-1}\mid M_j,X_j,R)
\le
\mathbb E\log_2
|D_{R,X_j}^{-1}(M_j)\cap\operatorname{supp}(M_{j-1}\mid X_j,R)|.
\tag{3}

\]

但式 (2) 的两个 conditional entropies每一步 conditioning 的 \(X_j\) 不同，
所以直接求和不 telescope。

## 3. Exact pathwise telescoping correction

### Theorem 3.1（reverse entropy balance）

定义

\[
r_j:=H(M_{j-1}\mid M_j,X_{\le j},R).
\tag{4}

\]

则有精确恒等式

\[
\boxed{
\sum_{j=1}^T r_j
=H(M_0\mid R)-H(M_T\mid X_{\le T},R)
-\sum_{j=1}^T I(M_{j-1};X_j\mid X_{<j},R).
}
\tag{5}

**证明。** 给定 \((R,X_{\le j})\)，式 (1) 使 \(M_j\) 成为 \(M_{j-1}\) 的
确定函数，所以

\[
r_j
=H(M_{j-1}\mid X_{\le j},R)-H(M_j\mid X_{\le j},R).
\tag{6}

\]

第一项改写为

\[
H(M_{j-1}\mid X_{<j},R)
-I(M_{j-1};X_j\mid X_{<j},R).
\]

把式 (6) 对 \(j\) 求和；相邻的
\(H(M_j\mid X_{\le j},R)\) 与下一项
\(H(M_j\mid X_{\le j},R)\) telescope，得到

\[
\sum_jr_j
=H(M_0\mid R)-H(M_T\mid X_{\le T},R)
-\sum_j I(M_{j-1};X_j\mid X_{<j},R).
\tag{7}

\]

特别地，

\[
\boxed{
\sum_{j=1}^T
H(M_{j-1}\mid M_j,X_{\le j},R)
\le H(M_0\mid R)\le H.
}
\tag{8}

\]

\(\square\)

mutual-information correction 的符号是负号：state与当前 delete label 的相关性
必须从 reverse-loss budget 中扣除，不能再收费一次。因此 prefix-conditioned
reverse entropy确实只有单个预算。

### Corollary 3.2（random permutation）

若 \(X_1,\ldots,X_T\) 是 initial set 的随机 deletion permutation，则式 (5)--(8)
仍逐字成立。state可能泄露下一个 delete label的信息；这部分由

\[
I(M_{j-1};X_j\mid X_{<j},R)
\]

从 reverse-loss budget中扣除，不能同时作为 reverse indegree 再收费一次。

## 4. 用户提出的逐步量为何不受 H 控制

原始候选量是

\[
\widetilde r_j
=H(M_{j-1}\mid M_j,X_j,R),
\tag{9}

\]

它没有 conditioning on previous delete labels。下面给出最小反例。

### Theorem 4.1（one-bit repeated-charge counterexample）

对任意 \(L\)，存在 \(H=1\) bit、长度 \(2L\) 的 deterministic labeled
trajectory，使

\[
\sum_{j=1}^{2L}
H(M_{j-1}\mid M_j,X_j)=L.
\tag{10}

**构造。** 令隐藏 bit \(Z\sim\operatorname{Bernoulli}(1/2)\)。使用一个不含
\(Z\) 的固定 erase label \(a\)，以及 restore labels \(b_0,b_1\)。定义

\[
D_a(m)=0,
\qquad
D_{b_z}(m)=z.
\]

令 deletion labels 依次为

\[
(a,b_Z,a,b_Z,\ldots,a,b_Z).
\]

每个 erase step 前 state为 \(Z\)、后 state为 0，而且当前 label \(a\) 不泄露
\(Z\)，所以贡献

\[
H(Z\mid 0,a)=1.
\]

每个 restore step把 0 映到 \(Z\)，其 predecessor确定，贡献 0。故 \(2L\)
steps总和为 \(L\)，而 state始终只有1 bit。

这个抽象 transducer可嵌入随机合法 deletion trajectories：initial random set
同时决定 hidden bit \(Z\) 和后续选择 \(b_Z\) key；所有待删 keys预先存在，按上面
顺序删除。它不需要是好的 membership filter；它足以否决从 deterministic
deletions单独推出 \(\sum\widetilde r_j\le H\)。\(\square\)

直观上，每步只条件于当前 \(X_j\)，忘记了过去 labels曾经恢复过同一 hidden bit，
于是同一 bit可被反复擦除、恢复和重新收费。Theorem 3.1 的 full-prefix conditioning
正好关闭这个漏洞。

## 5. Reverse branching 与 accepted shadow没有一般单调关系

### Pressure test 5.1（frozen false-positive mask）

令 public tape给出一个 frozen set \(F_R\subseteq U\)，每个 key以边缘概率
\(\varepsilon\) 落入 \(F_R\)。query接受

\[
A_R(S)=S\cup F_R.
\tag{11}

\]

state exact保存当前 set或其某个可删除表示。若 exact保存，delete maps在 reachable
states上 injective，所有 prefix-conditioned reverse entropies \(r_j=0\)，但每层
accepted shadow约为 \(\varepsilon u\)，同时 pointwise FPR恰为
\(\varepsilon\)。所以

\[
\text{large accepted shadows}
\not\Longrightarrow
\text{large reverse entropy}.
\]

该结构空间很大，不是 upper-bound反例；它否决的是不含 forward state-size项的
局部不等式。

### Pressure test 5.2（permutation cover / holonomy）

令 logical set \(S\) 附带一个 fiber coordinate \(g\in G\)，每个 deletion key
作用为 permutation \(g\mapsto g\sigma_x^{-1}\)。所有 delete maps严格可逆，所以

\[
r_j=0
\]

对全部 steps，但 history dependence与non-Abelian holonomy可以任意复杂。query
只使用 logical support union。这说明

\[
\text{history-dependent cover complexity}
\not\Longrightarrow
\text{reverse entropy}.
\]

reverse entropy只测量 many-to-one collapse，不测量可逆fiber运动。

### Pressure test 5.3（maximally erasing summary）

反过来，delete map可把许多 predecessor states全部映到一个 successor，使
\(r_j\) 很大，但 query在 predecessor和successor都选择ALL-YES。于是

\[
\text{large reverse entropy}
\not\Longrightarrow
\text{useful rejection}.
\]

因此不存在只依赖 \((r_j,|W_j|)\) 各自边缘的一维单调关系；需要 forward state
entropy、reverse collapse和accepted-set branch saturation三者的联合不等式。

## 6. 一个合法但有限的联合 identity

Theorem 3.1 可与 same-tape shadow path inequality并列：

\[
\log(u)_{\underline n}
\le H(M_0\mid R)+\sum_j\mathbb E\log|W_j|,
\tag{12}

\]

以及

\[
\sum_j r_j
=H(M_0\mid R)-H(M_T\mid X_{\le T},R)
-\sum_jI(M_{j-1};X_j\mid X_{<j},R).
\tag{13}

\]

二者共享同一个 \(H(M_0\mid R)\)；不能把两个右侧的 \(H(M_0)\) 各自上界为
\(H\) 后再相加，声称得到 \(2H\) budget。正确消元是由式 (14) 写

\[
H(M_0\mid R)
=H(M_T\mid X_{\le T},R)
+\sum_j r_j
+\sum_jI(M_{j-1};X_j\mid X_{<j},R),
\tag{14}

\]

再代入式 (13)。这只是同一个 initial-state entropy的分解，没有凭空产生更强
下界。

若要超过静态 \(n\log(1/\varepsilon)\)，真正缺少的是一个 **branch saturation
lemma**，形式应类似：

\[
\sum_j\bigl(\log N_{t_j}-\mathbb E\log|W_j|\bigr)
+\sum_j r_j
+H(M_T\mid X_{\le T},R)
+\sum_jI(M_{j-1};X_j\mid X_{<j},R)
\ge c n,
\tag{15}

\]

其中每一项都来自式 (15) 的单一预算分解，且 frozen mask、injective exact state、
permutation cover和ALL-YES collapse都不能击穿。本文没有证明式 (16) 对某个
\(c>0\) 成立；它是被压力测试后剩下的准确目标。

## 7. 裁决

严格成立：

1. prefix-conditioned reverse entropy满足单预算 telescoping，式 (5)--(8)；
2. 未记录过去 labels 的逐步 reverse entropy可对同一 hidden bit重复收费到
   \(\Theta(T)\)，即使 state只有1 bit；
3. reverse entropy、accepted shadow size和history-dependent holonomy之间不存在
   两两的普适单调关系。

因此 branching-sensitive路线不能只把
\(H(M_{j-1}\mid M_j,X_j,R)\) 加进旧 shadow bound。正确下一步是证明类似式
(16) 的四项联合 saturation inequality，并且只能使用一次
\(H(M_0\mid R)\) budget。在该 lemma完成前，reverse multiplicity尚未给出
\(2.349083n\) ordinary lower bound。
