# Multi-parent posterior deficit 与 `u >> n`：正面 lemma 和局部 no-go

> 日期：2026-08-13。状态：严格 source-list mutual-information lemma；严格
> ordinary cover-and-tombstone 反例。结论是：在 `u/n -> infinity` 下，可不经
> hard full-fiber transport 直接证明 `J_s` 的 Carter 级下界；但 rejection、单个
> source-fiber multiplicity 与 source-path mutual information 本身不能普适给出
> 超静态线性项。更强定理必须使用多个重叠 KLZ parents 的 simultaneous
> continuation capacity。

所有对数以 2 为底。

## 1. KLZ multi-parent statistic

令 `Theta` 包含 public partition、tree shape 和全部 non-rightmost labels，`R` 是
filter tape。Hidden batches

\[
X=(X_1,\ldots,X_b),
\qquad
X_k\in U_k^{\underline m},
\quad m=n/b,
\quad V=|U_k|=u/b
\tag{1}
\]

条件于 `Theta` 相互独立且均匀无放回。

对 pivot `s`，按 KLZ decode order 令 `D_k` 是发送第 `k` 批前已解码的 batches，
并令

\[
(r_k,\ell_k)=
\begin{cases}
(b,k-1),&k\le s,\\
(k,s),&k>s.
\end{cases}
\tag{2}
\]

定义

\[
J_s=\sum_{k=1}^b
I(X_k;F_{r_k}\mid\Theta,R,D_k).
\tag{3}
\]

所有 `F_{r_k}` 均由最终状态、public data 和已解码 batches 确定，所以

\[
J_s\le I(X;M_b\mid\Theta,R)\le H.
\tag{4}
\]

## 2. Unconditional source-list lemma

固定一个 `k`，写

\[
C=(\Theta,D_k),\qquad F=F_{r_k}.
\]

给定 `(C=c,R=r,F=f)`，定义 `X_k` 的 source list

\[
\mathcal L(c,r,f)
=\{x\in U_k^{\underline m}:
\Pr[X_k=x\mid C=c,R=r,F=f]>0\},
\tag{5}
\]

以及 coordinate union

\[
W(c,r,f)=\bigcup_{x\in\mathcal L(c,r,f)}\{x_1,\ldots,x_m\}.
\tag{6}
\]

这里 list 允许未被 `C` 固定的其他 hidden batches随 completion 改变。

### Lemma 1（source-list support is accepted）

对每个 realized `(c,r,f)`，

\[
W(c,r,f)\subseteq A_r(f)\cap U_k.
\tag{7}
\]

证明。若 `y in W`，存在一个正 posterior probability 的 source completion，使
同一物理 state `f` 的当前真集合包含 `y`。Zero false negatives 迫使 state `f`
查询 `y` 为 YES。Query 只依赖 `(r,f,y)`，故 (7) 对所有 completions同时成立。

### Lemma 2（unconditional expected list union）

对实际 source realization，令

\[
w=|W(C,R,F)|.
\]

则

\[
\boxed{\mathbb Ew\le m+\varepsilon(V-m).}
\tag{8}
\]

证明。固定 `Theta`、全部 hidden batches和由此确定的实际合法 history。对每个
`y in U_k\setminus X_k`，由于 blocks互不相交，`y` 是 state `F` 当前真集合的
nonmember。事件

\[
y\in W(C,R,F)
\]

由 (7) 蕴含 `Query_F(y)=YES`。因此对 filter tape `R` 的概率至多
`epsilon`。对 `V-m` 个 fixed nonmembers求和，再对 source randomness平均，即得
(8)。

关键是先固定实际 history，再只对 `R` 使用 pointwise FPR。证明没有在条件于
`R` 或 `F` 后重用 FPR。

### Theorem 3（source-list mutual information）

\[
\boxed{
I(X_k;F_{r_k}\mid\Theta,R,D_k)
\ge
\log(V)_{\underline m}
-\log\bigl(m+\varepsilon(V-m)\bigr)_{\underline m}.
}
\tag{9}
\]

证明。给定 `(C,R,F)`，list 中的每个 ordered tuple使用 `W` 中 distinct
coordinates，故

\[
|\mathcal L(C,R,F)|\le(w)_{\underline m}.
\tag{10}
\]

于是

\[
H(X_k\mid C,R,F)
\le\mathbb E\log(w)_{\underline m}.
\tag{11}
\]

函数

\[
z\longmapsto\log(z)_{\underline m}
=\sum_{i=0}^{m-1}\log(z-i)
\]

在 `z>=m` 上凹。实际 tuple 本身总在 list 内，所以 `w>=m`。由 Jensen 与 (8)，

\[
H(X_k\mid C,R,F)
\le
\log\bigl(m+\varepsilon(V-m)\bigr)_{\underline m}.
\tag{12}
\]

另一方面，`D_k` 只含其他 independent batches，故

\[
H(X_k\mid C,R)=\log(V)_{\underline m}.
\tag{13}
\]

两式相减即得 (9)。

### Corollary 4（`u >> n` Carter bound）

若 `V/m=u/n->infinity`，则一致地

\[
\log(V)_{\underline m}
-\log\bigl(m+\varepsilon(V-m)\bigr)_{\underline m}
=m\log(1/\varepsilon)-o(m).
\tag{14}
\]

对 (9) 的 `b` 个 terms求和，得到对每个 pivot `s`

\[
\boxed{
J_s\ge n\log(1/\varepsilon)-o(n).
}
\tag{15}
\]

结合 (4)，恢复 ordinary model 在 `u/n->infinity` 下的静态 Carter 下界。这个
证明允许 history dependence、non-monotonicity、global certificates 和任意
source-list correlation。

## 3. 为什么 parent rejection 尚未改善 (15)

令 `G` 是 batch insertion 前的 parent state。对 actual batch，pointwise FPR给

\[
\mathbb E|X_k\setminus A(G)|\ge(1-\varepsilon)m.
\tag{16}
\]

一个自然猜想是把 (16)、source-list multiplicity (10) 与 mutual information
(9) 联合，普适推出

\[
I(X_k;F\mid C,R)
\ge m\log(1/\varepsilon)+c m
\tag{17}
\]

for some `c>0`。下一节给出一个 ordinary arbitrary-history反例：即使 parent
拒绝整个 source batch，child source state仍可只有静态 cover rate。额外的未来
transition capacity可以存在于当时为常数零的大字段中，因而不被 source-path
mutual information看见。

## 4. Cover-and-tombstone ordinary filter

固定 `0<rho<epsilon`，取例如 `u=n^2`。Public tape含

\[
N=\lceil\rho^{-n}n^2\rceil
\tag{18}
\]

个 independent Bernoulli-`rho` subsets

\[
A_1,\ldots,A_N\subseteq U.
\]

Filter 有两种模式。

### Exact mode

用一个 `u`-bit vector精确保存当前集合。只要尚未发生 compression，query 和
updates都 exact。

当一次合法 insertion 后 load 第一次达到 `n`，设当前集合为 `S_0`。查找最小
index

\[
i=\min\{j:S_0\subseteq A_j\}.
\tag{19}
\]

若不存在，永远留在 exact mode。若存在，进入 cover mode，保存

\[
(i,T=\varnothing,E=\varnothing).
\tag{20}
\]

### Cover mode

`T subseteq A_i` 是 tombstones；`E subseteq U\setminus A_i` 是当前 exact live
exceptions。定义 query：

\[
\operatorname{Query}(x)=YES
\iff
x\in(A_i\setminus T)\cup E.
\tag{21}
\]

Updates 为：

- `Delete(x)`：若 `x in A_i`，加入 `T`；否则从 `E` 删除；
- `Insert(x)`：若 `x in A_i`，从 `T` 删除；否则加入 `E`。

用两个 `u`-bit vectors存 `T,E` 即可支持任意长 histories；tombstones不会
overflow。所有 modes padding 到同一个 fixed block，故 worst-case persistent
memory 是 `O(u+n log(1/rho))` bits。

### Lemma 5（correctness and pointwise FPR）

这个结构是 ordinary key-only、arbitrary-history one-sided filter，FPR 至多
`rho<=epsilon`。

证明。Zero false negatives由 (21) 的更新 invariant直接成立。固定任意合法
history和当前 nonmember `x`。

- 若从未 compression，query exact。
- 若 `x in S_0`，当前成为 nonmember意味着 compression 后最后相关操作是
  `Delete(x)`，故 `x in T`。
- 若 `x notin S_0`，但 compression 后曾 insert再 delete，最终同样被 `T` 或
  `E` 的 exact update拒绝。
- 唯一可能的 FP 是 `x notin S_0` 且之后从未成为 member，而 selected cover
  `A_i` 碰巧包含 `x`。

对每个 `j`，事件“`j` 是第一个包含 `S_0` 的 cover”只依赖各 cover在
`S_0` coordinates上的 bits；`x notin S_0` 的 bit独立且为 Bernoulli-`rho`。
所以

\[
\Pr_R[x\in A_i,\ i\text{ exists}]
=\rho\Pr_R[i\text{ exists}]\le\rho.
\tag{22}
\]

no-cover fallback exact，不贡献 FP。

## 5. Static-rate endpoint with maximal rejection

考虑从 empty exact state开始，插入一个均匀 random `n`-set `S` 的 canonical
ordered sequence。把 batch parent取为插入前的 empty state；它拒绝 `S` 中全部
keys。最终 load `n` 时发生 compression。

给定 public tape，最终 normal state只含 cover index `i`；`T,E` 是固定空向量。
No-cover概率至多

\[
(1-\rho^n)^N\le e^{-n^2}.
\tag{23}
\]

因此对 polynomial universe（例如 `u=n^2`），

\[
\begin{aligned}
I(S;M\mid R)
&=H(M\mid R)\\
&\le\log(N+1)
+e^{-n^2}\log{u\choose n}\\
&=n\log(1/\rho)+O(\log n).
\end{aligned}
\tag{24}
\]

所以该 source endpoint同时具有：

1. parent rejection probability `1`；
2. large static-cover source fibers；
3. 仅 Carter 级 mutual information；
4. 完整 ordinary arbitrary-history continuation closure。

大 `T,E` fields 对后续 operations至关重要，但在 source endpoint恒为零，不进入
(24)。这严格否决任何只依据这三个 endpoint observables，把 rejection额外线性
加到 mutual information上的 inequality。

## 6. Tensorized版本

取 `q` 个 disjoint universes，每个运行独立 cover-and-tombstone component，并把
global query/update路由到 key 所属 component。每个 component 在自己的 load
第一次达到 `n_0` 时 compression；超过 `n_0` 后仍由 `T,E` bitvectors合法处理，
所以不需要 per-component capacity promise。Global capacity取 `q n_0`。

对 source distribution，每个 component插入恰好 `n_0` 个独立 keys。最终 state
mutual information与 parent rejection均 direct-sum：

\[
I(S_{1:q};M\mid R)
\le qn_0\log(1/\rho)+o(qn_0),
\tag{25}
\]

而每个 parent拒绝自己的完整 batch。故反例对任意线性规模张量化；它不是一个
finite-depth pressure test。

## 7. 对 `J_s` 主线的精确裁决

已经严格得到：

\[
J_s\ge n\log(1/\varepsilon)-o(n)
\]

在 `u/n->infinity` 下成立，而且证明从不条件于 tape/state调用 FPR。

也已经严格否决：

> 单独从 unconditional rejection、一个 parent--child source-fiber multiplicity
> 和该 child 的 source mutual information，推出超 Carter 的普适线性项。

Cover-and-tombstone filter 并不直接计算 KLZ 特定 obfuscating tree 上的 `J_s`；
因此它没有否决一个真正使用 KLZ 多个重叠 parents 的 theorem。它否决的是把所需
主 lemma局部化为彼此独立的 single-parent inequalities。

剩余最小目标必须显式使用：

1. 同一个 final state同时导出许多 `F_r` parents；
2. 不同 parents 的 source fibers重叠，而非 disjoint tensor components；
3. continuation metadata虽可在一个 endpoint为常数零，却不能在全部 KLZ parents
   同时为零；
4. 全部收费仍通过 `J_s<=H` 的 single budget，而不是累加 intermediate state
   entropies。

换言之，真正缺失的是 **multi-parent overlap deficit**，不是更强的单 parent
rate-distortion inequality。若不能量化上述 overlap，soft-posterior 方法最多把
universe 条件降到 `u>>n` 并恢复 Carter rate，不能保留 endpoint batch converse 的
`1.434406...` dynamic premium。

