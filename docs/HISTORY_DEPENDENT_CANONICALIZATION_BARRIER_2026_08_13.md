# History-dependent key-only summaries 的 canonicalization barrier

> 日期：2026-08-13。结论：合法 insert/delete 的双向边确实强迫一个
> cancellative **co-representation relation**，但不强迫它传递。包含它的最小
> cancellative additive congruence 给出 Abelian lattice envelope，却会合并从未
> 共享过物理状态的 logical multisets，
> 因而不能保持 query 或给出所需的空间下界。即使额外要求 updates 严格可逆，
> 最一般的 normal form 也是带任意 holonomy 的 permutation cover，而不是
> Abelian quotient。

这说明现有 \(2.349083440193\ldots\) converse 不能仅凭 key-only deletion 从
canonical class 推广到所有 history-dependent filters。

## 1. Relational state model

令 alphabet 为 \([K]\)，容量为 \(n\)，logical multiset space 为

\[
X_n=\{x\in\mathbb N^K:|x|\le n\}.
\]

物理状态集合为有限集 \(Q\)。从固定初态出发执行任意合法 update history；同一
logical multiset 可由不同 histories 到达不同 states，同一 state 也可能由不同
logical multisets 到达。记

\[
R_x=\{s\in Q:(x,s)\text{ reachable}\}.
\tag{1}
\]

对 symbol \(i\) 有 deterministic transition \(I_i\) 与 \(D_i\)。它们只需满足：

\[
I_i(R_x)\subseteq R_{x+e_i}\quad(|x|<n),
\tag{2}
\]

\[
D_i(R_x)\subseteq R_{x-e_i}\quad(x_i>0).
\tag{3}
\]

式 (3) 只在 logical deletion 合法时要求正确。尤其不要求

\[
D_iI_i(s)=s;
\]

左侧只需落回同一个 logical fiber \(R_x\)。这正是 multiple representations
相对 canonical map \(\phi(x)\) 多出的自由度。

定义 co-representation relation

\[
x\mathrel C y
\quad\Longleftrightarrow\quad
R_x\cap R_y\ne\varnothing.
\tag{4}

\]

它表示两个 logical multisets 真正可能对应同一物理状态。

## 2. 能够保留的 cancellation

### Theorem 2.1（local translation and cancellation）

关系 \(C\) reflexive、symmetric，并且对任意 \(x,y,a\in\mathbb N^K\)，只要涉及
的 loads 不超过容量，

\[
xCy\Longrightarrow x+a\;C\;y+a,
\tag{5}
\]

以及

\[
x+a\;C\;y+a\Longrightarrow xCy.
\tag{6}

**证明。** 若 \(s\in R_x\cap R_y\)，从同一物理状态 \(s\) 按同一顺序插入
composition \(a\)。transition deterministic，所以两条 logical executions 到达
同一物理状态；式 (2) 给出式 (5)。

反之，若 \(t\in R_{x+a}\cap R_{y+a}\)，按同一顺序删除 \(a\) 中的 symbols。
每一步对两个 logical multisets 都合法，且 deterministic transitions 从共同状态
产生共同后继。式 (3) 最终给出 \(R_x\cap R_y\ne\varnothing\)。\(\square\)

这个定理说明 canonical cancellation lemma 并未完全消失；真正缺失的是
transitivity。

### Corollary 2.2（lattice envelope）

在无容量截断的 \(\mathbb N^K\) 模型中，令

\[
L=\langle x-y:xCy\rangle\le\mathbb Z^K.
\]

定义 \(x\equiv_Ly\) 当且仅当 \(x-y\in L\)。则 \(\equiv_L\) 是包含
\(C\) 的最小 cancellative additive congruence：

\[
x\equiv_L y\quad\Longleftrightarrow\quad x-y\in L.
\tag{7}

固定容量时只能谈相应的 truncated local relations；不能越过 boundary 静默使用
translations 或 group completion。

**证明。** 由定义，\(\equiv_L\) 是 cancellative additive congruence 且包含
\(C\)。反之，任意包含 \(C\) 的 cancellative additive congruence 经
Grothendieck group completion 后，其 zero class 是 \(\mathbb Z^K\) 的 subgroup，
并包含每个 generator \(x-y\)，故包含 \(L\)，因而也包含
\(\equiv_L\)。\(\square\)

这里不能把“最小 cancellative additive congruence”简写成 \(C\) 的普通传递
闭包。虽然每条 \(C\)-edge 可在共同 suffix 存在时 cancellation，一条 chain 的
中间 vertices 未必都含有该 suffix；普通传递闭包未必 cancellative。

式 (7) 是能无条件得到的最强 Abelian 对象。但它只是 **envelope**，不是实际
state equivalence。

## 3. 一个四状态严格反例

取 binary alphabet \(\{0,1\}\) 和容量 \(n=2\)。物理状态为

\[
Q=\{e,r,u,v\}.
\]

定义 insert transitions：

\[
I_0(e)=I_1(e)=r,
\qquad I_0(r)=u,
\qquad I_1(r)=v.
\tag{8}

load 2 时 insert 非法，无需定义。定义所有合法 delete transitions：

\[
D_0(r)=D_1(r)=e,
\tag{9}
\]

\[
D_0(u)=D_1(u)=D_0(v)=D_1(v)=r.
\tag{10}

对某个 state-symbol pair，若在部分 hidden logical multisets 上 deletion 非法，
其输出无关紧要；式 (9)--(10) 在所有合法 executions 上均正确。

从初态 \(e\) 出发，reachable fibers 恰包含

\[
R_{(0,0)}=\{e\},
\]

\[
R_{(1,0)}=R_{(0,1)}=\{r\},
\]

以及

\[
u\in R_{(2,0)}\cap R_{(1,1)},
\qquad
v\in R_{(1,1)}\cap R_{(0,2)}.
\tag{11}

但是

\[
R_{(2,0)}\cap R_{(0,2)}=\varnothing.
\tag{12}

因此

\[
(2,0)C(1,1),
\qquad
(1,1)C(0,2),
\qquad
(2,0)\not C(0,2).
\tag{13}

关系 \(C\) 明确不传递。该例仍显式保持 load：四个 states 分属 loads
\(0,1,2\)，没有 cross-load merge。

令 \(e\) 对两个 symbols 回答 `NO`，其他三个 states 对两个 symbols回答
`YES`，即可得到合法 one-sided approximate membership summary。它不是好的
filter，但已足以否决如下结构推断：

> deterministic + key-only insert/delete + exact load
> \(\Longrightarrow\) physical ambiguity 是 lattice quotient。

错误发生在把“存在共同 state”误当成 equivalence relation。无论普通传递闭包
还是 cancellative lattice envelope，都会由式 (13) 合并 \((2,0)\) 与
\((0,2)\)，但没有任何物理状态真正同时表示二者。

## 4. 严格可逆也只给 permutation cover

也许式 (13) 只是因为 \(D_iI_i\ne\mathrm{id}\)。下面说明，即使强行加入严格
可逆性，物理状态仍不必是 Abelian quotient。

取任意非 Abelian finite group \(G\)，例如 \(S_3\)，并选择不交换元素
\(\sigma_0,\sigma_1\in G\)。令

\[
Q=\{(x,g):x\in X_n, g\in G\}.
\tag{14}

定义

\[
I_i(x,g)=(x+e_i,g\sigma_i),
\qquad
D_i(x,g)=(x-e_i,g\sigma_i^{-1}).
\tag{15}

于是每条合法边上

\[
D_iI_i=\mathrm{id},
\qquad I_iD_i=\mathrm{id}.
\tag{16}

但 commutator loop 的 fiber action 是

\[
g\longmapsto
g\sigma_0\sigma_1\sigma_0^{-1}\sigma_1^{-1},
\tag{17}

可以非平凡。因此 insertion order 在 fiber 中留下 non-Abelian holonomy。

更一般地，若每个 logical fiber \(R_x\) 彼此不交、相邻 fibers 等大，且每条
insert edge 是以对应 delete 为逆的 bijection，那么准确 normal form 是：

> logical multiset grid 上的 permutation cover，外加由 zero-net loops 生成的
> holonomy transformation group。

该 holonomy group 可以是任意有限 permutation group，并无理由 Abelian。
只有再加入 square commutation

\[
I_iI_j=I_jI_i
\tag{18}

以及 trivial zero-net holonomy，才存在与 updates 相容的全局 canonical section；
此时才退回单值 \(\phi(x)\) 和 lattice normal form。

严格可逆 cover 的额外 fiber states通常只是 history overhead；丢掉它们可能减少
空间。但在 approximate summary 中 fibers 可以重叠，如第 3 节，不能假设存在
一个保持 transitions 与 query 的无损 quotient。

## 5. 为什么 lattice envelope 不能证明 FPR converse

对物理状态 \(s\)，zero false negatives 只强迫接受所有

\[
\bigcup_{x:s\in R_x}\operatorname{supp}(x)
\tag{19}

中的 symbols。它不强迫接受整个 \(\equiv_L\)-class 的 supports，因为生成
lattice envelope 的不同 \(C\)-edges 可以由不同物理 states witness。

因此，把 \(C\) 替换成 lattice envelope \(\equiv_L\) 会产生两个不可接受的变化：

1. 它可能增加 forced-YES query symbols，从而提高 FPR；
2. 它可能把多个不同物理 states 压成一个 class，从而降低形式 state count。

这两个方向恰好都会制造一个看似更容易证明、却与原 filter 不等价的 canonical
对象。由该对象得到的 sumset/rejection tradeoff 不是原 history-dependent filter
的 lower bound。

同样，任意为每个 \(x\) 选择一个 representative \(s_x\in R_x\) 也不够：通常

\[
I_i(s_x)\ne s_{x+e_i},
\]

而重新定义 transition 会改变数据结构；若不同 logical multisets 选到同一 state，
还会产生互相冲突的 successor requirements。不存在无条件的 canonical section
selection lemma。

## 6. 对 \(2.349083\) converse 的准确影响

现有 binary lattice theorem 的前提是单值 map

\[
\phi:\mathbb N^2\to\mathcal M.
\]

它的 kernel 是真正 equivalence relation，cancellation 后必为
\(q\mathbb Z\subseteq A_1\)，从而推出 threshold quotient 分类和
\(2.349083440193\ldots\) restricted optimum。

history-dependent filter 只有 relation \((R_x)_x\)。Theorem 2.1 没有把它提升
为 kernel；第 3 节严格证明该提升一般为假。因此当前不能声称：

\[
H\ge2.349083440193\ldots n-o(n)
\]

对全部 history-dependent key-only dynamic AMQs 成立。

这个反例也没有构造一个低于 \(2.349083\) 的好 filter；它否决的是证明桥梁，
不是数值结论本身。要真正推广 converse，必须使用比 lattice kernel 更强的工具，
直接约束 relational fibers，例如：

- co-representation hypergraph 的 state-cover entropy；
- labeled transition graph 上的 fractional cover / communication bound；
- 对每个 state 的 compatible-support union 作联合 FPR 与 transition counting；
- 证明 near-optimal filters 的 overlap relation 在某种稳定意义下近似传递。

最后一种“approximate canonicalization”仍可能成立，而且最接近现有结构定理：
不是证明所有 filters 都 canonical，而是证明任何显著低于
\(2.349083\) 的 filter 若存在，就必须包含大量 nontransitive overlap witnesses；
再用这些 witnesses 的 forced-YES 或 transition branching 证明额外代价。目前这
是一个明确的下一 lemma，而不是已经完成的 theorem。

## 7. 结论

双向 key-only updates 强迫的是

\[
\text{cancellative overlap relation}
\quad\longrightarrow\quad
\text{lattice envelope},
\]

而不是

\[
\text{physical states}=\text{Abelian quotient classes}.
\]

multiple representations 的本质自由度正是 nontransitive overlaps；严格可逆时则
表现为 permutation-cover holonomy。除非额外证明 transitivity、commuting square
或 trivial holonomy，canonical lattice converse 不能覆盖 history-dependent
filters。
