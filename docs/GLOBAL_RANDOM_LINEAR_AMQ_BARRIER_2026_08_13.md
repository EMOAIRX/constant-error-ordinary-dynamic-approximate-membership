# 全局随机线性 AMQ 的 sharp barrier

> 日期：2026-08-13。状态：本文中的 fixed-exponent saturation、random-linear
> collision lemma、reachable-image lower bound 和 half-error barrier 均为解析结论。
> 它们排除两类最自然的 cross-block additive sketches，但不构成 ordinary dynamic
> AMQ 的一般下界。

所有对数以 2 为底。

## 1. 从应用出发

Bloom filter、counting sketch、IBLT 和许多 retrieval structures 都把大量局部
occupancies 压成少量线性 checks。面对 fixed-error dynamic membership，一个自然
设想是跳过独立 blocks，直接保存所有 fingerprint coordinates 的全局 syndrome：

\[
x=(x_1,\ldots,x_M)\in\mathbb N^M,
\qquad (|x|,Ax).
\tag{1}
\]

这里 \(x_i\) 是第 \(i\) 个 fingerprint 的 multiplicity，\(M=\Theta(n)\)，
而 \(A\) 是公共随机带上的线性矩阵。Insert/Delete 只需加减一列，跨 coordinates
的 parity checks 看起来又可能比 block product 更有效地共享状态。

本文证明，这个方向存在一个 sharp obstruction。在 half error 下：

- 固定有限域或 bounded-exponent group 会因为一个高 occupancy coordinate 而
  渐近退化为 `ALL-YES`；
- characteristic 随 \(n\) 增长的 uniform random-linear sketch若保持常数拒绝率，
  则必须在 load-\(n\) composition simplex 上保持指数级接近单射；
- 再结合 unavoidable fingerprint collision，fixed worst-case state rate至少是
  \[
  2.384499842479\ldots n-o(n),
  \]
  严格劣于 order-3 binary threshold quotient 的
  \(2.349083440193\ldots n+o(n)\)。

所以真正的改进不能来自“把 fixed-field LDPC checks 做得更稀疏”，也不能来自
“把 random dense matrix 的域做大”。它必须使用高度设计的确定性大特征 quotient、
非线性 right congruence，或 history-dependent multiple representations。

## 2. 精确模型

容量为 \(n\)。公共 fully random fingerprint map把每个 key独立均匀送入
\([M]\)，其中

\[
\frac Mn\longrightarrow\alpha\in(0,\infty).
\tag{2}
\]

当前集合的 count vector为 \(x\in\mathbb N^M\)，\(|x|\le n\)。filter保存

\[
(|x|,Ax),
\qquad A\in\mathbb F_p^{r\times M},
\tag{3}
\]

其中 \(A\) 的 entries在公共随机带上 IID uniform，并与 fully random
fingerprint map 独立抽取；\(p=p_n\) 可以随 \(n\) 变化。写 \(Q=p^r\)。

给定 load \(c\)、syndrome \(s\) 和 query coordinate \(i\)，minimal one-sided
rule为

\[
Q_A(c,s,i)=\mathrm{YES}
\iff
\exists y\in\mathbb N^M:
|y|=c,\ Ay=s,\ y_i>0.
\tag{4}
\]

式 (4) 是固定 quotient 中的最优规则：fiber中只要有一个 composition包含
coordinate \(i\)，zero false negatives就强迫 `YES`。任何其他 one-sided rule
只会有更高 FPR。

物理内存是固定的 \(H\) bits。它必须覆盖公共矩阵 \(A\) 和 fingerprint map 的
每个可能 realization上、所有合法 key histories到达的 states；不能按 syndrome
的平均熵或整个 \(\mathbb F_p^r\) 的名义大小计费。在 abstract full-simplex
label model中全部 compositions都可达。ordinary finite-universe key API 另假设
\(|U|/n\to\infty\)；Section 5 用 rich-coordinate argument实现所需的
bounded compositions，不会把空 hash fibers静默计入状态数。

## 3. Bounded exponent 必然饱和

先给一个不需要矩阵随机性的 obstruction。

### Lemma 3.1（mass-transfer relation）

令 \(A:\mathbb Z^M\to G\) 是到 exponent为 \(q\) 的有限 Abelian group的
任意 homomorphism。则对所有 coordinates \(i,j\)，

\[
q(e_i-e_j)\in\ker A
\cap\{z:\mathbf1^\top z=0\}.
\tag{5}
\]

因此，若某个真实 composition满足 \(x_j\ge q\)，则它的 fixed-load syndrome
fiber对每个 \(i\in[M]\) 都包含

\[
y=x-qe_j+qe_i.
\tag{6}

特别地，minimal one-sided query在该 state对所有 coordinates回答 `YES`。

**证明。** 由 group exponent定义，\(qA(e_i)=qA(e_j)=0\)，故式 (5)成立。
式 (6) 非负、保持 total load且与 \(x\) 有相同 syndrome，并满足 \(y_i>0\)。
代入式 (4)即得结论。\(\square\)

### Theorem 3.2（bounded-characteristic no-go）

若 \(M/n\to\alpha\) 且 group exponent \(q=O(1)\)，则在 \(n\) 个 fixed members
的 uniform fingerprint occupancy下，

\[
\Pr[\max_jx_j\ge q]\longrightarrow1.
\tag{7}
\]

所以任意上述 additive quotient的拒绝概率趋于零，FPR趋于一。更一般地，只要

\[
q\le(1-o(1))\frac{\log n}{\log\log n},
\tag{8}
\]

标准 balls-into-bins maximum-load theorem仍给相同结论。

这排除任意 fixed-field dense matrix、fixed-field LDPC matrix，以及任意 fixed
finite Abelian target group；矩阵的 rank、sparsity、girth和dual distance都无关。

## 4. Growing characteristic 的 collision lemma

现在允许 \(p_n\to\infty\)。取任意整数 \(L\) 满足

\[
1\le L<p.
\tag{9}
\]

固定 query coordinate \(i\)，令

\[
\mathcal Y_{n,M,L}(i)
=\{y\in\{0,1,\ldots,L\}^M:|y|=n,\ y_i>0\},
\tag{10}
\]

并写 \(T_{n,M,L}=|\mathcal Y_{n,M,L}(i)|\)。由 symmetry，这个数量不依赖
\(i\)。

### Lemma 4.1（pairwise-independent witnesses）

固定任意真实 composition \(x\) 和满足 \(x_i=0\) 的 coordinate \(i\)。对
每个 \(y\in\mathcal Y_{n,M,L}(i)\)，写

\[
z_y=y-x\pmod p.
\tag{11}
\]

若某个 \(z_y=0\)，query已确定被接受。否则，集合
\(\{z_y:y\in\mathcal Y_{n,M,L}(i)\}\) 在
\(\mathbb F_p^M\) 中至少占据

\[
D\ge\frac{T_{n,M,L}}{L+1}
\tag{12}
\]

条不同 projective lines。每条 line取一个 representative后，事件

\[
Az_y=0
\tag{13}
\]

两两独立，且各自概率恰为 \(Q^{-1}\)。因此

\[
\boxed{
\Pr_A[Q_A(n,Ax,i)=\mathrm{NO}]
\le\frac{Q(L+1)}{T_{n,M,L}}.
}
\tag{14}
\]

**证明。** 固定一条 projective line及其中一个非零 \(z_y\)。选择
\((z_y)_j\ne0\) 的 coordinate \(j\)。若 \(z_{y'}=c z_y\)，则
\(y'_j-x_j=c(z_y)_j\pmod p\)。右侧的 \(c\) 由 \(y'_j\) 唯一决定，而
\(y'_j\in\{0,\ldots,L\}\) 且 \(L<p\)，所以该 line至多包含 \(L+1\) 个
candidates。这证明式 (12)。

不同 projective lines的 representatives线性独立成对；uniform random matrix
的两个 images因此独立均匀于 \(\mathbb F_p^r\)。令 \(Z\) 是式 (13)成立的
representatives数，则

\[
\mathbb EZ=D/Q,
\qquad \operatorname{Var}Z\le D/Q.
\]

Chebyshev给

\[
\Pr[Z=0]\le\frac{\operatorname{Var}Z}{(\mathbb EZ)^2}
\le\frac QD.
\]

任意 \(Z>0\) 都给式 (4)中的 witness，代入式 (12)即得式 (14)。\(\square\)

### Corollary 4.2（constant rejection forces a large syndrome range）

若在 load \(n\) 时整体拒绝概率至少为固定 \(\delta>0\)，则式 (14) 是对任意
\(x,i\) 的统一上界；对 member occupancy 与 query coordinate 取平均后仍有
\(\delta\le Q(L+1)/T_{n,M,L}\)，故必有

\[
\boxed{
Q\ge \frac{\delta T_{n,M,L}}{L+1}.
}
\tag{15}

这里没有把随机 query当成 pointwise保证。对 ordinary key API，固定一条
seed-independent history和固定 nonmember；它们的 fingerprints仍是独立 uniform
coordinates。式 (14)先对每个 realized member occupancy和query coordinate成立，
再作平均，所以恰好保留 pointwise量词。

## 5. 名义 group size 变成 reachable-state lower bound

式 (15)只下界 \(Q=|\mathbb F_p^r|\)，还不能直接把不可达 syndromes计入内存。
下一步关闭这个漏洞。

### Lemma 5.1（reachable image is exponentially large）

先在 abstract full-simplex label model中令

\[
\mathcal T_{n,M,L}
=\{y\in\{0,\ldots,L\}^M:|y|=n\},
\qquad T=|\mathcal T_{n,M,L}|.
\tag{16}
\]

对 uniform random \(A\)，存在一个 realization满足

\[
|A(\mathcal T_{n,M,L})|
\ge \frac{T}{1+T/Q}.
\tag{17}

因此，只要 \(Q\ge T/2^{o(n)}\)，任何覆盖全部公共 tapes的 fixed memory都有

\[
H\ge\log T-o(n).
\tag{18}

**证明。** 因为 \(L<p\)，不同 \(y,y'\in\mathcal T_{n,M,L}\) 在
\(\mathbb F_p^M\) 中仍不同，所以

\[
\Pr_A[Ay=Ay']=Q^{-1}.
\]

令各 syndrome fiber大小为 \(b_s\)。存在一个 \(A\) 使

\[
\sum_s {b_s\choose2}
\le {T\choose2}/Q.
\]

Cauchy--Schwarz给

\[
|A(\mathcal T)|
\ge\frac{(\sum_sb_s)^2}{\sum_sb_s^2}
\ge\frac{T}{1+T/Q},
\]

即式 (17)。该矩阵在公共随机分布中有正概率；固定 \(H\)-bit state必须也能表示
它的全部 reachable load-\(n\) syndromes，所以式 (18)成立。\(\square\)

这里用于 Corollary 4.2 的 collision estimate 与这里的 large-image matrix 不必由
同一张 tape 同时达到。前者下界共同参数 \(Q\)，后者从公共随机分布中选出一个
fixed memory 必须覆盖的 realization；\(H\) 对所有 tapes 使用同一个最坏情形上限。

注意这个证明只数正锥 simplex的真实 image，从未把全部 \(Q\) 个名义 syndromes
当成 reachable。

### Lemma 5.2（ordinary key API 的 richness lift）

假设 \(|U|/n\to\infty\)，\(M=\Theta(n)\)。固定任意常数 \(L\)。称 coordinate
\(j\) 为 \(L\)-rich，若至少有 \(L\) 个 universe keys hash到 \(j\)。则存在
fingerprint-map realization使 \(L\)-rich coordinates数

\[
M'=M-o(M).
\tag{18a}
\]

而且对任意固定 history和fixed nonmember query，除去这至多 \(n+1\) 个keys后，
同一结论仍成立。因此，所有
\(y\in\{0,\ldots,L\}^{M'}\)、\(|y|=n\) 都可由 distinct备用keys实现；要求
query coordinate出现一次只改变非指数因子。于是Lemmas 4.1和5.1都可限制到
这些rich coordinates，分别给出相同一阶的collision bound和

\[
H\ge \log [z^n](1+z+\cdots+z^L)^{M-o(M)}-o(n).
\tag{18b}
\]

**证明。** fixed coordinate的fiber size为
\(\operatorname{Bin}(|U|,1/M)\)，其均值 \(|U|/M\to\infty\)，所以该
coordinate不是 \(L\)-rich的概率为 \(o(1)\)。从universe中删掉fixed history
和query的至多 \(n+1\) 个keys后，均值仍为
\((|U|-O(n))/M\to\infty\)。不rich coordinates数的期望为
\(o(M)\)，Markov给式 (18a)对某些乃至高概率的hash realizations成立。fixed
memory必须覆盖这种 realization。每个rich coordinate独立提供至少 \(L\) 个
distinct keys，故相应bounded compositions全部可达。\(\square\)

## 6. Sharp half-error barrier

固定 \(L\) 时，bounded-composition coefficient满足

\[
T=[z^n](1+z+\cdots+z^L)^M.
\tag{19}

当 \(M/n\to\alpha\) 时，标准 saddle-point estimate给

\[
\frac1n\log T\longrightarrow s_L(\alpha).
\tag{20}

随 \(L\to\infty\)，monotone convergence或截断后的saddle equation给

\[
s_L(\alpha)\uparrow
s(\alpha):=(1+\alpha)\log(1+\alpha)-\alpha\log\alpha.
\tag{21}

要求某一指定 coordinate为正只损失一个非指数因子。精确地，由坐标对称性和
每个 \(y\in\mathcal T_{n,M,L}\) 满足 \(|\operatorname{supp}(y)|\ge n/L\)，

\[
T_{n,M,L}(i)
=\frac1M\sum_{y\in\mathcal T_{n,M,L}}|\operatorname{supp}(y)|
\ge\frac{n}{LM}T.
\tag{21a}
\]

因此固定 \(L\) 时，式 (20)--(21)也适用于 \(T_{n,M,L}\)。由式 (15)、
Lemmas 5.1--5.2，并先固定 \(L\)、再让
\(n\to\infty\)、
最后令 \(L\to\infty\)，得到：

### Theorem 6.1（random-linear simplex barrier）

设 \(p_n\to\infty\)，\(M/n\to\alpha\)，并且 uniform random-linear global
syndrome filter在load \(n\) 有固定正拒绝率。则

\[
\boxed{
H\ge s(\alpha)n-o(n).
}
\tag{22}

另一方面，任何 fingerprint-coordinate filter都满足 collision ceiling

\[
\Pr[\mathrm{reject}]
\le\left(1-\frac1M\right)^n
\longrightarrow e^{-1/\alpha},
\tag{23}

因为query coordinate若已有 member，zero false negatives强迫 `YES`。在 half
error下，拒绝率至少 \(1/2\)，故

\[
\alpha\ge\frac1{\ln2}.
\tag{24}

函数 \(s(\alpha)\) 严格递增。结合 Theorems 3.2和6.1，得到：

### Corollary 6.2（all random finite-field linear sketches at half error）

对任意 prime sequence \(p_n\) 和 uniform random
\(A_n\in\mathbb F_{p_n}^{r_n\times M_n}\)，若上述 filter满足 zero false
negatives、load-\(n\) pointwise FPR至多 \(1/2\)，以及fixed worst-case memory，
则 bounded \(p_n\) subsequence不可能存在；并且

\[
\boxed{
H\ge
\left[
\left(1+\frac1{\ln2}\right)
\log\left(1+\frac1{\ln2}\right)
-\frac1{\ln2}\log\frac1{\ln2}
\right]n-o(n)
}
\tag{25}
\]

即

\[
\boxed{
H\ge2.384499842479\ldots n-o(n).
}
\tag{26}

这个常数正是枚举所有 weak compositions在最佳 fingerprint collision load下的
rate。random linear quotient若想保持 constant rejection，必须在指数尺度上退回
这个完整composition barrier。

## 7. 含金量与边界

### 7.1 这条结论真正排除了什么

1. **Fixed-field LDPC/global parity checks。** 无论sparsity、girth或degree
   distribution如何，bounded exponent先触发mass-transfer saturation。
2. **Dense random matrices over growing fields。** 只要syndrome range小于
   bounded-composition family的指数规模，几乎每个query都有同syndrome witness；
   若把range做大，reachable image本身又需要完整composition rate。
3. **“只算 \(r\log p\)”和“只算reachable states”两个相反漏洞。** Lemma 4.1
   用前者控制collision，Lemma 5.1再把它严格转换为后者。
4. **Exact global cardinality。** 全部witness从一开始就保持load \(n\)，所以
   exact total load不能排除它们。

### 7.2 它没有证明什么

本文不覆盖：

- 精心设计的 deterministic large-characteristic matrices；
- 非域的unbounded-exponent groups，除非另行证明相应random homomorphism lemma；
- nonlinear canonical quotients；
- history-dependent multiple representations或randomized transitions；
- query使用额外key-dependent public labels；
- arbitrary ordinary dynamic AMQ。

因此不能把式 (26)称为FOCS 2025 fixed-error问题的lower bound。它是一条
broad-class no-go theorem：严格关闭了cross-block additive路线中最标准的
fixed-field和random-linear两端。

## 8. 下一步真正值得做的问题

剩下最有taste的正面问题不是继续随机搜索矩阵，而是证明或反驳：

> **Designed-lattice sharp problem.** 在全部保持total load的lattices
> \(L_n\le A_{M-1}\) 中，minimal one-sided query具有half rejection时，最小
> fixed-state rate是否恰为 \(2.349083440193\ldots\)，由binary order-3
> block-product lattice达到？

不能猜测所有designed lattices都满足式 (22) 的 \(2.3845n\) barrier：现有
order-3 threshold construction本身就是高度设计的lattice，并以
\(2.349083n\) 严格反驳该过强命题。正确目标是证明没有designed cross-block
lattice能进一步低于 \(2.349083n\)，或者找到一个反例。反例必须是高度非随机、
support-overlap-friendly的lattice packing；它本身就会给出最可信的新构造候选。

所需核心不等式可以写成weighted lattice-coset clustering形式。对fixed-load
composition classes \(C\)，令 \(U(C)\) 为class内supports的union。需要把

\[
\sum_C W(C)|U(C)|
\]

与quotient image大小直接联系，并利用所有classes来自同一个lattice，而不是任意
partition。这是当前最小、最清楚、同时具有正反两种论文产出的开放命题。
