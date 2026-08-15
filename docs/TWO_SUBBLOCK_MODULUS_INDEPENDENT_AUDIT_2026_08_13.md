# Two-subblock allocation modulus：独立 hostile audit

## 结论

**PASS，但定理的作用域必须保持为文中明确给出的单参数 family。**

严格可声称的是：固定内部余数阶数 (q=3)，并保存

\[
\bigl(c,(a_0+a_1)\bmod Q,a_1\bmod3,b_1\bmod3\bigr)
\]

时，在所有整数 (Q\ge1) 中，(Q=6) 是 half-error fixed-state
enumerative rate 的唯一极小点。这个结论不自动覆盖所有 two-subblock
Abelian quotients，也不覆盖内部阶数可变的二参数 family。

独立证书为 `scripts/verify_two_subblock_modulus_independent_audit.py`。所有断言只使用
整数和 `Fraction`；打印的小数不参与证明。

## 1. 有限部分

证书从四个 labeled increments 重新递推 reachable syndromes 与 walk
multiplicities。对 load (c) 的 syndrome (s)，第 (i) 个 symbol 在 fiber
support union 中出现，当且仅当 (s-v_i) 在 load (c-1) 可达。因此
rejection profile 可以直接用整数计数，不需要枚举并存储所有 compositions。

对 (Q=1,\ldots,8)，证书逐项核对文档中的 exact rational profiles，并为
Poisson half-error 根和 OGF saddle 根验证有理端点符号。得到的严格率区间宽度
均小于 (2.1\times10^{-10})。尤其

\[
0.0003159365<R_5-R_6<0.0003159370.
\]

证书还逐一验证 (Q=1,2,3,4,7,8) 的率严格大于 (R_5)，所以有限部分的
最近竞争者确实是 (Q=5)。

## 2. (Q\ge9) 的解析 reduction

### 2.1 state count 下界

令

\[
e_t=\min(t+1,3),\qquad D_c=\sum_{a=0}^c e_a e_{c-a}.
\]

当 (c<Q) 时 allocation load 没有 wrap，所以 (d_c(Q)=D_c)。此外，四个
increments 中含有 group zero increment (B_0)。给任意 load-(c) witness
追加一个 (B_0)，得到同一 syndrome 的 load-(c+1) witness，故 reachable
sets 嵌套，(d_c(Q)) 单调不减。因此

\[
d_c(Q)\ge D_{Q-1}\quad(c\ge Q-1).
\]

这严格推出真实 OGF coefficientwise 支配

\[
\underline A_Q(z)=\sum_{c=0}^{Q-1}D_cz^c
 +D_{Q-1}\frac{z^Q}{1-z}.
\]

又因为 (D_c) 单调递增，
(\underline A_{Q+1}\) coefficientwise 支配 (\underline A_Q)。所以只需认证
(Q=9)。原文的“translation”应改成上述 zero-increment injection；否则理由
写得过短。

### 2.2 half-error load 上界

保存 exact allocation load 的 uncoupled summary 是 allocation-mod-(Q)
summary 的 refinement。细分 fiber 只能缩小 support union，所以它逐 load 的
minimal one-sided rejection 不小于 quotient rejection。

这里还需要说明 half-error 根确实可比较。对任意固定 insertion sequence，若
某 coordinate 已被 support union 接受，追加任意 symbol 后，原 witness 也可
追加同一 symbol，故接受状态不会退回拒绝状态。在 Poisson process coupling
下 rejection probability 随 load 参数单调不增；在本有限 quotient 中它从
1 严格降到 0，half-error 根唯一。于是

\[
\lambda_Q\le\lambda_\infty.
\]

uncoupled rejection 可直接写为

\[
J_\infty(\lambda)
=e^{-\lambda/2}\sum_{t=0}^2\frac{(\lambda/4)^t}{t!}.
\]

证书严格认证

\[
2.65163815056<\lambda_\infty<2.65163815058.
\]

### 2.3 rate 比较

对 positive OGF，

\[
F(A,\lambda)=\inf_{0<z<1}
\left\{\lambda^{-1}\log_2 A(z)-\log_2z\right\}
\]

随 OGF coefficients 增加而不减，随 λ 增加而不增。结合前两节，

\[
R_Q\ge F(\underline A_Q,\lambda_\infty)
\ge F(\underline A_9,\lambda_\infty),\qquad Q\ge9.
\]

纯有理 saddle certificate 给出

\[
F(\underline A_9,\lambda_\infty)>2.3477511223
>R_6.
\]

因此 tail reduction 闭合。

## 3. 量词与 theorem boundary

这个 sharp converse 的安全表述需要同时写明：

1. (q=3) 固定；
2. allocation checksum 恰为 total (A)-subblock load modulo cyclic (Q)；
3. 两个内部坐标恰为 (a_1\bmod3,b_1\bmod3)；
4. 使用 minimal one-sided query 和 fixed-state enumerative asymptotic rate；
5. 优化变量仅为整数 (Q\ge1)。

不能从本证书推出“所有 fixed-(q=3) two-subblock additive quotients”中的
最优性。一般 checksum 可能改变 primitive coefficients、混合三个 residue
coordinates，或使用非循环 quotient；尤其 (3\mid Q) 时不能在未证明
normal-form/classification theorem 的情况下把这些情形消掉。也不能推出
((q,Q)) 二参数 family 的全局最优性。

所以最终判定是：

- 对 allocation-load-mod-(Q) family：**PASS**；
- 若标题或摘要声称覆盖所有 two-subblock order-3 lattices：**FAIL，属于
  overclaim**。
