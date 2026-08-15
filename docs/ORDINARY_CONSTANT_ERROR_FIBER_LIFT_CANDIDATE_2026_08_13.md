# 普通动态 Filter 的常数误差下界：全 fiber 提升候选

> 日期：2026-08-13。状态：候选新定理，正在 hostile audit。本文绕开 KLZ Section 5 中依赖随机 partition 的 reconstructible set，改用与 partition 无关的完整 state fiber。在逐项核对完成前，不应引用为已证结果。

所有对数以 2 为底。

## 1. 候选主结论

考虑 KLZ Definition 2.1 的普通动态 approximate-membership 模型：固定容量 \(n\)，固定 \(H\)-bit memory，免费只读公共随机带，支持 key-only Insert/Delete/Query；允许完整 history dependence 和 non-monotone accepted sets；成员永不 false negative；对每条固定合法历史和每个固定当前非成员，false-positive probability 至多固定常数 \(\varepsilon\)。

候选结论要求

\[
\frac{|U|}{n^2}\longrightarrow\infty
\]

并支持 KLZ obfuscating tree 所需的超线性长度更新序列。定义

\[
B(\delta)=\log\frac1\delta+(1-\delta)\log e-2h_2(\delta).
\]

候选定理是

\[
\boxed{H\ge n\sup_{k\ge1}\frac{B(\varepsilon^k)}k-o(n).}
\tag{1}
\]

特别地，在 \(\varepsilon=1/2\) 时，整数最优值为 \(k=5\)，从而

\[
\boxed{H\ge1.1992732344471508\ldots n-o(n).}
\tag{2}
\]

若证明闭合，式 (2) 将是 ordinary、history-dependent、non-monotone 模型中的新显式常数下界；它不依赖 HI、accepted-set monotonicity、exact counts、cell locality 或有限 churn。

## 2. 完整 state fiber

固定 filter tape \(r\)。对一个物理状态 \(m\) 与逻辑基数 \(s\le n\)，定义

\[
\mathcal F_r(m,s)
=\{S\subseteq U:|S|=s,\ \exists\text{合法历史 }h,\ S(h)=S,\ M_r(h)=m\},
\]

以及

\[
W_r(m,s)=\bigcup_{S\in\mathcal F_r(m,s)}S.
\tag{3}
\]

这里量化全部合法 histories，不要求 conform to 任何 partition。

### Lemma 2.1（accepted-union）

\[
S(h)\subseteq W_r(M_r(h),|S(h)|)\subseteq A_r(M_r(h)).
\tag{4}
\]

第一项由真实历史本身作 witness。若 \(x\in W_r(m,s)\)，则某条到达同一状态 \(m\) 的合法历史以包含 \(x\) 的集合结束；zero false negatives 强迫状态 \(m\) 接受 \(x\)，证明第二项。因此 \(W\) 继承 pointwise FPR 上界。

### Lemma 2.2（measurability repair）

条件于完整 obfuscation sequence \(\sigma\) 与 filter tape \(r\) 后，每个 endpoint state、endpoint cardinality 和相应的 \(W_r(m,s)\) 都是固定对象。它不依赖随机 partition 中未由 \(\sigma\) 暴露的 assignments。

因此 KLZ Claim 4.6 的 removing-\(U_k\) 计算可对 \(W(F_r)\setminus W(G_\ell)\) 使用。这正是原 Section 5 reconstructible set 缺少的性质。

## 3. Witness-conflict 近似 transport

令状态 \(m\) 的逻辑基数为 \(s\)。对每个 \(y\in W_r(m,s)\)，固定一个 witness set

\[
S_y\in\mathcal F_r(m,s),\qquad y\in S_y.
\]

从 \(m\) 执行一段对真实 endpoint 合法的 self-contained suffix \(w\)，到达 \(m'\)。记 \(I(w)\) 为 suffix 中被插入过的 distinct labels。因为 suffix self-contained，它不会删除初始集合中的键。

### Lemma 3.1（deterministic survival）

若 \(S_y\cap I(w)=\varnothing\)，则 \(w\) 对 witness history 也合法，且 \(y\) 在其 endpoint 仍为成员。因此

\[
W_r(m,s)\setminus W_r(m',s')
\subseteq\{y:S_y\cap I(w)\ne\varnothing\}.
\tag{5}
\]

### Lemma 3.2（随机 suffix 的期望损失）

若 suffix 的 \(L\) 个 distinct labels 从大小 \(V\) 的 fresh pool 无放回抽取，并且该随机性独立于起点 state/tape 与预先固定的 witnesses，则

\[
\mathbb E|W_r(m,s)\setminus W_r(m',s')|
\le |W_r(m,s)|\frac{sL}{V-L+1}.
\tag{6}
\]

KLZ 整棵深度 \(b\)、分支参数 \(M=4^b\) 的树最多有

\[
L_{\rm tree}<\frac{nM^{b+1}}b
\]

个 label occurrences。对每个相关 prefix-suffix pair，式 (6) 的粗界给

\[
D_n=O(n^2M^{b+1}/b).
\tag{7}
\]

必须选择 \(b\to\infty\) 足够慢，使

\[
bD_n=o(|U|),\qquad 9^{b^2}=o(|U|/n^2).
\tag{8}
\]

\(|U|/n^2\to\infty\) 允许这样的 diagonal choice。

## 4. 代入 Section 4

Witness-conflict transport 给

\[
\mathbb E|W(F_r)\setminus W(G_\ell)|
\le\mathbb E|W(F_r)|-\mathbb E|W(G_\ell)|+D_n.
\tag{9}
\]

沿 \(G_0,\ldots,G_b\) 同样有相邻 drop 至多 \(D_n\)。将 profile 单调化：

\[
\widehat w_k=\mathbb E|W(G_k)|+kD_n.
\tag{10}
\]

则 \(\widehat w_k\) 非降，且

\[
\widehat w_b\le (1-\delta)n+\delta|U|+bD_n
=((1-\delta)n+\delta|U|)(1+o(1)).
\tag{11}
\]

由 \(\widehat w_k-\widehat w_{k-1}\) 定义非负 layer increments。Claim 4.7 的 coupling 只使用 endpoint histories 的 distributional identity，所以把 accepted-set size 换成 partition-free \(W\)-size 后仍成立。Claim 4.6 由 Lemma 2.2 恢复。式 (9) 只给每个 batch 的 candidate-set bound 增加 \(D_n\)，而式 (8) 保证归一化 slack 在 KLZ Lemma 4.8 中为 \(o(1)\) 并且总通信损失为 \(o(n)\)。

因此，若上述 conditioning 逐式闭合，固定误差 \(\delta\) 的 ordinary filter 满足

\[
H\ge nB(\delta)-o(n).
\tag{12}
\]

## 5. AND amplification

取原误差-\(\varepsilon\) filter 的 \(k\) 个独立随机带副本，并对 query 取 AND。它仍是 ordinary、history-dependent、non-monotone filter，空间 \(kH\)，误差至多 \(\varepsilon^k\)。对固定 \(k\) 应用式 (12)，再除以 \(k\) 并优化，即得式 (1)。在 \(\varepsilon=1/2\) 时 \(k=5\) 给式 (2)。

## 6. 尚未闭合的 proof obligations

1. 对每个 \(G_\ell\to F_r\) suffix，证明条件于起点 transcript 后，future labels 仍满足式 (6) 所需的无放回均匀性；已暴露 labels 需单独扣除。
2. 证明 witness 选择不依赖 future suffix labels。
3. 将式 (9)--(11) 精确代入 KLZ Lemmas 3.4 与 4.8，验证每 batch slack 与总 slack 都是 \(o(n)\)。
4. 核对 Bob 可从 public tape、state 与 cardinality 枚举 \(W\)；空间模型不限制时间，但需明示有限 universe 与可计算性。
5. 重新逐项推导 fixed-error \(B(\delta)\)，不能沿用 \(\delta=o(1)\) 简化。
6. 做完整优先权检索。

## 7. 当前判断

这条路线若通过六项审计，就达到 SODA 级最低门槛：完整 ordinary 模型、明确的新线性常数、partition-free lifting lemma，以及对 FOCS 2025 常数误差开放问题的实质推进。

代价是 universe 假设加强为 \(|U|/n^2\to\infty\)。这不是结构性数据结构假设，但必须明确写进标题、摘要和定理。
