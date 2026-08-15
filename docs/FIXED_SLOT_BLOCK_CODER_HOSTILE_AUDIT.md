# Hostile audit of the fixed-slot multinomial block coder

## 1. Verdict

The fixed-slot block-coding idea is repairable.  There is no information-
theoretic obstruction to obtaining the Poisson-entropy coefficient with
`o(n)` redundancy and polylogarithmic core operations.  However, the short
claim in `PUBLISHABLE_THEOREM_PACKAGE.md` currently suppresses several facts
that must appear in a proof:

1. the block total must be stored;
2. a finite exact coder should use the conditional multinomial law, not
   irrational Poisson probabilities;
3. a dyadic point needs a constant number of guard bits;
4. all block-time pairs, rather than merely all times, enter the failure
   union bound;
5. multiword arithmetic and temporary storage must be charged;
6. a worst-case query may decode almost the entire block;
7. the operation-time theorem is conditional on an efficiently evaluable,
   consistent random-partition oracle.  A free random tape alone does not
   provide such an oracle in the ordinary word-RAM model.

Items 1--6 cost only `o(n)` bits and polylogarithmic time.  Item 7 is a real
model boundary, not a lower-order accounting issue.

## 2. A finite, exact fixed-slot code

Fix a block containing `b` equal-probability light cells.  Conditional on its
total being `s`, its occupancy vector

\[
C=(C_1,\ldots,C_b),\qquad \sum_i C_i=s,
\]

has probability

\[
P_s(c)=\frac{s!}{b^s\prod_i c_i!}.
\]

There is no need to arithmetic-code irrational Poisson probabilities.  View
the `b^s` strings in `[b]^s` as equally likely and place all strings having a
given histogram consecutively, with histograms in lexicographic order.  The
histogram `c` then owns an interval

\[
J_s(c)=\left[\frac{R_s(c)}{b^s},
              \frac{R_s(c)+M_s(c)}{b^s}\right),
\qquad
M_s(c)=\frac{s!}{\prod_i c_i!},
\]

where `R_s(c)` is the total size of all preceding histogram groups.  These
intervals partition `[0,1)` and have width exactly `P_s(c)`.

For a common slot length `L`, call `c` codeable when

\[
P_s(c)\ge 4\,2^{-L}.
\]

Choose

\[
z(c)=\left\lfloor\frac{2^L R_s(c)}{b^s}\right\rfloor+1.
\]

The guard factor four implies

\[
\frac{R_s(c)}{b^s}<\frac{z(c)}{2^L}
 <\frac{R_s(c)+M_s(c)}{b^s}.
\]

Thus the `L`-bit integer `z(c)` lies strictly inside `J_s(c)`.  Since the
interval interiors are disjoint, `s` and `z(c)` uniquely determine `c`.
This is a literal fixed-slot code; it is not an expected-length prefix code.

The constant four is only a convenient boundary convention.  It costs two
bits per block and hence `O(n/b)=o(n)` bits in total.

### Exact rank and unrank

All relevant quantities are integers.  For example, after fixing counts
`c_1,...,c_{i-1}` and leaving `t` balls and `m` cells, the number of strings
whose next count is `a` is

\[
\binom{t}{a}(m-1)^{t-a}
\]

times the multinomial factor already fixed by the prefix.  Summing these
terms over `a<c_i` computes the corresponding contribution to `R_s(c)`.
The inverse procedure locates `c_i` by comparing the scaled dyadic point
against the same cumulative integer sums.

If `s=O(b)`, every integer involved has

\[
O(s\log b)=O(b\log b)
\]

bits.  Even schoolbook exponentiation, multiplication, division, and a
linear search over possible counts use `log^{O(1)} n` word operations when
`b=ceil(log^4 n)` and the word size is `Theta(log n)`.  No unit-cost
operation on a `Theta(b log b)`-bit integer is being assumed.

This construction also gives an exact codeability test:

\[
M_s(c)2^L\ge 4b^s.
\]

Consequently the implementation need not evaluate logarithms or multinomial
CDFs approximately.

## 3. Uniform high-probability slot length

Define the conditional information density

\[
I_s(c)=-\log_2P_s(c)
=s\log_2b-\log_2(s!)+\sum_i\log_2(c_i!).
\]

If one of the `s` independent uniform cell choices is changed, two counts
change and

\[
|\Delta I_s|\le \log_2(s+1).
\]

McDiarmid's inequality therefore gives

\[
\Pr[I_s(C)-H(C\mid S=s)>u\mid S=s]
\le
\exp\!\left(-\frac{2u^2}
 {s\log_2^2(s+1)}\right).
\tag{3.1}
\]

The centre can be bounded at the correct constant.  Put `x=s/b`.  Directly,

\[
H(C\mid S=s)
=s\log_2b-\log_2(s!)+b\,\mathbb E\log_2(Z!),
\quad Z\sim\operatorname{Bin}(s,1/b).
\]

The binomial variable is below `Y~Pois(x)` in convex order, while
`k -> log(k!)` is convex.  Also `s! >= (s/e)^s`.  Hence

\[
H(C\mid S=s)\le bH_2(\operatorname{Pois}(s/b)).
\tag{3.2}
\]

For completeness, the convex-order assertion follows by first checking
`Bernoulli(p) <=cx Pois(p)` with the stop-loss characterization and then
using closure of convex order under independent sums.

Poisson entropy is increasing in its mean: if `y>x`, write
`Pois(y)=Pois(x)+Pois(y-x)` independently and use
`H(X+Y)>=H(X+Y|Y)=H(X)`.  Its derivative is bounded on every compact
subinterval of `(0,infinity)`.  Thus, for fixed `lambda>0` and

\[
s\le s_{\max}=\lambda b+A\sqrt{b\log n},
\]

equation (3.2) implies

\[
H(C\mid S=s)
\le bH_2(\operatorname{Pois}(\lambda))
   +O_A(\sqrt{b\log n}).
\tag{3.3}
\]

Combining (3.1)--(3.3), for every fixed desired exponent `K` there is a
constant `D=D(lambda,A,K)` such that the common slot length

\[
L=bH_2(\operatorname{Pois}(\lambda))
  +D\sqrt{b\log n}\log b+O(1)
\tag{3.4}
\]

makes the conditional probability of an uncodeable histogram at most
`n^{-K}`, uniformly over every `s<=s_max`.  Rounding (3.4) upward to an
integer and the two guard bits are included in the `O(1)` term.

## 4. Block totals and the full-history union bound

Suppose a light cell has probability `p=lambda_n/n`, where
`lambda_n -> lambda`, and a block contains `b` cells.  At a time when the
current set has size `k<=n`, its block total is

\[
S\sim\operatorname{Bin}(k,bp),\qquad \mathbb ES\le b\lambda_n.
\]

A Bernstein or Chernoff bound gives

\[
\Pr[S>b\lambda_n+A\sqrt{b\log n}]\le n^{-Omega(A^2)}.
\tag{4.1}
\]

Store `S` explicitly in `O(log b)` bits in each block.  The endpoint is
declared bad if (4.1) fails or if its histogram is not codeable in the sense
of Section 2.

There are `B=Theta(n/b)` blocks and at most `T+1<=n^c+1` endpoint states.
No independence across blocks or times is required.  Choose the constants in
(3.4) and (4.1) so that the bad probability for one block at one endpoint is
at most `n^{-(c+d+3)}`.  Then

\[
\Pr[\text{some bad block during the history}]
\le B(T+1)n^{-(c+d+3)}<n^{-d}
\]

for all sufficiently large `n`.

This argument is valid because the legal history is fixed independently of
the partition seed.  At each fixed endpoint its current key set is fixed, so
the displayed binomial and conditional multinomial laws are exact.  The
events at different endpoints may be arbitrarily correlated.

## 5. Complete space and operation accounting

Let `q=Theta(n)` light cells and `B=ceil(q/b)`. One clean exact choice is

\[
q=b\,\operatorname{round}\!\left(\frac{\alpha n}{\lambda b}\right),
\]

so `q=alpha n/lambda+O(b)` is a multiple of `b`. The permanent-positive
category has probability `beta=1-alpha`; give every light cell probability
`p=alpha/q` and put `lambda_n=np=lambda+O(b/n)`. The allocated slot length
uses `lambda_n`, not only its limit.

Reserve the following single preallocated memory block:

* `B` slots of length `L` from (3.4);
* `O(log b)` bits for each block total;
* one global sticky-failure bit;
* one reusable scratch area of `O(b log b)` bits, including a decoded count
  vector and the multiword integers used by rank/unrank.

If slots are word-aligned, charge an additional `O(log n)` padding bits per
block, totaling `O(n log n/b)=o(n)`. Alternatively, bit-pack the slots and
allow a slot to span word boundaries.

The scratch area is part of the advertised space; it is not free workspace.
The total is

\[
qH_2(\operatorname{Pois}(\lambda_n))
+O\!\left(
n\sqrt{\frac{\log n}{b}}\log b
+\frac{n\log b}{b}
+b\log b
\right).
\tag{5.1}
\]

For `b=ceil(log^4 n)`, every error term in (5.1) is `o(n)`.

An update decodes one complete block into the reserved scratch area, changes
one count and its block total, computes the new `z`, and only then overwrites
the old slot.  If the new endpoint is bad it sets the sticky-failure bit.
This ordering prevents an in-place overwrite from destroying the only copy
before codeability has been checked.

A query may sequentially unrank only up to its target coordinate, but in the
worst case this is essentially the whole block.  Thus the proven claim is
`log^{O(1)} n` time, not constant time and not local `O(1)` decoding.  After
sticky failure, all updates are no-ops and all queries answer YES.

## 6. The permanent-positive mixture and pointwise error

For a fixed nonmember `x` and a current set of size `k<=n`, before the
overflow event is added, the exact false-positive probability is

\[
\beta+qp\bigl(1-(1-p)^k\bigr)
\le \beta+(1-\beta)\bigl(1-(1-p)^n\bigr).
\tag{6.1}
\]

This remains a pointwise statement for every fixed `x`: all universe keys are
exchangeable, and `h(x)` is independent of the hashes of the distinct
current keys.  It does not matter if `x` occurred earlier in the fixed
history.

Overflow may be correlated with the collision event, so the safe bound is a
union bound, not a product calculation:

\[
\Pr[\mathrm{FP}(x)]\le \text{right side of (6.1)}
 +\Pr[\mathrm{overflow\ by\ this\ time}].
\]

Choose the base parameters for error `epsilon-eta_n`, with for example
`eta_n=1/log n`, and tune the history-wide overflow probability below
`n^{-d}`. This larger vanishing margin absorbs finite-`n` collision and
rounding errors as well as overflow. It gives pointwise FPR at most
`epsilon`; continuity of the rate changes the allocated space by only `o(n)`.

For the high-error optimum, `lambda=lambda_*` and the light key-mass is

\[
\alpha=\frac{1-\epsilon}{1-\epsilon_*},\qquad \beta=1-\alpha.
\]

Equation (5.1) then has leading term

\[
qH_2(\operatorname{Pois}(\lambda_*))
=\alpha n\frac{H_2(\operatorname{Pois}(\lambda_*))}{\lambda_*}+o(n),
\]

which is the claimed convex-envelope branch.  Top-mapped insertions and
deletions perform no core operation; consistency of the partition map is
nevertheless essential so that a later deletion follows the same branch as
the insertion.

## 7. Formal theorem that the audit supports

### Theorem (fixed-slot dynamic core, conditional oracle version)

Fix constants `lambda>0`, `alpha in (0,1]`, and `c,d>0`.  Let a consistent
random-partition oracle map distinct universe keys independently to `top`
with probability `1-alpha` and uniformly to
`q=(alpha/lambda)n+o(n)` light cells otherwise.  An oracle evaluation is
charged `tau_h(n)` word operations.  Against every seed-independent legal
history of length at most `n^c` and capacity `n`, there is a single-
preallocation, zero-transparent dynamic fingerprint multiset using

\[
\alpha n\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda}+o(n)
\]

bits, including metadata and scratch storage, such that:

1. outside one sticky ALL-YES state, all light-cell multiplicities are exact;
2. the probability of entering that state anywhere in the history is at
   most `n^{-d}`;
3. each operation takes `tau_h(n)+log^{O(1)}n` worst-case word operations.

The proof is Sections 2--5.  Applying (6.1) with a vanishing error margin
turns the core theorem into the corresponding pointwise one-sided filter
upper bound.

This theorem is strong enough for the proposed phase-transition upper bound
provided the paper explicitly adopts the random-partition-oracle model.

## 8. What is not yet proved in the ordinary word-RAM model

The theorem above deliberately exposes `tau_h(n)`.  An infinite free random
tape supplies entropy, but does not automatically supply random access to a
consistent iid value `h(x)` for every universe key.  The following are not
interchangeable:

* an ideal fully random function oracle;
* a random-access table of `|U|` independent labels on an uncharged tape;
* a short-seed hash family evaluable in constant time;
* a sequential read-only random tape.

Exact multinomial endpoint laws use full independence on every current set.
A short-seed `k`-wise independent hash family neither gives those laws nor
automatically gives their smooth-entropy statements, and high-degree
polynomial hashing may take non-polylogarithmic evaluation time.  Storing
labels lazily is also insufficient unless reinsertion and deletion
consistency, nonmember queries, and the storage cost of the label table are
handled.

Therefore the unconditional sentence

> sequential binomial coding gives a polylogarithmic word-RAM dynamic filter

is too strong as presently written.  The safe alternatives are:

1. state the result in an ideal random-partition-oracle RAM model;
2. prove a separate efficiently evaluable hashing lemma whose endpoint tail
   bounds are strong enough for Sections 3--4 and include its seed/storage
   cost; or
3. advertise only the polylogarithmic **multiset-core** operation time, while
   leaving outer hash evaluation outside the claim.

This hashing issue does not invalidate the fixed-slot coder or its
`nR+o(n)` space bound.  It does prevent the current manuscript from claiming
an ordinary word-RAM implementation without an additional lemma or an
explicit oracle assumption.

## 9. Minimal failure modes for an imprecise proof

The following small examples explain why each repair is necessary.

* If `s` is not stored, the same slot integer can lie in arithmetic intervals
  belonging to different conditional distributions `P_s`; decoding is not
  defined.
* If an interval merely has width `2^{-L}` and a half-open boundary contains
  the only dyadic grid point, a boundary convention can assign that point to
  the adjacent histogram.  Two guard bits remove the issue.
* Coding directly with `Pois(lambda)` invokes probabilities containing
  `exp(-lambda)` and is not an exact finite integer algorithm for general
  `lambda`.  Conditioning on `s` yields denominator `b^s` and fixes this.
* A per-endpoint bad probability `n^{-d}` is inadequate: there are
  `Theta(n^{c+1}/b)` block-time pairs.  The exponent must depend on `c+d`.
* Re-encoding in place without enough scratch memory can destroy the old
  code before discovering overflow.  A reusable `O(b log b)`-bit workspace
  is sufficient and must be included in the fixed allocation.
* The arithmetic code does not give random access to `C_i`.  A late-coordinate
  query can require almost a full block decode, which is still polylogarithmic
  for `b=log^4 n` but is not constant time.
