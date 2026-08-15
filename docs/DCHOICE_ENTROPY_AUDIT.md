# Two-choice dynamic membership: entropy audit and the real obstruction

## Executive conclusion

The natural two-choice **exact-multiplicity** extension does not currently
look like a path to beating the convexified single-fingerprint rate
`R_FM`.  Even a public deterministic orientation, which pays no separate
routing bits, is numerically worse because every query probes two cells.

There is, however, a sharper frontier hidden inside the calculation.  If one
stores only the occupied-cell support, a simple public min-rank two-choice law
has a snapshot entropy strictly below `R_FM` on a nontrivial constant-error
interval.  At error `1/2`, the candidate rates are

\[
R_{\rm support}=2.1216107112\ldots
<R_{\rm FM}=2.2006114830\ldots
<R_{\rm count}=2.8304000127\ldots .
\]

This is not yet a dynamic filter.  Exact deletion cannot in general be
implemented from the support alone: clearing a cell after deleting one key
can create a false negative for another key in the same cell, while never
clearing it causes ghosts to accumulate.  The publishable question is
therefore not “does cuckoo placement improve the Poisson count entropy?” but
whether deletion can maintain a near-support-entropy representation by
repairing or recycling ghosts without restoring the missing multiplicity
information.

## 1. A strict oracle-free two-choice model

Let `q=Theta(n)` and let the public tape specify two independent maps

\[
h_1,h_2:U\to[q].
\]

Each stored key is an edge

\[
e_x=\{h_1(x),h_2(x)\}
\]

of the public candidate multigraph.  A dynamic structure has one fixed
preallocated memory block.  It supports ordinary key-level `Insert(x)`,
`Delete(x)`, and `Query(x)`; deletion is promised legal.  There is no backing
exact dictionary, no insertion log, and no oracle that reveals the previous
orientation.  Hash seeds, stash contents, routing information, relocation
metadata, and scratch memory all count.

An exact-count orientation structure chooses

\[
\sigma_S(x)\in e_x
\]

for every current key and stores enough information to update the selected
cell counts

\[
N_v=|\{x\in S:\sigma_S(x)=v\}|.
\]

Query probes both candidates:

\[
Q(x)=\mathbf1[N_{h_1(x)}>0\ \vee\ N_{h_2(x)}>0].
\]

If the orientation is a fixed public function
`phi(h1(x),h2(x))`, deletion recomputes it and no persistent orientation bits
are necessary.  If placement or relocation depends on the current state,
the state must itself identify the current route of a deleted key.  A useful
information decomposition is then

\[
H(N,\sigma\mid\Gamma)
=H(N\mid\Gamma)+H(\sigma\mid N,\Gamma),
\]

where `Gamma` is the public candidate graph.  The second term is zero for a
public fixed orientation but may be linear for adaptive placement.  It cannot
be dropped or treated as free insertion-time advice.

## 2. The clean min-rank calculation

Order the cells publicly and orient every edge to its smaller endpoint:

\[
\phi(x)=\min\{h_1(x),h_2(x)\}.
\]

Write `q=n/alpha` and scale a cell index as `t in [0,1]`.  Up to rounding and
diagonal edges, the selected count at rank `t` has Poisson load

\[
\lambda_\alpha(t)=2\alpha(1-t).
\]

The mean occupied-cell fraction is

\[
\rho(\alpha)
=\int_0^1(1-e^{-\lambda_\alpha(t)})\,dt
=1-\frac{1-e^{-2\alpha}}{2\alpha}.
\]

A fresh nonmember probes two independent candidates, so

\[
\varepsilon(\alpha)
=1-(1-\rho(\alpha))^2.
\tag{1}
\]

### Exact-count source rate

If all cell multiplicities are represented, the candidate first-order rate is

\[
R_{\rm count}(\alpha)
=\frac1\alpha\int_0^1
H_2(\operatorname{Pois}(2\alpha(1-t)))\,dt.
\tag{2}
\]

At `epsilon=1/2`, equation (1) gives

\[
\rho=1-2^{-1/2},\qquad
\alpha=0.36918788070196074\ldots,
\]

and (2) gives

\[
R_{\rm count}=2.8304000127\ldots .
\]

This is substantially above

\[
R_{\rm FM}(1/2)=2.2006114830\ldots .
\]

Numerically the min-rank exact-count curve remains above `R_FM` throughout
the constant-error range.  This is not a proof against every two-choice
orientation, but it gives the correct warning: heterogeneous loads save
count entropy, while probing two cells imposes a larger collision budget.
State-dependent placement then has an additional routing term rather than a
free advantage.

### Support-only snapshot rate

Let

\[
B_v=\mathbf1[N_v>0].
\]

The product-Poisson snapshot benchmark is

\[
R_{\rm support}(\alpha)
=\frac1\alpha\int_0^1
h_2(1-e^{-2\alpha(1-t)})\,dt.
\tag{3}
\]

At error `1/2`, (3) gives

\[
R_{\rm support}=2.1216107112\ldots,
\]

which beats `R_FM` by about `0.07900` bit per key.  The largest sampled gap
is about `0.09104` bit per key near error `0.5745`.  The unconvexified support
curve crosses below `R_FM` near error `0.38948` and crosses back near
`0.87668`.  Its supporting line to `(1,0)` is tangent near

\[
\varepsilon=0.649515,
\qquad
\frac{R_{\rm support}}{1-\varepsilon}
=4.16820\ldots,
\]

strictly below the `R_FM` high-error slope
`4.4012229659...`.

The calculation is a real pressure test: an arbitrary-filter lower bound of
`n R_FM-o(n)` cannot be proved merely by asserting that every useful state
must contain the endpoint support.  Endpoint support has less entropy than
the exact multiplicity source and can even fall below the proposed universal
rate.

## 3. Why the support calculation is not already an upper bound

On `Delete(x)`, the structure can recompute the selected cell
`phi(x)`.  It cannot determine from `B_phi(x)=1` whether another true key
still selects the same cell.

* Clearing the bit may produce a false negative for that other member.
* Keeping the bit is safe, but leaves a ghost false positive.
* Keeping every ghost makes the accepted set monotonically grow.  Under
  sustained churn the false-positive rate approaches one.
* Recording whether this was the last copy is precisely multiplicity or
  deletion-witness information, which may restore a linear part of the gap.

This obstruction remains even though orientation is public and deterministic.
Relocation does not automatically fix it: after moving keys, the structure
must know which keys to move and how to find the current placement of a later
deleted key.  That information belongs in the memory accounting.

The strongest plausible SODA theorem would therefore have one of two forms.

**Separation theorem.**  Construct a standard one-sided dynamic filter with
ordinary key-only deletion whose rate is the lower convex envelope of (3),
plus `o(n)`, for polynomial oblivious histories, by a bounded ghost-repair or
epoch-recycling mechanism.  This would give a strict counterexample to
`R_FM` as the universal constant-error rate.

**Deletion-information theorem.**  Prove that every oracle-free dynamic
implementation of this two-choice support process must store an additional
linear deletion witness, and that

\[
H(B)+I_{\rm delete}\ge nR_{\rm FM}(\varepsilon)-o(n).
\]

This would identify the precise information cost hidden by static support
entropy and extend the fingerprint converse in a natural direction.

## 4. Minimal executable experiments

### Experiment A: endpoint source audit

For `q<=8` and `n<=6`:

1. Enumerate ordered `n`-tuples of candidate edges.
2. Enumerate public deterministic orientation rules, initially min-rank and
   then all symmetric local rules.
3. Compute the exact distributions of `N` and `B`.
4. Report `H(N)`, `H(B)`, `H(N|B)`, and fresh-edge FPR.
5. Compare the finite rates with (2), (3), and `R_FM`.

This verifies the entropy formulas and quantifies exactly how much
multiplicity information is being discarded.

### Experiment B: deletion transducer SAT/ILP

For `q=4, n=2` and then `q=5, n=3`, enumerate a fixed finite public candidate
graph and synthesize the smallest deterministic memory automaton satisfying:

* legal key-labeled inserts and deletes;
* no false negatives after every update;
* query is allowed to retain false-positive ghosts;
* an explicit cap on accepted vertices or fresh-edge FPR at every endpoint;
* no external exact-set or orientation oracle.

Variables describe the state assigned to each reachable set/history, query
masks, and labeled transitions.  An ILP minimizes the number of states; an LP
can subsequently mix public tapes to impose pointwise FPR.  Essential outputs
are whether histories with equal endpoint support can be merged, how many
ghost patterns are required, and whether a small repair cycle exists.

### Experiment C: bounded-churn ghost budget

Fix a free build snapshot and allow `T` replacements.  Optimize the number of
additional ghost/deletion-witness states for `T=0,1,...`.  This connects the
support gap to the broader question of when a static filter becomes dynamic.
Evidence of an `o(n)` witness for `T=o(n)` but an `Omega(n)` witness for
`T=Theta(n)` would itself suggest a rate-versus-churn theorem.

## 5. Literature and 2026 baseline

Blelloch, Hu, Kuszmaul, Li, and Zhou, *Dynamic Entropy-Encoded Arrays in
O(1) Time with Nearly Optimal Space* (arXiv:2608.06066), Theorem 8.2, already
implements the uniform Poisson-count fingerprint filter in worst-case
constant query time with high-probability time and space guarantees, using

\[
(1+o(1))\frac n\delta H(\operatorname{Pois}(\delta))+o(n)
\]

bits.  Thus constant-time uniform count coding is no longer a contribution.
Their general entropy-array theorems are also powerful enough to make an
`O(1)` heterogeneous-count implementation plausible after grouping cells
with comparable prescribed loads.  A permanent-positive component can be
handled by public routing to an always-YES region.  Consequently, merely
implementing the convexified `R_FM` curve in constant time is at best a
technical corollary unless a non-identically-distributed specialization
requires genuinely new machinery.

Backyard cuckoo hashing and later succinct dictionaries show that dynamic
key placement and routing can be stored succinctly relative to an exact
dictionary benchmark.  They do not give the support-entropy AMQ rate above:
their goal is to preserve exact keys, and the exact-key information dwarfs
the constant bits-per-key comparison here.  Engineering cuckoo filters and
flexible/elastic fingerprints optimize load, throughput, or resizing, but
the audited literature does not state the exact support-versus-deletion
entropy tradeoff.

## 6. Recommendation

Do not make generic exact-count `d=2` placement the primary route.  The clean
orientation already loses badly, while adaptive orientation introduces a
routing bill that must be proved small before it can help.

The support-only calculation is worth promoting to a short, tightly scoped
research sprint because it gives a concrete strict numerical target against
`R_FM`.  The sprint should be killed unless it produces one of the following:

1. a ghost-repair construction whose total metadata is below the observed
   `0.079` bit/key gap at error `1/2`;
2. a finite-state counterexample that scales or tensors;
3. a deletion-information lower bound explaining why the support gain is
   necessarily paid back.

Without one of these, (3) remains a useful counterexample to an overly simple
converse, not a paper theorem.
