# Monotone 动态 Membership 的常数误差放大下界

> 日期：2026-08-13。状态：主定理对 history-dependent monotone filters 成立；经 KLZ Section 5 提升到普通 non-monotone filters 仍有 partition-dependence 缺口。本文不宣称得到普通模型或常数误差下的紧界。

## 1. 结论

考虑 KLZ/FOCS 2025 的动态 approximate-membership 模型，并保留 Section 4 的 accepted-set monotonicity：容量为 (n)，使用固定 (H)-bit memory，支持任意合法插入和删除；允许免费无限只读随机带；成员从不产生 false negative；对每条预先固定的合法历史、每个时刻和固定当前非成员 (x)，false-positive probability 至多 (\varepsilon)。不假设 history independence、canonical state、cell locality 或 exact multiplicity recovery。

定义

\[
L_{\rm KLZ}(\delta)
=
\log_2\frac1\delta
+(1-\delta)\log_2 e
-2h_2(\delta),
\qquad 0<\delta\le \frac12.
\tag{1}
\]

完整保留 KLZ Proposition 4.3（Section 4）中的固定误差项，可以得到 history-dependent monotone 单副本下界

\[
H\ge nL_{\rm KLZ}(\delta)-o(n).
\tag{2}
\]

式 (2) 本身在 (delta=1/2) 为负，因而无用。核心观察是先对任意 filter 做独立 AND 放大，再把式 (2) 应用于放大后的 filter。

### Theorem 1：monotone 模型中放大后的 KLZ 下界

设 (\varepsilon\in(0,1/2]) 为固定常数，(|U|/n\to\infty)，原 filter 为 history-dependent monotone filter，且能支持 KLZ obfuscating-tree proof 所需的 (omega(n)) 次合法更新。则对每个固定整数 (k\ge1)，

\[
\boxed{
H
\ge
\frac{n}{k}L_{\rm KLZ}(\varepsilon^k)-o(n).
}
\tag{3}
\]

因此

\[
\boxed{
H
\ge
nR_{\rm amp}(\varepsilon)-o(n),
\qquad
R_{\rm amp}(\varepsilon)
=
\max_{k\ge1}
\frac{L_{\rm KLZ}(\varepsilon^k)}{k}.
}
\tag{4}
\]

在 (\varepsilon=1/2) 时，整数最优值为 (k=5)，从而

\[
\boxed{
H
\ge
1.1992732344471508\,n-o(n).
}
\tag{5}
\]

这严格超过：

- Carter 静态下界 (n-o(n))；
- Lovett--Porat 原文正式证明的 (1.1n)；
- 其单层数值最优 (1.10213\ldots n)；
- 其 Section 3.5 中未给参数证书的递归搜索值约 (1.13n)。

本文目前没有完成足以断言“文献最优”的系统优先权检索。上述比较只针对已经直接核对的论文表述。

## 2. 为什么放大保持 history-dependent monotonicity

取原 filter 的 (k) 份独立副本。第 (j) 份副本使用一段彼此独立的随机带 (R_j)，状态记为 (M_j)。

- `Initialize`：独立初始化所有副本；
- `Insert(x)`：对所有副本执行同一个合法插入；
- `Delete(x)`：对所有副本执行同一个合法删除；
- `Query(x)`：仅当所有副本均返回 YES 时返回 YES。

合并状态为

\[
M^\wedge=(M_1,\ldots,M_k),
\]

故固定 memory 长度为 (kH) bits。操作历史在每个副本中完全相同，所以若它对原逻辑集合合法，也对每个副本合法；更新次数不增加。

若 (x) 是当前成员，每个副本都确定性返回 YES，因此 AND 结构仍无 false negative。

若 (x) 是固定当前非成员，对任意预先固定的合法历史 (h)，第 (j) 份副本的 false-positive event

\[
E_j(h,x)
=
\{\operatorname{Query}_{R_j}(M_j(h),x)=\mathrm{YES}\}
\]

只依赖独立随机带 (R_j)，且

\[
\Pr[E_j(h,x)]\le\varepsilon.
\]

因此

\[
\Pr\left[\bigcap_{j=1}^kE_j(h,x)\right]
=
\prod_{j=1}^k\Pr[E_j(h,x)]
\le
\varepsilon^k.
\tag{6}
\]

注意 independence 是在固定历史 (h) 和固定 query key (x) 后使用的。这里没有条件于某个副本的随机状态再调用 FPR，也不允许历史依赖随机带；因此没有 state-conditioned FPR 漏洞。

放大结构正是一个容量 (n)、误差 (delta=\varepsilon^k)、空间 (kH) 的 history-dependent monotone filter。将式 (2) 应用于它，得到

\[
kH
\ge
nL_{\rm KLZ}(\varepsilon^k)-o(n).
\]

固定 (k) 时除以 (k)，即得式 (3)。

## 3. 单副本固定误差引理

KLZ 原证明发送 (b) 个 hidden batches，每批大小 (n/b)。若不把 (delta=o(1)) 吸收到 (o(n)) 中，Section 4 对 monotone filters 的总通信比较给出

\[
H
\ge
n\left[
-h_2(\delta)
-(1-\delta)\log_2\delta
+(1-\delta)\log_2(1-\delta)
+(1-\delta)\log_2e
\right]
-o(n).
\tag{7}
\]

利用

\[
h_2(\delta)
=
-\delta\log_2\delta
-(1-\delta)\log_2(1-\delta),
\]

式 (7) 化为式 (1)--(2)。

三项线性损失为

\[
2h_2(\delta)+\delta\log_2e:
\]

第一个 (h_2) 来自逐 key hit bit，第二个来自 hit/miss location mixture，(delta\log e) 来自 factorial saving 只发生在 miss branch。obfuscation、random partition 和 reconstructible-set reduction 在固定 (delta)、(|U|/n\to\infty) 时仍只损失 (o(n))。

完整常数审计见 [KLZ_FIXED_EPSILON_CONSTANT_AUDIT.md](./KLZ_FIXED_EPSILON_CONSTANT_AUDIT.md)。

## 4. 数值曲线

在 (0<\varepsilon\le1/2) 上，对整数 (k) 优化式 (4) 得到：

| (\varepsilon) | 最优 (k) | (R_{\rm amp}(\varepsilon)) | 静态率 (log_2(1/\varepsilon)) | 线性动态 gap |
|---:|---:|---:|---:|---:|
| 0.01 | 1 | 7.910538008 | 6.643856190 | 1.266681819 |
| 0.05 | 1 | 5.119694469 | 4.321928095 | 0.797766374 |
| 0.10 | 2 | 3.955269004 | 3.321928095 | 0.633340909 |
| 0.15 | 2 | 3.286826658 | 2.736965594 | 0.549861064 |
| 0.20 | 2 | 2.772129525 | 2.321928095 | 0.450201431 |
| 0.25 | 3 | 2.395974260 | 2.000000000 | 0.395974260 |
| 0.30 | 3 | 2.085468806 | 1.736965594 | 0.348503212 |
| 0.35 | 4 | 1.813635352 | 1.514573173 | 0.299062179 |
| 0.40 | 4 | 1.587457806 | 1.321928095 | 0.265529712 |
| 0.45 | 5 | 1.382152498 | 1.152003093 | 0.230149405 |
| 0.50 | 5 | 1.199273234 | 1.000000000 | 0.199273234 |

对相邻 (k) 的曲线求交，得到切换点：

\[
\begin{array}{c|c}
k&\varepsilon\text{ 区间}\cr
\hline
1&(0,0.0620466503]\cr
2&[0.0620466503,0.2119061641]\cr
3&[0.2119061641,0.3369744618]\cr
4&[0.3369744618,0.4318595557]\cr
5&[0.4318595557,0.5].
\end{array}
\]

这些端点为数值近似；定理本身使用离散最大值，不依赖端点认证。(o(n)) 项只允许固定 (k)，不能令 (k=k(n)) 无限制增长；所列区间的最优值都由固定有限 (k\le5) 达到。

## 5. 敌对测试

### 5.1 Frozen mask

单副本可使用高度相关的全局 false-positive mask；放大证明不要求同一副本内不同 keys 或不同时刻的 hit events 独立。只要求不同副本使用独立随机带。故 frozen mask 不击穿式 (6)。

### 5.2 Global ALL-YES coin

每个副本可用一个 global ALL-YES branch。(k) 份独立副本同时落入该 branch 的概率至多 (\varepsilon^k)。合并结构的 fixed worst-case memory 是 (kH)，没有按随机 branch 平均状态数。

### 5.3 Shared witnesses

一个副本内可用低熵证书同时接受大量 keys。证明不按 key 收费，而是把整个放大结构作为一个新的普通 filter 送入 KLZ protocol；证书共享被包含在其 (kH)-bit state 内。

### 5.4 Ghosts

删除后各副本可以继续接受 deleted key。放大只使用 pointwise FPR 和 one-sidedness，不要求 last-copy rejection、multiplicity recovery 或 deletion-distinguishability。

## 6. 当前没有解决的点

### 6.1 与 tight constant 仍有大 gap

2026 uniform-fingerprint multiset upper bound 在 (\varepsilon=1/2) 的 Poisson source rate 为

\[
\rho(1/2)=2.287904014\ldots
\]

bits/key，而式 (5) 只有 (1.199273234\ldots)。即使考虑已探索的 nonuniform fingerprint phase transition，monotone-filter 下界仍离候选最优率很远；普通 arbitrary-filter 下界还没有由本证明建立。

### 6.2 这不是 transition-sensitive sharp inequality

放大使用 deletion 的方式仅来自底层 KLZ proof。它没有给出 transition-constrained fiber covering 的精确极值，也没有解释 fingerprint occupancy 为什么应当最优。

### 6.3 优先权风险

独立 AND repetition 是标准 error-reduction 操作。真正的新意只能是：把它与 KLZ 固定误差常数函数组合，得到此前未记录的 history-dependent monotone-filter 常数曲线。投稿前必须核查：

- Lovett--Porat 及其后续是否已经对任意 lower-bound function 做过相同放大；
- KLZ 的后续版本或 2026 follow-up 是否已记录此 corollary；
- 更一般的非同质 product、随机 (k) 或 threshold composition 是否给出更强 black-box envelope。

因此当前最安全的表述是“已证候选新 corollary”，而不是“首次证明”。

### 6.4 单副本引理需要正文级重写

[KLZ_FIXED_EPSILON_CONSTANT_AUDIT.md](./KLZ_FIXED_EPSILON_CONSTANT_AUDIT.md) 已记录常数，但若投稿 monotone theorem，必须把 Lemma 4.5、Claims 4.6--4.7 与 Lemma 4.8 完整重写，明确所有 (o(n)) 对固定 (delta) 一致。reconstructible-set lifting 是另一个尚未解决的问题，不能作为这条 theorem 的一部分。

### 6.5 黑盒 Boolean composition 的边界

在只知道每个副本 pointwise marginal FPR 至多 (\varepsilon) 的黑盒模型中，AND 已经支配所有 monotone Boolean query rules。若某个 rule 在并非 all-ones 的输入 pattern 上也接受，可以构造合规且跨副本敌对相关的 filters，使该 pattern 以概率一出现，而 composition 的 FPR 变为一。只有要求所有副本均 YES 的 rule 对任意内部相关机制稳健。

这里的独立副本 construction 主动使用独立随机带，所以 all-ones 概率乘成 (\varepsilon^k)。非同质副本若需要不同 base errors，则不能从一个给定的 (\varepsilon)-filter 纯黑盒地产生；必须引入额外变换。因此在“复制同一个 filter + monotone Boolean rule”的范围内，式 (4) 是自然的 sharp envelope。

## 7. 更强 batch inequality 的状态

正在审计的目标是联合编码一个 hidden batch 的 branch pattern 和无放回 support，从而把单副本函数提升为

\[
B_{\rm joint}(\delta)
=(1-\delta)
\log_2\frac{e(1-\delta)}{\delta}.
\tag{8}
\]

若式 (8) 在普通 KLZ transcript 上成立，则同样放大可给

\[
H
\ge
n\max_{k\ge1}
\frac{B_{\rm joint}(\varepsilon^k)}k-o(n),
\]

在 (\varepsilon=1/2) 取 (k=4) 得 (1.2538091336n-o(n))。

但当前不能把式 (8) 视为定理。主要风险是：KLZ pivot states 和 reconstructible supports 依赖 hidden batch；条件于这些对象后，branch vector 不再自动服从由 support sizes 决定的超几何分布。必须由 obfuscation/fiber transport 给出相应 conditional symmetry，不能仅凭 pointwise FPR 或无放回抽样宣称成立。

## 8. 论文价值判断

式 (4)--(5) 是一个真实的 history-dependent monotone-model 正定量改进。它已经达到了“可以写成子类定理”的标准，而不是 ordinary-model conjecture。

不过，单靠一个标准 AND trick 与现有常数函数的组合，能否达到 SODA 的技术深度并不确定。较合理的 SODA package 是：

1. 证明 amplified KLZ envelope，并完成全面优先权审计；
2. 证明一个严格强于它的 transition-constrained batch lemma，或证明所有 black-box product/threshold compositions 的 sharp envelope；
3. 给出与 fingerprint occupancy 上界的结构比较，明确剩余 gap 来自哪一个 branch--support functional；
4. 最好进一步证明一种 composition barrier：仅使用 pointwise FPR、KLZ single-copy protocol 和 black-box Boolean composition，无法越过某个显式常数。

若第 2--4 项均没有推进，式 (5) 更像一篇重要 short note 或更大论文中的核心 lemma，而不应过度包装成 tight solution。

## 9. 当前下一步

最优先的两项是：

1. 完成 joint batch code 的 conditional-law 审计；若失败，给最小反例并保留式 (4) 作为主定理。
2. 将 AND 放大推广为 Boolean composition optimization。给定不同误差参数的独立副本和 monotone Boolean query rule，求单位总空间下 KLZ lower-bound certificate 的最优 envelope，并证明 AND 是否 black-box 最优。
