# Poisson-entropy phase transition: reduction and verified identities

Let (X_\lambda\sim\operatorname{Poi}(\lambda)), and use natural logarithms.
Changing to bits multiplies all rates and derivatives by (1/\log 2), so it
does not affect signs or the transition point.  Write

\[
H(\lambda)=H(X_\lambda),\qquad
r(\lambda)=\frac{H(\lambda)}{\lambda},\qquad
g(\lambda)=1-e^{-\lambda},\qquad
F(\lambda)=e^\lambda r(\lambda).
\]

This note records the exact analytic reduction.  It also states clearly the
one remaining inequality: a completely symbolic proof of that inequality has
not yet been supplied.  The accompanying script verifies it numerically over
a large grid but is not directed-rounding interval arithmetic.

## 1. Entropy derivative identities

For every (\lambda>0), termwise differentiation of the Poisson series gives

\[
H'(\lambda)
=\mathbb E\log(X_\lambda+1)-\log\lambda,
\tag{1}
\]

and a second differentiation, using

\[
\frac d{d\lambda}\mathbb E f(X_\lambda)
=\mathbb E[f(X_\lambda+1)-f(X_\lambda)],
\]

gives

\[
H''(\lambda)
=\mathbb E\log\frac{X_\lambda+2}{X_\lambda+1}-\frac1\lambda.
\tag{2}
\]

The differentiations are justified uniformly on compact subsets of
((0,\infty)): after one or two differentiations the summands are bounded by
a polynomial in (k), times the Poisson mass, times (O(k\log k)).

Consequently

\[
r'=\frac{H'}\lambda-\frac H{\lambda^2},
\qquad
r''=\frac{H''}\lambda-\frac{2H'}{\lambda^2}
       +\frac{2H}{\lambda^3}.
\tag{3}
\]

## 2. The two geometric sign tests

Since (g'=e^{-\lambda}>0), the curvature of the parametric curve when
viewed as (r=r(g)) has sign

\[
\operatorname{sgn}\frac{d^2r}{dg^2}
=\operatorname{sgn}(r''+r').
\tag{4}
\]

The line through ((g(a),r(a))) and the endpoint ((1,0)) has equation

\[
L_a(g)=e^a r(a)(1-g)=F(a)(1-g).
\]

At (g(\lambda)), the assertion that the curve lies above this line is

\[
r(\lambda)\ge e^{a-\lambda}r(a),
\]

which is exactly

\[
F(\lambda)\ge F(a).
\tag{5}
\]

Thus the claimed supporting-line property for all (\lambda\ge a) follows
immediately if (a) is the unique global minimizer of (F).

Differentiating,

\[
F'=e^\lambda(r+r'),
\qquad
F''=e^\lambda(r+2r'+r'').
\tag{6}
\]

The tangency condition is (F'(a)=0).  In terms of (H),

\[
r+r'=0
\quad\Longleftrightarrow\quad
\lambda H'(\lambda)+(\lambda-1)H(\lambda)=0.
\tag{7}
\]

## 3. A sufficient analytic lemma

All three geometric claims follow from the following single inequality and a
short local sign check.

**Lemma A.** For every (\lambda>0),

\[
F''(\lambda)
=e^\lambda\bigl(r+2r'+r''\bigr)>0.
\tag{8}
\]

Indeed, strict convexity makes (F') strictly increasing.  The small-load
expansion

\[
H(\lambda)=\lambda(1-\log\lambda)+O(\lambda^2|\log\lambda|)
\]

implies (F'(\lambda)=-1/\lambda+O(|\log\lambda|)\to-\infty).
The standard Poisson-entropy asymptotic

\[
H(\lambda)=\tfrac12\log(2\pi e\lambda)+O(1/\lambda)
\]

implies (F'(\lambda)>0) for all sufficiently large (\lambda).  Hence (F')
has exactly one zero (\lambda_*), and (F) has a unique global minimum there.
Equation (5) then proves the global supporting-line assertion.

For the low-error branch it remains only to prove

\[
r''(\lambda)+r'(\lambda)>0
\quad(0<\lambda\le\lambda_*).
\tag{9}
\]

This is a weaker inequality than Lemma A on this interval after using
(r+r'<0): from

\[
r+2r'+r''=(r''+r')+(r+r')
\]

Lemma A alone does not imply (9).  It must be checked separately.  Equations
(1)--(3) reduce both (8) and (9) to explicit Poisson expectations.

The numerical verifier finds

\[
\lambda_*=0.439931601244785\ldots,
\quad
\varepsilon_*=0.355919526120782\ldots,
\]

and

\[
e^{\lambda_*}r(\lambda_*)
=3.050695289843851\ldots\text{ nats}
=4.401222965921043\ldots\text{ bits}.
\]

It also finds that the full curve (r(g)) changes curvature only later, at

\[
\lambda_{\rm infl}=1.353077884158115\ldots.
\]

Thus the requested statement "convex on ((0,g_*))" is numerically consistent
and is not relying on the tangent occurring at the curve's inflection point.

## 4. What is and is not proved here

Equations (1)--(7), the reduction of the supporting-line claim to the unique
minimum of (F), and the endpoint/asymptotic arguments are rigorous.

The remaining global sign obligations are precisely Lemma A and (9).  The
dependency-free script evaluates the exact expectation identities, locates
the roots, and tests the signs on a dense logarithmic grid.  It is suitable as
a reproducible regression artifact, but floating-point sampling cannot rule
out a narrow sign change.  A paper-level proof still needs one of:

1. analytic bounds for the expectations in (1)--(2), split into compact and
   asymptotic load ranges; or
2. outward-rounded interval arithmetic on a compact interval, together with
   analytic small- and large-(\lambda) tail bounds.

Accordingly, the phase-transition theorem should remain labelled a theorem
candidate until (8) and (9) receive that final certification.

## 5. Reproduction

Run

```bash
python3 scripts/verify_poisson_phase_transition.py
```

from the repository directory.  The program has no third-party dependencies.
