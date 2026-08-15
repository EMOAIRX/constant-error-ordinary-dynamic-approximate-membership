# 跨 load binary lattice classification：hostile audit 与修正版

> 日期：2026-08-13。结论：`CROSS_LOAD_BINARY_LATTICE_CLASSIFICATION_2026_08_13.md`
> 的 rank-two、同号 rank-one、反号 rank-one 分类通过；单坐标 rank-one 的
> “被同 OGF threshold 逐负载支配”断言为假。修正后，half-error 的 sharp
> (q=3) 结论仍成立，但 domination theorem 必须单列 coordinate lattice。
> 此结论针对 block-local query；若额外保存 exact global cardinality 并允许查询
> 联合检查其他 blocks，仍需单独证明 global-compensation lemma。

## 1. 模型和计费

一个 block 的 binary composition 为 (x=(x_0,x_1)\in\mathbb N^2)。
deterministic canonical key-only insert/delete summary 的等价关系必为

\[
x\sim y\iff x-y\in L,
\qquad L\le\mathbb Z^2.
\tag{1}
\]

对 reachable coset (m)，定义最小逻辑负载

\[
w(m)=\min\{x_0+x_1:x\in\mathbb N^2,\ [x]_L=m\},
\tag{2}
\]

以及

\[
A_L(z)=\sum_{m\text{ reachable}}z^{w(m)}.
\tag{3}
\]

若持久状态只是 (B) 个 local summaries 的 tuple，容量至多 (n)，则状态数恰为

\[
[z^{\le n}]A_L(z)^B.
\tag{4}
\]

正向显然；反向对每个 coset 独立选择达到最小负载的 representative 即可。因此
式 (3) 是允许 cross-load merging 后正确的 local fixed-state OGF。

对正系数 OGF (A)，记 (n/B\to\lambda) 时的每 key rate 为

\[
\mathcal R_A(\lambda)
=\inf_{0<z<1}
\left\{\frac1\lambda\log_2A(z)-\log_2z\right\}.
\tag{5}
\]

它随 \(A\) 的逐系数增大而不减，并对固定非平凡 \(A\) 随
\(\lambda\) 增大而严格下降。后者在 interior saddle 处由

\[
\frac{d}{d\lambda}\mathcal R_A(\lambda)
=-\frac{\log_2A(z_\lambda)}{\lambda^2}<0
\tag{6}
\]

得到。

## 2. Rank zero 与 rank two

### Rank zero：通过

(L=\{0\}) 保存 exact composition，

\[
A_L(z)=\sum_{x_0,x_1\ge0}z^{x_0+x_1}
=\frac1{(1-z)^2}.
\tag{7}
\]

### Rank two：通过

若 (\operatorname{rank}L=2)，则 (G=\mathbb Z^2/L) 有限。令
(v_0,v_1\in G) 为两个 increments，(H) 为它们生成的 positive monoid。
有限群中的 finite submonoid 是 subgroup：对 (h\in H)，有限性给
(rh=sh)（(r<s)），故 (-h=(s-r-1)h\in H)。

于是对任意 reachable (s\in H) 和 symbol (i)，

\[
s-v_i\in H
\]

有 nonnegative composition representation。加回一个 (v_i)，便得到同 state
且包含 (i) 的 composition。因此在只读 local state 的 minimal one-sided
query 下，每个 state 对两个 symbols 都必须回答 `YES`，FPR 为一。

这个论证包括真实 composition 为空的 state；cross-load quotient 正是允许某个
非空 composition 与它共享 state。

## 3. Rank one 的完整审计

任意 rank-one subgroup 唯一地写为

\[
L=\langle(r,s)\rangle
\tag{8}
\]

（generator 只差符号）。不应假设 (\gcd(|r|,|s|)=1)：subgroup 在
(\mathbb Z^2) 中可以非 primitive。

### 3.1 同号 generator：通过

若 (rs>0)，换符号后令 (r,s>0)。每个 representative (x) 都与
(x+(r,s)) 等价，后者同时包含两个 symbols。因此每个 query 都必须接受。

### 3.2 单坐标 generator：原 domination 断言失败，但可单独排除

令

\[
L=\langle(a,0)\rangle,
\qquad a\ge1.
\tag{9}
\]

唯一 normal form 为

\[
(u,v),\qquad 0\le u<a,\quad v\ge0,
\tag{10}
\]

最小负载为 (u+v)，所以在两个 symbols 都有正概率时

\[
A_L(z)=\frac{1-z^a}{(1-z)^2}=:A_a(z).
\tag{11}
\]

令 member/query symbol 1 的概率为 (p)。symbol 0 对每个 state 都
compatible；symbol 1 当且仅当 (v>0) 时 compatible。因此 load 为 (c) 的
精确 rejection 为

\[
\rho_c^{\rm coord}(p)=p(1-p)^c.
\tag{12}
\]

这里原稿的错误是声称式 (12) 被 order-(a) exact-load threshold 的

\[
\rho_c^{(a)}(p)
=\mathbf1_{c<a}
\bigl[p(1-p)^c+(1-p)p^c\bigr]
\tag{13}
\]

逐点支配。当 (c\ge a) 时，式 (13) 为零而式 (12) 对
(0<p<1) 严格为正，所以该比较方向不成立。

不过 coordinate lattice 仍不能改善 half-error optimum。Poisson mixing 给

\[
J_{\rm coord}(\lambda,p)
=e^{-\lambda}\sum_{c\ge0}\frac{\lambda^c}{c!}p(1-p)^c
=p e^{-\lambda p}.
\tag{14}
\]

若 (J_{\rm coord}\ge1/2)，则 (p>1/2) 且

\[
\lambda\le \frac{\ln(2p)}p\le\ln2.
\tag{15}
\]

最后一个不等式由 (p\mapsto\ln(2p)/p) 在 ([1/2,1]) 上递增得到，因为其
导数为 ((1-\ln(2p))/p^2>0)。无论 (p\in(0,1)) 时使用式 (11)，还是
(p=1) 时只计真正 reachable 的 unary states，都有逐系数下界

\[
A_L(z)\succeq A_{\rm unary}(z):=\frac1{1-z}.
\tag{16}
\]

结合 rate 对 (A) 和 (\lambda) 的单调性，

\[
\mathcal R_{A_L}(\lambda)
\ge \mathcal R_{A_{\rm unary}}(\ln2)
=2.384499842478516\ldots
>2.349083440193141\ldots.
\tag{17}
\]

其中 unary saddle 为

\[
z=\frac{\ln2}{1+\ln2}.
\]

(L=\langle(0,a)\rangle) 完全对称。

### 3.3 反号 generator：通过

交换 symbols 后可写

\[
L=\langle(a,-b)\rangle,
\qquad a\ge b\ge1.
\tag{18}
\]

每个 orbit 的唯一 normal form 是

\[
(u,v),\qquad0\le u<a,quad v\ge0.
\tag{19}
\]

其他 nonnegative representatives 恰为

\[
(u+ka,v-kb),
\qquad0\le k\le\lfloor v/b\rfloor.
\tag{20}
\]

其 load 是 (u+v+k(a-b))，在 (k=0) 最小。因此即使
(\gcd(a,b)>1)，仍有

\[
A_L(z)=\sum_{u=0}^{a-1}\sum_{v\ge0}z^{u+v}
=\frac{1-z^a}{(1-z)^2}=A_a(z).
\tag{21}
\]

现在直接检查 compatibility。symbol 0 只能在真实 composition 为
((0,c)) 时缺席；由式 (20)，它仍不可加入当且仅当 (c<b)。类似地，
symbol 1 只在真实 composition 为 ((c,0)) 且 (c<a) 时不可加入。故

\[
\rho_c^L(p)
=(1-p)p^c\mathbf1_{c<b}
+p(1-p)^c\mathbf1_{c<a}.
\tag{22}
\]

由于 (b\le a)，逐 load 有

\[
\rho_c^L(p)
\le\mathbf1_{c<a}
\bigl[(1-p)p^c+p(1-p)^c\bigr]
=\rho_c^{(a)}(p).
\tag{23}
\]

而两者的 OGF 同为 (A_a)。所以每个反号 oblique lattice 都被
load-preserving order-(a) threshold 在 rejection 上逐负载支配。等号只在
(b=a) 或相应退化 bias/不可达事件中出现；(a=b) 正是保持 exact load 的
lattice。

## 4. 修正后的 domination theorem

### Theorem 4.1

任意 deterministic canonical binary local summary 恰落入以下类别之一：

1. (L=0)：exact composition；
2. rank two 或同号 rank one：local minimal query 为 ALL-YES；
3. 单坐标 rank one：其 half-error rate 至少为
   (2.384499842478516\ldots) bits/key；
4. 反号 rank one：被具有相同 minimal-weight OGF 的 load-preserving threshold
   quotient 逐 load 支配。

这四类穷尽 (\mathbb Z^2) 的全部 subgroups。注意第 3 类不能并入第 4 类的
逐点 domination statement。

### Corollary 4.2（half-error sharp optimum）

在以下明确范围内：

- uniform outer blocks；
- 任意 binary inner bias；
- deterministic canonical key-only local summary；
- query 只读被查询 block 的 local state；
- block tuples 使用式 (4) 的 joint enumerative coding；
- zero false negatives 与 minimal one-sided query；

即使允许不同 loads 共享 local state，

\[
\boxed{
q=3,\qquad p=\frac12,\qquad
R=2.349083440193141\ldots
}
\tag{24}
\]

仍是唯一非退化最优解（忽略 symbol 重命名与 quotient 同构）。

**证明。** 第 2 类不满足 half-error；第 3 类由式 (17) 严格更差；第 1 类在
最优 bias/load 下为 (2.384499842478516\ldots)。第 4 类可无损换成同 OGF、
rejection 更高的 load-preserving threshold。已有 biased-binary threshold
sharp converse 给出：(q=2) 更差，(q=3,p=1/2) 达到式 (24)，所有
(q\ge4) 满足

\[
R_{q,p}>\mathcal R_4(2\ln2)
=2.351275266054\ldots>R_3.
\]

故结论成立。

## 5. 必须保留的模型边界：global exact cardinality

式 (22) 使用的是 local minimal query：给定目标 block state，只要该 coset 中
存在含 query symbol 的某个 nonnegative representative，就必须回答 `YES`。

若数据结构另用 (O(\log n)) bits 保存当前 exact total cardinality (N)，并允许
query 联合读取全部其他 block states，则 compatibility 条件会变成：目标 block
的替代 representative 必须能由其他 blocks 的 load changes 补偿，使总 load
仍为 (N)。这可能排除某些 local witnesses。因此，不能从 local lattice
classification 静默推出带 global cardinality side information 的同一 FPR 公式。

对固定非退化参数，随机 occupancy 下通常会有线性多个 donor blocks，直觉上这种
补偿失败只具有 (e^{-\Omega(n)}) 概率；但要覆盖 pointwise public-hash 模型，需
正式证明一个 **global-compensation lemma**。rank-two finite quotients 尤其应
单独处理，不能只重复“positive monoid 是 group”的 local argument。

因此，式 (24) 删除了 exact **local** load 假设，却没有自动覆盖：

- exact global cardinality 参与 query；
- cross-block canonical auxiliary state；
- history-dependent multiple representations；
- randomized transitions；
- (K>2) alphabets；
- arbitrary ordinary dynamic AMQs。

## 6. 最终裁决

- **PASS**：rank-two local ALL-YES；同号 rank-one ALL-YES；反号 normal form；
  nonprimitive generator；minimal-weight OGF；式 (22) 的 bias coefficients；
  反号 lattice 被 threshold 支配。
- **FAIL，已修正**：单坐标 lattice 被 finite threshold 逐负载支配。
- **PASS after repair**：在明确的 block-local canonical binary class 中，允许
  cross-load merging 仍不能击败 (q=3) 的
  (2.349083440193141\ldots) bits/key。
- **OPEN beyond stated class**：带 exact global cardinality/cross-block query 的
  compensation 问题。
