# 次指数历史下异质 fingerprint 上界：量词、可靠性与随机带审计

> 日期：2026-08-14。状态：完整解析 theorem 与 hostile proof audit。本文闭合的是 KLZ
> free-random-tape、无时间要求模型中的 **seed-independent fixed history** 上界；
> 它不声称 adaptive-query robustness。核心改动是使用一个全局 occupancy
> information-spectrum slot，而不是对 polylog blocks 分别留 tail slack。

所有对数以 2 为底；概率尾界中的指数可临时换成自然底而不影响结论。

## 1. 三种不能混淆的 history 量词

固定容量 `n`、有限宇宙 `U_n` 和一个初始化随机带 `R`。

1. **Oblivious fixed history.** 整条合法 Insert/Delete/Query 序列在读取 `R`
   之前固定。每个 endpoint set 和每个 query key 均与 `R` 独立。这正是下面
   upper bound 覆盖的量词。
2. **Output-adaptive history.** 后续 query 或 update key 可以依赖先前 query
   answers。即使对手看不到 `R`，其选择的 key 和 endpoint set 也一般与 `R`
   相关。下面的 pointwise FPR 证明不覆盖它。
3. **Seed-adaptive history.** 对手直接读取 hash seed/random tape 后选择 keys。
   这比 output-adaptive 更强，标准 fingerprint map 在该量词下立即失效。

“对每条 fixed history 的 pointwise guarantee”不蕴含“对一个 adaptive adversary
产生的随机 history 的 conditional guarantee”。后者是 adaptive filter/broom-filter
一类不同模型。

## 2. 率函数与实现它的两种分布

令

\[
g(\lambda)=1-e^{-\lambda},\qquad
r(\lambda)=\frac{H(\operatorname{Pois}(\lambda))}{\lambda},
\]

并定义

\[
R_{\rm fp}(\varepsilon)
=\operatorname{lce}_{\lambda\in(0,\infty]}
\{(g(\lambda),r(\lambda))\}(\varepsilon).
\tag{2.1}
\]

不需要调用任何数值 phase certificate。因为 (2.1) 是平面曲线的下凸包，固定
`epsilon` 的边界点可由至多两个 curve points 的凸组合达到（若 infimum只在极限
达到，则取一个 `o(1)`-optimal 两点组合）。把 `lambda=infinity` 解释为 top mass。
已有 phase-geometry 进一步说明实际只出现以下两种形式之一：

- **Uniform light branch:** `M=n/lambda+o(n)` 个 tracked labels，每个概率
  `lambda/n+o(1/n)`，没有 top mass。
- **Light + top branch:** `M=alpha n/lambda_*+o(n)` 个 tracked labels，每个
  概率 `lambda_*/n+o(1/n)`，总 light mass为
  `alpha=(1-epsilon)/(1-epsilon_*)`，其余 `1-alpha` 映到永久 YES 的 top。

下面先证明一层 light alphabet 加可选 top 的 tail lemma，再给出有限类直和推论。
因此主定理只依赖凸几何，不依赖 `lambda_*` 的十进制值或 computer-assisted root
certificate。

## 3. 需要的全局 information-spectrum lemma

令 `M_n=Theta(n)`，`alpha_n -> alpha in (0,1]`。对一个大小为 `k<=n`
的固定集合，把每个 key 独立送到 `M_n` 个 light labels，每个 label 概率
`alpha_n/M_n`，或以概率 `1-alpha_n` 送到 top。令

\[
C^{(k)}=(C_1,\ldots,C_{M_n})
\]

为 light occupancy vector，`P_{n,k}` 为其分布，

\[
\imath_{n,k}(C)=-\log P_{n,k}(C).
\]

### Lemma 3.1（uniform occupancy information tail）

若 `M_n/n` stays in a compact subset of (0,infinity)`，则存在只依赖该
compact set 和 `alpha` 的常数 `c,C>0`，使得对所有 `k<=n` 和 `0<=t<=n`，

\[
\Pr\!\left[
\imath_{n,k}(C^{(k)})
>M_n H\!\left(\operatorname{Pois}
\left(\frac{\alpha_n n}{M_n}\right)\right)+C\log n+t
\right]
\le
C n^C\exp\!\left[-c\min\left\{\frac{t^2}{n},t\right\}\right].
\tag{3.1}
\]

在 `alpha=1` 时去掉 top；在 `alpha<1` 时 top count由
`k-sum_i C_i` 唯一决定。

### 完整解析证明

令 `K=sum_i C_i`。当 `alpha<1` 时，

\[
K\sim\operatorname{Bin}(k,\alpha_n),\qquad
C\mid K=s\sim\operatorname{Mult}(s;1/M_n,\ldots,1/M_n),
\tag{3.2}
\]

且总 information density精确分解为

\[
\imath_{n,k}(C)=J_k(K)+I_{M_n,K}(C),
\quad
J_k(s)=-\log\Pr[K=s].
\tag{3.3}
\]

Binomial 项无需 CLT：因为其 support 至多 `n+1`，

\[
\Pr[-\log\Pr(K)>a]\le(n+1)2^{-a}.
\tag{3.4}
\]

这是一般事实 `Pr[-log P(X)>a]<=|supp(X)|2^{-a}`。

还必须控制随机 `K` 使 conditional occupancy entropy 高于容量 endpoint 的可能性。
Poisson entropy 在这里涉及的有界 load interval上 Lipschitz，所以对某个常数 `L`，

\[
M_nH(\operatorname{Pois}(K/M_n))
\le M_nH(\operatorname{Pois}(\alpha_n n/M_n))
+L(K-\alpha_n k)_+.
\tag{3.5}
\]

而 binomial Chernoff 给出

\[
\Pr[(K-\alpha_n k)_+>v]
\le \exp[-c\min\{v^2/n,v\}].
\tag{3.6}
\]

证明 (3.1) 时先取 `v=t/(4L)`。坏的 `K` event 已有目标尾界；好的 event
上 conditional source mean至多容量 rate加 `t/4`。只使用 (3.4) 而遗漏这一步
是不够的，因为向上的 `K` fluctuation 会线性改变 occupancy entropy。

对 conditional multinomial，取独立
`Z_i~Pois(mu)`，`mu=s/M_n`。条件于 `sum Z_i=s`，向量 `Z` 精确服从
式 (3.2)。并且

\[
-\log\Pr[C=c\mid K=s]
=\sum_i[-\log\Pr(Z_i=c_i)]
+\log\Pr[\operatorname{Pois}(s)=s]
\quad\text{on }\sum_i c_i=s.
\tag{3.7}
\]

当 `mu` 位于一个固定正 compact interval 时，Poisson self-information 具有
一致的局部指数矩。这里可完全解析地验证：对
`Y_mu=-ln Pr[Pois(mu)=Z]` 和任意固定 `theta_0<1`，

\[
\mathbb E e^{\theta Y_\mu}
=\sum_{z\ge0}\Pr[Z=z]^{1-\theta}
\tag{3.8}
\]

在 `mu` 的任意正 compact interval及 `|theta|<=theta_0` 上，右侧及其前三阶
`theta` 导数一致收敛；ratio test即可，因为 `theta_0<1`。因此 centered
log-mgf满足 `log E exp(theta(Y_mu-EY_mu))<=V theta^2`，其中 `V` 一致。
Chernoff优化给出

\[
\Pr\left[\sum_i
(-\log\Pr(Z_i)-H(\operatorname{Pois}(\mu)))>t\right]
\le C\exp[-c\min\{t^2/M_n,t\}].
\tag{3.9}
\]

由 Stirling，`Pr[Pois(s)=s]>=c/sqrt(s+1)`。式 (3.7) 中的最后一项非正，故

\[
\Pr[I_{M_n,s}(C)>M_nH(Pois(s/M_n))+x\mid K=s]
\le C\sqrt{n}\exp[-c\min\{x^2/n,x\}]
\tag{3.10}
\]

只需用 (3.9) 的无条件概率除以 conditioning probability。这是精确
de-Poissonization；没有浮点近似，也没有未计费的线性 correction。

剩下 `mu` 接近 0 的 layers 不可直接声称 uniform Poisson Orlicz norm；正确处理是
分层。记容量 Poisson budget

\[
B_n=M_nH(Pois(\alpha_n n/M_n)).
\]

因为 `alpha_n n/M_n` stays in a fixed positive compact interval，存在固定
`b_0>0` 使 `B_n>=b_0n`。又

\[
\log\left|\{c\ge0:\sum c_i=s\}\right|
=\log\binom{M_n+s-1}{s}
\tag{3.11}
\]

除以 `n` 后在 `s/n ->0` 时趋于 0。因此可固定一个 `delta>0`，使所有
`s<=delta n` 都有 `log binom(M_n+s-1,s)<=B_n-b_0n/2`。对任意条件分布，

\[
\Pr[I_{M_n,s}>L\mid K=s]
\le \binom{M_n+s-1}{s}2^{-L}.
\tag{3.12}
\]

注意 (3.12) 才是正确的 low-load argument；support size并不逐点上界
self-information，它只通过 counting 上界 tail probability。

现在令 theorem threshold为 `B_n+C_0 log n+t`。若 `t<C_1 log n`，增大 (3.1)
右侧常数后结论平凡。否则排除三个事件：

1. `J_k(K)>C_0 log n/3+t/4`，由 (3.4) 控制；
2. `(K-alpha_n k)_+>t/(4L)`，由 (3.6) 控制；
3. conditional information超过其 Poisson budget加 `t/4`。

第三项在 `K>=delta n` 时由 (3.10) 控制；在 `K<delta n` 时由 (3.12) 及线性
budget gap控制。其余 event上，式 (3.5) 把随机 conditional budget提高的量限制在
`t/4`，而 `k<=n`。三项 union bound给出 (3.1)。

当 `alpha=1` 时，`K=k` 是确定的，直接删除前两个 binomial事件：若
`k>=delta n` 使用 (3.10)，若 `k<delta n` 使用 (3.12)。所以 alpha=1 并不存在
额外 conditioning gap。

### Corollary 3.2（固定有限个 light classes）

固定 `J=O(1)`。第 `j` 类有 `M_{n,j}=Theta(n)` 个等概率 light labels，总质量
`alpha_{n,j}->alpha_j>0`，并允许剩余 top mass。令 `C` 是所有 classes 的
concatenated occupancy vector，则 Lemma 3.1 成立，容量 budget替换为

\[
B_n=\sum_{j=1}^J M_{n,j}
H(Pois(\alpha_{n,j}n/M_{n,j})).
\tag{3.13}
\]

证明只需先编码 class totals
`(K_1,...,K_J,K_top)~Mult(k;alpha_{n,1},...,alpha_{n,J},beta_n)`；其 support
为 `n^{O(J)}`，self-information tail仍由 counting控制，各 total 的向上偏差由
multinomial Chernoff控制。条件于 totals，各 class occupancies独立，并分别应用
Lemma 3.1 的 conditional Poisson argument。`J` 固定，所以 union bound只改变常数。

这个 lemma 是全解析的；不需要浮点 optimizer、区间程序或 computer-assisted
certificate。它也解释了为何逐 block 的 McDiarmid `log^2 b` 损失不是本质障碍。

## 4. 次指数 horizon 定理

### Theorem 4.1（oblivious subexponential-horizon upper bound）

固定 `epsilon in (0,1)`，令 `f(n)>=1` 满足

\[
\log f(n)=o(n).
\tag{4.1}
\]

在 KLZ 的 fixed-memory、random-access read-only random-tape、无 operation-time
要求模型中，对充分大的 `n`，存在 one-sided ordinary dynamic approximate
membership filter，满足：

1. 支持容量至多 `n` 的合法 distinct-set Insert/Delete/Query histories；
2. 对每一条在 random tape 之前固定、长度至多 `f(n)` 的 history，以下保证成立；
3. 使用一个固定预分配的
   \[
   H_n=nR_{\rm fp}(\varepsilon)+o(n)
   \tag{4.2}
   \]
   bit state space；
4. 每个 member 在每条 tape 上都回答 YES；
5. 对每个 fixed endpoint 和 fixed current nonmember `x`，
   \[
   \Pr_R[\operatorname{Query}(x)=\mathrm{YES}]\le\varepsilon.
   \tag{4.3}
   \]

定理甚至可令整条 fixed history 中进入 sticky ALL-YES state 的概率为 `o(1)`；
该概率直接计入 (4.3)，不是额外排除的 correctness event。

### 参数与证明

令

\[
a_n=\log(f(n)+2)+\log(n+2),\qquad
\theta_n=(a_n/n)^{1/4},
\]

\[
t_n=n\theta_n,\qquad
\eta_n=(a_n/n)^{1/8}.
\tag{4.4}
\]

则 `theta_n,eta_n=o(1)`、`t_n=o(n)`，且

\[
t_n^2/n=\sqrt{na_n}=\omega(a_n).
\tag{4.5}
\]

先取 (2.1) 的一个两点 `o(eta_n)`-optimal convex combination，把 normal FPR
设为至多 `epsilon-eta_n`。对其有限 light points选择
`M_{n,j}=Theta(n)` 与 `alpha_{n,j}`，使

\[
\sum_j\alpha_{n,j}
(1-\alpha_{n,j}/M_{n,j})^n
\ge1-\varepsilon+\eta_n,
\tag{4.6}
\]

且 `alpha_{n,j}n/M_{n,j}` 收敛到相应 light load。可先留 `eta_n/2` 的额外
rejection margin，再按第 6 节的 equal dyadic cell probabilities同时取整；
总分布误差为 `o(eta_n)`，不会破坏 (4.6)。已知显式 phase geometry 下 `J=1`
加可选 top，但证明不需要使用该简化。

实际 finite-`n` capacity information budget为

\[
B_n=\sum_jM_{n,j}
H(\operatorname{Pois}(\alpha_{n,j} n/M_{n,j})).
\tag{4.7}
\]

由 optimal parameters 的连续逼近及 `R_fp` 在固定 interior error处连续，

\[
B_n=nR_{\rm fp}(\varepsilon)+o(n).
\tag{4.8}
\]

这里不需要把有限 `n` budget误写成恰好
`nR_fp(epsilon-eta_n)`；式 (4.8) 已足以得到目标一阶率。

对每个 `k<=n` 定义 typical family

\[
\mathcal A_{n,k}
=\{c:-\log P_{n,k}(c)\le B_n+C\log n+t_n\}.
\tag{4.9}
\]

由 counting，

\[
|\mathcal A_{n,k}|
\le2^{B_n+C\log n+t_n}.
\tag{4.10}
\]

状态存储 current cardinality `k` 和 `c` 在 `A_{n,k}` 中的 rank。所有 `k`
共用同一 fixed slot，因此只需额外 `O(log n)` bits，而不是把各层大小相加。
Insert/Delete 可用任意慢的 hardwired rank/unrank transition；这与 KLZ 的
time-unrestricted model一致。

若更新后的理想 vector 不在对应 `A_{n,k}`，转入 sticky ALL-YES。由 Lemma 3.1、
(4.5) 和对至多 `f(n)+1` 个 endpoints 的 union bound，

\[
\Pr[\text{fixed history ever enters sticky}]
\le f(n)n^C
\exp[-c\sqrt{na_n}]=o(\eta_n).
\tag{4.11}
\]

最后一个 `o(eta_n)` 是严格 diagonal：
`sqrt(na_n)/a_n=sqrt(n/a_n)->infinity`，而
`log(1/eta_n)=O(log n)=O(a_n)`。

第一次 actual failure 必对应某个 ideal endpoint 不在其 typical family：在此之前
actual rank state 与 ideal vector逐步一致。这给出所需 first-failure coupling。

在 normal branch，完全独立 categorical labels 给出容量 `k<=n` 时的精确 FPR

\[
1-\sum_j\alpha_{n,j}
(1-\alpha_{n,j}/M_{n,j})^k.
\tag{4.12}
\]

这是因为 query落入第 `j` 个 light class 的概率是 `alpha_{n,j}`，而每个 current
member 与该 query落入同一指定 cell 的概率是 `alpha_{n,j}/M_{n,j}`。式 (4.12) 最大于
`k=n`；由 (4.6) normal FPR至多 `epsilon-eta_n`。再加 (4.11) 后仍至多
`epsilon`。Sticky state仍 one-sided，故完成证明。

### 4.2 为什么小 block proof 不足，而 global slot 足够

若逐个大小 `b` 的 block 留 tail 并 union bound `f(n)` 个时刻，冗余通常含

\[
n\sqrt{\frac{\log f(n)}b}\,\operatorname{polylog}b.
\]

当 `log f` 接近 `n/log n` 时，要求它是 `o(n)` 会迫使 `b` 太大，并与 counted
scratch memory 冲突。这只是局部编码 architecture 的障碍。全局 slot 的 tail
尺度是 `exp[-Omega(t_n^2/n)]`，而 `t_n=o(n)` 已足以覆盖任意
`log f=o(n)`。

## 5. Heavy/always-YES mass 与 finite-n 细节

1. **Top 不编码 key identities.** 只保存各 light classes 的 counts；current total `k` 单独保存。
   top count是 `k-sum C_i`，仅用于 source probability/rank layer，updates 通过
   `h(x)=top` 识别为 light-count no-op。
2. **Heavy information cost.** `K=sum C_i` 的 binomial source entropy仅
   `O(log n)`；式 (3.4) 给出足够强的 self-information tail。因此 top 不引入
   隐藏的线性 cost。
3. **De-Poissonization.** 只使用 exact identity
   `Mult(s;1/M)=Law((Z_i)_i | sum Z_i=s)`；conditioning probability为
   `Theta(s^{-1/2})`，故只损失 `O(log n)`，不是线性项。
4. **Finite-n pointwise FPR.** 用 `epsilon-eta_n` 而非恰好 `epsilon` 设计参数；
   `M_n` 与 top mass 的取整均取为 `o(eta_n)`。精确公式是 (4.12)，不是把
   conditional light collision误写成 `1-(1-1/M_n)^k`。
5. **所有 set sizes.** `H(Pois(mu))` 随 `mu` 单调不减，所以 `k=n` 的 slot rate
   控制全部 `k<=n`；低 load layers由 Lemma 3.1 的 support-gap 分支覆盖。

## 6. Random tape 与 pointer cost

KLZ 明确允许免费、random-access、read-only random tape。无需 rejection sampling，
也无需一个可能增长的 local pointer。取

\[
L_n=\left\lceil 3\log_2 n+\log_2(1/\eta_n)\right\rceil.
\]

把 tape 分成由 `(x,b) in U_n times [L_n]` 固定寻址的 disjoint blocks；不同 keys
得到完全独立的 uniform `V_x in [2^{L_n}]`。对每个 light class `j` 选整数
`a_{n,j}^{hash}`，依次给它的 `M_{n,j}` 个 labels各分配一个长度
`a_{n,j}^{hash}` 的 interval，剩余 values映到 top。于是第 `j` 类每个 light
label 的概率精确相等于

\[
p_{n,j}=a_{n,j}^{hash}/2^{L_n},
\]

总 light mass精确为 `alpha_{n,j}=M_{n,j}p_{n,j}`。选择这些整数使
`p_{n,j}` 逼近目标 `lambda_j/n`；总 light-mass误差至多
`(sum_jM_{n,j})2^{-L_n}=o(eta_n)`。所以 actual source精确属于
Corollary 3.2 的 finite equal-light-classes模型，并且 (4.12) 是 exact finite-`n`
公式。

每次 operation 只重读 key `x` 的同一个 fixed `L_n`-bit block，不消耗 fresh
random bits，也没有随 history 增长的 tape pointer。即使把 block内 offset计入
working state，也只需 `O(log L_n)=O(log log n)` bits。因此 (4.2) 无隐藏的一阶
pointer cost。

若改用“fresh bits on demand”的等价模拟，则长度 `f(n)=2^{o(n)}` 的 history 所需
pointer只有 `log f(n)=o(n)` bits；但 fresh labels本身不能保证删除/重插时一致，
所以正式 construction 应使用上面的 fixed-address per-key blocks，而不能把 pointer
argument当作 persistent hash 的替代品。

若进一步要求 self-contained charged-seed、efficient word-RAM implementation，
上述 per-key random blocks不再免费；本文不解决该更强实现目标。若只需固定
endpoint的 `n+1`-wise law，也可用短 independence constructions进一步研究
charged seed，但那是另一个 implementation theorem。

## 7. Adaptive quantifiers 的严格反例

### Proposition 7.1（output-adaptive repeated-positive attack）

假设 universe 至少含 `2n` 个预先固定的 distinct keys。先插入其中固定的 `n` 个
形成 `S`，再依次 query另外 `n` 个候选，找到第一个 YES 后立即再次 query同一个
key。第二次 query 的 answer在同一 state、同一 persistent hash下确定为 YES。

条件于 `S` 的 labels，一个独立候选落入当前 accepted region 的概率为

\[
A(S)=1-\alpha_n+\alpha_n\frac{D(S)}{M_n},
\]

其中 `D(S)` 是 occupied light labels 数。`E A(S)` 收敛到目标常数 FPR，且改变
一个 member label只改变 `A(S)` 至多 `O(1/n)`；bounded differences 因而给出
`Pr[A(S)<epsilon/2]=e^{-Omega(n)}`（把 `epsilon/2` 换成任意严格小于目标 FPR
的常数也可）。候选 key blocks彼此独立，所以条件于 `A(S)>=epsilon/2`，扫描
`n` 个候选仍找不到 YES 的概率至多 `(1-epsilon/2)^n`。故被重query的 adaptive
nonmember以 `1-o(1)` 概率回答 YES；条件于已经找到它时，FPR恰为 1。

所以 Theorem 4.1 不能升级为“每个根据先前 answers 选择的 query仍有条件 FPR
至多 epsilon”。这不是 typical-set tail 的缺口，而是 fingerprint semantics 的
基本 adaptive attack。

### Proposition 7.2（seed-adaptive fiber attack）

若对手可读取 `h`：

- 当 top fiber非空时，直接选 top 中的 nonmember，query恒为 YES；
- 无 top 时，只要某个 tracked fiber含两个 distinct keys，插入其中一个并 query
  另一个，仍恒为 YES。

在 `|U|>M+1` 的通常 regime，pigeonhole 已保证后一种 fiber存在。因此本文上界在
seed-adaptive quantifier下的 worst-case FPR是 1。

更一般地，若某模型要求对手在看到 tape 后仍可选择 endpoint和 nonmember，任何
tape/state上存在的 false positive都能被选出；要得到 `epsilon<1` 保证，就必须让
足够大比例的 tapes在所有可达 seed-adaptive states上完全无 false positives。这已
接近 exact membership，而不是 KLZ 的 pointwise-over-randomness模型。

## 8. 最终 verdict

- **Oblivious fixed histories, `log f=o(n)`: PASS.** 全局
  information-spectrum slot给出 `nR_fp(epsilon)+o(n)` fixed memory；这比现有
  polynomial-horizon block theorem严格更强。
- **Output-adaptive histories: FAIL for the proposed fingerprint construction.** repeated-positive
  attack使 conditional FPR达到 1。
- **Seed-adaptive histories: FAIL.** 读 tape 后可直接选择 top key或同 fiber碰撞对。
- **Arbitrary infinite oblivious history: not proved.** 当 `log f`不再是 `o(n)`，
  typical-set redundancy不能同时保持 `o(n)`；全 support composition code可以
  支持无限 history，但率升到 `R_ES`，一般严格高于 `R_fp`。
- **Random-tape pointer: no hidden first-order cost in KLZ.** fixed-address polynomial
  不需要 pointer；fresh-bit simulation 的 pointer在次指数 horizon下也只有 `o(n)`，
  但不能代替 consistent hash。

因此，`R_fp` 在 FOCS/KLZ 最相关的“每条预先固定、次指数长度 history”的量词下
确实可达；它不在 adaptive-history 最强量词下可达。若论文 headline 写成
“subexponential-horizon oblivious upper bound”，该边界是严格且可防审稿攻击的。
