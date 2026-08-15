# Algebraic threshold quotients：ordinary dynamic AMQ 的新 fixed-state 上界机制

> 日期：2026-08-13。状态：信息论构造与一阶计数已给出。有限 (n) 的
> pointwise 校准和高效 word-RAM 实现尚未写；本结果是 fixed-memory、无限计算
> 模型中的候选定理。所有持久状态都计入空间，公共 fully random hashes 免费。

## 1. 结论

随机 snapshot partition 一般不能直接扩展成 update language 的 right
congruence。但是存在一个简单的跨所有 occupancy layers 的代数 quotient：

- 外层 hash 把 keys 分到 (B) 个 blocks；
- 内层 hash 为每个 key 给一个 bit；
- 每个 block 保存总负载 (c) 与 one-count (a) 模 (L+1)；
- 当 (cle L) 时，(amod(L+1)) 就是精确的 one-count；
- 当 (c>L) 时，该 block 对所有 queries 回答 `YES`。

更新只做

\[
c\leftarrow c\pm1,
\qquad
a\leftarrow a\pm h_{m in}(x)\pmod{L+1}.
\]

因此它支持 ordinary key-only deletion、任意长合法 history、零 false negative，
没有 ghost accumulation，也不需要外部 exact set 或 live-key enumeration。从
任意 high layer 降回 (cle L) 后，模摘要会自动恢复精确 multiset。

在 (arepsilon=1/2) 时，该 family 的最优 threshold 是 (L=2)。其一阶
fixed-state rate 为

\[
\boxed{R_2=2.3490834402\ldots\ {m bits/key},}
\]

严格优于 uniform exact-count fingerprint 的

\[
2.3844998425\ldots\ {m bits/key}.
\]

这尚未击败 smooth/current-state 的 (2.2006114830ldots)，但它是一个真正
利用 ordinary lossy semantics、且适用于无限历史的 fixed-state upper
mechanism。

## 2. 数据结构

公共随机带给出独立 maps

\[
g:U\to[B],
\qquad
h:U\to\{0,1\}.
\]

对当前集合 (S)，block (j) 的逻辑统计量是

\[
c_j=|\{x\in S:g(x)=j\}|,
\qquad
a_j=\sum_{x\in S:g(x)=j}h(x)\pmod{L+1}.
\tag{1}
\]

持久 memory 是整个数组

\[
((c_1,a_1),\ldots,(c_B,a_B)),
\qquad \sum_j c_j\le n,
\tag{2}
\]

在其全部可达状态集合中的 rank。这里不是 entropy/typical-set code；rank space
覆盖每个 composition (c_1+cdots+c_Ble n)，故不会 overflow。

`Insert(x)` 与 `Delete(x)` 分别对 (j=g(x)) 执行式 (1) 的加法与减法。
合法 deletion 保证被减 key 实际存在；算法不需要知道它在 block 内的 route。

查询 (x)，令 (j=g(x))：

1. 若 (c_j=0)，返回 `NO`；
2. 若 (1le c_jle L)，把 (a_jin\{0,\ldots,L\}) 解释为精确 one-count，
   当且仅当相应 bit 的 multiplicity 非零时返回 `YES`；
3. 若 (c_j>L)，返回 `YES`。

### Lemma 2.1（right congruence 与 zero FN）

式 (1) 在所有 insert/delete labels 下是群 accumulator，故 (2) 在每一层之间
有确定的 labeled successor/predecessor。若 (c_jle L)，真实 one-count 位于
([0,c_j]subseteq[0,L])，所以模 (L+1) 没有 wrap-around 并精确恢复二元
multiset。若 (c_j>L)，整块接受。因此任何成员永远返回 `YES`。

这个证明与 history 长度无关。特别地，高负载时虽然摘要有碰撞，随后删除的
逆群更新会保证一旦负载降回 threshold，剩余 low-load multiset 被精确恢复。

## 3. Pointwise FPR

固定任意合法 history 与当前固定 nonmember (x)。公共 outer hash 下，包含
(x) 的 block 中其他 (n) 个 keys 的负载渐近为

\[
C\sim\operatorname{Pois}(\lambda),
\qquad \lambda=n/B.
\]

条件于 (C=tle L)，内 bit 与 (h(x)) 碰撞的概率是

\[
1-2^{-t}.
\]

条件于 (C>L)，query 必为 false positive。因此极限 FPR 是

\[
\varepsilon_L(\lambda)
=1-e^{-\lambda}\sum_{t=0}^L\frac{(\lambda/2)^t}{t!}.
\tag{3}

对每个固定 (x,S)，fully random hashes 的 exchangeability 给出同一表达式，
所以这是 pointwise-over-randomness，而非平均 query guarantee。正式 finite-
(n) theorem 可取 (lambda) 比式 (3) 的目标根小 (o(1))，吸收 Binomial--
Poisson 和 rounding error，只改变 (o(n)) bits。

## 4. 固定空间枚举率

一个 block 在负载 (t) 上的 local state 数为

\[
d_t=
\begin{cases}
t+1,&0\le t\le L,\\
L+1,&t>L.
\end{cases}
\tag{4}

所以 local ordinary generating function 是

\[
A_L(z)
=\sum_{t=0}^L(t+1)z^t+(L+1)\frac{z^{L+1}}{1-z}.
\tag{5}

全部 (B)-block states、总负载至多 (n) 的数量是

\[
[z^{\le n}]A_L(z)^B.
\]

令 (B/n\to1/\lambda)。标准 positive-coefficient saddle point 给一阶率

\[
R_L(\lambda)
=\frac1\lambda\log_2 A_L(z)-\log_2z,
\tag{6}

其中 (z\in(0,1)) 是唯一满足

\[
\frac{zA_L'(z)}{A_L(z)}=\lambda
\tag{7}

的根。用 enumerative rank/unrank 需要

\[
nR_L(\lambda)+o(n)
\]

fixed bits。这里所有 block counts和 residues 都已经包含在 rank 中，不能再另加
一个 count array。

## 5. ε=1/2 的常数

令 (lambda_L) 是

\[
e^{-\lambda_L}
\sum_{t=0}^L\frac{(\lambda_L/2)^t}{t!}=\frac12
\tag{8}

的根。前几个 threshold 给出：

| (L) | (lambda_L) | (R_L(lambda_L)) |
|---:|---:|---:|
| 1 | 1.1461932206 | 2.3720575415 |
| 2 | 1.3258190753 | **2.3490834402** |
| 3 | 1.3754412465 | 2.3602958587 |
| 4 | 1.3847969144 | 2.3728359287 |
| 5 | 1.3861237487 | 2.3795350462 |

当 (L\to\infty)，式 (3) 趋于普通二元 exact fingerprints 的
(1-e^{-\lambda/2})，而 (5) 趋于 ((1-z)^{-2})，rate 回到 exact
composition 值 (2.3844998425ldots)。有限 threshold 允许重载 layers 合并，
(L=2) 在该 family 内形成非平凡最优点。

## 6. 为什么一般随机 snapshot partition不能这样扩展

若一个 snapshot color (phi_t(S)) 要在 insert/delete 下形成 deterministic
right congruence，则对每个 label (x) 必须存在 maps (T_x^pm) 使

\[
\phi_{t+1}(S\cup\{x\})=T_x^+(\phi_t(S)),
\qquad
\phi_{t-1}(S\setminus\{x\})=T_x^-(\phi_t(S)).
\tag{9}

任意随机 coloring 几乎必然违反 (9)：同色的两个 sets 在同一个共同合法 label
下会落入不同颜色。线性 sketch 之所以闭合，是因为

\[
\phi(S)=\sum_{x\in S}v_x
\]

把 update monoid 同态到有限群，insert/delete 分别加减 (v_x)。但是若 query
要求 sketch 在所有 occupancy layers 上恢复 support，零 false negative 会迫使
syndrome fibers的 union过大，通常退化到 exact multiplicity 空间。

Threshold quotient 绕过这一 obstruction：只要求 low layers 可解码；high
layers主动接受整个 block。有限群 residue让 high-to-low deletion 自动恢复，
而 query distortion由 high-layer Poisson tail精确支付。

## 7. 推广与当前障碍

可把内 alphabet 换成 (K>2)，并在 low layer保存能唯一恢复至多 (L) 个
symbols 的 additive Sidon/(B_L) syndrome。若群大小为 (G)，high layers
有 (G) 个摘要状态，空间生成函数相应变为

\[
\sum_{t=0}^L{K+t-1\choose t}z^t+G\frac{z^{L+1}}{1-z}.
\]

这里的明确 obstruction 是 additive recovery cost：能区分所有 size-(L)
multisets至少需要

\[
G\ge {K+L-1\choose L},
\]

而 query probing更多 symbols又增加 collision budget。初步枚举中 (K=2,L=2)
优于这些直接推广。要逼近或击穿 (2.200611)，需要一个不精确恢复整个 low-
load multiset、却仍能在 key-only deletions后安全回收的更 lossy group quotient。

### 7.1 不预设 threshold 的最小安全 query

更一般地，取有限交换群 Gamma 和 label embedding

\[
V=\{v_1,\ldots,v_K\}\subseteq\Gamma,
\qquad
s=\sum_{x\in S_j}v_{h(x)}.
\]

给定 block load (c) 与 syndrome (s)，zero false negative 强制 label (a)
至少在

\[
s-v_a\in(c-1)V
\tag{10}
\]

时回答 `YES`，其中 (rV) 是 (V) 的 (r)-fold sumset。这一规则恰等于
syndrome fiber 中所有 multisets 的 support union，因而是该 sketch 下最小的
安全 accepted set。删除 (a) 只需令 (s\leftarrow s-v_a)。

因此 local state 数至少为

\[
d_c=|cV|,
\]

而 fresh query rejection probability由 (c)-step random walk在 translates
(v_a+(c-1)V) 外的质量精确决定。这把 additive construction 的优化化为
sumset growth 与 random-walk nonmembership 的 tradeoff。

小 doubling 让状态少，却使 (cV) 很快饱和并失去 rejection；Sidon 型增长能
保留 rejection，却直接增加 local state 数。这是一个可由
Cauchy--Davenport/Kneser 方法研究的 restricted-class converse。

穷举 (|Gamma|\le10)、(K\le5) 的循环群 embeddings 后，最佳仍是

\[
\Gamma=\mathbb Z_3,\qquad V=\{0,1\}.
\]

其 reachable sizes 为 (1,2,3,3,...)，各 load 的 rejection probabilities
为 (1,1/2,1/4,0,...)，正是 (L=2) threshold construction。一个典型
partial-high-load方案 (Gamma=mathbb Z_9,K=3) 在 load (3,4) 仍能拒绝部分
queries，但其最优 rate 约为 (2.36657)，更差。这个有限枚举不是全局最优性
证明，但说明“只允许 high layers 部分 rejection”本身不会自动降低常数。

### 7.2 为什么永久 public mask 不给 fixed-state convexification

若公共随机带选 (Gsubseteq U)，对 (G) 永久回答 `YES`，其余 keys 交给某个
capacity-(n) inner transducer，则每条 fixed tape 上仍存在合法 history，使
全部 (n) 个 live keys 都落在 (Usetminus G)。所以 inner transducer 仍须
覆盖容量 (n) 的全部 reachable states。永久 mask 消耗 pointwise FPR，却不
按 (1-|G|/u) 比例缩短 worst-case persistent block。

这正是 current-state Shannon convexification 与 KLZ fixed-(H) 语义之间的
差别。对 (L=2) family 数值优化

\[
\varepsilon
=\alpha+(1-\alpha)\varepsilon_2(\lambda)
\]

也在 (alpha=0) 取最优；shared global mask 不改善 (2.34908344)。

### 7.3 Binary canonical quotients 的分类定理

下面严格排除最自然的 nested/variable-modulus 改进。固定 block load (c)，以
(a in {0,...,c}) 表示 one-count。设物理 state 是当前 (c,a) 的 canonical
quotient (phi_c(a))，并存在只依赖 state 和 bit label 的确定性
`Insert(0/1)`、`Delete(0/1)` transitions。Deletion只在相应 bit multiplicity
为正时要求合法。

令 (sim_c) 是 (phi_c) 的 state equality relation。Update determinism 等价于
以下四个 right-congruence 条件：若 (a sim_c b)，则

\[
\begin{aligned}
a&\sim_{c+1}b,\\
a+1&\sim_{c+1}b+1,\\
a&\sim_{c-1}b &&\text{if }a,b<c,\\
a-1&\sim_{c-1}b-1 &&\text{if }a,b>0.
\end{aligned}
\tag{11}
\]

#### Theorem 7.1

满足 (11) 的 equivalence-relation family 只有两类：

1. 每层都是 equality；或
2. 存在唯一整数 (d>=1)，使
   
   \[
   a\sim_cb
   \quad\Longleftrightarrow\quad
   a\equiv b\pmod d
   \tag{12}
   \]
   
   对所有 (c) 成立（当 (c<d) 时这仍是 equality）。

证明。若存在 collision，令 (d) 为出现 collision 的最小 layer。若
(a<b) 且 (a sim_d b)，当 (b<d) 时共同执行 `Delete(0)` 会在 layer
(d-1) 保留 collision；当 (a>0) 时共同执行 `Delete(1)` 也会在 layer
(d-1) 保留 collision。最小性迫使 (a=0,b=d)。

从 (0 sim_d d) 出发，对两个隐藏 worlds执行相同的 zero/one insertions，得到

\[
r\sim_c r+d
\qquad(0\le r\le c-d),
\]

所以模 (d) 的每个 class 必须被合并。

反设在最小 layer (e>d) 还出现不同模-(d) classes之间的额外 merge，取
(a<b) 为其中一对。若 (b<e)，共同删除 zero 把额外 merge带到 (e-1)；若
(a>0)，共同删除 one也把它带到 (e-1)。因此只能有 (a=0,b=e)。但已知
(e-d sim_e e)，传递性给 (0 sim_e e-d)。若 (e) 不是 (d) 的倍数，这是一对
端点以内的额外 merge，删除 zero再次矛盾；若 (e) 是 (d) 的倍数，则
(0,e) 本来已经同余，并非额外 merge。矛盾。故 (12) 是全部 relation。

#### Corollary 7.2

在这个 class 中，任意 lossy construction 都恰等于某个 threshold quotient：

- (c<d) 时有 (c+1) 个 exact states；
- (c>=d) 时有 (d) 个 residue states；
- (c<d) 时 fresh bit 的 rejection probability为 (2^{-c})；
- (c>=d) 时每个 residue fiber 的 support union都含两种 bits，因此必须全
  `YES`。

所以 local counts 是

\[
1,2,\ldots,d,d,d,\ldots,
\]

且该 family 正是前面的 (L=d-1) family。特别地，在 (epsilon=1/2) 时对全部
binary canonical multiscale quotients优化后，(d=3)，即 (L=2)，严格最优。

这说明 Chinese remainder、随 occupancy 改 modulus、或高负载逐层丢弃更多
residue bits都不能工作：coarsening 丢掉的 coset在共同合法 deletions下必须
继续碰撞；除第一次 endpoint collision外，任何新 merge都会在前一层制造
无法由 deletion label消解的 ambiguity。

定理不覆盖 history-dependent local states、多个 states表示同一个 count、跨
blocks共享 syndrome或非交换 automata；因此它是 algebraic/canonical quotient
的 sharp converse，不是 ordinary AMQ universal lower bound。

## 8. 论文价值

若 finite-(n) pointwise校准和 enumerative coefficient asymptotics写全，该结果
已经严格回答一个此前未闭合的问题：ordinary lossy dynamics 可以在任意长、
fixed-state模型中严格击穿 exact multiplicity rate。它不能声称解决 KLZ fixed-
error optimum，因为 (2.34908>2.20061)，也没有 matching lower bound。

作为 SODA 主结果，当前常数改进 (0.0354) bit/key偏薄；更合理的定位是一个
新 upper-bound primitive。若进一步给出整个 (arepsilon)-curve、证明
(K=2,L=2) 或更一般 algebraic threshold family 的 sharp optimum，或者结合
lower bound刻画“可逆摘要换取 high-load distortion”的最优 tradeoff，论文
价值会显著增强。
