# Ternary shortest relation at radius three：解析分类与 translate 表

> 日期：2026-08-13。状态：Sections 1--4 是解析的有限分类；Section 5 明确区分
> rank-one relation envelope 与 finite-index completion。结论识别出
> \(\mathbb Z_{12},V=\{0,1,4\}\) 的 shortest-relation type，并证明它是 radius
> three 两种 primitive support types中 rejection更高的一类，但尚未证明它在
> 全部 finite-index ternary lattices中 rate extremal。

## 1. 定义与 cancellation

令

\[
A_2=\{d\in\mathbb Z^3:d_0+d_1+d_2=0\},
\qquad L\le A_2
\tag{1}
\]

是 ternary load-preserving composition lattice。对 \(d\ne0\)，唯一写成

\[
d=d^+-d^-,
\qquad d^+,d^-\in\mathbb N^3,
\qquad \operatorname{supp}(d^+)\cap\operatorname{supp}(d^-)=\varnothing.
\tag{2}
\]

由于 \(d\in A_2\)，两边质量相等。定义 relation radius

\[
r(d)=|d^+|=|d^-|,
\qquad r(L)=\min_{d\in L\setminus\{0\}}r(d).
\tag{3}
\]

若 load-3 compositions \(x,y\) collision但有共同部分
\(t_i=\min(x_i,y_i)\)，则 cancellation 后

\[
x-t\sim y-t,
\qquad |x-t|=|y-t|<3.
\tag{4}
\]

所以在 \(r(L)=3\) 假设下，任何首次 load-3 collision pair必须恰为
\((d^+,d^-)\)，而不是任意两个质量 3 compositions。这删除了一个容易产生
假分类的歧义：任意 collision pair模置换/换向有十类，真正的 shortest positive/
negative parts只有下面两类。

## 2. 两种且仅两种 support types

### Theorem 2.1（radius-three finite classification）

设 ternary lattice满足 \(r(L)=3\)。任取 shortest relation \(d\)。在 coordinate
permutation和换号 \(d\mapsto-d\) 下，\((d^+,d^-)\) 恰属于：

\[
\begin{array}{c|c|c|c}
\text{type}&d^+&d^-&d\\ \hline
A&(3,0,0)&(0,3,0)&(3,-3,0)\\
B&(3,0,0)&(0,2,1)&(3,-2,-1).
\end{array}
\tag{5}
\]

**证明。** 两个 nonempty disjoint supports共同位于三个 coordinates中，所以至少
一边 support size为 1。置换后令该边为 \((3,0,0)\)。另一边是在剩余两个
coordinates上的 3 的 partition，只可能是 \(3+0\) 或 \(2+1\)。交换两边与
交换后两个 coordinates给式 (5)。\(\square\)

特别地，所谓“\((0,0,3)\) 与 \((0,1,2)\)”之类共享 coordinate 的 load-3
collision并不是第三种 shortest type；它 cancellation 后是 radius one relation。

## 3. 单 shortest relation 的全部 translates

先只取 rank-one subgroup \(\langle d\rangle\)，不加入 finite-index lattice的第二
个独立 generator。load \(c\ge3\) 的 primitive translate edges是

\[
d^++t\sim d^-+t,
\qquad t\in\mathbb N^3,quad |t|=c-3.
\tag{6}
\]

### Lemma 3.1（translate count 与 class count）

对 types A、B及每个 \(c\ge3\)：

1. 式 (6)有
   \[
   E_c={c-1\choose2}
   \tag{7}
   \]
   条 distinct edges；
2. 这些 edges沿 \(d\)-orbits形成 forests；
3. rank-one quotient的 load-\(c\) composition classes恰有
   \[
   \boxed{d_c^{\langle d\rangle}
   ={c+2\choose2}-{c-1\choose2}=3c.}
   \tag{8}
   \]

**证明。** 式 (7)是质量 \(c-3\) ternary compositions数。不同 \(t\)给不同有向
edge，因为减去固定 \(d^+\)恢复 \(t\)。每个 connected component位于一条
\(x+\mathbb Zd\) 上，按 coefficient \(k\) 排序后 edges连接相邻整数点，故无
cycle。因此每条 edge恰把 class count减少一。总 composition数为
\({c+2\choose2}\)，相减即得式 (8)。\(\square\)

式 (8)只描述 rank-one envelope。任意 finite-index completion \(L\supsetneq
\langle d\rangle\) 还会合并这些 orbits，所以只能推出

\[
d_c(L)\le3c,
\tag{9}
\]

不是下界。额外合并同时产生额外 support-union distortion；这正是需要联合分析的
部分。

## 4. 精确 rejection-loss 表

令 exact-composition rejection为

\[
a_c=\left(\frac23\right)^c.
\tag{10}
\]

对 rank-one quotient \(\langle d\rangle\)，按每个 orbit的 multinomial weight和
support union直接求和，可得闭式。

### Theorem 4.1（type A）

若 \(d=(3,-3,0)\)，则

\[
\boxed{
\rho_c^A
=\frac{2^{c+1}+c+5}{3^{c+1}}
\qquad(c\ge3).
}
\tag{11}
\]

相对 exact composition的 loss为

\[
\boxed{
a_c-\rho_c^A
=\frac{2^c-c-5}{3^{c+1}}.
}
\tag{12}
\]

**证明。** quotient只忘记 counts \((x_0,x_1)\) 之间的 multiples of 3，保留
\(x_2\)及 \(x_0\bmod3\)。若 \(x_2>0\)，symbol 2必接受；symbols 0、1分别在
fiber含相应 positive representative时接受。拒绝 symbol 2只可能在 \(x_2=0\)，
其总概率贡献为 \(2^c/3^{c+1}\)。

symbol 0被拒绝的 classes是 \(x_0=0\) 且 \(x_1=0,1,2\)；按 multinomial weights
求和得到

\[
\frac{2^c+1+c}{3^{c+1}}.
\]

symbol 1对称。三项合并并注意 pure symbol-2 class的计数重排，化简得式 (11)；
也可直接对 residues \((x_2,x_0\bmod3)\) 求和。式 (12)由
\(a_c=2^c/3^c\) 相减。\(\square\)

前几层为

\[
\begin{array}{c|c|c|c}
c&d_c^{\langle d\rangle}&\rho_c^A&a_c-\rho_c^A\\ \hline
3&9&22/81&2/81\\
4&12&38/243&10/243\\
5&15&64/729&32/729\\
6&18&4/81&28/729.
\end{array}
\tag{13}
\]

### Theorem 4.2（type B）

若 \(d=(3,-2,-1)\)，则

\[
\boxed{
\rho_c^B
=\frac{2^c+2c+5}{3^{c+1}}
\qquad(c\ge3),
}
\tag{14}
\]

以及

\[
\boxed{
a_c-\rho_c^B
=\frac{2^{c+1}-2c-5}{3^{c+1}}.
}
\tag{15}
\]

**证明。** 每个 orbit由

\[
(x_0,x_1,x_2)
\longleftrightarrow
(x_0+3,x_1-2,x_2-1)
\tag{16}
\]

连接。取 unique representative满足 \(x_0<3\) 或 \((x_1<2\text{ or }x_2<1)\)，
再按哪个 coordinate在整个可行 integer interval中恒为零分类。对每类用
multinomial theorem求 word mass：interior orbits接受三个 symbols，boundary
orbits分别贡献 binomial sums；整理得到式 (14)。式 (15)直接相减。
完整有限求和也可写为

\[
\rho_c^B=\frac1{3^{c+1}}
\sum_{C}\sum_{x\in C}\binom c{x_0,x_1,x_2}
\bigl(3-|\cup_{y\in C}\operatorname{supp}(y)|\bigr),
\tag{17}
\]

其中 \(C\) 遍历式 (16)的 integer intervals；两个 endpoint family的有限几何/
binomial sums正好给式 (14)。\(\square\)

前几层为

\[
\begin{array}{c|c|c|c}
c&d_c^{\langle d\rangle}&\rho_c^B&a_c-\rho_c^B\\ \hline
3&9&19/81&5/81\\
4&12&28/243&20/243\\
5&15&13/243&19/243\\
6&18&52/2187&140/2187.
\end{array}
\tag{18}
\]

### Corollary 4.3（type A 严格支配 type B）

两类具有完全相同的 rank-one state counts \(d_c=3c\)，但

\[
\boxed{
\rho_c^A-\rho_c^B
=\frac{2^c-c-2}{3^{c+1}}>0
\qquad(c\ge3).
}
\tag{19}
\]

所以在只比较一个 radius-three relation的 translate consequences时，type B 无法
成为最优 filter；唯一有竞争力的 shortest support type是 pure-to-pure type A。

## 5. \(\mathbb Z_{12},\{0,1,4\}\) 的位置

令 increments按 symbols排列为 \((0,1,4)\in\mathbb Z_{12}\)。其 composition
lattice为

\[
L_{12}=\{d\in A_2:d_1+4d_2\equiv0\pmod{12}\}.
\tag{20}
\]

直接检查 \(r\le3\) 的有限 vectors得

\[
r(L_{12})=3,
\qquad
L_{12}\cap\{r=3\}=\{\pm(3,0,-3)\}.
\tag{21}
\]

所以它唯一命中 type A。第二个独立 closure直到 radius 4出现，例如

\[
(0,4,-4),qquad(3,-4,1)\in L_{12}.
\tag{22}
\]

因此：

- load 3恰等于 type-A rank-one envelope，故
  \(d_3=9,\rho_3=22/81\)；
- load 4起，式 (22)进一步合并 rank-one classes，故不能继续使用
  \(d_c=3c,\rho_c^A\)；
- 精确 finite-index profile变为
  \[
  d=(1,3,6,9,11,12,12,\ldots),
  \tag{23}
  \]
  \[
  \rho=
  \left(1,\frac23,\frac49,\frac{22}{81},
  \frac{31}{243},\frac{31}{729},0,\ldots\right).
  \tag{24}
  \]

例如 load 4 的额外 radius-four closures把 \(d_4\) 从 type-A envelope的 12降到
11，同时 rejection从 \(38/243\) 降到 \(31/243\)。这正展示了 finite completion
的核心 tradeoff：第二 generator节省一个 state，但付出 \(7/243\) rejection。

## 6. Extremality 裁决与下一张有限表

本文件严格证明的是：

1. ternary shortest radius-three support types只有 A、B；
2. 两类 rank-one translate class counts相同；
3. A在每个 \(c\ge3\) 的 rejection严格高于 B；
4. \(\mathbb Z_{12},\{0,1,4\}\) 具有唯一 shortest type A，并由 radius-four
   closure产生其已知近优 profile。

它尚未证明 \(L_{12}\) 在全部 finite-index type-A completions中 extremal。原因是
\(\langle(3,-3,0)\rangle\) rank one、index无限；任何 filter所需 finite-index
completion都必须加入第二个 independent relation。不同 completion可以在不同
layers选择“更多 state、较少 distortion”或“更少 state、较多 distortion”，不能
由 shortest type单独排序。

下一步已经成为有限可认证分类：固定 type A generator，把第二 generator约化到
fundamental strip，按其 radius \(s\) 与 residue class分类。shortest-relation
converse已排除 \(r(L)\ge6\)，所以真正需联合处理的是

\[
r(L)=3,qquad s\in\{4,5\},
\tag{25}
\]

以及具有多个 independent radius-three relations的 finite exceptional cases。对每个
class应列出 loads 3--5 的

\[
(d_c,\rho_c),
\tag{26}
\]

再用 certified Poisson/OGF comparison排除低于 binary baseline。式 (25)的 Smith/
Hermite normal-form residue table，而不是继续无界 modulus浮点枚举，是下一步最
小且有论文价值的工作。
