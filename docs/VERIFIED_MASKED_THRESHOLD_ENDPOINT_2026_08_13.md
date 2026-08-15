# Masked threshold quotients 的高误差 fixed-state endpoint

> 日期：2026-08-13。状态：本文给出一个严格的 upper-bound theorem。构造、
> finite-\(n\) pointwise FPR、最坏情形 fixed-state 计数以及
> \(\varepsilon\uparrow1\) 的 leading constant 都已证明。这里没有 matching
> lower bound，也没有完成文献优先权审计；因此“类内或全局最优”仍是开放的。

所有持久状态都计入空间；公共 fully random hash tape 免费。算法允许无界计算，
支持任意长、容量始终不超过 \(n\) 的合法 key-only update history。所有对数
在推导中为自然对数，最终空间以 bits 计。

## 1. 主定理

令

\[
\delta=1-\varepsilon.
\]

存在 ordinary dynamic one-sided approximate-membership filters，使

\[
\boxed{
\limsup_{\delta\downarrow0}\;
\limsup_{n\to\infty}
\frac{H_{n,\delta}}
{n\delta\log_2(1/\delta)}
\le \frac e2.
}
\tag{1}
\]

等价地，

\[
H_{n,\delta}
\le
\left(\frac{e}{2\ln2}+o(1)\right)
n\delta\ln\frac1\delta.
\tag{2}
\]

这里每个 filter 都满足：

- 每条 tape 上 zero false negatives；
- 对每条预先固定的合法 history 和每个固定当前 nonmember，FPR 至多
  \(1-\delta\)；
- fixed worst-case memory，覆盖所有 tracked load 至多 \(n\) 的状态；
- 任意长合法 insertion/deletion，永不 overflow；
- 不使用外部 exact set、live-key enumeration 或 rebuild。

还存在一个 joint finite-\(n\) 版本。若

\[
\delta_n\downarrow0,
\qquad n\delta_n\to\infty,
\tag{3}
\]

则同一构造可取有限参数并满足严格 FPR \(\le1-\delta_n\)，同时

\[
H_n
\le
\left(\frac e2+o(1)\right)
n\delta_n\log_2\frac1{\delta_n}.
\tag{4}
\]

条件 \(n\delta_n\to\infty\) 只用于使 block 数趋于无穷并消除整数 rounding。
式 (1) 的 iterated fixed-error asymptotic 不需要这个额外表述。

## 2. 数据结构

取整数 \(q\ge2\)、tracked mass \(\beta\in(0,1)\) 和 block 数 \(B\)。公共
随机带为每个 key 独立给出：

1. 以概率 \(1-\beta\) 标为 \(\top\)；
2. 否则均匀进入某个 \(j\in[B]\)，并获得独立均匀 bit
   \(h(x)\in\{0,1\}\)。

标签 \(\top\) 永久回答 `YES`，其 keys 不写入持久状态。对 tracked block
\(j\)，保存

\[
c_j=\text{当前 tracked load},
\qquad
a_j=\sum_{x\text{ in block }j}h(x)\pmod q.
\tag{5}
\]

`Insert/Delete` 对相应 \((c_j,a_j)\) 加减 \((1,h(x))\)；对 \(\top\) key
什么也不做。查询 tracked key 时：

- 若 \(c_j<q\)，residue 是精确 one-count，查询相应 bit 是否出现；
- 若 \(c_j\ge q\)，返回 `YES`。

### Lemma 2.1（correctness 与 everlasting recovery）

该结构在每条合法 history 上没有 false negative。它支持任意长 history，且从
任意高负载状态经 deletions 降回 \(c_j<q\) 后自动恢复精确 binary support。

证明。当 \(c_j<q\) 时，真实 one-count 属于 \([0,c_j]\subset[0,q-1]\)，
所以模 \(q\) 没有 wrap-around；成员的 bit multiplicity 非零。当
\(c_j\ge q\) 或 key 属于 \(\top\) 时直接回答 `YES`。式 (5) 是群
accumulator，合法 deletion 减去被删 key 的 bit；因此无论之前经历多少高负载
碰撞，降回 \(c_j<q\) 时 residue 都等于剩余 keys 的真实 one-count。证毕。

## 3. 精确 finite-\(n\) pointwise FPR

固定任意与初始化随机带独立的合法 history，其当前集合为固定
\(S\)，\(|S|=s\le n\)；再固定 \(x\notin S\)。条件于 \(x\) 是 tracked key，
与其进入同一 block 的成员数满足

\[
C\sim\operatorname{Bin}\left(s,\frac\beta B\right).
\tag{6}
\]

条件于 \(C=t<q\)，query bit 与全部成员 bits 均不同的概率为 \(2^{-t}\)；
若 \(C\ge q\)，block 不拒绝。因此精确 rejection probability 是

\[
\boxed{
D_{n,q}(s;\beta,B)
=\beta\sum_{t=0}^{q-1}
{s\choose t}
\left(\frac\beta B\right)^t
\left(1-\frac\beta B\right)^{s-t}2^{-t}.
}
\tag{7}
\]

式 (7) 随 \(s\) 不增：可把 \(C_{s+1}=C_s+X\) coupling，其中
\(X\) 是 Bernoulli，而函数

\[
f_q(t)=2^{-t}\mathbf 1\{t<q\}
\]

单调不增。因此容量内最坏情形是 \(s=n\)，式 (7) 是 pointwise-over-
randomness guarantee，不是 query-distribution average。

定义

\[
\rho_q(\lambda)
=e^{-\lambda}
\sum_{t=0}^{q-1}\frac{(\lambda/2)^t}{t!}
=\mathbb E[f_q(\operatorname{Pois}(\lambda))].
\tag{8}
\]

若 \(n\beta/B\to\lambda\)，则式 (7) 趋于 \(\beta\rho_q(\lambda)\)。下面的
定量版本同时处理增长的 \(q\)。

### Lemma 3.1（uniform finite-\(n\) calibration）

对任意 \(q\ge2\)，若

\[
B=\left\lceil\frac{n\beta}{2}\right\rceil,
\tag{9}
\]

则

\[
D_{n,q}(n;\beta,B)
\ge
\beta\left(\rho_q(2)-\frac8n\right).
\tag{10}
\]

证明。令 \(p=\beta/B\) 和 \(\lambda_n=np\)。由 (9)，

\[
0<\lambda_n\le2,
\qquad p\le\frac2n.
\]

Le Cam inequality 给

\[
d_{\rm TV}(\operatorname{Bin}(n,p),
\operatorname{Pois}(\lambda_n))
\le2np^2\le\frac8n.
\]

因为 \(0\le f_q\le1\)，其 expectations 相差至多 \(8/n\)。Poisson random
variable 随 mean 随机单调增加，而 \(f_q\) 单调下降，所以

\[
\mathbb E f_q(\operatorname{Pois}(\lambda_n))
\ge\rho_q(2).
\]

乘以 query 被 tracked 的概率 \(\beta\) 即得 (10)。这个误差界完全不依赖
\(q\)。证毕。

## 4. Worst-case fixed-state 计数

公共 mask 不允许按 \(\beta n\) 的典型 tracked load 分配状态：在某条固定
tape 上，一条合法 history 可以把全部 \(n\) 个 live keys 放入 tracked region。
所以必须覆盖

\[
\sum_{j=1}^B c_j\le n.
\tag{11}
\]

这正是本证明使用的 worst-case constraint。

给定 load vector \((c_1,\ldots,c_B)\)，每个 block 至多有 \(q\) 个 residue
states。满足 (11) 的 load vectors 数为 \({n+B\choose B}\)。因此全部 formal
states 数满足

\[
\boxed{
N_{n,B,q}
\le q^B{n+B\choose B}.
}
\tag{12}
\]

实际 reachable state 数只会更小。对这些 states 作 enumerative rank/unrank，
得到固定长度

\[
H_{n,B,q}
\le
\log_2{n+B\choose B}+B\log_2q+1.
\tag{13}
\]

所有 block loads 和 residues 都已包含在 (13) 中，不能再另加 count array。
合法 update 保持 (11)，所以编码永不 overflow。该 argument 不要求 typical-set
concentration、有限 operation horizon 或 saddle-point asymptotic。

令 \(B/n\to b\)。Stirling formula 给

\[
\frac Hn
\le
\frac1{\ln2}
\left[
(1+b)\ln(1+b)-b\ln b+b\ln q
\right]+o(1).
\tag{14}
\]

当 \(b\downarrow0\) 时，右侧为

\[
\frac b{\ln2}
\left[
\ln\frac1b+ln q+1+O(b)
\right]+o(1).
\tag{15}
\]

式 (12) 是后面 \(q\to\infty\) 时 uniformity 的关键：无需对随参数变化的
生成函数鞍点或 local CLT 作任何一致估计。

## 5. 参数选择与 \(e/2\) constant

令

\[
L=\ln\frac1\delta,
\qquad
q(\delta)=\max\{2,\lceil\sqrt L\rceil\}.
\tag{16}
\]

在 Poisson target load \(\lambda=2\) 处，

\[
\rho_q(2)
=e^{-2}\sum_{t=0}^{q-1}\frac1{t!}
\longrightarrow e^{-1}.
\tag{17}
\]

取

\[
\beta=\frac\delta{\rho_q(2)},
\qquad
B\sim\frac{n\beta}{2},
\qquad
b=\frac Bn\sim\frac{\delta}{2\rho_q(2)}.
\tag{18}
\]

则

\[
b=\left(\frac e2+o(1)\right)\delta.
\tag{19}
\]

此外

\[
\ln q=O(\ln L)=o(L),
\qquad
\ln\frac1b=L+O(1)+o(1).
\tag{20}
\]

把 (19)--(20) 代入 (15)：

\[
\frac Hn
\le
\left(\frac{e}{2\ln2}+o(1)\right)
\delta L,
\tag{21}
\]

即式 (1)--(2)。常数 \(e/2\) 的来源也可直接看成

\[
\max_{\lambda>0}\lambda e^{-\lambda/2}
=\frac2e,
\tag{22}
\]

其唯一 maximizer 是 \(\lambda=2\)。增长的 modulus 使
\(\rho_q(\lambda)\to e^{-\lambda/2}\)，而每个 block 的 \(\ln q\) residue
开销由 \(\ln q=o(\ln(1/\delta))\) 吸收。

## 6. Joint finite-\(n\) theorem

现在令 \(\delta_n\downarrow0\)、\(n\delta_n\to\infty\)，并定义

\[
L_n=\ln(1/\delta_n),
\qquad
q_n=\max\{2,\lceil\sqrt{L_n}\rceil\},
\]

\[
\eta_n=(n\delta_n)^{-1/3},
\qquad
\beta_n=rac{\delta_n(1+\eta_n)}{\rho_{q_n}(2)},
\qquad
B_n=\left\lceil\frac{n\beta_n}{2}\right\rceil.
\tag{23}
\]

因为 \(\rho_{q_n}(2)\to e^{-1}\)，最终 \(\beta_n<1\)。由 Lemma 3.1，

\[
\begin{aligned}
D_{n,q_n}(n;\beta_n,B_n)
&\ge
\beta_n\left(\rho_{q_n}(2)-\frac8n\right)\\
&=
\delta_n(1+\eta_n)
-O\left(\frac{\delta_n}{n}\right)\\
&\ge\delta_n
\end{aligned}
\tag{24}
\]

for all sufficiently large \(n\)。所以 finite-\(n\) pointwise FPR 严格不超过
\(1-\delta_n\)。

又因为 \(n\delta_n\to\infty\)，rounding 给

\[
\frac{B_n}{n}
=\left(\frac e2+o(1)\right)\delta_n.
\tag{25}
\]

式 (13) 的 `+1`、Stirling remainder 和 \(B_n\) rounding 都是
\(o(n\delta_nL_n)\)。具体地，\(n\delta_n\to\infty\) 与
\(L_n/\ln q_n\to\infty\) 给

\[
\frac{\ln q_n}{n}=o(\delta_nL_n),
\]

而标准 bound

\[
\ln{n+B_n\choose B_n}
=n\big[(1+b_n)\ln(1+b_n)-b_n\ln b_n\big]
+O(\ln n)
\]

中的 \(O(\ln n)\) 若不额外限制 \(\delta_n\) 未必一致地是
\(o(n\delta_nL_n)\)。为完全避开这个表面 remainder，可用 elementary
binomial bound

\[
{n+B_n\choose B_n}
\le
\left(\frac{e(n+B_n)}{B_n}\right)^{B_n},
\tag{26}
\]

它没有 additive \(O(\ln n)\)。由 (26) 直接得到

\[
H_n
\le
B_n\log_2\left(\frac{eq_n(n+B_n)}{B_n}\right)+1,
\tag{27}
\]

再用 (25)、\(\ln q_n=o(L_n)\) 即得 (4)。这同时关闭了 joint limit 中的
Stirling-uniformity gap。

## 7. 与已有 exact-state heterogeneous baseline 的关系

只使用 tracked exact multiplicities 加永久 `YES` 类时，已知 fixed-state
heterogeneous construction 在同一 endpoint 给

\[
H_{\rm exact}
\le
(e+o(1))n\delta\log_2(1/\delta).
\tag{28}
\]

式 (1) 把 leading coefficient 从 \(e\) 降为 \(e/2\)。原因不是假设实际只
有 \(\beta n\) 个 tracked keys；两边都必须按最坏 tracked load \(n\) 编码。
改进来自 threshold quotient：每个 block 在高负载层只保留 \(q\) 个 residues，
从而让最有利的 tracked query block load 从 exact cells 的 \(1\) 提高到 \(2\)。

这个 factor-two comparison 只针对 **everlasting fixed-state/all-reachable-state**
上界。允许 polynomial horizon、small failure probability 和 source/typical-state
coding 的 smooth-memory constructions 可以有不同、甚至更低的 endpoint 尺度；
式 (1) 不与那些模型作直接最优性比较。

## 8. 已关闭与尚未关闭的缺口

本文已经关闭：

1. mask 后错误地按典型 \(\beta n\) tracked load 计空间的漏洞；
2. finite-\(n\) Poisson approximation 及其对增长 \(q\) 的一致性；
3. \(B\) rounding 与严格 pointwise FPR margin；
4. 随 \(q(\delta)\) 变化的 coefficient/saddle uniformity；
5. joint \((n,\delta_n)\) limit 中 Stirling remainder 可能过大的问题。

仍未关闭：

1. 是否存在 leading constant 小于 \(e/2\) 的 nonlinear、multisymbol、
   multihash 或 cross-block quotient；
2. 在一个自然且足够宽的 everlasting fixed-state class 中证明 matching
   \(e/2\) converse；
3. 高效 word-RAM rank/unrank 与 charged short-seed implementation；
4. 与 IBLT、counting/quotient filters、modular counters 及其他 overload-recovery
   summaries 的完整优先权审计。

特别地，IBLT 已经包含“超过设计阈值后功能退化、删除回阈值后恢复”的可加摘要
思想；因此不能把 overload recovery 本身称为首次。这里可单独核验的 theorem
是 one-sided pointwise AMQ、fixed worst-case bit state 及式 (1) 的精确
endpoint coefficient。没有 lower bound 和 priority audit 前，正确定位是
**verified new upper-bound candidate for publication**，不是 SODA-complete
optimality theorem。
