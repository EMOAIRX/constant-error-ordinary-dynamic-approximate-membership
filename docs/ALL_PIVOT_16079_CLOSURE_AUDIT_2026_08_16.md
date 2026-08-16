# $1.6079$ all-pivot lower bound：lifting closure audit

日期：2026-08-16。所有对数以 $2$ 为底。

## 结论

考虑 half-error ordinary dynamic approximate membership：zero false negatives、
pointwise false-positive probability 至多 $1/2$、arbitrary history dependence、
nonmonotone queries、固定最坏 $H$-bit persistent memory 和免费公共随机带。

若

$$
\frac{u}{n^2}\to\infty,
\qquad
\frac{f(n)}n\to\infty,
$$

并且数据结构对所有长度至多确定函数 $f(n)$ 的合法 histories 满足保证，则

$$
\boxed{H\ge1.6079n-o(n).}
$$

这里没有 BSSI、monotonicity、history independence、canonical state 或 locality
假设。该结论不覆盖只有 $u/n\to\infty$ 的自然宇宙 regime。

## 旧 hostile audit 的断点如何修复

旧审计指出：不能在同一个条件场中既固定完整 public partition，又把未暴露 keys 的
partition assignments 当作随机量。后续 lemma 使用两个嵌套条件场。

第一阶段条件于 $\mathcal P^-_{\ell,k}$。它固定 filter tape、tree shape、生成
$G_\ell$ 的 concrete prefix 和所有已暴露 label-level 关系，但不固定完整 partition，
也不包含 hidden batch $X_k$。partition-free full fiber $W(G_\ell)$ 此时是固定集合，
而 compatible balanced partition completions 仍均匀，因此可以合法估计
$W(G_\ell)\cap U_k$ 的 first moment。

第二阶段加入完整 partition：

$$
\mathcal P^+_{\ell,k}
=
\mathcal P^-_{\ell,k}\vee\sigma(\pi).
$$

此时 $G=W(G_\ell)\cap U_k$ 固定，而 $X_k$ 仍是 $U_k$ 中均匀无放回的 ordered
batch。这正是 batch-perspective lemma 所需的 hypergeometric 条件。两个阶段分别
证明条件估计，再取全期望；没有同时固定和平均 partition。

## Decoder 与 exact batch code

在每个 KLZ `Send` step，Bob 已知对应的 physical states $F_r,G_\ell$、公共 tape、
partition、load 和 exact time。无限计算允许他枚举两个 full fibers，因此他知道

$$
G=W(G_\ell)\cap U_k,
\qquad
D=(W(F_r)\setminus W(G_\ell))\cap U_k.
$$

$D$ 可以依赖 hidden batch $X_k$。编码先对 hit pattern 和 hit values 使用不依赖 $D$
的条件 code，再把 $Q$ 个 misses 排名为 $D$ 中的 ordered distinct tuple。期望长度为

$$
\log(V)_{\underline m}
+
\mathbb E\log
\frac{(|D|)_{\underline Q}}
     {(V-|G|)_{\underline Q}}
+O(1).
$$

因此 code 只要求 $Q$ 在给定 $G$ 后具有 hypergeometric 分布，不要求 $D$ 与 $X_k$
独立。

## Uniform transport 与 finite-$b$ 参数

common self-contained suffix 只会在 witness endpoint 已含 future insertion label 时破坏
full-fiber membership。对所有 relevant suffixes 统一取 transport debit $D_n$，并选择
缓慢增长且可被 $10$ 整除的 $b=b(n)$，可使

$$
bD_n=o\!\left(\frac{u}{4^b}\right).
$$

这里使用 KLZ relevant $G_\ell\to F_r$ excursions 的 deferred-edge 性质：suffix 中
每个 insertion edge 在 cut 后才被遍历，其 label 在 cut-prefix 条件场下尚未暴露。
对每个 $x$，witness endpoint 可按固定全序由 $(R,m,t,q,x)$ 确定，所以它只依赖
prefix；随后才对 suffix labels 做无放回平均。证明不在固定 future labels 后重复声称
独立性。

$u/n^2\to\infty$ 支付 witness-collision loss，$f(n)/n\to\infty$ 保证整棵有限深度
KLZ tree、替代 witness histories 和 common suffixes 都位于保证 horizon 内。rounding
$m=n/b$、$V=u/b$ 及 prefix-free framing 的总损失均为 $o(n)$。

Claim 4.7 可用于带 exact-time 坐标的 operational-history functional。结合 common-suffix
transport 和两阶段 partition removal，对所有 $\ell<k\le r$ 一致得到 prefix 与
difference first moments。于是每个 pivot $s$ 都满足

$$
\frac Hn\ge F_{b,s}(x)-o(1).
$$

不同 pivots 是使用同一个 $H$-bit state 的替代解码协议；证明取
$\max_sF_{b,s}(x)$，并未把多个协议的 mutual information 相加，所以不存在
multi-parent parity 型重复收费。

## Convex certificate

端点放松 $x_0\downarrow0$、$x_b\uparrow1$ 对 regularized pivot functional 的方向
正确。固定十个 macro-block 后，Jensen reduction 给出凸 minimax 常数 $C_{10}$。
纯有理 verifier 认证

$$
C_{10}
\ge
\frac{803993501430859}{500000000000000}
=
1.607987002861718\ldots
>
1.6079.
$$

验证器：

- `scripts/verify_ten_block_160_certificate.py`
- `scripts/verify_ten_block_pivot_160_dual.py`

## 仍然开放的问题

该证明的 hard-union transport 在 witness collisions 上支付约 $n^2$ scale，因此不能
直接降到 $u/n\to\infty$。已有 avalanche、posterior-deficit 和 rank-volume 结果没有
证明多个 operational parents 的 debits 可由同一份 $H$ 统一支付。

真正需要的新结构是 simultaneous replacement-response width / transition-overlap
定理，或者一个覆盖这类方法的 ordinary-transducer barrier。继续增加 macro-block
数量只会改进同一条件 theorem 的小数，不解决这个核心障碍。
