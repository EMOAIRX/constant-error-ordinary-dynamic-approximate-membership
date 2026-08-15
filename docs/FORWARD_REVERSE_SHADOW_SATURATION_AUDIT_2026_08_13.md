# Forward--reverse--shadow saturation：master identity 与 deletion-only barrier

> 日期：2026-08-13。状态：严格 master identity、严格静态-cover压力测试及一个
> semantic canonicalization theorem。结论是：仅使用 nested pure-deletion
> trajectory，即使联合 forward entropy、prefix-conditioned reverse collapse、
> shadow deficit和 delete-label mutual information，也不能普适证明 half error
> 下 \(H>(1+o(1))n\)。这些量精确分解同一个 initial-state budget；一个静态最优
> set-cover source encoder在所有删除中冻结其 accepted set，已经使所有可用约束在
> \(n+o(n)\) 饱和。

这不是 full dynamic filter 的 \(n\)-bit upper bound：压力测试没有实现后续
insertions。它严格说明，若要在 ordinary arbitrary模型中突破 \(n\)，证明必须
实质使用 **replacement branches**，不能只研究纯删除轨迹。

## 1. Random ordered-set experiment

令 \(S\) 均匀分布于 \({U\choose n}\)，并用一个预先固定的 canonical insertion
order建立 filter state \(M_0\)。令

\[
X_1,\ldots,X_n
\]

是 \(S\) 的均匀随机 deletion permutation。写

\[
D_j=\{X_1,\ldots,X_j\},
\qquad T_j=S\setminus D_j,
\qquad |T_j|=n-j,
\]

并令

\[
M_j=D_{R,X_j}(M_{j-1}).
\tag{1}

\]

给定 \((R,S)\)，canonical insertion history确定 \(M_0\)；给定
\((R,S,X_{\le j})\)，整个 state trajectory确定。filter本身可以
history-dependent；这里只固定了 source experiment的一条建立路径。

定义 prefix-conditioned reverse collapse

\[
r_i=H(M_{i-1}\mid M_i,X_{\le i},R)
\tag{2}

以及 delete-label information

\[
\iota_i=I(M_{i-1};X_i\mid X_{<i},R).
\tag{3}

\]

## 2. Exact master identity

### Theorem 2.1（forward--reverse cut decomposition）

对每个 \(0\le j\le n\)，

\[
\boxed{
H(M_0\mid R)
=I(T_j;M_j\mid X_{\le j},R)
+H(M_j\mid T_j,X_{\le j},R)
+\sum_{i=1}^j(r_i+\iota_i).
}
\tag{4}

在上述 canonical source experiment 中，第二项为零，故

\[
\boxed{
H(M_0\mid R)
=I(T_j;M_j\mid X_{\le j},R)
+\sum_{i=1}^j(r_i+\iota_i).
}
\tag{5}

**证明。** reverse entropy balance 给

\[
H(M_0\mid R)
=H(M_j\mid X_{\le j},R)
+\sum_{i=1}^j(r_i+\iota_i).
\tag{6}

\]

对第一项按 \(T_j\) 分解即得式 (4)。给定
\((T_j,X_{\le j})\) 可恢复完整 initial set
\[
S=T_j\cup D_j.
\]
canonical insertion order、public tape和 deletion order 随后唯一决定 \(M_j\)，
所以
\[
H(M_j\mid T_j,X_{\le j},R)=0.
\]
得到式 (5)。\(\square\)

式 (5) 是候选 saturation inequality 必须尊重的会计恒等式。三类量不是三份预算；
它们之和恰好是同一个 \(H(M_0\mid R)\)。

## 3. Same-tape shadow 给 forward information 的下界

固定 \((R,M_j,X_{\le j})\)。令 \(W_j\) 是 initial endpoint state fiber 经共同
删除 \(D_j\) 后的 lower-section union。same-tape shadow theorem 给

\[
T_j\subseteq W_j\subseteq A_R(M_j).
\tag{7}

\]

令

\[
V_j=U\setminus D_j,
\qquad t=n-j.
\]

条件于 \(X_{\le j}\)，随机变量 \(T_j\) 在 \({V_j\choose t}\) 上均匀。因此

### Lemma 3.1（forward cover information）

\[
\boxed{
I(T_j;M_j\mid X_{\le j},R)
\ge
\log_2{u-j\choose t}
-\mathbb E\log_2{|A_R(M_j)\setminus D_j|\choose t}.
}
\tag{8}

同样可把 accepted set替换为较小的 same-tape shadow \(W_j\)。

**证明。** 给定 \((M_j,X_{\le j},R)\)，所有 compatible \(T_j\) 都必须是
\(A_R(M_j)\setminus D_j\) 的 \(t\)-subsets。故 conditional entropy 至多右侧
第二项，减去 unconditional entropy即得。\(\square\)

把式 (8) 代入式 (5) 得一个完全合法的 arbitrary-filter lower bound：

\[
H(M_0\mid R)
\ge
\log_2{u-j\choose t}
-\mathbb E\log_2{|A_R(M_j)\setminus D_j|\choose t}
+\sum_{i=1}^j(r_i+\iota_i).
\tag{9}

\]

pointwise FPR只控制 accepted-set cardinality 的平均。用 concavity/Jensen放松后，
式 (9) 在 \(u/n^2\to\infty\) 时成为

\[
H(M_0\mid R)
\ge t\log_2(1/\varepsilon)
+\sum_{i=1}^j(r_i+\iota_i)-o(n).
\tag{10}

这正是最自然的 forward + reverse + label-information候选。

## 4. 为什么式 (10) 不能自行产生额外线性项

式 (5) 说明

\[
\sum_{i=1}^j(r_i+\iota_i)
=H(M_0\mid R)-I(T_j;M_j\mid X_{\le j},R).
\tag{11}

\]

因此要从式 (10) 推出 \(H>(1+c)n\)，必须证明 actual forward information比静态
cover lower bound多，或者证明 reverse/label项比 forward information的下降更快。
key-only deletion与pointwise FPR本身没有这种纯删除结论。

下面给出一个精确压力测试，说明所有只使用式 (1)--(10) 中性质的证明最多得到
静态 Carter rate。

## 5. Static random-cover deletion process

固定 \(0<\rho<1/2\)，令 public tape包含 \(N\) 个独立 Bernoulli-\(\rho\) subsets

\[
A_1,\ldots,A_N\subseteq U,
\qquad
\Pr[x\in A_i]=\rho.
\]

取

\[
N=\left\lceil \rho^{-n}n^2\right\rceil.
\tag{12}

\]

给定 initial set \(S\)，source encoder保存最小 index

\[
I(S)=\min\{i:S\subseteq A_i\};
\]

若不存在则保存 failure symbol \(\bot\)。query在 normal state \(i\) 接受
\(A_i\)，在 \(\bot\) 接受整个 universe。

### Lemma 5.1（static rate and pointwise error）

该 encoder zero-FN，使用

\[
\log_2(N+1)
=n\log_2(1/\rho)+O(\log n)
\tag{13}

bits。对每个 fixed \(S\) 和 \(x\notin S\)，

\[
\Pr_R[\text{Query}(x)=\mathrm{YES}]
\le \rho+e^{-n^2}.
\tag{14}

**证明。** 单个 \(A_i\) 包含 \(S\) 的概率为 \(\rho^n\)，所以 failure probability
至多
\[
(1-\rho^n)^N\le e^{-n^2}.
\]
条件于任意 index成为第一个包含 \(S\) 的集合，事件 \(x\in A_i\) 与
\(S\subseteq A_i\) 及更早 indices失败独立，概率为 \(\rho\)。加上 failure即得
式 (14)。\(\square\)

现在只考虑删除：状态 index保持不变，query始终使用同一个 \(A_i\)。删除后的
logical set是 \(S\) 的子集，所以 zero-FN持续成立；每条 fixed deletion history
的 pointwise FPR仍满足式 (14)。delete transitions为 identity，因此

\[
r_i=0.
\]

state对随机 delete labels 的全部相关性由 \(\iota_i\) 承担，并且式 (5)精确
telescopes。取例如

\[
\rho=\frac12-\frac1n,
\]

则式 (14)最终小于 \(1/2\)，而

\[
\log_2(N+1)=n+O(1)+O(\log n)=n+o(n).
\tag{15}

\]

accepted shadows在所有 deletion layers都保持约 \(u/2\)，而 forward information
的下降恰转移到 delete-label mutual information；没有额外 linear saturation。

### 这个压力测试证明了什么

它不是 full dynamic AMQ：source encoder没有给出只凭当前 index执行后续 fresh
insertions的方法。因此它不反驳一般 dynamic lower bound。

但它满足 pure-deletion master identity、same-tape shadow inclusion、zero-FN、
pointwise FPR、deterministic key-only deletions和single-budget reverse accounting。
所以任何只使用这些性质的 proof都无法区分它与真正 dynamic filter，也就不可能
从这些性质推出 \(H>(1+o(1))n\)。

这比 frozen mask压力测试更 sharp：它以 \(n+o(n)\) state bits同时饱和静态
set-cover rate与全部 nested deletion constraints。

## 6. 必须加入的最弱现实条件：replacement closure

full dynamic模型本来就额外保证：删除 \(D\) 后，机器必须从当前 state处理任意
fresh set \(Y\subseteq U\setminus(S\setminus D)\) 的 insertions，并继续满足
pointwise FPR。Static random-cover process失败的地方恰好是这里：index \(i\) 只
证明 \(S\setminus D\subseteq A_i\)，若 fresh \(y\notin A_i\)，它不知道 original
remaining set，无法安全转移到另一个 small accepted set。

因此，对 arbitrary模型继续推进不需要人为加入 canonical/locality假设；需要在
证明 experiment中使用已有的 **replacement closure**：

\[
S
\xrightarrow{\operatorname{Delete}(D)}
S\setminus D
\xrightarrow{\operatorname{Insert}(Y)}
(S\setminus D)\cup Y.
\tag{16}

\]

真正缺失的 saturation theorem必须是二维 branching版本：同时在许多 deletion
prefixes和许多 fresh insertion continuations上控制 endpoint fibers。一个准确的
候选形式是

\[
\boxed{
\text{forward cover information}
+\text{prefix reverse collapse}
+\text{delete-label information}
+\text{fresh-branch transition cost}
\ge(1+c)n.
}
\tag{17}

前三项被式 (5)锁死在一个 initial-state budget中；只有第四项能排除 static-cover
压力测试。第四项不能定义成另一个 pivot state entropy，否则会重复收费；它应是
条件于 \((R,M_j,X_{\le j})\) 后，不同 fresh \(Y\) 导致的 successor partition
或 accepted-shadow transversal entropy。

目前没有证明式 (17) 对某个 \(c>0\) 成立。它是 full arbitrary模型中最弱且
不额外改变问题语义的下一目标。

## 7. 如果允许一个结构条件：semantic confluence

若希望立即恢复 canonical converse，一个比“同一 multiset只有一个 physical
state”更弱的条件是 observational/semantic confluence。

定义两个 states \(s,t\) continuation-equivalent：对每条从各自 compatible
logical sets均合法的 finite key-only continuation，它们产生相同 query answers，
且 successor states仍 continuation-equivalent。

### Theorem 7.1（semantic canonicalization）

若对每个 logical multiset \(S\)，所有 reachable states in \(R_S\) 两两
continuation-equivalent，则把 physical states按 continuation equivalence取商，
得到一个 deterministic canonical summary

\[
\phi(S)=[s],\qquad s\in R_S,
\tag{18}

且：

1. \(\phi(S)\) 与 representative及history无关；
2. insert/delete maps在 quotient上良定义；
3. 所有 query行为和FPR完全保持；
4. quotient states数不超过原 physical states数。

**证明。** 假设保证式 (18) well-defined。continuation equivalence对每个合法
one-step continuation是 right congruence，所以 updates在 quotient上well-defined；
empty continuation中的 query equivalence保持输出。取商只合并 states，不增加
空间。\(\square\)

对 exact-load binary block-local summaries，Theorem 7.1 后可直接应用 lattice
normal form及 biased/masked binary theorem，恢复唯一

\[
q=3,qquad p=1/2,qquad \beta=1,
\]

以及 \(2.349083440193\ldots\) bits/key。

semantic confluence弱于 literal history independence，因为允许多个 physical
representations和任意内部 holonomy，只要求这些差异对所有未来可观察行为无影响。
但它仍是额外结构条件，不可从 ordinary semantics自动推出；nontransitive fiber
反例正说明其必要性。

## 8. 结论

对一般 arbitrary filter，forward、reverse、shadow和delete-label四类 deletion
量已经有完整会计：式 (5) 是精确恒等式，式 (8) 是 sharp static-cover接口。
Static random-cover deletion process证明，这套 pure-deletion信息最多强迫
\(n+o(n)\) bits。

因此主线 C 的下一步不应继续寻找另一个 deletion-only telescoping修正项。两条
诚实路线是：

1. 不加结构假设，证明 replacement-branch saturation inequality (17)；
2. 加最弱的 semantic confluence，取 observational quotient后回到 canonical
theory。

在 replacement cost被严格量化前，full arbitrary模型仍没有新的
\(>n\) lower bound。
