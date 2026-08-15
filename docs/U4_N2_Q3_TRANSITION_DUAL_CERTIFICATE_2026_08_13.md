# U=4, n=2, q=3 ordinary dynamic AMQ 的对称 transition dual

> 日期：2026-08-13。状态：LP/MILP certificate 已闭合；对称 dual 已提取成
> 五类 histories、整数权重 180。纯手写三状态 case split 尚未完成，因此
> “每个 transducer 得分至少 116”目前由 exact 0--1 pricing MILP认证。

## 1. 模型

取 universe U=[4]、capacity n=2，只检查从 empty 开始、长度至多 3 的合法
histories。一个 deterministic tape 有三个 persistent states，对每个 key a 有任意
确定 maps I_a,D_a，并有任意 initial state。zero false negatives 强迫某 state
接受所有曾在该 state 到达的 current sets 之 union，所以固定 transitions 后无损
采用这个 minimal accepted set。

随机 public-tape filter 是这些 deterministic tapes 的 convex mixture。对固定
history h 和 current nonmember x，false-positive indicator 记为

\[
F_T(h,x)\in\{0,1\}.
\tag{1}
\]

## 2. 五轨道 dual

下表中不同字母表示不同 keys，每个有序实例分别计数。

| 类型 | history 与 query | 实例数 | 每实例权重 |
|---|---|---:|---:|
| E | empty，query a | 4 | 3 |
| P | I_a,I_b，query c 不属于 {a,b} | 24 | 5 |
| R | I_a,D_a，query b 不等于 a | 12 | 1 |
| G | I_a,D_a,I_b，query deleted a | 12 | 1 |
| N | I_a,D_a,I_b，query c 不属于 {a,b} | 24 | 1 |

总权重为

\[
4\cdot3+24\cdot5+12+12+24=180.
\tag{2}
\]

定义 deterministic tape 的整数分数

\[
\begin{aligned}
\Phi(T)={}&3\sum_aF_T(\varnothing,a)\\
&+5\sum_{a\ne b}\sum_{c\notin\{a,b\}}F_T(I_aI_b,c)\\
&+\sum_{a\ne b}F_T(I_aD_a,b)\\
&+\sum_{a\ne b}F_T(I_aD_aI_b,a)\\
&+\sum_{a\ne b}\sum_{c\notin\{a,b\}}F_T(I_aD_aI_b,c).
\end{aligned}
\tag{3}
\]

### Certified finite lemma

对每个三状态 deterministic key-only transducer，

\[
\boxed{\Phi(T)\ge116,}
\tag{4}
\]

且存在 transducer 取等。

式 (4) 当前有两份机器可复核证明：

1. `scripts/finite_u_column_generation.py` 的 `PricingMILP` 用 binary variables显式表示
   所有 history states、labeled functions、accepted masks和 FP indicators；对式
   (3) 的整数 objective，HiGHS 返回全局 integer optimum 116；
2. checkpoint `/private/tmp/u4_n2_q3_depth3_columns.npz` 含 233 个 behavior
   columns；master optimum 与 exact pricing optimum 都是 29/45，reduced cost
   为零。完整 certificate 在 `/private/tmp/u4n2q3_certificate.npz`。

这里“exact”指有限 0--1 MILP 的全局最优证书。为完全独立于 solver，仍需补一个
穷举 verifier 或手写 case split。

## 3. LP 推论

把式 (3) 的权重除以 180，得到与 public tape 无关的固定 history-query 分布
mu。由式 (4)，每个 deterministic tape 都满足

\[
\mathbb E_{(h,x)\sim\mu}F_T(h,x)\ge\frac{116}{180}=\frac{29}{45}.
\tag{5}
\]

对任意 public-tape mixture再取期望，至少一个固定 history-query pair 的 FPR
不小于 29/45。反向，checkpoint master 给出 mixture，使全部 depth-3 pointwise
FPR 至多 29/45。因此

\[
\boxed{\operatorname{OPT}(U=4,n=2,q=3,\text{depth }3)=\frac{29}{45}.}
\tag{6}
\]

特别地，q<4 不可能达到 epsilon=1/2，即使只要求 depth 3。q=1,2 包含于
三状态类，也可用已知二状态更强值 3/4。四状态 frozen balanced mask 达到任意长
history、epsilon=1/2，所以这个最小实例的 state threshold 恰为 4=2^n。

## 4. 对称化的意义

solver直接返回的 optimal dual 支撑在 61 个 individual constraints 上且不对称。
对 S_4 重命名 keys 作群平均后，dual 值不变，因为 deterministic transducer 类与
constraints 都在该作用下闭合。平均后的 certificate 恰只支撑五个 orbits，并给出
式 (2)--(3) 的小整数权重。

五类 histories 的作用是：E 惩罚 initial ghosts；P 测量满容量 pair state 对
另外两个 keys 的 FP；R 测量 insert-delete 回到 empty 后的 ghosts；G 测量删除
a、再插入 b 后对旧 a 的 ghost；N 测量同一 trace 对第三方 keys 的 collateral
acceptance。pair snapshots 占总 dual mass 2/3，deletion compatibility贡献剩余
1/3。

这里可以精确量化动态额外代价。若完全删除 transitions，只要求给六个
2-subsets各分配三个 static states之一，并令 state mask 包含被分配 pairs 的 union，
穷举全部 \(3^6=729\) 个 colorings、再对 resulting columns 作 LP，得到

\[
\operatorname{OPT}_{\rm static}(U=4,n=2,q=3)=\frac5{12}.
\tag{7}
\]

因此同样 state budget 下，depth-3 dynamic right-congruence把最优 FPR提高

\[
\frac{29}{45}-\frac5{12}=\frac{41}{180}.
\tag{8}
\]

这是一条严格 static-versus-dynamic separation，不依赖渐近解释。

## 5. 精确组合 lemma 接口

令

\[
q_0=\text{initial},\quad r_a=I_a(q_0),\quad t_a=D_a(r_a),
\]

\[
s_{ab}=I_b(r_a),\quad u_{ab}=I_b(t_a)\quad(a\ne b).
\tag{9}
\]

对 state z，令 A_z 是所有长度至多 3、到达 z 的 histories 的 current sets之 union。
那么式 (4) 等价于：对任意三个 colors 的 q_0,r_a,t_a,s_ab,u_ab，只要存在共同
labeled maps I_a,D_a 使式 (9) 同时成立，按 A_z 计算的式 (3) 至少为 116。

不能删去“存在共同 labeled maps”。例如 r_a=r_a' 强迫

\[
s_{ab}=I_b(r_a)=I_b(r_{a'})=s_{a'b}.
\tag{10}
\]

这正是 history-dependent transducer 的 right-congruence 内容；若把每个 pair
history 独立着色，命题为假。

还不能只检查式 (3) 中获得正 dual 权重的五类 histories。零 false negative 所
强迫的 accepted set (A_z) 是**全部**深度至多 3 合法 histories 到达 (z) 时
current sets 的 union；一些 dual 权重为零的路径（例如插入两键后删除一个）仍会
扩大 (A_z)，进而改变五个加权轨道的 false positives。若只枚举式 (7) 中显式
出现的 successor 而忽略这种 closure，整数目标会出现伪最小值 (104<116)。
因此完整 history closure 不是求解器实现细节，而是 finite lemma 的必要语义。

## 6. Johnson graph 推广边界

这个 certificate 严格超过纯 static snapshot 信息；精确 gap 已由式 (7)--(8)
给出。但它仍只是有限定理，不能直接推出
任意 n 的 2^n-state lower bound。

对一般 U=[2n]，正确 analogue 应从 base n-set S 出发，使用 replacement edge

\[
S\longrightarrow S-a\longrightarrow S-a+b,
\qquad a\in S,\ b\notin S.
\tag{11}
\]

dual需同时给权重于 base nonmember、neighbor 上 deleted key a 的 ghost、neighbor
上其他 nonmembers以及 short Johnson cycles。S_{2n} 对称化会把权重压缩到由
intersection pattern决定的有限 orbits；这是从五轨道证书得到的严格方法接口。
目前没有证明任何一般 n 的 orbit weights 对所有 q<2^n transducers 给正 margin。

## 7. 严格裁决

已严格得到：

1. U=4,n=2、depth 3 下，三状态 randomized ordinary dynamic AMQ 的 optimal
   pointwise FPR 恰为 29/45；
2. half error 精确需要至少四 states，而四状态 frozen mask 已达到；
3. optimal dual可对称化成五个 history-query orbits 和整数 score 116/180；
4. static snapshot optimum 是 5/12，动态兼容产生 41/180 的 additive gap；
5. obstruction 不依赖 canonical、history independence、locality、monotonicity或
   lattice structure。

尚未得到：式 (4) 的纯手写 case split、任意 n 的 2^n lower bound、可张量化
dual或 SODA 级 asymptotic ordinary-AMQ下界。因此这是一个真实 finite theorem
和干净的 transition dual seed，但还不是 full ordinary 模型的渐近突破。
