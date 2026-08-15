# Transition-compatible coverings：接近 static rate 的构造审计

> 日期：2026-08-13。状态：没有找到低于 (n) bits 的 ordinary dynamic
> construction。本文给出精确 formulation、已证 (n)-bit upper bound、一个
> (n=2) finite-horizon impossibility certificate，以及计算工具的边界。

## 1. 从 static covering 到 labeled transition system

令 (Omega_{le n}=\{S\subseteq U:|S|\le n\})。一个 deterministic tape 的
ordinary filter 是：

1. finite state set (Q)；
2. 对每个 key (x)，确定 maps (I_x,D_x:Q\to Q)；
3. 每个 state 的 accepted superset (A(q)\subseteq U)；
4. 每条合法 history (h) 到达 state (q(h))，满足 (S(h)\subseteq A(q(h)))。

定义 relational fiber

\[
\mathcal F(q)=\{S:\exists h, S(h)=S, q(h)=q\}.
\]

transition compatibility 的精确条件是

\[
I_x(\mathcal F(q)\cap\{S:x\notin S,|S|<n\})
\subseteq\mathcal F(I_xq),
\tag{1}
\]

\[
D_x(\mathcal F(q)\cap\{S:x\in S\})
\subseteq\mathcal F(D_xq),
\tag{2}
\]

其中左边表示对 fiber 中所有共同合法 worlds 作相同 labeled logical update。
query correctness 强迫

\[
\bigcup_{S\in\mathcal F(q)}S\subseteq A(q).
\tag{3}

Static covering 只要求每个 (S) 至少有一个 (A\supseteq S)。式 (1)--(2)
要求同一 cover cell 中所有 worlds 对每个 label 使用同一个 successor。这正是
static Carter/ChainedFilter cover 通常缺失的结构。

随机 filter 是这些 deterministic labeled systems 的 public-tape mixture，并对
每条固定 history、固定 nonmember 强制 pointwise FPR。

## 2. 已证 (n)-bit construction

在 (U=[2n])、capacity (n)、(epsilon=1/2) 时，公共 tape 均匀选择
(n)-subset (G\subseteq U)。持久状态是由 (U\setminus G) 索引的 bit vector，
保存

\[
S\cap(U\setminus G).
\]

query 对 (G) 中 keys 永远 YES，对其余 keys读 exact bit。updates 只修改
(x\notin G) 的 bit。因此：

- fixed persistent memory 恰为 (n) bits；
- 支持任意长 history，无 overflow 或 rebuild；
- zero false negatives；
- 每个固定 nonmember 的 FPR 是 (Pr[x\in G]=1/2)。

这是一个 transition-compatible cylinder cover。它仍是当前最强严格 ordinary
fixed-state upper bound。Static dense covering rate (0.622556\ldots n) 没有已知
transition-compatible realization。

## 3. (U=4,n=2) 的 exact two-state obstruction

对所有 (2)-state deterministic key-only transducers作完全枚举：

- (8) 个 labeled operations (I_x,D_x)；
- 每个 operation 是 ([2]\to[2]) 的 arbitrary function；
- arbitrary initial state；
- query rule取 zero-FN 强迫的 minimal accepted union；
- 检查从 empty 开始深度至多 (3) 的全部合法 histories。

共有 (131072) 个 transducers、(206) 个不同 false-positive behavior columns。
对 columns 作任意 public-tape convex mixture，LP 的精确最优 worst pointwise FPR 是

\[
\boxed{3/4}.
\tag{4}

所以 (U=4,n=2,epsilon=1/2) 即使只要求 depth-3 histories，也不可能使用
两个 persistent states。一个 LP dual certificate 只支撑在四个 history-query
pairs，各权 (1/4)：

1. empty history，query key (2)；
2. `Insert(0), Delete(0)`，query (0)；
3. `Insert(2), Insert(3)`，query (1)；
4. `Insert(0), Insert(2), Delete(0)`，query (3)。

对每个 deterministic two-state transducer，这四个 constraints 中至少三个为
false positive；平均即得 (3/4)。该最后一句目前由 exhaustive enumeration
认证；要成为纯解析 lemma，需要对 two-state transition functions作短 case split。

因此最小实例已经严格否定“一 bit dynamic filter 可达到 static-style
(epsilon=1/2)”的希望，并与 (2^n=4) states conjecture 一致，但尚未证明
三 states 也不可能。

## 4. 计算审计边界

现有 column-generation MILP 能搜索 (q>2) states，但本轮结果不能作为证据：

- (q=3) run 没有完成可认证输出；
- (q=4) master 从单个 ALL-YES column 开始，pricing repeatedly 返回 zero-cost
  columns，而 master objective 仍为 (1)。这是缺少覆盖 dual directions 的 seed
  columns/degeneracy，不是 (q=4) impossibility。

因此当前唯一可引用的小例结论是式 (4)。不能把未收敛 column generation 解读为
三或四 states 的 lower bound。

下一次计算应：

1. 手工加入 balanced-cut deterministic columns作为 feasible incumbent；
2. 对 master dual 作 stabilization；
3. 保存每个 pricing column 的完整 transition table，便于提取 construction；
4. 至少跑到 reduced cost certificate 再报告 optimum。

## 5. 为什么 ghosts/history dependence 尚未给出构造

Ghosts 允许 deleted keys 继续 accepted，从而让 (A(q)) 变大；它可以简化
transitions，却直接消耗 FPR budget。History dependence允许同一个 (S) 有多个
representations，但每个 representation 仍需满足全部 labeled common-successor
constraints。Static cover 可以为每个 (S) 独立挑选一个精巧 accepted superset，
而 dynamic machine 必须在线选择 successors且不知道 fiber 中的 hidden world。

一个可能的 probabilistic-cover构造需要一族 accepted supersets和 transitions，使：

\[
\forall q,x,quad
\{S\cup\{x\}:S\in\mathcal F(q),x\notin S\}
\subseteq\mathcal F(q')
\]

对某个共同 (q') 成立，deletion 同理。随机独立 static covers 几乎必然不满足
这种 closure；简单将 successor 取 fiber union 会迅速扩张成 ALL-YES state。

## 6. 当前裁决

尚无接近 static Carter rate 的 full history-dependent ordinary dynamic AMQ。
当前证据是：

1. 严格 upper bound：(n) bits 的 balanced frozen mask；
2. 严格小例 obstruction：(n=2) 时两 states 即使有限 horizon 也只能做到
   FPR (3/4)；
3. static-optimal covers 缺少 labeled common-successor closure；
4. ghosts 的 transition便利与 accepted-union膨胀直接冲突。

这支持但没有证明 (n)-bit barrier。最有价值的下一步不是随机 sample 更多 static
covers，而是闭合 (U=4,n=2) 的三-state LP，随后观察 dual 是否推广成 Johnson
scheme 上的 labeled-cover inequality。若三 states 已可达到 (1/2)，应提取并
尝试张量化该 machine；若 optimum 仍大于 (1/2)，四 states 门槛将成为第一个
完整 finite theorem。
