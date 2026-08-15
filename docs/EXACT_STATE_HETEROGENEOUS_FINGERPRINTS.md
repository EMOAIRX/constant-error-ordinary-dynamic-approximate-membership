# 固定状态异质 fingerprints：普通动态模型中的相变上界

> 状态：新的候选主结果。本文处理固定预分配 \(H\)-bit 状态、任意长合法更新历史，不使用 overflow 或有限 horizon。组合优化与构造可写成有限 \(n\) 定理；优先权、有限宇宙类内 converse，以及 charged short-seed / 高效 word-RAM hash 实现仍需继续审计。在 KLZ free-random-tape、无时间要求的模型中，categorical hash 可由 tape 上的 degree-\(n\) polynomial 实现。

所有对数均以 2 为底。

## 1. 模型与动机

取一个初始化时抽取、之后固定不变的 categorical hash

\[
h:U\to\{\top,1,\ldots,q\}.
\]

对每个固定键，独立地令

\[
\Pr[h(x)=i]=p_i,
\qquad
\Pr[h(x)=\top]=1-\sum_{i=1}^q p_i.
\]

标签 \(\top\) 永久回答 YES。对 tracked label \(i\)，结构精确维护当前集合中映到 \(i\) 的 multiplicity \(C_i\)。查询 \(x\) 当且仅当 \(h(x)=\top\) 或 \(C_{h(x)}>0\) 时回答 YES。

只要当前集合大小不超过 \(n\)，完整 count vector 可用固定长度编码，因为

\[
(C_1,\ldots,C_q,C_\bot),
\qquad
C_\bot=n-\sum_i C_i,
\]

是 \(n\) 个不可区分球在 \(q+1\) 个盒中的 composition。因此所有可能向量的数量为

\[
\binom{n+q}{q},
\]

空间为

\[
H_{n,q}=\left\lceil\log\binom{n+q}{q}\right\rceil.
\]

该表示覆盖所有可能的 count vectors，所以没有 overflow。Insert/Delete 是 composition rank 的确定性更新，因而支持任意长合法历史。运行时间目前不作要求。

## 2. 精确有限 \(n\) 错误公式

对任意固定历史、当前集合 \(S\) 和固定非成员 \(x\notin S\)，hash values 在不同键之间独立，故

\[
\Pr[\operatorname{Query}(x)=\mathrm{NO}]
=
\sum_{i=1}^q p_i(1-p_i)^{|S|}
\ge
\sum_{i=1}^q p_i(1-p_i)^n.
\tag{1}
\]

因此容量 \(n\) 时的 pointwise FPR 至多 \(\varepsilon\)，只要

\[
\sum_{i=1}^q p_i(1-p_i)^n\ge1-\varepsilon.
\tag{2}
\]

最坏情况在 \(|S|=n\)，所以对这个 construction，条件 (2) 也是必要的。

这对任意长、预先固定且与初始化随机性独立的合法历史成立。若允许 workload 读取 hash seed 后自适应选键，则和标准 public-random fingerprint 构造一样需要单独定义 adversary model。

## 3. 固定 \(q\) 时的最优 rejection mass

令

\[
f_n(p)=p(1-p)^n,
\qquad 0\le p\le1.
\]

需要求

\[
\max\left\{\sum_{i=1}^q f_n(p_i):
p_i\ge0,\ \sum_i p_i\le1\right\}.
\tag{3}
\]

精确答案为

\[
\boxed{
R_{n,q}^{\rm rej}
=
\begin{cases}
\displaystyle
\frac{q}{n+1}\left(\frac n{n+1}\right)^n,
&q\le n+1,\\[1.2ex]
\displaystyle
\left(1-\frac1q\right)^n,
&q\ge n+1.
\end{cases}}
\tag{4}
\]

两支由以下分布达到：

- \(q\le n+1\)：每个 tracked cell 取 \(p_i=1/(n+1)\)，剩余质量 \(1-q/(n+1)\) 分给永久 YES 标签；
- \(q\ge n+1\)：无永久 YES 质量，取 \(p_i=1/q\)。

证明如下。

当 \(q\le n+1\) 时，单项 \(f_n\) 的全局最大值在

\[
a=\frac1{n+1},
\]

而 \(qa\le1\)，所以逐项取到最大值可行，得到第一支。

现在设 \(q\ge n+1\)。任何最优解都满足 \(\sum_i p_i=1\)：否则平均值严格小于 \(1/q\le a\)，至少有一个坐标小于 \(a\)，增加该坐标会严格增加目标值。最优解也不含零坐标。否则从任意正坐标向零坐标搬移无穷小质量时，目标的一阶变化是

\[
f_n'(0)-f_n'(p)=1-f_n'(p)>0,
\]

因为对每个 \(p>0\) 都有 \(f_n'(p)<1\)。

因此最优解是 simplex 内点，存在 Lagrange multiplier \(\mu\) 使每个坐标满足

\[
f_n'(p_i)
=(1-p_i)^{n-1}(1-(n+1)p_i)=\mu.
\tag{5}
\]

若 \(\mu<0\)，则所有 \(p_i>a\)，于是

\[
\sum_i p_i>qa\ge1,
\]

矛盾。若 \(\mu=0\)，则每个内点坐标只能等于 \(a\)；这只在 \(q=n+1\) 时满足总和为 1。若 \(\mu>0\)，则每个 \(p_i\in(0,a)\)，而 \(f_n'\) 在该区间严格递减，所以方程 (5) 只有一个解，全部坐标相等于 \(1/q\)。这证明第二支。

## 4. 渐近相变

令 \(q/n\to c>0\)。由 (4)，最大 rejection probability 收敛到

\[
\rho(c)=
\begin{cases}
c/e,&0<c\le1,\\
e^{-1/c},&c\ge1.
\end{cases}
\tag{6}
\]

要使 FPR 不超过固定 \(\varepsilon\)，需 \(\rho(c)\ge1-\varepsilon\)。最小可行 tracked-cell ratio 为

\[
\boxed{
c_*(\varepsilon)=
\begin{cases}
\displaystyle
\frac1{-\ln(1-\varepsilon)},
&0<\varepsilon\le1-e^{-1},\\[1.2ex]
e(1-\varepsilon),
&1-e^{-1}\le\varepsilon<1.
\end{cases}}
\tag{7}
\]

固定 composition state 的每-key rate为

\[
\Psi(c)
=(1+c)\log(1+c)-c\log c.
\tag{8}
\]

因此得到候选 exact-state rate

\[
\boxed{R_{\rm ES}(\varepsilon)=\Psi(c_*(\varepsilon)).}
\tag{9}
\]

相变点为

\[
\varepsilon_c=1-e^{-1}=0.6321205588\ldots.
\]

低误差支正是 uniform exact fingerprints。高误差支使用

\[
q\sim e(1-\varepsilon)n<n
\]

个 tracked cells 和一个永久 YES 类，并严格减少 state count。

例如 \(\varepsilon=3/4\) 时，

\[
c_{\rm uniform}=1/\ln4=0.721347\ldots,
\qquad
c_*=e/4=0.679570\ldots.
\]

因为 \(\Psi\) 严格递增，所以得到严格线性空间改进。

更具体地，

\[
R_{\rm uniform}^{\rm comp}(3/4)=1.6886650740\ldots,
\]

而

\[
R_{\rm ES}(3/4)=1.6352017409\ldots,
\]

改进 \(0.0534633331\ldots\) bit/key。误差 \(0.9\) 时改进扩大到 \(0.3168588626\ldots\) bit/key。

## 5. 与 Poisson entropy 路线的关系

Poisson typical-set rate

\[
\frac{H(\operatorname{Pois}(\lambda))}{\lambda}
\]

利用 occupancy source 的典型性，可在 whp、有限 horizon 模型中低于 composition state rate。本文的 \(R_{\rm ES}\) 则编码所有可能 occupancy vectors，因此：

- 固定 worst-case 内存，不发生 overflow；
- 任意长合法 history；
- 不需 union bound over time；
- 代价是 rate 高于 source-entropy rate，且 rank/unrank 可很慢。

这不是 2026 entropy-array uniform construction 的重述：后者固定 uniform fingerprint range，且 space/time 为 whp。式 (7)--(9) 显示，即便在更强的 fixed-state guarantee 下，uniform range 在 \(\varepsilon>1-e^{-1}\) 时也不是最优。

## 6. 可证明的类内 converse

在 single categorical label、永久 YES 类、exact tracked multiplicities、固定状态可覆盖所有容量不超过 \(n\) 的 vectors 这一类中：

1. 任意给定 \(q\) 至少需要区分相应 reachable count vectors；
2. 式 (4) 给出该 \(q\) 可达到的最大 rejection probability；
3. 因而最小 \(q\) 和最小 rate 分别由 (7) 与 (9) 给出。

严格说，有限宇宙上的 stars-and-bars converse 还要保证每个 tracked cell 的 preimage 足以实现相应 compositions。对 \(|U|/n\to\infty\) 的随机 categorical map，应改用带 cell-capacity 的 compositions，并证明其 log-support 的一阶项仍是 \(n\Psi(c)\)。这一步需要在正式稿中单列 lemma，不能把公共 hash 当作不影响 reachable state support。

该 converse 不覆盖：相关 labels、多个 hash choices、state-dependent rehashing、支持集合而非 exact counts，或任意普通 dynamic filters。

## 7. SODA 价值与缺口

这条路线的优点是结论直接给出一个合规的普通动态结构，并改进高误差区间的 uniform fixed-state benchmark；没有 HI、monotonicity、cell locality 或有限 churn 假设。

单独作为论文仍有三项风险：

1. 式 (4) 的优化可能被视为简单的 KKT/convexification；
2. 无高效 operation-time 结果时，数据结构贡献偏信息论；
3. converse 仍限于 exact categorical fingerprint 类，不解决 arbitrary-filter lower bound。

最自然的强化是把异质 labels 接入 entropy arrays，得到 \(O(1)\)-time、whp 的 \(R_{\rm FM}\) 相变上界；或证明任何 fixed-state exchangeable partition（允许相关标签）仍满足 (9)。前者更可实现，后者更接近真正的结构定理。

## 8. 下一步

1. 对式 (4) 的有限 \(n\) 证明做独立 hostile audit，并补齐有限宇宙 cell-capacity converse；
2. 核对 categorical hash 的有限种子实现与 KLZ free-random-tape 模型；
3. 对 Weighted/Daisy/ChainedFilter/2026 entropy arrays 做专门优先权审计；
4. 研究用 entropy-array 的 splitting trick 实现非均匀 tracked mass + permanent YES 类，争取 \(O(1)\) 时间的 \(R_{\rm FM}\) 上界；
5. 将 ordinary arbitrary-filter lower bound 保留为独立长期方向，不再依赖已失败的 fixed-chain rook lemma。

## 9. Hostile audit 注记（2026-08-13）

### 9.1 固定 \(q\) 优化：valid

式 (4) 的全局优化证明成立，但 KKT 部分宜补充下面两句以消除根结构歧义。

首先，

\[
f_n''(p)
=n(1-p)^{n-2}\bigl((n+1)p-2\bigr).
\]

因此 \(f_n'\) 在

\[
(0,a),\qquad a=\frac1{n+1},
\]

上严格递减。若 \(\mu>0\)，方程 \(f_n'(p)=\mu\) 的根只能位于 \((0,a)\)，故只有一个根，所有坐标必须等于 \(1/q\)。

若 \(\mu<0\)，方程在 \((a,1)\) 内确实可能有两个根：一个位于

\[
\left(a,\frac2{n+1}\right),
\]

另一个位于

\[
\left(\frac2{n+1},1\right).
\]

但这不产生遗漏的 mixed optimizer，因为任一这样的根都严格大于 \(a\)。于是 \(q\ge n+1\) 时

\[
\sum_i p_i>qa\ge1,
\]

与 simplex constraint 矛盾。故整个 \(\mu<0\) 分支不可行。

全局性也没有缺口：目标在 compact simplex 上达到最大值；当 \(q\ge n+1\) 时，原证明先严格排除了 slack constraint 和所有 zero-coordinate faces，所以 maximizer 是 simplex 内点，KKT 覆盖所有剩余候选。对 \(\mu=0\)，除 \(p=a\) 外 \(p=1\) 也是闭区间上的零点，但无零坐标且 \(q\ge2\)、总和为 1 排除了任何坐标等于 1。因此仅 \(q=n+1\) 的 uniform point 剩下。

结论：式 (4) 及其边界 \(q=n+1\) 均为 **valid**。

### 9.2 Hash tape 与固定状态：KLZ 模型内 valid，word-RAM 短种子版未证明

Composition rank 的

\[
H_{n,q}=\left\lceil\log\binom{n+q}{q}\right\rceil
\]

只编码动态 count state，不包含 categorical hash description。在 KLZ 的 space-only 模型中，这可以是合法的，因为无限只读 random tape 不计入 \(H\)。而且不必假设一个额外的 fully-random-function oracle：下面的显式免费-tape实现已足够。

取一个包含 \(U\) 的 field

\[
F=\operatorname{GF}(2^w),\qquad w=\Theta(\log n),
\]

从 random tape 的一个固定 prefix 读取 degree-\(n\) polynomial

\[
P(z)=a_0+a_1z+\cdots+a_nz^n
\]

的独立 uniform coefficients。每次操作重新读取同一个 prefix 并计算 \(P(x)\)。对任意至多 \(n+1\) 个 distinct keys，这些 values 严格独立 uniform。把 \(F\) 分成 \(q+1\) 个 deterministic intervals，便得到 grid-categorical probabilities。

这正好足够证明 pointwise FPR：一个 endpoint 只涉及至多 \(n\) 个 current members 和一个固定 query key。Hash 在任意长历史中保持一致，也不需要随时间增加随机性。若目标 probabilities 不是 field-grid points，取更大的 \(w=C\log n\)，使总 variation rounding error 为 \(o(1)\)；它只改变渐近 error constraint，不改变 \(n\Psi(c)+o(n)\) rate。

所以：

- 在 **KLZ free-random-tape、无时间要求** 的模型里，arbitrary-length fixed-state upper bound 是 **valid**，hash coefficients 不计入 \(H\)；
- 如果改成必须把有限 hash seed 存入 data-structure memory 的 self-contained word-RAM，则上述 degree-\(n\) seed 需要 \(\Theta(n\log n)\) bits，不能忽略；
- KLZ 的 sequential fresh-random-bit pointer 本身不会自动提供 consistent categorical hash。这里使用的是 random tape 上一个固定、可重复读取的 coefficient region；若所采用的 tape machine 不允许重读或按固定位置访问 random bits，则必须显式增加 random-access/read-only-tape假设；
- 本节没有给出 succinct charged seed 或高效 hash evaluation，因此不能据此声称高效普通 word-RAM implementation。

建议把开头的“公共随机函数实现仍需继续审计”改为更精确的边界：

> KLZ free-tape information-theoretic implementation可由 degree-\(n\) polynomial hash完成；charged short-seed与高效 word-RAM implementation仍开放。
