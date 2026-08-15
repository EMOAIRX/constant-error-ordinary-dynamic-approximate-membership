# Algebraic quotient dynamic filters：论文含金量审计

> 日期：2026-08-13。本文只区分已证结论、有限枚举证据和开放目标；不把
> restricted-class converse 表述成 ordinary dynamic AMQ 的全局最优性。

## 1. 结论先行

当前成果已经明显强于一个 \(0.0354n\)-bit 的参数改进：除了结构定理和
\(\varepsilon=1/2\) 的 sharp restricted converse，现在还有一条高误差端的新
ordinary upper bound

\[
R(1-\delta)
\le
\left(\frac e2+o(1)\right)\delta\log_2\frac1\delta,
\qquad \delta\downarrow0.
\]

它把 exact heterogeneous fingerprint benchmark 的首项常数改善一半。这个
factor two 不是相对于所有 static filters，也不是 arbitrary dynamic lower bound；
本工作仍没有解决 KLZ/FOCS 2025 的 general constant-error open problem。

可作为论文核心的严格 package 是：

1. 一个支持 ordinary `Insert/Delete/Query`、任意长合法 history、fixed worst-case
   memory 且无 overflow 的 algebraic threshold filter；在
   \(\varepsilon=1/2\) 时空间为
   
   \[
   2.349083440193\ldots n+o(n)\quad\text{bits}.
   \]

2. 一个 lattice normal-form theorem：任何由当前 symbol multiset 唯一决定、
   支持确定性 key-only insert/delete 的 canonical summary，都必然是
   \(\mathbb Z^K\) 的一个 lattice quotient；有限 Abelian syndrome 不是预设语法，
   而是可逆更新语义强迫出的结构。

3. 在显式保存 exact load 的 binary canonical class 中，允许任意 biased inner
   hash 后，
   
   \[
   q=3,\qquad p=1/2
   \]
   
   仍是 \(\varepsilon=1/2\) 的唯一最优解；因此 modular threshold 不是一个
   手工选择，而是该自然类中的 sharp optimum。

4. 一个 masked threshold family：公共随机 mask 允许一部分 keys 永久 YES，
   tracked keys 使用 threshold quotient。即使 fixed state 必须覆盖最坏情况下
   全部 \(n\) 个 live keys 都被 tracked，仍得到上述 \(e/2\) 端点常数。

这已经形成一篇有明确代数和渐近主题的可信论文核心。SODA 强度仍取决于能否
补一个对应的 restricted converse、一般 \(K\)-ary lattice quotient 的 sharp
converse，或允许跨 load merging 的 binary classification。

## 2. 已证 ordinary upper bound

公共随机带取

\[
g:U\to[B],\qquad h:U\to\{0,1\}.
\]

每个 block 保存 exact load \(c\) 和 residue

\[
a=\sum h(x)\pmod q.
\]

当 \(c<q\) 时 residue 精确恢复 one-count；当 \(c\ge q\) 时最小安全查询对
两个 symbols 都回答 YES。高负载时的 residue 仍随 deletion 作群逆更新，所以
负载降回 \(q-1\) 以下时自动恢复精确 support。这给出 zero false negatives、
key-only deletion 和任意长 history，不需要外部 exact set。

对固定历史和固定当前非成员，若 \(n/B\to\lambda\)，拒绝概率为

\[
J_q(\lambda)
=e^{-\lambda}\sum_{t=0}^{q-1}\frac{(\lambda/2)^t}{t!}.
\]

local state OGF 为

\[
A_q(z)=\frac{1-z^q}{(1-z)^2},
\]

因此 fixed-state rate 是

\[
\mathcal R_q(\lambda)
=\min_{0<z<1}
\left\{\frac{1}{\lambda}\log_2 A_q(z)-\log_2z\right\}.
\]

在 \(\varepsilon=1/2\) 时，\(q=3\) 给出

\[
\lambda=1.325819075285\ldots,
\qquad
R=2.349083440193\ldots.
\]

有限 \(n\) 的 pointwise FPR、总负载至多 \(n\) 的全状态 enumerative coding 和
saddle-point 一阶率都已经单独审计。

## 3. 新的结构主定理

把 \(K\)-symbol multiset 写成 \(x\in\mathbb N^K\)。若 canonical summary
\(\phi(x)\) 支持由状态和 label 唯一决定的 insert/delete，定义

\[
x\sim y\iff\phi(x)=\phi(y).
\]

共同插入和共同合法删除给出 cancellation：

\[
x+a\sim y+a\iff x\sim y.
\]

于是

\[
L=\{x-y:x\sim y\}\le\mathbb Z^K,
\qquad
x\sim y\iff x-y\in L.
\]

所以所有这样的 canonical summaries 都等价于 additive syndrome

\[
[x]_L\in\mathbb Z^K/L.
\]

若 exact load 显式保留，则 \(L\le A_{K-1}\)，其中

\[
A_{K-1}=\{z\in\mathbb Z^K:\sum_i z_i=0\}.
\]

每层状态数一致有界当且仅当 \([A_{K-1}:L]<\infty\)。minimal one-sided
query、FPR 和空间因此统一化为

\[
Q(c,s,i)=\mathrm{YES}
\iff s-v_i\in(c-1)V,
\]

\[
\rho_c=\sum_i p_i\Pr[S_c-v_i\notin(c-1)V],
\qquad
A(z)=\sum_{c\ge0}|cV|z^c.
\]

这把整个 canonical deterministic local-summary 类归约为一个明确的
sumset-growth versus random-walk-distortion 变分问题。

## 4. Binary sharp converse

当 \(K=2\) 且 exact load 显式保留时，\(A_1\cong\mathbb Z\)，其有限指数子群
只有 \(q\mathbb Z\)。因此每个 canonical quotient 都只能记录 one-count
modulo \(q\)，不存在真正的 nonlinear、variable-modulus 或 multi-accumulator
改进。

对 bias \(p=\Pr[h(x)=1]\)，低于 threshold 时的条件拒绝率为

\[
\rho_c(p)=p(1-p)^c+(1-p)p^c,
\]

总拒绝率为

\[
J_{q,p}(\lambda)
=e^{-\lambda}\sum_{c=0}^{q-1}
\frac{\lambda^c}{c!}\rho_c(p).
\]

利用

\[
p e^{-\lambda p}+(1-p)e^{-\lambda(1-p)}
\le e^{-\lambda/2}
\qquad(0<\lambda\le2),
\]

以及 \(\mathcal R_q\) 对 \(\lambda\) 严格下降、对 \(q\) 严格增加，可证明在
\(\varepsilon=1/2\) 时所有 \(q\ge4\) 都严格劣于 \(q=3,p=1/2\)；
\(q=2\) 直接比较也更差。这个 converse 覆盖任意 biased binary canonical
summary，但要求 summary 显式保留 exact load。

## 5. 优先权边界

不能把“高负载时暂时不可解码，删除降回阈值后恢复”称为首次发现。
Goodrich--Mitzenmacher 的 IBLT 已明确具有这个行为：超过设计阈值会暂时阻止
内容 listing 并降低 lookup 成功率，随后删除降回阈值时功能恢复。

Deletable Bloom filters、counting Bloom filters 和 multiset dictionaries 也早已研究
删除所需的 collision/multiplicity 信息。因此安全的新意不是“可删除”“可逆摘要”
或“阈值恢复”本身，而是：

1. one-sided approximate membership 下的 fixed-state 精确空间率；
2. canonical reversible summaries 的 lattice normal form；
3. quotient 的 sumset/random-walk 变分；
4. binary 类中的 matching restricted converse 和误差相变。
5. masked threshold family 的 fixed-state high-error rate 及 factor-two
   endpoint improvement。

目前没有核到直接采用“modulo residue + high-load ALL-YES”并给出上述 fixed-state
rate/converse 的先例，但正式投稿前仍需系统检查 IBLT、strata estimators、
counting/deletable Bloom filters 和 succinct multiset dictionaries 的全文与引用图。

## 6. 新的 high-error endpoint theorem

令

\[
\delta=1-\varepsilon.
\]

公共随机 mask 以概率 \(\beta\) 跟踪一个 key；untracked keys 不写持久状态且
永久回答 YES。tracked keys 使用 order-\(q\) threshold quotient。固定任意
history、固定 nonmember，若

\[
\lambda=\frac{\beta n}{B},
\qquad
F_q(\lambda)
=e^{-\lambda}\sum_{t=0}^{q-1}\frac{(\lambda/2)^t}{t!},
\]

则渐近拒绝概率为

\[
\delta=\beta F_q(\lambda).
\]

这里最危险的计费错误是把 tracked capacity 当成 \(\beta n\)。对固定公共 tape，
合法 history 可能让全部 \(n\) 个 live keys 都被 tracked，所以 state rank 必须
覆盖

\[
\sum_{j=1}^B c_j\le n.
\]

令 \(b=B/n=\beta/\lambda\)。正确 fixed-state rate 是

\[
S_q(b)
=\min_{0<z<1}
\left\{
b\log_2A_q(z)-\log_2z
\right\}.
\]

对 fixed \(q\) 和 \(b\downarrow0\)，

\[
S_q(b)
=b\log_2\frac1b+b\log_2q+O_q(b).
\]

定义

\[
M_q=\max_{\lambda>0}\lambda F_q(\lambda).
\]

最优校准给 \(b=\delta/M_q\)，且

\[
M_q\uparrow
\max_{\lambda>0}\lambda e^{-\lambda/2}
=\frac2e.
\]

先固定足够大的 \(q\)，再令 \(\delta\downarrow0\)，最后令 \(q\to\infty\)，
得到严格的双重极限上界

\[
\boxed{
\limsup_{\delta\downarrow0}
\frac{R_{\rm masked}(\delta)}
{\delta\log_2(1/\delta)}
\le\frac e2.
}
\]

有限 \(n\) 用精确 Binomial rejection 公式和略小的 calibrated load 吸收 rounding；
state rank pathwise 覆盖全部 tracked load 至多 \(n\)，因此没有 overflow、历史
长度限制或 concentration 假设。

这一结果相对 exact heterogeneous fingerprint 的

\[
(e+o(1))\delta\log_2(1/\delta)
\]

首项常数改善 factor two。但 Carter static benchmark 只有

\[
\log_2\frac1\varepsilon
=\left(\frac1{\ln2}+o(1)\right)\delta,
\]

所以新的 dynamic upper bound 仍多一个 \(\log(1/\delta)\) 因子；目前没有
matching dynamic lower bound 说明该因子或 \(e/2\) 必要。

## 7. 仍未解决的核心

### 7.1 \(K>2\) sharp converse

一般 finite Abelian \(G\) 和 \(V\subseteq G\) 的最优性仍未证明。小群穷举支持

\[
R(G,V;1/2)\ge2.349083440193\ldots,
\]

且等号由 \(\mathbb Z_3,\{0,1\}\) 实现；例如搜索到的最近非二元候选
\(\mathbb Z_{12},\{0,1,4\}\) 仍为约 \(2.352584\)。这只是证据，不是 theorem。

Cauchy--Davenport 只控制 \(|cV|\)，而 FPR 还依赖每个 syndrome 的表示结构；
分别极值化两者会给出无效下界。真正需要的是联合控制

\[
(|cV|)_{c\ge0}
\quad\text{与}\quad
(\rho_c)_{c\ge0}
\]

的 sharp inequality。

### 7.2 Cross-load merging

若不同 loads 可以共享物理状态，lattice 不再局限于 \(A_{K-1}\)。即使 binary
也会出现 full-rank 或 oblique lattices，不能再由单个 modulus \(q\) 分类。
当前没有证明它们不能改善 \(2.349083\)。因此主定理必须保留
“explicit exact load”这一假设。

### 7.3 Ordinary arbitrary-filter optimum

history-dependent、多表示、随机 transition、跨 block 全局状态都不在 lattice
normal form 内。更重要的是，目前 rate 仍高于 generalized fingerprint-multiset
source-coding benchmark

\[
2.2006114829\ldots.
\]

所以不能声称解决 KLZ 的 general constant-error conjecture。

### 7.4 Full error phase diagram

uniform binary quotients 出现清晰的相邻 phase transitions：

\[
q=3\to4:\ \varepsilon\approx0.691362376856,
\]

\[
q=4\to5:\ \varepsilon\approx0.880349221321,
\]

\[
q=5\to6:\ \varepsilon\approx0.953700123072.
\]

但是这些目前主要是高精度数值。高误差端 biased hash 会严格优于 uniform hash，
所以完整相图必须联合优化 \((q,p)\)，不能只分析整数 \(q\)。

## 8. SODA 级推进顺序

最有 taste 的顺序不是继续优化 \(2.349083\) 的小数位，而是：

1. 先完成 cross-load binary lattice classification；这是最小的结构缺口，结论若
   仍由 \(q=3\) 达到，就能删除当前最刺眼的 exact-load 假设。
2. 再证明一个 prime-cyclic 或 bounded-doubling \(K>2\) 的联合
   sumset--distortion inequality，并给出稳定性/等号分类。
3. 为 masked endpoint 证明一个 natural-class matching converse，或证明任何
   load-preserving canonical filter 都不能优于 \(e/2\) 的首项常数。
4. 同时完成 biased \((q,p)\) phase diagram；这可形成独立的第二结构定理。
5. 最后再研究 history-dependent/global quotients；这一步才真正触及 KLZ 的
   arbitrary-filter open problem。

当前 package 已经有可信的强会叙事：可逆动态 summary 的代数 normal form、
sharp binary optimum、以及比 exact multiplicity family 改善 factor two 的
high-error endpoint。最主要的 reviewer 风险从“只有一个小常数改进”变成了
“新上界缺 matching converse”。在补出第 1、2 或 3 项之一前，仍不应宣称已经
完成 arbitrary dynamic AMQ 的 SODA breakthrough。
