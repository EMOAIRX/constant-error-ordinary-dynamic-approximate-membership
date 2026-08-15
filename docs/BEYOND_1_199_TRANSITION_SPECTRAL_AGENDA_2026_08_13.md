# 超越 1.199：ordinary dynamic AMQ 的方法论裁决

> 日期：2026-08-13。状态：研究路线裁决。本文区分已经证明的局部结构、已经否决的单快照路线，以及真正可能成为论文核心的跨层命题。不声称已经解决该命题。

## 1. 结论

\[
H\ge 1.199273n-o(n)
\]

即使最终证明闭合，也不应单独作为论文的 conceptual headline。它由 fixed-error KLZ inequality、full-fiber technical lifting 和标准 AND amplification 组成。新颖部分主要是 lifting repair；数值本身没有解释 ordinary dynamic filter 的最优结构。

Full-fiber lifting可以作为有用的技术 lemma，但只跟踪 fiber union 时需要

\[
|U|/n^2\to\infty.
\]

这个 birthday barrier 在该证明语言中基本 tight，不只是松弛分析造成的。

## 2. 已证：support transport 的精确对象

固定一个 endpoint fiber

\[
\mathcal F\subseteq {U\choose t}.
\]

对 \(x\in\bigcup\mathcal F\)，令

\[
\mathcal F_x=\{S\in\mathcal F:x\in S\},
\qquad
C_x=\bigcap_{S\in\mathcal F_x}S.
\]

执行一次 fresh insertion \(y\) 后，\(x\) 从 transported union 消失，当且仅当

\[
y\in C_x.
\]

因此一次均匀 insertion 的精确平均 loss 为

\[
\frac1{|U|}\sum_x(|C_x|-1),
\]

在相对当前真实 endpoint \(S\) 的版本中应写成

\[
\frac1{|U|-t}
\sum_{x\in W\setminus S}|C_x\setminus S|.
\]

对一个包含 \(q\) 个 fresh labels 的 suffix，坏事件是 label set 成为 hypergraph \(\mathcal F_x\) 的 transversal。Kruskal--Katona lower-shadow theorem可以把它写成 section size与 transversal probability 的严格有限维不等式。

## 3. 已否决：只用 support entropy 的二择一

错误直觉是：

> fiber 大则 transport 稳定；fiber 小则 state 数多。

Rare-witness poisoning否决了它。取一个很厚的主 family，再为每个外部键添加唯一的稀有 witness。这样

\[
\log|\mathcal F|
\]

几乎不变，但 union 可以变成整个 universe，且这些外部 ghosts 的 core size 可达 \(t\)。因此 fiber 总大小或 order-0 entropy 不能控制 transport loss。

两两不交的 \(t\)-sets 组成的 fiber 进一步说明

\[
O(tQ|W|/|U|)
\]

量级可达。只用 \(W\) 无法去掉 \(|U|\gg n^2\)。

## 4. 已否决：只用 posterior Shannon entropy

令 \(\mu_m\) 是条件于 state \(m\) 的 posterior distribution。Posterior weighting会消除 rare-witness 的质量污染，但仍不能从

\[
I(S;M)\le H
\]

推出有用的 transport stability gap。

把全部 \(n\)-sets 随机等分成 \(2^H\) 个等大 fibers。每个 posterior 有恰好 \(H\) bits 的 entropy deficit，但其 random-\(q\)-suffix stability只比全空间静态基线多一个可以忽略的量。Johnson scheme 的谱解释是：线性信息可以藏在 suffix noise operator 几乎看不到的高阶 eigenspaces 中。

因此不存在仅依赖 \(I(S;M)/n\) 的非平凡 Mrs.-Gerber 型 snapshot inequality。

## 5. 真正缺失的结构：跨层 right congruence

上述反例都只构造单个 Johnson layer 上的任意 partition。真实动态 filter 的 states 不是独立 snapshot partitions；同一个 labeled finite-state transducer必须同时实现所有层之间的 maps：

\[
\Delta_y^{\rm ins}:\mathcal P_t\to\mathcal P_{t+1},
\qquad
\Delta_x^{\rm del}:\mathcal P_t\to\mathcal P_{t-1}.
\]

这些 partitions 构成 update language 的 right congruence。单层随机 partition通常不能为所有 labels 配置一致的 forward/reverse maps。

真正有 insight 的核心命题应是：

> 信息可以在一个 Johnson layer 中藏进高阶谱分量，但同一个小状态 labeled transducer 不可能在很多 consecutive layers 和所有 fresh labels 下，永久把它保持在高阶分量；否则某些 posterior sections、support unions 或 reverse fibers 必须膨胀。

这是一条 dynamic spectral leakage principle，而不是静态 covering bound。

## 6. 候选主定理形式

令 \(S_0,S_1,\ldots,S_T\) 是 fresh insertion/replacement hard process，
\(M_t\) 是同一 \(H\)-bit transducer 的状态。对每层 posterior partition定义：

1. support-union cost，控制 one-sided query 的 accepted set；
2. low-degree Johnson spectral mass，控制随机 suffix 可见的 correlations；
3. transition defect，衡量 labeled maps 对 posterior sections 的合并与细分。

需要证明一个 single-budget multi-layer inequality：

\[
H+
\sum_{t=0}^{T-1}\operatorname{Leak}_t
\ge
\operatorname{StaticInformation}
+\Omega(T),
\]

其中所有 \(M_t\) 共享同一个 \(H\)-bit budget，不能逐层重复收费。Pointwise FPR 应把累计 leakage 转化为 query support cost。

最小可发表版本不必直接达到 fingerprint rate，但必须满足至少一项：

- 在 ordinary model 中给出不依赖 \(|U|\gg n^2\) 的新常数；
- 给出第一个 transition-constrained Johnson spectral inequality；
- 证明一类单层优良 coverings 不可能扩展为 dynamic right congruence；
- 或从相同定理同时推出 dynamic AMQ 与 dynamic retrieval 的新下界。

## 7. 对当前工作的 taste 判断

- Full-fiber lift 加 \(1.199273\)：有用的技术结果，单独偏弱。
- Core/transversal identity：漂亮的局部 lemma，仍不足以成主论文。
- Rare-witness 与 random-partition no-go：重要，因为它们严格排除了两类自然证明。
- Transition-compatible spectral leakage：当前最有潜力成为真正主贡献的方向，但尚无定理。

因此下一阶段不应继续优化 \(1.199273\)，也不应继续研究单个 fiber 的更多 entropy surrogate。资源应集中在最小的 depth-2/depth-3 transition-constrained spectral inequality；若小层模型已经允许高阶信息无损隐藏，就应及时终止该路线。
