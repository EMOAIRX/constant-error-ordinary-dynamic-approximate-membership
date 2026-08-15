# Replacement saturation：精确链式恒等式与 finite-depth barrier

> 日期：2026-08-13。状态：严格 identity 与严格 bounded-horizon pressure test。
> 对 \(u=2n,\varepsilon=1/2\)，单步 replacement 的 forward/reverse mutual
> information identity不会加强静态 set-cover bound。更强地，存在支持任意预先
> 固定的 \(T=o(n/\log n)\) 次 replacements 的 key-only filter，只用
> \((0.622556\ldots+o(1))n\) bits。因此任何只检查常数深度、固定深度或
> \(o(n/\log n)\) 长 replacement trajectories 的 universal inequality，都不可能
> 推出目标 \(H\ge n-o(n)\)。

该 pressure test不是任意长 fully dynamic filter；它精确说明要证明 \(n\)-bit
converse，replacement saturation必须是 extensive-depth 或大规模 branching现象。

## 1. Stationary one-replacement experiment

令 \(U=[2n]\)，\(S\) 均匀分布于 \({U\choose n}\)。条件于 \(S\)，独立均匀取

\[
X\in S,
\qquad Y\in U\setminus S,
\]

并定义

\[
S'=S-\{X\}+\{Y\}.
\tag{1}

\]

则 \(S'\) 仍均匀分布于 \({U\choose n}\)。令 \(M\) 是建立 \(S\) 后的 state，
并令

\[
M'=I_{R,Y}(D_{R,X}(M)).
\tag{2}

\]

filter可以 arbitrary history-dependent、读取完整 public tape与 key identities。

### Theorem 1.1（one-step replacement contraction identity）

写 \(L=(X,Y)\)。因为给定 \(L\) 后 \(S\leftrightarrow S'\) 是双射，并且
\(M'\) 是 \((R,M,L)\) 的确定函数，

\[
\boxed{
I(S;M\mid L,R)
=I(S';M'\mid L,R)
+I(S';M\mid M',L,R).
}
\tag{3}

同时

\[
\boxed{
H(M\mid L,R)
=H(M'\mid L,R)+H(M\mid M',L,R).
}
\tag{4}

**证明。** 给定 \(L\)，用双射替换 \(S\) 为 \(S'\)：

\[
I(S;M\mid L,R)=I(S';M\mid L,R).
\]

再因 \(M'\) 是 \(M\) 的确定函数，对右侧按 \(M'\) chain rule展开即得式 (3)。
式 (4) 同理。\(square\)

式 (3) 说明 replacement 的 information loss就是 successor state未保留的
predecessor information。它不是额外预算；式 (4) 中同一量已经由 reverse
collapse支付。

## 2. Static finite-universe cover exponent

在 \(u=2n\) 时，若一个 state接受至多 \(m\) 个 universe keys，则它最多覆盖

\[
{m\choose n}
\]

个 logical \(n\)-sets。取 \(m=(3/2+o(1))n\)，静态 covering exponent为

\[
\begin{aligned}
R_{\rm stat}
&=\frac1n\left[
\log_2{2n\choose n}
-\log_2{3n/2\choose n}
\right]+o(1)\\
&=2-\frac32h_2(2/3)+o(1)\\
&=0.622556248918\ldots+o(1).
\end{aligned}
\tag{5}

\]

所以单个 endpoint的 accepted-set entropy只能给约 \(0.62256n\)，不是 \(n\)。
下面证明有限次 replacement仍无法排除这个静态极值。

## 3. Random accepted-superset cover

为避免 rounding，取整数

\[
m=\left\lfloor\frac{3n}{2}\right\rfloor-2.
\tag{6}

\]

令 public tape包含 \(N\) 个独立均匀 random \(m\)-subsets

\[
A_1,\ldots,A_N\in{U\choose m}.
\]

单个 \(A_i\) 包含 fixed \(n\)-set \(S\) 的概率为

\[
p_n=rac{{n\choose m-n}}{{2n\choose m}}.
\tag{7}

\]

取

\[
N=\left\lceil p_n^{-1}n^2\right\rceil.
\tag{8}

\]

初始建立 \(S\) 后，保存最小 index \(I\) 满足 \(S\subseteq A_I\)；若不存在则
进入 failure state。failure probability至多 \(e^{-n^2}\)。正常 state的 current
accepted superset初始为

\[
B_0=A_I.
\]

## 4. Replacement update rule

对合法 replacement

\[
S_{t+1}=S_t-\{x_t\}+\{y_t\},
\qquad x_t\in S_t,quad y_t\notin S_t,
\]

定义 accepted superset递推

\[
\boxed{
B_{t+1}=
\begin{cases}
B_t,&y_t\in B_t,\\
B_t-\{x_t\}+\{y_t\},&y_t\notin B_t.
\end{cases}
}
\tag{9}

\]

### Lemma 4.1（zero false negatives）

若 \(S_t\subseteq B_t\)，则 \(S_{t+1}\subseteq B_{t+1}\)，且始终
\(|B_t|=m\)。

**证明。** 若 \(y_t\in B_t\)，保持 \(B_t\) 已包含
\(S_t-\{x_t\}+\{y_t\}\)。若 \(y_t\notin B_t\)，从 superset中删除已离开 logical
set的 \(x_t\)，并加入新成员 \(y_t\)。\(square\)

### Lemma 4.2（pointwise FPR invariant）

固定任意与 public tape独立的合法 replacement history。若对 time \(t\) 的每个
fixed current nonmember \(z\notin S_t\)，

\[
\Pr_R[z\in B_t]\le\varepsilon_n,
\]

则 time \(t+1\) 也成立，其中

\[
\varepsilon_n
=\frac{m-n}{n}+e^{-n^2}
<\frac12
\tag{10}

for sufficiently large \(n\)。

**证明。** 先忽略 failure event。对初始 cover，条件于 \(I\) 是第一个包含
\(S_0\) 的 index，\(A_I\) 在所有包含 \(S_0\) 的 \(m\)-sets中均匀。因此 fixed
nonmember的 inclusion probability恰为
\[
\frac{m-n}{2n-n}=\frac{m-n}{n}.
\]

考虑 replacement后任意 \(z\notin S_{t+1}\)。

- 若 \(z\ne x_t\)，则 \(z\ne y_t\)，式 (9) 不会把原本不在 \(B_t\) 的 \(z\)
  加入；所以 \(\{z\in B_{t+1}\}\subseteq\{z\in B_t\}\)。
- 若 \(z=x_t\)，则式 (9) 给
  \[
  x_t\in B_{t+1}\Longleftrightarrow y_t\in B_t.
  \]
  而 \(y_t\notin S_t\)，由归纳假设该事件概率至多 \(\varepsilon_n\)。

加回 failure probability即得。\(square\)

该归纳逐 fixed history和fixed current nonmember成立，允许跨时间完全相关的
frozen/global certificates；没有使用独立 FPR events。

## 5. Bounded-horizon persistent encoding

若只要求最多 \(T\) 次 replacements，持久状态保存：

1. initial cover index \(I\in[N]\cup\{\bot\}\)；
2. 已执行的 replacement transcript
   \((x_0,y_0),\ldots,(x_{t-1},y_{t-1})\)，其中 \(t\le T\)。

由 \(R,I\) 和 transcript可无界计算重建 \(B_t\)，从而执行式 (9) 与 query。
固定长度 state可用

\[
H_T
\le\log_2(N+1)+2T\log_2(2n)+(T+1)+O(1)
\tag{11}

bits编码；额外 \(T+1\) bits处理当前 transcript length/self-delimiting格式。

由 Stirling与式 (5)--(8)，

\[
\log_2(N+1)
=\left(0.622556248918\ldots+o(1)\right)n.
\tag{12}

\]

所以若

\[
T=o\left(\frac n{\log n}\right),
\tag{13}

则

\[
\boxed{
H_T
\le\left(0.622556248918\ldots+o(1)\right)n,
}
\tag{14}

同时支持所有长度至多 \(T\) 的 fixed replacement histories、zero-FN 和严格
pointwise FPR \(<1/2\)。

## 6. 对 replacement saturation theorem 的限制

式 (14) 是一个普适 proof barrier：任何候选 lower-bound theorem若只使用

- 常数次 replacements；
- 任意 fixed depth \(d\)；
- 甚至 \(o(n/\log n)\) 次 sequential replacements；
- 每层的 forward/reverse entropy、accepted shadows、pointwise FPR与
  successor partition；

都不能推出 \(H\ge n-o(n)\)，因为上述真实 bounded-horizon transducer满足这些
语义而空间只有 \(0.62256n+o(n)\)。

这也解释了 fixed-depth Shearer/direct-product尝试为何不够：每个 replacement
label pair至多带 \(2\log(2n)\) bits；在 sublinear-over-log horizon内，机器可以
把整个 branch transcript原样保留，而不需要发生任何 saturation。

若目标是 full arbitrary model的 \(n\)-bit converse，至少需要以下之一：

1. \(\Omega(n/\log n)\) 个 sequential replacements，使 raw transcript不再是
   lower-order；
2. 在较浅深度同时考虑 \(2^{\Omega(n)}\) 个 branches，并证明 successor partition
   的联合 state reuse界；
3. 一个真正的 long-time recurrence/semigroup growth theorem，说明 compressed
   cover index无法在任意长 key-only replacements中持续更新。

## 7. 为什么这不是 full dynamic counterexample

当 \(T\) 无界时，保存 raw transcript会 overflow。直接保存 current
\(m\)-set \(B_t\) 需要

\[
\log_2{2n\choose m}
=1.622556\ldots n+o(n)
\]

bits，反而高于 public tracked-bitmap的 \(n\)-bit upper bound。本文没有找到将
式 (9) 对任意长 history压到 \(<n\) bits的方法。

因此当前裁决是：

- one-step exact chain rule已知，但不给额外信息；
- bounded-depth replacement saturation被式 (14)严格否决；
- full unbounded-history \(H\ge n-o(n)\) 仍可能为真，但证明必须是 extensive或
  exponentially branching的，不能来自固定深度局部不等式。
