# Acceptance-layer 路线的 hostile proof audit

> 结论：修正后的双向 pivot transcript 是可解码的；固定-chain rook identity 也是正确的纯组合恒等式。但后者不能控制前者，因为整个 acceptance chain 依赖待编码输入，并不是由最终状态给出的公共 side information。现阶段，acceptance forest / fixed-chain rook extremality 作为 lower-bound 证明路线是 **no-go**；pivot transcript 本身仍可作为其他 joint-support inequality 的载体。

## 1. 设置

固定随机带 \(r\)，考虑 history-independent、monotone filter。令

\[
X=(X_1,\ldots,X_n)\in U^{\underline n},
\qquad S_j=\{X_1,\ldots,X_j\},
\]

并令 \(M_j\) 和 \(A_j\) 分别为集合 \(S_j\) 的物理状态和 accepted set。固定 \(r\) 后，状态确定查询函数，所以 \(M_j\) 确定 \(A_j\)。History independence 保证 decoder 只要恢复 \(S_j\)，就可以重建同一个 \(M_j,A_j\)。

由 monotonicity，

\[
A_0\subseteq A_1\subseteq\cdots\subseteq A_n.
\]

定义

\[
L_i=A_i\setminus A_{i-1},\quad L_0=A_0,
\qquad
T_j=\min\{i:X_j\in A_i\}\le j.
\]

## 2. 严格的 pivot decoder 与 \(\mathcal L_s\)

Alice 先发送 \(M_n\)，再发送整个 \(T=(T_1,\ldots,T_n)\)。随后按顺序

\[
1,2,\ldots,s,n,n-1,\ldots,s+1
\]

发送 ranks。下面的候选集均可由 decoder 当时已知的信息计算。

### 2.1 正向部分：\(j\le s\)

此时 decoder 已恢复 \(X_1,\ldots,X_{j-1}\)，因而可重建所有 \(A_i,L_i\)（\(i\le j-1\)），并从 \(M_n\) 得到 \(A_n\)。令

\[
K_j^-=\{X_1,\ldots,X_{j-1}\}.
\]

若 \(T_j<j\)，使用

\[
P_j=L_{T_j}\setminus K_j^-.
\]

若 \(T_j=j\)，不能使用尚未知的 \(L_j\)，而必须使用

\[
P_j=A_n\setminus A_{j-1}.
\]

两种情形都有 \(X_j\in P_j\)。收到 rank 后，decoder 恢复 \(X_j\)，从而继续重建下一个 prefix state。

### 2.2 反向部分：\(k>s\)

处理 \(k\) 时，decoder 已知

\[
K_k^+=\{X_1,\ldots,X_s,X_{k+1},\ldots,X_n\}.
\]

它从 \(M_n\) 删除已恢复的 suffix keys；history independence 保证所得状态是 \(M_k\)，所以 \(A_k\) 可计算。它也可由 prefix \(S_s\) 重建 \(A_s\) 及所有 \(L_i\)（\(i\le s\)）。

若 \(T_k\le s\)，使用

\[
Q_k=L_{T_k}\setminus K_k^+.
\]

若 \(T_k>s\)，使用

\[
Q_k=(A_k\setminus A_s)\setminus K_k^+.
\]

同样 \(X_k\in Q_k\)。注意第二式必须扣除已恢复 suffix 中碰巧早已位于 \(A_k\) 的 keys；直接写成 \(\lvert A_k\setminus A_s\rvert\) 一般不对。

### 2.3 完整 functional

定义

\[
\boxed{
\mathcal L_s(X,T,A_\bullet)
=
\sum_{j=1}^{s}\log \lvert P_j\rvert
+
\sum_{k=s+1}^{n}\log \lvert Q_k\rvert.
}
\tag{1}
\]

这里的候选集按上述两种分支定义。它依赖 \(X\)，不能只写成 \(\mathcal L_s(T,A_\bullet)\) 而隐藏 decoded-key exclusions。

把每个 rank 看成其随过去 transcript 变化的有限字母表中的随机变量，有

\[
H(\mathsf{rank}_j\mid\mathsf{past})\le \mathbb E\log \lvert P_j\rvert
\]

及相同的 \(Q_k\) 版本。因此无需为每个 rank 支付一 bit 的 ceiling overhead。完整 lossless transcript 给出

\[
\boxed{
\log \lvert U\rvert^{\underline n}
\le
H+H(T\mid M_n,r)
+\mathbb E\mathcal L_s.
}
\tag{2}
\]

所以 pivot protocol 本身是 **go**。

## 3. Fixed-chain rook identity 的精确适用范围

若一个 nested chain

\[
C=(A_0,\ldots,A_n)
\]

是外部固定的，令 \(d_i=\lvert L_i\rvert\)、\(D_j=\lvert A_j\rvert\) 及 \(c_i(t)=\lvert\{j:t_j=i\}\rvert\)。则

\[
\sum_{t_j\le j}\prod_i(d_i)_{\underline{c_i(t)}}
=
\prod_{j=1}^n(D_j-j+1)
\tag{3}
\]

是正确的。由 log-sum，条件于这个固定 chain，

\[
H(T\mid C)
+\mathbb E\!\left[
\left.
\sum_i\log(d_i)_{\underline{c_i(T)}}
\right|C
\right]
\le
\sum_j\log(D_j-j+1).
\tag{4}
\]

问题不在 (3)--(4)，而在实际 filter 中 \(C=C(X,r)\) 依赖待传输 batch。最终状态 \(M_n\) 一般只给出 \(A_n\)，不给出 intermediate \(A_j\)。如果按 chain fibers 使用 (4)，完整计数必须包含

\[
H(C\mid M_n,r),
\tag{5}
\]

或一个等价的 transition-fiber 支持项。该项可能是线性的、\(\Theta(n\log n)\)，甚至包含 key identities；不能删除。

更根本地，(4) 中的 layer-location code 假设 chain 已知，而 (1) 的 decoder 刻意不发送 chain。二者不是同一个 functional。

## 4. 决定性的 exact-dictionary 测试

令

\[
A_j=S_j.
\]

则 \(T_j=j\)、\(d_j=1\)、\(D_j=j\)。固定-chain rook 右侧为

\[
\sum_{j=1}^n\log(D_j-j+1)=0.
\]

但真实 pivot ranks 为

\[
\prod_{j=1}^{s}\lvert A_n\setminus A_{j-1}\rvert
=\frac{n!}{(n-s)!},
\]

以及

\[
\prod_{k=s+1}^{n}\lvert A_k\setminus A_s\rvert
=(n-s)!.
\]

故对每个 pivot \(s\)，

\[
\boxed{\mathcal L_s=\log n!.}
\tag{6}
\]

这正好把最终 unordered set 的状态编码补成 ordered tuple。给定 \(M_n\) 后，随机 chain 还携带随机插入顺序，

\[
H(C\mid M_n,r)=\log n!.
\]

因此，任何从 fixed-chain rook 代价 \(0\) 直接推出真实 pivot 代价 \(0\) 的论证都立即错误。

## 5. 四类 hostile mechanisms

以下机制都在普通 one-sided 模型内，并在固定随机带后 HI、monotone。它们不击穿 (2)，但说明 acceptance times 不会自动产生 paintbox extremality。

### 5.1 Independent hits

在公共随机带上取有向图，每个有序对 \(y\to x\) 独立地以概率 \(p\) 出现，定义

\[
A(S)=S\cup\{x:\exists y\in S,\ y\to x\}.
\]

取

\[
p=1-(1-\varepsilon)^{1/n},
\]

则 size-\(n\) 集合对固定 absent key 的 FPR 是 \(\varepsilon\)。对随机 batch，

\[
\Pr[T_j=j]=(1-p)^{j-1},
\]

且对 \(i<j\)，

\[
\Pr[T_j=i]=p(1-p)^{i-1}.
\tag{7}
\]

不同 targets 的 hit times 可独立，但同一 inserted key 会同时创建一个大 layer。这不是 occupancy partition。一个直接实现仍需保存 \(S\) 才能支持删除，所以是 exact-dictionary-size hostile example，而不是更小空间的反例。给定最终 exact state 后，\((T,\mathsf{ranks})\) 仍必须传输集合的排列，故其联合 entropy 至少为 \(\log n!\)。

### 5.2 All-or-none global coin

公共随机 bit \(B\sim\operatorname{Bernoulli}(\varepsilon)\)。若 \(B=1\)，令 \(A(S)=U\)；若 \(B=0\)，令 \(A(S)=S\)。于是

\[
T=(0,\ldots,0)\quad(B=1),
\qquad
T=(1,2,\ldots,n)\quad(B=0).
\]

在 ALL-YES branch，

\[
\mathcal L_s=\log \lvert U\rvert^{\underline n}
\]

对每个 \(s\) 都成立；在 exact branch，

\[
\mathcal L_s=\log n!.
\]

因此（忽略由公开 \(B\) 决定的零条件熵）

\[
\mathbb E\mathcal L_s
=
\varepsilon\log \lvert U\rvert^{\underline n}
+(1-\varepsilon)\log n!.
\tag{8}
\]

它显示逐 key hit 熵不能直和；一个 global coin 可以让所有 acceptance times 完全相关。

### 5.3 Fixed-size frozen mask

公共随机带均匀选择固定大小集合 \(R\subseteq U\)，其中

\[
\lvert U\setminus R\rvert=\varepsilon \lvert U\rvert,
\]

并定义

\[
A(S)=(U\setminus R)\cup S.
\]

则

\[
T_j=0\quad(X_j\notin R),
\qquad
T_j=j\quad(X_j\in R).
\tag{9}
\]

令 \(m=\lvert S_n\cap R\rvert\)。给定 \(R,M_n\)，最终状态只给出 unordered set \(S_n\cap R\)。完整 \(T\) 给出哪些 positions 落在 \(R\)。条件于实现值 \(m\)，

\[
H(T\mid R,M_n,m)=\log\binom n m,
\]

因而无条件公式是

\[
H(T\mid R,M_n)=\mathbb E\log\binom n m.
\]

真实 ranks 的乘积为

\[
(\varepsilon \lvert U\rvert)_{\underline{n-m}}\,m!,
\]

即

\[
\boxed{
\mathcal L_s
=
\log(\varepsilon \lvert U\rvert)_{\underline{n-m}}
+\log m!,
}
\tag{10}
\]

与 \(s\) 无关。fixed-chain rook code 会把 singleton layers 中的 \(m\) 个 inside keys 当作 chain 已知，从而漏掉 \(\log m!\) 的顺序成本。

### 5.4 Overlapping hyperedge witnesses

在公共随机带上为每个 query key \(x\) 指定 witness family \(\mathcal H_x\subseteq 2^U\)，其分布满足对每个 \(x\notin S\)、\(\lvert S\rvert\le n\)，

\[
\Pr_r[\exists W\in\mathcal H_x:W\subseteq S]\le\varepsilon.
\]

例如，可以让一组 query keys 共享一个均匀随机的 \(d\)-subset witness \(W\)，并选择 \(d\) 使

\[
\frac{\binom nd}{\binom{\lvert U\rvert-1}d}\le\varepsilon.
\]

定义

\[
A(S)=S\cup\{x:\exists W\in\mathcal H_x,\ W\subseteq S\}.
\]

这是 HI、monotone、one-sided。对 batch key \(X_j\)，

\[
T_j=
\min\!\left(
j,
\min_{W\in\mathcal H_{X_j}}
\max\{i:X_i\in W\}
\right),
\tag{11}
\]

其中不完全包含在 batch prefix 的 witness 视为 \(+\infty\)。重叠 witnesses 可使许多 keys 同时进入一个 layer，也可让多个 acceptance times 通过共享 witness 高度相关；不存在单一 fingerprint parent。直接实现仍需知道 \(S\) 以判断 witnesses 和处理删除，因此同样是 exact-state hostile example。它证明 restricted-growth word 的可实现域远大于 paintboxes，但尚未给出更省空间的 ordinary dynamic filter。

## 6. Go / no-go

- **双向 pivot decoder 与式 (1)--(2)：GO。** 它是严格、可计算、容纳 global correlation 和 shared witnesses 的 lossless transcript。
- **fixed-chain rook identity (3)：GO，但仅作为条件于外部给定 chain 的组合恒等式。**
- **用 (3)--(4) 上界真实 pivot functional：NO-GO。** 缺失输入相关 chain 的信息项；exact dictionary 已给出 \(\log n!\) 的明确反例。
- **acceptance forest 单独导出非平凡 lower-bound gap：NO-GO。** 它不记录 physical-state/transition-fiber 成本。
- **“paintbox 是 extremizer”：当前无证据。** Independent hits 与 hyperedge witnesses 展示更大的合法机制类。
- **当前没有 ordinary KLZ 模型下击穿 fingerprint benchmark 的动态-filter 构造，也没有由 acceptance layers 得到新的常数下界。**

如果继续这条主线，所需的新 lemma 不能是 fixed-chain rook extremality，而必须直接控制

\[
\boxed{
\inf_s\left\{
H(T\mid M_n,r)+\mathbb E\mathcal L_s
\right\}
}
\tag{12}
\]

或等价的 transition-constrained joint support，并且必须把随机 chain 的信息通过 \(M_n\) 与 sequential ranks 共同核算。现有 rook identity 对 (12) 没有提供非平凡上界。
