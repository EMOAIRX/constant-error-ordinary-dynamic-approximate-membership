# 普通动态 Filter 的完整 Fiber-Union 提升

> 日期：2026-08-13。状态：新主定理候选。核心 transport lemma、单预算
> 误差核算和 KLZ 接口已经写出；在对外声称正式定理前，仍应把 Lemma 4.5
> 按下面的 slack 参数逐行重写。本文不使用 history independence、accepted-set
> monotonicity、有限历史保证或 partition-dependent reconstructible sets。

所有对数均以 (2) 为底。令 (u=|U|)。

## 1. 候选主定理

定义

\[
B(\delta)
=\log\frac1\delta+(1-\delta)\log e-2h_2(\delta),
\qquad 0<\delta\le\frac12.
\tag{1}
\]

### Theorem 1（ordinary fixed-error lower bound；候选）

设 (\delta\in(0,1/2]) 为固定常数，且

\[
\frac{u}{n^2}\longrightarrow\infty.
\tag{2}
\]

考虑 KLZ Definition 2.1 的普通动态 approximate-membership filter：固定
(H)-bit memory、免费只读随机带、key-only `Insert/Delete/Query`、zero false
negative，以及对每条固定合法历史和每个固定当前非成员的 pointwise FPR
至多 (\delta)。若结构支持 (f(n)=\omega(n)) 次合法操作，则

\[
\boxed{H\ge nB(\delta)-o(n).}
\tag{3}
\]

这里 filter 可以 history-dependent、non-monotone，并可使用 ghosts、全局
certificates、relocation 和任意跨时间相关性。

### Corollary 2（(\varepsilon=1/2)）

对原误差为 (1/2) 的 ordinary filter，取五份使用独立随机带的副本并对
query 取 AND。复合 filter 的误差为 (2^{-5}=1/32)，空间为 (5H)。若
Theorem 1 成立，则

\[
5H\ge nB(1/32)-o(n),
\]

因而

\[
\boxed{
H\ge\frac{B(1/32)}5n-o(n)
=1.1992732344471508\ldots n-o(n).
}
\tag{4}
\]

这严格超过 Lovett--Porat 正式的 (1.1n)、one-cut 数值
(1.10213\ldots n)，以及其 Section 3.5 报告但未认证的约 (1.13n)。

## 2. 为什么旧的 Section 5 对象失败

KLZ 的 reconstructible set 只量化 conform to 随机 partition
(\pi=(U_1,\ldots,U_b)) 的历史。固定 obfuscation transcript 和 filter tape
后，它仍依赖未暴露 keys 的 partition assignments。因此 Section 4 Claim 4.6
所需的“固定集合与随机 (U_k) 相交”条件化不成立。

新对象量化所有合法历史，完全不引用 (\pi)。代价是 exact monotonicity
变为 approximate transport；条件 (2) 恰好使 transport loss 消失。

## 3. 带时间索引的完整 fiber union

固定 filter tape (R)。对 memory state (m)、逻辑集合大小 (t) 和操作数
(q)，定义

\[
\mathcal W_R(m,t,q)
=\bigcup\left\{
S(h):
h\text{ 是从空集开始的合法历史},
|h|=q,
|S(h)|=t,
M_R(h)=m
\right\}.
\tag{5}
\]

时间索引 (q) 不能省略。否则一个 key 的 witness history 可能比数据结构承诺
支持的 horizon 更长，拼接 KLZ suffix 后便超出模型保证。

### Lemma 3（sandwich 与 FPR）

若固定历史 (h) 在 tape (R) 上到达 (m=M_R(h))，且
((t,q)=(|S(h)|,|h|))，则

\[
S(h)\subseteq\mathcal W_R(m,t,q)\subseteq A_R(m).
\tag{6}
\]

证明。第一项由 (h) 本身作为 witness。若
(x\in\mathcal W_R(m,t,q))，存在另一条合法历史 (h_x) 到达同一 memory
state，且其当前集合包含 (x)。zero false negative 迫使对该相同 state 查询
(x) 返回 YES，故 (x\in A_R(m))。

因此，对每条固定真实历史 (h)，

\[
\mathbb E_R|\mathcal W_R(M_R(h),t,q)|
\le t+\delta(u-t)
\le N:=(1-\delta)n+\delta u.
\tag{7}
\]

注意 (7) 只使用 pointwise FPR；没有逐 tape 的 accepted-set size 假设。

## 4. Approximate transport

令 (h) 是合法 prefix，(\tau) 是 self-contained suffix。记
(I(\tau)) 为 suffix 中所有被 `Insert` 的不同 keys。若
(x\in\mathcal W_R(M_R(h),t,|h|))，固定一条 witness history (h_x)，其
endpoint set 记为 (T_x)。

### Lemma 4（deterministic transport）

若

\[
T_x\cap I(\tau)=\varnothing,
\tag{8}
\]

则 (h_x\tau) 合法，并且

\[
x\in
\mathcal W_R(M_R(h\tau),|S(h\tau)|,|h\tau|).
\tag{9}
\]

证明。self-contained suffix 中每次 deletion 都删除此前在同一 suffix 中插入
且尚未删除的 key。因此它不会删除初始集合 (T_x) 的 key。拼接失败的唯一
可能是某次 `Insert(y)` 时 (y\in T_x)；式 (8) 排除了这一点。固定 tape 后，
(h) 与 (h_x) 到达相同 state，再执行相同 suffix 必到达相同 endpoint
state。并且 (x) 一直留在替代世界的逻辑集合中。

这一步不要求 actual accepted sets 单调。

### Lemma 5（随机 obfuscation suffix 的 loss）

在 KLZ obfuscating tree 中，条件于一个 prefix 的全部 labels、filter tape 和
操作数。设后续 self-contained suffix 至多包含 (Q) 个 insertion positions，
每个 position 的 label 在相应 block (U_j) 中均匀抽取；一个 edge 内无放回，
不同 edges 独立。则

\[
\mathbb E\left|
\mathcal W_R(M_R(h),t,|h|)
\setminus
\mathcal W_R(M_R(h\tau),t',|h\tau|)
\right|
\le t bQ\le nbQ.
\tag{10}
\]

证明。固定 (x) 及 witness (T_x)，其中 (|T_x|=t)。对一个已经由 prefix
暴露了 block 的 (y\in T_x)，union bound 给

\[
\Pr[y\in I(\tau)]
\le \max_j\frac{Q_j}{u/b}
\le\frac{bQ}{u}.
\]

未暴露 key 的剩余 partition assignment 是超几何分布，只会给同阶或更小的
界；把分母替换为 (u-L) 会产生 (1+o(1)) 因子，其中 (L) 是 prefix
暴露的不同 labels 数。于是

\[
\Pr[T_x\cap I(\tau)\ne\varnothing]
\le\frac{tbQ}{u}(1+o(1)).
\]

对至多 (u) 个 (x) 求和，再用 Lemma 4 即得 (10)。正式稿可把右侧写成
(tbQ\,u/(u-L))，避免渐近记号。

## 5. 参数选择：horizon 与 transport 同时满足

沿用 KLZ 的

\[
m=n/b,
\qquad M=4^b.
\]

整棵 obfuscating tree 的操作数和任一 relevant suffix 的 insertion positions
均满足

\[
Q\le \frac{nM^{b+1}}b.
\tag{11}
\]

由 (10)，取统一 transport slack

\[
D_n:=n^2M^{b+1}.
\tag{12}
\]

因为 (u/n^2\to\infty) 且 (f(n)/n\to\infty)，可令
(b=b(n)\to\infty) 足够慢，使

\[
Q=o(f(n)),
\qquad
D_n=o\left(\frac{\delta u}{4^b}\right).
\tag{13}

例如只需让 (4^{b(b+2)}=o(u/n^2)) 且
(4^{b(b+1)}/b=o(f(n)/n))。因此所有 actual 与 witness histories 都在
承诺 horizon 内，同时 transport loss 小于 KLZ Lemma 4.8 已经容忍的
(4^{-b}) slack。

## 6. 恢复 KLZ 的单调 profile

把 (5) 应用于 KLZ states (G_k,F_k)，并记

\[
g_k=\mathbb E|\mathcal W(G_k,km,q_{G_k})|.
\tag{14}

由 (G_{k-1}\) 到 (G_k) 的 suffix self-contained，Lemma 5 给

\[
g_k\ge g_{k-1}-D_n.
\tag{15}

定义 corrected profile

\[
\widehat g_k=g_k+kD_n,
\qquad
\widehat N=N+bD_n,
\tag{16}

以及

\[
a_k=\frac{\widehat g_k-\widehat g_{k-1}}{\widehat N}.
\tag{17}

则 (a_k\ge0)，且

\[
\sum_{k=1}^b a_k\le1.
\tag{18}

KLZ Claim 4.7 的 obfuscation coupling 是 operational-history 的分布恒等式，
不依赖 accepted-set monotonicity。把 statistic 换成带时间索引的
(|\mathcal W|) 后仍有

\[
\mathbb E|\mathcal W(F_r)|
\le g_r+\frac{N}{M}.
\tag{19}

另一方面，Lemma 5 对 (G_\ell\) 到 (F_r) 的整个 suffix 给

\[
\mathbb E|\mathcal W(G_\ell)\setminus\mathcal W(F_r)|
\le D_n.
\tag{20}

故

\[
\begin{aligned}
\mathbb E|\mathcal W(F_r)\setminus\mathcal W(G_\ell)|
&=\mathbb E|\mathcal W(F_r)|-g_\ell
 +\mathbb E|\mathcal W(G_\ell)\setminus\mathcal W(F_r)|\\
&\le \widehat N a_{(\ell,r]}+\frac NM+D_n.
\end{aligned}
\tag{21}
\]

这就是 exact monotonicity 恒等式
(|F_r\setminus G_\ell|=|F_r|-|G_\ell|) 的合法替代。所有层共享同一个
profile 和同一个 final (H)-bit state；没有重复收费状态预算。

## 7. 为什么 Claim 4.6 现在重新合法

(\mathcal W_R(m,t,q)) 只由 transducer、tape、state、size 和 time 定义，不
依赖 KLZ 随机 partition。条件于完整 obfuscation sequence (\sigma) 和 filter
tape 后，

\[
\mathcal D^*
=\mathcal W(F_r)\setminus\mathcal W(G_\ell)
\tag{22}
\]

是固定集合。未在 (\sigma) 中出现的 keys 到 (U_k) 的 assignment 仍均匀。
因此原 Claim 4.6 的 removing-(U_k) 计算逐字成立：若 (L) 是 transcript
暴露的不同 labels 数，(L_k) 属于 (U_k)，则

\[
\mathbb E[|\mathcal D^*\cap U_k|\mid\sigma,R]
\le L_k+\frac{u/b-L_k}{u-L}|\mathcal D^*|.
\tag{23}
\]

结合 (21)、(L\le nM^{b+1}/b) 与 (13)，得到 KLZ Lemma 4.5 所需的

\[
\mathbb E|\mathcal D^*\cap U_k|
\le
\frac{\delta u}{b}(1+o(1))
\left(a_{(\ell,r]}+O(4^{-b})\right).
\tag{24}

真实 batch keys 属于 (\mathcal W(F_r))，所以原 `Send` decoder 仍正确；
hit bit 改为检查 (x\in\mathcal W(G_\ell))。由 Lemma 3，该 event 的概率
至多 (\delta)。

## 8. 通信计算

将 (24) 代入 KLZ Section 4 的 fixed-error 版本。每个 batch 的期望编码长度
保持为

\[
\frac nb\log(u/b)
+\frac nb\log\delta
+(1-\delta)\frac nb
\log\left(a_{(\ell,r]}+O(4^{-b})\right)
+\frac nb\bigl[2h_2(\delta)+\delta\log e\bigr]
+o(n/b),
\tag{25}

等价地，总通信比较给

\[
H\ge
n\left[
\log\frac1\delta
-2h_2(\delta)
+(1-\delta)\log e
\right]-o(n).
\tag{26}

Lemma 3.4 只要求 (a_k\ge0) 且总和至多 (1)，故可应用于 corrected
profile (17)。Lemma 4.8 吸收 (24) 的 (O(4^{-b})) slack。这给出 (3)。

## 9. 敌对审计

### 9.1 不使用 monotonicity

唯一的集合 transport 来自同一 physical state 后执行同一合法 suffix。
actual accepted set 可以任意缩小；证明从不比较两个时刻的 accepted sets。

### 9.2 不使用 history independence

fiber 按完整 memory state 和操作数定义。不同历史只有在 state collision 后才
合并；(F_k,G_k) 仍可完全不同。

### 9.3 不依赖 partition

替代 witness histories 不要求 conform to (\pi)。这正是 (23) 可条件化的
原因，也是相对 Section 5 的关键变化。

### 9.4 Fresh legality

Lemma 4 明确排除 witness set 与 suffix insert labels 的冲突。loss 由 (10)
收费，而不是假设任意 witness continuation 自动合法。

### 9.5 有限操作 horizon

时间索引和 (13) 保证 witness history与 suffix 的总长度在 filter 承诺内。
不能改回无时间索引的 fiber。

### 9.6 已知 upper bounds

(1.199273n) 远低于 exact fingerprint count-vector 的
(2.384499842n+o(n)) fixed-state upper bound，不产生已知矛盾。此前错误的
Section 5 mechanical lifting 会推出 (2.442695n)，本证明不会。

## 10. 正式投稿前必须补齐的三点

1. 把 Lemma 5 写成 finite-(u) 超几何式，显式区分 prefix 已暴露 key 与
   未暴露 key，并保留 (u/(u-L)) 因子。
2. 按 (21)--(24) 重写 KLZ Lemma 4.5，逐项验证 (D_n)、exposed-label
   error 和 (N/M) 共同不超过 (O(4^{-b})) normalized slack。
3. 明确 horizon convention：若算法只承诺最多 (f(n)) 次操作，fiber 中只
   量化与 actual prefix 相同长度的 histories，并在参数选择中留出整个 suffix
   的长度。

这三项是正文级技术工作，不是新的概念障碍。若 finite-(u) Lemma 5 在完整
条件化下成立，则 (3)--(4) 是普通模型的新下界，而不再是 monotone 子类结果。

