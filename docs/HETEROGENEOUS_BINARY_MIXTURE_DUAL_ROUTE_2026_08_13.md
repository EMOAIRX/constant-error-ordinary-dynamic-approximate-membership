# Heterogeneous binary canonical mixtures at half error: dual route

> Status (2026-08-13): the infinite-dimensional mixture has been reduced
> rigorously to a pointwise two-constraint LP and an explicit supporting-line
> inequality.  The coordinate branch is eliminated analytically.  Numerical
> exploration finds no heterogeneous improvement.  The all-threshold
> supporting inequality is not yet a theorem; the exact missing lemma is
> isolated below.

All logarithms in the derivation are natural.  The target rejection is
\(\delta=1/2\).

## 1. Mixture LP

A threshold atom \(t=(q,p,\lambda)\), \(q\ge2\), has

\[
A_q(z)=\frac{1-z^q}{(1-z)^2},
\qquad
J_{q,p}(\lambda)
=e^{-\lambda}\sum_{c=0}^{q-1}\frac{\lambda^c}{c!}
 [p(1-p)^c+(1-p)p^c].
\]

One block per capacity key contributes

\[
a_t(z)=\ln A_q(z),\qquad
m_t=\lambda,\qquad
r_t=\lambda J_{q,p}(\lambda)
\]

to log state count, tracked mass, and rejection respectively.  If \(b_t\)
is the block density of atom \(t\), then for fixed \(z\)

\[
\Phi(z)=\inf_{b_t\ge0}
\left\{\sum_t b_ta_t(z):
 \sum_t b_tr_t\ge\frac12,
 \ \sum_t b_tm_t\le1\right\}.
\tag{1}
\]

The heterogeneous rate is exactly

\[
R_{\rm mix}=\frac1{\ln2}
\inf_{0<z<1}\{\Phi(z)-\ln z\}.
\tag{2}
\]

The two infima commute because the feasible mixture domain does not depend on
\(z\).  At fixed \(z\), every finite-dimensional restriction of (1) has an
extreme optimum supported on at most two atoms.  This justifies exhaustive
one- and two-atom numerical searches; it does not compactify the continuum by
itself.

## 2. The homogeneous contact point and its dual

Let

\[
q_0=3,\qquad p_0=\frac12,
\]

and let \(\lambda_0\) be the unique root

\[
J_{3,1/2}(\lambda_0)=\frac12.
\]

Let \(z_0\) be the unique saddle

\[
\lambda_0=\frac{z_0A_3'(z_0)}{A_3(z_0)}.
\]

Numerically,

\[
\lambda_0=1.325819075285\ldots,
\qquad
z_0=0.447778045429\ldots.
\]

Put \(K_0=\ln A_3(z_0)\).  Define \(u,v>0\) by tangency of

\[
u\lambda J_{3,1/2}(\lambda)-v\lambda
\]

at \(\lambda_0\), with value \(K_0\):

\[
u=\frac{-K_0/\lambda_0}
        {\lambda_0J'_{3,1/2}(\lambda_0)},
\qquad
v=u\,[J_{3,1/2}(\lambda_0)
       +\lambda_0J'_{3,1/2}(\lambda_0)].
\tag{3}
\]

The numerical values are

\[
u=2.228358477660\ldots,
\qquad
v=0.289376279006\ldots.
\]

If for a given \(z\) every atom satisfies

\[
\ln A_q(z)
\ge s(z)[u\lambda J_{q,p}(\lambda)-v\lambda],
\qquad
s(z)=\frac{\ln A_3(z)}{K_0},
\tag{4}
\]

then every feasible mixture satisfies

\[
\sum_tb_t\ln A_{q_t}(z)
\ge s(z)\left(\frac u2-v\right),
\tag{5}
\]

because rejection is at least \(1/2\), tracked mass is at most one, and
\(-sv\sum b_tm_t\ge-sv\).

The right side of (5), minus \(\ln z\), is precisely the homogeneous
\(q=3\) fixed-state objective.  Its unique minimum is at \(z_0\) and equals

\[
R_0\ln2,
\qquad
R_0=2.349083440193141\ldots.
\tag{6}
\]

Thus (4) for every \(z\) would prove the full heterogeneous theorem.

## 3. Coordinate lattices are rigorously harmless

For \(L=\langle(a,0)\rangle\), after naming the rejectable symbol with
probability \(p\),

\[
A_a(z)=\frac{1-z^a}{(1-z)^2}\ge A_1(z)=\frac1{1-z},
\qquad
J_{\rm coord}(\lambda,p)=p e^{-\lambda p}.
\]

For the unscaled contact inequality at \(z_0\), write \(t=\lambda p\).
Since \(p\le1\),

\[
u\lambda p e^{-\lambda p}-v\lambda
\le t(ue^{-t}-v).
\]

The latter has a unique maximum at the root of

\[
ue^{-t}(1-t)=v.
\]

Direct interval evaluation gives

\[
\sup_{t\ge0}t(ue^{-t}-v)
<0.572678
<0.593805
<\ln A_1(z_0).
\tag{7}
\]

Consequently coordinate atoms have a strict dual gap at the global contact
point.  More conceptually, a coordinate atom is operationally a masked unary
occupancy atom: only keys whose public symbol is the rejectable symbol need to
be retained.  It supplies no genuinely new two-symbol rejection mechanism.

## 4. Compactness of the missing atom inequality

The right side of (4) is nonpositive whenever

\[
J_{q,p}(\lambda)\le\frac vu
=0.1298607391\ldots.
\]

Since truncation can only reduce absence probability and

\[
J_{q,p}(\lambda)
\le p e^{-\lambda p}+(1-p)e^{-\lambda(1-p)},
\]

the existing untruncated-absence lemma implies, for \(\lambda\le2\), that
the right side is maximized by \(p=1/2\).  For larger \(\lambda\), the same
quantity is below \(v/u\) once \(\lambda\ge4.083\), using the envelope
\(e^{-\lambda/2}\) in the central range and direct endpoint splitting.

Therefore a formal interval proof need only inspect a compact load interval,
which may safely be enlarged to

\[
0\le\lambda\le4.1,qquad0\le p\le\frac12.
\tag{8}
\]

This is a substantive reduction: no large-load tail can violate the dual.

## 5. A uniform large-q barrier

For every finite threshold,

\[
J_{q,p}(\lambda)
\le p e^{-\lambda p}+(1-p)e^{-\lambda(1-p)}.
\]

Numerically, throughout the only range relevant to a positive dual right
side, the maximum of

\[
u\lambda J_{q,p}(\lambda)-v\lambda
\]

occurs at \(p=1/2\).  The \(q=\infty\) envelope is then

\[
C_\infty K_0
=\sup_{\lambda\ge0}\lambda(ue^{-\lambda/2}-v),
\qquad
C_\infty=1.047383480403\ldots.
\tag{9}
\]

For \(q\ge5\), \(A_q(z)\) increases with \(q\), while the threshold
rejection also increases with \(q\).  A valid all-\(q\) certificate can use
the stronger finite constants

\[
C_q=K_0^{-1}\sup_{p,\lambda}
 [u\lambda J_{q,p}(\lambda)-v\lambda]
\]

rather than the loose common \(C_\infty\).  Numerically,

\[
C_4=1.0382700782,quad
C_5=1.0460392628,quad
C_q\uparrow C_\infty.
\]

The worst lower endpoint of (4) is \(q=4\): its equality threshold is

\[
z_4=0.372567489468\ldots.
\tag{10}

For \(q\ge5\), the corresponding thresholds decrease to

\[
z_\infty=0.328200923441\ldots.
\tag{11}

Hence an interval certificate for the constants \(C_q\), together with a
monotonic-in-\(q\) comparison, would establish (4) for every threshold atom on
\(z\ge z_4\).  On this interval, (5) has its unique minimum at \(z_0\), so it
proves the desired rate.

For \(z<2^{-R_0}=0.196270677764\ldots\), the term \(-\log_2z\) alone proves
the target.  The remaining proof interval is therefore only

\[
[0.196271,0.372568].
\tag{12}

It requires a different dual contact atom (numerically \(q=4,5,\ldots\) as
\(z\) decreases), but it has a large objective margin above \(R_0\).  A
piecewise interval-dual certificate is the cleanest current route.

## 6. What is proved and what remains

Proved analytically:

1. the exact heterogeneous mixture LP (1)--(2);
2. support size at most two for each finite atom discretization;
3. the dual implication (4)--(6);
4. strict exclusion of coordinate lattices at the global contact point;
5. compact reduction of potentially violating loads;
6. trivial exclusion of \(z<2^{-R_0}\).

Supported by reproducible high-resolution numerics, but not yet a theorem:

1. no heterogeneous mixture beats \(R_0\);
2. all active threshold atoms have \(p=1/2\) and total tracked mass one;
3. the all-atom inequality (4) holds for \(z\ge z_4\);
4. a finite piecewise family of duals covers (12).

The exact remaining analytic lemma is:

> **Threshold dual lemma.** Certify \(C_q\) uniformly over
> \(q\ge2\), \(p\in[0,1/2]\), and \(\lambda\in[0,4.1]\), then prove the
> required ratios \(\ln A_q(z)/\ln A_3(z)\ge C_q\) on the appropriate
> piecewise-z intervals.

This is a compact real-analytic inequality with a discrete tail, not an open
infinite-dimensional data-structure argument.  Until it is certified, the
heterogeneous sharp converse must remain a conjecture.

## 7. Reproducibility

The finite-support search is implemented in
`scripts/verify_heterogeneous_binary_mixture_half.py`.  It scans every one- and
two-atom LP vertex after a Pareto pruning step.  The single-branch coordinate
and masking explorer is `scripts/verify_binary_coordinate_mask_phase.py`.  Both are
floating-point explorers and must not be cited as proof certificates.
