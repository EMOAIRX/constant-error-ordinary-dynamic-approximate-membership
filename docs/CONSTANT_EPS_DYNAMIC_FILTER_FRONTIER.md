# Constant-error dynamic filters: a concrete frontier after FOCS 2025

This memo switches the main problem to the open direction stated by Kuszmaul,
Liang, and Zhou, *Fingerprint Filters Are Optimal* (FOCS 2025,
[arXiv:2510.18129](https://arxiv.org/abs/2510.18129)).

## 1. Exact open problem

The FOCS 2025 theorem considers a dynamic filter of capacity `n` over an
arbitrary universe `U`.  It has a fixed `H`-bit memory, free read-only public
randomness, and supports Initialize, Query, Insert, and Delete.  Members are
never false negatives.  For every fixed nonmember `x`, the query returns false
with probability at least `1-epsilon`.  The theorem allows arbitrary update
time and requires only a sequence of `omega(n)` legal updates.

Theorem 1.1 proves, for `epsilon=o(1)` and
`|U|=omega(n/epsilon)`,

\[
H \ge n\log_2(1/\varepsilon)+n\log_2 e-o(n).
\]

Section 6 asks what happens for constant error, `epsilon^{-1}=Theta(1)`.
The authors conjecture that fingerprint filters remain optimal, but point out
that fingerprints now form a random **multiset**, not an almost-collision-free
set.  The multiset must be encoded according to its source distribution, and
both a tight lower bound and a time-efficient matching upper bound are open.

This is a worst-case fixed-memory question, not an expected-space or
high-probability memory question.

## 2. The candidate constant: Poisson occupancy entropy

Let a fingerprint range have

\[
q=\frac n\lambda,
\qquad
\lambda=-\ln(1-\varepsilon).
\]

For a random hash function, the `n` fingerprints have occupancy vector

\[
C=(C_1,\ldots,C_q)\sim\operatorname{Multinomial}
\left(n;\frac1q,\ldots,\frac1q\right).
\]

The nonmember false-positive probability is

\[
1-(1-1/q)^n=\varepsilon+o(1).
\]

The exact occupancy entropy is

\[
H(C)=n\log_2 q-\log_2(n!)
       +q\,\mathbb E\big[\log_2(C_1!)\big],
\]

where `C_1~Binomial(n,1/q)`.  Since `C_1` converges to
`K~Poisson(lambda)`,

\[
\boxed{
\rho(\varepsilon)
=\frac{H_2(\operatorname{Poisson}(\lambda))}{\lambda}
=-\log_2\lambda+\log_2 e
  +\frac{\mathbb E[\log_2(K!)]}{\lambda}
}
\]

is the natural information-theoretic fingerprint rate in bits/key.

Numerically:

\[
\rho(0.1)=4.7412129,\qquad
\rho(0.25)=3.3784979,\qquad
\rho(0.5)=2.2879040.
\]

As `epsilon -> 0`, `lambda~epsilon` and

\[
\rho(\varepsilon)=\log_2(1/\varepsilon)+\log_2e+o(1),
\]

recovering the FOCS 2025 leading expression.

This formula is not stated as a theorem in FOCS 2025; it is the precise
candidate suggested by their phrase “encode the fingerprint multiset based on
the distribution that the multiset comes from.”

## 3. A baseline partial upper bound

There is a clean source-coding baseline.  It is useful for fixing the target
constant and testing definitions, but by itself is probably not a publishable
community contribution.

### Theorem (oblivious polynomial-horizon, non-time-efficient upper bound)

Fix constant `epsilon in (0,1)`, polynomial `T(n)`, and `delta>0`.  For every
oblivious legal operation sequence of at most `T(n)` updates, and for every
current size `k<=n`, there is a randomized one-sided dynamic filter using

\[
\big(\rho(\varepsilon)+\delta\big)n+o(n)
\]

bits, with pointwise false-positive probability at most `epsilon` at every
time, no false negatives, and endpoint state determined only by the current
fingerprint multiset or a single absorbing overflow state.  Updates may take
unbounded computation time.

The statement is deliberately weaker than the FOCS open problem: the update
sequence is oblivious, the horizon is polynomial, and the data structure is not
time-efficient.

### Proof architecture

1. Use a slightly smaller target error `epsilon' < epsilon`, with
   `lambda'=-ln(1-epsilon')` and `q=n/lambda'`.
2. For each current size `k<=n`, let `P_{n,k}` be its multinomial occupancy
   law and define an
   information-spectrum typical set

   \[
   \mathcal T_{n,k}=
   \{c:-\log_2 P_{n,k}(c)\le
          \max_{0\le r\le n}H(P_{n,r})+\delta n/4\}.
   \]

   A sparse Poisson/type argument gives

   \[
   \left|\bigcup_{k=0}^n\mathcal T_{n,k}\right|
   \le(n+1)2^{\max_k H(P_{n,k})+\delta n/4},
   \qquad
   \max_kP_{n,k}(\mathcal T_{n,k}^c)
   \le e^{-\Omega_{\delta,\varepsilon}(n)}.
   \]

   The second estimate is the technical lemma: write the multinomial law as
   a conditioned product of Poisson variables and apply Chernoff bounds to
   `sum_j log(C_j!)`; conditioning on `sum C_j=n` costs only a polynomial
   factor.
3. Enumeratively rank the union of these typical sets into a fixed table.
   Store the rank
   and one overflow bit.  On an update, decode the entire vector, decrement
   one bucket, increment another, and re-encode.  If the new vector leaves
   `T_n`, enter an absorbing `OVERFLOW` state.  In `OVERFLOW`, answer YES to
   every query and remain there.
4. For an oblivious sequence, at any fixed time the occupancy vector is
   multinomial.  The probability of having entered `OVERFLOW` by time `t` is
   at most `t exp(-Omega(n))`, hence still `exp(-Omega(n))` for polynomial `t`.
5. A nonmember query has collision probability at most `epsilon' + o(1)`.  In
   overflow it is always a false positive.  Choosing `epsilon'` a fixed
   distance below `epsilon` absorbs the overflow probability and rounding.

The state count is `|T_n|+1`, so the space is

\[
H(P_n)+o(n)=\rho(\varepsilon')n+o(n).
\]

Letting `epsilon'` approach `epsilon` gives the claimed rate.

## 4. What remains genuinely open

The baseline does not settle the FOCS question for four separate
reasons.

### 4.1 Fixed worst-case memory versus typical entropy

The entropy rate `rho` describes the random occupancy distribution.  A fixed
`H`-bit filter must still define behavior on every public-randomness tape and
every legal update sequence.  The overflow trick spends the error budget and
is harmless only for an oblivious polynomial horizon.  It does not give an
arbitrarily long, adaptive-sequence guarantee.

### 4.2 Dynamic succinct coding

Enumerative ranking gives an upper bound with unbounded update time.  A
time-efficient implementation must support increment/decrement of a sparse
multiset while retaining `rho n+o(n)` worst-case bits.  Standard dynamic
succinct sequences generally add redundancy; showing `o(n)` redundancy for
this growing-alphabet, sparse-count distribution is itself nontrivial.

### 4.3 Adaptive operation sequences

If future keys can depend on previous answers, the current set becomes
correlated with the public hash function.  The multinomial occupancy law no
longer holds conditionally.  Any full theorem must either handle this
adaptivity or state an explicit oblivious-adversary model.

### 4.4 Matching lower bound

Shannon entropy of a proposed fingerprint construction is not a lower bound
for arbitrary dynamic filters.  The FOCS 2025 lower bound uses an
obfuscating-tree/reconstructibility argument that currently relies on sparse
fingerprints and large universes.  Extending it to linear fingerprint
multiplicities is the central lower-bound problem.

## 5. Results that would actually be contributions

The typical-set argument above is likely an implicit/easy baseline behind the
FOCS open question.  The following would be materially stronger.

### Target A: worst-case dynamic distribution-sensitive coding

Construct a filter with fixed

\[
H\le n\rho(\varepsilon)+o(n)
\]

bits that supports an unbounded legal update sequence and does not accumulate
an absorbing overflow probability.  Ideally updates and queries should be
polylogarithmic or constant time.  This requires a tail mechanism that can
continue to support exact multiplicity decrements without retaining the
original keys.

### Target B: a constant-error lower bound for arbitrary filters

Prove

\[
H\ge n\rho(\varepsilon)-o(n)
\]

for arbitrary dynamic filters, or determine a different correct rate.  Merely
retaining all constant terms in the existing KLZ communication proof does not
give this result.  In the large-universe limit that bookkeeping yields only

\[
B_\infty(\varepsilon)
=(1-\varepsilon)\log_2e-log_2\varepsilon-2h_2(\varepsilon),
\]

to be combined with the static lower bound.  At `epsilon=1/2` this dynamic
expression is negative, far below `rho(1/2)=2.287904...`.  The two
`h_2(epsilon)` losses identify where a genuinely new encoding or
reconstructibility argument is needed.

### Target C: sharp separation inside the fingerprint paradigm

For a fixed public hash and exact occupancy representation, every weak
composition of `n` into `q` buckets is possible.  A fixed-length lossless code
therefore costs

\[
w(\varepsilon)n+o(n),\qquad
w=(1+1/\lambda)\log_2(1+\lambda)
   -(1/\lambda)\log_2\lambda,
\]

which is strictly larger than `rho`.  Proving exactly which additional
randomization, overflow repair, or state-dependent hashing reduces `w` to
`rho` would clarify the model and could itself be a useful structural result.

A paper should therefore not lead with:

> typical multinomial fingerprints have entropy `rho(epsilon)n`.

That statement is valuable setup, but it is standard source coding unless it
is upgraded to Target A, B, or C.

## 6. Immediate validation tasks

1. Prove the sparse Poisson information-spectrum lemma with explicit constants.
2. Specify the random-hash model and show pointwise FPR for every fixed key.
3. Formalize the overflow state and prove its probability bound over `T(n)`
   updates.
4. Check whether FOCS's operation-sequence quantifier already permits
   oblivious sequences only; if it requires every sequence independent of the
   tape, state this exactly.
5. Benchmark the rate `rho(epsilon)` against known `O(n)`-redundancy dynamic
   filters; the contribution is only meaningful if the exact constant is new.

## 7. References

- Kuszmaul, Liang, Zhou, *Fingerprint Filters Are Optimal*, FOCS 2025,
  [arXiv:2510.18129](https://arxiv.org/abs/2510.18129).
- Lovett, Porat, *A Space Lower Bound for Dynamic Approximate Membership Data
  Structures*, FOCS 2010 / SICOMP 2013,
  [DOI](https://doi.org/10.1137/100806763).
- Bercea, Even, *A Dynamic Space-Efficient Filter with Constant Time
  Operations*, SWAT 2020, [arXiv:2005.01098](https://arxiv.org/abs/2005.01098).
- Kuszmaul, Walzer, *Space Lower Bounds for Dynamic Filters and Value-Dynamic
  Retrieval*, STOC 2024.
