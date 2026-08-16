# Audit of Theorem 8.2 of *Dynamic Entropy-Encoded Arrays*

Source: local HTML copy `references/entropy_arrays_2608.html` of Blelloch--Hu--Kuszmaul--Li--Zhou, *Dynamic Entropy-Encoded Arrays in \(O(1)\) Time with Nearly Optimal Space*, arXiv:2608.06066. This note audits only the effect of Theorem 8.2 on the constant-error question in KLZ25 Section 6.

## Exact statement

Theorem 8.2 is at HTML lines 6665--6674. Its parameters and guarantees are:

- fixed capacity parameter \(n\);
- universe \(U=\operatorname{poly} n\);
- \(\varepsilon=\Omega(1/\operatorname{polylog}n)\), \(\varepsilon\in(0,1)\), and \(1-\varepsilon=\Omega(1)\);
- word RAM with word size \(w=\Omega(\log U)\);
- a dynamic set \(S\subseteq[U]\) with \(|S|\le n\);
- insertions, deletions, and approximate-membership queries;
- fingerprint range
  \[
  [n\delta^{-1}+O(1)],\qquad
  \delta=\ln\frac1{1-\varepsilon};
  \]
- space
  \[
  \left(1+O\!\left(\frac{\log\log n}{\log n}\right)\right)
  n\delta^{-1}H_2(\operatorname{Pois}(\delta))
  +\frac{n}{\operatorname{polylog}n}
  \tag{8}
  \]
  bits;
- queries in worst-case constant time;
- both the space and time bounds hold with high probability in \(n\).

For every fixed constant \(\varepsilon\in(0,1)\) bounded away from 1, this is

\[
n\rho(\varepsilon)+o(n),\qquad
\rho(\varepsilon)=\frac{H_2(\operatorname{Pois}(\delta))}{\delta}.
\]

The additive `n/polylog n` has an arbitrarily tunable constant exponent in the parent entropy-array theorem; the multiplicative loss displayed in Theorem 8.2 is explicitly \(O(\log\log n/\log n)\).

## What type of filter it is

This is the uniform single-fingerprint multiset construction, not a nonuniform or heterogeneous fingerprint scheme.

- Section 8.2 maps keys through one random hash \(h:[U]\to[m]\), where \(m\) is the smallest integer satisfying \((1-1/m)^n\ge1-\varepsilon\) (lines 6740 onward, especially line 6740 in the local source excerpt beginning `S8.SS2.p5`).
- It stores the count array \(C_i=|\{x\in S:h(x)=i\}|\), and answers yes iff \(C_{h(x)}\ne0\) (proof paragraphs `S8.SS2.p5`--`S8.SS2.p6`, around lines 6740--6765).
- The theorem itself says that it stores “a multiset of fingerprints” in the uniform range above (line 6665).

Therefore Theorem 8.2 proves achievability of the **uniform Poisson-occupancy rate**. It proves nothing about the optimum over nonuniform fingerprint probabilities, heterogeneous loads, multiple choices, or arbitrary dynamic filters.

## False-positive quantifier actually established

The introductory definition says that a member query is guaranteed true and a nonmember query is false with probability at least \(1-\varepsilon\) (lines 1795--1798). The proof fixes \(n,\varepsilon\), chooses random \(h:[U]\to[m]\), and for a nonmember \(x\) computes

\[
\Pr_h[\exists y\in S:h(y)=h(x)]
=1-(1-1/m)^{|S|}
\le 1-(1-1/m)^n
\le\varepsilon
\]

(paragraph `S8.SS2.p6`, equation (92), around lines 6750--6765).

Thus the text supports the usual pointwise statement for each fixed current set/history and fixed nonmember key, with probability over the sampled hash/data-structure randomness. It does **not** state an adaptive-adversary theorem in which the update/query sequence is allowed to depend on revealed answers or hash-dependent behavior. No such `adaptive`, `oblivious`, or adversarial-sequence quantifier appears in Theorem 8.2 or its proof. Consequently an adaptive-sequence guarantee should not be attributed to this theorem without an additional argument.

## Updates and time

There is a wording mismatch worth preserving:

- The formal last sentence of Theorem 8.2 explicitly says “answers queries in worst-case constant time,” then says both the “space and time bounds” are with high probability (line 6674). It does not separately spell out the update-time adjective there.
- The theorem's first sentence says the filter supports insertions and deletions. The proof implements each insertion/deletion by one update to \(C_{h(x)}\) (`S8.SS2.p6`). The invoked entropy-array Theorem 1.1 supports both array updates and queries in worst-case constant time (lines 1657--1677), with its time guarantee holding whp.
- The introduction summarizes the first filter as supporting \(O(1)\)-time “operations,” whp (lines 1801--1810).

The proof therefore supports worst-case \(O(1)\) insertion, deletion, and query time in the paper's randomized/whp sense, but a quotation of the formal theorem should not silently replace its narrower wording.

## Space convention and operation horizon

Theorem 8.2 is **not** a KLZ-style fixed-length-memory theorem.

- Its displayed compressed-space bound holds with high probability, not for every random tape or every reachable state (line 6674).
- The proof first obtains expected space, then uses splitting/bucketing and concentration to upgrade the total to high-probability space (`S8.SS2.p4`, `S8.SS2.p8`, `S8.SS2.p9`, around lines 6724 and 6808--6889).
- On the complement of that high-probability event the theorem gives no displayed fixed cap of \(n\rho(\varepsilon)+o(n)\) bits. Hence it does not itself give one fixed \(H\)-bit state space of that size, as required by KLZ Definition 2.1.

The theorem says the structure “maintains” every set of size at most \(n\), and states no finite operation horizon. But its probability language is pointwise/current: “Both the space and time bounds are with high probability in \(n\).” The paper does not state that one random initialization simultaneously satisfies the bounds over an arbitrary infinite sequence, nor give a polynomial-horizon union-bound parameter in Theorem 8.2. It is therefore safe to claim support for arbitrary legal insert/delete operations at each invocation/current state, but **not** a simultaneous no-failure guarantee over an unbounded or update-adaptive execution.

## Effect on KLZ25 Section 6

### Proved by Theorem 8.2

1. For constant \(\varepsilon\) (and more generally its stated range), a uniform fingerprint multiset can be dynamically represented at
   \[
   n\rho(\varepsilon)+o(n)
   \]
   bits with constant-time operations in the paper's whp-space/whp-time word-RAM model.
2. The earlier purely algorithmic question “can the source-distributed uniform fingerprint multiset be entropy-encoded dynamically and time-efficiently?” is answered affirmatively under those probabilistic resource guarantees.
3. A new paper cannot claim novelty merely for an \(O(1)\)-time dynamic implementation of the uniform Poisson-count array with whp near-entropy space.

### Not proved by Theorem 8.2

1. It does not prove that \(\rho(\varepsilon)\) is optimal for arbitrary dynamic approximate-membership filters.
2. It does not give the missing constant-error KLZ lower bound.
3. It does not prove uniform fingerprints optimal even within a broader nonuniform/heterogeneous fingerprint class.
4. It does not match KLZ's fixed worst-case \(H\)-bit memory convention: its near-entropy space is whp.
5. It does not state a simultaneous guarantee over an infinite, polynomial, or adaptively chosen operation sequence.
6. It assumes \(U=\operatorname{poly}n\); it is not a theorem for every finite universe allowed in KLZ's information-theoretic model.

## Bottom line

Theorem 8.2 closes the **uniform-fingerprint dynamic coding upper-bound subproblem** in a high-probability resource model. It does not close KLZ25 Section 6's central arbitrary-filter constant-error optimality problem, and it does not furnish the same fixed-memory/no-extra-failure upper bound as the KLZ model. The correct post-2026 target remains either a sharp lower bound for arbitrary dynamic filters or a genuinely stronger/nonuniform construction together with the appropriately matched model and converse.
