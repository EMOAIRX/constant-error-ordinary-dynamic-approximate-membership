# Bounded source-section influence theorem：hostile audit

> 日期：2026-08-15。审计对象：
> `BOUNDED_SOURCE_SECTION_INFLUENCE_NATURAL_UNIVERSE_LOWER_BOUND_2026_08_15.md`。
> 裁决：endpoint transfer 的 proof interface 闭合；结论是 BSSI 子类在
> `u/n -> infinity` 下满足 `1.434406...n` 下界。SUC-only midpoint结论撤回。

## 1. 首要更正：旧 deficit 对齐失败

旧尝试把 parent union loss用 hidden batch posterior deficit `D_(s,k)` 支付，并写出
一个约 `1.09844` 的 self-consistent fixed point。数值计算没有错，但随机对象错位：

- transport剪枝的是 `G_ell` physical state上 endpoint worlds；
- batch chain rule中的 `D_(s,k)` 描述的是由 `F_r` 暴露的 future hidden batch
  `X_k` posterior；
- `X_k` 在 `G_ell` 历史结束时尚未插入。

普通 KLZ measurability并不给这两个 deficits 的比较。故该 fixed point不能作为
定理，相关草稿已删除。

BSSI proof不使用 posterior deficit。它直接把每个 fresh insertion杀掉的 source
witness-union质量限制为 `O(1)` keys，再 telescoping 为 `O(q)` transport loss。

## 2. BSSI cover 的量词

Cover必须在 cut 时、future labels揭示前固定。若允许看到 `Y_i` 后重选 cover，
Definition 3.1 会变成空条件。因此 theorem显式要求：

1. cover由 cut data、tape、parent state、load与time决定；
2. `F_(i-1)` 可含已经揭示的 insertion labels；
3. `Y_i` 在 (12) 的条件场外；
4. `kappa_b` 对所有 relevant cuts一致，且对 fixed `b` 不随 `n` 增长。

Pointwise版本 (13) 自动满足这些量词。

## 3. Common-suffix operational direction

对 survivor world `S \cap J_q=\varnothing`：

- suffix中的 Insert 不与 parent members冲突；
- suffix中的 Delete 只删除suffix自己更早插入的label；
- load profile与actual execution相同；
- fixed tape determinism保证同 parent state与同 update word到达同 successor state；
- survivor中的原有 key不会被suffix删除。

所以 survivor union包含于 successor operational union。额外 successor witnesses只
扩大 union。方向是

\[
W_C[J_q]\subseteq W^{op}(F_r),
\]

而不是反向 inclusion。

## 4. Rank debit没有 coefficient-one 偷换

证明只使用 set identity

\[
|W(F_r)\setminus W(G_ell)|
=|W(F_r)|-|W(G_ell)|
 +|W(G_ell)\setminus W(F_r)|.
\]

最后一项由 Lemma 4.1 直接以 key cardinality收费。随后它进入
`E|D|/V` 的 first moment，再由 exact batch perspective处理。

没有使用错误命题

\[
m\log\frac w{w-L}
\quad\Longrightarrow\quad
Q\log\frac{d+L}{d}
\]

的 coefficient-one比较。小 profile interval `d` 不会放大一个被隐藏的相对
transport debit；所有 loss在进入 logarithm前已作为 additive candidate mass处理。

## 5. Partition 两阶段条件化

第一条件场不含完整 partition。给定 concrete prefix、tape、state、load与time后，
`W^op(G_ell)` 是 fixed partition-free set；因此可以对未暴露 balanced assignments
平均 `W \cap U_k`。

第二条件场加入完整partition。此时 `U_k` 与 `G=W(G_ell) \cap U_k` 固定，而 hidden
rightmost batch `X_k` 仍在 `U_k` 中均匀无放回。Batch perspective所需的
hypergeometric law只在第二条件场调用。

BSSI cover可以依赖已暴露 partition data，但 removing-partition calculation只使用
它覆盖的 partition-free operational union，不在同一 sigma-field 中既固定又平均
完整 partition。

## 6. Pointwise FPR 的合法调用

对每条 concrete source history `h` 和 fixed current nonmember `x`，先对原 tape `R`
使用

\[
\Pr_R[Query(M_R(h),x)=YES]\le\varepsilon.
\]

由 `W^op(M_R(h)) \subseteq A_R(M_R(h))`，再对source与partition平均，得到 profile
总质量 `g_j<=N`。

证明从未条件于 `(R,state)` 后重用FPR。因此 ALL-YES coin、frozen mask与coordinate
erasure tapes仍被允许。

## 7. 自然宇宙 diagonal choice

对每个 fixed `b`：

- KLZ suffix、horizon与exposure常数 `c_b,c'_b` 有限；
- BSSI常数 `kappa_b` 有限且与 `n` 无关；
- transport loss至多 `kappa_b c_b n`。

因为 `u/n -> infinity` 与 `f(n)/n -> infinity`，可以让 `b(n)->infinity` 足够慢，
同时满足

\[
b4^b\kappa_bc_bn=o(u),
\qquad
4^bc'_bn=o(u),
\qquad
c'_bn=o(f(n)).
\]

这是标准 diagonal argument，不需要给出 `b(n)` 的闭式。若 `kappa_b` 随 `n`
增长，则 theorem不适用，除非直接验证同样的 quantitative `o(u/4^b)` 条件。

## 8. 压力测试

### Exact/canonical state

Operational fiber为singleton时，future legal insertion labels不在该set中，section
不改变family，可取 `kappa_b=0`。定理给出的 `1.4344n` 远低于 exact dictionary
空间，不矛盾。

### Complete fixed-size fiber

若family是 ground set上的全部 `t`-subsets，排除fresh label `y` 后，surviving union
只失去 `y`，故 `kappa_b=1`。该例说明 BSSI不要求posterior thinness或唯一表示。

### ALL-YES branch

若 operational union为整个 universe，但 source cover是section-stable的，BSSI可
成立；该 tape的巨大 accepted support由原联合FPR平均支付。若 union只靠
source-invisible ghosts维持，则 (10) 失败。

### Rare-witness poisoning

一个 common label `y` 可以承载大量 fringe keys的最后 witnesses；排除 `y` 后 union
失去 `Theta(u)` keys。这可以满足 source-union equality，却使 `kappa_b` 无界。
因此它不反驳 theorem，且证明 SUC alone确实不足。

### Cover-and-tombstone / absorbing state

若 non-source operational histories向同 state加入新的union keys，source cover条件
(10)失败。若这些keys已由source worlds覆盖，但依赖少量common tombstone witness，
则 influence条件 (12)失败。BSSI准确排除了两种已知 ghost机制。

### Belief-state arbitrary-history transducer

Ordinary belief-state realization可实现任意family sections。它既能实现
`kappa=1` 的complete fiber，也能实现unbounded-influence avalanche。前者通常使用
巨大state，满足下界；后者落在assumption外。Theorem没有假定普通semantics自动
推出BSSI。

## 9. 最终裁决

以下链条通过审计：

1. source cover在future labels前固定；
2. one-label influence telescopes为linear suffix transport；
3. common suffix把survivor worlds送入同一 operational successor；
4. transport loss以additive candidate mass进入batch perspective；
5. partition与FPR条件化合法；
6. slow-depth diagonal只需 `u/n -> infinity`；
7. endpoint convex/Jensen层沿用已有严格 theorem。

因此可以声明：BSSI ordinary filters在自然宇宙下满足解析 endpoint lower bound
`1.434406361243753...n-o(n)`。不能声明：

- unrestricted ordinary filters都满足BSSI；
- source-union completeness单独足够；
- 旧 `1.09844` fixed point或 `1.30395` midpoint theorem成立。
