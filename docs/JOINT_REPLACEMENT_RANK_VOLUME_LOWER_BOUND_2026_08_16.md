# Joint transportable-section rank-volume 下界与 residual-shadow hierarchy

> 日期：2026-08-16。状态：一般 finite-parameter 结构定理。本文把一次
> source-dependent replacement 的删除 labels、插入 labels 与未改变 survivors
> 联合编码，从而精确消去 single-cut 公式中的 suffix-source mutual information。
> 结论对 arbitrary history dependence、multiple representations、ghosts、holonomy
> 与 nonmonotone queries 都成立，不要求 BSSI。它给出一个非负的 transportable-
> section rank premium，但尚未证明该 premium 对所有 low-space ordinary filters
> 都线性为正，也尚未用 successor FPR 控制该 premium。

所有对数以 2 为底。

## 1. Fixed-word residual invariance

固定一个 concrete legal update word $\omega$。对每个在 $\omega$ 中出现的 label，
其 Insert/Delete 操作必定交替。定义：

- $P_\omega$：第一次操作是 Delete 的 labels；
- $N_\omega$：第一次操作是 Insert 的 labels；
- $F_\omega$：最后一次操作是 Insert 的 labels；
- $K_\omega=P_\omega\sqcup N_\omega$：全部 touched labels。

固定 parent load $t$，令 $k=t-|P_\omega|$。只要 word 的 load path 不超过容量，
其合法 domain 精确为

$$
S=P_\omega\sqcup X,
\qquad
X\in\binom{U\setminus K_\omega}{k},
$$

且逻辑 endpoint 精确为

$$
\phi_\omega(S)=F_\omega\sqcup X.
$$

因此 $\phi_\omega$ 在 compatible domain 上是双射，并保持全部 untouched
structure：

$$
\phi_\omega(S)\mathbin\triangle\phi_\omega(S')
=S\mathbin\triangle S'.
$$

特别地，对任意 compatible family，删除强制坐标后的 residual family、其 union、
全部 lower shadows 与 family cardinality 在逻辑更新前后完全相同。

### Common-continuation lemma

若同一个 word 对两个 sets $S,S'$ 都合法，则它不可能触碰
$S\mathbin\triangle S'$ 中的任何 label。否则第一次触碰该 label 时，Insert 对一边
合法而对另一边非法，或 Delete 对一边合法而对另一边非法。因此共同合法
continuation 严格保持对称差。

这解释了 fixed-word two-endpoint 方法为何天然退化为 survivor geometry：所有
被 word 明文改变的 coordinates 已成为 side information，真正同时存在于两个
endpoint 的随机对象只有 untouched survivors。

## 2. Operational sections

固定 tape $r$、physical state $m$、parent load $t$ 与 exact operation time $q$。
假设后续 word 仍位于 promised horizon 内。
令

$$
\mathcal O_r(m,t,q)
=\{S:\text{存在长度 }q\text{ 的合法 history 以 }S\text{ 结束并到达 }m\},
$$

并定义 full operational union

$$
W_r(m,t,q)=\bigcup_{S\in\mathcal O_r(m,t,q)}S,
\qquad w_r(m)=|W_r(m,t,q)|.
$$

对 disjoint $A,B\subseteq U$，$|A|=a$、$|B|=b$，考虑 concrete word：先按
固定顺序删除 $A$，再按固定顺序插入 $B$。令 $k=t-a$，并定义 residual section

$$
\mathcal F_{r,m}(A,B)
=\{S\setminus A:
S\in\mathcal O_r(m,t,q),\ A\subseteq S,\ S\cap B=\varnothing\}.
$$

它是 $\binom{U\setminus(A\cup B)}k$ 的一个 subfamily。固定 tape 后，所有 section
worlds 从同一个 $m$ 出发执行同一个 word，故到达同一个 successor state；其逻辑
image 恰为

$$
\{B\cup X:X\in\mathcal F_{r,m}(A,B)\}.
$$

注意这只是 image inclusion。Full successor fiber 可以因 physical-state merging
而更大；逻辑 word 可逆不意味着 physical transition 可逆。

## 3. Residual-shadow hierarchy

对 $\mathcal F\subseteq\binom Vk$ 与 $1\le d\le k$，定义 $d$-shadow

$$
\operatorname{Sh}_d(\mathcal F)
=\bigcup_{X\in\mathcal F}\binom Xd,
$$

以及其 $k$-clique completion

$$
\operatorname{Cl}_{k,d}(\mathcal F)
=\left\{K\in\binom Vk:
\binom Kd\subseteq\operatorname{Sh}_d(\mathcal F)\right\}.
$$

每个 actual member of $\mathcal F$ 都属于该 completion。并且

$$
\operatorname{Cl}_{k,k}(\mathcal F)=\mathcal F,
$$

而 $d=1$ 时

$$
\left|\operatorname{Cl}_{k,1}(\mathcal F)\right|
=\binom{|\bigcup\mathcal F|}{k}.
$$

随 $d$ 增大，completion 单调缩小。这给出从 query-visible union rank 到完整
operational support 的单调插值；相邻 levels 可以相等。

对 state $(r,m)$ 定义 joint transportable-section volume

$$
\Phi^{(d)}_{r,m}
=\sum_{\substack{A,B\subseteq U\\
|A|=a,\ |B|=b,\ A\cap B=\varnothing}}
\left|\operatorname{Cl}_{k,d}
\bigl(\mathcal F_{r,m}(A,B)\bigr)\right|.
$$

## 4. Joint transportable-section rank-volume theorem

令 $S$ 在 $\binom Ut$ 上均匀。对每个 $S$ 使用一个预先固定、与 random tape
$R$ 独立、operation time 相同的合法 source history，令 endpoint state 为 $M$。
固定参数 $0\le a<t$ 与 $0\le b\le u-t$。
给定 $S$ 后，独立均匀抽取

$$
A\in\binom Sa,
\qquad
B\in\binom{U\setminus S}b,
$$

并令 $K=S\setminus A$。假设 delete-$A$-then-insert-$B$ 的 load path 位于容量内。

### Theorem 4.1

对每个 $1\le d\le k=t-a$，

$$
\boxed{
H
\ge I(S;M\mid R)
\ge
\log\left[
\binom ut\binom ta\binom{u-t}b
\right]
-\mathbb E\log\Phi^{(d)}_{R,M}.
}
$$

#### Proof

三元组 $(A,B,K)$ 在全部 pairwise-disjoint、sizes 分别为 $(a,b,k)$ 的 triples 上
均匀，其总数为

$$
N_{a,b}
=\binom ut\binom ta\binom{u-t}b.
$$

给定 $(R,M)=(r,m)$，每个 actual triple 满足

$$
K\in\mathcal F_{r,m}(A,B)
\subseteq
\operatorname{Cl}_{k,d}(\mathcal F_{r,m}(A,B)).
$$

所以 conditional support 的总大小至多 $\Phi^{(d)}_{r,m}$，从而

$$
H(A,B,K\mid R,M)
\le\mathbb E\log\Phi^{(d)}_{R,M}.
$$

另一方面，$S=A\cup K$ 可由 triple 恢复，并且给定 $(S,R)$ 后，随机选择
$(A,B)$ 与 physical state $M$ 条件独立。因此

$$
I(A,B,K;M\mid R)=I(S;M\mid R).
$$

从 $H(A,B,K\mid R)=\log N_{a,b}$ 相减即得结论。整个 proof 只发送/收费 parent
state $M$，没有第二份 $H$。Section 2 另行证明每个 residual family 可运输到由
$(M,A,B)$ 决定的 successor；当前 entropy inequality 本身不使用 successor
accepted set 或 successor FPR。$\square$

### 为什么 suffix-source information 消失

若先固定 $(A,B)$ 再研究 $S$，删除 labels 来自 $S$、插入 labels 来自
$U\setminus S$，会出现一个大的 $I(S;A,B\mid R,M)$ penalty。Theorem 4.1 不把
$(A,B)$ 当免费 side information，而是联合编码 $(A,B,K)$。精确的 source entropy

$$
\log\binom ta+\log\binom{u-t}b
$$

已进入左侧总 volume，因此 mutual-information penalty 被整体消掉，而不是被忽略。

## 5. Static saving 加 transportable-section premium

令 $w=w_R(m)$。每个 completion triple $(A,B,K)$ 都给出一个 $t$-set
$A\cup K\subseteq W_r(m)$。对每个 fixed $t$-set，最多有
$\binom ta\binom{u-t}b$ 个这样的 $(A,B)$ choices。因此

$$
\Phi^{(d)}_{r,m}
\le
\binom wt\binom ta\binom{u-t}b.
$$

定义 nonnegative transportable-section rank premium

$$
\Delta^{(d)}_{r,m}
=\log
\frac{
\binom wt\binom ta\binom{u-t}b
}{\Phi^{(d)}_{r,m}}.
$$

Theorem 4.1 等价地给出

$$
\boxed{
H\ge
\log\binom ut
-\mathbb E\log\binom wt
+\mathbb E\Delta^{(d)}_{R,M}.
}
$$

对每条 fixed source history先使用 pointwise FPR，再对 source 平均，得到

$$
\mathbb E w\le t+\varepsilon(u-t)=:\mu.
$$

由于 $j\mapsto\log\binom jt$ 的 discrete increments 单调递减，其分段线性延拓
是凹函数。令 $c=\lfloor\mu\rfloor$、$\lambda=\mu-c$，并写

$$
\overline F_t(\mu)
=(1-\lambda)\log\binom ct
+\lambda\log\binom{c+1}t.
$$

则有 exact mean-only corollary

$$
\boxed{
H\ge
\log\binom ut
-\overline F_t\bigl(t+\varepsilon(u-t)\bigr)
+\mathbb E\Delta^{(d)}_{R,M}.
}
$$

当 $u/t\to\infty$ 且 $\varepsilon$ 固定时，

$$
\boxed{
H\ge
t\log\frac1\varepsilon
+\mathbb E\Delta^{(d)}_{R,M}
-o(t).
}
$$

这是一个一般 ordinary-model lower bound：任何正的 joint transportable-section
rank deficit 都在 Carter rate 之外逐 bit 加入，且没有 BSSI 或 suffix-source
information 项。证明尚未从 successor FPR 或 transition width 推出该 deficit 必须
为正。

## 6. Rank-1 premium 的严格 barrier

$d=1$ 只观察每个 section residual union。它仍可能完全看不见一个极薄的
operational family。

取 $u=5,t=3,a=b=1$，令 $\mathcal O$ 是全部 $3$-sets，删去

$$
\{0,1,4\},\qquad\{2,3,4\}.
$$

于是 $|\mathcal O|=8<10$。但对每个 distinct $a,b$，包含 $a$、避开 $b$ 的
section residual union 都是 $U\setminus\{a,b\}$，所以

$$
\Phi^{(1)}
=5\cdot4\cdot\binom32
=60
=\binom53\cdot3\cdot2.
$$

因此 $\Delta^{(1)}=0$，尽管 family 已经不是 complete layer。

更强地，若 $t/u$ 保持在 $(0,1)$ 的常数区间，随机取 $C\log u$ 个 $t$-sets 即可
以正概率满足：对每个 distinct triple $(a,x,b)$，某个 block 包含 $a,x$ 且避开
$b$。单 block 命中概率为

$$
\frac{t(t-1)(u-t)}{u(u-1)(u-2)}=\Theta(1),
$$

对少于 $u^3$ 个 triples 作 union bound 即可。于是每个 one-for-one replacement
section 仍有 full residual union，$\Delta^{(1)}=0$，但 family 只有 $O(\log u)$
个 sets。

所以 cardinality/union-rank 方法即使在高负载 replacement 下也有严格 design
barrier。下一步不能继续堆 fixed words 或 endpoint cuts；必须证明 recurrent
replacement 把某个 $d\ge2$ residual shadow 暴露为未来 point-query response，或给出
一个 right-congruent counterexample 说明这种 shadow exposure 不成立。

## 7. Collision-cylinder propagation

Shadow exposure 的一个严格 seed 来自 shared-state collisions。固定 tape 与
exact operation time，若同一 physical state $q$ 可由两个 endpoints

$$
S=A\cup C,
\qquad
T=B\cup C
$$

到达，其中 $A,B,C$ pairwise disjoint 且 $|A|=|B|$，则对任意与 $A\cup B$
disjoint、且 $|C'|=|C|$ 的 core $C'$，先删除 $C\setminus C'$，再插入
$C'\setminus C$，得到一个 common legal word。其 intermediate load 只会下降，
并假设 successor exact time仍在 promised horizon 内。Right congruence 强迫两条
histories到达同一个 successor
$q_{C'}$，而该 state 同时表示

$$
A\cup C',
\qquad
B\cup C'.
$$

所以 $A\cup B$ 在整个 core Johnson slice 上作为双向 operational ghosts传播。
若不同 core paths 再次 merge 到同一 state，该 state 的 accepted union还必须包含
这些 cores 的 union，产生下一代 ghost growth。

这个 lemma 对 multiple representations 有效，不要求 canonical fibers。但
holonomy 允许不同 paths 到达不同 representations，因此它目前给出的是 history
tree 上的 collision cylinder，不是一个 path-independent core quotient。

相应的本质目标是一个 public-tape-convexified cylinder-recursion inequality：若小
state space 在大量 parent collisions上反复复用 colors，则 recurrent core merges
必须产生足够大的 union penalty或高阶 shadow deficit。它真正使用 extensive-depth
recurrence，不是单个 parent 的 successor outdegree。

## 8. 当前结论

已经得到：

1. 任意合法 fixed word 的 residual family 与全部 shadows 精确 transport；
2. joint rank-volume theorem 用一份 $H$ 同时编码 replacement labels 与 survivors；
3. source-dependent suffix 的 mutual-information penalty 被精确消去；
4. 下界分解为 static union saving 加非负 transportable-section rank premium；
5. rank-1 premium 有严格 logarithmic-size covering-design barrier。

尚未得到：

1. $\mathbb E\Delta^{(d)}=\Omega(t)$ 对某个 universal $d$；
2. point queries 如何在一般 right congruence 中强迫 $d\ge2$ shadow exposure；
3. unrestricted ordinary constant-error model 的新 universal numerical constant。
