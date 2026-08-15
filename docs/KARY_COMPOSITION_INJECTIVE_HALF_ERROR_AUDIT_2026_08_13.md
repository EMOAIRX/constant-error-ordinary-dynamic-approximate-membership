# K-ary composition-injective quotients 在 half error 的严格审计

> 日期：2026-08-13。目标：检验多符号、低负载精确 composition、高负载
> quotient 的路线能否在 \(\varepsilon=1/2\) 显著优于 binary \(q=3\) 的
> \(2.349083440193\ldots\) bits/key。结论是否定的：在一个对该路线过度有利的
> 群大小下界 relaxation 中，所有已计算的 \(2\le K,q\le100\) 仍由
> \((K,q)=(2,3)\) 唯一最优；真实有限群构造只会使用更多状态。

本文区分严格解析结论与数值认证。不能把有限网格计算误称为全部整数参数的
解析定理。

## 1. 候选构造

每个 tracked key 均匀选择：

- outer block \(j\in[B]\)；
- inner symbol \(a\in[K]\)。

第 \(j\) 个 block 保存 exact load \(c_j\) 和 additive syndrome

\[
s_j=\sum_{x\text{ in block }j}v_{h(x)}\in G,
\tag{1}
\]

其中 \(V=\{v_1,\ldots,v_K\}\subseteq G\)，\(G\) 是有限 Abelian group。
固定 threshold \(q\ge2\)，要求对每个 \(c<q\)，map

\[
(m_1,\ldots,m_K)\longmapsto\sum_am_av_a,
\qquad m_a\ge0,quad\sum_am_a=c,
\tag{2}
\]

是 injective。因此低负载时可以恢复完整 symbol composition；高负载时本路线
保守地全部回答 `YES`。群 residue 仍随 updates 可逆变化，所以删除降回
\(c<q\) 时恢复精确 composition。

这相当于在有限群中要求一个 order-\((q-1)\) 的 generalized Sidon set。随机
cyclic embedding 可给存在性，但通常需要远大于信息论最小值的群；因此首先应在
最乐观的最小状态 relaxation 中判断路线是否有希望。

## 2. 精确 rejection 公式

若一个 block 的 Poisson mean load 为 \(\lambda=n/B\)，条件于 load \(c<q\)，
fresh query symbol 在 composition 中缺席的概率是

\[
\left(1-\frac1K\right)^c.
\]

所以渐近拒绝概率为

\[
\boxed{
J_{K,q}(\lambda)
=e^{-\lambda}\sum_{c=0}^{q-1}
\frac{\lambda^c}{c!}\left(1-\frac1K\right)^c.
}
\tag{3}
\]

它严格随 \(\lambda\) 下降。令 \(\lambda_{K,q}\) 为唯一满足

\[
J_{K,q}(\lambda_{K,q})=\frac12
\tag{4}
\]

的正根；达到 half-error 时 block density 是

\[
b=\frac Bn=\frac1{\lambda_{K,q}}.
\tag{5}

当 \(q\to\infty\) 时，式 (3) 变成

\[
e^{-\lambda/K},
\]

故最大可能 load 只趋于 \(K\ln2\)。增加 alphabet 确实线性增加单 block 可承载
load，但接下来会看到 composition-state 数也相应增长。

## 3. 对任何 finite-group realization 都成立的状态下界

在计数前先关闭一个看似可能的逃逸方向：低负载只恢复 symbol support，而不恢复
multiplicity composition。

### Lemma 3.1（exact support 强迫 composition injectivity）

设一个 deterministic canonical key-only summary 保持 exact load，并允许合法
insert/delete。若对所有 load \(c<q\) 的状态，minimal one-sided query 没有
false positive，即能精确恢复 support，那么 summary 在每个 \(c<q\) layer 上
必须对全部 compositions injective。

**证明。** 由 canonical cancellation/lattice normal form，若两个不同的同负载
compositions \(x\ne y\) 被合并，则 \(d=x-y\) 属于 equivalence lattice。
令 \(m_i=\min(x_i,y_i)\)，并共同删除 composition \(m\)。合法 deletion 的
cancellation 给

\[
x':=x-m\sim y':=y-m.
\]

两者仍有相同 load，且该 load 不超过原来的 \(c<q\)；同时
\(\operatorname{supp}(x')\cap\operatorname{supp}(y')=\varnothing\)，并且因为
\(x\ne y\)，二者非空。于是同一个物理状态同时兼容两个不同且互不相交的
supports。minimal zero-FN query 必须接受两个 supports 的 union，因此对任一个
真实 composition 都产生 false positive，与 exact-support 假设矛盾。\(\square\)

所以，在 canonical deletion 语义下，“低负载 exact support quotient”并不比
“低负载 exact composition”更便宜。若想绕开后面的 composition-state barrier，
必须允许 threshold 以下也有受控 false positives、跨 load merge、history
dependence，或其他不满足该引理前提的机制。

load \(c\) 的 compositions 数是

\[
N_{K,c}={c+K-1\choose K-1}.
\tag{6}

由式 (2)，对 \(c<q\) 必有

\[
|cV|=N_{K,c}.
\tag{7}

此外，任选 \(v\in V\)，translation \(x\mapsto x+v\) 把 \(cV\) injectively
映入 \((c+1)V\)，所以 \(|cV|\) 随 \(c\) 不减。因而对所有 \(c\ge q-1\)，

\[
|cV|\ge N_{K,q-1}.
\tag{8}

这给出任何真实 finite-group construction 的 local-state OGF 下界

\[
\boxed{
A_{K,q}^{\rm opt}(z)
=\sum_{c=0}^{q-2}N_{K,c}z^c
+N_{K,q-1}\frac{z^{q-1}}{1-z}.
}
\tag{9}

为与 threshold convention 对齐，也可把 exact layers 写到 \(c<q\)：此时

\[
\widetilde A_{K,q}^{\rm opt}(z)
=\sum_{c=0}^{q-1}N_{K,c}z^c
+N_{K,q-1}\frac{z^q}{1-z}.
\tag{10}

式 (10) 故意假设所有 high-load layers 只需 \(N_{K,q-1}\) 个 states。真实
sumsets \(|cV|\) 可能继续增长，且 group order 也可能远大于该数；所以它是对
候选路线最有利的 relaxation，而不是已实现的 upper bound。

在 exact-total-load、blockwise enumerative coding 下，任意此类构造的渐近率至少为

\[
\boxed{
R^{\rm relax}_{K,q}
=\min_{0<z<1}
\left\{
\frac1{\lambda_{K,q}}\log_2\widetilde A_{K,q}^{\rm opt}(z)
-\log_2z
\right\}.
}
\tag{11}

这是标准 positive-coefficient OGF saddle bound。任何具体 \((G,V)\) 的 OGF
逐系数不小于式 (10)，所以其 rate 不小于式 (11)。

## 4. Half-error 数值结果

对每个整数 \(2\le K,q\le100\)，我们用 monotone bisection 解式 (4)，再对
\(y=\ln z\in(-\infty,0)\) 作一维凸优化。最小的若干 relaxation rates 是：

| \(K\) | \(q\) | \(\lambda_{K,q}\) | \(R^{\rm relax}_{K,q}\) |
|---:|---:|---:|---:|
| 2 | 3 | 1.3258190753 | 2.3490834402 |
| 2 | 4 | 1.3754412465 | 2.3602958587 |
| 3 | 5 | 2.0409299384 | 2.3682125948 |
| 2 | 2 | 1.1461932206 | 2.3720575415 |
| 3 | 6 | 2.0704612395 | 2.3727433120 |
| 2 | 5 | 1.3847969144 | 2.3728359287 |
| 4 | 7 | 2.7511489303 | 2.3761302065 |
| 3 | 4 | 1.9477544954 | 2.3762378008 |

零外部依赖的复算程序见
`scripts/verify_kary_composition_half_error.py`。它打印整个网格中最小的十项；这里的
浮点计算是路线审计证据，不是 interval-arithmetic certificate。

因此：

1. 在审计范围内，唯一最佳仍是 binary \((K,q)=(2,3)\)。
2. 最好的 genuine ternary 候选已经是 \(2.36821\ldots\)，比 binary 差约
   \(0.01913\) bits/key。
3. 这是在把 high-load group states 压到信息论不可能再低的
   \(N_{K,q-1}\) 后的数值；真实 Sidon embedding 只会更差。
4. 因而该路线没有逼近 \(2.200611\) 的迹象，甚至不能击败 \(2.349083\)。

这里最关键的 hostile check 是 threshold indexing。若 \(c<q\) 精确，则最后一个
精确 layer 是 \(q-1\)，high-load tail 从 \(q\) 开始，并至少有
\(N_{K,q-1}\) states；式 (10) 正是这个 convention。若误把 tail state count
写成更小的 \(N_{K,q-2}\)，会制造虚假的改进。

## 5. 随机 cyclic embedding 为什么不能挽救路线

令

\[
\mathcal C=\bigcup_{c=0}^{q-1}
\{m\in\mathbb N^K:|m|=c\}.
\]

若把 \(v_1,\ldots,v_K\) 独立均匀放入 \(\mathbb Z_P\)，对两个不同、同 load
的 compositions \(m,m'\)，只要 \(P\) 不整除差向量的所有非零 coefficients，
collision probability 至多约 \(1/P\)。对所有 pairs 作 union bound，粗略需要

\[
P\gtrsim |\mathcal C|^2.
\tag{12}

这比式 (10) 赠送的 \(P=N_{K,q-1}\) 至少多一个平方级损失。更精细的
generalized Sidon constructions 可改善存在性常数或指数前因子，但不可能突破
由 injectivity 本身强迫的 \(|G|\ge N_{K,q-1}\)。由于连这个不可能更优的下界
relaxation 都没有击败 binary，优化 embedding 无法逆转结论。

式 (12) 还需注意 composite modulus 的 arithmetic：若 coefficient difference
与 \(P\) 不互素，collision probability 不一定恰为 \(1/P\)。选择足够大的素数
\(P>q\) 可避免这个问题。这个细节只影响 existence upper bound，不影响式
(9)--(11) 的 converse。

## 6. 能严格宣称什么

目前可以严格宣称：

> 对任意固定 \((K,q)\)，任何在所有 loads \(c<q\) 精确恢复 uniform
> \(K\)-symbol composition、并在 high loads 使用 additive finite-group
> syndrome 的 blockwise canonical filter，其 half-error rate 不低于式 (11)。

并且可以带 verifier 地宣称：

> 对所有 \(2\le K,q\le100\)，式 (11) 的唯一最小值由
> \((K,q)=(2,3)\) 取得，值为 \(2.349083440193\ldots\)。

还不能只凭这次计算宣称：

> 对全部无界整数 \(K,q\)，binary \((2,3)\) 解析全局最优。

要升级为无限参数 theorem，需要补一个 tail lower bound。例如证明对充分大的
\(K\) 或 \(q\)，式 (11) 统一大于 \(2.35\)。这看起来可行，因为当 exact
threshold 很高时，composition OGF 趋近

\[
\sum_{c\ge0}{c+K-1\choose K-1}z^c=(1-z)^{-K},
\]

配合 \(\lambda\to K\ln2\) 恢复 exact-composition baseline
\(2.384499842\ldots\)，但尚未把 convergence 写成足够 sharp 的显式界。

## 7. 研究裁决

K-ary composition-injective quotient 是一个合理但错误的突破方向。它清楚揭示了
失败机制：

\[
\underbrace{\lambda\text{ 随 }K\text{ 增长}}_{\text{每 block 拒绝效率提高}}
\quad\text{恰被}\quad
\underbrace{{c+K-1\choose K-1}\text{ 增长}}_{\text{精确 composition 状态}}
\]

抵消。

因此，下一步若仍以 \(2.200611\) 为目标，不能继续要求“低负载恢复完整
composition”。真正可能有空间的对象必须在低负载层也进行 **query-sufficient
quotienting**：只保存足以判断 symbol support 的信息，而不是完整 multiplicity
composition；同时还要以可逆方式支持未来 deletions。这正是比 generalized
Sidon embedding 更难、也更可能有含金量的结构问题。
