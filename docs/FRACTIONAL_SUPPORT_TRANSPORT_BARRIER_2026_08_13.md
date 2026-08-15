# Fractional support--transport barrier

> 日期：2026-08-13。状态：有限参数解析定理与 lossless-coding no-go。
> 本文严格否决把 truncated、quantile、sampled 或 fractional fiber support
> 作为 full-fiber union 的局部替代，从而直接把 universe 条件从
> `u >> n^2` 降到 `u >> n`。本文不是 AMQ space lower bound，也不否决把
> state information 与 transport 联合收费的全局路线。

所有对数以 2 为底。

## 1. 设置

设 `n | u`，把大小为 `u` 的 universe 分割成

\[
U=B_1\sqcup\cdots\sqcup B_K,
\qquad K=u/n,
\qquad |B_i|=n.
\tag{1}
\]

考虑 endpoint fiber

\[
\mathcal F=\{B_1,\ldots,B_K\},
\tag{2}
\]

并令真实 endpoint `S` 在 `\mathcal F` 上均匀。给每个 key 一个 fractional support
weight

\[
w_x\in[0,1].
\tag{3}
\]

允许整个 weight vector 随机，但其随机性必须独立于随后抽取的真实 endpoint
和 suffix labels。硬 support 是 `w_x in {0,1}` 的特例；随机抽若干 witness、
多阈值 mixture 和 randomized quantile support 均包含在这个形式内。

定义真实 endpoint 的期望 escape mass

\[
E(w)
=\mathbb E_{S\sim\mathcal F}
  \sum_{x\in S}(1-w_x).
\tag{4}
\]

从 `U` 中均匀无放回抽取 `q` 个 distinct insertion labels，记其集合为
`Y`。执行这些 insertions 时，一个替代 endpoint `B_i` 能被共同 transport
当且仅当

\[
B_i\cap Y=\varnothing.
\tag{5}
\]

定义由冲突 blocks 丢失的 fractional support mass

\[
L_q(w,Y)
=\sum_{i:B_i\cap Y\ne\varnothing}
  \sum_{x\in B_i}w_x.
\tag{6}
\]

这里 `L_q` 只测量 common-suffix transport 的局部损失；它不计 physical state
或 endpoint posterior 的信息量。

## 2. 精确 barrier theorem

### Theorem 1（fractional support--transport identity）

对任意 deterministic weight vector `w` 和 `0 <= q <= u`，采用约定
`binom(u-n,q)=0` when `q>u-n`，有

\[
\boxed{
\mathbb E_Y L_q(w,Y)
=\left(\sum_{x\in U}w_x\right)
 \left[1-\frac{\binom{u-n}{q}}{\binom uq}\right].
}
\tag{7}
\]

又因为

\[
E(w)
=n-\frac1K\sum_{x\in U}w_x,
\tag{8}
\]

所以有精确 tradeoff

\[
\boxed{
\mathbb E_YL_q(w,Y)
=\frac un\,[n-E(w)]
 \left[1-\frac{\binom{u-n}{q}}{\binom uq}\right].
}
\tag{9}
\]

特别地，若 `E(w) <= eta n`，则

\[
\boxed{
\mathbb E_YL_q(w,Y)
\ge(1-\eta)u
 \left[1-\frac{\binom{u-n}{q}}{\binom uq}\right].
}
\tag{10}
\]

当 `nq=o(u)` 时，

\[
\mathbb E_YL_q(w,Y)
\ge(1-\eta)nq\,(1-o(1)).
\tag{11}
\]

### 证明

每个 block 被均匀 `q`-set `Y` 命中的概率相同，恰为

\[
p_q
=1-\frac{\binom{u-n}{q}}{\binom uq}.
\tag{12}
\]

对式 (6) 逐 block 使用线性期望，得到

\[
\mathbb E_YL_q(w,Y)
=p_q\sum_i\sum_{x\in B_i}w_x
=p_q\sum_xw_x,
\]

证明式 (7)。另一方面，真实 endpoint 在 `K` 个 blocks 上均匀，故

\[
E(w)
=\frac1K\sum_i\sum_{x\in B_i}(1-w_x)
=n-\frac1K\sum_xw_x,
\]

得到式 (8)--(10)。最后，

\[
1-\frac{\binom{u-n}{q}}{\binom uq}
=1-\prod_{j=0}^{q-1}\left(1-\frac n{u-j}\right)
=\frac{nq}{u}(1-o(1))
\]

在 `nq=o(u)` 下成立，推出式 (11)。证毕。

### Corollary 2（randomized supports）

若 `w` 还依赖一份独立 public randomness，则式 (9) 对该 randomness 再平均后
仍逐字成立。

证明。先条件于 weight vector 使用 Theorem 1，再取期望。因式 (9) 对
`E(w)` 为线性的，不产生 Jensen slack。

因此下列所有局部方案都不能绕过式 (10)：

- 只保留 section multiplicity 超过某个阈值的 keys；
- 随机抽取有限或增长数量的 witness histories；
- 对多个阈值作 mixture；
- 给每个 key 一个按 posterior degree 决定的 fractional weight；
- 在不同 public tapes 上随机选择不同 support rules。

## 3. 更强的 endpoint-capture 版本

若 hard support `A subseteq U` 要求

\[
\Pr_{S\sim\mathcal F}[S\subseteq A]\ge1-\eta,
\tag{13}
\]

则 `A` 必须完整包含至少 `(1-eta)K` 个 blocks。因此

\[
|A|\ge(1-\eta)u,
\tag{14}
\]

且随机 suffix 造成的期望 hard-support loss至少为

\[
(1-\eta)u
\left[1-\frac{\binom{u-n}{q}}{\binom uq}\right].
\tag{15}
\]

所以把“低 expected member escape”加强成“高概率完整覆盖真实 endpoint”不会
修复障碍，反而给出同一 tradeoff 的更直接版本。

## 4. Lossless escape-code corollary

考虑一个 rank-based lossless batch protocol：decoder 使用 retained support
编码落在 support 内的真实 keys，落在 support 外的 keys 通过大小为 `V` 的
ambient block作 escape rank。设一个大小为 `m` 的真实 batch 平均有 `e`
个 escapes，并令随机变量 `E <= m` 是实际 escape 数。即使忽略发送 escape
pattern 的成本，仅发送这些 values 的期望成本也至少为

\[
\mathbb E\log(V)_{\underline E}
\ge \mathbb E[E]\log(V-m+1)
=e\log(V-m+1)
\tag{16}
\]

bits。这里逐 realization 使用
`log(V)_{underline E} >= E log(V-m+1)`；没有把随机 `E` 错换成其均值。
若普通 support rank 的目标成本是 `Theta(m)`，并且 `V/m -> infinity`，
要使 escape overhead 为 `o(m)`，至少需要

\[
e=o\left(\frac{m}{\log(V/m)}\right).
\tag{17}
\]

因此 endpoint escape fraction必须满足

\[
\eta=o\left(\frac1{\log(V/m)}\right).
\tag{18}
\]

当 batch source 中每个坐标具有同一个 endpoint posterior，且 retained rule
逐坐标使用上述 weights 时，平均 escape fraction正是
`eta=e/m`。在这个明确接口下，将式 (18) 代入式 (10)--(11)，每个 fresh
insertion仍造成

\[
(1-o(1))n
\tag{19}
\]

量级的 local support loss。故 ambient-rank escape不能把 full-fiber proof 的
birthday-scale transport条件降为 `u/n -> infinity`。

另一种选择是用真实 endpoint posterior 对 escapes 作 arithmetic coding。但
此时 exact chain rule 给出

\[
H(\text{escape pattern})
+H(S\mid\text{escape pattern})
=H(S).
\tag{20}
\]

posterior pruning得到的 log-loss恰由 branch description补回。若没有额外的
multi-parent/state-information inequality，这种 soft code不会产生动态
communication saving。

### 范围说明

式 (16)--(20) 否决的是“support truncation加局部 escape code”这一协议模板。
它不是所有可能 lossless communication protocols 的 lower bound。

## 5. Hostile boundaries

### 5.1 Frozen mask

frozen-mask filter 的典型 fiber不是式 (2) 的 disjoint thin family。被精确跟踪的
coordinates固定后，未跟踪区域产生一个厚 cylinder；大量 endpoint共享同一
support，随机 insertion通常不会整块删除一批 rare witnesses。

Theorem 1 不声称 frozen mask 必有大 transport loss。正确的全局 theorem必须
允许 frozen mask 由低 transport项支付，并允许 tape-wise reliability allocation。

### 5.2 Global ALL-YES coin

在 ALL-YES tapes 上，endpoint fiber可以是全部 `n`-sets，section cores极小，
transport稳定；在可靠 tapes 上则由 state information支付。Theorem 1 只固定
一个 thin fiber，不允许把不同 tapes当独立证书重复收费，因此不与 global coin
冲突。

### 5.3 Static random cover

一个 static accepted superset `A` 对应的 fiber近似 `C(A,n)`，也是厚 family。
它可以沿纯 deletion冻结并保持低 transport。Theorem 1 不否决 static cover；
它说明相反端点的 thin fibers不能靠局部 truncation伪装成厚 fibers。

### 5.4 Rare-witness poisoning

传统 poisoning 是“一个厚 core family加许多 degree-one endpoints”。Theorem 1
给出更强的极端：全部 endpoints 都是 degree-one block witnesses。任何 quantile
rule若删掉这些 endpoints，就付出真实 endpoint escapes；若保留它们，就付出
线性 transport loss。

## 6. 为什么这不是 AMQ lower bound

式 (2) 的 fiber 本身携带很大的 endpoint information。若要用这种 disjoint-block
fibers覆盖全部 `n`-sets，physical state必须区分大量不同 partitions/cells。
在存在相应 resolvable design 的参数上，一个 cell只覆盖 `u/n` 个 endpoints，
所以仅静态计数已要求约

\[
\log\binom un-\log(u/n)
\tag{21}
\]

bits，接近 exact-set representation。

因此 Theorem 1 不是一个低空间 dynamic-filter construction，也没有反驳 ordinary
AMQ 的强下界。它只证明：thin fibers的困难不能在每个 fiber内部，通过选择一个
较聪明的 support消除；其成本必须由全局 state budget识别并收费。

## 7. 最小 global functional

令 uniform source endpoint为 `S`，public filter tape为 `R`，physical state为
`M`。对每个 `(R,M)` 允许选择任意 fractional support

\[
w_{R,M,x}\in[0,1].
\]

一个可能绕过 Theorem 1 的正确对象必须至少联合三个量：

\[
\boxed{
I(S;M\mid R),
\qquad
\mathbb E\sum_{x\in S}(1-w_{R,M,x}),
\qquad
\mathbb E L_q(w_{R,M},Y).
}
\tag{22}

所需 theorem 的定性形式是

\[
I(S;M\mid R)
+\operatorname{EscapeCost}(w)
+\operatorname{TransportCost}(w)
\ge \operatorname{SourceRequirement},
\tag{23}
\]

并且全部 layers只能使用同一个 `H`-bit state budget：

\[
I(S;M\mid R)\le H.
\tag{24}
\]

式 (23) 必须满足：

- disjoint-block fibers主要由 `I(S;M|R)` 支付；
- frozen masks和static covers主要由低 transport支付；
- global ALL-YES coin只在 tapes上分配一次 reliability；
- rare witnesses按 source incidence收费，但 decoder仍对真实 batch lossless；
- 多个 KLZ pivots不能重复收取同一个 final-state information。

本文没有证明式 (23)。它只是 Theorem 1 之后仍未被否决的最小全局接口。

## 8. 结论

严格得到的是：

1. fractional endpoint escape与随机 suffix transport之间的有限精确恒等式；
2. 对 randomized、quantile、multi-threshold和sampled-witness supports的统一
   no-go；
3. ambient-rank与exact-posterior两类 natural escape codes的障碍；
4. 一个必须显式加入 state information 的最小后续 functional。

没有得到的是：

1. `u >> n` 下新的 ordinary AMQ lower bound；
2. 对所有 lossless protocols的普适不可能性；
3. full-fiber `u >> n^2` 条件本身的必要性；
4. 任何低空间 AMQ upper bound。

所以安全结论是：**局部 support truncation不能去掉 birthday-scale universe
条件；下一步必须证明 state-information/escape/transport 的全局联合不等式。**
