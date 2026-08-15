# Full-fiber incidence graph 的 transport-or-information dichotomy

> 日期：2026-08-13。状态：Sections 2--5 是完整有限参数定理。它把 hard-union transport 的 birthday loss替换为一个 entropy-deficit会计，并将所需 universe regime 从该局部 lemma 的 \(u\gg n^2\) 降到 \(u\gg n\)。它尚未自动闭合完整 KLZ communication lower bound；最后仍需把相对 support loss 纳入 pivot rank functional。

所有 logarithms 以 2 为底。

## 1. Incidence-graph formulation

令

\[
\mu\in\mathcal P\!\left(\binom Un\right)
\]

是一个 state fiber 上的 source posterior。它不必在其 support 上均匀；这允许 history-dependent transducer 中不同 endpoint sets 具有不同 history multiplicities。

定义 bipartite incidence graph：

- 右侧 vertices 是 \(\operatorname{supp}\mu\) 中的 endpoint sets；
- 左侧 vertices 是
  \[
  W=\bigcup_{S\in\operatorname{supp}\mu}S,
  \qquad w=|W|;
  \]
- \(x\) 与 \(S\) 相邻当且仅当 \(x\in S\)。

先抽取 \(S\sim\mu\)，再从 \(U\setminus S\) 中均匀无放回抽取一个 \(q\)-set \(I\)。把所有与 \(I\) 相交的右侧 vertices 删除。给定观察值 \(I\)，surviving posterior 为

\[
\mu_I(T)
=
\frac{\mu(T)\mathbf 1[T\cap I=\varnothing]}
{Z(I)},
\qquad
Z(I)=\mu\{T:T\cap I=\varnothing\}.
\tag{1}
\]

令

\[
W_I=\bigcup_{T\in\operatorname{supp}\mu_I}T,
\qquad
L(I)=W\setminus W_I,
\qquad
\ell(I)=|L(I)|.
\tag{2}
\]

\(L(I)\) 正是“所有 witnesses 都与 suffix insertion set \(I\) 冲突”后失去的 left vertices。Shared witnesses、overlapping hyperedges 和 rare sections 都被这个定义原样允许。

## 2. 单 fiber 的精确 entropy dichotomy

定义 fiber 在自身 union 内的 entropy deficit

\[
\mathsf D_W(\mu)
=
\log\binom wn-H(\mu)
\ge0.
\tag{3}
\]

### Theorem 2.1（incidence transport-or-information）

若 \(u-n-q+1>0\)，则

\[
\boxed{
n\,\mathbb E_I
\log\frac{w}{w-\ell(I)}
\le
\mathsf D_W(\mu)+I(S;I).
}
\tag{4}
\]

此外，

\[
\boxed{
I(S;I)
\le
\Delta_{u,n,q}
:=
\log
\frac{\binom uq}{\binom{u-n}q}
\le
(\log e)\frac{nq}{u-n-q+1}.
}
\tag{5}
\]

因此

\[
\boxed{
n\,\mathbb E_I
\log\frac{w}{w-\ell(I)}
\le
\mathsf D_W(\mu)+\Delta_{u,n,q}.
}
\tag{6}
\]

这里 \(\ell=w\) 时左侧解释为 \(+\infty\)；这种情形只有在 survivor posterior 不存在时才可能发生，而实际 sampling 保证 \(S\cap I=\varnothing\)，所以 \(Z(I)>0\) 且 \(w-\ell\ge n\) almost surely。

### Proof

给定 \(I\)，surviving posterior \(\mu_I\) 支持在

\[
\binom{W_I}{n}.
\]

所以

\[
H(\mu_I)\le\log\binom{w-\ell(I)}n.
\tag{7}
\]

对 \(I\) 取期望，并使用

\[
I(S;I)=H(\mu)-\mathbb E_IH(\mu_I),
\tag{8}
\]

得到

\[
\begin{aligned}
\mathbb E_I\left[
\log\binom wn-\log\binom{w-\ell(I)}n
\right]
&\le
\log\binom wn-\mathbb E_IH(\mu_I)\\
&=
\mathsf D_W(\mu)+I(S;I).
\end{aligned}
\tag{9}
\]

另一方面，对任意 \(0\le\ell\le w-n\)，

\[
\begin{aligned}
\log\frac{\binom wn}{\binom{w-\ell}n}
&=
\sum_{j=0}^{n-1}
\log\frac{w-j}{w-\ell-j}\\
&\ge
n\log\frac{w}{w-\ell}.
\end{aligned}
\tag{10}
\]

式 (9)--(10) 给出 (4)。

最后，

\[
H(I\mid S)=\log\binom{u-n}q,
\qquad
H(I)\le\log\binom uq,
\]

所以得到 (5) 的第一项。第二项由

\[
\log\frac{\binom uq}{\binom{u-n}q}
=
\sum_{j=0}^{q-1}
\log\left(1+\frac{n}{u-n-j}\right)
\]

以及 \(\log_2(1+x)\le(\log_2e)x\) 得到。证毕。

## 3. 等价的线性与 tail 形式

由

\[
\log_2\frac1{1-z}\ge(\log_2e)z,
\qquad 0\le z<1,
\]

Theorem 2.1 推出

\[
\boxed{
\mathbb E\frac{\ell(I)}w
\le
\frac{\ln2}{n}
\left(
\mathsf D_W(\mu)+\Delta_{u,n,q}
\right).
}
\tag{11}
\]

对任意 \(\theta\in(0,1)\)，还得到

\[
\boxed{
\Pr[\ell(I)\ge\theta w]
\le
\frac{\mathsf D_W(\mu)+\Delta_{u,n,q}}
{n\log(1/(1-\theta))}.
}
\tag{12}
\]

所以严格的 dichotomy 是：

> 若一个随机 suffix 以显著概率删除 fiber union 的常数比例，则该 fiber 在自身 union 内必有 \(\Omega(n)\) entropy deficit，或 suffix 必携带 \(\Omega(n)\) source information。

当 \(q=o(u)\) 时，第二种可能只有 \(o(n)\)；此时 constant-fraction transport loss 必强迫 \(\mathsf D_W(\mu)=\Omega(n)\)。

### Corollary 3.1（uniform full fiber）

若 \(\mu\) 是任意非空 family

\[
\mathcal F\subseteq\binom Un
\]

上的 uniform distribution，则

\[
\boxed{
n\,\mathbb E
\log\frac{w}{w-\ell(I)}
\le
\log\frac{\binom wn}{|\mathcal F|}
+\Delta_{u,n,q}.
}
\tag{13}
\]

特别地，若对某个 \(\theta,\tau\in(0,1)\)，

\[
\Pr[\ell(I)\ge\theta w]\ge\tau,
\]

则

\[
\boxed{
\log|\mathcal F|
\le
\log\binom wn
-\tau n\log\frac1{1-\theta}
+\Delta_{u,n,q}.
}
\tag{14}
\]

这给出最直接的 transport-or-fiber-size dichotomy：常数概率的常数比例 union loss，强迫 full fiber 相对 \(\binom Wn\) 指数级变薄。

## 4. 全部 state fibers 的 single-budget 版本

令 \(S\) 在 \(\binom Un\) 中均匀，\(R\) 是独立 filter tape，\(M=M_R(S)\) 是某个 endpoint 的 \(H\)-bit physical state。这里可以先固定一条生成 \(S\) 的 source history convention；history dependence 只会改变 posterior weights，不影响下面结论。

条件于 \((R,M)=(r,m)\)，令 posterior 为 \(\mu_{r,m}\)，其 union size 为 \(w_{r,m}\)。定义

\[
\mathsf A(w)
=
\log\frac{\binom un}{\binom wn}.
\tag{15}
\]

### Theorem 4.1（global excess-information budget）

对每个 state posterior 独立执行 Section 1 的 random suffix experiment，有

\[
\boxed{
n\,\mathbb E
\log\frac{W}{W-L}
\le
I(S;M\mid R)
-\mathbb E\mathsf A(W)
+\Delta_{u,n,q}.
}
\tag{16}
\]

特别地，

\[
\boxed{
n\,\mathbb E
\log\frac{W}{W-L}
\le
H-\mathbb E\mathsf A(W)
+\Delta_{u,n,q}.
}
\tag{17}
\]

### Proof

对每个 \((r,m)\)，有精确分解

\[
\begin{aligned}
\log\binom un-H(\mu_{r,m})
&=
\log\frac{\binom un}{\binom{w_{r,m}}n}
+
\left[
\log\binom{w_{r,m}}n-H(\mu_{r,m})
\right]\\
&=
\mathsf A(w_{r,m})
+\mathsf D_{W_{r,m}}(\mu_{r,m}).
\end{aligned}
\tag{18}
\]

对 \((R,M)\) 平均，左侧为

\[
I(S;M\mid R),
\]

故

\[
\mathbb E\mathsf D_W(\mu)
=
I(S;M\mid R)-\mathbb E\mathsf A(W).
\tag{19}
\]

平均使用 Theorem 2.1 即得 (16)。由于 \(M\) 至多 \(H\) bits，

\[
I(S;M\mid R)\le H,
\]

得到 (17)。证毕。

式 (16) 是所需的 single-budget accounting：所有 fibers 的 transport loss 共同使用同一个 \(I(S;M\mid R)\le H\)，不能逐 state 或逐 witness 重复收费。

## 5. 加入 one-sided FPR 后的静态基线

令 \(A_R(M)\) 是物理状态的 YES-set。Source-fiber union 满足

\[
W_R(M)\subseteq A_R(M)
\tag{20}
\]

by zero false negatives。

对均匀随机 source set \(S\) 平均每个 fixed history/key 的 pointwise FPR，有

\[
\mathbb E|A_R(M)|
\le
n+\varepsilon(u-n)
=:\bar a.
\tag{21}
\]

将 \(\log\binom an\) 用 gamma function延拓到实数 \(a\ge n\)。函数

\[
\mathsf A(a)=
\log\binom un-\log\binom an
\]

在 \(a\ge n\) 上递减且凸。确实，

\[
\frac{d^2}{da^2}\left[-\log\binom an\right]
=
\frac1{\ln2}\sum_{j=0}^{n-1}\frac1{(a-j)^2}>0.
\]

由 \(W\le|A_R(M)|\)、Jensen 及 (21)，

\[
\mathbb E\mathsf A(W)
\ge
\mathsf A(\bar a).
\tag{22}
\]

代入 (17)：

\[
\boxed{
n\,\mathbb E
\log\frac{W}{W-L}
\le
H-
\log\frac{\binom un}
{\binom{n+\varepsilon(u-n)}n}
+\Delta_{u,n,q}.
}
\tag{23}
\]

右侧第一、二项之差正是 state information 超过 Carter accepted-support baseline 的部分。Rare-witness poisoning不能免费扩大 transport loss：它要么扩大 accepted support并消耗 pointwise FPR，要么缩小 posterior entropy并出现在这个 excess-information budget 中。

若

\[
\frac un\to\infty,
\qquad
q=o(u),
\]

则

\[
\Delta_{u,n,q}=o(n).
\tag{24}
\]

因此，在仅比 static accepted-support lower bound 多 \(o(n)\) bits 的结构中，

\[
\mathbb E\log\frac{W}{W-L}=o(1),
\qquad
\mathbb E\frac LW=o(1).
\tag{25}
\]

这就是局部 transport lemma 层面从 \(u\gg n^2\) 到 \(u\gg n\) 的严格改进。

## 6. 为什么 fractional matching / transversal 不是正确主变量

对每个 \(x\in W\)，lost event 是 \(I\) 成为 section

\[
\mathcal F_x=\{S\in\operatorname{supp}\mu:x\in S\}
\]

的 transversal。Fractional matching number可以逐 \(x\) 上界该事件，但无法把不同 \(x\) 的费用相加：

- 一个 shared witness set 可同时让 \(n\) 个 left vertices 消失；
- rare sections 的 posterior mass可趋零但数量可很大；
- global masks 可让所有 sections 的 events完全相关。

Theorem 2.1 不逐 left vertex收费。它只观察 pruning 后整个 posterior 的支持宇宙从 \(w\) 缩到 \(w-\ell\)，再用 entropy upper bound

\[
H(\mu_I)\le\log\binom{w-\ell}n.
\]

这自动容纳 shared witnesses 和任意 dependence。因此 Shearer/fractional-transversal 可作为特定 fiber 的强化，但不应作为 ordinary-model 主会计。

## 7. Hostile examples

### 7.1 Rare-witness poisoning

取一个大 core \(A\subset W\)，把 \(\binom An\) 作为主 family，再加入少量覆盖 \(W\setminus A\) 的 isolated witness sets。Posterior mass几乎全部在主 family上，但随机 \(I\) 可一次删除许多 isolated witnesses。

Hard union只看到大量 lost keys。Theorem 2.1 同时看到

\[
\mathsf D_W(\mu)
\approx
\log\binom wn-\log\binom{|A|}n,
\]

所以这些 keys 不是免费 poison；其支持宇宙扩张已产生相应 entropy deficit。

### 7.2 Shared witness

若一个 rare \(n\)-set 同时是其 \(n\) 个 keys 的唯一 witness，\(I\) 击中该 set 时会一次丢失 \(n\) 个 keys。式 (9) 直接把 surviving support universe 缩小 \(n\)，不作错误的逐 key independence假设。

### 7.3 Global ALL-YES coin

在 ALL-YES branch，若 posterior 是完整 \(\binom Un\)，则 \(W=U\) 且任意合法 \(I\) 后仍有 \(W_I=U\)，所以 \(L=0\)。Global correlation 不制造虚假的 transport charge。

### 7.4 Exact dictionary

给定 exact endpoint state，posterior 是 point mass，\(W=S\)。所有合法 suffix insertions均与 \(S\) disjoint，故 \(L=0\)。其巨大 state cost体现在

\[
\mathsf A(W)=\log\binom un,
\qquad
\mathsf D_W=0,
\]

而不是被 transport functional重复收费。

### 7.5 Random additive-syndrome fibers

Approximate-design fibers可使 fixed-degree Johnson marginals几乎 uniform，但 Theorem 2.1 不依赖 low-degree spectrum。若一个 suffix 真正使 union缩小常数比例，则 conditional support entropy必下降 \(\Omega(n)\)；若 syndrome fiber 在 suffix noise 下稳定，则 \(L/W=o(1)\)。这与高阶信息隐藏反例兼容。

## 8. 与 ordinary transition 的连接

固定随机带和一个 physical state \(m\)。若一个 concrete self-contained suffix 的 distinct insertion set 是 \(I\)，则对每个满足 \(T\cap I=\varnothing\) 的 endpoint witness \(T\)，该 suffix 对 \(T\) 合法。Fixed-tape determinism使所有这些 witness histories从同一个 \(m\) 到达同一个 successor state；zero false negatives于是保证 successor YES-set包含 \(W_I\)。

所以 ordinary full-fiber transport 的实际 union loss不超过 Sections 1--4 定义的 \(\ell(I)\)。定理没有把 suffix legality当作概率事件，也没有选择依赖 \(I\) 的 witness。

## 9. 对完整 lower bound 的剩余缺口

式 (23) 已经严格解决“random suffix 是否能在 \(u\gg n\) 下稳定 transport source-fiber union”的局部问题，但它不能被直接替换进现有 hard-rank proof：

1. KLZ rank code 使用 candidate-set 的绝对大小；式 (23) 控制相对 log-shrinkage
   \[
   \log(W/(W-L)).
   \]
2. 右侧含 \(H-\mathsf A(\bar a)\)。完整 proof 必须把它作为同一个 state message 的已用 budget，而不是在每个 pivot重复支付。
3. Obfuscating tree 中 suffix 有 partition profile；需使用 profile-conditioned version。相同证明逐 block成立，额外 profile entropy至多 \(b\log(n+1)\)，但必须与所有 pivots联合核算。
4. Source-fiber union只包含当前 communication source可达 endpoints。对 common suffix transport这是足够的；若某个 decoder step需要所有 operational histories 的 hard full fiber，则必须重写 candidate code，不能静默替换。

因此当前准确结论是：

> \(u\gg n^2\) 不是 posterior-incidence transport 的内生 barrier；Theorem 4.1--(23) 在 \(u\gg n\) 下给出严格的 transport-or-information dichotomy。尚未证明的是一个 all-pivot communication inequality，能够一次性扣除 static support information并只对 excess information收费。

这是下一步应解决的唯一接口。若成功，现有 endpoint/all-pivot variational常数可望在 \(u/n\to\infty\) 下成立；若失败，反例必须展示一种在同一 \(H\)-bit final state中重复利用 excess-information budget跨多个 pivots的 ordinary dynamic mechanism。
