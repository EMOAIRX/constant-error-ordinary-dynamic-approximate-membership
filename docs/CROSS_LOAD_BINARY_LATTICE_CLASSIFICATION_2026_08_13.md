# 跨 load binary canonical summaries 的完整 lattice 分类

> 日期：2026-08-13。状态：解析证明。结论删除了此前 binary sharp converse
> 中“显式保存 exact load”的假设，但仍只覆盖 deterministic canonical local
> summaries，不覆盖 history-dependent 或 randomized representations。

## 1. 模型与全局计费

一个 block 的 binary multiset 写成

\[
x=(x_0,x_1)\in\mathbb N^2.
\]

canonical deterministic key-only insert/delete semantics 由 lattice normal
form 给出

\[
x\sim y
\quad\Longleftrightarrow\quad
x-y\in L
\]

for some subgroup \(L\le\mathbb Z^2\)。这里允许不同 total loads 的 vectors
共享物理状态。

对一个 quotient state \(m\)，定义其最小逻辑负载

\[
w(m)=\min\{x_0+x_1:[x]_L=m,\ x\in\mathbb N^2\}.
\tag{1}
\]

local minimal-weight OGF 为

\[
A_L(z)=\sum_{m\text{ reachable}}z^{w(m)}.
\tag{2}
\]

对 \(B\) 个独立 blocks、全局容量 \(n\)，可达物理状态 tuples 恰由

\[
[z^{\le n}]A_L(z)^B
\tag{3}
\]

计数：任意实际 multiset tuple 的总最小负载不超过其总实际负载；反过来，
对每个 local state 独立选择达到式 (1) 的 representative，就实现任意
总最小负载至多 \(n\) 的 tuple。

因此允许跨 load merging 后，正确计费对象是式 (2)，而不是每个固定 load
的 state count。

## 2. 按 lattice rank 完整分类

### 2.1 Rank zero

若 \(L=\{0\}\)，summary 保存 exact binary composition，且

\[
A_L(z)=\frac1{(1-z)^2}.
\tag{4}
\]

这等于 threshold modulus \(q=\infty\) 的极限。

### 2.2 Rank two

若 \(\operatorname{rank}L=2\)，则 \(G=\mathbb Z^2/L\) 有限。两个 increments
\(v_0,v_1\) 在 \(G\) 中生成的 positive monoid 是一个有限 subgroup \(H\)：
有限 monoid 中每个 element 的 inverse 都是它的一个非负倍数。

对任意 reachable state \(s\in H\) 和 query symbol \(i\)，

\[
s-v_i\in H
\]

有一个非负 composition representation。因此同一物理状态总有一个相容
multiset 包含 symbol \(i\)。minimal one-sided query 对两个 symbols、每个
state 都必须回答 YES，FPR 为一。

### 2.3 Rank one

写

\[
L=\langle(r,s)\rangle
\]

where \((r,s)\ne(0,0)\) 是该 subgroup 的一个 generator。注意
\(\gcd(|r|,|s|)\) 不必为一；证明不能静默假设 quotient torsion-free。

#### 同号生成元

若 \(rs>0\)，改变 generator 符号后可设 \(r,s>0\)。每个 state 若有
representative \(x\)，也有 \(x+(r,s)\)，后者同时包含两个 symbols。因此
所有 queries 都回答 YES。

#### 单坐标生成元

若 \(L=\langle(a,0)\rangle\)、\(a\ge1\)，states 的 normal form 是

\[
(u,v),\qquad 0\le u<a,\quad v\ge0,
\]

且 \(w=u+v\)。所以

\[
A_L(z)
=\frac{1-z^a}{(1-z)^2}
=A_a(z).
\tag{5}
\]

symbol 0 永远 compatible；symbol 1 只在 \(v>0\) 时 compatible。若 inner
symbol 1 的概率为 \(p\)，固定实际 block load \(c\) 的拒绝概率是

\[
\rho_c^{L}(p)=p(1-p)^c.
\tag{6}
\]

这逐点不超过 load-preserving order-\(a\) threshold quotient 的

\[
\rho_c^{(a)}(p)
=\mathbf1_{c<a}
\left[p(1-p)^c+(1-p)p^c\right],
\tag{7}
\]

并且二者有相同 OGF \(A_a\)。\(L=\langle(0,a)\rangle\) 对称。

#### 反号生成元

若 \(rs<0\)，交换 symbols 后可写

\[
L=\langle(a,-b)\rangle,
\qquad a\ge b\ge1.
\tag{8}
\]

每个 orbit 有唯一 normal form

\[
(u,v),\qquad 0\le u<a,\quad v\ge0.
\tag{9}
\]

从 \((u,v)\) 出发的其他 nonnegative representatives 是

\[
(u+ka,v-kb),
\qquad 0\le k\le\lfloor v/b\rfloor.
\]

因为 \(a\ge b\)，其 total load

\[
u+v+k(a-b)
\]

在 \(k=0\) 最小。因此再次有

\[
A_L(z)=A_a(z)=\frac{1-z^a}{(1-z)^2}.
\tag{10}
\]

这一结论不要求 \(\gcd(a,b)=1\)；可能存在的 quotient torsion 已包含在
\(a\) 个 normal-form residues 中。

symbol 0 被拒绝当且仅当实际 composition 为 \((0,c)\) 且 \(c<b\)；
symbol 1 被拒绝当且仅当实际 composition 为 \((c,0)\) 且 \(c<a\)。
所以

\[
\rho_c^L(p)
=(1-p)p^c\mathbf1_{c<b}
+p(1-p)^c\mathbf1_{c<a}.
\tag{11}
\]

逐个 \(c\) 比较可得

\[
\rho_c^L(p)
\le
\mathbf1_{c<a}
\left[(1-p)p^c+p(1-p)^c\right]
=\rho_c^{(a)}(p).
\tag{12}
\]

因此每个反号跨-load quotient 都被一个具有完全相同 state OGF 的
load-preserving order-\(a\) threshold quotient 在 rejection 上逐负载支配。

## 3. Domination theorem

### Theorem 3.1

对任意 deterministic canonical binary local summary，恰有下列之一：

1. 它是 exact composition；
2. 它对所有 queries 回答 YES；
3. 存在一个 load-preserving order-\(q\) threshold quotient，使二者具有相同
   local minimal-weight OGF，且 threshold quotient 对每个 load 和任意 bias
   的拒绝概率都不小于原 summary。

**证明。** 按 Section 2 的 lattice rank 和 rank-one generator 符号分类。
这些情形穷尽 \(\mathbb Z^2\) 的全部 subgroups。 \(\square\)

这个 theorem 的强点不是把跨 load quotient 写成另一个 modulus；反号 lattice
确实是 numerical-semigroup summary。结论是它节省下来的 query distinctions
没有减少 fixed-state OGF，因而严格受对应 load-preserving quotient 支配。

## 4. 删除 exact-load 假设后的 sharp theorem

### Theorem 4.1

考虑 uniform outer blocks、任意 binary inner bias、minimal one-sided query、
blockwise joint enumerative coding，以及任意 deterministic canonical key-only
binary local summaries。允许 summary 合并不同 loads。在
\(\varepsilon=1/2\) 时，唯一最优非退化设计仍为

\[
q=3,\qquad p=\frac12,
\]

其 fixed-state rate 为

\[
\boxed{
2.349083440193141\ldots\ \text{bits/key}.
}
\tag{13}
\]

**证明。** 由 Theorem 3.1，每个跨-load summary 被某个 load-preserving
threshold quotient 支配，或退化为 exact/ALL-YES。exact composition 是
\(q=\infty\) 极限，ALL-YES 不能满足 FPR \(1/2\)。因此优化可无损限制到
load-preserving biased binary thresholds。

该 family 的 sharp theorem 已证明：\(q=2,3\) 的 rejection 在
\(p=1/2\) 最大，且 \(q=3\) 更优；对所有 \(q\ge4\) 和任意 \(p\)，

\[
R_{q,p}
>\mathcal R_4(2\ln2)
=2.351275266054\ldots
>2.349083440193\ldots.
\]

\(q=\infty\) 也包含在同一 barrier 的极限中。故式 (13) 成立。唯一性除去
重命名 symbols、lattice/group 同构和不可达状态等平凡等价。 \(\square\)

## 5. 边界

Theorem 4.1 现在覆盖：

- 是否显式保存 load 的任意选择；
- rank-zero、rank-one 和 rank-two binary lattices；
- nonprimitive rank-one generators 与 quotient torsion；
- 任意 inner bias；
- 所有 deterministic canonical key-only binary local encodings。

它仍不覆盖：

- 同一 multiset 的 history-dependent multiple representations；
- randomized transition kernels；
- \(K>2\) symbols；
- 跨 blocks 的 noncanonical global state；
- arbitrary ordinary dynamic AMQs。

所以它删除的是 exact-load 假设，而不是 canonical/local 假设。
