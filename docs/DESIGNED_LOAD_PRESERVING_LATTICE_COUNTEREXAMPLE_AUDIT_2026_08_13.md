# Designed load-preserving lattices：反例搜索与最接近候选

> 日期：2026-08-13。状态：construction interface 与每个具体 quotient 的 profile
> 公式是严格的；有限群枚举和 rate 比较是 candidate search，不是全 lattice
> converse。搜索目标是在 ordinary block-product construction 中严格击败 binary
> order-three 的 \(2.349083440193\ldots\) bits/key。本轮没有找到反例。

## 1. 可张量化模型

取有限 Abelian group \(G\) 和不同 increments

\[
V=\{v_1,\ldots,v_K\}\subseteq G.
\tag{1}
\]

每个 outer block保存 exact load \(c\) 与 syndrome

\[
s=\sum_{x\text{ in block}}v_{h(x)}.
\tag{2}
\]

insert/delete分别加减对应 increment，所以 construction支持任意长合法 histories，
没有 overflow、rebuild 或 history horizon。固定 load的 composition lattice是

\[
L=\left\{a\in A_{K-1}:\sum_i a_iv_i=0\right\},
\tag{3}
\]

故确为 load-preserving \(L\le A_{K-1}\)。相同 \((G,V)\) 必须同时生成全部
occupancy layers；不能逐层挑选不相容的 state/rejection profile。

定义

\[
cV=\{v_{i_1}+\cdots+v_{i_c}\},\qquad d_c=|cV|.
\tag{4}
\]

对 uniform inner symbols，令 \(S_c=X_1+\cdots+X_c\)。minimal one-sided query
的 load-\(c\) rejection是

\[
\rho_c
=\Pr[S_c-v_A\notin(c-1)V],
\tag{5}
\]

其中 \(A,X_1,\ldots,X_c\) IID uniform于 \(V\)。式 (5)也可由 composition
coset的 support union精确计算；两种算法交叉核对可避免负坐标 reduction错误。

令

\[
J(\lambda)=e^{-\lambda}\sum_{c\ge0}\frac{\lambda^c}{c!}\rho_c.
\tag{6}
\]

half-error calibration取唯一正根 \(J(\lambda)=1/2\)。local OGF为

\[
A(z)=\sum_{c\ge0}d_cz^c.
\tag{7}
\]

在 homogeneous block product与总 load joint enumeration 中，rate为

\[
R(G,V)=\inf_{0<z<1}
\left\{\frac1\lambda\log_2A(z)-\log_2z\right\}.
\tag{8}
\]

因此每个搜索结果都是一个真正可张量化、任意长 dynamic upper bound；唯一非严格
部分是浮点求根/优化及“有限搜索没有反例”不能外推成无限 family theorem。

## 2. 搜索范围与核验

本轮复用了 cyclic Cayley enumerator，并新增
`scripts/search_finite_abelian_cayley_quotients.py`。新程序：

1. 枚举 invariant-factor finite Abelian groups；
2. 只保留生成全群的 \(V\)，消除不可达 ambient states；
3. 用 integer random-walk multiplicities精确计算每层 rejection numerator；
4. 枚举 sumsets直到首次稳定，此后 \(d_c\) 常数且 \(\rho_c=0\)；
5. 最后才用浮点二分解式 (6) 与式 (8)。

已覆盖的主要范围是：

- cyclic groups：ternary到 order 60，quaternary到 order 45；
- noncyclic invariant-factor groups：ternary到 group order 48；
- quaternary noncyclic到 group order 28；
- rank至多 3，尤其包括 \(\mathbb Z_a\times\mathbb Z_b\) 中大量 short-circuit
  configurations。

这个范围远非全部 finite Abelian quotients，也没有 interval certificate。因此
“没有更优候选”只能作为方向审计证据。

## 3. 最接近候选

除 binary \(G=\mathbb Z_3,V=\{0,1\}\) 本身外，最佳 genuine multi-symbol
quotient仍是

\[
\boxed{G=\mathbb Z_{12},\qquad V=\{0,1,4\}.}
\tag{9}
\]

它由两个短 same-load relations主导：

\[
3(4-0)=0,
\qquad
4(1-0)=4-0
\quad\text{in }\mathbb Z_{12},
\tag{10}
\]

即 composition lattice含三支持以内的低 \(\ell_1\)-norm circuits。其精确 profile
是

\[
d=(1,3,6,9,11,12,12,\ldots),
\tag{11}
\]

\[
\rho=
\left(
1,\frac23,\frac49,\frac{22}{81},
\frac{31}{243},\frac{31}{729},0,\ldots
\right).
\tag{12}
\]

其中 load 3的首次 collision是 pure compositions \((3,0,0)\) 与
\((0,0,3)\)；它只损失一小部分 rejection，同时把十个 compositions压到九个
states。随后 translates令 \(d_4=11,d_5=12\)，并逐步把 support unions扩张到
全 alphabet。

浮点校准给

\[
\lambda=1.990055161899\ldots,
\qquad
z_*=0.451195618750\ldots,
\tag{13}
\]

以及

\[
\boxed{R=2.352584133736\ldots.}
\tag{14}
\]

它比 binary baseline高

\[
0.003500693543\ldots\text{ bits/key}.
\tag{15}
\]

这是目前真正值得继续分析的唯一近邻，而不是一个反例。

最佳 noncyclic ternary候选出现在 \(\mathbb Z_2\times\mathbb Z_8\)，典型
increments为

\[
V=\{(0,0),(0,1),(1,2)\},
\]

其 rate为 \(2.362650874722\ldots\)。最佳已搜 quaternary cyclic候选在
\(\mathbb Z_{30}\) 中，rate为 \(2.361935125137\ldots\)；最佳已搜 noncyclic
quaternary rate为 \(2.364787352612\ldots\)。它们均明显更差。

## 4. 系统 barrier

搜索结果揭示的不是简单的“大 alphabet 总是更差”，而是一个短 circuit 的两面性。
设 \(a\in L\setminus\{0\}\)，写成正负部分

\[
a=a^+-a^-,
\qquad |a^+|=|a^-|=r.
\tag{16}
\]

它在 load \(r\) 首次合并两个 compositions，能减少 \(d_r\)。但同一个 relation
的全部 nonnegative translates

\[
a^++t\sim a^-+t
\tag{17}
\]

会在每个更高 layer同时出现。若两端 supports不同，式 (17)迫使每个相应 coset
接受 support union；因此 state saving与 rejection loss无法独立调节。

两个极端都已知失败：

- circuit很短且大量重叠时，sumset很快饱和，但 query states也迅速 ALL-YES；
- circuit很长或很稀疏时，低 occupancy rejection接近 exact composition，然而
  \(d_c\) 在 Poisson质量集中的 layers几乎保持完整 simplex growth。

\(\mathbb Z_{12},\{0,1,4\}\) 正处于二者之间：首次 collision直到 load 3，且
前几次 translate的 support-union损失较温和。这解释了它为何接近 baseline，也
定位了反例若存在必须改善的量：

> 在保持 \(\rho_3,\rho_4,\rho_5\) 接近式 (12) 的同时，把
> \((d_3,d_4,d_5)=(9,11,12)\) 至少再降低一个 weighted state，或在相同 state
> profile上提高 tail rejection。

非循环 torsion在已搜范围没有做到这一点；它通常把 saturation order提高到 16、
20或更大，额外 tail rejection不足以抵消 OGF增长。

## 5. 下一条可发表的 theorem 应是什么

继续扩大 brute-force modulus的论文价值有限。围绕候选 (9)，更有 taste 的目标是
一个 **short-circuit translate inequality**：对 ternary finite-index
\(L\le A_2\)，由最短 relation \(a\) 的 support型和 \(\ell_1\)-长度，联合下界

\[
\sum_c d_cz^c
\quad\text{并上界}\quad
e^{-\lambda}\sum_c\frac{\lambda^c}{c!}\rho_c.
\tag{18}
\]

理想的 sharp theorem应证明：对 half-error saddle相关窗口，所有 ternary
lattices满足

\[
R(L)\ge R(\mathbb Z_{12},\{0,1,4\})
>R(\mathbb Z_3,\{0,1\}),
\tag{19}
\]

并分类式 (9) 的 equality orbit。即使最终只闭合 ternary class，这也是一个真正的
multi-layer weighted lattice-coset clustering theorem；它比继续列举 finite
quotients更可能成为论文结果。

目前式 (19)尚未证明。第二层五点定理只控制 \((d_2,\rho_2)\)，无法排除从 load
3才出现的候选 (9)。第一个未证步骤正是：把一个 load-3 circuit的 translate
packing及 support-union损失，在所有 Poisson-relevant layers中不重不漏地收费。

## 6. 裁决

本轮没有找到低于 \(2.349083440193\ldots\) 的 designed load-preserving lattice。
最接近的 genuine候选是式 (9)，差距仅 \(0.00350069\) bits/key，足够近，值得作为
结构定理的 extremal target；但有限搜索不能证明它在全部 ternary lattices中最优。

因此这条路线当前更适合作为 converse/stability论文，而不是反例 construction：
核心问题已经缩小为 short circuits 的 translate growth与 weighted support-union
distortion之间的 sharp多层不等式。
