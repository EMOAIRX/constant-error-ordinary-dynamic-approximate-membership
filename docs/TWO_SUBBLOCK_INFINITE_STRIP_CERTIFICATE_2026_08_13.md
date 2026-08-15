# Two-subblock modulus family：(q\le5) 的无限横带证书

> 日期：2026-08-13。状态：解析 reduction 加有理区间证书。它证明对固定
> (q=2,3,4,5)，所有充分大的 allocation modulus (Q) 都严格差于已认证的
> ((q,Q)=(3,6)) rate。它把每条无限横带缩成有限多个 (Q)；尚未认证这些有限
> cases中除了 ((3,6)) 以外全部更差，因此不是完整 ((q,Q)) 全整数 sharp theorem。

## 1. Family

状态保存 exact load (c) 与

\[
(a\bmod Q, a_1\bmod q, b_1\bmod q),
\]

其中 (a=a_0+a_1)。对应生成元为

\[
A_0=(1,0,0),\quad A_1=(1,1,0),\quad
B_0=(0,0,0),\quad B_1=(0,0,1)
\]

in (mathbb Z_Q\timesmathbb Z_q\timesmathbb Z_q)。

当 (c<Q) 时 allocation residue没有 wrap，reachable-state count精确为

\[
\boxed{
d_q(c)=\sum_{a=0}^c
\min(a+1,q)\min(c-a+1,q).
}
\tag{1}

## 2. Uncoupled rejection domination

忘掉 (a\bmod Q) collisions、改为保存 exact allocation (a)，只会缩小
syndrome fibers并提高 minimal-query rejection。因此任意有限 (Q) 的 Poisson
rejection不超过 uncoupled two-subblock值

\[
\boxed{
J_{q,\infty}(\lambda)
=e^{-\lambda/2}\sum_{t=0}^{q-1}\frac{(\lambda/4)^t}{t!}.
}
\tag{2}

令 (lambda_{q,\infty}) 是 (J_{q,\infty}=1/2) 的根，则真实 half-error load
满足 (lambda_{q,Q}\le\lambda_{q,\infty})。

证书使用下列有理上界：

\[
\begin{array}{c|c}
q&\bar\lambda_q\\\hline
2&2.293\\
3&2.652\\
4&2.751\\
5&2.770
\end{array}
\tag{3}

Taylor余项有理计算严格验证
(J_{q,\infty}(\bar\lambda_q)<1/2)，故
(lambda_{q,Q}<\bar\lambda_q)。

## 3. Frozen-tail state lower bound

由于 (d_c) 随 load不减，且 (d_c=d_q(c)) 对所有 (c<Q)，真实 OGF逐系数
支配

\[
\boxed{
A_{q,Q}^{\rm fr}(z)
=\sum_{c=0}^{Q-1}d_q(c)z^c
+d_q(Q-1)\frac{z^Q}{1-z}.
}
\tag{4}

因此真实 rate满足

\[
R_{q,Q}\ge
F_{q,Q}:=inf_{0<z<1}
\left\{
\bar\lambda_q^{-1}\log_2A_{q,Q}^{\rm fr}(z)-\log_2z
\right\}.
\tag{5}

这里同时用到：OGF coefficientwise domination；rate在 load参数上递减；以及式
(3) 的 load上界。

## 4. 为什么一个 (Q_0) 证书覆盖整个 tail

对固定 (q)，(d_q(c)) 非减。直接比较式 (4) 得

\[
A_{q,Q+1}^{\rm fr}(z)-A_{q,Q}^{\rm fr}(z)
=\frac{[d_q(Q)-d_q(Q-1)]z^{Q+1}}{1-z}\ge0.
\tag{6}

所以 (F_{q,Q}) 关于 (Q) 非减。只需认证一个 (Q_0)，即可覆盖全部
(Q\ge Q_0)。

## 5. 有理证书

以已认证的

\[
R_{3,6}<2.34616
\tag{7}

为 benchmark。脚本 `scripts/verify_two_subblock_infinite_strips.py` 只使用
`Fraction`、有理 exponential Taylor余项与 logarithm atanh-series余项；它在
(z\in[0.3,0.55]) 作有理 rectangle cover，并用 log-OGF convexity认证两侧
exteriors。输出：

\[
\begin{array}{c|c|c}
q&Q_0&F_{q,Q_0}\text{ 的认证下界}\\\hline
2&6&2.359303343\ldots\\
3&9&2.346586457\ldots\\
4&7&2.350447370\ldots\\
5&7&2.360427439\ldots
\end{array}
\tag{8}

每项均严格大于 (2.34616)。结合式 (6)：

\[
\boxed{
q=2,Q\ge6;quad
q=3,Q\ge9;quad
q=4,Q\ge7;quad
q=5,Q\ge7
}
\]

全部严格差于 ((3,6))。

## 6. Sharp theorem还缺什么

无限横带已缩成有限 cases：

\[
\begin{array}{c|c}
q&\text{仍需认证的 }Q\\\hline
2&1,\ldots,5\\
3&1,\ldots,8\\
4&1,\ldots,6\\
5&1,\ldots,6
\end{array}
\]

其中 ((3,6)) 已有完整 interval certificate；其余需要 exact profile加各自 rate
certificate。还必须另行处理 (q\ge6)，才能称为全整数 ((q,Q)) sharp theorem。

因此严格结论是 (q\le5) 的 infinite-strip theorem，而不是完整 family最优性。
