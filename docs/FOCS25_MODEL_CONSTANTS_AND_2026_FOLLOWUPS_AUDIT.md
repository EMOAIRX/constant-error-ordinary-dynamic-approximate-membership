# KLZ25 model, numerical constants, and 2026 follow-up audit

Date: 2026-08-13. All logarithms are base two unless stated otherwise.

This note separates statements in Kuszmaul--Liang--Zhou (KLZ),
*Fingerprint Filters Are Optimal*, from calculations and candidate theorems in
the local research notes. PDF page numbers refer to the arXiv PDF
arXiv:2510.18129v1.

## 1. The ordinary dynamic-filter model in KLZ

KLZ uses the following computational model immediately before Definition 2.1
(PDF p. 2): the data structure has fixed-length memory with arbitrary access.
It may also read an infinite, read-only tape of independent random bits; this
tape is not charged to the space bound.

KLZ footnote 5 (PDF p. 2) distinguishes this random-access read-only tape from
an oracle that emits fresh bits on demand. Their simulation of the latter
stores a pointer to the last revealed tape bit. The pointer is charged to
memory, but costs only `o(n)` bits when the total number of random-number calls
is at most `2^{o(n)}`. Thus a subexponential operation/random-call horizon can
be determinized by fixing the tape at only `o(n)` first-order cost. A proposed
construction that runs for an arbitrary infinite history while consuming
fresh random bits on every step cannot cite this footnote to make its evolving
randomness state free; it needs a pointer-free addressing rule or a finite
random object sampled in advance.

Definition 2.1 (PDF pp. 2--3) fixes a finite universe

\[
U=\{1,\ldots,u\},
\]

capacity `n`, and false-positive parameter `epsilon in (0,1)`. The data
structure maintains a logical set `S subset U`, `|S| <= n`, and supports:

- `Initialize()` from the empty set;
- `Query(x)`, which is deterministically true for `x in S`, and is false with
  probability at least `1-epsilon` for each fixed `x notin S`; the probability
  is over the data structure's randomness and `x` is explicitly not assumed
  random;
- legal `Insert(x)` under the promise `x notin S`;
- legal `Delete(x)` under the promise `x in S`.

The paragraph following Definition 2.1 (PDF p. 3) additionally says that an
update sees only the stored data-structure information, the input key, and the
random tape. It does not receive the current set `S` explicitly.

Consequently, the ordinary model does not assume history independence,
monotonicity, a canonical state, locality, or an exact backing set. Theorem 1.1
eventually applies without the first two assumptions; Sections 3 and 4 use them
only as intermediate restrictions.

## 2. What KLZ actually proves and leaves open

Theorem 1.1 (PDF p. 2, restated p. 3) says:

\[
\epsilon=o(1),\qquad |U|=\omega(n\epsilon^{-1})
\]

and support for a sequence of `omega(n)` insertions and deletions imply

\[
H\ge n\log\epsilon^{-1}+n\log e-o(n).
\tag{KLZ-1}
\]

This is a fixed-memory, operation-time-independent lower bound. It is not a
fixed-constant-error theorem.

Section 6 (PDF p. 21) explicitly asks for tight upper and lower bounds when

\[
\epsilon^{-1}=\Theta(1).
\]

The authors conjecture that fingerprint filters remain optimal, with the
caveat that fingerprints now form a multiset and must be encoded according to
their source distribution in an information-theoretically optimal way. They
state that both a time-efficient such upper bound and strong lower bounds in
this regime remain open, and warn that careful bookkeeping of the existing
proof does not appear sufficient.

Neither `1.61`, `2.35`, nor `2.349083` appears in KLZ. None is an original KLZ
theorem or conjectured coefficient.

## 3. Source and status of `1.61`

The relevant local result is the equal-block all-pivot full-fiber converse at
`epsilon=1/2`. Its claimed hypotheses are:

- the KLZ fixed `H`-bit/public-random-tape/key-only model;
- arbitrary history dependence, nonmonotonicity, ghosts, and global
  certificates;
- pointwise FPR at most `1/2` and zero false negatives;
- `f(n)=omega(n)` supported operations;
- the stronger universe condition
  \[
  u/n^2\longrightarrow\infty;
  \tag{3.1}
  \]
- the separately derived partition-free full-fiber batch interface.

For ten equal macro-blocks, equations (18) and (28) of
`EQUAL_BLOCK_ALL_PIVOT_CONVERSE_2026_08_13.md` define a convex minimax constant
`C_10` and certify

\[
C_{10}\ge
\frac{803993501430859}{500000000000000}
=1.607987002861718\ldots>1.6079.
\tag{3.2}
\]

The floating-point/numerical location is

\[
C_{10}=1.6079870048457\ldots,
\tag{3.3}
\]

but the safe theorem statement furnished by the certificate is

\[
H>1.6079n-o(n),
\tag{3.4}
\]

conditional on the stated full-fiber lifting. It is not valid to round (3.2)
up and state a certified `H >= 1.61n-o(n)` theorem: `1.607987 < 1.61`.
One may describe (3.3) informally as "approximately 1.608" or "approximately
1.61", provided it is labelled numerical rather than a proved lower bound.

An older local all-pivot experiment reports a finite-depth value near `1.612`
at depth 20. That is numerical evidence only and is not the source of a
certified `1.61` theorem.

This result also does not settle KLZ Section 6 because (3.1) is stronger than
the KLZ large-universe regime `u/n -> infinity`, and because the lower bound is
far below the known upper bounds.

## 4. Source and status of `2.349083` and `2.35`

The number is produced by the local algebraic threshold-quotient construction,
not by KLZ. Public fully random maps send a key to an outer block and a binary
inner symbol. A block stores its exact load `c` and the one-count modulo
`q=L+1`. At low load `c <= L`, this recovers the binary multiset exactly; at
high load the block answers YES to both symbols. Insertions and deletions add
and subtract the inner symbol in the finite group, so after arbitrary high-load
churn the summary again becomes exact when the load falls below the threshold.

For modulus `q=3` (`L=2`), define

\[
A_3(z)=\frac{1-z^3}{(1-z)^2}.
\]

At FPR `epsilon=1/2`, the calibrated outer load and saddle are

\[
\lambda=1.325819075285\ldots,
\qquad
z=0.447778045429\ldots,
\]

and the all-state enumerative rate is

\[
R=\frac1\lambda\log A_3(z)-\log z
=2.349083440193\ldots\quad\text{bits/key}.
\tag{4.1}
\]

The construction has been locally audited as an ordinary KLZ-model upper
bound: fixed worst-case persistent memory, no overflow, zero false negatives,
legal key-only insert/delete/query, pointwise FPR after finite-`n` calibration,
and arbitrary history length. It is information-theoretic and does not claim
efficient rank/unrank operations. Thus the safe global statement is

\[
H^*(n,1/2)\le2.349083440193\ldots n+o(n).
\tag{4.2}
\]

Writing `2.35n` is a harmless looser decimal upper bound. It must not be called
the ordinary optimum or an ordinary lower bound. Matching results in the local
notes concern restricted binary finite-Abelian/canonical accumulator classes;
they do not cover arbitrary dynamic filters.

## 5. Three 2026 papers citing KLZ

### 5.1 arXiv:2608.06066

Blelloch--Hu--Kuszmaul--Li--Zhou, *Dynamic Entropy-Encoded Arrays in O(1) Time
with Nearly Optimal Space*, directly addresses the efficient multiset upper
bound mentioned in KLZ Section 6.

Theorem 8.2 (PDF p. 31), with

\[
\delta=\ln\frac1{1-\epsilon},
\]

assumes `U=poly(n)`, `epsilon=Omega(1/polylog n)`, and
`1-epsilon=Omega(1)`. It maintains `S subset [U]`, `|S|<=n`, in the word RAM
with `w=Omega(log U)`, supports insertion, deletion, and approximate-membership
queries, and uses

\[
\left(1+O\!\left(\frac{\log\log n}{\log n}\right)\right)
n\delta^{-1}H(\operatorname{Pois}(\delta))
+\frac{n}{\operatorname{polylog}n}
\tag{5.1}
\]

bits. Queries take worst-case constant time. Both space and time bounds hold
with high probability in `n`. The proof on PDF p. 32 first obtains expected
space with free randomness and then uses splitting to obtain the stated whp
guarantee and remove fully random hashing. Theorem 8.4 (PDF p. 33) gives the
same leading rate for a modified quotient filter with expected constant-time
operations and whp space.

Verdict: this closes the time-efficient uniform fingerprint-multiset upper-bound
side of the KLZ question in its stated polynomial-universe/whp model. It does
not prove an arbitrary-filter lower bound and does not give a KLZ-style fixed
worst-case `H`-bit space guarantee for every tape/history.

### 5.2 arXiv:2606.15944

Kuszmaul--Putterman--Xu--Zhou--Zhou, *Resizable Retrieval*, studies space as a
function of the current cardinality, rather than the precise fixed-capacity
linear coefficient in KLZ Section 6.

Theorem 1.1 (PDF p. 2; restated p. 20) gives a resizable retrieval structure
for `polylog(U)<=n<=U/2`, `v=O(log U)`, and constant `k`, with

\[
nv+O(n\log\log(U/n)+n\log^{(k)}n)+U^\eta
\tag{5.2}
\]

bits and `O(k)=O(1)` operations with high probability in `n` in the word RAM.
Corollary 3.14 (PDF pp. 20--21) converts it into a resizable filter with

\[
n\log\epsilon^{-1}
+O(n\log\log(U/n))
+\operatorname{polylog}U+O(U^\eta)
\tag{5.3}
\]

bits, for `log epsilon^{-1}=O(log U)`, and constant-time operations whp.

Verdict: (5.3) is a resizability result with a non-sharp linear/additive term.
It neither determines the fixed-constant-error coefficient nor supplies the
KLZ fingerprint-multiset entropy upper or arbitrary-filter lower bound.

### 5.3 arXiv:2602.00906

Guo--Li, *Hallucination is a Consequence of Space-Optimality: A
Rate-Distortion Theorem for Membership Testing*, studies static randomized-set
membership testing, not ordinary dynamic filters.

Definition 2.1 (PDF p. 3) has one `Init(K)` followed by queries and no update
operations. Its memory budget is mutual information

\[
B(M)=I(W;K),
\]

which lower-bounds physical space but is not a fixed `H`-bit dynamic state
requirement. Errors are defined from the output distributions for a uniformly
random set `K`, a uniformly random key, and a uniformly random non-key after a
permutation-invariance reduction (Definitions 2.3--2.4, PDF pp. 3--4).

Theorem 3.1 (PDF pp. 4--5) takes `n/u -> 0` and characterizes asymptotic memory
per key by a minimum KL divergence between key and non-key score
distributions. Its binary/two-sided-filter specialization recovers static
filter rates; Appendix D gives a random-oracle hash construction. The paper
itself notes in footnote 3 on PDF p. 3 that dynamic filters have an additional
space cost.

Verdict: this is neither the pointwise fixed-history KLZ error model nor a
dynamic insert/delete theorem. It does not resolve or directly strengthen KLZ
Section 6.

## 6. Safe one-line frontier at `epsilon=1/2`

Under the extra `u/n^2 -> infinity` hypothesis and the local full-fiber batch
theorem, the certified arbitrary-filter lower bound is

\[
H>1.6079n-o(n).
\]

The local information-theoretic ordinary threshold-quotient construction gives

\[
H\le2.349083440193\ldots n+o(n).
\]

These are not matching bounds, have different provenance from KLZ, and do not
solve the Section 6 fixed-constant-error problem.
