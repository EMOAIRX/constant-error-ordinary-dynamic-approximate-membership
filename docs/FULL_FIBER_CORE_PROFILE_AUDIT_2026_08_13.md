# Full-fiber transport 的 core profile 审计

> 日期：2026-08-13。状态：严格的局部结构 lemma，加上尚未证明的
> entropy--transport 研究方向。本文不声称改善 ordinary dynamic filter 的
> 已知空间下界。

## 1. 结论

只记录 fiber union 的 transport loss 时，

\[
O(tQ|W|/u)
\]

在一般 deterministic transducer 中不能改成更小的统一上界。达到该量级的
fiber 可以由两两不交的 \(t\)-sets 构成。因而
`ORDINARY_FIBER_UNION_LIFT_CANDIDATE_2026_08_13.md` 中要求
\(u/n^2\to\infty\) 并不只是选择单个 witness 导致的松弛；若证明只保留
\(|W|\)，这个 birthday scale 是真实的。

但 union 不是完整对象。精确的单步损失由 fiber 的 implication/core profile
决定。它提示一个可能更强的 rate--distortion 路线：联合收费 state 所保留的
endpoint 信息与 fiber 内的必然共现质量。

## 2. 精确单 insertion 公式

固定随机带、时间、集合大小和物理状态。令 endpoint fiber 为

\[
\mathcal F\subseteq {U\choose t},
\qquad
W=\bigcup_{S\in\mathcal F}S.
\]

对 \(x\in W\)，定义

\[
\mathcal F_x=\{S\in\mathcal F:x\in S\},
\qquad
C_x=\bigcap_{S\in\mathcal F_x}S.
\]

这里 \(C_x\) 是在该 fiber 内只要 \(x\) 出现就必然同时出现的 keys。

对 label \(y\) 执行一次 insertion。只保留 insertion 对其 endpoint 合法的
隐藏 worlds，得到

\[
\mathcal F^{(y)}=\{S\cup\{y\}:S\in\mathcal F, y\notin S\}.
\]

于是对任意 \(x\ne y\)，有精确等价

\[
x\notin\bigcup\mathcal F^{(y)}
\quad\Longleftrightarrow\quad
y\in C_x.
\tag{1}
\]

证明只是展开量词：右侧表示每个包含 \(x\) 的 witness 都已经包含 \(y\)，
所以没有一个 witness 可以合法执行 `Insert(y)`；反之，只要存在
\(S\in\mathcal F_x\) 且 \(y\notin S\)，该 world 合法并在 successor 中继续
包含 \(x\)。

若 \(Y\) 在 \(U\) 中均匀，则忽略 \(Y=x\) 的 API 边界项后，期望 union loss
恰为

\[
\mathbb E_Y\left|W\setminus\bigcup\mathcal F^{(Y)}\right|
=\frac1u\sum_{x\in W}(|C_x|-1).
\tag{2}
\]

对一个 insertion-label set \(I\)，相应的精确条件是

\[
x\text{ 被 transport 丢失}
\quad\Longleftrightarrow\quad
I\text{ hitting }\mathcal F_x,
\tag{3}
\]

即每个包含 \(x\) 的 endpoint witness 都与 \(I\) 相交。多步问题因此是 fiber
hypergraph 的 transversal profile，而不是独立 witness 的 union bound。

## 3. 为什么原来的 loss bound 是 tight 的

令

\[
\mathcal F=\{S_1,\ldots,S_K\},
\]

其中 \(S_i\) 是两两不交的 \(t\)-sets。则对每个 \(x\in S_i\)，唯一包含
\(x\) 的 endpoint 是 \(S_i\)，所以

\[
C_x=S_i,
\qquad |C_x|=t.
\]

由 (2)，

\[
\mathbb E_Y[\mathrm{loss}]
=\frac{Kt(t-1)}u
=\frac{(t-1)|W|}u.
\tag{4}
\]

这与任取一个 \(t\)-element witness 后所得的 \(t|W|/u\) 上界只差低阶项。
若 \(|W|=\Theta(u)\)、\(t=\Theta(n)\)，每个随机 insertion 已能造成
\(\Theta(n)\) 的 union loss；经过 \(Q\) 个 labels，粗粒度临界量自然是
\(nQ/u\)。

这种 fiber 也不是违反 ordinary semantics 的抽象集合族。一个确定性
belief-state transducer 可以把物理状态解释为 endpoint 候选族：query 接受其
union；`Insert/Delete` 先筛掉操作不合法的候选，再逐候选执行逻辑更新。
one-sidedness 自动成立。删除一个 matching block 内的 key 会把相关 subfiber
缩到单个 endpoint，说明高 conflict 可以由后续 exact recovery 支付。
这种 automaton 空间很差，不能作为新 upper bound；它只证明 union-only
transport inequality 已经到达正确量级。

## 4. implication preorder

定义

\[
x\preceq_{\mathcal F}y
\quad\Longleftrightarrow\quad
y\in C_x.
\tag{5}
\]

这是一个 preorder。每个 \(S\in\mathcal F\) 都是该 preorder 的
\(t\)-element upset。若 \(e_t(P)\) 表示 preorder \(P\) 的 \(t\)-element
upsets 数量，则必有

\[
|\mathcal F|\le e_t(P_{\mathcal F}).
\tag{6}
\]

两个端点说明了需要联合优化的量：

- 若 \(\mathcal F={W\choose t}\)，preorder 是 antichain，\(C_x=\{x\}\)，
  transport loss 为零，但 fiber entropy 最大；
- 若 \(\mathcal F\) 是不交 blocks，preorder 的强连通类正是这些 blocks，
  fiber 很薄，而 core loss 达到 (4)。

固定 common core 的 families 给出另一类压力测试：fiber 仍可指数大，但大量
implications 由一个共享 certificate 产生。因此不能把 comparable pairs 逐对
当作独立信息收费。

## 5. 真正缺失的强不等式

先有一个严格的单-fiber entropy--core inequality。令 (S) 在
(mathcal F) 中均匀，再条件于 (S) 从其 (t) 个成员中均匀抽取 (X)。
给定 (X=x) 后，(S) 必须包含 (C_x)，故

\[
H(S\mid X=x)
\le
\log { |W|-|C_x| \choose t-|C_x|}.
\tag{7}
\]

另一方面，

\[
H(S,X)=\log|\mathcal F|+\log t
=H(X)+H(S\mid X),
\]

且 (H(X)\le\log|W|)。所以

\[
\boxed{
\log|\mathcal F|
\le
\log\frac{|W|}{t}
+\mathbb E_X
\log { |W|-|C_X| \choose t-|C_X|}.
}
\tag{8}
\]

对 fiber 上任意 endpoint 分布，同一证明把左侧换成 (H(S))。这严格表达
了“thin/high-conflict fiber 必须由 endpoint 信息支付”。但是它不能直接替换
full-union transport bound：式 (2) 按 union keys 不加权求和，而 (8) 中

\[
\Pr[X=x]=\frac{|\mathcal F_x|}{t|\mathcal F|}
\]

按 endpoint incidence 加权。一个 fiber 可以由一个极厚的主 family 加上许多
degree-one 的稀有 witnesses 组成。稀有 witnesses 对 endpoint entropy 几乎无
影响，却能显著扩大 union 及其 transport loss。这一 rare-witness gap 不能靠
Jensen 或 Shearer 直接消除；需要 pointwise FPR、多个预先固定 histories 或
一个 seed-independent averaging argument共同参与。

值得尝试的不是继续改进 (10) 的 union bound，而是证明一个
entropy--comparability inequality，并在所有 states 上只支付一次 memory
budget。抽象目标为：对随机 endpoint \(S\) 和 state \(M\)，联合控制

\[
I(S;M)
\quad\text{与}\quad
\mathbb E_M\sum_{x\in W(M)}(|C_x(M)|-1),
\tag{9}
\]

或更一般的 multi-insertion transversal functional。直观上：

- thin fibers 由 \(I(S;M)\) 支付；
- thick fibers 的 cores 小，因而可近乎无损 transport；
- shared cores 和 frozen certificates 必须只收费一次。

若能把 (6)、(8) 的 extremal upper bound与

\[
H(S)=I(S;M)+H(S\mid M)
\]

结合，并沿 KLZ obfuscation transcript 保持单一 \(H\)-bit budget，就有机会在
不要求 \(u/n^2\to\infty\) 的情况下得到新的普通模型下界，甚至改善单副本
fixed-error 常数。当前没有这样的定理，因此这部分只能标为研究方向。

## 6. 对 full-fiber lift 的审计结论

目前未找到以下接口的具体反例：

1. time-indexed full fiber 对 horizon 的处理；
2. \(G_{k-1}\to G_k\) 与 \(G_\ell\to F_r\) 的 self-contained suffix
   合法性；
3. Claim 4.7 的 operational-history distribution identity 对
   \((M,t,q)\mapsto|\mathcal W(M,t,q)|\) 的迁移；
4. 条件于完整 \(\sigma,R\) 后，partition-free \(\mathcal W\) 在 Claim 4.6
   中成为固定集合。

因此 hostile verdict 不是“已找到反例”，而是：现有 full-fiber lift 在
\(u/n^2\to\infty\) 的范围内值得继续逐行形式化；其 transport loss 在只使用
union profile 的证明中已经基本 tight。若要获得更强结论，必须引入 fiber
thickness/core/transversal 的联合信息量，而不能只优化常数。
