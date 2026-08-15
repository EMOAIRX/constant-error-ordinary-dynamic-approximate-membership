# 常数误差动态 Membership：SODA 级突破研究计划

> 状态：研究议程，不是已证明结果。日期：2026-08-12。
>
> 本文档以 Blelloch–Hu–Kuszmaul–Li–Zhou 2026 年 8 月的新结果为最新基线：uniform fingerprint multiset 已能以 Poisson 熵率和 \(O(1)\) 时间动态维护。因此，单纯把现有 block coder 从 polylog 加速到 \(O(1)\) 已不再构成新的主结果。

## 1. 最新基线与问题重置

令

\[
\delta=-\ln(1-\varepsilon),\qquad
R_{\mathrm{unif}}(\varepsilon)
=\frac{H_2(\operatorname{Pois}(\delta))}{\delta}.
\]

Blelloch–Hu–Kuszmaul–Li–Zhou，*Dynamic Entropy-Encoded Arrays in \(O(1)\) Time with Nearly Optimal Space*，arXiv:2608.06066，Theorem 8.2，给出 uniform fingerprint filter，使用

\[
(1+o(1))nR_{\mathrm{unif}}(\varepsilon)
\]

bit，并支持 worst-case \(O(1)\) 查询与更新，其时间和空间保证为 whp。

当前稿件仍可能新增：

1. 异质 fingerprint loads 的下凸包严格优于 uniform rate；
2. 相变后的候选率
   \[
   R_{\mathrm{FM}}(\varepsilon)
   =\operatorname{lce}\{(1-e^{-\lambda},H_2(\operatorname{Pois}(\lambda))/\lambda)\};
   \]
3. exact IID multiplicity 类内 converse。

但高效动态编码本身已不再是优先权核心。下一篇工作必须提供以下至少一种：

- 普通动态 filter 的新下界；
- 严格低于 \(R_{\mathrm{FM}}\) 的自然新构造；
- 一个新的、匹配上下界的率函数或 separation。

## 2. 主线 A：两选择 placement 的信息守恒或严格改进

### 2.1 自然模型

每个键 \(x\) 公开随机获得两个候选位置

\[
\Gamma(x)=\{h_1(x),h_2(x)\}.
\]

插入算法选择一个 orientation

\[
\sigma(x)\in\Gamma(x),
\]

允许根据当前状态 relocation。查询只检查两个候选位置是否至少有一个被占用。删除只获得键 \(x\)；结构不能免费获得 insertion-time orientation。所有 orientation、routing、stash、relocation metadata 与持久随机种子均计入空间。

定义 \(R_2(\varepsilon)\) 为该模型中的最优一阶空间率。

### 2.2 双向成功标准

以下任一结论均可成为 SODA 主结果。

**严格改进：**存在常数区间及 \(\Delta(\varepsilon)>0\)，使

\[
R_2(\varepsilon)
\le R_{\mathrm{FM}}(\varepsilon)-\Delta(\varepsilon).
\]

这将证明 IID fingerprint multiset 不是 KLZ 常数误差问题的正确普适极限。

**信息守恒：**对所有常数 \(d\)，即使允许状态相关 placement 与 relocation，

\[
R_d(\varepsilon)
\ge R_{\mathrm{FM}}(\varepsilon).
\]

证明内容必须包括 orientation 信息，不能预先固定 placement rule。其核心应是

\[
\text{occupancy entropy 的下降}
\le
\text{orientation/routing entropy 的增加}
+\text{多候选查询的 FPR 代价}.
\]

### 2.3 正确的数学对象

给定当前集合，候选关系形成随机图：键为边，位置为顶点，placement 为边 orientation。需要研究的是

\[
H(\text{state}\mid \Gamma),
\]

而不只是 occupied-vertex vector 的熵。只优化 occupied image 会退化成 vertex-cover/minimum-image 问题，但动态删除还需要区分每条边当前指向哪个端点，或者证明该信息可由更小的共享状态隐式恢复。

### 2.4 第一阶段杀伪

对 \(n\le 8\) 的随机候选图：

1. 枚举或 ILP 求所有 orientations 与 relocation-closed state families；
2. 计算 fresh random edge 命中 occupied set 的概率；
3. 计算 state count 或 \(H(\text{state}\mid\Gamma)\)；
4. 强制 `Delete(x)` 仅由 \(x\)、public candidates 和当前 state 执行；
5. 与有限 \(n\) 的最佳 single-choice benchmark 比较。

若只能在免费 orientation oracle 下得到改进，立即杀掉该构造。

## 3. 主线 B：普通动态 filters 的 exact multi-letter 下界

### 3.1 不预设 fingerprint 的语义模型

固定 public random tape \(r\)。令 \(M_r(S)\) 是集合 \(S\) 的 canonical state，

\[
A_r(S)=\{y:\operatorname{Query}(M_r(S),y;r)=\mathrm{YES}\}.
\]

要求：

\[
S\subseteq A_r(S),
\]

\[
\Pr_r[y\in A_r(S)]\le\varepsilon
\quad(y\notin S),
\]

以及逐 tape 单调性

\[
T\subseteq S\Longrightarrow A_r(T)\subseteq A_r(S).
\]

Insert/Delete 转移必须与 canonical states 兼容。模型不要求 multiplicity recovery、hash partition、zero transparency 或 union preservation。

### 3.2 研究对象不是单字母 FPR

取随机有序不同键 \(X_1,\ldots,X_n\)，令 \(S_k=\{X_1,\ldots,X_k\}\)。需要保留整个 accepted-set trace 的联合信息，例如

\[
Z_{i,j}=\mathbf 1[X_j\in A_r(S_i)],
\]

以及

\[
D_{i,j}=|A_r(S_j)\setminus A_r(S_i)|.
\]

KLZ 在低误差下可把相应 entropy terms 吸收到 \(o(n)\)；常数误差下，逐 key 使用 \(h_2(\varepsilon)\) 上界会损失线性信息。候选突破是联合编码整批 trace，而不是对每个 key 独立编码命中/未命中标志。

### 3.3 候选定理

第一目标不是直接断言答案为 \(R_{\mathrm{FM}}\)，而是证明：

\[
H\ge nL_*(\varepsilon)-o(n),
\]

其中 \(L_*\) 是一个由 exchangeable nested accepted-set processes 定义的显式 multi-letter 变分值。

随后再证明或推翻

\[
L_*(\varepsilon)=R_{\mathrm{FM}}(\varepsilon).
\]

若 Poisson paintbox 是极值，则得到自然语义下界；若不是，optimizer 会给出超越 fingerprints 的新动态范式。

### 3.4 高阶 witness 语言

对固定 \(r,y\)，谓词

\[
f_{r,y}(S)=\mathbf 1[y\in A_r(S)]
\]

是一般单调 Boolean function，其 minimal positive certificates 构成 antichain hypergraph。Fingerprint 对应 singleton-OR witnesses；Bloom/threshold 与相关 ghosts 产生高阶、重叠 witnesses。

必须证明这些 higher-order witnesses 不能降低 multi-letter rank entropy，或者从反例中提炼新结构。不能把单调性偷偷加强为 union-preserving。

### 3.5 第一阶段杀伪

从 \(n=2,|U|=4,\varepsilon=1/2\) 开始：

1. SAT 枚举 deterministic canonical tapes、query masks 与 labeled transitions；
2. LP 混合 tapes，满足 pointwise FPR；
3. 输出完整 accepted traces 和 minimal witnesses；
4. 精确计算每个 KLZ pivot 的 joint coding cost；
5. 比较 singleton paintbox、二阶 witnesses、thresholds 与 shared global ghosts。

之后扩展到 \(n=3,|U|=6\) 或 \(9\)。任何 representation/gluing lemma 必须先通过这些最小方块实例。

## 4. 新候选技术线 C：support-only 压力测试与 deletion certificates

两选择的初步数值显示，精确维护 counts 很可能没有收益，但只保存 occupied support 可能严格击败 (R_{\mathrm{FM}})。以一个 min-rank 两选择模型为例，在 \(\varepsilon=1/2\) 的近似计算中：

\[
R_{\mathrm{count}}\approx 2.8304,
\qquad
R_{\mathrm{support}}\approx 2.1216,
\qquad
R_{\mathrm{FM}}\approx 2.2006.
\]

count 版本明显更差；support-only 代理则有约 (0.079n) bit 的潜在优势。它暴露了当前 exact-multiplicity converse 最关键的缺口：普通 `Delete` 并不要求最后一个副本消失后立刻清除对应 YES 状态。

### 4.1 核心问题

构造只保存 support bits。删除键时，如果无法判断其位置是否仍有其他真实成员，就保留该位置为 ghost，而不清零。这样保持 one-sidedness，但 ghost 会提高未来 FPR。

需要严格刻画：

\[
\text{support entropy 节省}
\quad\text{vs.}\quad
\text{ghost accumulation、repair 与 routing 代价}.
\]

但是，最简单的 sticky-ghost 正面构造已经被标准 pointwise FPR 量词立即排除。对固定历史

\[
\operatorname{Insert}(x),\quad
\operatorname{Delete}(x),\quad
\operatorname{Query}(x),
\]

删除后的 \(x\) 是固定非成员。若结构保留其 support bit，则最后一次查询以概率 \(1\) 返回 YES。因此 fresh random query 的平均 FPR 计算不能替代标准 pointwise guarantee；即使只发生一次删除，never-clear 结构也不合法。

所以正面 ghost-repair 构造降为低优先级。真正值得研究的是负面结果：删除后结构必须以足够概率认证“这个 witness 已没有真实成员”，同时不能清除仍被其他成员依赖的 witness。候选定理是某种 deletion-certificate 或 ghost-conservation lower bound：

\[
H(\text{support snapshot})
+H(\text{deletion certificates})
\ge nR_{\mathrm{FM}}(\varepsilon)-o(n),
\]

或至少严格高于 support-only benchmark。它有机会把普通动态删除语义与 occupancy entropy 连接起来，而不直接假设 exact multiplicity recovery。

### 4.2 不能偷用的资源

- 外部 exact set 或 periodic full rebuild；
- 删除时免费的 insertion-time orientation；
- 能按 seed 选择的 favorable history；
- 不计费的 remote dictionary 或 repair log；
- 只分析 endpoint ghost density而不证明全历史 pointwise FPR。

### 4.3 第一阶段实验

1. 对小图精确枚举可删除 state machines，强制检查历史 `Insert(x), Delete(x), Query(x)`；
2. 测量区分 zero/one/many active witnesses 所需的最小状态数；
3. 允许随机 tapes 后用 LP 施加每个固定删除键的 pointwise FPR；
4. 计算 support entropy 与额外 deletion-certificate entropy；
5. 检验 extra entropy 是否趋近 (H(N\mid \mathbf 1[N>0]))，或对应一个新的 rate-distortion functional。

## 5. 主线 D：rate–horizon–failure reliability function

这条路线直接研究当前典型集 overflow 模型的本质，但若只限于 exact multiplicity 类，模型风险较高。

### 5.1 参数化问题

令历史长度

\[
T_n=2^{\tau n+o(n)},
\]

允许全历史 overflow probability

\[
2^{-\gamma n+o(n)}.
\]

定义达到 pointwise FPR \(\varepsilon\) 所需的最优固定空间率

\[
R(\varepsilon;\tau,\gamma).
\]

预期它由 Poisson/multinomial information density 的大偏差率函数控制。Polynomial horizon 对应 \(\tau=0\)，应回到 Shannon/smooth entropy rate；zero-overflow 或无限枚举历史对应 support entropy。

### 5.2 zero-overflow 端点候选

若 \(q=cn+o(n)\) 个 tracked cells 的所有 weak compositions 都必须表示，则

\[
R_\infty(c)
=(1+c)\log_2(1+c)-c\log_2 c.
\]

但以下问题必须先审计，当前不作为定理：

- permanent-positive mass 是否改变约束；
- universe preimages 是否足以实现所有 compositions；
- 支持所有集合大小还是仅大小 \(n\)；
- arbitrary heterogeneous loads 是否减少所需 cell density；
- public hash 是否泄露线性 side information。

仅证明这个端点可能被视为 stars-and-bars 计数。要达到 SODA，需要显式的中间 reliability curve、匹配上下界，以及最好对一类 dynamic product sources 的通用定理。

## 6. 已淘汰或降级的路线

### 6.1 单纯的 \(O(1)\) histogram coder

arXiv:2608.06066 已给动态 entropy-encoded arrays 和 uniform constant-error fingerprint filter 的 \(O(1)\) 实现。除非得到明显更强的 guarantee（例如新的 fixed-memory/no-failure reliability theorem），否则该方向不再是独立主线。

### 6.2 dense finite-universe det-WHI 单点

只在 \(|U|=2n,\varepsilon=1/2\) 和 deterministic-update WHI 下证明 separation，仍有四重模型限制，更适合 ICALP/ESA。要达到 SODA，至少需要 fully stochastic/general replacement 模型的 sharp curve。

### 6.3 继续扩张 IID load class

更多负载层次、更多相变小数、放宽 heavy-cell 正则性都不会解决一般动态 filter 为什么必须支付 occupancy 信息的问题。

## 7. 研究 portfolio 与停止规则

### 高风险主线

**deletion-certificate entropy。**support-only snapshot 是目前最具体的反例语言，但正面 sticky ghosts 已被 pointwise FPR 杀掉。主目标改为证明删除语义迫使额外保存 last-copy/collision 信息。

停止规则：若结论最终仍需把 exact counts 或 zero-transparent label API 直接写入模型，则没有实现语义升级；应停止并回到 multi-letter accepted-trace 路线。

### 最高影响长期线

**Exact multi-letter semantic lower bound。**先完整刻画 KLZ warmup 的常数误差联合泛函，再尝试 paintbox extremality，随后才接 obfuscating-tree/reconstructible-set 技术。

停止规则：若有限 \(n\) 搜索已显示 one-switch communication functional 显著低于 \(R_{\mathrm{FM}}\)，不再试图靠 bookkeeping 证明 equality，转而设计更强协议或提炼 proof barrier。

### 备选新率函数

**Rate–horizon–failure curve。**只有在 zero-overflow 端点公式通过审计且能推导非平凡中间曲线后，才升级为论文主线。

### 自然备选问题

**Free Build 后的 bounded churn。**定义 `Build(S)` 可以读取完整初始集合，之后结构只能依靠压缩状态支持 \(T\) 次 replacement。争取证明

\[
T=o(n)\Longrightarrow H=H_{\mathrm{static}}+o(n),
\]

而对某个常数 \(\alpha>0\)，

\[
T=\alpha n\Longrightarrow
H\ge H_{\mathrm{static}}+\Omega(n).
\]

该问题定量回答静态 filter 经历多少 churn 后必须支付动态空间代价。它比 WHI 模型自然，但仍比 KLZ 普通动态接口弱。

## 8. SODA 级最低结果包

最终论文至少应满足下列一项：

1. 在普通 arbitrary dynamic filter 模型中给出新的显式常数误差线性下界，严格超过已知静态/旧通信下界；
2. 给出自然 \(d=2\) dynamic placement filter，严格击败 \(R_{\mathrm{FM}}\)，并完整计费删除与 orientation 信息；
3. 证明所有固定 \(d\) placement freedom 都不能击败 \(R_{\mathrm{FM}}\)，形成真正的 canonicalization/information-conservation theorem；
4. 给出匹配上下界的 rate–horizon–failure reliability function，而不是只有 Shannon 与 support 两个端点。
5. 证明 ordinary key-level deletion 所需的 deletion certificates 必然补回 support-only 丢弃的线性信息，而不假设 exact multiplicity recovery。
6. 给出 free-Build bounded-churn 的 sublinear/linear 更新阈值及匹配空间 separation。

没有上述任一条时，不应把模型内相变、实现加速或单点 WHI separation 包装为 SODA 级突破。

## 9. 立即执行顺序

1. 完成 support-only 两选择的 deletion-certificate 小图 state search；
2. 完成 \(n=2,|U|=4\) canonical accepted-trace SAT/LP；
3. 推导 polynomial/exponential horizon 的 smooth-max entropy 数值变分；
4. 验证 free-Build (T=o(n)) 的 static-state + churn-log upper bound；
5. 用新 entropy-array 论文替换当前稿件中的 upper-bound priority 叙事；
6. 根据前两项结果，在“strictly beyond fingerprints”和“paintbox extremality”之间选择正式主线。
