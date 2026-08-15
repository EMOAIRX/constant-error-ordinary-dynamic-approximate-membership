# Posterior-aware batch code：exact cancellation 与二分之一 barrier

> 日期：2026-08-13。状态：严格信息论会计与抽象近等号反例。结论是：仅把
> `FULL_FIBER_TRANSPORT_INFORMATION_DICHOTOMY` 的 entropy deficit 与 state
> message 作 chain-rule cancellation，不能把原 all-pivot constant 从
> `u >> n^2` 搬到 `u >> n`。该接口最多给出
> `max{A+D,C-D}`，优化后为 `(A+C)/2`。要保留 `C`，必须再证明
> multi-parent overlap使同一 deficit不能同时支付全部 transport losses。

所有 logarithms 以 2 为底。

## 1. 单个 posterior section 的精确分解

令 `X` 是一个均匀 source，source entropy为 `S`。令 `M` 是 decoder首先得到的
physical state，公共 context记入 conditioning而省略。给定 `M=m`，source
posterior支持在一个 ambient hard-support list `Omega_m` 中。定义

\[
A_m=S-\log|\Omega_m|,
\tag{1}
\]

以及 posterior相对 ambient list的 entropy deficit

\[
D_m=\log|\Omega_m|-H(X\mid M=m)\ge0.
\tag{2}
\]

平均后写 `A=E A_M`、`D=E D_M`。因为 source均匀，exact chain rule给

\[
\boxed{I(X;M)=A+D.}
\tag{3}
\]

这正是 transport-information dichotomy 中

\[
I=\mathbb E\mathsf A(W)+\mathbb E\mathsf D_W(\mu)
\]

的抽象形式。`A` 是 Carter/static accepted-support information，`D` 是 fiber
在自身 union内的额外薄度。

## 2. Posterior-aware conditional message的硬下界

给定 state `M` 后，任何 lossless second-stage message `Y` 都满足

\[
\boxed{\mathbb E|Y|\ge H(X\mid M)=S-A-D-o(n),}
\tag{4}
\]

其中 `o(n)` 只容纳 prefix/Shannon coding overhead。Exact posterior arithmetic
code在式 (4) 取等。

另一方面，hard-support batch rank code在 transport完全理想时，若获得动态 saving
`K`，其期望长度形式为

\[
S-A-K.
\tag{5}
\]

若 suffix pruning/transport failure使候选 rank增大 `T` bits，长度变成

\[
S-A-K+T.
\tag{6}
\]

式 (4) 对式 (6) 给出必要条件

\[
S-A-D
\le S-A-K+T+o(n),
\]

即

\[
\boxed{K\le D+T+o(n).}
\tag{7}

这是 exact chain-rule cancellation 的正确方向。Entropy deficit `D` 不是可从
state message中扣掉的免费 credit；它恰好是 hard-support rank相对 posterior
optimal code的冗余。动态 rank saving只有在不超过这份冗余和 transport correction
时才可能存在。

## 3. 代入 transport-information dichotomy

新的 incidence theorem在 `u/n -> infinity`、suffix insertion count足够慢时给

\[
T\le D+o(n),
\tag{8}
\]

这里 `T` 用相对 log-shrinkage量度，并假定 batch rank degradation可由同一量以
系数 1 上界。将式 (8) 代入式 (7)，只能得到

\[
K\le2D+o(n),
\qquad
D\ge\frac K2-o(n).
\tag{9}

再由式 (3) 与 `I(X;M)<=H`，得到

\[
H\ge A+D
\ge A+\frac K2-o(n).
\tag{10}

若理想 hard-transport converse为

\[
C=A+K,
\tag{11}

则式 (10) 恰为

\[
\boxed{H\ge\frac{A+C}{2}-o(n).}
\tag{12}

同一个结论也可由两条 lower bounds直接写成

\[
H\ge A+D,
\qquad
H\ge C-T\ge C-D-o(n),
\tag{13}

所以

\[
\boxed{
H\ge\max\{A+D,C-D\}-o(n).
}
\tag{14}

对 `D>=0` 取最坏值，若 `C>=A`，

\[
\min_D\max\{A+D,C-D\}
=\frac{A+C}{2},
\qquad
D_*=\frac{C-A}{2}.
\tag{15}

因此 posterior-aware coding没有恢复旧 `C`；它只把 static baseline与旧 converse
取中点。

## 4. Half-error 数值含义

在 large-universe half error 下，static Carter baseline为

\[
A=1.
\tag{16}

使用已经认证的十块 all-pivot常数

\[
C_{10}>1.6079,
\]

式 (12) 只给

\[
H>1.30395n-o(n).
\tag{17}

它甚至弱于原先在更强 universe条件下的 endpoint/all-pivot constants。即使未来
连续 all-pivot极限数值约为 `1.7`，此接口也只给约 `1.35n`。

所以不能把 transport-information dichotomy局部从 `u >> n^2` 降到 `u >> n`
误写成旧 all-pivot theorem在相同 universe范围内自动成立。

## 5. 最小 exact posterior反例

取均匀 source

\[
X\in\{00,01,10,11\},
\qquad S=H(X)=2.
\tag{18}
\]

state `M` 只发送第一 bit，所以 `H(M)=1`；给定 `M` 后 posterior是相应两个
source words上的均匀分布，conditional entropy为 1。对每个 state故意令 hard
ambient list仍是全部四个 words，因此

\[
A=S-\log|\Omega_M|=0,
\qquad
D=\log|\Omega_M|-H(X\mid M)=1.
\tag{19}
\]

令理想 hard-rank analysis声称 `K=2` bits saving，而 transport使实际 rank
增加 `T=1` bit。则 second-stage hard message长度为

\[
S-A-K+T=2-0-2+1=1=H(X\mid M).
\tag{20}
\]

所以 posterior Shannon code和transport-degraded hard code同时取等；state的
1 bit加second-stage的1 bit正好无损编码2-bit source。与此同时

\[
A+D=1,
\qquad
C-D=(A+K)-D=1.
\tag{21}

两条 lower bounds都只能给1 bit，而理想无transport常数 `C=2`。这是一个有限、
exact、四元 source反例：任何只使用式 (3)--(8) 的推导都无法恢复 `C`。

它不是 ordinary AMQ transducer反例；它否决的是所提议的 information-accounting
lemma。若要利用 AMQ/KLZ额外结构排除它，必须加入 multi-parent overlap条件。

## 6. 一般抽象近等号 posterior

下面说明式 (15) 不是代数证明过松。固定任意 `A`、`K>0`，令

\[
D=T=K/2.
\tag{22}

取一个 posterior source，使 ambient hard list大小为

\[
|\Omega|=2^{S-A},
\]

而 posterior均匀支持在其中一个大小

\[
2^{S-A-D}
\]

的子集上。于是

\[
H(X\mid M)=S-A-D,
\qquad
I(X;M)=A+D.
\tag{23}

令理想 hard-support protocol声称 saving `K`，但 transport使 rank增加
`T=D`。其 second-stage长度为

\[
S-A-K+T
=S-A-D
=H(X\mid M).
\tag{24}

因此：

- posterior Shannon lower bound取等；
- transport inequality `T<=D` 取等；
- state information bound为 `A+D`；
- hard-rank bound为 `C-D=A+K-D=A+D`；
- 两条 lower bounds在 `(A+C)/2` 相交。

所有当前会计式同时饱和，所以仅靠重新排列 chain rule不可能排除式 (22)--(24)。

### Fiber近等号模板

该抽象例可以由 rare-support fiber近似。取 `W_0 subset W`，使

\[
\log\binom{|W|}{n}
-\log\binom{|W_0|}{n}
\approx D.
\tag{25}

posterior质量几乎全部均匀分布在 `binom(W_0,n)`，再给覆盖 `W\setminus W_0`
的 witness endpoints总计任意小正质量，使 posterior support union仍为 `W`。
一个删除这些 rare witnesses的 suffix把 union降到 `W_0`，产生

\[
n\log\frac{|W|}{|W_0|}\approx D
\tag{26}

的 relative transport loss，而 posterior entropy deficit也约为 `D`。令 rare
mass趋零即可逼近式 (22)--(24)。

这是一种 near-equality机制说明，不是已形式化的 AMQ construction：要使随机
suffix的期望 loss精确等于式 (26)，还需安排 rare witness sections的 transversal
分布。严格 no-go已经由前面的四元 source给出；这个 fiber模板只说明相同现象与
rare-witness geometry相容。要排除它必须使用多个 KLZ parents的重叠或全局
state-counting，而不是单 fiber chain rule。

## 7. 多 batch / pivot 下没有自动改善

对固定 pivot按 decode order记 batch contexts为 `C_k`。Exact chain rule给

\[
\sum_k I(X_k;F_{r_k}\mid C_k)
\le I(X;M_b\mid\Theta,R)
\le H.
\tag{27}

若每 batch分解为 `A_k+D_k`，则同一 pivot内可安全地写

\[
\sum_k(A_k+D_k)\le H.
\tag{28}

但 incidence dichotomy只给对应 transport costs

\[
T_k\le D_k+o(m)
\tag{29}

时，求和仍是

\[
\sum_kT_k\le\sum_kD_k+o(n).
\tag{30}

把式 (30) 代入该 pivot的 hard-rank inequality，仍只得到式 (14)。不同 pivots
共享同一 final state，并不允许把式 (28) 对每个 pivot相加；那会重复收费同一
mutual information。也不能选择 posterior arithmetic code后再保留 hard-rank
saving；式 (4) 已说明两者由同一个 conditional entropy约束。

这里还有一个更早的 measurability caveat：Theorem 4.1 的 `D` 属于某个具体
parent posterior，而 KLZ 首先发送的是共同 final state。式 (28) 假设这些 parent
deficits能按 decode order与 `I(X;M_b)` 作同一个可加分解；现有 theorem尚未证明
这种对齐。因此式 (14)--(15) 应理解为 **best-case accounting ceiling**：即便
额外赠送完美的 parent/final-state alignment，这条路线也最多得到中点。它本身
还不是 `u/n -> infinity` 下的新 ordinary-AMQ lower bound。

所以旧 all-pivot `C_q` 在 `u/n -> infinity` 下成立所需的真正新命题必须是：

> 多个 overlapping parents 的 total transport loss严格小于可见 entropy
> deficits之和，或同一 deficit不能在所有 active pivots同时作为 transport credit。

单 parent定理 `T<=D` 不足够。

## 8. 什么额外 lemma 才能恢复 `C`

以下任一形式足够：

1. **vanishing transport:** `T=o(n)`，直接恢复 hard all-pivot converse；
2. **strict coefficient:** 对某个 `kappa<1`，`T<=kappa D+o(n)`，则
   \[
   H\ge A+\frac{C-A}{1+\kappa}-o(n),
   \]
   仍不足以完全恢复 `C`，除非 `kappa=0`；
3. **overlap deficit:** 对全部 active pivots联合，transport debit只支付一次，
   而 state deficit在 pivot minimax中不能被对手分别重用；
4. **thickness lower bound:** 直接证明 `D` 本身至少为理想 dynamic premium `K`，
   此时 `H>=A+D>=C`，无需用 transport saving。

第 3 项是最贴近 KLZ结构的剩余路线；第 4 项则是更强的 fiber-thickness converse。

## 9. 裁决

严格成立：

1. posterior-aware second-stage message受式 (4)约束；
2. entropy deficit与 hard-rank冗余是同一个 `D`，不能同时作为 state credit和
   communication saving重复使用；
3. `T<=D` 最多给出 `max{A+D,C-D}`；
4. 该 tradeoff有抽象 posterior和 rare-support fiber近等号例；
5. 多 batch chain rule在单 pivot内求和后仍不突破这个 barrier。

因此当前不能证明 old all-pivot `C_q` 在 `u/n -> infinity` 下成立。新的
transport-information dichotomy是重要局部进展，但其直接全局推论只有中点型
lower bound。下一步必须证明真正的 multi-parent overlap deficit；继续调整
posterior code本身不会消除这一因子二损失。
