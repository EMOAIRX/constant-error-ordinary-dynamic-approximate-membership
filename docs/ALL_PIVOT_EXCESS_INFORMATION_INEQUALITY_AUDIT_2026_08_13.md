# All-pivot excess-information inequality：精确会计、ordinary反例与最小缺参

> 日期：2026-08-13。状态：finite-parameter weighted chain rule 是严格定理；
> 一个 ordinary、fixed-memory、arbitrary-history transducer 严格反驳把不同 parent
> source-posterior deficits作未加权直和，也展示 posterior pruning 与 operational
> full-fiber transport之间的缺口。结论：all-pivot dual weights下“deficit只收费一次”
> 本来就成立，但它仍不足以从 `u/n -> infinity` 恢复理想 hard all-pivot
> \(L_m\)；真正缺少的是 rank-redundancy/transport complementarity 或
> source-to-operational thickness invariant。

所有 logarithms 以 2 为底。

## 1. 有限参数 setup 与 conditioning

令

\[
X=(X_1,\ldots,X_b)
\tag{1}
\]

在给定 public context \(\Theta\) 后条件独立，\(R\) 是与 \((X,\Theta)\)
独立的 filter tape，\(M\) 是最终 \(H\)-bit state。对每个 pivot
\(s\in\mathcal S\)，固定一个 decode permutation \(\pi_s\)。在第 \(k\) 步前，
decoder已经知道

\[
C_{s,k}=(\Theta,R,X_{\pi_s(1)},\ldots,X_{\pi_s(k-1)}).
\tag{2}
\]

parent/child state \(F_{s,k}\) 必须是

\[
F_{s,k}=f_{s,k}(M,C_{s,k})
\tag{3}
\]

的确定函数。这正是 KLZ reverse simulation 所需的 measurability；不能把 future
hidden batches静默加入 \(C_{s,k}\)。

给定 \((C_{s,k},F_{s,k})=(c,f)\)，令 batch posterior 的 source-coordinate
union为 \(W_{s,k}(c,f)\)，其允许的 ordered batch universe为
\(\Omega(W_{s,k})\)。定义

\[
A_{s,k}
=H(X_{\pi_s(k)}\mid C_{s,k})
-\mathbb E\log|\Omega(W_{s,k})|,
\tag{4}
\]

\[
D_{s,k}
=\mathbb E\left[
\log|\Omega(W_{s,k})|
-H(X_{\pi_s(k)}\mid C_{s,k},F_{s,k})
\right].
\tag{5}
\]

只要 posterior确实支持于 \(\Omega(W_{s,k})\)，就有 exact decomposition

\[
\boxed{
A_{s,k}+D_{s,k}
=I(X_{\pi_s(k)};F_{s,k}\mid C_{s,k}).
}
\tag{6}
\]

这里所有 quantities先条件于完整 \((\Theta,R)\) 再平均。Pointwise FPR只能在
固定 source history后对 \(R\) 使用；不能在给定 \((R,F_{s,k})\) 后重新调用。

## 2. All-pivot weighted single-charge theorem

### Theorem 2.1

对每个 pivot \(s\)，

\[
\boxed{
\sum_{k=1}^b(A_{s,k}+D_{s,k})
\le I(X;M\mid\Theta,R)\le H.
}
\tag{7}

因此对任意 dual weights \(\lambda_s\ge0\)、\(\sum_s\lambda_s=1\)，

\[
\boxed{
\sum_s\lambda_s\sum_k(A_{s,k}+D_{s,k})
\le I(X;M\mid\Theta,R)\le H.
}
\tag{8}

**证明。** 由式 (3) 和 data processing，

\[
I(X_{\pi_s(k)};F_{s,k}\mid C_{s,k})
\le I(X_{\pi_s(k)};M\mid C_{s,k}).
\]

对 decode permutation 使用 chain rule，右侧求和为
\(I(X;M\mid\Theta,R)\)。代入式 (6)得到式 (7)。式 (8) 是式 (7) 的
convex combination。\(\square\)

所以在 all-pivot convex dual真正使用的归一化权重下，“多个 parents 的
posterior deficit只能对 final state收费一次”无需新 lemma；它已经是普通 chain
rule。不同 pivots的 bounds不能未加权相加，因为那会把同一个 \(H\)-bit message
重复收费。

## 3. 为什么 single charge 仍不能保留 ideal \(L_m\)

设第 \(s\) 个 ideal hard-rank branch为 \(L_s\)，transport debit为
\(T_s=\sum_kT_{s,k}\)。假设最乐观地已有

\[
T_{s,k}\le D_{s,k}+\Delta_{s,k},
\qquad
\sum_s\lambda_s\sum_k\Delta_{s,k}=o(n).
\tag{9}
\]

令

\[
\bar A=\sum_s\lambda_s\sum_kA_{s,k},
\qquad
\bar D=\sum_s\lambda_s\sum_kD_{s,k},
\qquad
C=\sum_s\lambda_sL_s.
\tag{10}
\]

式 (8)--(9) 最多给

\[
H\ge\bar A+\bar D,
\qquad
H\ge C-\bar D-o(n).
\tag{11}
\]

于是

\[
\boxed{
H\ge\max\{\bar A+\bar D,C-\bar D\}-o(n).
}
\tag{12}

对未知 \(\bar D\) 最坏化仍是

\[
\boxed{
H\ge\frac{\bar A+C}{2}-o(n).
}
\tag{13}

这说明问题不是 deficit在不同 pivots间被重复收费。真正的 factor two来自同一
parent内的两种用途：

1. \(D\) 是 hard ambient rank相对 posterior Shannon code的冗余；
2. suffix transport又允许 debit \(T\le D\)。

要恢复 \(C\)，需要控制 \(D+T\)，而不只是跨 parents控制 \(D\)。普通 entropy
chain rule没有给

\[
D+T\le D
\quad\text{或}\quad T=o(n).
\tag{14}
\]

## 4. 一个 parity source：跨 pivots 未加权 deficit 直和严格失败

取 independent uniform bits \(B_1,\ldots,B_b\)，令

\[
M=B_1\oplus\cdots\oplus B_b.
\tag{15}
\]

对每个 \(k\)，取 context \(C_k=B_{-k}\)。则

\[
I(B_k;M\mid B_{-k})=1,
\tag{16}
\]

但

\[
I(B_{1:b};M)=1.
\tag{17}
\]

所以

\[
\sum_{k=1}^bI(B_k;M\mid B_{-k})=b
\tag{18}
\]

不能由 final-state information上界。这些 contexts恰好对应“让每个 batch分别在
不同 pivot中最后解码”。在任何一个固定 decode permutation内，只有最后一个 bit
支付 1，其余 chain-rule increments总和仍为 1。因而：

- 单 pivot求和合法；
- 归一化 pivot convex combination合法；
- 从每个 pivot挑一个最有利 parent再未加权相加不合法。

## 5. Ordinary arbitrary-history transducer embedding

上面的 parity现象可以嵌入真正的 ordinary dynamic AMQ，而不只是抽象 random
variables。

令 universe分成 \(b\) 个四元 blocks \(U_k=\{0,1,2,3\}\)。Source endpoint在
每个 block选择一条 edge

\[
X_k\in\binom{U_k}{2}
\tag{19}
\]

且各 blocks独立均匀。把六条 edges分成

\[
\mathcal E_0=\{01,02,23\},
\qquad
\mathcal E_1=\{03,12,13\}.
\tag{20}
\]

每个 family都有三条 edges，且 vertex union均为整个 \(U_k\)。记 edge color为
\(c(X_k)\in\{0,1\}\)。容量为 \(n=2b\)。

public tape先取公平 coin \(Z\)。Filter有如下两 branches，并 padding 到同一个
fixed memory block。

### Exact branch \(Z=0\)

永久精确保存当前 set，queries与updates均 exact。

### Lossy branch \(Z=1\)

初始也精确保存当前 set。当 current load第一次达到 \(2b\) 且每个 block恰有两个
members时，压缩为一 bit

\[
P=\bigoplus_{k=1}^bc(X_k).
\tag{21}
\]

之后进入 absorbing mode：所有 updates被忽略，所有 queries回答 YES。若 profile
从未满足，始终留在 exact mode。

### Lemma 5.1（ordinary correctness）

该 filter使用 fixed worst-case memory，支持任意长合法 key-only histories，
zero false negatives，并对每条 fixed history与每个 fixed current nonmember有
FPR至多 \(1/2\)。

**证明。** Exact branch从不误报。Lossy branch在 compression前也 exact，之后
ALL-YES，故永远没有 false negative。对任意 fixed history/nonmember，FP只可能
发生在 \(Z=1\) branch，概率至多 \(1/2\)。Absorbing updates无需知道 logical
current set；合法性 promise属于外部 operation sequence。固定 memory取 exact
branch所需容量并加入 mode/parity metadata即可。\(\square\)

### Source posterior deficits

在 canonical source build endpoint：

- exact branch posterior为 point mass；其信息全部属于 support term \(A\)，
  within-union deficit为零；
- lossy branch给定 \(P\) 后 posterior均匀分布在 \(6^b/2\) 个 source vectors上，
  每个 block的 coordinate union仍为四个 vertices。因此 global excess deficit
  恰为一 bit。

故平均 global excess deficit只有

\[
\mathbb E D_{\rm global}=\frac12.
\tag{22}
\]

但对每个 \(k\)，若 context给出所有其他 \(X_{-k}\)，则 lossy branch的 parity
确定 \(c(X_k)\)。Batch posterior均匀分布在 \(\mathcal E_0\) 或
\(\mathcal E_1\) 的三条 edges上，coordinate union仍为四 vertices，所以

\[
D_k=\log\binom42-\log3=1
\tag{23}
\]

on the lossy branch，而 exact branch的 \(D_k=0\)。因此

\[
\mathbb ED_k=\frac12,
\qquad
\sum_{k=1}^b\mathbb ED_k=\frac b2.
\tag{24}

相对式 (22) 可重复任意大的 factor。这是 ordinary、infinite-history、pointwise
half-error transducer中的真实 multi-parent repetition，不是 posterior-only toy。

它不违反 Theorem 2.1：这些 \(b\) favorable contexts来自不同 decode
permutations。任一固定 permutation内，parity总共只贡献一 bit。

## 6. 同一例中的 posterior pruning 与 operational transport分离

固定一个 lossy parent及其 color family \(\mathcal E_z\)。抽取实际 edge
\(X_k\)，再从两个 nonmember vertices中均匀抽取 suffix insertion label \(Y_k\)。
在 source posterior中删除所有与 \(Y_k\) 相交的 witness edges。直接枚举给：

\[
|W_{Y_k}|=
\begin{cases}
2,&\text{probability }1/3,\\
3,&\text{probability }2/3.
\end{cases}
\tag{25}
\]

因此 unordered hard-list shrinkage为

\[
\begin{aligned}
T_k
&=\mathbb E\log
\frac{\binom42}{\binom{|W_{Y_k}|}2}\\
&=\frac13\log6+\frac23\log2\\
&=1.5283208\ldots>0.
\end{aligned}
\tag{26}

同时

\[
D_k=1,
\qquad
I(X_k;Y_k\mid c(X_k))
=H(Y_k\mid c(X_k))-1
=0.9182958\ldots,
\tag{27}
\]

所以有限参数 pruning theorem的

\[
T_k\le D_k+I(X_k;Y_k\mid c(X_k))
\tag{28}
\]

严格成立。

但 operationally，lossy absorbing state在 suffix后仍是同一个 ALL-YES state；
它的 full operational endpoint union仍是整个 universe，真正 full-fiber transport
loss为零。正 transport只存在于 KLZ source posterior list，不存在于同 physical
state的完整 operational fiber。

这说明 ordinary semantics本身不保证：

> source posterior pruning所见的 union shrinkage，可以作为 operational
> right-congruence parent的 hard transport saving。

Cover/tombstone或absorbing continuation metadata可以在 source endpoint上不可见，
却让同一 state拥有大量 non-source operational witnesses。

## 7. 严格裁决：什么成立、什么失败

### 已证明成立

1. 每个 pivot内部的 \(A+D\) 由 final-state mutual information收费一次；
2. 任意归一化 all-pivot dual combination仍只收费一次，式 (8) 已是 exact theorem；
3. 单 parent incidence theorem的 \(T\le D+\Delta\) 可在
   \(u/n\to\infty\) 的适当参数窗口给 \(\Delta=o(n)\)。

### 被严格反驳

1. 从不同 pivots各挑一个 favorable parent后，将 deficits未加权直和；
2. 仅凭“所有 parents由同一 final state导出”证明
   \(\sum D_{parent}\le I(X;M)\)；
3. 把 source-posterior union shrinkage自动等同于 operational full-fiber
   transport；
4. 认为 weighted single-charge本身足以恢复 ideal \(L_m\)。式 (12)--(13)
   表明它仍停在 midpoint。

## 8. 恢复 ideal all-pivot bound 所需的最小 invariant

要从理想 hard-rank saving \(K\) 推出 \(H\ge A+K\)，需要的不是另一个普通
chain rule，而是以下二者之一。

### 8.1 Rank--transport complementarity

对 dual-weighted全部 active parent/batch pairs证明

\[
\boxed{
\sum_s\lambda_s\sum_k
\bigl(D_{s,k}+T_{s,k}\bigr)
\le
I(X;M\mid\Theta,R)-\bar A+o(n).
}
\tag{29}

因为 hard-rank correctness给 \(K\le D+T\)，式 (29)会直接推出
\(K\le H-\bar A+o(n)\)，即 \(H\ge\bar A+K-o(n)\)。

式 (29) 不是 Shannon identity：单 parent四元 posterior例已可令 \(D=T\)，而
Section 5--6 的 ordinary transducer展示 source-posterior版本也没有自动的
operational理由。

### 8.2 Source-to-operational thickness / principal-fiber invariant

对每个 active physical parent state \(g\)，令

\[
\mathcal P_g=\text{KLZ source completions reaching }g,
\qquad
\mathcal O_g=\text{all legal operational histories reaching }g.
\tag{30}
\]

需要证明 source posterior在所有 relevant common-suffix sections中对
\(\mathcal O_g\) 具有定量 thickness，例如一个足以推出式 (29) 的
fractional domination：

\[
\Pr_{\mathcal P_g}[E]
\ge2^{-o(n)}\Pr_{\nu_g}[E]
\tag{31}
\]

对某个定义在 full operational fiber上的共同 prior \(\nu_g\)，并对全部 active
parent suffix events \(E\) 同时成立。等价表述可以是：active source fibers拥有
transition-compatible principal core，且所有 suffix-pruned unions由同一个 joint
core posterior见证。

Section 5 的 absorbing branch最大程度违反式 (31)：source posterior只有一个
parity cell，而 operational fiber包含 compression后任意更新产生的 worlds；source
pruning会缩小，operational union完全不缩小。

仅要求 pairwise parent overlap、共同 final state、或每个 parent单独有大 source
fiber都不够。所需 invariant必须同时控制：

1. 多个 parents的 source fibers在同一 operational fiber中的联合厚度；
2. common suffix下 witness mass，而非只控制 support union；
3. rank redundancy \(D\) 与 transport debit \(T\) 的联合而非分别上界；
4. dual weights下single final-state budget。

## 9. 最终结论

对所问 all-pivot excess-information路线，答案分两层：

1. **是：** posterior deficits在归一化 all-pivot convex combination中本来就只
   收费一次，这是 Theorem 2.1 的 exact chain rule。
2. **否：** 这一事实不能把 `u/n -> infinity` 下的 bound恢复到理想
   all-pivot \(L_m\)。同一 deficit仍可同时表现为 hard-rank redundancy和
   transport debit，留下不可消除的 factor-two/midpoint barrier。

因此下一步若继续追求旧 \(C_q\)，必须证明式 (29) 这样的新 combinatorial
complementarity，或证明 KLZ source fibers相对 full operational fibers满足式
(31) 的 transition-compatible thickness。继续对已有 mutual-information chain
rule重新排列，不可能完成升级。
