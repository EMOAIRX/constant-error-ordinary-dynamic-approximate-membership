# Nonuniform fingerprints at constant error: candidate paper theorem

Status: theorem candidate under active priority and model audit.  The
variational calculation below is rigorous in the Poissonized source-coding
model.  It is not yet a fixed-worst-case dynamic-filter upper bound or an
arbitrary-filter lower bound.

Priority caveat: permanent-YES allocation is conceptually adjacent to Weighted
Bloom Filters and, especially, Daisy Bloom Filters.  Those works exploit an
externally nonuniform input/query distribution and generally optimize an
average query error.  The proposed model instead randomizes the heterogeneous
partition so that all universe elements remain exchangeable and each fixed
nonmember has the same pointwise-over-randomness error.  The phase-transition
idea alone is nevertheless too close to standard convexification to be a full
paper; the dynamic exact-constant implementation and converse are essential.

## 1. Why uniform fingerprints may be the wrong conjecture

The most literal constant-error extrapolation of FOCS 2025 chooses a uniform
fingerprint range of size `q=n/lambda`, with

\[
\lambda=-\ln(1-\varepsilon),
\]

and predicts the multinomial occupancy entropy rate

\[
r(\lambda)=\frac{H_2(\operatorname{Poi}(\lambda))}{\lambda}.
\]

At constant error there is no information-theoretic reason that fingerprint
buckets must have equal probabilities.  A randomly permuted heterogeneous
alphabet preserves the same marginal distribution for every universe key and
therefore preserves the pointwise-over-randomness error semantics.

Let bucket `j` have probability

\[
p_j=\lambda_j/n,
\qquad \sum_j\lambda_j=n.
\]

Under Poissonization its occupancy is `Poi(lambda_j)`.  Define the size-biased
load random variable

\[
\Pr[\Lambda=\lambda_j]=\lambda_j/n.
\]

Then the source entropy per stored key and false-positive probability are

\[
R=\mathbb E[r(\Lambda)],
\qquad
\varepsilon=\mathbb E[g(\Lambda)],
\qquad
g(\lambda)=1-e^{-\lambda}.
\]

Consequently the optimal fingerprint-source rate is the lower convex envelope
of the parametric curve

\[
\lambda\mapsto(g(\lambda),r(\lambda)).
\]

## 2. Phase-transition theorem

Let `lambda_*` be the unique minimizer of

\[
e^\lambda r(\lambda).
\]

Numerically,

\[
\lambda_*=0.439931619\ldots,
\qquad
\varepsilon_*=1-e^{-\lambda_*}
=0.355919538\ldots,
\]

and

\[
C_*=e^{\lambda_*}r(\lambda_*)
=4.401222966\ldots.
\]

The convex-envelope calculation gives

\[
\boxed{
R_{\rm fp}(\varepsilon)=
\begin{cases}
r(-\ln(1-\varepsilon)),&0<\varepsilon\le\varepsilon_*,\\[4pt]
C_*(1-\varepsilon),&\varepsilon_*\le\varepsilon<1.
\end{cases}}
\]

Below the threshold, uniform fingerprints are source-coding optimal.  Above
the threshold, the optimal distribution mixes:

- load `lambda_*`, carrying size-biased key mass
  \[
  \alpha=\frac{1-\varepsilon}{1-\varepsilon_*};
  \]
- a load tending to infinity, carrying the remaining mass and contributing
  asymptotically one unit of false-positive probability but zero entropy per
  stored key.

Equivalently, the high-error optimum combines an efficiently encoded residual
fingerprint multiset at the universal load `lambda_*` with a randomly placed
near-universal YES/ghost component.

At `epsilon=1/2`,

\[
R_{\rm fp}(1/2)=2.200611483\ldots,
\]

strictly below the uniform prediction

\[
r(\ln2)=2.287904014\ldots.
\]

Thus the natural “uniform Poisson multiset” constant is not even optimal
inside the unrestricted fingerprint source-coding paradigm.

## 3. Proof obligations

The paper-level theorem requires analytic, rather than merely numerical,
verification of the following facts:

1. The curve `r` as a function of `g` is convex up to `lambda_*`.
2. The line from `(g(lambda_*),r(lambda_*))` to `(1,0)` supports the entire
   remaining curve.
3. `e^lambda r(lambda)` has a unique minimizer.
4. Finite alphabets with a large but finite load approximate the endpoint
   `(1,0)` with `o(1)` rate loss.
5. Exact multinomial entropy converges uniformly to the Poissonized objective,
   including heterogeneous loads and the large-load component.

The tangency condition is

\[
\frac{d r/d\lambda}{d g/d\lambda}(\lambda_*)
=-\frac{r(\lambda_*)}{1-g(\lambda_*)},
\]

equivalently

\[
\frac d{d\lambda}\left(e^\lambda r(\lambda)\right)
\bigg|_{\lambda=\lambda_*}=0.
\]

## 4. What this does and does not solve

### It would establish

- the exact distributional source-coding optimum among exchangeable
  fingerprint alphabets;
- a sharp phase transition at `epsilon_*`;
- strict suboptimality of uniform hashing at sufficiently large constant
  error;
- a corrected candidate benchmark for the FOCS 2025 constant-error problem.

### It would not yet establish

- a fixed-worst-case `H`-bit dynamic filter at rate `R_fp`;
- time-efficient increment/decrement coding;
- resilience to arbitrary sets correlated with the public random tape;
- a lower bound for arbitrary, non-fingerprint dynamic filters.

The high-load component is particularly delicate.  With a randomly placed
ghost region, every fixed nonmember has the correct marginal error, but a
worst-case set for a realized public tape may avoid that region and put more
than the expected number of keys in the residual component.  This prevents a
direct conversion of source entropy into fixed worst-case memory.

## 5. Potential paper package

A source-coding phase transition alone may be considered too close to a
one-dimensional convexification unless it is packaged with at least one of:

1. a matching fixed-memory upper bound for oblivious polynomial-horizon
   dynamic filters, with an exact optimality theorem in that model;
2. a lower bound showing that every exchangeable fingerprint scheme has rate
   at least `R_fp`, including arbitrary heterogeneous alphabets and codes;
3. a separation theorem between distributional/oblivious space `R_fp` and
   self-contained exact-fingerprint worst-case space `w`;
4. an online balanced-ghost construction that realizes the high-error branch
   under fixed memory, which would directly change the FOCS 2025 candidate
   upper bound.

The most plausible complete first paper is (1)+(2): define a standard
oblivious-source dynamic-filter model, derive its exact optimal fingerprint
rate, and show a phase transition missed by uniform hashing.  Priority and
community relevance of that model still require adversarial review.

## 6. Stronger fixed-memory finite-horizon variant

A more data-structural model avoids average code length while retaining the
standard hash-independence assumption used by many randomized dictionaries:

- the legal operation sequence is fixed independently of the public seed;
- the horizon is `T=n^O(1)`;
- the structure has a fixed state budget and succeeds with probability
  `1-n^{-Omega(1)}` over its seed;
- conditional on success, the light fingerprint multiset is represented
  exactly and supports deletion.

For a uniform residual load `lambda`, exact fixed-length composition coding
costs

\[
w(\lambda)=
\frac{1+\lambda}{\lambda}\log_2(1+\lambda)-\log_2\lambda
\]

bits per residual key.  A random permanent-YES region absorbs key mass
`1-alpha`; the residual region stores at most
`alpha n+O(sqrt(n log n))` current keys simultaneously over the polynomial
horizon, by a union bound over binomial concentration.  The error constraint
is

\[
\varepsilon=(1-\alpha)+\alpha(1-e^{-\lambda}),
\qquad
\alpha=(1-\varepsilon)e^\lambda.
\]

Thus the achievable fixed-state rate is

\[
(1-\varepsilon)e^\lambda w(\lambda).
\]

Let

\[
\lambda_{\rm wc}
=\arg\min_{\lambda>0}e^\lambda w(\lambda)
=0.402298543\ldots,
\]

\[
\varepsilon_{\rm wc}=1-e^{-\lambda_{\rm wc}}
=0.331218944\ldots,
\qquad
C_{\rm wc}=e^{\lambda_{\rm wc}}w(\lambda_{\rm wc})
=4.506663790\ldots.
\]

The candidate exact-fingerprint rate becomes

\[
R_{\rm fp}^{\rm poly-whp}(\varepsilon)=
\begin{cases}
w(-\ln(1-\varepsilon)),&\varepsilon\le\varepsilon_{\rm wc},\\
C_{\rm wc}(1-\varepsilon),&\varepsilon\ge\varepsilon_{\rm wc}.
\end{cases}
\]

At `epsilon=1/2` this gives

\[
R_{\rm fp}^{\rm poly-whp}(1/2)=2.253331895\ldots,
\]

compared with `2.384499842...` for uniform exact fingerprints.

This theorem would be stronger than the Shannon phase transition: it gives a
fixed memory layout and exact deletion semantics over a polynomial operation
horizon.  The matching upper uses:

1. a randomly permuted heavy/ghost region;
2. a Chernoff-sized residual capacity valid at every endpoint;
3. stars-and-bars rank/unrank, or a succinct dynamic bitvector, for residual
   occupancies;
4. an explicit failure state on the negligible seed event.

A full converse must show that every heterogeneous exact-fingerprint scheme in
this model pays the lower convex envelope of `(g(lambda),w(lambda))`, including
the capacity quantile required by the high-probability guarantee.  This is the
most concrete current candidate for a complete upper/lower paper theorem.

## 7. Correct paper theorem after adversarial audit

The preceding `w`-rate paragraph applies only if the representation is required
to accommodate every residual composition.  In the standard polynomial-horizon
`whp` model, a fixed-size state space may instead encode only a sufficiently
high-probability information-spectrum set and enter an absorbing failure state
outside it.  Therefore the sharp first-order rate in the audited model is the
Shannon-envelope rate `R_fp`, not `w`.

### Audited model

A **static-seed random-partition, deletion-exact fingerprint filter** has:

1. one seed that assigns every universe element to a fingerprint cell or an
   always-YES cell;
2. a seed-independent legal operation history of length at most `n^c`;
3. on normal states, lossless recoverability of the tracked-cell occupancy
   vector, so Insert/Delete perform exact `+1/-1` changes;
4. query YES exactly for a nonempty tracked cell or the always-YES cell;
5. a fixed preallocated state space and an absorbing ALL-YES failure state;
6. failure probability at most `n^{-d}` for every such history.

This is a natural abstraction of single-hash fingerprint/counting/quotient
filters and random-multiset dictionaries.  It does not contain arbitrary
cuckoo placement, state-dependent rehashing, support-only ghost filters, or
general dynamic filters.

### Main theorem candidate

For every constant `epsilon in (0,1)` and constants `c,d>0`, the optimal
first-order fixed-memory rate in this class is

\[
\boxed{R_{\rm fp}(\varepsilon)}
\]

from Section 2.  More explicitly,

\[
R_{\rm fp}(\varepsilon)=
\begin{cases}
H_2(\operatorname{Poi}(-\ln(1-\varepsilon)))
/[-\ln(1-\varepsilon)],&\varepsilon\le0.355919538\ldots,\\
4.401222966\ldots(1-\varepsilon),&\varepsilon\ge0.355919538\ldots.
\end{cases}
\]

The upper bound uses heterogeneous hashing, high-probability multinomial
typical sets for every current size, fixed-length ranking, and sticky failure.
The lower bound uses a uniform random current set, smooth max entropy of the
multinomial occupancy vector, Poissonization, a decomposition into bounded and
diverging-load cells, and the convex-envelope variational problem.

The theorem gives the strict uniform-hashing separation

\[
R_{\rm fp}(1/2)=2.200611483\ldots
<2.287904014\ldots.
\]

### Remaining proof lemmas

The theorem skeleton is complete, but a paper proof must still supply:

1. a triangular-array smooth-max-entropy/AEP lemma for heterogeneous
   multinomial occupancies with polynomially small discarded mass;
2. uniform de-Poissonization and treatment of diverging heavy cells;
3. an analytic or computer-assisted proof that the lower convex hull has the
   claimed single transition and unique tangent.

These are technical proof obligations, not unresolved conceptual steps.

### Efficiency status

The rank/decode/update/rerank construction is information-theoretic and may
take superpolynomial time.  Existing dynamic compressed bitvectors naturally
achieve all-composition entropy `w`, not the smaller distribution-sensitive
typical-set rate.  Achieving `R_fp n+o(n)` bits with polylogarithmic or constant
operations requires a new dynamic typical-set coder.  Adding such a structure
would substantially strengthen the paper.

### Safe contribution claim

> We determine the exact linear space coefficient for deletion-exact,
> exchangeable random-partition fingerprint filters at constant error.
> Heterogeneous hidden loads cause a sharp phase transition, and uniform
> fingerprints cease to be optimal above error `0.355919...`.

Do not claim that this resolves the FOCS 2025 open problem for arbitrary
dynamic filters.
