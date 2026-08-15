# 固定误差 binary canonical dynamic filters：闭合结果与真实边界

> 日期：2026-08-13。本文合并 lattice normal form、跨 load 分类、global
> cardinality compensation、参数 compactness 与 permanent-YES masking。主结果是
> 一个全固定误差的精确变分刻画，以及在 \(\varepsilon=1/2\) 的显式 sharp
> theorem。它不是 arbitrary dynamic AMQ 的下界。

所有对数以 2 为底。记目标拒绝概率

\[
\delta=1-\varepsilon\in(0,1).
\]

## 1. 模型

公共随机标签先以概率 \(1-\beta\) 把 key 送入 permanent-YES 类；其余
\(\beta\) 质量均匀送入 \(B\) 个 blocks，并在 block 内取 binary symbol，
symbol 1 的概率为 \(p\)。每个 block 保存当前 binary composition 的
deterministic canonical key-only summary。允许：

- 不同 loads 共享 local state；
- lattice、bias、block 数和 mask 随 \(n\) 改变；
- query 读取全部 block states 与 exact global cardinality；
- 任意长合法 update history、zero false negatives、fixed worst-case memory；
- 对全部 block states 作联合 enumerative coding。

不允许额外的 history-dependent representations、randomized transition kernels，
或跨 blocks 的 noncanonical auxiliary quotient。普通 key API 下假设
\(|U_n|/n\to\infty\)，以保证一阶状态计数不把公共 hash 的空 fibers 当成可达状态。

## 2. Threshold 分支

order-\(q\) threshold quotient 的 local minimal-weight OGF 为

\[
A_q(z)=\frac{1-z^q}{(1-z)^2},\qquad q\ge2.
\tag{1}
\]

令一个 tracked block 的实际 Poisson load 为 \(\lambda\)。其条件拒绝率为

\[
J_{q,p}(\lambda)
=e^{-\lambda}\sum_{c=0}^{q-1}\frac{\lambda^c}{c!}
\left[p(1-p)^c+(1-p)p^c\right].
\tag{2}
\]

若 \(b=B/n\)，则 \(\lambda=\beta/b\)，总拒绝率为

\[
\delta=\beta J_{q,p}(\lambda)
=b\lambda J_{q,p}(\lambda).
\tag{3}
\]

fixed-state rate 是

\[
S_q(b)=\inf_{0<z<1}
\left\{b\log A_q(z)-\log z\right\}.
\tag{4}
\]

这里 mask 只改变一条固定 history 上的随机 load，不改变 fixed-state capacity：
对某张公共 tape，合法集合可能让全部 \(n\) 个 live keys 都落入 tracked region，
所以状态编码仍必须覆盖 total tracked load 至多 \(n\)，不能按 \(\beta n\) 计费。

它关于 \(b\) 严格递增。因此在给定 \((q,p)\) 后，问题等价于在可行约束

\[
J_{q,p}(\lambda)\ge\delta
\tag{5}
\]

下最大化每 block 拒绝效率 \(\lambda J_{q,p}(\lambda)\)。对应参数为

\[
b=\frac{\delta}{\lambda J_{q,p}(\lambda)},
\qquad
\beta=\frac{\delta}{J_{q,p}(\lambda)}\le1.
\tag{6}
\]

## 3. 全 fixed-error 变分闭包

定义

\[
\boxed{
R_{\rm th-mask}(\varepsilon)
=\inf_{\substack{q\in\{2,3,\ldots,\infty\},\ 0\le p\le1,\ \lambda>0\\
J_{q,p}(\lambda)\ge1-\varepsilon}}
S_q\!\left(
\frac{1-\varepsilon}{\lambda J_{q,p}(\lambda)}
\right).
}
\tag{7}
\]

式 (7) 在 \(q=\infty\) 处按极限解释：

\[
A_\infty(z)=\frac1{(1-z)^2},
\qquad
J_{\infty,p}(\lambda)
=p e^{-\lambda p}+(1-p)e^{-\lambda(1-p)}.
\tag{7f}
\]

coordinate lattice 的优化也可以显式完成。对

\[
L=\langle(a,0)\rangle
\]

有同一 OGF \(A_a\)，而 tracked rejection 为

\[
J_{\rm coord}(\lambda,p)=p e^{-\lambda p}.
\tag{7a}
\]

令 \(x=\lambda p\)。消去 mask 后，每 block 拒绝效率为 \(x e^{-x}\)。由
\(\beta=\delta e^x/p\le1\) 与 \(p\le1\)，可行性恰要求

\[
0<x\le\ln(1/\delta).
\]

所以

\[
x^*=\min\{1,\ln(1/\delta)\},
\qquad
b_{\rm coord}(\delta)=\frac{\delta}{x^*e^{-x^*}}.
\tag{7b}
\]

即

\[
b_{\rm coord}(\delta)=
\begin{cases}
1/\ln(1/\delta),&\delta\ge e^{-1},\\
e\delta,&\delta\le e^{-1}.
\end{cases}
\tag{7c}
\]

由于 \(A_a(z)\) 随 \(a\) 逐系数增加，coordinate family 的最优值由
\(a=1\)、\(A_1(z)=(1-z)^{-1}\) 达到。记

\[
R_{\rm coord}(\varepsilon)
=S_1(b_{\rm coord}(1-\varepsilon)).
\tag{7d}
\]

### Theorem 3.1

在 Section 1 的 homogeneous masked binary canonical product class 中，最优
一阶 fixed-state rate恰为

\[
\boxed{
R_{\rm can-bin}(\varepsilon)
=\min\{R_{\rm th-mask}(\varepsilon),R_{\rm coord}(\varepsilon)\}.
}
\tag{7e}
\]

证明由四部分组成。

1. Canonical cancellation 把每个 local summary 化为
   \(L\le\mathbb Z^2\) 的 lattice quotient。rank two 与同号 rank one 强迫
   ALL-YES；反号 rank one 被具有相同 OGF 的 threshold quotient 支配；
   coordinate rank one 由式 (7a)--(7d) 精确优化；rank zero exact composition
   是 threshold 的 \(q\to\infty\) 极限。
2. 式 (2)--(6) 消去 tracked mass 与 block density，给出 threshold branches；
   相应 quotient 与 mask 直接达到该值。
3. Donor compensation 说明 exact global cardinality 与读取其他 block cosets
   不会在一阶上改善 rejection。Chabauty/local compactness、vanishing-bias 和
   outer-density 边界论证允许 \(L_n,p_n,B_n\) 同时变化。
4. permanent-YES mask 只引入 \(\beta\)，所以不需要额外优化变量。

式 (7e) 是 homogeneous product-lattice class 的精确 characterization。它不等于
所有切换点都已有解析闭式：证明所有整数 \(q\) 分支只按相邻顺序切换、给出
uniform tail bound，以及判断 heterogeneous 多 block types 的 convexification
是否进一步改善，仍未闭合。

## 4. \(\varepsilon=1/2\) 的显式 sharp theorem

### Theorem 4.1

在 Section 1 的模型中，若 \(\varepsilon=1/2\)，则唯一非退化最优解（忽略
symbol 重命名和 quotient 同构）为

\[
q=3,\qquad p=\frac12,\qquad \beta=1,
\tag{8}
\]

并且

\[
\lambda=1.325819075285\ldots,
\qquad
\boxed{R_{\rm can-bin}(1/2)=2.349083440193\ldots.}
\tag{9}
\]

证明要点如下。

- \(q=2,3\) 的拒绝率由 \(p=1/2\) 唯一最大化，直接比较得 \(q=3\) 更优。
- 对所有 \(q\ge4\)，untruncated absence bound 与 \(\lambda<2\) 的凹性给
  \(\lambda<2\ln2\)，从而
  \[
  R_{q,p}>\mathcal R_4(2\ln2)
  =2.351275266054\ldots>2.349083440193\ldots.
  \]
- coordinate lattice 的 half-error rate 至少
  \(2.384499842479\ldots\)，其余跨-load lattices 由分类排除。
- 对任意 \((q,p)\)，在 \(J_{q,p}(\lambda)\ge1/2\) 的可行域中
  \(\lambda J_{q,p}(\lambda)\) 严格递增。因此 masked effective load
  \(2\lambda J\) 不超过 unmasked half-error root，等号仅在 \(\beta=1\)。
  所以 permanent-YES mask 严格无益。

## 5. Mask 相变为何在固定误差也重要

对固定 \((q,p)\)，令 \(\lambda^*_{q,p}\) 最大化
\(\lambda J_{q,p}(\lambda)\)，并记

\[
\delta^*_{q,p}=J_{q,p}(\lambda^*_{q,p}).
\tag{10}
\]

当 \(\delta>\delta^*_{q,p}\) 时，约束 (5) 卡紧，故 \(\beta=1\)；当
\(\delta<\delta^*_{q,p}\) 时，采用效率最大点并令 \(\beta<1\)。因此 mask
不是只在 \(\delta\downarrow0\) 才出现的技巧，而是在整个固定误差相图中产生
一个真正的 constrained/unconstrained 相变。

例如 uniform \(q=3\) 分支的数值为

\[
\lambda^*_3=1.716188659327\ldots,
\quad
\delta^*_3=0.400169593254\ldots,
\quad
\varepsilon^*_3=0.599830406746\ldots.
\tag{11}
\]

这些小数目前是高精度数值，不在没有 interval certificate 时充当解析常数。

## 6. 与 \(2.200611\) benchmark 的关系

式 (9) 与 heterogeneous fingerprint-multiset 的

\[
R_{\rm FM}(1/2)=2.20061148296\ldots
\tag{12}
\]

不矛盾。后者是 ordinary key-level 上界，允许 seed-independent polynomial
horizon 内以 \(n^{-d}\) 概率进入 sticky ALL-YES failure state；式 (9) 的构造
和 converse 针对 arbitrary-length、zero-overflow canonical quotient states。

因此正确比较是：

- 若允许 polynomial horizon 与极小 failure，式 (12) 是更好的已知上界；
- 若要求任意长 history、固定状态覆盖全部合法 updates 且无 overflow，式 (9)
  给出 binary canonical product 类的 sharp 答案；
- arbitrary ordinary dynamic AMQ 在 fixed error 下的 matching lower bound仍开放。

## 7. 不能外推的边界

式 (7)--(9) 不覆盖：

- \(K>2\) 的 lossy quotients；
- history-dependent multiple representations；
- randomized local transitions；
- 跨 blocks 的 noncanonical global state；
- arbitrary ordinary dynamic AMQs。

history dependence 不能通过免费 canonicalization 消除。co-representation
relation 虽然可平移、可沿共同 suffix cancellation，却不必传递；容量 2 的四状态
binary machine已经给出严格反例。即便逐边更新严格可逆，状态空间仍可形成带
non-Abelian holonomy 的 permutation cover。因此下一步必须研究 relational
fiber-cover entropy 或 approximate-transitivity，而不是继续假设 lattice normal
form 对一般 filters 无损成立。

## 8. 当前论文定位

已经闭合的是一个有清楚结构内容的 restricted-class package：

\[
\text{lattice normal form}
+\text{cross-load classification}
+\text{global compensation/compactness}
+\text{threshold fixed-error variational rate}.
\]

它足以形成 binary reversible-summary 论文的核心。若要达到解决 FOCS 2025
constant-error open direction的强度，仍需至少完成以下之一：

1. 对 \(K>2\) lossy quotients证明 matching sumset--distortion converse；
2. 对 history-dependent fiber covers证明新的线性 transition cost；
3. 给任意 ordinary filters 建立接近式 (12) 的 fixed-error lower bound；
4. 在 zero-failure、arbitrary-length 模型中构造显著低于式 (9) 的非canonical
   filter。
