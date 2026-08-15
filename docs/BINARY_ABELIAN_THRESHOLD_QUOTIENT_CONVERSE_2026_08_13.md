# 二符号 Abelian accumulator 的完整分类与最优性

> 日期：2026-08-13。状态：结构 converse 与全整数 threshold 最优性已证。
> 结论把 algebraic threshold quotient 从一个构造提升为 natural algebraic class
> 内的 sharp theorem：在 (arepsilon=1/2) 时，任意 finite Abelian group、
> 任意两个 symbol increments 和 minimal one-sided query rule 的最优 fixed-state
> rate 都由 order-(3) difference 实现，即 (L=2)，常数为
> (2.349083440193\ldots) bits/key。

## 1. 模型

公共随机 outer hash 把 keys 均匀分到 (B) 个 blocks。独立 inner hash 把
每个 key 均匀映射到两个 symbols (0,1)。固定有限 Abelian group (G) 和
increments

\[
v_0,v_1\in G.
\]

每个 block 保存

\[
(c,a),
\qquad
a=\sum_{x\text{ in block}}v_{h(x)}\in G,
\tag{1}
\]

其中 (c) 是 block load。Insert/Delete 对 (a) 加减相应 increment。

query rule 只读 ((c,a)) 与 query symbol (b\in\{0,1\})，必须满足 zero
false negatives。为最小化 FPR，可无损地取 **minimal one-sided rule**：当且
仅当存在一个与 ((c,a)) 相容、且包含 symbol (b) 的 size-(c) multiset 时
回答 YES。任何额外 YES 只增大 FPR而不减少 state space。

只枚举 reachable local states；(G) 中永远不可达的 elements 不计入 rate。

## 2. 一切二符号 Abelian accumulator 都是 threshold quotient

令

\[
d=v_1-v_0,
\qquad
q=\operatorname{ord}(d)\in\{1,2,\ldots\}.
\tag{2}
\]

给定 load (c)，若 block 内 one-count 为 (k\in\{0,\ldots,c\})，则

\[
a=cv_0+kd.
\tag{3}
\]

所以平移掉已知的 (cv_0) 后，state 只记录 (k\pmod q)。

### Theorem 1（结构分类）

若 (q\ge2)，则：

1. 当 (0\le c<q) 时，map (k\mapsto kd) 在
   (\{0,\ldots,c\}) 上 injective，state 精确恢复 one-count (k)；
2. 当 (c\ge q) 时，对每个 reachable residue，至少存在一个相容 multiset
   包含 symbol (0)，也至少存在一个相容 multiset 包含 symbol (1)；因此
   minimal one-sided rule 对两个 query symbols 都回答 YES；
3. load (c) 的 reachable local state 数为
   \[
   d_c=\min\{c+1,q\};
   \tag{4}
   \]
4. local OGF 恰为
   \[
   \boxed{
   A_q(z)=\sum_{c=0}^{q-1}(c+1)z^c
   +q\frac{z^q}{1-z}
   =\frac{1-z^q}{(1-z)^2}.
   }
   \tag{5}
   \]

证明。第一项由 (d) 的 order 为 (q)。对第二项，固定 residue
(r\in\{0,\ldots,q-1\})。当 (c\ge q) 时，总能在 ([0,c]) 中选择
(k\equiv r\pmod q)。若 (r\ne0)，可取 (1\le k\le q-1\le c-1)，该
multiset 同时含两种 symbols。若 (r=0)，(k=0) 给纯 zero multiset，
(k=q) 给含 one 的 multiset；并且 (k=q\le c)。若 (c=q)，后者可能是纯
one，但与 (k=0) 一起仍迫使两个 query symbols 均被接受。(c>q) 更直接。
第三项是 residues 数，第四项求和化简。

若 (q=1)，两个 increments 相同，任意非空 block 必须对两个 symbols 都
回答 YES；这是退化且更差的 outer occupancy filter，可单独排除。

### Corollary 2

任意 finite Abelian (G) 与两个 increments 的 reachable quotient 只取决于
(q=\operatorname{ord}(v_1-v_0))，并与 threshold (L=q-1) 的构造完全
等价。使用非循环群、扩大 (G)、改变 (v_0)，或保留额外不可达 group
elements都不能改善 rate/FPR tradeoff。

## 3. FPR 与 rate

令 outer load 极限为 (lambda=n/B)。由 Theorem 1，fixed nonmember 的
极限 FPR 为

\[
\varepsilon_q(\lambda)
=1-e^{-\lambda}
\sum_{t=0}^{q-1}\frac{(\lambda/2)^t}{t!}.
\tag{6}
\]

令 (lambda_q) 是 (arepsilon_q(lambda_q)=1/2) 的唯一正根。

对 fixed (lambda)，定义 class rate

\[
\mathcal R_q(\lambda)
=\min_{0<z<1}
\left\{
\frac1\lambda\log_2 A_q(z)-\log_2z
\right\}.
\tag{7}

minimum 的唯一 saddle 满足

\[
\lambda
=\frac{zA_q'(z)}{A_q(z)}
=\frac{2z}{1-z}-\frac{qz^q}{1-z^q}.
\tag{8}

目标 rate 是

\[
R_q=\mathcal R_q(\lambda_q).
\tag{9}

式 (7) 是全状态 fixed-memory rate，而非平均 entropy。

## 4. (q=3) 对全部整数 (q) 全局最优

### Lemma 3（两个单调性）

1. 对 fixed (q)，(mathcal R_q(\lambda)) 随 (lambda) 严格下降；
2. 对 fixed (lambda)，(mathcal R_q(\lambda)) 随整数 (q) 严格增加。

证明。对第一项，用 envelope theorem 对 (7) 在其 interior unique minimizer
(z=z_q(\lambda)) 处求导：

\[
\frac{d}{d\lambda}\mathcal R_q(\lambda)
=-\frac{\log_2A_q(z_q(\lambda))}{\lambda^2}<0.
\tag{10}
\]

对第二项，(0<z<1) 时

\[
A_{q+1}(z)-A_q(z)=\frac{z^q-z^{q+1}}{(1-z)^2}
=\frac{z^q}{1-z}>0.
\tag{11}
\]

所以 (7) 中每个 (z) 的 objective 随 (q) 严格增加，取 minimum 后仍不减；
strictness 可由 minimizer 代入反向比较得到。

### Lemma 4（load 上界）

对每个 finite (q)，

\[
\lambda_q<\lambda_\infty:=2\ln2.
\tag{12}
\]

证明。令 (q\to\infty)，(6) 的 complement趋于

\[
e^{-\lambda}\sum_{t\ge0}\frac{(\lambda/2)^t}{t!}
=e^{-\lambda/2}.
\]

其 (1/2)-root 为 (2\ln2)。对 finite (q)，partial sum严格小于 full
exponential，所以在相同 (lambda) 下 FPR 严格更大；为保持 FPR (1/2)，
必须取更小的 (lambda_q)。

### Theorem 5（sharp binary-Abelian converse at (1/2)）

在 Section 1 的全部二符号 finite-Abelian accumulator 类中，最小 fixed-state
rate 由

\[
q=3
\qquad(L=2)
\]

唯一实现，并等于

\[
\boxed{
R_{m bin-Ab}
=2.349083440193141\ldots\text{ bits/key}.
}
\tag{13}

证明。直接计算 (q=2) 给

\[
R_2=2.372057541534090\ldots>R_3.
\tag{14}
\]

对任意 (q\ge4)，Lemmas 3--4 给

\[
\begin{aligned}
R_q
&=\mathcal R_q(\lambda_q)\\
&>\mathcal R_q(2\ln2)\\
&\ge\mathcal R_4(2\ln2)\\
&=2.351275266054009\ldots\\
&>2.349083440193141\ldots=R_3.
\end{aligned}
\tag{15}

所以只需两个数值比较，不需要无限枚举 thresholds。

## 5. 数值认证接口

Theorem 5 的结构部分完全解析。正式稿应对下面三个一维根给 interval
certificate：

\[
\lambda_2\in
[1.1461932206205,1.1461932206207],
\]

\[
\lambda_3\in
[1.3258190752851,1.3258190752853],
\]

以及 (q=3) 的 saddle

\[
z_3\in
[0.4477780454288,0.4477780454291].
\]

对 barrier (\mathcal R_4(2\ln2))，saddle 位于

\[
z\in[0.4339705040579,0.4339705040582].
\]

在这些 rational decimal intervals 上用 directed rounding 检查端点符号，再
对 (7) 作 interval evaluation，即可认证式 (14)--(15) 至少有
(10^{-3}) 的宽裕 margin。这里不需要高精度 symbolic root formula。

## 6. 定理边界

Theorem 5 覆盖：

- 任意 finite Abelian group；
- 任意 two increments；
- exact group accumulator updates；
- minimal one-sided query；
- uniform binary inner hash；
- arbitrary outer blocks 与 fixed-state enumerative coding。

它不覆盖：

- biased inner symbols；
- (K>2) symbols；
- 一个 key 同时更新多个 accumulators；
- nonlinear local automata；
- query-dependent sketches；
- low-load 也允许 lossy merge 的 quotient。

所以正确标题是“binary Abelian accumulator class-optimal”，不是 ordinary AMQ
全局最优。

## 7. Paper taste

这个 converse 显著增强原单点构造：

1. 解释了 threshold 不是人为 design choice，而是所有二符号 Abelian
   accumulators 的必然 normal form；
2. 用 group element order (q) 完整分类空间/FPR tradeoff；
3. 解析证明 (q=3) 对无限整数 family 全局最优；
4. 与 construction 一起形成 matching restricted upper/lower theorem。

作为论文 package，它比“改善 (0.0354) bits/key”更有含金量。若再加入完整
(arepsilon)-curve（不同 (q) 的相变区间）以及 (K>2) 的 Kneser/Sidon
推广，会形成一篇有明确代数主题的 SODA candidate。仅有 binary theorem 时，
更稳妥的判断是：已经足够成为严谨 paper 的核心结果，但 venue 强度取决于
generalization 与 literature priority audit。

