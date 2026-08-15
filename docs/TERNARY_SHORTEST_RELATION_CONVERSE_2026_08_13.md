# Ternary lattice 的最短关系分叉

> 日期：2026-08-13。状态：最短关系与低层 composition injectivity 为解析
> theorem；(r\ge4) 的 optimistic frozen-tail half-error 排除由现有零依赖
> verifier给出严格可复算数值证据。这个结果把 ternary 全 converse缩小到最短
> relation mass (r\le3) 的有限结构分支，但尚未解析分类这些分支的全部 tails。

## 1. 模型与最短 balanced relation

令

\[
A_2=\{z\in\mathbb Z^3:z_0+z_1+z_2=0\},
\]

且 (L\le A_2) 是有限指数子格。load-(c) ternary compositions

\[
\mathcal C_c=\{m\in\mathbb N^3:|m|=c\}
\]

按 (m\sim m'iff m-m'\in L) 分成 syndrome states。定义

\[
r(L)=\min_{0\ne z\in L}|z^+|
=\min_{0\ne z\in L}|z^-|,
\tag{1}
\]

其中 (z=z^+-z^-)，(z^+,z^-\ge0) 且 supports disjoint。因为
(z\in A_2)，正负质量相等；本文的“relation mass”指其中任一侧的质量，
不是 \(\|z\|_1=2r\)。

## 2. 最短关系精确控制第一 collision layer

### Lemma 2.1（low-load injectivity）

若 \(c<r(L)\)，则 quotient map在 \(\mathcal C_c\) 上 injective。因此

\[
d_c:=|\mathcal C_c/L|
=|\mathcal C_c|
={c+2\choose2}.
\tag{2}
\]

反之，在 load (r=r(L)) 必有 collision：(z^+,z^-\in\mathcal C_r) 且
(z^+-z^-=z\in L)。所以 (r(L)) 正好是第一个可能发生 composition collision
的 load。

证明。若 (m,m'\in\mathcal C_c) collision，则 (z=m-m'\in L\setminus\{0\})。
令 (a=m\wedge m') 为 coordinatewise minimum。则

\[
z^+=m-a,\qquad z^-=m'-a,
\]

故

\[
|z^+|=|z^-|=c-|a|\le c<r(L),
\]

与式 (1) 矛盾。反向直接使用 (z^+,z^-)。

### Corollary 2.2（exact low-layer rejection）

对 (c<r(L))，syndrome确定完整 composition，minimal one-sided uniform
fresh-symbol rejection恰为

\[
\rho_c=\left(\frac23\right)^c.
\tag{3}
\]

特别地，(r(L)\ge4) 强迫 loads (0,1,2,3) 全部 composition-injective，而
不是仅仅 support-exact。

## 3. 对 (r\ge4) 最有利的 frozen-tail relaxation

translation (m\mapsto m+e_0) 将每个 load-(c) quotient class injectively映到
load-(c+1) quotient class；若两幅像相同，cancellation给原 classes相同。因此

\[
d_{c+1}\ge d_c.
\tag{4}
\]

结合 Lemma 2.1，对所有 (c\ge r) 都有

\[
d_c\ge d_{r-1}={r+1\choose2}.
\tag{5}

为了给该 lattice尽可能小的形式空间，定义 frozen-tail OGF

\[
\boxed{
A_r^{\rm fr}(z)
=\sum_{c=0}^{r-1}{c+2\choose2}z^c
+{r+1\choose2}\frac{z^r}{1-z}.
}
\tag{6}

真实 state OGF逐系数不小于式 (6)。

为了给它尽可能大的可承载 Poisson load，只使用低层被强迫的 rejection，并把
未知 tail rejection全部丢掉：

\[
J_r^{0}(\lambda)
=e^{-\lambda}\sum_{c=0}^{r-1}
\frac{\lambda^c}{c!}\left(\frac23\right)^c.
\tag{7}

令 \(\lambda_r\) 为 \(J_r^0(\lambda_r)=1/2\) 的唯一正根。这里把 tail
设为 zero 会减小 rejection，因此 \(\lambda_r\) 小于真实 half-error load；
它不适合作为逐个 lattice 的 lower bound。相反，composition-injective exact tail

\[
\rho_c=(2/3)^c\quad(c\ge0)
\tag{8}

给最大 universal one-sided rejection，half-error load为

\[
\lambda_\infty=3\ln2.
\tag{9}

把式 (6) 与这个不可能更有利的 load结合，得到 optimistic rate floor

\[
\boxed{
R_r^{\rm opt}
=\min_{0<z<1}
\left\{
\frac{1}{3\ln2}\log_2 A_r^{\rm fr}(z)-\log_2z
\right\}.
}
\tag{10}

重要 caveat：式 (10) 同时赠送“tail state不再增长”和“tail rejection仍保持
exact composition”两件通常不相容的好处，所以它是对 converse过度有利的
relaxation。只有当 (R_r^{\rm opt}) 已高于 benchmark 时，才能直接排除该分支。

## 4. 数值分叉与严格可用范围

复算式 (10) 得

\[
\begin{array}{c|c}
r&R_r^{\rm opt}\\\hline
4&2.295986679665\ldots\\
5&2.346301750907\ldots\\
6&2.367820007972\ldots\\
7&2.377144602390\ldots
\end{array}
\tag{11}

因此这个最乐观 relaxation本身只能无条件排除

\[
\boxed{r(L)\ge6.}
\tag{12}

它不能排除 (r=4,5)：这不是数值误差，而是 relaxation确实太宽。若误写成
“(r\ge4) 全部排除”，会越过式 (11) 的明确反例。

另一方面，使用真实 threshold relaxation——loads (c<r) exact、tail
rejection设为 zero、state tail冻结——其 rate为

\[
\widetilde R_r
=\min_{0<z<1}
\left\{\lambda_r^{-1}\log_2A_r^{\rm fr}(z)-\log_2z\right\}.
\tag{13}

数值为

\[
\widetilde R_4=2.376237800758\ldots,
\qquad
\widetilde R_5=2.368212594796\ldots.
\tag{14}

它们都高于 (2.349083440193\ldots)，但式 (13) 不是任意 lattice 的
lower bound，因为真实 tail若有正 rejection可增大 half-error load、降低 rate。
所以式 (14) 只能排除“first relation后直接 ALL-YES”的 threshold路线，不能排除
一般 (r=4,5) lattice。

## 5. 剩余最小结构问题

最短关系分叉把 ternary converse分成：

1. (r\ge6)：由式 (10)--(12) 的 optimistic relaxation排除；
2. (r=4,5)：必须证明 first relation的 translates造成定量 tail rejection loss，
   不能把式 (8) 的 exact tail与式 (6) 的 frozen states同时近似实现；
3. (r=2,3)：需要有限短关系类型分类。现有 load-two rigidity处理了 (r=2)
   的第一层现象，但尚未给完整 multi-layer rate theorem。

对 \(r=4,5\) 最精确的下一 lemma应是：若 \(z\in L\) 的 shortest mass为 \(r\)，
则 collision (z^+\sim z^-) 的所有 nonnegative translates在 loads
(r,r+1,\ldots) 中造成一个可显式求和的 weighted support-union penalty；该 penalty
应代入 Poisson rejection，而不是只用 Kneser或 entropy增长。

## 6. 对一般 clustering inequality 的裁决

单层 entropy/Shearer界最多给 syndrome entropy与平均 predecessor-degree的关系；
它看不到一条 shortest relation在后续所有 layers中的 translate packing。Kneser只
控制 \(|cV|\) 的 cardinality，也不记录每个 coset的 support union。式 (11) 的
(r=4,5) optimistic profiles正是二者共同留下的 gap。

因此当前最强解析 theorem是 Lemma 2.1 加 monotone tail count (5)；当前最强全率
裁决是 (r\ge6) 的排除。要完成 ternary (r\ge4) converse，必须新增 shortest-
relation translate clustering inequality；简单 entropy、Shearer或Kneser不能完成。
