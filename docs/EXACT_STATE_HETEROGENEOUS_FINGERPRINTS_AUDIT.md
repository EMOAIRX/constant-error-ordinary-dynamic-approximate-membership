# Exact-state heterogeneous fingerprints: finite optimization and converse audit

Status: finite optimization proved below; the unrestricted key-level converse
in the candidate note requires repair. All logarithms are base two.

## 1. Finite optimization theorem

Let

\[
f_n(p)=p(1-p)^n,
\qquad
F_{n,q}=\max\left\{\sum_{i=1}^q f_n(p_i):
p_i\ge0,\ \sum_i p_i\le1\right\}.
\]

### Theorem 1

For integers `n>=1,q>=1`,

\[
F_{n,q}=
\begin{cases}
\displaystyle
\frac q{n+1}\left(\frac n{n+1}\right)^n,
&q\le n+1,\\[1.1ex]
\displaystyle
\left(1-\frac1q\right)^n,
&q\ge n+1.
\end{cases}
\]

For `q<n+1`, every maximizing tracked coordinate equals `1/(n+1)`
and the remaining probability is assigned to the permanent-YES category.
For `q>n+1`, the unique maximizing tracked vector is
`p_1=...=p_q=1/q` and there is no permanent-YES mass. At `q=n+1` the
two descriptions coincide.

### Proof

The function `f_n` has its unique global maximum at

\[
a=\frac1{n+1},
\]

because

\[
f_n'(p)=(1-p)^{n-1}(1-(n+1)p).
\]

If `q<=n+1`, summing the pointwise bound `f_n(p_i)<=f_n(a)` proves
the first branch; it is attained by setting every tracked probability to
`a`, whose total mass is at most one.

Now suppose `q>n+1`. Compactness gives a maximizer. It must use all
probability mass. Otherwise either a zero coordinate can be increased, or a
positive coordinate strictly below `a` can be increased; at least one such
coordinate exists because the current total is below one and `q>n+1`.

No maximizing coordinate is zero. If `p_i=0`, then among the remaining
`q-1>=n+1` coordinates some `p_j<=1/(q-1)<=a`. Moving an infinitesimal
mass from `j` to the zero coordinate has directional derivative

\[
f_n'(0)-f_n'(p_j)>0,
\]

unless `p_j=0`, in which case simply adding to either zero coordinate before
the total-mass constraint is saturated gives the same contradiction. Thus
all coordinates are positive.

At an interior constrained maximum, `f_n'(p_i)=mu` for all `i`. The
multiplier satisfies `mu>0`: since the average coordinate is `1/q<a`, at
least one coordinate is below `a`, and its derivative is positive. Hence
every coordinate is below `a`, because `f_n'(p)<=0` for `p>=a`.

Finally,

\[
f_n''(p)=n(1-p)^{n-2}((n+1)p-2),
\]

so `f_n'` is strictly decreasing on `[0,a]` (indeed on
`[0,2/(n+1)]`). The equal-derivative conditions therefore force all
coordinates to be equal. The mass constraint gives `p_i=1/q`, proving the
second branch and uniqueness.

## 2. Exact FPR consequence

For an IID categorical map with tracked probabilities `p_i` and a
permanent-YES category, a fixed nonmember has rejection probability at
current set size `s` equal to

\[
\sum_i p_i(1-p_i)^s.
\]

It is minimized over `s<=n` at `s=n`. Therefore a categorical fingerprint
construction has capacity-`n` FPR at most `epsilon` exactly when

\[
\sum_i p_i(1-p_i)^n\ge1-\varepsilon.
\]

Theorem 1 consequently gives the exact best rejection probability attainable
with `q` tracked labels.

## 3. Repair needed for the state-count converse

The assertion that every implementation must distinguish exactly

\[
\binom{n+q}{q}
\]

vectors is not automatic in the ordinary key-level KLZ API.

First, for current cardinality *at most* `n`, the tracked vector is any
`C in N^q` with `sum C_i<=n`; the number of such vectors is indeed
`binom(n+q,q)`. The extra slack coordinate is a combinatorial device, not
`n-sum C_i` interpreted as the number of real keys mapped to the permanent
YES category: current set size may be below `n`, and top-mapped true keys are
not determined by the tracked vector.

Second, on a fixed public hash tape not every abstract vector need be
reachable. If a tracked fiber `h^{-1}(i)` contains fewer than `n` distinct
keys, large values of `C_i` are impossible. More generally the number of
reachable vectors is

\[
\left|\left\{C\in\mathbb N^q:
0\le C_i\le |h^{-1}(i)|,\ \sum_i C_i\le n\right\}\right|,
\]

which can be strictly smaller than `binom(n+q,q)`.

Third, ordinary approximate membership queries do not force different
multiplicities to have different physical states. After deleting the last
key in a label, retaining that label as a false-positive ghost may be legal.
Behavioral injectivity follows only from a stronger exact tracked-label API,
or from explicitly requiring that normal state determine the multiplicity
vector.

### Lemma 2 (correct exact-state converse)

Fix a hash map `h` whose every tracked fiber contains at least `n` distinct
keys. Consider an implementation required to maintain the exact tracked
multiplicity vector after arbitrary legal key insertions and deletions, with
the vector recoverable from its physical state and public tape. Then its
fixed memory has at least

\[
\left\lceil\log_2\binom{n+q}{q}\right\rceil
\]

bits.

Proof: every vector `C>=0,sum C_i<=n` is reachable by choosing `C_i`
distinct keys from fiber `i`; exact recoverability makes the endpoint-state
map injective.

The rich-fiber premise can be replaced by an exact label-level API supporting
`InsertLabel(i)` and `DeleteLabel(i)`. Without exact recoverability, a label
query that reports exact zero/nonzero is sufficient for injectivity only if
the API also forces a zero label to answer NO; ordinary approximate membership
does not.

## 4. Relationship to the KLZ fixed-memory model

The construction is a valid upper bound in the KLZ-style fixed-memory sense,
subject to the usual pointwise randomness convention: preallocate
`ceil(log binom(n+q,q))` bits, encode every tracked vector of total at most
`n`, and perform unbounded-time rank/unrank updates. There is no overflow and
the representation supports arbitrarily long legal histories.

However, the matching lower bound is only for the declared exact-state
categorical subclass. It is not a KLZ arbitrary-filter lower bound because
KLZ does not require exact multiplicities, cell labels, zero transparency,
or rich hash fibers on every tape.

The FPR calculation also assumes that the fixed history/current set and query
key are independent of the sampled categorical hash. It establishes the
usual pointwise-over-randomness guarantee for every fixed history. It does not
protect against an adversary that observes the public tape and then selects
keys from chosen fibers.

## 5. Paper-value assessment

Theorem 1 plus the rank/unrank construction gives a clean finite-`n` exact
theorem and the stated asymptotic phase transition. It strictly improves the
uniform all-compositions benchmark for `epsilon>1-e^{-1}`.

As a stand-alone conference paper the package is weak:

- the optimization is an elementary separable KKT lemma;
- the converse is definition-level once exact recoverability is imposed;
- operation time is unbounded;
- it does not resolve or improve an arbitrary-filter lower bound;
- permanent-YES mass is a standard convexification device adjacent to
  weighted/Daisy-style filtering.

It is best positioned as a rigorous section or lemma supporting a larger
paper. It becomes substantially stronger if paired with an efficient
fixed-worst-case implementation, a converse for a meaningfully broader
exchangeable class, or a new arbitrary-filter lower bound.
