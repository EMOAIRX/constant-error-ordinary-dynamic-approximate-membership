# Arbitrary filter 的 same-tape deletion fiber 定理：证明与极值障碍

> 日期：2026-08-13。状态：pathwise transport 与 unconditional first-moment bound
> 严格成立；从该 first moment 经 Jensen/Hölder 推导强 state lower bound 的步骤
> 不成立。本文完全不假设 local/hash/canonical/history independence。

## 1. 模型

Universe (U) 大小为 (u)。filter 容量为 (n)，固定 (H)-bit persistent
memory，可读取免费随机 tape (r)。支持 key-only updates、zero false negatives，
并对每条预先固定的合法 history和每个固定当前 nonmember (x) 满足

\[
\Pr_r[Q_r(M_r(h),x)=\mathrm{YES}]\le\varepsilon.
\tag{1}
\]

filter 可完整 history-dependent。下面固定一个与 tape 无关的 canonical insertion
order，例如按 universe 的固定全序插入集合元素。它只是选择每个集合的一条合法
history，不假设 filter state canonical。

固定 tape (r)。令

\[
\mathcal F_r(m)
=\{T\in{U\choose n}:\text{canonical insertion history of }T
\text{ reaches }m\}.
\tag{2}
\]

取 (d\le n)，写 (k=n-d)。对每个 (D\in{U\choose d})，固定按 universe
全序执行 deletes，记最终 state 为

\[
m_{r,D}=\Delta_r^{\operatorname{Delete}(D)}(m).
\]

只对 (D\subseteq T) 的 hidden worlds，该 continuation 合法。

## 2. Pathwise accepted-union theorem

定义

\[
W_r(m,D)
=\bigcup_{\substack{T\in\mathcal F_r(m)\\D\subseteq T}}(T\setminus D),
\tag{3}
\]

并令

\[
a_{r,m,D}
=|\{T\in\mathcal F_r(m):D\subseteq T\}|.
\tag{4}
\]

### Theorem 2.1

对每个固定 ((r,m,D))，

\[
\boxed{
W_r(m,D)\subseteq A_r(m_{r,D}),
}
\tag{5}

其中 (A_r(q)) 是 state (q) 的 accepted-key set。而且

\[
\boxed{
a_{r,m,D}\le {|W_r(m,D)|\choose k}.
}
\tag{6}

**证明。** 对式 (3) 中每个 witness (T)，canonical insertion 到达同一 state
(m)。因为 (D\subseteq T)，同一列 fixed-order deletions 对该 hidden world
合法；固定 tape 后 transitions deterministic，所以全部 witnesses 到达同一
(m_{r,D})。每个 (x\in T\setminus D) 是该 endpoint 的成员，zero false
negatives 强迫 (x\in A_r(m_{r,D}))。取 union 得式 (5)。

每个包含 (D) 的 (T) 对应一个不同的 (k)-set (T\setminus D\subseteq W)，
故 witnesses 数至多 (W) 的 (k)-subsets 数，得到式 (6)。证毕。

这部分完全是 same-tape indistinguishability，不比较不同 tapes，也不需要
canonical state semantics。

## 3. Pointwise FPR 能合法推出什么

先固定一个 (n)-set (T)，再独立均匀选择 (D\in{T\choose d})，执行

\[
h_{T,D}=\operatorname{InsertCanonical}(T);\operatorname{DeleteOrdered}(D).
\]

对每个固定 pair ((T,D)) 与每个固定 (x\notin T\setminus D)，式 (1) 合法
适用。因此

\[
\mathbb E_r|A_r(M_r(h_{T,D}))|
\le k+\varepsilon(u-k).
\tag{7}
\]

由式 (5)，真实 endpoint 所属的 (W_r(M_r(T),D)) 被该 accepted set 包含。
所以再平均 (T,D) 得

\[
\boxed{
\mathbb E_{T,D,r}|W_r(M_r(T),D)|
\le k+\varepsilon(u-k).
}
\tag{8}

注意式 (8) 是 unconditional expectation，其中抽样方式是先 uniform (T)，再
uniform (D\subseteq T)。不能声称对每个 conditioned ((r,m,D)) 都有同样
上界；state 和 fiber 本身依赖 tape。

用 pair weights 写，式 (8) 等价于

\[
\frac{1}{{u\choose n}{n\choose d}}
\sum_{r}\Pr[r]
\sum_{m,D}a_{r,m,D}|W_r(m,D)|
\le k+\varepsilon(u-k),
\tag{9}

因为 triple ((T,D,r)) 落到 cell ((r,M_r(T),D)) 的 multiplicity 正是 (a)。

## 4. State counting identity

对每个 tape，fibers partition all (n)-sets，所以

\[
\boxed{
\sum_{m,D}a_{r,m,D}
={u\choose n}{n\choose d}
={u\choose d}{u-d\choose k}.
}
\tag{10}

非空 cells 数至多

\[
2^H{u\choose d}.
\tag{11}

若能从式 (6)、(9) 控制高阶 moment，式 (10)--(11) 看似可能给 (H) 下界。
真正障碍就在这里。

## 5. Jensen/Hölder 推导为何失败

式 (6) 的右侧

\[
f(w)={w\choose k}
\]

对 (w\ge k) 是增长很快的凸函数。式 (9) 只控制 (a)-size-biased 的 first
moment (E_a[W])，却需要 upper-bound (E_a[{W\choose k}]) 或最大 cell size。
Jensen 给出的方向是

\[
\mathbb E_a{W\choose k}
\ge {\mathbb E_aW\choose k},
\]

与所需方向相反。Hölder 也不能从 first moment upper-bound (k)-th moment；
它只会给 lower bounds，除非另有 tail 或 higher-moment 控制。

一个极端分布已经说明障碍。令

\[
W=
\begin{cases}
k,&\text{概率 }1-\varepsilon,\\
u,&\text{概率 }\varepsilon.
\end{cases}
\tag{12}

则

\[
\mathbb EW=k+\varepsilon(u-k)
\]

恰好满足式 (8)，但

\[
\mathbb E{W\choose k}
=(1-\varepsilon)+\varepsilon{u\choose k}
\]

由 rare (W=u) cells 主导。特别地，(arepsilon=1/2) 时它允许一半 mass 位于
ALL-YES fibers。这个分布正对应 frozen-mask/shared-certificate 压力测试，不是
纯数值伪影。

因此，仅由式 (6)、(8)--(11) 不能推出强于 trivial state bound 的一般结论。

## 6. First moment 能推出的最强通用 tail 形式

Markov 对 size-biased cell distribution 给：对任意
(L>k+\varepsilon(u-k))，

\[
\Pr_a[W>L]
\le\frac{k+\varepsilon(u-k)-k}{L-k}
=\frac{\varepsilon(u-k)}{L-k}.
\tag{13}

所以至少

\[
1-\frac{\varepsilon(u-k)}{L-k}
\]

的 pair mass 位于 (W\le L) cells。每个这样的 cell 有

\[
a\le{L\choose k}.
\]

结合 cell count 给出 family：

\[
\boxed{
2^H
\ge
\left(1-\frac{\varepsilon(u-k)}{L-k}ight)
\frac{{u-d\choose k}}{{L\choose k}},
\qquad
L>k+\varepsilon(u-k).
}
\tag{14}

对 (L) 优化是这组 first-moment premises 能给出的直接 state lower bound。

但在大宇宙 (u\gg n)、(k=\Theta(n))、固定 (arepsilon) 下，合法 (L)
必须至少约为 (arepsilon u)。式 (14) 的主项至多恢复

\[
k\log_2(1/\varepsilon)-O(k)-O(\log n),
\tag{15}

即 Carter/static 量级；选择删除 (d>0) 还把系数从 (n) 降到 (k=n-d)。
它不能产生动态的额外线性常数，更不可能仅靠调整 (d) 越过最佳 static bound。

## 7. 如何真正加强

需要 pointwise FPR 对多个预先固定 deletion continuations 的联合控制，从而获得

\[
\mathbb E_a\left(\frac Wu\right)^j
\]

的 higher-moment upper bounds，或直接控制 fiber core/shadows。单次 deletion
实验只给 (j=1)。对多个 query keys 取 AND 不能免费得到同 tape 的 joint moment；
pointwise marginals允许完全相关的 frozen mask。

另一条可能路线是使用同一个 large fiber 的许多不同 (D)，通过 Kruskal--Katona/
LYM 证明 rare huge-(W) cells 必同时污染大量预先固定 histories，而不能把所有
污染集中在 (arepsilon) tapes。但这需要新的跨-(D)、跨-tape incidence lemma，
不包含在当前定理中。

## 8. 审计结论

严格成立：

1. (W_r(m,D)\subseteq A_r(m_{r,D}))；
2. (a_{r,m,D}\le{|W_r(m,D)|\choose k})；
3. 在 uniform ((T,D)) 抽样下，unconditional size-biased first moment 满足式 (8)--(9)；
4. Markov truncation 给出式 (14)。

不成立：

1. 条件于 tape/state/fiber 后重新调用 pointwise FPR；
2. 用 Jensen 从 (E[W]) upper-bound (E[{W\choose k}])；
3. 由单个 first moment 推出强动态 state lower bound。

最终判断：same-tape theorem 本身正确而且一般，但其自然 Jensen/Hölder closure
失败。当前最强无额外假设推论仍不超过 static/Carter 量级。
