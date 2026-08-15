# 等块 all-pivot converse：ordinary half-error dynamic AMQ 的 `1.6079n` 下界

> 日期：2026-08-13。状态：full-fiber batch interface 的 prefix-mass 步骤已改写为
> two-sigma-field lemma，并通过独立敌对复核；`q=10` 的数值下界由纯有理
> convex-dual verifier 认证。本文不解除
> `u/n^2 -> infinity`，也不声称解决常数误差的 tight rate。

所有对数以 2 为底。

## 1. 结论

沿用 `ENDPOINT_BATCH_CONVERSE_2026_08_13.md` 已证明的模型与 batch interface：

- 容量为 `n`，固定最坏 `H`-bit persistent memory；
- 免费只读 public random tape；
- arbitrary history dependence、non-monotonicity、ghosts 和 global certificates；
- key-only legal `Insert/Delete/Query`；
- zero false negatives；
- 每条固定 history、每个固定 current nonmember 的 pointwise FPR 至多 `1/2`；
- `u/n^2 -> infinity`，并支持 `omega(n)` 次操作。

则

\[
\boxed{H\ge C_{10}n-o(n),\qquad C_{10}>1.6079.}
\tag{1}
\]

其中 `C_10` 是下面显式 10 维凸变分的值。数值定位为

\[
C_{10}=1.6079870048457\ldots,
\tag{2}
\]

而纯有理 verifier 严格认证下界

\[
C_{10}\ge
\frac{803993501430859}{500000000000000}
=1.607987002861718\ldots>1.6079.
\tag{3}
\]

因此这严格改进了 endpoint constant `1.434406...` 与 three-pivot certified
constant `1.48`。改进来自同时使用 11 个 KLZ pivots，而不是新的数据结构假设。

## 2. 已有 full-fiber pivot functional

令

\[
\Phi(a,c)=\left(1-\frac a2\right)
\log\frac{2-a}{c-a},\qquad 0\le a<c\le1,
\tag{4}
\]

并定义

\[
A(x)=\Phi(0,x)=\log\frac2x,
\qquad
B(x)=\Phi(x,1)
=\left(1-\frac x2\right)\log\frac{2-x}{1-x}.
\tag{5}
\]

full-fiber exact batch code 已给出：对任意 `b -> infinity` 和非降 profile

\[
0=x_0\le x_1\le\cdots\le x_b=1,
\tag{6}
\]

每个 pivot `s in {0,...,b}` 都满足

\[
\frac Hn\ge F_{b,s}(x)-o(1),
\tag{7}
\]

其中

\[
F_{b,s}(x)=\frac1b\left[
\sum_{k=1}^{s}\Phi(x_{k-1},1)
+\sum_{k=s+1}^{b}\Phi(x_s,x_k)
\right].
\tag{8}
\]

有限 `b` 的正式证明先使用 denominator `c-a+gamma_b`，其中
`gamma_b=O(4^{-b})`；完成以下固定维数凸 reduction 后才令
`b -> infinity` 与 `gamma_b -> 0`。

## 3. `q` 个等块的有限维凸层级

固定整数 `q>=1`，取 `b=qh`。将内部坐标分成 `q` 个长度 `h-1` 的 blocks：

\[
I_r=\{rh+1,\ldots,(r+1)h-1\},
\qquad 0\le r<q,
\tag{9}
\]

并定义 block averages

\[
p_r=\frac1{h-1}\sum_{i\in I_r}x_i.
\tag{10}
\]

profile 单调性给

\[
0<p_0\le p_1\le\cdots\le p_{q-1}<1.
\tag{11}
\]

只保留 pivots `s=jh`，其中 `j=0,...,q`。在每个 block 中丢掉至多一个
boundary term，损失总计 `O(q/b)=o(1)`。

### Endpoint `j=0`

对每个 block 的 `A(x_k)` 使用 Jensen：

\[
F_{b,0}(x)
\ge \frac1q\sum_{r=0}^{q-1}A(p_r)-o(1).
\tag{12}
\]

### Interior pivot `1<=j<q`

左侧 `j` 个 blocks 对 `B(x_{k-1})` 使用 Jensen。右侧 block `r>=j`
中的第一变量是 cut coordinate `x_{jh}`，且

\[
x_{jh}\ge p_{j-1}.
\]

函数 `Phi(a,c)` 对第一变量非降、对第二变量凸，故

\[
F_{b,jh}(x)
\ge\frac1q\left[
\sum_{r<j}B(p_r)
+\sum_{r\ge j}\Phi(p_{j-1},p_r)
\right]-o(1).
\tag{13}
\]

### Endpoint `j=q`

同理，

\[
F_{b,b}(x)
\ge\frac1q\sum_{r=0}^{q-1}B(p_r)-o(1).
\tag{14}
\]

定义 `q+1` 个 branches

\[
L_{q,0}(p)=\frac1q\sum_{r=0}^{q-1}A(p_r),
\tag{15}
\]

\[
L_{q,j}(p)=\frac1q\left[
\sum_{r<j}B(p_r)
+\sum_{r\ge j}\Phi(p_{j-1},p_r)
\right],
\quad1\le j<q,
\tag{16}
\]

\[
L_{q,q}(p)=\frac1q\sum_{r=0}^{q-1}B(p_r).
\tag{17}
\]

于是得到严格的 finite-dimensional hierarchy：

\[
\boxed{
C_q=\inf_{0<p_0\le\cdots\le p_{q-1}<1}
\max_{0\le j\le q}L_{q,j}(p),
\qquad
H\ge C_qn-o(n).
}
\tag{18}
\]

当 `q=1` 时式 (18) 是 endpoint bound；`q=2` 正是此前的 three-pivot
二维变分。

## 4. 为什么这是凸优化

`A` 和 `B` 都是凸函数。代换

\[
y_a=1-a/2,\qquad y_c=1-c/2
\]

后，

\[
\Phi(a,c)=y_a\log\frac{y_a}{y_a-y_c},
\tag{19}
\]

它是 relative-entropy perspective 与 affine map 的复合，因此在
`a<c` 上联合凸。每个 `L_(q,j)` 都是凸函数之和，式 (18) 是凸 minimax。

这一点允许用一个有限 dual witness 对整个连续可行域给全局证书，而不需要
高维网格枚举。

## 5. `q=10` 的全局 dual certificate

取 verifier 中列出的有理小数向量 `p*` 和正权重

\[
\lambda_0,\ldots,\lambda_{10}>0,
\qquad\sum_j\lambda_j=1.
\tag{20}
\]

定义凸函数

\[
L(p)=\sum_{j=0}^{10}\lambda_jL_{10,j}(p).
\tag{21}
\]

对任意可行 `p`，

\[
\max_jL_{10,j}(p)\ge L(p).
\tag{22}
\]

凸性的一阶下界给

\[
L(p)\ge L(p^*)+\nabla L(p^*)\cdot(p-p^*).
\tag{23}
\]

因为每个坐标属于 `[0,1]`，

\[
L(p)\ge L(p^*)-\|\nabla L(p^*)\|_1.
\tag{24}
\]

主证书 `scripts/verify_ten_block_160_certificate.py` 只使用 Python `Fraction`。
每个自然对数由恒等式

\[
\log x=2\sum_{k\ge0}\frac{z^{2k+1}}{2k+1},
\qquad z=\frac{x-1}{x+1},
\tag{25}
\]

的前 120 项和显式几何尾界包住。它严格输出

\[
L(p^*)\ge1.607987003822005\ldots,
\tag{26}
\]

\[
\|\nabla L(p^*)\|_1
\le9.602862443443853\cdot10^{-10}.
\tag{27}
\]

所以

\[
\boxed{
C_{10}\ge
\frac{803993501430859}{500000000000000}
>1.6079.
}
\tag{28}

这证明式 (1)。证书只需要检查有理级数尾界、正权重、权重和为一以及式 (26)--(27)；
不信任 SLSQP 或任何 local optimizer。

## 6. Sanity checks 与贡献边界

### 没有超过已知 upper bounds

half error 下，当前相关 benchmarks 约为：

- uniform fingerprint multiset 的 Shannon/whp rate：`2.287904n`；
- everlasting binary threshold quotient：`2.349083n`；
- exact fingerprint count-vector fixed-length baseline：`2.384500n`。

式 (1) 仍显著低于它们，不存在数值矛盾。不同 upper bounds 的空间语义并不完全
相同，因此这里只作 sanity check，不声称 matching gap。

### 仍有主要限制

式 (1) 完全继承 full-fiber transport 的条件

\[
u/n^2\longrightarrow\infty.
\]

它没有解决 KLZ/FOCS 2025 在一般 `u/n -> infinity` regime 的完整 constant-error
open problem，也没有给出 matching construction。`cover-and-tombstone` 反例说明
单 parent rejection lemma 不能解除该限制；需要真正的 multi-parent overlap
或 entropy--transport dichotomy。

### 方法上的新增内容

相对于只报告一个更大常数，本结果的可复用部分是：

1. 从全部 KLZ pivots 系统抽取任意固定阶 `q` 的凸 converse hierarchy；
2. 用 block averages 处理任意跳跃的 profile，而不假设光滑极限；
3. 用正 convex-dual witness 对连续高维 minimax 作短小、全局、机器可核验认证。

数值探索显示 `C_q` 随所试阶数继续上升，但本文只声明经过 dual 认证的 `q=10`
结论。整除 refinement 的严格单调性 `C_(kq)>=C_q` 见
`MACRO_BLOCK_PIVOT_HIERARCHY_2026_08_13.md`；连续 all-pivot 极限的识别以及解除
`u >> n^2` 仍开放。

## 7. 复核命令

```bash
python3 scripts/verify_ten_block_160_certificate.py
python3 scripts/verify_ten_block_pivot_160_dual.py
python3 scripts/verify_four_block_pivot_154.py
python3 scripts/verify_three_pivot_148.py
```

第一条是主证书；第二条是独立的纯有理、有 power-of-two range reduction 的
交叉检查；其余两条是低维交叉检查。
