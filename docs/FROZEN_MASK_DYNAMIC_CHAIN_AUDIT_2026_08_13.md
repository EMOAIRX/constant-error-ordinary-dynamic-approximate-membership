# Frozen-mask exact-residual chains for dynamic AMQ

> Status (2026-08-13): rigorous no-gain theorem for public, key-routed frozen
> chains with exact multiplicity residuals; rigorous state-count identity for
> recursive unary collision layers; explicit deletion obstruction for
> state-dependent approximate residual routing.  This does not rule out
> arbitrary history-dependent dynamic filters.

The target is an ordinary one-sided dynamic filter with capacity \(n\),
arbitrary-length legal histories, fixed memory, zero overflow/failure, and
pointwise false-positive probability \(1/2\).  The global key universe obeys
\(|U|/n\to\infty\).

## 1. The tempting but invalid bit-vector calculation

Choose a public tracked mask of density \(\theta\), hash tracked keys to
\(q=cn\) cells, and store one occupancy bit per cell.  A fixed nonmember is
rejected with asymptotic probability

\[
\delta=\theta e^{-\theta/c}.
\tag{1}
\]

If these bits supported deletion, minimizing \(c\) subject to
\(\delta=1/2\) would give \(\theta=1\),

\[
c=\frac1{\ln2}=1.442695\ldots,
\tag{2}
\]

apparently beating both \(2.200611\) and \(2.349083\) bits per key.

This is not a dynamic filter.  If two live keys hash to the same occupied
cell, deleting either one cannot clear the bit.  A one-bit cell does not tell
whether another colliding key remains.  Clearing it produces a false negative;
retaining it after the last copy is deleted creates a ghost and loses the
claimed exact-residual semantics.

Thus the correct exact residual is a multiplicity, not a bit.

## 2. Key-routed recursive chains collapse to one alphabet

Let public frozen masks route every key, independently of the current state,
to one of tracked types \(i=1,\ldots,L\), or to a permanent-YES type.  Write
the routing mass as \(\theta_i\).  Type \(i\) hashes into

\[
q_i=c_i n
\]

labels and maintains every label multiplicity exactly.  Define

\[
\lambda_i=\frac{\theta_i}{c_i}.
\]

A fixed nonmember is rejected exactly when it is routed to a tracked type and
its label is empty.  Hence

\[
\delta
=\sum_i\theta_i e^{-\lambda_i}+o(1)
=\sum_i c_i\lambda_i e^{-\lambda_i}+o(1),
\tag{3}
\]

with

\[
\sum_i c_i\lambda_i=\sum_i\theta_i\le1.
\tag{4}
\]

Let

\[
c=\sum_i c_i,
\qquad
Q=\sum_iq_i=cn.
\]

Use balanced public routing inside each type.  Since \(|U|/n\to\infty\), the
smallest positive label-fiber capacity \(L_n\) tends to infinity (for every
fixed positive-mass type).  Reachable occupancies are weak compositions with
the additional coordinate caps \(N_j\le L_n\).  These caps do not change the
linear exponent.  One way to see this is to fix a constant cap \(K\), count
coefficients of

\[
(1+z+\cdots+z^K)^Q,
\]

take \(n\to\infty\), and then let \(K\to\infty\); the saddle converges
monotonically to that of \((1-z)^{-Q}\).  Consequently fixed zero-failure
memory has at least

\[
\binom{n+Q}{Q}\,2^{-o(n)}
\tag{5}
\]

states at the exponential scale.  With uncapped formal labels, the exact count
is \(\binom{n+Q}{Q}\); fixing cardinality exactly \(n\) gives
\(\binom{n+Q-1}{Q-1}\).  All these variants have the same linear exponent

\[
\Phi(c)
=(1+c)\log_2(1+c)-c\log_2c.
\tag{6}
\]

The routing types and recursion depth disappear from (5): jointly, they are
just one disjoint fingerprint alphabet of size \(Q\).

### Theorem 2.1 (half-error rate of exact frozen chains)

Every regular type-uniform public key-routed frozen chain described above,
with exact multiplicity residuals and rejection at least \(1/2-o(1)\), has

\[
c\ge\frac1{\ln2}
\]

and hence uses at least

\[
\boxed{
\Phi(1/\ln2)n-o(n)
=2.384499842479\ldots n-o(n)
}
\tag{7}
\]

bits.  Equality is attained in the class by one unmasked uniform type.

#### Proof

For fixed total cell density \(c\), maximize (3) under (4).  If \(c\ge1\),
the average load (including zero-load cells) is at most \(\mu=1/c\le1\).
For every \(a\in(0,1]\), the tangent to
\(f(\lambda)=\lambda e^{-\lambda}\) at \(a\) is a global upper bound on
\(f\).  Indeed, concavity proves this on \([0,2]\); beyond 2 the tangent is
nondecreasing while \(f\) is already decreasing.  Applying the tangent at
the actual average and then using that \(f\) is increasing on \([0,1]\)
gives

\[
\delta\le e^{-1/c},
\tag{8}
\]

with equality at total tracked mass one and uniform load \(1/c\).  If
\(c\le1\), the global supporting line \(f(\lambda)\le1/e\) per cell gives

\[
\delta\le c/e<1/2.
\tag{9}
\]

Thus half rejection forces \(c\ge1/\ln2>1\).  Substitute this in the strictly
increasing state exponent (6).  The uniform unmasked construction attains
both (8) and the weak-composition count.  \(\square\)

The same argument allows heterogeneous masks, different finite residual
universe sizes, and arbitrarily many public routing levels.  They cannot reach
\(2.200611\), let alone beat it.

## 3. Recursive collision bit-vectors give the same count exactly

There is another natural chain representation.  For an occupancy vector
\(N=(N_1,\ldots,N_Q)\), let

\[
B_k=\{j:N_j\ge k\},\qquad k\ge1.
\tag{10}
\]

Then

\[
B_1\supseteq B_2\supseteq\cdots,
\qquad
\sum_{k\ge1}|B_k|=\sum_jN_j\le n.
\]

The first layer is an occupancy bit-vector, the second records duplicate
copies, and so on.  Insert/delete flips the first zero/last one in the column.
This is a valid exact recursive residual representation.

But the map

\[
N\longleftrightarrow(B_1,B_2,\ldots)
\tag{11}

is a bijection.  Therefore the number of nested residual chains with total
weight at most \(n\) is exactly

\[
\binom{n+Q}{Q}.
\tag{12}

Any apparent saving obtained by separately coding sparse higher layers must
be offset by the layer-size/profile information.  The conditional binomial
chain rule telescopes to the same stars-and-bars exponent.  Recursive exact
residuals reorganize multiplicity information; they do not remove it.

## 4. Why a large-universe exact residual cannot be a finite bit-vector

A balanced public mask \(C\subseteq U\) of density \(\theta\) supports the
simple exact filter storing \(S\cap C\).  In a dense universe such as
\(|U|=2n\), this gives the familiar \(n\)-bit half-error construction.

For \(|U|/n\to\infty\), however, a literal characteristic vector costs

\[
|C|=\Theta(|U|)
\]

bits.  A worst-case exact dictionary for up to \(n\) elements of \(C\) costs

\[
\log_2\binom{|C|}{n}
=n\log_2(|U|/n)+O(n),
\tag{13}

not \(O(n)\).

Hashing \(C\) to \(\Theta(n)\) residual coordinates restores linear space but
also restores collisions.  A bit-vector then ceases to support correct
deletion; exact counts return to Theorem 2.1.

## 5. The state-dependent routing obstruction

One may try to store one implicit representative per occupied first-level
cell and route only colliding keys to a second residual dictionary.  This can
work statically because the complete set is available during construction.
For ordinary dynamic deletion it creates a sharp interface problem.

Suppose deletion of key \(x\) tests whether \(x\) is present in the residual
dictionary:

* if YES, delete it from the residual;
* otherwise, regard it as the implicit representative and promote another
  colliding key.

If the residual dictionary is approximate, a false positive on the implicit
representative sends the deletion down the wrong branch.  It removes residual
state that did not represent \(x\), or fails to promote a remaining key.  A
later query can then be a false negative.  One-sided query error does not
permit one-sided update-routing error.

Making the residual exact avoids the wrong branch but requires storing actual
large-universe identities.  In a random constant-load hash table the number
of excess keys

\[
n-|B_1|
\]

is linear, so (13) again has a superlinear leading term unless those identities
are fingerprinted.  Fingerprinting them recursively recreates the same
update-routing ambiguity.

There are only three generic exits:

1. route every key by public randomness alone, which collapses to Theorem 2.1;
2. maintain exact multiplicities or a reversible algebraic quotient, leading
   back to canonical count/threshold constructions;
3. store placement/history metadata that identifies the chosen level, which
   is a genuinely noncanonical dynamic structure and must be charged.

This is an obstruction to this chain design, not an impossibility theorem for
all ordinary dynamic filters.  Cuckoo relocation, randomized transition
kernels, or globally shared history-dependent states may implement option 3
more efficiently.

## 6. Relation to ChainedFilter

The static chain rule may choose a later residual universe from the false
positives of an earlier state after seeing the complete set.  That residual
universe is state-dependent.  On insertion or deletion, it can change for many
keys, and a compressed AMQ state generally does not determine the true set
needed to rebuild it.

For a deterministic dynamic state \(m\) with logical fiber

\[
\mathcal F(m)=\{S:\text{some legal history for }S\text{ reaches }m\},
\]

every labeled update must choose one common successor for all worlds in
\(\mathcal F(m)\) on which that update is legal.  Static covering/chain-rule
cells impose no such common-successor closure.  This is the precise reason
the static lossless chain rule cannot simply be used as a dynamic update
algorithm.

Frozen masks repair transition compatibility because the residual route of
each key is public and state-independent.  The price of that repair is exactly
the collapse in Theorem 2.1.

## 7. Final assessment

The recursive frozen-mask exact-residual proposal does not give a new upper
bound at half error:

| residual semantics | valid dynamic rate/consequence |
|---|---:|
| one occupancy bit per finite cell | \(1/\ln2\) apparent bits/key, but deletion is invalid |
| exact multiplicity, regular type-uniform public frozen chain | \(2.384499842479\ldots\) bits/key |
| recursive unary collision layers | exactly the same weak-composition state count |
| literal exact residual in a balanced subset of large \(U\) | \(\Omega(n\log(|U|/n))\) bits |
| state-dependent approximate residual | deletion-routing error can create false negatives |

Thus this route neither reaches \(2.200611\) nor improves the zero-failure
canonical \(2.349083\) construction.  Its useful contribution is a clean
identity and obstruction: **public routing is dynamically safe but collapses;
state-dependent routing is potentially cheaper but needs exact placement
information.**  Any successful ordinary-filter construction must exploit the
second regime without paying the full identity/placement cost.
