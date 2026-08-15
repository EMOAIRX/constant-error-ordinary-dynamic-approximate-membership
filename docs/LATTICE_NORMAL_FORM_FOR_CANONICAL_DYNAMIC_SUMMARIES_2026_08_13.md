# Canonical key-only dynamic summaries 的 lattice normal form

> 日期：2026-08-13。状态：结构定理已证明；它把任意确定性 canonical
> multiset summary 归约为 Abelian lattice quotient。本文不声称覆盖一般
> history-dependent 或 randomized dynamic filters，也不声称已经证明所有
> (K)-ary quotients 中的最优空间率。

## 1. 为什么这个定理重要

Algebraic threshold quotient 最初看起来只是一个有限群构造。下面的定理说明，
在一个自然但受限的模型中，有限群并不是设计选择，而是更新语义强迫出的 normal
form：只要一个 block 的物理状态由当前 symbol multiset 唯一决定，并且能从状态
执行确定的 key-only insert/delete，那么任何非线性编码、多个并行 accumulator，
甚至表面上非交换的状态机，最后都等价于一个 Abelian lattice quotient。

因此，真正还未解决的部分不是寻找另一种 canonical 状态机语法，而是在所有
lattice quotients 上证明 sharp 的

\[
\text{sumset growth}\quad\text{vs.}\quad\text{one-sided rejection}
\]

不等式。

## 2. 精确模型

固定内层 alphabet ([K]=\{1,\ldots,K\})。一个 block multiset 写成 count vector

\[
x=(x_1,\ldots,x_K)\in\mathbb N^K,
\qquad |x|=\sum_i x_i.
\]

一个 **canonical deterministic summary** 是 map

\[
\phi:\mathbb N^K\to\mathcal M,
\]

以及确定 maps (I_i:\mathcal M\to\mathcal M) 和在合法状态上定义的
(D_i:\mathcal M\to\mathcal M)，满足

\[
I_i(\phi(x))=\phi(x+e_i),
\]

和当 (x_i>0) 时

\[
D_i(\phi(x))=\phi(x-e_i).
\]

允许 state 同时编码 load；也允许不同 loads 被合并，只要上述 labeled updates
仍良定义。定义 (x\sim y\) 当且仅当 \(\phi(x)=\phi(y)\)。

这些量词很重要：同一个 (I_i,D_i) 必须同时适用于该物理状态所代表的全部
隐藏 multisets；delete 只在被删 symbol 在真实 multiset 中出现时要求正确。

## 3. Cancellation lemma

### Lemma 3.1

对任意 (x,y,a\in\mathbb N^K)，

\[
x+a\sim y+a
\quad\Longleftrightarrow\quad
x\sim y.
\tag{1}
\]

**证明。** 正向由依次对双方执行同一组 insert labels 得到。反向从
(x+a\sim y+a) 开始，按任意顺序共同删除 (a_i) 次 symbol (i)。每一步在
两个隐藏 multiset 中都合法；delete determinism 保持状态相等。删完得到
(x\sim y)。\(\square\)

这里不能只引用“delete 是 insert 的逆”：transition map 在整个物理状态空间上
未必双射。式 (1) 使用的是两边共同 suffix 的逐步合法删除。

## 4. Lattice normal form

定义差分集合

\[
L=\{x-y:x,y\in\mathbb N^K,\ x\sim y\}\subseteq\mathbb Z^K.
\tag{2}
\]

### Theorem 4.1

(L) 是 (mathbb Z^K) 的子群，并且

\[
\boxed{x\sim y\quad\Longleftrightarrow\quad x-y\in L.}
\tag{3}

所以存在 Abelian group

\[
G=\mathbb Z^K/L
\]

使 canonical summary 恰等价于正锥在该群中的 additive syndrome

\[
\phi(x)=[x]_L=\sum_i x_i[e_i]_L,
\tag{4}

\]

更精确地，\(\phi(\mathbb N^K)\) 与 reachable subset
\(\{[x]_L:x\in\mathbb N^K\}\subseteq G\) 双射。一般不能声称正锥命中
\(G\) 的每一个 coset；后续只枚举 reachable states。

**证明。** (0\in L)，且等价关系的对称性给 (L=-L)。若
(a=x-y\in L) 和 (b=u-v\in L)，则 (x\sim y) 与 (u\sim v)。共同加
(u) 和共同加 (y) 分别给

\[
x+u\sim y+u\sim y+v,
\]

故 (a+b=(x+u)-(y+v)\in L)。所以 (L) 是子群。

式 (3) 的正向是定义。反向设 (x-y=u-v\) 且 (u\sim v)。于是
(u+y=v+x)。对 (u\sim v) 共同加 (y)，得到

\[
u+y\sim v+y,
\]

即 (v+x\sim v+y)。由 Lemma 3.1 cancellation 掉共同的 (v)，得到
(x\sim y)。\(\square\)

### Corollary 4.2（显式 load 的版本）

若不同 loads 永不合并，则

\[
L\subseteq A_{K-1}:=\{z\in\mathbb Z^K:\sum_i z_i=0\}.
\]

反之，任意 \(L\le A_{K-1}\) 都定义一个保持 load 的 canonical summary。
每个固定 load layer 无论如何都只有有限个 multisets；真正有内容的等价条件是
各 load layers 的 reachable-state 数一致有界。当且仅当

\[
[A_{K-1}:L]<\infty.
\tag{5}

\]

时，这个一致有界性成立。必要性可由 \(e_i-e_K\) 生成 \(A_{K-1}\) 看出：若
商无限，逐层 sumsets 的并集生成一个无限、有限生成的 Abelian group，故其
cardinality 不可能一致有界。此时去掉一个基准 increment 后，固定层 syndrome
位于有限 Abelian group \(A_{K-1}/L\)。注意 \(L\le\mathbb Z^K\) 的 index 仍是无限的，因为 load 本身
无界；正确的有限性条件是式 (5)，不是 ([\mathbb Z^K:L]<\infty)。

### Corollary 4.3（允许跨 load merge）

若不同 loads 可以合并且全局只有有限个 canonical states，则恰有

\[
[\mathbb Z^K:L]<\infty.
\]

此时整个 summary 的 reachable subset 是有限 Abelian group
\(\mathbb Z^K/L\) 中由 increments 生成的有限 submonoid；在有限群中它其实是
increments 所生成的 subgroup 的一个 coset-semigroup，删去不可达 elements 即可。若物理状态还
显式保存一个 unbounded exact load，则应使用 Corollary 4.2。

## 5. Minimal one-sided query 与 sumsets

取 increments

\[
v_i=[e_i]\in G,
\qquad V=\{v_1,\ldots,v_K\}.
\]

load (c) 的 reachable syndrome set是

\[
cV=\{v_{i_1}+\cdots+v_{i_c}:i_j\in[K]\}.
\tag{6}

给定 state ((c,s))，zero false negatives 强迫 query symbol (i) 在存在一个
相容 multiset 含 (i) 时回答 YES。等价地，最小安全规则是

\[
\boxed{Q(c,s,i)=\mathrm{YES}
\quad\Longleftrightarrow\quad
s-v_i\in(c-1)V.}
\tag{7}

\]

证明只是剥掉一个 (i)：右侧恰表示 (s) 有一个由 (c) 个 increments
组成且其中一个为 (v_i) 的表示。任何额外的 YES 都增加误报而不减少 reachable
state 数，故在固定 quotient 内研究最优 FPR 时可无损采用式 (7)。

若内 hash 的 symbol law 是 (p=(p_i))，令 (S_c=X_1+\cdots+X_c)，其中
(\Pr[X=v_i]=p_i)。条件于 outer-block load 为 (c)，fresh query 的拒绝概率
恰为

\[
\rho_c
=\sum_i p_i\Pr[S_c-v_i\notin(c-1)V].
\tag{8}

\]

若 outer load 极限为 (operatorname{Pois}(\lambda))，总拒绝概率为

\[
e^{-\lambda}\sum_{c\ge0}\frac{\lambda^c}{c!}\rho_c.
\tag{9}

\]

而 local state OGF 为

\[
A(z)=\sum_{c\ge0}|cV|z^c.
\tag{10}

\]

式 (8)--(10) 是 canonical deterministic class 的完整优化接口。

## 6. 已覆盖与未覆盖的设计

Theorem 4.1 覆盖：

- 任意 canonical nonlinear encoding；
- 任意有限个 Abelian accumulators，因为其联合状态只是直积群 syndrome；
- 任意以非交换 transition 代码实现、但最终 canonical multiset equivalence
  仍满足相同 labeled insert/delete 语义的 automaton；定理说明其可观察 quotient
  必为 Abelian；
- binary threshold quotients，它们对应 (A_1=d\mathbb Z\)。

它不覆盖：

- **history-dependent / multiple representations**：同一个 multiset 可随路径落在
  不同物理状态时，(phi(x)) 不是函数，因而不能在 (mathbb N^K) 上定义上述
  equivalence relation；
- **randomized transitions**：state successor 是分布而非确定点，kernel equality
  不给 Lemma 3.1 的点态 cancellation；
- **仅对部分 canonical representatives 保证更新**：若共同删除不能从两个相等
  states 同时合法执行，证明失效；
- **跨 blocks 联合编码且更新会同时改变全局 auxiliary state**：除非全局状态仍是
  全部 block count vectors 的 canonical 函数，否则单 block lattice 不适用；
- **query-dependent stored sketches** 或能够访问外部 exact set 的更新器。

因此，本文给的是一个有内容的 restricted-class normal form，不是 ordinary dynamic
AMQ 的 WLOG reduction。

## 7. 二元情形为何立即闭合

当 (K=2) 且显式保存 load 时，

\[
A_1=\{(t,-t):t\in\mathbb Z\}\cong\mathbb Z.
\]

它的每个有限指数子群都是 (q\mathbb Z)。因此所有 canonical deterministic
binary summaries 都由 one-count modulo (q) 给出；这直接恢复 threshold
quotient 分类：

\[
|cV|=\min(c+1,q),
\]

且 (c<q) 时精确、(c\ge q) 时两个 symbols 都必须接受。

这比“有限 Abelian group 加两个 increments”的原表述更强：它不预设 summary
以群运算实现，而是从 canonical key-only update semantics 推出群结构。

## 8. (K>2) 的第一个解析边界及其局限

若 (G=\mathbb Z_p) 为素数阶且 (V\subseteq G)、
(|V|=K\ge2)，Cauchy--Davenport 给

\[
|cV|\ge\min\{p,c(K-1)+1\}.
\tag{11}

\]

等号长期成立的集合由 Vosper 型逆定理强迫为 arithmetic progression（需排除
标准边界情形）。这严格说明 (K>2) 想压低 local state count 时，最佳候选只能
接近 arithmetic progression；任意 Sidon-like (V) 的 sumset 增长只会更快。

但是式 (11) **不能单独推出** (\varepsilon=1/2) 的 rate 下界。原因是 FPR 由
式 (8) 的表示结构决定，而不只由 cardinalities (|cV|) 决定。把
(\rho_c) 粗暴上界为 fresh symbol 在真实 (c) 个 symbols 中缺席的概率
((1-1/K)^c)，再与式 (11) 联合，会给出低于 (2.34908) 的虚假“下界”数值，
因而不足以排除 (K>2)。缺失的 sharp lemma 必须联合控制：

\[
\bigl(|cV|\bigr)_{c\ge0}
\quad\text{和}\quad
\bigl(\rho_c\bigr)_{c\ge0},
\]

而不能分别极值化两者。

一个准确的下一目标是证明在 uniform symbols、有限 Abelian (G) 下，若式 (9)
至少为 (1/2)，则由式 (10) 产生的 saddle rate 满足

\[
R(A,\lambda)\ge2.349083440193\ldots,
\tag{12}

\]

且等号只由 (G=\mathbb Z_3,V=\{0,1\})（忽略平移与群同构）实现。式 (12)
目前是经小群枚举支持的猜想，不是本文定理。

## 9. 当前可辩护的论文结论

已经严格得到的增强是：

> binary (q=3) 的最优性不只覆盖“预设为 finite-Abelian accumulator”的构造，
> 而覆盖所有**显式保持 exact load** 的 deterministic canonical、key-only、
> 任意长 multiset summaries。

更一般地，Theorem 4.1 给出全部 (K) 的 lattice normal form，把后续 converse
精确归约成一个 additive-combinatorics optimization。要把它升级成完整 SODA
主定理，仍需证明式 (12) 或找到反例；有限枚举本身不能承担该结论。

## 10. Biased binary hashes 不改善 \(\varepsilon=1/2\)

Lattice normal form 还允许把原来的 uniform-bit converse 严格推广到任意固定
bias。令 query/member symbol 独立服从

\[
\Pr[1]=p,\qquad \Pr[0]=1-p,
\]

并令 quotient order 为 \(q\ge2\)。local state OGF 仍为

\[
A_q(z)=\frac{1-z^q}{(1-z)^2},
\tag{13}
\]

与 \(p\) 无关。条件于 block 中有 \(c<q\) 个 members，syndrome 精确恢复
one-count；fresh query 被拒绝当且仅当它的 symbol 在这些 members 中缺席。因此

\[
\rho_c(p)=p(1-p)^c+(1-p)p^c.
\tag{14}
\]

当 \(c\ge q\) 时两个 symbols 都必须接受，故精确 Poisson rejection 是

\[
J_{q,p}(\lambda)
=e^{-\lambda}\sum_{c=0}^{q-1}
\frac{\lambda^c}{c!}
\left[p(1-p)^c+(1-p)p^c\right].
\tag{15}
\]

注意 \(c=0\) 的括号等于 1。

### Lemma 10.1（untruncated absence bound）

对 \(0<\lambda\le2\) 和 \(0\le p\le1\)，

\[
p e^{-\lambda p}+(1-p)e^{-\lambda(1-p)}
\le e^{-\lambda/2},
\tag{16}
\]

等号在 \(0<\lambda<2\) 时只可能为 \(p=1/2\)。

**证明。** 令左侧为 \(F_\lambda(p)\)。直接求导两次：

\[
F_\lambda''(p)
=\lambda e^{-\lambda p}(\lambda p-2)
+\lambda e^{-\lambda(1-p)}(\lambda(1-p)-2)\le0.
\]

所以 \(F_\lambda\) 在 \([0,1]\) 上凹；它关于 \(p=1/2\) 对称，故最大值在
\(1/2\)，代入即得式 (16)。当 \(\lambda<2\) 时内部严格凹，给出唯一性。
\(\square\)

式 (16) 正是没有 threshold truncation 时的拒绝概率，因为

\[
e^{-\lambda}\sum_{c\ge0}\frac{\lambda^c}{c!}\rho_c(p)
=p e^{-\lambda p}+(1-p)e^{-\lambda(1-p)}.
\tag{17}
\]

### Theorem 10.2（sharp biased-binary optimum at one-half error）

在所有**显式保持 exact load** 的 deterministic canonical binary key-only
summaries、任意 bias \(p\in[0,1]\)、minimal one-sided query rule，以及
blockwise fixed-state enumerative coding 中，\(\varepsilon=1/2\) 的唯一最优
非退化 quotient 是

\[
q=3,\qquad p=\frac12,
\]

其 rate 为

\[
\boxed{2.349083440193141\ldots\ \text{bits/key}.}
\tag{18}
\]

**证明。** 对 \(q=2\)，式 (15) 只含
\(\rho_0=1\) 与 \(\rho_1=2p(1-p)\)；对 \(q=3\)，还包含
\(\rho_2=p(1-p)\)。这些量都由 \(p=1/2\) 唯一最大化。因此达到 rejection
\(1/2\) 时可采用的最大 \(\lambda\) 分别在 uniform bias 取得。由于固定
\(q\) 的 enumerative rate \(\mathcal R_q(\lambda)\) 随 \(\lambda\) 严格下降，
biased choices 不会改善 \(q=2,3\)；直接比较给 \(q=3\) 更优。

对任意 finite \(q\ge4\)，式 (15) 严格小于式 (17)。在
\(\lambda_\infty=2\ln2<2\) 处，Lemma 10.1 给

\[
J_{q,p}(2\ln2)<\frac12.
\]

序列 \(\rho_c(p)\) 随 \(c\) 非增，且 truncation 后最终为零，所以
\(J_{q,p}(\lambda)\) 随 \(\lambda\) 严格下降。故其 \(1/2\)-root 满足

\[
\lambda_{q,p}<2\ln2.
\]

沿用 \(\mathcal R_q\) 对 \(\lambda\) 严格下降、对整数 \(q\) 严格增加的
两个单调性，得到

\[
\mathcal R_q(\lambda_{q,p})
>\mathcal R_q(2\ln2)
\ge\mathcal R_4(2\ln2)
=2.351275266054\ldots
>2.349083440193\ldots.
\]

退化端点 \(p\in\{0,1\}\) 只留下 outer occupancy filter，也不取等号。
因此式 (18) 在整个 load-preserving biased binary canonical class 中唯一最优。
\(\square\)

### Remark 10.3（不能静默删除的模型边界）

Theorem 10.2 不能扩写成所有 canonical binary summaries。若允许不同 loads
共享物理状态，Theorem 4.1 给出的是满秩 lattice
\(L\le\mathbb Z^2\)，而非 \(L=qA_1\)；其 quotient 可同时混合 load residue
与 one-count residue，reachable-state/FPR tradeoff 不再由单个整数 \(q\)
刻画。目前没有证明 cross-load merging 不能改善 rate。因此一般跨 load 的
canonical class 仍是 open case。

### Remark 10.4

该结论只针对 \(\varepsilon=1/2\)。当 \(\varepsilon\to1\) 时，偏置会显著
改变最优解，不能由本定理推断 full error curve 仍为 uniform。事实上初步数值
显示 optimal \(q\) 增大且 \(p\) 趋向 0；完整相变与端点渐近需要另行证明。
