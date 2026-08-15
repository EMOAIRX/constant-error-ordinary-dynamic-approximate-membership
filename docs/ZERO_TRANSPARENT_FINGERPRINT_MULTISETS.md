# Zero-Transparent Random-Partition Fingerprint Multisets

Status: this development note contains an invalid use of a seed-dependent
label continuation under a seed-independent-history failure guarantee. It is
not an authoritative theorem statement. See `VERIFIED_MAIN_THEOREM.md` for
the repaired exact-multiplicity model.

## 1. Purpose and scope

This note isolates a natural fingerprint-dictionary API for which fingerprint
multiplicity is forced by observable update behavior rather than assumed as
part of the representation.  It gives the appropriate model for a sharp
constant-error source-coding theorem while keeping the boundary with general
dynamic approximate membership explicit.

The model covers the exact multiset core used by single-fingerprint quotient
filters, counting quotient filters, vector quotient filters, and succinct
fingerprint dictionaries that correctly support deletion in the presence of
duplicate fingerprints.  It does not claim to cover arbitrary dynamic
filters, adaptive two-choice placement, state-dependent rehashing, or filters
that intentionally retain false-positive ghosts after the last copy of a
fingerprint has been deleted.

All logarithms are base two.

## 2. The zero-transparent multiset API

Let \(L\) be a finite fingerprint-label space.  A logical multiset is an
occupancy vector

\[
N=(N_\ell)_{\ell\in L}\in\mathbb N^L,
\qquad \|N\|_1\le n.
\]

A **zero-transparent fingerprint multiset** supports the following operations.

1. \(\mathsf{InsertLabel}(\ell)\): replace \(N_\ell\) by \(N_\ell+1\).
2. \(\mathsf{DeleteLabel}(\ell)\): replace \(N_\ell\) by \(N_\ell-1\).  The
   operation is promised to be issued only when \(N_\ell>0\).
3. \(\mathsf{Nonempty}(\ell)\): return YES if \(N_\ell>0\), and NO if
   \(N_\ell=0\).

The zero test is exact.  The interface does not expose a count operation and
does not assume that an occupancy vector can be decoded from memory.

The implementation may be randomized.  As in the public-random-tape model,
fixing the complete tape makes initialization, updates, and queries
deterministic.  A polynomial-horizon high-probability variant may additionally
have an absorbing failure state; all statements about exact behavior below
are conditioned on not entering that state.

### Lemma 2.1 (behavioral occupancy injectivity)

Fix the complete random tape.  Two distinct occupancy vectors reachable
without failure cannot have the same memory state.

#### Proof

Suppose distinct vectors \(N,N'\) shared a state.  Choose a label \(j\) for
which, after exchanging the vectors if necessary,

\[
N_j=a<N'_j.
\]

Apply the same continuation consisting of \(a\) calls to
\(\mathsf{DeleteLabel}(j)\).  Every deletion is legal for both logical
multisets.  Since the starting memory states and operation labels agree, the
resulting memory states also agree.  But \(\mathsf{Nonempty}(j)\) must now
return NO for the first multiset and YES for the second, a contradiction.
\(\square\)

Thus exact recovery of \(N\) is an information-theoretic consequence of the
API.  It is not an additional representation axiom.

### Why ordinary \(\mathsf{DeleteKey}\) is insufficient

For a standard approximate-membership filter, deleting the last true key with
fingerprint \(j\) does not force the current state to answer NO on other keys
with that fingerprint.  They are nonmembers and may remain false positives.
Consequently, the final zero test in Lemma 2.1 can legitimately return YES in
both executions.  Different multiplicities can therefore remain
indistinguishable.  Requiring merely that a deleted key have false-positive
probability at most \(\varepsilon\) on its next query does not repair the
argument: the guarantee is averaged over the random tape, whereas the common
continuation argument operates on each fixed tape.

This is the precise semantic gap between a deletion-exact fingerprint
multiset core and an arbitrary dynamic filter.

## 3. From the core to approximate membership

Let a seed choose a random partition map

\[
h:U\longrightarrow L\cup\{\top\}.
\]

The distinguished label \(\top\) is optional and represents a permanent
positive, or ghost, region.  A key set \(S\) is represented by the multiset

\[
N_\ell=|\{x\in S:h(x)=\ell\}|,
\qquad \ell\in L.
\]

Keys mapped to \(\top\) need not be stored.  The outer approximate-membership
operations are

\[
\begin{aligned}
\mathsf{Insert}(x)&:
  &&h(x)=\top\text{ does nothing; otherwise call }
    \mathsf{InsertLabel}(h(x)),\\
\mathsf{Delete}(x)&:
  &&h(x)=\top\text{ does nothing; otherwise call }
    \mathsf{DeleteLabel}(h(x)),\\
\mathsf{Query}(x)&:
  &&\text{return YES if }h(x)=\top;
    \text{ otherwise return }\mathsf{Nonempty}(h(x)).
\end{aligned}
\]

There are no false negatives.  For a fixed nonmember \(x\), its false-positive
probability is the probability that it lands in \(\top\), or in a tracked
label occupied by at least one current key.

Assume the partition is exchangeable over universe keys.  Write the tracked
cell probabilities as \(p_j\), define their loads \(\lambda_j=np_j\), and use
the key-size-biased empirical law

\[
\nu_n=\sum_j p_j\,\delta_{\lambda_j},
\]

placing the permanent-positive probability mass at \(\lambda=\infty\).
For a uniform random set of \(n\) distinct keys from a sufficiently large
universe, or equivalently under the standard Poissonized calculation, define

\[
g(\lambda)=1-e^{-\lambda},
\qquad
r(\lambda)=\frac{H(\operatorname{Pois}(\lambda))}{\lambda},
\]

with \(g(\infty)=1\) and \(r(\infty)=0\).  Then, up to \(o(1)\),

\[
\text{false-positive probability}
  =\int g(\lambda)\,d\nu_n(\lambda),
\]

and

\[
\frac{1}{n}H(N)
  =\int r(\lambda)\,d\nu_n(\lambda).
\]

The permanent-positive region is therefore the legitimate
\(\lambda=\infty\) endpoint of the nonuniform fingerprint variational
problem, not an unrelated special construction.

## 4. Dynamic probability model

The sharp entropy-rate theorem below uses the common oblivious, finite-horizon
hashing model.

* A legal operation history of length \(T=n^c\) is fixed independently of the
  random partition seed.
* Every true set in the history has size at most \(n\).
* With probability at least \(1-n^{-d}\) over the seed, the data structure
  remains in its normal exact state for the whole history.
* On an atypical occupancy vector it may enter one absorbing failure state
  that answers YES to every query.  This preserves the no-false-negative
  guarantee.  Its contribution to pointwise false-positive probability is at
  most the failure probability.

This model matches the standard high-probability analysis of randomized hash
structures against a seed-independent operation sequence.  It is strictly
weaker than a fixed-memory guarantee for every history after the tape has been
revealed.  An unbounded adversary can enumerate sets concentrated outside a
random ghost region, so the theorem must not be advertised as a result in the
stronger arbitrary-history model.

## 5. Sharp first-order rate

Let \(R_{\rm ZT}(\varepsilon)\) denote the optimal first-order number of memory
bits per capacity key for zero-transparent random-partition fingerprint
multisets in the preceding model.  Equivalently, the memory is allowed
\(nR+o(n)\) bits, polynomially small failure probability, and pointwise false
positive probability \(\varepsilon+o(1)\).

### Theorem 5.1 (zero-transparent random-partition fingerprint theorem)

\[
R_{\rm ZT}(\varepsilon)
=\operatorname{lce}\bigl\{(g(\lambda),r(\lambda)):
       0<\lambda\le\infty\bigr\}(\varepsilon),
\]

where \(\operatorname{lce}\) denotes the lower convex envelope as a function
of the first coordinate.  More explicitly, let \(\lambda_*\) be the unique
minimizer of

\[
e^\lambda r(\lambda).
\]

Numerically,

\[
\lambda_*=0.439931601\ldots,
\qquad
\varepsilon_*=g(\lambda_*)=0.355919526\ldots,
\]

and

\[
C_*=e^{\lambda_*}r(\lambda_*)
   =4.401222966\ldots.
\]

Consequently,

\[
R_{\rm ZT}(\varepsilon)=
\begin{cases}
\displaystyle
\frac{H(\operatorname{Pois}(-\ln(1-\varepsilon)))}
     {-\ln(1-\varepsilon)},
&0<\varepsilon\le\varepsilon_*,\\[1.25em]
C_*(1-\varepsilon),
&\varepsilon_*\le\varepsilon<1.
\end{cases}
\]

The high-error branch mixes light cells of load \(\lambda_*\) with a
permanent-positive region.  Its size-biased mass on the light component is

\[
\alpha=\frac{1-\varepsilon}{1-\varepsilon_*};
\]

the remaining mass \(1-\alpha\) is placed at \(\lambda=\infty\).

### Proof architecture

The proof reduces to four lemmas.

1. **Behavioral injectivity.** Lemma 2.1 makes every successful state an
   injective encoding of its occupancy vector.
2. **Smooth multinomial source coding.** For an occupancy vector
   \(N\sim\operatorname{Mult}(n;p_1,p_2,\ldots)\), the logarithm of the
   smallest set carrying probability \(1-n^{-d}\) is
   \(H(N)+o(n)\).  This is the polynomial-tail smooth max-entropy statement
   needed for fixed-length, high-probability storage.
3. **Poissonized entropy formula.** If the size-biased load laws converge to
   \(\nu\), then
   \[
   H(N)/n=\int r\,d\nu+o(1),
   \qquad
   \operatorname{FPR}=\int g\,d\nu+o(1).
   \]
   Loads tending to infinity contribute zero entropy per key and unit
   false-positive probability, yielding the endpoint \((1,0)\).
4. **One-dimensional variational problem.** Minimizing \(\int r\,d\nu\)
   subject to \(\int g\,d\nu\le\varepsilon\) gives the lower convex envelope.
   The supporting line from \((g(\lambda_*),r(\lambda_*))\) to \((1,0)\)
   obeys
   \[
   \frac{dr}{dg}(\lambda_*)
   =-\frac{r(\lambda_*)}{1-g(\lambda_*)},
   \]
   equivalently \((e^\lambda r(\lambda))'|_{\lambda_*}=0\).

For achievability, choose a partition with the optimizing one- or two-point
load law and encode only a polynomial-tail typical set of occupancy vectors.
Decode, change one coordinate, and re-encode on each update.  If the result is
outside the typical set, enter the absorbing all-YES state.  A union bound over
the \(n^c\) seed-independent states in the history gives the desired total
failure probability.  The construction is information-theoretic and makes no
claim about update time.

## 6. Priority and positioning

The appropriate conceptual predecessor is the dynamic multiset dictionary
underlying fingerprint filters, rather than arbitrary approximate-membership
filters.  The result would show that, at constant error, the optimal
fingerprint distribution need not be uniform: above \(\varepsilon_*\), an
information-theoretically optimal zero-transparent multiset uses a randomized
permanent-positive region and light cells at a universal load.

Before making a novelty claim, the following literature must be audited for
nonuniform fingerprints and deliberate permanent positives:

* Carter et al. and Pagh--Pagh--Rao fingerprint dictionaries;
* quotient, counting quotient, and vector quotient filters;
* constant-error upper bounds discussed in *Fingerprint Filters Are Optimal*;
* average-case and distribution-sensitive Bloom/filter constructions.

The theorem should not be described as resolving the general constant-error
dynamic-filter problem.  If the variational phase transition is new and the
smooth-entropy proof is completed, the result is plausibly appropriate for an
ITCS/ICALP/ESA-level paper.  A FOCS/STOC-level claim would require extending
the lower bound to adaptive multiple-choice placement, state-dependent
rehashing, or arbitrary dynamic filters.
