# Same-tape set-fiber shadows 与 nested deletion 的单预算定理

> 日期：2026-08-13。状态：严格 ordinary-filter theorem。它允许 arbitrary public
> tape、key-identity-dependent operations、history dependence、multiple
> representations、ghosts 和 nontransitive endpoint fibers。全文只比较同一 tape
> 上到达同一 physical state 的 histories，不使用跨 tape label collision。

主结论有两部分：

1. common deletion 把 endpoint set fiber 精确 transport 成 lower-section shadow，
   shadow union 必须包含在 successor accepted set 中；
2. 任意 nested deletion state transcript 由一个 initial \(H\)-bit state和已删除
   labels确定，所以全部 pivot states 只能收费一次。仅使用 shadow-union inclusion
   与 pointwise FPR 时，sharp universal entropy inequality仍止于静态
   \(n\log_2(1/\varepsilon)\) barrier；它不能单独推出 \(2.349083n\)。

## 1. Ordinary fixed-tape endpoint fibers

设 universe 为 \(U\)，\(|U|=u\)。filter 有 \(H\)-bit persistent memory和免费只读
public random tape \(R\)。固定一条 tape \(r\)、操作数 \(q\)、当前 set size \(k\)
和 physical state \(m\)。定义完整 endpoint fiber

\[
\mathcal F_r(m,k,q)
=\{S\in{U\choose k}:\text{存在长度 }q\text{ 的合法 history }h,
S(h)=S, M_r(h)=m\}.
\tag{1}

\]

这里同一个 \(S\) 可以有多个 histories/states；fiber 只记录在指定
\((r,m,k,q)\) 下存在的 logical endpoints。

对一个 ordered tuple \(\mathbf d=(d_1,\ldots,d_s)\) of distinct keys，写

\[
D=\{d_1,\ldots,d_s\}.
\]

定义 fiber 的 common-deletion section

\[
\mathcal F_r(m,k,q)[D]
=\{S\setminus D:S\in\mathcal F_r(m,k,q),\ D\subseteq S\},
\tag{2}

以及其 union shadow

\[
W_r(m,k,q;D)
=\bigcup_{T\in\mathcal F_r(m,k,q)[D]}T.
\tag{3}

\]

若 section 为空，则 \(W=\varnothing\)。

## 2. Exact common-deletion transport

### Theorem 2.1（same-tape lower-section shadow）

固定 \((r,m,k,q)\) 和 ordered deletion tuple \(\mathbf d\)。从 state \(m\) 依次
执行

\[
\operatorname{Delete}(d_1),\ldots,
\operatorname{Delete}(d_s)
\]

所得 physical state 记为

\[
m_{\mathbf d}=D_{r,d_s}\cdots D_{r,d_1}(m).
\tag{4}

\]

则

\[
\boxed{
W_r(m,k,q;D)
\subseteq
\mathcal W_r(m_{\mathbf d},k-s,q+s)
\subseteq A_r(m_{\mathbf d}),
}
\tag{5}

其中 \(\mathcal W\) 是 successor state 的完整 endpoint union，\(A_r(m')\) 是
state \(m'\) 接受的 universe keys。

**证明。** 取任意
\(x\in W_r(m,k,q;D)\)。存在 \(S\in\mathcal F_r(m,k,q)\) 满足
\(D\subseteq S\)、\(x\in S\setminus D\)，以及一条 witness history \(h_S\)
在同一 tape \(r\) 上到达 state \(m\) 和 logical set \(S\)。因为
\(D\subseteq S\)，按 \(\mathbf d\) 删除在该 witness world 中每一步都合法。
filter transitions在固定 tape 上 deterministic，所以 \(h_S\mathbf d\) 到达
同一个 state \(m_{\mathbf d}\)，logical endpoint 为 \(S\setminus D\)，仍含
\(x\)。故 \(x\) 属于 successor endpoint union。zero false negatives 再给第二个
inclusion。\(\square\)

该证明允许 update读取完整 tape和 key identity；比较的所有 worlds共享同一
\(r\)、同一 physical state \(m\) 与同一 concrete delete sequence。

### Corollary 2.2（nested semigroup action）

若

\[
D_0=\varnothing\subset D_1\subset\cdots\subset D_ell
\tag{6}

由一个 ordered deletion sequence 的 prefixes 产生，令 \(m_j\) 为从 \(m_0=m\)
删除 \(D_j\) 后的 state。则对每个 \(j\)，

\[
W_r(m,k,q;D_j)\subseteq A_r(m_j),
\tag{7}

且

\[
m_j=\Phi_{r,D_j}(m_0)
\tag{8}

是 \((r,m_0,D_j\text{ 的删除顺序})\) 的确定函数。

这里不声称 unordered sets \(D_j\) 的作用交换；正确对象是 free labeled deletion
semigroup在 state space 上的 action。不同删除顺序可有 holonomy，但不影响式
(7)--(8)。

## 3. Random nested deletion experiment

为把所有 layers用同一预算计费，进行如下只用于证明的 experiment：

1. 从 \({U\choose n}\) 均匀取 \(S\)；
2. 在 \(S\) 上均匀取一个随机排列
   \(X=(X_1,\ldots,X_n)\)；
3. 按一个预先固定的 canonical order 插入 \(S\)，得到 initial state \(M_0\)；
4. 依次删除 \(X_1,X_2,\ldots\)，令 \(M_j\) 为删除前 \(j\) 个 keys 后的 state。

\(S,X\) 与 public tape \(R\) 独立。每个 realization 都是一条 fixed合法 history，
所以可以逐 history 应用 pointwise FPR；随机 experiment 后面只用于 averaging。

令

\[
D_j=\{X_1,ldots,X_j\},
\qquad t_j=n-j.
\]

由 Theorem 2.1，actual remaining set \(S\setminus D_j\) 包含于 same-tape shadow
union

\[
W_j:=W_R(M_0,n,n;D_j)
\subseteq A_R(M_j).
\tag{9}

\]

特别地，下一个待删 key \(X_{j+1}\) 必属于 \(W_j\)。

## 4. 所有 pivot states 只占一个 H-bit budget

### Theorem 4.1（single-budget transcript theorem）

在上述 experiment 中，

\[
\boxed{
H(M_0,M_1,\ldots,M_n\mid R,X_1,ldots,X_n)
\le H.
}
\tag{10}

更强地，对任意 \(j\)，

\[
M_j=\Psi_j(R,M_0,X_1,ldots,X_j)
\tag{11}

为确定函数。因此 nested proof 不能把 \(H(M_j)\le H\) 对不同 \(j\) 相加；
整条轨迹的新持久信息只来自 \(M_0\)。

**证明。** 式 (11) 由依次应用 deterministic key-only delete transitions直接
得到。条件于 \((R,X)\)，transcript 是 \(M_0\) 的函数，故条件熵不超过
\(H(M_0\mid R,X)\le H\)。\(\square\)

这个结论精确关闭了 recursive/pivot arguments 中的重复收费风险。即使每层 state
看起来都有 \(H\) bits，也不能据此得到 \(\ell H\) 的信息预算。

## 5. Nested shadow entropy inequality

### Theorem 5.1（exact single-budget path inequality）

上述 random ordered set \(X=(X_1,ldots,X_n)\) 均匀分布在
\(U^{\underline n}\)，故

\[
H(Xmid R)=\log_2(u)_{\underline n}.
\]

same-tape shadows满足

\[
\boxed{
\log_2(u)_{\underline n}
\le
H+sum_{j=0}^{n-1}\mathbb E\log_2|W_j|.
}
\tag{12}

**证明。** Chain rule 给

\[
H(X\mid R)
\le H(M_0\mid R)
+\sum_{j=0}^{n-1}
H(X_{j+1}\mid R,M_0,X_1,ldots,X_j).
\]

条件于右侧信息，state \(M_j\) 由式 (11)确定，因而 full same-tape fiber shadow
\(W_j\) 也确定。式 (9) 给随机变量 \(X_{j+1}\) 的 conditional support 包含于
\(W_j\)，所以其条件熵至多 \(\log_2|W_j|\)。取期望并相加即得式 (12)。
\(\square\)

式 (12) 是 nested deletion fibers 的单预算熵不等式。每个 shadow layer 都参与，
但 state information \(H\) 只出现一次。

## 6. Pointwise FPR specialization

假设 filter 对每条 fixed合法 history、每个 fixed current nonmember 的 FPR 至多
\(\varepsilon\)。对一条 current size 为 \(t\) 的 fixed history，zero-FN 与
pointwise FPR 给

\[
\mathbb E_R|A_R(M)|
\le t+\varepsilon(u-t)
=:N_t.
\tag{13}

对随机 \((S,X)\) averaging 后仍成立。由 \(W_j\subseteq A_R(M_j)\)、Jensen
不等式和式 (12)，得到：

### Corollary 6.1（ordinary nested-shadow lower bound）

\[
\boxed{
H
\ge
\log_2(u)_{\underline n}
-\sum_{t=1}^{n}\log_2\bigl[t+\varepsilon(u-t)\bigr].
}
\tag{14}

若 \(u/n^2\to\infty\)，则

\[
H
\ge
n\log_2\frac1\varepsilon-o(n).
\tag{15}

在 \(\varepsilon=1/2\) 时只给

\[
H\ge n-o(n).
\tag{16}

**证明。** 对每个 \(j\)，

\[
\mathbb E\log|W_j|
\le\log\mathbb E|W_j|
\le\log N_{t_j}.
\]

代入式 (12) 即得式 (14)。当 \(u/n^2\to\infty\) 时，

\[
\log(u)_{\underline n}=n\log u-o(n),
\]

且 uniformly in \(t\le n\)，

\[
\log[t+\varepsilon(u-t)]
=\log(\varepsilon u)+o(1).
\]

相减得到式 (15)。\(\square\)

## 7. 为什么这个路线单独不能到 2.349083

式 (14) 不是证明技巧太松导致的偶然常数。仅知道

\[
W_j\subseteq A(M_j),
\qquad
\mathbb E|A(M_j)|\le N_{t_j}
\]

时，每层 entropy 上界 \(\log N_{t_j}\) 可以同时接近饱和。例如 exact
fingerprint-multiplicity states 的 same-tape fiber union在每个 layer都近似为
“当前出现 fingerprints 的全部 universe preimages”，其大小为
\(\varepsilon u+o(u)\)，而整条 deletion trajectory仍由 initial count vector和
deleted keys确定。对这类结构，式 (12)--(15) 只看见静态
\(n\log(1/\varepsilon)\) 信息，即使真实 fixed-state cost更高。

因此，多层 nested deletion 本身不会自动把静态 benchmark累加成更大的常数。
要超过 \(n\) bits，必须加入一个不只依赖 shadow union cardinality 的量，例如：

- reverse-transition multiplicity；
- 一个 accepted set在多少不同 deletion branches上可同时饱和；
- fiber lower sections之间的 joint intersection/transversal profile；
- 初始 state对整条随机删除排列的 conditional rank，而不只是每步 support size。

而且这些量必须与 Theorem 4.1 的 single \(H\)-bit budget联合收费，不能逐 pivot
state重复收费。

## 8. 对当前研究目标的裁决

本文严格完成了 arbitrary-filter、same-tape 层面的两件事：

1. full endpoint fiber在 common deletion 下的 exact lower-section shadow theorem；
2. 任意 nested deletion transcript 的 single-budget entropy inequality。

它同时给出一个重要 no-go：如果后续证明只使用 accepted-union inclusion、
pointwise FPR 的 accepted-size bound和“轨迹由 initial state确定”，那么最强直接
熵界就是式 (14)，在 half error 端只有 \(n-o(n)\)。因此这条接口不能单独升级
canonical \(2.349083\) converse。

要继续获得实质突破，下一目标必须是一个 **branching-sensitive same-tape
inequality**：同一个 initial state若在很多 nested deletion branches上都保持
\(|W_j|\approx\varepsilon u\)，则 reverse fibers或 transition transcript必须消耗
额外信息。该命题目前尚未证明；在完成前不能声称 arbitrary history-dependent
filters达到 \(2.349083n\)。
