# Support-only ghost recycling 的任意规模障碍

> 日期：2026-08-13。状态：Theorem 2.1 是任意规模解析定理，不要求 canonical
> representation、exact multiplicity recovery 或 history independence。它严格排除
> constant-state local support machines 在 label-level arbitrary churn 中维持常数
> pointwise error。本文同时说明为什么该定理不能直接升级为 ordinary public-hash
> AMQ lower bound。

## 1. 问题背景

support-only snapshot 之所以看起来便宜，是每个 exchangeability class只保存
一个 occupied bit。动态删除的困难不是 orientation：同类 copies 可以互换；真正
的问题是删除一份 copy 后，机器必须决定该 class 是否仍有成员。

允许 ghost 后，机器不必在最后一份 copy删除时立刻返回 empty。但任意长 churn
要求这些 ghosts以后能够回收，否则一个固定 zero-count history最终会永久回答
YES。下面的定理给出这件事的精确有限状态代价。

## 2. Unary ghost-recycling theorem

考虑容量为 \(N\) 的 unary dynamic membership API。逻辑状态是
\(c\in\{0,1,\ldots,N\}\)，支持：

- \(I:c\mapsto c+1\)，仅当 \(c<N\) 时合法；
- \(D:c\mapsto c-1\)，仅当 \(c>0\) 时合法；
- `Nonempty` query。

算法有免费公共随机带。固定随机带后，它是至多 \(K\) 个 persistent states 的
任意 deterministic machine；允许同一 logical count有多个 representations，也
允许不同 counts共享 state。只要求：

1. 当 \(c>0\) 时，每条 tape 上 query 都回答 YES；
2. 对每条预先固定、以 \(c=0\) 结束的合法 history，query 回答 YES 的概率至多
   \(\varepsilon\)。

### Theorem 2.1

任何这样的 machine 必须满足

\[
\boxed{K\ge (1-\varepsilon)N+1.}
\tag{1}
\]

特别地，在 \(\varepsilon=1/2\) 时，至少需要 \(N/2+1\) 个 local states。

**证明。** 固定一条 tape \(r\)，令 \(s_i(r)\) 是从初态连续执行 \(i\) 次
\(I\) 后的物理状态，\(0\le i\le N\)。定义

\[
B_r=\{i\in\{0,\ldots,N-1\}:\exists j>i,\ s_i(r)=s_j(r)\}.
\tag{2}
\]

序列 \(s_0,\ldots,s_N\) 中，每个出现过的物理状态至多有一个最后出现位置。
因此若不同状态数至多为 \(K\)，非最后出现位置至少有

\[
|B_r|\ge N+1-K.
\tag{3}
\]

对每个 \(i\in B_r\)，选某个 \(j>i\) 使 \(s_i=s_j\)。从这两个共同状态执行
相同 continuation \(D^i\)。它对 count \(i\) 和 count \(j\) 都合法；determinism
使两个 endpoints仍在同一物理状态。第一条 history

\[
h_i=I^iD^i
\tag{4}
\]

以 count zero结束，第二条 \(I^jD^i\) 以正 count \(j-i\) 结束。zero false
negatives强迫共同 state回答 YES，所以 tape \(r\) 在固定 zero history \(h_i\)
上产生 ghost false positive。

令 \(F_i(r)\) 是 history \(h_i\) 上的 false-positive indicator。上面证明

\[
\sum_{i=0}^{N-1}F_i(r)\ge N+1-K.
\tag{5}
\]

对随机带取期望。每个 \(h_i\) 都是在抽取随机带前固定的合法 history，所以可以
逐项使用 pointwise FPR：

\[
N+1-K
\le\sum_i\mathbb E F_i
\le\varepsilon N.
\tag{6}
\]

整理即得式 (1)。证毕。

## 3. 结论比 exact-count injectivity 弱在哪里、强在哪里

若要求每个 zero endpoint都精确回答 NO，Myhill--Nerode区分给 \(K\ge N+1\)。
Theorem 2.1 允许每条 tape留下任意 history-dependent ghosts，并且只使用每个固定
zero history 的平均 FPR。因此它是一个真正 approximate、public-coin 的下界。

但结论只要求 \(K=\Omega(N)\) states，即 \(\Omega(\log N)\) bits；它没有强迫
保存完整计数的 \(\log(N+1)\) 之外更多信息。其用途不是给整体 linear-bit lower
bound，而是严格否决“每个高 multiplicity class仍只需常数个 support/ghost状态”。

## 4. 对 state-dependent placement 的影响

exchangeable-fingerprint deletion lemma说明同一个

\[
(\text{unordered bucket pair},\text{fingerprint})
\]

class内不需要 per-key orientation。Theorem 2.1 补充了另一半：如果该 class可承载
\(N\) 份 copies，那么在 label-level semantics下，任意能长期回收 ghosts 的局部
machine需要 \(\Omega(N)\) states。

因此 state-dependent placement 可以消除 orientation metadata，却不能把
multiplicity recovery压成一个 occupied bit。可行结构仍必须采用以下至少一种：

1. class counter或 threshold residue；
2. dynamically allocated heavy-class state；
3. 跨 classes共享的全局 reversible syndrome；
4. 允许某些 tapes/histories将该 class永久并入 accepted region。

第 2 项需要保存 heavy-class identifier/allocation；第 3 项面对 one-sided safe
decoding；第 4 项消耗 pointwise reliability budget。

## 5. Ordinary public-hash 模型中的关键边界

Theorem 2.1 的 operations \(I,D\) 是 seed-independent labels。若一个 AMQ 的
exchangeability class由公共随机 hash决定，那么“选取 \(N\) 个都落在同一
class的 keys”通常依赖随机带。式 (4) 对应的 key history便不是抽取 tape前固定
的 history，不能合法调用 pointwise FPR。

这是从局部 multiplicity障碍到 arbitrary ordinary-filter lower bound 的准确缺口：

- 对每条坏 tape，universe中可能存在巨大的同类 key fiber；
- fixed memory要求结构在该 tape上仍有定义，可以暂时回答 ALL YES；
- 但 pointwise FPR不限制 adversary在看见 tape后选择这些 keys；
- 要收费，必须把 seed-dependent heavy fiber转成一族固定 histories的 fractional
  cover，并证明同一 tape会污染其中足够大的固定质量。

简单 union bound通常失败，因为指定 \(N\) 个固定 keys全落入同一 class的概率
可能指数小。一个一般 lower bound需要利用许多 overlapping fixed histories，或
证明 heavy-state allocation本身扩大了大量固定 keys的 accepted union。

## 6. Sticky-failure 不能解决任意长历史

另一个常见方案是：每个 epoch用新鲜公共 randomness建立 support-only layout；
一旦 overflow就进入 absorbing ALL-YES state。若每个固定 epoch在条件于过去未
失败时有失败概率至少 \(p>0\)，则执行 \(T\) 个固定 build/delete cycles 后，
absorbing failure概率至少

\[
1-(1-p)^T.
\tag{7}
\]

它随 \(T\to\infty\) 趋于一，违反任意固定 \(\varepsilon<1\) 的 pointwise FPR。
所以 polynomial-horizon typical-set/filter constructions不能通过“增加 tape长度”
自动升级为 arbitrary-history fixed-memory construction。

任意长模型中的 overflow state必须是可恢复的。恢复时若没有 exact set oracle，
机器必须保留足够的 reversible residue，使未来 deletions能把它带回可查询状态；
这正是 threshold quotient保存高负载 residue的原因。

## 7. 当前构造侧裁决

没有得到低于 heterogeneous fingerprint benchmark \(2.2006114830n\) 的严格普通
dynamic AMQ。support-only two-choice 的 \(2.1216107112n\) 仍只是 snapshot
entropy，差额约 \(0.07900n\) 必须容纳：

\[
\text{heavy-class identifiers}
+\text{ghost-recycling state}
+\text{zero-overflow fallback}.
\]

Theorem 2.1 严格证明 constant-state local ghost recycling不够；式 (7) 严格证明
sticky typical-set failure不能支持无限 history。剩余的真正可能性只有跨 class 的
全局 reversible quotient或一种 fractional heavy-fiber allocation，它既避免保存
identities，又能在所有 tapes上从 overflow恢复。目前没有这样的构造。

