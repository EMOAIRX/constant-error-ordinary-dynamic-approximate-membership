# 跨块负载共享的动态近似成员过滤器

> 论文结构草稿。本文的无条件贡献是一个 ordinary、one-sided、fixed-state
> 动态近似成员过滤器上界，以及一个自然 two-subblock order-3 子族内的 sharp
> converse。本文不声称解决任意动态过滤器在常数错误率下的最优空间，也不声称
> 在全部 canonical lattices 中最优。

## 1. Introduction

近似成员查询结构通常位于昂贵存储或网络访问之前：一次否定回答可以直接跳过后端
查找，而一次假阳性只会产生额外访问，不会破坏正确性。静态 Bloom filter 及其
后继结构已经形成成熟的理论与工程体系；在缓存目录、持续更新的去重集合和可变索引
中，过滤器还必须在固定容量内支持插入与删除。本文研究这种 one-sided dynamic
approximate membership 的一个基础问题：当假阳性率是固定常数时，一个能够经历
任意长合法更新历史的自包含过滤器，究竟需要多少固定内存？

低错误率区间的主导空间是

\[
n\log_2(1/\varepsilon).
\]

Kuszmaul、Liang 与 Zhou 在 FOCS 2025 的《Fingerprint Filters Are Optimal》中
证明，当 \(\varepsilon=o(1)\) 且宇宙足够大时，任意动态过滤器还必须支付
\(n\log_2 e-o(n)\) 的线性冗余。他们同时明确留下常数错误率
\(\varepsilon^{-1}=\Theta(1)\) 的紧界问题。在这个区间，所有被低阶项隐藏的线性
常数都会成为主项；现有证明不能通过更精细的 bookkeeping 直接延伸。

一种自然方法是把每个键映射为短 fingerprint，并维护 fingerprint multiset。
如果只关心某个随机快照的源熵，这个对象可以被高度压缩；但 ordinary fixed-state
模型要求一个预先分配的 \(H\)-bit codebook 覆盖所有容量不超过 \(n\) 的合法状态，
并允许删除把高负载状态重新带回低负载状态。直接精确保存所有 fingerprint
multiplicities 因而较昂贵。另一方面，如果在高负载时简单丢弃信息，删除后通常无法
恢复低负载下的辨识能力。

本文提出一种不同的机制：不分别保存若干子块的精确负载，而只保存总负载，并用一个
有限指数 allocation lattice 记录子块之间的负载分配。这个摘要在高负载时允许跨子块
合并状态，在删除后又能通过可逆的群更新自动恢复低负载信息。关键点不是使用更大的
alphabet，而是让两个局部过滤器共享原本重复保存的 load-allocation information。

具体地，每个宏块使用四个等概率 symbols
\(A_0,A_1,B_0,B_1\)。若其 composition 为

\[
(a_0,a_1,b_0,b_1),\qquad c=a_0+a_1+b_0+b_1,
\]

则只保存

\[
\boxed{
\left(c,(a_0+a_1)\bmod 6,a_1\bmod3,b_1\bmod3\right).
}
\tag{1.1}
\]

这等价于在

\[
G=\mathbb Z_6\times\mathbb Z_3\times\mathbb Z_3
\]

中维护 additive syndrome。插入和删除只需加减相应 increment；查询采用由
one-sidedness 强迫的 minimal support-union rule。该结构没有 overflow、rebuild、
sticky failure state 或外部 exact set，并支持任意长合法更新历史。

### 1.1 Main results

本文的第一个结果是一个严格的新 fixed-state upper bound。

> **定理 1.1（cross-block upper bound，简化表述）。** 令
> \(\varepsilon=1/2\)。存在 ordinary one-sided dynamic approximate membership
> filter，使其对每条预先固定、与公共随机带独立的有限合法历史和每个固定当前
> nonmember 满足假阳性率至多 \(1/2\)，并使用
> \[
> H\le 2.34614905664\,n+o(n)
> \]
> bits 的固定最坏情形内存。该结构逐随机带没有假阴性，支持任意长合法插入与删除，
> 且不发生 overflow 或 failure。

此前的 binary order-3 threshold quotient 给出

\[
2.349083440193\ldots n+o(n)
\]

bits。新构造将其严格改进约

\[
0.00293438539\,n
\]

bits。这个数值改进较小，但它否定了“独立 binary product 已经是 designed additive
quotient 的自然终点”：跨子块共享负载信息确实能够产生严格收益。

第二个结果说明 modulus 6 不是一次偶然的参数搜索。考虑整个 two-subblock
order-3 allocation-modulus family

\[
\left(c,(a_0+a_1)\bmod Q,a_1\bmod3,b_1\bmod3\right),
\qquad Q\in\mathbb Z_{\ge1}.
\tag{1.2}
\]

> **定理 1.2（子族内 sharp converse）。** 在式 (1.2) 的全部整数
> \(Q\ge1\) 中，\(Q=6\) 是 \(\varepsilon=1/2\) fixed-state asymptotic rate
> 的唯一最小点。

证明分为解析尾部与有限认证两部分。对于 \(Q\ge9\)，前 \(Q\) 个 load layers
尚未发生 allocation wrap-around；由这些被强迫的 state counts、单调 frozen tail
以及 independent-subblock rejection 上界即可统一排除全部无限尾部。剩余
\(Q=1,\ldots,8\) 的 reachable-state 与 rejection profiles 均为精确有理数，
再用有理区间证书比较 Poisson calibration root 与 enumerative saddle。最接近的
竞争者是 \(Q=5\)，其 rate 为

\[
2.346464991509\ldots,
\]

仍严格高于 \(Q=6\)。

### 1.2 Why cross-block sharing works

独立保存两个 binary order-3 子块时，状态包含

\[
(a,a_1\bmod3;b,b_1\bmod3),
\qquad a+b=c.
\]

式 (1.1) 只保存总负载 \(c\)、一个 allocation residue \(a\bmod6\)，以及两个
one-count residues。因此它允许

\[
(a,u,b,v)\sim(a+6,u,b-6,v),
\tag{1.3}
\]

在保持总负载不变时跨子块合并状态。模数过小会过早混合两个子块的 supports，导致
拒绝能力迅速消失；模数过大则接近分别保存两个 exact loads，无法获得足够的状态
共享。\(Q=6\) 位于这两个极端之间，并在定理 1.2 的整个自然子族中达到唯一最优。

### 1.3 Technical overview

固定 load \(c\) 时，可达 syndrome 恰为

\[
\{(a\bmod6,u\bmod3,v\bmod3):
0\le a\le c,\ 0\le u\le a,\ 0\le v\le c-a\}.
\]

由此得到精确 state profile

\[
(d_c)_{c\ge0}
=(1,4,10,18,27,36,44,50,53,54,54,\ldots)
\]

和生成函数

\[
A(z)=\frac{1+3z+6z^2+8z^3+9z^4+9z^5+8z^6+6z^7+3z^8+z^9}{1-z}.
\]

对每个 syndrome fiber，minimal one-sided query 接受该 fiber 中所有
compositions 的 support union。按 multinomial weight 求和得到

\[
(\rho_0,\ldots,\rho_9)
=\left(1,\frac34,\frac9{16},\frac{13}{32},\frac9{32},\frac3{16},
\frac{237}{2048},\frac{63}{1024},\frac{189}{8192},\frac{189}{32768}\right),
\]

且 \(\rho_c=0\) 对全部 \(c\ge10\) 成立。若 outer block load 的极限为
\(\operatorname{Pois}(\lambda)\)，则拒绝概率为

\[
J(\lambda)=e^{-\lambda}
\sum_{c=0}^{9}\frac{\lambda^c}{c!}\rho_c.
\]

方程 \(J(\lambda_*)=1/2\) 的唯一根满足

\[
\lambda_*\in[2.64801769,2.64801770].
\]

所有 block states 采用一个全局 fixed-length enumerative code，而不是分别按平均熵
编码。其一阶空间率为

\[
R=\min_{0<z<1}
\left\{\frac1{\lambda_*}\log_2 A(z)-\log_2z\right\}.
\]

有理区间计算认证主定理所需的固定测试点上界

\[
R<2.34614905664.
\]

数值优化给出 $R\approx2.346149054803345$；该小数用于定位，不作为 verifier 已认证的
两侧区间。旧稿中的 lower endpoint 来自固定 $z$ evaluation，不能下界 $\inf_z$，现已
删除。

有限 \(n\) 下，将 target load 向下偏移 \(n^{-1/4}\)，再用 Le Cam bound 控制
binomial-to-Poisson 误差，可以得到严格的 pointwise FPR。固定 codebook 枚举所有
总 load 不超过 \(n\) 的 abstract block tuples；有限宇宙中的不可达状态只会减少
实际状态数。

### 1.4 Scope and limitations

本文不证明 \(2.346149\ldots\) 是 ordinary dynamic approximate membership 的
最优常数。当前任意过滤器的常数错误率上下界之间仍有显著缺口。本文的 sharp
converse 只覆盖式 (1.2) 的 two-subblock order-3 allocation-modulus family；它不
覆盖任意内部 modulus、更多子块、一般 finite-Abelian increment sets、
history-dependent multiple representations 或 randomized state transitions。

此外，空间上界是 information-theoretic fixed-state 结果。它允许昂贵的全局
rank/unrank，不声称常数时间。FPR 的量词与标准 public-random fingerprint 模型
一致：历史和查询键在公共随机带之前固定；本文不提供对读取 hash seed 或根据先前
回答自适应选择更新的 adversary 的持续保证。

## 2. Related Work

### 2.1 Approximate membership and fingerprint filters

Carter 等人的经典工作建立了 approximate membership 的计数下界与 fingerprint
reduction。Pagh、Pagh 与 Rao 的 Bloom filter replacement 以及后续动态 multiset
dictionaries 表明，维护 fingerprint multiplicities 是支持删除的一条基本路线。
这些结果通常把空间写成
\(n\log_2(1/\varepsilon)+O(n)\)；当 \(\varepsilon\) 为常数时，隐藏在
\(O(n)\) 中的系数正是本文所研究的对象。

Bloomier filters、Xor filters、ribbon filters 和相关 retrieval structures 在静态
场景中提供了非常紧凑而高效的表示；cuckoo filters、quotient filters 及其变体提供
实用的动态更新。它们构成重要的算法基线，但并未给出 ordinary fixed-capacity
dynamic AMQ 在常数错误率下的精确 fixed-state 空间常数。

### 2.2 Dynamic lower bounds and the constant-error frontier

Pagh、Segev 与 Wieder 研究未知最终大小的 incremental filters，并揭示在线扩张
造成的额外空间。Kuszmaul 与 Walzer 证明动态 filters 相比静态 membership 具有
线性额外代价。Kuszmaul、Liang 与 Zhou 随后在 \(\varepsilon=o(1)\) 区间证明
fingerprint filters 在 \(o(n)\) 精度内最优，并明确提出
\(\varepsilon^{-1}=\Theta(1)\) 时的 tight upper and lower bounds 作为开放问题。

本文处理这个前沿中的一个构造问题：在最强的 fixed worst-case state guarantee 下，
可逆的 canonical quotient 能否通过跨块共享信息改进已有构造。我们的结果给出肯定
答案，但没有解决 arbitrary-filter matching lower bound。

### 2.3 Entropy-coded dynamic arrays

2026 年关于 dynamic entropy-encoded arrays 的工作实现了按随机 occupancy source
熵编码 fingerprint multiset，并支持常数时间操作；其空间与时间保证为相应论文中
的 high-probability resource semantics。本文研究不同的保证：一个预先分配的固定
codebook 必须覆盖全部容量不超过 \(n\) 的 abstract states，并支持任意长合法历史，
没有 overflow 或 failure event。因此两个结果的数值常数不能直接比较为同一模型下
的上下界。

### 2.4 Static chain rules and distribution-aware filters

ChainedFilter 用 chain rule 组合静态 membership filters，并刻画 finite-universe
及 distribution-aware 场景中的空间收益；其一般动态扩展并不保留同一无损 chain
rule。Weighted Bloom filters、Daisy Bloom filters 等工作也研究非均匀错误预算，
但通常使用外部给定的输入或查询分布。本文中的四个 symbols 对所有固定键保持相同
随机律；收益来自动态状态空间中的 load-allocation quotient，而不是已知键类别或
平均查询权重。

### 2.5 Algebraic and quotient-based filters

Quotient-style filters 广泛利用短 fingerprints、桶负载与局部余数支持更新。本文的
代数对象不同于哈希表中的 quotient/remainder decomposition：我们研究的是
composition lattice 上的可逆 right congruence。对于 canonical deterministic
key-only summaries，插入与合法删除的 cancellation 性质自然导出 Abelian lattice
quotient；state growth 与 one-sided rejection 因而分别由 sumsets 和 syndrome
fiber 的 support unions 控制。本文的 cross-block construction 是这一接口下第一个
严格优于独立 binary product 的例子。

## 3. Paper Organization

第 3 节形式化 ordinary fixed-state 模型与 canonical additive block products。
第 4 节给出 cross-block mod-6 构造及其任意历史更新语义。第 5 节推导精确 state
profile 与 rejection profile。第 6 节完成 Poisson calibration、有限 \(n\) 误差
控制和 fixed codebook 计数。第 7 节证明 two-subblock order-3 family 中
\(Q=6\) 的唯一最优性。附录给出所有有限 residue 表、有理区间证书、finite-\(n\)
校准细节以及可复算的 verifier 说明。

## 4. Suggested Theorem Boundary for the Abstract

摘要中可以安全写：

> We give an ordinary one-sided dynamic approximate-membership filter with
> fixed worst-case space \(2.34614905664n+o(n)\) bits at false-positive rate
> \(1/2\). The construction supports arbitrarily long legal update histories
> without overflow or failure. Its key mechanism is a cross-block allocation
> lattice that shares exact load information between two binary order-three
> subfilters. We further prove that modulus six is the unique optimum within
> the entire two-subblock order-three allocation-modulus family.

摘要中不应写：

- “optimal dynamic filter at constant error”；
- “matching upper and lower bounds for ordinary filters”；
- “optimal among all lattices”或“optimal among all fingerprint filters”；
- 对 seed-adaptive histories 或 adaptive-query adversaries 的保证；
- 常数时间或 word-RAM 高效实现。
