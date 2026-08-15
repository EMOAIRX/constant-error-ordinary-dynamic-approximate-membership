# Publishable theorem package: exact-rate random fingerprint multisets

Status: superseded as the compact final statement by
`VERIFIED_MAIN_THEOREM.md`. This file retains the development narrative and
venue discussion.

## 1. Claim boundary

This project does **not** claim a lower bound for arbitrary dynamic
approximate-membership filters. The exact converse is for the random
fingerprint-multiset core that KLZ25 explicitly identifies in its
constant-error open discussion. The upper bound, however, wraps this core in
the ordinary key-level `Insert/Delete/Query` interface and is a standard
one-sided dynamic filter; exact counts are internal and are not exposed to the
user.

The model must expose exact multiplicities, either by requiring the normal
state to represent the tracked occupancy vector or by supporting exact
`CountLabel`.  This avoids the invalid argument that tried to infer
occupancy injectivity from seed-dependent deletion continuations under only
an oblivious-history success guarantee.

## 2. Model

Fix a capacity `n`, a constant error target `epsilon`, and constants `c,d>0`.
A static random fingerprint map sends every distinct universe key
independently to tracked labels `j` with probabilities `p_{n,j}`, or to a
permanent-positive category `top` with probability `beta_n`.

The tracked core maintains the exact vector

\[
N_j=|\{x\in S:h(x)=j\}|.
\]

It supports exact increment, legal decrement, and count/nonempty operations.
The outer filter answers YES on `top` and otherwise tests whether the
corresponding tracked count is positive.

The operation history has length at most `n^c`, contains sets of size at most
`n`, and is fixed independently of the hash seed.  Memory is one fixed
preallocated block.  With probability at most `n^{-d}` over the seed, the
structure may enter a sticky ALL-YES overflow state.  Normal states are exact.

For the converse, the source is the induced random fingerprint multiset (or,
equivalently, a random set independent of the hash seed with the conditional
occupancy entropy made explicit).  The hash tape is public side information;
the lower bound first shows that this side information leaks only `o(n)` bits
about the occupancy source and then applies Fano's inequality.  It is not an
unconditional entropy calculation over the data structure's own coins.

## 3. Variational rate theorem

Define, in bits,

\[
g(\lambda)=1-e^{-\lambda},
\qquad
r(\lambda)=\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda},
\]

with endpoint values `g(infinity)=1` and `r(infinity)=0`.

For regular triangular arrays of tracked probabilities, with light-cell
loads bounded away from zero and infinity and with only an `o(n)`-entropy
heavy part, let the key-size-biased load law converge to `nu`.  Then

\[
\frac1n H(N\mid h)
=\int r(\lambda)\,d\nu(\lambda)+o(1),
\]

while the pointwise false-positive probability is

\[
\int g(\lambda)\,d\nu(\lambda)+o(1).
\]

Consequently the exact first-order optimum within this random-multiset
fingerprint class is

\[
R_{\mathrm{FM}}(\varepsilon)
=\inf_{\nu:
\int g\,d\nu\le \varepsilon}
\int r\,d\nu
=\operatorname{lce}\{(g(\lambda),r(\lambda)):
0<\lambda\le\infty\}(\varepsilon).
\]

The converse ranges over arbitrary regular heterogeneous alphabets, not only
the construction used in the upper bound.

## 4. Phase-transition theorem

Let

\[
\lambda_*=\arg\min_{\lambda>0}
e^\lambda r(\lambda).
\]

The certified small-load convexity, rational root enclosure, and monotonicity
of Poisson entropy beyond unit load imply that the lower convex envelope has
the explicit form

\[
R_{\mathrm{FM}}(\varepsilon)=
\begin{cases}
\displaystyle
\frac{H_2(\operatorname{Pois}(-\ln(1-\varepsilon)))}
{-\ln(1-\varepsilon)},
&0<\varepsilon\le\varepsilon_*,\\[1.2ex]
C_*(1-\varepsilon),
&\varepsilon_*\le\varepsilon<1,
\end{cases}
\]

where

\[
\lambda_*=0.439931601244785\ldots,
\quad
\varepsilon_*=1-e^{-\lambda_*}
=0.355919526120782\ldots,
\]

and

\[
C_*=e^{\lambda_*}r(\lambda_*)
=4.401222965921043\ldots.
\]

Thus uniform fingerprinting is optimal up to error
`0.355919526...` and strictly suboptimal above it.  At error `1/2`,

\[
R_{\mathrm{FM}}(1/2)=2.20061148296\ldots
\]

bits per capacity key, whereas the best uniform-load fingerprint multiset
uses

\[
r(\ln 2)=2.28790401\ldots
\]

bits per key.  The high-error optimum mixes light cells of universal load
`lambda_*` with a random permanent-YES region.

## 5. Efficient dynamic achievability

For the optimizing one- or two-level distribution, split the
`Theta(n)` light cells into blocks of

\[
b=\lceil\log^4 n\rceil.
\]

Conditioned on a block total `s`, its occupancy vector has distribution

\[
\operatorname{Mult}(s;1/b,\ldots,1/b).
\]

Using one arithmetic code for the whole block, a common fixed slot of length

\[
bH_2(\operatorname{Pois}(\lambda))
+O(\sqrt{b\log n}\log b+\log^2 b)
\]

has polynomially small overflow probability.  The information-density tail
follows from bounded differences applied to

\[
-\log P(C)
=s\log b-\log(s!)+\sum_i\log(C_i!).
\]

An exact integer interval code for the conditional multinomial law gives
encode/decode/re-encode in `log^{O(1)} n` word operations using
polylogarithmic scratch space.  The block total and two dyadic guard bits are
stored explicitly, so fixed-slot padding is unambiguous. Summed over all
blocks, the redundancy is

\[
O\!\left(
n\sqrt{\frac{\log n}{b}}\log b
+\frac{n\log b}{b}
\right)=o(n).
\]

With a vanishing FPR margin and a union bound over all block-time pairs, this
yields a fixed-memory dynamic upper bound of

\[
nR_{\mathrm{FM}}(\varepsilon)+o(n)
\]

bits and failure probability at most `n^{-d}` over every seed-independent
history of length `n^c`. For a polynomial-size universe, the two-level
finite-independence construction evaluates the partition and performs each
operation in `log^{O(1)}n` worst-case word operations, using a polylogarithmic
seed included in the advertised space.

## 6. Why this is a paper rather than a calculation

The contribution package is the conjunction of:

1. a class-wide converse for arbitrary regular heterogeneous and heavy
   fingerprint loads;
2. an exact first-order coefficient, rather than an unspecified `O(n)` term;
3. a sharp analytic phase transition showing uniform fingerprints become
   strictly suboptimal;
4. a fixed-preallocated-memory, polylogarithmic dynamic implementation with
   `o(n)` redundancy;
5. a precise boundary explaining why the result does not yet solve the
   arbitrary-filter lower-bound half of KLZ25's open problem.

The nearest literature contains each broad intuition separately: weighted
filters allocate error nonuniformly, Daisy filters permit always-YES classes,
PPR/Bercea--Even maintain fingerprint multiplicities, and KLZ25 predicts that
the constant-error multiset must be source-coded.  The searched literature
does not contain this exact heterogeneous rate theorem, its converse, or the
phase transition.

## 7. Remaining proof obligations before submission

The theorem package is a concrete paper target. The main mathematical and
implementation lemmas now have proof-level writeups; final consolidation and
review are still required before submission.

The efficient outer hash uses the two-level finite-independence construction
in `FINITE_INDEPENDENCE_BLOCK_HASHING_LEMMA.md`: the outer hash controls block
loads, while an independent inner hash is fully independent on every
nonoverflowing block. Thus no random-partition oracle is required for a
polynomial-size universe.

The public-hash converse is proved in
`PUBLIC_HASH_CONDITIONAL_ENTROPY.md`, and the fixed-slot integer coder is
audited in `FIXED_SLOT_BLOCK_CODER_HOSTILE_AUDIT.md`. The local phase geometry
and root have exact certificates, and global uniqueness follows from entropy
monotonicity beyond unit load. The two-level hashing lemma removes the ideal
oracle. In particular,
the earlier zero-transparent continuation argument must not be reused under
an oblivious-history failure guarantee.

## 8. Safe title and venue assessment

Working title:

> **Exact Space and a Constant-Error Phase Transition for Dynamic Random
> Fingerprint Multisets**

With all three obligations completed, this is a credible ESA/ICALP paper and
potentially a SODA submission if the dynamic coding machinery is sufficiently
substantial.  It is not a FOCS-level resolution of the full KLZ25 conjecture
without a matching lower bound for arbitrary dynamic filters.
