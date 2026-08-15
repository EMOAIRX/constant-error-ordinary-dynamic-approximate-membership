# Masked binary block filters 的 sharp high-error converse

> 日期：2026-08-13。状态：本文给出一个有限 \(n\) 的 restricted converse。
> 它允许 infinitely exchangeable public labels、任意 block-dependent bias、任意
> binary canonical quotient、任意模数，以及任意多种 block 类型的 mixture。
> 在明确的 full-simplex fixed-state 模型中，
> masked threshold quotient 的 \(e/2\) 高误差常数是 sharp 的。

所有持久状态均计入空间，公共随机标签免费。算法必须支持任意长、容量始终不
超过 \(n\) 的合法 key-only update history，并在每条 tape 上没有 false negative。

## 1. 模型

公共随机带给每个 key 分配一个标签

\[
L(x)\in\{\top\}\cup\{(j,a):j\in[B],\ a\in\{0,1\}\}.
\tag{1}
\]

我们允许 labels 在 keys 间相关，但要求它们形成一个 **infinitely
exchangeable** sequence。由 de Finetti 定理，存在随机概率向量

\[
P=(P_\top,(P_{j,a})_{j,a})
\tag{2}
\]

使得条件于 \(P\)，所有 key labels i.i.d. 服从 \(P\)。普通 fully random hash
是 \(P\) 确定的特例；随机选择 block-type mixture、全局随机 bias 或随机 outer
mass 也都包含在内。记无条件边缘概率

\[
r_{j,a}=\Pr[L(x)=(j,a)]=\mathbb E P_{j,a},
\qquad
\Pr[L(x)=\top]=1-\sum_{j,a}r_{j,a}.
\tag{3}
\]

这已经允许：

- 任意 tracked mass 和 permanent-YES mask；
- 每个 block 有不同的 outer mass；
- 每个 block 有不同且任意的 binary bias；
- 任意多种 block 类型的 mixture。

结构的持久状态由 \(B\) 个 local summaries 联合编码。第 \(j\) 个 summary 是该
block 当前 binary multiset 的 deterministic canonical、key-only summary，并且
显式保持 exact local load \(c_j\)。summary 可以是任意 lattice quotient；在
binary load-preserving 情形，lattice normal form 等价地把它分类为 exact
one-count 或 one-count modulo 任意 \(q_j\)。本文的拒绝上界甚至不使用这个分类，
只要求 query 除了当前状态外只能看到标签 \((j,a)\)。\(\top\) queries 永久回答
`YES`。

最后采用以下 fixed-state 条件：固定长度内存必须表示所有

\[
(c_1,\ldots,c_B)\in\mathbb N^B,
\qquad \sum_jc_j\le n,
\tag{4}
\]

且不同 load vectors 不能共享物理状态。称之为 **full-simplex exact-load
semantics**。这是“按最坏 tracked load \(n\) 计费”的形式化版本，而不是按平均
tracked load 计费。若从有限 universe 的 reachable states 出发，也只需每个
正质量 block 的 preimage 足以实现式 (4)；本文不把这一 richness 条件静默藏在
计数中。

对任意预先固定、与公共随机带独立的合法 history，以及任意固定当前 nonmember，
要求 pointwise false-positive probability 至多 \(1-\delta\)。

## 2. 一个与 quotient 无关的 rejection bound

### Lemma 2.1（absence necessity）

固定一条 tape、当前集合 \(S\) 和 nonmember \(x\)。若
\(L(x)=(j,a)\)，且存在 \(y\in S\) 满足 \(L(y)=(j,a)\)，则 query \(x\)
必须回答 `YES`。

**证明。** Query 可见的 key-dependent 信息只有标签 \((j,a)\)。在相同物理状态
下查询成员 \(y\) 必须因 zero false negatives 回答 `YES`，而 \(x\) 与 \(y\)
向 query procedure 提供完全相同的标签。因此 \(x\) 也必须回答 `YES`。\(\square\)

这个引理比 threshold 分类更强。无论 local state 是 modulo \(q_j\)、多个
accumulators 的直积，还是任意其他 canonical quotient，拒绝都必然要求 query
所在的 block-symbol atom 在成员中完全缺席。

### Theorem 2.2（有限 \(n\) rejection ceiling）

令当前集合恰有 \(n\) 个固定成员。上述任意 masked binary block filter 的拒绝
概率 \(D_n\) 满足

\[
\boxed{
D_n
\le
\mathbb E\!\left[
\sum_{j=1}^B\sum_{a=0}^1P_{j,a}(1-P_{j,a})^n
\right]
\le
\frac{2B}{n}\left(\frac{n}{n+1}\right)^{n+1}.
}
\tag{5}
\]

特别地，

\[
D_n<\frac{2B}{en}.
\tag{6}
\]

**证明。** 由 Lemma 2.1，条件 \(L(x)=(j,a)\) 下，拒绝事件蕴含 \(n\) 个成员
均不在 atom \((j,a)\)。条件于 de Finetti parameter \(P\)，labels i.i.d.，
所以该 atom 对无条件拒绝率至多贡献
\(\mathbb E[P_{j,a}(1-P_{j,a})^n]\)。对

\[
f_n(r)=r(1-r)^n,\qquad 0\le r\le1,
\]

求导可知唯一内部极大点是 \(r=1/(n+1)\)，其极大值为

\[
f_n\!\left(\frac1{n+1}\right)
=\frac1n\left(\frac n{n+1}\right)^{n+1}.
\]

总共有至多 \(2B\) 个非 top atoms，逐项相加即得式 (5)。又
\((n/(n+1))^{n+1}<e^{-1}\)，得到式 (6)。\(\square\)

### Corollary 2.3（达到 rejection \(\delta\) 所需的 blocks）

若 pointwise FPR 至多 \(1-\delta\)，则

\[
\boxed{
\frac Bn
\ge
\frac{\delta}{2a_n},
\qquad
a_n:=\left(\frac n{n+1}\right)^{n+1},
}
\tag{7}
\]

因而 \(B/n>(e/2)\delta\)，并在 \(n\to\infty\) 时得到

\[
\frac Bn\ge\left(\frac e2-o(1)\right)\delta.
\tag{8}
\]

注意式 (7) 同时覆盖任意 bias、任意 \(q_j\)、任意 mixture，以及 infinitely
exchangeable 的全局相关性。它也解释了 uniform binary hash 与 Poisson load
\(2\) 为何出现：式 (5) 中的两个 atoms 必须同时在
单项极值点附近，即

\[
r_{j,0}\simeq r_{j,1}\simeq\frac1n.
\]

因此一个近最优 block 的总 mass 约为 \(2/n\)，条件 bias 约为 \(1/2\)。

## 3. Fixed-state 空间 converse

### Lemma 3.1（load-simplex counting）

在 full-simplex exact-load semantics 下，固定内存 \(H\) 满足

\[
2^H\ge {n+B\choose B}.
\tag{9}
\]

**证明。** 式 (4) 中 load vectors 的数量由 stars-and-bars 恰为
\({n+B\choose B}\)。exact local loads 意味着不同 vectors 对应不同物理状态。
每个状态还可能有多个 residue/syndrome values；忽略它们只会减弱下界。\(\square\)

### Theorem 3.2（sharp \(e/2\) endpoint converse）

令 \(H_{n,\delta}\) 是上述 class 中任意满足 rejection 至少 \(\delta\) 的 filter
的 fixed worst-case memory。则

\[
H_{n,\delta}
\ge
\log_2{n+\lceil n\delta/(2a_n)\rceil\choose
\lceil n\delta/(2a_n)\rceil}.
\tag{10}
\]

特别地，在先令 \(n\to\infty\)、再令 \(\delta\downarrow0\) 的 iterated limit 中，

\[
\boxed{
\liminf_{\delta\downarrow0}\;
\liminf_{n\to\infty}
\frac{H_{n,\delta}}
{n\delta\log_2(1/\delta)}
\ge\frac e2.
}
\tag{11}
\]

**证明。** Corollary 2.3 给出所需的最小 \(B\)，而
\(B\mapsto{n+B\choose B}\) 单调增加，故式 (10) 由 Lemma 3.1 得到。令
\(b=B/n\)。标准 entropy asymptotic 为

\[
\frac1n\log_2{n+B\choose B}
=\frac{(1+b)\ln(1+b)-b\ln b}{\ln2}+o_n(1).
\tag{12}
\]

右侧关于 \(b\) 严格递增。代入
\(b\ge(e/2)\delta+o_n(1)\)，再用

\[
(1+b)\ln(1+b)-b\ln b
=b\ln\frac1b+O(b),
\tag{13}
\]

即得式 (11)。\(\square\)

结合 masked threshold quotient 的 upper bound，立刻得到：

### Corollary 3.3（restricted-class sharp theorem）

在 infinitely exchangeable public labels、binary key-oblivious local queries、
full-simplex exact-load fixed states 组成的 class 中，允许任意 canonical
quotient、任意 bias、任意
block masses 和任意 block-type mixture，最优 high-error rate 满足

\[
\boxed{
H^*_{n,\delta}
=\left(\frac e2+o(1)\right)
n\delta\log_2\frac1\delta.
}
\tag{14}
\]

upper bound 由 uniform binary labels、每 block Poisson mean \(2\)、增长但满足
\(\ln q=o(\ln(1/\delta))\) 的 threshold quotient 达到。converse 表明 bias、
heterogeneous loads、不同 moduli 和 mixtures 均不能改善 leading constant。

## 4. 稳定性信息

证明还给出一个接近等号时的结构约束。令

\[
g_n(r)=r(1-r)^n,
\qquad m_n=\max_rg_n(r).
\]

若一个 family 满足

\[
D_n\ge(1-o(1))\,2Bm_n,
\tag{15}
\]

则除 \(o(B)\) 个 atoms 的总 deficit 外，贡献主要拒绝率的 atoms 必须满足

\[
nr_{j,a}=1+o(1).
\tag{16}
\]

这是因为缩放 \(r=x/n\) 后，

\[
ng_n(x/n)\longrightarrow xe^{-x},
\]

而 \(xe^{-x}\) 在 \(x=1\) 有唯一严格极大点。若某个正比例的有效贡献来自
\(|nr-1|\ge\eta\)，式 (14) 会损失只依赖 \(\eta\) 的常数比例。

因此，任何达到 \(e/2\) 的 binary mixture 在 leading order 上都被强迫回

\[
\text{uniform inner bit}\quad+\quad\text{outer mean load }2.
\]

这里的稳定性是 rejection ceiling 的稳定性；若要声明完整 filter state 也唯一，
还需分析 residue-state 开销何时为 lower order。本文不作这个过强声明。

## 5. 边界与不能外推之处

式 (14) 是一个真正 matching、且比“固定 \(q\) 的最优性”更宽的 restricted
theorem，但它不是 ordinary dynamic AMQ 的全局 converse。关键边界是：

1. **Binary label budget。** 若每 block 有 \(K\) 个 query-distinguishable atoms，
   同一 argument 只给 \(D_n\le K B/(en)\)，常数变为 \(e/K\)。因此不能把
   \(e/2\) 外推到 multisymbol filters。
2. **Key-oblivious local query。** 若 query 能使用标签外的额外 key-dependent
   public information，这些信息必须计入有效 alphabet；否则 Lemma 2.1 的
   indistinguishability 不成立。
3. **Infinite extendibility。** 本定理允许 infinitely exchangeable labels，因而
   已包含 de Finetti mixtures 所描述的相关性；但只在一个有限 universe 上定义、
   不可无限延拓的 exchangeable 无放回分配不在模型内。对后者，条件 absence
   probability 可以严格大于 i.i.d. 值，必须结合 universe richness 单独处理。
4. **Exact per-block loads。** 式 (9) 使用 full-simplex load preservation。允许
   cross-load merging 或跨 blocks 联合 quotient 时，load-simplex 下界可能失效。
5. **Universe richness。** 若实现只需编码某张有限 tape 上实际 reachable 的
   states，必须显式保证 block preimages 足够大；不能把 formal load vectors 自动
   当作 reachable vectors。

第一点尤其重要：这个 converse 在 binary class 中封口，同时明确指出更有潜力的
下一条路线不是继续调 bias 或混合 \(q\)，而是研究 multisymbol quotient 的

\[
\text{atom 数带来的 rejection 增益}
\quad\text{vs.}\quad
\text{syndrome states 的额外代价}.
\]

## 6. 结论

在指定 natural class 内，\(e/2\) 不是参数优化的偶然常数。它由两个独立且都
sharp 的障碍相乘得到：

\[
\underbrace{2B/(en)}_{\text{每个 binary block 的最大拒绝贡献}}
\quad+\quad
\underbrace{\log_2{n+B\choose B}}_{\text{最坏 load simplex}}.
\]

这给出了 masked threshold endpoint 的 matching restricted converse，并排除了
biased hash、任意 modulus、heterogeneous block loads 和 block-type mixtures
作为突破 \(e/2\) 的可能来源。若要获得更强结论，必须真正越过至少一个模型边界：
增加 alphabet、合并 loads、使用 cross-block quotient，或允许不可无限延拓的
有限 exchangeable 公共标签结构。
