# Ordinary dynamic AMQ：full-fiber 定理与 soft-posterior 前沿

> 日期：2026-08-13。本文严格区分已经闭合的定理、hard-union 方法的障碍，
> soft-posterior 的严格 no-go，以及最后留下的 multi-parent posterior deficit。
> 所有对数以 2 为底。

## 1. 当前结论

FOCS 2025 留下的 constant-error ordinary dynamic approximate-membership
问题尚未完全解决。不过，当前已经得到一个不依赖 history independence、
accepted-set monotonicity、locality、exact multiplicity 或 bounded churn 的解析
下界，并把下一步压缩为一个明确的 posterior-coding 问题。

设 universe 大小为 `u`，容量为 `n`，filter 用固定 `H` bit persistent memory，
免费只读随机带，支持 key-only `Insert/Delete/Query`，zero false negatives，且对
每条固定合法 history 和每个固定当前 nonmember 的 pointwise FPR 至多固定
`0 < delta <= 1/2`。若

\[
u/n^2\longrightarrow\infty,
\qquad f(n)/n\longrightarrow\infty,
\]

则

\[
\boxed{
H\ge n\left[
\log\frac1\delta+(1-\delta)\log e-2h_2(\delta)
\right]-o(n).
}
\tag{1}
\]

对误差 `1/2` 的 filter 取 `k` 个独立副本并对 query 取 AND，得到

\[
H\ge n\max_{k\ge1}\frac{B(2^{-k})}{k}-o(n),
\qquad
B(\delta)=\log\frac1\delta+(1-\delta)\log e-2h_2(\delta).
\tag{2}
\]

离散最大值在 `k=5` 达到：

\[
\boxed{H\ge1.1992732344471508\ldots n-o(n).}
\tag{3}
\]

式 (3) 已被 joint batch converse 严格改进。当前最强的闭合结论是

\[
\boxed{H\ge C_{\rm end}(\delta)n-o(n),}
\tag{3a}
\]

其中

\[
C_{\rm end}(\delta)=
\min_{0<x<1}\max\left\{
\log\frac1{\delta x},
(1-\delta x)\log\frac{1-\delta x}{\delta(1-x)}
\right\}.
\tag{3b}
\]

在 `delta=1/2` 时，两个函数在
`x=0.739998185722401...` 相交，给出

\[
\boxed{H\ge1.434406361243753\ldots n-o(n).}
\tag{3c}
\]

证明联合编码整个 hidden batch 的 hit pattern 与 hit values，并分别对 KLZ 的两个
endpoint pivots 使用凸性/Jensen，因此允许任意 hit correlation。此前把两个
endpoint sums 交叉逐项平均得到 `1.432309...` 的论证方向错误，已经撤回。
式 (3c) 仍离 constant-error 最优率很远，不能称为 fingerprint optimality。

## 2. Partition-free full fiber

固定 filter tape `R`。对物理状态 `m`、逻辑 load `t` 和操作数 `q`，定义

\[
W_R(m,t,q)
=\bigcup\{S(h):h\text{ 合法},\ |h|=q,\ |S(h)|=t,\ M_R(h)=m\}.
\tag{4}
\]

对任意固定合法 history `h`，

\[
S(h)\subseteq W_R(M_R(h),t,q)\subseteq A_R(M_R(h)).
\tag{5}
\]

第二个 inclusion 只使用 zero false negatives。与 KLZ Section 5 的
conforming-history reconstructible set 不同，式 (4) 不引用随机 partition；
条件于完整 operational transcript 和 filter tape 后，它是固定集合，因此可合法
进入 KLZ Claim 4.6 的 removing-`U_k` 计算。

时间坐标 `q` 不可省略。它保证替代 witness history 与真实 prefix 等长，拼接
suffix 后仍处于 filter 承诺支持的 operation horizon 内。

## 3. Deferred-suffix transport

固定 KLZ cut prefix `p`，只暴露 tree shape、cut 前已经遍历的 edge labels 和
filter tape，不暴露 future suffix labels。令 `w` 是

- `sigma_(G_k) \ sigma_(G_(k-1))`，或
- `sigma_(F_r) \ sigma_(G_ell)`，其中 `ell <= r`。

两类 `w` 都是 self-contained。若 `T_x` 是 `x in W(p)` 的一个 witness endpoint，
那么 `T_x` 与 `w` 的拼接失败的唯一原因是跨边界 duplicate insertion：suffix
中的 deletion 都匹配 suffix 自己较早的 insertion，load profile 与真实执行相同，
也不会删除 cut 时已经存在的 key。因此

\[
T_x\cap I(w)=\varnothing
\quad\Longrightarrow\quad
x\in W(pw).
\tag{6}
\]

设 `E_j(w)` 是 suffix 中尚未暴露的 level-`j` downward edges 数。每个 future
level-`j` edge 是从 `U_j` 中均匀无放回抽取的 `n/b`-tuple。条件于 cut exposure，

\[
\mathbb E|W(p)\setminus W(pw)|
\le |W(p)|\frac{nt}{u}\max_jE_j(w)
\le n^2M^b,
\qquad M=4^b.
\tag{7}
\]

证明顺序很重要：先条件于 cut-prefix exposure 对 future labels 平均 transport
loss；随后才在 Claim 4.6 中条件于完整 transcript 估计与 `U_k` 的交。不能在
已经固定 future labels 后再次使用其独立性。

## 4. 显式参数窗口

令

\[
A_n=u/n^2,
\qquad F_n=f(n)/n,
\qquad
T_n=\min\{\log_4A_n,\log_4F_n,\log_4n\},
\]

并取

\[
b=\left\lfloor\frac{\sqrt{T_n}}4\right\rfloor,
\qquad M=4^b.
\tag{8}
\]

为避免假设 `b` 整除 `n`，在容量 `n` 的结构中只使用
`n'=b floor(n/b)=n-o(n)` 个 keys。于是

\[
Q\le \frac{nM^{b+1}}b=o(f(n)),
\tag{9}
\]

\[
D=n^2M^b,
\qquad
bD=o(N/M),
\qquad
N=(1-\delta)n+\delta u,
\tag{10}
\]

并且 exposed-label correction、`L/u` finite-population correction、原 KLZ 条件
`9^(b^2)=o(delta u/n)` 以及 Lemma 4.8 的 `O(4^-b)` slack 同时成立。

定义

\[
g_k=\mathbb E|W(G_k)|,
\qquad
\widehat g_k=g_k+kD,
\qquad
\widehat N=N+bD.
\tag{11}
\]

则 corrected increments 非负且总质量至多一。KLZ Claim 4.7 比较的是完整
operational histories 的条件分布，因此可直接用于带时间索引的 full-fiber
functional。逐项代回 KLZ Lemma 4.5 后，每个 batch 的正确 fixed-error 成本为

\[
\frac nb\left[
\log(u/b)+\log\delta+2h_2(\delta)
+(1-\delta)\log(a_{(\ell,r]}+O(4^{-b}))
\right]+o(n/b).
\tag{12}
\]

KLZ pivot lemma 提供的 factorial saving 只有 miss mass `1-delta` 能使用，因而
得到式 (1)。这里没有额外的 `delta log e` 项。

## 5. 为什么 hard union 无法把 `u >> n^2` 降到 `u >> n`

只保留 `W=union F` 时，式 (7) 的 birthday-scale loss 基本 tight。更强的障碍是
rare-witness poisoning：取一个很厚的主 family，再为 `U` 中许多额外元素各加入
一个总 posterior mass 趋零的 endpoint。endpoint entropy、incidence-weighted
core statistic 和任意连续的 posterior functional 几乎不变，但 hard union 立即
扩大到整个 `U`，随机 insertion 可删除 `Theta(n)` 个 union elements。

因此，不存在一个仅依赖 endpoint posterior 且对 rare mass 连续的 inequality，
能够普适控制

\[
|W_{\rm before}\setminus W_{\rm after}|.
\tag{13}
\]

这说明 `u >> n^2` 是 KLZ 当前“从 hard set difference 中发送 rank”接口的内生
限制，不只是 witness 选择过粗。

## 6. Soft-posterior transport theorem

令 `U=disjoint_union_j U_j`，`|U_j|=u_j`。令 `S~mu` 是固定 profile
`s_j=|S cap U_j|` 的随机 `t`-set。给定 `S` 后，从 `U_j \ S` 中均匀抽取
`q_j` 个 insertion labels `Y_j`，并令 `Y=union_j Y_j`。定义 survivor mass

\[
Z(Y)=\mu\{T:T\cap Y=\varnothing\},
\qquad
\mu_Y(T)=\frac{\mu(T)\mathbf1[T\cap Y=\varnothing]}{Z(Y)}.
\tag{14}
\]

则有精确恒等式

\[
\boxed{
\mathbb E\log\frac1{Z(Y)}
=I(S;Y)
=H(\mu)-\mathbb EH(\mu_Y).
}
\tag{15}
\]

并且

\[
I(S;Y)
\le\sum_j\log
\frac{{u_j\choose q_j}}{{u_j-s_j\choose q_j}}
\le(\log e)\sum_j
\frac{s_jq_j}{u_j-s_j-q_j+1}.
\tag{16}
\]

证明只用 Bayes rule：`mu_Y` 是观察到 suffix 与 endpoint 不冲突后的 posterior，
且 `D(mu_Y || mu)=log(1/Z(Y))`；再由
`I(S;Y)<=H(Y)-H(Y|S)` 得到组合上界。若 profile 可变，条件于 profile 只额外
支付至多 `b log(n+1)` bits。

式 (15) 是一个有用的新会计恒等式：hard union pruning 按 rare keys 计费，而 soft
posterior pruning 按 endpoint probability 计费，并且全部 suffix conflict 只支付为
一次 posterior entropy drop。在 total inserted labels 为 `q` 时，其自然尺度约为

\[
O(nq/u),
\tag{17}
\]

所以通过足够慢的 obfuscation growth，它在 `u/n -> infinity` 下可以成为
`o(n)`。但是下一节说明：小 transport log-loss 不等于新的 communication saving。

## 7. Exact-posterior Send 是严格 no-go

给定 decoder 已知的 common context `C`，令 `mu_C` 是待编码 batch `X` 的精确
posterior，`Z` 是由 query state 决定的完整 hit pattern。先在 posterior 下编码
`Z`，再在 `mu_C(.|Z)` 下编码 `X`，虽然 lossless，但有精确守恒

\[
H(Z\mid C)+H(X\mid Z,C)=H(X\mid C).
\tag{18}
\]

若改用任意 proposal `nu_C`，expected cross-entropy 变为

\[
H(X\mid C)+D(\mu_C\Vert\nu_C)\ge H(X\mid C).
\tag{19}
\]

按 KLZ pivot 顺序逐批使用 exact posterior，全部条件熵链式相加为

\[
\sum_k H(X_k\mid C_k)
=H(X_{1:b}\mid M_b,\Theta,R).
\tag{20}
\]

再加最终状态携带的信息

\[
I(X_{1:b};M_b\mid\Theta,R)\le H
\tag{21}
\]

恰好恢复 source entropy。式 (15) 中 pruning 造成的 posterior entropy drop，也
会被识别 suffix 或 branch 所需的 mutual information 补回。因此：

> 仅把 KLZ 的 hard-set rank code 替换为 exact-posterior arithmetic code，必然是
> 链式法则恒等式，不可能产生新的 lower bound。

还有一个量词问题。若 posterior 只支持 KLZ source completions，不同 completion
对应的 future labels 也不同，因而不存在 full-fiber lemma 所需的 fixed common
suffix；若扩张到同一 state 的全部合法 histories，则没有 canonical prior，rare
non-source witnesses 又重新出现。给这些 witnesses 加 `eta` mass 只是在 hard union
和 soft code 之间移动问题。

## 8. 真正的最小未解 lemma

令 `Theta` 包含 partition、tree shape 与所有 non-rightmost labels，`R` 是 filter
tape，`X=(X_1,...,X_b)` 是独立均匀 batches，`M_b=F_b` 是协议首先发送的最终
状态。对 pivot `s`，按 KLZ decode order 令 `D_k` 为此前已经解码的 batches，并令

\[
(r_k,\ell_k)=
\begin{cases}
(b,k-1),&k\le s,\\
(k,s),&k>s.
\end{cases}
\tag{22}
\]

每个 `F_(r_k)` 都是 `(M_b,D_k,Theta,R)` 的确定函数。定义

\[
\boxed{
J_s=\sum_{k=1}^b
I(X_k;F_{r_k}\mid\Theta,R,D_k).
}
\tag{23}
\]

由 data processing 与 chain rule，严格有

\[
\boxed{
J_s\le I(X;M_b\mid\Theta,R)\le H.
}
\tag{24}
\]

这正是所需的 single-budget statistic：它按 source probability 计费，避开 rare
witness poisoning；所有 parent states 都从同一个 final state 导出，不会重复收费。

真正需要的新定理是证明，对任意 ordinary right-congruence AMQ，存在 pivot `s`
使

\[
J_s\ge nL(\varepsilon)-o(n),
\tag{25}
\]

其中 `L` 严格超过当前 arbitrary-filter frontier，理想值是正确的 fingerprint-
multiset rate。

式 (25) 目前尚未证明。FPR 不能在条件于 `(R,F_state)` 后重新使用；所需 local
inequality 必须在固定 source history 的原始联合分布上，同时联系：

- rejection matrix 的未条件化平均；
- source-fiber section multiplicities；
- `I(X_k;F_r | R,D_k)`。

朴素逐 batch Carter bound 会条件于 tape/state 或重复收费，global coin、frozen
mask 和 coordinate erasure 都会反驳它。这个 unconditional
rejection--multiplicity--information inequality 是现在最小、最准确的主缺口。

## 9. 研究价值判断

已经闭合的 full-fiber theorem 有两个真实贡献：它修复 KLZ Section 5 的
partition-dependence interface，并把 fixed-error ordinary nonmonotone 模型的
一般动态证明推进到显式常数。单独的 `1.199273...` 数值仍不足以成为 sharp SODA
主结果；joint batch converse 随后把常数提高到 `1.434406...`。

soft-posterior theorem 的价值是揭示 hard-union 障碍并给出正确熵会计；它已经被
证明不能单独产生 communication saving。更高价值的主线现在是式 (25) 的
multi-parent posterior deficit。成功后既可能把 universe 条件降到 `u >> n`，也
可能直接显著提高 fixed-error coefficient；失败时，一个满足普通模型的 extremal
construction 也会揭示比 fingerprints 更一般的动态压缩机制。

与主线互补的障碍定理是：若一个 exchangeability class 最多容纳 `N` 个 live
copies，而局部 transducer 只有 `K` 个状态并支持任意长 churn，则

\[
K\ge(1-\varepsilon)N+1.
\tag{26}
\]

它说明 orientation 可以通过 fingerprint exchangeability 消除，但 multiplicity
和 ghost recycling 不能用常数状态消失。该结果解释构造困难，却不代替 arbitrary
AMQ 的全局 converse。
