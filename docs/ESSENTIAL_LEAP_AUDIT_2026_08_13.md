# Ordinary dynamic AMQ：什么才算本质跃升

> 日期：2026-08-13。状态：研究裁决。本文把目前的严格进展、已关闭的错误路线和
> 唯一仍可能形成 tight theorem 的接口放在同一张账本中。没有把候选结论升级成
> 已解决问题。

## 1. 结论先行

继续提高 finite-pivot lower-bound 常数不能关闭 FOCS 2025 的 constant-error问题。
原因有两个：

1. ordinary fixed-state upper bound目前约为 `2.349083n`，而 all-pivot relaxation
   数值极限约在 `1.7n` 附近；
2. all-pivot functional只记录 full-fiber union的一阶大小，丢失决定 state count的
   posterior thickness。

因此一个真正的跃升必须是以下二者之一：

- **下界侧：** multi-parent posterior-overlap theorem，在 `u/n->infinity` 下把
  thickness、transport和所有 pivots放入同一个 `H`-bit预算，并产生严格线性缺口；
- **上界侧：** 构造一个小于 `2.349083n`、任意长 history、zero-overflow 的 lossy
  right congruence。

## 2. 已经严格得到的结构

### 2.1 Large-universe all-pivot hierarchy

在 `u/n^2->infinity` 下，已有一般凸层级

\[
H\ge C_qn-o(n),\qquad C_{kq}\ge C_q,
\]

以及纯有理证书 `C_10>1.6079`。这是可靠 lower bound，但不是 tight-rate候选。

### 2.2 Transport-or-information dichotomy

对 state posterior `mu` 的 union `W`，随机合法 suffix pruning 后 union为 `W_I`，
严格有

\[
\mathbb E\log\frac{\binom{|W|}{n}}{\binom{|W_I|}{n}}
\le
\log\binom{|W|}{n}-H(\mu)+I(S;I).
\]

其中

\[
I(S;I)\le
\log\frac{\binom uq}{\binom{u-n}q}
\le(\log_2e)\frac{nq}{u-n-q+1}.
\]

所以局部 full-fiber transport 的 birthday barrier不是内生的：`u/n->infinity`
足以把 suffix dependence压到 `o(n)`，前提是 posterior thickness deficit被正确计费。

### 2.3 Single-pivot exact no-go

定义 static support saving `A`、transport saving `K`、fiber deficit `D` 和 fresh
suffix penalty `Gamma`。单 pivot中精确有

\[
H\ge A+K-\Gamma,
\qquad K\le D+I(S;I\mid M),
\]

且右侧组合恰好退化为 conditional mutual-information chain rule。Exact posterior
code、显式发送 state与联合 list code都不能突破 Carter static rate。

因此“用 posterior entropy修复 transport”在单 pivot上不会产生 dynamic premium。

## 3. All-pivot极限为何不是闭环

dyadic `C_(2^j)` 单调有界，所以极限存在。数值为

\[
C_{64}\approx1.68487,
\quad C_{128}\approx1.69751,
\quad C_{256}\approx1.70518.
\]

候选 `1+1/(2 ln 2)` 尚无证明；简单显式 density已被代回否决。即使最终解析求出
该极限，也只关闭一阶 union-profile relaxation。相同 union profile可以来自 thick
fiber或近乎不交的 thin fiber，二者的 physical-state复杂度完全不同。

## 4. Upper-bound闭环为何也尚未出现

uniform Poisson occupancy entropy约为 `2.287904n`，但这是 current-state/whp
source-coding rate。它不能通过以下通用补丁升级为无限历史 fixed cap：

- global reserve或多个 codebooks；
- epoch rebuild；
- sticky ALL-YES overflow；
- 保持 exact occupancy的 multiple representations。

原因是 exact occupancy vectors可由共同 deletion continuation区分，必须占据不同
physical states。其 zero-overflow all-compositions rate约为 `2.384500n`。另一方面，
sticky overflow在无限多个 epochs上会累计到违反 pointwise FPR。

ordinary filters可以通过 ghosts合并 multiplicities；order-3 algebraic quotient正是
因此达到 `2.349083n`。所以改进上界需要新的 lossy transition congruence，而不是
更好的典型集压缩。

## 5. 最小开放核心：multi-parent total correlation

设多个 KLZ parents `P_1,...,P_s` 都由同一个 final state与不同已解码 side
information导出。每个 parent posterior有 deficit `D_i` 和 suffix pruning saving
`K_i`。单独应用 transport theorem只给 `K_i<=D_i+o(n)`；逐 `i` 相加会重复使用
同一 final-state information。

需要的定理必须量化

\[
\sum_iD_i
-I(X;M_{final}\mid R,\Theta)
\]

中的 conditional total correlation，并证明 KLZ 随机分块迫使它支付线性成本，
或构造一个 shared-transversal ordinary transducer证明该缺口可以为零。

这给出一个清晰的可证伪分叉：

1. 若存在 `Omega(n)` overlap deficit，则可望同时得到 `u/n->infinity` 与新的动态
   lower-bound premium；
2. 若存在近等号 shared-transversal transducer，则 all-pivot/thickness路线被关闭，
   研究应转向新的 right-congruence upper bound。

## 6. Two-parent no-go 与研究优先级

对独立 hidden batches `X,Y` 和共同 state `M`，chain rule给出

\[
I(X;M)+I(Y;M)
=I(X,Y;M)-I(X;Y\mid M).
\tag{1}
\]

所以 two-parent overlap correction正是 conditional total correlation
`I(X;Y|M)`。它没有普适正下界：若 state posterior fibers是 product rectangles，
则 `X,Y` 给定 `M` 后仍独立，式 (1) 的 correction严格为零。两种 decode orders
也分别只给

\[
I(X;M)+I(Y;M\mid X)=I(X,Y;M),
\]

\[
I(Y;M)+I(X;M\mid Y)=I(X,Y;M).
\]

把两个顺序相加会重复收费同一 state information；取最大值则没有额外 premium。
任何只观察常数个 parents 的普适信息不等式都必须允许这个 rectangle近等号机制。

KLZ 若能产生正 gap，必须证明长程 online updates迫使 posterior持续偏离 product
rectangles。已有 finite-depth suffix-logging theorem表明，固定深度 `d` 只需
`O(d log u)` bits显式记录，不能产生线性动态成本。因此正面定理的深度至少要增长到
`Omega(n/log u)`。

第一优先级不是继续认证 `C_20`，而是对随 `n` 增长的 parents证明或否决

\[
\sum_iD_i
\le I(X;M_{final}\mid R,\Theta)
+\operatorname{TC}(X_1,\ldots,X_s\mid M_{final},R,\Theta)+o(n),
\]

并利用 transition compatibility证明 total correlation或另一种非矩形度为
`Omega(n)`。仅由 hidden batches先验独立不能推出这一点。

第二优先级是构造侧：搜索跨 occupancy layers闭合的 finite monoid/group-action
summary，使 state growth小于 order-3 quotient，同时保持 pointwise half-error。

这两个目标都可能真正改变 gap；有限常数优化、typical-set overflow和单 posterior
编码已经被严格审计为不足。
