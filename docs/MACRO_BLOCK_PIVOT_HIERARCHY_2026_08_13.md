# KLZ all-pivot converse 的宏观分块层级

> 日期：2026-08-13。本文给出一个一般的、可逐层加强的有限维凸下界。
> 两个 blocks 恢复此前的三-pivot 常数 `1.485506...`；一般层级形成严格的
> refinement hierarchy。十个 blocks 的十一-pivot convex dual 已用纯有理证书
> 严格认证超过 `1.60`。完整连续极值仍未求解。

以下固定 `delta=1/2`，所有 logarithms 以 2 为底。记

\[
\Phi(a,c)=\left(1-\frac a2\right)
 \log\frac{2-a}{c-a},\qquad
A(c)=\Phi(0,c),\qquad B(a)=\Phi(a,1).
\tag{1}
\]

## 1. `m`-block 凸极值

给定整数 `m>=2` 和

\[
0<z_1\le\cdots\le z_m<1,
\tag{2}
\]

定义 `m+1` 个 branch

\[
G_0(z)=\frac1m\sum_{j=1}^m A(z_j),
\tag{3}
\]

\[
G_r(z)=\frac1m\left[
 \sum_{j=1}^r B(z_j)+
 \sum_{j=r+1}^m\Phi(z_r,z_j)
 \right],\qquad 1\le r<m,
\tag{4}
\]

以及

\[
G_m(z)=\frac1m\sum_{j=1}^m B(z_j).
\tag{5}
\]

在 diagonal 上把 `Phi(a,a)` 定义为 `+infinity`。宏观层级的第 `m` 层是

\[
\boxed{
L_m=\inf_{z\text{ satisfies }(2)}\max_{0\le r\le m}G_r(z).
}
\tag{6}
\]

每个 `G_r` 都是凸函数。因此 (6) 是有限维 convex epigraph problem；任意
正权重 `lambda_0,...,lambda_m`、`sum lambda_r=1` 都给出 dual lower bound

\[
\max_rG_r(z)\ge\sum_{r=0}^m\lambda_rG_r(z).
\tag{7}
\]

若在某个有理点 `z^0` 附近认证

\[
g\in\partial\left(\sum_r\lambda_rG_r\right)(z^0),
\tag{8}
\]

则凸性在整个 cube 上给出

\[
L_m\ge
\sum_r\lambda_rG_r(z^0)
-\sum_{j=1}^m |g_j|\max\{z_j^0,1-z_j^0\}.
\tag{9}
\]

式 (9) 正是纯有理 interval verifier 的接口；它不需要数值 optimizer 本身
是可靠的，也不需要先证明 optimizer 唯一。

## 2. 从 finite profile 到宏观层级

令 finite profile 长度 `b=mh`，并写成

\[
0=x_0\le x_1\le\cdots\le x_b=1.
\tag{10}
\]

第 `j` 个宏观 block 的内部平均为

\[
z_j^{(b)}=\frac1{h-1}
\sum_{i=(j-1)h+1}^{jh-1}x_i.
\tag{11}
\]

只保留 pivots `s=rh`，`0<=r<=m`。对 endpoint pivot `0`，在每个 block
丢掉边界点并对 `A` 使用 Jensen，得到

\[
F_{b,0}(x)\ge\frac{h-1}{b}
 \sum_{j=1}^m A(z_j^{(b)})
=\left(1-\frac1h\right)G_0(z^{(b)}).
\tag{12}
\]

同理，pivot `b` 给出

\[
F_{b,b}(x)\ge
\left(1-\frac1h\right)G_m(z^{(b)}).
\tag{13}
\]

固定 `1<=r<m`。pivot `rh` 左侧的 predecessor terms 中，每个前 block
保留 `h-1` 个内部点，对 `B` 分 block 使用 Jensen。右侧每个后 block 也保留
`h-1` 个内部点，对 `c` 使用 Jensen。又因为单调性给出

\[
z_r^{(b)}\le x_{rh}\le z_j^{(b)},\qquad j>r,
\tag{14}
\]

且 `partial_a Phi>=0`，所以

\[
\begin{aligned}
F_{b,rh}(x)
&\ge\frac{h-1}{b}\left[
 \sum_{j=1}^rB(z_j^{(b)})+
 \sum_{j=r+1}^m\Phi(x_{rh},z_j^{(b)})
 \right]\\
&\ge\left(1-\frac1h\right)G_r(z^{(b)}).
\end{aligned}
\tag{15}
\]

由 (12)--(15)，

\[
\max_{0\le s\le b}F_{b,s}(x)
\ge\left(1-\frac1h\right)L_m.
\tag{16}
\]

因此对每个固定 `m`，在 full-fiber theorem 中选择趋于无穷的
`b=mh`，就得到

\[
\boxed{H\ge L_m n-o(n).}
\tag{17}
\]

### 正则项没有改变结论

正式 batch inequality 使用

\[
\Phi_{\delta,\gamma}(a,c)
=(1-\delta a)\log
 \frac{1-\delta a}{\delta(c-a+\gamma)},
\qquad\gamma\downarrow0.
\tag{18}
\]

它仍然联合凸。更重要的是，令

\[
t=\frac{1-\delta a}{\delta(c-a+\gamma)},
\]

则以自然 logarithm 计算有

\[
\partial_a\Phi_{\delta,\gamma}
=\frac{\delta}{\ln2}(t-\ln t-1)\ge0.
\tag{19}
\]

所以 (15) 的单调性方向在 finite `gamma` 下完全相同。对固定 `m`，任意有界
sublevel 都迫使 `z_1`、`1-z_m` 和相邻 gaps 远离零；否则相应 endpoint 或
interior branch 发散。故在相关 compact sublevel 上
`Phi_{delta,gamma}->Phi_{delta,0}` 一致，(17) 可安全通过 `gamma->0` 极限。

## 3. 层级的 refinement 单调性

### Theorem 3.1

对任意正整数 `k,m`，

\[
\boxed{L_{km}\ge L_m.}
\tag{20}
\]

**证明。** 给定 fine profile `w_1<=...<=w_{km}`，把连续的每 `k` 个变量
合成一组，并记组平均为

\[
p_j=\frac1k\sum_{i=(j-1)k+1}^{jk}w_i.
\tag{21}
\]

在 fine problem 中只保留 branches `0,k,2k,...,mk`。Endpoint branches
逐组 Jensen 后至少是 coarse profile `p` 的对应 branch。对内部 branch `rk`，
左侧 `B` terms 同样逐组 Jensen；其 right kernel 的左坐标是 `w_{rk}`，而
`p_r<=w_{rk}`。先对每个后组的右坐标使用 Jensen，再用
`partial_a Phi>=0`，得到

\[
G_{rk}^{(km)}(w)\ge G_r^{(m)}(p).
\tag{22}
\]

因此 fine branches 的最大值至少为 `max_r G_r^{(m)}(p)>=L_m`。对 `w`
取 infimum 即得 (20)。证毕。

特别地，

\[
L_2\le L_4\le L_8\le\cdots.
\tag{23}
\]

该序列有有限极限。事实上取均匀测试点 `z_j=j/(m+1)`，用
`m!>=(m/e)^m` 分别控制 endpoint sums 和 interior factorial sums，即可给出
一个与 `m` 无关的粗常数上界。这里无需知道极限的精确值。

## 4. 当前严格常数与数值前沿

`m=2` 时，(6) 正是此前的三-pivot 二维极值。纯有理证书给出

\[
L_2>1.48,
\]

而数值优化把它定位在 `1.4855061257...` 附近；后一个小数不是精确值证明。

`m=4` 的数值定位为

\[
z\approx(0.43528658,0.67247400,0.82240523,0.92552205),
\tag{24}
\]

Fraction-only interval verifier `scripts/verify_four_block_154_certificate.py` 已严格认证

\[
\boxed{
L_4\ge\frac{1541537885859}{10^{12}}>1.54.
}
\tag{25}
\]

数值优化把最优值定位在 `1.5415378859...` 附近，但证书不声称该小数是
精确最优值，也不依赖 optimizer 唯一。

五个 branches 在 (24) 处等势；对应正 dual weights 约为

\[
(0.31697718,0.14764927,0.12483846,0.11747221,0.29306288).
\tag{26}
\]

这些小数只用于定位有理证书。式 (25) 才是正式 decimal theorem：verifier
使用有理 atanh 级数及显式尾界包住所有 logarithms，再通过 (9) 在整个
`[0,1]^4` 上扣除 gradient residual。

同一种 convex-dual 接口在 `m=10` 给出更强的纯有理证书。脚本
`scripts/verify_ten_block_pivot_160_dual.py` 仅使用 `Fraction` 算术、atanh 级数和显式
余项界，认证

\[
\boxed{
L_{10}\ge \frac{321597400969}{200000000000}
=1.607987004845>1.60.
}
\tag{27}
\]

这里分数是 verifier 向下截断得到的可读下界；未经截断的有理区间下界更强。
凸性把正权 branch mixture 在一个有理近驻点处的函数值推广到整个
`[0,1]^{10}`，再显式扣除全部梯度残差。因此式 (27) 不是局部搜索、网格覆盖或
浮点优化结论。

进一步的数值形状为

\[
L_8\approx1.5933391054,
\qquad
L_{16}\approx1.6349007171,
\qquad
L_{32}\approx1.6648667206.
\tag{28}
\]

这些层级的全部 branches 在数值精度内等势，说明宏观层级不是一次性常数技巧；
它正在系统吸收更多 internal-pivot information。但式 (28) 仍只是数值定位，
不能写成定理。当前最高的正式常数声明是式 (27) 的 `L_10>1.60`。

## 5. 研究含义与未解点

这一层级给出的核心结论不是把 `1.485` 的末位数字继续提高，而是：

1. 任意固定深度都化为一个可全局认证的有限维 convex program；
2. refinement 在整除意义下严格保持下界，dyadic 层级有极限；
3. 十 blocks 已用纯有理证书严格跨过 `1.60`，更深层数值仍持续上升；
4. 每一层只使用原 KLZ transcript 中同一个状态的不同合法 pivots，没有重复收费。

尚未完成的是识别 `lim_j L_{2^j}` 与完整连续 Bellman 极值是否相等，以及解析求出
该极限。证明 equality 需要处理 monotone path jumps、diagonal logarithmic
singularity、lower semicontinuity 和 recovery sequence。当前论文最稳的主定理应是
一般层级 (6)、finite-profile reduction (17)、refinement theorem (20)，再加一个
完全机器可核验的 `L_10>1.60` dual certificate。这里从 finite profile 到
ordinary dynamic AMQ 的结论仍显式依赖已单独审计的 full-fiber batch theorem；
本文件没有重新证明那一 lifting。
