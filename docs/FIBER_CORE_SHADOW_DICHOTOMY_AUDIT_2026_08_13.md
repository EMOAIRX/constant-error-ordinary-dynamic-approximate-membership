# Fiber core、随机右同余与 Johnson-shadow 障碍

> 日期：2026-08-13。状态：本文中的 core inequality、(q)-shadow theorem 和
> rare-witness counterexample 已证。它们给出一个可复用的 ordinary dynamic
> automata 接口，但也严格否决了“只由单个 fiber 的大小推出低 transport loss”
> 的研究路线。

## 1. 抽象设置

令 (U) 是大小为 (u) 的宇宙，

\[
\mathcal F\subseteq\binom Un
\]

是某个 fixed-tape physical state 的 endpoint fiber。对每个
(x\in W(\mathcal F):=\bigcup_{S\in\mathcal F}S)，定义 section 和 core

\[
\mathcal F_x=\{S\in\mathcal F:x\in S\},
\qquad
C_x=\bigcap_{S\in\mathcal F_x}S,
\qquad
c_x=|C_x|.
\tag{1}
\]

若 (x\notin W(\mathcal F))，约定 (c_x=\infty)。

考虑从这个 state 执行一个由 (q) 个 distinct insert labels 组成的 suffix，
其 label set 为 (Y\in\binom Uq)。只看由 (mathcal F) 中替代 histories 产生
的 transported fiber。一个 (x\in W(\mathcal F)) 可被 transport 当且仅当

\[
\exists S\in\mathcal F_x:\quad S\cap Y=\varnothing.
\tag{2}
\]

这里暂时忽略 actual endpoint set 与 (Y) 的 freshness 条件；在 AMQ 应用中
应把抽样宇宙换成 (U\setminus S_0)，并相应修改分母。

## 2. 单步 exact core identity

当 (q=1)、(Y=\{y\}) 时，(x) 从 transported union 中消失当且仅当

\[
y\in C_x.
\tag{3}
\]

因此若 (y) 在 (U\setminus\{x\}) 中均匀，单个 (x) 的 loss probability
恰为

\[
\frac{c_x-1}{u-1},
\tag{4}
\]

而期望 transported-union loss 恰为

\[
\boxed{
\frac1{u-1}
\sum_{x\in W(\mathcal F)}(c_x-1).
}
\tag{5}
\]

式 (5) 比“为每个 (x) 随便选一个 witness (S_x)”所得的
(n|W|/u) union bound 精确。它也说明正确的障碍不是 witness 的最大距离，
而是 section 的强制交 core。

## 3. Fiber entropy 能推出的最强简单 core inequality

### Theorem 1（core-profile inequality）

令

\[
r=\frac{|\mathcal F|}{\binom un}.
\]

则

\[
\boxed{
nr
\le
\sum_{x\in W(\mathcal F)}
\frac{(n)_{c_x}}{(u)_{c_x}}.
}
\tag{6}

其中 ((a)_j=a(a-1)\cdots(a-j+1))。

证明。双计数给

\[
\sum_x|\mathcal F_x|=n|\mathcal F|.
\tag{7}
\]

每个 (S\in\mathcal F_x) 都包含固定 core (C_x)，所以

\[
|\mathcal F_x|
\le\binom{u-c_x}{n-c_x}.
\tag{8}
\]

对 (x) 求和，再除以 (inom un)，并使用

\[
\frac{\binom{u-c}{n-c}}{\binom un}
=\frac{(n)_c}{(u)_c},
\]

即得 (6)。

这个 inequality 对 star family 取等：若
(mathcal F=\{S:K\subseteq S\})，则对 (x\in K)，(C_x=K)。

### Corollary 2（短 core 的必要数量）

令

\[
N_d=|\{x:1\le c_x\le d\}|,
\qquad
a_j=\frac{(n)_j}{(u)_j}.
\]

因为 (a_j) 随 (j) 下降，

\[
nr\le N_da_1+(u-N_d)a_{d+1},
\]

故

\[
\boxed{
N_d\ge
\left[
\frac{nr-u a_{d+1}}{a_1-a_{d+1}}
\right]_+.
}
\tag{9}

式 (9) 是严格的 Johnson-local-density consequence。但它只在 fiber density
(r) 足够大时非平凡；AMQ state fibers 通常可能具有指数小的 (r)，因此它
本身不能闭合动态下界。

## 4. 任意 (q) 的最优 shadow 界

定义坏 suffix family

\[
\operatorname{Bad}_q(x)
=\left\{Y\in\binom Uq:
Y\cap S\ne\varnothing\text{ for every }S\in\mathcal F_x
\right\}.
\tag{10}

它恰是使所有 (x)-witness 都发生 fresh-insertion 冲突的 label sets。

### Theorem 3（Kruskal--Katona transport bound）

令 (s_x=|\mathcal F_x|)，并用唯一实数 (z_x\ge u-n) 写成

\[
s_x=\binom{z_x}{u-n}
\tag{11}

（使用 generalized binomial coefficient）。若 (q\le u-n)，则

\[
\boxed{
|\operatorname{Bad}_q(x)|
\le
\binom uq-\binom{z_x}{q}.
}
\tag{12}

证明。令

\[
\mathcal G_x=\{U\setminus S:S\in\mathcal F_x\}
\subseteq\binom U{u-n}.
\]

一个 (Y\) 是 good 当且仅当它包含于某个
(G\in\mathcal G_x)，即属于 (mathcal G_x) 的 (q)-lower shadow。
Lovasz 形式的 Kruskal--Katona theorem 给

\[
|\partial_q\mathcal G_x|\ge\binom{z_x}{q}.
\]

取补即得 (12)。

所以均匀 (q)-suffix 下的总期望 transport loss 满足

\[
\boxed{
\mathbb E_Y\operatorname{Loss}(Y)
\le
\sum_{x\in W(\mathcal F)}
\left(1-\frac{\binom{z_x}{q}}{\binom uq}\right).
}
\tag{13}

这是一条 sharp 的 section-profile 到随机右同余误差的转换定理。它允许
arbitrary global correlation，不假设 fiber 是 Hamming/Johnson ball、star
或 product family。

## 5. 为什么总 fiber entropy 无法控制 transport

下面的构造否决任何只依赖 (|\mathcal F|) 或其一阶指数率的普适低-loss
结论。

### Proposition 4（rare-witness poisoning）

取 (V\subset U)，(|V|=v>n)，并令

\[
\mathcal F_0=\binom Vn.
\]

对每个 (x\in U\setminus V)，任取一个包含 (x) 的 (n)-set (T_x)，并令

\[
\mathcal F=\mathcal F_0\cup\{T_x:x\in U\setminus V\}.
\tag{14}

则：

1. (W(\mathcal F)=U)；
2. 对每个 (x\notin V)，若 (T_x) 是唯一包含 (x) 的额外 set，则
   (mathcal F_x=\{T_x\}) 且 (C_x=T_x)，所以 (c_x=n)；
3. 
   \[
   |\mathcal F|=\binom vn+O(u),
   \tag{15}
   \]
   当 (inom vn\gg u) 时，加入所有 rare witnesses 不改变 fiber 的一阶
   entropy；
4. 对均匀单个 insert label (y)，仅由这些外部 keys 贡献的期望 loss 为
   \[
   \frac1{u-1}
   \sum_{x\notin V}(n-1)
   =\frac{(u-v)(n-1)}{u-1}.
   \tag{16}
   \]

若 (v=\theta u) 且 (	heta<1) 固定，式 (16) 为
((1-\theta)n+o(n))。因此一个对 (log|\mathcal F|) 几乎不可见的
(O(u))-sized poisoning 可以制造线性 transport loss。

这个构造也解释了式 (6) 为什么不能反向控制
(sum_x c_x)：双计数按 section multiplicity (|\mathcal F_x|) 加权，rare
sections 的权重只有 (1)，而 transported union 对每个出现过一次的 key
都按权重 (1) 收费。

## 6. 对 ordinary AMQ 下界的含义

### 6.1 已经得到的通用 insight

对 fixed-tape finite-state update system，state fiber 定义了一个右同余：若
两个 histories 到达同一 state，则任何对两者都合法的共同 suffix 保持 state
collision。Theorem 3 定量描述当 suffix 只因 fresh-update legality 而部分失效时，
这个右同余对随机 suffix 的近似稳定性。

从这个角度，dynamic AMQ 的非单调性障碍可以精确分成两部分：

\[
\text{transport error}
=
\text{section profile}
+
\text{random-suffix shadow expansion}.
\]

这比任取 witness 的 union bound 强，也比 partition-dependent reconstructible
set 更干净。

### 6.2 尚未得到的 dichotomy

Proposition 4 说明不存在如下单-tape theorem：

> fiber 大，所以大多数 ghost 有短 witness/core，所以 transport loss 小。

要闭合 ordinary AMQ lower bound，至少还必须使用以下一种跨对象信息：

1. **跨 random tapes 的 pointwise FPR：** 一个固定 key 不能在过多 tapes 的
   fixed-history endpoint 成为 rare poisoned ghost；
2. **跨 histories 的 state budget：** 对每个 fixed history 同时跟踪它落入各
   state fiber 的概率，而不是只看一个 fiber 的大小；
3. **weighted decoder：** 让通信代价按 section multiplicity 计费，从而不把
   rare witness 和 high-mass witness 等权；但这需要新的 lossless protocol。

这些信息不能由 Johnson graph 的单个 fiber expansion 自动提供。

## 7. 独立论文价值评估

Theorem 3 是一个简洁的极值组合/online-automata lemma：它把 state-fiber
sections 的 entropy profile 精确转成随机合法 suffix 下的 right-congruence
稳定性。配合 exact identity (5) 和 poisoning barrier (14)，可以形成一个
技术上完整的短 note 或较大 AMQ 论文中的结构章节。

但它单独还不像 SODA 主结果：

- 没有导出新的 AMQ space lower bound；
- Kruskal--Katona 是经典工具，主要新意在正确识别 section profile；
- rare-witness barrier 是重要的路线判定，却不是目标问题的正面解答。

真正达到 SODA taste 的下一步应是一个 **public-coin weighted fiber theorem**：
联合 pointwise FPR、state budget 和 (13)，证明所有 tapes/histories 上的 rare
sections 不能同时 poison 足够多的 query keys。若这种 theorem 给出新常数，
Theorem 3 会成为它的核心局部引理；若做不到，full-fiber transport 应被定位为
KLZ proof-interface repair，而不是独立突破。

