# Continuous optimality and thick-fiber upper barrier

> Status: Sections 2--4 are finite, parameter-free structural theorems. They
> do not identify the decimal value of $C_{\mathrm{AP}}$ and do not improve
> the lower bound under only $u/n\to\infty$. Section 5 rules out the most
> direct attempt to turn an optimal union profile into a matching ordinary
> upper bound.

All logarithms are base two unless stated otherwise.

## 1. Scope

The continuous all-pivot theorem proves

$$
C_{\mathrm{AP}}=\lim_{q\to\infty}C_q,
\qquad C_q<C_{\mathrm{AP}}.
$$

This does not by itself prove that the numerical all-active solution near
$1.7156$ is the optimizer. Two additional steps would be needed:

1. prove that every finite minimizer uses every pivot with positive KKT
   weight and pass those equalities through the diagonal singularity;
2. construct a nonnegative exact adjoint measure, or otherwise prove strong
   duality for the unbounded kernel.

The results below isolate the exact finite sign problem and show why the
union profile alone cannot be reversed into a data structure.

## 2. Unique finite minimizer

Recall

$$
C_q
=
\inf_{0<p_0\le\cdots\le p_{q-1}<1}
\max_{0\le s\le q}L_{q,s}(p).
$$

### Theorem 2.1

For every finite $q$, the objective

$$
p\longmapsto\max_sL_{q,s}(p)
$$

has a unique minimizer, and it satisfies

$$
0<p_0<p_1<\cdots<p_{q-1}<1.
$$

### Proof

The endpoint branches are strictly convex because $A$ and $B$ are strictly
convex. Fix an interior branch $1\le s<q$. Its left part contains
$B(p_0),\ldots,B(p_{s-1})$. Equality in the convexity inequality for this
part forces all left coordinates of two candidate vectors to agree. Once
$p_{s-1}$ is fixed, each right coordinate occurs in the strictly convex
function

$$
c\longmapsto\Phi(p_{s-1},c),
$$

so equality also forces all right coordinates to agree. Hence every
$L_{q,s}$ is strictly convex. The maximum of finitely many strictly convex
functions is strictly convex, so there is at most one minimizer.

Existence follows from boundary coercivity. The endpoint branches diverge if
$p_0\downarrow0$ or $p_{q-1}\uparrow1$, while

$$
\Phi(p_i,p_{i+1})\longrightarrow+\infty
$$

if two adjacent coordinates collide. Thus every minimizing sequence remains
in a compact subset of the strict interior. This proves existence,
uniqueness, and strict ordering. $\square$

## 3. The adjacent-difference Jacobian is an $M$-matrix

Set

$$
\Delta_s(p)=L_{q,s}(p)-L_{q,s-1}(p),
\qquad1\le s\le q,
$$

and let $J$ be the Jacobian of $\Delta=(\Delta_1,\ldots,\Delta_q)$.

The derivative identities

$$
\partial_2\Phi(a,c)
=-\frac{2-a}{2(c-a)\ln2},
$$

$$
\partial_1\Phi(a,c)
=\frac1{2\ln2}
\left[
\frac{2-c}{c-a}-\ln\frac{2-a}{c-a}
\right]
>0
$$

give the following exact sign pattern in row $s$ of $J$:

$$
\partial_{p_j}\Delta_s
\begin{cases}
=0,&j<s-2,\\
<0,&j=s-2,\\
>0,&j=s-1,\\
<0,&j\ge s.
\end{cases}
$$

Terms with an impossible index are omitted.

### Theorem 3.1

The Jacobian of the map

$$
p\longmapsto
(L_{q,1}-L_{q,0},\ldots,L_{q,q}-L_{q,q-1})
$$

is nonsingular everywhere on the strict ordered domain. Consequently, every
finite all-branch equalizer is locally unique.

### Proof

Let $D=J^{\mathsf T}$. The displayed sign pattern says that $D$ is a
$Z$-matrix: its diagonal is positive and all off-diagonal entries are
nonpositive. Telescoping the adjacent differences gives

$$
D\mathbf1
=
\nabla L_{q,q}-\nabla L_{q,0}
>0
$$

coordinatewise, because $B'>0$ and $A'<0$. A $Z$-matrix that maps a positive
vector to a strictly positive vector is a nonsingular $M$-matrix. Hence all
principal minors of $D$, and therefore of $J$, are positive. In particular,
$\det J>0$ everywhere, and the inverse function theorem makes every zero of
$\Delta$ locally unique. $\square$

The classical global Gale--Nikaido theorem for a $P$-matrix Jacobian is
stated on rectangular domains. The strict ordered simplex is not rectangular,
so the calculation above does not by itself prove global injectivity. A
properness or order-domain extension would be needed for that stronger
conclusion.

This theorem does not yet prove that the unique minimizer is the equalizer.
At a minimizer, let $\lambda_s$ be KKT weights and define tail weights

$$
\Lambda_s=\sum_{r=s}^q\lambda_r.
$$

The endpoint KKT weights must be positive: without $\lambda_0$, the
$p_0$ stationarity equation contains only positive derivatives, and without
$\lambda_q$, the $p_{q-1}$ equation contains only negative derivatives.
Consequently $0<\Lambda_s<1$ for $1\le s\le q$. What remains is the strict
monotonicity

$$
1=\Lambda_0>\Lambda_1>\cdots>\Lambda_q>0,
$$

which is equivalent to $\lambda_s>0$ for every branch. A general
$M$-matrix does not imply this stronger sign-regularity; it is the precise
finite all-activation problem.

## 4. Why weak compactness cannot prove full activation

Bounded branch energy and an atomless weak limit do not imply uniform
integrability at the diagonal. To see this, take smooth atomless quantiles
$y_k$ and replace each by a pair

$$
p_{2k}=y_k,
\qquad
p_{2k+1}=y_k+e^{-\alpha q},
\qquad\alpha>0.
$$

The empirical measures have the same atomless weak limit as the unpaired
quantiles, and their endpoint energies remain bounded. Nevertheless, the
left pivot of every pair contains

$$
\frac1q\Phi(p_{2k},p_{2k+1})
\longrightarrow
\frac{\alpha(1-y_k/2)}{\ln2}>0.
$$

Thus a nonzero diagonal defect can survive weak convergence. Any proof that
passes finite adjacent equalities to the all-active integral equation must
first use exact optimizer structure to exclude this pairing. Portmanteau and
the existing logarithmic anti-concentration estimate alone cannot do so.

## 5. Complete thick fibers cannot give a matching upper bound

Fix a deterministic tape, load $t$, exact operation time, and physical state
$m$. Let its operational endpoint fiber contain

$$
\binom Wt,
\qquad |W|=w.
$$

Take disjoint sets

$$
D\in\binom Wk,
\qquad
Y\in\binom{U\setminus W}k,
\qquad1\le k<t.
$$

Run any fixed alternating word that deletes the labels of $D$ and inserts
the labels of $Y$. For every $S\in\binom Wt$ containing $D$, the word is
legal. Fixed-tape determinism sends all these histories from $m$ to the same
successor state $m_{D,Y}$. Their endpoint sets are

$$
(S\setminus D)\cup Y.
$$

As $S$ ranges over all members containing $D$, their union is exactly

$$
(W\setminus D)\cup Y.
$$

### Theorem 5.1

Assume every such successor operational union has size at most $w$; that is,
the proposed construction has no union slack along these replacement words.
Then it has at least

$$
\boxed{
\binom wk\binom{u-w}k
}
$$

distinct successor states.

### Proof

Zero false negatives and the common-word argument show that the successor
union contains $(W\setminus D)\cup Y$, which already has size $w$. The
no-slack assumption makes this containment equality. Distinct pairs $(D,Y)$
give distinct unions, since

$$
D=W\setminus W(m_{D,Y}),
\qquad
Y=W(m_{D,Y})\setminus W.
$$

Two histories at the same load and exact time cannot reach the same physical
state with different operational unions. Hence all these successor states
are distinct. $\square$

If $w=\Theta(u)$, $t=\Theta(n)$, and $k=\Theta(n)$, then

$$
\log_2\binom wk+
\log_2\binom{u-w}k
=
\Omega\!\left(n\log\frac un\right).
$$

Therefore an $O(n)$-bit matching construction cannot realize the continuous
profile by complete thick fibers with tight successor unions. It must use at
least one feature invisible to the all-pivot union profile: exponentially
incomplete fibers, substantial union slack, or history-dependent multiple
representations with nonprincipal overlap.

## 6. Exact analytic target

If a full-support countably additive exact dual exists, write
$\sigma=\lambda/C_{\mathrm{AP}}$. Complementarity requires the parameter-free
log-Volterra equation

$$
B(c)\sigma([c,1])
+
\int_{[0,c)}\Phi(a,c)\,d\sigma(a)
=1,
\qquad0<c\le1.
$$

Then

$$
C_{\mathrm{AP}}
=
\frac1{\sigma([0,1])}.
$$

Writing $m=\sigma([0,1])$, the equation forces the boundary law

$$
d\sigma(a)
\sim
\frac{(1-m)\ln2}
{a[\ln(1/a)]^2}\,da
\qquad(a\downarrow0)
$$

and the endpoint moment

$$
\int_0^1B(a)\,d\sigma(a)=1.
$$

Proving existence and positivity for this singular equation, together with a
complementary primal measure, would identify $C_{\mathrm{AP}}$ naturally.
Those steps remain open; no decimal obtained from the all-active numerical
equation is used here.
