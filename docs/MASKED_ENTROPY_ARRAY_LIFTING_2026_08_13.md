# Permanent-YES thinning 与动态熵数组的相变 lifting

> 日期：2026-08-13。状态：抽象 thinning lemma 与对 Theorem 8.2 的代数
> lifting 已闭合；实现结论严格继承原论文的 whp-space/whp-time 量词，不宣称
> KLZ fixed-memory 或 history-wide success。KLZ 型 fixed-memory、polynomial-horizon
> 版本由本项目已有的 fixed-slot coder 单独给出，操作时间为 polylogarithmic。

所有对数以 2 为底。令

\[
g(\lambda)=1-e^{-\lambda},\qquad
r(\lambda)=\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda}.
\]

## 1. 一个与 fingerprints 无关的 thinning lemma

设 \(\mathcal F_m\) 是容量 \(m\)、one-sided error \(\varepsilon_0\) 的 ordinary
dynamic approximate-membership filter。初始化时，独立抽取一个 frozen public mask

\[
T:U\to\{0,1\},\qquad \Pr[T(x)=1]=\alpha.
\]

对 \(T(x)=1\) 的 keys 调用 \(\mathcal F_m\)；对 \(T(x)=0\) 的 keys，Insert/Delete
不改变内部状态，Query 永远回答 YES。

### Lemma 1.1（ordinary-filter thinning）

固定一条与 mask seed 独立的合法 history。若在该 history 的所有端点都有

\[
|S_t\cap T^{-1}(1)|\le m,
\tag{1}
\]

则组合结构是一个合法 ordinary dynamic filter，且对每个 fixed current nonmember
\(x\)，其 FPR 至多

\[
(1-\alpha)+\alpha\varepsilon_0.
\tag{2}
\]

若 inner filter 还有概率至多 \(\xi\) 的 resource failure，并在 failure 时改为
ALL-YES，则总 FPR 至多

\[
(1-\alpha)+\alpha\varepsilon_0+\xi.
\tag{3}
\]

**证明。** 若 \(T(x)=0\)，成员与非成员都回答 YES；若 \(T(x)=1\)，所有对
\(x\) 有关的操作与 inner filter 完全一致。故没有 false negatives。对 fixed
nonmember，按 \(T(x)\) 分解概率即得 (2)；把任意 resource-failure event 以
概率 \(\xi\) 加入即得 (3)。删除不需要额外 route metadata，因为同一 frozen
mask 可由 key 重新计算。\(\square\)

这个 lemma 不依赖 inner filter 是 fingerprint、Bloom、quotient 还是其他结构。
但它本身不允许把 inner capacity 从 \(n\) 免费降到 \(\alpha n\)：这需要
seed-independent history 下的同时 load concentration。

### Lemma 1.2（polynomial-horizon tracked-load concentration）

固定常数 \(c,d>0\)，history 长度至多 \(n^c\)，且每个端点 \(|S_t|\le n\)。若
mask 对任意端点的 keys 提供 \(k=\Theta(\log n)\)-wise independence，则取

\[
m=\alpha n+K\sqrt{n\log n}
\tag{4}
\]

并令常数 \(K\) 足够大，可使 (1) 在整条 history 上失败的概率至多 \(n^{-d}\)。

**证明。** 对每个固定 endpoint，\(|S_t\cap T^{-1}(1)|\) 是均值至多
\(\alpha n\) 的 limited-independent Bernoulli sum。标准 \(k\)-th moment
Chernoff bound 令超过 (4) 的概率至多 \(n^{-(c+d+2)}\)。对至多 \(n^c+1\)
个 endpoints union bound。\(\square\)

因此，若容量 \(m\) 的 inner family 使用

\[
mR(\varepsilon_0)+o(m)
\]

bits，则在同一 polynomial-horizon failure 语义下，thinning 给出

\[
n\alpha R(\varepsilon_0)+o(n)
\tag{5}
\]

bits，目标误差为 \(1-\alpha(1-\varepsilon_0)+o(1)\)。这说明任何这类
achievable rate curve 都对 endpoint \((1,0)\) 的连线闭合。

## 2. 对 uniform Poisson fingerprint filter 的精确优化

取 inner uniform filter 的 Poisson load 为 \(\lambda\)。其 conditional FPR 与
每个 tracked key 的 entropy rate 分别为

\[
\varepsilon_0=g(\lambda),\qquad R(\varepsilon_0)=r(\lambda).
\]

为了达到总目标 \(\varepsilon\)，式 (2) 取等给出

\[
\alpha=\frac{1-\varepsilon}{1-g(\lambda)}
=(1-\varepsilon)e^\lambda,
\tag{6}
\]

可行条件为 \(g(\lambda)\le\varepsilon\)。空间率是

\[
\alpha r(\lambda)
=(1-\varepsilon)e^\lambda r(\lambda).
\tag{7}
\]

令 \(\lambda_*\) 是 \(e^\lambda r(\lambda)\) 的唯一全局极小点。本项目的解析
证明与纯有理 certificate 给出

\[
0.4399316012447<\lambda_*<0.4399316012449,
\]

\[
\varepsilon_*=1-e^{-\lambda_*}
=0.35591952612078\ldots,
\]

\[
C_*=e^{\lambda_*}r(\lambda_*)
=4.40122296592104\ldots.
\]

于是 (7) 的 constrained optimum 为

\[
R_{\rm thin}(\varepsilon)=
\begin{cases}
r(-\ln(1-\varepsilon)),&0<\varepsilon\le\varepsilon_*,\\[1ex]
C_*(1-\varepsilon),&\varepsilon_*\le\varepsilon<1.
\end{cases}
\tag{8}
\]

这与 generalized IID fingerprint-multiset lower convex envelope 完全一致。特别地，

\[
R_{\rm thin}(1/2)=2.20061148296052\ldots,
\tag{9}
\]

严格小于 uniform \(\lambda=\ln2\) 的

\[
r(\ln2)=2.28790401364596\ldots.
\]

## 3. Entropy-array lifting theorem

### Theorem 3.1（继承 Theorem 8.2 量词的 O(1)-time 相变上界）

固定常数 \(\varepsilon\in(0,1)\)，且 \(1-\varepsilon=\Omega(1)\)，令
\(U=\operatorname{poly}(n)\)。在 Blelloch--Hu--Kuszmaul--Li--Zhou 2026
Theorem 8.2 的 word-RAM 与 whp resource 语义下，存在 ordinary one-sided
dynamic filter，空间为

\[
nR_{\rm thin}(\varepsilon)+o(n)
\tag{10}
\]

bits，并支持 worst-case \(O(1)\)-time Insert/Delete/Query，概率语义与原
entropy-array theorem 相同。

**构造与核算。**

- 当 \(\varepsilon\le\varepsilon_*\) 时，直接使用 Theorem 8.2 的 uniform
  filter，参数 \(\lambda=-\ln(1-\varepsilon)\)。
- 当 \(\varepsilon>\varepsilon_*\) 时，取
  \[
  \alpha=\frac{1-\varepsilon}{1-\varepsilon_*}
  =(1-\varepsilon)e^{\lambda_*}.
  \]
  mask evaluation 为一次 constant-time sufficiently-independent hash。结构
  始终维护所有 tracked keys 的 fingerprint counts；fingerprint range 按典型
  tracked load
  \[
  m=\alpha n+o(n)
  \]
  校准，inner collision load 为 \(\lambda_*\)。这里 \(m\) 是 range-calibration
  参数，不是一个可能被历史越过的逻辑容量。
- inner fingerprint range 是
  \[
  m/\lambda_*+O(1),
  \]
  不是 \(n/\lambda_*\)。
- 总 FPR 为
  \[
  (1-\alpha)+\alpha(1-e^{-\lambda_*})+o(1)
  =1-\alpha e^{-\lambda_*}+o(1)
  =\varepsilon+o(1).
  \]
  用一个 vanishing negative error margin 吸收有限独立性与 finite-size 误差后，
  可校准为至多 \(\varepsilon\)。
- 空间为
  \[
  m\,r(\lambda_*)+o(n)
  =n(1-\varepsilon)e^{\lambda_*}r(\lambda_*)+o(n),
  \]
  即 (10)。mask seed 与 metadata 为 \(o(n)\)。

实现上不能把容量-\(m\) 的 Theorem 8.2 filter 原样当成黑盒：一张 atypical
mask tape 可能把多于 \(m\) 个当前 keys 标成 tracked。正确做法是重复其 proof：
建立一个长度约 \(m/\lambda_*\) 的 count array，但每个 counter 允许到 \(n\)，
并用底层 dynamic entropy-array theorem 编码。于是所有合法 updates 始终有定义，
zero-FN 是逐 tape 的；对每个 fixed current set，tracked total 为
\(\alpha|S|+o(n)\) 且 count-array empirical entropy 满足上述空间界，概率为
\(1-n^{-\Omega(1)}\)。这恰好是原论文的 current-state whp resource 语义。
Theorem 8.2 proof 中用于移除 free randomness 的 mega-bucket splitting 可原样加入
一个独立 mask bit；其 seed、tracked total counter 与 metadata 均为 \(o(n)\)。

\(\square\)

### 量词边界

Theorem 3.1 不把 2026 theorem 升级成它没有声明的模型：

1. 原定理的 compressed space 与 time 是 whp，不是每张 tape 上固定的
   \(H\)-bit state space；
2. 原定理没有声明一次初始化对任意长或 adaptive history 同时成功；
3. 因此这里安全的表述是“在原 theorem 的 whp resource 语义下”的 closure；
4. 对 seed-independent polynomial history，Lemma 1.2 可以让 outer tracked
   load history-wide 集中，但 inner entropy array 是否具有同样可调的
   history-wide exponent 不能仅从 Theorem 8.2 的正文自动推出。

## 4. KLZ fixed-memory 版本

本项目的 `VERIFIED_MAIN_THEOREM.md` 使用两级 finite-independence hashing 与
fixed-slot block coder，直接给出：对任意固定 \(c,d>0\)，在 polynomial universe、
seed-independent、长度至多 \(n^c\) 的 history 上，存在固定预分配

\[
nR_{\rm thin}(\varepsilon)+o(n)
\]

bits 的 ordinary filter；它逐 tape zero-FN，history-wide sticky ALL-YES 概率
至多 \(n^{-d}\)，并把该概率显式计入 pointwise FPR。其 worst-case operation
time 是 \(\operatorname{polylog}n\)，不是 \(O(1)\)。

所以两个 theorem 的贡献不同：

- entropy-array lifting：\(O(1)\) operations，但继承 whp resource 语义；
- fixed-slot theorem：KLZ-style fixed preallocation 与显式 polynomial horizon，
  但 operations 为 polylogarithmic。

## 5. 尚未解决的核心问题

式 (8) 是 generalized IID exact-multiplicity fingerprint class 的 sharp converse，
不是 arbitrary ordinary filter 的 lower bound。特别是 support-only、multi-choice、
history-dependent 或 lossy reversible summaries 可能不保留完整 occupancy vector。

一个真正能把该相变提升为更广结构定理的目标是：对 block-local、可逆更新、
one-sided query summary，设 Poisson block load 为 \(\lambda\)，局部随机状态为
\(Z\)，fresh-query rejection 为 \(J\)，证明或反驳

\[
H(Z)\ge C_*\lambda J.
\tag{11}
\]

若 (11) 对一个自然且严格大于 exact fingerprints 的 transducer class 成立，
则 thinning 后立即得到 \(R(\varepsilon)\ge C_*(1-\varepsilon)\)，并在 high-error
branch 与 (8) matching。现有 per-layer entropy-distortion inequality 单独不足；
必须使用同一 right-congruence 跨所有 load layers 的兼容性。
