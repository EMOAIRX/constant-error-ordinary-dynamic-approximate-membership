# All-pivot 与 symmetric transition dual 的合成 barrier

> 日期：2026-08-13。状态：本文给出当前局部 relaxation 的精确 midpoint optimum、
> 两类 operational realizability pressure test，以及要超过 midpoint 必须新增的全局
> 信息。本文没有给出新的 asymptotic lower-bound constant。

## 1. 想要合成的两个对象

对 dual-weighted all-pivot batch experiments，记：

- `A`：posterior coordinate-union 带来的 source support cost；
- `D`：同一 coordinate union 内，posterior 相对满 rank list 的 entropy deficit；
- `C`：理想 hard full-fiber all-pivot rank saving；
- `T`：从 hard saving 中因 suffix/replacement transport 失败而扣除的 debit；
- `H`：唯一的 persistent state budget。

现有 chain rule 与 transport accounting 至多给

\[
A+D\le H,
\tag{1}
\]

\[
C-T\le H+o(n),
\tag{2}
\]

以及最乐观的 local posterior-pruning comparison

\[
0\le T\le D+o(n).
\tag{3}
\]

式 (1) 已经把 all-pivot dual weights归一化并对 final state只收费一次。有限
symmetric transition dual只能为式 (2)--(3) 提供额外局部约束；它没有独立的、可与
式 (1) 相加的 memory budget。

## 2. 精确 midpoint optimum

忽略 `o(n)`，固定 `A,C`，对所有满足式 (1)--(3) 的 `D,T` 最小化 `H`。由

\[
H\ge\max\{A+D,C-T\}
\]

及 `T<=D`，得到

\[
H\ge\max\{A+D,C-D\}.
\]

右侧在

\[
D=T=\frac{C-A}{2}
\tag{4}
\]

处取最小值

\[
\boxed{H=\frac{A+C}{2}.}
\tag{5}

因此任何只添加 `A,D,C,T` 的逐 parent线性/凸约束、且允许式 (4) 的 relaxation，
都不可能超过 midpoint。更多 pivots 或更精确的有限 dual weights不会改变这个事实。

## 3. 为什么式 (4) 不是纯代数伪影

### 3.1 Bounded-horizon operational witness

在 `U=[2n]`、half error 下，先用约 `0.622556n` bits保存一个包含 initial set 的
random accepted superset。每次 replacement 后更新该 superset，但把全部 replacement
labels原样追加到 persistent transcript。对

\[
T=o(n/\log n)
\]

次 replacements，transcript只占 `o(n)` bits。这个 ordinary key-only filter支持
所有该深度内 histories、zero-FN 与 pointwise FPR，却保持 static 一阶率。

所以任意只检查 fixed depth、常数个 transition orbits，甚至 `o(n/log n)` 条实际
路径的合成 LP，都不能产生线性 dynamic premium。它可以把局部 transport loss全部
存入尚未饱和的 transcript字段。

### 3.2 Arbitrary-history posterior/operational separation

absorbing parity transducer在 source endpoint只保存一个 parity cell，故不同
leave-one-out parents各自看到 positive posterior deficit和 source-list pruning；压缩
后所有 updates被忽略、queries全部 YES，故 full operational fiber在同样 suffix下
完全不缩小。它支持任意长合法 histories、逐 tape zero-FN和 half-error pointwise
FPR。

cover-and-tombstone给出同一现象的非吸收版本：source endpoint上的 tombstone与
exception字段全零，不贡献 source mutual information；未访问 replacement branches
却可把它们写成大 continuation metadata。因此 endpoint posterior看见的 deficit与
operational transition capacity可以分离。

这两个例子不提供低空间 arbitrary-history upper bound；它们证明的是：不存在只由
posterior、有限 transition probes和 ordinary causality推出 `D+T` 单次收费的普适
lemma。

## 4. 有限 symmetric dual 能做什么

`U=4,n=2` 的五轨道 dual严格证明三状态 depth-3 optimum FPR为 `29/45`。它说明
right-congruence compatibility确实比 static covering更强，且识别出五类必要测试：

- initial ghosts；
- full pair snapshots；
- insert-delete residual ghosts；
- delete-then-insert 对旧 key 的 ghosts；
- delete-then-insert 对第三方 key 的 collateral acceptance。

但该 dual的 premium位于中间 histories。不同 gadgets顺序执行时，mutable memory可先
支付一个 gadget、删除其信息，再支付下一个。故它不能与式 (1) 直接相加，也不能靠
普通 tensor product变成 asymptotic width theorem。

正确的渐近推广必须把有限五轨道变成同一个 color上的指数多个 simultaneous
counterfactual branches，而不是线性多个 sequential probes。

## 5. 必须新增的最小全局信息

有两个等价接口。

### 5.1 Source-to-operational thickness

对 active state `q`，令 `P_q` 是 KLZ source completions，`O_q` 是全部 operational
histories。需要证明 `P_q` 在所有 dual-active suffix sections上同时支配 `O_q` 的某个
共同 prior，例如

\[
\Pr_{P_q}[E]\ge2^{-o(n)}\Pr_{\nu_q}[E]
\tag{6}
\]

对指数多个 suffix events `E` 同时成立。它将禁止“source list很薄、operational
continuations很厚”的 absorbing/tombstone witness。

### 5.2 Branch-response width

先商掉 query-silent state，得到 future-response quotient `Q_bar`。对同一个 color
`q`，考察全部未访问 replacement probes的完整 response table

\[
T(q)=\bigl(\text{response}(q,p)\bigr)_{p\in P}.
\tag{7}
\]

需要一个 width theorem：若当前 cell接近 Carter-optimal且式 (7) 在大量 branches上
保持低 false-positive penalty，则 successor response tables必须占据指数多个 colors。
该 theorem必须在 coordinate erasure上 sharp，并允许 public tapes之间的极端
reliability allocation。

只有式 (6) 或式 (7) 这样的 invariant，才能排除 midpoint equality witness (4)。

## 6. 判停条件

一个拟议的 all-pivot/transition inequality若满足任一项，应立即判停：

1. 只检查实际 source paths，不检查未访问 branches；
2. 对不同时间的 transition premiums求和，却没有 simultaneous-live width解释；
3. 没有先商掉 query-silent XOR fields；
4. 在 coordinate-erasure的 `0/1` reliability allocation上重复收费；
5. 只使用 `o(n/log n)` replacement depth；
6. 把 source posterior pruning自动当作 full operational-fiber shrinkage。

## 7. 裁决

all-pivot profile constraints与当前 symmetric transition constraints的直接 convex/LP
closure仍有精确 midpoint witness，不能产生超过 midpoint barrier 的 asymptotic
theorem。失败并非 dual weights不足，而是 relaxation没有记录 source fibers在完整
replacement tree中的厚度和 recurrence。

下一步最小任务不是继续增加 orbit或 pivot，而是先证明一个单-parent、future-minimal
response-table inequality；若该命题失败，给出 future-minimal反例即可形成干净的
barrier result。只有单-parent版本成立后，joint single-budget才值得研究。
