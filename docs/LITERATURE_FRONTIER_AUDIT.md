# Finite-universe replacement membership：敌对式文献与社区价值审计

审计日期：2026-08-11。

## 0. 结论先行

当前交叉模型尚未被我核到的文献隐含解决：

\[
|U|=(1+\lambda)n,\quad |S|=n,\quad
S\mapsto S-\{x\}+\{y\},
\]

配合 one-sided pointwise false-positive guarantee，以及“更新算法只能看当前压缩状态和合法 replacement 标签 \((x,y)\)”的要求。

但模型上的每一个单独成分几乎都有强先例：

- finite-universe 静态 membership 的信息论 benchmark 已在 Carter 型计数论证和 ChainedFilter 中出现；
- 动态 approximate membership 的静态—动态分离已有 Lovett–Porat、Kuszmaul–Walzer、Kuszmaul–Liang–Zhou；
- weak/strong history independence、canonical representation 已是成熟的数据结构安全分支；
- replacement 与 fixed-capacity churn 在 sliding-window filters、cache/filter 工程中有现实原型；
- 公共局部更新、可塑编码、rewriting/local update codes 提供相邻语言，但没有 membership fiber 的 one-sided ambiguity。

所以不能把论文定位成“首次研究动态/历史无关 approximate membership”。真正可能的新贡献只有两类：

1. 一个严格的、线性的静态—replacement-WHI 空间分离；或
2. 一个有限宇宙 replacement filter 的紧空间刻画，最好覆盖不止 history-independent 子类。

最值得追的锚点结论是：

\[
g_{\mathrm{WHI,det}}(1,1/2)=1,
\]

即在 \(|U|=2n,|S|=n,\varepsilon=1/2\) 时，所有“初始化随机、之后更新确定、终点分布 weakly history-independent”的 replacement filters 都需要

\[
n-o(n)\ \text{bits},
\]

而存在 \(n+o(n)\)-bit matching construction。与静态 benchmark

\[
f_{\rm stat}(1,1/2)
=2-\frac32H_2(2/3)
=0.622556\ldots
\]

相比，这会给出一个 sharp linear separation。若只能证明 cylinder-fiber 子类，则不足以单独支撑高水平会议论文，除非同时给出一般 fiber 的 rigidity 定理或更广参数曲线。

## 1. 模型必须如何陈述

### 1.1 主模型

定义状态空间 \(\mathcal M\)，每个 \(n\)-subset \(S\subseteq U\) 对应终点状态分布 \(\mu_S\)。查询满足：

- \(x\in S\) 时无 false negative；
- 对每个固定 \(x\notin S\)，概率 \(\Pr_{M\sim\mu_S}[Q(M,x)=1]\le \varepsilon\)。

合法原子 replacement 为

\[
\tau_{x,y}(S)=S-\{x\}+\{y\},\qquad x\in S,\ y\notin S.
\]

更新 kernel 只能依赖 \((x,y)\) 和当前状态：

\[
\mu_SK_{x,y}=\mu_{\tau_{x,y}(S)}.
\]

这正是 single-snapshot / endpoint-distribution weak history independence。它不是 strong history independence：后者还限制观察多个中间快照或访问轨迹时泄漏的历史信息。

### 1.2 必须分层，而不是混成一个定义

建议同时定义：

\[
g_{\rm rep}^{\rm gen},\qquad
g_{\rm rep}^{\rm WHI},\qquad
g_{\rm rep}^{\rm det-WHI},\qquad
g_{\rm rep}^{\rm canonical}.
\]

- **general replacement**：不要求终点分布 history-independent；
- **WHI replacement**：只要求相同终点集合得到相同状态分布；
- **det-WHI**：build 可随机，但 replacement transition 是确定函数；
- **canonical fixed-seed**：给定全局 seed 后，每个集合只有唯一表示。

包含关系是

\[
\text{canonical fixed-seed}
\subsetneq
\text{det-WHI}
\subsetneq
\text{stochastic-kernel WHI}.
\]

论文若只证明 det-WHI，必须明确它不是一般动态 filter 下界。它的合理性来自“随机性在初始化时固定，此后硬件/数据面更新确定”的实现模式，以及 uniquely represented / canonical data structures；不能声称所有 cuckoo/Xor/ribbon filters 都属于它。

### 1.3 随机性计费

标准文献常允许免费 public random tape 或固定 hash oracle。例如《Fingerprint Filters Are Optimal》显式允许无限只读公共随机带，并仅在需要时计入指针的 \(o(n)\) 成本。当前模型若坚持“所有影响未来的 instance-specific seed、PRNG 状态、metadata 都计入状态”，是合理但更严格的建模选择。

需要区分：

- 算法描述中固定、所有实例共享的公共函数；
- 每个实例随机抽取且未来更新/查询必须继续访问的 seed；
- 每次更新新鲜且无需保存的随机币。

不能把第三类随机币 WLOG 去掉；小实例已有 stochastic kernel 严格强于 deterministic transition 的现象。

## 2. 优先权与覆盖表

| 文献/方向 | 已有准确结论 | 是否覆盖当前模型 | 对论文定位的约束 |
|---|---|---|---|
| Carter et al., *Exact and Approximate Membership Testers*, STOC 1978 ([ACM DOI](https://doi.org/10.1145/800133.804332)) | 建立 approximate membership 的经典计数下界与 fingerprint reduction；动态 filter 的 fingerprint 范式由此开始 | 不覆盖 fixed-capacity replacement + WHI；但静态计数与 fingerprint 不能声称新 | 静态下界应追溯 Carter，不应只归功于 ChainedFilter |
| Li et al., *ChainedFilter*, SIGMOD 2024 ([arXiv:2308.13632](https://arxiv.org/abs/2308.13632)) | finite-universe general membership 静态空间率 \(f(\varepsilon,\lambda)\)，以及 chain rule；§4.3.1 明确说 chain rule 不适用于一般动态 membership | 不覆盖原子 replacement，也不含 HI；其 dynamic 扩展只是替换 elementary filters 的工程框架 | 当前工作不是简单 ChainedFilter 后续；应把它当静态 benchmark 和动机来源 |
| Pagh–Pagh–Rao, *An Optimal Bloom Filter Replacement*, SODA 2005 ([DBLP](https://dblp.org/rec/conf/soda/PaghPR05.html)) | 通过 fingerprint multiset/dictionary 得到动态 AMQ，达到 \(n\log(1/\varepsilon)+O(n)\) 级空间 | 大宇宙、标准 insert/delete、只给渐近 leading term；不刻画 dense finite universe 的精确常数 | “Bloomier/新 filter 已经超越 Bloom 最优性”是误解；它是构造范式，不闭合当前空间率 |
| Dietzfelbinger–Pagh, *Succinct Data Structures for Retrieval and Approximate Membership*, ICALP 2008 ([arXiv:0803.3693](https://arxiv.org/abs/0803.3693))；Porat, CSR 2009 | 静态 retrieval/AMQ 可达 \(n\log(1/\varepsilon)+o(n)\) | 静态、大宇宙；不支持 replacement | 说明 Bloomier/Xor/ribbon 的理论核心是 retrieval；不是动态 lower-bound 框架 |
| Lovett–Porat, *A Space Lower Bound for Dynamic Approximate Membership Data Structures*, FOCS 2010 / SICOMP 2013 ([DOI](https://doi.org/10.1137/120867044)) | 对常数 \(\varepsilon\) 给出动态/甚至 incremental filter 超过静态的线性额外空间 | 参数与证明依赖大宇宙；不处理 \(|U|=(1+\lambda)n\)；不要求 HI | “动态性产生额外空间”已有先例；新意必须是 dense finite-universe 的 sharp rate 或 HI separation |
| Pagh–Segev–Wieder, *How to Approximate a Set Without Knowing Its Size in Advance*, FOCS 2013 ([arXiv:1304.1188](https://arxiv.org/abs/1304.1188)) | unknown-size incremental filter 需要 \(n\log(1/\varepsilon)+\Omega(n\log\log n)\)；核心是隐藏集合共享状态导致 accepted superset 必须在线扩张 | replacement 不是单调插入；但其“state 不知道 fiber 内真实集合”的论证与 support-fiber lemma 高度相邻 | 当前组合路线应明确视为 PSW hidden-set ambiguity 的非单调 replacement analogue |
| Naor–Yogev, *Sliding Bloom Filters* ([arXiv:1304.5872](https://arxiv.org/abs/1304.5872)) | 对最近 \(n\) 个流元素的 sliding-window membership 给出近紧空间界 | 有 fixed-capacity/隐式 eviction，但 eviction 是 FIFO，允许窗口 slack；不含 finite-universe dense rate 或 WHI | replacement 的现实动机不能说首次；必须强调“显式合法 swap + exact current set + snapshot HI”差别 |
| Bender et al., *Bloom Filters, Adaptivity, and the Dictionary Problem*, FOCS 2018 ([arXiv:1711.01616](https://arxiv.org/abs/1711.01616)) | 定义并研究对自适应查询稳健的 AMQ；给出 local/remote 结构和紧结果 | 查询 adversary 维度，不是更新历史独立 | 不要把 snapshot-HI 与 adaptive-query robustness 混为一谈 |
| Bercea–Even, *A Dynamic Space-Efficient Filter with Constant Time Operations*, SWAT 2020 ([arXiv:2005.01098](https://arxiv.org/abs/2005.01098)) | 对常数或较大 \(\varepsilon\) 也能做 space-efficient fully dynamic filters，常数时间、whp；空间为 leading-term 意义的 \((1+o(1))n\log(1/\varepsilon)+O(n)\) | \(O(n)\) 隐藏了当前要研究的全部常数；大宇宙 fingerprint multiset reduction | 不能用“已有 dynamic filter”否定问题，但也不能忽略这是成熟构造基线 |
| Kuszmaul–Walzer, *Space Lower Bounds for Dynamic Filters and Value-Dynamic Retrieval*, STOC 2024 ([DBLP](https://dblp.org/rec/conf/stoc/KuszmaulW24.html)) | 对 dynamic filters 得到 \(n\log(1/\varepsilon)+\Omega(n)\)；建立 dynamic filters 与 value-dynamic retrieval 的分离框架 | 仍是大宇宙；不是 dense finite-universe exact constant | 当前问题必须与其 communication/accepted-set 技术比较，而非只从 ChainedFilter 出发 |
| Kuszmaul–Liang–Zhou, *Fingerprint Filters Are Optimal*, FOCS 2025 ([arXiv:2510.18129](https://arxiv.org/abs/2510.18129)) | 当 \(\varepsilon=o(1)\)、\(|U|=\omega(n/\varepsilon)\) 时，任意 dynamic filter 需 \(n\log(1/\varepsilon)+n\log e-o(n)\)；不要求 HI 或时间限制 | 明确不覆盖常数 \(\varepsilon\)，也不覆盖 \(|U|=\Theta(n)\)；replacement-only 也弱于其 insert/delete API | 这是最重要的当前前沿；正文把 \(\varepsilon^{-1}=\Theta(1)\) 的紧界列为首要 open problem |
| Agarwala–Even, *Approximate Membership with Duplicate Insertions or Deletions of Nonelements* ([arXiv:2412.19249](https://arxiv.org/abs/2412.19249)) | 若允许 invalid delete 或 duplicate insert，则空间退化到 exact-representation 的常数比例；使用 witness/sticky false-positive 论证 | 当前 replacement 明确承诺 \(x\in S,y\notin S\)，所以不覆盖 | 显示 update API 的 promise 本身会决定空间；论文必须把“合法 replacement”写进标题或主定义 |
| Kuszmaul et al., *Tight Bounds and Phase Transitions for Incremental and Dynamic Retrieval*, SODA 2025 ([arXiv:2410.10002](https://arxiv.org/abs/2410.10002)) | 完成 incremental/dynamic retrieval 多个 redundancy regime 的紧界，并发现 phase transition | retrieval query 对非键可返回任意 value；不等同 one-sided membership | 说明社区目前非常关注 dynamism 造成的精确 redundancy；支持本问题的会议价值，但也抬高了“必须 tight”的门槛 |
| Hu et al., *Static Retrieval Revisited*, 2025 ([arXiv:2510.18237](https://arxiv.org/abs/2510.18237)) | 给出静态 retrieval/filter 的紧 time-space tradeoff；其 filter theorem 要求大宇宙条件 | 不覆盖 dense finite universe 或 updates | 若新论文不研究时间，可以不直接竞争，但必须承认“静态 filter optimality”已被进一步细化 |
| Kuszmaul et al., *Resizable Retrieval*, 2026 ([arXiv:2606.15944](https://arxiv.org/abs/2606.15944)) | 解决 2006 年提出的 resizable dynamic retrieval 问题，并给出 dynamic filter corollary | 关注当前大小而非固定 capacity；空间只有 \(O(n)\) 级余项，不给 dense 常数 | dynamic/resizable 不是空白；当前贡献必须是 finite-universe 精确率和/或 HI 代价 |
| Naor–Teague, *Anti-Persistence*, STOC 2001 ([DBLP](https://dblp.org/rec/conf/stoc/NaorT01.html)); Blelloch–Golovin, FOCS 2007 ([DBLP](https://dblp.org/rec/conf/focs/BlellochG07.html)); Naor–Segev–Wieder, ICALP 2008 ([DBLP](https://dblp.org/rec/conf/icalp/NaorSW08.html)) | 建立 weak/strong history independence、uniquely represented hashing、history-independent cuckoo hashing | 不研究 approximate membership 的 finite-universe space；但 \(\mu_S\) 只依赖终点集合的抽象绝非新 | 必须把贡献写成“HI 的空间代价/分离”，不能写成“提出 distributional HI kernel” |
| Bloomier / cuckoo / Xor / binary-fuse / ribbon filters | Bloomier 是 static support lookup/retrieval；Xor、binary fuse、ribbon 是高效静态构造；cuckoo/quotient filters 支持动态更新但通常有 placement-history | 没有给出当前模型的紧空间下界；常规 cuckoo 状态通常不 WHI，静态 peeling 结构通常需 rebuild | 它们是 upper-bound ingredients 和实验 baselines，不是已解决当前理论问题的证据 |
| Malleable coding / locally updatable codes / rewriting codes | 研究源消息变化时的重编码距离、局部读写、受限介质写入 | 通常 decoder 可区分完整消息，或 encoder 知道新旧消息；没有 one-sided membership fiber ambiguity 和公共 kernel 兼容性 | 可放 related work 最后一段，不能作为主定位，也不能声称直接套用其界 |

## 3. ChainedFilter 到底与当前问题是什么关系

### 3.0 三条容易混淆的动态下界必须分开

1. **Lovett–Porat（FOCS 2010；SICOMP 2013）**研究标准 fixed-capacity dynamic/incremental approximate membership。对每个固定常数 \(\varepsilon>0\)，它证明静态大宇宙下界 \(n\log(1/\varepsilon)\) 之外还必须付出正的线性余项；《Fingerprint Filters Are Optimal》把它概括为
   \[
   n\log(1/\varepsilon)+n f(\varepsilon),\qquad f(\varepsilon)>0.
   \]
   这个下界甚至对 insertion-only incremental filters 成立。它不是 unknown-size/resizable 下界，也没有给出常数 \(\varepsilon\) 的 sharp coefficient。

2. **Pagh–Segev–Wieder（FOCS 2013）**研究“不预先知道最终集合大小、并要求空间随当前大小增长”的 extendable/incremental filter。Theorem 3.1 的参数化结论为：若所有 \(\alpha n<m<n\) 的前缀都只用 \(\beta m\) bits，则
   \[
   \beta\ge
   \left(1-\frac1\gamma\right)
   \left(
   \log(1/\varepsilon)
   +(1-9\varepsilon)\log\log_\gamma(1/\alpha)
   -\Theta(1)
   \right).
   \]
   取 \(\alpha=1/\sqrt n\) 得到
   \[
   (1-o(1))n\log(1/\varepsilon)+\Omega(n\log\log n).
   \]
   额外 \(n\log\log n\) 来自“每个当前大小都要紧凑”，不是普通 fixed-capacity dynamic filter 的结论。

3. **Kuszmaul–Walzer（STOC 2024）与 Kuszmaul–Liang–Zhou（FOCS 2025）**重新研究 fixed-capacity dynamic filters 的 sharp linear redundancy。前者把大宇宙、\(\varepsilon=o(1)\) 的下界推进到 \(n\log(1/\varepsilon)+\Omega(n)\)；后者把常数精确到 \(n\log e-o(n)\)。它们不依赖 history independence。

因此不能把 “Lovett–Porat dynamic gap”“PSW unknown-size gap”“Fingerprint optimality” 合并成同一个结果。

### 3.0.1 PSW 的 hidden-set ambiguity 到底是什么

PSW §3 在不限制查询时间时先作 witness closure：固定随机带后，可以 WLOG 令状态对 \(x\) 回答 YES，当且仅当“存在一条与当前状态一致、且曾插入过 \(x\) 的历史”。令 \(\widehat S_i\) 为处理前缀 \(S_i\) 后的 YES-set。由于旧状态 fiber 内的每条候选历史在继续插入下一批元素后仍是合法候选，得到

\[
\widehat S_i\subseteq \widehat S_{i+1}.
\]

这正是“压缩状态不知道 fiber 内哪一个隐藏集合/历史是真的”所迫出的单调闭包。

然后：

- **Lemma 3.2** 通过固定随机带，把 randomized pointwise FPR 转成“对至少一半输入序列，最终 YES-set 测度至多 \(4\varepsilon\)”；
- **Lemma 3.3** 对几何分块前缀做 telescoping，找到某一步使
  \[
  \mu(\widehat S_i)-\mu(\widehat S_{i-1})
  \le
  \frac{4\varepsilon}{\log_\gamma(1/\alpha)-2};
  \]
- **Lemma 3.4** 说明对大量输入，新 block 中最多 \(9\varepsilon\) 比例的元素已经在旧 YES-set 中；
- 最后用 \(\widehat S_i\setminus\widehat S_{i-1}\) 很小来压缩新 block，导出 Theorem 3.1。

当前 support-fiber transport 是这个现象的 replacement analogue：插入不再单调，取而代之的是同一个 \(K_{x,y}\) 必须同时运输一个共享状态 fiber 中所有兼容隐藏集合。PSW 没有处理删除、replacement、Johnson graph 环路或 endpoint WHI，因此不能直接推出当前下界。

### 3.1 是直接后续吗？

不是严格意义上的直接后续。

ChainedFilter 的理论对象是静态 finite-universe membership。其 §4.3.1 明确写道：

- 第二级 filter 构造前需要知道第一级全部 false positives；
- 因而 chain rule 并不完美适配动态场景；
- 一般动态 membership 的 chain rule 甚至不成立。

它建议把 Bloomier filter 换成 Othello hashing、Coloring Embedder、Bloom/Cuckoo filters，以支持某些在线 inclusion/exclusion；这是工程组合，不是动态最优性结论。

更精确地说，ChainedFilter §4.3.1 的论证引用：

- [29] Arbitman–Naor–Segev, *Backyard Cuckoo Hashing*，说明动态 exact membership 可用 \((1+o(1))\) 倍静态 exact-space benchmark；
- [30] Lovett–Porat，说明动态 approximate membership 在大宇宙下需要
  \[
  n f'(\varepsilon,\infty)
  =n C(\varepsilon) f(\varepsilon,\infty),
  \qquad C(\varepsilon)>1.
  \]

它据此写出动态 chain rule 的反例不等式：

\[
f'(0,\lambda)
=f(0,\lambda)
=f(\varepsilon,\lambda)+f(0,\varepsilon\lambda)
<f'(\varepsilon,\lambda)+f'(0,\varepsilon\lambda).
\]

含义不是“所有动态组合都不可能”，而是静态最优率的无损加法分解不能原样升级成一般 dynamic optimum。当前 replacement-WHI 问题正是在一个更窄 API 上问：动态 penalty 能否被精确量化。

### 3.2 《Fingerprint Filters Are Optimal》的精确定理与明示 open question

其 Theorem 1.1 的完整适用范围是：

- \(\varepsilon=o(1)\)；
- \(|U|=\omega(n\varepsilon^{-1})\)；
- filter capacity 为 \(n\)；
- 支持 \(\omega(n)\) 次合法 insertions/deletions；
- 对每个固定非成员 \(x\notin S\) 给 pointwise false-positive probability \(\le\varepsilon\)；
- 不限制 operation time；
- 允许免费无限只读公共随机带。

结论是任何 dynamic filter 都需要

\[
n\log(1/\varepsilon)+n\log e-o(n)
\]

bits。证明先在 history-independent + monotone 子类上作 warmup，随后依次移除 history independence 与 monotonicity，所以最终定理不是 HI-only。

它的 §6 明确把以下问题列为第一 open direction：当

\[
\varepsilon^{-1}=\Theta(1)
\]

时求 tight upper/lower bounds。作者猜测 fingerprint filters 仍应最优，但此时不能把 fingerprints 当作集合，必须按其随机 **multiset distribution** 做信息论最优编码；甚至时间高效的 matching upper bound 也仍开放。论文还明确说，当前 lower-bound proof 不能靠更仔细的 bookkeeping 自然延伸到该 regime。

所以 \(|U|=2n,\varepsilon=1/2\) 完全落在其定理之外：既违反 \(\varepsilon=o(1)\)，也违反 \(|U|=\omega(n/\varepsilon)\)。当前模型只能被称为 constant-error frontier 的 structured finite-universe special case，不能声称解决了其 general open problem。

当前问题真正新增的是：当 filter 不能访问外部 exact set、只能从压缩状态和合法 replacement 标签更新时，静态 covering 的 fiber 是否能在 Johnson graph 的全部边上由同一组公共 kernels 运输。

因此更准确的谱系是：

\[
\text{Carter/ChainedFilter static covering}
+
\text{PSW hidden-set online ambiguity}
+
\text{HI endpoint invariance}.
\]

### 3.2 ChainedFilter 静态 benchmark 的量词要补严

ChainedFilter 的证明把 false-positive rate 写成对 input sets、filter states 和负元素的总体平均。当前模型要求 oblivious pointwise：对每个固定 \(S\) 和 \(x\notin S\) 都满足概率界。

下界没有问题：pointwise guarantee 蕴含平均 guarantee。

上界不能只引用一句“取一个覆盖”。需要显式构造或证明存在 balanced randomized covering，使每个 \((S,x)\) 的 conditional incidence 都不超过 \(\varepsilon+o(1)\)，同时状态数仍为

\[
2^{n f_{\rm stat}(\varepsilon,\lambda)+o(n)}.
\]

一个可行路线是随机选取 accepted supersets，并把 block size 设为 \((\varepsilon-o(1))|U\setminus S|\)，用每个 \(S\) 的亚指数/多项式 degree 做 covering 与 concentration；但论文必须把这个 lemma 写全，不能把 average 和 pointwise 静默互换。

## 4. Bloomier、Xor、Ribbon、Cuckoo 是否意味着“问题已最优”

不意味着。

- **Bloomier filter** 是 static support lookup/retrieval，非键可返回任意值；用随机 fingerprint 可转成 static AMQ。
- **Xor / binary fuse / ribbon** 是 retrieval linear systems 的工程化静态实现，核心优势是接近 \(r n\) bits 和高查询吞吐；更新通常需要重建。
- **Cuckoo / quotient / vector quotient filters** 是 dynamic fingerprint filters；它们证明动态 filter 可行且实用，但不提供 dense finite-universe 的精确最优率，也通常不满足 endpoint history independence。
- **Pagh–Pagh–Rao / Bercea–Even / Bender et al.** 给出理论动态 filters，但 \(O(n)\) 余项在常数 \(\varepsilon\) 下就是主项，不能回答 \(0.622556n\) 与 \(n\) 谁对。

2025 年《Fingerprint Filters Are Optimal》恰恰说明该领域没有结束：它解决的是 \(\varepsilon=o(1)\) 的大宇宙 regime，并明确把常数 \(\varepsilon\) 留作 open problem。当前 dense finite-universe anchor 是这个 open regime 的一个高度结构化特例，而不是被它闭合的情形。

## 5. 真正有社区价值的未决问题

按潜在影响排序：

### A. 常数错误率下任意 dynamic filters 的 sharp bound

《Fingerprint Filters Are Optimal》明确提出。当 \(\varepsilon^{-1}=\Theta(1)\) 时，需要以信息论最优方式编码随机 fingerprint multiset；上下界都未闭合。

这是最主流、最高影响的问题，但比当前 finite-universe replacement-WHI 模型难得多。

### B. finite-universe dynamic/replacement membership 的精确率函数

定义

\[
g_{\rm rep}^{\mathcal C}(\lambda,\varepsilon)
=\limsup_{n\to\infty}\frac1n
\min\log_2|\mathcal M|,
\]

其中 \(\mathcal C\) 分别为 general、WHI、det-WHI、canonical。

核心问题是：

\[
g_{\rm rep}^{\mathcal C}(\lambda,\varepsilon)
\stackrel{?}{=}
f_{\rm stat}(\lambda,\varepsilon),
\]

若不等，动态 penalty 和 history-independence penalty 各是多少？

这是最能涵盖 ChainedFilter、动态 filters、HI 三个社区的问题。

### C. history independence 是否在线性尺度上增加 filter 空间

这是最适合当前工具的会议论文问题：在一个最小参数点证明 sharp separation，随后比较 general stochastic、WHI、det-WHI、canonical 四层。

如果能证明

\[
f_{\rm stat}(1,1/2)=0.622556\ldots
<g_{\rm det-WHI}(1,1/2)=1,
\]

这是一个容易解释、数值显著、且与成熟 HI 文献直接对话的主结果。

### D. value-dynamic retrieval 的 sharp redundancy

《Fingerprint Filters Are Optimal》也明确指出：当 value size \(v=\omega(1)\) 时，minimal perfect hashing 的 \(n\log e-o(n)\) redundancy 是否最优仍开。影响很高，但与当前 fiber/query 模型连接较弱，不应硬塞入同一论文。

### E. resizable filters 的更紧常数与直接构造

2026《Resizable Retrieval》已经解决动态缩放的主要存在性问题，但其 filter corollary 仍有 \(O(n\log\log n)\) 或 \(O(n)\) 级余项；直接 filter-specific 构造与常数优化仍有空间。更偏数据结构构造与时间复杂度。

## 6. 最推荐的会议论文 formulation

### 6.1 一句话问题

> 在一个 self-contained、fixed-capacity 的 one-sided membership filter 中，如果每次合法更新只告知被替换的成员 \(x\) 和新成员 \(y\)，且内存快照不能泄漏更新历史，那么静态信息论最优压缩是否仍然可在线维护？

### 6.2 建议标题

- *The Space Cost of History Independence in Approximate Membership*
- *Static Compression versus Replacement Dynamics in Membership Filters*
- *History-Independent Filters under Fixed-Capacity Churn*

### 6.3 目标主定理

在 \(U=[2n]\)、\(|S|=n\)、\(\varepsilon=1/2\) 下：

1. 静态 pointwise randomized filter 的最优空间为
   \[
   (0.622556\ldots)n+o(n).
   \]
2. 每个 deterministic-update WHI replacement filter 需要
   \[
   n-o(n)
   \]
   bits。
3. 存在匹配的
   \[
   n+o(n)
   \]
   bit construction。

若能再证明以下任一项，论文强度明显提高：

- 同一结论对所有 stochastic-kernel WHI 成立；
- 给出一般 \((\lambda,\varepsilon)\) 的闭式曲线；
- 证明 general replacement 与 WHI replacement 的严格分离；
- lower bound 同时适用于常数 update locality/time 的广泛实现类。

### 6.4 论文必须包含的结构结果

- support-fiber transport / trace equality；
- deterministic forward/reverse kernels 在相关 supports 上形成保概率 partial permutations；
- 初始化随机 token 的质量 multiset、support size、conditional entropy 沿 Johnson graph 不变；
- 一个真正一般的 orbit-versus-selectivity inequality，而不只是若干构造族的 case analysis；
- matching construction；
- 小实例计算只作为 evidence/appendix，不能代替渐近证明。

### 6.5 cylinder theorem 的地位

若先限制

\[
\mathcal F_m=\{S:I_m\subseteq S,\ Z_m\cap S=\varnothing\},
\]

则可以覆盖 accepted-superset 与 frozen/random-cut 两个极端，是很好的技术 warmup。

但只有“cylinder fibers 需要 1 bit/key”时，审稿人会质疑：为什么最优 filter 的 fiber 必须是 cylinder？因此 cylinder 结果最好是：

- 一般 theorem 的第一步；或
- 配合 rigidity theorem，证明任何近最优 fiber 都可近似化为 cylinder；或
- 配合非平凡 lower-bound transfer，把任意 fiber 规约为 cylinder 且损失 \(o(n)\)。

## 7. 现实意义：哪些说法成立，哪些不成立

### 成立的动机

- 固定容量 cache、active-flow table、recent-item set、硬件 admission table 都天然执行“evict \(x\), insert \(y\)”；
- 在 quotienting/bucketing 后，局部 remainder universe 常处于 \(U=\Theta(n)\) 的 dense regime，因此 finite universe 不必被解释成全局 key universe 很小；
- endpoint HI 对持久化内存快照、取证攻击、canonical serialization、deduplication 有意义；
- deterministic-after-seeding 模型接近固定 hash/PRF seed 的硬件或数据面实现。

### 必须承认的限制

- 许多实际 Bloom/LSM filters 背后存在 authoritative exact set；若允许更新算法访问该外部集合且不计空间，它可以每次重建静态最优结构，当前 lower bound 不适用；
- 当前模型不计 update/query time，只说明 self-contained compressed state 的信息障碍；
- dense finite universe 是结构化 regime，不等于标准 64-bit key universe；
- WHI 保护的是快照，不保护已被观察到的 update transcript；
- 若只研究 det-WHI，fresh-randomized relocation filters 不在定理范围内。

因此最诚实的现实表述是：这是对“self-contained canonical/endpoint-private mutable filters”的基础限制，而不是对所有 RocksDB/Cuckoo/Bloom 实现的通用 lower bound。

## 8. 推荐与不推荐判决

### 推荐

**有条件推荐继续。** 条件是目标必须升级成 sharp separation 或 exact rate，而不是只定义 \(g_{\rm rep}\) 并给粗上下界。

优先顺序：

1. 证明 det-WHI anchor 的 \(n-o(n)\) lower bound；
2. matching \(n+o(n)\) construction；
3. 把 pointwise static benchmark 补严；
4. 尝试从 cylinder 推向一般 fibers；
5. 最后再研究 fully stochastic kernels。

### 不推荐

- 不推荐把论文写成 ChainedFilter 的直接 sequel；
- 不推荐以“信息热力学”“可逆物理”作为主卖点；
- 不推荐把 Bloomier/Xor/ribbon 的新变体本身当作理论问题；
- 不推荐用大量构造特例替代一个统一 extremal statement；
- 不推荐在只有 12/13/15-state 小实例和 cylinder theorem 时宣称一般 conjecture 已基本解决；
- 不推荐声称“finite-universe dynamic AMQ 首次被研究”，因为 sliding/extendable/dense-dictionary 相邻结果很多。

## 9. 最终优先权判决

| 可能声明 | 判决 |
|---|---|
| “首次定义 history-independent data structure / endpoint distribution” | 明确不可 |
| “首次给 finite-universe membership 静态信息论表达” | 明确不可 |
| “首次研究 dynamic approximate membership” | 明确不可 |
| “ChainedFilter 的 chain rule 在 dynamic replacement 下仍成立” | 很可能错误；ChainedFilter 自己已说明一般 dynamic chain rule 失效 |
| “首次 sharp 刻画 fixed-capacity replacement + pointwise one-sided error + WHI 的空间” | 当前检索未发现先例，可作为目标声明，但投稿前仍需正式 citation search |
| “history independence 在线性尺度上增加 approximate membership 空间” | 若得到一般 det-WHI 或 WHI 紧分离，将是清楚且有价值的新结论 |
| “解决常数 \(\varepsilon\) dynamic filter open problem” | 当前模型太受限，不能这样声称；最多说为该 open regime 提供结构化特例/新技术 |

## 10. 核心来源

- [ChainedFilter: Combining Membership Filters by Chain Rule](https://arxiv.org/abs/2308.13632)
- [Fingerprint Filters Are Optimal](https://arxiv.org/abs/2510.18129)
- [Static Retrieval Revisited: To Optimality and Beyond](https://arxiv.org/abs/2510.18237)
- [Tight Bounds and Phase Transitions for Incremental and Dynamic Retrieval](https://arxiv.org/abs/2410.10002)
- [Resizable Retrieval](https://arxiv.org/abs/2606.15944)
- [How to Approximate a Set Without Knowing Its Size in Advance](https://arxiv.org/abs/1304.1188)
- [A Space Lower Bound for Approximate Membership with Duplicate Insertions or Deletions of Nonelements](https://arxiv.org/abs/2412.19249)
- [A Dynamic Space-Efficient Filter with Constant Time Operations](https://arxiv.org/abs/2005.01098)
- [Fully-Dynamic Space-Efficient Dictionaries and Filters with Constant Number of Memory Accesses](https://arxiv.org/abs/1911.05060)
- [Bloom Filters, Adaptivity, and the Dictionary Problem](https://arxiv.org/abs/1711.01616)
- [Sliding Bloom Filters](https://arxiv.org/abs/1304.5872)
- [Fast Succinct Retrieval and Approximate Membership using Ribbon](https://arxiv.org/abs/2109.01892)
- [Succinct Data Structures for Retrieval and Approximate Membership](https://arxiv.org/abs/0803.3693)
