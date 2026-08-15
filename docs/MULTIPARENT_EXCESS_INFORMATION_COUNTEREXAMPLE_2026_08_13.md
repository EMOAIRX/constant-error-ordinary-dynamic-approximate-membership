# Multi-parent excess information：XOR 反例与 replacement-response 前沿

> 日期：2026-08-13。状态：一般 posterior direct-sum 的严格渐近反例；ordinary
> transducer 中的严格 query-silent embedding；一个避开该反例、但尚未证明的
> replacement-response 候选命题。所有对数以 2 为底。

## 1. 普通 total correlation 不是正确余项

令

\[
X_1,\ldots,X_s\stackrel{\rm iid}{\sim}\operatorname{Unif}(\mathbb F_2^L),
\qquad
M=X_1\oplus\cdots\oplus X_s .
\tag{1}
\]

则对每个 parent (i)，给定其余 coordinates 后，(M) 完全确定 (X_i)：

\[
I(X_i;M\mid X_{-i})=L.
\tag{2}
\]

另一方面

\[
I(X_{1:s};M)=L,
\qquad
\operatorname{TC}(X_{1:s}\mid M)=L.
\tag{3}
\]

因此当 (s>2) 时，

\[
\sum_{i=1}^s I(X_i;M\mid X_{-i})=sL
>2L
=I(X_{1:s};M)+\operatorname{TC}(X_{1:s}\mid M).
\tag{4}
\]

取 (s,L\to\infty) 即得到真正的 growing-parent 反例，而不是固定字母表或固定
depth 的压力测试。

正确恒等式使用 conditional dual total correlation（也称 binding information）

\[
\operatorname{DTC}(X_{1:s}\mid M)
=H(X_{1:s}\mid M)
-\sum_i H(X_i\mid X_{-i},M).
\tag{5}
\]

只要 (X_i) 先验独立，就精确有

\[
\boxed{
\sum_i I(X_i;M\mid X_{-i})
=I(X_{1:s};M)+\operatorname{DTC}(X_{1:s}\mid M).
}
\tag{6}
\]

式 (1) 中 (operatorname{DTC}=(s-1)L)，所以式 (6) 取等。这说明把 TC 换成
DTC 虽可修正公式，却不会产生 lower-bound gap；DTC 正是“同一 (L)-bit parity
被 (s) 个 leave-one-out parents 重复使用”的精确费用。

## 2. 该机制与 ordinary arbitrary-history transitions 相容

给任意合法 dynamic AMQ 增加一个 persistent 字段

\[
Z(S)=\bigoplus_{x\in S}g(x)\in\mathbb F_2^L,
\tag{7}
\]

其中 (g:U\to\mathbb F_2^L) 在 public tape 上。插入或删除 (x) 都执行

\[
Z\leftarrow Z\oplus g(x).
\tag{8}
\]

query 完全忽略 (Z)。于是：

1. updates 是 ordinary key-only deterministic transitions；
2. 支持任意长合法 history；
3. zero false negatives 与每条 fixed history/key 的 pointwise FPR 完全不变；
4. 从同一 final state和 (X_{-i}) 可恢复第 (i) 批的 checksum。

若每批含至少两个、来自足够大独立 bucket 的 keys，则固定 batch checksum 后，
posterior 仍有 full coordinate projections，但 thickness 少约 (L) bits。因而同一
final (L)-bit 字段可以在任意多个 parent posteriors 中各制造 (L)-bit deficit，
而不改变任何 query behavior。

这不是一个低空间 AMQ upper bound：字段 (Z) 是冗余的。它严格说明的是，online
transition compatibility 本身不排除 XOR/product-code posterior；任何仅使用
parent unions、posterior deficits、final-state mutual information与普通 TC 的
multi-parent inequality都不成立。

## 3. 必须先商掉 query-silent state

把 deterministic implementation 的 update maps 在非法 inputs 上任意 totalize。
定义两个 physical states (q\sim_{\rm fut}q')，若对每个有限 update word以及
其后的每个 query，它们给出相同答案。令

\[
\bar Q=Q/\!\sim_{\rm fut}
\tag{9}
\]

为这个 Moore machine 的 future-behavior quotient。这个定义刻意比“共同合法
continuations”更强，从而确实是 transition congruence；totalization只会把商分得
更细，不会虚假合并 operationally distinguishable states。式 (7) 的不同 checksum
states 在该商中相同；所以
任何声称“nonrectangular posterior 必导致 query distortion”的命题，若不先通过
式 (9)，都会被 query-silent XOR 立即否决。

注意这一步不能作为一般空间无损 canonicalization：它只是定义证明中可观测的
behavioral variable，不能把原数据结构的 memory charge降为
(log|\bar Q|)。原 state 仍应按 (H) bits收费。

## 4. 一个明确的 replacement-response 候选命题

固定 tape-independent 的 probe family (mathcal P_i)。其中每个 probe 是：从第
(i) 个 KLZ parent开始，插入一个从未在真实 history 中访问过的 replacement
batch，执行固定 delete suffix，再对一批 fresh keys查询。令

\[
T_i(q)=\bigl(\text{所有 }p\in\mathcal P_i
\text{ 从 }q\text{ 出发得到的 response vectors}\bigr)
\tag{10}
\]

为完整 counterfactual response table；实际使用的是
(T_i(\bar q))，所以 query-silent fields自动消失。

令 (K_i) 是第 (i) 个 parent中理想 hard transport/rank saving，(C_i) 是
decoder 在该步已有的 side information。令 (L_i) 是 probe family 中由 false
positives 或 ALL-YES branches造成的精确 log-list penalty。最小有用的单 parent
命题是

\[
\boxed{
K_i
\le
I(X_i;T_i(\bar Q_i)\mid C_i,R,\mathcal P_i)
+L_i+o(m).
}
\tag{11}
\]

multi-parent版本还必须要求 probes 与 conditioning 按一个共同 decode order选择，
使

\[
\boxed{
\sum_i I(X_i;T_i(\bar Q_i)\mid C_i,R,\mathcal P_{1:s})
\le H.
}
\tag{12}
\]

式 (11)--(12) 若成立，就给

\[
\sum_i K_i\le H+\sum_iL_i+o(n),
\tag{13}
\]

而 pointwise FPR与 replacement sampling应控制 (sum_iL_i)。这比
“overlap deficit 为正”更明确：它指定了随机变量、conditioning order、单一
(H)-bit budget以及必须由 FPR 支付的失败项。

当前式 (11) 与式 (12) 都是候选，不是定理。尤其 parent state由 final state加
不同 decoded side information得到；若 response tables不能按同一个 decode order
测量，式 (12) 仍会重复收费。

## 5. 三个敌对模型的压力测试

### Query-silent XOR

式 (7) 在 future-behavior quotient中消失，因此不贡献式 (11) 的 mutual
information。它也不改变 (K_i)。所以候选不会把冗余 parity误当成可重复的
transport credit。

### Coordinate erasure

对 tracked coordinates，replacement response table必须区分 exact exception
branches，信息进入式 (11) 第一项。对 erased coordinates，所有相应 branches
永久回答 YES，信息项可以为零，但损失进入 (L_i)。因此不能同时让两项都小。

### Frozen mask / cover-and-tombstone

mask 或 cover内部的 replacement branches具有近矩形 behavior，但 fresh query在
这些 branches上以相应 mask/cover密度回答 YES，进入 (L_i)。cover外的 insertion
进入 exact-exception字段，未来 response table必须区分它，进入 mutual-information
项。大 tombstone/exception字段在 source endpoint为零并不绕过 probes，因为式
(10) 显式访问此前未走过的 continuation branches。

这三项只说明候选通过了已知反例，不构成证明。

## 6. 最小研究分叉

第一步应只证明有限参数的式 (11)：对一个 parent、一个固定 replacement probe
family，response-table information与 FP log-list penalty是否覆盖全部 pruning
saving。若失败，应给出 reduced transducer反例；query-silent辅助字段不再算反例。

第二步才研究式 (12)。若 overlapping KLZ parents的 response tables不能由共同
final state按一个 decode order联合收费，则应构造一个 future-minimal
right-congruent transducer，使该失败达到 (Omega(n))。这将成为真正的 barrier
theorem。若能收费，再与 pointwise FPR的 oblivious replacement averaging结合，
才可能把 (u\gg n^2) 的 hard-transport converse推进到 (u\gg n)。

因此当前最强裁决是：一般 multi-parent posterior/TC路线已被 XOR严格关闭；尚未
被关闭的最小对象不是另一个 entropy deficit，而是 future-minimal transition
table在未访问 replacement branches上的联合 response information。
