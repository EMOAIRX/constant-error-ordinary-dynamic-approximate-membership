# Acceptance layers：ordinary dynamic filter 的具体 multi-letter 路线

> 状态：经 hostile audit 后降级为 no-go 记录。固定 nested-chain 的联合计数恒等式是正确的纯组合事实，修正后的双向 pivot communication protocol 也成立；但 chain 本身依赖待编码输入，不能作为 decoder 的免费 side information。Exact dictionary 显示漏掉的 \(H(C\mid M_n,r)\) 可恰为 \(\log n!\)。因此本文原拟的 fixed-chain extremality 路线不能推出动态 filter 下界。

完整反例与修正 protocol 见 [ACCEPTANCE_LAYER_HOSTILE_PROOF_AUDIT.md](./ACCEPTANCE_LAYER_HOSTILE_PROOF_AUDIT.md)。

## 1. Warmup 定义

先在 KLZ 的 history-independent、monotone warmup 中固定随机带。令随机有序真键为

\[
X_1,\ldots,X_n,
\qquad
S_j=\{X_1,\ldots,X_j\},
\]

并令 accepted sets 构成 nested chain

\[
A_0\subseteq A_1\subseteq\cdots\subseteq A_n.
\]

定义 acceptance layers

\[
L_0=A_0,
\qquad
L_i=A_i\setminus A_{i-1},
\]

以及

\[
d_i=|L_i|,
\qquad
D_j=|A_j|=\sum_{i=0}^j d_i.
\]

每个真键的首次接受时间为

\[
T_j=\min\{i:X_j\in A_i\}.
\]

one-sidedness 给出 `0<=T_j<=j`。

`T_j=0` 表示 permanent/global YES；`T_j=j` 表示键到来时才被接受；`0<T_j<j` 表示它在插入前已是假阳性。

把 `j` 指向 `T_j` 可画成 forest-like 图，但一般 filter 的触发可能依赖多个 earlier keys，故 `T_j` 不具有单一 parent 的因果意义。更准确的对象是 acceptance-time restricted-growth word。

## 2. Fingerprints 在该对象中的位置

若键有 IID categorical fingerprint `H_j`，则

\[
T_j=\min\{i\le j:H_i=H_j\}.
\]

同一 fingerprint 的 indices 形成一个 partition block

\[
B=\{j_1<\cdots<j_c\},
\]

满足

\[
T_{j_1}=j_1,
\qquad
T_{j_2}=\cdots=T_{j_c}=j_1.
\]

所以 fingerprints 对应 paintbox partition；heterogeneous fingerprints 对应任意 atom weights；permanent-positive region 对应 root `0`。

一般 filter 的 acceptance-time word 不必来自 partition paintbox。thresholds、overlapping hyperedges 和共享 witnesses 都可产生更一般的 restricted-growth law。

## 3. 已证：固定 chain 的 rook-polynomial 恒等式

给定 acceptance word `t`，令

\[
c_i(t)=|\{j:t_j=i\}|.
\]

在固定 nested chain 中，产生该 word 的 ordered distinct batches 数为

\[
\prod_{i=0}^n(d_i)_{\underline{c_i(t)}}.
\]

于是有恒等式

\[
\boxed{
\sum_{\substack{t_1,\ldots,t_n\\t_j\le j}}
\prod_{i=0}^n(d_i)_{\underline{c_i(t)}}
=
\prod_{j=1}^n(D_j-j+1).
}
\tag{1}
\]

证明：左侧按首次进入的 layer 对全部 ordered distinct batches 分类。顺序选择 `X_j` 时，它必须位于 `A_j`；此前 `j-1` 个真键全部已在 `A_j` 中，所以恰有 `D_j-j+1` 个剩余选择。两种计数得到 (1)。

由 log-sum/Gibbs inequality，任意支持在这些 words 上的分布满足

\[
\boxed{
H(T)
+\mathbb E\sum_{i=0}^n
\log(d_i)_{\underline{c_i(T)}}
\le
\sum_{j=1}^n\log(D_j-j+1).
}
\tag{2}
\]

式 (2) 是一个真正的 multi-letter branch--location inequality：

- 不逐 key 支付 `h_2(epsilon)`；
- 同一 layer 内的位置用 falling factorial 而不是 powers；
- collision group 的 partition entropy 与 location saving 自动抵消；
- frozen masks 与 shared witnesses 可直接代入。

## 4. 为什么 forest 单独是 no-go

`T` 不记录 layer sizes。正确联合代价是

\[
H(T)+
\mathbb E\sum_i
\log(d_i)_{\underline{c_i(T)}},
\]

而不是 `H(T)` 或 `sum_j log d_{T_j}`。

此外，沿单条输入链，几乎任意满足 `T_j<=j` 的 word 与 nested sets 都可实现。例如定义

\[
A(S)=S\cup\bigcup_{i:S_i\subseteq S}A_i.
\]

它在指定 chain 上实现 `A(S_j)=A_j`，但可能需要近乎 exact-set 的巨大空间。

exact dictionary 更直接：

\[
A_j=S_j,
\qquad
T_j=j,
\qquad
d_j=1.
\]

此时 forest 熵为零，物理状态却很昂贵。因此 acceptance forest 不能脱离最终状态和 transition-compatible fibers 单独优化。

## 5. 正确的 KLZ 双向 pivot protocol

保留 KLZ 顺序

\[
1,2,\ldots,s, n,n-1,\ldots,s+1.
\]

先发送最终物理状态 `M_n`，再联合编码完整 acceptance-time word `T`。

- 对 `j<=s`：若 `T_j<j`，从 earlier layer `L_{T_j}` 定位；若 `T_j=j`，从 `A_n\setminus A_{j-1}` 定位。
- 对 `j>s`：decoder 持有删除后状态 `M_j`；若 `T_j<=s`，从 `L_{T_j}` 定位；若 `T_j>s`，从 `A_j\setminus A_s` 定位。

所有位置集合必须扣除已解码 keys，故使用 falling factorial。记完整位置代价为

\[
\mathcal L_s(T,A_\bullet).
\]

可构造一个 one-way protocol，使

\[
\log|U|^{\underline n}
\le
H
+H(T\mid M_n,r)
+\mathbb E\mathcal L_s(T,A_\bullet).
\tag{3}
\]

因此

\[
\boxed{
H\ge
\log|U|^{\underline n}
-H(T\mid M_n,r)
-\mathbb E\mathcal L_s(T,A_\bullet).
}
\tag{4}
\]

在 exact dictionary 上，式 (4) 正确恢复 exact-set/factorial cost；它不会像单独的 forest entropy 那样错误地给出零。

## 6. 原拟的缺失 lemma（已否决）

真正需要证明或反驳的是：对任意 HI+monotone dynamic filter，存在 pivot `s`，使

\[
\boxed{
H(T\mid M_n,r)
+\mathbb E\mathcal L_s(T,A_\bullet)
\le
\log|U|^{\underline n}
-nR_*(\varepsilon)
+o(n),
}
\tag{5}
\]

其中 `R_*(epsilon)` 严格改善现有 arbitrary-filter lower bound。若进一步证明 `R_*=R_FM`，才得到 fingerprint extremality。

式 (5) 不能由固定-chain rook identity 导出，因为 \(\mathcal L_s\) 的真实 decoder 并不知道整个 input-dependent chain。Exact dictionary 已给出决定性反例。继续研究时必须直接控制

\[
\inf_s\left\{H(T\mid M_n,r)+\mathbb E\mathcal L_s\right\},
\]

或等价的 transition-constrained joint support；现有 rook identity 对此没有非平凡上界。

## 7. Hostile tests

### Frozen mask

若 `R` 内 exact、`U\setminus R` 永久 YES，则

\[
T_j=
\begin{cases}
0,&X_j\notin R,\\
j,&X_j\in R.
\end{cases}
\]

它是 root-0 加 singleton roots。完整位置代价仍支付永久区域和 exact subset 的成本，因此只否决 `H(T)` 版本，不否决 (4)--(5)。

### Shared/high-order witnesses

许多 keys 可同时进入同一 `L_i`。falling factorial 允许这种共享，不逐键重复收费。真正未解的是：这种高阶共享能否使式 (5) 的左侧严格大于所有 paintboxes，从而产生更低的 filter-space rate。

### Global coin

全局 coin 可让全部 times 同时为 `0` 或采用 exact behavior。条件熵 `H(T|M_n,r)` 与 fixed worst-case state length仍正确处理这种相关性。

## 8. Lifting 边界

KLZ reconstructible sets 在 obfuscated batch endpoints 上形成 nested chain，所以概念上可定义 batch-level first-acceptance time。

但原证明只有 `b=omega(1)` 个 batch levels；粗粒度 time 可能丢失本应抵消的 `Theta(n log n)` partition/location 项。需要 block rook-polynomial inequality或递归细化 obfuscation，不能只把 actual accepted sets 替换成 reconstructible sets便宣称完成。

## 9. Go / no-go

- Acceptance forest 单独作为 lower-bound statistic：no-go。
- Acceptance time + fixed-chain layer sizes + falling-factorial ranks：no-go，因为 chain 不是免费 side information。
- 修正后的 KLZ 双向 pivot 联合 transcript：协议本身 go，但当前没有可用 extremality inequality。
- “optimizer 必为 fingerprint paintbox”：无依据，可能错误。
- 下一步：不要再从式 (1)--(2) 推导式 (5)。若继续下界，只能直接研究 state-conditioned transition transcript；同时优先探索能给出新上界的异质 fingerprint 构造。
