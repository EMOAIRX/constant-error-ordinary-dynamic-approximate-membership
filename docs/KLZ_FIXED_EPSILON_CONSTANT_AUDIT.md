# KLZ Proposition 4.3 at fixed error：monotone-model audit

Source: Kuszmaul--Liang--Zhou, *Fingerprint Filters Are Optimal*, arXiv:2510.18129v1. All logarithms are base two. PDF page numbers below refer to the arXiv PDF.

## Conclusion

Let the false-positive parameter be a fixed constant

\[
0<\varepsilon\leq \tfrac12,
\qquad |U|=\omega(n/\varepsilon).
\]

If one runs the proof of Proposition 4.3 for history-dependent monotone filters without using \(\varepsilon=o(1)\), the protocol proves

\[
H_{\rm filter}
\geq
n\,L_{\rm KLZ}(\varepsilon)-o(n),
\]

where

\[
\boxed{
L_{\rm KLZ}(\varepsilon)
=
\log\frac1\varepsilon
+(1-\varepsilon)\log e
-2h(\varepsilon)
}
\]

and

\[
h(\varepsilon)
=-\varepsilon\log\varepsilon
 -(1-\varepsilon)\log(1-\varepsilon).
\]

Equivalently,

\[
L_{\rm KLZ}(\varepsilon)
=-(1-\varepsilon)\log\varepsilon
 +(1-\varepsilon)\log(1-\varepsilon)
 +(1-\varepsilon)\log e
 -h(\varepsilon).
\]

At \(\varepsilon=1/2\),

\[
L_{\rm KLZ}(1/2)
=1+\tfrac12\log e-2
=-0.278652479555518\ldots .
\]

Thus this communication protocol gives no nontrivial lower bound at error \(1/2\): after also using the tautology \(H_{\rm filter}\geq0\), it yields only \(H_{\rm filter}\geq0\). Combining with the classical static approximate-membership lower bound instead gives \(H_{\rm filter}\geq n-o(n)\), but that one-bit coefficient is not obtained from the extra dynamic/factorial part of Proposition 4.3.

The displayed proof functional is positive only for
\(\varepsilon<0.4424394892\ldots\). This threshold is merely where this
particular lower bound crosses zero; it has no claimed structural significance.

This calculation confirms the warning in Section 6: the constant-error problem is not resolved by retaining the terms hidden in \(o(n)\).

## Exact prelimit inequality

Write

\[
u=|U|,\qquad V=u/b,\qquad m=n/b,
\qquad N=(1-\varepsilon)n+\varepsilon u,
\qquad M=4^b.
\]

For the \(k\)-th call to `Send`, put

\[
z_k=a_{(\ell_k,r_k]}.
\]

Claims 4.6 and 4.7 imply, before either approximation (19) or (20),

\[
\mathbb E\bigl[|((\overline F_{r_k}\setminus
\overline G_{\ell_k})\cap U_k)|\bigr]
\leq K(z_k+\gamma),
\]

where one may take

\[
K=\frac{uN}{bu-nM^{b+1}},
\]

and

\[
\gamma
=\frac1M+
\frac{nM^{b+1}}b\frac{bu-nM^{b+1}}{uN}.
\]

Equation (16), retaining the binary hit-bit entropy, consequently gives the batch cost

\[
\frac nb\left[
h(\varepsilon)
+\varepsilon\log V
+(1-\varepsilon)
\left(
\log\frac{K}{1-\varepsilon}
+\log(z_k+\gamma)
\right)
\right].
\]

Here the proof has used only \(p_k=\Pr[Z_x=1]\leq\varepsilon\). For \(0<\varepsilon\leq1/2\), \(h(p_k)\leq h(\varepsilon)\). For the location part, KLZ first replaces the conditional expectation by an unconditional first moment divided by \(1-p_k\), and the resulting expression is increasing in \(p_k\) because the conditional candidate-set size is at most \(V\); this is the same monotonicity argument stated explicitly in Claim 3.3 on PDF pp. 6--7. Thus substituting \(p_k=\varepsilon\) gives a valid worst-case bound under exactly the marginal information used by the original proof.

Combining it with Claim 4.4 gives

\[
\begin{aligned}
H_{\rm filter}\geq{}&
b\log\left(V^{\underline m}\right)
-nh(\varepsilon)-n\varepsilon\log V\\
&-(1-\varepsilon)n\log\frac K{1-\varepsilon}
-(1-\varepsilon)\frac nb
\sum_{k=1}^b\log(z_k+\gamma).
\end{aligned}
\]

Under KLZ's choice \(b\to\infty\) sufficiently slowly and
\(9^{b^2}=o(\varepsilon u/n)\),

\[
b\log(V^{\underline m})=n\log V-o(n),
\]

\[
K=\varepsilon V(1+o(1)),
\qquad
\gamma\leq 2/4^b+o(4^{-b}),
\]

and Lemmas 3.4 and 4.8 give

\[
\sum_{k=1}^b\log(z_k+\gamma)
\leq-b\log e+o(b).
\]

Substitution and cancellation of \(n\log V\) produce

\[
\begin{aligned}
H_{\rm filter}\geq n\bigl[&
-h(\varepsilon)
-(1-\varepsilon)\log\varepsilon
+(1-\varepsilon)\log(1-\varepsilon)\\
&+(1-\varepsilon)\log e
\bigr]-o(n),
\end{aligned}
\]

which is the stated \(L_{\rm KLZ}\).

## Where each linear loss comes from

Relative to the small-error target

\[
\log(1/\varepsilon)+\log e,
\]

the retained proof loses

\[
2h(\varepsilon)+\varepsilon\log e
\]

bits per key.

### 1. One \(h(\varepsilon)\): separately transmitting every hit bit

In Lemma 4.5, immediately before equation (16), Alice sends

\[
Z_x=\mathbf 1[x\in\overline G_\ell]
\]

for every key separately. KLZ upper-bounds its entropy by
\(h(\varepsilon)\). This contributes \(nh(\varepsilon)\) bits over all
keys. See PDF p. 15, Lemma 4.5, first paragraph of its proof and (16).

This is a protocol loss, not a property proved necessary of arbitrary
filters. Jointly coding the whole hit vector can only reduce this term,
because \(H(Z^m)\leq\sum_i H(Z_i)\). However, marginal FPR alone permits
independent Bernoulli-\(\varepsilon\) hit bits, so deleting this term requires
a new structural inequality tying the joint hit vector to the filter state or
to the conditional accepted-set differences. It cannot be removed merely by
rewriting the same single-letter calculation.

### 2. A second \(h(\varepsilon)\): the branch/location mixture

Ignoring the \(z_k\) term, the exact branch-location cost in (16) is

\[
\varepsilon\log V
+(1-\varepsilon)
\log\frac{\varepsilon V}{1-\varepsilon}.
\]

The identity

\[
\varepsilon\log V
+(1-\varepsilon)
\log\frac{\varepsilon V}{1-\varepsilon}
=\log V+\log\varepsilon+h(\varepsilon)
\]

shows precisely the second entropy loss. In the published proof this is
absorbed by the statements \(\log(1-\varepsilon)=o(1)\) and
\(\varepsilon\log\varepsilon=o(1)\) on PDF p. 17, between (20) and the
conclusion of Lemma 4.5.

Under only the one-key information used there---\(p_x\leq\varepsilon\) and
an unconditional first-moment bound on the candidate-set size---this loss is
not eliminated by sharper algebra. Recovering it would require joint or
conditional information that equation (16) discards.

### 3. \(\varepsilon\log e\): factorial saving is available only on misses

The sum of logarithmic interval masses is multiplied by \(1-\varepsilon\)
in Lemma 4.5 and equation (22). Hence Lemma 3.4's factorial saving contributes
only

\[
(1-\varepsilon)n\log e,
\]

not \(n\log e\). The published last line on PDF p. 19 changes this to
\(n\log e-o(n)\) using \(\varepsilon=o(1)\).

This loss arises because on a hit, \(Z_x=1\), `Send` transmits \(x\) from all
of \(U_k\) and obtains no shrinking/interval-mass saving. Recovering it needs a
new way to encode hit keys; it is not a rounding or Stirling loss.

### 4. No further linear loss from obfuscation or removal of monotonicity

The following losses remain \(o(n)\) even for fixed \(\varepsilon\), provided
\(u/n\to\infty\):

- random-partition falling factorial: Claim 4.4 and (21), PDF pp. 12 and 18;
- the ratio \(N/(\varepsilon u)=1+o(1)\): (19), PDF p. 17;
- exposure of keys in the obfuscating tree and the additive \(2/4^b\):
  Claims 4.6--4.7 and (19)--(20), PDF pp. 15--17;
- perturbing \(z_k\) by \(2/4^b\): Lemma 4.8, (24)--(25), PDF pp. 18--19;
- Stirling/factorial remainder: Lemma 3.4 as invoked in (23), PDF p. 18.

Definition 5.2 and Lemma 5.3 introduce no new coefficient loss. They replace
the accepted set by a reconstructible set \(\widetilde F\) satisfying

\[
S_F\subseteq\widetilde F\subseteq\overline F
\]

and the required prefix monotonicity. Since
\(\widetilde F\subseteq\overline F\), the same pointwise FPR upper bound and
the same expectation bound \((1-\varepsilon)n+\varepsilon u\) remain valid.
See Definition 5.2 and Lemma 5.3, PDF p. 20.

## Status

### Proved by retaining the original proof's terms

For fixed \(0<\varepsilon\leq1/2\), \(u=\omega(n/\varepsilon)\), and the same
operation-horizon assumptions used by KLZ,

\[
H_{\rm filter}\geq
n\left[
\log(1/\varepsilon)+(1-\varepsilon)\log e-2h(\varepsilon)
\right]-o(n).
\]

This statement is proved for history-dependent monotone filters and does not
assume history independence. The claimed extension through Lemma 5.3 to
arbitrary non-monotone filters is **conditional**: reconstructible sets depend
on the public partition, so Claim 4.6's fixed-set removing-\(U_k\) argument
cannot be copied from actual accepted sets. See
[SECTION5_PARTITION_DEPENDENCE_HOSTILE_AUDIT_2026_08_13.md](./SECTION5_PARTITION_DEPENDENCE_HOSTILE_AUDIT_2026_08_13.md).

### Not proved

The audited Section 4 proof does not establish the constant-error
fingerprint/occupancy entropy rate, nor any sharp arbitrary-filter coefficient.
In particular, without a new partition-safe argument it gives no ordinary
non-monotone dynamic improvement at \(\varepsilon=1/2\).

### Necessary new ingredient

Any improvement substantial enough to address the Section 6 open problem must
couple the hit-pattern entropy with the cost of locating keys on the hit and
miss branches. Improving only Lemma 3.4, Stirling terms, the obfuscation
coupling, or the reconstructible-set construction cannot recover the missing
linear coefficient.
