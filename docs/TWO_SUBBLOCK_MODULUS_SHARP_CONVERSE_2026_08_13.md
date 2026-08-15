# Two-subblock order-3 allocation modulus family 的 sharp converse

> 日期：2026-08-13。状态：固定内部 order (q=3) 时，解析 tail reduction与
> (Q=1,ldots,8) 的零外部依赖有理区间证书均已闭合。验证程序
> `scripts/verify_two_subblock_modulus_sharp_converse.py` 已运行并输出 `PASS`。

## 1. Family

四个均匀 symbols 为 (A_0,A_1,B_0,B_1)。对 composition

\[
(a_0,a_1,b_0,b_1),\qquad c=a_0+a_1+b_0+b_1,
\]

保存

\[
\left(c,\ (a_0+a_1)\bmod Q,\ a_1\bmod3,\ b_1\bmod3\right).
\tag{1}
\]

记其 load-(c) reachable-state 数和 minimal one-sided rejection 为
(d_c(Q)) 与 \(\rho_c(Q)\)。

## 2. 任意 (Q) 的精确有限公式

对 (0\le r<Q)、(u\in\{0,1,2\})，定义

\[
m_Q(r,u)=\min\{a\ge u:a\equiv r\pmod Q\}
=r+Q\max\left(0,\left\lceil\frac{u-r}{Q}\right\rceil\right).
\tag{2}
\]

一个 residue triple ((r,u,v)\in\mathbb Z_Q\times\mathbb Z_3^2) 在 load
(c) 可达，当且仅当存在 (a\equiv r\pmod Q) 满足

\[
u\le a\le c-v.
\tag{3}
\]

等价地，

\[
\boxed{
d_c(Q)=\#\{(r,u,v):m_Q(r,u)+v\le c\}.
}
\tag{4}
\]

随机 syndrome 的整数权重是多项式

\[
(1+X+XY+Z)^c
\pmod{X^Q-1,\,Y^3-1,\,Z^3-1}
\tag{5}
\]

的 coefficients。对每个 syndrome，用式 (3) 分别增加约束
(a_0>0,a_1>0,b_0>0,b_1>0)，即可精确判断 fiber support union。
因此 \(\rho_c(Q)\) 是一个由至多 (9Q) 个 residues 的有限整数计算给出的
有理数。sumset 稳定后 \(d_c=9Q\)，下一层开始 \(\rho_c=0\)。

## 3. (Q\ge9) 的解析排除

令

\[
e_t=\min(t+1,3),\qquad
D_c=\sum_{a=0}^c e_a e_{c-a}.
\tag{6}
\]

(D_c) 是分别保存两个 binary order-3 subblock exact loads 时的 macro-layer
state count。若 (c<Q)，则 (0\le a\le c) 使 (a\bmod Q) 无 wrap，故

\[
d_c(Q)=D_c\qquad(c<Q).
\tag{7}
\]

translation 给 (d_c(Q)) 单调不减，所以

\[
d_c(Q)\ge D_{Q-1}\qquad(c\ge Q-1).
\tag{8}
\]

定义对真实 quotient 过度有利的 frozen-tail OGF

\[
\underline A_Q(z)
=\sum_{c=0}^{Q-1}D_cz^c+D_{Q-1}\frac{z^Q}{1-z}.
\tag{9}
\]

分别保存 exact subblock loads 只会细分 syndrome fibers，因而其 rejection
逐点不小于 allocation-mod-(Q) quotient。写 \(\lambda_Q\) 为 half-error
根，则

\[
\lambda_Q\le\lambda_\infty
=2\lambda_{3}
=2.651638150570379\ldots,
\tag{10}
\]

其中 \(\lambda_3\) 是 binary order-3 的 half-error 根。

对 positive OGF，

\[
F(A,\lambda)=\inf_{0<z<1}
\left\{\lambda^{-1}\log_2A(z)-\log_2z\right\}
\tag{11}
\]

随 coefficients 增加而增加，并随 \(\lambda\) 增加而减少。因此

\[
R_Q\ge F(\underline A_Q,\lambda_\infty).
\tag{12}
\]

式 (9) 随 (Q) coefficientwise 增加：从 (Q) 到 (Q+1) 时，低于 (Q)
的 coefficients 不变，而从 degree (Q) 起由 (D_{Q-1}) 提升为
(D_Qge D_{Q-1})。故右侧随 (Q) 单调增加。直接认证
(Q=9) 的一维 saddle 给

\[
F(\underline A_9,\lambda_\infty)
=2.3477511225\ldots
>2.3461490549.
\tag{13}
\]

所以所有 (Q\ge9) 都严格劣于 (Q=6)。

## 4. 剩余有限表

精确枚举 (Q=1,ldots,8) 得到：

| (Q) | rate |
|---:|---:|
| 1 | 2.454422292991... |
| 2 | 2.396564577061... |
| 3 | 2.380274516613... |
| 4 | 2.354635406580... |
| 5 | 2.346464991509... |
| 6 | **2.346149054803...** |
| 7 | 2.347360640026... |
| 8 | 2.348237321930... |

最小 gap 是 (R_5-R_6=0.000315936706\ldots)。随附 verifier 对每个
(Q\le8) 使用 exact integer convolution 生成 profile，并以 rational Taylor
余项分别认证 Poisson root、saddle root 和 rate separation。最接近的一对满足

\[
R_5>2.346464991347,
\qquad
R_6<2.346149054805.
\tag{14}
\]

同一 verifier 还认证

\[
F(\underline A_9,\lambda_\infty)
>2.347751122371.
\tag{15}
\]

> 在所有整数 (Q\ge1) 的 two-subblock order-3 allocation-modulus family 中，
> (Q=6) 是唯一的 half-error rate minimizer。

## 5. 尚未证明的更大命题

若把内部 one-count modulus 也改成任意 (q)，式 (2)--(5) 只需把 (3)
替换为 (q)，仍给精确有限公式。当前搜索中 ((q,Q)=(3,6)) 是全局最佳；但
尚未给出对全部无界整数 (q) 的统一 analytic tail bound。因此不能把本节的
(q=3) sharp theorem 称为整个 two-parameter family 的 matching converse。
