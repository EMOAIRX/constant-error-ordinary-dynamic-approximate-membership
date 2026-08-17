# focs-paper：FOCS 论文包

> 基于本仓库 2026-08-17 *simultaneous replacement-cover width* 定理的论文包与
> 常数优化。所有数值声明有可执行验证脚本；所有外部文献均下载原文逐字核对
> （版权原因不收录原文，按 arXiv/ECCC/DOI 编号自行获取）。
> 论文手稿（14 页 LaTeX，含完整主定理证明）按本仓库 `.gitignore` 政策保持本地，
> 需要可另发。

## 结论摘要

- **主定理 witness 常数**：$H\ge(1+2^{-20})n-o(n)$（ε=1/2，u/n→∞），把仓库原
  witness $2^{-48}$ 改进 $2^{28}$ 倍；框架自洽极限封顶在 $2^{-\Theta(1)}$。
- **一般 ε**：对每个固定 ε∈(0,1)，$H\ge(1+2^{-X(\varepsilon)-2})n\log_2(1/\varepsilon)-o(n)$，
  $X(\varepsilon)=\frac{4\log_2(1/\varepsilon)}{1-\varepsilon}+9.755-2\log_2(1-\varepsilon)+\log_2\log_2(1/\varepsilon)$。
- **融合分析（负结果）**：multicut 1.198 的 KL-posterior 移植在唯一一步失败
  （bank 包含 $V_i\subseteq A(q)$ 被当前段碰撞破坏，损失 $\Theta(n^2/u)$ 不可消除；
  放弃包含则不等式空泛）。四个已知"超静态"证明家族共享同一碰撞机制。
- **三份 hostile audit 闭环**：两个源定理 SOUND + 论文 .tex GAPS-FOUND→全部修复。

## 文件

| 文件 | 内容 |
|---|---|
| [GENERAL_EPS_EXTENSION.md](./GENERAL_EPS_EXTENSION.md) | 一般 ε 推广：推导、X(ε) 公式与数值表、δ_n 分段定义、三个待写清的细节 |
| [CONSTANT_OPTIMIZATION_SQRT_TAILS.md](./CONSTANT_OPTIMIZATION_SQRT_TAILS.md) | witness 常数优化：√γ tails、α 参数版覆盖界、$2^{-\Theta(1)}$ 封顶论证 |
| [FUSION_ANALYSIS_AND_PSW_CHECK.md](./FUSION_ANALYSIS_AND_PSW_CHECK.md) | multicut 融合尝试四步记录与失败点精确定位；PSW FOCS 2013 威胁排查 |
| [SUBSAGENT_AUDITS.md](./SUBSAGENT_AUDITS.md) | 三份独立 hostile audit 完整记录（含全部修复项） |
| [ASSESSMENT.md](./ASSESSMENT.md) | FOCS 可发表性评估：novelty 链、风险清单、论文结构、路线图 |
| [verify_replacement_cover_constant.py](./verify_replacement_cover_constant.py) | 主定理全部不等式与常数的机器验证（Fraction 精确算术） |
| [verify_fusion_analysis.py](./verify_fusion_analysis.py) | multicut 不动点、融合空泛性、KL 计费质量、PSW 量词的机器验证 |

## 运行验证

```bash
python3 verify_replacement_cover_constant.py   # ALL PARTS PASS
python3 verify_fusion_analysis.py              # ALL CHECKS PASS
```

## 对仓库文档的三处修正建议（audit 发现，已并入手稿）

1. quantitative 论证的 δ_n 需分段定义：δ(ε)=4（ε≤3/4）/ 4/(1−ε)（ε>3/4）；
   否则与 ε=1/2 witness 的 α=(1/2)(1−4τ) 不一致——按统一的 4τ/(1−ε) 定义时
   witness 值为 0.99716 < 1+2^{-20}，矛盾不成立（分段后 gap 恒正：τ(3−4ε) / 3τ）。
2. 一般 ε 版本中 δ_n 修正项对固定 γ 是 Θ(√γ·log(1/γ)) 而非 o(1)，故常数需
   η_ε=2^{−X(ε)−2}（+2 margin；修正上界在 x=X(ε)+2 处全 ε 最大 0.033）。
3. 主定理使用 deletion（replacement 词），不能声称适用于 incremental filters；
   incremental 的静态分离对应物是 multicut 1.198（只用 insertions）。
