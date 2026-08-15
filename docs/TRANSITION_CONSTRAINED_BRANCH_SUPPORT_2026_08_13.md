# Transition-constrained branch--support：当前严格边界

> 日期：2026-08-13。状态：已得到一个 abstract exact batch-code identity 和一条 conditional 定量推导。普通 KLZ 模型还缺 partition-dependent reconstructible set 的 symmetry / removing-\(U_k\) lemma；主常数 \(B_{\rm joint}\) 不是已证定理。

## 1. 模型与目标

沿用 KLZ/FOCS 2025 的普通动态 filter 模型。固定容量 (n)、误差 (\varepsilon)、有限宇宙 (U) 和固定 (H)-bit memory。算法可使用免费无限只读随机带；更新只看到当前 memory、更新 key 和随机带。允许任意 history dependence、ghosts、global certificates 和全局重排。

不假设：

- history independence 或 canonical endpoint state；
- actual accepted-set monotonicity；
- exact multiplicity recovery；
- cell locality、singleton witnesses 或 memory direct sum。

KLZ 随机 partition 给出 (U=U_1\sqcup\cdots\sqcup U_b)，每个 hidden batch

\[
X_k=(X_{k,1},\ldots,X_{k,m}),
\qquad
m=n/b,
\qquad
V=|U|/b,
\]

是从 (U_k) 均匀无放回抽取的 ordered distinct tuple。

对于一次 `Send(X_k,F_r,G_\ell)`，使用 Section 5 的 reconstructible sets，定义

\[
G=\widetilde G_\ell\cap U_k,
\qquad
D=(\widetilde F_r\setminus\widetilde G_\ell)\cap U_k,
\]

并记

\[
g=|G|,
\qquad d=|D|,
\qquad
Z_i=\mathbf1[X_{k,i}\in G],
\qquad
Q=\sum_{i=1}^m(1-Z_i).
\]

由于真实 batch keys 属于 (\widetilde F_r)，每个 miss key 都在 (D) 中。

## 2. Decoder side information

在发送第 (k) 批时，Bob 已知：

- public random partition (pi) 与 obfuscating tree 的所有公开 labels；
- filter random tape；
- 已经解码的 batches；
- 当前两个 physical pivot states (F_r,G_\ell)；
- 因而可以无时间限制地计算 (G,D,g,d)。

他不知道 hidden batch (X_k)。所有 ranks 均使用双方固定的 (U_k) 顺序。

这里不对 random tape 或 physical state 条件化后调用 FPR。FPR 只会在最后对原始联合实验取无条件期望时使用。

## 3. 实际 reconstructible prefix support 退化

对每次 KLZ `Send`，都有 ℓ<k。Section 5 原文对 conforming reconstruction sequence 的证明给出：size 为 ℓm 的 endpoint 的所有 true keys 都属于

\[
\bigcup_{j\le\ell}U_j.
\]

因此

\[
G=\widetilde G_\ell\cap U_k=\varnothing,
\qquad g=0,
\qquad Q=m.
\tag{1}
\]

所以真正的 Section 5 reconstructible prefix support 不是一个 density-ε hit mask；它在 future block 上严格为空。

在更一般的抽象 batch experiment 中，如果另有 (G\perp X_k)，则

\[
Q\mid G
\sim
\operatorname{Hypergeom}(V,V-g,m),
\qquad
\mu_G:=\mathbb E[Q\mid G]
=m\frac{V-g}{V}.
\tag{2}
\]

注意 (F_r,D) 可以强烈依赖 (X_k)。证明不声称 (X_k\mid G,D) 是均匀的，也不声称 (Q\mid G,D) 是 hypergeometric。对真正的 Section 5 protocol，应直接使用 (1)，而不是随机-mask 解释。

## 4. 已证的抽象结果：exact branch--hit entropy identity

以下 lemma 的显式前提是：给定 \(G\) 后，\(X_k\) 在 \(U_k\) 中均匀无放回。令 \(P\) 包含完整 branch vector \(Z\)，以及按坐标顺序排列的所有 hit values \(X_{k,i}\)（即 \(Z_i=1\) 的坐标值）。则

\[
\boxed{
H(P\mid G)
=
\log_2(V)_{\underline m}
-\mathbb E\!left[
\log_2(V-g)_{\underline Q}
\mid G
\right].
}
\tag{3}
\]

证明是精确计数。给定 (P=(z,x_{\rm hit}))，尚未揭示的 (Q) 个 ordered miss values 可以是 (U_k\setminus G) 中任意 ordered distinct tuple，恰有

\[
(V-g)_{\underline Q}
\]

种；原 batch 在 ((V)_{\underline m}) 个 ordered distinct tuples 上均匀。故

\[
\Pr[P=p\mid G]
=
\frac{(V-g)_{\underline{Q(p)}}}{(V)_{\underline m}},
\]

直接取熵即得 (3)。

这条 identity 自动联合了 branch-pattern entropy 与 hit-side location。它对 frozen masks 和 shared certificates 都成立；不需要 (Z_i) 独立，也不需要下界 (H(Z))。

## 5. Exact batch code

Alice 先用 Shannon code 发送 (P)，再把按原坐标顺序排列的 (Q) 个 miss values 作为 (D) 中的 ordered distinct tuple 发送，长度至多

\[
\log_2(d)_{\underline Q}+1.
\]

由 (3)，期望 batch message length 满足

\[
\boxed{
\mathcal C_k
\le
\log_2(V)_{\underline m}
+
\mathbb E\log_2
\frac{(d)_{\underline Q}}{(V-g)_{\underline Q}}
+O(1).
}
\tag{4}
\]

若 (Q=0)，ratio 约定为 (1)。合法 transcript 上 (d\ge Q)，所以不会出现无法排名的情况。

式 (4) 是 reviewer-safe 的 batch coding lemma。它不要求 (D) 与 batch 独立；(D) 的全部依赖只出现在实际 rank length 中。

## 6. 定量上界：当前证明骨架

由 falling-factorial ratio 的逐项上界，

\[
\log_2
\frac{(d)_{\underline Q}}{(V-g)_{\underline Q}}
\le
Q\log_2\frac d{V-g}.
\tag{5}
\]

拆成

\[
Q\log_2\frac dQ
+Q\log_2\frac Q{V-g}.
\tag{6}
\]

### 6.1 (d)-项

函数

\[
(q,d)\mapsto q\log_2(d/q)
\]

是 log 的 perspective，联合凹。令

\[
\bar q=\mathbb E Q,
\]

则

\[
\mathbb E\!left[Q\log_2(d/Q)\right]
\le
\bar q\log_2\frac{\mathbb E d}{\bar q}.
\tag{7}
\]

### 6.2 Hypergeometric fluctuation 项

条件于 (G)，令 (mu=mu_G=m(V-g)/V)。则

\[
Q\log_2\frac Q{V-g}
=
Q\log_2\frac mV
+Q\log_2\frac Q\mu.
\]

用 (ln x\le x-1)，

\[
\mathbb E\!left[Q\ln(Q/\mu)\mid G\right]
\le
\frac{\operatorname{Var}(Q\mid G)}\mu
\le1.
\tag{8}
\]

因此

\[
\mathbb E\!left[Q\log_2\frac Q{V-g}\right]
\le
\bar q\log_2\frac mV+log_2e.
\tag{9}
\]

合并 (7) 与 (9)：

\[
\mathbb E\log_2
\frac{(d)_{\underline Q}}{(V-g)_{\underline Q}}
\le
\bar q\log_2
\frac{m\,\mathbb E d}{V\bar q}
+O(1).
\tag{10}
\]

令

\[
\alpha=\frac{\bar q}{m}
=1-\frac{\mathbb E g}{V}.
\]

由于 (X_{k,i}) 是 (G_\ell) 当前逻辑集合之外的 fixed-distribution key，KLZ 的无条件 pointwise FPR averaging 给

\[
\mathbb E g/V\le\varepsilon,
\qquad
\alpha\ge1-\varepsilon.
\tag{11}
\]

ordinary-filter lifting 还需要证明 Claims 4.6--4.7 对 partition-dependent reconstructible difference 给出

\[
\mathbb E d
\le
\varepsilon V(1+o(1))(a_{(\ell,r]}+\gamma_b),
\qquad
\gamma_b=2/4^b+o(4^{-b}).
\tag{12}
\]

式 (12) 目前没有证明。无条件、立即可证的替代只有

\[
\boxed{
\mathbb E d
\le
m+\varepsilon(V-m).
}
\tag{12'}
\]

证明：由 (1)，(D=widetilde F_rcap U_k)。其中 (X_k) 的 (m) 个成员必在 (widetilde F_r)；对每个 (yin U_k\setminus X_k)，固定完整合法 history 后，它是 endpoint nonmember，且

\[
\Pr[y\in\widetilde F_r]
\le
\Pr[y\in\operatorname{Accept}(F_r)]
\le\varepsilon
\]

（概率只对 filter tape 取）。求和再对公共历史平均即得 (12')。

由于 (x\mapsto\log_2(x)_{\underline m}) 在 (x\ge m) 上凹，真正的 Section 5 batch 可直接用

\[
\mathcal C_k
\le
\mathbb E\log_2(d)_{\underline m}+O(1)
\le
\log_2\bigl(m+\varepsilon(V-m)\bigr)_{\underline m}+O(1).
\tag{12''}
\]

在 KLZ 的 (V/m=|U|/n\to\infty) regime，(12'') 只重现静态 (n\log_2(1/\varepsilon)-o(n)) 下界，不含 (a_{(\ell,r]})，因而不给 dynamic redundancy。

代入 (10)：

\[
\mathcal C_k
\le
\log_2(V)_{\underline m}
+m\alpha
\log_2
\frac{\varepsilon(a_{(\ell,r]}+\gamma_b)}\alpha
+o(m).
\tag{13}
\]

对固定 (0<c\le1)，函数

\[
\alpha\mapsto\alpha\log_2(c/\alpha)
\]

在 (alpha\ge1-\varepsilon\ge1/2) 上递减；这里 (c=\varepsilon(a+\gamma_b)\le1/2+o(1))。故

\[
\boxed{
\mathcal C_k
\le
\log_2(V)_{\underline m}
+(1-\varepsilon)m
\log_2
\frac{\varepsilon(a_{(\ell,r]}+\gamma_b)}{1-\varepsilon}
+o(m).
}
\tag{14}
\]

## 7. Conditional main theorem

若 (11)--(14) 在 KLZ Section 4--5 的完整 conditioning order 下逐行成立，则用 (14) 替换 Lemma 4.5，并用原 Lemma 3.4/4.8 的 pivot choice，得到

\[
\boxed{
H
\ge
nB_{\rm joint}(\varepsilon)-o(n),
\qquad
B_{\rm joint}(\varepsilon)
=(1-\varepsilon)
\log_2\frac{e(1-\varepsilon)}\varepsilon.
}
\tag{15}
\]

相较原 fixed-(\varepsilon) KLZ 常数，这个 code 精确消掉 branch/location 的两个 (h_2(\varepsilon)) 损失；factorial saving 仍只在 miss 质量上出现。

对 (k) 个独立副本取 AND 后，若 (15) 成立，则

\[
H
\ge
n\max_{k\ge1}
\frac{B_{\rm joint}(\varepsilon^k)}k-o(n).
\tag{16}
\]

在 (\varepsilon=1/2) 时，(k=4) 给

\[
H\ge1.2538091335540973\,n-o(n).
\tag{17}
\]

## 8. 为什么仍标为 conditional

式 (3)--(10) 在抽象前提下的批编码和解析不等式是自洽的。剩余问题不是例行 bookkeeping，而是一个真实的 partition-dependent lifting 缺口：

1. KLZ Section 5 的 reconstructible set 本身依赖 public partition π。即使固定 obfuscation sequence 和 filter tape，未在 sequence 中出现的 keys 的 partition assignments 仍会改变哪些 conforming histories 可以作为 reconstruction sequences；reconstructible difference 不自动成为一个固定集合 (A^*)。
2. 原 Claim 4.6 对 actual accepted-set difference 的 `remove (U_k)` 条件化不能逐字替换为 reconstructible difference。式 (12) 需要一个新的 **partition-dependent first-moment interface lemma**。
3. 实际上，按 conforming-history 定义，ℓ<k 时严格有 (widetilde G_ell\cap U_k=\varnothing)。这杀掉了把 prefix reconstructible support 当作一般 hit mask 的解释。
4. 式 (12) 只能在原联合实验中使用。应用 perspective Jensen 时不得偷偷切换成条件于 state/tape 的 FPR。
5. (O(1)) Shannon overhead 经过 (b=o(n)) 个 batches 后为 (o(n))；所有极小 (d)、(V-g) 边界仍需使用合法 transcript 的 (d\ge Q) 和 falling-factorial convention。

在新的 partition-dependent interface lemma 被证明前，式 (15) 不应对外声明为 theorem。更强地，若机械地把原 Claims 4.6--4.7 的 actual accepted-set first moment 以同样强度搬到 reconstructible (D)，由于此时 (Q=m)，会推出

\[
H\ge n\bigl(\log_2(1/\varepsilon)+\log_2e\bigr)-o(n).
\]

在 \(\varepsilon=1/2\) 这等于 \(2.442695\ldots n\)。这里有一个同属 KLZ fixed-memory、无限计算模型的显式反证，而不必诉诸 whp upper bound：取一个免费 fully-random hash (h:U\to[q])，其中 (q/n\to1/\ln2)，状态精确保存 (q) 个 fingerprints 的 count vector（总质量至多 (n)）。查询看相应 count 是否非零，更新作精确加减。其 pointwise FPR 为

\[
1-(1-1/q)^n\le1/2+o(1),
\]

而全部 count vectors 可用

\[
\log_2\binom{n+q}{n}
=2.384499842\ldots n+o(n)
\]

个 fixed bits 编码。这严格小于 (2.442695\ldots n)。稍微增大 (q) 可把误差压到严格不超过 (1/2)，而常数 gap 保持。因此足以推出小误差目标的 fixed-\(\varepsilon\) reconstructible first-moment lifting **必为假**；不是单纯尚未写细节。当前 exact batch lemma 只对满足相应 (G\)-symmetry 与 (mathbb E d) bound 的抽象实验成立；普通 KLZ corollary 未完成，并已有这个定量 obstruction。

## 9. Hostile tests

- **Frozen mask：** 不需要 (H(Z)\ge mh_2(\varepsilon))；相关性由 exact identity (3) 与 hit values 的 support 联合收费。
- **Global ALL-YES coin：** 大 (g) 会降低 (Q)，但其概率只通过无条件 (mathbb E g/V\le\varepsilon) 使用；没有按 random branch 平均 memory。
- **Shared witnesses：** 任意多个 coordinates 可由同一个 certificate 命中；证明从不逐 key 收费。
- **Ghosts：** 删除后的 accepted keys 可保留；只用 reconstructible inclusion 和现有 KLZ difference first moment，不恢复 multiplicity。

## 10. 当前诚实判断

abstract 式 (4) 已把 decoder 和实际 message 写清楚，也明确避开了 (D) 与 hidden batch 的错误独立性。但它目前不能直接替换 KLZ Lemma 4.5。真正缺失的不是 (G) 的 symmetry：在 actual reconstructible protocol 中 (G=\varnothing)。唯一核心问题是求一个较弱、且不与已知 upper bound 冲突的 partition-dependent (D)-first-moment inequality。

原式 (12) 的强度已被上面的 (2.442695>2.287904) sanity check 否决。因此下一步不应再尝试“逐字 lifting KLZ Claim 4.6”，而应找出 partition leakage 对 (mathbb E|D|) 必须增加的精确 correction term，并判断 correction 后是否仍留下正的常数改进。若没有，式 (15)--(17) 失效；abstract code (4) 与在显式 symmetry/first-moment 前提下的 inequality (10) 仍成立。

当前可以无保留宣称的相应新定量结论只属于 history-dependent monotone 子类，即独立 AND 放大后的 fixed-\(\varepsilon\) KLZ envelope：

\[
H\ge n\max_kL_{\rm KLZ}(\varepsilon^k)/k-o(n),
\]

其 (\varepsilon=1/2) 常数为 (1.199273234447\ldots)。式 (15)--(17) 应在完成 lifting 审计后再升级为主定理。

## 11. 对既有 KLZ fixed-error 审计的影响

同一个 obstruction 不只否决新的 (B_{\rm joint}) lifting，也影响逐项保留 KLZ 常数的普通 non-monotone corollary。

- 对 Section 4 的 history-dependent **monotone filters**，actual accepted sets 在固定 \(\sigma\) 与 filter tape 后确实固定，Claim 4.6 可用。因此相应 fixed-\(\varepsilon\) 常数审计仍成立。
- 对 Section 5 的普通 filters，把 accepted sets 换成 partition-dependent reconstructible sets 后，Claim 4.6 不再逐字成立；目前没有证明

  \[
  H\ge nL_{\rm KLZ}(\varepsilon)-o(n)
  \]

  的这一 ordinary-filter corollary。
- 只用 pointwise FPR 可由 (12') 救回静态 \(n\log_2(1/\varepsilon)-o(n)\)，但不能保留 interval \(a_{(\ell,r]}\) 和 dynamic factorial gain。
- 回到 actual accepted sets 也不能直接救普通模型：没有 actual monotonicity 时，

  \[
  |\operatorname{Accept}(F_r)\setminus\operatorname{Accept}(G_\ell)|
  \]

  不能化为两个 accepted-set sizes 之差；KLZ 的 marginal distribution coupling 不控制这个 joint difference。

因此既有 fixed-error 文档应明确改标为“Section 4 monotone-model calculation；ordinary non-monotone lifting conditional”。同理，这个 proof-interface gap 原则上也触及 KLZ Section 5 对 \(\varepsilon=o(1)\) 的原始 general-filter lifting；除非补出新的 partition-safe joint argument，不能用现有文字性 replacement 自动消除该问题。
