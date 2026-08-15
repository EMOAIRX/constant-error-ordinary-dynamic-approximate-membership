# Algebraic threshold quotient：经审计的 ordinary dynamic AMQ 上界

> 日期：2026-08-13。状态：核心有限状态构造、zero-FN、任意长 history、有限 \(n\) pointwise FPR 公式和一阶状态计数已独立复核。完整 \(\varepsilon\)-curve、所有 threshold 的全局最优性及更一般群商 converse 仍在研究。

所有对数以 2 为底。

## 1. 主结论

在 KLZ 的 fixed-memory、免费公共随机带、无时间限制模型中，存在一个 ordinary、key-only、任意长历史的动态 approximate-membership filter，在

\[
\varepsilon=\frac12
\]

时使用

\[
\boxed{
H\le 2.349083440193\ldots\,n+o(n)
}
\]

bits。

它具有：

- zero false negatives；
- 对每条固定合法历史和每个固定当前非成员的 pointwise FPR；
- fixed worst-case persistent memory；
- 无 overflow 或 failure state；
- 无外部 exact set；
- 无 live-key enumeration；
- history-dependent 与 non-monotone ordinary API 完全允许。

该结果严格优于 exact multiplicity/all-compositions benchmark

\[
2.384499842479\ldots\,n+o(n).
\]

改进为

\[
0.035416402286\ldots\,n
\]

bits。

## 2. Block transducer

公共随机带给出独立 fully random maps

\[
g:U\to[B],
\qquad
h:U\to\{0,1\}.
\]

对 block \(j\)，令

\[
c_j=|\{x\in S:g(x)=j\}|,
\qquad
a_j=\sum_{x\in S:g(x)=j}h(x)\pmod{L+1}.
\]

持久状态是全部 pairs \((c_j,a_j)\) 的联合 enumerative rank，受约束

\[
\sum_jc_j\le n.
\]

更新为

\[
\operatorname{Insert}(x):
(c_j,a_j)\leftarrow(c_j+1,a_j+h(x)),
\]

\[
\operatorname{Delete}(x):
(c_j,a_j)\leftarrow(c_j-1,a_j-h(x)),
\]

其中 \(j=g(x)\)，第二坐标按模 \(L+1\) 运算。

查询 \(x\) 时：

1. \(c_j=0\)：返回 NO；
2. \(1\le c_j\le L\)：由于真实 one-count 位于 \([0,c_j]\subseteq[0,L]\)，residue 等于精确 one-count；查询相应 bit multiplicity 是否非零；
3. \(c_j>L\)：整块返回 YES。

### Zero-FN 与 deletion recovery

低负载时完整二元 multiset可从 \((c_j,a_j)\) 恢复；高负载时整块接受。因此成员永远回答 YES。

高负载时 residue 虽不服务当前 query，但仍随每次 deletion 作逆群更新。一旦负载重新降到 \(L\) 或以下，它自动等于剩余 keys 的精确 one-count。这个性质支持任意长历史，不产生 ghost，也不需要知道 block 内的 live keys。

## 3. 有限 \(n\) pointwise FPR

固定任意合法历史，其当前集合为固定 \(S\)，令 \(s=|S|\le n\)；固定非成员 \(x\notin S\)。

令

\[
C=|\{y\in S:g(y)=g(x)\}|
\sim\operatorname{Bin}(s,1/B).
\]

条件于 \(C=t\le L\)，query bit 与所有 \(t\) 个 member bits均不碰撞的概率为 \(2^{-t}\)。条件于 \(C>L\)，block 总是 false positive。因此精确 rejection probability 是

\[
\boxed{
\Pr[\operatorname{Query}(x)=\mathrm{NO}]
=
\sum_{t=0}^L
\binom st
\left(\frac1B\right)^t
\left(1-\frac1B\right)^{s-t}
2^{-t}.
}
\tag{1}
\]

该式随 \(s\) 非增，因此最坏情况在 \(s=n\)。选择 \(B\) 使式 (1) 在 \(s=n\) 时至少为 \(1-\varepsilon\)，即可得到有限 \(n\) pointwise guarantee。

若 \(n/B\to\lambda\)，式 (1) 收敛到

\[
e^{-\lambda}\sum_{t=0}^L\frac{(\lambda/2)^t}{t!},
\]

故极限 FPR 为

\[
\varepsilon_L(\lambda)
=1-e^{-\lambda}\sum_{t=0}^L\frac{(\lambda/2)^t}{t!}.
\tag{2}
\]

取比目标根小 \(o(1)\) 的 \(\lambda_n\)，即可吸收 finite-\(n\) rounding 且空间率只改变 \(o(1)\)。

## 4. Fixed-state rate

负载 \(t\) 的 local reachable-state 数为

\[
d_t=
\begin{cases}
t+1,&0\le t\le L,\\
L+1,&t>L.
\end{cases}
\]

其 ordinary generating function 为

\[
A_L(z)
=\sum_{t=0}^L(t+1)z^t
+(L+1)\frac{z^{L+1}}{1-z}.
\tag{3}
\]

全部 \(B\)-block states、总负载至多 \(n\) 的精确数量是

\[
[z^{\le n}]A_L(z)^B.
\]

令 \(B/n\to1/\lambda\)。标准正系数 saddle-point / tilted local-limit argument给

\[
\frac1n\log_2[z^{\le n}]A_L(z)^B
=
\frac1\lambda\log_2A_L(z_\lambda)-\log_2z_\lambda+o(1),
\tag{4}
\]

其中 \(z_\lambda\in(0,1)\) 唯一满足

\[
\frac{z_\lambda A_L'(z_\lambda)}{A_L(z_\lambda)}
=\lambda.
\tag{5}
\]

## 5. 参数 \(\varepsilon=1/2\)

对 \(L=2\)，式 (2) 的边界根为

\[
\lambda_2=1.325819075285\ldots.
\]

式 (5) 给

\[
z_{\lambda_2}=0.447778045429\ldots,
\]

代入式 (4)：

\[
\boxed{
R_2(1/2)
=2.349083440193\ldots.
}
\]

独立重算的相邻 thresholds 为：

| \(L\) | \(\lambda_L\) | rate |
|---:|---:|---:|
| 0 | 0.693147180560 | 2.384499842479 |
| 1 | 1.146193220621 | 2.372057541534 |
| 2 | 1.325819075285 | **2.349083440193** |
| 3 | 1.375441246548 | 2.360295858677 |
| 4 | 1.384796914431 | 2.372835928750 |
| 5 | 1.386123748662 | 2.379535046200 |
| 6 | 1.386277678745 | 2.382463602726 |

这证明 \(L=2\) 优于这些相邻值；尚未在本文中证明它对所有整数 \(L\) 全局最优。

## 6. 一般有限群 formulation

令内 hash alphabet嵌入有限阿贝尔群 \(G\)：

\[
V=\{v_a:a\in[K]\}\subseteq G.
\]

block 保存

\[
(c,s),\qquad s=\sum v_{h(x)}\in G.
\]

在负载 \(c\) 时，reachable syndrome set是 sumset \(cV\)。Zero-FN 所允许的最小 accepted rule 为：

\[
\boxed{
\text{query symbol }a\text{ 接受}
\iff
s-v_a\in(c-1)V.
}
\tag{6}
\]

因此：

- local state 数由 \(|cV|\) 决定；
- query distortion由 random-walk sum落入 translate \(v_a+(c-1)V\) 的概率决定；
- insert/delete 是群加减，自动形成跨所有 occupancy layers 的 right congruence。

这把 construction class 的优化化为

\[
\text{Cayley sumset growth}
\quad\text{vs}\quad
\text{random-walk query distortion}.
\]

小 doubling降低 state count，但 sumset更快饱和、FPR上升；Sidon 型增长保留 rejection，却增加 local states。

对 \(|G|\le10,K\le5\) 的穷举中，最优仍是

\[
G=\mathbb Z_3,\qquad V=\{0,1\},
\]

即上面的 \(L=2\) construction。该有限枚举不是一般最优性证明。

## 7. 论文价值与剩余门槛

已经严格建立的是：

> Ordinary lossy dynamics 可以在 fixed-state、任意长 history 模型中严格击穿 exact multiplicity rate。

这否定了“key-only deletion 必然要求精确维护全部 multiplicities”的自然猜测，并给出了一个明确机制：当前不可查询的群 residue可以作为未来低负载恢复所需的可逆信息。

要形成含金量更高的论文，还需要至少一项：

1. 给出完整的 \(R_{\rm alg}(\varepsilon)\) 相图；
2. 证明 \(\mathbb Z_3,\{0,1\}\) 在某个自然的有限阿贝尔群 quotient 类内最优；
3. 用 Kneser、Cauchy--Davenport 或 additive-energy工具给出 matching restricted converse；
4. 构造更强的多尺度 quotient，显著低于 \(2.349083\)；
5. 将信息论构造实现为高效 word-RAM filter。

在完成上述强化前，它是一个真实的新 upper-bound primitive，而不是 KLZ 常数误差开放问题的完整答案。
