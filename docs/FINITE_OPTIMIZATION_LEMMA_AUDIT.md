# Audit of the finite heterogeneous-fingerprint optimization

Consider, for integers \(n,q\ge 1\),

\[
M_{n,q}=\max\left\{\sum_{i=1}^q p_i(1-p_i)^n:
p_i\ge 0,\ \sum_{i=1}^q p_i\le 1\right\}.
\]

The formula asserted as (4) in `EXACT_STATE_HETEROGENEOUS_FINGERPRINTS.md`
is correct.  In fact it follows from a global affine-majorant lemma, so no
case-by-case KKT classification is needed.

## Lemma (global tangent majorant below the mode)

Let

\[
f_n(x)=x(1-x)^n,\qquad b=\frac1{n+1}.
\]

For every \(a\in(0,b]\), the tangent line

\[
T_a(x)=f_n(a)+f_n'(a)(x-a)
\]

satisfies

\[
f_n(x)\le T_a(x)\qquad (0\le x\le1).
\tag{A}
\]

If \(a<b\), equality in (A) holds only at \(x=a\).  If \(a=b\),
\(T_b\equiv f_n(b)\), and equality again holds only at \(x=b\).

### Proof

The derivatives are

\[
f_n'(x)=(1-x)^{n-1}(1-(n+1)x)
\]

and, in the interior (with the evident endpoint interpretation when
\(n=1\)),

\[
f_n''(x)=n(1-x)^{n-2}((n+1)x-2).
\]

Thus \(f_n\) is strictly concave on \([0,b]\), while \(b\) is its unique
global maximizer on \([0,1]\).  Concavity gives \(f_n(x)\le T_a(x)\) for
\(x\in[0,b]\).  Moreover \(f_n'(a)\ge0\), so for \(x\in[b,1]\),

\[
T_a(x)\ge T_a(b)\ge f_n(b)\ge f_n(x).
\]

Strict concavity on \([0,b]\), and the strict inequalities
\(T_a(b)>f_n(b)\) when \(a<b\), give the equality statement. \(\square\)

## Theorem (exact finite optimum)

For all integers \(n,q\ge1\),

\[
M_{n,q}=
\begin{cases}
\displaystyle
\frac{q}{n+1}\left(\frac n{n+1}\right)^n,
&q\le n+1,\\[1.2ex]
\displaystyle
\left(1-\frac1q\right)^n,
&q\ge n+1.
\end{cases}
\tag{B}
\]

In the first regime the unique maximizing vector is
\(p_i=1/(n+1)\) for every \(i\), leaving slack
\(1-q/(n+1)\).  In the second regime the unique maximizing vector is
\(p_i=1/q\) for every \(i\).  At \(q=n+1\), the two descriptions coincide.

### Proof

If \(q\le n+1\), the pointwise bound

\[
f_n(p_i)\le f_n(b)=\frac1{n+1}\left(\frac n{n+1}\right)^n
\]

gives the first branch, and setting every \(p_i=b\) is feasible and attains
it.

If \(q\ge n+1\), set \(a=1/q\le b\).  Applying (A) coordinatewise gives

\[
\begin{aligned}
\sum_{i=1}^q f_n(p_i)
&\le \sum_{i=1}^q\bigl(f_n(a)+f_n'(a)(p_i-a)\bigr)\\
&=qf_n(a)+f_n'(a)\left(\sum_{i=1}^q p_i-1\right)\\
&\le qf_n(a)
=\left(1-\frac1q\right)^n,
\end{aligned}
\]

because \(f_n'(a)\ge0\).  The uniform vector \(p_i=a\) attains the bound.
The equality conditions in the lemma prove uniqueness. \(\square\)

## Why ordinary Jensen or bare KKT is insufficient

The function \(f_n\) is not concave on all of \([0,1]\): its inflection
point is \(2/(n+1)\).  Consequently a statement that simply invokes Jensen
on the whole feasible region would be invalid.  The global tangent majorant
is the missing argument: the tangent is taken to the left of the mode, and
after the mode its nonnegative slope keeps it above the decreasing function.

The KKT equations are consistent with (B), but are less economical.  At an
interior stationary point with the mass constraint active they require
\(f_n'(p_i)=\lambda\) for all \(i\); because \(f_n'\) is not globally
one-to-one, this alone permits apparent two-level candidates.  Inequality
(A) rules out all such candidates globally, as well as boundary vectors
with zero coordinates or coordinates beyond the inflection point.

## Computational pressure test

Two independent finite searches found no counterexample:

1. random Dirichlet search over the active simplex for
   \(1\le n\le20\) and \(n+1\le q\le n+15\), using several concentration
   parameters from \(0.01\) through \(10\);
2. exhaustive rational grids (including slack mass) for
   \(1\le n\le7\), \(1\le q\le8\), with denominator 50 for \(q\le4\)
   and denominator 18 otherwise.

These computations are only a pressure test; theorem (B) is established by
the analytic proof above.

## Audit conclusion

Equation (4) is **proved**, not conjectural.  The only correction needed in
the source note is to replace the candidate language and the stated proof
gap by the theorem and tangent-majorant proof above.  No finite \((n,q)\)
counterexample exists.
