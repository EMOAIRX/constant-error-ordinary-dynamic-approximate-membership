# Depth-2 fresh insertion：single-budget 精确界与 spectral-leakage no-go

> 日期：2026-08-13。状态：本文件中的有限下界与 hash-count 上界均为严格
> 结论。它们裁决的是从空集，或从一个固定公开集合开始的两次 fresh insertion；
> 不把该结论外推为一般多层动态 filter 定理。

所有对数以 (2) 为底。令 (u=|U|)。

## 1. 最小 right-congruence 模型

固定一条 deterministic public tape。结构从空状态开始，依次接收两个不同
labels (x,y)。第一层状态为

\[
c(x)=\Delta(m_0,\operatorname{Insert}(x)),
\]

第二层状态为

\[
d(x,y)=\Delta(c(x),\operatorname{Insert}(y)).
\]

因此 (c(x)=c(x')) 强迫

\[
d(x,y)=d(x',y)
\]

对每个同时合法的 (y) 成立。这正是 labeled-successor congruence；不假设
history independence，所以一般不要求 (d(x,y)=d(y,x))。每个物理状态的
YES-set必须包含到达该状态的所有 path labels。

随机 filter 是上述 deterministic transducers 的任意 public-tape 混合。它有
至多 (q=2^H) 个 persistent states，并对每个固定 ordered pair ((x,y))
和固定 (z\notin\{x,y\}) 满足 pointwise FPR 至多 (arepsilon)。

## 2. Single-budget 下界

### Theorem 1

任意上述 depth-2 filter 满足

\[
\boxed{
H\ge
\log (u)_{\underline 2}
-\log\Bigl[(2+\varepsilon(u-2))(1+\varepsilon(u-2))\Bigr].
}
\tag{1}
\]

特别地，当 (u\to\infty) 而 (arepsilon) 固定时，

\[
\boxed{H\ge 2\log(1/\varepsilon)-o_u(1).}
\tag{2}
\]

这里没有把第一层和第二层的 state entropy 相加；只对最终物理状态收取一次
(H)-bit budget。

### Proof

令 ((X,Y)) 是从 (U^{\underline 2}) 均匀抽取的 ordered distinct pair，
(R) 是 public tape，(M=M_R(X,Y)) 是最终状态。对固定 (R=r,M=m)，
记 query YES-set 为 (A_r(m))，大小为 (a_r(m))。zero false negative说明：
所有映到 (m) 的 ordered pairs 都属于 (A_r(m)^{\underline 2})。故

\[
H(X,Y\mid R,M)
\le \mathbb E\log (a_R(M))_{\underline 2}.
\tag{3}
\]

另一方面，pointwise FPR逐历史求和给

\[
\mathbb E[|A_R(M)|\mid X=x,Y=y]
\le 2+\varepsilon(u-2).
\tag{4}
\]

再对均匀 ((X,Y)) 平均，右侧不变。函数

\[
f(a)=\log(a(a-1)),\qquad a\ge2,
\]

满足 (f''(a)<0)。由 Jensen、(H(M\mid R)\le H) 以及 chain rule，

\[
\begin{aligned}
\log(u)_{\underline2}
&=H(X,Y\mid R)\\
&\le H(M\mid R)+H(X,Y\mid R,M)\\
&\le H+
\log\Bigl[(2+\varepsilon(u-2))(1+\varepsilon(u-2))\Bigr].
\end{aligned}
\]

移项即得 (1)。

## 3. 满足完整 transition congruence 的 matching upper bound

### Theorem 2

令 (B) 满足

\[
1-(1-1/B)^2\le\varepsilon.
\tag{5}
\]

存在支持任意两次 fresh insertion 的 ordinary transducer，使用

\[
\boxed{
H\le\left\lceil\log\binom{B+2}{2}\right\rceil
}
\tag{6}
\]

bits，并有 zero false negatives和 pointwise FPR至多 (arepsilon)。当
(arepsilon\to0) 时，

\[
H\le2\log(1/\varepsilon)+O(1).
\tag{7}
\]

### Construction and proof

public tape选择 fully random hash (h:U\to[B])。状态是总质量至多 (2) 的
(B)-维 nonnegative count vector。这样的向量共有

\[
\sum_{j=0}^2\binom{B+j-1}{j}=\binom{B+2}{2}.
\]

执行 `Insert(x)` 时增加 coordinate (h(x))。query (z) 当且仅当对应
coordinate为正时回答 YES。更新只依赖当前 count vector 和 label，故这是
一个真正的 labeled deterministic transducer，不是独立选择的两层静态编码。

对固定 distinct history ((x,y)) 和固定非成员 (z)，fully random hash给

\[
\Pr[h(z)\in\{h(x),h(y)\}]
=1-(1-1/B)^2\le\varepsilon.
\]

这证明所有保证。特别地，第一层 partition、第二层 successor maps 与 query
fibers来自同一个 right congruence。

## 4. 固定公开起始集合不会改变结论

若起点是固定且双方公开的 (S_0)，结构可对 (S_0) 永久回答 YES，并只对
两个 fresh additions保存上述 count vector。查询域限制到 (U\setminus S_0)
后，Theorems 1--2 原样成立。

如果 (S_0) 本身是隐藏输入，则它的静态表示成本已经进入初始 state。此时
只观察随后两次 insertion，不能把初始集合的静态成本误称为 depth-2 transition
leakage；要发现动态附加项，必须联合比较很多起始 fibers 或很多 consecutive
layers。

## 5. 对 spectral-leakage 路线的裁决

Theorems 1--2说明：最小 depth-2 模型只恢复二元素 Carter 项，并且
transition-compatible hash-count fibers在常数项内达到它。由此得到三个严格
边界。

1. 只使用一个起点后的两个 fresh labels、最终 accepted support 和 labeled
   successor congruence，不能推出随全局 capacity (n) 线性增长的动态附加项。
2. 把两个局部 transition entropies相加会重复收费；正确的 single-budget
   论证退化为最终 state 的静态编码不等式 (1)。
3. 任意声称“right congruence 本身迫使高阶 Johnson 信息在 depth 2 产生正的
   线性 leakage”的命题，必须加入跨许多起点或许多层共享同一 state budget的
   假设；否则 Theorem 2 是直接反例。

这不否决 multi-layer spectral leakage。它说明最小有希望的对象至少应包含：

- θ(n) 个随机 initial-set coordinates 或 θ(n) 个 consecutive updates；
- 同一个 tape 上的 joint state profile，而非逐层 entropy之和；
- 防止 global hash/count certificate在全部局部实验间共享成本的直接和机制。

## 6. 与有限宇宙 replacement 的关系

在 (U=[2n])、当前集合大小 (n) 的 replacement 问题中，真正的压力来自
对整个 Johnson graph 的长期 labeled compatibility。只检查一条 path上的两个
fresh additions既没有保持容量，也看不到 Johnson cycles。因此 depth-2 fresh
模型不能为 conjectured (n)-bit replacement lower bound提供证据。

若要使用最小实例杀伪，应改成 replacement square：从同一个 (n)-set出发，
比较两个不同 swap labels 及其 reverse continuations，并对所有起点同时收费。
即便如此，two-step commutator本身不受 FPR约束；必须联合 endpoint fiber union
或 reverse-fiber support。单纯比较两条操作次序是否到达同一状态仍然无效。

## 7. Taste 判断

式 (1) 是干净的 single-budget finite theorem，但本质上属于静态 Carter编码，
不够独立投稿。真正有价值的产出是 no-go：它排除了把普通动态突破压缩成一个
孤立 depth-2 successor inequality的路线。

下一步若继续 spectral方向，应直接研究 multi-origin depth-2 functional，或
depth-θ(n) 的 joint right-congruence functional。若仍只得到局部 pairwise
collision、commutator或逐层 entropy项，应停止，因为这些量已经被上述
hash-count transducer完整吸收。
