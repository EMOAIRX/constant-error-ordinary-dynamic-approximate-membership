# Lovett--Porat 下界到 fresh-distinct KLZ API 的 robust repair

> 日期：2026-08-13。状态：核心 witness-conflict lemma 已证，one-cut proof 的完整渐近骨架已给出；正式稿仍需逐行展开 Claims 12--16 的 falling-factorial rounding。结论候选：当 \(|U|/n^2\to\infty\) 时，Lovett--Porat one-cut inequality 可以转移到普通 KLZ fresh-insertion API。它只是既有 LP 常数到 fresh-distinct API 的迁移，不是新的数值下界。

所有对数以 \(2\) 为底。记 \(u=|U|\)。

## 1. 目标

只使用从空集开始的 \(n\) 次 fresh, pairwise-distinct insertions。filter 可以 history-dependent、non-monotone；不使用 deletion、Section 5 或 reconstructible sets。

写

\[
H=\eta n\log(1/\varepsilon).
\]

目标是恢复 Lovett--Porat one-cut inequality：对每个固定 \(c\in(0,1)\)，

\[
\boxed{
(1/\varepsilon)^\eta\varepsilon^c
\ge
\left(
\frac{1-\varepsilon^{\eta/c}}
{\varepsilon-\varepsilon^{\eta/c}}
\right)^{(1-\varepsilon^{\eta/c})(1-c)}.
}
\tag{1}
\]

在 \(\varepsilon=1/2\) 时，这给原文正式的 \(H\ge1.1n-o(n)\)。单切数值 optimum \(1.10213\ldots\) 是可认证的精炼，但不是新社区常数。

## 2. Fresh-distinct layered graph

固定随机带 \(r\)。第 \(i\) 层 state 数至多 \(2^H\)。对 ordered distinct prefix \(w\in U^{\underline i}\)，记 endpoint 为 \(I_r(w)\)。对 state \(v\)，定义

\[
L_r(v)
=\bigcup\{\operatorname{supp}(w'):
w'\in U^{\underline i},\ I_r(w')=v\}.
\tag{2}
\]

在 repeated-label 模型中，若 \(I_r(w')=I_r(w)\)，任意 continuation \(z\) 都可拼接。fresh API 中可能有 \(z\cap w'\ne\varnothing\)，这正是旧 proof-interface gap。

## 3. Witness-conflict robust transport

固定 distinct prefix \(w\in U^{\underline k}\)，令 \(v=I_r(w)\)。对每个 \(y\in L_r(v)\)，固定一条 witness prefix

\[
w_y\in U^{\underline k},
\qquad I_r(w_y)=v,
\qquad y\in\operatorname{supp}(w_y).
\]

令 \(z\) 从 \(U\setminus\operatorname{supp}(w)\) 中均匀无放回抽取，长度 \(m=n-k\)。令 \(A_r(wz)\) 是 final accepted set。

### Lemma 3.1：deterministic inclusion

若

\[
\operatorname{supp}(z)
\cap
(\operatorname{supp}(w_y)\setminus\operatorname{supp}(w))
=\varnothing,
\]

则 \(y\in A_r(wz)\)。

证明。此时 \(w_yz\) 是合法 fresh-distinct history。由于 \(I_r(w_y)=I_r(w)\)，fixed-tape determinism 给 \(I_r(w_yz)=I_r(wz)\)。替代历史含 \(y\)，故共同 endpoint 接受 \(y\)。

### Lemma 3.2：expected loss

定义

\[
D_r(w,z)=L_r(v)\setminus A_r(wz).
\]

则

\[
\boxed{
\mathbb E_z|D_r(w,z)|
\le
|L_r(v)|\frac{m(k-1)}{u-k-m+1}
=O(n^2).
}
\tag{3}
\]

证明。对每个 \(y\)，冲突集合

\[
B_y=\operatorname{supp}(w_y)
\setminus(\operatorname{supp}(w)\cup\{y\})
\]

大小至多 \(k-1\)。若 \(y\notin A_r(wz)\)，则 \(z\cap B_y\ne\varnothing\)。无放回 union bound 后对 \(y\) 求和即得。

令

\[
a_n=n^2/u=o(1),
\qquad \xi_n=a_n^{1/3}.
\]

Markov 给 uniformly over \(r,w\)：

\[
\Pr_z[|L_r(w)\setminus A_r(wz)|>\xi_nu]
\le O(a_n^{2/3})=o(1).
\tag{4}
\]

这替代 repeated-label proof 中的 exact inclusion \(L(w)\subseteq A(wz)\)。

## 4. 固定随机带、good mass 与 Claim 8

对每条 fixed distinct history \(W\)，pointwise FPR 给

\[
\mathbb E_R|A_R(W)|
\le n+\varepsilon(u-n).
\]

交换期望后，可固定一条 \(r^*\) 使随机 distinct \(W\) 的平均 accepted-set size 不超过该值。从此固定该 tape。

令

\[
a_n=n^2/u,
\qquad
\delta_n=\max\{a_n^{1/3},n^{-1}\},
\qquad
\alpha_n=
\frac{\varepsilon+n/u}{1-3\delta_n}.
\tag{5}
\]

Markov inequality 给

\[
\Pr_W[|A(W)|\le\alpha_nu]\ge3\delta_n,
\qquad
\alpha_n=\varepsilon+o(1).
\tag{6}
\]

若第 \(k\) 层 state \(v\) 满足 \(|L(v)|\le\beta u\)，到达它的 distinct prefixes 至多

\[
(\beta u)_{\underline k}.
\]

因此，对任意 \(\beta>0\)，

\[
\Pr[|L(w)|\le\beta u]
\le
\frac{2^H(\beta u)_{\underline k}}{(u)_{\underline k}}.
\tag{7}
\]

取

\[
\beta
=\delta^{1/k}2^{-H/k}
\left(\frac{(u)_{\underline k}}{u^k}\right)^{1/k},
\tag{8}
\]

则 (7) 至多 \(\delta\)。取 \(\delta=\delta_n\)。若 \(k=cn\) 且 \(u/n^2\to\infty\)，则

\[
\beta=\varepsilon^{\eta/c}(1-o(1)).
\tag{9}
\]

## 5. Hypergeometric continuation

固定 prefix \(w\)，令 \(|L(w)|=\beta'u\)。因为 actual prefix keys 属于 \(L(w)\)，fresh continuation 与 \(L(w)\) 的交数服从 hypergeometric law，均值

\[
m\frac{|L(w)|-k}{u-k}=m(\beta'+o(1)).
\tag{10}
\]

无放回 Hoeffding bound 替代原 proof 的 iid Chernoff。令

\[
\gamma_n=
\sqrt{\frac{3\ln(2/\delta_n)}m}=o(1).
\]

对每个 fixed prefix，intersection count 偏离 (10) 的均值超过 \(\gamma_nm\) 的概率至多 \(\delta_n\)。由 (4)，robust inclusion 失败概率为

\[
O(a_n^{2/3})=o(\delta_n).
\]

因此 accepted-size、large-\(L\)、hypergeometric concentration 和 robust inclusion 四个 events 同时成立的 full distinct sequences 集合 \(\mathcal W\) 满足

\[
\boxed{
\frac{|\mathcal W|}{(u)_{\underline n}}
\ge\delta_n-o(\delta_n).
}
\tag{11}

## 6. Claims 12--16 的可审计 robust covering count

对 prefix \(w\in U^{\underline k}\)，定义

\[
\mathcal W(w)
=\{z\in(U\setminus\operatorname{supp}(w))^{\underline m}:wz\in\mathcal W\},
\]

\[
\delta'(w)
=\frac{|\mathcal W(w)|}{(u-k)_{\underline m}},
\qquad
\mathcal N(w)=\{A(wz):z\in\mathcal W(w)\}.
\tag{12}
\]

由 (11)，

\[
\mathbb E_{w\in U^{\underline k}}\delta'(w)
\ge\delta_n-o(\delta_n).
\tag{13}

对 good prefix \(w\) 与 final accepted set \(A=A(wz)\)，由

\[
|A|\le\alpha u,
\qquad
|L(w)\setminus A|\le\xi_nu
\]

得

\[
|A\setminus L(w)|
\le(\alpha-\beta'+\xi_n)u.
\tag{14}
\]

令 \(|L(w)|=\beta'u\)。good continuation 的 intersection count \(j\) 落在

\[
J_w=
\left[
m\frac{\beta'u-k}{u-k}-\gamma_nm,
m\frac{\beta'u-k}{u-k}+\gamma_nm
\right]\cap\mathbb Z.
\tag{15}
\]

若 continuation 有 \(j\in J_w\) 个 keys 落在 \(L(w)\)，产生同一 \(A\) 的 distinct continuations 至多

\[
\binom mj
 (\beta'u-k)_{\underline j}
((\alpha-\beta'+\xi_n)u)_{\underline{m-j}}.
\tag{10}
\]

因此对任意 \(A\in\mathcal N(w)\)，其 preimage 至多

\[
K_w=
\sum_{j\in J_w}
\binom mj
(\beta'u-k)_{\underline j}
((\alpha_n-\beta'+\xi_n)u)_{\underline{m-j}}.
\tag{16}
\]

这里不需要假设 \(X\mid A\) 均匀；(16) 是逐个 endpoint accepted set 的确定性计数上界。由 \(|\mathcal W(w)|=\delta'(w)(u-k)_{\underline m}\)，

\[
\boxed{
|\mathcal N(w)|
\ge
\frac{\delta'(w)(u-k)_{\underline m}}{K_w}.
}
\tag{17}
\]

对固定 \(c\)、所有 \(j\le m\)，条件 \(u/n^2\to\infty\) 给 uniformly

\[
\log (xu)_{\underline j}
=j\log(xu)+o(n)
\]

只要相关 \(x\) 离零的距离为常数；靠近边界时可先保留 (17)，再取紧子区间极限。对 \(j/m=\beta'+o(1)\)，Stirling 公式给

\[
\log\binom mj
=m h_2(\beta')+o(n).
\]

代入 (16)--(17)，并使用

\[
-h_2(\beta')-\beta'\log\beta'
=(1-\beta')\log(1-\beta'),
\]

得到

\[
|\mathcal N(w)|
\ge
2^{-o(n)}\delta'(w)
\left(
\frac{1-\beta'+o(1)}
{\alpha_n-\beta'+\xi_n+o(1)}
\right)^{(1-\beta'+o(1))m}.
\tag{18}
\]

函数

\[
x\longmapsto
\left(\frac{1-x}{a-x}\right)^{1-x}
\]

在 \(0\le x<a<1\) 上单调递增。good prefixes 满足 \(\beta'\ge\beta\)，故 (18) 可统一放松为

\[
|\mathcal N(w)|
\ge
2^{-o(n)}\delta'(w)
\left(
\frac{1-\beta+o(1)}
{\alpha_n-\beta+\xi_n+o(1)}
\right)^{(1-\beta+o(1))m}.
\tag{19}
\]

定义 pair family

\[
\mathcal X=\{(w,A(wz)):wz\in\mathcal W\}.
\]

由 (13) 与 (19)，

\[
|\mathcal X|
=\sum_w|\mathcal N(w)|
\ge
(u)_{\underline k}
(\delta_n-o(\delta_n))2^{-o(n)}
\left(
\frac{1-\beta+o(1)}
{\alpha_n-\beta+\xi_n+o(1)}
\right)^{(1-\beta+o(1))m}.
\tag{20}
\]

另一方面，每个 final physical state 决定一个 accepted set \(A\)，且 \(|A|\le\alpha_nu\)。每个这样的 \(A\) 含 actual prefix，compatible ordered distinct prefixes 至多

\[
(|A|)_{\underline k}\le(\alpha_nu)_{\underline k}.
\]

final states 至多 \(2^H\)，所以

\[
|\mathcal X|
\le2^H(\alpha_nu)_{\underline k}.
\tag{21}
\]

比较 (20)--(21)，吸收

\[
\log\frac{(u)_{\underline k}}{(\alpha_nu)_{\underline k}}
=-k\log\alpha_n+o(n)
\]

以及 \(\log(1/\delta_n)=o(n)\)，得到

\[
2^H\alpha^k
\ge
2^{-o(n)}
\left(
\frac{1-\beta}{\alpha-\beta}
\right)^{(1-\beta)(n-k)}.
\tag{22}
\]

令 \(\alpha\to\varepsilon\)、\(\beta\to\varepsilon^{\eta/c}\)，即得 (1)。

## 7. Hostile audit

- exact dictionary：robust loss 为零；下界很松但正确。
- fingerprint count vector：witness collision 是 universe-key 冲突，不是 hash collision；Lemma 3.1 仍成立。所得 \(1.1n\) 远低于合法 count-vector upper bound。
- frozen mask / ALL-YES coin：proof 只固定一次随机带，并用 final accepted-set covering，不按时间独立收费。
- ghosts：证明不用 deletion。
- history dependence：只使用“同一 physical state 后执行同一 concrete continuation得到同一 endpoint”。

## 8. Recursion audit

任意固定深度 \(d\) 的 repeated-label recursive proof 一旦被严格写出，就能转移到 fresh API：每个节点的 witness loss 和 factorial correction 均为 \(O(n^2/u)\)，固定 \(O_d(1)\) 个节点仍为 \(o(1)\)。若深度随 \(n\) 增长，至少需要 \(d(n)n^2/u=o(1)\)。

但 LP Section 3.5 没有给出完整 recurrence。它只建议把 Claim 8 中的

\[
\beta=\delta^{1/k}2^{-M/k}
\]

换成

\[
\beta=\delta^{1/k}2^{-M_D(k,\varepsilon)/k}.
\]

这里存在必须补出的量词：Claim 8 使用 layer-state 数的上界 \(2^M\)，而 \(M_D(k,\varepsilon)\) 是最小 memory 的下界参数。需要一个 nested case split 或 induced-subgraph lemma 才能合法替换。机械 scalar iteration 会给出超过已知 upper bound 的荒谬常数，说明不能当作 Bellman recurrence。

精确剩余 lemma 是：给定 nested cuts \(k_d<\cdots<k_1<n\)，建立 finite-\(n\) multi-layer covering inequality，明确每层 state-family cardinality、good mass 和共享 final accepted-set budget，且不能重复使用同一个 \(H\)-bit state budget。

因此目前可认证的是 fresh-distinct one-cut \(1.1\)（或数值认证 \(1.10213\ldots\)），不是 \(>1.13\)，也不接近 \(\varepsilon=1/2\) 的 \(2.200611\ldots\) fingerprint upper rate。这个数值没有超越 Lovett--Porat；新内容仅是 API 迁移。
