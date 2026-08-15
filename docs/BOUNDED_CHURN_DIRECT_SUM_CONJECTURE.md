# Bounded churn direct-sum：反例与停止报告

> 状态：原 direct-sum 猜想为假。本文件保留反例、错误根源与仍可安全使用的结论，避免后续再次复用该猜想。

## 1. 被否决的猜想

原计划把初始集合拆成 surviving old keys 与 newcomers，并试图证明

\[
F_T
\stackrel{?}{\ge}
(n-T)\log_2(1/\varepsilon)
+C(\varepsilon)T\log_2(1/\varepsilon)-o(n).
\tag{1}
\]

其直觉是：最终物理状态必须同时支付 survivor 的静态 membership 信息与 newcomer 的 incremental 信息。

这个直觉不成立。两个任务可以共享同一份随机 rejection certificate；各自的下界只能直接推出 maximum，不能推出 sum。

## 2. Frozen-mask 反例

取

\[
m=2n,\qquad \varepsilon=\frac12.
\]

从免费只读随机带上取一个均匀的 balanced mask

\[
C\subseteq U,\qquad |C|=n,
\]

并在持久状态中精确存储 `S cap C` 的 characteristic vector。查询规则为：

- 若 `x in C`，精确回答 `x in S`；
- 若 `x notin C`，一律回答 YES。

更新只需在 `C` 内修改相应的 bit。它不需要 history independence、外部 exact set 或 rebuild oracle，并支持任意长的合法 insert/delete 或 replacement history。

对任意固定当前非成员 `x`，

\[
\Pr[x\notin C]=\frac12,
\]

所以 pointwise FPR 恰为 `1/2`。空间为

\[
n+O(1)\text{ bits}.
\tag{2}
\]

而 (1) 在 `epsilon=1/2` 时给出

\[
F_T\ge n+(C(1/2)-1)T-o(n),
\]

只要 `T=Theta(n)` 且 `C(1/2)>1` 就与 (2) 矛盾。

## 3. 错误的精确位置

原 fiber-product 论证隐含了以下伪命题：

> 固定 survivor source 后的 newcomer reachable-state families，会随不同 survivor sources 近似相乘。

实际上一组物理状态可以被大量 survivor fibers 共用。frozen mask 中，同一个 `C` 同时承担：

1. 对旧成员的 exact rejection certificate；
2. 对新成员的 exact rejection certificate；
3. 所有时刻的 pointwise false-positive budget。

因此：

- `U_0` 与 `U_1` 上的错误预算可以高度相关；
- 不能分别固定“对两边都好”的随机带再把代价相加；
- endpoint accepted masks、reachable transcripts 与状态 fibers 都可能完全重叠；
- static entropy 与 incremental entropy 不是独立资源。

任何后续 lower bound 都必须显式给 shared rejection certificates 定价。

## 4. Dense regime 的正确边界

在同一参数下，静态 finite-universe optimum 为

\[
F_0(2n,n,1/2)
=\bigl(2H_2(1/4)-1\bigr)n+o(n)
=0.6225562489\ldots n+o(n).
\]

结合 frozen mask，对所有 `T`，包括无限 churn，只有

\[
0.6225562489\ldots n-o(n)
\le F_T(2n,n,1/2)
\le n+o(n).
\tag{3}
\]

所以动态性最多可能增加

\[
0.3774437511\ldots n
\]

bits。任何随 `T` 无界线性增长的 dense-universe 公式都应立即判错。

## 5. Dummy reduction 的安全边界

以公开 dummies 初始化，并用

\[
d_i\longmapsto x_i
\]

模拟 fresh incremental insertions 的 reduction 本身是正确的。但它只能转移一个已经针对 **互异 fresh keys** 证明的 incremental lower bound。

Lovett--Porat 原证明的 hard distribution 位于 `U^k`，允许重复标签。其 path-label closure 在 distinct-insertion 模型中不自动成立：另一个到达同一状态的 prefix 可能已经使用了实际 continuation 中的 key，使拼接后的 history 非法。

把第 `i` 次新键限制在互不相交的时间层 `U_i` 可以恢复 continuation legality。若每层大小为 `q` 且需要 `q\gg T`，总新键宇宙满足

\[
m-n=Tq\gg T^2.
\]

但时间层彼此独立时，也可逐层使用静态编码，总空间只有
`T log_2(1/epsilon)+o(T)`；Lovett--Porat 的额外常数正好消失。因此这不是 lower-bound repair。

在 `epsilon=1/2`，reviewer-safe 的显式常数是
`C_LP(1/2)>=1.1`。`1.13` 只是原文未给参数证书的 computer-search remark，不能当作正式定理常数。

## 6. 对 SODA 路线的结论

以下内容不足以单独构成 SODA 主结果：

- `T log(m/T)=o(n)` 时的 black-box stability lifting；
- dummy-key reduction；
- time-layered Lovett--Porat 合法性修补；
- static-survivor 与 newcomer 两项下界的普通相加。

仍可能够 SODA 的 bounded-churn 结果必须是以下之一：

1. 一个显式允许 certificate sharing 的 transition-product inequality；
2. 一个匹配的 hybrid upper/lower churn curve；
3. 一个反过来利用 shared certificates、严格改善现有动态 filter 的普通模型构造。

在出现其中之一以前，bounded churn 应作为主问题的 warmup 和反例实验室，而不是已接近完成的主论文。
