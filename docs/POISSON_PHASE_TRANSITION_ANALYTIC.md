# Audited analytic work on the Poisson-entropy phase geometry

Let `X ~ Poi(lambda)`, use natural logarithms, and put

\[
H=H(X),\qquad r=H/\lambda,\qquad g=1-e^{-\lambda},
\qquad F=e^\lambda r.
\]

This note proves the required small-load curvature inequalities and gives
pure-rational sign certificates near the stationary point. An earlier version
claimed the unnecessary stronger statement that `F` is globally strictly
convex; hostile review correctly invalidated its large-load lower bound. The
global phase theorem is repaired below using monotonicity of Poisson entropy.

## 1. Elementary expectation bounds

Write

\[
A(\lambda)=\mathbb E\log(X!),
\quad H=\lambda(1-\log\lambda)+A.
\]

Poisson differentiation gives

\[
A'=\mathbb E\log(X+1),\qquad
A''=\mathbb E\log\frac{X+2}{X+1}.
\]

The following bounds will be used:

\[
0\le A,\qquad
e^{-\lambda}\log2\le A''\le \frac{1-e^{-\lambda}}\lambda,
\tag{1}
\]

\[
e^{-\lambda}\lambda\log2\le A'\le\log(1+\lambda).
\tag{2}
\]

The lower bounds retain respectively the events `X=0` and `X=1`.
The upper bound in (2) is Jensen.  For (1),
`log(1+t) <= t` and

\[
\mathbb E\frac1{X+1}=\frac{1-e^{-\lambda}}\lambda.
\]

## 2. Strict convexity of F through unit load

Direct substitution gives

\[
D(\lambda):=\lambda^3e^{-\lambda}F''(\lambda)
=\lambda^2H''+2\lambda(\lambda-1)H'
 +(\lambda^2-2\lambda+2)H.
\tag{3}
\]

For `0 < lambda <= 1`, use `A >= 0`, the upper bound on `A'`
(its coefficient is nonpositive), and the lower bound on `A''`.  After
simplification,

\[
D(\lambda)\ge \lambda\{q(\lambda)-\lambda^2\log\lambda\},
\tag{4}
\]

where

\[
q(x)=(1-x)^2+x e^{-x}\log2-2(1-x)\log(1+x).
\]

Since `-x^2 log x >= 0`, it is enough to prove `q>0`.  On `[0,1]`, use

\[
\log2\ge69/100,
\]

\[
e^{-x}\ge1-x+x^2/2-x^3/6+x^4/24-x^5/120,
\]

and

\[
\log(1+x)\le x-x^2/2+x^3/3-x^4/4+x^5/5.
\]

Their directions are the standard alternating-series remainder theorem.
They give `q(x) >= P(x)`, where

\[
P(x)=1-\frac{331}{100}x+\frac{331}{100}x^2
-\frac{793}{600}x^3+\frac{631}{600}x^4
-\frac{697}{800}x^5+\frac{1577}{4000}x^6.
\]

The exact-rational verifier `scripts/verify_poisson_phase_analytic.py` subdivides
`[0,1]` into six dyadic intervals and verifies that every Bernstein
coefficient of `P` on every interval is strictly positive.  Hence `D>0` on
`(0,1]`.

The earlier draft tried to extend this to `lambda>=1` by claiming

\[
D(\lambda)\ge
((\lambda-1)^2+1)(\lambda-\log\lambda)
+2\lambda(\lambda-1)e^{-\lambda}-(1-e^{-\lambda}).
\tag{5}
\]

from the elementary lower bounds on `H,H',H''`. This implication is invalid:
after direct substitution the coarse lower bound is negative at `lambda=2`,
whereas (5) is positive. Thus the valid conclusion of this section is only

\[
F''(\lambda)>0\qquad(0<\lambda\le1).
\]

In particular, the stationary point below `0.44` is unique on `(0,1]`.

For `lambda>1`, no second-derivative estimate is needed. Poisson entropy is
nondecreasing: if `mu>lambda`, write

\[
X_\mu=X_\lambda+Y,
\qquad Y\sim\operatorname{Pois}(\mu-\lambda)
\]

independently. Then

\[
H(X_\mu)\ge H(X_\mu\mid Y)=H(X_\lambda).
\]

Since `H` is differentiable, `H'(lambda)>=0`. The sign of `F'` is the sign of

\[
S(\lambda)=\lambda H'(\lambda)+(\lambda-1)H(\lambda).
\]

For every `lambda>1`, the second term is strictly positive and the first is
nonnegative, so `S(lambda)>0`. At `lambda=1`, positivity follows from the
strict increase of `F'` on `(0,1]` and its already certified positive value at
`0.44`. Therefore the root below `0.44` is the unique stationary point on the
whole positive axis and the unique global minimizer of `F`.

## 3. Convexity of r as a function of g before the tangent

The sign of `d^2r/dg^2` is the sign of `r''+r'`.  Its numerator is

\[
C(\lambda):=\lambda^3(r''+r')
=\lambda^2H''+(\lambda^2-2\lambda)H'+(2-\lambda)H.
\tag{6}
\]

For `0 < lambda <= 11/25`, apply the same bounds as above and additionally
`-log lambda >= 1-lambda`.  One obtains

\[
C(\lambda)\ge\lambda R(\lambda),
\]

\[
R(x)=1-\frac{331}{100}x+\frac{431}{100}x^2
-\frac83x^3+\frac23x^4.
\tag{7}
\]

The exact Bernstein coefficients of `R` on `[0,11/25]` are

\[
1,\quad \frac{6359}{10000},\quad\frac{38519}{93750},
\quad\frac{201089}{750000},\quad\frac{412139}{2343750},
\]

all positive.  Hence the curve `(g(lambda),r(lambda))` is strictly convex
through `lambda=11/25=0.44`.

The exact rational Poisson-series verifier proves that the stationary
equation changes sign inside

\[
0.4399316012447<\lambda_*<0.4399316012449<0.44.
\]

Consequently the valid curvature interval covers the entire low-error branch.
The global uniqueness argument above makes the line from this tangent to
`(1,0)` a supporting line for the whole remaining curve, because

\[
F(\lambda)\ge F(\lambda_*)\qquad(\lambda>0).
\]

## 4. Exact reproduction

Run

```bash
python3 scripts/verify_poisson_phase_analytic.py
python3 scripts/verify_poisson_root_certificate.py
```

The first output certifies the two polynomial positivity claims. The second
uses rational Taylor remainders and a geometric Poisson-tail bound to certify
the signs of the stationary equation at rational endpoints. Both use only
Python integer arithmetic and `fractions.Fraction` for their logical tests.

## 5. Certified phase constants

The verifier establishes

\[
0.4399316012447<\lambda_*<0.4399316012449,
\]

\[
0.35591952612072764
<\varepsilon_*<
0.35591952612085648,
\]

and

\[
4.4012229659190423
<C_*<
4.4012229659230444
\quad\text{bits}.
\]

The longer decimal strings used elsewhere are compatible regression values;
the intervals above are formally supported values for the global phase point.
