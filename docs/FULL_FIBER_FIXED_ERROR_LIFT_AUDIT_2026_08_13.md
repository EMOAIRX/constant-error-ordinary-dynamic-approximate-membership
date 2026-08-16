# Full-fiber fixed-error lifting：逐项审计与修正版

> 日期：2026-08-13。结论：full-fiber union 确实绕开了 KLZ Section 5 的
> partition-dependence；在 `u/n^2 -> infinity`、`f(n)/n -> infinity` 下，
> transport、obfuscation coupling 和 fixed-error communication calculation 可以
> 闭合。原候选稿有两处必须修正：统一 slack 需要控制 `b D_n`，式 (25) 中多写的
> `delta log e` 必须删除。修正后得到 ordinary non-monotone filter 的
> `1.199273234447... n` 下界，但不是常数误差最优率。

所有对数以 2 为底。令 `u=|U|`，误差为固定
`0 < delta <= 1/2`，KLZ 参数为

\[
m=n/b,\qquad V=u/b,\qquad M=4^b,
\qquad N=(1-\delta)n+\delta u.
\tag{1}
\]

## 1. 修正后的定理

### Theorem 1

设

\[
u/n^2\longrightarrow\infty,
\qquad f(n)/n\longrightarrow\infty.
\tag{2}
\]

任意使用固定 `H` bit persistent memory、免费只读随机带、支持至多 `f(n)` 次
合法 key-only `Insert/Delete/Query` 的 one-sided dynamic filter，若对每条固定
合法 history 和每个固定当前 nonmember 的 pointwise FPR 至多 `delta`，则

\[
\boxed{
H\ge n\left[
\log\frac1\delta+(1-\delta)\log e-2h_2(\delta)
\right]-o(n).
}
\tag{3}
\]

该结论允许完整 history dependence、non-monotone accepted sets、ghosts、global
certificates 和任意跨时间相关性。

对误差 `1/2` 的 filter 取 `k` 个独立副本并以 AND 回答，得到

\[
H\ge n\max_{k\ge1}
\frac{B(2^{-k})}{k}-o(n),
\quad
B(\delta)=\log\frac1\delta+(1-\delta)\log e-2h_2(\delta).
\tag{4}
\]

离散最大值在 `k=5` 达到：

\[
\boxed{H\ge1.1992732344471508\ldots n-o(n).}
\tag{5}
\]

## 2. Partition-free full fiber

固定 filter tape `R`。对物理状态 `m`、逻辑 load `t` 和已经执行的操作数 `q`，
定义

\[
W_R(m,t,q)=\bigcup\{S(h): |h|=q,\ |S(h)|=t,\ M_R(h)=m\},
\tag{6}
\]

其中 union 只遍历从空集出发、长度恰为 `q` 的合法 histories。时间坐标不可
删除；它保证替代 witness history 拼接 suffix 后仍在承诺 horizon 内。

对任意固定合法 history `h`，令 `(m,t,q)` 为其 endpoint data，则

\[
S(h)\subseteq W_R(m,t,q)\subseteq A_R(m).
\tag{7}
\]

第二个 inclusion 只用 zero false negatives：`x in W` 意味着同一 memory
representation 也可代表一个包含 `x` 的逻辑世界。因此

\[
\mathbb E_R|W_R(M_R(h),t,q)|
\le t+\delta(u-t)\le N.
\tag{8}
\]

关键点是：给定 `(R,m,t,q)` 后，`W_R(m,t,q)` 完全不引用 KLZ public
partition。它因此不会继承 conforming-history reconstructible set 的
partition leakage。

## 3. Common-suffix transport

令 `tau` 是 self-contained suffix，`I(tau)` 是其中出现过的 insertion labels。
若 `T_x` 是 `x in W_R(M_R(h),t,q)` 的一个 fixed witness endpoint，并且

\[
T_x\cap I(\tau)=\varnothing,
\tag{9}
\]

则 `h_x tau` 合法，并且固定 tape 后与 `h tau` 到达相同物理状态。因此 `x`
仍属于 successor full fiber。

这里没有偷偷要求 suffix 对整个 fiber 合法。所有不合法 witness 都明确由事件
`T_x cap I(tau) != emptyset` 支付。

这里的条件场必须只包含 cut 前信息，不能包含完整预采样 public labels。正式地，令

\[
\mathscr F_\ell
=\sigma(R,\pi,\text{tree shape},
\text{在 }\sigma_{G_\ell}\text{ 中已经执行的 labels/operations},
X_1,\ldots,X_\ell).
\tag{9a}
\]

它显式排除 rightmost `X_j`（`j>ell`）和尚未遍历的 subtree-edge labels。给定
`mathscr F_ell` 后，prefix state、load、exact time 和 full fiber 都固定。对每个
`x in W(G_ell)`，按一个与 KLZ source tree 无关的固定全序选择第一条 witness history；
于是 `T_x` 是 `mathscr F_ell`-measurable，不读取 future suffix labels。

KLZ 的 relevant `G_ell -> F_r` excursion 完全位于 cut 后尚未遍历的 rightmost
subtree。未来 level-`j` edge labels 在 `U_j` 中独立抽取，每个 edge 内是无放回的
ordered tuple；rightmost future batches 同样独立。即使完整 public tree 对通信双方
可见，概率证明也无需对尚未执行的 labels 条件化。若 suffix 有至多 `Q` 个 insertion
positions，则逐位置条件化给出有限形式

\[
\Pr[T_x\cap I(\tau)\ne\varnothing]
\le \frac{tQ}{V-m+1}
\le \frac{tbQ}{u-n}.
\tag{10}
\]

对至多 `u` 个 union elements 求和，得到

\[
\mathbb E|W(h)\setminus W(h\tau)|
\le \frac{utbQ}{u-n}
\le \frac{unbQ}{u-n}.
\tag{11}
\]

原候选稿把右侧简写成 `nbQ`。在 `u/n -> infinity` 下二者相差 `1+o(1)`；
正式证明应保留 (11)。这个估计不需要对 tape-conditioned state 使用 FPR。

## 4. 参数与 corrected profile

整棵 tree 和任一 relevant suffix 可粗略统一界为

\[
Q_{\max}\le nM^{b+1}/b.
\tag{12}
\]

定义

\[
D_n:=\frac{unbQ_{\max}}{u-n}
=\frac{u}{u-n}n^2M^{b+1}.
\tag{13}
\]

必须选择 `b=b(n)->infinity` 足够慢，使

\[
Q_{\max}=o(f(n)),
\qquad
bD_n=o(\delta u/4^b).
\tag{14}
\]

第二项是原候选稿需要加强的地方：profile 最高累计 `b` 次 transport loss，故
只写 `D_n=o(delta u/4^b)` 不够。条件 (2) 保证可以选择这样的 `b`；一个充分
条件是

\[
b4^{b(b+2)}=o(u/n^2),
\qquad
4^{b(b+1)}/b=o(f(n)/n).
\tag{15}
\]

令

\[
g_k=\mathbb E|W(G_k,km,q_{G_k})|,
\quad
\widehat g_k=g_k+kD_n,
\quad
\widehat N=N+bD_n.
\tag{16}
\]

由 (11)，`g_k >= g_{k-1}-D_n`。所以

\[
a_k=(\widehat g_k-\widehat g_{k-1})/\widehat N\ge0,
\qquad
\sum_{k=1}^b a_k\le1.
\tag{17}
\]

注意 `g_0` 无需作为 `a_0` 加入：式 (17) 的总质量是
`(g_b-g_0+bD_n)/widehat N <= 1`，而 KLZ pivot lemma 只使用 `a_1,...,a_b`
非负且总和至多一。

## 5. Obfuscation coupling 仍成立

KLZ Claim 4.7 实际证明的是 operational histories 的分布恒等式：条件于
rightmost node 的 child count 分别为 `i` 和 `i+1`，`sigma_{F_k}` 与
`sigma_{G_k}` 同分布。这个等式包括 sequence length，所以可对 functional

\[
\sigma\mapsto |W_R(M_R(\sigma),km,|\sigma|)|
\]

直接使用。结合 (8)，得到

\[
\mathbb E|W(F_k)|\le g_k+N/M.
\tag{18}
\]

对任意 `ell<r`，common-suffix transport 再给

\[
\begin{aligned}
\mathbb E|W(F_r)\setminus W(G_\ell)|
&\le g_r-g_\ell+N/M+D_n\\
&\le \widehat N a_{(\ell,r]}+N/M.
\end{aligned}
\tag{19}
\]

最后一步利用 `r-ell>=1`，所以 `widehat N a_(ell,r]` 中已经含至少一个
`D_n`。无需再在 (19) 末尾重复加 `D_n`。

## 6. Removing `U_k` 现在是合法的

条件于完整 obfuscation sequence `sigma` 和 filter tape `R`，状态、load、time
都固定，故

\[
D^*=W(F_r)\setminus W(G_\ell)
\tag{20}
\]

是一个 partition-independent fixed set。若 transcript 暴露 `L` 个 labels，
其中 `L_k` 个属于 `U_k`，则标准超几何条件化给

\[
\mathbb E[|D^*\cap U_k|\mid\sigma,R]
\le L_k+\frac{V-L_k}{u-L}|D^*|.
\tag{21}
\]

这正是原 Section 5 reconstructible set 缺失的 measurability 条件。将 (19)、
`L<=nM^{b+1}/b` 与 (14) 代入，得到

\[
\mathbb E|D^*\cap U_k|
\le \frac{\delta u}{b}(1+o(1))
\left(a_{(\ell,r]}+O(4^{-b})\right).
\tag{22}
\]

Decoder 也合法：true batch keys 属于 `W(F_r)`；Bob 由物理状态、tape、load、
time 和无限计算可枚举两个 full fibers。hit event 使用 `x in W(G_ell)`，由
`W(G_ell) subseteq A(G_ell)` 及 pointwise FPR 有无条件概率至多 `delta`。

## 7. Fixed-error 熵的正确会计

对一个 key，记 `Z=1[x in W(G_ell)]`，`p=Pr[Z=1]<=delta`。逐 key code 的
严格上界与 KLZ 式 (16) 相同：

\[
h_2(p)+p\log V+(1-p)
\log\frac{\mathbb E|D^*\cap U_k|}{1-p}.
\tag{23}
\]

对 `0<delta<=1/2`，与原 Claim 3.3 相同的单调性允许代入 `p=delta`。使用
(22)，每个 batch 的成本为

\[
\frac nb\left[
\log V+\log\delta+2h_2(\delta)
+(1-\delta)\log(a_{(\ell,r]}+O(4^{-b}))
\right]+o(n/b).
\tag{24}
\]

恒等式是

\[
\delta\log V+(1-\delta)
\log\frac{\delta V}{1-\delta}
=\log V+\log\delta+h_2(\delta).
\tag{25}
\]

再加发送 hit bit 的一个 `h_2(delta)`，便得到 (24)。原候选稿式 (25) 中的
`delta log e` 没有来源，而且与其下一式不一致，必须删除。

KLZ Lemmas 3.4 和 4.8 对 (17) 给出某个 pivot `s` 使

\[
\sum_{k=1}^b
\log(a_{(\ell_k,r_k]}+O(4^{-b}))
\le-b\log e+o(b).
\tag{26}
\]

另一方面

\[
b\log(V)_{\underline m}=n\log V-o(n)
\tag{27}
\]

在 `u/n^2 -> infinity` 下成立。用 source entropy (27) 减去 state `H` 和
(24) 的总通信，正好得到 (3)。没有额外的 `delta log e`；factorial/pivot saving
只有 miss mass `1-delta` 能使用，所以是 `(1-delta) log e`。

## 8. Hostile checks

1. **Exact dictionary.** Full fiber 等于当前 set，不产生虚假 transport loss；
   定理常数远低于 exact-set rate。
2. **Frozen mask / ALL-YES coin.** FPR 只在原联合实验中使用；证明不要求 hit
   bits 独立，也不条件于 tape 调用 FPR。
3. **Rare witnesses.** 每个 union key 可选独立 witness；(11) 按 union mass
   收费，因此不会漏掉 degree-one witnesses。代价是需要 `u >> n^2`。
4. **History dependence.** Coupling 收费的是同一个 history functional 的分布，
   不把 `F_k` 与 `G_k` 当成相同 state。
5. **Known upper bounds.** `1.199273n` 远低于 `2.349083n` everlasting quotient
   upper bound 和 `2.384500n` exact count-vector baseline，无数值矛盾。

## 9. 贡献边界

这个定理若按上述 finite-population 细节正式写完，贡献是：

- 给 ordinary history-dependent、non-monotone filters 一个新的显式 fixed-error
  下界；
- 用 partition-free full fiber 修复 KLZ Section 5 接口，而不是继续对
  partition-dependent reconstructible set 做不合法的 Claim 4.6 lifting；
- 把普通模型中的已证 half-error 常数提高到 `1.199273...`。

但它没有证明 fingerprint optimality，也没有接近 `2.2--2.35` 的上界区间。
数值提升本身不足以称为 SODA 级 sharp result。更高价值的后续必须至少完成其一：

1. 用 fiber thickness/core profile 把 transport 条件从 `u >> n^2` 降到 KLZ 的
   `u >> n`；
2. 把逐 key code (23) 换成真正的 transition-constrained batch code，显著提高
   fixed-error coefficient；
3. 证明 full-fiber transport inequality 的 extremal structure，并给接近
   everlasting quotient upper bound 的 converse。
