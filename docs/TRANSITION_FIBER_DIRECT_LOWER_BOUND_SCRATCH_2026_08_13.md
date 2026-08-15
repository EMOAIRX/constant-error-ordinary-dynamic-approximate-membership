# 普通 KLZ 模型中的直接 transition-fiber 路线

> 日期：2026-08-13。状态：严格 scratch note。本文不使用 Section 5 reconstructible-set lifting，也不假设 history independence、accepted-set monotonicity、exact counts 或 locality。已得到一个普通模型下成立的单层碰撞定理；它只给 Carter 级别的单步收费，不能张量化为额外线性常数。

所有对数以 \(2\) 为底。

## 1. 模型与量词

令 \(R\) 是免费只读随机带。固定 \(R=r\) 后，filter 是 deterministic transducer：

\[
M_r(h\circ\operatorname{op}(x))
=T^r_{\operatorname{op},x}(M_r(h)),
\qquad Q_r(M,x)\in\{0,1\}.
\]

下面每个 history、key 和候选 family 都在抽取 \(R\) 以前固定。模型保证：

- 若 \(x\in S(h)\)，则对每个 \(r\)，\(Q_r(M_r(h),x)=1\)；
- 若 \(x\notin S(h)\)，则
  \[
  \Pr_R[Q_R(M_R(h),x)=1]\le\varepsilon.
  \]

证明从不在条件于 random physical state 后重新调用 FPR。

## 2. Pairwise successor collision

### Lemma 2.1

固定合法历史 \(h\)，当前集合 \(S\) 满足 \(|S|<n\)。对 distinct \(x,y\notin S\)，

\[
\boxed{
\Pr_R\!\left[
T^R_{\mathrm{ins},x}(M_R(h))
=T^R_{\mathrm{ins},y}(M_R(h))
\right]\le\varepsilon .
}
\tag{1}
\]

证明。记碰撞事件为 \(E\)。在 \(r\in E\) 上，`Insert(x)` 后 \(x\) 是成员，所以共同 successor 接受 \(x\)。但同一 successor 也由固定合法历史 \(h\circ\operatorname{Insert}(y)\) 到达；该历史中 \(x\) 是非成员。因此 \(E\) 包含于该固定历史下 \(x\) 的 false-positive event，概率至多 \(\varepsilon\)。

### Corollary 2.2：collision fibers

固定 \(X\subseteq U\setminus S\)，\(|X|=N\)。令

\[
c_{r,m}
=\bigl|\{x\in X:T^r_{\mathrm{ins},x}(M_r(h))=m\}\bigr|.
\]

对 ordered distinct pairs 求和可得

\[
\boxed{
\mathbb E_R\sum_m c_{R,m}(c_{R,m}-1)
\le\varepsilon N(N-1).
}
\tag{2}
\]

若 \(J\) 在 \(X\) 中均匀且独立于 \(R\)，令 \(C_R(J)\) 是 \(J\) 所在 successor cell 的大小，则

\[
\mathbb E C_R(J)\le1+\varepsilon(N-1),
\tag{3}
\]

从而

\[
\mathbb E\log C_R(J)
\le\log(1+\varepsilon(N-1)).
\tag{4}
\]

## 3. 精确 Rényi--Carter 定理

### Theorem 3.1

令

\[
Y=T^R_{\mathrm{ins},J}(M_R(h)).
\]

则

\[
\boxed{
H(Y\mid R)
\ge
\log\frac{N}{1+\varepsilon(N-1)}.
}
\tag{5}
\]

特别地，若 persistent memory 至多 \(H\) bits，

\[
H\ge\log\frac{N}{1+\varepsilon(N-1)}.
\tag{6}
\]

证明。固定 \(r\)，

\[
\Pr[Y=m\mid R=r]=c_{r,m}/N.
\]

故 conditional collision probability 为

\[
\operatorname{cp}(Y\mid R=r)
=\sum_m(c_{r,m}/N)^2.
\]

由 (2)，

\[
\mathbb E_R\operatorname{cp}(Y\mid R)
\le \frac1N+\varepsilon\left(1-\frac1N\right).
\]

Shannon entropy 不小于 Rényi-2 entropy，再对凸函数 \(-\log\) 使用 Jensen，即得 (5)。而 \(Y\mid R=r\) 的字母表至多 \(2^H\)，故 \(H(Y\mid R)\le H\)。

当 \(N\to\infty\) 时，右侧只趋于 \(\log(1/\varepsilon)\)。因此 pairwise collision 方法给出的是一个 fixed predecessor、一个未知 insertion label 的 Carter 项，不是 \(n\) 倍可加的动态项。

### Theorem 3.2：任意 fixed endpoint family

预先固定 \(K\) 条合法 histories \(h_1,\ldots,h_K\)，其 endpoint logical sets 两两不同。令 \(I\) 在 \([K]\) 中均匀且独立于 \(R\)，\(Y=M_R(h_I)\)。则

\[
\boxed{
H(Y\mid R)
\ge\log\frac{K}{1+\varepsilon(K-1)}.
}
\tag{7}
\]

因为对 \(i\ne j\)，可取 \(x\in S_i\triangle S_j\)；若两个 endpoint states 相同，较小逻辑集合的 endpoint 对 \(x\) 产生 false positive。随后重复 collision-entropy 证明。

式 (7) 即使 \(K\) 指数大也只趋于 \(\log(1/\varepsilon)\)。完整 state equality 是过于粗糙的统计量。

## 4. Partition entropy 与 support rank

令 \(\Pi_R\) 是 \(X\) 按 successor equality 得到的 partition。给定 \(R,Y\)，均匀 label \(J\) 在对应 cell 中均匀，所以有精确恒等式

\[
\boxed{
\log N
=H(Y\mid R)+H(J\mid Y,R),
}
\tag{8}
\]

且

\[
H(J\mid Y,R)=\mathbb E\log C_R(J).
\tag{9}
\]

因此 one-step 的正确 tradeoff 是

\[
\text{successor-state entropy}
+\text{within-cell rank}
=\log N.
\]

global ALL-YES coin 精确展示这一点。以概率 \(\varepsilon\) 所有 labels 进入同一 successor，以概率 \(1-\varepsilon\) 使用 distinct exact successors。则

\[
H(Y\mid R)=(1-\varepsilon)\log N,
\qquad
H(J\mid Y,R)=\varepsilon\log N.
\]

两项仍恰好相加为 \(\log N\)。多轮 collision pattern 的熵却只有一个 \(h_2(\varepsilon)\)，所以不能逐层收取 certificate entropy。

## 5. Deletion 与 ghosts

固定 history \(h\)，当前 \(x,y\in S\) 且 distinct。若 `Delete(x)` 与 `Delete(y)` 产生同一 state，则该 state 在删除 \(x\) 的世界中仍接受 \(x\)，因为它也是删除 \(y\) 后仍含 \(x\) 的 state。因此

\[
\Pr_R[T^R_{\mathrm{del},x}=T^R_{\mathrm{del},y}]
\le
\Pr_R[Q_R(M_R(h\circ\operatorname{Delete}(x)),x)=1]
\le\varepsilon.
\tag{10}
\]

这不是 rejection witness；collision 完全可以藏在 ghost event 中。故不能按 deletion 次数收费。

## 6. 为什么不能张量化

对每个 fixed prefix \(w_{<i}\)，Lemma 2.1 都成立；但沿随机输入 path，当前 state 依赖同一个 \(R\)。一般没有

\[
\Pr[\text{collision at }i\mid M_{i-1},w_{<i}]\le\varepsilon.
\]

global ALL-YES coin 使所有层 collision 完全相关，是最小反例。fixed-state fingerprint count vector 则给另一个警告：两次 insertion successor 相同仅当 hash labels 相同，概率约 \(1/q\ll\varepsilon\)，尽管结构 FPR 是常数。故 successor equality 甚至不接近 fingerprint upper bound 的紧统计量。

## 7. Sibling collision 与 LP path fiber 的形式差异

取 label universe \([N]\)。构造两层 graph：初态经 label \(a\) 到不同 predecessor \(p_a\)；从 \(p_a\) 经 label \(b\) 到 \(q_{a+b\bmod N}\)。

对每个 fixed \(p_a\)，映射 \(b\mapsto q_{a+b}\) 是 bijection，所以 sibling collision 为零。可是每个 \(q_c\) 有 paths \((a,c-a)\)，其 path-label union 是整个 universe。限制 \(a\ne b\) 只删除 \(O(1)\) 条 path，不改变结论。

因此 fixed-predecessor collision 不控制 Lovett--Porat 的

\[
L(v)=\bigcup\{\text{path labels reaching }v\}.
\]

缺失对象是跨 predecessors 的 merging consistency。

## 8. Two-step commutator 没有 FPR 约束

比较 `Insert(x); Insert(y)` 与反序。两个 endpoint logical sets 相同，所以 state 相同或不同都不产生 false-positive witness：

- history-independent exact dictionary 与 fingerprint counts 可以总是 commute；
- history-tagged exact dictionary 可以从不 commute，同时 query 完全精确；
- global coin 可以混合两种行为。

因此 noncommutativity 只测量 history information，必须和 endpoint-state entropy联合编码，不能单独给下界。

## 9. 精确剩余 open lemma

纯 successor-collision 路线目前不能推出超出 Carter 的线性项。需要一个 multi-parent inequality，联合控制

\[
\text{endpoint/path-state support}
+\text{shared-certificate entropy}
+\text{label-rank cost},
\]

并满足：exact dictionary 由 state/support 项支付；ALL-YES coin 的 certificate 只收一次；count-vector filter 的下界不超过其 fixed-state rate。当前没有这样的 universal inequality。
