# Joint transportable-section rank-volume theorem：hostile audit

> 日期：2026-08-16。审计对象：
> `JOINT_REPLACEMENT_RANK_VOLUME_LOWER_BOUND_2026_08_16.md`。
> 裁决：joint-volume entropy proof、operational-section transport 与 shadow
> hierarchy 成立；它是一般 structural lower bound，不是 unrestricted universal
> constant 已解。

## 1. Source history 与 operational fiber 的量词

Source 对每个 $t$-set 使用一条预先固定、与 tape 独立、exact time 相同的合法
history。Filter 可以 history-dependent；这里只选择一个 hard source path。

Full operational fiber 仍固定：

- tape；
- physical state；
- logical load；
- exact operation time。

Append word还必须位于 promised horizon 内。若 random-tape cursor 不显式存入
physical memory，固定 exact time保证比较的 histories读取同一 tape位置。

Actual canonical endpoint 必在该 fiber 中，因此 conditional source support 必被
operational section completion 覆盖。没有假设 canonical endpoint state 或
source-cover equality。

## 2. Joint triple 的分布

$S$ uniform in $\binom Ut$，再取 uniform $A\subseteq S$ 与 uniform
$B\subseteq U\setminus S$。映射

$$
(S,A,B)\longleftrightarrow(A,B,K=S\setminus A)
$$

是到全部 disjoint size-$(a,b,k)$ triples 的等重双射。因此 joint source entropy
确实是

$$
\log\binom ut+\log\binom ta+\log\binom{u-t}b.
$$

给定 $(S,R)$ 后，随机选择 $(A,B)$ 与 state $M$ 条件独立，所以

$$
I(A,B,K;M\mid R)=I(S;M\mid R).
$$

这一步是 suffix-source MI cancellation 的全部来源；没有假设 $A,B$ 与 $S$
独立。

## 3. Conditional support count

固定 $(R,M)=(r,m)$。每个 actual triple 满足

$$
S=A\cup K\in\mathcal O_r(m,t,q),
\quad A\subseteq S,
\quad S\cap B=\varnothing.
$$

所以 $K$ 属于 residual family，继而属于任意 $d$-shadow clique completion。对全部
$(A,B)$ 求和给出 $\Phi^{(d)}_{r,m}$。Completion 可以包含大量并非真实 endpoint
的 spurious $K$；这只扩大 conditional list，使 lower bound 变弱，不会造成错误。

## 4. Envelope multiplicity

若 $K$ 属于某个 completion，则 residual shadow 的 ground set包含于 operational
union $W$，且 $A\subseteq W$，所以 $A\cup K$ 是 $W$ 的一个 $t$-subset。

对 fixed $t$-set $T\subseteq W$：

- $A$ 至多有 $\binom ta$ 种；
- $B$ 必须避开 $T$，至多有 $\binom{u-t}b$ 种。

因此

$$
\Phi^{(d)}_{r,m}
\le\binom wt\binom ta\binom{u-t}b.
$$

这里没有把 completion candidates 误当成 actual operational endpoints；只使用了
一个 many-to-one counting envelope。

## 5. 一份 state budget

Successor state不作为 message 发送。给定 tape、parent state与 concrete $(A,B)$，
fixed-tape determinism 已经确定 successor state。因此 theorem 只使用

$$
I(S;M\mid R)\le H.
$$

若改为分别发送 parent 与 successor，会得到 $2H$ 并失去意义；主证明没有这样做。
同时必须明确：entropy inequality只计算 parent operational sections；fixed-word
lemma证明这些 sections可运输到 successor，但当前 theorem没有对 candidate-dependent
successor accepted sets调用 FPR。

## 6. Logical reversibility 不等于 physical reversibility

Fixed word 在 compatible logical domain 上是双射，但 full successor fiber 可以
包含来自其他 parent states 的 merged images。

最小例：parent state $m$ 的 fiber含 $\{1,3\}$，另一个 state $m'$ 的 fiber含
$\{1,4\}$；word Delete$(1)$、Insert$(2)$ 把两个 physical states 都映到 $n$。
从 $m$ 的 image 只有 $\{2,3\}$，但 $n$ 的 inverse-compatible full section还含
$\{2,4\}$。执行 inverse word也不必恢复 $m$。主定理只声明 image inclusion，未
声明 full-fiber equality。

## 7. Pointwise FPR 的使用

对 fixed source set $S$ 与 fixed nonmember $z$，若
$z\in W_R(M_R(S))$，则同 tape、同 physical state存在一个 operational witness
把 $z$ 作为 member。Zero false negatives 强迫 actual source state也回答 YES。
所以先对原 tape 使用 pointwise FPR，得到

$$
\Pr_R[z\in W_R(M_R(S))]\le\varepsilon.
$$

再对 $z,S$ 求和才得到 $\mathbb Ew\le t+\varepsilon(u-t)$。证明没有在条件于
$(R,M)$ 后重用 FPR，也没有把两个 endpoint 的共同 ghost probability错写为
$\varepsilon^2$。

## 8. Shadow hierarchy 的端点

对 $d=1$，completion 是 residual union 上的全部 $k$-sets；这就是 rank-1 theorem。

对 $d=k$，completion 等于 residual family本身，并且

$$
\Phi^{(k)}_{r,m}
=|\mathcal O_r(m,t,q)|\binom ta\binom{u-t}b.
$$

因此 hierarchy 从 query-visible union rank 单调插值到 full operational-support
count。不能跳过中间步骤并声称 point queries自动控制 $d=k$；这正是剩余 open gap。

## 9. Covering-design barrier 的范围

$O(\log u)$ family 使 $\Delta^{(1)}=0$ 的例子只证明：rank-1 section unions不能
推出 operational family 很厚。它不构成一个 low-space fully dynamic filter upper
bound，也不否决高阶 shadow theorem。

Collision-cylinder propagation 同样只是严格 seed。不同 core replacement paths
可以因 holonomy 到达不同 physical representations，所以不能把它静默升级为
canonical Johnson-slice quotient。后续 width theorem必须直接处理 history tree 上的
merge/reuse，并对 public-tape reliability allocation 作 convexification。

因此可以声明：

1. joint transportable-section rank volume 给出无 suffix-MI penalty 的一般 lower bound；
2. 任何 rank deficit 都在 Carter rate外逐 bit收费；
3. fixed-word residual structure与全部 shadows精确 transport；
4. rank-1/union-only closure 有严格 design barrier。

不能声明：

1. 某个 fixed $d$ 对全部 ordinary filters 都有线性 premium；
2. recurrent right congruence 已强迫高阶 shadow 暴露；
3. unrestricted ordinary constant-error lower bound 的 universal constant 已提高。
