# Relational collision 的 oblivious occupancy lifting

> 日期：2026-08-13。状态：严格 finite-\(n\) 与 Poisson lifting theorem，但模型
> 范围必须明确：local transducer 是 **label-oblivious**，update 只读取
> \((\text{block},h(x))\)，query 只读取 local state 与 \(h(x)\)。它允许完全
> history-dependent、multiple representations 和 nontransitive overlaps。
> 随机 survivor mask 解决了 outer-hash-adaptive history 的量词问题，但不能删除
> label-oblivious 假设。

本文把 bounded-load collision lemma 提升到固定全局 history：若每个 block 的
load-\(c\) reachable states 至多为 \(c\)，则存在一个与 public tape 独立的
deterministic insert/delete history，使固定 nonmember query 的 rejection 出现
显式 deficit。

## 1. 全局模型与范围

固定 \(n\) 个不同 update keys

\[
x_1,\ldots,x_n
\]

以及一个固定 query key \(y\)，且 \(y\notin\{x_1,ldots,x_n\}\)。公共随机标签
对每个 key 独立给出

\[
g(x)\in[B],
\qquad h(x)\in\{0,1\},
\tag{1}

其中 \(g\) 均匀、\(h\) 均匀且彼此独立。

每个 block 运行相同 deterministic local transducer。它可以是 history-dependent：
同一 local multiset 可有多个 states，不同 multisets 可共享 state，insert/delete
无需互逆，overlap relation 无需传递。但要求：

1. `Insert/Delete(x)` 对 local machine 提供的信息只有 \(h(x)\)；
2. `Query(y)` 对 query rule 提供的信息只有 current local state 与 \(h(y)\)；
3. local machine 不读取 key identity、其他 public hash bits 或完整 tape；
4. zero false negatives 对每条 tape 成立。

令 \(Q_c\) 为从 local empty state 通过任意合法 local history、以 load \(c\)
到达的 physical states，记

\[
d_c=|Q_c|.
\tag{2}

假设对某个固定 \(c\ge2\)，

\[
d_c\le c.
\tag{3}

这是 local state-saving hypothesis。

### 为什么 label-oblivious 不可省略

bounded-load pigeonhole 比较不同 inner-bit assignments \(w^{(k)}\)。若 transition
或 query 还能读取完整 public tape，那么“两个 assignments 到达同一个 bitstring
state”并不保证后续 delete transition或 query behavior 相同：public tape 本身是
额外的免费 side information。本文所有 same-state indistinguishability 都依赖
上述 1--3。

因此下面不是 arbitrary ordinary filter 的 WLOG reduction。要覆盖一般 public-
tape algorithm，需要 same-tape collision/communication argument；random survivor
mask 本身不能提供它。

## 2. 每个 ordered block list 的 canonical witness

对任意 \(c\) 个 key identities 组成的 ordered list

\[
L=(z_1,ldots,z_c),
\]

从 local empty state 按该顺序插入。考虑 \(c+1\) 个 monotone inner words

\[
w^{(k)}=0^{c-k}1^k,
\qquad 0\le k\le c.
\]

由式 (3)，至少两个 words 到达同一 physical state。为使 witness 对 key list
确定且与 random survivor mask 独立，按 lexicographic rule 选择最小 collision pair

\[
(k_L,\ell_L),
\qquad k_L<\ell_L.
\tag{4}

令

\[
T_L=\{c-\ell_L+1,\ldots,c-k_L\},
\qquad t_L=|T_L|\in[c].
\tag{5}

\]

这个 witness 可依赖 ordered key identities 若 local transition 本身允许这样；在
本文 label-oblivious 模型中它实际只依赖 transducer 与 \(c\)。即使允许
block-specific fixed transducers，也可对每个 block 分别采用确定 tie-breaking；
后续 survivor probability 只使用 \(|T_L|\)。

## 3. 随机固定历史

证明中临时引入 independent survivor indicators

\[
M_i\sim\operatorname{Bernoulli}(\alpha),
\qquad 0<\alpha<1.
\tag{6}

\]

给定 mask \(M=(M_1,ldots,M_n)\)，定义一条完全确定的合法 history \(H_M\)：

1. 按顺序插入全部 \(x_1,ldots,x_n\)；
2. 按同一固定全局顺序删除所有 \(M_i=0\) 的 keys；
3. 查询固定 nonmember \(y\)。

一旦 \(M\) 固定，\(H_M\) 与 public hash tape 无关，满足 pointwise-history 模型的
量词。随机 mask 只用于 averaging，最终会选出一个 deterministic \(M^*\)。

令 query target block 为 \(J=g(y)\)，并记删除前该 block 中 update keys 的 ordered
list 为 \(L_J\)，其 load 为

\[
C=|L_J|\sim\operatorname{Bin}(n,1/B).
\tag{7}

\]

条件于 \(C=c\) 及 ordered list \(L_J=L\)，事件

\[
E_L=\{M\text{ 在 }L\text{ 上恰保留 ranks }T_L\}
\tag{8}

的概率是

\[
\Pr_M(E_L)=\alpha^{t_L}(1-\alpha)^{c-t_L}.
\tag{9}

该概率与 outer hash、inner bits 独立。对 block 外 mask bits 不作限制。

## 4. 精确 deficit lemma

### Theorem 4.1（finite-\(n\) oblivious occupancy lifting）

在式 (1)--(3) 的模型中，对任意 \(0<\alpha<1\)，存在一个 deterministic mask
\(M^*\) 及对应 fixed history \(H_{M^*}\)，使固定 nonmember \(y\) 的 rejection
满足

\[
\boxed{
\operatorname{Rej}(H_{M^*},y)
\le
\mathbb E\,2^{-S}
-\Pr[C=c]\,2^{-c}
\min_{1\le t\le c}
\alpha^t(1-\alpha)^{c-t},
}
\tag{10}

其中

\[
S\sim\operatorname{Bin}(n,\alpha/B)
\tag{11}

是 deletion 后 query block 的 survivor load。因此第一项精确等于

\[
\mathbb E2^{-S}
=\left(1-\frac{\alpha}{2B}\right)^n,
\tag{12}

且

\[
\Pr[C=c]
={n\choose c}B^{-c}(1-B^{-1})^{n-c}.
\tag{13}

**证明。** 先联合平均 \(M,g,h\)。对任意 fixed \((M,g)\)，query block 当前
有 \(S\) 个 members。one-sided universal ceiling 给 inner-bit 平均 rejection
至多 \(2^{-S}\)。对 \((M,g)\) 再平均得到式 (12)。

现在限制到事件 \(C=c\)。条件于 ordered list \(L_J=L\)，若 survivor mask 恰为
\(E_L\)，则 bounded-load monotone collision 的两份完整 inner assignments
\(w^{(k_L)}\)、\(w^{(\ell_L)}\) 在插入全部 \(c\) keys 后到达同一 local state。
随后删除相同 complement ranks，deterministic label-oblivious transitions 保持状态
相同；剩余 \(t_L\) keys 在两个 assignments 中分别全 0 与全 1。query rule 只见
该 state 与 query bit，所以 zero-FN 强迫两个 query bits 都 `YES`。

相对 current load \(t_L\) 的 ceiling \(2^{-t_L}\)，这两个完整 assignment-query
原子各损失 \(2^{-c-1}\)，合计精确 deficit 至少 \(2^{-c}\)。注意 mask 已固定
complement bits，但 inner assignments 仍指定删除 keys 的 bits；因此每个完整 word
概率确为 \(2^{-c}\)，不能错误地改成 \(2^{-t_L}\)。

由式 (9)，条件平均 deficit 至少

\[
2^{-c}\alpha^{t_L}(1-\alpha)^{c-t_L}
\ge
2^{-c}\min_{1\le t\le c}
\alpha^t(1-\alpha)^{c-t}.
\]

乘以式 (13) 得联合平均上界 (10) 的右侧。最后，若每个 deterministic mask
的 rejection 都严格大于该联合平均上界，则对 \(M\) 平均也严格大于，矛盾。
故至少存在一个确定 \(M^*\) 满足式 (10)。\(\square\)

### 删除顺序检查

全局删除顺序固定后，它在 query block 上诱导一个固定 local subsequence。在两份
collision assignments 中被删 key identities 完全相同，故 delete labels 序列的
inner bits也相同：monotone words只在保留区间 \(T_L\) 上不同，在 complement 上
相同。因此从共同 pre-delete state 出发确实执行相同 transition maps。删除其他
blocks 的 keys 不触碰 query block local state。

## 5. Poisson lifting

令

\[
\frac nB\to\lambda.
\]

则 \(C\Rightarrow\operatorname{Pois}(\lambda)\)，而
\(S\Rightarrow\operatorname{Pois}(\alpha\lambda)\)。Theorem 4.1 立即给：

### Corollary 5.1（Poisson deficit）

存在一列 deterministic fixed histories，使其固定 nonmember rejection 满足

\[
\boxed{
\limsup_{n\to\infty}\operatorname{Rej}
\le
e^{-\alpha\lambda/2}
-e^{-\lambda}\frac{\lambda^c}{c!}\,2^{-c}
\min_{1\le t\le c}
\alpha^t(1-\alpha)^{c-t}.
}
\tag{14}

特别地：

- 若 \(d_2\le2\)，deficit term 至少为
  \[
  e^{-\lambda}\frac{\lambda^2}{8}
  \min\{\alpha(1-\alpha),\alpha^2\};
  \tag{15}
  \]
- 若 \(d_3\le3\)，deficit term 至少为
  \[
  e^{-\lambda}\frac{\lambda^3}{48}
  \min\{\alpha(1-\alpha)^2,alpha^2(1-\alpha),\alpha^3\}.
  \tag{16}
  \]

取 \(\alpha=1/2\) 得到简单显式形式

\[
d_2\le2:qquad
\limsup\operatorname{Rej}
\le e^{-\lambda/4}-e^{-\lambda}\frac{\lambda^2}{32},
\tag{17}
\]

\[
d_3\le3:qquad
\limsup\operatorname{Rej}
\le e^{-\lambda/4}-e^{-\lambda}\frac{\lambda^3}{384}.
\tag{18}

这些是对 pointwise fixed-history guarantee 的真实约束，不是 tape-adaptive local
history。

## 6. 结论的意义与局限

Theorem 4.1 关闭了前一个 finite fiber-cover lemma 的主要量词缺口：local collision
witness 可以通过预先独立的 survivor mask 以正概率自动被选中；对 mask averaging
后固定一个 deterministic history。因此，在 label-oblivious block transducer 类中，
load-2 从 3 states 压到 2、或 load-3 从 4 states 压到 3，都会在全局 pointwise
FPR 中产生显式 Poisson deficit。

但式 (14) 本身还不是 \(2.349083n\) 的完整 state-rate converse。原因有二：

1. 它一次只利用一个 deficient load layer；要得到 sharp rate，需要把所有
   \((d_c)\) 与所有 induced deficits 联合成一个 OGF/FPR 变分不等式。
2. 它不覆盖 arbitrary public-tape algorithms。若 transition/query 可读取 key
   identity 或其他免费 hash bits，不同 inner assignments 是不同 tapes，same stored
   state 不再给 indistinguishability。需要新的 same-tape communication 或
   public-randomness conditioning lemma。

所以当前可严格宣称的是：

> 在 label-oblivious、history-dependent binary block filters 中，任何
> \(d_2\le2\) 或 \(d_3\le3\) 的 local state saving 都可由一条 oblivious fixed
> global history检测到，并导致式 (15)--(18) 的显式 rejection deficit。

这已经把“nontransitive overlaps 必须付出更多 YES”从局部 adaptive witness 提升
到了 ordinary pointwise history量词，但仍不能外推为所有 dynamic AMQs 的 global
lower bound。
