# n²/u 碰撞门槛的结构性刻画 + 多割定理融合尝试（负结果存档）

> 2026-08-17。目的：(1) 尝试把 replacement-cover 的 KL-posterior 技巧移植进 multicut
> 1.198 证明，去掉 u/n²→∞ 假设；(2) 精确刻画为什么失败；(3) 排查 PSW FOCS 2013 是否
> 威胁 novelty。结论：融合在唯一一个精确点失败（bank 包含 V_i ⊆ A(q)），且该失败量
> 与 n²/u 同阶、任何证明方法（union bound 或 KL posterior）都无法消除；PSW 无威胁。
> 全部数值结论有脚本复现。

## 1. PSW FOCS 2013 核查（无威胁，且自身也带 n²/u 结构）

原文（arXiv:1304.1188，已存档 `literature/psw.pdf`）Theorem 3.1 的精确量词：

- **宇宙**：$n\le\sqrt{\varepsilon u}$，即 $u\ge n^2/\varepsilon$——PSW 的界本身就
  需要 $u/n^2\to\infty$ 级别的大宇宙；
- **空间计费**：要求"对任意长度 $m\in(\alpha n,n)$ 的插入序列，空间至多
  $\beta m$ 位"——按当前大小计费（compact-prefix 模型），不是 KLZ 的固定最坏 H 位；
  固定 H 位 filter（H=n log(1/ε)+O(n)）对任意 m<n 的空间"人均"是
  H/m = n log(1/ε)/m + o(1)——远超 βm，不构成反例；
- **硬分布**：$S\in U^n$ 有序序列、**允许重复 labels**——同 LP。

结论：PSW 的 (1−o(1))n log(1/ε)+Ω(n log log n) 在三重意义上不适用于 KLZ ordinary
模型（u/n→∞、固定 H 位、fresh-distinct API）。novelty 表新增 PSW 一行（见 ASSESSMENT）。
**附加观察**：四个"超越静态基线"的已知动态下界——LP13、PSW13、multicut 1.198、
all-pivot C_AP——全部要么允许重复 labels、要么需要 u/n²→∞、要么要求 compact-prefix
计费；无一在 u/n→∞ + fresh API + 固定 H 位下成立。这不是巧合，见 §4。

## 2. 融合尝试：multicut + KL-posterior 银行

多割证明（MULTICUT_PREFIX_UNION doc）唯一需要 u/n²→∞ 的地方是 §5 的
fresh-distinct transport：$|L(P_i)\setminus A(W)|$ 的 witness 冲突损失
$O(n^2/u)$。尝试用 replacement-cover 的 per-branch posterior pruning 替换：

**Step 1（KL chain rule 移植成功）**。在割 i 固定状态 z_i，令 μ 为前缀 P_i 的
posterior，Z_{>i} 为后续段。参考律 ν：P_i ~ Unif C(A_{z_i}, k_i)，Z_{>i} 同机制。
两次 chain rule 给

$$
\mathbb E_{Z_{>i}}\,
D\bigl(\mu_{P_i|z_i,Z_{>i}}\,\big\|\,
\operatorname{Unif}\binom{A_{z_i}\setminus Z_{>i}}{k_i}\bigr)
\;\le\; d_{z_i}.
\tag{1}
$$

定义银行 $V_i=V_i(z_i,Z_{>i})$ = 该 posterior 的支撑并。则
$V_i\subseteq A_{z_i}$、$V_i\cap Z_{>i}=\varnothing$，且在好分支
（$X_i\in\varepsilon\pm\tau$、KL≤τ²n）上

$$
v_i/u\;\ge\;(\varepsilon-2\tau)\,2^{-\tau^2/c_i}\;\ge\;\varepsilon-3\tau.
\tag{2}
$$

**Step 2（大银行下界，成功）**。对任意 $\beta<\varepsilon$：

$$
\Pr[v_i/u\le\beta,\,X_i\text{ 好}]
\;\le\;
\frac{\mathbb E d_{z_i}}{k_i\log((\varepsilon-2\tau)/\beta)}
\;\le\;
\frac{\gamma}{1+\gamma-c_i}\cdot\frac{\log(1/\varepsilon)}{\log(1/\varepsilon)}
\;=\;\frac{\gamma}{1+\gamma-c_i},
\tag{3}
$$

其中 $\beta=2^{-h/c_i}$、$h=(1+\gamma)\log(1/\varepsilon)$。对 $c_i$ 有界远离 1
（或 $c_i\le1-\Theta(\gamma)$），该质量为 o(1)/小常数。**即"银行大"可以用 KL 计费
认证，且不需要 u/n²**。数值验证见 `verify_fusion_analysis.py`。

**Step 3（唯一失败点：包含 V_i ⊆ A(q)）**。树界需要 per-node 的容量
$|A(q)\setminus V_i|\le(\alpha-b)u$，等价于 $V_i\subseteq A(q)$。对 $y\in V_i$，
witness p'_y 只保证与 Z_{>i} 不交；若**当前段** z_i 与 p'_y\{y} 相交，p'_y z_i Z_{>i}
非法，无法推出 y∈A(q)。精确损失：

$$
\mathbb E\,|V_i\setminus A(q)|
\;\le\; v_i\cdot\frac{m_i(k_i-1)}{b_i}
\;=\;\Theta(n^2/u)\cdot u.
\tag{4}
$$

无论用 union bound 还是 KL-posterior 论证（(1) 中 posterior 接近 Unif C(b,k_i) 时
witness 必然"铺开"，冲突概率仍是 m_i k_i/b = Θ(n²/u)），该损失同阶。**u=o(n²) 时
包含不可修复。**

**Step 4（两种规避都退化，数值验证）**：
- *银行改为条件在当前段上*：$V_i(z_i,Z_{>i})$——包含成立但段计数自指
  （z_i 的可行域依赖 z_i 自己），无一致 per-node 容量。
- *放弃包含*：per-node 容量变为 $|A(q)\setminus V_i|\le\alpha u$，树界损失从
  $f_\alpha(b)=(1-b)\log_2\frac{1-b}{\alpha-b}$ 退化为
  $g_\alpha(b)=(1-b)\log_2\frac{1-b}{\alpha}$。数值事实：对**所有** h>0 都有
  $\int_0^1 g_{1/2}(2^{-h/c})dc < h$（g 在银行过半质量时取负值），即融合不等式
  $h\ge\int g$ 被平凡满足——**完全空泛**，连 Carter 静态界都不如
  （`verify_fusion_analysis.py` 已验：I_g(0.5)=0.17、I_g(1)=0.49、I_g(h)<h 全区间成立）。
- *replacement-cover 的 reservoir 版本*：shrinkage 是 transition-dependent
  （z_i ⊆ A(s_{i+1})，reservoir C_i 依赖 (s_i,s_{i+1}) 对），路径和
  Σ_{中间状态} 只留下**最后一个**指数因子——多轮退化（round 1 已分析）。

## 3. 结论：融合失败是结构性的

在 u/n→∞ + fresh API + 固定 H 位下，"超越静态基线"的已知证明全部依赖
witness/endpoint 与未来标签的**几何碰撞**，碰撞概率 Θ(n²/u)：

| 证明家族 | 碰撞对象 | 逃逸手段 | 在 u=o(n²) 的结果 |
|---|---|---|---|
| LP13（重复标签） | 硬分布本身允许重复 | 无 | 不适用（模型不同） |
| PSW13 | 压缩论证的 prefix 结构 | 无 | 需 u≥n²/ε + compact-prefix 计费 |
| multicut 1.198 | witness prefix × 后续段 | 无（本笔记尝试的 KL 移植在包含步失败） | 退化到静态界 |
| all-pivot C_AP | 同上（all-pivot 接口） | 无 | 同上 |
| replacement-cover | posterior × 当前分支 (D,I) | **分支条件化（成功）** | (1+2^{-20})n |

replacement-cover 是唯一成功的逃逸：把"银行"条件化在**当前分支**上使 witness 自动
避开插入集，但该结构要求 delete+insert 的 successor 形态，且 reservoir shrinkage 是
transition-dependent——多段/多轮不 telescope。因此该框架的常数封顶在 2^{-Θ(1)}
（round 1 已论证：Markov 约束 τ≥Θ(√γ) × 指数容量）。

**对研究方向的推论**（与仓库 NORMALIZED_DUAL_CONDITIONAL_NOVELTY 的结论一致）：
要把 natural-universe 常数推进到 1.6 级，需要的是：(a) linear-depth recurrent
response（碰撞损失不按 n²/u 单点计费的循环结构）；或 (b) 跨 state 的 transversality
定理；或 (c) 证明碰撞在某个结构化子类中可被"热标签"集中（operational avalanche 的
hot-label 形态，见 OPERATIONAL_SUPPORT_COMPLETION doc 的 fiber 剖面结构）。
这些都不是本笔记解决的——但本笔记把 frontier 精确到了**一个 lemma**：
"bank 包含 V_i ⊆ A(q) 的 Θ(n²/u) 损失不可消除"的严格 barrier 证明，或对该损失的
新计费方式。这将成为论文 Open Problems 节的核心内容，也是下一轮的主攻方向。

## 4. 数值验证脚本

`verify_fusion_analysis.py`：
- (a) multicut 固定点 h\*=1.19811（复现仓库 1.1981007740）；
- (b) 无包含融合：I_g(h)<h 对全部 h>0 成立（g 可负）→ 融合不等式空泛，甚至不产生
  有效固定点；
- (c) KL 计费质量 γ/(1+γ−c_i)：c=0.9,γ=0.05 → 0.33；c=0.95,γ=0.001 → 0.02
  （c→1 退化，需 c_max=1−Θ(γ)）；
- (d) PSW 量词 u ≥ n²/ε。
