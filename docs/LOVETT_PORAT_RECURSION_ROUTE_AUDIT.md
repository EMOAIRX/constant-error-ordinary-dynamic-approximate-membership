# Lovett--Porat recursion route: preliminary hostile audit

Status: research-route assessment, not a new theorem. Source checked directly:
ECCC TR10-087 / FOCS 2010 version of Lovett--Porat, *A lower bound for
dynamic approximate membership data structures*. The 2013 SIAM journal page
confirms the publication metadata but its full text was not available in the
current access session.

All logarithms in the source are base two.

## 1. Model and proved nonrecursive result

The LP structure is an **incremental** approximate-membership data structure:
it supports sequential insertion of at most `n` keys and queries, with no
false negatives and pointwise false-positive probability at most `epsilon`.
It does not assume deletions. Thus every LP lower bound automatically applies
to a fully dynamic filter supporting insertions and deletions, but the proof
uses only the insertion-only API.

Writing

\[
M_D(n,\varepsilon)=\eta n\log_2(1/\varepsilon),
\]

the proved one-cut inequality is LP equation (12): for every `0<c<1`,

\[
(1/\varepsilon)^{\eta}\varepsilon^c
\ge
\left(
  \frac{1-\varepsilon^{\eta/c}}
       {\varepsilon-\varepsilon^{\eta/c}}
\right)^{(1-\varepsilon^{\eta/c})(1-c)}.
\tag{LP12}
\]

The important exponent comes from Claim 8:

\[
\beta=\delta^{1/k}2^{-M/k}
      =\varepsilon^{\eta/c}(1+o(1)),
\qquad k=cn.
\]

The paper proves `eta*(1/2)>=1.1` by substituting `eta=1.1,c=0.7`
and checking that (LP12) fails. It separately reports the numerical
single-cut optimum

\[
\eta^*(1/2)=1.10213\ldots
\]

as an empirical value, not as the formal theorem constant.

## 2. What the recursion paragraph actually says

Section 3.5 of the ECCC/FOCS version contains no full multilevel recurrence,
induction theorem, optimizer, or proof certificate. It says that Claim 8 can
be recursively strengthened by replacing the global memory bound `M` in the
first `k` layers with a lower bound on

\[
M_D(k,\varepsilon),
\]

so that

\[
\beta=\delta^{1/k}2^{-M_D(k,\varepsilon)/k}.
\tag{R}
\]

For an `r`-step recursion it proposes constants

\[
0<c_r<\cdots<c_1<1,
\qquad k_i=c_i n,
\]

and states:

> We performed a computer search for `epsilon=1/2` ... We obtained the bound
> `eta*(1/2)>=1.13`.

Consequently, in the checked source:

- `1.1` is explicitly proved;
- `1.10213...` is an empirical single-cut optimization;
- `1.13` is a computer-search remark for the recursive extension;
- the parameter sequence, finite-depth inequality, rounding margins and
  rigorous certificate for `1.13` are not supplied.

## 3. Natural dynamic-programming formulation

Let `R(t)` denote a certified lower-bound coefficient for filters of capacity
`tn`, normalized per stored key:

\[
M_D(tn,\varepsilon)
\ge tn\log_2(1/\varepsilon)R(t)-o(n).
\]

At a cut `s<t`, equation (R) changes the Claim-8 density from the one-cut
quantity `epsilon^(eta/c)` to

\[
\beta(s)=\varepsilon^{R(s)}.
\]

The covering part then transports this certified prefix density through the
remaining interval. Hence a finite-depth proof can be expressed as a Bellman
feasibility recursion on `(t,R(t))`: select a previous certified scale `s`,
insert `beta=epsilon^{R(s)}` into the LP covering inequality for the interval
`[s,t]`, and retain the strongest resulting lower bound at `t`.

This is a legitimate way to make the LP computer search reproducible. It is
not yet a theorem until the exact rescaled version of Claims 6--16 is written
and proved for every recursive call. In particular, one must preserve the
shared graph layer-size bound, all `delta` losses, and the condition
`beta<alpha`; blindly iterating equation (LP12) is not justified.

## 4. Contribution assessment

The source itself already says recursion improves the bound only slightly and
reports approximately `1.13`. Therefore a paper whose main result is merely:

- formalize the omitted recursion;
- run a better optimizer; and
- certify `C(1/2)>1.1` or approximately `1.13`

would be a rigorous completion of an old computer-search remark, not a new
SODA-level conceptual advance.

Even a small improvement past `1.13` would remain far below the Bloom-filter
coefficient `log_2 e=1.44269...`, and more importantly would not address the
FOCS 2025 constant-error dynamic-filter rate. It would strengthen an
incremental lower-bound constant, but would not exploit deletion and would
not identify the sharp arbitrary-dynamic coefficient.

The route becomes potentially significant only if one proves one of the
following qualitatively stronger statements:

1. solves the infinite-depth Bellman problem in closed form and finds a
   substantially larger coefficient than the reported `1.13`;
2. proves that the entire LP recursive framework has a sharp ceiling, thereby
   explaining structurally why it cannot approach fingerprint bounds; or
3. combines the recursion with a genuinely new dynamic/deletion inequality.

Current verdict: **do not use rigorous certification of the reported `1.13`
as the main SODA route**. It is suitable as a lemma, benchmark, or historical
closure project. Without a new structural inequality, its expected technical
increment and numerical gain are too small.
