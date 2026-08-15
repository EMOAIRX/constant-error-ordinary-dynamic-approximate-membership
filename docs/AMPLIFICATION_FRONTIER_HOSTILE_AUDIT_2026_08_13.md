# KLZ 常数误差放大的敌对审计

> 日期：2026-08-13。本文只记录已经逐项核对的结论。最重要的更正是：下面的放大曲线目前只对 KLZ Definition 4.2 的 history-dependent monotone filters 成立，不能作为 ordinary non-monotone dynamic filters 的下界。此前把固定误差常数机械地经 Section 5 提升到普通模型的说法应撤回。

所有对数均以 \(2\) 为底；\(\ln\) 表示自然对数。

## 1. 最终判定

令

\[
B(\delta)
=\log\frac1\delta+(1-\delta)\log e-2h_2(\delta),
\qquad 0<\delta\le \frac12.
\tag{1}
\]

逐项保留 Kuszmaul--Liang--Zhou（KLZ）Proposition 4.3 中被
\(\varepsilon=o(1)\) 吸收的项，严格得到的是：对每个固定
\(\delta\in(0,1/2]\)，每个满足 KLZ Definition 4.2 的 monotone dynamic
filter，

\[
H\ge nB(\delta)-o(n).
\tag{2}
\]

这里不需要 history independence，但仍需要 accepted-set monotonicity。

若把同一个 monotone filter 的 \(k\) 份独立副本取 AND，则对每个固定整数
\(k\) 且 \(\varepsilon^k\le 1/2\)，

\[
H\ge \frac{n}{k}B(\varepsilon^k)-o(n).
\tag{3}
\]

因此安全的放大曲线是

\[
L_{\rm amp}^{\rm mon}(\varepsilon)
=\sup_{k\ge1:\,\varepsilon^k\le1/2}
\frac{B(\varepsilon^k)}k.
\tag{4}
\]

当 \(0<\varepsilon\le1/2\) 时约束自动满足。在
\(\varepsilon=1/2\) 处，整数最优值为 \(k=5\)：

\[
L_{\rm amp}^{\rm mon}(1/2)
=\frac{B(1/32)}5
=1.1992732344471508\ldots.
\tag{5}
\]

式 (5) **不是 ordinary-filter lower bound**。ordinary non-monotone 模型中，
目前既没有证明单副本式 (2)，也不能据此使用 AND 放大。

## 2. 固定误差常数的逐项核对

沿用 KLZ Section 4 的记号，令

\[
u=|U|,\quad V=u/b,\quad m=n/b,\quad
N=(1-\delta)n+\delta u,\quad M=4^b.
\]

对一次 `Send`，保留 hit bit 的熵和 hit/miss 两个 location branch，KLZ
Claims 4.6--4.7 给出预极限通信比较

\[
\begin{aligned}
H\ge{}& b\log(V^{\underline m})-nh_2(\delta)-n\delta\log V\\
&-(1-\delta)n\log\frac{K}{1-\delta}
-(1-\delta)\frac nb\sum_{j=1}^b\log(z_j+\gamma),
\end{aligned}
\tag{6}
\]

其中在 KLZ 的慢增长参数选择下

\[
b\log(V^{\underline m})=n\log V-o(n),\qquad
K=\delta V(1+o(1)),
\tag{7}
\]

且 Lemmas 3.4、4.8 给出

\[
\sum_{j=1}^b\log(z_j+\gamma)\le-b\log e+o(b).
\tag{8}
\]

代入并消去所有 \(n\log V\) 项，得到

\[
\begin{aligned}
H\ge n\bigl[&-h_2(\delta)
-(1-\delta)\log\delta
(1-\delta)\log(1-\delta)\\
&+(1-\delta)\log e\bigr]-o(n).
\end{aligned}
\tag{9}
\]

由二元熵恒等式，方括号正好等于式 (1) 的 \(B(\delta)\)。三项线性损失
是两个 \(h_2(\delta)\) 和一个 \(\delta\log e\)：分别来自逐 key hit bit、
branch/location mixture，以及 factorial saving 只发生在 miss branch。

### 2.1 量词与 \(o(n)\)

式 (2) 的正确量词是：先固定常数 \(\delta\)，再令 \(n\to\infty\)，并令
KLZ 的 batch 参数 \(b=b(n)\to\infty\) 足够慢。它不提供对
\(\delta=\delta(n)\) 的一致 \(o(n)\)。

放大时先固定 \(k\)，于是 \(\delta=\varepsilon^k\) 仍是固定常数，可以合法
调用式 (2)：

\[
kH\ge nB(\varepsilon^k)-o_k(n).
\]

除以固定 \(k\) 即得式 (3)。不能把 \(k=k(n)\) 直接塞进同一个
\(o(n)\) 中。

这不妨碍式 (4)。对每个固定 \(k\)，先取 \(\liminf H/n\)，再对这些常数
取 supremum 即可。并且当 \(k\to\infty\) 时

\[
\frac{B(\varepsilon^k)}k
\longrightarrow \log(1/\varepsilon),
\]

而充分大的有限 \(k\) 已严格超过该极限，所以 supremum 由某个有限固定
\(k\) 取得。最终定理不需要增长的 \(k(n)\)。

## 3. 为什么 AND 构造本身合规

取原 filter 的 \(k\) 份副本，各自读取互不相交的独立随机带。所有副本执行
同一条合法更新历史，查询仅在全部副本回答 YES 时回答 YES。

对成员，每个副本确定性回答 YES，因此没有 false negative。对固定历史、
固定当前非成员 \(x\)，各副本的 false-positive event 只依赖各自的独立随机
带，故

\[
\Pr[\text{AND answers YES}]
=\prod_{j=1}^k\Pr[E_j]\le\varepsilon^k.
\tag{10}
\]

若原算法满足 KLZ Definition 4.2 的 monotonicity，每个副本的 accepted set
沿 self-contained suffix 单调增长；交集也单调增长。因此 AND 后的结构仍在
Proposition 4.3 的类中，空间为 \(kH\)。

这个论证不要求同一副本内部不同 keys 或不同时刻的错误独立，也允许 frozen
mask、global ALL-YES branch、ghosts 和共享 witnesses。

## 4. ordinary non-monotone lifting 的精确断点

KLZ Section 5 为固定 public partition
\(\pi=(U_1,\ldots,U_b)\) 定义 reconstructible set
\(\widetilde F\)。Lemma 5.3 正确证明了

\[
S_F\subseteq\widetilde F\subseteq\overline F
\]

以及 protocol endpoints 所需的 prefix monotonicity。问题出现在“把 Section 4
中所有 accepted sets 直接换成 reconstructible sets”这一步。

### 4.1 Claim 4.6 对 actual accepted sets 为什么成立

Claim 4.6 条件于完整 obfuscation sequence \(\sigma\) 和 filter random tape。
此时 filter states \(F_r,G_\ell\) 以及 actual difference

\[
A^*=\overline F_r\setminus\overline G_\ell
\]

都是固定集合。条件中只暴露了出现在 \(\sigma\) 内的少量 keys；其余 keys
到 \(U_k\) 的分配仍保持均匀，因此可以“移除 \(U_k\)”并估计
\(\mathbb E|A^*\cap U_k|\)。

### 4.2 对 reconstructible sets 为什么失败

\(\widetilde F\) 的定义量化所有 conforming histories，而“conforming”本身
依赖完整 partition \(\pi\)。即使固定 \(\sigma\) 和 filter tape，未出现在
\(\sigma\) 中的 keys 属于哪个 \(U_j\)，仍会改变哪些 histories 可以作为
reconstruction sequences。因此

\[
\widetilde F_r\setminus\widetilde G_\ell
\]

在 Claim 4.6 的条件概率空间里不是固定集合。若进一步条件于完整 \(\pi\)，
该集合虽然固定，但 \(U_k\) 也已经固定，原来的均匀抽样论证消失。

Lemma 5.3 的 set inclusion 与 pointwise FPR 并不补上这个条件独立性。

此外，对 \(\ell<k\)，conforming-history 定义直接给出

\[
\widetilde G_\ell\cap U_k=\varnothing.
\tag{11}
\]

若仍机械沿用 Section 4 的 first-moment bound，hit branch 会被错误地完全消掉，
从而推出固定误差下

\[
H\ge n\bigl(\log(1/\varepsilon)+\log e\bigr)-o(n).
\tag{12}
\]

下面的显式上界否决了这种 mechanical lifting。

### 4.3 \(\varepsilon=1/2\) 的 fixed-state sanity check

取免费一致随机 hash \(h:U\to[q]\)，精确保存 \(q\) 个 hash fibers 的
multiplicity vector，总质量至多 \(n\)。查询检查相应 count 是否非零；插入和
删除执行精确加减。这是合法的 fixed-memory dynamic filter，并且实际上也满足
Definition 4.2 的 monotonicity。

取

\[
q=\frac n{\ln2}+o(n)
\]

并稍微向上取整，则容量 \(n\) 时的 pointwise FPR 不超过 \(1/2\)：

\[
1-(1-1/q)^n\le\frac12.
\tag{13}
\]

全部 count vectors 可用固定长度

\[
\log\binom{n+q}{n}
=2.3844998424785\ldots n+o(n)
\tag{14}
\]

编码，而式 (12) 在 \(1/2\) 处要求

\[
1+\log e=2.4426950408889\ldots
\]

bits/key。常数 gap 为正，故机械的 reconstructible-set Claim 4.6 必然错误。

这个反例不直接否决较弱的 \(B(\delta)\) 数值本身；它否决的是目前唯一被提出
的 ordinary lifting 证明。结论应当是“ordinary 式 (2) 未证”，而不是“已经
构造出违反式 (2) 的 filter”。

## 5. 整数 AND 曲线的精确优化

对 \(0<\varepsilon\le1/2\)，令

\[
x=\ln(1/\varepsilon),\qquad y=kx,qquad d=e^{-y}=\varepsilon^k.
\]

若 \(H(d)=-d\ln d-(1-d)\ln(1-d)\) 是自然对数熵，则

\[
\frac{B(e^{-y})}{\log_2(e^y)}
=R(y)
:=1+\frac{1-e^{-y}-2H(e^{-y})}{y}.
\tag{15}
\]

因此

\[
\frac{B(\varepsilon^k)}k
=\log_2(1/\varepsilon)\,R(kx).
\tag{16}
\]

### 5.1 连续极值只有一个

写

\[
A(y)=1-e^{-y}-2H(e^{-y}).
\]

则 \(R'(y)\) 的符号由

\[
N(y)=yA'(y)-A(y)
\tag{17}
\]

决定。令 \(d=e^{-y}\)，有

\[
A'(y)=d\left(1+2\ln\frac{1-d}{d}\right),
\]

\[
A''(y)=d\left[-1-2\ln\frac{1-d}{d}+\frac2{1-d}\right].
\tag{18}
\]

式 (18) 的方括号作为 \(y\) 的函数严格递减：其导数为

\[
-\frac{2e^y}{e^y-1}
-\frac{2e^{-y}}{(1-e^{-y})^2}<0.
\]

故 \(A''\) 只改变一次符号，而 \(N'(y)=yA''(y)\)。再结合

\[
N(y)=2y+o(y)\quad(y\downarrow0),
\qquad N(y)\to-1\quad(y\to\infty),
\]

可知 \(N\) 恰有一个零点，因而 \(R\) 有唯一全局最大值。数值为

\[
y_*=3.735540479022715\ldots,
\tag{19}
\]

\[
d_*=e^{-y_*}=0.0238602716068370\ldots,
\tag{20}
\]

\[
R_*=R(y_*)=1.200969863367900\ldots.
\tag{21}
\]

### 5.2 \(\varepsilon\to1\) 的整数离散逼近

式 (4) 对 \(\varepsilon>1/2\) 仍可使用，只需限制
\(\varepsilon^k\le1/2\)。令 \(x=\ln(1/\varepsilon)\downarrow0\)。由式
(16)，

\[
\frac{L_{\rm amp}^{\rm mon}(\varepsilon)}
{\log_2(1/\varepsilon)}
=\sup_{k:\,kx\ge\ln2}R(kx).
\tag{22}
\]

整数网格 \(x\mathbb N\) 在 \(x\to0\) 时变稠密。取
\(k_x\) 为最接近 \(y_*/x\) 的合法整数，则
\(k_xx\to y_*\)。另一方面每个网格值均不超过连续 supremum \(R_*\)。所以

\[
\boxed{
\lim_{\varepsilon\uparrow1}
\frac{L_{\rm amp}^{\rm mon}(\varepsilon)}
{\log_2(1/\varepsilon)}
=1.200969863367900\ldots
}
\tag{23}
\]

并且最优重复数满足

\[
k_{\rm opt}\sim
\frac{y_*}{\ln(1/\varepsilon)},
\qquad
\varepsilon^{k_{\rm opt}}\to d_*.
\tag{24}
\]

注意 \(0.200969863\ldots\) 是相对静态率的额外比例；式 (23) 的总比例是
\(1.200969863\ldots\)。

### 5.3 \(0<\varepsilon\le1/2\) 的最优整数区间

由于 \(R\) 单峰，离散序列 \(R(kx)\) 也是先增后减。相邻整数的数值切换点为

\[
\begin{array}{c|c}
\text{相邻候选}&\varepsilon\text{ 切换点}\\
\hline
1\leftrightarrow2&0.0620466502585276\ldots\\
2\leftrightarrow3&0.2119061641263904\ldots\\
3\leftrightarrow4&0.3369744617891274\ldots\\
4\leftrightarrow5&0.4318595557282034\ldots
\end{array}
\tag{25}
\]

\(5\leftrightarrow6\) 的切换发生在
\(0.5043990896809402\ldots>1/2\)，所以在目标区间内只出现
\(k=1,2,3,4,5\)。边界点有并列最优。

在 \(\varepsilon=1/2\) 处：

\[
\begin{array}{c|c}
k&B(2^{-k})/k\\
\hline
1&-0.2786524796\\
2&0.7297325159\\
3&1.0584097581\\
4&1.1694866169\\
5&1.1992732344\\
6&1.1979871300\\
7&1.1856564516
\end{array}
\tag{26}
\]

## 6. 更一般 black-box composition 能否加强

这一节只考虑真正的 black-box error reduction：使用同一个容量-\(n\)、误差
\(\varepsilon\) filter 的 \(m\) 份独立副本，不改变其内部算法。

### 6.1 Boolean composition：AND 是严格的 pointwise 最优

固定历史和非成员 query 后，令副本输出为
\(Y_1,\ldots,Y_m\)。它们独立同分布，

\[
Y_i\sim\operatorname{Bernoulli}(p),\qquad p\le\varepsilon.
\]

任意 deterministic Boolean rule
\(\phi:\{0,1\}^m\to\{0,1\}\) 若没有 false negative，必须满足

\[
\phi(1,\ldots,1)=1.
\]

因此逐点有

\[
\phi(y)\ge \mathbf1[y=(1,\ldots,1)],
\]

从而

\[
\Pr[\phi(Y)=1]\ge p^m.
\tag{27}
\]

AND 恰好达到 \(p^m\)。允许额外 query randomness 也不改变结论，因为在
all-ones 输入上必须以概率 \(1\) 接受。

在 \(0<\delta\le1/2\) 上，\(B(\delta)\) 严格随 \(\delta\) 下降。因此对固定
副本数 \(m\)，没有 threshold、非单调 Boolean function 或 randomized rule 能
给出比 AND 更强的 KLZ-\(B\) certificate。

### 6.2 随机重复数、混合与非均匀分组

在 fixed worst-case memory 中，若最多分配 \(mH\) bits：

- 随机只启用其中一部分副本，不会小于全部 \(m\) 份取 AND 的错误；
- 在 AND 结果上混入 ALL-YES branch 只会增大错误；
- 把副本分成不同大小的 groups 后再组合，最终 all-ones event 仍不可拒绝，
  不能优于直接 AND 全部副本；
- expected-space convexification 属于不同模型，不能改善 KLZ 的固定内存下界。

### 6.3 容量缩放不是免费 black box

把容量 \(n\) 的任意集合拆给较小容量副本，需要路由、负载保证或动态迁移；
这些都不是原 filter API 免费提供的。对同一个容量-\(n\) black box，仅在较小
容量 \(N<n\) 上运行只会把 KLZ 下界的 \(n\) 换成 \(N\)，不会加强。按 key
分片后 query 单个 shard 不产生 error product；query 多个 shards 并取 OR 反而
增大 FPR。

因此，在“不修改 filter 内部结构”的清晰 black-box 类里，整数 AND 曲线已经
是 sharp envelope。超过它必须使用新的单副本 inequality，或利用 state
transitions、partition/reconstruction structure 等非黑盒信息。

## 7. 与 Lovett--Porat 的统一比较

Lovett--Porat 写作

\[
M_D(n,\varepsilon)
=\eta(\varepsilon)n\log_2(1/\varepsilon).
\]

所以正式的 \(1.1\)、单层经验最优 \(1.10213\ldots\) 和递归搜索报告的
\(1.13\) 都是乘在 \(\log_2(1/\varepsilon)\) 上的**无量纲系数**；只有在
\(\varepsilon=1/2\) 时，它们才数值上等于 bits/key。

一般地，若已有某个普通模型下界

\[
H\ge nG(\delta)-o(n),
\]

AND 只能形式化地产生 closure

\[
H\ge n\sup_k\frac{G(\varepsilon^k)}k-o(n).
\tag{28}
\]

若 \(G(\delta)=\eta(\delta)\log_2(1/\delta)\)，则式 (28) 等于

\[
H\ge n\log_2(1/\varepsilon)
\sup_k\eta(\varepsilon^k)-o(n).
\tag{29}
\]

Lovett--Porat 原文只正式给出每个固定误差存在某个
\(\eta(\delta)>1\)，并在 \(1/2\) 给出显式 \(1.1\)。它没有提供一条已认证的
全误差 closed-form curve 足以证明式 (29) 比 \(k=1\) 更强。对其 one-cut
方程的数值优化，\(\eta(\delta)\) 在 \(\delta\) 变小时下降，因此 AND 数值上
选择 \(k=1\)，但这只是对该数值优化的观察，不应升级成文献定理。

此外，Lovett--Porat 的原 hard distribution 使用 \(U^n\) 并允许重复 labels，
而 KLZ Definition 2.1 的 `Insert(x)` 假设当前 \(x\notin S\)。在没有写出合法的
API reduction 前，不应把 LP 常数与这里的 fresh-insertion KLZ 模型完全等同。

## 8. 优先权与 novelty 敌对审计

独立重复并取 AND 是 approximate membership 中最标准的误差缩减操作之一；
Boolean optimality式 (27) 也近乎定义级事实。它们本身没有新颖性。

本次核对包括 KLZ v1 原文、本地 Lovett--Porat ECCC/FOCS 版本，以及以
“dynamic approximate membership / fingerprint filters / amplification / AND
repetition / lower bound”为关键词的公开索引检索。没有定位到一篇明确写出
\(B(\varepsilon^k)/k\) 这条 KLZ 固定常数 envelope 的论文。但这个“未找到”
不是完备优先权证明，而且普通模型主张已经因 Section 5 缺口撤回。

安全的 novelty 判断是：

1. 式 (2)--(5) 是一个可复核的 **monotone-subclass corollary**；
2. 式 (23)--(25) 是该 corollary 的完整解析优化；
3. black-box Boolean barrier 是有用的范围界定，但技术深度很低；
4. 这些结果没有改善 ordinary KLZ dynamic filters 的社区 best-known lower
   bound。

## 9. SODA 价值与真实缺口

当前 package 单独不具有 SODA 级突破价值。原因不是常数不够漂亮，而是 headline
模型退回了 monotone subclass；放大技术又是标准操作。

真正可能有社区价值的后续有两条：

1. **修复或否决 KLZ Section 5 的 partition-safe interface。** 需要为
   partition-dependent reconstructible differences 建立正确的 first-moment
   inequality，显式包含 partition leakage correction。这个 correction 必须与
   式 (14) 的 count-vector upper bound 相容。
2. **绕开 Section 5。** 直接对 ordinary states/transitions 建立新的 batch
   branch--support inequality；它不能只使用 marginal accepted-set sizes，也不能
   把 reconstructible chain 当成免费 side information。

只有在普通 non-monotone 模型中得到显式新线性 gap，或者证明一个结构性的
composition/interface barrier，才接近 SODA 级贡献。当前已证结果应作为审计
lemma 或后续论文的附属工具，而不是主突破。

## 10. 核心来源

- Kuszmaul--Liang--Zhou, *Fingerprint Filters Are Optimal*, FOCS 2025,
  [arXiv:2510.18129](https://arxiv.org/abs/2510.18129).
- Lovett--Porat, *A Lower Bound for Dynamic Approximate Membership Data
  Structures*, FOCS 2010 / SIAM J. Comput. 2013.
- 本地固定误差代数审计：
  [KLZ_FIXED_EPSILON_CONSTANT_AUDIT.md](./KLZ_FIXED_EPSILON_CONSTANT_AUDIT.md)。
- 本地 partition-dependent obstruction：
  [TRANSITION_CONSTRAINED_BRANCH_SUPPORT_2026_08_13.md](./TRANSITION_CONSTRAINED_BRANCH_SUPPORT_2026_08_13.md)。
