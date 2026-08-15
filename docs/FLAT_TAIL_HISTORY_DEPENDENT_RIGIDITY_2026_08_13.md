# Binary exact-load transducer 的 flat-tail rigidity

> 日期：2026-08-13。状态：解析结构定理。覆盖 arbitrary history dependence、
> multiple representations、nontransitive fibers 与 independent public mixture。
> 结论：若低负载层以最小状态数保持 maximal rejection，而高负载 tail不增加
> states，则整个无限 automaton 必须是 canonical modulo quotient。因而这类
> noncanonical/right-congruence尝试不能改善 `2.349083`。

## 1. 模型

固定 public seed后，binary exact-load local transducer有 load layers \(Q_c\) 和

\[
I_b:Q_c\to Q_{c+1},
\qquad
D_b:Q_c\to Q_{c-1},
\qquad b\in\{0,1\}.
\tag{1}
\]

它支持任意长合法 histories。允许：

- 同一 binary composition由多个 states表示；
- 不同 compositions共享 state；
- insert/delete不互逆；
- insertion order产生 holonomy；
- overlap relation不传递。

对 load \(c\) 和 one-count \(k\in\{0,\ldots,c\}\)，令

\[
R_{c,k}\subseteq Q_c
\tag{2}
\]

为所有 endpoint composition为 \((c-k,k)\) 的合法 histories可到达的 states。

fresh uniform query bit的 universal one-sided rejection ceiling为

\[
\rho_c^{\max}=2^{-c}.
\tag{3}
\]

只有 pure-zero/query-one 与 pure-one/query-zero两个原子可以被拒绝。

## 2. Saturated prefix rigidity

### Lemma 2.1

设 \(L\ge1\)。若对每个 \(0\le c\le L\)：

1. \(|Q_c|\le c+1\)；
2. 每条 fixed load-\(c\) history达到 rejection ceiling \(2^{-c}\)；

则存在恰好 \(c+1\) 个 states \(q_{c,0},\ldots,q_{c,c}\)，并且

\[
\boxed{R_{c,k}=\{q_{c,k}\}.}
\tag{4}
\]

**证明。** 对 \(c\) 归纳。\(c=0\) 平凡。假设 layer \(c-1\) 已唯一表示每个
one-count。

若 \(0\le k<\ell\le c\) 共享 state：

- 除非 \(\{k,\ell\}=\{0,c\}\)，两 compositions共享某个 symbol \(b\)。共同
  删除一个 \(b\) 后，deterministic map \(D_b\) 给同一 successor state，但
  successor one-count不同，违反归纳唯一性。
- 若 \(k=0,\ell=c\)，shared state同时兼容 pure zero与pure one，zero-FN强迫
  对两种 query bits都回答 YES。这会使相应 fixed pure history达不到式 (3)。

故 \(c+1\) compositions必须占据不同 states。由 \(|Q_c|\le c+1\)，每类唯一且
没有额外 representation。\(\square\)

若 public mixture的平均 rejection达到逐 seed hard ceiling，则 equality迫使上述
性质在 almost every seed上成立。因此 global reliability allocation不能绕过
Lemma 2.1。

## 3. Flat-tail theorem

### Theorem 3.1（history-dependent flat tail is modulo \(q\)）

固定整数 \(q\ge2\)。假设：

1. 对 \(0\le c<q\)，每条 history达到 maximal rejection \(2^{-c}\)，且
   \(|Q_c|\le c+1\)；
2. 对所有 \(c\ge q-1\)，\(|Q_c|\le q\)。

则对每个 \(c\ge0\) 存在 states

\[
q_{c,0},\ldots,q_{c,\min(c,q-1)}
\]

使得

\[
\boxed{
R_{c,k}=\{q_{c,k\bmod q}\}
\qquad(0\le k\le c).
}
\tag{5}

因此该 relational transducer在 reachable states上与保存 one-count modulo \(q\)
完全等价；特别地

\[
\rho_c=
\begin{cases}
2^{-c},&c<q,\\
0,&c\ge q.
\end{cases}
\tag{6}

**证明。** Lemma 2.1给出式 (5) 到 layer \(q-1\)。

考虑 layer \(c=q\)。compositions \(k=1,\ldots,q-1\) 通过共同删除 `0` 映到
上一层不同 states \(q_{q-1,k}\)，故彼此不能共享 state。boundary \(k=0\)
也由 \(D_0\) 与它们分离；boundary \(k=q\) 由 \(D_1\) 与它们分离。共有
\(q+1\) compositions却至多 \(q\) states，所以唯一允许的合并是 \(k=0,q\)。
这正是 modulo \(q\) classes。

归纳设式 (5) 在 layer \(c-1\) 成立，其中 \(c\ge q+1\)。mixed compositions

\[
k=1,\ldots,c-1
\]

包含全部 \(q\) residues modulo \(q\)。对 \(s\in R_{c,k}\)，删除一个 `0`
给

\[
D_0(s)=q_{c-1,k\bmod q}.
\tag{7}
\]

所以不同 residues不能共享 state。mixed compositions已经占满恰好 \(q\) 个
states，并且不能有额外 representations。

对 pure-zero state \(s\in R_{c,0}\)，式 (7) 的 output是
\(q_{c-1,0}\)，在刚才的 \(q\) 个 top states中只有 residue-zero state具有该
\(D_0\) output，故 \(s=q_{c,0}\)。对 pure-one同理使用 \(D_1\)：只有 residue
\(c\bmod q\) 的 top state映到 \(q_{c-1,(c-1)\bmod q}\)。归纳完成。

当 \(c\ge q\)，每个 residue class在 \([0,c]\) 内的 composition union都包含
两种 symbols：mixed class显然如此；含 pure endpoint的 class还含相差 \(q\) 的
另一个 composition。minimal one-sided query因此在所有 states上ALL-YES，得到
式 (6)。\(\square\)

## 4. 对 half-error rate 的推论

上述 theorem覆盖一个自然且明显大于 canonical constructions 的类：local
machine可以 history-dependent、multiple-represented、noninvertible，只约束每层
state count和低层 rejection达到其 information-theoretic ceiling。

在 uniform outer Poisson blocks中，这个类的每个 component仍只能产生 threshold
profile

\[
d_c=\min(c+1,q),
\qquad
\rho_c=2^{-c}\mathbf1\{c<q\},
\tag{8}
\]

其 local OGF为

\[
A_q(z)=\frac{1-z^q}{(1-z)^2}.
\tag{9}

已有全整数优化证明：在 \(\varepsilon=1/2\) 时，所有 \(q\ge2\) 中唯一最优是

\[
q=3,
\qquad
R=2.349083440193\ldots\text{ bits/key}.
\tag{10}

所以在 flat-tail minimal-layer类中，history dependence和multiple
representations严格不能改善已知 upper bound。

## 5. 这一定理排除了什么

它排除：

1. 保留 load \(0,1,2\) 的全部 rejection，却在三状态 tail中加入 positive
   load-3/4/... rejection；
2. 对任意 \(q\)，保留 exact/maximal low-load behavior，再利用 nontransitive
   overlaps把 flat \(q\)-state tail做得优于 modulo \(q\)；
3. 用 different public tapes轮流选择 tail rejection layer，同时让 saturated
   prefix在平均上取等；hard ceiling取等会逐 seed触发同一个 rigidity；
4. 通过同一 composition的额外 representations获得免费 tail selectivity；flat
   state budget已被 mixed residue classes占满。

## 6. 真正仍开放的上界分叉

要严格低于 `2.349083`，至少必须违反以下一项：

1. **低层 tradeoff：** 牺牲某些 load-\(c<q\) histories的 rejection，换取后续
   layers rejection；需要完整 weighted cross-layer frontier，而非单层 profile。
2. **非平坦 state counts：** 某些高层使用超过 \(q\) states，随后在更高层重新
   合并；必须证明增加的 OGF cost被 rejection收益超过。
3. **cross-block state sharing：** global physical state不能分解成 local load
   layers，故 \(d_c\) 不再是合法预算。
4. **额外 alphabet/query-dependent sketch：** binary symbol与single local
   automaton前提失效。
5. **tape-dependent labels：** local update/query读取未计费的其他 public tape
   information；这需要重新处理 pointwise-history量词。

前两项仍属于 local right-congruence搜索，但不能再从保持 lower layers不变的
“免费 tail改良”开始。第三项影响最大，也最难：它必须给出一个真正 global
finite-state quotient，而不是只列不可联合实现的局部 \((d_c,\rho_c)\) profile。

## 7. 裁决

本轮没有得到小于 `2.349083` 的 ordinary everlasting construction。得到的严格
no-go是：在所有 saturated-prefix、flat-tail binary exact-load transducers中，
arbitrary history dependence与multiple representations不会扩大可实现的
rate/FPR region；每个 machine都被强迫回 modulo threshold quotient。

因此下一次可信的构造尝试应直接优化“低层 rejection牺牲 + 非平坦 state growth”
或真正 cross-block quotient。继续在三状态 tail中寻找 hidden positive rejection
已被 Theorem 3.1 完全关闭。
