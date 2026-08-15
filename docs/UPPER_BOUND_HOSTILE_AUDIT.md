# \(nR_{\rm FM}+o(n)\) 动态 upper bound 的 hostile audit

> **总判定。** 在 VERIFIED_MAIN_THEOREM.md 明示的模型——多项式宇宙、容量 \(n\)、长度至多 \(n^c\)、整条合法历史在 seed 之前固定——中，没有发现破坏 \(nR_{\rm FM}(\varepsilon)+o(n)\) 构造的致命 bug。两级 finite-independence hash、fixed-slot coder、exact multiplicity update 和 sticky ALL-YES fallback 可以拼成普通 key-level filter。
>
> 但该结论必须被称为 **oblivious polynomial-horizon upper bound**，不能不加限定地写成 KLZ Definition 2.1 下对任意长或 seed-adaptive history 的 dynamic upper bound。现有 union bound 无法支持无限历史，有限独立 tail 也没有覆盖根据先前回答选择更新/查询的 adaptive history。

## 1. 审计对象与必须满足的语义

固定常数

\[
\varepsilon\in(0,1),\qquad c,d>0,
\]

以及一个在初始化随机 seed 之前确定的合法历史

\[
\mathcal H=(\mathsf{op}_1,\ldots,\mathsf{op}_T),
\qquad T\le n^c.
\]

每个 endpoint 的真实集合 \(S_t\) 因而是固定集合，而不是 hash seed 的函数。所需保证应表述为：

1. 对每个 seed，结构从不产生 false negative；
2. 对每个预先固定的 endpoint \(t\) 和 \(x\notin S_t\)，
   \[
   \Pr_{\rm seed}[\mathsf{Query}_t(x)=\mathsf{YES}]\le\varepsilon;
   \]
3. 内存是一块初始化时固定预分配的 \(H\)-bit block；
4. Insert/Delete/Query 的最坏时间为 \(\log^{O(1)}n\)；
5. sticky failure 不是额外排除的事件。进入 ALL-YES 后产生的 false positives 必须已经包含在第 2 项的概率内。

在这个语义下，下面逐项审计。

## 2. 两级 hash 是否真正实现目标 mixture

取

\[
b=2^{\lceil 2\log_2\log_2 n\rceil}=\Theta(\log^2 n).
\]

在有限域 \(F=\operatorname{GF}(2^w)\) 中嵌入 universe，其中 \(w=\Theta(\log n)\) 且常数足够大。Outer polynomial \(G\) 的 degree 小于

\[
k_{\rm out}=\Theta((c+d+1)\log n),
\]

inner polynomial \(H\) 的 degree 小于

\[
k_{\rm in}=s_{\max}=\Theta(\log^2 n).
\]

二者的 coefficients 独立均匀。

把 \(F\) 的 \(Bm\) 个值划成 \(B\) 个等大小 outer intervals，每个概率

\[
\delta=\frac{m}{|F|}
=\frac{\lambda b}{n}+o(n^{-C})
\]

for any prescribed constant \(C\)。剩余 field values 映射到 top。再把 \(H(x)\) 线性投影为 \([b]\) 上的 uniform label。于是每个 light cell 的概率是

\[
p=\frac{\delta}{b}=\frac{\lambda}{n}+o(n^{-C}),
\]

light key mass 是 \(\alpha_n=B\delta\)，而 permanent-positive mass 是 \(\beta_n=1-\alpha_n\)。通过整数选择 \(B,m,w\)，可令

\[
\alpha_n=\alpha+o(1),\qquad
Bb=\frac{\alpha n}{\lambda}+o(n).
\]

特别地，\(\alpha=1\) 时 grid 可能留下 \(o(1)\) 的 top mass；它必须算入 FPR margin，但只改变 \(o(n)\) 空间。

**判定：成立。** 该 construction 足够实现定理真正用到的两个 optimizer：

- low-error branch：\(\alpha=1\)，一个 light load；
- high-error branch：load \(\lambda_*\) 的 light cells 加一个 top category。

它没有实现任意连续 heterogeneous load law，但主定理的显式 phase geometry 并不需要。

## 3. 条件于 outer block 后 inner labels 是否严格 IID

固定 endpoint set \(S_t\)，固定 block \(j\)，并条件于 **整个 outer assignment**

\[
(g(x):x\in S_t),
\]

而不只是 block total。令

\[
A_j=\{x\in S_t:g(x)=j\},\qquad s=|A_j|.
\]

这个 conditioning 只涉及 \(G\)。由于 \(H\) 与 \(G\) 的 seeds 独立，\(A_j\) 仍是一个与 \(H\) 独立的固定 distinct-key set。若 \(s\le s_{\max}=k_{\rm in}\)，则 polynomial \(H\) 在 \(A_j\) 上的 values 是严格独立 uniform field values；surjective linear projection 保持其为严格独立 uniform \([b]\)-labels。因此

\[
C_j\mid(g(x):x\in S_t)
\sim\operatorname{Mult}(s;1/b,\ldots,1/b)
\]

是精确等式，不是 approximation。

这里有三个不可删除的前提：

1. conditioning 是 outer assignment，不能再条件于涉及 \(H\) 的事件；
2. outer 和 inner seeds 必须独立；
3. endpoint set 必须独立于 seeds。

**判定：成立。** 条件于 nonoverflowing outer block 也安全，因为事件 \(s\le s_{\max}\) 只由 outer assignment 决定。

## 4. Outer load 与所有 block-times 的 union bound

对固定 \(S_t\) 和 block \(j\)，

\[
S_{t,j}=\sum_{x\in S_t}\mathbf 1[g(x)=j]
\]

是 \(k_{\rm out}\)-wise independent Bernoulli sum，且 \(\mu_{t,j}\le n\delta=\lambda b+o(1)\)。取 \(r=\Theta((c+d+1)\log n)\) 和

\[
s_{\max}=\left\lceil\lambda b+A\sqrt{b\log n}\right\rceil.
\]

标准 \(2r\)-th centered moment expansion只涉及至多 \(2r\) 个 keys，所以与 full independence 相同。增大常数 \(A\) 后，

\[
\Pr[S_{t,j}>s_{\max}]\le n^{-K}
\]

可令 \(K>c+d+3\)。

条件于 \(S_{t,j}\le s_{\max}\)，inner multinomial law 精确，fixed-slot information-density tail 同样可做到

\[
\Pr[\text{block histogram uncodeable}\mid G]\le n^{-K}.
\]

历史中至多有

\[
(T+1)B=O(n^{c+1}/b)
\]

个 block-endpoint pairs。因此

\[
\Pr[\exists\text{ ideal endpoint with a bad block}]
\le 2B(T+1)n^{-K}
\le n^{-d}.
\tag{1}
\]

不同 blocks 或 times 之间不需要独立。

为了把 ideal endpoints 的 union bound 转为实际 implementation 的 first-failure bound，作如下 coupling：即使实际结构已失败，也在分析中继续计算每个真实 endpoint 的 ideal histogram。若此前所有 ideal endpoints 可编码，则 actual slot 与 ideal slot 相同；所以第一次 actual failure 必然对应一个 bad ideal endpoint。因而 actual failure event 包含于 (1) 中。

**判定：成立。** 现稿应补上最后这个 induction/coupling 句子，否则 endpoint tail 到动态 first failure 的连接只是隐含的。

## 5. Pointwise FPR 与 Bonferroni

固定 endpoint \(S_t\) 和固定 \(x\notin S_t\)。若 \(x\) 映射到 top，query 必然为 YES。条件于 \(x\) 落入一个指定 light cell，对每个 \(y_i\in S_t\) 定义

\[
E_i=\{y_i\text{ 落入该 light cell}\}.
\]

对任意 \(r\) 满足 \(r+1\le\min(k_{\rm out},k_{\rm in})\)，\(x\) 加任意 \(r\) 个 distinct members 的 outer values 与 inner values分别独立，所以

\[
\Pr\!\left[\bigcap_{\ell=1}^rE_{i_\ell}
\;\middle|\;
x\text{ 在指定 light cell}\right]
=p^r.
\]

取 odd

\[
R=\Theta((c+d+1)\log n/\log\log n)
\]

并令其低于两个 independence thresholds。Bonferroni 给出

\[
\Pr\!\left[\bigcup_iE_i\mid x\text{ in cell}\right]
\le
\sum_{r=1}^{R}(-1)^{r+1}\binom{|S_t|}{r}p^r.
\]

因为 \(|S_t|p=O(1)\)，tail 至多

\[
\left(\frac{e|S_t|p}{R+1}\right)^{R+1}
=n^{-\Omega(c+d+1)}.
\]

于是 normal branch 的 pointwise FPR 至多

\[
\beta_n+\alpha_n\!\left(1-(1-p)^{|S_t|}\right)
+n^{-\Omega(c+d+1)}.
\tag{2}
\]

若文中要写 differs from full independence，还应同时引用 even truncation \(R-1\)；但 upper bound (2) 已足以证明 filter theorem。

加入 sticky failure 时，不能假设 failure 与 collision 独立。安全公式是

\[
\Pr[\mathsf{FP}_t(x)]
\le
\beta_n+\alpha_n\!\left(1-(1-p)^{|S_t|}\right)
+n^{-\Omega(c+d+1)}
+\Pr[\mathsf{failure\ by\ }t].
\tag{3}
\]

按目标 error \(\varepsilon-\eta_n\) 选择 base mixture，其中例如 \(\eta_n=1/\log n\)。Grid rounding、finite-independence remainder、finite-\(n\) binomial/Poisson difference及 \(n^{-d}\) 都是 \(o(\eta_n)\)。因此充分大 \(n\) 时 (3) 不超过 \(\varepsilon\)。

**判定：成立。** Sticky failure 后 ALL-YES 不破坏 one-sidedness；其概率必须像 (3) 一样直接计入 pointwise FPR。它不是 theorem correctness 之外的 failure probability。

## 6. Fixed preallocation 与所有持久空间

每个 light block分配一个固定 \(L\)-bit slot，其中

\[
L=bH_2(\operatorname{Pois}(\lambda_n))
+O(\sqrt{b\log n}\log b).
\]

另需：

- 每 block 的 \(O(\log b)\)-bit total；
- 两个 polynomial hash seeds；
- sticky bit；
- word padding；
- 一个 reusable \(O(b\log b)\)-bit scratch area；
- fixed-slot exact rank/unrank 所需的 constant number of \(O(b\log b)\)-bit integers。

Hash seeds 共占

\[
O((k_{\rm out}+k_{\rm in})w)=O(\log^3n)
\]

bits。总 fixed allocation 是

\[
\alpha n\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda}
+O\!\left(
n\sqrt{\frac{\log n}{b}}\log b
+\frac{n\log b}{b}
+\frac{n\log n}{b}
+b\log b
+\log^3n
\right).
\]

对 \(b=\Theta(\log^2n)\)，括号内是 \(o(n)\)。

**判定：成立。** 不能把 seeds 称作免费 oracle；这里的短 seed 已经明确存入空间。即使 KLZ 的 random tape 免费，收费 seed 只会给出更强的 upper bound。

## 7. Exact counts、删除和 sticky transition

Normal state 中每个 block slot 加 total 唯一恢复整个 histogram，所以每个 light-cell multiplicity 是 exact 的。

- Insert(x)：计算 \((g(x),h(x))\)。若 top，no-op；否则 decode block，给对应 count 加一，检查 outer threshold 与 codeability，通过后才覆盖 slot。
- Delete(x)：若 top，no-op；否则 decode block，给对应 count 减一并重编码。合法-history promise 保证该 count 原先至少为一。
- Query(x)：若 top 回答 YES；否则 decode 到目标 coordinate，并检查 count 是否正。

若新 endpoint 不可编码，implementation 先设置 sticky bit，不覆盖旧 slot。此后 updates no-op，queries 全部 YES。于是即使 failure 后不再保存真实集合，所有未来 member queries 仍为 YES；ordinary filter API 并不要求失败状态能恢复集合。

**判定：成立。** 需要明确只支持合法 distinct-set histories；duplicate insert 和 delete-nonelement 不在这个 theorem 内。

## 8. Worst-case time

Polynomial evaluation分别需要 \(k_{\rm out}\) 与 \(k_{\rm in}\) 次 field operations。Block decode/re-encode 操作

\[
O(b\log b)=\log^{O(1)}n
\]

bit integers，并扫描至多 \(b=\Theta(\log^2n)\) 个 coordinates。即使使用 schoolbook multiword arithmetic，也是 \(\log^{O(1)}n\) word operations。

没有使用 amortization：每次 operation 只访问一个 block及固定 scratch area。Sticky branch 是 \(O(1)\)。

**判定：polylogarithmic worst-case 成立。** 该 coder不支持 \(O(1)\) random access，不能把结论提升为 constant time。

## 9. 真正的模型边界

### 9.1 Polynomial horizon 是实质限制

对一个无限 history，任一固定的非零 per-endpoint bad probability都无法直接 union bound。Sticky ALL-YES 一旦发生便使此后每个 nonmember query 都是假阳性。因此当前 proof 不支持：

- 任意长历史上的 uniform pointwise FPR；
- 初始化后永远工作的 Las Vegas succinct structure；
- KLZ 模型中不带 horizon qualification 的最强 upper-bound表述。

这不是 \(o(n)\) bookkeeping，而是 theorem scope。

### 9.2 Seed-adaptive history 没有被证明

如果 updates 或 queried keys 根据 earlier answers、timings或暴露的状态选择，则 endpoint set \(S_t\) 可能成为 hash seed 的函数。此时：

- outer load 不再是 fixed-set Bernoulli sum；
- \(A_j\) 不再自动独立于 inner hash；
- 对 fixed endpoint 的 union bound不能直接应用。

因此 theorem 必须保留 seed-independent/oblivious history。

### 9.3 普通 key-level 与普通 KLZ quantifiers 要分开

该 construction 的接口确实只有 Insert/Delete/Query，没有暴露 counts，因此是普通 key-level filter。但它的 workload quantifiers 比不带 horizon/adaptivity限制的完整 KLZ upper-bound语义更弱。建议避免单独写：

> resolves the KLZ constant-error dynamic upper-bound problem.

更准确的是：

> resolves the time-efficient fingerprint-multiset upper bound for polynomial-length oblivious histories.

## 10. 精确修正版 theorem

### Theorem（oblivious polynomial-horizon dynamic fingerprint upper bound）

固定常数

\[
\varepsilon\in(0,1),\qquad c,d>0,
\]

并设 universe \(U_n\) 可嵌入 \(\Theta(\log n)\)-bit words，\(\lvert U_n\rvert=n^{O(1)}\)。对充分大的 \(n\)，存在一个随机化 one-sided dynamic membership filter，满足：

1. **Workload.** 它支持容量至多 \(n\) 的合法 distinct-set Insert/Delete/Query history。对每一条在初始化 seed 之前固定、长度至多 \(n^c\) 的 history，以下保证成立。
2. **Space.** 它使用一个初始化时固定预分配的
   \[
   nR_{\rm FM}(\varepsilon)+o(n)
   \]
   bit memory block。该空间包括两个 finite-independence hash seeds、全部 fixed slots、block totals、metadata、padding、sticky bit 和 reusable scratch space。
3. **One-sidedness.** 对每个 seed、每个 endpoint 和每个当前 member，query 必然返回 YES。
4. **Pointwise error.** 对每个预先固定的 endpoint \(t\) 及每个 \(x\notin S_t\)，
   \[
   \Pr_{\rm initialization}[\mathsf{Query}_t(x)=\mathsf{YES}]
   \le\varepsilon.
   \]
5. **Failure implementation.** 正常状态精确维护所有 light-cell multiplicities。结构可以进入一个 sticky ALL-YES state；对该固定 history，历史中进入此状态的概率至多 \(n^{-d}\)。该事件已经计入第 4 项的 FPR，而不是从 correctness probability中排除。
6. **Time.** 每次 query、insert 和 delete 使用 \(\log^{O(1)}n\) 个 \(\Theta(\log n)\)-bit word operations，最坏界成立而非 amortized。

空间率中的

\[
R_{\rm FM}(\varepsilon)
=
\begin{cases}
\displaystyle
\frac{H_2(\operatorname{Pois}(-\ln(1-\varepsilon)))}
{-\ln(1-\varepsilon)},
&\varepsilon\le\varepsilon_*,\\[1.2ex]
C_*(1-\varepsilon),
&\varepsilon\ge\varepsilon_*,
\end{cases}
\]

令

\[
\varepsilon_n=\varepsilon-\eta_n,
\qquad \eta_n=\frac1{\log n}.
\]

忽略只用于 field-grid 取整的更小 \(o(\eta_n)\) 调整，空间率由如下参数达到：

- 第一支使用单一 light load
  \[
  \lambda_n=-\ln(1-\varepsilon_n)
  =-\ln(1-\varepsilon+\eta_n);
  \]
- 第二支使用 light load \(\lambda_*\) 与 permanent-positive mass
  \[
  1-\frac{1-\varepsilon_n}{1-\varepsilon_*}.
  \]

这些参数先把理想 FPR 降到 \(\varepsilon_n\)，再用 \(\eta_n\) 吸收 finite grid、Bonferroni remainder、finite-\(n\) collision error 和 sticky failure。由 \(R_{\rm FM}\) 在固定 \(\varepsilon\in(0,1)\) 处连续，

\[
nR_{\rm FM}(\varepsilon_n)
=nR_{\rm FM}(\varepsilon)+o(n).
\]

## 11. 最终 verdict

- **Finite-independence two-level hash：PASS。**
- **Conditional exact IID inner labels：PASS，前提必须完整写出。**
- **All block-times union bound：PASS，需补 ideal/actual first-failure coupling。**
- **Fixed preallocated \(nR_{\rm FM}+o(n)\) space：PASS。**
- **Exact multiplicities and deletion：PASS under legal distinct-set histories。**
- **Polylog worst-case operations：PASS。**
- **Sticky failure semantics：PASS only when its probability is included in every pointwise FPR bound。**
- **Unqualified arbitrary-history KLZ upper bound：FAIL / NOT PROVED。**

所以现有构造不是技术上崩溃，而是 theorem headline 必须降到其真正证明的 quantifiers。若目标是完整 arbitrary-length ordinary KLZ upper bound，还需要一个不会随历史累积 failure probability 的新动态 succinct representation或 rebuild/refresh机制；当前 finite-horizon typical-set coding没有提供这一点。
