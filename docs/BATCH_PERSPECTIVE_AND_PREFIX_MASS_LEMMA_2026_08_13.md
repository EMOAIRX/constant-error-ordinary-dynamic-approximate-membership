# Batch perspective 与 prefix-mass interface：reviewer-safe lemma

> 日期：2026-08-13。状态：严格 lemma。旧 endpoint cross-average 的
> `1.432309...n` 已撤回；本文闭合 exact batch code 到 first moments 的步骤，
> 以及 full-fiber prefix support 的 block-local first moment。合法的 endpoint
> convexification 见 `ENDPOINT_BATCH_CONVERSE_2026_08_13.md`。

所有对数以 2 为底。令一个 KLZ block 的大小为 `V`，hidden ordered distinct
batch 长度为 `m`，其中 `m->infinity` 且 `m/V->0`。

## 1. Abstract batch experiment

随机集合 `G subseteq [V]` 在 hidden batch `X` 之前产生。条件于生成 `G` 的
全部 side information，

\[
X=(X_1,\ldots,X_m)
\]

在 `[V]` 中均匀无放回。另有随机集合 `D subseteq [V]\setminus G`，允许 `D`
任意依赖 `X` 和后续 transcript。记

\[
g=|G|,\qquad d=|D|,
\qquad Q=|\{i:X_i\notin G\}|.
\tag{1}
\]

假设每个 miss value 都属于 `D`。由于 `X` distinct，合法 transcript 上必有

\[
Q\le d\le V-g.
\tag{2}
\]

令

\[
\bar q=\mathbb E Q,\qquad \alpha=\bar q/m.
\tag{3}
\]

### Lemma 1（batch perspective inequality）

采用约定 `(a)_0=1`，并在 `Q=0` 时把所有 `Q log(...)` 项定义为零，则

\[
\boxed{
\mathbb E\log
\frac{(d)_{\underline Q}}{(V-g)_{\underline Q}}
\le
m\alpha\log\frac{\mathbb E d/V}{\alpha}
+\log e.
}
\tag{4}
\]

若 `alpha=0`，右侧的 perspective 项按连续延拓定义为零，式 (4) 仍成立。
因此每 batch 的 fluctuation loss 是 `O(1)=o(m)`，而不是 `O(m)`。

这个 lemma 不要求：

- `D` 与 `X` 独立；
- `d` 条件于 `G` 集中；
- hit indicators 独立；
- `g,d,V-g` 远离零。

## 2. Lemma 1 的证明

写 `N=V-g`。由 (2)，对 `0<=i<Q`，

\[
\frac{d-i}{N-i}\le\frac dN.
\]

所以

\[
\log\frac{(d)_{\underline Q}}{N_{\underline Q}}
\le Q\log\frac dN.
\tag{5}
\]

在 `Q=0` 时两侧都是零；若 `Q>0`，(2) 保证 `d,N>0`。分解

\[
Q\log\frac dN
=Q\log\frac dQ+Q\log\frac QN.
\tag{6}
\]

函数

\[
(q,d)\longmapsto q\log(d/q)
\]

是 `log` 的 closed perspective，在 `q=0` 处取值零，并在可行锥
`0<=q<=d` 上联合凹。因此 Jensen 给

\[
\mathbb E\left[Q\log\frac dQ\right]
\le \bar q\log\frac{\mathbb E d}{\bar q}.
\tag{7}
\]

下面处理第二项。条件于 `G`，

\[
Q\sim\operatorname{Hypergeom}(V,N,m),
\qquad \mu=\mathbb E[Q\mid G]=mN/V.
\tag{8}
\]

若 `N=0`，则 `Q=0`，相应条件贡献为零。若 `N>0`，

\[
Q\log\frac QN
=Q\log\frac mV+Q\log\frac Q\mu.
\tag{9}
\]

用自然对数和 `ln x<=x-1`，

\[
\begin{aligned}
\mathbb E\left[Q\ln\frac Q\mu\mid G\right]
&\le
\mathbb E\left[Q\left(\frac Q\mu-1\right)\middle|G\right]\\
&=\frac{\operatorname{Var}(Q\mid G)}\mu\\
&=\left(1-\frac NV\right)\frac{V-m}{V-1}
\le1.
\end{aligned}
\tag{10}
\]

这里 `Q=0` 的项按 `0 ln 0=0` 解释。转回 base two 并对 `G` 平均，

\[
\mathbb E\left[Q\log\frac QN\right]
\le \bar q\log\frac mV+\log e.
\tag{11}
\]

合并 (5)、(7)、(11)：

\[
\begin{aligned}
\mathbb E\log\frac{(d)_{\underline Q}}{N_{\underline Q}}
&\le
\bar q\log\frac{\mathbb E d}{\bar q}
+\bar q\log\frac mV+\log e\\
&=m\alpha\log\frac{\mathbb E d/V}{\alpha}+\log e,
\end{aligned}
\]

即 (4)。注意整个证明中只有 `Q|G` 需要 hypergeometric；`D` 始终可以依赖
`X`。

## 3. Full-fiber corrected profile

固定 filter tape `R`。对物理状态 `m_0`、逻辑 load `t` 和 history length `q`
定义 partition-free full fiber union

\[
W_R(m_0,t,q)=
\bigcup\{S(h): |h|=q,\ |S(h)|=t,\ M_R(h)=m_0\}.
\tag{12}
\]

对 KLZ prefix state `G_j`，记

\[
g_j=\mathbb E|W(G_j)|.
\tag{13}
\]

令 `D_n` 是统一 common-suffix transport loss，并取

\[
\widehat g_j=g_j+jD_n,
\qquad
\widehat N=N+bD_n,
\qquad
x_j=\widehat g_j/\widehat N,
\tag{14}
\]

其中

\[
N=(1-\delta)n+\delta u.
\tag{15}
\]

参数选择保证

\[
bD_n=o(\delta u/4^b),
\qquad
\widehat N=\delta u(1+o(1)).
\tag{16}
\]

于是

\[
0\le x_0\le x_1\le\cdots\le x_b\le1.
\tag{17}
\]

## 4. Prefix support 的 removing-partition lemma

考虑 `Send(X_k,F_r,G_ell)`，其中 `ell<k`。令

\[
G=W(G_\ell)\cap U_k,
\qquad g=|G|.
\tag{18}
\]

### Lemma 2（block-local prefix mass）

在 KLZ/full-fiber 联合实验中，

\[
\boxed{
\frac{\mathbb E g}{V}
\le\delta x_\ell+o(4^{-b}).
}
\tag{19}
\]

更粗地写，右侧是 `delta x_ell+o(1)`。

### 正确的两阶段条件化

这里必须区分两个嵌套的 sigma-fields。不能在同一个条件化中既固定完整
partition，又把未暴露的 partition assignments 当作随机量。

对当前发送步写成 `P_{ell,k}^-`。它包含：

- filter tape `R` 和 tree shape；
- 生成 prefix state `G_ell` 所执行的全部 concrete labels、operations 和重复次数；
- 每个已暴露 label 所属的 level；
- 不包含完整 partition，也不包含 hidden rightmost batch `X_k`。

它还显式排除 `F_r`、difference set `D`、以及任何依赖 `X_k` 的 state、message
或 side information。等价地，只允许加入给定完整 partition 后与 `X_k` 条件独立
的 public variables。由于 `ell<k`，`sigma_{G_ell}` 在插入 rightmost `X_k` 前
结束；tree shape、filter tape、其他 rightmost batches和全部 non-rightmost edge
labels在给定 partition 后均与 `X_k` 独立。因此

\[
X_k\perp\!\!\!\perp\mathcal P_{\ell,k}^-\mid\pi.
\tag{19a}
\]

给定 `P_{ell,k}^-` 后，物理 state、load、exact time 都固定。因为 full fiber 的定义
只引用 concrete history、tape、load 和 time，而不引用 partition，

\[
W(G_\ell)
\]

是一个 fixed set。设已有 `L` 个 distinct labels 的 partition cells 被暴露，其中
`L_k` 个属于 `U_k`。在这些约束下，未暴露 keys 的 partition assignments仍为
均匀有限总体分配。正式理由是：对任一与已暴露 label--level constraints 相容的
balanced partition，每条 level-`j` edge 的 ordered `m`-tuple label具有相同条件
概率 `(V)_{underline m}^{-1}`。因此整个已观测 transcript 的 likelihood与具体
相容 partition无关，Bayes公式说明 partition posterior仍在所有相容 balanced
partitions上均匀。跨 edge 的 label重复不会改变这个常数；不同 levels 出现同一
label则是不相容的零概率事件。因此精确地有

\[
\begin{aligned}
\mathbb E[g\mid\mathcal P_{\ell,k}^-]
&=|W(G_\ell)\cap E_k|
+\frac{V-L_k}{u-L}|W(G_\ell)\setminus E|\\
&\le
L_k+\frac{V-L_k}{u-L}|W(G_\ell)|,
\end{aligned}
\tag{20}
\]

其中 `E` 是 partition cell 已暴露的 labels 集合，`E_k=E cap U_k`。第一行也明确
处理了 `W(G_ell)` 与已暴露 labels 的任意相关性。

取全期望，使用 `L,L_k<=nM^{b+1}/b` 的统一暴露界，得到

\[
\mathbb E g
\le
\frac Vu(1+o(4^{-b}))g_\ell+o(\delta V4^{-b}).
\tag{21}
\]

由 (14)--(16)，

\[
g_\ell\le\widehat g_\ell=x_\ell\widehat N
=x_\ell\delta u(1+o(4^{-b})),
\tag{22}
\]

代入 (21) 即得 (19)。

### 第二阶段：hidden batch 仍为 hypergeometric

令

\[
\mathcal P_{\ell,k}^+
=\mathcal P_{\ell,k}^-\vee\sigma(\pi),
\tag{22a}
\]

其中 `pi=(U_1,...,U_b)` 是完整 partition。给定 `P_{ell,k}^+` 后，`U_k` 以及

\[
G=W(G_\ell)\cap U_k
\]

都固定。KLZ 对 rightmost `X_k` 的抽样独立于 tree 中所有 non-rightmost
level-`k` labels；生成 `G_ell` 的 prefix 在插入 rightmost `X_k` 前结束。因此

\[
X_k\mid\mathcal P_{\ell,k}^+
\]

仍是 `U_k` 中均匀无放回的 ordered `m`-tuple，进而

\[
Q\mid\mathcal P_{\ell,k}^+
\sim\operatorname{Hypergeom}(V,V-|G|,m).
\tag{22b}
\]

这正好提供 Lemma 1 的 (8)。完整 partition只能在第二阶段加入；若把它提前放入
`P_{ell,k}^-`，式 (20) 的有限总体平均就不再合法。完整 non-rightmost public tree
labels若已由 decoder 知道，可在第一阶段连同其 level assignments一并加入；它们
只增加暴露集合 `E`，且由于与 rightmost `X_k` 独立，不改变 (22b)。

## 5. 与 difference first moment 的组合

full-fiber common-suffix transport 和 obfuscation coupling 独立给出

\[
\frac{\mathbb E d}{V}
\le\delta(x_r-x_\ell)+o(4^{-b}),
\tag{23}
\]

其中

\[
D=(W(F_r)\setminus W(G_\ell))\cap U_k.
\]

由 Lemma 2，

\[
\alpha=1-\mathbb E g/V
\ge1-\delta x_\ell-o(4^{-b}).
\tag{24}
\]

把 (23)--(24) 代入 Lemma 1，便得到 transition-profile batch functional。正式
finite-`b` 形式把 (23) 的 additive error 写入

\[
\Phi_{\delta,\gamma_b}(a,c)
=(1-\delta a)
\log\frac{1-\delta a}{\delta(c-a+\gamma_b)},
\qquad \gamma_b=O(4^{-b})+o(4^{-b}),
\tag{25}
\]

并在完成凸性论证后令 `gamma_b->0`。两个 endpoint pivots 分别在同一组内部
profile coordinates 上给出 `A_delta` 与 `B_delta` 的平均；分别应用 Jensen 后得到

\[
H\ge n\min_{0<x<1}\max\left\{
\log\frac1{\delta x},
(1-\delta x)\log\frac{1-\delta x}{\delta(1-x)}
\right\}-o(n).
\tag{26}
\]

在 `delta=1/2` 时，式 (26) 的常数为
`1.434406361243753...`。这不是已撤回的逐区间 cross-average；它允许 profile
存在任意 jumps。全部 pivots 的更强极值仍未解析闭合。
