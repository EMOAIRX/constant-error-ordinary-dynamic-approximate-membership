# An efficient short-seed outer hash for the fixed-slot block coder

## 1. Purpose and conclusion

This note closes the random-partition-oracle gap in the fixed-slot upper
bound.  The useful construction is not a single low-independence categorical
hash.  It is a product of two independent polynomial hashes:

1. a `k_1=Theta(log n)`-wise independent hash chooses `top` or a light
   **block**;
2. a `k_2=Theta(log^4 n)`-wise independent hash chooses the coordinate
   inside that block.

The first hash gives a polynomially small upper tail for every block load.
Conditional on the first hash and on a block load at most `k_2`, the second
hash is genuinely iid uniform on all keys in the block.  Consequently the
conditional multinomial law, including the information-density tail needed
by the fixed-slot arithmetic code, is exact.  No claim that ordinary
`Theta(log n)`-wise independence fools a high-degree codeability event is
needed.

For a universe of `w`-bit keys, `w=Theta(log n)`, the two seeds use

\[
O((k_1+k_2)w)=O(\log^5 n)
\]

bits.  Horner evaluation over `GF(2^w)` takes `log^{O(1)} n` word operations,
even if field multiplication is implemented by elementary polynomial
arithmetic rather than treated as a unit-cost instruction.  The seed and
field metadata are `o(n)` bits.

The construction preserves, against every seed-independent legal history of
polynomial length:

* history-wide overflow probability at most `n^{-d}`;
* the exact conditional multinomial information-density bound in every
  nonoverflowing block;
* pointwise one-sided FPR, up to a tunably polynomially small additive term;
* the leading space `n R + o(n)` and polylogarithmic worst-case operation
  time in an ordinary word-RAM implementation.

## 2. Exact construction

Let the universe be a subset of `GF(2^w)`, where

\[
M=2^w\ge |U|\ge n,
\qquad w=O(\log n).
\]

The injection of universe keys into the field is fixed and public.  Set

\[
b=2^{\lceil 4\log_2\log_2 n\rceil};
\]

thus `log^4 n <= b < 2 log^4 n`, and fix a surjective `GF(2)`-linear map

\[
\pi:GF(2^w)\longrightarrow GF(2^{\log_2b}).
\]

After identifying the range of `pi` with `[b]`, a uniform field element maps
exactly uniformly to `[b]`.

Fix desired limiting parameters `lambda>0` and `alpha in (0,1]`.  Choose

\[
t=\max\left\{1,
 \left\lfloor {\lambda M b\over n}+{1\over2}\right\rfloor\right\},
\qquad
B=\left\lfloor {\alpha M\over t}\right\rfloor,
\]

decreasing `B` by one only if necessary to ensure `Bt<=M`.  Define

\[
\theta_n={t\over M},\qquad
p_n={t\over Mb},\qquad
\lambda_n=np_n,
\qquad
\alpha_n={Bt\over M}.
\tag{2.1}
\]

Because `M>=n`,

\[
\lambda_n=\lambda+O(1/b),
\qquad
\alpha_n=\alpha+O(b/n).
\tag{2.2}
\]

Choose independently two random polynomials over `GF(2^w)`,

\[
P_1(X)=\sum_{i=0}^{k_1-1}a_iX^i,
\qquad
P_2(X)=\sum_{i=0}^{k_2-1}c_iX^i,
\]

with uniform independent coefficients.  Use the standard `w`-bit vector
representation to enumerate the field elements by their binary integer
values.  Partition the first `Bt` outputs of `P_1` into `B` consecutive
sets `A_1,...,A_B`, each of cardinality `t`; all remaining outputs form
`A_top`.  Define

\[
h(x)=
\begin{cases}
\mathsf{top},&P_1(x)\in A_{\mathsf{top}},\\
(j,\pi(P_2(x))),&P_1(x)\in A_j.
\end{cases}
\tag{2.3}
\]

Every light cell has probability exactly `p_n`; every light block has
probability exactly `theta_n`; and `top` has probability `1-alpha_n`.
Given `P_1(x)`, membership in `A_top` and the block index are computed by one
comparison and one division of `w`-bit integers, so this categorical map is
efficiently evaluable rather than merely existential.

For any `r<=min(k_1,k_2)` distinct keys, their complete labels under (2.3)
are iid with this categorical distribution.  This follows because polynomial
evaluation at `r` distinct field points is uniform in `GF(2^w)^r`,
deterministic maps preserve independence, and the two polynomial seeds are
independent.

## 3. Limited-independence block-load lemma

The following standard moment form is sufficient.

### Lemma 3.1

Let `X_1,...,X_N` be `2r`-wise independent Bernoulli variables with common
mean `theta`, let `S=sum_i X_i`, and put `mu=N theta`.  There is an absolute
constant `C` such that

\[
\mathbb E|S-\mu|^{2r}
\le \bigl(C(r\mu+r^2)\bigr)^r.
\tag{3.1}
\]

#### Proof

After replacing every power `X_i^a`, `a>=1`, by `X_i`, the polynomial
`(S-mu)^{2r}` involves at most `2r` distinct variables in each monomial.
Its expectation is therefore identical to the expectation for fully
independent Bernoulli variables.

For the independent sum, Bernstein's inequality gives

\[
\Pr[|S-\mu|\ge u]
\le 2\exp\left(-{u^2\over 2(\mu+u/3)}\right).
\]

Integrating
`2r int_0^infinity u^{2r-1} Pr[|S-mu|>=u] du`, splitting at `u=mu`,
and applying the Gamma integral on each part yields (3.1), after changing
an absolute constant.  This also proves the result when `mu<r`.  `square`

### Corollary 3.2

Fix constants `c,d>0` and put `K=c+d+4`.  There are constants `gamma,A>0`,
depending only on `lambda,c,d`, such that, with

\[
r=\lceil\gamma\log n\rceil,
\qquad k_1\ge2r,
\qquad
s_{\max}=\left\lceil\lambda_n b+A\sqrt{b\log n}\right\rceil,
\tag{3.2}
\]

the number `S` of active keys mapped to any fixed light block at any fixed
endpoint satisfies

\[
\Pr[S>s_{\max}]\le n^{-K}.
\tag{3.3}
\]

#### Proof

At a fixed endpoint the active set is fixed independently of the seed and
has cardinality at most `n`.  Its block indicators are `k_1`-wise independent
Bernoulli variables of mean `theta_n=t/M`, and

\[
\mu\le n\theta_n=\lambda_n b.
\]

Since `b=Theta(log^4 n)` and `r=Theta(log n)`, for large `n` equation (3.1)
and Markov's inequality give

\[
\Pr[S-\mu>A\sqrt{b\log n}]
 \le\left({C'\gamma\over A^2}\right)^r.
\]

First choose `gamma` large enough and then `A` so that the right side is at
most `n^{-K}`.  The rounding errors in (3.2) can be absorbed by increasing
`A`.  `square`

There are `B=Theta(n/b)` light blocks and at most `n^c+1` endpoint states.
Taking `K=c+d+4` leaves more than enough slack for a union bound over every
block-time pair.

## 4. Exact transfer of the information-density tail

Set

\[
k_2=s_{\max}.
\tag{4.1}
\]

Fix an endpoint and a block, and condition on the entire first polynomial
`P_1`.  This conditioning determines the set `V` of active keys assigned to
the block and its size `S`, but it reveals no information about the
independent polynomial `P_2`.  On the event `S<=s_max=k_2`, the values

\[
(\pi(P_2(x)))_{x\in V}
\]

are **fully independent** uniform coordinates in `[b]`.  Therefore,
conditional on `P_1` and `S=s<=s_max`, the block occupancy vector is exactly

\[
\operatorname{Mult}(s;1/b,\ldots,1/b).
\tag{4.2}
\]

In particular, every statement in Sections 2--3 of
`FIXED_SLOT_BLOCK_CODER_HOSTILE_AUDIT.md` applies without approximation.  If
the common slot has length

\[
L=bH_2(\operatorname{Pois}(\lambda_n))
 +D\sqrt{b\log n}\log b+O(1),
\tag{4.3}
\]

then, uniformly for all `s<=s_max`, the conditional probability that the
histogram is not codeable is at most `n^{-K}`.  Averaging over `P_1` preserves
the same bound.

Combining this with (3.3), a fixed block-time pair is bad with probability at
most `2n^{-K}`.  Hence

\[
\Pr[\text{some bad block in the whole history}]
\le 2B(n^c+1)n^{-K}<n^{-d}
\tag{4.4}
\]

for all sufficiently large `n`.  Independence between blocks or endpoint
states is neither asserted nor required.

This two-level argument is the reason the information-density issue closes.
A single `Theta(log n)`-wise independent categorical hash transfers low
moments of the block total, but it does not automatically transfer the
high-degree histogram codeability event.  Equation (4.2) supplies the exact
law on every endpoint for which the code is required to operate.

## 5. Pointwise false-positive probability

Limited independence also suffices for the pointwise FPR, although it does
not give the exact expression under full independence.

Fix a query key `x` outside the active set `S`, where `|S|=N<=n`.  For
`y in S`, let `E_y` be the event that `x` and `y` receive the same light
cell.  For every `r` with `r+1<=min(k_1,k_2)`, and every distinct
`y_1,...,y_r`,

\[
\Pr[x\text{ is light and }E_{y_1}\cap\cdots\cap E_{y_r}]
=\sum_{\ell\text{ light}}\Pr[h(x)=h(y_1)=\cdots=h(y_r)=\ell]
=q p_n^{r+1}=\alpha_n p_n^r,
\tag{5.1}
\]

where `q=Bb` and `q p_n=alpha_n`.

Let `m` be odd and `m+2<=min(k_1,k_2)`.  Bonferroni's inequality and (5.1)
give

\[
\Pr[x\text{ is light and some }E_y]
\le \alpha_n\sum_{r=1}^m(-1)^{r+1}{N\choose r}p_n^r.
\tag{5.2}
\]

For a deterministic number `Z` of occurring events,

\[
\sum_{r=1}^m(-1)^{r+1}{Z\choose r}-\mathbf1[Z\ge1]
= {Z-1\choose m}\mathbf1[Z\ge m+1]
\le {Z\choose m+1}.
\]

Taking expectations in the fully independent comparison experiment yields

\[
\Pr[x\text{ is light and some }E_y]
\le \alpha_n\bigl(1-(1-p_n)^N\bigr)
 +\alpha_n{N\choose m+1}p_n^{m+1}.
\tag{5.3}
\]

Since `Np_n<=lambda_n=Theta(1)`, the remainder is at most

\[
\left({e\lambda_n\over m+1}\right)^{m+1}.
\tag{5.4}
\]

Choosing an odd

\[
m=Theta((c+d+1)\log n/\log\log n)
\]

makes (5.4) at most any prescribed inverse polynomial.  This is already
smaller than `k_1=Theta(log n)` used for the block-load tail.

Adding the top probability and the history-wide overflow event gives, for
every fixed nonmember query at every fixed endpoint,

\[
\Pr[\mathrm{FP}(x)]
\le 1-\alpha_n
 +\alpha_n\bigl(1-(1-p_n)^N\bigr)
 +n^{-D}+n^{-d}.
\tag{5.5}
\]

As in the oracle construction, choose the base collision parameters for
error `epsilon-eta_n`, for example `eta_n=1/log n`.  Equations (2.2), (5.4),
and (4.4) are all `o(eta_n)`, so the final pointwise FPR is at most the target
`epsilon` for sufficiently large `n`.

The argument remains valid if `x` appeared earlier in the fixed history:
only the current active set must exclude `x`.  Seed independence of the
history ensures that the active set and query key are fixed before the two
polynomials are sampled.

## 6. Space and evaluation cost

The number of light cells is `q=Bb`, and by (2.1)

\[
qH_2(\operatorname{Pois}(\lambda_n))
=\alpha_n n\,{H_2(\operatorname{Pois}(\lambda_n))\over\lambda_n}.
\tag{6.1}
\]

Together with (2.2), continuity of Poisson entropy, and the block-coder
redundancy, this is

\[
\alpha n\,{H_2(\operatorname{Pois}(\lambda))\over\lambda}+o(n).
\tag{6.2}
\]

The persistent hash representation consists of `k_1+k_2` field coefficients,
the integers `t,B,b`, and a description of the fixed field representation and
projection.  It uses

\[
O((k_1+k_2)w)=O(\log^5 n)=o(n)
\]

bits.  The first polynomial takes `O(k_1)` field operations to evaluate and
the second takes `O(k_2)`.  Arithmetic in `GF(2^w)` on `w=O(log n)` bits can
be performed in `poly(w)` word operations by elementary shift/XOR polynomial
arithmetic.  Thus one complete hash evaluation, including block selection and
the within-block coordinate, takes `log^{O(1)} n` worst-case word operations.

For `top` keys it is unnecessary to evaluate `P_2`: evaluate `P_1` first and
stop.  Light-key updates and queries evaluate both hashes and then perform one
`log^{O(1)} n` block decode/re-encode or partial decode.  The resulting full
filter, not merely its multiset core, therefore has polylogarithmic worst-case
operation time.

## 7. Formal hashing lemma for insertion into the main theorem

### Theorem 7.1 (short-seed efficient partition)

Fix constants `lambda>0`, `alpha in (0,1]`, and `c,d>0`.  Let
`U subseteq {0,1}^w`, where `log n<=w=O(log n)`.  There is a static hash
family represented by `log^{O(1)} n` bits and evaluable in
`log^{O(1)} n` worst-case word operations with the following property.

For every legal capacity-`n` history of at most `n^c` operations, fixed
independently of the hash seed, the fixed-slot dynamic fingerprint multiset
built from this family uses

\[
\alpha n{H_2(\operatorname{Pois}(\lambda))\over\lambda}+o(n)
\]

total bits, including the hash seed, metadata, and scratch space, and:

1. outside a sticky ALL-YES state, all light-cell multiplicities are exact;
2. the probability of entering the sticky state anywhere in the history is
   at most `n^{-d}`;
3. every operation takes `log^{O(1)} n` worst-case word operations;
4. before the sticky-state contribution, every fixed nonmember has false-
   positive probability
   \[
   1-\alpha+\alpha(1-e^{-\lambda})+o(1),
   \]
   with the `o(1)` made smaller than any prescribed inverse polynomial plus
   the parameter-rounding error.

Using a vanishing FPR margin converts item 4 and the sticky-state probability
to the exact target pointwise FPR while changing space by only `o(n)`.

The theorem assumes ordinary set histories: active universe keys are
distinct.  Repeated operations on the same inactive/active key must obey the
usual legal dynamic-set semantics.  This is necessary because polynomial
hash evaluations at repeated inputs are identical, not independent balls.

## 8. Why the proposed single-hash truncated-polynomial route is unsafe

There is a tempting alternative argument: truncate all cell counts at
`K_0`, interpolate `log(c!)` by a degree-`K_0` Newton polynomial, and transfer
a high centered moment under `2rK_0`-wise independence.  As stated, that
argument has a gap.  The interpolation polynomial agrees with `log(c!)` only
for `c<=K_0`; outside that interval it can grow as `c^{K_0}`.  Moment matching
therefore transfers the moment of the polynomial on the entire probability
space, including the rare high-count event, and a separate bound on
`Pr[max C_i>K_0]` does not by itself bound the polynomial's contribution on
that event.  A bounded low-degree sandwich polynomial might repair the route,
but it is unnecessary.

The two-level construction above avoids this issue completely: `P_1`
controls the number of keys in a block, and `P_2` supplies literal full
independence for all those keys whenever the block is within its allocated
capacity.
