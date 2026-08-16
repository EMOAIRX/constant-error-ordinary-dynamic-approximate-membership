# All-pivot converse 的 matching upper bound 审计

> 日期：2026-08-13。状态：严格的等号条件/no-go 分析，加上明确标注的数值
> 压力测试。结论是：当前 all-pivot profile functional 不能单独导出 matching
> ordinary filter；它已经丢掉了决定 fixed-state rate 的 fiber thickness。

所有对数以 2 为底。

## 1. 问题与结论

half-error ordinary dynamic AMQ 的已证 full-fiber all-pivot converse给出

\[
H\ge C_qn-o(n),
\qquad C_{10}>1.6079,
\tag{1}
\]

并且数值上 `C_64≈1.68487`。自然问题是：能否把 optimizer profile
`x(t)` 反向实现成一个 ordinary transducer，从而得到 matching upper bound？

当前答案是否定的，且不是因为还没猜到正确 hash 参数：

1. profile 只记录 full-fiber union 的一阶大小；
2. 相同 profile 可以由厚度、section multiplicity和状态数完全不同的 fibers实现；
3. batch perspective、Jensen 与 pivot convexification 的同时等号只约束这些一阶
   moments，不控制覆盖全部 source endpoints 所需的 state count；
4. 已知 quotient/fingerprint constructions 的 realizable profiles并不接近 all-pivot
   optimizer的等势形状；
5. 即使强行用 heterogeneous fingerprint mixtures拟合 optimizer profile，所需
   occupancy entropy仍远高于 converse值。

所以 all-pivot optimizer 是 proof relaxation 的 extremizer，不是目前有证据支持的
filter extremizer。要闭环必须加入 fiber thickness/section multiplicity，或给出一种
真正越过 canonical quotient 的新 right congruence。

## 2. 已知 ordinary upper bounds

### 2.1 Cross-block mod-$6$ quotient

目前在 KLZ fixed-memory、任意长 history、pointwise FPR模型中最强的已认证显式
ordinary half-error construction是 cross-block mod-$6$ quotient。它使用

\[
H\le2.34614905664n+o(n).
\]

它在两个 binary order-$3$ children 之间只保存一个 allocation load modulo $6$，
从而严格改进下面的独立 binary baseline。

### 2.2 被改进的 binary order-$3$ baseline

该 baseline 使用：

- public outer hash 到 blocks；
- uniform inner bit；
- 每 block保存 exact load和 one-count modulo `3`；
- load `0,1,2` 时精确查询，load至少 `3` 时整块回答 YES。

它使用

\[
H\le2.349083440193\ldots n+o(n).
\tag{2}
\]

该结构不是 heuristic：它是 arbitrary-history key-only right congruence，高负载
residue在删除后自动恢复低负载 composition。

在 deterministic canonical、exact-load、binary key-only summary 类中，lattice
normal form把所有结构归约为 one-count modulo `q`，而 `q=3` 在 half error 下最优。
但该 converse不覆盖 history-dependent multiple representations、cross-block
quotients或 randomized transitions。

### 2.3 Fingerprint baselines

其他相关 rates约为：

- uniform fingerprint multiset Shannon/whp：`2.287904n`；
- uniform exact count-vector fixed-state：`2.384500n`。

第一项空间语义弱于固定最坏任意长 history；第二项属于同一 fixed-state语义但高于
式 (2)。没有已知 ordinary construction接近 `1.6--1.7n`。

## 3. 已知 constructions 的 profile 不等势

对一个 canonical construction，load fraction为 `t` 时，令

\[
x(t)=\frac{\mathbb E|W_t|}{u/2}
\tag{3}
\]

为 half-error归一化 full-fiber union profile。

### Uniform exact fingerprints

若最终 load的 Poisson mean是 `lambda=ln 2`，则

\[
x_{\rm fp}(t)=2(1-e^{-\lambda t}).
\tag{4}
\]

### Order-3 threshold quotient

令 `lambda=1.325819075285...`。一个 block在 load `0,1,2` 时接受已出现 inner
symbols，在更高 load时接受两个 symbols，所以

\[
x_{\rm th}(t)
=2\left[1-e^{-\lambda t}
\left(1+\frac{\lambda t}{2}+\frac{(\lambda t)^2}{8}\right)\right].
\tag{5}
\]

把式 (4)--(5) 在十个等长区间取平均，再代入 all-pivot branches，数值压力测试给：

\[
\max_jL_{10,j}(x_{\rm fp})\approx2.16413,
\tag{6}
\]

\[
\max_jL_{10,j}(x_{\rm th})\approx2.19936.
\tag{7}

而 optimizer为 `1.60799...`，所有 11 个 branches近乎等势。式 (6)--(7) 不是
construction space的 lower bound；它们只证明已知 constructions 的一阶 profile
与 optimizer形状显著不同，无法作为 matching equality witness。

复现实验见 `scripts/compare_realisable_profiles.py`。

## 4. Perspective batch lemma 的同时等号要求

一个 hidden batch的关键上界为

\[
\mathbb E\log\frac{(d)_{\underline Q}}{(V-g)_{\underline Q}}
\le m\alpha\log\frac{\mathbb E d/V}{\alpha}+O(1).
\tag{8}
\]

要使 all-pivot converse接近等号，至少需要：

1. falling-factorial ratio近似其 power relaxation，即 `Q=o(V-g-d)` 尺度上碰撞
   correction消失；
2. perspective Jensen近等号，要求 `d/Q` 在相关 batch experiments中近常数；
3. prefix support和difference first moments同时饱和：
   \[
   \mathbb E g/V\approx x_\ell/2,
   \qquad
   \mathbb E d/V\approx(x_r-x_\ell)/2;
   \]
4. 每个宏观 pivot的 block Jensen近等号，迫使 profile在小 blocks内接近常数；
5. 所有 active pivots同时等势。

这些条件约束 union sizes与rank-code候选数量，却没有约束同一 union support下有多少
source endpoints、每个 key的 section multiplicity或这些 sections在 updates下如何
重叠。因此满足全部式 (8) 的一阶等号条件，仍不能给出 `2^(C n)` 个足以覆盖所有
sources的 physical states。

## 5. 为什么“实现 optimizer profile”不足以给上界

给每个 load `t` 指定 accepted/full-fiber union大小，只定义了一个 distortion
curve。一个 actual transducer还必须提供：

\[
\mathcal F(q)\subseteq{U\choose t},
\qquad
\bigcup\mathcal F(q)\subseteq A(q),
\tag{9}
\]

以及对每个共同合法 label的 deterministic successor。两种极端可有相同 union：

- thick fiber接近 `{W choose t}`，一个 state覆盖指数多 endpoints且 transport稳定；
- thin fiber由少量近乎不交的 sets组成，union相同但 state counting接近 exact set，
  随机 insertion还会产生 birthday-scale transport loss。

all-pivot functional只看到 `|W|`，无法区分这两者。这不是技术上的小 slack，而是
many-to-one projection：从 fiber hypergraph到 union profile不可逆。

因此不存在如下 black-box converse-to-construction转换：

> 给定满足 all-pivot constraints 的 nondecreasing `x(t)`，总能构造使用
> `n sup_t F_t[x]+o(n)` bits 的 ordinary dynamic filter。

要让该命题成立，至少还需指定一个 transition-compatible fiber covering，其 cell
数本身达到对应 rate；profile没有提供这一信息。

## 6. Heterogeneous fingerprints 的拟合压力测试

exact heterogeneous fingerprint mixtures产生 completely monotone形状

\[
x_\nu(t)=2\int(1-e^{-\lambda t})\,d\nu(\lambda),
\tag{10}
\]

并满足 half-error endpoint

\[
2\int(1-e^{-\lambda})\,d\nu(\lambda)=1.
\tag{11}

这是一类非常宽的 realizable profiles。对 64-block optimizer作非负 Laplace
mixture拟合，数值上可把最大 profile误差压到约 `0.00204`，但代价是：

- 约 `0.347` 的 size-biased mass落在 `lambda<0.1`；
- 约 `0.0241` 的 mass落在 `lambda>10` 或永久 YES endpoint；
- 对应 Poisson occupancy Shannon rate约为 `4.11` bits/key。

这些数字只是离散 NNLS压力测试，不是定理，也不证明 `4.11` 为最佳拟合成本。
它们揭示的机制是稳健的：optimizer在 `t=0` 附近增长很快、又必须在 `t=1` 固定
half-error endpoint；Laplace mixture只能同时使用大量极轻与极重 cells。极轻 cells
的 occupancy entropy per key很高，极重 cells则浪费 FPR budget。

复现实验见 `scripts/fit_optimizer_fingerprint_mixture.py`。

## 7. 可实现 tight adversary 的判定

当前不能证明 full-fiber converse存在 matching filter，也不能证明它绝对不可实现。
可以严格判定的是：

1. **现有 canonical binary quotients不是 tight adversary。** 它们的 profile和rate
   均与 optimizer不匹配。
2. **ordinary fingerprint mixtures不是显然的 tight adversary。** 即使拟合 profile，
   状态熵不会随之降到 all-pivot值。
3. **cover-and-tombstone不是 tight adversary。** 它能让单个 source endpoint达到
   Carter rate，却使用 `Theta(u)` continuation fields；它否决 single-parent lemma，
   不给低空间 global construction。
4. **仅用 profile不可能认证 tightness。** matching theorem必须增加 cell
   multiplicity或直接给 transition-compatible covering construction。

所以当前最合理的解释是：all-pivot hierarchy仍是一个非紧 relaxation。其极值
`1.6--1.7` 不能被当作候选最优 ordinary rate，直到有人构造相应 fiber system。

## 8. 下一条真正的 matching 目标

有两条可证伪、且不会退回小数优化的路线。

### 路线 A：thickness-strengthened converse

对每个 full fiber记录 section-weighted厚度，例如

\[
T(q)=H(S\mid M=q,R)
\quad\text{或}\quad
\tau_x(q)=\Pr[x\in S\mid M=q,R].
\tag{12}
\]

证明一个联合不等式

\[
I(S;M\mid R)
+\operatorname{BatchSupportCost}(x)
+\operatorname{TransportDeficit}(\tau)
\ge\operatorname{SourceEntropy}.
\tag{13}
\]

它应在 thick covers上由低 transport支付，在 thin fibers上由 state information支付，
并且所有 pivots只使用一次 `H` budget。若闭合，lower bound可能向 `2.2--2.35`
移动，并解释为何 all-pivot optimizer不可实现。

### 路线 B：history-dependent covering upper bound

直接构造一族 state fibers与 labeled successors，使：

\[
\#\text{states}=2^{Rn+o(n)},
\qquad R<2.349083,
\tag{14}
\]

同时满足 pointwise half error。这里不能只给 snapshot covers；必须给全部 labels的
common-successor closure。一个严格低于 order-3 quotient的 construction本身就是
重要结果，即使仍高于 all-pivot下界。

当前证据更支持路线 A。binary canonical、bias、mask、有限群小例与 heterogeneous
fingerprints均未产生接近 optimizer的新 transducer；缺失信息恰好是 thickness，
而不是另一个 profile parameter。

## 9. 最终裁决

这轮没有 matching upper bound theorem。得到的高价值否定结论是：

> all-pivot optimizer只优化一阶 union profile；该对象不足以决定或构造 fixed-state
> ordinary dynamic filter。现有最强 constructions在其上都不取等，而能够拟合
> profile的 fingerprint mixtures仍支付远高的 occupancy state entropy。

因此下一阶段不应把 `lim C_q` 当作 ordinary optimum去寻找构造。连续极值仍可作为
lower-bound技术定理求解，但若目标是闭合社区问题，必须升级到
thickness-sensitive converse或真正新的 transition-compatible covering construction。
