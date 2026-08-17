# 主定理定量常数的优化推导（γ^{1/4} → √γ tails）

> 2026-08-17。目的：把 SIMULTANEOUS_REPLACEMENT_COVER_WIDTH 文档 §7 中刻意保守的
> witness 常数 2^{-48} 换成更优的解析 witness。结论：该框架的自洽极限约为
> $H \ge (1+2^{-25})n - o(n)$（≈ 1+3.1e-8），并论证了为什么这个框架本身**不能**给出
> 1+0.1 级别的常数（指数结构封顶），大幅提升必须走 all-pivot 融合路线。

## 1. 假设与异常预算

设 $H \le (1+\gamma)n$。沿用文档记号：$X = a_Z/u$，$d_Z$ 为 posterior deficit，
分支 KL 为 $\mathrm{KL}_{z,D,I} = D(\mu_{K|z,D,I}\|\nu_{K|z,D,I})$。

已证（文档 §7，本评估逐步复算过）：

$$
\mathbb E(X-\tfrac12)^2 \le 2\ln2\,\gamma + o(1), \qquad
\mathbb E d_Z \le \gamma n + o(n), \qquad
\mathbb E_{z}\mathbb E_{D,I}\,\mathrm{KL}_{z,D,I} \le \mathbb E d_Z.
$$

取窗口 $\tau = c\sqrt{\gamma}$（$c$ 待定，与文档的 $\tau=\gamma^{1/4}$ 不同）。Markov/Chebyshev 给异常质量：

- parent $X$：$\Pr[|X-\tfrac12|>\tau] \le \frac{2\ln2\,\gamma}{\tau^2} = \frac{2\ln2}{c^2}+o(1)$；
- successor $X'$：同上，$\frac{2\ln2}{c^2}+o(1)$；
- $\Pr[d_Z>\tau^2 n] \le \frac{\gamma}{\tau^2} = \frac1{c^2}+o(1)$；
- 分支 KL 超阈值质量的期望界同上：$\frac1{c^2}+o(1)$（对 $(z,D,I)$ 联合测度）。

超几何例外（$|I\setminus A|<q/3$）为 $2^{-\Omega(n)}$。
选 $c^2 = 2(4\ln2+2)$ 即 $c\approx3.090$，则异常总质量
$\le (4\ln2+2)/c^2 = 1/2$，good 分支质量 $\ge 1/2 - o(1)$。注意：good 质量只需常数下界，
无需 $1-o(1)$，因为 Fubini 固定 $(r,s,d)$ 后只需常数比例的 good $i$。

## 2. 好分支上的 reservoir

好分支：$a \ge (\tfrac12-\tau)u$，$a' \le (\tfrac12+\tau)u$，分支 KL $\le \tau^2 n$。

$$
b = a - q - |I\cap A| \ge (\tfrac12-\tau)u - n = (\tfrac12-2\tau)u \quad(u/n\to\infty),
$$

$$
v \ge b\,2^{-2\tau^2} \ge (\tfrac12-2\tau-2\tau^2)u \ge (\tfrac12-\tfrac52\tau)u \quad(\tau\to0).
$$

由 $V\subseteq A$ 与 $V\cup i\subseteq A'$：

$$
|C| = |A'\setminus A| \le a'-v \le (\tfrac12+\tau)u-(\tfrac12-\tfrac52\tau)u = \tfrac72\tau u.
$$

## 3. 容量与状态数

$s_0 = \lceil q/3\rceil$，每个 successor state 至多吸收

$$
\binom{|C|}{s_0}\binom{u-s_0}{q-s_0}
\le \Big(\frac{e|C|}{s_0}\Big)^{s_0}\binom uq\frac{(q)_{s_0}}{(u)_{s_0}}
\le \binom uq\Big(\frac{21e\tau}{2}\Big)^{s_0}
$$

（$\frac{e\cdot\frac72\tau u}{q/3} = \frac{21e\tau u}{2q} = \frac{21e\tau}{2}\cdot\frac uq$，再乘 $\frac{(q)_{s_0}}{(u)_{s_0}}\le(q/u)^{s_0}$）。

good insertion sets 数 $\ge (\tfrac12-o(1))\binom{u-n}{q}$，故 distinct successor states

$$
\ge \frac{(\tfrac12-o(1))\binom{u-n}{q}}{\binom uq\,(\frac{21e\tau}2)^{s_0}}
= 2^{-o(n)}\Big(\frac{21e\tau}{2}\Big)^{-q/3}
\qquad\Big(\log_2\tfrac{\binom{u-n}{q}}{\binom uq}=o(n)\Big).
$$

于是

$$
\frac Hn \ge \frac16\log_2\frac{2}{21e\tau} - o(1)
= \frac16\log_2\frac1\tau - \frac16\log_2\frac{21e}{2} - o(1).
$$

## 4. 自洽与结论

代入 $\tau = c\sqrt\gamma$，$c = 3.090$：

$$
\frac Hn \ge \frac1{12}\log_2\frac1\gamma - \frac16\log_2\frac{21e\cdot3.090}{2} - o(1)
= \frac1{12}\log_2\frac1\gamma - 1.077 - o(1).
$$

与假设 $H\le(1+\gamma)n$ 对照：矛盾当且仅当

$$
\frac1{12}\log_2\frac1\gamma - 1.077 - o(1) > 1+\gamma,
$$

即（令 $x=-\log_2\gamma$）$x > 12(2.077+\gamma)$。自洽阈值

$$
\boxed{\gamma^* \approx 2^{-24.92} \approx 3.1\times10^{-8}.}
$$

**结论：主定理可写成**

$$
\boxed{H \ge (1+2^{-25})n - o(n),\qquad u/n\to\infty,\ \varepsilon=1/2,}
$$

比文档的 $2^{-48}$ 强约 $2^{23}$ 倍。进一步微调（更锐的切线下界、超几何精确尾部、
good/异常质量的联合优化、$s_0$ 与 $\tau$ 的联合优化）可以把指数常数从 24.9 再压几个单位，
但**不可能**压到 3 以下（见 §5）。

## 5. 为什么该框架封顶在 2^{-Θ(1)}（重要）

两个结构性约束：

1. 异常质量全部来自 Markov/Chebyshev：$\tau \ge \Theta(\sqrt\gamma)$ 是硬约束
   （$\Pr[|X-1/2|>\tau] \le 2\ln2\gamma/\tau^2$ 与 $\Pr[d_Z>\tau^2n]\le\gamma/\tau^2$）。
2. capacity 对 reservoir 尺寸是**指数依赖**：$(\Theta(\tau))^{q/3}$，来自
   "good insertion set 至少 $q/3$ 个元素落在 $U\setminus A$，且 $i\subseteq A'=A\cup C$"
   的集合包含计数——这是 zero-FN 集合论证的固有指数形态，不是常数可优化的。

因此下界形式必为 $H/n \ge \Theta(\log(1/\gamma))$，自洽解 $\gamma^*=2^{-\Theta(1)}$。
**想要 1.1、1.19 或 1.6 级别常数，必须换机制**（all-pivot hierarchy 的
$C_{\mathrm{AP}}$ 在 $u/n\to\infty$ 下的融合，即仓库 README 的下一步 #1/#3），
或者找到多项式依赖 $\tau$ 的新的信息量计费方式。

## 6. 与文档 §7 的对照（已按 hostile audit 修正）

文档用 $\tau=\gamma^{1/4}$（更保守的异常预算）得到 $\gamma=2^{-48}$ 的 witness。
文档 (7) 的 $-\frac12$ 来自其 §7 的更粗覆盖界
$2^q\cdot(5\tau)^{s_0}$（indep. audit 已逐项验证 (7) 精确成立；注意文档原文是
"any fixed larger constant"，**不是** "3e 可替换为 8"，8<3e 不可行——本推导不依赖该替换）。
本推导用更紧的 overcount 界 $\binom{|C|}{s_0}\binom{u-s_0}{q-s_0}$（无 $2^q$ 因子），
配 $\tau=\Theta(\sqrt\gamma)$，得到 $\gamma=2^{-25}$（α=1/3 版）；
再把 α 优化到 $(1-\varepsilon)(1-\delta_n)$ 后得到 ε=1/2 的 witness
$H\ge(1+2^{-20})n-o(n)$（见 `GENERAL_EPS_EXTENSION.md`，该文件同时给出一般 ε 的
$H\ge(1+2^{-40})n\log_2(1/\varepsilon)-o(n)$）。

## 7. 验证脚本建议

可写一个 `scripts/verify_replacement_cover_constant.py`：
- 用 Fraction 验证 §1 的四个 Markov/Chebyshev 界与 $c=3.090$ 的选择
  （$(4\ln2+2)/c^2 < 1/2$ 的区间证书）；
- 验证 $v\ge b\,2^{-2\tau^2}$ 与 $|C|\le\frac72\tau u$ 的逐步不等式；
- 验证 $\gamma=2^{-25}$ 处的符号：$\frac1{12}\cdot25 - 1.077 > 1+2^{-25}$（矛盾成立），
  而 $\gamma=2^{-23}$ 处 $\frac1{12}\cdot23 - 1.077 < 1+2^{-23}$（无矛盾，取 $o(1)$ 项为 0 的安全形式）。
