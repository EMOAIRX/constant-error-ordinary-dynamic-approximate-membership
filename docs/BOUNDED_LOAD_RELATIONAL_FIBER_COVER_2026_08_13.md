# Bounded-load history-dependent binary summaries 的 sharp collision lemma

> 日期：2026-08-13。状态：严格 finite theorem。它不假设 canonical state，允许
> 同一 multiset 有多个 representations、不同 multisets 共享 state。结论把
> nontransitive overlap 的代价定量化：若在 load \(c\) 少于 \(c+1\) 个 states，
> 则存在一条固定合法 history，其 rejection 相对 one-sided information-theoretic
> maximum 至少损失 \(2^{-c}\)。因此 load \(2,3\) 的 maximal-rejection state
> counts 仍分别强迫为 \(3,4\)。

该结论是 history-dependent fiber-cover converse 的第一个有限版本。它尚未自动
提升为 Poisson blocks 下的 \(2.349083\) 全局 converse；最后一节明确说明缺少的
lifting lemma。

## 1. 模型

考虑一个 binary local summary。每个 key 有独立均匀 public bit
\(h(x)\in\{0,1\}\)。状态机有 deterministic key-only maps

\[
I_0,I_1,D_0,D_1.
\]

它支持容量至少 \(C\) 的任意合法 insertion/deletion history，且没有 false
negative。允许：

- 同一当前 multiset 因 history 不同到达多个 states；
- 一个 state 同时兼容多个 binary compositions；
- insert/delete 回环不返回原 state；
- arbitrary nontransitive fiber overlaps。

假设物理状态显式保持 current load。记 \(Q_c\) 为所有能在某条合法 history 后、
以 current load \(c\) 到达的物理 states，令

\[
d_c=|Q_c|.
\tag{1}

对一条固定 key history \(H\)，其结尾有 \(t\) 个 current members。fresh query
key 独立于 history keys。记 \(\operatorname{Rej}(H)\) 为对所有 public bits 取
概率后，nonmember query 被回答 `NO` 的概率。

### Lemma 1.1（universal one-sided ceiling）

对任意结尾 load 为 \(t\) 的固定 history，

\[
\boxed{
\operatorname{Rej}(H)\le2^{-t}.
}
\tag{2}

**证明。** 若 current members 同时包含 bit 0 和 bit 1，zero false negatives
迫使两个 query bits 都回答 `YES`。拒绝只可能发生在：

- 所有 \(t\) 个 member bits 为 0 且 query bit 为 1；
- 所有 member bits 为 1 且 query bit 为 0。

两事件概率之和为

\[
2^{-t}\cdot\frac12+2^{-t}\cdot\frac12=2^{-t}.
\]

history-dependent state 只能把某些 pure cases 也变成 `YES`，不能创造第三种安全
拒绝事件。\(\square\)

## 2. Monotone-word collision

固定 \(c\le C\)，选择 \(c\) 个不同 keys \(x_1,\ldots,x_c\)，按此顺序从空
状态插入。对 \(k=0,1,\ldots,c\)，定义 monotone word

\[
w^{(k)}=0^{c-k}1^k.
\tag{3}

\]

令 \(s_k\in Q_c\) 是当

\[
(h(x_1),\ldots,h(x_c))=w^{(k)}
\]

时 insertion history 到达的状态。

### Theorem 2.1（state saving forces a fixed-history rejection deficit）

若

\[
d_c\le c,
\tag{4}

则存在整数 \(1\le t\le c\) 和一条结尾 load 为 \(t\) 的固定合法 history
\(H\)，使

\[
\boxed{
\operatorname{Rej}(H)
\le2^{-t}-2^{-c}.
}
\tag{5}

**证明。** \(c+1\) 个 states \(s_0,\ldots,s_c\) 落在至多 \(c\) 个物理 states
中，所以存在 \(0\le k<\ell\le c\) 满足

\[
s_k=s_\ell.
\tag{6}

令

\[
T=\{c-\ell+1,\ldots,c-k\},
\qquad t=|T|=\ell-k.
\tag{7}

这正是两个 monotone words 不同的位置区间；在 \(T\) 上，\(w^{(k)}\) 全为
0，而 \(w^{(\ell)}\) 全为 1。构造固定 history \(H\)：先按顺序插入全部
\(x_1,\ldots,x_c\)，再删除所有 index 不在 \(T\) 的 keys，删除顺序任意固定。

从式 (6) 的同一个物理 state 出发，对同一列 key-only delete labels 执行
deterministic transitions，最终仍到达同一个 state，记为 \(u\)。但在完整 hash
assignment \(w^{(k)}\) 下，current \(t\) 个 keys 全为 0；在 assignment
\(w^{(\ell)}\) 下，它们全为 1。因此 state \(u\) 同时兼容 pure-zero 和 pure-one
current multisets。zero false negatives 强迫 \(u\) 对 query bit 0、1 都回答
`YES`。

Lemma 1.1 的 ceiling \(2^{-t}\) 假设每个 pure current assignment 都能拒绝相反
query bit。在 fixed history \(H\) 中，以下两个原本可拒绝的原子事件被迫变成
`YES`：

\[
(w^{(k)},\ h(\text{query})=1),
\qquad
(w^{(\ell)},\ h(\text{query})=0).
\]

每个事件概率为 \(2^{-c-1}\)，总损失为 \(2^{-c}\)。其他 assignments 不可能
超过 Lemma 1.1 ceiling，故得到式 (5)。\(\square\)

证明只用 insertion collision、共同合法 deletions 和 zero-FN；没有使用 fiber
overlap 的 transitivity、canonical lattice 或 insert/delete 互逆。

## 3. Sharp maximal-rejection corollary

### Corollary 3.1（bounded-load exact frontier at the top point）

若对所有结尾 load \(t\le C\) 的固定合法 histories 都有

\[
\operatorname{Rej}(H)>2^{-t}-2^{-C},
\tag{8}

则对每个 \(0\le c\le C\)，

\[
\boxed{d_c\ge c+1.}
\tag{9}

特别地，若所有 histories 都达到信息论最大 rejection \(2^{-t}\)，则前
\(C\) 层的 state counts 至少为

\[
1,2,3,\ldots,C+1.
\tag{10}

**证明。** 若某个 \(c\le C\) 有 \(d_c\le c\)，Theorem 2.1 给出 history \(H\)
满足

\[
\operatorname{Rej}(H)
\le2^{-t}-2^{-c}
\le2^{-t}-2^{-C},
\]

与式 (8) 矛盾。\(\square\)

下界可达到：保存 exact one-count \(0,1,\ldots,c\) 使用恰 \(c+1\) 个 states，
并在每个 history 上达到式 (2)。因此式 (9) 在 maximal-rejection endpoint 是
sharp 的。

## 4. Loads 2 and 3

### Corollary 4.1（load 2）

若 \(d_2\le2\)，则存在一条结尾 load \(t\in\{1,2\}\) 的 fixed history，使

\[
\operatorname{Rej}(H)
\le2^{-t}-\frac14.
\tag{11}

所以，要让 load 至多 2 的每条 history 都达到最大 rejection，必须且足以使用

\[
(d_0,d_1,d_2)=(1,2,3).
\tag{12}

这正是 canonical \(q=3\) quotient 的前三层；history dependence 不能在保持
这些层全额 rejection 的同时把 load-2 states 从 3 降到 2。

### Corollary 4.2（load 3）

若 \(d_3\le3\)，则存在一条结尾 load \(t\in\{1,2,3\}\) 的 fixed history，使

\[
\operatorname{Rej}(H)
\le2^{-t}-\frac18.
\tag{13}

所以，要在 load 至多 3 的全部 histories 上达到 maximal rejection，必须且足以
使用

\[
(d_0,d_1,d_2,d_3)=(1,2,3,4).
\tag{14}

## 5. Fiber-cover interpretation

对每个 physical state \(s\in Q_c\)，令

\[
\mathcal W_s
=\{w\in\{0,1\}^c:
\text{固定顺序插入 word }w\text{ 后到达 }s\}.
\tag{15}

\]

则 \((\mathcal W_s)_{s\in Q_c}\) 是 insertion words 的 partition；允许其他
histories 后，同一个 state 的 full relational fiber 只会更大。Theorem 2.1 的
内容是：若这个 partition 用少于 \(c+1\) 个 cells 覆盖 monotone chain

\[
0^c,0^{c-1}1,\ldots,1^c,
\]

则某个 cell 含两个 chain points。共同 deletion 将这个 collision 投影成一个
pure-zero/pure-one overlap，迫使 corresponding state 的 query acceptance union
为 \(\{0,1\}\)。

因此 bounded-load sharp tradeoff 可以写成：

\[
\boxed{
\text{少一个 load-}c\text{ cover cell}
\Longrightarrow
\text{某条 fixed history 至少多 }2^{-c}\text{ 的 YES mass}.}
\tag{16}

这比“nontransitivity 可能发生”更强：它定量说明任何利用 nontransitive fibers
压缩 monotone composition chain 的方案都必须支付一个可观测 FPR 代价。

## 6. 为什么还没有自动得到 \(2.349083\) global converse

binary canonical \(q=3\) 在 Poisson block load \(C_\lambda\) 下使用 rejection
profile

\[
2^{-c}\mathbf1\{c<3\}.
\tag{17}

Corollaries 4.1--4.2 表明，history-dependent local transducer 若减少前两三个
layers 的 state count，就必在某条局部 fixed history 上产生常数 rejection deficit。
这排除了“无代价地把 \(3\) states 改成 \(2\)”的局部突破。

但 ordinary block filter 的外层 hash 随机地把全局 fixed history 分配到 blocks。
Theorem 2.1 中的坏 history 是在知道一组 keys 已进入同一 local machine 后构造的；
pointwise FPR 模型不允许全局 adversary 根据 public random tape 选择 keys。因此
不能静默地在每个 block 部署该局部坏 history。

缺失的提升应是如下形式的 **oblivious occupancy lifting lemma**：

> 若正比例 blocks 的某个 load layer 少于 canonical cover cells，则存在一条与
> outer hash tape 独立的固定全局 history，使由随机 occupancy 自动产生的 local
> monotone collisions 带来与式 (16) 同阶的总 rejection deficit。

证明它需要把 collision witnesses 对 key identities 对称化，或用随机 fixed
histories + averaging 选出一条 deterministic history；同时必须确保共同 deletions
不依赖已观察到的 block assignments。目前本文没有完成这一步。

所以准确结论是：

1. bounded loads \(2,3\) 的 maximal-rejection state frontier 已对任意
   history-dependent transducer 闭合；
2. nontransitive overlap 的节省与 forced-YES 代价已有显式 \(2^{-c}\) 定量；
3. 将它积分进 Poisson/direct-product fixed-history 模型，仍需一个新的 occupancy
   lifting argument；在完成前不能宣称一般 history-dependent filters 满足
   \(2.349083n\) 下界。
