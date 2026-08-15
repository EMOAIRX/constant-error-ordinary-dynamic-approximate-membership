# 普通动态 Membership 的 SODA 突破前沿

> 日期：2026-08-13。本文是严格的研究审计，不宣称已经解决 KLZ/FOCS 2025 的常数误差开放问题。除明确标注“已证”外，所有主定理表述均为猜想或研究目标。

## 1. 结论

目前没有得到一个新的 SODA 级 arbitrary-filter 下界。真正的进展是把问题压缩到了一个更精确、且不能再靠隐藏假设绕过的核心：

> 对 KLZ obfuscating-tree 产生的一个 hidden batch，联合编码整批 hit pattern 与条件候选集合。证明即使 hit events 可由 frozen mask 或共享 rejection certificate 高度相关，二者的联合 branch--support 代价仍然具有线性下界。

这个结论比“每次删除产生信息”严格得多。普通模型允许完整 history dependence、全局相关状态和免费只读随机带；pointwise FPR 只控制每个固定键在随机带上的边缘概率。逐键相加、条件于状态使用 FPR、恢复 exact multiplicity、或把物理状态规范化为当前集合的函数，都是不合法的。

当前最小可证明的新语义工具是 common-legal-continuation fiber transport。它准确说明同一物理状态所混淆的隐藏集合怎样在共同合法更新下被运输，但它本身还不给出线性空间下界。

因此，一个可信的 SODA 主定理必须是新的 batch branch--support inequality 或等价的 transition-constrained fiber-covering theorem。单纯重算 KLZ 常数、联合编码 hit bits、bounded-churn direct sum、或 deletion certificates 的逐键求和都不够。

## 2. 唯一允许的主模型

固定完整随机带 \(r\) 后，filter 是任意确定性有限状态 transducer：

- 物理状态空间 \(\mathcal M_r\)，\(|\mathcal M_r|\le 2^H\)；
- query 接受集
  \[
  A_r(m)=\{x:\operatorname{Query}_r(m,x)=\mathrm{YES}\};
  \]
- labeled update 转移 \(\Delta_r(m,u)\)，其中 \(u\) 是 `Insert(x)` 或 `Delete(x)`；
- 状态可保存任意 routing、ghost、epoch、relocation、历史摘要和全局证书；
- 随机带免费、只读、可被更新和查询算法任意读取。

随机算法是这些 deterministic transducers 的公共随机混合。要求对每条固定合法历史 \(h\)、每个时刻和每个当前非成员 \(z\)，

\[
\Pr_r[z\in A_r(M_r(h))]\le\varepsilon,
\]

而成员在每条随机带上都必须返回 YES。

主定理中不能假设：

- history independence 或 canonical endpoint state；
- accepted-set monotonicity；
- exact multiplicity recovery；
- singleton witnesses 或 union preservation；
- cell-local query/update 或可加 memory decomposition；
- 删除时免费的 insertion-time orientation。

## 3. KLZ 原证明在常数误差下到底给什么

完整保留 Proposition 4.3 到 Lemma 5.3 中被 \(\varepsilon=o(1)\) 吸收的项，只得到

\[
H\ge nL_{\rm KLZ}(\varepsilon)-o(n),
\]

其中

\[
\boxed{
L_{\rm KLZ}(\varepsilon)
=\log_2\frac1\varepsilon
+(1-\varepsilon)\log_2 e
-2h_2(\varepsilon).
}
\]

在 \(\varepsilon=1/2\) 时，

\[
L_{\rm KLZ}(1/2)
=-0.2786524796\ldots,
\]

所以动态 communication 部分完全失效；此时已知的一 bit/key 只来自静态 Carter 下界。

相对低误差目标 \(\log(1/\varepsilon)+\log e\)，原协议损失

\[
2h_2(\varepsilon)+\varepsilon\log_2 e.
\]

三项来源分别是：

1. 逐 key 发送 hit bit 的 \(h_2(\varepsilon)\)；
2. hit/miss 分支与 location code 混合产生的第二个 \(h_2(\varepsilon)\)；
3. factorial saving 只在 miss branch 获得，损失 \(\varepsilon\log e\)。

obfuscation、随机 partition 和 reconstructible-set reduction 在固定 \(\varepsilon\)、\(|U|/n\to\infty\) 下只损失 \(o(n)\)。所以主障碍不在 KLZ Section 4--5 的 history-dependence 技术，而在 Section 3/4 的单字母发送规则。

## 4. 已证：fiber semantics 与 transport

固定随机带 \(r\) 和一族合法历史 \(\mathcal H\)。对物理状态 \(m\)，定义 state fiber

\[
\mathcal F_r(m)
=\{S:\exists h\in\mathcal H,
\operatorname{Set}(h)=S,
\operatorname{State}_r(h)=m\}.
\]

定义其 reconstructible support

\[
W_r(m)=\bigcup_{S\in\mathcal F_r(m)}S.
\]

### Lemma 4.1：accepted-union lemma（已证）

对任意物理状态 \(m\)，

\[
\boxed{W_r(m)\subseteq A_r(m).}
\]

证明：若 \(x\in W_r(m)\)，则存在一条到达同一 memory representation \(m\) 的合法历史，其真实集合包含 \(x\)。one-sidedness 要求在该 memory representation 上查询 \(x\) 返回 YES。query 只依赖 \(m,x,r\)，故 \(x\in A_r(m)\)。

这是 KLZ reconstructible set 的 fiber 表述，不依赖 HI、实际 accepted-set monotonicity 或 locality。

### Lemma 4.2：common-legal-continuation transport（已证）

令 \(w=(u_1,\ldots,u_t)\) 是一段具体 labeled update word，并定义

\[
\mathcal F_r(m;w)
=\{S\in\mathcal F_r(m):w\text{ 对 }S\text{ 全程合法}\}.
\]

对 \(S\in\mathcal F_r(m;w)\)，令 \(\Phi_w(S)\) 是执行逻辑更新后的真实集合。由于固定随机带后的转移是确定的，所有这些隐藏世界从同一 \(m\) 执行同一 \(w\) 后到达同一状态

\[
m_w=\Delta_r^w(m).
\]

若历史族对这些 continuations 闭合，则

\[
\boxed{
\Phi_w(\mathcal F_r(m;w))
\subseteq\mathcal F_r(m_w),
}
\]

从而

\[
\boxed{
\bigcup_{S\in\mathcal F_r(m;w)}\Phi_w(S)
\subseteq W_r(m_w)
\subseteq A_r(m_w).
}
\]

这个 lemma 是任何 deletion-transcript 证明的合法起点。特别地，若 `Delete(x)` 只对 fiber 的一部分合法，必须先限制到该共同合法 subfiber；不能选择依赖随机带或隐藏集合的 continuation。

## 5. 为什么单状态或逐删除信息论不够

### 5.1 Frozen-mask 压力测试

随机带选一个全局集合 \(G_r\subseteq U\)，使每个固定 \(x\) 满足

\[
\Pr_r[x\in G_r]=\varepsilon.
\]

结构可以让 \(G_r\) 中所有键永久返回 YES，并用另一部分状态保证 true keys。对任意固定非成员，边缘 FPR 仍为 \(\varepsilon\)，但一批键的 false-positive indicators 可以完全由同一个全局模式决定。

所以从 pointwise marginals 不能推出

\[
H(Z_1,\ldots,Z_b)\ge b h_2(\varepsilon)
\]

或任何按删除次数相加的 rejection entropy。

### 5.2 Shared rejection certificate

更一般地，状态可含一个低熵全局 certificate \(C\)，让一大簇 keys 同时 accepted/rejected。批量 rejection vector 只取少量全局模式。任何声称“每次 deletion 提供 \(\Omega(1)\) 独立信息”的 lemma 都是假的。

### 5.3 相关性必须与 support 一起收费

Frozen mask 并没有证明小空间可达：若 hit vector 极度相关，hit branch 的候选集合通常会很大。正确 tradeoff 是

\[
\text{branch-pattern entropy}
+\text{conditional support/location cost},
\]

而不是单独控制其中一项。

## 6. 精确的最小缺失 lemma

考虑 KLZ 一个 batch 中的 hidden distinct keys

\[
X=(X_1,\ldots,X_m),\qquad m=n/b,
\]

以及用于发送这个 batch 的两个 reconstructible sets \(\widetilde G_\ell\subseteq\widetilde F_r\)。令

\[
Z_i=\mathbf1[X_i\in\widetilde G_\ell].
\]

给定完整 hit vector \(Z=z\)，decoder 的合法位置集合分别是：

- \(z_i=1\)：某个 hit-side support \(B_z\subseteq U_k\)；
- \(z_i=0\)：某个 miss-side support \(D_z\subseteq(\widetilde F_r\setminus\widetilde G_\ell)\cap U_k\)。

原 KLZ proof 把坐标逐个发送，用 marginal FPR 和一阶矩分别放松。需要替换为以下 batch quantity：

\[
\mathsf{BS}_m
=H(Z)
+\mathbb E_Z\log N_Z,
\]

其中 \(N_Z\) 是在给定物理 pivot state、随机 partition、public tape 和 branch pattern 后，与 one-sidedness 及 common-continuation transport 相容的整个 ordered distinct batch 的候选数。

### Conjecture 6.1：joint branch--support inequality（未证，主缺口）

存在显式函数 \(J_m(\varepsilon;\mathcal T)\)，其中 \(\mathcal T\) 记录 KLZ prefix/transcript 的 fiber-transport 约束，使任意普通 filter 都满足

\[
\boxed{
H(Z)+\mathbb E\log N_Z
\le m\log |U_k|-mJ_m(\varepsilon;\mathcal T)+o(m).
}
\]

并且对某个固定 \(\varepsilon\) 区间，

\[
\liminf_{m\to\infty}J_m(\varepsilon;\mathcal T)
>
\text{KLZ single-letter saving}.
\]

若这个 inequality 在 obfuscating-tree/reconstructible-set transcript 上成立，则可直接替换 Lemma 4.5，得到一般 KLZ 模型中的显式新线性下界。若其极值由 fingerprint occupancy process 达到，才进一步得到 fingerprint optimality；这一点不能预设。

这比抽象的“transcript entropy conjecture”更精确：需要界的是 branch pattern 与 batch support 的联合码长，并且优化域必须允许 arbitrary correlation、frozen masks 和共享 certificates，同时保留 legal-continuation transport。

## 7. 已失败的推导

以下命题均不能作为论文 lemma：

1. **同一状态必须恢复 multiplicities。** 错。普通 filter 可以保留 ghosts；删除最后副本后不要求立刻回答 NO。
2. **同一 state fiber 中的集合必须 pairwise deletion-distinguishable。** 错。一个状态可以覆盖很多集合，只要 accepted set 覆盖其 union，后续状态覆盖 transported unions。
3. **删除后对固定 tape 或条件于当前 state，键以至少 \(1-\varepsilon\) 概率被拒绝。** 错。FPR 是对整个随机带的边缘概率，当前 state 本身依赖随机带。
4. **每次 deletion 贡献 \(h_2(\varepsilon)\) 或 \(\log(1/\varepsilon)\) 独立信息。** 错。frozen masks 和共享 certificates 直接反驳。
5. **多个 pivot states 的 entropy 可以相加。** 错。所有 pivots 都来自同一个 \(H\)-bit transducer；known update path 可能让整个 transcript 由一个状态重建。
6. **static survivors 与 incremental newcomers 的空间下界直接相加。** 错。全局 rejection certificate 可以同时服务两个任务；在 dense universe 中 frozen-mask 构造给出显式反例。
7. **Lovett--Porat 的 incremental 下界可经 dummy replacement 原样转移。** 未证。dummy reduction 只转移 fresh/distinct incremental lower bound；LP 原 proof 允许重复标签，其 continuation closure 在 fresh API 下会断裂。
8. **只联合编码 hit vector 就能消掉 KLZ 的 \(h_2(\varepsilon)\)。** 错。marginals 可独立；反过来，共享 mask 虽使 hit entropy 很小，却扩大 location support。
9. **2026 年 uniform entropy-array 上界解决了整个问题。** 错。它给 uniform fingerprints 的 whp near-entropy space/constant time，不给 arbitrary-filter converse，也不是 KLZ 的固定最坏 \(H\)-bit保证。

## 8. 一条更可执行的证明路线

### 阶段 A：先解决 monotone/HI warmup 的 exact batch functional

不应先在完整 obfuscating tree 上堆抽象。固定一对 nested accepted/reconstructible sets \(G\subseteq F\)，定义所有 permutation-symmetric joint laws

\[
(X^m,Z,B_Z,D_Z)
\]

满足：

- \(X^m\) 是从 \(U_k\) 无放回抽取的 ordered batch；
- \(Z_i=1\) 的边缘概率至多 \(\varepsilon\)；
- true-key inclusion；
- 给定 \(Z\) 后 decoder 可从相应 supports 无歧义恢复整个 batch；
- supports 来自同一个 physical-state fiber，而不是自由选择的集合。

先精确求

\[
\sup\bigl\{H(Z)+\mathbb E\log N_Z\bigr\}.
\]

只有当这个值严格低于 KLZ 逐键上界时，才存在可移植的线性 improvement。

### 阶段 B：证明 global-certificate extremality 或找反例

候选 optimizer 至少包括：

- independent Bernoulli hits；
- one-bit all-or-none frozen mask；
- 固定大小 global mask；
- 少量共享 certificates 的 mixture；
- higher-order overlapping witnesses。

必须证明极端相关性节省的 branch entropy 被 support term 完全补回，或者找到一个严格更优、可张量化的 joint law。后一种结果将指向超越 fingerprints 的构造，同样具有论文价值。

### 阶段 C：只移植新的 batch inequality

KLZ Section 4 已把 \(F_k,G_k\) 的状态分布耦合到足够接近；Section 5 已构造满足 prefix monotonicity 的 reconstructible sets。若阶段 A 的 inequality 只使用：

- state/query 可计算性；
- reconstructible-set inclusion；
- prefix/common-continuation transport；
- public-random partition 的 exchangeability；

则 obfuscation 和 nonmonotone reduction应只引入 \(o(n)\) 损失。若它要求 canonical endpoint distributions 或逐 tape FPR，就不能移植。

## 9. SODA 级成功标准

最小可接受主结果：存在固定常数区间 \(I\subset(0,1)\) 和显式 \(\Delta(\varepsilon)>0\)，在完整 KLZ 模型中证明

\[
H\ge n\bigl(L_{\rm known}(\varepsilon)+\Delta(\varepsilon)\bigr)-o(n),
\qquad\varepsilon\in I,
\]

其中 \(L_{\rm known}\) 至少包含最佳静态/既有 arbitrary-filter 下界；证明不能附加 HI、monotonicity、locality、exact counts 或 restricted update API。

更强结果：给出显式 multi-letter 变分值 \(L_*(\varepsilon)\)，证明

\[
H\ge nL_*(\varepsilon)-o(n),
\]

并给出匹配构造，或证明 \(L_*=R_{\rm FM}\)。

同样可接受的反向突破：构造可张量化普通 dynamic automaton，其完整物理状态、删除、公共随机带和 pointwise FPR 均合规，并严格低于所有 fingerprint-multiset rates。

以下不应包装为 SODA 突破：

- 只证明 fiber transport；
- 只改善 restricted fingerprint/exact-count 类；
- 只给 finite-state 数值；
- 只重算 KLZ 常数；
- 只提出抽象变分问题而无定量线性 improvement；
- 依赖 bounded-churn、WHI 或 dense-universe 特例却声称解决普通模型。

## 10. 现实判断

目前最有 taste 的主线不是继续添加假设，而是证明一个允许最坏全局相关性的 branch--support tradeoff。它直接解释 KLZ 常数误差证明为什么困难，也精确覆盖 frozen masks、共享 certificates、higher-order witnesses 与 deletion transport。

当前已经做到的是：

- 校准了最新 uniform-fingerprint 上界；
- 精确算清 KLZ 固定误差常数；
- 建立了无 HI/单调/locality 的 fiber transport lemma；
- 找到并杀掉了逐删除信息、multiplicity recovery、条件 FPR 和朴素 direct sum；
- 把 SODA 主定理缩小为一个明确的 joint branch--support inequality。

还没有做到的是最重要的一步：证明该 inequality 的线性 gap，或找到违反它的可张量化 automaton。因此现在应称为“定位到最小技术障碍的研究纲领”，不能称为已经取得 SODA 级突破。

## 参考基线

- Kuszmaul--Liang--Zhou, *Fingerprint Filters Are Optimal*, FOCS 2025, arXiv:2510.18129。
- Blelloch--Hu--Kuszmaul--Li--Zhou, *Dynamic Entropy-Encoded Arrays in \(O(1)\) Time with Nearly Optimal Space*, arXiv:2608.06066。
- Lovett--Porat, *A Space Lower Bound for Dynamic Approximate Membership Data Structures*, FOCS 2010 / SICOMP 2013，DOI `10.1137/120867044`。
- Li et al., *ChainedFilter: Combining Membership Filters by Chain Rule*, SIGMOD 2024 / arXiv:2308.13632。
- Guo--Li, *Hallucination is a Consequence of Space-Optimality: A Rate-Distortion Theorem for Membership Testing*, arXiv:2602.00906。该文提供静态 membership 的 output-distribution/KL 语言，但不处理动态 history-dependent transducers；其直接 data-processing lower bound只恢复静态项，不能替代上面的 transcript lemma。
