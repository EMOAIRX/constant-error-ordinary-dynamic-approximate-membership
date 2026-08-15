# Public hash side information for a random fingerprint multiset

## 1. Setting and the correct conditional object

Let `m=|U|`, let `S` be a uniformly random `n`-subset of `U`, and let

\[
h:U\longrightarrow [q]
\]

assign the keys independently with categorical law
`p=(p_1,...,p_q)`.  The set and the hash function are independent.  Write

\[
N_j=|S\cap h^{-1}(j)|,
\qquad
C_j=|h^{-1}(j)|.
\]

Marginally, `N` has law `Mult(n,p)`.  Conditional on the public hash tape,
however, it is multivariate hypergeometric:

\[
\Pr[N=a\mid h]
=\Pr[N=a\mid C]
=\frac{\prod_j {C_j\choose a_j}}{{m\choose n}}.
\]

Thus `C` is sufficient side information: `N` and `h` are conditionally
independent given `C`.  This is the point that must replace an unconditional
multinomial-entropy assertion in the converse.

All logarithms below are natural unless a subscript 2 is displayed.

## 2. Exact mutual-information identities

### Proposition 2.1

Let `M_k` denote a random vector with law `Mult(k,p)`.  Then

\[
\boxed{
I(N;h)=I(N;C)=H(M_m)-H(M_{m-n}).
}
\]

Moreover, if `\widehat p_k=M_k/k`, then

\[
\boxed{
I(N;h)
=\sum_{k=m-n+1}^{m}
  \mathbb E D(\widehat p_k\Vert p).
}
\]

#### Proof

The conditional hypergeometric law depends on `h` only through `C`, proving
sufficiency.  In the joint law of `(N,C)`, expose the labels of the sampled
and unsampled keys in a uniformly random order.  Then

\[
C=N+R,
\qquad
N\sim\operatorname{Mult}(n,p),
\quad
R\sim\operatorname{Mult}(m-n,p),
\]

with `N` and `R` independent.  Hence

\[
I(N;C)=H(C)-H(C\mid N)=H(M_m)-H(M_{m-n}).
\]

For the second identity, couple `M_k` as the type of iid labels
`X_1,...,X_k`.  The map

\[
(M_{k-1},X_k)\longleftrightarrow(M_k,X_k)
\]

is bijective, while `X_k` is independent of `M_{k-1}`.  Exchangeability
gives `\Pr[X_k=j\mid M_k]=M_{k,j}/k`.  Consequently

\[
\begin{aligned}
H(M_k)-H(M_{k-1})
&=H(p)-H(X_k\mid M_k)\\
&=H(p)-\mathbb E H(\widehat p_k)\\
&=\mathbb E D(\widehat p_k\Vert p).
\end{aligned}
\]

Telescoping proves the claim.  \(\square\)

In particular, the requested conditional Shannon entropy has the exact
finite-universe expression

\[
\boxed{
H(N\mid h)
=H(M_n)-H(M_m)+H(M_{m-n}).
}
\]

### Corollary 2.2: a distribution-free upper bound

If all `p_j>0`, then

\[
\mathbb E D(\widehat p_k\Vert p)\le \frac{q-1}{k}
\]

and therefore

\[
\boxed{
I_2(N;h)
\le \frac{q-1}{\ln 2}
\sum_{k=m-n+1}^{m}\frac1k
\le \frac{(q-1)n}{(m-n+1)\ln 2}.
}
\]

Indeed, `log x <= x-1` gives

\[
\begin{aligned}
\mathbb E D(\widehat p_k\Vert p)
&\le
\sum_j\frac{\mathbb E\widehat p_{k,j}^2}{p_j}-1\\
&=\frac{q-1}{k}.
\end{aligned}
\]

In particular, if `q=Theta(n)` and `m/n -> infinity`, then

\[
I(N;h)=O(n^2/m)=o(n).
\]

No lower bound on the individual `p_j` is needed for this Shannon bound.

### Proposition 2.3: the first-order side-information saving

Suppose, for fixed constants `0<a<=A<infinity`,

\[
\frac an\le p_j\le\frac An
\quad(1\le j\le q),
\qquad L=\frac mn\longrightarrow\infty.
\]

Then

\[
I(N;h)
=\frac{q-1}{2}
  \sum_{k=m-n+1}^{m}\frac1k
  +O_{a,A}\!\left(\frac{n}{L^{3/2}}\right)
\]

in nats.  Equivalently,

\[
I_2(N;h)
=\frac{q-1}{2\ln 2}\log\frac m{m-n}
  +O_{a,A}\!\left(\frac{n}{L^{3/2}}+\frac{n^2}{m^2}\right).
\]

The expansion follows cell by cell from

\[
p_j\,\mathbb E\left[
\frac{B_j}{kp_j}\log\frac{B_j}{kp_j}
\right]
=\frac{1-p_j}{2k}
+O_{a,A}\!\left(p_j(kp_j)^{-3/2}\right),
\]

where `B_j~Bin(k,p_j)`.  To justify the uniform remainder, put
`Y=(B_j-kp_j)/(kp_j)` and expand
`(1+Y)log(1+Y)` through second order on `|Y|<=1/2`.  The remainder is at
most a constant times `|Y|^3`, and the binomial third absolute central
moment is `O((kp_j)^{3/2})`.  On the complementary event, summation of the
binomial Chernoff tail (rather than multiplication by the maximum possible
value) gives an exponentially small contribution.  Since
`kp_j >= a(L-1)`, this is uniformly
`O(p_j(kp_j)^{-3/2})`.  Summing over `j` and then over the `n` values of `k`
gives the displayed estimate.

This asymptotic is not needed to prove `o(n)`, but it quantifies exactly how
much first-order space the public population histogram can save.

## 3. Polynomial-tail information-density bound

An `o(n)` Shannon mutual information bound alone is not enough for a fixed
memory theorem with failure `n^{-D}`.  The necessary stronger fact is that
the *upper tail* of the information density is `o(n)` with polynomially high
probability.

### Proposition 3.1

Under the regularity assumptions of Proposition 2.3, for every fixed
`D>0` there is a deterministic `b_{n,D}=o(n)` such that

\[
\Pr\left[
\imath(N;h)>b_{n,D}
\right]\le n^{-D},
\]

where

\[
\imath(N;h)
=\log\frac{\Pr[N\mid h]}{\Pr[N]}
=\log\frac{\Pr[N\mid C]}{\Pr[N]}.
\]

One admissible (non-optimized) order is

\[
b_{n,D}
=O_{a,A,D}\!\left(
\frac n{\sqrt L}
+\sqrt{\frac{n\log n}{\sqrt L}}
+\frac{\log^2 n}{L\log\log n}
\right)
+O\!\left(\frac nL\right).
\]

#### Proof

For a jointly realized pair `N=a`, `C=c`, the hypergeometric likelihood
ratio is

\[
\imath(a;c)
=\log\frac{m^n}{(m)_n}
+\sum_j\sum_{r=0}^{a_j-1}
  \log\frac{c_j-r}{mp_j}.
\]

Using `log x<=x-1` and discarding a nonpositive depletion term gives

\[
\imath(N;C)
\le A_{m,n}
+\sum_j\frac{N_j(C_j-mp_j)}{mp_j},
\tag{3.1}
\]

where

\[
A_{m,n}=\log\frac{m^n}{(m)_n}
\le\frac{n(n-1)}{2(m-n+1)}=O(n/L).
\]

Write `C=N+R`, with `R~Mult(m-n,p)` independent of `N`.  The last sum in
(3.1) splits as

\[
Z_N=\sum_j\frac{N_j(N_j-np_j)}{mp_j},
\qquad
Z_R=\sum_j\frac{N_j(R_j-(m-n)p_j)}{mp_j}.
\]

For every fixed `D`, standard balls-into-bins Chernoff bounds give

\[
\max_jN_j
\le B_D=O_{A,D}(\log n/\log\log n)
\]

with failure at most `n^{-D-2}`.  Also, with the same failure allowance,

\[
\sum_jN_j^2\le (1+A)n+n\sqrt L.
\tag{3.2}
\]

For completeness, (3.2) follows by applying bounded differences to
`sum_j min(N_j,B_D)^2`; changing one ball changes this truncated statistic
by at most `4B_D+2`, its expectation is at most
`E sum_j N_j^2 <= (1+A)n`, and

\[
\exp\left(-\Omega(nL/B_D^2)\right)=n^{-\omega(1)}.
\]

On (3.2),

\[
Z_N
\le\frac1{aL}\sum_jN_j^2
=O_{a,A}(n/\sqrt L+n/L)=o(n).
\]

Conditional on `N`, `Z_R` is a sum of `m-n` centered iid variables with

\[
\operatorname{Var}(Z_R\mid N)
\le\frac1m\sum_j\frac{N_j^2}{p_j}
\le\frac1{aL}\sum_jN_j^2
=O_{a,A}(n/\sqrt L+n/L)
\]

and summand bound at most `B_D/(aL)`.  Bernstein's inequality, with a
constant chosen according to `D`, yields

\[
Z_R
\le O_{a,A,D}\!\left(
\sqrt{\frac{n\log n}{\sqrt L}}
+\frac{B_D\log n}{L}
\right)
\]

except with probability `n^{-D-2}`.  Combining these estimates in (3.1)
proves the proposition.  \(\square\)

The estimate deliberately sacrifices the sharp mean `Theta(n/L)` in order
to remain valid for every diverging `L`, even one growing more slowly than
`log log n`.

## 4. Conditional polynomial-smooth support entropy

To avoid a terminology ambiguity, define the classical fixed-length source
coding quantity explicitly.  For `delta in (0,1)`, let

\[
H_{0}^{\delta}(N\mid h)
=\min_{E:\Pr[(N,h)\in E]\ge1-\delta}
  \max_h\log_2|\{a:(a,h)\in E\}|.
\tag{4.1}
\]

Rare hash tapes may be discarded as part of the total failure event.  For
each retained tape, (4.1) is the logarithm of the largest required codebook.
This is the operational `conditional smooth max/support entropy` relevant to
a fixed preallocated memory block.  It is often denoted `H_0^delta`, rather
than the quantum-information quantity also called `H_max`.

### Theorem 4.1

Under

\[
q=\Theta(n),\qquad
\frac an\le p_j\le\frac An,\qquad
\frac mn\longrightarrow\infty,
\]

for every fixed `D>0`,

\[
\boxed{
H_{0}^{n^{-D}}(N\mid h)
=H_2(\operatorname{Mult}(n,p))+o(n).
}
\]

The two `o(n)` terms can be chosen uniformly over all arrays satisfying the
displayed fixed constants `a,A,D` and any specified diverging lower bound on
`m/n`.

#### Proof

First establish a polynomial-tail AEP for the marginal multinomial source.
Its surprisal is

\[
J(N)=-\log\Pr[N].
\]

Changing one of the `n` iid categorical draws changes `J` by at most

\[
\log(nA/a)+O(1).
\]

McDiarmid's inequality therefore implies, for every fixed `D`,

\[
\Pr[|J(N)-H(N)|>a_{n,D}]\le n^{-D-2},
\qquad
a_{n,D}=O_{a,A,D}(\sqrt n\,\log^{3/2}n)=o(n).
\tag{4.2}
\]

For the upper bound in (4.1), take the same marginal typical set for every
hash tape:

\[
T=\{a:-\log_2\Pr[N=a]\le H_2(N)+a_{n,D}/\ln2\}.
\]

Equation (4.2) gives polynomially small discarded mass, while

\[
|T|\le2^{H_2(N)+a_{n,D}/\ln2}.
\]

For the lower bound, use

\[
-\log\Pr[N\mid h]=J(N)-\imath(N;h).
\]

Proposition 3.1 and the lower-tail half of (4.2), with constants tuned so
that their total exceptional probability is at most `n^{-D}/2`, show that

\[
\Pr\left[
-\log_2\Pr[N\mid h]
<H_2(N)-c_{n,D}
\right]\le n^{-D}/2,
\qquad c_{n,D}=o(n).
\tag{4.3}
\]

If an event `E` has at most `M` retained values of `N` above each hash tape,
then (4.3) gives

\[
\Pr[(N,h)\in E]
\le n^{-D}/2+M2^{-H_2(N)+c_{n,D}}.
\]

To make the left side at least `1-n^{-D}`, one needs

\[
\log_2M\ge H_2(N)-c_{n,D}+O(1).
\]

Together with the typical-set upper bound this proves the theorem.
\(\square\)

## 5. Boundaries and counterexamples

1. **The condition `m/n -> infinity` is substantive.**  If `m=n`, then
   `S=U`, so `N=C` is determined by the public hash and
   `H(N|h)=0`, while `H(Mult(n,p))=Theta(n)` in the regular regime.  More
   generally, if `m/n` stays bounded above one, Proposition 2.3 gives a
   `Theta(n)` side-information saving.

2. **The number of positive cells matters.**  Corollary 2.2 only gives
   `I(N;h)=o(n)` when `qn/m=o(n)`.  With `q=Theta(n)` this is exactly supplied
   by `m/n -> infinity`; an enormous dust alphabet can invalidate the
   conclusion and also destroys the polynomial-tail AEP.

3. **Independence of the source and hash is essential.**  If the current set
   is chosen after seeing the public hash, `N|h` need not be hypergeometric
   and can be concentrated on exceptional cells.  The theorem applies to a
   uniform random lower-bound source, or to an oblivious history whose keys
   are fixed independently of the seed, not to a seed-adaptive workload.

4. **A fixed set is not itself a conditional-entropy source.**  For a named
   fixed `S`, `N` is deterministic once `h` is public.  The converse uses a
   random `S` and averages a per-fixed-set correctness guarantee over that
   source.  This is the standard Yao/source-coding step and must be stated.

## 6. A permanent-positive category and finitely many heavy cells

The phase-transition construction has a distinguished `top` category of
constant probability `beta`; keys mapped there are answered YES without
storing a count.  This category is not covered literally by the hypothesis
`p_j=Theta(1/n)`.  It is nevertheless harmless, for two separate reasons.

First, the exact identities and Shannon bound in Section 2 hold for an
arbitrary categorical law.  If the vector contains `r=O(1)` heavy categories
and `q=Theta(n)` light categories, Corollary 2.2 still gives

\[
I(N;h)=O(qn/m)=o(n).
\]

Second, the polynomial-smooth theorem extends directly to finitely many
heavy categories, provided the total light mass is bounded away from zero.
The proof of Proposition 3.1 is unchanged for the light cells.  For a heavy
cell, `p_j=Theta(1)`, its contribution to `Z_N` is `O(n/L)` on the usual
binomial typical event, its contribution to the conditional variance of
`Z_R` is also `O(n/L)`, and its centered summand is `O(1/L)`.  There are only
`O(1)` such cells.  In the marginal AEP, changing one categorical draw still
changes the multinomial surprisal by only `O(log n)`, because the ratio of
the largest heavy probability to the smallest light probability is `O(n)`.
Consequently the same argument gives

\[
H_0^{n^{-D}}(N_{\rm full}\mid h)
=H_2(N_{\rm full})+o(n).
\]

For one permanent-positive category, its count is already determined by
the tracked vector through

\[
N_{\top}=n-\sum_{j\in\mathrm{light}}N_j.
\]

Thus deleting `top` from the represented vector loses no entropy.  In the
Poisson load integral it is exactly the endpoint `lambda=infinity`, whose
per-key rate is zero.  The conditional-smooth converse can therefore be
stated for the full vector and then transferred *exactly* to the represented
light vector by this bijection.  Although the heavy count itself has only
`O(log n)` Shannon entropy, that observation alone would not be enough for a
polynomial-tail fixed-memory theorem; the direct information-density
extension above is the required justification.

## 7. Consequence for the fingerprint-multiset converse

Suppose a normal state must recover the exact occupancy vector and an
`H`-bit fixed memory block overflows with probability at most `n^{-D}` for
every fixed set, over the public random hash.  Average this guarantee over a
uniform random `n`-subset `S`.  For each public tape, at most `2^H`
occupancies can be represented in normal states.  Theorem 4.1 therefore
implies

\[
H\ge H_2(\operatorname{Mult}(n,p))-o(n).
\]

Thus public hash side information does not change the first-order
multinomial occupancy rate when `|U|/n -> infinity`, even at polynomially
small failure probability.  No assumption such as `|U| >> n^2` is needed.

## 8. Reproducible finite-instance check

The script `scripts/verify_public_hash_entropy.py` exhaustively enumerates every hash
tape and every `n`-subset for several nonuniform binary and ternary examples.
It verifies, to floating-point conversion tolerance while accumulating the
probabilities exactly as rational numbers,

\[
I(N;h)=I(N;C)=H(M_m)-H(M_{m-n})
\]

and also checks that the marginal occupancy law is exactly `Mult(n,p)`.
Run it with

```text
python3 scripts/verify_public_hash_entropy.py
```
