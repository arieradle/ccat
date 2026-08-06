# Cyclotomic Coefficient Arithmetic

## Part XVIII — Ternary Sharpness and Uniform Cyclotomic Axis Rigidity

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete for the sharp ternary capacity, the visible three-term identity classification, ternary quadratic and cubic visibility, and the arbitrary-context axis-rigidity reduction; the uniform upper bound for all nonreal contexts remains open  
**Scope:** Common-depth rank-three factorial circuits with at most two positive endpoints, exact identities in the visible one-direction sector, the complete formula

\[
\boxed{C^{\mathrm{cd}}_3(3,2)=4,}
\]

uniform real/anti-real axis rigidity for the chiral five-jet conic, the endpoint obstruction invariants \(\Omega_d,\Delta_d,\Sigma_d\), and the remaining route to

\[
C^{\mathrm{cd}}_d(3,2)=4\qquad(d\ge 1).
\]

---

# 0. Purpose, status, and relation to Part XVII

Part XVII established three facts.

1. The self-conjugate binary context is sharp:
   \[
   C^{\mathrm{cd}}_2(3,2)=4.
   \]
2. Every context admits a three-term, two-endpoint circuit of excess four:
   \[
   C^{\mathrm{cd}}_d(3,2)\ge4.
   \]
3. For every visible two-endpoint direction with nonzero quadratic cumulant, dependence of the first five local jets is governed by one explicit chiral conic.

The open question was whether the conic can contain exponent-lattice points that do not come from exact identities. The first nonreal context, \(d=3\), is the decisive test.

This chapter proves four new conclusions.

## Proved conclusion A — exact visible identities

For every context \(d\), every exact three-term dependence in a visible one-direction family comes from one of three elementary binomial units. There are no hidden three-term identities.

## Proved conclusion B — full ternary visibility

At \(d=3\), every visible endpoint direction has both

\[
C\ne0
\qquad\text{and}\qquad
J\ne0.
\]

Thus neither quadratic invisibility nor disappearance of chirality occurs in the visible ternary sector.

## Proved conclusion C — uniform cyclotomic axis rigidity

At every nonreal cyclotomic context, the chiral conic forces each centered drift point onto the real or anti-real axis of the cyclotomic field. Every possible five-jet rank loss has the universal shape

\[
\boxed{x_1=u,\qquad x_2=-u,\qquad x_3=v,}
\]

with

\[
u\in\tfrac12\mathbb Z,
\qquad
v\in K_d^-,
\qquad
n_1=n_2.
\]

This yields three endpoint-only obstructions \(\Omega_d,\Delta_d,\Sigma_d\).

## Proved conclusion D — sharp ternary capacity

For \(d=3\), the endpoint obstruction vanishes only for the already classified exact identities. The unique subcritical pair \((1,2)\) is handled by a separate Wronskian argument. Therefore

\[
\boxed{C^{\mathrm{cd}}_3(3,2)=4.}
\]

The sharp data are now

\[
\boxed{
C^{\mathrm{cd}}_1(3,2)
=
C^{\mathrm{cd}}_2(3,2)
=
C^{\mathrm{cd}}_3(3,2)
=4.
}
\]

The uniform conjecture remains open for \(d\ge4\). The remaining obstacles are no longer an uncontrolled high-dimensional conic: they are explicit endpoint conditions, possible vanishing of low cumulants, and the subcritical sector.

Throughout,

\[
D=q\frac d{dq},
\qquad
q=\zeta e^x,
\]

so that \(D=d/dx\). All calculations are exact.

---

# 1. Setup: visible two-endpoint common-depth families

Fix an integer \(d\ge1\) and a primitive \(d\)-th root of unity \(\zeta\). Let

\[
0<A<B,
\qquad
r_A=\left\lfloor\frac Ad\right\rfloor,
\qquad
r_B=\left\lfloor\frac Bd\right\rfloor.
\]

The pair is **visible** if

\[
r_A+r_B>0.
\]

A two-endpoint factorial term is

\[
T(q)=q^\alpha(q;q)_A^u(q;q)_B^v,
\]

and its depth at context \(d\) is

\[
v_{\Phi_d}(T)=ur_A+vr_B.
\]

For a visible pair, equal-depth exponent vectors differ in one primitive lattice direction. Put

\[
g=\gcd(r_A,r_B)
\]

when both entries are positive. Define

\[
(e_A,e_B)=
\begin{cases}
\left(\dfrac{r_B}{g},-\dfrac{r_A}{g}\right),&r_A,r_B>0,\\[3mm]
(1,0),&r_A=0<r_B.
\end{cases}
\]

The associated zero-depth ratio is

\[
\boxed{
R_{A,B}(q)=(q;q)_A^{e_A}(q;q)_B^{e_B}.
}
\]

It is a local unit at \(q=\zeta\).

Let

\[
R_0=R_{A,B}(\zeta),
\qquad
\lambda=D\log R_{A,B}(\zeta),
\]

where evaluation is interpreted after local regularization. Define

\[
\boxed{
H(x)=
\log\frac{R_{A,B}(\zeta e^x)}{R_0}
-\lambda x.
}
\]

Then

\[
H(0)=H'(0)=0.
\]

After factoring one common-depth base term and absorbing nonzero residual constants into the outer coefficients, every local circuit term has the form

\[
\boxed{
f_{p,n}(x)=\exp\bigl(px+nH(x)\bigr),
\qquad
p=\beta+n\lambda,
\qquad
\beta,n\in\mathbb Z.
}
\]

Write

\[
C=H''(0),
\qquad
J=H^{(3)}(0),
\qquad
D_4=H^{(4)}(0).
\]

Because \(R_{A,B}\) is signed-reciprocal, there is an integer \(E\) and a sign \(\varepsilon\in\{\pm1\}\) such that

\[
R_{A,B}(q^{-1})=\varepsilon q^{-E}R_{A,B}(q).
\]

Differentiating the local reciprocity relation gives

\[
\lambda+\bar\lambda=E.
\]

Define the anti-real drift

\[
\boxed{
\mu=\lambda-\frac E2.
}
\]

Then

\[
\bar\mu=-\mu.
\]

The normalized reciprocal-germ theorem gives

\[
C,D_4\in K_d^+,
\qquad
J\in K_d^-,
\]

where

\[
K_d=\mathbb Q(\zeta),
\qquad
K_d^+=\{z:\bar z=z\},
\qquad
K_d^-=\{z:\bar z=-z\}.
\]

---

# 2. Exact three-term identities in a visible direction

The first theorem classifies exact functional dependence before any finite-jet question is considered.

## Theorem 2.1 — Uniform visible three-term identity classification

Let \((A,B)\) be visible at context \(d\), and let \(R=R_{A,B}\). Suppose three distinct functions

\[
q^{\beta_i}R(q)^{n_i},
\qquad i=1,2,3,
\]

are linearly dependent over \(\mathbb Q\). Apart from repeated proportional terms, this occurs if and only if one of the following holds.

### Family I — invisible lower endpoint \(A=1\)

\[
r_A=0<r_B,
\qquad
A=1,
\qquad
R(q)=1-q.
\]

Every dependence is obtained from

\[
\boxed{1=q+(1-q)}
\]

by multiplying by a monomial and a power of \(R\).

### Family II — adjacent endpoints in one \(d\)-block

\[
B=A+1,
\qquad
r_A=r_B>0,
\qquad
R(q)=\frac1{1-q^B}.
\]

Every dependence is obtained from

\[
\boxed{1=q^B+(1-q^B)}.
\]

### Family III — the positive exceptional pair

\[
d=1,
\qquad
(A,B)=(1,2),
\qquad
R(q)=\frac1{1+q}.
\]

Here the nontrivial binomial-unit relation is

\[
\boxed{R^{-1}=1+q}.
\]

Equivalently, after multiplying by \(R\),

\[
\boxed{1=R+qR}.
\]

Every dependence is obtained from this relation by multiplying by a common monomial and a common power of \(R\).

No other exact three-term identities occur in a visible two-endpoint family.

### Proof

Assume

\[
c_1q^{\beta_1}R^{n_1}
+c_2q^{\beta_2}R^{n_2}
+c_3q^{\beta_3}R^{n_3}=0,
\qquad
c_i\ne0.
\tag{2.1}
\]

Because \(R\) is a nonconstant rational function whose zeros and poles are roots of unity, choose a nonzero root of unity at which \(R\) has nonzero valuation. The monomial \(q\) is a unit there.

If \(n_1,n_2,n_3\) were pairwise distinct, the three summands in (2.1) would have pairwise distinct valuations. The term of least valuation would be unique and could not cancel. Thus two of the \(n_i\) coincide.

If all three coincide, factor out the common power of \(R\). The remaining relation is a relation among three distinct Laurent monomials in \(q\), which is impossible. Hence, after relabeling,

\[
n_1=n_2=n,
\qquad
n_3=n+s,
\qquad
s\ne0.
\]

After dividing by a common monomial, a common power of \(R\), and one nonzero coefficient, the relation becomes

\[
R(q)^s=1-\eta q^k
\tag{2.2}
\]

for some \(k\ge1\) and \(\eta\in\mathbb Q^\times\). The constant term of every \(q\)-factorial is one, so \(R(0)=1\); this fixes the constant term on the right side.

Every zero or pole of \(R^s\) is a root of unity. Hence every zero of \(1-\eta q^k\) has modulus one. Therefore \(|\eta|=1\). Since \(\eta\in\mathbb Q\),

\[
\eta=\pm1.
\]

Thus

\[
R^s=1-q^k
\qquad\text{or}\qquad
R^s=1+q^k.
\tag{2.3}
\]

Both right sides are squarefree products of cyclotomic polynomials.

### Case 1: \(r_A,r_B>0\)

The exponent of \(\Phi_B\) in \(R\) is

\[
v_{\Phi_B}(R)=-\frac{r_A}{g}<0,
\]

because \(A<B\). The right side of (2.3) is a polynomial, so \(s<0\). Its \(\Phi_B\)-exponent is at most one, and therefore

\[
-s=1,
\qquad
\frac{r_A}{g}=1.
\tag{2.4}
\]

Hence

\[
R^{-1}=1\pm q^k,
\qquad
g=r_A,
\qquad
r_A\mid r_B.
\tag{2.5}
\]

The largest cyclotomic index in \(R^{-1}\) is \(B\). Therefore \(B=k\) in the minus case and \(B=2k\) in the plus case.

Suppose \(A\le B-2\). Then \(\Phi_{B-1}\) occurs in \((q;q)_B\) but not in \((q;q)_A\). Hence it occurs in \(R^{-1}\). It cannot divide \(1-q^B\), because \(B-1\nmid B\) except at \(B=2\); and it cannot divide \(1+q^{B/2}\), because an element of order \(B-1\) cannot satisfy a power equation of order dividing \(B\), again except at the trivial boundary \(B=2\). Thus

\[
A=B-1.
\]

Adjacent quotient depths differ by at most one. Since \(r_A\mid r_B\), either

\[
r_A=r_B
\]

or

\[
r_A=1,
\qquad
r_B=2.
\]

In the first case,

\[
R^{-1}
=
\frac{(q;q)_B}{(q;q)_A}
=
1-q^B,
\]

which is Family II.

In the second case, adjacency gives

\[
A=2d-1,
\qquad
B=2d.
\]

If \(d>1\), the factor \(\Phi_A\) remains in the denominator of

\[
R^{-1}=\frac{(q;q)_B}{(q;q)_A^2},
\]

because \(A\nmid B\). Thus \(R^{-1}\) is not a polynomial, contradicting (2.5). If \(d=1\), then \((A,B)=(1,2)\), and

\[
R^{-1}
=
\frac{(q;q)_2}{(q;q)_1^2}
=
\frac{1-q^2}{1-q}
=
1+q.
\]

This is Family III.

### Case 2: \(r_A=0<r_B\)

The primitive direction is \((1,0)\), so

\[
R=(q;q)_A.
\]

The factor \(\Phi_A\) occurs with exponent one, so squarefreeness in (2.3) forces \(s=1\).

If \(A\ge3\), then \(\Phi_{A-1}\) divides \((q;q)_A\), but it divides neither \(1-q^A\) nor the possible plus-binomial \(1+q^{A/2}\). Hence \(A\le2\).

For \(A=2\),

\[
(q;q)_2=(1-q)(1-q^2)
\]

is not a binomial. Thus \(A=1\), and

\[
R=1-q.
\]

This is Family I.

Conversely, each displayed family gives the stated exact identity. Multiplication by a common monomial and power of \(R\) produces every relation obtained in the reduction to (2.2). ∎

## Corollary 2.2 — Exact identities are binomial units

Every exact visible three-term dependence is supported by a ratio of the form

\[
\boxed{R(q)=(1-q^k)^\varepsilon,\qquad \varepsilon\in\{1,-1\},}
\]

except for the harmless positive-context unit \((1+q)^{-1}\).

---

# 3. Ternary one-factor cumulants

From now through Section 8, set

\[
d=3,
\qquad
\zeta=\zeta_3,
\qquad
\sigma=\sqrt{-3}=2\zeta+1.
\]

Then

\[
K_3=\mathbb Q(\sigma),
\qquad
K_3^+=\mathbb Q,
\qquad
K_3^-=\sigma\mathbb Q.
\]

Write

\[
N=3a+s,
\qquad
0\le s\le2.
\]

For the regularized logarithm of \((q;q)_N\), write

\[
D\log(q;q)_N(\zeta)=\frac{N(N+1)}4+\sigma\ell_s(a),
\]

and denote the next three cumulants by

\[
C_s(a),
\qquad
\sigma j_s(a),
\qquad
D_s(a).
\]

## Proposition 3.1 — Closed ternary cumulant formulas

The exact formulas are

\[
\boxed{
\begin{aligned}
\ell_0(a)&=\frac a6,\\
\ell_1(a)&=-\frac{2a+1}{6},\\
\ell_2(a)&=\frac{a+1}{6},
\end{aligned}
}
\tag{3.1}
\]

\[
\boxed{
\begin{aligned}
C_0(a)&=\frac{a(54a^2+9a-5)}{24},\\
C_1(a)&=\frac{(2a+1)(27a^2+27a+8)}{24},\\
C_2(a)&=\frac{(a+1)(54a^2+99a+40)}{24},
\end{aligned}
}
\tag{3.2}
\]

\[
\boxed{
\begin{aligned}
j_0(a)&=-\frac{a(9a^2-2)}9,\\
j_1(a)&=\frac{(2a+1)(9a^2+9a+1)}9,\\
j_2(a)&=-\frac{(a+1)(9a^2+18a+7)}9,
\end{aligned}
}
\tag{3.3}
\]

and

\[
\boxed{
\begin{aligned}
D_0(a)
&=-\frac{a(13122a^4+405a^3-6930a^2+1013)}{1200},\\
D_1(a)
&=-\frac{(2a+1)(6561a^4+13122a^3+11574a^2+5013a+400)}{1200},\\
D_2(a)
&=-\frac{(a+1)(13122a^4+52083a^3+70587a^2+37413a+6800)}{1200}.
\end{aligned}
}
\tag{3.4}
\]

### Proof

For \(\rho=\zeta\) or \(\zeta^2\), the regularized one-factor kernels are

\[
K_1(\zeta)=\frac12-\frac\sigma6,
\qquad
K_1(\zeta^2)=\frac12+\frac\sigma6,
\]

\[
K_2(1)=\frac1{12},
\qquad
K_2(\zeta)=K_2(\zeta^2)=\frac13,
\]

\[
K_3(1)=0,
\qquad
K_3(\zeta)=\frac\sigma9,
\qquad
K_3(\zeta^2)=-\frac\sigma9,
\]

and

\[
K_4(1)=-\frac1{120},
\qquad
K_4(\zeta)=K_4(\zeta^2)=-\frac13.
\]

Therefore

\[
\ell_s(a)
=
\frac16
\left(
\sum_{\substack{m\le3a+s\\m\equiv2\ (3)}}m
-
\sum_{\substack{m\le3a+s\\m\equiv1\ (3)}}m
\right),
\tag{3.5}
\]

\[
C_s(a)
=
\frac13\sum_{m=1}^{3a+s}m^2
-
\frac14\sum_{k=1}^{a}(3k)^2,
\tag{3.6}
\]

\[
j_s(a)
=
\frac19
\left(
\sum_{\substack{m\le3a+s\\m\equiv1\ (3)}}m^3
-
\sum_{\substack{m\le3a+s\\m\equiv2\ (3)}}m^3
\right),
\tag{3.7}
\]

and

\[
D_s(a)
=
-\frac13\sum_{m=1}^{3a+s}m^4
+
\frac{13}{40}\sum_{k=1}^{a}(3k)^4.
\tag{3.8}
\]

Insert the ordinary formulas for power sums and simplify. This gives (3.1)–(3.4). ∎

---

# 4. Full ternary quadratic and cubic visibility

Let

\[
A=3a+s,
\qquad
B=3b+t,
\qquad
0\le s,t\le2.
\]

If \(a,b>0\), zero tests are unchanged if the primitive direction is temporarily scaled from

\[
\left(\frac bg,-\frac ag\right)
\]

to \((b,-a)\). In that unscaled direction,

\[
\ell=b\ell_s(a)-a\ell_t(b),
\]

\[
C=bC_s(a)-aC_t(b),
\]

\[
j=bj_s(a)-aj_t(b),
\]

\[
D_4=bD_s(a)-aD_t(b),
\]

and

\[
\mu=\sigma\ell,
\qquad
J=\sigma j.
\]

## Theorem 4.1 — Ternary quadratic visibility

For every visible ternary endpoint pair,

\[
\boxed{C\ne0.}
\]

### Proof

If \(a=0<b\), then \(A\in\{1,2\}\), the primitive direction is \((1,0)\), and (3.2) gives

\[
C_1(0)=\frac13,
\qquad
C_2(0)=\frac53.
\]

Thus \(C\ne0\).

Assume \(a,b>0\). Define

\[
V_s(a)=\frac{C_s(a)}a.
\]

From (3.2),

\[
\begin{aligned}
V_0(a)&=\frac94a^2+\frac38a-\frac5{24},\\
V_1(a)&=\frac94a^2+\frac{27}{8}a+\frac{43}{24}+\frac1{3a},\\
V_2(a)&=\frac94a^2+\frac{51}{8}a+\frac{139}{24}+\frac5{3a}.
\end{aligned}
\tag{4.1}
\]

The following differences are positive for every \(a\ge1\):

\[
V_1(a)-V_0(a)=\frac{(3a+1)^2}{3a},
\]

\[
V_0(a+1)-V_1(a)=\frac{36a^2+15a-8}{24a},
\]

\[
V_2(a)-V_0(a+1)=\frac{36a^2+81a+40}{24a},
\]

\[
V_1(a+1)-V_2(a)
=
\frac{36a^3+75a^2+7a-40}{24a(a+1)},
\]

\[
V_2(a+1)-V_1(a+1)=\frac{(3a+5)^2}{3(a+1)},
\]

and

\[
V_0(a+2)-V_2(a)
=
\frac{36a^2+45a-20}{12a}.
\]

Hence

\[
V_0(a)<V_1(a)<V_0(a+1)<V_2(a)<V_1(a+1)<V_2(a+1),
\tag{4.2}
\]

and

\[
V_2(a)<V_0(a+2).
\tag{4.3}
\]

Now

\[
C=ab\bigl(V_s(a)-V_t(b)\bigr).
\]

If \(b=a\), then \(A<B\) implies \(s<t\), and (4.2) gives strict inequality. If \(b=a+1\), (4.2) again excludes equality for every residue pair. If \(b\ge a+2\), then

\[
V_t(b)\ge V_0(b)\ge V_0(a+2)>V_2(a)\ge V_s(a).
\]

Thus \(C\ne0\). ∎

## Theorem 4.2 — Ternary cubic visibility

For every visible ternary endpoint pair,

\[
\boxed{J\ne0.}
\]

### Proof

If \(a=0<b\), then (3.3) gives

\[
j_1(0)=\frac19,
\qquad
j_2(0)=-\frac79,
\]

so \(J=\sigma j\ne0\).

Assume \(a,b>0\). Define

\[
W_s(a)=\frac{j_s(a)}a.
\]

Then

\[
\begin{aligned}
W_0(a)&=-a^2+\frac29,\\
W_1(a)&=2a^2+3a+\frac{11}{9}+\frac1{9a},\\
W_2(a)&=-a^2-3a-\frac{25}{9}-\frac7{9a}.
\end{aligned}
\tag{4.4}
\]

The branch \(W_1\) is positive, while \(W_0,W_2\) are negative, so no positive branch can meet a negative branch. Each of \(W_0\) and \(W_2\) is strictly decreasing, so equal-residue collisions are impossible.

For \(A<B\), the only cross-branch equality not already excluded by order is

\[
W_2(a)=W_0(b).
\]

It would imply

\[
b^2=a^2+3a+3+\frac7{9a}.
\tag{4.5}
\]

But

\[
(a+1)^2
<
a^2+3a+3+\frac7{9a}
<
(a+2)^2
\]

for every \(a\ge1\). Hence (4.5) cannot hold for an integer \(b\). Therefore \(j\ne0\), and so \(J=\sigma j\ne0\). ∎

## Corollary 4.3 — No invisible visible direction at \(d=3\)

Every visible ternary pair is in the genuinely chiral five-jet regime:

\[
\boxed{C\ne0,\qquad J\ne0.}
\]

---

# 5. The chiral five-jet conic

We recall the exact local rank-loss equations because they are the input to the new uniform theorem.

Let

\[
f_{p,n}(x)=e^{px+nH(x)},
\qquad
H(0)=H'(0)=0,
\qquad
C=H''(0)\ne0.
\]

The first five derivatives are

\[
\begin{aligned}
f(0)&=1,\\
f'(0)&=p,\\
f''(0)&=p^2+nC,\\
f^{(3)}(0)&=p^3+3pnC+nJ,\\
f^{(4)}(0)&=p^4+6p^2nC+4pnJ+3n^2C^2+nD_4.
\end{aligned}
\tag{5.1}
\]

If three parameter pairs are distinct and two drift values coincide, rows \(0,1,2\) already separate them. If all three drift values coincide, rows \(0,2,4\) give a Vandermonde determinant in the \(n_i\). Thus a five-jet dependence can occur only when the \(p_i\) are pairwise distinct.

## Theorem 5.1 — Chiral five-jet conic

For pairwise distinct \(p_1,p_2,p_3\), the first five jet columns are dependent if and only if there exist \(t,N\in K_d\) and

\[
x_i=p_i-t
\]

such that

\[
\boxed{
\sum_{i=1}^{3}x_i=-\frac{J}{2C},
}
\tag{5.2}
\]

\[
\boxed{
n_i=N-\frac{x_i^2}{C},
}
\tag{5.3}
\]

and

\[
\boxed{
\sum_{i=1}^{3}x_i^2
=
\frac{7J^2-4CD_4}{4C^2}.
}
\tag{5.4}
\]

The center is

\[
3t=p_1+p_2+p_3+\frac{J}{2C}.
\]

### Proof

Rank at most two means each of rows two, three, and four in (5.1) is affine in \(p_i\).

From row two there exist \(a,b\) such that

\[
p_i^2+Cn_i=ap_i+b.
\]

Completing the square gives

\[
n_i=N-\frac{(p_i-t)^2}{C}
\]

for suitable \(N,t\), proving (5.3).

Substitute this expression into row three. Reduce the resulting cubic polynomial in \(p\) modulo

\[
\prod_{i=1}^{3}(p-p_i).
\]

The quadratic coefficient of the remainder vanishes exactly when

\[
3t=p_1+p_2+p_3+\frac{J}{2C},
\]

which is equivalent to (5.2).

Substitute the same quadratic expression into row four. After reduction modulo the same cubic, the remaining quadratic coefficient is

\[
2C^2s_1^2-6C^2s_2+3CD_4-5J^2,
\]

where

\[
s_1=p_1+p_2+p_3,
\qquad
s_2=p_1p_2+p_1p_3+p_2p_3.
\]

Using

\[
\sum_i p_i^2=s_1^2-2s_2
\]

and the formula for \(t\), its vanishing is exactly (5.4).

Conversely, (5.2)–(5.4) make rows two, three, and four affine functions of the three values \(p_i\). Hence all five row vectors lie in the span of rows zero and one, and the columns are dependent. ∎

---

# 6. Uniform cyclotomic axis rigidity

The next theorem is the main arbitrary-context result of this chapter.

## Theorem 6.1 — Uniform Cyclotomic Axis-Rigidity Theorem

Let \(d\ge3\), let \((A,B)\) be visible, and assume

\[
C\ne0,
\qquad
J\ne0.
\]

Suppose three distinct local terms

\[
f_i(x)=\exp\bigl(p_ix+n_iH(x)\bigr),
\qquad
p_i=\beta_i+n_i\lambda,
\qquad
\beta_i,n_i\in\mathbb Z,
\]

have dependent first five jets.

Then, after relabeling, their centered conic coordinates have the form

\[
\boxed{
x_1=u,
\qquad
x_2=-u,
\qquad
x_3=v,
}
\tag{6.1}
\]

where

\[
\boxed{
u\in K_d^+,\qquad v\in K_d^-.}
\]

Moreover,

\[
\boxed{n_1=n_2,}
\tag{6.2}
\]

\[
\boxed{
u=\frac{\beta_1-\beta_2}{2}\in\frac12\mathbb Z,}
\tag{6.3}
\]

and, with

\[
\Delta=n_3-n_1,
\]

one has

\[
\boxed{
v=\mu\Delta=-\frac{J}{2C}.}
\tag{6.4}
\]

Consequently, five-jet dependence is possible only if

\[
\boxed{
\Omega_d(A,B)
:=
\mu(J^2-CD_4)+JC^2
=0,
}
\tag{6.5}
\]

\[
\boxed{
\Delta_d(A,B)
:=
\frac{J^2-CD_4}{2C^3}
\in\mathbb Z\setminus\{0\},
}
\tag{6.6}
\]

and

\[
\boxed{
\Sigma_d(A,B)
:=
\frac{3J^2-2CD_4}{C^2}
\in\{m^2:m\in\mathbb Z\setminus\{0\}\}.
}
\tag{6.7}
\]

More precisely,

\[
\Delta_d(A,B)=n_3-n_1
\]

and

\[
\Sigma_d(A,B)=(\beta_1-\beta_2)^2.
\]

There is also the parity equation

\[
\boxed{
2\beta_3-\beta_1-\beta_2+E\Delta=0.
}
\tag{6.8}
\]

### Proof

By Theorem 5.1,

\[
x_i^2-x_j^2=-C(n_i-n_j)\in K_d^+.
\tag{6.9}
\]

Thus the anti-real parts of the three squares \(x_i^2\) are equal. Their sum is real by (5.4), so the sum of those three equal anti-real parts is zero. Characteristic zero gives

\[
x_i^2\in K_d^+
\qquad(i=1,2,3).
\tag{6.10}
\]

Write

\[
x_i=a_i+b_i,
\qquad
a_i\in K_d^+,
\qquad
b_i\in K_d^-.
\]

Then

\[
x_i^2-\overline{x_i^2}=4a_ib_i.
\]

By (6.10), this is zero. Since \(K_d\) is a field,

\[
a_ib_i=0.
\]

Therefore every \(x_i\) lies on one of the two axes:

\[
\boxed{x_i\in K_d^+\quad\text{or}\quad x_i\in K_d^-.}
\tag{6.11}
\]

The sum in (5.2) is nonzero and anti-real because \(J\ne0\). Hence three real points are impossible.

### Excluding three anti-real points

If all \(x_i\) are anti-real, the real parts of all \(p_i=x_i+t\) are equal. But

\[
p_i^+=\beta_i+\frac E2n_i.
\]

Therefore

\[
x_i-x_j=p_i-p_j=\mu(n_i-n_j).
\tag{6.12}
\]

If \(\mu=0\), the right side is zero, contradicting distinctness. Thus \(\mu\ne0\), and there exists \(\nu\in K_d^+\) such that

\[
x_i=\mu(n_i-\nu).
\]

Substitution into (5.3) gives

\[
n_i=N-\frac{\mu^2}{C}(n_i-\nu)^2.
\]

Thus the three distinct integers \(n_i\) would be roots of one quadratic polynomial, impossible.

### Excluding one real and two anti-real points

The unique real point must be zero because the real parts sum to zero. Relabel so that \(x_1=0\). Then \(n_1=N\), and the same real-part comparison gives

\[
x_i=\mu(n_i-n_1),
\qquad i=2,3.
\]

If \(n_i\ne n_1\), equation (5.3) gives

\[
n_i-n_1
=-\frac{\mu^2}{C}(n_i-n_1)^2,
\]

so every nonzero difference equals the single value

\[
-\frac C{\mu^2}.
\]

Hence \(n_2=n_3\) and then \(x_2=x_3\), contradicting distinctness.

### The surviving pattern

Thus exactly two points are real and one is anti-real. The real parts in (5.2) sum to zero, so the real points are opposite. This proves (6.1).

Because

\[
x_1-x_2=2u\in K_d^+,
\]

while

\[
p_1-p_2
=
\beta_1-\beta_2
+
\frac E2(n_1-n_2)
+
\mu(n_1-n_2),
\]

its anti-real part is \(\mu(n_1-n_2)\).

If \(\mu=0\), every \(p_i\) is real, but

\[
p_1-p_3=x_1-x_3=u-v
\]

has nonzero anti-real part because

\[
v=-\frac{J}{2C}\ne0.
\]

Therefore \(\mu\ne0\), and

\[
n_1=n_2.
\]

It follows that

\[
2u=p_1-p_2=\beta_1-\beta_2,
\]

proving (6.3).

Put

\[
\Delta=n_3-n_1.
\]

Since \(x_1+x_2=0\),

\[
p_3-\frac{p_1+p_2}{2}=v.
\]

Taking anti-real parts gives

\[
v=\mu\Delta.
\]

Taking real parts gives (6.8). Equation (5.2) gives independently

\[
v=-\frac{J}{2C}.
\]

This proves (6.4).

Now (5.4) gives

\[
2u^2+v^2
=
\frac{7J^2-4CD_4}{4C^2}.
\]

Since

\[
v^2=\frac{J^2}{4C^2},
\]

we obtain

\[
u^2=\frac{3J^2-2CD_4}{4C^2}.
\tag{6.13}
\]

Also, from (5.3),

\[
\Delta
=
\frac{u^2-v^2}{C}
=
\frac{J^2-CD_4}{2C^3}.
\tag{6.14}
\]

Because \(\Delta=n_3-n_1\), this proves (6.6). Equation (6.3) and (6.13) give

\[
\frac{3J^2-2CD_4}{C^2}
=(\beta_1-\beta_2)^2,
\]

which proves (6.7).

Finally, substitute (6.14) into

\[
\mu\Delta=-\frac{J}{2C}.
\]

Multiplication by \(2C^3\) gives

\[
\mu(J^2-CD_4)+JC^2=0.
\]

This is (6.5). ∎

## Corollary 6.2 — Endpoint-only rejection test

For a visible endpoint pair with \(C,J\ne0\), the first five jets are independent whenever at least one of the following holds:

\[
\Omega_d(A,B)\ne0,
\]

\[
\Delta_d(A,B)\notin\mathbb Z\setminus\{0\},
\]

or

\[
\Sigma_d(A,B)
\text{ is not a positive integer square}.
\]

No exponent-lattice search is required.

## Corollary 6.3 — Formal independence from \(\varphi(d)\)

The geometry of every possible five-jet failure is always

\[
\text{two opposite half-integral real points}
+
\text{one anti-real point}.
\]

The dimension of the cyclotomic field does not enlarge the formal rank-loss configuration.

---

# 7. The ternary endpoint obstruction

At \(d=3\), write

\[
\mu=\sigma\ell,
\qquad
J=\sigma j.
\]

Since \(\sigma^2=-3\), the uniform obstruction (6.5) becomes

\[
\Omega_3=\sigma\omega,
\]

where

\[
\boxed{
\omega
=
jC^2-\ell(3j^2+CD_4).
}
\tag{7.1}
\]

Thus five-jet dependence requires

\[
\omega=0.
\]

## Theorem 7.1 — Complete ternary endpoint obstruction classification

Let \((A,B)\) be a visible ternary endpoint pair. Then

\[
\boxed{\omega(A,B)=0}
\]

if and only if one of the following exact-identity families occurs:

1. \(A=1\), so \(R=1-q\);
2. \(B=A+1\) and
   \[
   \left\lfloor\frac A3\right\rfloor
   =
   \left\lfloor\frac B3\right\rfloor,
   \]
   so \(R=(1-q^B)^{-1}\).

There are no other visible ternary endpoint pairs with \(\omega=0\).

### Proof

If \(a=0<b\), then \(A=1\) or \(2\). From (3.1)–(3.4),

\[
(\ell,C,j,D_4)\big|_{A=1}
=
\left(-\frac16,\frac13,\frac19,-\frac13\right),
\]

which gives \(\omega=0\), while

\[
(\ell,C,j,D_4)\big|_{A=2}
=
\left(\frac16,\frac53,-\frac79,-\frac{17}{3}\right),
\]

which gives

\[
\omega=-\frac89\ne0.
\]

Now assume \(a,b>0\). Use the unscaled direction \((b,-a)\); scaling all four invariants by the same nonzero factor does not change the equation \(\omega=0\).

For each residue pair \((s,t)\), write

\[
b=
\begin{cases}
a+h,&s<t,\\
a+h+1,&s\ge t,
\end{cases}
\qquad h\ge0.
\tag{7.2}
\]

Substitute (3.1)–(3.4) into (7.1). Exact expansion gives the following sign table.

| \((s,t)\) | exact behavior of \(\omega\) |
|---|---|
| \((0,0)\) | strictly positive |
| \((0,1)\) | zero exactly at \(h=0\); positive for \(h>0\) |
| \((0,2)\) | strictly positive |
| \((1,0)\) | positive at \(h=0\); negative for \(h\ge1\) |
| \((1,1)\) | strictly negative |
| \((1,2)\) | zero exactly at \(h=0\); negative for \(h>0\) |
| \((2,0)\) | nonzero; negative only at \((a,h)=(1,0)\), positive otherwise |
| \((2,1)\) | negative at \(h=0\); positive for \(h\ge1\) |
| \((2,2)\) | strictly positive |

The finite coefficient certificate proving the table is given in Appendix A. Every sign assertion is reduced there to a polynomial with positive integer coefficients after one of the shifts

\[
a=X+1,
\qquad
h=Y,
\qquad
h=Y+1,
\qquad
\text{or}\qquad
a=X+2.
\]

The only zeros are therefore

\[
(s,t,h)=(0,1,0)
\]

and

\[
(s,t,h)=(1,2,0).
\]

These are precisely

\[
(A,B)=(3a,3a+1)
\]

and

\[
(A,B)=(3a+1,3a+2),
\]

that is, adjacent endpoints inside one ternary block. In both cases

\[
R(q)=\frac1{1-q^B}.
\]

Together with \(A=1\), these are exactly the two ternary instances of Theorem 2.1. ∎

---

# 8. Visible ternary five-jet rigidity

The endpoint theorem now closes the visible sector.

## Lemma 8.1 — Binomial units saturate the obstruction

Let

\[
R(q)=(1-q^k)^\varepsilon,
\qquad
\varepsilon\in\{1,-1\},
\qquad
3\nmid k.
\]

For its ternary local germ,

\[
\boxed{
\Omega_3=0,
\qquad
\Delta_3=\varepsilon,
\qquad
\Sigma_3=k^2.
}
\tag{8.1}
\]

If three columns have dependent first five jets, then after relabeling

\[
n_1=n_2=n,
\qquad
n_3=n+\varepsilon,
\]

and

\[
\beta_1-\beta_2=\pm k.
\]

The parity equation forces the exact identity

\[
q^{\beta_2}R^n
=
q^{\beta_2+k}R^n
+
q^{\beta_2}R^{n+\varepsilon}
\]

or the same relation with the first two terms interchanged.

### Proof

At a nontrivial ternary residue,

\[
C=\varepsilon\frac{k^2}{3},
\qquad
J=\pm\varepsilon\frac{\sigma k^3}{9},
\qquad
D_4=-\varepsilon\frac{k^4}{3},
\]

and

\[
\mu=\mp\varepsilon\frac{\sigma k}{6}.
\]

Direct substitution gives (8.1).

Theorem 6.1 then gives

\[
n_3-n_1=\varepsilon
\]

and

\[
\beta_1-\beta_2=\pm k.
\]

The signed reciprocal degree is \(E=\varepsilon k\). If

\[
\beta_1-\beta_2=k,
\]

then (6.8) gives \(\beta_3=\beta_2\). Since

\[
R^\varepsilon=1-q^k,
\]

the displayed exact identity follows. The other sign is obtained by interchanging the first two terms. ∎

## Theorem 8.2 — Visible ternary five-jet injectivity

For every visible ternary endpoint pair, the map

\[
\operatorname{span}
\{q^{\beta_i}R_{A,B}^{n_i}:1\le i\le3\}
\longrightarrow
K_3[[x]]/(x^5)
\]

is injective.

Equivalently, every nonzero visible common-depth circuit satisfies

\[
\boxed{
\operatorname{ord}_{q=\zeta_3}F\le h+4.
}
\]

### Proof

Factor the common depth and pass to the local unit family.

If the actual function span has dimension three and the first five jets were dependent, repeated drift values are excluded by the elementary minors preceding Theorem 5.1. Thus the chiral conic applies. Theorems 4.1 and 4.2 give \(C,J\ne0\), and Theorem 6.1 forces \(\Omega_3=0\). By Theorem 7.1, the endpoint ratio is one of the binomial units in Lemma 8.1. That lemma shows the rank loss is an exact functional identity, contradicting dimension three.

If the actual function span has dimension at most two, take two distinct functions and divide one by the other. In each exact-identity family the ratio is

\[
q^r(1-q^k)^s.
\]

After its value at \(\zeta_3\) is normalized to one, the logarithm has first derivative

\[
r+sD\log(1-q^k)(\zeta_3).
\]

If this derivative does not vanish, the two-term difference has order one. If it vanishes and \(s\ne0\), the second derivative is

\[
sC_k
\]

with \(C_k\ne0\), so the order is exactly two. If \(s=0\), distinctness gives \(r\ne0\), so the order is one. Thus a nonzero two-dimensional combination cannot vanish to order five.

Hence the five-jet map is injective on the actual span in every visible case. ∎

---

# 9. The unique subcritical ternary pair

For \(d=3\), the only pair with

\[
0<A<B<3
\]

is

\[
(A,B)=(1,2).
\]

Every term can be written uniquely as

\[
q^\beta(q;q)_1^u(q;q)_2^v
=
q^\beta(1-q)^a(1+q)^b
\]

for integers \(\beta,a,b\). Common depth is zero and gives no one-direction reduction.

## Lemma 9.1 — Two-term subcritical contact

Let

\[
h(q)=q^\beta(1-q)^a(1+q)^b
\]

be nonconstant. After normalizing \(h(\zeta_3)=1\),

\[
\operatorname{ord}_{q=\zeta_3}(h-1)\le2.
\]

### Proof

With

\[
P(q)=q(q^2-1),
\]

one has

\[
\frac{h'}h=\frac{A(q)}{P(q)},
\]

where

\[
A(q)=(\beta+a+b)q^2+(a-b)q-\beta.
\tag{9.1}
\]

If \(A(\zeta_3)\ne0\), the logarithmic germ has nonzero first derivative and \(h-1\) has order one.

If \(A(\zeta_3)=0\), then \(\Phi_3\mid A\). Since both have degree at most two,

\[
A=c\Phi_3.
\]

If \(c\ne0\), then \(A/P\) has a simple zero at \(\zeta_3\), so the logarithm and therefore \(h-1\) have exact order two. If \(c=0\), then \(h'/h=0\), so \(h\) is constant. ∎

## Lemma 9.2 — Wronskian numerator

After dividing three terms by one local unit, consider

\[
1,
\qquad
f=q^\beta(1-q)^a(1+q)^b,
\qquad
g=q^\gamma(1-q)^c(1+q)^e.
\]

Define

\[
A(q)=(\beta+a+b)q^2+(a-b)q-\beta,
\]

\[
B(q)=(\gamma+c+e)q^2+(c-e)q-\gamma,
\]

and

\[
P(q)=q(q^2-1).
\]

Then

\[
\boxed{
W(1,f,g)
=fg\frac{\mathcal N(q)}{P(q)^3},
}
\tag{9.2}
\]

where

\[
\boxed{
\mathcal N
=
AB(B-A)+P(AB'-BA').
}
\tag{9.3}
\]

Moreover,

\[
\deg\mathcal N\le6.
\]

### Proof

Since

\[
\frac{f'}f=\frac AP,
\qquad
\frac{g'}g=\frac BP,
\]

we have

\[
\frac{f''}f
=
\frac{A^2+A'P-AP'}{P^2},
\]

and the analogous formula for \(g\). Substitute into

\[
W(1,f,g)=f'g''-f''g'.
\]

The terms containing \(P'\) cancel, leaving (9.2)–(9.3). Degree counting gives the bound. ∎

## Lemma 9.3 — Exact quadratic Wronskian elimination

Let

\[
\Phi=q^2+q+1.
\]

For arbitrary quadratic polynomials \(A,B\in\mathbb Q[q]\), define \(\mathcal N\) by (9.3). If

\[
\Phi^3\mid\mathcal N,
\]

then exactly one of the following holds.

1. \(\mathcal N=0\);
2. there exist \(r,s\in\mathbb Q\) such that
   \[
   A=r\Phi,
   \qquad
   B=s\Phi.
   \]

### Proof

Write uniquely

\[
A=\alpha\Phi+uq+v,
\qquad
B=\beta\Phi+rq+s.
\tag{9.4}
\]

The coefficient of \(q^6\) in \(\mathcal N\) is

\[
c=\alpha\beta(\beta-\alpha).
\]

Since \(\deg\mathcal N\le6\), divisibility by \(\Phi^3\) gives

\[
\mathcal N=c\Phi^3.
\tag{9.5}
\]

If \(c=0\), then (9.5) gives \(\mathcal N=0\).

Assume \(c\ne0\). Then \(\alpha\ne0\), and we may divide both quadratics by \(\alpha\). Put

\[
k=\frac{\beta}{\alpha},
\qquad
U=\frac u\alpha,
\qquad
V=\frac v\alpha,
\qquad
R=\frac r\alpha,
\qquad
S=\frac s\alpha.
\]

Then \(k\ne0,1\), and the equation becomes

\[
\widetilde{\mathcal N}-k(k-1)\Phi^3=0,
\]

where

\[
\widetilde A=\Phi+Uq+V,
\qquad
\widetilde B=k\Phi+Rq+S.
\]

Equating the six coefficients gives an ideal in

\[
\mathbb Q(k)[U,V,R,S].
\]

Its reduced Gröbner basis in graded reverse lexicographic order is

\[
\boxed{U,\ V,\ R,\ S.}
\]

The exact SymPy computation producing this basis is recorded in Appendix B. Hence

\[
U=V=R=S=0,
\]

and therefore

\[
u=v=r=s=0.
\]

Thus \(A=\alpha\Phi\) and \(B=\beta\Phi\). ∎

## Lemma 9.4 — Subcritical five-jet injectivity

The first five jets of the subcritical ternary family are injective on every three-dimensional function span.

### Proof

Suppose a nonzero combination of \(1,f,g\) vanishes to order at least five.

If only two coefficients occur, Lemma 9.1 gives a contradiction. Thus all three coefficients are nonzero. Solving for one function in terms of the other two plus an \(O((q-\zeta_3)^5)\) error shows

\[
W(1,f,g)=O((q-\zeta_3)^3).
\]

Because the numerator \(\mathcal N\) has rational coefficients,

\[
\Phi_3^3\mid\mathcal N.
\]

Apply Lemma 9.3.

If \(\mathcal N=0\), then

\[
\left(\frac{g'}{f'}\right)'=0
\]

where defined, so \(g'=cf'\) and \(g=cf+d\). Thus \(1,f,g\) are exactly dependent, contradicting the assumption that their function span has dimension three.

Otherwise

\[
A=r\Phi_3,
\qquad
B=s\Phi_3.
\]

Let \(U\) be the local analytic function defined by

\[
U(\zeta_3)=0,
\qquad
U'=\frac{\Phi_3}{P}.
\]

Since \(\Phi_3\) has a simple zero and \(P(\zeta_3)\ne0\),

\[
\operatorname{ord}_{\zeta_3}U=2.
\]

After constant normalization,

\[
f=e^{rU},
\qquad
g=e^{sU}.
\]

If \(r,s\) are distinct and nonzero, the coefficient matrix of \(1,U,U^2\) in

\[
1,
e^{rU},
e^{sU}
\]

has determinant

\[
\frac12rs(s-r)\ne0.
\]

Thus every nonzero combination has leading \(U\)-degree at most two and therefore \(q\)-order at most four. In particular, order five is impossible.

If \(r=0\), \(s=0\), or \(r=s\), the actual function span has dimension at most two and Lemma 9.1 applies. ∎

## Theorem 9.5 — Subcritical ternary upper bound

Every nonzero three-term circuit supported on \((A,B)=(1,2)\) satisfies

\[
\boxed{
\operatorname{ord}_{q=\zeta_3}F\le4.
}
\]

### Proof

If the function span has dimension three, apply Lemma 9.4. If it has dimension at most two, apply Lemma 9.1. ∎

---

# 10. The sharp ternary theorem

## Theorem 10.1 — Ternary upper bound

Every nonzero common-depth rank-three factorial circuit with at most two positive endpoints satisfies

\[
\boxed{
\operatorname{ord}_{q=\zeta_3}F\le h+4.
}
\]

### Proof

If the endpoint pair is visible, apply Theorem 8.2 after factoring the common depth \(h\).

If the pair is subcritical, it must be \((1,2)\), common depth is zero, and Theorem 9.5 applies.

If the circuit uses fewer than two positive endpoints, it lies in a boundary class already covered by the same five-jet estimate, and in fact by the sharper one-endpoint and two-term bounds of Part XIII.

Therefore every nonzero circuit has excess contact at most four. ∎

## Theorem 10.2 — Universal excess-four witness

For every \(d\ge1\), define

\[
R_d(q)=\frac{(q;q)_d^2}{(q;q)_{2d}},
\qquad
Y_d(q)=q^{d^2}R_d(q)^2.
\]

At every primitive \(d\)-th root,

\[
Y_d(\zeta)=\frac14,
\qquad
DY_d(\zeta)=0,
\qquad
D^2Y_d(\zeta)\ne0.
\]

Hence

\[
\boxed{
\left(Y_d(q)-\frac14\right)^2
}
\]

is a three-term, two-endpoint, common-depth circuit of exact order four.

### Proof

The depth of \(R_d\) is

\[
2\left\lfloor\frac dd\right\rfloor
-
\left\lfloor\frac{2d}{d}\right\rfloor
=0.
\]

The local factorial residual formula gives

\[
R_d(\zeta)=\frac12.
\]

A direct logarithmic derivative calculation gives

\[
D\log R_d(\zeta)=-\frac{d^2}{2},
\]

and

\[
D^2\log R_d(\zeta)
=-\frac{d^2(2d^2+1)}{12}.
\]

Therefore

\[
D\log Y_d
=d^2+2D\log R_d=0,
\]

while

\[
D^2\log Y_d
=2D^2\log R_d
=-\frac{d^2(2d^2+1)}6\ne0.
\]

Since \(\zeta^{d^2}=1\),

\[
Y_d(\zeta)=\frac14.
\]

Thus \(Y_d-1/4\) has exact order two, and its square has exact order four. Expanding the square gives exactly three terms, all using only endpoints \(d\) and \(2d\), and all of depth zero. ∎

## Sharpness Theorem 10.3 — Exact ternary capacity

\[
\boxed{
C^{\mathrm{cd}}_3(3,2)=4.
}
\]

### Proof

Theorem 10.1 gives the upper bound

\[
C^{\mathrm{cd}}_3(3,2)\le4.
\]

Theorem 10.2 with \(d=3\) gives the explicit witness

\[
\boxed{
\left(
q^9\frac{(q;q)_3^4}{(q;q)_6^2}
-
\frac14
\right)^2,
}
\]

which has exact order four and common depth zero. Hence

\[
C^{\mathrm{cd}}_3(3,2)\ge4.
\]

The two inequalities give equality. ∎

---

# 11. Consequences for the general-\(d\) problem

## Corollary 11.1 — First three contexts are chirality-independent

\[
\boxed{
C^{\mathrm{cd}}_1(3,2)
=
C^{\mathrm{cd}}_2(3,2)
=
C^{\mathrm{cd}}_3(3,2)
=4.
}
\]

Thus the first genuinely complex context does not increase the rank-three two-endpoint capacity.

## Corollary 11.2 — Uniform visible-sector reduction

For every \(d\ge3\), every visible endpoint pair with \(C,J\ne0\) is five-jet rigid unless all three endpoint tests hold:

\[
\Omega_d=0,
\qquad
\Delta_d\in\mathbb Z\setminus\{0\},
\qquad
\Sigma_d\in\mathbb Z_{>0}^{\,2}.
\]

The exponent parameters themselves need not be searched.

## Corollary 11.3 — Exact binomial identities lie on the obstruction locus

For

\[
R(q)=(1-q^k)^\varepsilon,
\qquad
\varepsilon\in\{1,-1\},
\]

the obstruction invariants satisfy

\[
\boxed{
\Omega_d=0,
\qquad
\Delta_d=\varepsilon,
\qquad
\Sigma_d=k^2.
}
\]

Thus the known exact identities saturate, rather than evade, the uniform necessary conditions.

## Conjecture 11.4 — Uniform common-depth capacity

\[
\boxed{
C^{\mathrm{cd}}_d(3,2)=4
\qquad(d\ge1).
}
\]

Theorems 6.1 and 10.3 remove two earlier reasons to expect growth with \(d\): neither the formal conic dimension nor the first nonreal context produces additional capacity.

---

# 12. Remaining boundaries

The uniform conjecture now has three sharply separated components.

## 12.1 Endpoint obstruction theorem

Prove that, for every \(d\ge4\), the simultaneous conditions

\[
\Omega_d=0,
\qquad
\Delta_d\in\mathbb Z\setminus\{0\},
\qquad
\Sigma_d\in\mathbb Z_{>0}^{\,2}
\]

occur only for exact binomial identities.

## 12.2 Vanishing low cumulants

The axis theorem assumes

\[
C\ne0,
\qquad
J\ne0.
\]

At \(d=3\), Theorems 4.1 and 4.2 prove this uniformly. At larger contexts, residue-channel cancellation may make one of these invariants vanish. Such directions require passage to the first nonzero even and odd cumulants.

## 12.3 Subcritical pairs

For \(d\ge4\), there are several pairs

\[
0<A<B<d.
\]

Common depth gives no exponent relation. The ternary pair was closed by a degree-six Wronskian. A uniform subcritical theorem should replace the finite pair-by-pair analysis by a rank-three logarithmic-derivative argument whose complexity depends only on two endpoints, not on \(d\).

---

# 13. Theorem inventory

1. **Uniform visible identity classification.**  
   Every exact three-term dependence comes from \(1-q\), an adjacent unit \((1-q^B)^{-1}\), or the positive pair \((1+q)^{-1}\).

2. **Closed ternary cumulants.**  
   Explicit formulas for \(\ell_s,C_s,j_s,D_s\).

3. **Ternary quadratic visibility.**  
   \(C\ne0\) for every visible pair.

4. **Ternary cubic visibility.**  
   \(J\ne0\) for every visible pair.

5. **Uniform axis rigidity.**  
   Every chiral five-jet failure has two opposite real points and one anti-real point.

6. **Endpoint obstruction invariants.**  
   Five-jet dependence forces \(\Omega_d=0\), integral \(\Delta_d\), square \(\Sigma_d\), and the parity equation.

7. **Complete ternary endpoint obstruction.**  
   \(\Omega_3=0\) only for exact identities.

8. **Visible ternary five-jet injectivity.**

9. **Subcritical ternary Wronskian rigidity.**

10. **Sharp ternary capacity.**  
    \[
    C^{\mathrm{cd}}_3(3,2)=4.
    \]

---

# Appendix A. Exact coefficient certificate for Theorem 7.1

The following SymPy script performs the entire endpoint audit over \(\mathbb Q\). It uses no floating-point arithmetic. Each positivity assertion checks that every coefficient after the indicated shift has the required strict sign.

```python
import sympy as sp

# Positive integer variables in the proof:
a, b, h = sp.symbols("a b h", integer=True)
X, Y = sp.symbols("X Y", nonnegative=True, integer=True)


def S2(n):
    return n * (n + 1) * (2*n + 1) / 6


def S4(n):
    return n * (n + 1) * (2*n + 1) * (3*n**2 + 3*n - 1) / 30


def progression(start, step, count, power):
    k = sp.symbols("k", integer=True)
    return sp.summation((start + step*k)**power, (k, 0, count - 1))


def one_factor(s):
    N = 3*a + s
    c1 = a + (1 if s >= 1 else 0)
    c2 = a + (1 if s >= 2 else 0)

    r1 = progression(1, 3, c1, 1)
    r2 = progression(2, 3, c2, 1)
    q1 = progression(1, 3, c1, 3)
    q2 = progression(2, 3, c2, 3)

    ell = sp.factor((r2-r1)/6)
    C = sp.factor(sp.Rational(1,3)*S2(N)-sp.Rational(9,4)*S2(a))
    j = sp.factor((q1-q2)/9)
    D = sp.factor(-sp.Rational(1,3)*S4(N)
                  +sp.Rational(1053,40)*S4(a))
    return ell, C, j, D


I = {s: one_factor(s) for s in range(3)}


def obstruction(s, t):
    ellA, CA, jA, DA = I[s]
    ellB, CB, jB, DB = [z.subs(a, b) for z in I[t]]

    ell = sp.expand(b*ellA-a*ellB)
    C = sp.expand(b*CA-a*CB)
    j = sp.expand(b*jA-a*jB)
    D = sp.expand(b*DA-a*DB)

    W = sp.factor(j*C**2-ell*(3*j**2+C*D))
    b_value = a+h if s < t else a+h+1
    numerator, denominator = sp.fraction(sp.together(W.subs(b, b_value)))
    return sp.factor(numerator), sp.factor(denominator)


# Positive factors stripped before coefficient checking.
obvious = {
    (0,0): [(a,3),(h+1,3),(a+h+1,3),(2*a+h+1,1),(12*a+6*h+7,2)],
    (0,1): [(a,3),(h,1),(a+h,1)],
    (0,2): [(a,3)],
    (1,0): [(a,1),(h+1,1),(a+h+1,3)],
    (1,1): [(a,1),(h+1,3),(a+h+1,1)],
    (1,2): [(a,1),(h,1)],
    (2,0): [(a+h+1,3)],
    (2,1): [(h+1,1),(a+h+1,1)],
    (2,2): [(h+1,3)],
}


def core(s, t):
    numerator, denominator = obstruction(s, t)
    P = numerator
    for factor, exponent in obvious[(s,t)]:
        P = sp.cancel(P/factor**exponent)
    return sp.factor(P)


def all_positive(poly, substitution):
    Q = sp.Poly(sp.expand(poly.subs(substitution)), X, Y)
    return all(c > 0 for c in Q.coeffs())


def all_negative(poly, substitution):
    Q = sp.Poly(sp.expand(poly.subs(substitution)), X, Y)
    return all(c < 0 for c in Q.coeffs())


# Uniform positive/negative coefficient certificates.
assert all_positive(core(0,0), {a:X+1, h:Y})
assert all_positive(core(0,1), {a:X+1, h:Y})
assert all_positive(core(0,2), {a:X+1, h:Y})

assert all_positive(core(1,0).subs(h,0), {a:X+1})
assert all_negative(core(1,0), {a:X+1, h:Y+1})
assert all_negative(core(1,1), {a:X+1, h:Y})
assert all_negative(core(1,2), {a:X+1, h:Y})

assert all_positive(core(2,0), {a:X+1, h:Y+1})
assert all_negative(core(2,1).subs(h,0), {a:X+1})
assert all_positive(core(2,1), {a:X+1, h:Y+1})
assert all_positive(core(2,2), {a:X+1, h:Y})

# The sole mixed boundary polynomial for (2,0), h=0.
Q = sp.factor(core(2,0).subs(h,0))
assert Q.subs(a,1) == -641725
assert all_positive(Q, {a:X+2})

# Exact zero factors and nonzero quotients.
for pair in [(0,1), (1,2)]:
    numerator, _ = obstruction(*pair)
    assert sp.expand(numerator.subs(h, 0)) == 0
    quotient = sp.cancel(numerator/h)
    assert quotient.is_polynomial(a, h)
```

The script proves exactly the sign table used in Theorem 7.1. The two factors \(h\) give the two adjacent same-block identity families.

---

# Appendix B. Exact elimination certificate for Lemma 9.3

On the nonzero-leading-coefficient locus, normalize

\[
A=\Phi+Uq+V,
\qquad
B=k\Phi+Rq+S,
\qquad
k\ne0,1,
\]

where

\[
\Phi=q^2+q+1.
\]

Set

\[
P=q(q^2-1),
\qquad
\mathcal N=AB(B-A)+P(AB'-BA').
\]

The following exact SymPy computation works over the rational function field \(\mathbb Q(k)\). It verifies that the six coefficients of

\[
\mathcal N-k(k-1)\Phi^3
\]

generate the ideal \((U,V,R,S)\).

```python
import sympy as sp

q = sp.symbols("q")
k = sp.symbols("k")
U, V, R, S = sp.symbols("U V R S")

Phi = q**2 + q + 1
P = q*(q**2 - 1)
A = Phi + U*q + V
B = k*Phi + R*q + S

N = sp.expand(
    A*B*(B-A)
    + P*(A*sp.diff(B, q)-B*sp.diff(A, q))
)

F = sp.Poly(sp.expand(N-k*(k-1)*Phi**3), q)
equations = [F.coeff_monomial(q**i) for i in range(6)]

K = sp.QQ.frac_field(k)
G = sp.groebner(
    equations,
    U, V, R, S,
    order="grevlex",
    domain=K,
)

assert [sp.factor(g.as_expr()) for g in G.polys] == [U, V, R, S]
```

Thus the only solution over \(\mathbb Q(k)\) is

\[
U=V=R=S=0.
\]

Undoing the normalization gives

\[
u=v=r=s=0.
\]

When the leading coefficient

\[
c=\alpha\beta(\beta-\alpha)
\]

vanishes, divisibility by the degree-six polynomial \(\Phi^3\) forces \(\mathcal N=0\). This is exactly the dichotomy of Lemma 9.3.

---

# Final synthesis

The first nonreal cyclotomic context is now completely solved:

\[
\boxed{C^{\mathrm{cd}}_3(3,2)=4.}
\]

The proof does more than settle one case. It identifies a uniform geometric law at every nonreal context:

\[
\boxed{
\text{five-jet failure}
\Longrightarrow
\text{two opposite half-integral real points}
+
\text{one anti-real point}.
}
\]

The apparent high-dimensional cyclotomic conic therefore collapses to three endpoint invariants:

\[
\boxed{\Omega_d,\quad\Delta_d,\quad\Sigma_d.}
\]

At \(d=3\), exact endpoint arithmetic shows that their obstruction locus contains only genuine binomial identities. The remaining uniform theorem is no longer a vague search for deeper chiral collisions. It is the explicit statement:

> For every \(d\ge4\), classify the visible endpoint pairs satisfying the three obstruction conditions, classify the directions with vanishing \(C\) or \(J\), and prove a uniform subcritical Wronskian bound.

If those three tasks close as they do at \(d=3\), then

\[
\boxed{C^{\mathrm{cd}}_d(3,2)=4\qquad(d\ge1).}
\]

## End of Part XVIII
