# KLZ Section 5 的 partition-dependence 断点：hostile audit

> 日期：2026-08-13。所有对数均为二进制。本文区分三个结论：
>
> - **已证：** fixed-error KLZ 计算和 AND amplification 对 history-dependent monotone filters 成立；
> - **未证：** 将同一计算经 Section 5 提升到普通 non-monotone filters；
> - **已否决：** 不加 correction 地把 Claim 4.6 原样用于 reconstructible sets。

## 1. 最终结论

KLZ Section 4 的 Proposition 4.3 本来就允许 history dependence，只保留 accepted-set monotonicity。对任意固定
\(\delta\in(0,1/2]\)，逐项保留论文中在 \(\delta=o(1)\) 时被吸收到 \(o(n)\) 的常数，可得到

\[
L_{\mathrm{KLZ}}(\delta)
=
\log_2(1/\delta)
+(1-\delta)\log_2 e
-2h_2(\delta).
\tag{1}
\]

因此，对任意 history-dependent monotone filter，取 \(k\) 个独立副本并对 query 取 AND，严格得到

\[
H\ge
n\max_{k\ge1}
\frac{L_{\mathrm{KLZ}}(\varepsilon^k)}{k}
-o(n),
\tag{2}
\]

其中 \(k\) 是不随 \(n\) 增长的常数。在 \(\varepsilon=1/2\) 时，\(k=5\) 给出

\[
H\ge1.1992732344471508\,n-o(n).
\tag{3}
\]

这里不需要 history independence。独立副本的状态可以依赖各自的完整历史；固定合法历史后，各副本的 false-positive event 仍是各自随机带的独立函数。AND 也保持 monotonicity，因为复合 accepted set 是各副本 accepted sets 的交。

但是，(2)--(3) **目前不能提升到普通 non-monotone filters**。断点不是 AND，也不是 fixed-error bookkeeping，而是 Section 5 的 reconstructible set 依赖 public partition \(\pi\)，使 Section 4 Claim 4.6 的 removing-\(U_k\) 条件化失效。

更强地，不带 partition-leakage correction 的机械 lifting 不只是“缺证明”，而是错误的：在 \(\varepsilon=1/2\) 时它会推出 \(2.442695\ldots n\) 的下界，却存在同一 fixed-memory/free-random-tape 模型中只用 \(2.384499842\ldots n+o(n)\) bits 的合法动态 filter。

## 2. Section 4 中 Claim 4.6 为什么对 monotone filters 合法

KLZ source 的位置如下：

- `history_dependent.tex` lines 17--25：定义 history-dependent monotonicity，并明确 Proposition 4.3 对 monotone filters 成立；对应 arXiv PDF p. 10。
- lines 183--220：Lemma 4.5 与 Claim 4.6；对应 PDF p. 15。
- lines 221--241：Claim 4.6 的 removing-\(U_k\) 证明；对应 PDF pp. 15--16。
- lines 244--274：Claim 4.7 的 obfuscation coupling；对应 PDF p. 16。
- lines 276--295：合并两条 claim 得到 batch candidate-set 的 first-moment bound；对应 PDF pp. 16--17。

Claim 4.6 要控制

\[
\mathbb E\left|
\bigl(A(F_r)\setminus A(G_\ell)\bigr)\cap U_k
\right|,
\qquad \ell<k\le r.
\tag{4}
\]

它先条件于 obfuscation sequence \(\sigma=\sigma^*\) 和 filter random tape \(R=R^*\)。对 ordinary accepted sets，这一步确实使物理状态 \(F_r,G_\ell\) 以及

\[
A^*=A(F_r)\setminus A(G_\ell)
\tag{5}
\]

完全固定。与此同时，除去已经出现在 \(\sigma^*\) 中的少量 keys，\(U_k\) 仍是均匀随机定长子集。因此可写

\[
\mathbb E[|A^*\cap U_k|\mid\sigma^*,R^*]
\le
L_k+
\frac{|U|/b-L_k}{|U|-L}|A^*|.
\tag{6}
\]

这正是 source equation `ineq:expectation_of_intersection_conditioned`，即 Claim 4.6 的核心。对 history-dependent monotone filters，(5) 是固定集合，且

\[
|A(F_r)\setminus A(G_\ell)|
=|A(F_r)|-|A(G_\ell)|
\tag{7}
\]

由 monotonicity 成立。再结合 Claim 4.7 的边际 size coupling，即得到 Section 4 所需的 layer increments。

所以 Section 4 并不要求 HI；它已经是 history-dependent monotone theorem。fixed-error 计算只改写其通信代价，没有改变这一步的逻辑。

## 3. Section 5 的精确断点

Section 5 的关键 source 位置为：

- `non-monotone.tex` lines 4--10：声称只要 reconstructible sets 满足三项列出的性质，就能把 Section 4 中所有 accepted sets 替换掉；对应 PDF p. 19。
- lines 12--21：conformity 显式依赖 partition \(\pi\)；对应 PDF p. 19。
- lines 23--34：Definition 5.2 定义 reconstructible set；对应 PDF p. 20。
- lines 38--60：Lemma 5.3 证明 inclusion 与 prefix monotonicity；对应 PDF p. 20。

固定 partition \(\pi=(U_1,\ldots,U_b)\)。对一个 memory representation \(m\) 和当前集合大小 \(t\)，reconstructible set 是

\[
\widetilde A_{\pi}(m,t)
=
\{x:\text{存在一条 conform to }\pi\text{ 的历史，到达 }m,
\text{大小为 }t,\text{且真实集合含 }x\}.
\tag{8}
\]

即使固定 \(\sigma=\sigma^*\) 和 filter tape \(R=R^*\)，memory representations 已固定，(8) 仍会随着尚未由 \(\sigma^*\) 暴露的 keys 的 partition assignments 改变。原因是这些 assignments 会改变哪些替代历史 conform to \(\pi\)，从而改变 reconstruction witnesses 的存在性。

因此

\[
\widetilde A_{\pi}(F_r)\setminus
\widetilde A_{\pi}(G_\ell)
\tag{9}
\]

在 Claim 4.6 的 conditioning 后不是固定集合。不能把它命名为 \(A^*\)，再使用 (6) 的 hypergeometric intersection 计算。这项 partition measurability/independence 不是 Section 5 列出的三项性质之一。

还有一个更强的结构事实。若一条 conforming history 的 endpoint size 为 \(\ell n/b\)，它的当前集合只能包含

\[
U_1\cup\cdots\cup U_\ell
\tag{10}
\]

中的 keys。因此对 \(k>\ell\)，严格有

\[
\boxed{
\widetilde A_{\pi}(G_\ell)\cap U_k=\varnothing.
}
\tag{11}
\]

这说明 reconstructible prefix 并不是 Section 4 中一般的 hit mask。在发送第 \(k\) batch 时，所有 hidden keys 都走 miss branch；真正需要控制的是

\[
D=\widetilde A_{\pi}(F_r)\cap U_k.
\tag{12}
\]

Section 4 的 global difference
\(|A(F_r)|-|A(G_\ell)|\) 之所以有 layer functional，是因为 \(A(G_\ell)\) 可以占据随机 \(U_k\) 的一部分。对 reconstructible sets，(11) 说明这项 subtraction 完全位于 \(U_k\) 外，不能自动转化为 (12) 的减少。

## 4. 错误 lifting 为什么推出 \(2.442695n\)

假设错误地把 Claim 4.6--4.7 以原强度应用到 (12)。令 \(V=|U|/b\)、\(m=n/b\)，并像 Section 4 一样用 \(a_{(\ell,r]}\) 表示 normalized layer increment。由于 (11)，发送 \(X_k\) 不再需要 KLZ 的 hit bit，也没有 hit branch；每个 key 都作为 \(D\) 的元素发送。

错误的 first-moment lifting 会给出

\[
\mathbb E|D|
\le
\varepsilon V
\left(a_{(\ell,r]}+o(1)\right).
\tag{13}
\]

于是一个 batch 的通信代价至多

\[
m\log_2 V
+m\log_2\varepsilon
+m\log_2 a_{(\ell,r]}
+o(m).
\tag{14}
\]

将 \(b\) 个 batches 相加，加上初始 \(H\)-bit filter state，并与 hidden ordered batches 的 entropy
\(n\log_2V-o(n)\) 比较，得到

\[
H
\ge
n\log_2(1/\varepsilon)
-\frac nb\sum_{k=1}^b
\log_2 a_{(\ell_k,r_k]}
-o(n).
\tag{15}
\]

KLZ 的 pivot/factorial lemma 给出某个 \(s\) 使

\[
\sum_{k=1}^b\log_2a_{(\ell_k,r_k]}
\le-b\log_2e+o(b).
\tag{16}
\]

代入即得

\[
\boxed{
H\ge n\left(\log_2(1/\varepsilon)+\log_2e\right)-o(n).
}
\tag{17}
\]

当 \(\varepsilon=1/2\) 时，右侧常数为

\[
1+\log_2e
=2.4426950408889634.
\tag{18}
\]

这不是一个可信的“意外强定理”，因为下一节给出严格更小的合法 fixed-space upper bound。

## 5. 合法的 \(2.384499842n\) fixed-memory 反证

取一个公共随机 hash

\[
h:U\to[q],
\tag{19}
\]

其描述位于免费只读随机带上。只需对任意当前至多 \(n\) 个 distinct members 和一个固定 query key 保证联合独立；在 KLZ 的无时间限制模型中，可由 random tape 上固定位置的 degree-\(n\) polynomial hash 实现。取

\[
\frac qn\to\alpha=\frac1{\ln2},
\tag{20}
\]

并将 \(q\) 略微增大 \(o(n)\)，使有限 \(n\) 时的错误严格不超过 \(1/2\)。

内存精确保存 count vector

\[
C=(C_1,\ldots,C_q),
\qquad C_j\ge0,
\qquad \sum_jC_j\le n.
\tag{21}
\]

操作为：

- `Insert(x)`：增加 \(C_{h(x)}\)；
- `Delete(x)`：减少 \(C_{h(x)}\)；合法 deletion 保证该 count 为正；
- `Query(x)`：当且仅当 \(C_{h(x)}>0\) 时回答 YES。

这对任意长的合法 update history 都有效，不需要 history independence。成员从不出现 false negative。对任意固定 endpoint history 和固定非成员 \(z\)，

\[
\Pr[h(z)\in h(S)]
=1-(1-1/q)^{|S|}
\le1-(1-1/q)^n
\le\frac12.
\tag{22}
\]

所有可能的 (21) 是 \(q+1\) 个变量总和恰为 \(n\) 的 weak compositions（加入 slack coordinate），故总数为

\[
\binom{n+q}{n}.
\tag{23}
\]

无时间限制下，可对 composition rank/unrank，用一个固定长度的 memory block 保存其 rank。因此

\[
H_{\rm upper}
=\left\lceil\log_2\binom{n+q}{n}\right\rceil.
\tag{24}
\]

由 Stirling 公式，若 \(q/n\to\alpha\)，则

\[
\frac{H_{\rm upper}}n
=(1+\alpha)\log_2(1+\alpha)
-\alpha\log_2\alpha
+o(1).
\tag{25}
\]

代入 \(\alpha=1/\ln2\) 得

\[
\boxed{
H_{\rm upper}
=2.3844998424785167\,n+o(n).
}
\tag{26}
\]

而

\[
2.4426950408889634
-2.3844998424785167
=0.0581951984104467>0.
\tag{27}
\]

所以 (17) 对普通 filters 为假，进而 (13) 或其前置 partition-independence 假设必定失败。这个反证使用的是 fixed worst-case state count，不是 Shannon average，也不依赖 2026 entropy-array 的 whp space guarantee。

## 6. 两层随机性修复为什么没有直接恢复 factorial gain

一个自然建议是把两种随机性分开：

1. 先采样 \(\pi=(U_1,\ldots,U_b)\)，只用于定义 conformity 和 reconstructible sets；
2. 再在每个 \(U_k\) 内独立采样 thinning/subcell \(W_k\subseteq U_k\)，从 \(W_k\) 抽取 hidden batch 和 obfuscating labels。

这样在条件于 \(\pi,\sigma,R\) 后，reconstructible sets 的确固定；除去已暴露 labels 后，\(W_k\) 仍有 hypergeometric residual randomness。更精确地，令 \(R_k\) 是 transcript \(\sigma\) 中已经出现的 distinct level-\(k\) labels，\(t_k=|R_k|\)。由于任意包含 \(R_k\) 的候选 \(W_k\) 产生这些 labels 的 likelihood 相同，条件分布

\[
W_k\mid(\pi,\sigma)
\]

恰为 \(U_k\) 中所有包含 \(R_k\) 的均匀 \(|W_k|\)-subsets。若
\(B\subseteq U_k\) 已由 \((\pi,\sigma,R)\) 固定，则 exact removing-\(W_k\) 公式是

\[
\mathbb E[|B\cap W_k|\mid\pi,\sigma,R]
=|B\cap R_k|
+\frac{|W_k|-t_k}{|U_k|-t_k}
|B\cap(U_k\setminus R_k)|.
\tag{28}
\]

当 \(t_k=o(|W_k|)\) 时，主项约为
\((|W_k|/|U_k|)|B|\)，但这是 **block-local mass**，不是原 Claim 4.6 的
\((|W_k|/|U|)|A|\) 跨 blocks averaging。换言之，修复 conditioning 本身可以完全自洽，失败发生在它暴露出来的新 functional 上。

但它没有恢复 KLZ 的 layer subtraction。因为 \(W_k\subseteq U_k\)，由 (11) 仍有

\[
\widetilde A_\pi(G_\ell)\cap W_k=\varnothing
\qquad(\ell<k).
\tag{29}
\]

于是

\[
\bigl(\widetilde A_\pi(F_r)
\setminus\widetilde A_\pi(G_\ell)\bigr)\cap W_k
=\widetilde A_\pi(F_r)\cap W_k.
\tag{30}
\]

式 (28) 只能把问题化为控制 \(F_r\) 在第 \(k\) 个 conformity layer 内的质量；global quantity
\(|\widetilde A(F_r)|-|\widetilde A(G_\ell)|\) 中被减去的整项位于其他 layers，不能用于缩小 (30)。仅由 one-sidedness 和 pointwise FPR，可安全得到的量级是

\[
\mathbb E|\widetilde A_\pi(F_r)\cap W_k|
\le m+\varepsilon(|W_k|-m),
\tag{31}
\]

其中 \(m\) 个 true batch keys 必须被接受。将 (31) 代入通信协议，只恢复静态
\(n\log_2(1/\varepsilon)-o(n)\) 项，没有 \(n\log_2e\) 的 factorial gain。

也可以把这个失败写成最小矩阵反例。令 \(V=|U_k|\)，并按适当 normalization 定义

\[
p_{r,k}
=
\frac{\mathbb E|\widetilde A(G_r)\cap U_k|}
{m+\varepsilon(V-m)}.
\tag{31a}
\]

conformity 强迫 \(p_{\ell,k}=0\) 对所有 \(\ell<k\)；obfuscation coupling 最多把同一列中的 \(F_r\) 换成 \(G_r+o(1)\)。因此原来的一维 interval functional 不再出现，protocol \(Q_s\) 的候选 log-saving 变成类似

\[
\sum_{k\le s}\log_2p_{b,k}
+\sum_{k>s}\log_2p_{k,k}.
\tag{31b}
\]

lower-triangular profile

\[
p_{r,k}=\mathbf1[r\ge k]
\tag{31c}
\]

满足非负、逐列单调、conformity 的零区域以及 normalized endpoint bound，却使 (31b) 对每个 \(s\) 都恰为零，而不是 \(-b\log_2e+o(b)\)。这个 diagonal obstruction 正是“每个 block 的 reconstructible support 在它自己的 insertion level 才出现”的自然行为，说明原 choice-of-\(s\) lemma 没有 block-matrix 版本可由这些约束推出。

此外还有一个独立的 size tradeoff。\(R_k\) 是 conditioned transcript 中所有 level-\(k\) edge labels 的 union。若这一层使用了 \(E_k\) 条近似独立的 \(m\)-tuple labels，则一般

\[
t_k=|R_k|=\Theta(\min\{|W_k|,mE_k\}).
\tag{31d}
\]

要让 (28) 留下接近均匀 thinning 的 residual randomness，必须
\(t_k=o(|W_k|)\)，即 \(|W_k|/m\gg E_k\)。KLZ 的 obfuscating tree 取
\(M=4^b\)，相关 \(E_k\) 可达到随 \(b\) 超常数增长的量级。因此：

- 若取 \(|W_k|=cm\) 保留非平凡 finite-universe falling-factorial correction，那么大量 public labels 通常会使 \(R_k=W_k\)，\(W_k\) 被 transcript 完全暴露，(28) 没有可用随机性；
- 若取 \(|W_k|\gg mE_k\) 保留 residual randomness，则 \(c=|W_k|/m\to\infty\)，batch source 与静态 candidate support 的每-key saving 只趋于 \(\log_2(1/\varepsilon)\)，finite-\(c\) correction 消失。

具体地，若 \(|W_k|=cm\) 且静态候选大小为
\(d m\)，其中 \(d=1+\varepsilon(c-1)\)，falling-factorial 的每-key saving 趋于

\[
\Psi_c(\varepsilon)
=\int_0^1
\log_2\frac{c-x}{1+\varepsilon(c-1)-x}\,dx
\le\log_2(1/\varepsilon),
\tag{31e}
\]

并且 \(c\to\infty\) 时取等号极限。故简单两层方案甚至在 size scaling 上也无法同时拥有“未暴露的 thinning randomness”和“非平凡 factorial layer gain”。

另一种尝试是把 \(\pi\) 变粗，让多个发送 batches 的 \(W\)-cells 落在同一个 conformity cell 中，使 prefix reconstructible set 可能与未来 \(W_k\) 相交。但这会破坏 Lemma 5.3 的 common-continuation argument。原证明在 `non-monotone.tex` lines 53--58 使用

\[
S(G')\subseteq U_1\cup\cdots\cup U_\ell,
\qquad
\text{suffix inserts}\subseteq U_{\ell+1}\cup\cdots\cup U_b,
\tag{32}
\]

来排除 duplicate insertion，并保证 reconstruction history 与固定 suffix 的拼接仍 self-contained。若 earlier 和 future \(W\)-batches共享同一 coarse conformity cell，某个 reconstruction world \(G'\) 可以已经包含 suffix 随后要 `Insert` 的 key；此时拼接历史非法，prefix monotonicity不再成立。

因此简单两层随机结构面对一个精确二难：

\[
\begin{array}{c|c|c}
\text{conformity partition} & \text{common continuation} & \text{future-layer subtraction}\\
\hline
\text{按 batch 精细分层} & \checkmark & \times\text{，由 (29)}\\
\text{合并多个 batches} & \times\text{，可能 duplicate insert} & \text{可能恢复 mixing}
\end{array}
\tag{33}
\]

独立 thinning 修复了 measurability，却没有修复 layer functional；coarsening 可能修复 mixing，却失去 Section 5 用来建立 monotonicity 的合法 continuation。

## 7. D-choice/support 路线与当前基准的比较

两选择 min-rank 的 exact-count snapshot 在 \(\varepsilon=1/2\) 时为

\[
R_{\rm count}=2.8304000127\ldots,
\tag{34}
\]

并不提供更小的普通动态 filter upper bound，也不形成 universal lower bound。support-only snapshot entropy 为

\[
R_{\rm support}=2.1216107112\ldots,
\tag{35}
\]

但 support state 无法安全执行普通 key-only deletion：清 bit 可能造成 false negative，永久保留则 ghosts 在 churn 下累积。因此 (35) 只是对“endpoint support 必须支付 fingerprint-count entropy”这类 converse 的反例，不是动态 theorem。

它也不能与 (3) 直接比较为更强下界：(3) 是 monotone-filter universal lower bound，(35) 是 restricted two-choice process 的静态候选 upper rate。当前 D-choice 路线没有超过 (3) 的已证 ordinary/monotone theorem。

## 8. 最值得保留的 precise open lemma

目前最精确、且未被 (26) 反驳的开放目标不是原 Claim 4.6，而是带 partition leakage correction 的 first-moment interface：

> 对 KLZ conforming-history reconstructible set，刻画最小 correction
> \(\mathrm{Leak}_{\pi,k}\)，使
> \[
> \mathbb E|\widetilde A(F_r)\cap U_k|
> \le
> \text{KLZ layer term}
> +\mathrm{Leak}_{\pi,k}.
> \tag{36}
> \]
> correction 必须允许 arbitrary history dependence、ghosts、global certificates 和完整 partition dependence，并在代入 batch code 后不超过已知合法 upper bounds。

在 \(\varepsilon=1/2\) 时，任何仍推出 (17) 的 correction 都至少必须消除每 key

\[
0.0581951984104467
\tag{37}
\]

bits 的虚假 gap；这只是由 uniform count-vector upper bound强迫的必要条件，不是充分条件。若 correction 后还能严格超过最佳已证 monotone/普通基准，才可能形成新的下界 theorem。

与 D-choice 对应的另一条精确开放命题是 deletion-information dichotomy：要么构造一个普通 key-only dynamic filter，以接近 support entropy 的状态通过 bounded repair/epoch recycling 控制 ghosts；要么证明任何实现该 support process 的 transducer 都必须额外保存线性 deletion witness。它是有意义的结构问题，但目前不如 (36) 直接连接 KLZ/FOCS 2025 的主缺口。

## 9. 可对外使用与必须撤回的表述

可以严格使用：

1. Section 4 fixed-\(\delta\) 常数 (1) 对 history-dependent monotone filters 成立。
2. AND amplification 保持该模型，故 (2)--(3) 对 history-dependent monotone filters 成立。
3. Section 5 reconstructible sets 依赖 \(\pi\)，原 Claim 4.6 的固定集合条件没有由 Lemma 5.3 的三项性质保证。
4. 不加 correction 的 lifting 被 (26) 定量反驳。
5. 简单独立 thinning 只修复 measurability，不恢复 factorial layer functional。

目前必须撤回或标为 conditional：

1. “\(1.199273n\) 是普通 arbitrary-filter 下界”；
2. “Section 5 只替换 accepted sets 即可逐字继承 Section 4 全部估计”；
3. “joint batch code 已给普通模型 \(1.253809n\) 下界”；
4. “two-choice support entropy 已经给出动态 filter upper bound”。

当前最诚实的 theorem boundary 是：\(1.199273n\) 属于 history-dependent monotone 子类；普通模型仍缺一个 partition-safe 的 branch/support 或 leakage-correction inequality。
