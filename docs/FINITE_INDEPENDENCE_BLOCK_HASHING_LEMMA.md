# Finite-independence replacement for the random-partition oracle

## 1. Purpose and conclusion

The fixed-slot block coder does **not** require a fully random function
oracle.  It is enough to use two independent finite-independence hashes:

* an outer hash that chooses `top` or one of the light blocks, with
  `Theta(log n)`-wise independence; and
* an inner hash that chooses a cell inside the selected light block, with
  `Theta(log^2 n)`-wise independence.

The separation into two hashes is important.  Conditional on a light block
receiving at most `s_max` current keys, the inner values on exactly those
keys are genuinely independent uniforms.  Thus the conditional multinomial
law used by the arithmetic coder remains exact.  There is no need to prove
an information-density inequality directly under limited independence.

For a polynomial universe, both hashes can be represented by
`O(log^3 n)` bits and evaluated in `log^{O(1)} n` word operations.  Hence the
conditional-oracle qualification in Section 8 of
`FIXED_SLOT_BLOCK_CODER_HOSTILE_AUDIT.md` can be removed, at the cost of
using `b=Theta(log^2 n)` and advertising polylogarithmic, rather than
constant, hash evaluation time.

## 2. Hash construction

Assume that universe keys inject into the field `F=GF(2^w)`, where
`w=Theta(log n)`.  Let

\[
 b=2^{\lceil 2\log_2\log_2 n\rceil}=\Theta(\log^2 n)
\]

and choose the number `B=Theta(n/b)` of light blocks as in the target
mixture.  Choose an integer `m` such that

\[
 \delta=\frac m{|F|}=\frac{\lambda b}{n}+O(n^{-C_0})
\]

and `Bm<=|F|`. Increasing `w` by a sufficiently large constant factor makes
the displayed rounding error `O(n^{-C_0})` for any prescribed constant
`C_0`. Partition `Bm` field elements into `B` equal intervals of
size `m`; all remaining field elements form `top`.

Let `G:F->F` be a uniformly random polynomial of degree at most
`k_out-1`.  The outer label `g(x)` is the block whose interval contains
`G(x)`, or `top`.  Thus each block has probability exactly `delta`, and the
outer labels of any at most `k_out` distinct keys are independent.

Independently choose a uniformly random polynomial `H:F->F` of degree at
most `k_in-1`.  Let `h(x)` be a fixed surjective linear projection of
`H(x)` onto `log_2 b` bits.  The values `h(x)` of any at most `k_in`
distinct keys are independent and uniform on `[b]`.

The final light-cell label is `(g(x),h(x))`.  Its probability is

\[
 p=\delta/b,
 \qquad
 \lambda_n=np=n\delta/b=\lambda+o(1).
\]

The polynomial coefficients occupy

\[
 O((k_{\rm out}+k_{\rm in})w)
\]

bits.  Finite-field arithmetic and Horner evaluation take
`(k_out+k_in) log^{O(1)} n` word operations even without assuming
unit-cost carryless multiplication.

## 3. Outer-load lemma

We use the following standard limited-independence moment bound.

**Lemma 3.1 (Bernoulli moment bound).**  There is a universal constant `C`
such that, if `X_1,...,X_m` are `2r`-wise independent Bernoulli variables,
`S=sum_i X_i`, and `mu=E S`, then

\[
 \mathbb E|S-\mu|^{2r}
 \le [C(r\mu+r^2)]^r.                 \tag{3.1}
\]

Consequently

\[
 \Pr[|S-\mu|\ge t]
 \le \left(\frac{C(r\mu+r^2)}{t^2}\right)^r. \tag{3.2}
\]

One proof expands the centered `2r`-th moment.  Every monomial involves at
most `2r` coordinates, so its expectation is the same as under full
independence.  For independent Bernoullis, integrate the Bernstein tail
`2 exp(-t^2/(2(mu+t/3)))`; splitting the integral at `t=mu` gives
`E|S-mu|^(2r) <= [C(r mu+r^2)]^r`.  This proves (3.1) without importing a
limited-independence Chernoff theorem as a black box.

Fix a desired one-block exponent `K`.  At a fixed endpoint containing
`k<=n` keys, the number `S_j` assigned to outer block `j` is a sum of
`k_out`-wise independent Bernoulli variables with

\[
 \mu_j=k\delta\le n\delta=\lambda_n b.
\]

Take

\[
 r=\lceil \gamma\log n\rceil,
 \qquad k_{\rm out}=2r,
 \qquad
 t=A\sqrt{b\log n}.                 \tag{3.3}
\]

Here `gamma>0` is any fixed constant, and then `A=A(lambda,K,gamma)` is a
sufficiently large constant.  Since `b=Theta(log^2 n)`, equations
(3.2)--(3.3) give, uniformly in `j`, `k`, and the endpoint,

\[
 \Pr[S_j>\lambda_n b+A\sqrt{b\log n}]\le n^{-K}. \tag{3.4}
\]

Indeed, the ratio in (3.2) is at most
`C'(gamma lambda+o(1))/A^2`; choosing it below
`exp(-K/gamma-1)` proves (3.4).

Set

\[
 s_{\max}=\left\lceil\lambda_n b+A\sqrt{b\log n}\right\rceil,
 \qquad k_{\rm in}=s_{\max}.        \tag{3.5}
\]

Thus `k_in=Theta(log^2 n)`.

## 4. Exact conditional multinomial law

Fix an endpoint set `S` independently of both hash seeds, fix a block `j`,
and condition on the **entire outer assignment** of the keys of `S`, not
merely on its total.  Let

\[
 A_j=\{x\in S:g(x)=j\},\qquad s=|A_j|.
\]

The inner hash is independent of the outer hash.  If `s<=s_max=k_in`, then

\[
 (h(x):x\in A_j)
\]

is a vector of genuinely independent uniforms on `[b]`.  Therefore the
occupancy histogram `C_j` has the exact law

\[
 C_j\mid (g(x):x\in S)
 \sim \operatorname{Mult}(s;1/b,\ldots,1/b).     \tag{4.1}
\]

This proves more than conditioning only on `S_j=s`, and avoids the false
step of assuming that finite independence survives arbitrary conditioning.

Apply the fixed-slot coder's McDiarmid bound to (4.1).  With

\[
 L=bH_2(\operatorname{Pois}(\lambda_n))
   +D\sqrt{b\log n}\log b+O(1),      \tag{4.2}
\]

where `D=D(lambda,A,K)`, the conditional probability that a histogram with
`s<=s_max` is uncodeable is at most `n^{-K}`.  Averaging over the outer
assignment preserves this bound.  Combining with (3.4), a fixed
block-endpoint pair is bad with probability at most `2n^{-K}`.

For a seed-independent history of length `T<=n^c`, there are
`B(T+1)=O(n^{c+1}/b)` block-endpoint pairs.  Taking
`K>c+d+2` and union bounding gives history-wide sticky-overflow probability
at most `n^{-d}`.  Independence between blocks or times is not used.

The redundancy in (4.2), totals, padding, and scratch storage is

\[
 O\!\left(
 n\sqrt{\frac{\log n}{b}}\log b
 +\frac{n\log b}{b}
 +\frac{n\log n}{b}
 +b\log b
 +\log^3n
 \right)=o(n),                       \tag{4.3}
\]

where the last term includes both seeds.  Thus changing from
`b=log^4 n` to `b=Theta(log^2 n)` preserves the desired first-order rate.

## 5. Pointwise false-positive probability

Limited independence also suffices for the pointwise FPR calculation, but
the exact formula `1-(1-p)^k` must be replaced by a Bonferroni estimate.
Fix a nonmember `x` and an endpoint set of size `k<=n`.  Conditional on `x`
landing in a specified light cell, let `E_i` be the event that member `i`
lands in that cell.  For every `r` with

\[
 r+1\le \min(k_{\rm out},k_{\rm in}),
\]

the joint probability of any `r` distinct events is exactly `p^r`.
For an odd `R` below this independence threshold, Bonferroni gives

\[
 \Pr[\cup_iE_i\mid x\text{ is in that cell}]
 \le \sum_{r=1}^{R}(-1)^{r+1}{k\choose r}p^r.   \tag{5.1}
\]

For `R+1>kp`, the omitted binomial terms decrease in magnitude.  The right
side therefore differs from `1-(1-p)^k` by at most

\[
 {k\choose R+1}p^{R+1}
 \le \left(\frac{e\lambda_n}{R+1}\right)^{R+1}. \tag{5.2}
\]

Take an odd

\[
 R=\Theta((c+d+1)\log n/\log\log n).
\]

Then (5.2) is `n^{-Omega(c+d+1)}`.  Our choices
`k_out=Theta((c+d+1)log n)` and `k_in=Theta(log^2 n)` exceed `R+1`.
After averaging over the light cells, the pre-overflow pointwise FPR is

\[
 \beta_n+(1-\beta_n)(1-(1-p)^k)+n^{-\Omega(c+d+1)}, \tag{5.3}
\]

where `beta_n=1-Bdelta`.  The field-grid rounding error is `o(1)` and can,
together with (5.2) and the overflow probability, be absorbed by the same
vanishing FPR margin already used by the fixed-slot construction.

## 6. Formal replacement lemma

**Lemma 6.1 (efficient finite-independence partition).**  Fix constants
`lambda>0`, `alpha in (0,1]`, and `c,d>0`, and assume a universe of size
`n^{O(1)}` represented in `Theta(log n)`-bit words.  There is a distribution
over consistent maps from universe keys to `top` or
`B b=alpha n/lambda+o(n)` light cells with the following properties.

1. The map has a seed of `O(log^3 n)` bits and is evaluable in
   `log^{O(1)} n` worst-case word operations.
2. Against every legal seed-independent history of capacity `n` and length
   at most `n^c`, the fixed-slot multinomial block core with
   `b=Theta(log^2 n)` enters its sticky overflow state with probability at
   most `n^{-d}`.
3. Outside overflow it maintains exact light-cell multiplicities, and its
   total fixed allocation, including the two hash seeds, metadata, padding,
   and scratch space, is

   \[
   \alpha n\frac{H_2(\operatorname{Pois}(\lambda))}{\lambda}+o(n).
   \]

4. For every fixed nonmember query at every endpoint, its collision
   probability differs from the corresponding fully independent mixture by
   `n^{-Omega(c+d+1)}`.  Hence a vanishing parameter margin gives pointwise
   one-sided error at most the target `epsilon`, including overflow.

The construction and proof are Sections 2--5.

## 7. Why direct polynomial approximation is unnecessary

One tempting route is to interpolate `phi(t)=log(t!)` by a degree-`K_0`
Newton polynomial and match high moments of `sum_i phi(C_i)` using a
`Theta(K_0 log n)`-wise independent one-level hash.  This route needs extra
care that the two-level construction avoids:

* the interpolating polynomial agrees with `phi` only for `t<=K_0` and can
  grow very rapidly beyond the truncation point;
* conditioning on the event `max_i C_i<=K_0` destroys moment matching;
* a full-independence bounded-difference moment for the true `phi` does not
  automatically bound the untruncated interpolating polynomial.

One can probably repair the argument using a clipped polynomial and a
separate witness expansion, but it gives no better asymptotic seed or time
for the present theorem.  The outer/inner split makes the multinomial law
literally exact on every nonoverflow block and is therefore the safer proof.
