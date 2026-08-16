# 一个严格低于 (2.349083n) 的 designed cross-block lattice

> 日期：2026-08-13。状态：构造、逐层状态数、逐层 rejection、任意历史更新语义
> 均已解析闭合；一维单调根与 saddle 的有理区间证书已由
> `scripts/verify_cross_block_mod6_construction.py` 验证通过。

所有对数以 2 为底。

## 1. 结论

在ordinary one-sided dynamic approximate membership的information-theoretic
fixed-state模型中，存在一个canonical additive construction，在half error下使用

\[
\boxed{2.34614905664n+o(n)}
\]

bits，严格优于此前binary order-3 threshold quotient的

\[
2.349083440193\ldots n+o(n).
\]

改进约为

\[
0.002934385390\ldots n
\]

bits。数值不大，但结构机制是新的：两个binary order-3子块共享exact macro-load，
只额外保存其中一个子块load modulo 6，从而跨子块合并原本分别保存的load信息，
同时保留足够的support rejection。

## 2. Local quotient

每个outer macroblock内有四个symbols

\[
A_0,A_1,B_0,B_1,
\]

各以概率 \(1/4\) 出现。令composition为

\[
x=(a_0,a_1,b_0,b_1)\in\mathbb N^4,
\qquad c=|x|.
\]

local state保存

\[
\boxed{
\left(c, (a_0+a_1)\bmod6, a_1\bmod3, b_1\bmod3\right).
}
\tag{1}

等价地，保存exact load和有限群

\[
G=\mathbb Z_6\times\mathbb Z_3\times\mathbb Z_3
\]

中的additive syndrome，四个increments为

\[
v_{A_0}=(1,0,0),
\quad v_{A_1}=(1,1,0),
\quad v_{B_0}=(0,0,0),
\quad v_{B_1}=(0,0,1).
\tag{2}

Insert/Delete只需加减对应increment并更新exact load，因此：

- updates是key-only且确定的；
- 支持任意长合法history；
- 没有overflow、rebuild或failure event；
- 高load删除回低load时，syndrome自动恢复相应辨识力。

query使用minimal one-sided rule：给定 \((c,s)\) 和symbol \(i\)，当且仅当存在
某个非负composition \(y\) 满足

\[
|y|=c,\qquad Ay=s,\qquad y_i>0
\tag{3}
\]

时回答 `YES`。因此zero false negatives逐tape成立。

## 3. State profile

写

\[
a=a_0+a_1,
\qquad u=a_1,
\qquad v=b_1.
\]

load \(c\) 的reachable syndromes恰为

\[
\{(a\bmod6,u\bmod3,v\bmod3):
0\le a\le c, 0\le u\le a, 0\le v\le c-a\}.
\tag{4}

直接按 \(a\) 的six-residue intervals分类，得到

\[
(d_0,d_1,\ldots)
=(1,4,10,18,27,36,44,50,53,54,54,\ldots).
\tag{5}

load 9 已命中全部 \(6\cdot3\cdot3=54\) 个group states。若 \(cV=G\)，固定
任一increment \(v_i\) 即有 \((c+1)V\supseteq cV+v_i=G\)，所以从 \(c=9\)
起所有layers都命中整个group。于是local-state
OGF为

\[
\boxed{
A(z)=\sum_{c\ge0}d_cz^c
=\frac{P(z)}{1-z},
}
\tag{6}

其中

\[
P(z)=1+3z+6z^2+8z^3+9z^4+9z^5
+8z^6+6z^7+3z^8+z^9.
\tag{7}

式 (5) 也可由式 (4) 作有限的54个residue检查；它不是随机搜索假设。

## 4. Rejection profile

固定load \(c\)。对每个syndrome fiber \(C\)，minimal rule的accepted symbols
是fiber内composition supports的union。uniform multinomial source下，rejection
恰为

\[
\rho_c
=1-\frac14\sum_CW_c(C)|U(C)|.
\tag{8}

对式 (4) 的residue classes作解析有限分类，得到

\[
\boxed{
(\rho_0,\ldots,\rho_9)
=\left(
1,\frac34,\frac9{16},\frac{13}{32},\frac9{32},\frac3{16},
\frac{237}{2048},\frac{63}{1024},
\frac{189}{8192},\frac{189}{32768}
\right),
}
\tag{9}

并且

\[
\boxed{\rho_c=0\qquad(c\ge10).}
\tag{10}

一个简洁的可核对证书是，各load中support-union size为
\(0,1,2,3,4\) 的syndrome class数依次为

\[
\begin{array}{c|ccccc}
c&0&1&2&3&4\\\hline
0&1&0&0&0&0\\
1&0&4&0&0&0\\
2&0&4&6&0&0\\
3&0&0&14&4&0\\
4&0&0&10&16&1\\
5&0&0&6&24&6\\
6&0&0&4&24&16\\
7&0&0&2&20&28\\
8&0&0&0&12&41\\
9&0&0&0&4&50\\
10&0&0&0&0&54.
\end{array}
\tag{11}

为严格推出式 (9)，还需在每个class中按multinomial weight而非只按class数求和；
代入式 (8)即得到所列有理数。load 10 的每个fiber support union均为四个
symbols。若load \(c\) 的每个syndrome分别有包含四种symbols的witnesses，固定
任一increment \(v_j\)；对load \(c+1\) 的任意syndrome \(t\)，由 \(cV=G\)
知 \(t-v_j\in cV\)。把 \(v_j\) 插入该fiber的四个witnesses，仍得到 \(t\)
fiber内的四种symbols。因此式 (10) 归纳地对全部tail成立。

## 5. Half-error calibration

取 \(B\) 个outer macroblocks，fully random outer hash使load极限为
\(\operatorname{Pois}(\lambda)\)。fixed nonmember的渐近拒绝概率是

\[
J(\lambda)
=e^{-\lambda}\sum_{c=0}^{9}\frac{\lambda^c}{c!}\rho_c.
\tag{12}

它严格递减；令 \(\lambda_*\) 是唯一满足

\[
J(\lambda_*)=\frac12
\tag{13}

的正根。数值为

\[
\lambda_*=2.648017694023161\ldots.
\tag{14}

全状态joint enumerative coding的asymptotic fixed-state rate为

\[
R
=\min_{0<z<1}
\left\{
\frac1{\lambda_*}\log_2A(z)-\log_2z
\right\}.
\tag{15}

唯一saddle满足

\[
\lambda_*=\frac{zA'(z)}{A(z)},
\tag{16}

其数值为

\[
z_*=0.453320842862439\ldots.
\tag{17}

代回式 (15) 的 numerical optimum 为

\[
\boxed{R=2.346149054803345\ldots.}
\tag{18}

与旧常数的gap约为 \(0.002934385389796\)，远大于最后显示小数的舍入误差。
随附的零外部依赖 verifier `scripts/verify_cross_block_mod6_construction.py` 完全使用
`Fraction`，逐composition枚举式 (5)、(9)、(11)，并用有理Taylor余项定位

\[
\lambda\in[2.64801769,2.64801770],
\qquad
z\in[0.45332084,0.45332085]
\]

上式 (13)、(16) 的端点符号。用于主定理的 reviewer-safe 结论是固定测试点给出的
严格上界

\[
R<2.34614905664<2.34908.
\tag{18a}
\]

旧版文档曾把 verifier 在一个固定 $z$ 上打印的下端值误写成 $R$ 的严格下界；固定
测试点只能给 $\inf_z$ 的上界。式 (18) 保留为 numerical location，不作为两侧区间
证书。

## 6. Ordinary key API 与 finite (n)

公共hash把每个key送到 \([B]\times[4]\)。对每条预先固定、与public seed独立
的legal history和fixed current nonmember，member labels IID，query label独立。
若current set大小为 \(m\le n\)，target block中的member数为
\(\operatorname{Bin}(m,1/B)\)。Cayley quotient的pathwise deletion projection给
\(\rho_{c+1}\le(3/4)\rho_c\)，也可由式 (9) 直接核对；故rejection随block load
下降。于是 \(m=n\) 是FPR的最坏current size，只需校准
\(\operatorname{Bin}(n,1/B)\)。取

\[
\lambda_n=\lambda_*-n^{-1/4},
\qquad B_n=\left\lceil n/\lambda_n\right\rceil.
\tag{18b}
\]

令 \(\mu_n=n/B_n\le\lambda_n\)。因为式 (9) 的
rejection functional有界，Le Cam bound给它与
\(\operatorname{Pois}(\mu_n)\) 下期望之差为
\(O(n/B_n^2)=O(1/n)\)。而 \(J'(\lambda_*)<0\)，故

\[
J(\lambda_n)=\frac12+\Theta(n^{-1/4}).
\]

又因 \(J\) 递减，\(J(\mu_n)\ge J(\lambda_n)\)。上述margin支配Poisson误差
和rounding，故对充分大 \(n\) 以及全部 \(m\le n\)，FPR严格不超过
\(1/2\)。有限多个较小 \(n\) 可用exact dictionary处理，不影响渐近式。
\(B_n=n/\lambda_*+o(n)\)，所以不改变一阶rate。

fixed state枚举所有block tuples

\[
((c_1,s_1),\ldots,(c_B,s_B)),
\qquad \sum_jc_j\le n,
\]

其中每层syndrome数为式 (5)。capacity-\(n\) state总数满足，对任意
\(0<z<1\)，

\[
N_{n,B}=[z^{\le n}]A(z)^B
\le z^{-n}A(z)^B.
\tag{18c}
\]

在式 (16) 的saddle取值并enumeratively编码，得到
\(\log_2N_{n,B}=nR+o(n)\)。这是对全部合法histories有效的固定codebook，不是
平均熵。这个upper bound不需要rich-fiber假设：codebook枚举abstract block
states的superset；finite universe中不可达的states只会减少实际状态数。只需
\(|U|\ge n+1\) 使fixed nonmember query存在。fully random labels在不同distinct
keys上独立，已经足够推出上述pointwise FPR。

这里的history量词与ordinary KLZ模型一致：结论对每条预先固定、与public seed
独立的任意有限legal history成立，history长度没有上界。本文不额外声称对根据
hash seed或既往query answers选择updates的adaptive adversary仍有同一FPR；那是
更强且不同的模型。zero false negatives与update合法性则逐tape、对任意长
history成立，因为state始终是当前composition的canonical additive function。

## 7. 为什么这是cross-block而不是换了alphabet

若分别保存两个binary order-3 subblocks的exact loads，state是

\[
(a,a_1\bmod3; b,b_1\bmod3),
\qquad a+b=c.
\]

新构造只保存 \(c\)、\(a\bmod6\) 和两个one-count residues。它把

\[
(a,u,b,v)
\sim(a+6,u,b-6,v)
\tag{19}

的nonnegative compositions跨subblocks合并。这个合并节省了load-allocation
states，却不像完全忘掉 \(a\) 那样立刻让两个subblocks的supports互相污染。

模数6不是任意调参：它正好是binary support-recovery周期3的两倍。小模数3的
跨load合并过早，rate约为 \(2.38027\)；模数6达到 \(2.34615\)；随后模数
\(9,12,\ldots\) 从下方回到uncoupled binary limit
\(2.34908344\)。因此突破来自一个有限强度的cross-load coupling，而不是更大
group带来的近单射编码。

## 8. 结论边界与下一步

本文严格给出一个ordinary canonical additive upper bound，因而已经回答：

> designed cross-block lattices确实可以严格击败binary product lattice的
> \(2.349083440193n\) barrier。

它还没有回答：

- \(2.346149054803\ldots\) 是否在全部designed lattices中最优；
- 其他subblock数量、不同threshold moduli或非均匀inner symbols能否继续下降；
- history-dependent/noncanonical filters能否显著更优；
- 是否存在matching restricted converse。

最自然的下一族是：取 \(k\) 个order-3 binary subblocks，保存总load、每个
one-count mod3，以及前 \(k-1\) 个独立load-allocation线性组合的适中模数。
需要用Smith normal form分类这些allocation lattices，并联合优化support-union
distortion与OGF。与盲目搜索大群不同，这个family已有明确机制和严格基点：
\(k=2\)、allocation modulus 6 给式 (18)。
