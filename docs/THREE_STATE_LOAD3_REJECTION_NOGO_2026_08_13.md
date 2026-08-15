# 三状态 load-3 positive rejection 的严格 no-go

> 日期：2026-08-13。状态：解析定理。允许 history dependence、每个 logical
> composition 多 representations、nontransitive fibers，以及 independent public
> mixture of local transducers。主结论进一步分类全部三状态 infinite tail；
> 它否决形式 profile
> \((d_0,d_1,d_2,d_3,\ldots)=(1,2,3,3,\ldots)\) 在保留
> \(\rho_2=1/4\) 的同时取得任意 \(\rho_3>0\)。

## 1. 模型与量词

考虑 exact-load binary local summary。每个 operation key有独立均匀 symbol
\(b\in\{0,1\}\)。public seed \(R\) 独立于这些 symbols；固定 \(R=r\) 后，
local machine deterministic，具有 load layers \(Q_c(r)\) 与 maps

\[
I_{r,b}:Q_c(r)\to Q_{c+1}(r),
\qquad
D_{r,b}:Q_c(r)\to Q_{c-1}(r).
\tag{1}
\]

maps只读取 local state与 operation symbol。它们只需在相应 hidden logical
composition中 operation合法时保持正确。允许同一 composition由多个 states表示，
也允许一个 state兼容多个 compositions；不要求 insert/delete互逆或不同 insertion
orders汇合。

query读取 state与 query symbol，zero false negatives在每条 seed上成立。假设

\[
|Q_2(r)|\le3,
\qquad
|Q_3(r)|\le3
\tag{2}
\]

对几乎每个 seed成立。

对任意 fixed two-key history，令 \(\operatorname{Rej}_2\) 是对两个 member
symbols、fresh query symbol和 \(R\) 平均的 rejection probability。one-sidedness
总给

\[
\operatorname{Rej}_2\le\frac14.
\tag{3}
\]

## 2. Load-2 equality rigidity

### Lemma 2.1

若每条 fixed two-key history都达到

\[
\operatorname{Rej}_2=\frac14,
\tag{4}
\]

则对几乎每个 \(r\)，\(Q_2(r)\) 恰有三个 relevant states

\[
q_{00},\quad q_{01},\quad q_{11},
\tag{5}
\]

并且每个 reachable load-2 state只兼容相应 one-count \(0,1,2\) 中的一个。
特别地，任意 insertion order和任意 earlier legal history只要 endpoint one-count
相同，都只能落入式 (5) 的相应 state。

**证明。** 固定 seed。load 2 的 rejection只可能来自两个原子：member symbols
为 `00` 且 query symbol为 `1`，或 member symbols为 `11` 且 query symbol为
`0`。每个原子概率 \(1/8\)，所以式 (3) 的上限是 \(1/4\)。

对 seed先条件化。每个 seed的平均 rejection仍至多 \(1/4\)，故式 (4) 强迫几乎
每个 seed都取等；进一步，两种 pure原子都必须被拒绝。于是任何表示 `00` 的
reachable state必须拒绝 symbol `1`，任何表示 `11` 的 state必须拒绝 symbol
`0`。表示 mixed composition的 state由 zero-FN必须接受两个 symbols，因而不能与
任一 pure composition共享。两个 pure compositions也不能共享同一 state。因此
三类各至少占一个 state。由 \(|Q_2|\le3\)，每类恰有唯一 state，且不存在额外
representation。\(\square\)

这里 public mixture没有提供自由度：因为式 (3) 是逐 seed都成立的 hard ceiling，
平均取等强迫 almost-sure取等。

## 3. Common-deletion separation

固定 seed \(r\)。用 \(k\in\{0,1,2,3\}\) 表示 load-3 composition中的
one-count。

### Lemma 3.1

若一个 state \(s\in Q_3(r)\) 同时兼容不同 compositions \(k<\ell\)，则必有

\[
\{k,\ell\}=\{0,3\}.
\tag{6}
\]

**证明。** 除 \(0\) 与 \(3\) 外，任意两个 binary load-3 compositions都有
共同出现的 symbol \(b\)。在两个 compatible worlds中各删除一个 symbol为 \(b\)
的 key。从同一物理 state执行同一个 deterministic map \(D_{r,b}\)，所得 state
相同。但两个 successor one-count仍不同：若 \(b=0\) 则仍为 \(k,\ell\)，若
\(b=1\) 则为 \(k-1,\ell-1\)。这与 Lemma 2.1 中三个 load-2 compositions的
state唯一性矛盾。\(\square\)

这个证明直接作用于 relational fibers，不使用 overlap transitivity或 canonical
section。

## 4. 主定理

先给一个更强的 quantitative form。固定三个 distinct operation keys
\(x_1,x_2,x_3\) 及其 insertion order。对 \(i\in\{1,2,3\}\)，令
\(H_i\) 是插入三键后删除 \(x_i\) 的 fixed history。记 \(\rho_3(r)\) 为在
删除前对三个 member symbols与 fresh query symbol平均的 rejection，
\(\rho_2^{(i)}(r)\) 为 \(H_i\) 后的相应平均；三键中被删除 key的 symbol仍参与
平均。

### Theorem 4.1（sharp leave-one-out tradeoff）

若 \(|Q_3(r)|\le3\)，则对每条 deterministic seed与每个 \(i\)，

\[
\boxed{
\rho_2^{(i)}(r)+\rho_3(r)\le\frac14.
}
\tag{7}
\]

所以对任意 independent public mixture也有

\[
\boxed{
\mathbb E_R\rho_2^{(i)}(R)+
\mathbb E_R\rho_3(R)\le\frac14.
}
\tag{8}
\]

**证明。** 乘以 \(16\)，把每个 complete member/query bit assignment看成一个
unit。load 3至多有两个可拒绝 units：`000` 后 query `1`，以及 `111` 后 query
`0`。记实际被拒绝的 pure units数为 \(a\in\{0,1,2\}\)，所以
\(16\rho_3=a\)。

删除 \(x_i\) 后，load 2至多有四个可拒绝 units：remaining bits为 `00` 或
`11`，而 deleted bit可以是 `0` 或 `1`。下面证明 load-3每拒绝一个 pure unit，
这四个 units中至少一个必不能拒绝；两种 load-3 pure units造成的损失位于不相交
的 deleted-bit slices。

若 `000/query 1` 在 load 3被拒绝，则表示 `000` 的 top state不能兼容任何含
`1` 的 word，因而是 singleton fiber。考虑 deleted bit为 `1` 的 slice。若
remaining `00/query 1` 与 remaining `11/query 0` 两个 leave-one-out pure
units都被拒绝，则其 top states必须不同；再加 singleton `000` 已用完三个 top
states。但该 slice中 remaining bits为 `01` 与 `10` 的另外两个 words必须落入
后两个 top states之一。对它们执行同一个 \(D_1\) 后，successor含两种 symbols，
zero-FN强迫接受两个 query bits，与对应 pure unit的拒绝矛盾。因此该 slice至少
损失一个 unit。

对称地，若 `111/query 0` 在 load 3被拒绝，则 deleted bit为 `0` 的 slice至少
损失一个 load-2 pure unit。这两个 slices disjoint，故 load-2至多拒绝
\(4-a\) units：

\[
16\rho_2^{(i)}\le4-a=4-16\rho_3.
\]

即得式 (7)。对 \(R\) 平均给式 (8)。\(\square\)

三状态 depth-3 endpoint/deletion relaxation中，等号 points

\[
(\rho_2,\rho_3)=(1/4,0),\quad(3/16,1/16),\quad(1/8,1/8)
\tag{9}
\]

均可达到。因此式 (7) 的系数不能只靠同一个 leave-one-out局部约束改善。这里不
声称每个 equality point都能延拓成支持任意长 histories 的完整 automaton。

### Corollary 4.2（three-state load-3 no-go）

在 Sections 1--2 的条件下，每个 reachable load-3 state都对两个 query symbols
回答 `YES`。因此对任意 fixed load-3 history，

\[
\boxed{\operatorname{Rej}_3=0.}
\tag{10}
\]

特别地，不存在满足

\[
(d_0,d_1,d_2,d_3,\ldots)=(1,2,3,3,\ldots),
\quad
\rho_2=\frac14,
\quad
\rho_3>0
\tag{11}
\]

的 public-mixture、history-dependent binary exact-load local right
congruence。

**证明。** 四个 load-3 compositions都由某些 histories到达。由 Lemma 3.1，
一个 state若兼容两个不同 compositions，唯一可能的 pair是 \(\{0,3\}\)。mixed
compositions \(1\) 与 \(2\) 各自至少需要一个不同 state。由于总共至多三个
states，剩下唯一 state必须同时兼容 pure-zero与pure-one compositions。

zero-FN于是强迫该 state接受两个 query symbols。表示 compositions \(1,2\) 的
states本来就因两种 symbols均出现而必须接受两个 query symbols。所以全部
load-3 states均为 ALL-YES，给出式 (10)。论证对几乎每个 seed分别成立，再对
public mixture平均仍为零。\(\square\)

multiple representations也不能绕过计数：如果任一 composition另有 state，mixed
compositions仍各需独占一个 state，而任何与它共享 state的另一个 composition
都违反 Lemma 3.1；三状态预算立即不足。

## 5. 对候选 `2.3055` upper bound 的裁决

形式 profile

\[
d_c=(1,2,3,3,\ldots),
\qquad
\rho_0=1, \rho_1=1/2, \rho_2=1/4, \rho_3=1/8
\tag{12}
\]

代入 Poisson FPR与 OGF saddle可能产生约 `2.3055` bits/key，但式 (12) 不可由
上述任何真实 local right congruence实现。问题不是 tail OGF 或数值校准，而是
cross-layer deletion compatibility：load 2 的取等状态已经把三个 compositions
完全分离，load 3 的一次 state saving只能合并两个 disjoint-support endpoints，
恰好消灭全部 pure-case rejection。

更一般地，只要 global construction声称 \(\rho_2=1/4\) 是逐 fixed history的
保证，public tapes之间的 reliability allocation也无效，因为每条 tape的 load-2
rejection都受同一个 \(1/4\) ceiling。Theorem 4.1进一步刻画允许
\(\rho_2<1/4\) 时的 sharp depth-3交易。对 Poisson mean \(\lambda<3\)，把固定
budget从 \(\rho_2\) 移到 \(\rho_3\) 不会改善 rejection，因为两项权重分别为

\[
e^{-\lambda}\frac{\lambda^2}{2}\rho_2,
\qquad
e^{-\lambda}\frac{\lambda^3}{6}\rho_3,
\]

而后者每单位只有前者的 \(\lambda/3<1\) 倍。因此在 order-3 construction相关的
\(\lambda\approx1.326\) 区域，sharp tradeoff本身把 optimum推回
\((\rho_2,\rho_3)=(1/4,0)\)，而不只是排除单个 \(1/8\) 猜测。

## 6. 全层 rigidity

前面的三层论证实际上可以推广到任意长 history，并完全分类三状态 tail。

对 load \(c\) 和 one-count \(k\in\{0,\ldots,c\}\)，令

\[
R_{c,k}(r)\subseteq Q_c(r)
\tag{13}
\]

为所有 endpoint composition为 \((c-k,k)\) 的合法 histories可到达的 states。
它允许 arbitrary multiple representations。

### Theorem 6.1（three-state tail rigidity）

假设对几乎每个 public seed

\[
|Q_c(r)|\le3\qquad(c\ge2),
\tag{14}
\]

并且每条 fixed load-2 history在对 \(R\)、member symbols与 query symbol平均后
达到 rejection \(1/4\)。则对几乎每个 seed及所有 \(c\ge2\)，存在恰好三个
states \(q_{c,0},q_{c,1},q_{c,2}\)，满足

\[
\boxed{
R_{c,k}(r)=\{q_{c,k\bmod3}\}
\qquad(0\le k\le c).
}
\tag{15}
\]

换言之，即使允许 history dependence与multiple representations，完整 infinite
tail仍被强迫为 one-count modulo 3 的 canonical quotient。特别地，

\[
\boxed{
\rho_c=0\qquad(c\ge3).
}
\tag{16}

**证明。** 先取所有 fixed load-2 histories的 countable intersection。由逐 seed
hard ceiling \(1/4\) 及平均取等，Lemma 2.1 对几乎每个 seed同时适用于全部这些
histories。因此式 (15) 在 \(c=2\) 成立。

对 \(c=3\)，mixed compositions \(k=1,2\) 不能共享 state：共同删除一个 `0`
会分别落到唯一的 load-2 states \(q_{2,1},q_{2,2}\)。boundary composition
\(k=0\) 不能与任一 mixed state共享，因为 \(D_0\) 会落到不同的 load-2 state；
同理 \(k=3\) 不能与 mixed state共享。三状态预算于是强迫 \(k=0,3\) 共享第三
state。这正是 residue classes modulo 3，所以 base \(c=3\) 成立。

现在设式 (15) 对 layer \(c-1\) 成立，其中 \(c\ge4\)。考虑所有 mixed
compositions

\[
k=1,2,\ldots,c-1.
\]

若 \(s\in R_{c,k}\)，删除一个 `0` 合法，且

\[
D_0(s)=q_{c-1,k\bmod3}.
\tag{17}
\]

因此 residues不同的 mixed compositions不能共享 state。由于区间
\(1,\ldots,c-1\) 在 \(c\ge4\) 时包含全部三个 residues，这些 mixed
compositions已强迫三个不同 states；由式 (14)，它们恰为
\(q_{c,0},q_{c,1},q_{c,2}\)，且每个 mixed composition只能落到对应 residue
state。这一步同时排除了 mixed compositions的额外 representations。

若 \(s\in R_{c,0}\)，则 \(D_0(s)=q_{c-1,0}\)。但对刚才定义的 top state
\(q_{c,r}\)，任取一个 residue为 \(r\) 的 mixed witness，式 (17) 给
\(D_0(q_{c,r})=q_{c-1,r}\)。故 \(s=q_{c,0}\)。同理，若
\(s\in R_{c,c}\)，删除一个 `1` 给

\[
D_1(s)=q_{c-1,(c-1)\bmod3}.
\]

而 mixed residue-\(r\) witness给

\[
D_1(q_{c,r})=q_{c-1,(r-1)\bmod3},
\]

所以唯一可能是 \(s=q_{c,c\bmod3}\)。归纳完成式 (15)。

当 \(c\ge3\) 时，每个 modulo-3 residue class在 \([0,c]\) 中的 compositions
union都包含 symbol `0` 与 symbol `1`：interior class本身含 mixed composition，
而含 pure endpoint的 class还包含与其相差 3 的 composition。minimal one-sided
rule因此在三个 states上都接受两种 query symbols，得到式 (16)。\(\square\)

### Corollary 6.2（public reliability allocation 不能制造 tail）

在 Theorem 6.1 的条件下，不存在通过不同 tapes选择不同 load layers来拒绝的
方案。load-2 的平均 ceiling取等已经逐 seed固定了整个 infinite transition
tail；因此对任意 Poisson weights \(a_c\ge0\)，

\[
\sum_{c\ge2}a_c\rho_c
=a_2\rho_2
=\frac{a_2}{4}.
\tag{18}
\]

特别地，这比仅在 \(\lambda<3\) 下证明 weighted inequality更强：对任意
\(\lambda>0\)，取 \(a_c=\lambda^c/c!\) 都严格没有 tail compensation。

## 7. 边界

Theorems 4.1、6.1 与相应 corollaries 覆盖：

- arbitrary history dependence与multiple representations；
- nontransitive composition-state overlaps；
- deterministic local transitions的 independent public mixture；
- 任意长 histories，因为证明只使用模型本身保证的合法 common deletion；
- 每条 seed的 exact load layers与 zero-FN。

它不覆盖：

- local transition/query读取 key identity或未计费的其他 public hash bits；
- automaton seed与被操作 keys的 binary labels相关；
- cross-block global states，其“local \(d_c\)”不是一个真正 state-layer上界；
- simultaneous cross-block state sharing，其 local三状态预算无法单独定义。

因此安全结论是：`rho3=1/8` 的直接 upper leap严格不存在于所提出的 binary
exact-load local right-congruence模型。更强地，只要 load-2 rejection保持
\(1/4\) 且每层至多三个 states，整个 tail唯一是 modulo-3 quotient。若要低于
`2.349083`，必须牺牲 lower-layer rejection、扩大某层 state count、扩大 local
alphabet，或使用真正 cross-block / tape-dependent structure。
