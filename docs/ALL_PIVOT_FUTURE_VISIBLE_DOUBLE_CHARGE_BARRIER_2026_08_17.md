# All-pivot excess 与 future-visible rank 的重复计费 barrier

> 状态：严格结构性 no-go；它不是新的 numerical lower bound。

## 1. 结论

Full-fiber all-pivot、multicut prefix-union 和 replacement-rank 不能仅因名字或 decoder
不同就作为独立 premiums 相加。同一个 mutable state statistic 可以同时表现为

- within-union posterior deficit；
- full-section rank deficit；
- deletion 后可观察的 future query-response distinction。

因此，未来 converse 中允许额外收费的量必须是**条件于已有 all-pivot message 后的
novel information**，而不是同一 syndrome 的另一种 rank 或 visibility 度量。

## 2. Exact fingerprint-count witness

取 fully random public hash

$$
h:U\to[B]
$$

并保存每个 bucket 的 exact current multiplicity

$$
c=(c_1,\ldots,c_B),
\qquad
\sum_jc_j\le n.
$$

Insert/Delete 对相应 count 加减；query $x$ 当且仅当 $c_{h(x)}>0$ 时回答 `YES`。
这是 ordinary、任意长、key-only、zero-false-negative filter。其固定 state 数为

$$
\binom{B+n}{n},
$$

所以 persistent memory 为

$$
H_{\rm fix}=\log_2\binom{B+n}{n}.
$$

取满足

$$
(1-1/B_n)^n\ge\frac12
$$

的最小整数 $B_n$。则 $B_n\sim n/\ln2$，load-$n$ pointwise FPR 至多 $1/2$，且

$$
H_{\rm fix}=2.3844998424\ldots n+o(n).
$$

## 3. The same deficit in two guises

固定 public hash $h$ 和 count vector $c$。Operational fiber 是所有在每个 bucket
恰有 $c_j$ 个 members 的 $n$-sets，记为 $\mathcal F_c$。其 support union $W_c$ 是
所有 occupied buckets 的并。

相对于只知道 $S\subseteq W_c$ 的粗 code，exact fiber deficit 是

$$
D(c)
=\log_2\binom{|W_c|}{n}-\log_2|\mathcal F_c|.
$$

这个同一个 $D(c)$ 同时是：

1. within-union posterior/all-pivot excess，因为 posterior support 从
   $\binom{W_c}{n}$ 缩到 $\mathcal F_c$；
2. full-section exact-rank premium，因为合法 source section 的 rank 也恰为
   $|\mathcal F_c|$。

它也不是 query-silent junk。若某 occupied bucket 的 count 是 $1$，删除其唯一 member
后该 bucket 立即从 accepted union 消失；若 count 至少为 $2$，同一次删除后仍接受该
bucket。因而 count statistic 决定合法 deletion suffix 后的 query-response row，属于
genuinely future-visible state information。

在 $u/n^2\to\infty$、uniform $n$-set source 下，standard occupancy asymptotics 给出

$$
A=n-o(n),
$$

$$
D_{\rm AP}=D_{\rm rank}
=1.28790401364596\ldots n+o(n).
$$

所以裸加会错误地要求

$$
A+D_{\rm AP}+D_{\rm rank}
=3.57580802729192\ldots n-o(n),
$$

而真实 fixed codebook 只有

$$
H_{\rm fix}
=2.3844998424785\ldots n+o(n).
$$

## 4. Consequence for converse synthesis

任何拟议证明若先把 $D(c)$ 作为 all-pivot/posterior saving 收费一次，再把同一个
fiber 的 exact 或 future-visible rank 作为独立 premium 收费一次，就会在上述合法
ordinary filter 上重复计算同一 count information。

安全的 chain-rule 形式只能是

$$
H
\ge
A
+I(X;M\mid C,W),
$$

或把第二项下界为某个 branch-response statistic 的**条件互信息**。不能从两个
unconditional deficits 分别成立推出

$$
H\ge A+D_{\rm all\text{-}pivot}+D_{\rm rank}.
$$

## 5. Positive interface left open

设 $W$ 是现有 all-pivot message 已决定的 coarse support，$P$ 是与 source 独立的
probe，$Y$ 是由 $(M,C,P)$ 决定的 future response statistic。Data processing 给出

$$
I(X;Y\mid C,W,P)
\le
I(X;M\mid C,W).
$$

所以 branch response 可以作为同一 residual information budget 的可观测下界；它
不能在该 budget 之外再收费。真正可能改进 $1.6079$ 的目标，是对 KLZ probe family
证明这个 conditional response information 在 all-pivot extremal profiles 上仍为
$\Omega(n)$，并在一个统一 code 中只收费一次。

Multicut prefix-union 本身只记录 coarse union mass。它与 all-pivot endpoint 在公共
source/profile 上重合，因而不自动提供上述 conditional novelty。
