# Algebraic threshold quotient：hostile correctness 与 novelty audit

> 日期：2026-08-13。审计对象：
> `ALGEBRAIC_THRESHOLD_QUOTIENT_UPPER_BOUND_2026_08_13.md`。
> 结论：核心构造正确；未发现 zero-FN、删除、ghost、任意长历史或 fixed-state
> 语义漏洞。(L=2) 的 (2.3490834402\ldots) rate 已独立复算。正式定理仍需
> 补 finite-(n) FPR、累计系数鞍点 lemma，以及 (L=2) 对所有 (L) 的最优性
> 证明或降级表述。

## 1. 最终判定

这个构造是真正的 ordinary dynamic upper bound mechanism：

- key-only `Insert/Delete/Query`；
- zero false negatives；
- pointwise-over-public-randomness FPR；
- fixed worst-case memory，覆盖全部总负载至多 (n) 的 states；
- 支持任意长合法 history，不是 finite-horizon/whp no-overflow theorem；
- 不访问 exact backing set，不枚举 live keys；
- 高负载状态允许 lossy merge，但 deletion 后能自动恢复 low-load exact support。

因此它严格击穿 uniform binary fingerprint exact-multiplicity 的

\[
2.38449984248\ldots n
\]

all-compositions rate；这不是 smooth/current-state Shannon rate 的重述。

## 2. Local automaton

每个 outer block 保存

\[
c=\text{block load},
\qquad
a=\sum_{x\text{ in block}}h(x)\pmod{L+1}.
\tag{1}
\]

### 2.1 Insert/Delete 是完整 right congruence

对 label (x)，令 (b=h(x)\in\{0,1\})。操作为

\[
(c,a)\xmapsto{\operatorname{Insert}(x)}(c+1,a+b),
\]

\[
(c,a)\xmapsto{\operatorname{Delete}(x)}(c-1,a-b),
\tag{2}
\]

第二坐标在 (\mathbb Z/(L+1)\) 中计算。若两个隐藏 multisets 给出相同
((c,a))，执行相同合法 label 后仍给出相同 pair。故 quotient 对每个 labeled
update 都闭合；不是 snapshot coloring。

### 2.2 高负载碰撞不会破坏删除

假设 block 从任意 (c>L) 的 state 经若干合法 deletes 降到 (c'\le L)。群
accumulator 的 telescope identity 给最终 residue

\[
a'\equiv\sum_{x\text{ remaining}}h(x)\pmod{L+1}.
\tag{3}
\]

右侧真实 one-count 位于 ([0,c']\subseteq[0,L])，因此 residue 的标准代表元
恰等于真实 one-count；不可能 wrap。这里不需要知道哪些其他 keys 与被删 key
共享 inner bit。合法 deletion promise只用于保证 logical set transition有效，
算法本身只需重算 (g(x),h(x))。

所以没有 ghost accumulation，也不需要在 high layer 保存额外 route。

### 2.3 Query 与 zero FN

- (c=0)：block 空，回答 NO；
- (1\le c\le L)：由 (a\in[0,c]) 得 one-count，zero-count 为 (c-a)，
  精确恢复两个 inner symbols 是否出现；
- (c>L)：回答 YES。

成员在 low layer 的 symbol multiplicity至少为一，在 high layer 整块接受，故
zero FN 对每条 tape、每条 history 确定性成立。

## 3. Pointwise FPR

固定任意合法 history，其当前集合为 (S)，(|S|=s\le n)，再固定
nonmember (x\notin S)。在 fully random independent (g,h) 下，

\[
C=|\{y\in S:g(y)=g(x)\}|
\sim\operatorname{Bin}(s,1/B).
\tag{4}
\]

条件于 (C=t\le L)，query 误报概率为 (1-2^{-t})；条件于 (C>L)，误报
概率为一。因此 exact finite-(n) FPR 是

\[
\boxed{
\varepsilon_{n,L}(s,B)
=1-\sum_{t=0}^{L}
\binom st
\left(\frac1B\right)^t
\left(1-\frac1B\right)^{s-t}2^{-t}.
}
\tag{5}
\]

等价地，complement 是
(\mathbb E[2^{-C}\mathbf1(C\le L)])。式 (5) 随 (s) 不减；可由增加一个
Bernoulli trial 的 coupling 直接证明。因此最坏情形是 (s=n)。

若 (n/B\to\lambda)，(5) 收敛到

\[
1-e^{-\lambda}\sum_{t=0}^L\frac{(\lambda/2)^t}{t!}.
\tag{6}
\]

原稿式 (3) 是正确极限，但“fully random exchangeability 给出同一表达式”应
改成 (5)：finite (n) 是 Binomial，不是精确 Poisson。

要得到有限 (n) 时严格 FPR (\le\varepsilon)，可选择

\[
\frac nB=\lambda_L-o(1)
\tag{7}
\]

或直接取使 (5) 在 (s=n) 不超过目标的最小整数 (B)。因为校准只改
(B/n) 一个 (o(1))，空间只改 (o(n))。这一步必须在正式 theorem 中写出。

所需随机性：fully random (g,h) 足够且在 KLZ 免费公共随机带模型内。若要
换 finite-independence seed，必须重新证明对每个 fixed (S,x) 的 (5) 或足够
接近的上界；当前信息论 theorem 不需要做这一步。

## 4. Fixed-state enumeration

负载 (t\) 的可达 local state 数为

\[
d_t=\begin{cases}
t+1,&t\le L,\\
L+1,&t>L.
\end{cases}
\tag{8}
\]

low load 时每个 one-count (0,\ldots,t) 可达；high load 时每个 residue
(0,\ldots,L) 可达，例如先选择适当 number of one-bits，再用 (L+1) 个
one-bits改变真实 count而保持 residue，剩余负载用 zero-bits补足。对实际有限
universe，fully random tape 上某 block/symbol 可能缺 key；把所有 formal
states 编进去只是 upper bound，不伤 correctness。

所以 local OGF

\[
A_L(z)=\sum_{t=0}^L(t+1)z^t+(L+1)\frac{z^{L+1}}{1-z}
\tag{9}
\]

正确，全局所有 formal states 的数量恰由

\[
N_{B,n}=[z^{\le n}]A_L(z)^B
\tag{10}
\]

上界。rank/unrank (10) 给单一 fixed block；counts 与 residues 没有被另算。

### 4.1 累计系数 saddle point

令 (B/n\to1/\lambda)，取唯一 (z\in(0,1)) 满足

\[
zA_L'(z)/A_L(z)=\lambda.
\tag{11}
\]

则 positive aperiodic sequence 的标准 saddle/local-CLT 给

\[
\log_2 N_{B,n}
=B\log_2A_L(z)-n\log_2z+o(n),
\tag{12}
\]

即每 key rate

\[
R_L(\lambda)
=\lambda^{-1}\log_2A_L(z)-\log_2z.
\tag{13}
\]

这里使用累计系数不会改变一阶 exponent。一个正文级证明可定义 tilted IID
local load

\[
\Pr_z[T=t]=d_tz^t/A_L(z).
\]

其均值为 (\lambda)、方差为有限正常数、span 为一。local CLT 给
(\Pr[\sum_{i=1}^BT_i\in[n-O(\sqrt n),n]]=\Theta(1))。在该窗口中把
(z^{-\sum T_i}) 与 (z^{-n}) 比较，只损 (2^{o(n)})，从而给 (12) 的下界；
Cauchy/tilting 直接给上界。正式稿应加入此 lemma，而不只写“standard”。

## 5. 数值独立复算

解 (6) 的 (1/2)-root，再解 (11)，得到：

| (L) | (\lambda_L) | saddle (z_L) | (R_L(\lambda_L)) |
|---:|---:|---:|---:|
| 1 | 1.146193220621 | 0.454639314141 | 2.372057541534 |
| 2 | 1.325819075285 | 0.447778045429 | **2.349083440193** |
| 3 | 1.375441246548 | 0.431720696326 | 2.360295858677 |
| 4 | 1.384796914431 | 0.420530483422 | 2.372835928750 |
| 5 | 1.386123748662 | 0.414653009152 | 2.379535046200 |
| 6 | 1.386277678745 | 0.411828743855 | 2.382463602726 |
| 10 | 1.386294360648 | 0.409488020194 | 2.384443430239 |

数值与原稿前五行逐项一致。(L\to\infty) 时趋于
(2.38449984248\ldots) 也与公式一致。

但是，当前表格本身只证明 (L=2) 优于所列 (L)。若正文声称“该 family 的
全局最优 threshold 是 (L=2)”，仍需：

1. 对所有整数 (L\ge3) 给 analytic lower bound；或
2. 给 interval-arithmetic certificate 覆盖有限范围，再用显式 tail bound
   处理所有大 (L)。

在补齐前，安全表述是“在已核验的 (L\le10) 中 (L=2) 最优，且
(L\to\infty) rate 更大”；不能把它升级成全 family theorem。

## 6. 任意长历史与公共随机性

state code覆盖所有

\[
\{((c_j,a_j))_{j=1}^B:\sum_jc_j\le n\}
\]

formal states。每次合法 update 后仍在该集合中；rank 编码没有随机 overflow、
typical-set failure 或 horizon union bound。公共 (g,h) 固定后，(2) 是永久
可重复的 deterministic transition。任意长 churn 只在有限状态图中循环，不会
累积额外 metadata。

因此该 construction 的“everlasting fixed-state”主张成立。

## 7. 最小压力测试

取 (L=2)。high state ((c,a)=(3,0)) 可来自 inner ones count (0) 或 (3)。
这两个 worlds发生 collision。若共同删除一个 (h=1) 的真实 key，只在第二个
world合法，故不用比较。若从第二个world删除该 key，得到 ((2,2))，它正确表示
剩余 two ones；若从 first world 删除 (h=0) key，得到 ((2,0))，正确表示 two
zeros。继续任意合法 deletes，每次 accumulator 都跟随被删 label，降到 low
layer 时总能恢复真实 support。

这个例子说明“high collision 后 low decode不可能”这一自然反对意见是错误的：
不同 hidden worlds不必共享同一个合法 deletion label；对实际 world 的 label
更新携带恰好所需的逆信息。

## 8. Novelty 与 paper 价值

### 8.1 真实贡献

该机制第一次在当前研究组合中严格展示：ordinary key-only deletion 的 lossy
right congruence 可以把全部 exact multiplicity states 合并，并在未来删除后
无代价恢复 low layer。它把 fixed-state rate 从

\[
2.38449984248\ldots
\]

降到

\[
2.34908344019\ldots,
\]

改善约

\[
0.03541640229\text{ bits/key}.
\]

这不是 engineering filter variant；核心是 finite-state algebraic quotient 与
all-state generating-function rate。

### 8.2 当前不足

单独作为 SODA headline 仍偏薄：

- 只改善一个常数约 (1.5\%\)；
- 距 smooth/current-state benchmark (2.20061148\ldots) 仍有明显 gap；
- 没有 matching converse；
- 当前没有 efficient word-RAM implementation；
- “(L=2) 全 family 最优”尚未证明。

### 8.3 可形成论文的增强方向

最有价值的 package 是：

1. 给全部 (\varepsilon\) 的 threshold-quotient envelope
   (\min_LR_L(\lambda_L(\varepsilon))) 与相变点；
2. 证明 binary threshold family 的全局最优 (L) 区间；
3. 对更一般 finite abelian accumulators 建立 restricted converse，刻画
   “low-load decodability versus high-load state collapse”的最优 tradeoff；
4. 找到严格低于 (2.34908) 的 nonbinary/Sidon 或 support-only quotient；
5. 或实现 succinct dynamic rank/unrank，使构造不只信息论存在。

若完成 1--3，论文会有清晰的 algebraic classification，而不只是单点常数。若再
显著逼近 (2.2006)，SODA 价值会更强。

## 9. 主稿需要立即修正的文字问题

原 Markdown 含三个 ASCII control characters：backspace `0x08` 一处、vertical
tab `0x0b` 两处，分别破坏 (c\le L)、(\varepsilon) 等公式；另有若干
`\rm` 在写入时变成 carriage-return 风格的乱码显示。应清除 control bytes 并
统一使用普通 LaTeX，例如 `\mathrm{in}`、`\mathrm{bits/key}`。

这些是可读性问题，不影响数学构造，但正式稿必须修复。

