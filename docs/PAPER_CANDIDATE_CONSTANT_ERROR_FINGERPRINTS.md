# Paper candidate: Nonuniform fingerprints and a constant-error phase transition

## Proposed contribution

Determine the exact linear memory coefficient for **zero-transparent,
exchangeable random-partition fingerprint multisets** under a seed-independent
polynomial update horizon.  The result shows that uniform fingerprints cease
to be optimal at a universal constant error threshold.

The intended safe claim is:

> We determine the exact first-order space of deletion-exact fingerprint
> multiset filters at constant false-positive probability.  Allowing hidden
> heterogeneous fingerprint loads produces a sharp phase transition: uniform
> hashing is optimal below error `0.355919...` and strictly suboptimal above
> it.

This is not a claim about arbitrary dynamic filters and does not resolve the
full FOCS 2025 open problem.

## Model

A seed gives each universe key a static label in `L` or a permanent-positive
label `top`.  The internal multiset core supports:

- `InsertLabel(l)`;
- legal `DeleteLabel(l)` when the current multiplicity is positive;
- exact `Nonempty(l)`.

The implementation may enter an absorbing ALL-YES failure state with
probability at most `n^{-d}` over any legal, seed-independent operation
history of length at most `n^c`.  It has one fixed preallocated memory block.

The exact zero test behavior forces state injectivity for the occupancy
vector: if two vectors differ in coordinate `j`, delete the smaller
multiplicity from both and then call `Nonempty(j)`.

## Main theorem candidate

Let

\[
g(\lambda)=1-e^{-\lambda},
\qquad
r(\lambda)=\frac{H_2(\operatorname{Poi}(\lambda))}{\lambda}.
\]

The optimal bits/key rate is the lower convex envelope of the curve
`(g(lambda),r(lambda))`.  Let `lambda_*` minimize
`e^lambda r(lambda)`.  Then

\[
\lambda_*=0.439931601\ldots,
\qquad
\varepsilon_*=0.355919526\ldots,
\]

and

\[
R^*(\varepsilon)=
\begin{cases}
\dfrac{H_2(\operatorname{Poi}(-\ln(1-\varepsilon)))}
{-\ln(1-\varepsilon)},
&\varepsilon\le\varepsilon_*,\\[1.2ex]
4.401222966\ldots(1-\varepsilon),
&\varepsilon\ge\varepsilon_*.
\end{cases}
\]

At error `1/2`, the optimal generalized fingerprint rate is

\[
2.200611483\ldots
\]

bits/key, whereas uniform fingerprints require

\[
2.287904014\ldots.
\]

The high-error optimum combines light cells of the universal load
`lambda_*` with a randomly placed permanent-positive region.

## Upper-bound proof

1. Choose an exchangeable random partition whose size-biased load law is the
   optimal one- or two-point distribution.
2. For each current set size `k<=n`, construct a polynomial-tail multinomial
   information-spectrum set.
3. Allocate a fixed rank space for the union of these sets and store `k` in
   `O(log n)` bits.
4. Decode, change one occupancy coordinate, and re-rank on an update.
5. Enter absorbing ALL-YES failure outside the encoded set.
6. A union bound over `n^c` endpoints gives total failure `n^{-d}`; reserve an
   `o(1)` portion of the error budget for failure.

This proves the rate information-theoretically but currently has unbounded
update time.

## Lower-bound proof

1. Behavioral injectivity forces every successful state to encode the full
   occupancy vector.
2. Fixed memory with failure `n^{-d}` costs the polynomial-tail smooth max
   entropy of the heterogeneous multinomial source.
3. A triangular-array AEP shows smooth max entropy equals Shannon entropy up
   to `o(n)`.
4. Poissonization and heavy-cell decomposition give
   \[
   H(N)/n=\int r(\lambda)d\nu(\lambda)+o(1),
   \]
   while pointwise FPR implies
   \[
   \int g(\lambda)d\nu(\lambda)\le\varepsilon+o(1).
   \]
5. Minimizing over load laws gives the lower convex envelope.

## Proof status

Completed or reduced rigorously:

- behavioral injectivity;
- exact multinomial entropy identity;
- load-distribution variational formulation;
- upper/lower coding architecture;
- Poisson entropy derivative identities;
- numerical transition constants with reproducible code;
- priority/model audit.

Still required before the theorem can be called proved:

1. heterogeneous multinomial smooth-max AEP with diverging heavy atoms;
2. uniform de-Poissonization;
3. rigorous certification that the Poisson curve has the claimed unique
   supporting tangent.  Current numerics show a large positive margin, but are
   not interval arithmetic.

## Efficient-structure enhancement

Partition the `Theta(n)` light buckets into blocks of
`b=log^3 n`.  Fixed slots with local information-density slack have total
overhead

\[
O\left(n\sqrt{\frac{\log n}{b}}\right)=O(n/\log n).
\]

An update touches one block.  If each block's likelihood-threshold set admits
polylogarithmic membership/rank/unrank, this gives `R^*n+o(n)` bits and
polylogarithmic operations.  The missing construction lemma is an efficient
rank/unrank algorithm for these block typical sets; existing dynamic succinct
bitvectors naturally encode all compositions and do not automatically attain
the smaller distribution-sensitive rate.

## Priority boundary

Must cite and distinguish:

- KLZ, *Fingerprint Filters Are Optimal*, FOCS 2025;
- Pagh--Pagh--Rao and Bercea--Even dynamic multiset/fingerprint dictionaries;
- Weighted Bloom Filters;
- Daisy Bloom Filters, which already uses always-YES classes under externally
  nonuniform input/query distributions;
- adaptive/broom filters;
- dynamic retrieval lower bounds.

Novelty is not “always YES saves space” or “typical sets compress a
multinomial.”  It is the exact exchangeable fingerprint coefficient, the
phase transition, the class-wide converse including arbitrary heterogeneous
and heavy cells, and ideally a dynamic implementation with `o(n)` redundancy.

## Expected venue strength

- information-theoretic theorem with all proof lemmas: plausible ITCS/ESA/
  ICALP contribution, subject to full priority search;
- plus polylog or constant-time exact-rate structure: stronger ICALP/SODA
  candidate;
- plus matching lower bound for arbitrary dynamic filters: resolution of the
  KLZ open problem and potentially FOCS-level.

