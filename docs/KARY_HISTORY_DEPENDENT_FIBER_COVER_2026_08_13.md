# 一般 K-symbol history-dependent summary 的 relational fiber-cover 界

> 日期：2026-08-13。状态：fiber-cover inequality 为严格有限定理，不假设
> canonical、lattice、history independence 或 delete inverse。(c=2,3) 的小
> alphabet 表为 exact finite optimization；一般 closed form 仍是 covering-design
> 问题。

## 1. 模型与固定历史

考虑任意 deterministic local transducer。每个 key 有独立均匀 label
(h(x)\in[K])。机器支持合法 insert/delete，zero false negatives，并显式知道
当前 load。允许同一 multiset 有多个 states、不同 multisets 共享 state，以及
任意 history dependence。

固定 (c) 个不同 keys (x_1,\ldots,x_c)，并固定 history

\[
H_c=\operatorname{Insert}(x_1),\ldots,\operatorname{Insert}(x_c).
\]

每个 label word (w\in[K]^c) 确定一个最终 state (f(w))。设这条固定 history
可到达至多 (d) 个 states。

## 2. Exact fiber-cover functional

对 fiber (F_s=f^{-1}(s))，定义 support union

\[
A_s=\bigcup_{w\in F_s}\operatorname{supp}(w)\subseteq[K].
\]

zero false negatives 强迫 state (s) 接受每个 (a\in A_s)。因此 fresh uniform
query 的 rejection 至多

\[
1-\frac1{K^{c+1}}\sum_s|F_s||A_s|.
\tag{1}
\]

定义 universal cover cost

\[
\mathsf C_{K,c}(d)
=\min_{\substack{r\le d\\A_1,\ldots,A_r\subseteq[K]}}
\sum_{w\in[K]^c}
\min_{j:\operatorname{supp}(w)\subseteq A_j}|A_j|,
\tag{2}
\]

其中若某个 word 无可用 (A_j)，该 family 不可行。

### Theorem 2.1（general relational fiber-cover inequality）

对任意上述 history-dependent transducer，

\[
\boxed{
\operatorname{Rej}(H_c)
\le1-\frac{\mathsf C_{K,c}(d)}{K^{c+1}}.
}
\tag{3}

而且式 (3) 作为单层、单历史命题是 sharp 的。

**证明。** 取机器实际 fibers (F_s) 及其 (A_s)。每个 word (w\in F_s)
满足 (operatorname{supp}(w)\subseteq A_s)，故

\[
\sum_s|F_s||A_s|
\ge
\sum_w\min_{s:\operatorname{supp}(w)\subseteq A_s}|A_s|
\ge\mathsf C_{K,c}(d).
\]

结合式 (1) 得式 (3)。反之，给定式 (2) 的 family，把每个 word 分配给包含其
support 且 cardinality 最小的 (A_j)，并让对应 state 恰接受 (A_j)，即可在
这个单层静态 relation 上取等号。该 equality construction 不自动给出跨层动态
transducer，所以 sharpness 只针对定理声明的单层范围。证毕。

## 3. Support-poset / covering-code 重写

令

\[
N_{K,c}(S)
=\#\{w\in[K]^c:\operatorname{supp}(w)=S\}
=|S|!\,\mathrm S(c,|S|),
\tag{4}

其中 (mathrm S(c,t)) 是第二类 Stirling 数。则

\[
\boxed{
\mathsf C_{K,c}(d)
=\min_{|\mathcal A|\le d}
\sum_{\substack{S\subseteq[K]\\1\le|S|\le c}}
|S|!\mathrm S(c,|S|)
\min_{A\in\mathcal A:S\subseteq A}|A|.
}
\tag{5}

这是一类 weighted upward-covering code：support poset 的每个 (S) 必须由某个
superset center (A) 覆盖，代价是 (|A|)，weight 是产生该 support 的 words
数。它与 ordinary set cover 不同，因为 centers 可重叠，而每个 demand 只支付
最便宜 center。

式 (5) 是一般 (K) 的精确 relational fiber-cover inequality。Sperner/LYM
可以用于限制固定 cardinality centers 的覆盖能力；但 heterogeneous center sizes
使完整 closed form 等价于一个非平凡 covering-design optimization。

## 4. (c=2) 的精确小 alphabet frontier

此时 singleton support 的 weight 为 (1)，pair support 的 weight 为 (2)。
对 (K=3)：

| states (d) | (mathsf C_{3,2}(d)) | maximal rejection |
|---:|---:|---:|
| 1 | 27 | (0) |
| 2 | 23 | (4/27) |
| 3 | 18 | (1/3) |
| 4 | 17 | (10/27) |
| 5 | 16 | (11/27) |
| 6 | 15 | (4/9) |

这里 (d=3) 的最优 centers 是三个 two-subsets；每个 singleton 由两个 centers
覆盖，每个 pair 由自身 center 覆盖。(d=6) 使用三个 singleton 与三个 pairs，
达到 exact-support ceiling (4/9)。

对 (K=4)，前几项为：

| (d) | maximal rejection |
|---:|---:|
| 1 | (0) |
| 2 | (9/64) |
| 3 | (20/64) |
| 4 | (26/64) |
| 5 | (28/64) |
| 6 | (32/64) |
| 7 | (33/64) |
| 8 | (34/64) |
| 9 | (35/64) |

exact-support ceiling 为 ((3/4)^2=36/64)，需要全部 (K+{K\choose2}=10)
个 nonempty supports。

这些值比 lattice 五点定理允许更多中间点，因为一般 history-dependent fibers
不要求 equivalence relation 跨 histories 或 layers 具有 additive closure。

## 5. (c=3) 的精确小 alphabet frontier

此时 size-(1,2,3) supports 的 word weights分别为 (1,6,6)。对 (K=3)：

| (d) | (mathsf C_{3,3}(d)) | maximal rejection |
|---:|---:|---:|
| 1 | 81 | (0) |
| 2 | 73 | (8/81) |
| 3 | 66 | (15/81) |
| 4 | 60 | (21/81) |
| 5 | 59 | (22/81) |
| 6 | 58 | (23/81) |
| 7 | 57 | (24/81=8/27) |

最后一项使用全部七个 nonempty supports，并达到 exact-support ceiling
((2/3)^3=8/27)。

对 (K=4)，(d=1,\ldots,9) 的 maximal rejection 依次为

\[
0,
\frac{27}{256},
\frac{46}{256},
\frac{64}{256},
\frac{72}{256},
\frac{80}{256},
\frac{86}{256},
\frac{92}{256},
\frac{98}{256}.
\]

## 6. Common-deletion projection

单层 cover bound 还可通过共同删除传播。若两个 words (u,v\in[K]^c) 位于同一
fiber，并存在坐标集合 (Tsubseteq[c])，使保留 (T) 后的 subwords supports
分别为 (B_u,B_v)，则从相同 physical state 执行同一列“删除 ([c]\setminus T)
中的 key” transitions，最终 state 必须同时接受

\[
B_u\cup B_v.
\tag{6}

这是一般 (K) common-deletion lemma。特别地，若 (u,v) 是 composition poset
中一条 chain 上的两个适当编码点，可选择 (T) 放大 support symmetric
difference。binary monotone-chain lemma正是 (B_u=\{0\},B_v=\{1\}) 的特例。

但一般 (K) 不存在一条长度等于全部 composition 数的 chain；单一 Sperner
chain collision只能给局部 witness。要把式 (6) 与式 (5) 组合成跨层 sharp
tradeoff，需要设计一个 chain decomposition，使每个 fiber 的多次 common-
deletion witnesses 不被重复收费。这是当前未闭合的部分。

## 7. 结论边界

严格得到的是：

1. 不带 canonical/lattice 假设的一般 (K) exact fiber-cover functional；
2. (c=2,3) 的 sharp small-alphabet单层 frontiers；
3. 任意 fiber collision 的 common-deletion support-union传播 lemma。

它尚未给出全局 ordinary filter lower bound。原因与 binary 版本相同：坏 local
fiber 是在 keys 已落入同一 block 后识别的，而 pointwise FPR 只允许选择与公共
outer hash tape 独立的 fixed history。仍需 oblivious occupancy lifting，或一个
直接在全局 fixed histories 上建立的 product fiber-cover theorem。
