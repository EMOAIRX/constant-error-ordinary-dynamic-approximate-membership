# 单 pivot 中 transport-or-information 的精确熵账本

> 日期：2026-08-13。状态：完整有限参数 source-coding lemma 与 barrier identity。结论是：Theorem 4.1 可以无损嵌入单 pivot，但其 entropy deficit 出现在 transport saving 的**上界**，不能单独产生新的 lower bound。Exact-posterior code退化为 chain-rule 恒等式。

所有 logarithms 以 2 为底。

## 1. 单 pivot 实验

令 \(S\) 是 \(U\) 中均匀随机的 \(t\)-set，\(R\) 是独立 public tape，并令

\[
M=f_R(S)
\]

是某个 \(H\)-bit endpoint state。取 \(q\ge0\) 满足

\[
t+q\le n.
\]

给定 \(S\)，从 \(U\setminus S\) 均匀无放回抽取 \(q\)-set \(I\)。于是 insertion word \(\operatorname{Ins}(I)\) 对真实 endpoint 合法。

条件于 \((R,M)\)，定义 source fiber posterior

\[
\mu_{R,M}(T)
=
\Pr[S=T\mid R,M],
\]

其支持 union 为

\[
W=W(R,M)
=
\bigcup_{T:\mu_{R,M}(T)>0}T,
\qquad w=|W|.
\]

观察 \(I\) 后，surviving source fiber 与 union 为

\[
\mathcal F_I
=
\{T:\mu_{R,M}(T)>0,\ T\cap I=\varnothing\},
\]

\[
W_I=\bigcup_{T\in\mathcal F_I}T,
\qquad w_I=|W_I|.
\tag{1}
\]

由于 \(S\in\mathcal F_I\)，总有 \(w_I\ge t\)。固定 \(R,M,I\) 后，从同一个物理状态执行同一 insertion word，所有 \(T\in\mathcal F_I\) 到达同一个 successor state。Zero false negatives保证该 successor接受 \(W_I\)。

## 2. 不重复发送 \(H\) 的直接 list code

### Lemma 2.1（single-pivot list inequality）

定义

\[
\mathsf A
=
\log\binom ut-\mathbb E\log\binom wt,
\tag{2}
\]

\[
\mathsf K
=
\mathbb E\log
\frac{\binom wt}{\binom{w_I}t},
\tag{3}
\]

以及 unavoidable fresh-label penalty

\[
\Gamma_{u,t,q}
=
\log\frac{\binom ut}{\binom{u-q}t}
=
\log\frac{\binom uq}{\binom{u-t}q}.
\tag{4}
\]

则

\[
\boxed{
H\ge
\mathsf A+\mathsf K-\Gamma_{u,t,q}.
}
\tag{5}
\]

### Proof

联合 source \((S,I)\) 的 entropy 是

\[
H(S,I\mid R)
=
\log\binom ut+\log\binom{u-t}q
=
\log\binom uq+\log\binom{u-q}t.
\tag{6}
\]

Alice 发送：

1. \(M\)，用固定 \(H\) bits；
2. \(I\)，作为 \(\binom Uq\) 中的元素；
3. \(S\)，作为 \(\binom{W_I}t\) 中的元素。

Decoder 由 \(R,M,I\) 穷举 \(\mathcal F_I\) 并计算 \(W_I\)，所以第三步可解码。由 source entropy 不超过 lossless message entropy，

\[
\log\binom uq+\log\binom{u-q}t
\le
H+\log\binom uq+\mathbb E\log\binom{w_I}t.
\tag{7}
\]

消去 \(\log\binom uq\)，再加减

\[
\mathbb E\log\binom wt
\]

即得 (5)。证毕。

式 (5) 的符号是唯一正确的：

- \(\mathsf A\) 是起点 state fiber support 给出的静态 saving；
- \(\mathsf K\) 是 common suffix 后 surviving union缩小的动态 saving；
- \(\Gamma\) 必须减去，因为 \(I\) 是从 \(U\setminus S\) 而不是 \(U\) 中抽取。

## 3. Deficit 与 transport saving 的准确关系

定义 fiber entropy deficit

\[
\mathsf D
=
\mathbb E\left[
\log\binom wt-H(S\mid R,M)
\right].
\tag{8}
\]

因为 \(S\) uniform，

\[
\boxed{
\mathsf D
=
I(S;M\mid R)-\mathsf A.
}
\tag{9}
\]

再令

\[
\mathsf J=I(S;I\mid R,M).
\tag{10}
\]

条件于 \((R,M,I)\)，\(S\) 支持在 \(\binom{W_I}t\)，所以

\[
H(S\mid R,M,I)
\le
\mathbb E\log\binom{w_I}t.
\]

与 (8) 相减得到 Theorem 4.1 在这个 pivot 上的精确形式：

\[
\boxed{
\mathsf K\le\mathsf D+\mathsf J.
}
\tag{11}
\]

注意这是 \(\mathsf K\) 的**上界**。它证明 transport loss 必须由 fiber deficit 或 suffix information支付，但不能证明 transport saving 本身为正。

把 (9) 与 (11) 代入 list lower-bound expression：

\[
\begin{aligned}
\mathsf A+\mathsf K-\Gamma
&\le
\mathsf A+\mathsf D+\mathsf J-\Gamma\\
&=
I(S;M\mid R)+I(S;I\mid R,M)-I(S;I\mid R).
\end{aligned}
\tag{12}
\]

这里

\[
I(S;I\mid R)=\Gamma_{u,t,q},
\tag{13}
\]

因为 \(R\) 独立，且 \(I\mid S\) uniform on \(\binom{U\setminus S}q\)。Chain rule于是给

\[
\boxed{
\mathsf A+\mathsf D+\mathsf J-\Gamma
=
I(S;M\mid R,I)
\le H.
}
\tag{14}
\]

因此 single-pivot transport-or-information inequality与 state budget完全相容，但没有产生一个超过 \(H\) 的矛盾；所有 deficit 与 suffix information恰好补回 conditional state information。

## 4. Exact-posterior code 是恒等式

如果第三步不用 support list \(\binom{W_I}t\)，而是在 exact posterior

\[
\mu_{R,M,I}
\]

下 arithmetic-code \(S\)，则 expected message entropy为

\[
H+\log\binom uq+H(S\mid R,M,I).
\]

与 source entropy比较，只得到

\[
\boxed{
H\ge I(S;M\mid R,I).
}
\tag{15}
\]

这只是 \(M\) 是 \(H\)-bit variable 的事实。若不显式发送 \(M\)，而把所有 state-indexed posterior lists组成一个 disjoint union，则 code必须同时标识使用哪一个 list；最优标识代价正是 state entropy。Kraft inequality重新给出 (15)，不会消除 \(M\) 的费用。

所以 posterior list code 与显式发送 \((M,S)\) 在信息论上等价。

## 5. 只使用 successor FPR 得到什么

由于 \(W_I\) 被 successor state接受、包含真实 \(S\)，并且与 inserted set \(I\) 不交，对每个预先固定的 \((S,I)\) 应用 pointwise FPR再平均，得到

\[
\mathbb E w_I
\le
t+\varepsilon(u-t-q).
\tag{16}
\]

函数 \(a\mapsto\log\binom at\) 在 \(a\ge t\) 上递增且凹。因此由 Lemma 2.1 的原始形式 (7)，

\[
\boxed{
H\ge
\log\binom{u-q}t
-
\log\binom{t+\varepsilon(u-t-q)}t.
}
\tag{17}
\]

当 \(u/t\to\infty\) 且 \(q=o(u)\) 时，

\[
\frac Ht
\ge
\log\frac1\varepsilon-o(1).
\tag{18}
\]

这只是 Carter static rate，没有 dynamic premium。原因很明确：单个 successor snapshot 的 FPR只约束 \(w_I\) 的绝对大小；它没有强迫相对于起点 \(W\) 的 shrinkage \(\mathsf K\) 为正。

## 6. 两个必要的 hostile tests

### 6.1 Full-family ALL-YES accounting test

取一个 state，接受整个 \(U\)，令 source fiber为 \(\binom Ut\)。这不是 \(\varepsilon<1\) 的合法 AMQ；它只用于测试 source-coding identity 的符号。此时

\[
\mathsf A=0,
\qquad
W=U,
\qquad
W_I=U\setminus I,
\]

所以

\[
\mathsf K
=
\log\frac{\binom ut}{\binom{u-q}t}
=
\Gamma.
\]

于是 (5) 精确给 \(H\ge0\)。任何遗漏 \(-\Gamma\) 的候选 inequality都会错误地声称 \(H\ge\Gamma>0\)。这证明 suffix penalty不可删除。

### 6.2 Exact dictionary

给定 exact state 后 posterior 是 point mass，\(W=S\)，且 \(I\cap S=\varnothing\)，所以

\[
\mathsf A=\log\binom ut,
\qquad
\mathsf K=0,
\qquad
\mathsf D=0.
\]

式 (5) 给出的 bound比 exact-state cost弱 \(\Gamma\)，因为 code发送了 \(I\)，而条件于 \(I\) 后 source entropy本来就从 \(\log\binom ut\) 降为 \(\log\binom{u-q}t\)。此时

\[
\mathsf J=I(S;I\mid M,R)=0
\]

（\(M\) 已精确确定 \(S\)），而 exact-posterior code同样只退回

\[
H\ge I(S;M\mid R,I)=\log\binom{u-q}t.
\]

若要恢复完整 exact-state cost，不能把 \(I\) 作为 decoder 免费获得或额外发送的 side information；这再次说明 suffix information 的使用必然有代价。

## 7. 单 pivot 的最终裁决

Theorem 4.1 已经能够严丝合缝地嵌入 source coding，但结果是 barrier，而不是新的 dynamic lower bound：

\[
\boxed{
\text{list lower bound}
=
\mathsf A+\mathsf K-\Gamma,
\qquad
\mathsf K\le\mathsf D+\mathsf J.
}
\]

若把第二式直接代入第一式，只会得到 upper consistency

\[
\mathsf A+\mathsf K-\Gamma
\le I(S;M\mid R,I)\le H,
\]

而不会得到更大的 lower bound。

要产生净 dynamic premium，下一步必须使用至少两个 pivots或多个 successor observations，并证明：

1. 不同 pivots 的实际 \(\mathsf K_s\) 中至少一个或某个加权组合足够大；
2. 所有 \(\mathsf D_s+\mathsf J_s\) 共享同一个
   \[
   I(X;M_{\rm final}\mid R)\le H
   \]
   budget，而不是分别支付；
3. fresh-label penalties \(\Gamma_s\) 只按 joint suffix source支付一次。

单 pivot、exact posterior、或只用 successor FPR都不可能完成这一步。最小剩余对象是 multi-pivot conditional total correlation，而不是另一个单-fiber entropy surrogate。
