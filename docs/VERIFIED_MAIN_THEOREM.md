# Verified main theorem: constant-error dynamic fingerprint multisets

This document states the theorem package supported by the accompanying proof
notes and exact verifiers. It is a research proof package rather than a
typeset submission: the named lemmas have been independently attacked and
mechanically checked where indicated, but publication still requires normal
line-by-line peer review. It distinguishes the standard dynamic-filter upper
bound from the matching converse inside the fingerprint-multiset paradigm.

All logarithms are base two unless stated otherwise.

## Model

Fix constants `epsilon in (0,1)` and `c,d>0`.  The universe has size
`n^{O(1)}` and its keys fit in `Theta(log n)`-bit words.  A legal dynamic-set
history has capacity `n`, length at most `n^c`, and is fixed independently of
the initialization seed.

A generalized IID fingerprint filter maps distinct universe keys
independently according to an arbitrary categorical law over tracked
fingerprint cells and finitely many permanent-positive categories. Its normal
internal state maintains the exact multiplicity of every tracked cell. The
external interface is the ordinary key-level `Insert`, `Delete`, and `Query`;
counts are not exposed. The structure may enter one sticky ALL-YES state with
history-wide probability at most `n^{-d}`. The memory is one fixed
preallocated block.

For the converse, light cell probabilities are regular:

\[
\frac an\le p_{n,j}\le\frac An
\]

for constants `0<a<=A<infinity`; finitely many heavy/permanent-positive
categories are allowed.  The key-size-biased load law is

\[
\nu_n=\sum_jp_{n,j}\delta_{np_{n,j}},
\]

with heavy categories represented by the endpoint `infinity`.

## Main theorem

Define

\[
g(\lambda)=1-e^{-\lambda},
\qquad
r(\lambda)=\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda},
\]

and set `g(infinity)=1`, `r(infinity)=0`.

### Theorem

The exact first-order space coefficient within the preceding generalized IID
fingerprint-multiset class is

\[
R_{\rm FM}(\varepsilon)
=\inf_{\nu:\int g\,d\nu\le\varepsilon}
  \int r\,d\nu
=\operatorname{lce}
 \{(g(\lambda),r(\lambda)):0<\lambda\le\infty\}(\varepsilon).
\tag{1}
\]

Let `lambda_*` be the unique zero of

\[
\lambda H'(\lambda)+(\lambda-1)H(\lambda)=0,
\qquad H(\lambda)=H_2(\operatorname{Pois}(\lambda)).
\tag{2}
\]

Then

\[
R_{\rm FM}(\varepsilon)=
\begin{cases}
\displaystyle
\frac{H_2(\operatorname{Pois}(-\ln(1-\varepsilon)))}
{-\ln(1-\varepsilon)},
&0<\varepsilon\le\varepsilon_*,\\[1.2ex]
C_*(1-\varepsilon),
&\varepsilon_*\le\varepsilon<1,
\end{cases}
\tag{3}
\]

where

\[
0.4399316012447<\lambda_*<0.4399316012449,
\]

\[
0.35591952612072764
<\varepsilon_*<
0.35591952612085648,
\]

and

\[
4.4012229659190423
<C_*<
4.4012229659230444
\quad\text{bits}.
\]

Thus uniform fingerprints are optimal below the threshold and strictly
suboptimal above it.  The high-error optimum mixes light cells of load
`lambda_*` with a randomly assigned permanent-positive category.

Moreover, for every fixed `epsilon`, there is an ordinary key-level one-sided
dynamic filter, implemented with the finite-independence two-level hash below,
using

\[
nR_{\rm FM}(\varepsilon)+o(n)
\]

bits, including hash seeds, metadata, fixed slots, and scratch memory.  It has
polylogarithmic worst-case query and update time, pointwise false-positive
probability at most `epsilon`, no false negatives, and history-wide sticky
failure probability at most `n^{-d}`.

The matching converse is within the exact IID fingerprint-multiset class. The
efficient finite-independence construction attains the same coefficient but
is stated as a separate upper bound. The theorem does not claim a matching
lower bound for arbitrary dynamic filters or for all correlated exchangeable
partitions.

## Proof map

1. **Public hash side information and converse.**
   `PUBLIC_HASH_CONDITIONAL_ENTROPY.md` proves the exact identity

   \[
   I(N;h)=H(\operatorname{Mult}(m,p))
          -H(\operatorname{Mult}(m-n,p))
   \]

   and a polynomial-smooth conditional support theorem.  When `m/n->infinity`
   and there are `Theta(n)` regular light cells, the public tape saves only
   `o(n)` bits.  Exact multiplicity recovery therefore forces

   \[
   H\ge H_2(\operatorname{Mult}(n,p))-o(n).
   \]

2. **Occupancy entropy.**  Poissonization/de-Poissonization gives

   \[
   \frac1nH_2(\operatorname{Mult}(n,p))
   =\int r(\lambda)\,d\nu(\lambda)+o(1),
   \]

   while pointwise collision probability converges to

   \[
   \int g(\lambda)\,d\nu(\lambda).
   \]

   Minimization over load laws is the lower convex envelope in (1).

3. **Phase geometry.**  `POISSON_PHASE_TRANSITION_ANALYTIC.md` proves
   `F''>0` on `(0,1]` for `F=e^lambda r` and proves the curve is convex through
   `lambda=0.44`.  `scripts/verify_poisson_root_certificate.py` encloses the root
   below `0.44`.  For `lambda>1`, Poisson entropy is nondecreasing by adding
   independent Poisson noise, so

   \[
   \lambda H'(\lambda)+(\lambda-1)H(\lambda)>0.
   \]

   Hence the root is globally unique and gives the global supporting line to
   `(1,0)`.  This proves (3).

4. **Fixed-slot dynamic coder.**  `FIXED_SLOT_BLOCK_CODER_HOSTILE_AUDIT.md`
   gives an exact integer interval code for conditional multinomial blocks.
   With `b=Theta(log^2 n)`, the total redundancy is `o(n)`, and each block can
   be decoded and re-encoded in polylogarithmic word operations.

5. **Efficient finite-independence hash.**
   `FINITE_INDEPENDENCE_BLOCK_HASHING_LEMMA.md` uses an outer
   `Theta(log n)`-wise hash for block loads and an independent
   `Theta(log^2 n)`-wise inner hash.  Conditional on a nonoverflowing outer
   block, the inner labels are exactly IID uniform.  This preserves the block
   code's multinomial tail, gives a polylogarithmic seed and evaluation time,
   and controls pointwise FPR through Bonferroni truncation.

6. **Priority boundary.** `REVIEWER_HOSTILE_PRIORITY_AUDIT_2026.md` compares
   the theorem against Weighted Bloom Filters, Daisy Bloom Filters,
   ChainedFilter, Pagh--Pagh--Rao, Bercea--Even, adaptive/broom filters, and
   2024--2026 variable/elastic fingerprint structures. No searched work states
   the same exact heterogeneous occupancy coefficient, phase theorem, and
   matching dynamic implementation. The audit is evidence of novelty, not a
   legal guarantee of priority.

## Scope and nonclaims

The theorem applies to polynomial universes, seed-independent polynomial
histories, and ordinary distinct-key dynamic-set semantics. The converse
assumes IID categorical fingerprint assignments; exchangeability alone is
insufficient because labels may have global correlations. It does not cover
seed-adaptive histories, superpolynomial-word universes, state-dependent
rehashing, multiple-choice placement, or arbitrary filters that need not
retain exact fingerprint multiplicities.

It therefore resolves the time-efficient constant-error **fingerprint
multiset upper-bound problem** identified by KLZ25 and proves an exact optimum
inside a broad heterogeneous fingerprint class.  The arbitrary-filter
constant-error lower bound remains open.

## Reproduction

Run

```text
./run_theorem_verifiers.sh
```

to check the finite public-hash identities, exact Bernstein positivity
certificates, rational root enclosure, certified constants, and floating-point
regression values.
