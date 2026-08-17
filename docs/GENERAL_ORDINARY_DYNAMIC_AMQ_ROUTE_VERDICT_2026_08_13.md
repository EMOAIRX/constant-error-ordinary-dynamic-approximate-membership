# 一般 ordinary dynamic AMQ：从特例回到正确的全局对象

> 日期：2026-08-13。状态：一般模型的 formulation 与路线裁决。本文不把任何
> 有限宇宙计算包装成主结果；所有正面主命题均明确标为开放。

> 2026-08-17 update：本文 Section 6 隔离的 extensive replacement-width 目标已经由
> [simultaneous replacement-cover theorem](./SIMULTANEOUS_REPLACEMENT_COVER_WIDTH_LOWER_BOUND_2026_08_17.md)
> 闭合，得到原始模型下 $H\ge(1+2^{-48})n-o(n)$。本文保留为此前 barrier 与
> formulation 的历史记录；“尚未证明超过 Carter”的判断不再代表当前 frontier。

## 1. 目标

固定常数误差 \(0<\varepsilon<1\)，考虑容量 \(n\)、
\(|U|/n\to\infty\) 的 ordinary one-sided dynamic approximate membership：

- 固定 \(H\)-bit persistent state；
- 免费只读 public random tape；
- key-only `Insert/Delete/Query`；
- 任意 history dependence、global relocation、ghosts 和 shared certificates；
- 每条 fixed legal history、每个 fixed current nonmember 的 FPR 至多
  \(\varepsilon\)；
- 每条 tape 上 zero false negatives。

真正的问题是确定

\[
R_{\rm dyn}(\varepsilon)
=\liminf_{n\to\infty}\frac{H^*(n,\varepsilon)}n.
\tag{1}
\]

任何只对 \(n=2\)、固定深度、canonical summaries、local cells 或 exact
multiplicities成立的结论都不回答式 (1)。

## 2. 精确的一般 formulation

令 \(\mathcal L_n\) 是所有合法 update histories 的 prefix language，
\(S(h)\) 是 history \(h\) 的 current set。固定 tape \(r\) 后，filter state map

\[
f_r:\mathcal L_n\to[2^H]
\]

诱导 finite-index labeled right congruence：若 \(f_r(h)=f_r(h')\)，则对任何
同时合法的 labeled continuation \(w\)，

\[
f_r(hw)=f_r(h'w).
\tag{2}
\]

一个 class \(C\) 的最小 one-sided reproduction 是

\[
A_r(C)=\bigcup_{h\in C}S(h).
\tag{3}
\]

随机 filter 正好是这些 right congruences 的 public-coin mixture，并满足

\[
\forall h,\ \forall x\notin S(h),\qquad
\Pr_R[x\in A_R([h]_R)]\le\varepsilon.
\tag{4}
\]

所以式 (1) 是一个 **fractional right-congruence covering rate**，而不是普通
static graph entropy，也不是 canonical occupancy entropy。

## 3. 四个一般 no-go 定理

### 3.1 固定深度不能产生线性动态项

任意 static \(t\)-set filter 都可通过显式保存至多 \(d\) 个 fresh suffix keys，
扩展成 depth-\(d\) right-congruence transducer，额外空间

\[
\log_2\sum_{i=0}^d{ |U|\choose i}
\le d\log_2|U|+O(d).
\tag{5}
\]

若 \(d\log|U|=o(n)\)，一阶空间率与 static optimum相同。因此任何 fixed-depth
orbit、constant-size gadget 或局部 Johnson inequality都不可能证明式 (1) 中的
额外线性项。

### 3.2 Sequential causal direct sum 为假

final-state chain rule

\[
I(X_{1:k};M\mid R)
=\sum_i I(X_i;M\mid R,X_{<i})\le H
\tag{6}
\]

严格成立，但看不见已经删除的 blocks和中间 ghost tests。完整 transcript的
directed information能看见它们，却不受 \(H\) 一次上界。一个 1-bit
`Load/Probe/Clear` transducer可依次暴露 \(k\) 个 independent bits，最后 state
为零。因此不能把 sequential local transition premiums相加来下界 persistent
memory。

### 3.3 同误差 block tensorization 为假

取 \(k\) 个一键 fully dynamic blocks。public tape均匀选择 \(m\) 个 coordinates
精确维护，其余 coordinates永久回答 YES。该 filter支持任意长 histories，使用

\[
H=m
\]

bits，且每个 fixed nonmember 的 FPR 恰为

\[
\varepsilon=1-m/k.
\tag{7}
\]

在 \(\varepsilon=1/2\) 时只需 \(k/2\) bits，而把单块同误差成本相乘会错误地
给 \(k\) bits。公共随机带可以在每条 tape上完全牺牲不同 blocks；任何正确的
direct sum必须先允许这种 reliability allocation。

### 3.4 Pure-deletion saturation不能超过静态率

存在使用 \(n\log_2(1/\rho)+o(n)\) bits 的随机 set-cover source encoder：保存
第一个包含 initial set 的 Bernoulli-\(\rho\) accepted set index，并在所有删除中
冻结该 index。它满足 deletion-only zero-FN 和 pointwise FPR
\(\rho+o(1)\)，并同时饱和 forward information、reverse collapse、shadow 和
delete-label mutual information。在 \(\rho\uparrow1/2\) 时空间是 \(n+o(n)\)。

所以纯删除轨迹上的任何联合 entropy bookkeeping都不能证明 half error 下
\(H>(1+o(1))n\)。必须实质使用 fresh replacement closure。

## 4. 正确候选：reliability-allocation functional

对一条 tape \(r\) 和一族同时 live 的任务，令 \(\alpha_i(r)\in[0,1]\) 表示
block \(i\) 在该 tape上的 rejection reliability。pointwise FPR只给

\[
\mathbb E_R\alpha_i(R)\ge1-\varepsilon.
\tag{8}
\]

coordinate erasure说明 \(\alpha_i\in\{0,1\}\) 的极端 allocation必须被允许。
因此合理的全局对象不是

\[
\sum_i R_{\rm one}(\varepsilon),
\]

而应是：先对每条 tape证明 state cost至少为一个联合势

\[
\log|\mathcal M_r|
\ge \Phi_n(\alpha_1(r),\ldots,\alpha_k(r)),
\tag{9}
\]

再在式 (8) 下优化 \(\mathbb E_R\Phi_n\)。\(\Phi_n\) 必须同时看到：

1. 线性数量的 uncertainty同时 live；
2. history classes 的 support unions；
3. delete-then-fresh-insert 的 replacement branches；
4. global certificates和全局 reliability allocation；
5. 所有时刻只使用同一个 \(H\)-bit state budget。

这可以称为 fractional right-congruence rate，但只有证明式 (9) 的解析 lower
bound后，这个名字才有数学内容。

## 5. 最小的论文级主命题

一个足以形成真正一般贡献、同时没有隐藏结构假设的目标是：

### Conjecture A（simultaneous-live replacement potential）

存在 support-sensitive functional \(\Phi_n\)，对 arbitrary deterministic
right congruence满足式 (9)，并且对所有满足式 (8) 的 public-coin mixtures，

\[
\mathbb E_R\Phi_n(\alpha(R))
\ge nL(\varepsilon)-o(n),
\tag{10}
\]

其中 \(L(\varepsilon)>\log_2(1/\varepsilon)\) 在某个固定常数误差区间成立。

式 (10) 的最低价值是首次在完整 ordinary 模型中超过 Carter static rate。更强的
版本应识别 \(L\) 为 fingerprint-multiset rate或给出反例构造。

### 必须通过的 sharpness tests

- frozen balanced mask / coordinate erasure；
- global ALL-YES coin；
- exact dictionary；
- exact fingerprint count vector；
- static random cover followed by pure deletions；
- additive-syndrome approximate-design fibers；
- support-only multiple-choice snapshots。

任一候选势函数若在这些例子上重复收费、条件于 tape重新调用 FPR、或假设
reliability逐 block均匀，就不是 ordinary-model theorem。

## 6. 当前最有 taste 的路线

不再研究 fixed gadgets。直接在 KLZ 的线性深度 obfuscating tree 中选择一个
cut，使线性数量的 hidden keys在同一 pivot state上同时 live；随后加入一族
seed-independent replacement continuations。要证明的不是每个 key贡献独立 bit，
而是一个 weighted support statement：

\[
\text{large same-state endpoint family}
+\text{low accepted support}
+\text{replacement closure}
\Longrightarrow
\text{large reliability-weighted successor partition}.
\tag{11}
\]

式 (11) 必须按 section multiplicity加权，避免 rare-witness poisoning；必须在
random tapes上联合平均，避免逐 tape support断言；并且 successor partition的
代价必须留在一个 simultaneous-live final state中，避免 reusable-memory反例。

这是目前唯一同时躲过四个一般 no-go theorem 的接口。它尚未被证明，因此当前
不能宣称已经解决 FOCS 2025 的 constant-error open problem。

## 7. 有限结果的地位

\(U=4,n=2\) 的 transition separation只说明 replacement compatibility确实能在
某些参数下严格超过 static covering。它可用于发现式 (11) 的权重，但不能作为
主结果，也不能通过普通 direct sum推出渐近定理。正式论文中应最多作为附录的
sanity check；若式 (10)--(11) 没有闭合，就不应以该有限结果投稿。
