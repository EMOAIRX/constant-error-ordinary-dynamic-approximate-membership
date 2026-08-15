# 三 pivot 常数 `C_3>1.48`：证书独立审计

> 日期：2026-08-13。结论：`scripts/verify_three_pivot_148_certificate.py` 给出真正的
> 纯有理证书。它证明的是严格不等式 `C_3>1.48`，不证明
> `C_3=1.485506...`，也不依赖数值 optimizer、KKT 解的唯一性或三个 branches
> 同时 active。

## 1. 解析输入

写

\[
f_0(p,q)=\frac{A(p)+A(q)}2,
\quad
f_1(p,q)=\frac{B(p)+B(q)}2,
\quad
f_m(p,q)=\frac{B(p)+\Phi(p,q)}2.
\]

在凸域 `D={(p,q):0<p<q<1}` 上，三个函数均凸。对正有理权重

\[
(\lambda_0,\lambda_1,\lambda_m)
=\frac1{1000}(388,411,201),
\qquad \sum_i\lambda_i=1,
\]

定义

\[
L=\lambda_0f_0+\lambda_1f_1+\lambda_mf_m.
\]

于是对所有 `(p,q) in D`，

\[
\max\{f_0,f_1,f_m\}\ge L(p,q).
\tag{1}
\]

取有理证书点

\[
(p_0,q_0)=\left(\frac{149}{250},\frac{107}{125}\right).
\]

凸性的一阶不等式给

\[
L(p,q)\ge L(p_0,q_0)
+g_p(p-p_0)+g_q(q-q_0),
\tag{2}
\]

其中 `(g_p,g_q)=nabla L(p_0,q_0)`。不需要梯度恰为零。

## 2. 全局残差界

脚本用有理区间分别包住 `L(p_0,q_0)`、`g_p` 和 `g_q`。因为 `D` 包含在
`[0,1]^2` 中，

\[
|p-p_0|\le\max\{p_0,1-p_0\},
\qquad
|q-q_0|\le\max\{q_0,1-q_0\}.
\]

若 `G_p,G_q` 分别是梯度区间中绝对值的上界，则式 (2) 对所有 `D` 中的点给出

\[
L(p,q)\ge
\underline L_0
-G_p\max\{p_0,1-p_0\}
-G_q\max\{q_0,1-q_0\}.
\tag{3}
\]

这里使用更大的矩形而非三角域，只会使下界更弱，不影响正确性。

## 3. 对数区间为何严格

对有理 `x>=1`，令 `z=(x-1)/(x+1)`。脚本使用

\[
\log x
=2\sum_{k=0}^{T-1}\frac{z^{2k+1}}{2k+1}+R_T,
\]

以及纯有理余项界

\[
0\le R_T
\le\frac{2z^{2T+1}}{(2T+1)(1-z^2)}.
\]

`x<1` 时通过 `log x=-log(1/x)` 翻转区间。除法、乘法和符号翻转均由
`Fraction` 的区间运算完成；没有浮点数参与断言。

脚本中的导数公式也已逐项核对：

\[
A'(x)=-\frac1{x\ln2},
\]

\[
B'(x)=\frac1{\ln2}
\left[-\frac12\left(\ln\frac{2-x}{1-x}+1\right)
+\frac{2-x}{2(1-x)}\right],
\]

\[
\partial_p\Phi(p,q)=\frac1{\ln2}
\left[-\frac12\left(\ln\frac{2-p}{q-p}+1\right)
+\frac{2-p}{2(q-p)}\right],
\]

\[
\partial_q\Phi(p,q)
=-\frac{2-p}{2(q-p)\ln2}.
\]

## 4. 可复核输出

运行

```bash
python3 scripts/verify_three_pivot_148_certificate.py
```

得到一个由完整区间结果向下截断的短有理数

\[
\inf_{(p,q)\in D}L(p,q)
\ge\frac{740704116123}{500000000000}
=1.481408232246.
\]

与 `1.48=37/25` 的精确差为

\[
\frac{704116123}{500000000000}>0.
\]

结合式 (1)，

\[
\boxed{C_3>1.48}.
\]

## 5. 审计边界与残余风险

本证书只认证已经定义好的二维变分常数 `C_3`。从数据结构模型到 profile
functional、从 finite batch 到 `C_3` 的三-pivot Jensen reduction，以及最后的
`H>=C_3 n-o(n)` lifting，都是外部定理依赖，不由此脚本复核。

另外，`1.485506...` 仍只是高精度定位值。要认证该数值区间，需要对更接近精确
KKT 权重的有理 mixture 给出上下界或对 optimizer 做区间存在性认证；当前
`>1.48` 定理不需要这些步骤。
