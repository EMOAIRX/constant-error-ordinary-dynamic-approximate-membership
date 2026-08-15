# Public-hash conditional converse for random fingerprint occupancies

Status: superseded by the sharper and fully audited
`PUBLIC_HASH_CONDITIONAL_ENTROPY.md`.

This note removes the public-randomness gap in the fingerprint-multiset
converse. The lower bound does not require a polynomial-tail conditional AEP.
An `o(n)` mutual-information bound, followed by Fano's inequality, is enough.

All logarithms and divergences below are base two.

## 1. Setup

Let `U` be a universe of size `u`. Let

\[
h:U\to\{0,1,\ldots,q\}
\]

be a fully random categorical map: the values `h(x)` are independent and

\[
\Pr[h(x)=j]=p_j.
\]

Category `0` may be the permanent-YES category. Let `S` be a uniformly random
`n`-subset of `U`, independently of `h`, and let

\[
N_j=|\{x\in S:h(x)=j\}|.
\]

The full vector `N=(N_0,...,N_q)` has the unconditional distribution

\[
N\sim\operatorname{Mult}(n;p_0,\ldots,p_q).
\]

If the data structure stores only tracked categories `1,...,q`, then `N_0`
is determined by their sum and the known current set size. Hence omitting
`N_0` does not change the entropy.

## 2. Public-hash leakage lemma

### Lemma 2.1

For the preceding experiment,

\[
I(N;h)
\le
\log_2\frac{u^n}{(u)_n}
+\frac{nq}{u\ln 2},
\tag{1}
\]

where `(u)_n=u(u-1)\cdots(u-n+1)`.

Consequently, if `q=O(n)` and `u/n\to\infty`, then

\[
I(N;h)=o(n)
\quad\text{and}\quad
H(N\mid h)=H(N)-o(n).
\tag{2}
\]

### Proof

Sample an ordered sequence `X=(X_1,...,X_n)` uniformly without replacement
from `U`, and put

\[
L=(h(X_1),\ldots,h(X_n)).
\]

The occupancy vector `N` is a function of `L`, so data processing gives

\[
I(N;h)\le I(L;h).
\tag{3}
\]

Unconditionally, the sampled keys are distinct and the random variables
`h(X_i)` are values of a fully random map at distinct arguments. Therefore

\[
L\sim p^{\otimes n}.
\]

For a fixed map `h`, let

\[
\widehat p_j=\frac{|h^{-1}(j)|}{u}
\]

be its empirical category law, and write `P_h` for the conditional law of
`L` given `h`. Each coordinate of `P_h` has marginal `\widehat p`. Hence

\[
\begin{aligned}
D(P_h\|p^{\otimes n})
&=D(P_h\|\widehat p^{\otimes n})
  +\mathbb E_{P_h}\sum_{i=1}^n
      \log_2\frac{\widehat p_{L_i}}{p_{L_i}}\\
&=D(P_h\|\widehat p^{\otimes n})
  +nD(\widehat p\|p).
\end{aligned}
\tag{4}
\]

The law `P_h` is obtained by applying `h` coordinatewise to a uniform ordered
sample without replacement. The law `\widehat p^{\otimes n}` is obtained by
applying the same map to `n` independent uniform universe samples. By data
processing,

\[
D(P_h\|\widehat p^{\otimes n})
\le
D(X_{\rm wor}\|X_{\rm wr})
=\log_2\frac{u^n}{(u)_n}.
\tag{5}
\]

Here the last identity holds because the without-replacement law is uniform
on the `(u)_n` distinct ordered tuples, while the with-replacement law assigns
each such tuple probability `u^{-n}`.

The empirical law `\widehat p` is the frequency vector of `u` independent
categorical samples from `p`. Using

\[
D_2(a\|b)\le\frac1{\ln2}\chi^2(a,b)
\]

and the multinomial variances,

\[
\begin{aligned}
\mathbb E_h D(\widehat p\|p)
&\le
\frac1{\ln2}\sum_{j:p_j>0}
\frac{\mathbb E(\widehat p_j-p_j)^2}{p_j}\\
&=
\frac1{u\ln2}\sum_{j:p_j>0}(1-p_j)\\
&\le\frac q{u\ln2}.
\end{aligned}
\tag{6}
\]

Finally,

\[
I(L;h)=\mathbb E_hD(P_h\|p^{\otimes n}),
\]

so (4)--(6) imply (1). Moreover,

\[
\log_2\frac{u^n}{(u)_n}
=\sum_{i=0}^{n-1}-\log_2(1-i/u)
=O(n^2/u)
\]

when `n/u=o(1)`. With `q=O(n)`, both terms in (1) are `o(n)` whenever
`u/n\to\infty`. This proves (2). `square`

## 3. Fixed-memory converse

### Theorem 3.1

Consider a fingerprint-multiset core using a fixed `B`-bit memory block. Its
random tape, including `h`, is public and free. On every fixed legal build
history for a set of size `n`, independently of the tape, suppose that with
probability at least `1-delta_n` the final normal state permits exact recovery
of every tracked multiplicity. Assume

\[
q=O(n),\qquad u/n\to\infty,\qquad \delta_n=o(1).
\]

Then, for

\[
N\sim\operatorname{Mult}(n;p_0,\ldots,p_q),
\]

the memory satisfies

\[
B\ge H(N)-o(n).
\tag{7}
\]

### Proof

Draw `S` uniformly among the `n`-subsets and build it in any canonical order.
For each realized `S`, this is a fixed history independent of the random tape,
so averaging the promised failure probability over `S` gives joint decoding
error at most `delta_n`.

Let `M` be the final `B`-bit memory state and include all public random coins
in `R`. On a normal state, exact count queries recover the tracked vector and
hence the full vector `N`. Thus a decoder using `(M,R)` reconstructs `N` with
error probability at most `delta_n`.

The number of possible tracked occupancy vectors is at most

\[
\binom{n+q}{q}=2^{O(n)}
\]

for `q=O(n)`. Fano's inequality therefore gives

\[
H(N\mid M,R)
\le h_2(\delta_n)
  +\delta_n\log_2\binom{n+q}{q}
=o(n).
\tag{8}
\]

The coins other than `h` are independent of `(S,h)` and hence reveal no
additional information about `N` once `h` is given. Lemma 2.1 gives

\[
H(N\mid R)=H(N\mid h)=H(N)-o(n).
\tag{9}
\]

Therefore

\[
\begin{aligned}
H(N)-o(n)
&=H(N\mid R)\\
&\le I(N;M\mid R)+H(N\mid M,R)\\
&\le H(M)+o(n)\\
&\le B+o(n),
\end{aligned}
\]

which proves (7). `square`

## 4. Consequence for heterogeneous fingerprints

The theorem reduces the public-seed lower bound to the ordinary entropy of a
heterogeneous multinomial source. Under the regular load assumptions used in
the main theorem,

\[
\frac1nH(N)
=\int r(\lambda)\,d\nu(\lambda)+o(1).
\]

Thus the public hash function does not invalidate the first-order occupancy
converse, even in the full regime `|U|=omega(n)` relevant to constant error.

This argument is deliberately only for exact fingerprint-multiset cores. It
does not imply that an arbitrary approximate-membership filter must encode
`N`, and therefore does not solve the arbitrary-filter lower-bound half of
the KLZ25 open problem.

## 5. Why this is preferable to conditional smooth max entropy

The fixed-space lower bound needs only `delta_n=o(1)`, because the support of
the occupancy vector has logarithm `O(n)`. Fano absorbs the failed executions
in `o(n)` bits. There is consequently no need to prove a polynomial-tail
conditional AEP or to control the information density of `N|h` at probability
`n^{-d}`. The polynomial failure exponent remains relevant to the dynamic
upper bound, but not to this first-order converse.
