# Bounded-churn stability for one-sided membership filters

> Status: the black-box lifting theorem is proved.  The dummy-key simulation is
> also correct as a reduction to a *fresh-distinct* incremental model.  The
> Lovett--Porat corollary formerly stated here is not justified in that model
> and has been withdrawn.  A naive time-layer repair restores legality but
> destroys the extra lower-bound constant.

## 1. Model

Let the universe have size `m`, and let every logical set have size exactly `n`.
An initialization procedure `Build(S_0)` may inspect the complete initial set.
After initialization, the data structure receives at most `T` legal replacement
updates

\[
S\leftarrow S-\{x\}+\{y\},
\qquad x\in S,\ y\notin S.
\]

It must use only its persistent state, the update label `(x,y)`, and its random
tape.  It is not given an external exact set or a rebuild oracle.  Members have
no false negatives.  For every history fixed independently of the random tape,
every time, and every current nonmember `z`, the false-positive probability is
at most `epsilon`.

Write `F_T(m,n,epsilon)` for the minimum fixed memory in bits.  Thus `F_0` is
the corresponding static problem.

## 2. Theorem

Define

\[
P(m,T)=
\sum_{k=0}^{\min\{T,n,m-n\}}
\binom{m}{k}\binom{m-k}{k}.
\]

Then

\[
F_0(m,n,\varepsilon)
\le F_T(m,n,\varepsilon)
\le F_0(m,n,\varepsilon)+\lceil\log_2 P(m,T)\rceil+O(1).
\tag{1}
\]

Consequently,

\[
F_T(m,n,\varepsilon)
\le F_0(m,n,\varepsilon)
+O\!\left(T\log\frac{em}{T}\right).
\tag{2}
\]

In particular, if `m=Theta(n)` and `T=o(n)`, then

\[
F_T(m,n,\varepsilon)=F_0(m,n,\varepsilon)+o(n).
\tag{3}
\]

More generally, (3) holds whenever

\[
T\log(m/T)=o(n).
\]

## 3. Construction

At build time, create any optimal static one-sided filter `B_0` for `S_0`.
Additionally maintain two disjoint exact sets

\[
A=S\setminus S_0,
\qquad
D=S_0\setminus S.
\tag{4}
\]

They satisfy

\[
S=(S_0\setminus D)\cup A,
\qquad |A|=|D|\le T.
\tag{5}
\]

For a legal replacement `x -> y`, perform:

- if `x in A`, remove `x` from `A`; otherwise add `x` to `D`;
- if `y in D`, remove `y` from `D`; otherwise add `y` to `A`.

For a query `z`, answer:

- YES if `z in A`;
- NO if `z in D`;
- otherwise return `B_0.Query(z)`.

The structure never needs to enumerate or recover `S_0`.

## 4. Correctness

We first verify the invariant (4).  Suppose it holds before replacing `x` by
`y`.

- If `x in A`, then `x` is a current element outside `S_0`; deleting it removes
  it from `S\\S_0`.  If `x notin A`, legality gives `x in S`, and (4) then forces
  `x in S_0\\D`; deleting it adds it to `S_0\\S`, hence to `D`.
- If `y in D`, then `y in S_0\\S`; inserting it removes it from `D`.  If
  `y notin D`, legality gives `y notin S`, and (4) then forces `y notin S_0`;
  inserting it adds it to `S\\S_0`, hence to `A`.

Thus the invariant is preserved.

If `z in S`, then either `z in A`, in which case the query returns YES, or
`z in S_0\\D`, in which case the static filter returns YES.  Hence there are no
false negatives.

Now let `z notin S`.

- If `z in D`, the query returns NO.
- If `z notin A union D`, then (5) implies `z notin S_0`, so the query inherits
  the static filter's pointwise false-positive probability, at most `epsilon`.

The overlay therefore causes neither accumulated error nor a special problem
for previously deleted keys.

## 5. Space count

For each possible `k=|A|=|D|`, the ordered pair of disjoint sets `(A,D)` can
be chosen in

\[
\binom{m}{k}\binom{m-k}{k}
\]

ways.  Since `k<=min{T,n,m-n}`, all possible overlays can be enumeratively
encoded using `ceil(log_2 P(m,T))` bits, plus `O(1)` delimiter/control bits.
This proves the upper bound in (1).  The lower bound in (1) follows by looking
at the state immediately after `Build`, before any replacement: it is already
a valid static filter.

Finally,

\[
P(m,T)
\le (T+1)\max_{k\le T}
\left(\frac{em}{k}\right)^k
\left(\frac{e(m-k)}{k}\right)^k,
\]

which gives (2).  For `m=Theta(n)` and `T=o(n)`,

\[
T\log(n/T)+O(T)=o(n),
\]

proving (3).

## 6. A conditional route from fresh-distinct incremental filters

The following simulation is exact, but it transfers only lower bounds already
proved for incremental histories with fresh, pairwise distinct inserted keys.

### Reduction theorem

Let `M_inc^fresh(k,epsilon;u)` be the minimum memory of an insertion-only filter
that starts empty, receives `k` pairwise distinct real keys from a universe of
size `u`, and has the usual pointwise one-sided error guarantee.  If the
bounded-churn universe
contains `n` public dummy keys disjoint from these `u` real keys, then for every
`k<=n`,

\[
F_k(n+u,n,\varepsilon)
\ge M_{\rm inc}^{\rm fresh}(k,\varepsilon;u)-O(\log n).
\tag{6}
\]

#### Proof

Fix dummy keys `d_1,...,d_n` and build the bounded-churn structure on

\[
S_0=\{d_1,\ldots,d_n\}.
\]

To simulate the `i`-th insertion of a real key `x_i`, execute the legal
replacement

\[
d_i\longrightarrow x_i.
\]

After `i` insertions, the physical logical set is

\[
\{x_1,\ldots,x_i\}
\cup
\{d_{i+1},\ldots,d_n\}.
\]

On a query for a real key, this is a valid incremental membership filter for
the inserted real set: inserted real keys are members, while every uninserted
real key is a physical nonmember and inherits the pointwise false-positive
guarantee.  An `O(log n)` counter identifies the next dummy.  This proves (6).

### Why Lovett--Porat cannot yet be substituted into (6)

Lovett--Porat's hard distribution is over `U^k` and permits repeated labels.
Their layered-graph proof uses a closure property of all labels on all paths
reaching a state.  In a fresh-distinct model, an alternative prefix reaching
the same state may already contain a key from the actual future continuation;
concatenating that continuation is then not a legal incremental history.

Consequently, replacing powers by falling factorials or iid concentration by
hypergeometric concentration does not by itself repair the proof.  The former
large-universe corollary and its `alpha>10/11` separation were therefore
overstated and are not theorems of this note.

Assigning the `i`-th insertion its own public alphabet `U_i`, disjoint from all
other time layers, does restore continuation legality.  If each layer has size
`q\gg k`, then the real universe must satisfy

\[
u=kq\gg k^2.
\]

But this modification also admits an independent per-layer static encoding
using only `k log_2(1/epsilon)+o(k)` bits, so the Lovett--Porat extra constant
disappears.  It is therefore a legality check, not a lower-bound repair.  At
`epsilon=1/2`, the explicit reviewer-safe constant in the original repeated-
label model is `1.1`; the reported `1.13` comes from an uncertified computer
search.

## 7. What remains open

The lifting theorem gives a genuine stability regime.  The dummy simulation
identifies a possible lower-bound transfer, but currently establishes no
Lovett--Porat linear endpoint under the ordinary fresh-distinct API.

- Stability is proved when
  \[
  T\log(m/T)=o(n).
  \]
- No matching general linear-churn lower bound is proved here.

The clean sparse-universe target is to determine a rate function

\[
\Gamma(\alpha,\varepsilon)
=
\limsup_n
\frac{F_{\alpha n}(m_n,n,\varepsilon)-F_0(m_n,n,\varepsilon)}{n},
\qquad m_n/n\to\infty,
\]

or at least to locate its positivity threshold.  Any improvement must account
for shared rejection certificates.  At the dense anchor
`m=2n, epsilon=1/2`, a frozen balanced mask gives an `n+O(1)`-bit filter for
arbitrarily long churn, while the static optimum is
`0.6225562489...n+o(n)`; hence no penalty formula may grow unboundedly with
`T`.
