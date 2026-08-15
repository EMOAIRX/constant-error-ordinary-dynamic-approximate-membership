# Bounded source-section influence 下的自然宇宙 endpoint 下界

> 日期：2026-08-15。状态：条件结构定理。本文把 ordinary dynamic AMQ 的
> endpoint batch converse 从 `u/n^2 -> infinity` 降到 `u/n -> infinity`，但不把
> source-union completeness 本身误当成充分条件。新增的结构假设是：KLZ source
> witnesses 覆盖完整 operational union，并且逐个 fresh suffix insertion 对该
> witness cover 的 section influence 一致有界。

所有对数以 2 为底。

## 1. 模型与结论

考虑容量为 `n`、宇宙大小为 `u` 的 ordinary one-sided dynamic approximate
membership filter：

- persistent memory 是固定的 `H`-bit block；
- 可读取免费只读 public random tape；
- 支持 key-only legal `Insert/Delete/Query`；
- 每条 tape 上 zero false negatives；
- 对每条预先固定且与 random tape 独立的合法 history、每个固定 current
  nonmember，FPR 至多固定 `epsilon in (0,1/2]`；
- 支持确定 horizon `f(n)`，其中 `f(n)/n -> infinity`。

本文只要求

\[
\frac un\longrightarrow\infty.
\tag{1}
\]

定义

\[
C_{\rm end}(\varepsilon)
=\min_{0<x<1}\max\left\{
\log\frac1{\varepsilon x},
(1-\varepsilon x)
\log\frac{1-\varepsilon x}{\varepsilon(1-x)}
\right\}.
\tag{2}
\]

主结果是：在 Section 3 的 bounded source-section influence 假设下，

\[
\boxed{H\ge C_{\rm end}(\varepsilon)n-o(n).}
\tag{3}
\]

特别地，当 `epsilon=1/2` 时，

\[
\boxed{
H\ge1.434406361243753\ldots n-o(n).
}
\tag{4}
\]

这个进展不是增加有限 pivot/block 数。它保留已有的两端点解析变分，只改变
transport 的结构接口与 universe 范围。

## 2. Partition-free operational fiber

固定 tape `r`、physical state `m`、logical load `t` 和 exact operation time `q`。
定义完整 endpoint fiber

\[
\mathcal O_r(m,t,q)
=\{S(h): |h|=q,\ |S(h)|=t,\ M_r(h)=m\},
\tag{5}
\]

其中只遍历从空集出发、处于承诺 horizon 内的合法 histories。其 union 为

\[
W_r^{\rm op}(m,t,q)
=\bigcup_{S\in\mathcal O_r(m,t,q)}S.
\tag{6}
\]

它不引用 KLZ random partition。Zero false negatives 给

\[
W_r^{\rm op}(m,t,q)\subseteq A_r(m),
\tag{7}
\]

其中 `A_r(m)` 是 state `m` 的 YES-set。

运行 KLZ obfuscating-tree source。对一次 endpoint-pivot
`Send(X_k,F_r,G_ell)`，`G_ell` 在 hidden future batch `X_k` 插入前结束，
`F_r` 由 `G_ell` 后的 concrete self-contained suffix 到达。令该 suffix 中的
distinct insertion labels 按首次出现次序为

\[
Y=(Y_1,\ldots,Y_q).
\tag{8}
\]

Suffix 中的每个 deletion 都匹配 suffix 自己更早的 insertion；所以任一 parent
endpoint set只要与 `{Y_1,...,Y_q}` 不交，整个 suffix 就合法，且不会删除任何
parent member。

## 3. Bounded source-section influence

固定 KLZ cut 时已经暴露的 public data、tape、parent physical state、load 与 exact
time，但不暴露 future suffix labels。令

\[
\mathcal P^{\rm src}_{\rm cut}
\subseteq\mathcal O_R(G_\ell,t_\ell,q_\ell)
\]

是所有与该 cut data 相容、到达同一 parent state 的 KLZ source-prefix endpoints。
一个 **source witness cover** 是一个在该 cut 时已经固定的 family

\[
\mathcal C\subseteq\mathcal P^{\rm src}_{\rm cut}
\subseteq\mathcal O_R(G_\ell,t_\ell,q_\ell)
\tag{9}
\]

满足：

1. actual source endpoint 属于 `C`；
2. `C` 的 union 覆盖完整 operational union：
   \[
   \bigcup_{S\in\mathcal C}S
   =W_R^{\rm op}(G_\ell,t_\ell,q_\ell).
   \tag{10}
   \]

对 distinct label set `J` 定义 section

\[
\mathcal C[J]
=\{S\in\mathcal C:S\cap J=\varnothing\},
\qquad
W_{\mathcal C}[J]
=\bigcup_{S\in\mathcal C[J]}S.
\tag{11}
\]

令 `J_i={Y_1,...,Y_i}`。actual endpoint 与整个 insertion set 不交，所以所有
`C[J_i]` 都非空。

### Definition 3.1（bounded source-section influence, BSSI）

若对每个固定 KLZ depth `b`，存在只依赖 `b` 的有限常数 `kappa_b`，使全部 endpoint
pivot cuts 都可选择满足 (9)--(10) 的 source witness cover，并且对每个 suffix
insertion step

\[
\boxed{
\mathbb E\left[
|W_{\mathcal C}[J_{i-1}]\setminus
  W_{\mathcal C}[J_i]|
\mid\mathscr F_{i-1}
\right]
\le\kappa_b,
}
\tag{12}
\]

则称 filter 具有 BSSI。这里 `\mathscr F_{i-1}` 包含 cut data 和已经揭示的
`Y_1,...,Y_(i-1)`，但不包含 `Y_i`；cover `C` 不能在看见 `Y_i` 后重选。

更强而易检查的 pointwise 条件

\[
|W_{\mathcal C}[J]\setminus W_{\mathcal C}[J\cup\{y\}]|
\le\kappa_b
\tag{13}
\]

显然推出 (12)。

BSSI 不要求：

- history independence 或 canonical representation；
- source posterior 在 support 上均匀；
- 一个 endpoint 只有一个 physical representation；
- update actions commute；
- query YES-sets 沿 history 单调；
- locality、exact multiplicity recovery 或无 ghosts。

它只排除一种具体机制：一个 fresh insertion label 通过杀掉少量或极低 posterior
mass 的最后 witnesses，使 operational union 同时失去无界多个其他 keys。

典型边界例：

- 若一个 state 的 operational fiber 是 singleton，则可取 `kappa_b=0`；
- 若 witness family 是某个 ground set上的全部定大小 subsets，则排除一个 label
  只会从 union 中删除该 label，可取 `kappa_b=1`；
- source-invisible operational ghosts违反 (10)；
- rare-witness avalanche 可满足 (10)，但违反 (12)。

## 4. BSSI transport lemma

### Lemma 4.1（linear source-section transport）

在 Definition 3.1 下，对任一相关 `G_ell -> F_r` suffix，

\[
\boxed{
\mathbb E
|W_R^{\rm op}(G_\ell)\setminus W_R^{\rm op}(F_r)|
\le\kappa_b q.
}
\tag{14}
\]

### Proof

由 (12) telescoping，

\[
\mathbb E
|W_{\mathcal C}[\varnothing]\setminus W_{\mathcal C}[J_q]|
\le\kappa_b q.
\tag{15}
\]

取任意 `x in W_C[J_q]`。存在 `S in C[J_q]` 含 `x`。因为
`S \cap J_q=\varnothing`，concrete suffix 对 witness history `S` 全程合法。固定 tape
后的 transition deterministic，所以该 witness 从同一个 `G_ell` 到达与 actual
execution相同的 `F_r`。Suffix self-contained，故 `x` 仍是 successor member；于是

\[
W_{\mathcal C}[J_q]
\subseteq W_R^{\rm op}(F_r).
\tag{16}
\]

再用 (10) 与 (15) 即得 (14)。`F_r` 还可能有额外 source 或 operational witnesses；
它们只扩大右侧 union，不会改变方向。\(\square\)

这一步没有 entropy deficit，也没有把 `G_ell` 的 endpoint posterior 与
`F_r` 的 hidden-batch posterior混为一谈。

## 5. 自然宇宙参数窗口

对固定 depth `b`，KLZ tree 中任一相关 self-contained suffix 的 distinct insertion
数至多

\[
q\le c_b n,
\tag{17}
\]

总 operation 数与 exposed labels 也至多 `c'_b n`，其中 `c_b,c'_b` 对固定 `b`
是有限常数。令

\[
D_{n,b}=\kappa_b c_b n.
\tag{18}
\]

由 (14)，所有 endpoint pairs 的 expected full-fiber transport loss至多
`D_(n,b)`。因为

\[
\frac un\to\infty,
\qquad
\frac{f(n)}n\to\infty,
\tag{19}
\]

而对每个 fixed `b`，`kappa_b,c_b,c'_b` 都固定，可以作标准 diagonal choice
`b=b(n)->infinity`，使

\[
c'_b n=o(f(n)),
\qquad
b4^bD_{n,b}=o(u),
\qquad
4^bc'_bn=o(u).
\tag{20}
\]

因此 horizon、transport、partition exposure 与 falling-factorial corrections
可同时为 `o(n)`。这里没有使用 `u/n^2 -> infinity`。

## 6. Corrected full-fiber profile

令

\[
g_j=\mathbb E|W(G_j)|,
\qquad
N=(1-\varepsilon)n+\varepsilon u.
\tag{21}
\]

对每条 fixed source history，先对原 random tape 使用 pointwise FPR，再对 source
与partition平均，由 (7) 得

\[
g_j\le N.
\tag{22}
\]

定义

\[
\widehat g_j=g_j+jD_{n,b},
\qquad
\widehat N=N+bD_{n,b},
\qquad
x_j=\widehat g_j/\widehat N.
\tag{23}
\]

相邻 suffix 的 (14) 给

\[
0=x_0\le x_1\le\cdots\le x_b\le1.
\tag{24}
\]

对一次 `Send(X_k,F_r,G_ell)`，令

\[
G=W(G_\ell)\cap U_k,
\qquad
D=(W(F_r)\setminus W(G_\ell))\cap U_k.
\tag{25}
\]

两阶段 partition conditioning 与原 endpoint batch lemma相同：

1. 在不固定完整partition的第一条件场中，`W(G_ell)` 是 partition-free fixed set，
   可对尚未暴露的 balanced assignments 作有限总体平均；
2. 加入完整partition后，`X_k` 仍在 `U_k` 中均匀无放回，且 `G` 已固定。

由 (20)--(23)，得到一致的 first moments

\[
\frac{\mathbb E|G|}{V}
\le\varepsilon x_\ell+o(4^{-b}),
\tag{26}
\]

\[
\frac{\mathbb E|D|}{V}
\le\varepsilon(x_r-x_\ell)+o(4^{-b}),
\tag{27}
\]

其中 `V=u/b`。式 (27) 使用恒等式

\[
|W(F_r)\setminus W(G_\ell)|
=|W(F_r)|-|W(G_\ell)|
 +|W(G_\ell)\setminus W(F_r)|
\tag{28}
\]

以及 BSSI transport bound；没有把 source posterior union loss按 coefficient one
直接塞进 batch rank。

## 7. Exact batch code 与 endpoint reduction

令 hidden ordered batch长度为 `m=n/b`，并写

\[
Q=|\{i:X_{k,i}\notin G\}|,
\qquad
\alpha=\mathbb EQ/m.
\tag{29}
\]

联合编码完整 hit pattern、hit values 与 miss values 的 exact rank code给

\[
\mathcal C_k
\le
\log(V)_{\underline m}
+\mathbb E\log
\frac{(|D|)_{\underline Q}}
     {(V-|G|)_{\underline Q}}
+O(1).
\tag{30}
\]

Batch perspective lemma给

\[
\mathcal C_k
\le
\log(V)_{\underline m}
-m\Phi_{\varepsilon,\gamma_b}(x_\ell,x_r)+o(m),
\tag{31}
\]

其中 `gamma_b->0`，且

\[
\Phi_\varepsilon(a,c)
=(1-\varepsilon a)
\log\frac{1-\varepsilon a}{\varepsilon(c-a)}.
\tag{32}
\]

只取 KLZ 的两个 endpoint pivots。删除每个 sum 中至多一个非负 endpoint term后，
两条不等式作用在同一组内部 coordinates `x_1,...,x_(b-1)`：

\[
\frac Hn
\ge\frac1b\sum_{i=1}^{b-1}
\log\frac1{\varepsilon(x_i+\gamma_b)}-o(1),
\tag{33}
\]

\[
\frac Hn
\ge\frac1b\sum_{i=1}^{b-1}
(1-\varepsilon x_i)
\log\frac{1-\varepsilon x_i}
{\varepsilon(1-x_i+\gamma_b)}-o(1).
\tag{34}
\]

两 integrands 都凸。对同一个内部平均 `bar x` 分别使用 Jensen，再令
`b->infinity`、`gamma_b->0`，得到

\[
\frac Hn
\ge
\max\left\{
\log\frac1{\varepsilon\bar x},
(1-\varepsilon\bar x)
\log\frac{1-\varepsilon\bar x}{\varepsilon(1-\bar x)}
\right\}-o(1).
\tag{35}
\]

对 `bar x in (0,1)` 最小化即得 (3)。

当 `epsilon=1/2` 时，第一项严格递减、第二项严格递增，唯一交点为

\[
x_*=0.739998185722401\ldots,
\tag{36}
\]

共同函数值为 (4)。仓库中的 `scripts/verify_endpoint_batch_constant.py` 复现该数值。

## 8. 为什么 source-union completeness 单独不够

只要求 (10) 不能推出 (14)。取一个 belief family，包含一个不含 `y` 的 actual
core world，并为大量 keys `z` 各加入一个同时含 `y,z` 的 rare witness world。
Family union覆盖所有这些 `z`；但合法 suffix

\[
\operatorname{Insert}(y),\operatorname{Delete}(y)
\]

把所有含 `y` 的 worlds 一次性删除，union 可同时失去线性多个 `z`。普通
belief-state transducer 可把该 family实现成完整 operational fiber，所以
source union与operational union可以完全相等，transport仍发生 avalanche。

因此旧的 SUC-only midpoint草稿已撤回。真正缺少的不是更精细的 posterior
coefficient，而是 section influence 本身。

## 9. 定理边界

本文证明的是一个 broad structural subclass theorem，而不是 unrestricted ordinary
lower bound。它允许 arbitrary history dependence、nonmonotone YES-sets、holonomy、
multiple representations、global certificates 与 public-coin reliability allocation。

剩余 unrestricted 问题被压缩为：低空间 right congruence 是否能在大量 KLZ cuts
上持续制造 unbounded source-section influence，同时仍保持低 accepted support 与
pointwise FPR。若答案是否定的，需要一个 replacement-response width theorem；若
答案是肯定的，则该 avalanche机制应能导出新的 ordinary upper-bound construction。
