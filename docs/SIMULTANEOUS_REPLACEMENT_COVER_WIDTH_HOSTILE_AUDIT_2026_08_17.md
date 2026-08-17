# Simultaneous replacement-cover width: hostile proof audit

> Status: independent line-by-line audit of the natural-universe theorem. The
> verdict is positive. This document records the quantifier ledger, the exact
> conditional laws, the explicit-constant calculation, and the attempted
> counterexamples. It introduces no stronger theorem than the main proof.

The audited theorem is
[Simultaneous replacement-cover width](./SIMULTANEOUS_REPLACEMENT_COVER_WIDTH_LOWER_BOUND_2026_08_17.md).
All logarithms are base two.

## 1. Quantifier ledger

The model guarantee is

$$
\forall h\ \forall x\notin S(h),
\qquad
\Pr_R[\operatorname{Query}_R(h,x)=\mathrm{YES}]\le\frac12.
$$

The proof samples $S,D,I$ without inspecting $R$:

$$
S\sim\operatorname{Unif}\binom Un,
\qquad
D\mid S\sim\operatorname{Unif}\binom Sq,
\qquad
I\mid S\sim\operatorname{Unif}\binom{U\setminus S}q.
$$

All labels within a set are processed in a fixed universe order. Thus every
realized parent and successor history is fixed independently of the tape, and
the pointwise FPR can be averaged before any tape is fixed.

Only after the global good-event probability is bounded does Fubini fix
$(r,s,d)$. Conditional on that triple,

$$
I\sim\operatorname{Unif}\binom{U\setminus s}q
$$

exactly. The proof never applies FPR conditional on $R=r$ and never asserts
that the reference marginal $Q(I\mid z,d)$ is uniform; that marginal generally
is not uniform.

## 2. Parent and successor Carter identities

For $Z=(R,M)$ let $A_Z$ be the actual YES-set, $a_Z=|A_Z|$, and
$\mu_z=\mathcal L(S\mid Z=z)$. Zero false negatives give
$\operatorname{supp}\mu_z\subseteq\binom{A_z}n$. Therefore

$$
d_z
=D\!\left(\mu_z\,\middle\|\,\operatorname{Unif}\binom{A_z}n\right)
=\log\binom{a_z}n-H(S\mid Z=z).
$$

Write

$$
L=\log\binom un,
\qquad
B=\log\binom{(u+n)/2}{n},
\qquad
J=B-\mathbb E\log\binom{a_Z}n.
$$

Because the source history is independent of $R$,

$$
I(S;Z)=I(S;M\mid R)\le H.
$$

Pointwise FPR gives $\mathbb E a_Z\le(u+n)/2$, so concavity gives $J\ge0$.
The exact accounting identity is

$$
I(S;Z)=(L-B)+J+\mathbb E d_Z\le H.
\tag{1}
$$

As $u/n\to\infty$, $L-B=n-o(n)$. Hence, under
$H\le(1+\gamma)n$,

$$
J\le\gamma n+o(n),
\qquad
\mathbb E d_Z\le\gamma n+o(n).
\tag{2}
$$

The successor set $S'=S\setminus D\cup I$ is uniform in $\binom Un$. Its full
history remains independent of $R$, so the identical calculation applies to
the successor accepted size. No stationary distribution is used.

## 3. Accepted-size concentration

There are two exact derivations. The first uses the curvature of
$f(x)=\log\binom xn$:

$$
f''(x)
=-\frac1{\ln2}\sum_{j=0}^{n-1}\frac1{(x-j)^2}
\le-\frac n{u^2\ln2}.
$$

The tangent gap at $(u+n)/2$ and (2) yield

$$
\Pr\left[\left|a_Z-\frac{u+n}{2}\right|>\tau u\right]
\le O\left(\frac\gamma{\tau^2}\right)+o(1).
\tag{3}
$$

For the explicit constant, set $X=a_Z/u$. The product formula gives

$$
\log\frac{\binom un}{\binom{a_Z}n}
=\sum_{j=0}^{n-1}\log\frac{u-j}{a_Z-j}
\ge n\log\frac1X.
$$

Together with $\mathbb EX\le1/2+o(1)$ and

$$
-\log_2x-1+\frac2{\ln2}(x-1/2)
\ge\frac{(x-1/2)^2}{2\ln2},
$$

this proves

$$
\mathbb E(X-1/2)^2\le2\ln2\,\gamma+o(1).
\tag{4}
$$

The directions in (3)--(4) are important: a loose upper approximation to
$\log\binom an$ is not by itself enough to prove concentration.

## 4. Conditional replacement law

Fix $z=(r,m)$ and set $A=A_z$. Compare the actual posterior $\mu_z$ with
$\nu_z=\operatorname{Unif}\binom An$. Apply to both laws the same kernel:

1. choose $D$ uniformly among the $q$-subsets of $S$;
2. choose $I$ uniformly among the $q$-subsets of $U\setminus S$;
3. output $K=S\setminus D$.

For each fixed compatible $(d,i,k)$, the reference joint probability is

$$
\frac1{\binom an\binom nq\binom{u-n}q},
$$

independent of $k$. Consequently,

$$
K\mid(D=d,I=i,Z=z)
\sim
\operatorname{Unif}
\binom{A\setminus(d\cup i)}{n-q}
$$

under the reference law. KL chain rule gives

$$
\mathbb E_{D,I}
D(\mu_{K\mid z,D,I}\|\nu_{K\mid z,D,I})
\le d_z.
\tag{5}
$$

Let $V$ be the union of the actual conditional support of $K$, let $v=|V|$,
and let

$$
b=|A\setminus(d\cup i)|=a_z-q-|i\cap A|.
$$

The conditional reference is uniform on $\binom Bk$, while the actual law is
supported on $\binom Vk$. Therefore

$$
D(\mu_{K\mid z,d,i}\|\nu_{K\mid z,d,i})
\ge\log\frac{\binom bk}{\binom vk}
\ge k\log\frac bv.
\tag{6}
$$

Equations (2), (5), and (6) are the entire posterior-pruning charge. They do
not require all witnesses to avoid every insertion suffix, which is why the
proof pays no $n^2/u$ collision probability.

## 5. Common successor and outside capacity

Every $K$ in the conditional support corresponds to a canonical parent source
$d\cup K$ that reaches the same fixed-tape state $m$ and avoids $i$. Hence the
same delete-$d$, insert-$i$ word is legal from every source and reaches one
successor state $m_i$. Zero false negatives imply

$$
V\cup i\subseteq A(r,m_i).
\tag{7}
$$

Take $\tau=\gamma^{1/4}$ and discard branches whose conditional KL in (6)
exceeds $\tau^2n$. By (2) and (5), their mass is
$O(\sqrt\gamma)+o(1)$. On the remaining branches,

$$
v\ge(a-q-|i\cap A|)2^{-2\tau^2}
\ge(a-n)2^{-2\tau^2}.
$$

Combining this with the parent and successor size windows gives

$$
\frac{|A(r,m_i)\setminus A|}{u}
\le
(1/2+\tau)-(1/2-\tau-o(1))2^{-2\tau^2}
\le3\tau+o(1).
\tag{8}
$$

Also, conditioned on the actual $S$ and $A$, the random variable
$|I\setminus A|$ is hypergeometric with success density

$$
\frac{u-a}{u-n}=\frac12+O(\tau)+o(1).
$$

Thus $|I\setminus A|\ge q/3$ except with probability $\exp(-\Omega(n))$.

## 6. Fubini and distinct branch counting

The parent-size, successor-size, conditional-KL, and hypergeometric bad masses
sum to $O(\sqrt\gamma)+o(1)$. For sufficiently small fixed $\gamma$, Fubini
fixes $(r,s,d)$ for which at least half of the

$$
N=\binom{u-n}q
$$

equally likely insertion sets in $\binom{U\setminus s}q$ are good.

For one successor state, put $C=A(r,m_i)\setminus A$. Equations (7)--(8) give
$|C|\le3\tau u+o(u)$, and every good insertion set mapped to that state has at
least $s_0=\lceil q/3\rceil$ elements in $C$. A union bound over the chosen
$s_0$ elements gives

$$
N_{\rm one\ state}
\le
\binom{|C|}{s_0}\binom{u-s_0}{q-s_0}.
\tag{9}
$$

Using

$$
\frac{\binom{|C|}{s_0}\binom{u-s_0}{q-s_0}}{\binom uq}
=\binom q{s_0}\frac{\binom{|C|}{s_0}}{\binom u{s_0}},
$$

the conservative bounds $\binom q{s_0}\le2^q$ and

$$
\frac{\binom{|C|}{s_0}}{\binom u{s_0}}
\le(5\tau)^{s_0}
$$

hold for all sufficiently large instances. Moreover,

$$
\log\frac{\binom uq}{\binom{u-n}q}
=O\left(\frac{nq}{u}\right)=o(n)
$$

under only $u/n\to\infty$. Therefore

$$
\frac Hn
\ge-\frac12+\frac16\log_2\frac1{5\gamma^{1/4}}-o(1).
\tag{10}
$$

At $\gamma=2^{-48}$, the right side is greater than $1.11-o(1)$, contradicting
$H/n\le1+2^{-48}$. Floors in $q$ and $s_0$ change only $o(n)$ terms.

## 7. Counterexample pressure tests

The following known mechanisms do not invalidate the proof.

| Mechanism | Where it is charged |
|---|---|
| ALL-YES or coordinate-erasure tapes | The FPR and Carter averaging occur before the tape is fixed; unreliable tapes enlarge the Jensen gap. |
| Shared gate | A gate that destroys many compatible remainders creates conditional KL in (5)--(6). |
| Refresh labels | New labels must fit in the same successor reservoir $C$ and are counted by (9). |
| Query-silent parity or checksum | It may thin the posterior, but that thinning appears in $d_z$ and cannot enlarge $V$ for free. |
| Multiple representations and holonomy | The proof uses only canonical source histories to define the posterior; the common suffix starts from one actual physical state. |
| Highly nonuniform reference insertion marginal | Never used; distinct insertion sets are counted only after the actual source $s$ is fixed. |

## 8. Verdict and remaining scope

The proof establishes

$$
H\ge(1+2^{-48})n-o(n)
$$

for the original ordinary model under only $u/n\to\infty$. The audit found no
hidden stationarity, BSSI, monotonicity, canonical-state, per-tape-FPR, or
$u/n^2$ assumption.

The constant $2^{-48}$ is intentionally conservative. This theorem does not
identify the optimal coefficient and does not lift the stronger
$C_{\mathrm{AP}}>1.607987\ldots$ bound to the natural-universe regime.
