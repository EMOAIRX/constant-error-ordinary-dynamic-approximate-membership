# 常数误差动态指纹过滤器的精确空间与相变

> 完整研究草稿。本文的匹配下界属于精确 IID 指纹重数模型；达到相同一阶空间率的上界是普通键接口的动态 membership filter。本文不声称解决任意动态 filter 的常数误差下界。

## 1. 引言

近似成员查询结构位于许多系统的第一道筛选路径上。一次否定回答可以避免访问磁盘、远端节点或昂贵的后端索引；一次假阳性虽然不破坏正确性，却会触发原本可以省去的访问。静态 Bloom filter 已广泛用于 SSTable 等不可变对象，而缓存目录、滑动去重窗口、网络连接状态和持续变化的分片索引还要求结构在固定内存中支持插入与删除。本文研究这类单侧错误动态成员查询结构在假阳性率为常数时的精确空间代价。

设结构最多保存 \(n\) 个不同的键，并允许假阳性概率 \(\varepsilon\)。当 \(\varepsilon\to0\) 时，空间中的主导项通常写成

\[
n\log_2\frac1\varepsilon.
\]

当 \(\varepsilon\) 固定时，这一项本身只有 \(\Theta(n)\)，过去被写进 \(O(n)\) 的常数便成为问题的全部。Kuszmaul、Liang 与 Zhou 在《Fingerprint Filters Are Optimal》中证明了低误差区间中动态 fingerprint filter 的最优性，并指出常数误差下需要压缩的是一个 fingerprint multiset，而不是普通集合。他们同时留下两个不同方向：如何高效达到该 multiset 的信息率，以及如何对任意动态 filter 证明匹配下界。本文完成前一个方向，并在一个明确而广泛的 IID fingerprint-multiset 类中给出精确 converse；后一个一般下界仍然开放。

动态删除解释了为什么 multiset 无法被跳过。设随机函数 \(h\) 把每个键映射到一个指纹单元 \(j\)，当前集合为 \(S\)，并令

\[
N_j=\bigl|\{x\in S:h(x)=j\}\bigr|.
\]

查询只需判断 \(N_{h(x)}>0\)，但删除必须把对应重数减一。如果结构只记录某个指纹是否出现过，就无法区分“该单元中只有被删除的键”和“还有其他键与它碰撞”。因此，支持精确删除的指纹核心所维护的自然对象是占用向量

\[
N=(N_1,N_2,\ldots).
\]

标准 fingerprint reduction 通常令所有指纹单元等概率出现。本文允许不同单元具有不同概率 \(p_j\)，同时允许一个永久肯定区域（permanent-positive region）：映射到该区域的查询恒回答 `YES`，结构也不保存相应重数。这里的异质性不是由已知的键热度、查询频率或语义类别产生的。每个原始键都服从同一个 IID categorical law；对任意预先固定的键，它进入各区域的概率完全相同。换言之，键仍然对称，异质性只存在于隐藏的随机指纹划分中。

考虑概率为 \(p=\lambda/n\) 的轻指纹单元。在容量达到 \(n\) 时，它的占用数渐近服从 \(\operatorname{Pois}(\lambda)\)。该单元对假阳性的贡献是其非空概率，而每个被映射键所承担的信息成本是占用熵除以平均负载。定义

\[
g(\lambda)=1-e^{-\lambda},
\qquad
r(\lambda)=\frac{H(\operatorname{Pois}(\lambda))}{\lambda},
\tag{1.1}
\]

其中熵以 bit 为单位，并约定 \(g(\infty)=1\)、\(r(\infty)=0\)。端点 \(\lambda=\infty\) 正是永久肯定区域：它不需要存储状态，但使用了一单位错误概率。

对于有限的概率向量，容量为 \(n\) 时，一个固定非成员的碰撞概率为

\[
p_{\mathsf{top}}+
\sum_jp_j\bigl[1-(1-p_j)^n\bigr].
\tag{1.2}
\]

定义键质量加权的负载分布

\[
\nu_n=\sum_jp_j\,\delta_{np_j}
+p_{\mathsf{top}}\delta_\infty.
\]

\(\nu_n\) 不是均匀选择一个指纹单元后看到的分布，而是随机选择一个键后看到的单元负载。式 (1.2) 渐近等于 \(\int g\,d\nu_n\)，占用向量的每键熵渐近等于 \(\int r\,d\nu_n\)。因此，精确的一阶率由以下变分问题给出：

\[
R_{\mathrm{FM}}(\varepsilon)
=
\inf_{\nu:\,\int g\,d\nu\le\varepsilon}
\int r\,d\nu.
\tag{1.3}
\]

它等于曲线 \((g(\lambda),r(\lambda))\) 与端点 \((1,0)\) 的闭下凸包。这个优化存在一个非平凡相变。设 \(\lambda_*\) 是

\[
\lambda H'(\lambda)+(\lambda-1)H(\lambda)=0,
\qquad H(\lambda)=H(\operatorname{Pois}(\lambda))
\tag{1.4}
\]

的唯一正根，并令

\[
\varepsilon_*=1-e^{-\lambda_*},
\qquad
C_*=e^{\lambda_*}\frac{H(\operatorname{Pois}(\lambda_*))}{\lambda_*}.
\]

则

\[
R_{\mathrm{FM}}(\varepsilon)=
\begin{cases}
\displaystyle
\frac{H(\operatorname{Pois}(-\ln(1-\varepsilon)))}
{-\ln(1-\varepsilon)},
&0<\varepsilon\le\varepsilon_*,\\[1.4ex]
C_*(1-\varepsilon),
&\varepsilon_*\le\varepsilon<1,
\end{cases}
\tag{1.5}
\]

其中

\[
\lambda_*=0.4399316012\ldots,
\quad
\varepsilon_*=0.3559195261\ldots,
\quad
C_*=4.4012229659\ldots\ \text{bits}.
\]

当 \(\varepsilon\le\varepsilon_*\) 时，所有轻单元使用同一负载 \(\lambda=-\ln(1-\varepsilon)\)，uniform fingerprints 最优。当 \(\varepsilon>\varepsilon_*\) 时，继续均匀提高所有单元的负载反而次优。最优设计把轻区负载固定在 \(\lambda_*\)，并将新增错误预算放入随机的永久肯定区域。轻区的键质量为

\[
\alpha
=\frac{1-\varepsilon}{1-\varepsilon_*}
=(1-\varepsilon)e^{\lambda_*}.
\tag{1.6}
\]

这不是预先识别并放弃某类“不重要的键”；每个固定键落入永久肯定区域的概率都相同。

信息论公式本身还不足以给出动态数据结构。公开哈希函数可能泄露占用信息，变长的典型集编码也不能直接放进固定内存，而完全随机函数无法由短种子表示。本文分别解决这三个问题：首先证明公开哈希关于占用向量只提供 \(o(n)\) bit 的一阶信息；其次构造固定槽的精确 multinomial 整数区间码；最后用外层有限独立哈希控制 block load，用独立的内层哈希在每个正常 block 中恢复真正的 IID multinomial law。

最终得到的普通动态 filter 使用

\[
nR_{\mathrm{FM}}(\varepsilon)+o(n)
\]

bit，包括哈希种子、元数据、对齐和工作空间；每次插入、删除和查询耗时 \(\log^{O(1)}n\)。对任何在初始化种子之前固定、长度至多 \(n^c\)、容量至多 \(n\) 的合法历史，整个历史进入 sticky `ALL-YES` 状态的概率至多 \(n^{-d}\)。结构始终没有假阴性；对每个预先固定的时刻和当前非成员键，假阳性概率至多为 \(\varepsilon\)。

### 1.1 主要贡献

本文的贡献是以下四部分形成的整体，而不是“首次使用非均匀 fingerprints”或“首次设置 always-YES 区域”。

1. 我们刻画 generalized IID fingerprint-multiset 类的精确一阶空间率，并将其写成 Poisson 占用曲线的闭下凸包。
2. 我们解析求出该下凸包，证明 uniform design 在 \(\varepsilon>0.355919526\ldots\) 时严格次优，并得到唯一相变。
3. 我们把公开哈希视为 side information，证明在 
   \(|U|/n\to\infty\) 时它只能减少 \(o(n)\) bit，从而得到 exact IID multiplicity 类中的匹配 converse。
4. 我们以固定槽 block coder 和两层有限独立哈希实现同一空间率，得到固定预分配内存、最坏情形 polylog 时间的普通 key-level 动态 filter。

### 1.2 结论边界

类内下界不是从普通 `Delete`/`Query` 行为反推出重数。我们将“正常状态可以恢复全部 tracked multiplicities”明确作为 fingerprint-multiset core 的定义要求。该 converse 不覆盖相关的 exchangeable partitions、multiple-choice 或 cuckoo placement、state-dependent rehashing、seed-adaptive histories，以及不需要恢复指纹重数的一般动态 filter。

另一方面，上界使用有限独立哈希而不是真正的 IID 随机函数。它达到与 IID 类最优率相同的一阶系数，但这不意味着有限独立构造本身属于 converse 的 IID source class。本文解决的是 KLZ 所留下的 time-efficient fingerprint-multiset upper-bound side；任意动态 filter 的常数误差匹配下界仍然开放。

## 2. 模型、保证与记号

本节把信息论下界的模型与数据结构上界的模型分开定义。这样可以避免把“类内最优”误读成“任意动态 filter 最优”。

所有熵均以 bit 为单位，\(\ln\) 表示自然对数。容量参数为 \(n\)，误差 \(\varepsilon\in(0,1)\) 固定。宇宙 \(U_n\) 的键可由 \(\Theta(\log n)\)-bit word 表示。

### 2.1 动态 membership 接口

一个 one-sided dynamic membership filter 支持：

- `Insert(x)`：要求 \(x\) 当前不在集合中；
- `Delete(x)`：要求 \(x\) 当前在集合中；
- `Query(x)`：若 \(x\) 在集合中必须返回 `YES`；若 \(x\) 不在集合中，可以以至多 \(\varepsilon\) 的概率返回 `YES`。

历史是容量不超过 \(n\)、长度不超过 \(n^c\) 的合法 distinct-key 操作序列，并在初始化随机种子之前固定。概率仅对初始化种子取。本文不保证由种子、内部状态或先前响应自适应选择的历史。

### 2.2 exact IID fingerprint-multiset 类

对下界，取 categorical law

\[
p_n=(p_{n,\mathsf{top}},p_{n,1},\ldots,p_{n,q_n}),
\qquad q_n=O(n).
\]

公开随机映射 \(h:U_n\to\{\mathsf{top},1,\ldots,q_n\}\) 在不同键上 IID，并服从 \(p_n\)。正常状态必须存在确定性恢复算法，给定内存状态、公开随机带和当前集合大小，可以恢复

\[
N_j=|\{x\in S:h(x)=j\}|,
\qquad 1\le j\le q_n.
\]

查询规则固定为：映射到 \(\mathsf{top}\) 时返回 `YES`；映射到 tracked cell \(j\) 时返回 \(\mathbf 1[N_j>0]\)。所有行为相同的 permanent-positive labels 均合并为一个 \(\mathsf{top}\) 类。

轻单元满足某些固定常数 \(0<a\le A<\infty\) 下的正则性条件

\[
\frac an\le p_{n,j}\le\frac An.
\tag{2.1}
\]

允许有限个 heavy tracked categories；其重数向量只有多项式大小的支持，因此一阶熵为 \(o(n)\)。轻区总质量假设有固定正常数下界。对 public-hash converse 还要求

\[
\frac{|U_n|}{n}\longrightarrow\infty.
\tag{2.2}
\]

这个条件是实质性的：若 \(|U_n|=n\) 且当前集合就是整个宇宙，公开的 \(h\) 已经完全确定占用向量，条件熵可以降为零。

### 2.3 上界模型

动态上界只要求 

\[
|U_n|=n^{O(1)},
\tag{2.3}
\]

从而键可嵌入大小为 \(n^{O(1)}\) 的有限域。实现使用固定预分配内存，并允许在整个固定历史中以至多 \(n^{-d}\) 的概率进入 sticky `ALL-YES` 状态。进入该状态后，更新成为 no-op，所有查询返回 `YES`；因此不会产生假阴性。该失败概率被计入假阳性预算。

## 3. 三个主定理

### 3.1 类内信息论下界

> **定理 3.1（exact IID fingerprint-multiset converse）**  
> 考虑第 2.2 节的模型，设 \(q_n=O(n)\)、\(|U_n|/n\to\infty\)，正常状态可以恢复全部 tracked multiplicities，并且对每个在公开随机带之前固定的构造历史，恢复失败概率为 \(o(1)\)。定义
> \[
> \nu_n=
> \sum_{j\in L_n}p_{n,j}\delta_{np_{n,j}}
> +\Bigl(1-\sum_{j\in L_n}p_{n,j}\Bigr)\delta_\infty,
> \]
> 其中 \(L_n\) 为满足式 (2.1) 的轻单元集合，有限 heavy/top 质量置于 \(\infty\)。若 pointwise FPR 至多为 \(\varepsilon\)，则任何固定 \(B_n\)-bit 内存满足
> \[
> B_n\ge nR_{\mathrm{FM}}(\varepsilon)-o(n).
> \]
> 更精确地，
> \[
> \frac{B_n}{n}
> \ge\int r(\lambda)\,d\nu_n(\lambda)-o(1),
> \qquad
> \int g(\lambda)\,d\nu_n(\lambda)
> \le\varepsilon+o(1).
> \]

证明见附录 A–C。核心是：对一个独立的随机 \(n\)-子集，公开哈希只泄露 \(o(n)\) bit；Fano 不等式迫使内存保存几乎全部 occupancy entropy；该 entropy 等于各 Poisson marginal entropies 之和加 \(o(n)\)。

### 3.2 Poisson 曲线的解析相变

> **定理 3.2（唯一相变）**  
> \(R_{\mathrm{FM}}\) 具有式 (1.5) 的显式分段形式。方程 (1.4) 有唯一正根，并且
> \[
> 0.4399316012447<\lambda_*<0.4399316012449,
> \]
> \[
> 0.35591952612072764
> <\varepsilon_*<
> 0.35591952612085648,
> \]
> \[
> 4.4012229659190423
> <C_*<
> 4.4012229659230444.
> \]
> 因此 uniform fingerprints 在 \(0<\varepsilon\le\varepsilon_*\) 时最优，在 \(\varepsilon>\varepsilon_*\) 时严格次优。高误差分支的唯一最优边界设计混合负载 \(\lambda_*\) 与端点 \(\infty\)。

证明见附录 D。证明并不声称某个辅助函数在整个正半轴上全局凸；我们只证明足以覆盖 \(\lambda_*\) 的局部曲率，再用 Poisson entropy 的单调性完成全局 supporting-line 论证。

### 3.3 动态可实现性

> **定理 3.3（固定内存动态上界）**  
> 固定 \(\varepsilon\in(0,1)\) 和常数 \(c,d>0\)，并设 \(|U_n|=n^{O(1)}\)。存在普通 key-level one-sided dynamic membership filter，使得对每个在初始化种子之前固定、长度至多 \(n^c\)、容量至多 \(n\) 的合法历史：
>
> 1. 总固定内存为
>    \[
>    nR_{\mathrm{FM}}(\varepsilon)+o(n)
>    \]
>    bit，包括哈希种子、metadata、word padding 和 scratch space；
> 2. 每次插入、删除和查询耗时 \(\log^{O(1)}n\) 个 word operations；
> 3. 对所有种子都没有假阴性；
> 4. 对每个预先固定的时刻和当前非成员 \(x\)，
>    \[
>    \Pr[\operatorname{Query}(x)=\mathrm{YES}]\le\varepsilon;
>    \]
> 5. 整个历史中进入 sticky `ALL-YES` 状态的概率至多 \(n^{-d}\)。

证明见附录 E–I。构造使用 \(b=\Theta(\log^2n)\) 的 blocks、精确整数区间码，以及相互独立的 outer/inner finite-independence hashes。

## 4. 从占用向量到变分率

本节解释式 (1.3) 为什么是自然且完整的优化对象。

设轻单元 \(j\) 的概率为 \(p_j=\lambda_j/n\)。容量为 \(n\) 时，它的 occupancy marginal 为 \(\operatorname{Bin}(n,p_j)\)，并收敛到 \(\operatorname{Pois}(\lambda_j)\)。如果一个固定非成员也映射到该单元，它与集合发生指纹碰撞的概率为

\[
1-(1-p_j)^n\longrightarrow1-e^{-\lambda_j}=g(\lambda_j).
\]

与此同时，整个 occupancy vector 的熵并不等于 marginal entropies 的精确和，因为所有坐标之和固定为 \(n\)。但是这种 conditioning 只损失 \(o(n)\) bit。附录 B 证明了更一般的结论：若 \(Z_j\sim\operatorname{Pois}(np_j)\) 独立，则

\[
H(\operatorname{Mult}(n,p))
=\sum_jH(Z_j)+o(n).
\tag{4.1}
\]

乘除 \(p_j\) 后，式 (4.1) 可以写成

\[
\frac1nH(\operatorname{Mult}(n,p))
=\sum_jp_j
\frac{H(\operatorname{Pois}(np_j))}{np_j}
+o(1)
=\int r\,d\nu_n+o(1).
\tag{4.2}
\]

有限个 heavy cells 的每个计数只取 \(n+1\) 个值，因此总熵为 \(O(\log n)=o(n)\)；它们的非空概率趋于一。于是把其键质量放在端点 \(\infty\)，恰好得到 \(r(\infty)=0\)、\(g(\infty)=1\)。同样，单一 top count 由 \(n-\sum_jN_j\) 确定，省略它不改变可恢复信息。

对任意负载分布 \(\nu\)，pair

\[
\left(\int g\,d\nu,\int r\,d\nu\right)
\]

位于曲线 \((g(\lambda),r(\lambda))\) 的闭凸包中。反过来，任意有限凸组合都可通过若干负载 classes 渐近实现：质量为 \(\alpha_i\)、负载为 \(\lambda_i\) 的 class 使用约 \(\alpha_i n/\lambda_i\) 个单元，每个单元概率约为 \(\lambda_i/n\)，取整误差为 \(o(1)\)。平面上的 Carathéodory 定理说明三点已经足够；下一节的几何分析进一步证明最优解实际只需一点，或一点加端点 \(\infty\)。

## 5. 相变的含义

令

\[
F(\lambda)=e^\lambda r(\lambda).
\]

从曲线点 \((g(\lambda),r(\lambda))\) 连到 \((1,0)\) 的割线斜率绝对值正比于

\[
\frac{r(\lambda)}{1-g(\lambda)}
=e^\lambda r(\lambda)=F(\lambda).
\]

因此，高误差分支的支撑线由 \(F\) 的全局最小点决定。直接微分可知 \(F'(\lambda)\) 的符号等于

\[
S(\lambda)
=\lambda H'(\lambda)+(\lambda-1)H(\lambda).
\]

附录 D 证明 \(S\) 在 \(0.4399316012447\) 与 \(0.4399316012449\) 之间变号，并证明该根是全局唯一根。曲线 \((g,r)\) 在根之前严格凸，因此低误差分支保留原曲线；根之后，由 \(\lambda_*\) 处切线与端点 \((1,0)\) 构成下凸包。

例如，当 \(\varepsilon=1/2\) 时，最优异质设计使用

\[
R_{\mathrm{FM}}(1/2)=2.2006114829\ldots
\]

bit/key，而 uniform design 使用

\[
r(\ln2)=2.287904014\ldots
\]

bit/key。差距在 \(\varepsilon\) 接近一时继续扩大。高误差区间更自然的系统解释是内存极紧的第一层筛选器或级联 filter 的廉价前级；本文只证明空间结论，并不声称已经建立端到端系统收益。

## 6. 类内 converse 的证明路线

下界最容易出错的地方，是把公开哈希函数当作与编码无关的免费对象。对于一个固定的命名集合 \(S\)，占用向量在给定 \(h\) 后当然是确定的；因此不能直接写 \(H(N\mid h)=H(\operatorname{Mult}(n,p))\)。正确做法是选择一个独立的随机下界源。

固定查询键 \(x\in U\)，令 \(S\) 在 \(U\setminus\{x\}\) 的所有 \(n\)-子集中均匀分布，并独立选择公开 IID hash。于是 \(x\) 确定不是成员，同时 occupancy marginal 仍是 multinomial。记

\[
C_j=|h^{-1}(j)|.
\]

给定整个 hash function 后，\(N\) 的分布只依赖于总体 histogram \(C\)，并且

\[
I(N;h)=I(N;C)
=H(\operatorname{Mult}(m,p))
-H(\operatorname{Mult}(m-n,p)),
\tag{6.1}
\]

其中这里的 \(m=|U|-1\)。进一步，

\[
I_2(N;h)
\le
\frac{q-1}{\ln2}
\sum_{k=m-n+1}^{m}\frac1k
=o(n)
\tag{6.2}
\]

只要 \(q=O(n)\) 且 \(m/n\to\infty\)。

对每个固定集合 \(S\)，按 canonical order 插入其元素，得到一个 seed-independent history。将结构的失败概率对随机 \(S\) 平均，正常状态的 decoder 仍以 \(1-o(1)\) 概率恢复 \(N\)。occupancy vector 的支持至多为

\[
\binom{n+q}{q}=2^{O(n)}.
\]

Fano 不等式于是给出

\[
B\ge H(N\mid h)-o(n)
=H(N)-o(n).
\]

最后代入式 (4.2) 与 FPR 约束，得到定理 3.1。

## 7. 达到最优率的动态结构

构造只需实现低误差的一点 optimizer 和高误差的两点 optimizer。为了给有限 \(n\) 的取整、有限独立误差和 sticky overflow 留出空间，我们实际按

\[
\varepsilon_n=\varepsilon-\eta_n,
\qquad \eta_n=\frac1{\log n}
\]

选参数。连续性保证

\[
nR_{\mathrm{FM}}(\varepsilon_n)
=nR_{\mathrm{FM}}(\varepsilon)+o(n).
\]

低误差时取 \(\alpha=1\)、\(\lambda=-\ln(1-\varepsilon_n)\)。高误差时取 \(\lambda=\lambda_*\)，并令

\[
\alpha=\frac{1-\varepsilon_n}{1-\varepsilon_*}.
\]

轻区分成 \(B\) 个 blocks，每个 block 含

\[
b=2^{\lceil2\log_2\log_2n\rceil}=\Theta(\log^2n)
\]

个指纹单元。outer hash 决定 `top` 或某个 block，inner hash 决定 block 内坐标。

### 7.1 为什么需要两层哈希

outer hash 使用 \(k_{\mathrm{out}}=\Theta(\log n)\)-wise independence。有限独立高阶矩界保证，对所有 block-time pairs 做联合界后，每个正常 block 的总负载不超过

\[
s_{\max}
=\lambda_nb+A\sqrt{b\log n}
=\Theta(\log^2n).
\]

inner hash 与 outer hash 独立，并使用 \(k_{\mathrm{in}}=s_{\max}\)-wise independence。固定一个 endpoint，并条件于所有活跃键的完整 outer assignment。某个正常 block 中至多有 \(k_{\mathrm{in}}\) 个键，因此它们的 inner labels 是真正的 IID uniform variables。相应 occupancy vector 条件于 block total \(s\) 后精确服从

\[
\operatorname{Mult}\left(s;\frac1b,\ldots,\frac1b\right).
\tag{7.1}
\]

这里没有假设“有限独立性在任意条件化后仍然保持”；精确 multinomial law 来自 inner seed 与整个 outer assignment 的独立性。

### 7.2 固定槽整数码

对满足 \(\sum_i c_i=s\) 的 histogram \(c\)，式 (7.1) 的精确概率为

\[
P_s(c)=\frac{s!}{b^s\prod_i c_i!}.
\tag{7.2}
\]

将 \([b]^s\) 中具有相同 histogram 的字符串排在一起。若 \(M_s(c)=s!/\prod_i c_i!\)，\(R_s(c)\) 是之前所有 groups 的字符串总数，则 \(c\) 占据区间

\[
J_s(c)=
\left[
\frac{R_s(c)}{b^s},
\frac{R_s(c)+M_s(c)}{b^s}
\right).
\]

当

\[
P_s(c)\ge4\cdot2^{-L}
\]

时，整数

\[
z(c)=\left\lfloor
\frac{2^LR_s(c)}{b^s}
\right\rfloor+1
\]

对应的 dyadic point 严格落在 \(J_s(c)\) 内。因此固定的 \(L\)-bit slot 与单独存储的 \(s\) 唯一确定 histogram。因所有分母都是 \(b^s\)，编码、可编码性测试和 rank/unrank 都只需精确整数运算，不需要计算不可表示的 Poisson 概率。

条件信息密度

\[
I_s(c)=-\log_2P_s(c)
\]

在改变一个 inner label 时至多变化 \(\log_2(s+1)\)。McDiarmid 不等式与 Poisson entropy 上界给出公共槽长

\[
L=
bH(\operatorname{Pois}(\lambda_n))
+O\!\left(\sqrt{b\log n}\log b\right),
\tag{7.3}
\]

使每个 block-endpoint 不可编码的概率低于任意指定的 \(n^{-K}\)。实际算法可用截断 Poisson 级数的有理上逼近计算槽长；每槽增加的近似误差取 \(O(b/\log n)\) bit，总计仍为 \(o(n)\)。

### 7.3 空间、时间与全历史失败

总内存由固定 slots、block totals、两个哈希种子、word padding、sticky bit，以及一个可复用 scratch area 组成。其总量为

\[
\alpha n
\frac{H(\operatorname{Pois}(\lambda))}{\lambda}
+o(n).
\tag{7.4}
\]

一次更新先把目标 block 解码到 scratch，修改一个计数并测试新 histogram 是否可编码，成功后才覆盖旧 slot；否则进入 sticky state。查询最坏需要解码到 block 的末端，因此结论是 \(\log^{O(1)}n\) 最坏时间，而不是 \(O(1)\)。

block 数为 \(B=\Theta(n/b)\)，历史包含至多 \(n^c+1\) 个 endpoint。把每个 block-endpoint 的 bad probability 调到 \(n^{-K}\)，其中 \(K>c+d+2\)，无需假设不同时间或不同 blocks 独立，直接 union bound 即得

\[
\Pr[\text{历史中发生 overflow}]\le n^{-d}.
\]

pointwise FPR 使用奇数阶 Bonferroni 截断。对固定非成员 \(x\)，碰撞概率至多为全独立理想值加 \(n^{-\Omega(c+d+1)}\)。再加上 overflow 概率，并用 \(\eta_n=1/\log n\) 的 margin 吸收所有有限 \(n\) 误差，得到定理 3.3。

## 8. 相关工作

KLZ 在 \(\varepsilon=o(1)\) 的区间证明了动态 fingerprint filters 的 sharp optimality，并明确指出常数误差下需要按来源分布压缩 fingerprint multiset。他们没有给出本文的异质 Poisson 率、下凸包相变或达到该率的动态 block coder。本文处理其高效上界侧，并只在 exact IID multiplicity 类中给出匹配 converse。

Pagh–Pagh–Rao 与 Bercea–Even 的动态 multiset dictionaries 说明 multiplicity 是支持删除的正确对象，并给出了固定空间或多项式操作期内的高效结构。其空间通常写成主导项加 \(O(n)\)；在 constant-error regime 中，这个 \(O(n)\) 正好隐藏了本文所求的一阶常数。本文不能声称首次维护动态 fingerprint multiplicities。

Weighted Bloom Filters、后续 popularity-aware filters 以及 Daisy Bloom Filters 已经研究非均匀错误分配；Daisy 也允许某些外部类别始终回答 `YES`。它们的异质性来自已知的输入或查询分布，误差往往对查询分布平均。本文中所有原始键服从同一个 IID law，并对每个预先固定的非成员给出对随机种子的 pointwise FPR；优化对象是动态 occupancy multiset 的熵。

ChainedFilter 用 chain rule 组合静态 membership filters，并讨论 distribution-aware 与 learned settings，但其 lossless chain rule 不覆盖一般动态 membership。elastic、flexible 和 variable-fingerprint cuckoo filters 主要优化扩容、placement、删除便利性或吞吐量；adaptive/broom filters 处理根据先前回答选择查询的对手；retrieval 则保存比 membership 更强的 per-key value 信息。这些方向与本文相邻，但保证和目标均不相同。

| 工作方向 | 异质性来源 | 误差保证 | 动态更新 | multiplicity | 精确线性率 |
|---|---|---|---:|---:|---:|
| 标准 Bloom / uniform fingerprint | 无或 uniform hashing | 通常 pointwise | 部分支持 | 视结构而定 | constant-error 常数未闭合 |
| Weighted Bloom | 外部 key/query weights | 加权或平均 | 多为静态 | 否 | 不同模型 |
| Daisy Bloom | 外部输入与查询分布 | 对查询分布平均 | 静态 | 否 | 其分布模型内有界 |
| ChainedFilter | 组件与数据分布 | 静态模型 | 一般动态 chain rule 不成立 | 否 | 静态率 |
| PPR / Bercea–Even | uniform fingerprints | pointwise / whp | 是 | 是 | \(O(n)\) 项未定常数 |
| KLZ | uniform fingerprint reduction | pointwise | 是 | 是 | \(\varepsilon=o(1)\) 时 sharp |
| 本文 | 隐藏 IID cell probabilities | 对每个固定查询 pointwise | 是 | 是 | IID multiplicity 类内 exact |

## 9. 局限与开放问题

最重要的开放问题仍然是任意动态 filter 的 constant-error 下界：是否每个结构都必须支付至少 \(nR_{\mathrm{FM}}(\varepsilon)-o(n)\) bit，或者 multiple-choice placement、相关随机划分、state-dependent rehashing 等机制可以越过本文的 fingerprint-multiset 边界？

第二个问题是时间。本文达到精确空间率，但操作时间为 polylogarithmic。能否在保持固定预分配空间和 \(o(n)\) redundancy 的同时，把操作时间降到最坏 \(O(1)\) 或高概率 \(O(1)\)，需要更局部的 distribution-sensitive coder。

第三个问题是适应性。本文历史与查询键在初始化种子之前固定。对手若根据过去的回答选择未来操作，可能主动寻找 permanent-positive 或高碰撞区域。把相同空间率扩展到 adaptive query/update histories，可能需要 broom-filter 式修复机制，也可能产生新的线性代价。

## 附录 A：公开哈希作为 side information

本附录证明：当宇宙比集合渐近更大时，公开 IID hash 只能减少 \(o(n)\) bit 的 occupancy entropy。

### A.1 条件分布与精确互信息恒等式

令 \(|U|=m\)，\(S\) 是 \(U\) 的均匀 \(n\)-子集，\(h:U\to[q]\) 在各键上 IID，categorical law 为 \(p=(p_1,\ldots,p_q)\)。定义

\[
N_j=|S\cap h^{-1}(j)|,
\qquad
C_j=|h^{-1}(j)|.
\]

边缘上 \(N\sim\operatorname{Mult}(n,p)\)。给定 \(h\) 后，

\[
\Pr[N=a\mid h]
=\Pr[N=a\mid C]
=\frac{\prod_j\binom{C_j}{a_j}}{\binom mn},
\]

因此 \(C\) 是关于 \(N\) 的充分统计量。

> **引理 A.1** 设 \(M_k\sim\operatorname{Mult}(k,p)\)，则
> \[
> I(N;h)=I(N;C)=H(M_m)-H(M_{m-n}).
> \tag{A.1}
> \]
> 若 \(\widehat p_k=M_k/k\)，则以 nat 为单位，
> \[
> I(N;h)
> =\sum_{k=m-n+1}^{m}
> \mathbb E D(\widehat p_k\Vert p).
> \tag{A.2}
> \]

**证明。** 将被抽中的键与未抽中的键随机排序并暴露其 labels。于是

\[
C=N+R,
\qquad
N\sim\operatorname{Mult}(n,p),
\quad
R\sim\operatorname{Mult}(m-n,p),
\]

且 \(N,R\) 独立。因此

\[
I(N;C)=H(C)-H(C\mid N)=H(M_m)-H(M_{m-n}).
\]

再把 \(M_k\) 耦合为 IID labels \(X_1,\ldots,X_k\) 的 type。映射

\[
(M_{k-1},X_k)\longleftrightarrow(M_k,X_k)
\]

是双射，而 \(X_k\) 与 \(M_{k-1}\) 独立。由交换性，

\[
\Pr[X_k=j\mid M_k]=\frac{M_{k,j}}k=\widehat p_{k,j}.
\]

故

\[
\begin{aligned}
H(M_k)-H(M_{k-1})
&=H(p)-H(X_k\mid M_k)\\
&=H(p)-\mathbb EH(\widehat p_k)\\
&=\mathbb ED(\widehat p_k\Vert p).
\end{aligned}
\]

从 \(m-n+1\) 到 \(m\) 求和即得式 (A.2)。

> **推论 A.2** 若正概率 categories 的数量为 \(q\)，则
> \[
> I_2(N;h)
> \le\frac{q-1}{\ln2}
> \sum_{k=m-n+1}^{m}\frac1k.
> \tag{A.3}
> \]

**证明。** 由 \(\ln x\le x-1\)，

\[
\begin{aligned}
\mathbb ED(\widehat p_k\Vert p)
&\le
\sum_j\frac{\mathbb E\widehat p_{k,j}^2}{p_j}-1\\
&=\frac{q-1}{k}.
\end{aligned}
\]

代入式 (A.2) 并由 nat 换算成 bit。若 \(q=O(n)\)、\(m/n\to\infty\)，右侧为 \(o(n)\)。该界不要求各 \(p_j\) 都是 \(\Theta(1/n)\)，因此也允许一个 top category 和有限 heavy cells。

### A.2 Fano converse

> **引理 A.3** 假设一个 \(B\)-bit 固定内存的 normal state 可以恢复全部 tracked multiplicities，且对每个固定构造历史失败概率为 \(\delta_n=o(1)\)。若 \(q=O(n)\)、\(|U|/n\to\infty\)，则
> \[
> B\ge H(\operatorname{Mult}(n,p))-o(n).
> \tag{A.4}
> \]

**证明。** 固定一个查询键 \(x\)，从 \(U\setminus\{x\}\) 中均匀选择 \(n\)-子集 \(S\)，并按固定 canonical order 插入。对每个 \(S\)，该历史独立于公开随机带，因此平均后的 joint decoding error 仍至多为 \(\delta_n\)。

记 \(M\) 为内存状态，\(R\) 为全部公开随机性。tracked vector 与单一 top count 之间满足

\[
N_{\mathsf{top}}=n-\sum_{j=1}^{q}N_j,
\]

所以恢复 tracked vector 等价于恢复 full occupancy vector。其支持大小至多

\[
\binom{n+q}{q}=2^{O(n)}.
\]

Fano 不等式给出

\[
H(N\mid M,R)
\le h_2(\delta_n)
+\delta_n\log_2\binom{n+q}{q}
=o(n).
\]

除 \(h\) 外的公开 coins 与 \((S,h)\) 独立，因此

\[
H(N\mid R)=H(N\mid h)=H(N)-o(n),
\]

最后一个等号来自推论 A.2。于是

\[
\begin{aligned}
H(N)-o(n)
&=H(N\mid R)\\
&\le I(N;M\mid R)+H(N\mid M,R)\\
&\le H(M)+o(n)\\
&\le B+o(n).
\end{aligned}
\]

移项即得结论。

## 附录 B：异质 multinomial occupancy entropy

本附录补全正文式 (4.1)，并避免把“Poissonization/de-Poissonization”当作未经证明的黑箱。

### B.1 一个直接的 Poissonization 恒等式

设 \(p=(p_1,\ldots,p_q)\)，令 \(Z_j\sim\operatorname{Pois}(np_j)\) 相互独立，并令

\[
T=\sum_jZ_j\sim\operatorname{Pois}(n).
\]

条件于 \(T=t\)，向量 \(Z\) 服从 \(\operatorname{Mult}(t,p)\)。记

\[
h_t=H(\operatorname{Mult}(t,p)).
\]

由 entropy chain rule，

\[
\sum_jH(Z_j)=H(T)+\mathbb Eh_T.
\tag{B.1}
\]

> **引理 B.1** 若 categories 数 \(q=n^{O(1)}\)，则
> \[
> H(\operatorname{Mult}(n,p))
> =\sum_jH(\operatorname{Pois}(np_j))+o(n),
> \tag{B.2}
> \]
> 且误差可统一取为 \(O(\sqrt n\log n)\)。

**证明。** 令 \(X_t\sim\operatorname{Mult}(t,p)\)，再独立取 \(Y\sim p\) 的一个 categorical unit vector。则 \(X_t+Y\sim\operatorname{Mult}(t+1,p)\)。一方面，条件于 \(Y\) 时平移不改变 entropy，故

\[
h_{t+1}=H(X_t+Y)\ge H(X_t+Y\mid Y)=h_t.
\]

另一方面，\(X_t+Y\) 是 \((X_t,Y)\) 的函数，故

\[
h_{t+1}\le H(X_t,Y)=h_t+H(p)\le h_t+\log_2q.
\]

因此

\[
|h_t-h_n|\le|t-n|\log_2q.
\]

由于 \(T\sim\operatorname{Pois}(n)\)，

\[
\mathbb E|T-n|\le\sqrt{\operatorname{Var}T}=\sqrt n.
\]

又 \(H(T)=O(\log n)\)，式 (B.1) 给出

\[
\begin{aligned}
\left|h_n-\sum_jH(Z_j)\right|
&\le H(T)+\mathbb E|h_T-h_n|\\
&\le O(\log n)+\sqrt n\log_2q\\
&=O(\sqrt n\log n)=o(n).
\end{aligned}
\]

证毕。

该引理比本文实际所需更一般：它不要求 \(p_j=\Theta(1/n)\)，只要求 categories 数为多项式量级。

### B.2 size-biased load law 与 heavy categories

令轻单元集合 \(L_n\) 满足式 (2.1)，并定义 \(\lambda_j=np_j\)。则

\[
\frac1n\sum_{j\in L_n}
H(\operatorname{Pois}(\lambda_j))
=\sum_{j\in L_n}p_jr(\lambda_j).
\tag{B.3}
\]

有限个 heavy categories 的每个 Poisson entropy 为 \(O(\log n)\)，总贡献为 \(o(n)\)。因此将它们连同 top mass 放在 \(\lambda=\infty\)，由 \(r(\infty)=0\)，引理 B.1 化为

\[
\frac1nH(\operatorname{Mult}(n,p))
=\int r(\lambda)\,d\nu_n(\lambda)+o(1).
\tag{B.4}
\]

对于一个固定非成员 \(x\)，\(h(x)\) 与集合中 \(n\) 个键的 labels 独立，因此 fingerprint core 的碰撞概率精确为

\[
p_{\mathsf{top}}
+\sum_{j\in L_n}p_j[1-(1-p_j)^n]
+\sum_{j\in H_n}p_j[1-(1-p_j)^n].
\tag{B.5}
\]

在 \(\lambda_j\in[a,A]\) 上，

\[
1-\left(1-\frac{\lambda_j}{n}\right)^n
=1-e^{-\lambda_j}+O(1/n)
\]

一致成立。有限 diverging-load categories 的非空概率趋于一。因此

\[
\Pr[\text{fingerprint collision}]
=\int g(\lambda)\,d\nu_n(\lambda)+o(1).
\tag{B.6}
\]

sticky failure 只会把更多查询变成 `YES`，所以在下界方向上，advertised FPR 不小于式 (B.5)。若 advertised pointwise FPR 至多为 \(\varepsilon\)，便得到

\[
\int g\,d\nu_n\le\varepsilon+o(1).
\]

结合引理 A.3 与式 (B.4)，定理 3.1 得证。

## 附录 C：变分原理与可实现的负载分布

定义

\[
\Gamma=\{(g(\lambda),r(\lambda)):0<\lambda\le\infty\}.
\]

对于任意概率测度 \(\nu\)，\((\int g\,d\nu,\int r\,d\nu)\) 位于 \(\overline{\operatorname{conv}}(\Gamma)\)。反过来，若

\[
\sum_{i=1}^k\alpha_i=1,
\qquad \alpha_i\ge0,
\]

则对每个有限 \(\lambda_i\)，取

\[
q_i=\left\lfloor\frac{\alpha_i n}{\lambda_i}\right\rfloor
\]

个概率接近 \(\lambda_i/n\) 的单元；剩余 \(o(1)\) 质量并入 top 或通过 vanishing parameter perturbation 吸收。这样便渐近实现对应的有限凸组合。故

\[
R_{\mathrm{FM}}(\varepsilon)
=\inf\left\{
\sum_i\alpha_ir(\lambda_i):
\sum_i\alpha_ig(\lambda_i)\le\varepsilon
\right\}.
\tag{C.1}
\]

由于端点 \((1,0)\) 存在，增加 top mass 可以提高 error 并降低 rate，最优边界满足等号。式 (C.1) 因而就是 \(\Gamma\) 的闭下凸包在横坐标 \(\varepsilon\) 处的值。

## 附录 D：Poisson 曲线相变的完整证明

为便于微分，本附录暂时使用 natural-log entropy；最后除以 \(\ln2\) 转换成 bit。令 \(X\sim\operatorname{Pois}(\lambda)\)，并写

\[
H=H(X),
\qquad
r=H/\lambda,
\qquad
g=1-e^{-\lambda},
\qquad
F=e^\lambda r.
\]

再令

\[
A(\lambda)=\mathbb E\ln(X!).
\]

由 Poisson differentiation，

\[
H=\lambda(1-\ln\lambda)+A,
\]

\[
A'=\mathbb E\ln(X+1),
\qquad
A''=\mathbb E\ln\frac{X+2}{X+1}.
\tag{D.1}
\]

以下初等界直接来自保留事件 \(X=0,1\)、Jensen 不等式及 \(\ln(1+t)\le t\)：

\[
0\le A,
\qquad
e^{-\lambda}\ln2\le A''\le\frac{1-e^{-\lambda}}\lambda,
\tag{D.2}
\]

\[
e^{-\lambda}\lambda\ln2\le A'\le\ln(1+\lambda).
\tag{D.3}
\]

### D.1 \(F\) 在小负载区间的严格凸性

直接微分得

\[
D(\lambda):=\lambda^3e^{-\lambda}F''(\lambda)
=\lambda^2H''+2\lambda(\lambda-1)H'
+(\lambda^2-2\lambda+2)H.
\tag{D.4}
\]

当 \(0<\lambda\le1\) 时，在式 (D.4) 中使用 \(A\ge0\)、式 (D.2) 的下界，以及式 (D.3) 的上界——此处 \(A'\) 的系数非正——可得

\[
D(\lambda)
\ge\lambda\{q(\lambda)-\lambda^2\ln\lambda\},
\tag{D.5}
\]

其中

\[
q(x)=(1-x)^2+xe^{-x}\ln2-2(1-x)\ln(1+x).
\]

因为 \(-x^2\ln x\ge0\)，只需证明 \(q(x)>0\)。在 \([0,1]\) 上使用

\[
\ln2\ge\frac{69}{100},
\]

\[
e^{-x}\ge1-x+\frac{x^2}{2}-\frac{x^3}{6}
+\frac{x^4}{24}-\frac{x^5}{120},
\]

\[
\ln(1+x)\le x-\frac{x^2}{2}+\frac{x^3}{3}
-\frac{x^4}{4}+\frac{x^5}{5},
\]

得到 \(q(x)\ge P(x)\)，其中

\[
P(x)=1-\frac{331}{100}x+\frac{331}{100}x^2
-\frac{793}{600}x^3+\frac{631}{600}x^4
-\frac{697}{800}x^5+\frac{1577}{4000}x^6.
\tag{D.6}
\]

把 \([0,1]\) 分成

\[
[0,1/2],\ [1/2,5/8],\ [5/8,21/32],
\ [21/32,11/16],\ [11/16,3/4],\ [3/4,1].
\]

将 \(P\) 在每个区间仿射变换到 \([0,1]\) 并转为 Bernstein basis，所有系数均为正；每段最小系数依次为

\[
\frac{39901}{768000},\quad
\frac{101841}{41943040},\quad
\frac{1190903857}{4294967296000},
\]

\[
\frac{1640463541}{6442450944000},\quad
\frac{433094371}{201326592000},\quad
\frac{294373}{16384000}.
\]

因此 \(P>0\)，从而

\[
F''(\lambda)>0,
\qquad0<\lambda\le1.
\tag{D.7}
\]

### D.2 驻点的全局唯一性

\(F'\) 的符号等于

\[
S(\lambda)=\lambda H'(\lambda)+(\lambda-1)H(\lambda).
\tag{D.8}
\]

附录 I 所述的 exact-rational verifier 使用 \(e^{-\lambda}\)、\(\ln\lambda\) 的有理 Taylor 上下界及 Poisson 尾的几何上界，证明

\[
S(0.4399316012447)<0,
\qquad
S(0.4399316012449)>0.
\tag{D.9}
\]

由式 (D.7)，\(F'\) 在 \((0,1]\) 严格递增，因此该根在此区间唯一。

对于 \(\lambda>1\)，Poisson entropy 单调不减。事实上，若 \(\mu>\lambda\)，可写

\[
X_\mu=X_\lambda+Y,
\qquad
Y\sim\operatorname{Pois}(\mu-\lambda)
\]

且二者独立，于是

\[
H(X_\mu)
\ge H(X_\mu\mid Y)
=H(X_\lambda).
\]

故 \(H'(\lambda)\ge0\)。当 \(\lambda>1\) 时，式 (D.8) 的第二项严格为正，第一项非负，因此 \(S(\lambda)>0\)。所以式 (D.9) 中的根是整个正半轴上的唯一驻点，也是 \(F\) 的唯一全局最小点。

### D.3 原曲线在切点之前严格凸

因为 \(g'(\lambda)=e^{-\lambda}>0\)，\(r\) 关于 \(g\) 的二阶导数符号与 \(r''+r'\) 相同。令

\[
C(\lambda)=\lambda^3(r''+r')
=\lambda^2H''+(\lambda^2-2\lambda)H'
+(2-\lambda)H.
\tag{D.10}
\]

当 \(0<\lambda\le11/25\) 时，使用式 (D.2)–(D.3) 以及 \(-\ln\lambda\ge1-\lambda\)，得到

\[
C(\lambda)\ge\lambda R(\lambda),
\]

\[
R(x)=1-\frac{331}{100}x+\frac{431}{100}x^2
-\frac83x^3+\frac23x^4.
\tag{D.11}
\]

\(R\) 在 \([0,11/25]\) 上的 Bernstein coefficients 为

\[
1,\quad
\frac{6359}{10000},\quad
\frac{38519}{93750},\quad
\frac{201089}{750000},\quad
\frac{412139}{2343750},
\]

全部为正。又由式 (D.9)，\(\lambda_*<11/25\)，故原曲线在整个低误差分支上严格凸。

最后，从 \((g(\lambda),r(\lambda))\) 到 \((1,0)\) 的割线斜率由 \(F(\lambda)\) 决定，而 \(F(\lambda)\ge F(\lambda_*)\) 对所有 \(\lambda>0\) 成立。因此 \(\lambda_*\) 处切线延伸到 \((1,0)\) 后是全局 supporting line。下凸包先沿原曲线到 \(\lambda_*\)，再沿该直线到 \((1,0)\)，这证明式 (1.5)。

## 附录 E：参数离散化与两层有限独立哈希

本附录开始证明定理 3.3。固定优化器参数 \(\alpha,\lambda\)，并取

\[
b=2^{\lceil2\log_2\log_2n\rceil}.
\]

令 \(Q=2^w=n^{\Theta(1)}\)，并将键嵌入 \(\mathbb F=\operatorname{GF}(Q)\)。取

\[
B=\operatorname{round}\!\left(\frac{\alpha n}{\lambda b}\right),
\qquad
m=\left\lfloor\frac{\alpha Q}{B}\right\rfloor,
\qquad
\delta=\frac mQ.
\tag{E.1}
\]

则 \(Bm\le Q\)，并且通过把 \(Q\) 取为足够高次的 \(n\) 的幂，可以保证

\[
B\delta=\alpha+o(1),
\qquad
\lambda_n=\frac{n\delta}{b}=\lambda+o(1),
Bb=\frac{\alpha n}{\lambda}+o(n).
\tag{E.2}
\]

选择随机多项式 \(G:\mathbb F\to\mathbb F\)，次数小于 \(k_{\mathrm{out}}\)。将 \(Bm\) 个域元素分成 \(B\) 个等长区间，每段大小为 \(m\)；\(G(x)\) 落入某段时得到对应 light block，其余为 top。于是每个 block 概率精确为 \(\delta\)。

独立选择次数小于 \(k_{\mathrm{in}}\) 的随机多项式 \(H\)，再通过一个满射线性投影把 \(H(x)\) 映到 \(\log_2b\) bit，得到 block 内坐标。分别取

\[
k_{\mathrm{out}}=2\lceil\gamma\log n\rceil,
\]

\[
k_{\mathrm{in}}=s_{\max}
=\left\lceil\lambda_nb+A\sqrt{b\log n}\right\rceil.
\tag{E.3}
\]

两个种子共占

\[
O((k_{\mathrm{out}}+k_{\mathrm{in}})\log Q)
=O(\log^3n)
\]

bit。Horner evaluation 在 word RAM 上使用 \(\log^{O(1)}n\) 次操作。

## 附录 F：outer load 与 block 内精确 multinomial law

> **引理 F.1（有限独立 Bernoulli 高阶矩）** 存在绝对常数 \(C\)，使得若 \(X_1,\ldots,X_t\) 是 \(2r\)-wise independent Bernoulli variables，\(S=\sum_iX_i\)、\(\mu=\mathbb ES\)，则
> \[
> \mathbb E|S-\mu|^{2r}
> \le[C(r\mu+r^2)]^r.
> \tag{F.1}
> \]

**证明。** 展开 centered \(2r\)-th moment。每个 monomial 至多涉及 \(2r\) 个 coordinates，因此其期望与完全独立情形相同。对完全独立 Bernoulli sum 使用 Bernstein tail

\[
\Pr[|S-\mu|\ge t]
\le2\exp\left(-\frac{t^2}{2(\mu+t/3)}\right),
\]

并通过

\[
\mathbb E|S-\mu|^{2r}
=\int_0^\infty 2r\,t^{2r-1}
\Pr[|S-\mu|\ge t]\,dt
\]

在 \(t=\mu\) 处分段积分，可得式 (F.1)，其中常数吸收 Gamma-function bounds。

由 Markov 不等式，

\[
\Pr[|S-\mu|\ge t]
\le\left(\frac{C(r\mu+r^2)}{t^2}\right)^r.
\tag{F.2}
\]

在固定 endpoint，某个 outer block 的负载 \(S_j\) 是均值至多 \(\lambda_nb\) 的有限独立 Bernoulli sum。令 \(r=\lceil\gamma\log n\rceil\)、\(t=A\sqrt{b\log n}\)。因 \(b=\Theta(\log^2n)\)，先固定 \(\gamma\)，再取足够大的 \(A\)，式 (F.2) 给出

\[
\Pr[S_j>s_{\max}]\le n^{-K}
\tag{F.3}
\]

对任意预先指定常数 \(K\) 成立。

现在固定 endpoint set，并条件于所有键的完整 outer assignment。对 block \(j\)，令

\[
A_j=\{x:g(x)=j\},
\qquad s=|A_j|.
\]

inner seed 与 outer assignment 独立。如果 \(s\le s_{\max}=k_{\mathrm{in}}\)，则 \(H\) 在这些不同键上的值是独立均匀域元素，投影后仍为 \([b]\) 上的 IID uniforms。因此

\[
C_j\mid(g(x):x\in S)
\sim\operatorname{Mult}(s;1/b,\ldots,1/b).
\tag{F.4}
\]

这就是 block coder 所使用的精确条件分布。

## 附录 G：固定槽整数区间码

### G.1 编码正确性

给定 block total \(s\)，每个 histogram \(c=(c_1,\ldots,c_b)\) 对应

\[
M_s(c)=\frac{s!}{\prod_ic_i!}
\]

个字符串。按 histogram 的 lexicographic order 排列全部 \(b^s\) 个字符串，并令 \(R_s(c)\) 为 \(c\) 之前的字符串数。若

\[
M_s(c)2^L\ge4b^s,
\tag{G.1}
\]

则

\[
z(c)=\left\lfloor\frac{2^LR_s(c)}{b^s}\right\rfloor+1
\]

满足

\[
\frac{R_s(c)}{b^s}
<\frac{z(c)}{2^L}
<\frac{R_s(c)+M_s(c)}{b^s}.
\tag{G.2}
\]

左侧来自 floor 后加一；右侧使用式 (G.1) 留出的两个 guard bits。不同 histogram 的 interval interiors 不交，因此 \((s,z)\) 唯一确定 \(c\)。\(s=0\) 时 histogram 确定，单独编码。

### G.2 exact rank/unrank

固定前缀 \(c_1,\ldots,c_{i-1}\)，设剩余 \(t\) 个 balls 和 \(m=b-i+1\) 个 coordinates。对候选下一计数 \(a\)，所有此前前缀相同且 \(c_i=a\) 的 histogram groups 的字符串总数为

\[
W_i(a)
=
\frac{s!}{\bigl(\prod_{\ell<i}c_\ell!\bigr)t!}
\binom ta(m-1)^{t-a}.
\tag{G.3}
\]

这是因为先在剩余 \(t\) 个 labeled positions 中选择 \(a\) 个送入坐标 \(i\)，其余各自选择 \(m-1\) 个后续 coordinates，再乘上已固定前缀对应的 multinomial factor。对 \(a<c_i\) 累加式 (G.3)，再逐坐标进行，得到 \(R_s(c)\)。

unrank 反向执行：对每个坐标按 \(a=0,1,\ldots,t\) 扫描 \(W_i(a)\)，比较给定 dyadic point 与累计 integer boundaries，确定唯一的 \(a\)，随后进入下一坐标。比较可交叉乘为 \(z b^s\) 与 \(2^L R\) 的整数比较。

所有整数至多有 \(O(s\log b)\) bit。算法进行 \(O(bs)\) 次加、乘、除和比较；当 \(b,s=O(\log^2n)\) 时，即使采用 schoolbook multiword arithmetic，也只需 \(\log^{O(1)}n\) 个 word operations 和 \(O(b\log b)\) bit scratch space。

### G.3 槽长与 codeability tail

定义

\[
I_s(c)=-\log_2P_s(c)
=s\log_2b-\log_2(s!)+\sum_i\log_2(c_i!).
\]

改变一个 inner label 时两个 counts 各改变一，因此

\[
|\Delta I_s|\le\log_2(s+1).
\]

McDiarmid 不等式给出

\[
\Pr[I_s(C)-H(C\mid S=s)>u]
\le
\exp\left(-\frac{2u^2}{s\log_2^2(s+1)}\right).
\tag{G.4}
\]

此外，若 \(Z\sim\operatorname{Bin}(s,1/b)\)，则

\[
H(C\mid S=s)
=s\log_2b-\log_2(s!)+b\,\mathbb E\log_2(Z!).
\]

\(k\mapsto\log(k!)\) 为凸函数，而

\[
\operatorname{Bin}(s,1/b)
\le_{\mathrm{cx}}
\operatorname{Pois}(s/b).
\]

再由 \(s!\ge(s/e)^s\)，得到

\[
H(C\mid S=s)
\le bH(\operatorname{Pois}(s/b)).
\tag{G.5}
\]

Poisson entropy 随均值单调不减，并在固定紧区间上 Lipschitz。对 \(s\le s_{\max}\)，

\[
H(C\mid S=s)
\le bH(\operatorname{Pois}(\lambda_n))
+O(\sqrt{b\log n}).
\]

结合式 (G.4)，取

\[
L=\left\lceil
bH(\operatorname{Pois}(\lambda_n))
+D\sqrt{b\log n}\log b
\right\rceil+2
\tag{G.6}
\]

并令 \(D\) 足够大，可使每个正常 block 在固定 endpoint 不可编码的概率至多 \(n^{-K}\)。

## 附录 H：全局空间、时间与 overflow

每个 block 保存一个 \(L\)-bit slot 和一个可表示 \(0,\ldots,s_{\max}\) 的 total。全局另保存 sticky bit、两个哈希种子，以及一个 \(O(b\log b)\)-bit reusable scratch area。若 slots word-aligned，每个 block 额外浪费 \(O(\log n)\) bit。

由 \(B=\Theta(n/b)\) 与式 (G.6)，总空间为

\[
\begin{aligned}
&BbH(\operatorname{Pois}(\lambda_n))\\
&\quad+O\left(
n\sqrt{\frac{\log n}{b}}\log b
+\frac{n\log b}{b}
+\frac{n\log n}{b}
+b\log b
+\log^3n
\right).
\end{aligned}
\tag{H.1}
\]

因为 \(b=\Theta(\log^2n)\)，括号中各项均为 \(o(n)\)。由式 (E.2)，首项为

\[
\alpha n
\frac{H(\operatorname{Pois}(\lambda))}{\lambda}
+o(n).
\tag{H.2}
\]

一次更新计算 outer/inner labels，解码一个 block，修改一个 count 和 total，测试式 (G.1)，再重新编码。旧 slot 只在新 code 通过后覆盖；因此一次失败不会破坏进入 sticky state 之前的唯一副本。查询可在 unrank 时走到目标坐标，最坏为整个 block。有限域求值和 multiword arithmetic 均为 polylog，因此所有操作为 \(\log^{O(1)}n\) worst case。

固定历史有 \(T+1\le n^c+1\) 个 endpoints 和 \(B=O(n/b)\) 个 blocks。选 \(K>c+d+2\)。由式 (F.3) 和附录 G 的 codeability tail，一个 block-endpoint pair 为 bad 的概率至多 \(2n^{-K}\)。无需独立性，union bound 给出

\[
\Pr[\exists\text{ bad block-time pair}]
\le2B(T+1)n^{-K}
\le n^{-d}
\]

对充分大的 \(n\) 成立。

## 附录 I：pointwise FPR 与可复现证书

### I.1 有限独立下的 FPR

固定 endpoint set \(S\)，\(|S|=k\le n\)，再固定 \(x\notin S\)。条件于 \(x\) 落入一个指定 light cell，令 \(E_i\) 表示第 \(i\) 个成员也落入该 cell。若

\[
r+1\le\min(k_{\mathrm{out}},k_{\mathrm{in}}),
\]

则任意 \(r\) 个事件同时发生的概率精确为 \(p^r\)，其中 \(p=\delta/b\)。取低于独立度的奇数 \(R\)，Bonferroni 不等式给出

\[
\Pr\left[\bigcup_iE_i\right]
\le\sum_{r=1}^{R}(-1)^{r+1}\binom krp^r.
\tag{I.1}
\]

当 \(R+1>kp\) 时，后续 binomial terms 绝对值递减，故式 (I.1) 至多为

\[
1-(1-p)^k
+\binom{k}{R+1}p^{R+1}
\le
1-(1-p)^k
+\left(\frac{e\lambda_n}{R+1}\right)^{R+1}.
\tag{I.2}
\]

取

\[
R=\Theta\left(\frac{(c+d+1)\log n}{\log\log n}\right)
\]

为奇数。式 (I.2) 的余项为 \(n^{-\Omega(c+d+1)}\)，且 \(R+1\) 小于两层哈希的独立度。平均所有 light cells 后，overflow 之前的 pointwise FPR 至多为

\[
\beta_n+(1-\beta_n)[1-(1-p)^k]
+n^{-\Omega(c+d+1)}.
\tag{I.3}
\]

再加 history-wide overflow probability，并用 \(\eta_n=1/\log n\) 的参数 margin 吸收式 (E.2) 的 grid rounding、式 (I.3) 的有限独立余项及 overflow，最终 FPR 不超过 \(\varepsilon\)。

### I.2 计算机辅助但可精确复现的部分

下列脚本均位于本文同一研究目录：

- `scripts/verify_public_hash_entropy.py`：穷举有限实例，验证式 (A.1)；
- `scripts/verify_fixed_slot_integer_code.py`：穷举小 \(b,s\)，验证 dyadic interval code 的唯一性；
- `scripts/verify_poisson_phase_analytic.py`：使用 `fractions.Fraction` 验证附录 D 中 Bernstein coefficients 的严格正性；
- `scripts/verify_poisson_root_certificate.py`：使用有理 Taylor remainder 和 Poisson 几何尾界验证式 (D.9) 及 \(\varepsilon_*,C_*\) 的严格区间；
- `scripts/verify_poisson_phase_transition.py`：仅作 floating-point regression，不承担逻辑证明。

统一运行命令为：

```bash
./run_theorem_verifiers.sh
```

有理证书只依赖 Python 整数与 `fractions.Fraction` 运算；浮点网格只用于回归检查，不用于证明 positivity 或根的包围。

## 参考文献说明

本稿引用的核心方向包括 Carter 等人的经典 approximate membership 下界与 fingerprint reduction、Pagh–Pagh–Rao 的动态 fingerprint multiset、Bercea–Even 的动态 filter 与 multiset dictionary、Weighted Bloom Filters、Daisy Bloom Filters、ChainedFilter、adaptive/broom filters、dynamic retrieval，以及 Kuszmaul–Liang–Zhou 的《Fingerprint Filters Are Optimal》。正式投稿前应以最终 BibTeX 再次核对作者顺序、会议版本、年份与页码；本文不在尚未核验时伪造完整书目信息。
