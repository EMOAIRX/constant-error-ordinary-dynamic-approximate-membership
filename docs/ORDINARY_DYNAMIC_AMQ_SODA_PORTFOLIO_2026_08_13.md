# 普通动态 Approximate Membership：SODA 级研究组合

> 日期：2026-08-13。
>
> 状态：研究决策文档。除明确标注“已证”外，本文中的主定理均为猜想或研究目标。本文不使用 history independence、accepted-set monotonicity、exact multiplicity、cell locality、bounded churn 或 seed-dependent hard history 作为普通模型主结果的假设。

## 1. 结论先行

目前仍没有得到一个新的 SODA 级普通动态 filter 定理。最重要的收获不是又多了一个受限模型常数，而是把问题分成了三个原先容易混淆的空间率：

1. **smooth / current-state rate**：典型 fingerprint occupancy 在 whp 空间模型中的 Shannon 率；
2. **exact fixed-state rate**：一个固定长度状态必须覆盖全部可达 multiplicity vectors 时的 enumerative 率；
3. **ordinary lossy dynamic rate**：允许不同 multiplicities 合并、允许 ghosts，但仍须支持 key-only deletion、永久保持零 false negative 和 pointwise FPR 的真正最优率。

在 \(\varepsilon=1/2\) 时，前两者已经严格分离：

\[
R_{\rm smooth}=2.20061148296\ldots,
\qquad
R_{\rm exact}=2.38449984248\ldots.
\]

第三个率目前未知。它不是简单的 Poisson entropy，也不是 stars-and-bars；它正是 ordinary deletion 允许丢掉多少 multiplicity 信息、又必须为在线消除 ghosts 补回多少信息的问题。

综合 novelty、模型强度和证明可执行性，建议把研究资源按以下顺序投入：

1. **有限宇宙 ordinary dynamic chain-rule separation**：在 \(|U|=2n,\varepsilon=1/2\) 证明普通动态率为 \(1\) bit/key；
2. **fresh-distinct incremental 的 multi-layer lower bound**：超过 Lovett--Porat 的 \(1.13\) frontier，且不重复收费同一个状态；
3. **everlasting lossy occupancy transducer**：构造严格低于 \(2.384499842n\) 的完整 fixed-state ordinary upper bound，或证明 deletion information 下界；
4. **rate--horizon--failure 曲线**：作为可闭合的 fallback，但必须给完整中间曲线，不能只给 Shannon 与 all-compositions 两个端点。

其中第一条最符合“简单、普适、能和多个社区对话”的 taste；第二条最可能先产生普通模型新下界；第三条风险最高，但若成功会直接改变对 FOCS 2025 开放问题的理解。

## 2. 唯一主模型

固定完整随机带 \(r\) 后，filter 是任意确定性有限状态 transducer：

- 固定状态空间 \(\mathcal M_r\)，\(|\mathcal M_r|\le 2^H\)；
- query 接受集
  \[
  A_r(m)=\{x:\operatorname{Query}_r(m,x)=\mathrm{YES}\};
  \]
- labeled transitions \(\Delta_r(m,\operatorname{Insert}(x))\) 与 \(\Delta_r(m,\operatorname{Delete}(x))\)；
- 状态可以包含任意历史摘要、routing、ghost、relocation、epoch 和全局 certificate；
- 算法可免费读取固定公共随机带，但不能访问外部 exact set。

对每条固定合法历史 \(h\)、每个时刻和每个当前非成员 \(z\)，要求

\[
\Pr_r[z\in A_r(M_r(h))]\le\varepsilon,
\]

成员则在每条随机带上都必须返回 YES。

下界可以只使用 insertion-only 或 replacement histories，因为它们是普通 fully dynamic API 支持的合法子类；这不是对数据结构增加结构性假设。相反，HI、单调性、exact counts、有限 horizon 和 bounded churn 都不能进入主定理而不在标题与结论中明示。

## 3. 截至 2026 年 8 月的严格基线

### 3.1 已证：smooth heterogeneous fingerprint rate

定义

\[
g(\lambda)=1-e^{-\lambda},
\qquad
r(\lambda)=\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda}.
\]

在 generalized IID fingerprint-multiset 类内，source-coding optimum 是曲线 \((g(\lambda),r(\lambda))\) 的 lower convex envelope。其相变参数为

\[
\lambda_*=0.439931601244785\ldots,
\]

\[
\varepsilon_*=0.355919526120782\ldots,
\qquad
C_*=4.401222965921043\ldots.
\]

因此

\[
R_{\rm FM}(\varepsilon)=
\begin{cases}
r(-\ln(1-\varepsilon)),&\varepsilon\le\varepsilon_*,\\
C_*(1-\varepsilon),&\varepsilon\ge\varepsilon_*.
\end{cases}
\]

特别地，

\[
R_{\rm FM}(1/2)=2.20061148296\ldots.
\]

在与 Blelloch--Hu--Kuszmaul--Li--Zhou 2026 相同的 whp/current-state 空间语义下，其 dynamic entropy-encoded array 可以实现 top/light mixture 的 \(nR_{\rm FM}+o(n)\) 空间与 \(O(1)\) 操作。这个 reduction 是可信的，但基本是其 Theorem 1.1/8.2 的直接 corollary，不足以单独成为 SODA 主结果。

### 3.2 已证：fixed exact-state rate 与 smooth rate 不同

若一个 categorical fingerprint filter 精确维护 \(q\) 个 light counts，并要求一个固定状态块覆盖全部

\[
\{C\in\mathbb N^q:\|C\|_1\le n\},
\]

则 rich fibers 下至少需要

\[
\log_2\binom{n+q}{q}
\]

bits。对于 \(\varepsilon=1/2\)，uniform exact fingerprints 取

\[
q/n=1/\ln 2=1.44269504089\ldots
\]

并使用

\[
R_{\rm exact}(1/2)
=(1+c)\log_2(1+c)-c\log_2c
=2.38449984248\ldots
\]

bits/key。

把 smooth-optimal top/light 参数直接放进 all-compositions code 反而需要

\[
2.61005023755\ldots
\]

bits/key。因此不能把 \(2.2006\) 的 whp entropy-array construction 静默升级成 KLZ fixed-length upper bound。

### 3.3 已证：普通 transition 的一阶信息只恢复静态项

对 distinct nonmembers \(x,y\)，普通模型中可以严格证明 successor collision bound

\[
\Pr_r[\Delta_r(m,\operatorname{Insert}(x))
=\Delta_r(m,\operatorname{Insert}(y))]\le\varepsilon.
\]

删除存在相应的 ghost/collision 表述。这些 pairwise inequalities 可以恢复 Carter 的 \(n\log(1/\varepsilon)\) 静态率，但 frozen masks 和共享 certificates 阻止其直接张量化成额外线性项。

### 3.4 Fresh-distinct Lovett--Porat repair 的准确地位

在 \(|U|/n^2\to\infty\) 时，witness-conflict robust transport 可以把 LP one-cut argument 严格迁移到 fresh-distinct histories，得到

\[
H\ge1.1n-o(n)
\]

以及 one-cut 数值优化约 \(1.10214n\)。

这不是新的数值下界：常数属于 Lovett--Porat 已有 frontier。它目前最多是 API/证明接口的严格化；Claims 12--16 的 finite-\(n\) 代数仍需正式展开。LP 文中提到的 \(1.13\) 是 computer-search remark，不应当作已证明定理引用。

### 3.5 已否决的捷径

- AND amplification 的 \(1.199273n\) 只对 history-dependent monotone filters 成立；
- KLZ Section 5 的机械 lifting 有 partition-dependence gap；
- exact-count two-choice 在 \(\varepsilon=1/2\) 约为 \(2.8304\) bits/key，明显更差；
- support-only two-choice 的 \(2.1216107\) 只是 snapshot entropy，尚不能执行 ordinary key-only deletion；
- fully dynamic retrieval/Bloomier 在 constant value size 下带有更大的 dynamic redundancy，不能给出低于 \(2.2006\) 的 ordinary AMQ upper bound。

## 4. 主线 A：有限宇宙 ordinary dynamic chain-rule separation

### 4.1 为什么这是最有 taste 的问题

取

\[
U=[2n],\qquad |S|\le n,\qquad\varepsilon=1/2.
\]

静态 membership 的最优 covering rate为

\[
f_{\rm stat}(1,1/2)
=2-\frac32h_2(2/3)
=0.6225562489\ldots.
\]

另一方面，普通动态模型有一个完全严格的 \(n\)-bit upper bound。

### Theorem 4.1（已证的 matching-candidate upper bound）

从公共随机带均匀选择一个 \(n\)-子集 \(G\subseteq U\)。结构用一个由 \(U\setminus G\) 索引的 \(n\)-bit vector，精确保存

\[
S\cap(U\setminus G).
\]

查询 \(x\) 时，若 \(x\in G\) 则回答 YES；否则返回对应 membership bit。Insert/Delete 只在 \(x\notin G\) 时更新该 bit。

这个结构：

- 支持任意长合法普通 Insert/Delete history；
- 不依赖 HI、单调性或有限 horizon；
- 永远没有 false negative；
- 对每个固定非成员 \(x\)，
  \[
  \Pr[x\in G]=1/2,
  \]
  因而 pointwise FPR 恰为 \(1/2\)；
- 使用恰好 \(n\) persistent bits。

### Conjecture A（首选 SODA 目标）

任意普通 dynamic filter 在上述参数下都必须使用

\[
\boxed{H\ge n-o(n).}
\]

若成立，将给出

\[
0.622556\ldots n
=H_{\rm static}
<H_{\rm dynamic}
=n-o(n),
\]

即一个 sharp、常数显著、无 HI 假设的 dynamic chain-rule separation。它同时连接：

- ChainedFilter 的 finite-universe static rate；
- ordinary dynamic filters；
- history-independent data structures，但不依赖 HI；
- replacement/Johnson-graph transition systems；
- randomized state compression 与 one-sided automata。

### 4.2 合法的确定性 fiber 结构

固定随机带。对状态 \(m\) 定义 endpoint fiber

\[
\mathcal F(m)=\{S:\text{某条合法历史以集合 }S\text{ 到达 }m\}.
\]

总有

\[
\bigcup_{S\in\mathcal F(m)}S\subseteq A(m).
\]

更重要的是，若 \(S,T\in\mathcal F(m)\) 且 \(|S|=|T|=n\)，记

\[
c=|S\cap T|=|U\setminus(S\cup T)|.
\]

可以对两条隐藏历史执行相同的合法删除：逐个删除 \(S\cap T\)。固定随机带后的确定性转移把它们送到同一个物理状态，而两个隐藏 endpoint 是互不相交的

\[
S\setminus T,\qquad T\setminus S,
\]

各有 \(n-c\) 个元素。因此新状态必须接受至少

\[
(S\setminus T)\cup(T\setminus S),
\]

共 \(2(n-c)\) 个键。共同 replacement 只能把 intersection 与 common-outsider 同步搬移；它保持两隐藏集合的交大小，不能把任意 collision pair 变成两个互补 \(n\)-sets。

这给出一个严格的 pair-collision consequence，但单独仍不足以证明 \(n\) bits：要使用上述 deletion schedule，必须先固定一对 \(S,T\)；不能在看到随机带后挑选某个发生 collision 的 pair。不同固定 pairs 的大 accepted-union 后果也可以分散到不同随机带和不同 histories，pointwise FPR 不能按 pair 直接求和。

### 4.3 真正缺失的 lemma

需要证明一个 **Johnson-fiber continuation packing inequality**。其输入是同一个 fixed-tape transducer 的全部 fibers 和全部 replacement transitions，而不是一个静态 covering。它应把以下三项联合收费：

\[
\text{state 数}
+\text{fiber union 大小}
+\text{由 pair continuations 产生的大 accepted-union histories 数量}.
\]

目标形式可以是：对任意 deterministic transducer with \(K\) states，若每个 reachable \(n\)-set history 的 accepted set 在随机带平均下满足 pointwise \(1/2\)-FPR，则

\[
K\ge2^{n-o(n)}.
\]

证明必须避免选择依赖随机带的 collision pair 或 continuation。最可能的语言是 fractional covering/LP duality：把每个固定 pair-specific continuation 当作一个约束，然后用 Johnson scheme 的对称性构造一个 seed-independent dual certificate。

### 4.4 第一阶段验证与停止条件

1. 对 \(n=2,3,4\) 枚举 deterministic state machines，并用 LP 混合 tapes满足 pointwise FPR；
2. 比较最优状态数与 \(2^n\)，输出最优 fibers，而不是只输出常数；
3. 检验 static-optimal coverings 是否存在 transition-compatible quotient；
4. 尝试在 Johnson association scheme 上把 LP 对称化为只依赖 \(|S\cap T|\) 的有限维问题。

若小实例稳定给出低于 \(2^n\) 的可张量化构造，应立即放弃 \(n\)-bit conjecture，并把该构造升级为新的 ordinary dynamic upper bound。若小实例等于 \(2^n\) 且 dual certificate 呈 Krawtchouk/Johnson 多项式结构，则这条路线优先级最高。

## 5. 主线 B：fresh-distinct incremental 的 multi-layer lower bound

### 5.1 目标不能只是重新认证 \(1.13\)

只把 LP 的 computer search 写成 rigorous \(1.13\) 证书，论文价值有限。SODA 目标应至少是：对 \(\varepsilon=1/2\)、\(|U|/n^2\to\infty\) 的任意普通 fresh-distinct incremental filter，证明

\[
\boxed{H\ge(1.13+\delta)n-o(n)}
\]

for an explicit \(\delta>0\)，最好达到 \(1.2n\) 以上。因为 proof 只使用合法 insertions，结论自动适用于 fully dynamic filters。

### 5.2 为什么现有递归不合法

LP one-cut proof 在深度一使用一次 \(2^H\) state budget。机械递归会把容量 \(k\) 的独立最优内存 \(M_D(k,\varepsilon)\) 当成当前机器在第 \(k\) 层的 state-count bound，从而重复收费同一个 \(H\)-bit transducer。

因此缺失的不是更多数值优化，而是一个 **single-budget multi-layer transition-covering theorem**：

- 同时处理 cuts \(k_d<\cdots<k_1<n\)；
- 全部层只使用一次 \(2^H\)；
- 联合跟踪 prefix-fiber support、conditional good mass 和 final accepted support；
- depth one 必须严格退化为 LP one-cut inequality；
- 允许 frozen masks、共享 certificates 和任意跨层相关性。

### 5.3 建议的数学对象

固定随机带，令 \(V_i\) 是随机 distinct prefix 长度 \(i\) 后的状态，\(L_i(V_i)\) 是对应 fiber union。不要逐层只记录 \(|L_i|\)，而记录 joint profile

\[
\Pi=(V_{k_d},\ldots,V_{k_1},V_n;
|L_{k_d}|,\ldots,|L_{k_1}|,|A_n|).
\]

待证 inequality 应直接界定给定一个 profile 后能够产生的 ordered distinct paths 数量，并以

\[
H(V_{k_d},\ldots,V_{k_1},V_n\mid R)
\]

而不是各层 entropy 之和收费。因为这些 states 来自同一个 transducer，该 joint entropy 的处理是突破点。

### 5.4 停止条件

- 若 depth-2 对称变分的最优值不超过 \(1.13\)，停止机械多层路线；
- 若 improvement 只在 monotone/HI tapes 上出现，不升级为主结果；
- 若必须重新引入 KLZ Section 5 的 partition-dependent reconstructible sets，先给 leakage-corrected lemma，否则停止。

## 6. 主线 C：everlasting lossy occupancy transducer

### 6.1 精确问题

现有 \(2.2006n\) 上界只描述典型 current state。要把它升级成完整 fixed-state ordinary upper bound，需要一个从未被现有 entropy-array theorem 提供的 primitive：

> **Everlasting fixed-block lossy occupancy transducer.** 对 \(q=\Theta(n)\) 个 labels 和容量 \(n\)，使用固定 \(H\) bits；支持任意长合法 key-only updates；每条 tape 上零 false negative；每条固定历史、每个当前非成员的 FPR 至多 \(\varepsilon\)；永不 overflow，且不依赖外部 exact set或 live-key enumeration。它可以合并不同 count vectors和保留 ghosts，但必须能在线安全回收 ghosts。

若要求 exact zero transparency，这个目标已被 all-compositions counting 排除。因此任何严格改善

\[
H<(2.38449984248-o(1))n
\]

的 \(\varepsilon=1/2\) construction 都必须真正利用普通 filter 允许的 lossy semantics。

### 6.2 Support-only pressure test

两选择 min-rank support snapshot 在 \(\varepsilon=1/2\) 的 entropy 为

\[
2.1216107112\ldots n,
\]

比 \(R_{\rm FM}\) 还低。但共享 witness 上的 multiplicity \(1\) 与 \(2\) 无法由 support 区分：

- 清除 witness 可能对另一个成员产生 false negative；
- 不清除会在 singleton world 留下 ghost；
- epoch rotation 需要知道旧 epoch 是否仍有 live dependency；
- global rehash 需要枚举 live keys；
- cuckoo relocation 需要保存 later Delete 所需的 route。

因此 publishable 目标有两个互斥方向：

1. **construction**：总 metadata 小于 support gain，并给出永久 ghost recycling；
2. **deletion-information lower bound**：证明任何 ordinary implementation 必须为 last-copy/routing information 付出线性代价。

### 6.3 一个更一般的 deletion-shadow 对象

对 fixed-tape state \(m\) 和 label \(x\)，定义共同合法 subfiber

\[
\mathcal F_x(m)=\{S\in\mathcal F(m):x\in S\}.
\]

执行共同的 \(\operatorname{Delete}(x)\) 后，one-sidedness 强迫

\[
\bigcup_{S\in\mathcal F_x(m)}(S\setminus\{x\})
\subseteq A(\Delta(m,\operatorname{Delete}(x))).
\]

这给出 ordinary filters 中完全合法的 deletion shadow。真正需要的是一个 multi-delete shadow profile theorem：若状态没有保存足够信息来不断细分这些 subfibers，则沿某条固定、seed-independent deletion schedule，accepted unions 必须产生过多 pointwise false positives。

单次 shadow lemma不会给线性项；必须联合整棵 deletion decision tree，并允许不同分支共享同一个全局 certificate。

### 6.4 停止条件

- 只证明 pure support、local counters 或 fixed orientation 的 no-go，不足以成为主论文；
- 构造若依赖 polynomial horizon、sticky ALL-YES 或 backing exact dictionary，只能作为受限 upper bound；
- lower bound 若预设 exact counts、zero transparency 或 per-cell decomposition，不得包装为 ordinary theorem。

## 7. Fallback：rate--horizon--failure reliability function

定义历史长度

\[
T_n=2^{\tau n+o(n)}
\]

和全历史 overflow 概率

\[
2^{-\gamma n+o(n)}.
\]

对 exact fingerprint occupancy source，求最小固定 allocation rate

\[
R_{\rm occ}(\varepsilon;\tau,\gamma).
\]

这应由 multinomial/Poisson information density 的 large-deviation quantile 决定：

- \(\tau=0\) 对应 Shannon/smooth rate；
- exponential horizon 增加一个 reliability penalty；
- zero-overflow endpoint 回到 all-compositions rate。

只有在得到完整中间曲线、matching converse 与 dynamic implementation 时，这条路线才可能达到 SODA。只观察 \(2.2006\) 与 \(2.3845\) 不同，或只证明 stars-and-bars endpoint，贡献不够。

## 8. 推荐的实际执行顺序

### Sprint 1：先杀伪有限宇宙 conjecture

1. 建立 \(n\le4\) 的 ordinary history-dependent replacement automaton SAT/ILP；
2. 对 deterministic tapes枚举 query masks和 labeled transitions；
3. 用 LP 混合 tapes并逐 \((h,x,t)\) 强制 pointwise FPR；
4. 输出最小 state count、fibers 与 dual certificate；
5. 判断 \(H=n\) 是否在小实例已经被反例否决。

### Sprint 2：并行做 depth-2 fresh-distinct functional

1. 把 LP one-cut finite-\(n\) proof完全形式化；
2. 写出只收费一次 state entropy 的 depth-2 counting problem；
3. 先数值求其对称 relaxation；
4. 只有 relaxation 超过 \(1.13\) 才投入完整 proof。

### Sprint 3：upper-bound prototype

1. 枚举小 q 的 lossy count transducers；
2. 测量支持 arbitrary legal \(+e_i/-e_i\) cycles 时最少 ghost states；
3. 比较 support entropy、last-copy certificate 与 route entropy；
4. 搜索能张量化的局部 gadget，而不是直接设计复杂工程 filter。

## 9. SODA 门槛

以下任一项可视为可信的 SODA candidate：

1. ordinary \(|U|=2n,\varepsilon=1/2\) dynamic filter 的 sharp \(n-o(n)\) lower bound，与 \(n\)-bit construction 匹配；
2. ordinary fresh-distinct incremental filters 的新 multi-layer lower bound，严格越过已知 \(1.13\) frontier，并给通用 \(\varepsilon\)-curve；
3. 任意长、fixed-state ordinary filter 的首个严格优于 \(2.384499842n\) 的 \(\varepsilon=1/2\) upper bound；
4. ordinary deletion-information theorem，证明 snapshot-support 的节省必然由 routing/last-copy 信息部分或全部补回；
5. fingerprint occupancy 的完整 rate--horizon--failure reliability function，带匹配上下界与非平凡中间相变。

以下内容不应再作为主结果：

- top/light entropy-array corollary本身；
- monotone/HI amplification 常数；
- exact-count 或 zero-transparent 类内的简单 KKT converse；
- support-only snapshot 数值；
- 只认证 LP 已报告的 \(1.13\)；
- 依赖有限 horizon/overflow 却声称解决 fixed-length ordinary 模型。

## 10. 最终判断

如果目标是“最快形成一篇严谨论文”，异质 fingerprint phase transition 包仍可整理成一个 class-optimal 信息论结果，但它已不是最好的 SODA 赌注。

如果目标是“真正对社区有帮助的突破”，应把中心问题改成：

\[
\boxed{
\text{动态更新兼容性究竟迫使一个 one-sided covering 多保存多少信息？}
}
\]

有限宇宙 \((2n,n,1/2)\) 给出了最简洁的 sharp test case；large-universe fresh-distinct multi-layer inequality给出了最成熟的下界技术入口；everlasting lossy transducer则给出了最直接的构造性挑战。这三条路线都作用于 ordinary model，不需要用强结构性假设制造“突破”。
