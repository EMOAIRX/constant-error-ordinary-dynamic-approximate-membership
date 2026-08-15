# Four-symbol tree lattices：从参数构造到结构分类

> 日期：2026-08-13。状态：Sections 1--4 为解析结构定理；Section 5 的
> `(3,6,3)` sharpness 目前由有限精确 profile 枚举和已有 interval rate certificate
> 支撑。要把整个无界 tree-weight family 的最优性写成最终 theorem，仍需为
> Sections 6 的 tail reduction补齐统一有理区间证书。

## 1. 模型

令四个 symbols 为顶点

\[
A_1-A_0-B_0-B_1
\]

组成的一条 path。对三条边分别给正整数权重

\[
(q_A,Q,q_B).
\]

在 composition lattice

\[
A_3=\{x\in\mathbb Z^4:\sum_i x_i=0\}
\]

中定义

\[
L(q_A,Q,q_B)=\langle
q_A(e_{A_1}-e_{A_0}),
Q(e_{A_0}-e_{B_0}),
q_B(e_{B_1}-e_{B_0})
\rangle_{\mathbb Z}.
\tag{1}
\]

block 显式保存 exact load 与 coset modulo `L`。这是 deterministic canonical、
key-only、任意长 history 的 additive summary。

## 2. Tree-edge basis theorem

### Theorem 2.1

对任意有 `K` 个顶点的树 `T`，任意定向后的边差

\[
b_e=e_u-e_v,\qquad e\in E(T),
\]

构成根格

\[
A_{K-1}=\{x\in\mathbb Z^K:\sum_i x_i=0\}
\]

的一组整数基。

**证明。** 边差显然线性无关：从叶子开始看该叶坐标即可逐条消去系数。另一方面，
固定根 `r` 后，每个 `e_v-e_r` 都是从 `r` 到 `v` 的 path edge differences 之和；
而这些向量生成 `A_{K-1}`。故树边差既线性无关又整生成根格。`□`

### Corollary 2.2

给每条边权重 `q_e>=1`，令

\[
L_T(q)=\langle q_eb_e:e\in E(T)\rangle.
\]

则

\[
\boxed{[A_{K-1}:L_T(q)]=\prod_{e\in E(T)}q_e.}
\tag{2}
\]

在 tree-edge basis 中 quotient 是坐标商

\[
A_{K-1}/L_T(q)\cong\bigoplus_{e\in E(T)}\mathbb Z_{q_e}.
\tag{3}
\]

注意 `(q_e)` 未必是 invariant-factor normal form；若需要 Smith normal form，仍需
把这些 cyclic factors 按素因子重新组合。但 group order 一定是式 (2)。

## 3. Two-subblock family 的精确等价

取 oriented path edges

\[
b_1=e_{A_1}-e_{A_0},\quad
b_2=e_{A_0}-e_{B_0},\quad
b_3=e_{B_1}-e_{B_0}.
\]

保存 exact load 后，式 (1) 的 coset可由三坐标表示：

\[
\left(
a_1\bmod q_A,
(a_0+a_1)\bmod Q,
b_1\bmod q_B
\right).
\tag{4}
\]

这是因为跨 middle edge 的一侧 subtree load 正是 `a_0+a_1`；端点 edge 的
subtree loads分别是 `a_1,b_1`。所以此前的 two-subblock construction

\[
(c,(a_0+a_1)\bmod Q,a_1\bmod q_A,b_1\bmod q_B)
\]

不是一个偶然坐标选择，而是全部 four-vertex weighted-path lattices 的 tree normal
form。

特别地，cross-block mod-6 construction 恰为

\[
\boxed{(q_A,Q,q_B)=(3,6,3)},
\]

其 quotient order为

\[
3\cdot6\cdot3=54.
\]

## 4. 固定 quotient group 内的进一步分类

由 CRT，

\[
G=\mathbb Z_6\times\mathbb Z_3^2
\cong \mathbb Z_2\times\mathbb F_3^3.
\tag{5}
\]

考虑四个均匀 increments，平移后令第一个为零，并要求它们生成整个 `G`。其
`F_3^3` 投影必须是四个 affine independent points：否则三个 differences 不能生成
三维 `F_3` 空间。任意 affine frame 都可由 `AGL(3,3)` 送到

\[
0,e_1,e_2,e_3.
\]

因此只剩四个点的 `Z_2` labels。允许 symbol permutation、整体 `Z_2` translation
和 affine-frame permutation 后，非退化 labels 只有两类：

1. balanced `2+2` split；
2. unbalanced `1+3` split。

constant `0+4` split不生成 `Z_2` factor。

精确 walk-count/support-union 计算给：

### Balanced type

\[
d=(1,4,10,18,27,36,44,50,53,54,54,\ldots),
\]

\[
\rho=\left(1,\frac34,\frac9{16},\frac{13}{32},\frac9{32},\frac3{16},
\frac{237}{2048},\frac{63}{1024},\frac{189}{8192},
\frac{189}{32768},0,\ldots\right).
\]

其 half-error rate由已有 interval verifier认证为

\[
2.34614905208<R_{2+2}<2.34614905664.
\]

### Unbalanced type

state profile相同，但 rejection profile为

\[
\rho=\left(1,\frac34,\frac9{16},\frac{51}{128},\frac{135}{512},
\frac{333}{2048},\frac{189}{2048},\frac{189}{4096},
\frac{567}{32768},\frac{567}{131072},0,\ldots\right),
\]

数值 rate为

\[
R_{1+3}=2.368816943174\ldots.
\]

因为两个 types有完全相同的 state OGF，而 balanced type从 load 3 起逐层具有更高
rejection，所以其 half-error calibrated load更大，rate严格更低。这个严格比较不需要
依赖 `2.3688` 的小数值。

因此：

> 在固定 group `Z_6 x Z_3^2`、四个均匀 symbols、increments生成全群的全部
> Cayley quotients中，balanced `2+2` type（包括 `(3,6,3)` path lattice）是唯一
> profile type optimum；唯一性只差平移、群 automorphism和 symbol permutation。

这比“在 allocation modulus `Q` 中 `Q=6` 最优”强：它排除了同一 54-state group
内所有 primitive coefficients、mod-3 mixing和非 tree-looking generator choices。

## 5. 当前最有价值的主结论

若只提交 finite family sharpness，主叙事不应是 `0.0029n` 的小改进，而应是：

1. canonical reversible summaries 的 lattice normal form；
2. tree-edge bases把一类 cross-block summaries完全参数化；
3. `(3,6,3)` 首次击穿 binary canonical optimum；
4. CRT/affine-frame classification证明它在整个 54-state four-symbol Cayley design
   space中结构最优。

这已经是可解释的结构结论，而非黑盒参数搜索。

## 6. 仍未闭合的更强命题

无界 weighted-path family

\[
(q_A,Q,q_B)\in\mathbb N^3
\]

的全局最优性目前只有广泛有限搜索支持：在 `1<=q_A,q_B,Q<=12` 中，唯一最佳参数
（忽略 path reversal）是 `(3,6,3)`。这不是一般证明。

一个 reviewer-safe 的解析路线是：

1. 用 binary threshold converse排除某条 endpoint edge过小或过大的 tails；
2. 对固定 endpoint weights，使用 allocation frozen-tail relaxation统一排除大 `Q`；
3. 对剩余有限 box使用 exact rational profiles和 interval rate certificates；
4. 证明 asymmetry `(q_A,q_B)!=(3,3)` 的 uniform tail barrier，而不是把有限搜索
   包装成 theorem。

完成这四步后，才可声称 `(3,6,3)` 在全部 four-symbol weighted-tree lattices中唯一
最优。它仍是 canonical local additive class的 sharp theorem，不是 arbitrary ordinary
dynamic AMQ 的 matching converse。
