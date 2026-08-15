# Two-choice placement 是否能击败 \(R_{\rm fp}\)：一个解析 information-conservation 审计

> 日期：2026-08-14。状态：Theorem 2.1--2.2 为解析定理，不依赖数值优化或
> computer-assisted certificate。它们关闭的是所有 **public stateless routing +
> exact-multiplicity encoding** 的 two-choice / \(d\)-choice 路线，不是所有
> key-recomputable routes。对 lossy reversible label summaries、跨 label global
> quotients 和真正 state-dependent cuckoo placement，本文给出完整收费清单与严格
> barrier，但尚未证明 unrestricted no-go，也未构造低于 \(R_{\rm fp}\) 的普通动态
> filter。

所有对数以 2 为底。目标误差固定为常数 \(\varepsilon\in(0,1)\)。

## 1. 结论先行

two-choice 只有两种本质不同的用法。

1. **路由可由 key 与 public tape 重算。** 例如始终选
   \(\min\{h_1(x),h_2(x)\}\)，或对候选位置应用任意固定公开函数。此时 query
   也能重算同一位置，只需 probe 一个 cell。整个结构精确退化为一个非均匀
   single-fingerprint **update-label map**。如果状态 exact 地维护 label
   multiplicities，则 Poisson occupancy rate 必须位于 \(R_{\rm fp}\) 的可行域中，
   不能严格击败它；如果状态只维护 lossy / ghost / quotient summary，则仍需单独分析。
2. **路由依赖当前 state。** 这才是真正的 cuckoo / power-of-two-choices
   placement。此时 query 通常必须 probe 多个候选位置；而 key-only deletion 必须
   从 persistent state 恢复、消除或安全地绕过 insertion-time route。支持集合、
   orientation、relocation、last-copy certificate、stash、overflow recovery 都必须
   一起收费。只计算 occupied support 的 Shannon entropy 不是一个动态 upper bound。

因此，\(2.1216107112n\) 的 min-rank support 数字不能直接作为
\(R_{\rm fp}(1/2)=2.2006114829\ldots\) 的反例：min-rank 本身属于第一种情形，
而让 query 无条件 probe 两格只是人为放宽 FPR，并没有产生一个可删除的动态状态。

## 2. Public stateless routing 精确退化为 categorical fingerprints

令 public tape 为每个 key 产生候选 tuple

\[
H(x)=(h_1(x),\ldots,h_d(x))\in[q]^d.
\]

一个 public stateless route 是固定函数

\[
\phi:[q]^d\longrightarrow\mathcal A,
\]

其中 \(\mathcal A\) 是 tracked labels；也允许一个 permanent-YES label
\(\top\)。插入与删除都只更新 label \(\phi(H(x))\) 的 multiplicity。query 对
\(\phi(H(x))=\top\) 永远回答 YES；否则只查询相应 tracked label 是否非空。

令

\[
p_a=\Pr[\phi(H(x))=a],\qquad a\in\mathcal A,
\]

概率取自 public tape。注意 \(p_a\) 可以极不均匀；\(d\)、候选之间的相关性和
\(\phi\) 的复杂性全部已经被吸收到 \((p_a)\) 中。

### Theorem 2.1（stateless-choice update-label collapse）

任意 public stateless \(d\)-choice route 都诱导一个 categorical label map：直接把
\(x\) 映射到 \(a=\phi(H(x))\)，其 tracked probabilities 正是 \((p_a)\)。因此两者
在每条 tape、每条 key-level history 上产生相同的 **logical label-multiplicity
process**。如果物理结构是 exact-multiplicity encoding，则两者也具有相同的物理
update semantics 与 query answers。

**证明。** 定义单一 public map \(f=\phi\circ H\)。对每个 key，两种描述在
Insert/Delete 时作用于同一个 logical label \(f(x)\)，故 logical count process
逐操作相同。若状态 exact 地编码这些 counts，query 也读取同一非零谓词。\(\square\)

这个定理不只覆盖 min-rank。随机但 frozen 的 tie-breaking、按候选地址的公开
priority、多个 hash 的任意布尔组合，以及任何不读取 persistent state 的路由都被
同时压成同一个 categorical update-label model。这里没有声称一个 lossy physical
summary 必须恢复 counts。

## 3. 解析 rate 公式与 \(R_{\rm fp}\) no-go

取容量 \(n\)，令

\[
\lambda_a=np_a.
\]

对 seed-independent 的 fixed set，在标准 Poisson occupancy 极限下，tracked
label \(a\) 的 count 为 \(\operatorname{Pois}(\lambda_a)\)。定义 size-biased load
measure

\[
\nu_n=\sum_{a\in\mathcal A}p_a\,\delta_{\lambda_a}.
\]

若 tracked mass 小于 1，缺失质量就是 permanent-YES component，可等价地视为
\(\lambda=\infty\)。令

\[
g(\lambda)=1-e^{-\lambda},
\qquad
r(\lambda)=\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda}.
\]

则 exact-multiplicity source 的每 key rate 与 FPR 分别为

\[
R=\int r(\lambda)\,d\nu_n(\lambda)+o(1),
\tag{1}
\]

\[
\varepsilon=\int g(\lambda)\,d\nu_n(\lambda)+o(1).
\tag{2}
\]

式 (1) 只是恒等变形：

\[
\frac1n\sum_a H_2(\operatorname{Pois}(np_a))
=\sum_a p_a\frac{H_2(\operatorname{Pois}(\lambda_a))}{\lambda_a}.
\]

式 (2) 来自 query label 的 size-biased sampling：一个固定非成员落入 \(a\) 的
概率为 \(p_a\)，该 label 被当前集合占据的概率渐近为
\(1-e^{-\lambda_a}\)。

定义

\[
R_{\rm fp}(\varepsilon)
=\operatorname{lce}_{\lambda>0}\bigl(g(\lambda),r(\lambda)\bigr)(\varepsilon),
\tag{3}
\]

其中同时允许与 endpoint \((1,0)\) convexify。

### Theorem 2.2（exact-multiplicity analytic conservation）

对任意 public stateless \(d\)-choice exact-multiplicity family，若其 pointwise
FPR 至多 \(\varepsilon+o(1)\)，则其 Poisson source rate 满足

\[
\boxed{R\ge R_{\rm fp}(\varepsilon)-o(1).}
\tag{4}
\]

**证明。** 式 (1)--(2) 说明 \((\varepsilon,R)\) 是曲线
\((g(\lambda),r(\lambda))\) 上点的概率混合；permanent-YES mass 给 endpoint
\((1,0)\)。所有这种混合的下边界按定义就是 lower convex envelope (3)。
\(\square\)

这不是 numerical comparison，而是对任意 \(d\)、任意非均匀候选分布和任意公开
静态 route 的 **exact-multiplicity subclass** 的解析 no-go。它解释了这个 subclass
中“power of choices”为何没有出现：choice 只是在重新设计 categorical hash
distribution；这一自由度已经被 \(R_{\rm fp}\) 的 load mixture 完整优化。

### Hostile scope correction

Theorem 2.2 **不能**推出下列更强命题：

\[
\text{public stateless route}\Longrightarrow H\ge nR_{\rm fp}-o(n)
\]

对任意 ordinary dynamic physical summary 成立。逻辑 counts 可以被一个
history-dependent right congruence 压缩：zero count 允许暂时落在 query-YES ghost
state；多个 labels 还可以共享 global modular residue 或 reversible syndrome。普通
AMQ 不要求恢复 count vector，也不要求空 label 立即回答 NO。因此 (1) 的
Poisson-count entropy 只是 exact-multiplicity source rate，不是 arbitrary summary
的下界。

## 3.1 对 per-label right-congruent summaries 能证明到哪里

先固定一个 label，逻辑 count 为 \(c\in\{0,\ldots,N\}\)。固定 public tape 后，
它是一个 deterministic unary transducer，合法操作为
\(I:c\mapsto c+1\) 与 \(D:c\mapsto c-1\)。所有 \(c>0\) 的 representations
必须 query YES；\(c=0\) 可以是 NO，也可以是 history-dependent ghost YES。

### Proposition 3.1（canonical-reset 强迫 exact counting）

假设一个 per-label transducer 满足：

1. 每条以 count zero 结束的合法 word 都回到同一个 state \(e\)；
2. \(e\) query NO；
3. 每个正 count state query YES。

则从 \(e\) 连续插入得到的 states

\[
s_i=I^i(e),\qquad 0\le i\le N,
\]

两两不同。因此 local machine 至少有 \(N+1\) 个 states。

**证明。** 若 \(s_i=s_j\) 且 \(i<j\)，从共同 state 执行 \(D^i\)。从
\(s_i\) 出发的 endpoint count 为 zero，按 canonical reset 到达 \(e\) 并回答 NO；
从 \(s_j\) 出发的 endpoint count 为 \(j-i>0\)，同一 deterministic continuation
却到达同一 state，必须回答 YES，矛盾。\(\square\)

若 \(q\) 个 labels 是独立 state product，且总 count 至多 \(n\)，对每个 abstract
count vector 按 label 顺序从 empty 插入即可到达相应 product state。Proposition 3.1
使不同 vectors 的 product states 不同，于是 fixed memory 至少为

\[
\log_2\binom{n+q}{q}.
\tag{4a}
\]

这甚至强于典型 Poisson source 的 Shannon rate，但前提也明显更强：zero endpoint
必须 canonical reset 且 labels 不共享 state。

### Proposition 3.2（canonical count-only summaries 的二分）

更一般地，假设一个 label 的 local physical state 只依赖当前 count：

\[
m=\psi(c),\qquad 0\le c\le N,
\]

并且 Insert/Delete 在这些 canonical states 上是确定的合法 right congruence。则恰有
以下二分。

1. 若 \(\psi(0)\) query NO，则 \(\psi(0),\ldots,\psi(N)\) 两两不同，local
   summary 是 exact count 的重命名；
2. 若 \(\psi(0)\) query YES，则由于所有正 counts 也必须 YES，这个 label 在所有
   logical states 上永久回答 YES。若 labels 之间没有 coupling，它的 persistent
   counter可全部删除而不改变 query semantics。

**证明。** 第一种情形若 \(\psi(i)=\psi(j)\)、\(i<j\)，共同执行 \(D^i\) 后得到
\(\psi(0)=\psi(j-i)\)，同一 state 必须同时 NO 与 YES，矛盾。第二种情形的 query
谓词在 \(c=0\) 与所有 \(c>0\) 上均为 YES。\(\square\)

因此，对 **independent per-label canonical summaries**，不存在介于 exact counter
与 permanent-YES label 之间的第三种机制。在典型-source / Poisson 编码语义下，
跨 labels 随机混合这两类恰好仍落入 Theorem 2.2 的 load-mixture convexification，
所以不能低于 \(R_{\rm fp}\)。这是当前能对 per-label right-congruent summaries
得到的最强解析关闭。

命题的边界同样重要。threshold residues之所以不被它排除，是因为一个 physical
block联合摘要多个 query labels，例如同时保存 total load 与某个 bit-count residue；
单个 label 的 state 不是自身 count 的函数。更一般的 global syndrome 也通过
labels coupling 逃离 Proposition 3.2。

### 为什么不能删掉 canonical-reset 前提

若允许 ghost zero states，\(s_i=s_j\) 只迫使特定 balanced history
\(I^iD^i\) 在该 tape 上 false positive，并不产生 false negative。随机 tapes 可以
把不同 zero histories 的 ghost events高度相关。已知 unary collision argument只给

\[
K\ge (1-\delta)N+1
\]

个 local states（这里 \(\delta\) 是每个固定 zero history 的 FPR），但它不能直接
张量化成 \(q\) 个 labels 的 Poisson entropy lower bound：

- ordinary public hashing 下，“向指定 label 插入 \(i\) 个 keys”通常依赖 tape，
  不是合法的 seed-independent fixed history；
- global quotient 可以让 labels 共享同一批 residue bits，破坏 product direct sum；
- pointwise FPR 控制的是每个 fixed key/history 对 tapes 的边缘，不是条件于某个
  label fiber 或当前 state 的错误率。

所以目前可以严格关闭的是 canonical count-only product summaries；对任意
per-label **history-dependent** right congruence，仍缺一个 fractional
fixed-history covering lemma。对允许 multi-label/global coupling 的 summaries，
问题更强，已经回到完整的 transition-constrained fiber-width converse。已有
threshold-quotient constructions正是一个严格警告：它们支持任意长 key-only
updates 与可恢复 high-load states，虽然当前已知 rate 仍高于 \(R_{\rm fp}\)，却已
证明“stateless route 必须保存 exact Poisson counts”这个更强命题为假。

## 4. min-rank 例子的正确解释

取两个独立 uniform candidates，公开排序后选择较小者。令 \(q=n/\alpha\)，将
cell rank 缩放为 \(t\in[0,1]\)。selected label 的 query density 与 Poisson load
分别是

\[
f(t)=2(1-t),
\qquad
\lambda(t)=\alpha f(t)=2\alpha(1-t).
\]

正确的 selected-cell FPR 是

\[
\begin{aligned}
\varepsilon_{\rm sel}(\alpha)
&=\int_0^1 f(t)\bigl(1-e^{-\lambda(t)}\bigr)\,dt\\
&=1-2\int_0^1 y e^{-2\alpha y}\,dy\\
&=1-\frac{1-(1+2\alpha)e^{-2\alpha}}{2\alpha^2}.
\end{aligned}
\tag{5}
\]

exact-count rate 是

\[
R_{\rm count}(\alpha)
=\frac1\alpha\int_0^1
H_2(\operatorname{Pois}(2\alpha(1-t)))\,dt.
\tag{6}
\]

式 (5)--(6) 正是 Theorem 2.2 中一个连续 load mixture，所以自动满足

\[
R_{\rm count}(\alpha)
\ge R_{\rm fp}(\varepsilon_{\rm sel}(\alpha)).
\tag{7}
\]

此前 support-only 压力测试使用

\[
\varepsilon_{\rm OR}=1-(1-\rho)^2,
\qquad
\rho=1-\frac{1-e^{-2\alpha}}{2\alpha},
\]

即 query 无条件检查两个 candidate cells。对于 min-rank route，这不是最强 query：
查询者知道哪一个 candidate 被选中。更重要的是，support bits 不能在 Delete 时判断
被删 key 是否是 selected cell 的最后一份 copy。于是
\(R_{\rm support}=2.1216107112\ldots\) 同时混合了：

- 一个不必要的 two-probe query rule；
- 一个缺少合法 deletion transition 的 snapshot representation。

它仍是反驳“endpoint support entropy 必须至少为 \(R_{\rm fp}\)”的好例子，但不是
ordinary dynamic upper bound。

## 4.1 另一个解析极端：symmetric collision-free benchmark 也不够便宜

也可以走相反极端，设 adaptive cuckoo placement 保证每个 occupied cell 恰有一
个 key。这样 last-copy 问题消失，但若有 \(n\) 个 live keys，就必须有恰好 \(n\)
个 occupied cells。令 \(q=n/\rho\)。一个 fresh query probe 两个独立 candidates
时

\[
\varepsilon=1-(1-\rho)^2,
\qquad
\rho=1-\sqrt{1-\varepsilon}.
\tag{7a}
\]

若 placement law 对 cell permutations 对称，则 size 恰为 \(n\) 的 occupied
support 在 \(q\) 个 cells 上均匀。即使暂时把 orientation 与 dynamic matching
certificate 当作免费，其 snapshot entropy 仍为

\[
\frac1n\log_2\binom qn
=\frac{h_2(\rho)}{\rho}+o(1)
\tag{7b}
\]

bits/key。在 \(\varepsilon=1/2\) 时，\(\rho=1-1/\sqrt2\)，且 (7b) 可精确写成

\[
\log_2(2+\sqrt2)+\frac{1+\sqrt2}{2}
=2.978\ldots,
\tag{7c}
\]

已经显著高于 \(R_{\rm fp}(1/2)\)，尚未计入 routing。

这不是对所有非对称 adaptive placements 的下界；公开 priorities 可以破坏上述
uniform-support law。但它给出第二个干净压力测试，并显示 two-choice 面临的
conservation tension：

- 把 loads 压到 0/1 会消除 multiplicity，但 occupied-support cardinality 本身过大；
- 利用 collisions 降低 support entropy，必须重新支付 last-copy / reversible
  multiplicity information。

旧的 \(2.1216\) snapshot 正位于第二端：它通过大量 collisions 节省 support，
却恰好删掉了动态删除所需的信息。

## 5. 真正 adaptive two-choice 必须支付什么

若 insertion route 为

\[
\sigma_h(x)\in\{h_1(x),h_2(x)\}
\]

并依赖当前 history/state，则 Theorem 2.1 不再适用。此时一个完整构造必须同时给出
以下对象，且全部位于同一个 fixed worst-case \(H\)-bit state 中。

1. **Query support.** query 必须知道哪些候选 cell 当前可接受。
2. **Deletion route.** 给定 key \(x\) 和当前 state，Delete 必须知道应撤销哪一次
   placement，或者证明撤销任一候选都不会造成 false negative。
3. **Last-copy certificate.** 即使 route 已知，也必须区分该 cell 的 occupancy 是
   1 还是至少 2；否则清除会产生 false negative，保留会产生 ghost。
4. **Relocation transcript.** cuckoo move 改变旧 keys 的位置。未来只给出被删除
   key，不提供其 insertion handle；当前 state 必须让 deletion 找到 move 后位置。
5. **Multiplicity and stash.** 重边、同 fingerprint copies、cycles、stash 和失败
   状态都必须计入。
6. **Recoverable overflow.** 固定 worst-case memory 不允许忽略 atypical tape。
   arbitrary history 下 absorbing ALL-YES overflow 会被重复 churn 放大到 FPR 1。
7. **Public randomness quantifier.** pointwise FPR 只适用于抽 tape 前固定的 history；
   不能先看 candidate graph，再选择碰撞最坏的 keys 来论证下界或构造成功。

这给出一个严格的模型分叉。

### Case A：route 只由 \(x\) 与 public tape 决定

Theorem 2.1 把它压成 categorical update labels。若 state exact 地编码
multiplicities，Theorem 2.2 给出 rate 不低于 \(R_{\rm fp}\)；若 state 使用
history-dependent ghosts、mod counters 或 global quotient，则仍未关闭。

### Case B：route 读取 persistent state

若 state 显式保存一个 retrieval map

\[
x\mapsto \sigma_h(x),
\]

其所有 bits 都必须收费；不能把 orientation 称为 insertion-time free advice。若不
保存该 map，则必须给出一个由 query support、local counters 或全局 syndrome
唯一决定删除效果的 transition theorem。仅给 endpoint occupancy law 不足以定义
Delete。

## 6. 任意 history 与 subexponential fixed history

两种 horizon 不能混为一谈。

### 6.1 任意长 history

typical-set failure 不能被永久吸收到 ALL-YES。若每个 epoch 有条件失败概率
\(p>0\)，重复固定 build/delete cycle \(T\) 次后 sticky failure 概率至少

\[
1-(1-p)^T\to1.
\]

所以必须实现 zero overflow，或保留可逆信息使失败状态能恢复。对 support-only
placement，这恰好重新引入 multiplicity / routing residue。

### 6.2 长度 \(f(n)=2^{o(n)}\) 的 fixed histories

union bound 可以把单个 endpoint 的失败概率放大到整条固定 history，但它只解决
resource probability，不解决 key-only deletion。一个候选构造至少需要：

\[
\Pr[\text{任一 endpoint routing/deletion failure}]
\le \exp(-\omega(\log f(n))),
\tag{8}
\]

并在 failure tape 上仍保持逐 tape zero false negatives。若 failure 后进入 ALL-YES，
其概率必须计入每个 fixed query 的 FPR；若希望重复使用 epoch，则必须说明怎样在不
保存 exact set 的前提下 rebuild。

因此 subexponential horizon 确实比 arbitrary history 留出空间，但“support typical
entropy + union bound”本身仍不是构造。

## 7. 当前最强裁决

本次探索得到一个 clean、非 computer-assisted 的关闭结果：

\[
\boxed{
\begin{gathered}
\text{key-recomputable public }d\text{-choice route}
\equiv\text{ categorical update-label map},\\
\text{再加 exact-multiplicity encoding，或 independent canonical count-only summaries}
\Longrightarrow R\ge R_{\rm fp}.
\end{gathered}}
\]

所以，若 ordinary dynamic AMQ 真能低于 \(R_{\rm fp}\)，突破至少必须走下面两类
机制之一：

1. public stateless route 加上非 exact、history-dependent 的 reversible label
   summary，尤其是跨 labels 的 global quotient；
2. state-dependent placement，并同时解决 routing / deletion information。

第二类必须同时处理：

- state-dependent placement；
- 非平凡的 key-only deletion mechanism；
- routing 与 last-copy information 的联合压缩；
- 对 fixed worst-case memory 和 overflow 的完整处理。

目前尚无合规构造，也尚无 theorem 排除全部 Case B。对社区最有价值的下一 lemma
不是继续优化 two-choice snapshot 常数，而是下面的 transition-constrained
information-conservation 命题：

> 对随机 candidate graph 上的任意 fixed-memory transducer，若 query 只读取两个
> candidates，update 只给 key，并支持 zero-FN、pointwise FPR 与可恢复 overflow，
> 则 query-support entropy 与 routing/last-copy transition width 之和至少为
> \(nR_{\rm fp}(\varepsilon)-o(n)\)。

证明它会关闭整个 two-choice/cuckoo-like 反例路线；反例则必须直接给出一个严格低于
\(R_{\rm fp}\) 的 ordinary dynamic construction。两种结果都具有真正的论文价值。

## 8. Multi-label commutative additive quotients：解析 zero-certificate inequality

下面把 no-go 推到一个严格大于 binary threshold residues 的自然 class。令
\(\Gamma\) 为任意有限 Abelian group，query alphabet 为 \(\mathcal A\)，public
label distribution 为 \(\mu\)，每个 label 关联向量

\[
v_a\in\Gamma.
\]

一个 block 内有 \(c\) 个 iid labels \(A_1,\ldots,A_c\sim\mu\)，结构保存

\[
Z_c=\sum_{i=1}^c v_{A_i}.
\tag{9}
\]

它还可保存 exact total load \(c\)。Insert/Delete 对 (9) 做群加减，所以这是一个
支持任意长 key-only history、自动从 high layers 恢复的 right congruence。

给定 \(Z_c=z\)，one-sidedness 下最小安全 accepted-label set 为

\[
K_c(z)=\{a:\Pr[Z_{c-1}=z-v_a]>0\}.
\tag{10}
\]

令该 state 的 prior rejection mass 为

\[
R_c(z)=1-\mu(K_c(z)),
\qquad
\bar R_c=\mathbb E R_c(Z_c).
\tag{11}
\]

### Theorem 8.1（entropy increment pays for zero certificates）

对每个 \(c\ge1\)，

\[
\boxed{
H(Z_c)-H(Z_{c-1})
\ge
\mathbb E\log_2\frac1{1-R_c(Z_c)}
\ge
\log_2\frac1{1-\bar R_c}.}
\tag{12}
\]

从而

\[
\boxed{
H(Z_c)
\ge c\,\mathbb E\log_2\frac1{1-R_c(Z_c)}
\ge c\log_2\frac1{1-\bar R_c}.}
\tag{13}
\]

**证明。** 给定 \(Z_c=z\)，后验分布
\(P_{A_c\mid Z_c=z}\) 的 support 包含于 \(K_c(z)\)。在所有支撑于
\(K_c(z)\) 的 distributions 中，相对 prior \(\mu\) 的最小 KL divergence 是
\(-\log_2\mu(K_c(z))\)，由 \(\mu\) 条件化到 \(K_c(z)\) 达到。因此

\[
I(A_c;Z_c)
\ge\mathbb E\log_2\frac1{1-R_c(Z_c)}.
\]

另一方面，群平移不改变 entropy，故

\[
I(A_c;Z_c)
=H(Z_c)-H(Z_c\mid A_c)
=H(Z_c)-H(Z_{c-1}).
\]

这给出 (12)，第二个不等式是 Jensen。为证 (13)，注意 \(A_i\) 独立，故

\[
\sum_{i=1}^c I(A_i;Z_c)
\le I(A_1,\ldots,A_c;Z_c)=H(Z_c).
\]

由 exchangeability，每项都等于 \(I(A_c;Z_c)\)，结合前式即得。\(\square\)

同一证明适用于 cancellative commutative monoid，只要 translation 在相关 support
上保持 entropy；对一般 monoid 则保留 KL-support 版本，但 entropy increment 恒等式
可能变为不等式。

### Corollary 8.2（Poisson block functional）

若 block load \(C\sim\operatorname{Pois}(\lambda)\)，且 state 保存 \((C,Z_C)\)，
其 entropy 与 fresh-query rejection probability分别满足

\[
\mathcal H
=H_2(\operatorname{Pois}(\lambda))
+\sum_{c\ge1}\Pr[C=c]H(Z_c),
\tag{14}
\]

\[
\beta
=e^{-\lambda}+\sum_{c\ge1}\Pr[C=c]\bar R_c,
\tag{15}
\]

以及解析 lower bound

\[
\boxed{
\mathcal H
\ge H_2(\operatorname{Pois}(\lambda))
+\sum_{c\ge1}\Pr[C=c]\,
c\log_2\frac1{1-\bar R_c}.}
\tag{16}
\]

这里 \(e^{-\lambda}\) 是 empty block 的必然 rejection。式 (16) 同时覆盖任意
group size、任意向量 multiset \(V=(v_a)\)、任意非均匀 \(\mu\)，没有使用 binary、
\(q=3\) 或有限枚举。

这里的 \(\mathcal H\) 是 Poisson source / typical-snapshot entropy。把它提升成
fixed worst-case \(H\)-bit construction 仍需覆盖 atypical global compositions；
反过来，(16) 也不是 arbitrary ordinary-filter lower bound，因为它假设物理 state
确实是 commutative additive syndrome \((C,Z_C)\)。

## 9. 为什么这还没有推出 sharp \(C_*\)

希望证明的高误差支 inequality 是

\[
\mathcal H\stackrel{?}{\ge}C_*\lambda\beta,
\qquad C_*=4.4012229659\ldots.
\tag{17}
\]

Theorem 8.1 是正确的 loadwise zero-certificate inequality，但 (17) **不可能通过
逐 load 的线性命题**

\[
H(Z_c)\ge C_*c\bar R_c
\tag{18}
\]

得到。最小反例已经在 \(c=1\)：取两个等概率 labels，令
\(v_0\ne v_1\)。则

\[
H(Z_1)=1,qquad \bar R_1=\frac12,
\]

所以 (18) 会错误地要求 \(1\ge C_*/2>2\)。事实上 (13) 在此例取等：

\[
H(Z_1)=\log_2\frac1{1-\bar R_1}=1.
\]

因此 \(C_*\) 若为真，只能来自 **跨 occupancy layers 的 convolution
compatibility** 与 Poisson weights，而不是某一 layer 的静态 support certificate。

这里还有一个可利用的解析结构。定义 entropy increments

\[
\Delta_c=H(Z_c)-H(Z_{c-1}).
\]

由 (12)，

\[
\bar R_c\le1-2^{-\Delta_c}.
\tag{19}
\]

而 \((\Delta_c)\) 单调不增：由 exchangeability
\(\Delta_c=I(A_1;Z_c)\)，且
\(A_1\to Z_c\to Z_c+v_{A_{c+1}}=Z_{c+1}\) 是加独立噪声的 Markov chain，故
data processing 给 \(\Delta_{c+1}\le\Delta_c\)。同时

\[
H(Z_c)=\sum_{j=1}^c\Delta_j.
\tag{20}
\]

于是 additive-quotient sharp converse 被压成：在不仅满足
\(\Delta_1\ge\Delta_2\ge\cdots\ge0\)，而且确实可由某个 commutative random walk
实现的 entropy-increment sequences 上，证明

\[
H_2(\operatorname{Pois}(\lambda))
+\sum_c p_c\sum_{j\le c}\Delta_j
\ge
C_*\lambda\left[p_0+
\sum_{c\ge1}p_c(1-2^{-\Delta_c})\right].
\tag{21}
\]

目前不能声称 (21) 只靠单调性成立；任意抽象单调 sequence 仍比 genuine convolution
entropy profiles 更宽。缺失的是一个 sharpened entropy-growth / sumset-growth
constraint，刻画哪些 \((\Delta_c)\) 能由有限 Abelian random walk 实现。

### 当前裁决

- 已得到任意 multi-label Abelian quotient 的解析 entropy--zero-certificate theorem
  (12)--(16)；
- 已严格否决 loadwise \(C_*\) inequality，给出 equality counterexample；
- 尚未找到违反 Poisson-aggregated (17) 的合法 additive quotient；
- 要证明 (17)，下一步应研究 random-walk entropy increments 的可实现域，而不是继续
  枚举小群。一个足够强的 Mrs-Gerber/Kneser 型 inequality 会关闭整个 commutative
  additive-quotient 路线；其反例则会直接给出超越 \(R_{\rm fp}\) 的构造蓝图。
