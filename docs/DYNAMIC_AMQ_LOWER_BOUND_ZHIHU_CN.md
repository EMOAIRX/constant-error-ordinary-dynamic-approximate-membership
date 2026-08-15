# 动态 Bloom Filter 为什么比静态结构更贵：一个 $1.6079n$ bit 的信息论下界

> 本文讨论一个尚未完全解决的理论问题：当假阳性率固定为 $1/2$ 时，支持插入和
> 删除的动态近似成员查询结构至少需要多少空间？文中的严格结论是
> 
> \[
> H>1.6079n-o(n),
> \]
> 
> 但它需要较强的大宇宙条件 $|U|/n^2\to\infty$。这个结果不是 tight bound，
> 也没有证明 fingerprint filters 在常数错误率下最优。

## 1. Introduction

近似成员查询结构解决的是一个非常简单的问题：给定一个键 $x$，判断它是否属于
当前集合 $S$。

它允许两种回答：

- 如果 $x\in S$，必须回答 `YES`；
- 如果 $x\notin S$，可以以至多 $\varepsilon$ 的概率误答 `YES`。

因此它没有假阴性，只有假阳性。一次 `NO` 可以安全地跳过磁盘、网络节点或后端
数据库；一次错误的 `YES` 最多造成一次多余访问。

Bloom filter 是这个问题最著名的静态解法。对于大宇宙中的 $n$ 个键，经典信息论
下界约为

\[
n\log_2\frac1\varepsilon
\]

bit。当 $\varepsilon=1/2$ 时，这个静态 benchmark 只有

\[
n
\]

bit。

然而，很多实际集合并不是静态的。缓存目录、去重窗口、路由状态和持续变化的索引都
要求过滤器支持

\[
\operatorname{Insert}(x),\qquad
\operatorname{Delete}(x),\qquad
\operatorname{Query}(x).
\]

删除使问题发生了本质变化。一个静态过滤器只需回答当前集合的查询；动态过滤器还要
保证，经过任意多次碰撞、插入和删除之后，剩余成员仍然没有假阴性，并且当前非成员
的假阳性概率仍受控制。

这种时间方向上的一致性究竟会增加多少空间？

本文介绍的结果表明：在一个相当一般的 ordinary dynamic filter 模型中，当
$\varepsilon=1/2$ 时，动态结构至少需要

\[
\boxed{H>1.6079n-o(n)}
\]

bit。与静态的 $n$-bit benchmark 相比，这证明了至少

\[
0.6079n-o(n)
\]

bit 的动态额外代价。

这个下界允许结构具有任意 history dependence、ghost entries、全局证书和非单调
查询集合。它不要求结构是 Bloom filter、fingerprint filter、哈希表或 canonical
representation。

但需要提前说明：这还不是问题的最终答案。当前严格上界仍显著高于
$1.6079n$，而且本文的下界需要

\[
\frac{|U|}{n^2}\longrightarrow\infty.
\]

如何把宇宙条件降低到更自然的 $|U|/n\to\infty$，并进一步闭合上下界，仍然是
真正的开放问题。

## 2. 模型：下界究竟覆盖什么

令宇宙为有限集合 $U$，其大小记为

\[
u=|U|.
\]

数据结构维护一个当前集合 $S\subseteq U$，始终满足 $|S|\le n$。它拥有一个
固定长度的 $H$-bit persistent state，并可以读取免费的公共随机带。

更新接口是普通的 key-only API：

- `Insert(x)` 只获得键 $x$，并承诺 $x\notin S$；
- `Delete(x)` 只获得键 $x$，并承诺 $x\in S$；
- 更新算法不能直接读取真实集合 $S$，也不能调用一个不计空间的 exact backing
  dictionary。

我们只要求结构支持合法历史，但允许其物理状态依赖完整历史。换言之，同一个当前
集合可以由不同更新顺序到达不同内存状态。

假阳性保证采用 public-random filter 中标准的 pointwise 量词：对每条在公共随机带
之前固定的合法历史，以及每个固定的当前非成员 $x$，都有

\[
\Pr[\operatorname{Query}(x)=\mathrm{YES}]\le\frac12.
\]

概率只对结构的公共随机性取。

主定理还假设：

\[
u/n^2\to\infty,
\qquad
f(n)/n\to\infty,
\]

其中 $f(n)$ 是结构承诺支持的操作数。第二个条件意味着结构必须支持超线性的更新
窗口，但不要求运行时间高效。

### 主定理

> **定理（ordinary half-error dynamic AMQ lower bound）。** 在上述模型和
> 参数条件下，任何 one-sided dynamic approximate-membership filter 都满足
> \[
> H\ge C_{10}n-o(n),
> \]
> 其中
> \[
> C_{10}\ge
> \frac{803993501430859}{500000000000000}
> =1.607987002861718\ldots>1.6079.
> \]

数值优化给出

\[
C_{10}=1.6079870048457\ldots,
\]

但安全的定理表述是经过有理证书认证的

\[
H>1.6079n-o(n),
\]

而不是把小数向上舍入为 $1.61n$。

## 3. 为什么静态计数不能直接处理删除

静态 approximate membership 的经典下界大致可以这样理解：一个 $H$-bit 状态
至多有 $2^H$ 种取值，而每个状态只能同时代表数量有限的真实集合，否则它必须对
过多非成员回答 `YES`。对状态所能覆盖的集合数量做计数，就能推出空间下界。

动态问题的困难在于，同一个物理状态可能代表很多通过不同历史到达的集合，而且这些
表示在未来更新下还会继续分化或重新合并。

例如，一个结构可以留下已经删除的键作为 ghost。删除 $x$ 后继续对 $x$ 回答
`YES` 并不违反定义，因为 $x$ 只是一个假阳性。结构也可以复用同一批内存，先
记录一部分历史信息，再在后续更新中覆盖它。

因此，不能简单地要求：

> 如果两个当前集合不同，那么它们必须对应不同内存状态。

这个命题一般是错的。真正需要研究的是：一个物理状态所代表的全部逻辑世界，在未来
共同执行某段更新后，还能保留多少可区分信息。

## 4. Full fiber：一个状态究竟可能代表哪些键

固定结构的随机带 $R$。对物理状态 $m$、当前集合大小 $t$ 和已经执行的操作数
$q$，定义

\[
W_R(m,t,q)
=
\bigcup
\left\{
S(h): |h|=q,\ |S(h)|=t,\ M_R(h)=m
\right\}.
\tag{4.1}
\]

这里 $h$ 遍历所有从空集出发的合法历史；$S(h)$ 是其逻辑终点集合，
$M_R(h)$ 是其物理内存状态。

可以把 $W_R(m,t,q)$ 理解为这个物理状态的 full fiber union：

> 在相同随机带、相同当前大小和相同时间坐标下，这个内存状态曾经可能代表过的所有
> 键的并集。

为什么需要保留时间坐标 $q$？因为同一个 bit string 在不同时间可能具有完全不同的
未来更新语义。把时间删掉，会错误地拼接原本不在操作承诺范围内的历史。

若当前真实历史是 $h$，显然

\[
S(h)\subseteq W_R(M_R(h),t,q).
\]

更重要的是，full fiber 中的每个键都必须被当前物理状态接受。若
$x\in W_R(m,t,q)$，就存在另一条历史，使同一个状态 $m$ 代表一个包含 $x$ 的
集合。查询算法只看 $m,x,R$，无法知道真实世界是哪一个，所以 one-sidedness
强迫它回答 `YES`。因此

\[
W_R(m,t,q)\subseteq A_R(m),
\tag{4.2}
\]

其中 $A_R(m)$ 是状态 $m$ 接受的全部键。

对任意固定历史，pointwise FPR 于是给出

\[
\mathbb E_R|W_R(M_R(h),t,q)|
\le t+\frac12(u-t).
\tag{4.3}
\]

式 (4.3) 是整个证明的第一条桥梁：它把查询错误率转化成了一个状态 fiber 的平均
几何大小。

## 5. Common-suffix transport：为什么删除历史可以被比较

假设两条历史 $h$ 和 $h'$ 到达同一个物理状态。由于后续更新只看当前物理状态、
输入键和随机带，如果从两边继续执行同一段合法 suffix，那么它们仍会到达相同物理
状态。

问题在于，同一 suffix 未必对 fiber 中的每一个隐藏集合都合法。如果 suffix 要插入
键 $y$，某个 witness 集合可能已经包含 $y$。

证明没有忽略这个问题，而是显式计算这种 witness collision 的损失。若 suffix 中
使用 $Q$ 个未来插入标签，而 witness 集合大小至多为 $n$，那么在一个足够大的
随机宇宙块中，发生碰撞的概率大致是

\[
O\!\left(\frac{nQ}{u}\right).
\]

对全部 fiber keys 累加后，误差规模变成 birthday-like 的 $n^2/u$。这正是当前
证明需要

\[
u/n^2\to\infty

\]

的根本原因。

在这个条件下，可以选择一个缓慢增长的分块参数，使所有 suffix transport loss 在
一阶空间中都是 $o(n)$。于是 KLZ 操作树上不同 pivot states 的 full-fiber 大小可以
被组织成一个近似单调 profile。

## 6. 为什么要一次编码一整批键

如果逐个编码隐藏键，每个键是否已经落入 prefix fiber 会产生一个 hit/miss bit。
直接把这些 bit 当作独立 Bernoulli 变量通常是错误的：一个全局状态可以让它们高度
相关。

正确做法是联合编码整个 batch。

设一个宇宙块包含 $V$ 个键，隐藏 batch

\[
X=(X_1,\ldots,X_m)
\]

是其中均匀无放回抽取的 ordered distinct tuple。给定 prefix full fiber
$G\subseteq[V]$，令

\[
Q=|\{i:X_i\notin G\}|
\]

是 miss 数量。所有 miss values 必须落在另一个 difference set
$D\subseteq[V]\setminus G$ 中，记 $g=|G|$、$d=|D|$。

联合编码先发送 hit pattern 和 hit values，再把全部 miss values 作为 $D$ 中的
ordered distinct tuple 编码。精确计数给出通信量

\[
\mathcal C
\le
\log(V)_{\underline m}
+\mathbb E\log
\frac{(d)_{\underline Q}}
{(V-g)_{\underline Q}}
+O(1).
\tag{6.1}
\]

这里

\[
(a)_{\underline q}=a(a-1)\cdots(a-q+1)
\]

是下降阶乘。

式 (6.1) 的好处是，它不需要 hit indicators 独立，也不要求 $D$ 与隐藏 batch
独立。所有复杂相关性都被保留在一个下降阶乘比值中。

利用 log perspective 的凹性和 hypergeometric variance，可以进一步证明

\[
\mathbb E\log
\frac{(d)_{\underline Q}}
{(V-g)_{\underline Q}}
\le
m\alpha
\log_2\frac{\mathbb E d/V}{\alpha}
+O(1),
\tag{6.2}
\]

其中

\[
\alpha=\frac{\mathbb E Q}{m}.
\]

关键是余项只有 $O(1)$ 每 batch，而不是 $O(m)$。在 batch 数缓慢增长时，全部
余项加起来仍是 $o(n)$。

## 7. Pivot functional：每个切分位置都给出一个下界

KLZ 的操作树包含一系列可以选择的 pivot。不同 pivot 对应不同的方式：哪些隐藏
batches 从较早状态解码，哪些从较晚状态解码。

经过 full-fiber transport 和 batch coding 后，可以用一个单调 profile

\[
0=x_0\le x_1\le\cdots\le x_b=1

\]

描述 normalized fiber growth。定义

\[
\Phi(a,c)
=
\left(1-\frac a2\right)
\log_2\frac{2-a}{c-a},
\qquad 0\le a<c\le1.
\tag{7.1}
\]

对每个 pivot $s\in\{0,1,\ldots,b\}$，都有

\[
\frac Hn
\ge
F_{b,s}(x)-o(1),
\tag{7.2}
\]

其中

\[
F_{b,s}(x)
=\frac1b\left[
\sum_{k=1}^{s}\Phi(x_{k-1},1)
+\sum_{k=s+1}^{b}\Phi(x_s,x_k)
\right].
\tag{7.3}
\]

这个公式是证明的核心。结构可以自由选择自己的 fiber-growth profile，但通信协议也
可以选择最不利于它的 pivot。因此下界具有一个 minimax 形式：

\[
\inf_x\max_s F_{b,s}(x).

\]

只使用最左和最右两个 endpoint pivots 已经能得到约

\[
1.434406n

\]

的下界。加入更多中间 pivots，可以进一步排除那些只在某些局部区间快速增长、试图
同时逃避两个 endpoint 的 profiles。

## 8. 从无限维 profile 到十维凸优化

直接优化所有 $x_1,\ldots,x_{b-1}$ 并不方便。证明把它们分成 $q$ 个等长宏块，
并记每块平均值为

\[
0<p_0\le p_1\le\cdots\le p_{q-1}<1.
\]

由于 $\Phi$ 具有合适的单调性和联合凸性，可以在每个宏块中使用 Jensen
不等式，把原来的高维 profile 压缩为 $q$ 维凸 minimax：

\[
C_q
=
\inf_{0<p_0\le\cdots\le p_{q-1}<1}
\max_{0\le j\le q}L_{q,j}(p).
\tag{8.1}
\]

这里

\[
A(x)=\log_2\frac2x,
\]

\[
B(x)=
\left(1-\frac x2\right)
\log_2\frac{2-x}{1-x},
\]

并定义

\[
L_{q,0}(p)=\frac1q\sum_{r=0}^{q-1}A(p_r),
\tag{8.2}
\]

\[
L_{q,j}(p)
=\frac1q\left[
\sum_{r<j}B(p_r)
+\sum_{r\ge j}\Phi(p_{j-1},p_r)
\right],
\qquad1\le j<q,
\tag{8.3}
\]

\[
L_{q,q}(p)=\frac1q\sum_{r=0}^{q-1}B(p_r).
\tag{8.4}
\]

因此对每个固定 $q$，都有严格下界

\[
H\ge C_qn-o(n).

\]

取 $q=10$ 得到本文的 $1.6079$ 常数。

## 9. 为什么数值优化可以变成严格证明

仅仅运行一个 nonlinear optimizer 并得到

\[
1.6079870048\ldots

\]

当然不构成证明。局部优化器可能停在错误点，浮点误差也可能掩盖真正的最小值。

这里使用凸 dual witness 把数值候选转化为全局证书。

选择正权重

\[
\lambda_0,\ldots,\lambda_{10}>0,
\qquad
\sum_j\lambda_j=1,
\]

并定义凸组合

\[
L(p)=\sum_{j=0}^{10}\lambda_jL_{10,j}(p).

\]

对任意 $p$，都有

\[
\max_jL_{10,j}(p)\ge L(p).

\]

在一个有理近似点 $p^*$ 处，由凸性，

\[
L(p)
\ge
L(p^*)+\nabla L(p^*)\cdot(p-p^*).

\]

因为每个坐标位于 $[0,1]$，进一步有

\[
L(p)
\ge
L(p^*)-\|\nabla L(p^*)\|_1.
\tag{9.1}
\]

验证程序完全使用有理数，并通过带显式尾界的级数包住所有对数。最终严格认证

\[
L(p^*)\ge1.607987003822005\ldots,
\]

以及

\[
\|\nabla L(p^*)\|_1
\le9.603\times10^{-10}.
\]

代入式 (9.1)，得到

\[
C_{10}\ge1.607987002861718\ldots>1.6079.

\]

所以这里的机器计算不是有限实例搜索，而是一个覆盖整个连续十维可行域的全局凸
证书。

## 10. 这个下界的意义

这个结果首先给出了一个明确的动态 premium。在 $\varepsilon=1/2$ 时，静态
Carter benchmark 是 $n$ bit，而 ordinary dynamic filter 至少需要

\[
1.6079n-o(n)

\]

bit。

其次，它不依赖某种具体数据结构语法。证明允许：

- 同一个集合具有多个物理表示；
- 状态依赖完整更新历史；
- 删除后保留 ghost positives；
- 查询接受集合随时间非单调变化；
- 使用 global certificates 或跨键共享信息；
- 任意昂贵的计算。

因此它不是“某类 Bloom filter 需要这么多空间”，而是 ordinary key-only dynamic
membership API 下的信息论结论。

第三，证明产生了一个可继续加强的层级

\[
C_1,C_2,\ldots,C_q,\ldots

\]

而不是只给出一个孤立常数。十块只是目前完成严格 dual certificate 的层级；更高阶
profile 或连续极限可能继续提高常数。

## 11. 这个结果没有解决什么

边界同样重要。

### 11.1 它不是 tight bound

目前的 fixed-state 上界仍显著高于 $1.6079n$。因此我们既不知道真正最优常数，
也不知道 extremal filter 应该长什么样。

### 11.2 它需要 $u\gg n^2$

FOCS 2025 更自然的大宇宙条件接近

\[
u/n\to\infty.

\]

本文之所以需要 $u/n^2\to\infty$，是因为 common-suffix transport 对 full-fiber
witnesses 使用了 birthday-scale union bound。解除这个条件需要一种能控制 witness
overlap 或 fiber thickness 的新方法。

### 11.3 它不证明 fingerprint filters 最优

KLZ 在 $\varepsilon=o(1)$ 区间证明了 fingerprint optimality；本文只处理
$\varepsilon=1/2$ 下的一个一般下界。当前结果远不足以推出常数错误率时任意动态
过滤器都必须达到某个 fingerprint-multiset rate。

### 11.4 它不处理 seed-adaptive adversary

假阳性保证针对预先固定、与公共随机带独立的历史和查询键。若对手读取 hash seed，
或根据先前回答不断寻找碰撞键，需要使用 adaptive AMQ 的另一套模型与技术。

## 12. Related Work

### 12.1 静态 approximate membership

Carter 等人的经典工作建立了 approximate membership 的计数下界和 fingerprint
reduction。Bloomier、Xor、ribbon 及 retrieval-based filters 后来给出了很多接近
静态信息率且高效的构造，但静态结构不需要保证删除后的状态可继续演化。

### 12.2 动态 filters 与 fingerprint multisets

Pagh、Pagh 与 Rao 的 Bloom filter replacement，以及后续动态 multiset
dictionaries，说明维护 fingerprint multiplicities 是支持删除的一条自然路径。
这类结果通常把空间写成

\[
n\log_2(1/\varepsilon)+O(n).

\]

在低错误率时，$O(n)$ 是低阶项；在常数错误率时，它正好隐藏了问题的全部线性
常数。

### 12.3 动态下界

Lovett–Porat、Kuszmaul–Walzer 等工作逐步证明，动态更新会产生静态计数法看不到的
额外空间。Kuszmaul、Liang 与 Zhou 在 FOCS 2025 进一步证明，当
$\varepsilon=o(1)$ 且宇宙足够大时，任何动态 filter 都需要

\[
n\log_2(1/\varepsilon)+n\log_2e-o(n)

\]

bit，并明确将常数错误率的 tight upper and lower bounds 留作开放问题。

本文使用其 operation-tree 与 pivot 思想，但重新定义 partition-independent full
fiber，并使用 joint batch coding 与 all-pivot convex hierarchy 处理固定错误率。

### 12.4 ChainedFilter 与有限宇宙结果

ChainedFilter 使用 chain rule 组合静态 membership filters，并研究 finite-universe
和 distribution-aware 的静态空间率。其无损 chain rule 不直接适用于一般动态
membership：一个组件状态必须在未来插入和删除下继续保持合法，而不仅仅代表当前
snapshot。

因此本文并不是 ChainedFilter 静态公式的直接动态化。两者共享信息论视角，但核心
约束不同：前者关注静态集合的分解，本文关注同一个物理状态在未来更新下的 full-fiber
transport。

## 13. 接下来真正值得解决的问题

目前最重要的三个方向是：

1. 将宇宙条件从 $u\gg n^2$ 降到 $u\gg n$；
2. 识别 all-pivot hierarchy 的连续极限，继续提高 $1.6079$ 常数；
3. 找到与最强 fixed-state construction 相匹配的一般下界，或者证明
   history-dependent / noncanonical filters 能严格击败现有 fingerprint-style
   上界。

第一个问题需要控制不同 witnesses 的重叠，而不是继续使用逐 witness union bound；
第二个问题需要理解 convex profile 的极值结构；第三个问题则可能要求一种同时看见
全部 replacement branches、但只对最终 $H$-bit state 收费一次的新信息论不等式。

## 14. 一句话总结

动态 approximate membership 的困难不只是“多支持一个 Delete 操作”。删除迫使
同一段有限内存在许多可能历史之间保持未来一致性。通过 full fiber、整批编码和
all-pivot 凸层级，可以把这种一致性转化为严格的信息代价：在 half error、
$u\gg n^2$ 的 ordinary 模型中，任何结构都至少需要

\[
\boxed{1.6079n-o(n)\text{ bits}.}

\]

这已经严格超过静态 benchmark，但距离常数错误率下真正的最优答案仍有很长一段
路。

---

## 附：可复核的证书

主常数由以下两个独立 verifier 复核：

```bash
python3 scripts/verify_ten_block_160_certificate.py
python3 scripts/verify_ten_block_pivot_160_dual.py
```

第一个程序认证

\[
C_{10}\ge1.607987002861718\ldots>1.6079,

\]

第二个程序使用不同的有理对数区间实现作交叉检查。两者都不是用浮点网格代替证明。
