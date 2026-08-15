# 次指数 horizon 下的 width 目标与线性阶 Johnson-syndrome barrier

> 日期：2026-08-14。状态：Sections 1--2 是解析定理；Section 3 是一般
> ordinary dynamic AMQ 下界的最小 sharp conjecture。本文不宣称已经证明
> fingerprint optimality。

所有对数以 2 为底。容量为 \(n\)，universe 大小为 \(u\)，operation horizon
为 \(f(n)\)。随机带免费且只读，persistent memory 是固定的 \(H\) bits。

## 1. 次指数 horizon 消除了 typical-set upper bound 的 worst-case-space 障碍

考虑有限个 tracked types \(i=1,\ldots,L\)。一个 key 以概率 \(\theta_i\)
进入 type \(i\)，随后均匀进入该 type 的
\(q_i=c_i n+O(1)\) 个 cells；剩余概率 \(1-\sum_i\theta_i\) 进入
permanent-YES 类。令

\[
\lambda_i=\theta_i/c_i.
\tag{1}
\]

机器精确维护 tracked cells 的 multiplicity vector。对固定 nonmember，在
current load \(s\le n\) 时 rejection probability 为

\[
\sum_i\theta_i\left(1-\frac1{q_i}\right)^s,
\tag{2}
\]

其最小值在 \(s=n\)，并趋于

\[
\alpha=\sum_i\theta_i e^{-\lambda_i}.
\tag{3}
\]

记 \(C_s\) 为 \(s\) 个独立 keys 产生的 tracked count vector。

### Lemma 1.1（sparse multinomial 的 uniform typical family）

固定 \(L,(c_i),(\theta_i)\)，且所有正参数均与 \(n\) 无关。对任意固定
\(\delta>0\)，存在 count-vector family \(\mathcal T_n\)，使

\[
|\mathcal T_n|
\le
2^{\,n(R+\delta)},
\qquad
R=\sum_i c_i H(\operatorname{Pois}(\lambda_i)),
\tag{4}
\]

并且对所有 \(0\le s\le n\)，

\[
\Pr[C_s\notin\mathcal T_n]\le e^{-\gamma n}
\tag{5}
\]

for some \(\gamma>0\), for all sufficiently large \(n\).

#### 证明

先处理 \(s=\tau n+O(1)\)、\(\tau\in[\tau_0,1]\)。把每个 cell count
Poissonize 成相互独立的
\(Z_{i,j}\sim\operatorname{Pois}(\tau\lambda_i)\)，再条件于总 tracked count
和 permanent-YES count，可得到 \(C_s\) 的精确 multinomial law。
Poisson information density

\[
-\log \Pr[Z_{i,j}]
\]

在参数位于 compact interval 时具有一致的 exponential moment。因此 Chernoff
给 information density 的 \(e^{-\Omega(n)}\) concentration；对 totals
conditioning 只损失多项式因子。于是每个 \(s\) 有一个概率
\(1-e^{-\Omega(n)}\) 的 typical family，大小至多
\(2^{H(C_s)+\delta n/3}\)。

加一个 independent ball 把 \(C_s\) 变成 \(C_{s+1}\)，而离散群上的独立卷积
满足 \(H(X+Y)\ge H(X)\)，故 \(H(C_s)\le H(C_n)\)。标准 sparse-occupancy
entropy asymptotic 给

\[
H(C_n)=n\sum_i c_iH(\operatorname{Pois}(\lambda_i))+o(n).
\]

对至多 \(n+1\) 个 \(s\) 取 union，只增加 \(O(\log n)\) bits。最后，
\(s<\tau_0n\) 时直接收进全部 support-size 至多 \(\tau_0n\) 的 count vectors；
其 exponent 随 \(\tau_0\downarrow0\) 趋于零。先取足够小的 \(\tau_0\)，再合并
两部分，即得 (4)--(5)。\(\square\)

### Theorem 1.2（fixed-space、zero-failure 的次指数-horizon fingerprints）

若

\[
\log f(n)=o(n),
\tag{6}
\]

则上述参数存在一个支持每条长度至多 \(f(n)\) 的合法 history 的 ordinary
dynamic filter，使用

\[
H\le n(R+o(1))
\tag{7}
\]

bits，zero false negatives，且 pointwise FPR 至多

\[
1-\alpha+o(1).
\tag{8}
\]

#### 证明

normal states 是 \(\mathcal T_n\) 中的 exact count vectors，另加一个 absorbing
ALL-YES overflow state。normal state 上的 insert/delete 精确修改相应 cell
count；若 successor 不在 \(\mathcal T_n\)，转入 overflow。overflow 对所有
updates 保持不变、对所有 queries 回答 YES。因此没有 overflow failure，也永远
没有 false negative。

固定任意一条与随机带独立、长度至多 \(f(n)\) 的合法 history。每个时刻的 key
set 是固定集合，所以其随机 count vector 服从某个 \(C_s\)。由 union bound，

\[
\Pr[\text{在该 history 上曾 overflow}]
\le f(n)e^{-\gamma n}=o(1).
\]

未 overflow 时使用 (2)，overflow 时至多贡献上述 \(o(1)\)。state 数由
Lemma 1.1 给出。证毕。

### Corollary 1.3（候选 fingerprint rate 是合法 upper bound）

令

\[
R_{\rm fp}(\varepsilon)
=
\inf\left\{
\sum_i\theta_i\frac{H(\operatorname{Pois}(\lambda_i))}{\lambda_i}:
\sum_i\theta_i e^{-\lambda_i}\ge1-\varepsilon,\ 
\sum_i\theta_i\le1
\right\}.
\tag{9}
\]

等价地，这是曲线

\[
\left(1-e^{-\lambda},
\frac{H(\operatorname{Pois}(\lambda))}{\lambda}\right)
\]

与点 \((1,0)\) 的 lower convex envelope。对任意固定
\(0<\varepsilon<1\) 和 \(\log f=o(n)\)，

\[
H^*_{f(n)}(n,\varepsilon)
\le nR_{\rm fp}(\varepsilon)+o(n).
\tag{10}
\]

证明时先给 error 留固定 slack，再让 slack 趋于零。这个结论说明：有限但
次指数 horizon 中，Shannon typical-set coding 与 fixed worst-case memory 并不
冲突；atypical trajectory 被合法地送入 ALL-YES state，而不是 overflow failure。

## 2. 线性阶 Johnson components 仍看不见 transition information

取随机 columns

\[
a_x\in\mathbb F_2^H,\qquad x\in U,\qquad H=\eta n+O(1),
\tag{11}
\]

并定义对所有 \(|S|\le n\)

\[
f(S)=\bigoplus_{x\in S}a_x.
\tag{12}
\]

Insert/Delete \(x\) 都执行 \(m\mapsto m\oplus a_x\)，所以这是支持任意长
history 的 exact labeled right-congruence transducer。

### Theorem 2.1（linear-design syndrome fibers）

设 \(u/n\to\infty\)，\(j/n\to\beta>0\)，并固定

\[
0<\vartheta<\beta/2.
\tag{13}
\]

则存在 columns 的 realization，使对每个 syndrome
\(m\in\mathbb F_2^H\)、每个 \(B\subseteq U\) with
\(|B|\le\vartheta n\)，一致地有

\[
\#\{S\in{U\choose j}:B\subseteq S,\ f(S)=m\}
=
2^{-H}{u-|B|\choose j-|B|}(1+o(1)).
\tag{14}
\]

特别地，每个 fiber 对所有 degree 至多 \(\vartheta n\) 的 inclusion monomials
都与 uniform Johnson slice 渐近一致。

#### 证明

固定 \(B,m\)，令式 (14) 左侧为 \(N_{B,m}\)。不同非空 sets 的 random
syndromes pairwise independent，故

\[
\mathbb E N_{B,m}=2^{-H}{u-|B|\choose j-|B|},
\qquad
\operatorname{Var}N_{B,m}\le\mathbb E N_{B,m}.
\tag{15}
\]

对所有 \(m\) 和 \(|B|\le d=\lfloor\vartheta n\rfloor\) 作 Chebyshev union
bound。所需的无量纲比值至多

\[
\mathcal R_n
=
2^{2H}
\frac{\sum_{b\le d}{u\choose b}}
{{u-d\choose j-d}}.
\tag{16}
\]

写 \(u=ng_n\)，\(g_n\to\infty\)。Stirling bounds 给

\[
\log \mathcal R_n
\le
-(\beta-2\vartheta)n\log g_n+O(n)= -\omega(n).
\tag{17}
\]

取 relative-error threshold
\(\zeta_n=\mathcal R_n^{1/4}=o(1)\)，总失败概率至多
\(\mathcal R_n^{1/2}=o(1)\)。因此存在一个 realization 同时满足 (14)。
\(\square\)

### Corollary 2.2（低于半层的 section/spectral lower bound 不可能成立）

上述 transducer 的 state budget 是 \(\eta n+O(1)\)，所有 insert/delete maps
完全 transition-compatible；然而它的每个 fiber 包含每个 coordinate 的某个
member set，所以 minimal accepted union 是整个 \(U\)，rejection 为零。

因此，任何 theorem 若只使用

1. state budget 与 labeled right congruence；
2. replacement sections 的至多 \((1/2-\Omega(1))j\) 个 prescribed coordinates；
3. 相应的 Johnson components、bounded-order moments 或 local marginals；

而不把 accepted-support/FPR 同时放进同一个 inequality，就不能推出任何正的
selectivity premium。fixed-degree spectral leakage 不是差一点；barrier 一直延伸到
严格低于 half-layer 的线性 degree。

## 3. lower bound 的最小 sharp 形式

令 \(\Pi_n\) 是一个与随机带独立的、长度至多 \(f(n)\) 的 replacement-tree
history/query distribution。对 deterministic index-\(K\) right congruence \(C\)，
令

\[
\operatorname{rej}_{\Pi_n}(C)
=\Pr_{(h,x)\sim\Pi_n}[x\notin A_C([h]_C)].
\tag{18}
\]

### Conjecture 3.1（Poisson replacement width；minimal sharp form）

对每个 fixed \(0<\varepsilon<1\) 和每个
\(f(n)=\omega(n)\), \(\log f(n)=o(n)\)，存在显式 symmetric
\(\Pi_n\)，使对任意 \(\delta>0\)，

\[
K\le2^{n(R_{\rm fp}(\varepsilon)-\delta)}
\quad\Longrightarrow\quad
\operatorname{rej}_{\Pi_n}(C)<1-\varepsilon-o(1)
\tag{19}
\]

对每个 deterministic labeled right congruence \(C\) 成立。

由 finite LP minimax，(19) 与 ordinary public-tape lower bound

\[
H^*_{f(n)}(n,\varepsilon)
\ge nR_{\rm fp}(\varepsilon)-o(n)
\tag{20}
\]

等价。结合 Corollary 1.3 就真正 close 该 horizon 下的 constant-error 问题。

这个 conjecture 不能弱化成 endpoint support entropy、固定深度 replacement、
逐 block direct sum 或低阶 Johnson leakage：这些版本分别被 static cover、
transcript storage、coordinate erasure 和 Theorem 2.1 严格否决。正确 witness
必须同时收费：

\[
\text{整棵 replacement tree 的 branch pattern}
+
\text{各 branch transported fiber 的 accepted support}.
\]

它还必须先对 reliability allocation 取凸包；点
\((\varepsilon,R)=(1,0)\) 对应 ALL-YES tapes，不能被排除。

## 4. 五类必须逐项通过的 pressure tests

1. **ALL-YES mixture。** 一条 deterministic tape 可以用一个 state 对所有 query
   回答 YES。故任何 per-tape cost function 必须在 reliability \(0\) 处取值 \(0\)。

2. **Coordinate erasure。** 在 disjoint one-key tasks 上，一条 tape 可精确保存
   selected coordinates、牺牲其余 coordinates。故同一 error 参数的 block direct
   sum 为假；只允许 fractional reliability allocation 的 theorem 才可能成立。

3. **Belief/parity transducer。** XOR syndrome 支持任意长 history，且同一个
   \(H\)-bit state budget 可携带线性 entropy；但 fiber union 是 \(U\)，所以它没有
   rejection。transition entropy 必须和 transported support 同时收费。

4. **Low-degree Johnson syndrome。** Theorem 2.1 表明不仅 fixed degree，而且
   严格低于 half-layer 的所有线性 degree moments 都可完全伪装成 uniform。

5. **Finite-depth transcript storage。** 从任意 static cover 出发，显式保存
   \(T\) 个 update labels 只花 \(O(T\log u)\) bits。因此当
   \(T\log u=o(n)\) 时，只观察 depth-\(T\) branches 的 lower bound 不能产生新的
   线性 dynamic premium。

## 5. 当前裁决

已经闭合的是 upper-bound side 和一个比 fixed-degree 更强的线性谱 barrier。
尚未闭合的是 (19)。在证明 (19) 前，\(R_{\rm fp}\) 只能称为有 matching
construction 的 sharp candidate，不能称为一般 arbitrary-filter theorem。

## 6. 一个可证的 source-weighted grouped-cell branch-width theorem

这一节给出 deletion-created zero 的严格 simultaneous-state inequality。它精确
允许 coordinate erasure，但仍不足以 close 主问题。

考虑 label-level count lattice

\[
\mathcal C_{n,q}=\{c\in\mathbb N^q:\|c\|_1\le n\}.
\]

对每个 \(c\) 固定一条 canonical build history，并令 \(M_r(c)\) 是 deterministic
tape \(r\) 上的最终 state。对 coordinate \(j\)，从 \(M_r(c)\) 执行
\(c_j\) 次同一个 label operation \(\operatorname{DeleteLabel}(j)\)，然后 query
label \(j\)。记 rejection indicator 为 \(Z_r(c,j)\)。这条 history 的 logical
count 已为零，所以 public-coin guarantee 给

\[
\mathbb E_r Z_r(c,j)\ge1-\varepsilon.
\tag{21}
\]

### Theorem 6.1（upper-envelope branch width）

令 \(C\) 是 \(\mathcal C_{n,q}\) 上任意 source，\(J\) 是任意独立 coordinate
source。对 deterministic tape \(r\)，定义

\[
\alpha_r=\Pr[Z_r(C,J)=1].
\]

令

\[
\mathsf R^+_{C,J}(\alpha)
=
\inf I(C;A),
\tag{22}
\]

其中 infimum 取遍所有 random reproductions \(A\in\mathbb N^q\) 满足

\[
A\ge C\quad\text{coordinatewise},\qquad
\Pr[A_J=C_J]\ge\alpha.
\tag{23}
\]

则每个使用至多 \(K\) states 的 deterministic label-level transducer 满足

\[
\boxed{\log K\ge \mathsf R^+_{C,J}(\alpha_r).}
\tag{24}
\]

因此任意 public-coin filter 满足

\[
\boxed{
H\ge
\mathsf R^+_{C,J}(1-\varepsilon),
}
\tag{25}
\]

其中使用了 rate-distortion function 对 distortion 的凸性。

#### 证明

对 state \(m\) 的 canonical fiber

\[
\mathcal F_m=\{c:M_r(c)=m\}
\]

定义 coordinatewise upper envelope

\[
A_j(m)=\max_{c\in\mathcal F_m}c_j.
\tag{26}
\]

显然 \(A(M_r(C))\ge C\)。若 \(Z_r(c,j)=1\) 却存在同 fiber 的
\(c'\) 满足 \(c'_j>c_j\)，则从同一 physical state 执行同一个
\(c_j\)-fold deletion word 后到达同一 successor。第一条 logical history 的
coordinate \(j\) 已为零并被拒绝；第二条仍为正，zero false negatives 强迫接受，
矛盾。因此

\[
Z_r(c,j)\le\mathbf1\{c_j=A_j(M_r(c))\}.
\tag{27}
\]

令 \(A=A(M_r(C))\)。由 data processing，

\[
\log K\ge H(M_r(C))\ge I(C;A),
\]

而 (27) 说明 \(A\) 对 (22)--(23) 可行，得到 (24)。对 tapes 平均后，
\(\mathbb E_r\alpha_r\ge1-\varepsilon\)；\(\mathsf R^+\) 作为 ordinary
rate-distortion function 对允许 distortion \(1-\alpha\) 凸，Jensen 给 (25)。
\(\square\)

### 这个 theorem 为什么仍没有 close

Theorem 6.1 只使用 deletion sections，因而把 full right-congruence domain
relax 成 one-sided reproduction \(A\ge C\)。这个 relaxation 严格允许并非
transition-compatible 的 merger。例如一维 Poisson source 上取

\[
A=
\begin{cases}
1,&C\in\{0,1\},\\
C,&C\ge2.
\end{cases}
\tag{28}
\]

它满足 \(A\ge C\)，并在除 \(C=0\) 外的所有 atoms 上 equality，故是 (22) 的
合法 lossy reproduction。但它不是 counter transducer quotient：state \(A=1\)
同时代表 counts \(0,1\)；执行一次 Insert 时，两者分别应到 counts \(1,2\)，
同一个 deterministic successor 不可能同时实现这两个 reproduction states。

因此 (25) 是真正的 source-weighted branch-width lower bound，也精确包含
coordinate erasure；但要达到 fingerprint curve，必须把 insertion closure 加入
rate-distortion domain。最小的下一对象不是普通 \(A\ge C\) RDF，而是

\[
\text{one-sided Poisson RDF}
\quad\cap\quad
\text{labeled successor-closed cells}.
\tag{29}
\]

式 (28) 是对任何只证明 deletion-envelope theorem 的最小严格反例。

### Unary one-shot ghost barrier

甚至“存在一个可靠 empty history”也不推出 multiplicity width。两状态 unary
machine 即可做到：

- 初始 empty state \(e\) 对该 label 回答 NO；
- 第一次 Insert 后进入 state \(p\)；
- \(p\) 对 query 永远回答 YES，所有后续 Insert/Delete 都保持在 \(p\)。

它对所有合法 histories 保持 zero false negatives，但仅初始 empty
representation 可拒绝；第一次触碰以后，ghost 永久存在。故

\[
\text{reliable zero history}\not\Rightarrow\text{counter width}.
\]

要排除该反例，hard source 必须在同一个 recurrent component 中反复产生并测试
return-to-zero histories。也就是说，真正的 grouped-cell中间对象应是
stationary causal one-sided Poisson rate-distortion over successor-closed cells，
而不是 snapshot RDF (22)。
