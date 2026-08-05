# Cyclotomic Coefficient Arithmetic

## Part XVII — Rank-Three Two-Endpoint Cyclotomic Contact: Binary Sharpness and the General-d Five-Jet Reduction

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete for the binary capacity, the universal sharp lower bound, and the general five-jet rank-loss classification; conjectural for the uniform upper bound at nonreal contexts  
**Scope:** Common-depth three-term factorial circuits with at most two positive factorial endpoints, the exact formula

\[
\boxed{C^{\mathrm{cd}}_2(3,2)=4,}
\]

a universal construction proving

\[
\boxed{C^{\mathrm{cd}}_d(3,2)\ge 4\qquad(d\ge1),}
\]

the arbitrary-context two-endpoint normal form, the chiral five-jet conic, the complete binary endpoint obstruction, the ternary quadratic-field specialization, and the uniform-capacity conjecture.

---

# 0. Purpose, corrected status, and relation to earlier parts

Part XII proved that for every fixed cyclotomic order \(d\), top fan-in \(m\), and endpoint complexity \(S\), the common-depth excess-contact constant

\[
C^{\mathrm{cd}}_d(m,S)
\]

is finite. The proof is Noetherian and does not give the exact value in the first genuinely higher-rank box

\[
(m,S)=(3,2).
\]

Part XIII solved the two-term and one-endpoint boundary regimes. Part XVI then proved the positive-context theorem

\[
\boxed{C^{\mathrm{cd}}_1(3,2)=4.}
\]

Part IV identified the structural distinction between self-conjugate and nonreal cyclotomic contexts:

- at \(d=1\) and \(d=2\), normalized reciprocal germs are genuinely even;
- at every \(d\ge3\), normalized reciprocal germs have real even cumulants and generally nonzero purely anti-real odd cumulants.

The present chapter has three logically separate conclusions.

## Proved conclusion A — the binary context

The binary case is completely solved:

\[
\boxed{C^{\mathrm{cd}}_2(3,2)=4.}
\]

The proof transfers the five-jet geometry of Part XVI to \(q=-1\), but the endpoint arithmetic is different and is handled here in full.

## Proved conclusion B — every context admits excess four

For every \(d\ge1\), there is an explicit three-term, two-endpoint, common-depth circuit with exact excess contact four. Therefore

\[
\boxed{C^{\mathrm{cd}}_d(3,2)\ge4\qquad(d\ge1).}
\]

Thus neither chirality nor growth of \(\varphi(d)\) can lower the capacity below four.

## Proved conclusion C — the general five-jet obstruction

Whenever common depth reduces the endpoint exponents to one lattice direction and the quadratic logarithmic cumulant is nonzero, five-jet dependence is governed by one explicit chiral conic. The formula is independent of \(\varphi(d)\); dependence on \(d\) enters only through the cyclotomic cumulants and their arithmetic field.

## Open conclusion — the uniform upper bound

This chapter does **not** prove

\[
C^{\mathrm{cd}}_d(3,2)\le4
\qquad(d\ge3).
\]

The natural conjecture is

\[
\boxed{C^{\mathrm{cd}}_d(3,2)=4\qquad(d\ge1),}
\]

but three obstructions remain at nonreal contexts:

1. endpoint pairs \(0<A<B<d\), for which common depth imposes no linear relation on the endpoint exponents;
2. visible endpoint directions whose quadratic cumulant vanishes;
3. arithmetic solutions of the chiral five-jet conic that are not exact functional identities.

Earlier drafts blurred proved binary statements, experimental ternary calculations, and the general conjecture. This rebuild separates them completely.

Throughout,

\[
D=q\frac d{dq},
\qquad
q=\zeta e^x,
\]

so that \(D=d/dx\). All local calculations are exact.

---

# 1. Common-depth factorial circuits and capacity

For \(N\ge0\), write

\[
(q;q)_N=\prod_{j=1}^{N}(1-q^j),
\qquad
(q;q)_0=1.
\]

Fix a primitive \(d\)-th root of unity \(\zeta\).

A two-endpoint factorial term is

\[
T(q)=q^\alpha(q;q)_A^u(q;q)_B^v,
\qquad
0<A<B,
\qquad
\alpha,u,v\in\mathbb Z.
\]

Negative factorial exponents are allowed, so the term may be rational. Its cyclotomic depth is

\[
\boxed{
 h_d(T)
 =v_{\Phi_d}(T)
 =u\left\lfloor\frac Ad\right\rfloor
 +v\left\lfloor\frac Bd\right\rfloor.
}
\]

A factorial circuit of top fan-in at most three is

\[
F(q)=\sum_{i=1}^{s}c_iT_i(q),
\qquad
1\le s\le3,
\qquad
c_i\in\mathbb Q^\times.
\]

## Definition 1.1 — Common depth

The circuit has **common depth** \(h\) at context \(d\) if

\[
h_d(T_i)=h
\qquad(1\le i\le s).
\]

## Definition 1.2 — Common-depth excess capacity

Let \(C^{\mathrm{cd}}_d(3,2)\) be the least integer \(C\) such that every nonzero common-depth circuit with at most three terms and at most two positive factorial endpoints satisfies

\[
\boxed{
\operatorname{ord}_{q=\zeta}F\le h+C.
}
\]

The order is independent of the chosen primitive \(d\)-th root because the circuit has rational coefficients.

Part XII proves finiteness for every fixed \(d\).

## Definition 1.3 — Visible and subcritical endpoint pairs

Put

\[
r_A=\left\lfloor\frac Ad\right\rfloor,
\qquad
r_B=\left\lfloor\frac Bd\right\rfloor.
\]

The pair \((A,B)\) is **visible at context \(d\)** if

\[
r_A+r_B>0.
\]

It is **subcritical** if

\[
0<A<B<d,
\]

so \(r_A=r_B=0\).

For a visible pair, common depth constrains the endpoint exponents to one affine lattice line. For a subcritical pair, common depth is identically zero and gives no such reduction. This distinction is absent at \(d=1,2\), but becomes essential for \(d\ge3\).

---

# 2. The arbitrary-context two-endpoint normal form

This section isolates the part of the argument valid for every \(d\).

Fix a visible endpoint pair \((A,B)\). Put

\[
g=\gcd(r_A,r_B),
\]

with the convention that when \(r_A=0<r_B\), the primitive direction below is \((1,0)\).

## Lemma 2.1 — Primitive common-depth direction

If \(r_A,r_B>0\), every difference of two exponent vectors \((u,v)\) of the same depth is an integer multiple of

\[
\boxed{
(e_A,e_B)=\left(\frac{r_B}{g},-\frac{r_A}{g}\right).
}
\]

If \(r_A=0<r_B\), common depth fixes \(v\), and the primitive variable direction is

\[
\boxed{(e_A,e_B)=(1,0).}
\]

### Proof

A difference \((\Delta u,\Delta v)\) of equal-depth exponent vectors satisfies

\[
r_A\Delta u+r_B\Delta v=0.
\]

When both depths are positive, the primitive integer kernel of \((r_A,r_B)\) is generated by

\[
(r_B/g,-r_A/g).
\]

When \(r_A=0<r_B\), the equation is \(r_B\Delta v=0\), so \(\Delta v=0\) and \(\Delta u\) is arbitrary. ∎

Define the zero-depth endpoint ratio

\[
R_{A,B}(q)=(q;q)_A^{e_A}(q;q)_B^{e_B}.
\]

Because

\[
e_Ar_A+e_Br_B=0,
\]

this ratio is a local unit at \(q=\zeta\). Let

\[
R_0=R_{A,B}(\zeta)\ne0
\]

be its locally regularized value and define

\[
\lambda
=
\left.D\log R_{A,B}(q)\right|_{q=\zeta}.
\]

The normalized nonlinear logarithm is

\[
\boxed{
H(x)
=
\log\frac{R_{A,B}(\zeta e^x)}{R_0}
-\lambda x.
}
\]

Then

\[
H(0)=H'(0)=0.
\]

## Proposition 2.2 — Universal two-parameter germ

After factoring one common-depth base term and absorbing nonzero local residuals into the outer coefficients, every term of a visible two-endpoint common-depth circuit has the form

\[
\boxed{
f_{p,n}(x)=\exp\bigl(px+nH(x)\bigr),
}
\]

where

\[
n\in\mathbb Z,
\qquad
p=\beta+n\lambda,
\qquad
\beta\in\mathbb Z.
\]

### Proof

By Lemma 2.1, every endpoint-exponent vector differs from a fixed base vector by \(n(e_A,e_B)\). The corresponding ratio of factorial parts is \(R_{A,B}^n\). The remaining independent monomial shift is \(q^\beta\). In the coordinate \(q=\zeta e^x\), its nonzero factor \(\zeta^\beta\) is absorbed into the coefficient and its unit germ is \(e^{\beta x}\). Substitution of the normalized logarithm of \(R_{A,B}\) gives the result. ∎

## Corollary 2.3 — Where the cyclotomic order enters

For visible endpoint pairs, the local analytic family is always two-parameter:

\[
(p,n)\longmapsto e^{px+nH(x)}.
\]

The order \(d\) enters through:

1. the lattice containing \(p=\beta+n\lambda\);
2. the cumulants of \(H\);
3. arithmetic in \(\mathbb Q(\zeta_d)\).

It does not increase the number of local parameters.

---

# 3. Reciprocity, evenness, and chirality

The ratio \(R_{A,B}\) is reciprocal as a rational function. If its reciprocal degree is \(E\), then

\[
R_{A,B}(q^{-1})=q^{-E}R_{A,B}(q).
\]

Part IV gives the normalized reciprocity law.

## Theorem 3.1 — Parity-reality of the nonlinear cumulants

Write

\[
H(x)=\sum_{j\ge2}\kappa_j\frac{x^j}{j!}.
\]

After the linear drift is removed,

\[
\boxed{
\kappa_{2j}\in K_d^+,
\qquad
\overline{\kappa_{2j+1}}=-\kappa_{2j+1},
}
\]

where

\[
K_d=\mathbb Q(\zeta_d),
\qquad
K_d^+=\{a\in K_d:\bar a=a\}.
\]

At \(d=1,2\), every odd nonlinear cumulant vanishes. At \(d\ge3\), odd anti-real cumulants may survive.

### Proof

This is the normalized reciprocal-germ symmetry of Part IV applied to the zero-depth ratio. The logarithm satisfies

\[
\overline{H(-\bar x)}=H(x).
\]

Comparison of coefficients gives

\[
\kappa_j=(-1)^j\overline{\kappa_j}.
\]

For \(d=1,2\), the context is real and every coefficient is real, so every odd coefficient equals its negative and therefore vanishes. ∎

Define the first nonlinear invariants

\[
\boxed{
C=H''(0),
\qquad
J=H^{(3)}(0),
\qquad
D_4=H^{(4)}(0).
}
\]

Then

\[
C,D_4\in K_d^+,
\qquad
\bar J=-J.
\]

At \(d=1,2\),

\[
J=0.
\]

---

# 4. Universal five-jet algebra

The next theorem is purely formal. It is valid over any characteristic-zero field equipped with the required parameters.

Let

\[
f_{p,n}(x)=e^{px+nH(x)},
\]

where

\[
H(0)=H'(0)=0,
\qquad
C=H''(0)\ne0.
\]

## Lemma 4.1 — First five derivatives in the chiral case

\[
\boxed{
\begin{aligned}
f_{p,n}(0)&=1,\\
f'_{p,n}(0)&=p,\\
f''_{p,n}(0)&=p^2+nC,\\
f^{(3)}_{p,n}(0)&=p^3+3pnC+nJ,\\
f^{(4)}_{p,n}(0)
&=p^4+6p^2nC+4pnJ+3n^2C^2+nD_4.
\end{aligned}
}
\]

### Proof

Apply the complete exponential Bell polynomials to the exponent

\[
px+nH(x),
\]

whose first four derivatives at zero are

\[
p,
\qquad
nC,
\qquad
nJ,
\qquad
nD_4.
\]

Substitution gives the formulas. ∎

Define the five-jet column

\[
\mathcal J(p,n)
=
\begin{pmatrix}
1\\
p\\
p^2+nC\\
p^3+3pnC+nJ\\
p^4+6p^2nC+4pnJ+3n^2C^2+nD_4
\end{pmatrix}.
\]

## Lemma 4.2 — Repeated drift values are separated

Let \((p_i,n_i)\), \(1\le i\le3\), be distinct.

1. If all \(p_i\) are equal, the columns \(\mathcal J(p_i,n_i)\) are independent.
2. If exactly two \(p_i\) are equal, the three columns are independent.

### Proof

If all \(p_i=p\), use rows \(0,2,4\). After elementary row operations, the determinant is a nonzero multiple of

\[
C^3
\det
\begin{pmatrix}
1&1&1\\
n_1&n_2&n_3\\
n_1^2&n_2^2&n_3^2
\end{pmatrix},
\]

which is nonzero because the \(n_i\) are distinct.

If \(p_1=p_2\ne p_3\), then \(n_1\ne n_2\), and the determinant of rows \(0,1,2\) is, up to sign,

\[
C(n_2-n_1)(p_3-p_1)\ne0.
\]

∎

## Project Theorem 4.3 — Chiral five-jet conic

Assume \(p_1,p_2,p_3\) are pairwise distinct. Their five-jet columns are dependent if and only if there exist \(t,N\) and centered coordinates

\[
x_i=p_i-t
\]

such that

\[
\boxed{
\sum_{i=1}^{3}x_i=-\frac{J}{2C},
}
\tag{4.1}
\]

\[
\boxed{
n_i=N-\frac{x_i^2}{C},
}
\tag{4.2}
\]

and

\[
\boxed{
\sum_{i=1}^{3}x_i^2
=
\frac{7J^2-4CD_4}{4C^2}.
}
\tag{4.3}
\]

The center is

\[
\boxed{
3t=p_1+p_2+p_3+\frac{J}{2C}.
}
\]

### Proof

Because rows zero and one are independent, rank at most two means every remaining row is affine in \(p_i\).

Dependence of rows \(0,1,2\) gives constants \(a,b\) such that

\[
p_i^2+Cn_i=ap_i+b.
\]

Hence

\[
n_i=N_0+Lp_i-\frac{p_i^2}{C}
\]

for suitable \(N_0,L\). Completing the square gives

\[
n_i=N-\frac{(p_i-t)^2}{C},
\qquad
t=\frac{CL}{2}.
\]

Now substitute this quadratic expression into the third-derivative row. Reducing the resulting cubic modulo

\[
\prod_{i=1}^{3}(p-p_i)
=p^3-s_1p^2+s_2p-s_3,
\qquad
s_1=p_1+p_2+p_3,
\]

and requiring the quadratic remainder coefficient to vanish gives

\[
3CL=2s_1+\frac JC.
\]

Since \(t=CL/2\),

\[
3t=s_1+\frac{J}{2C}.
\]

Therefore

\[
\sum_i x_i=s_1-3t=-\frac{J}{2C},
\]

which is (4.1).

Substitute the same quadratic expression for \(n\) into the fourth-derivative row. The quadratic coefficient of its remainder modulo the cubic vanishes exactly when

\[
2C^2s_1^2-6C^2s_2+3CD_4-5J^2=0.
\]

Using

\[
\sum_i p_i^2=s_1^2-2s_2
\]

and the formula for \(t\), this becomes

\[
\sum_i(p_i-t)^2
=
\frac{7J^2-4CD_4}{4C^2}.
\]

This is (4.3).

Conversely, equations (4.1)–(4.3) imply that rows two, three, and four are affine functions of the three values \(p_i\). Hence all five row vectors lie in the span of rows zero and one, and the three columns are dependent. ∎

## Corollary 4.4 — Achiral specialization

At \(d=1,2\), one has \(J=0\). The chiral conic becomes

\[
\boxed{
\sum_i x_i=0,
\qquad
n_i=N-\frac{x_i^2}{C},
\qquad
\sum_i x_i^2=-\frac{D_4}{C}.
}
\]

This is the centered-parabola geometry used in Parts XVI and XVII.

## Corollary 4.5 — No formal \(\varphi(d)\)-growth in the five-jet equations

The rank-loss equations (4.1)–(4.3) involve only

\[
C,
\quad
J,
\quad
D_4,
\quad
p_i,
\quad
n_i.
\]

There is no multiplicative factor \(\varphi(d)\) and no increase in jet order as \(d\) grows.

Thus any dependence of the exact capacity on \(d\) must arise from endpoint arithmetic, vanishing of low cumulants, or the subcritical endpoint sector—not from a larger formal local parameter count.

---

# 5. A universal sharp lower bound

The following construction works at every cyclotomic context and is the central correction to earlier speculation that chiral contexts might have capacity two.

For \(d\ge1\), define

\[
\boxed{
R_d(q)=\frac{(q;q)_d^2}{(q;q)_{2d}}
=\frac1{{2d\brack d}_q}
}
\]

and

\[
\boxed{
Y_d(q)=q^{d^2}R_d(q)^2.
}
\]

The two factorial endpoints are \(d\) and \(2d\).

## Lemma 5.1 — Depth and root value of the universal ratio

At a primitive \(d\)-th root \(\zeta\),

\[
\boxed{v_{\Phi_d}(R_d)=0,}
\]

and

\[
\boxed{R_d(\zeta)=\frac12.}
\]

### Proof

The valuation is

\[
2\left\lfloor\frac dd\right\rfloor
-
\left\lfloor\frac{2d}{d}\right\rfloor
=2-2=0.
\]

The local factorial residual formula gives

\[
(q;q)_d
\sim
-d^2x,
\]

and

\[
(q;q)_{2d}
\sim
2d^4x^2.
\]

Therefore

\[
R_d(\zeta)
=
\frac{d^4}{2d^4}
=\frac12.
\]

Equivalently, the \(q\)-Lucas theorem gives

\[
{2d\brack d}_{\zeta}=2.
\]

∎

## Lemma 5.2 — First two logarithmic derivatives

At \(q=\zeta\),

\[
\boxed{
D\log R_d=-\frac{d^2}{2},
}
\]

and

\[
\boxed{
D^2\log R_d
=-\frac{d^2(2d^2+1)}{12}.
}
\]

### Proof

Write

\[
R_d(q)
=
\prod_{m=1}^{d}
\frac{1-q^m}{1-q^{d+m}}.
\]

Use \(q=\zeta e^x\).

For \(1\le m<d\), the first logarithmic derivative of the \(m\)-th ratio at \(x=0\) is

\[
d\frac{\zeta^m}{1-\zeta^m}.
\]

The singular ratio \(m=d\) contributes \(-d/2\). Since

\[
\sum_{m=1}^{d-1}
\frac{\zeta^m}{1-\zeta^m}
=-\frac{d-1}{2},
\]

we obtain

\[
D\log R_d
=-\frac{d(d-1)}2-\frac d2
=-\frac{d^2}{2}.
\]

For the second derivative, put

\[
a_m=\frac{\zeta^m}{(1-\zeta^m)^2}.
\]

The nonsingular channels contribute

\[
\sum_{m=1}^{d-1}d(d+2m)a_m,
\]

and the singular ratio contributes \(-d^2/4\).

The classical root-of-unity identities are

\[
\sum_{m=1}^{d-1}a_m
=-\frac{d^2-1}{12},
\]

and, because \(a_{d-m}=a_m\),

\[
\sum_{m=1}^{d-1}ma_m
=
\frac d2\sum_{m=1}^{d-1}a_m
=-\frac{d(d^2-1)}{24}.
\]

Therefore

\[
\begin{aligned}
D^2\log R_d
&=
 d^2\sum a_m
 +2d\sum ma_m
 -\frac{d^2}{4}\\
&=
-\frac{d^2(d^2-1)}{12}
-\frac{d^2(d^2-1)}{12}
-\frac{d^2}{4}\\
&=
-\frac{d^2(2d^2+1)}{12}.
\end{aligned}
\]

The formulas remain valid for \(d=1\), where the nonsingular sums are empty. ∎

## Proposition 5.3 — A universal double contact

At every primitive \(d\)-th root,

\[
\boxed{
Y_d(\zeta)=\frac14,
\qquad
DY_d(\zeta)=0,
\qquad
D^2Y_d(\zeta)\ne0.
}
\]

Hence

\[
\boxed{
\operatorname{ord}_{q=\zeta}
\left(Y_d-\frac14\right)=2.
}
\]

### Proof

Because \(\zeta^{d^2}=1\) and \(R_d(\zeta)=1/2\),

\[
Y_d(\zeta)=\frac14.
\]

Moreover,

\[
D\log Y_d
=d^2+2D\log R_d
=d^2-d^2=0.
\]

Finally,

\[
D^2\log Y_d
=2D^2\log R_d
=-\frac{d^2(2d^2+1)}6\ne0.
\]

Since \(DY_d(\zeta)=0\),

\[
\frac{D^2Y_d(\zeta)}{Y_d(\zeta)}
=D^2\log Y_d(\zeta)\ne0.
\]

Thus the contact is exactly two. ∎

## Project Theorem 5.4 — Universal excess-four construction

For every \(d\ge1\),

\[
\boxed{
\left(Y_d(q)-\frac14\right)^2
=Y_d(q)^2-\frac12Y_d(q)+\frac1{16}
}
\]

is a three-term, two-endpoint, common-depth circuit of exact order four at every primitive \(d\)-th root.

Consequently,

\[
\boxed{
C^{\mathrm{cd}}_d(3,2)\ge4
\qquad(d\ge1).
}
\]

### Proof

The three terms use only the endpoints \(d\) and \(2d\). Their endpoint exponent vectors are

\[
(8,-4),
\qquad
(4,-2),
\qquad
(0,0).
\]

Because the endpoint depths are \(1\) and \(2\), all three term depths are zero:

\[
8-8=0,
\qquad
4-4=0,
\qquad
0=0.
\]

Proposition 5.3 gives

\[
\operatorname{ord}_{q=\zeta}
\left(Y_d-\frac14\right)=2.
\]

Squaring gives exact order four. ∎

## Corollary 5.5 — The ternary conjecture cannot be two

In particular,

\[
\boxed{C^{\mathrm{cd}}_3(3,2)\ge4.}
\]

Any claim that the chiral ternary capacity equals two is false.

---

# 6. The binary context: exact endpoint germ

From this point through Section 13, set

\[
d=2,
\qquad
\zeta=-1,
\qquad
q=-e^x.
\]

Put

\[
r_N=\left\lfloor\frac N2\right\rfloor.
\]

For \(j\ge1\), define the binary visibility moment

\[
\boxed{
W_{2j}(N)
=
\sum_{\substack{1\le m\le N\\2\mid m}}m^{2j}
+
(2^{2j}-1)
\sum_{\substack{1\le m\le N\\2\nmid m}}m^{2j}.
}
\]

## Lemma 6.1 — One-factor binary logarithms

For even \(m\), after removing the simple zero,

\[
\log\frac{1-e^{mx}}{-mx}
=
\frac{mx}{2}
+
\sum_{j\ge1}
\frac{B_{2j}}{2j(2j)!}m^{2j}x^{2j}.
\]

For odd \(m\),

\[
\log\frac{1+e^{mx}}{2}
=
\frac{mx}{2}
+
\sum_{j\ge1}
\frac{B_{2j}}{2j(2j)!}
(2^{2j}-1)m^{2j}x^{2j}.
\]

### Proof

The first formula is the regularized singular expansion. For odd \(m\), use

\[
\frac{1+e^{mx}}2
=e^{mx/2}\cosh(mx/2)
\]

and the Bernoulli expansion of \(\log\cosh\). ∎

## Proposition 6.2 — Binary factorial normal form

For every \(N\ge0\), there is a nonzero constant \(b_N\) such that

\[
\boxed{
(q;q)_N\big|_{q=-e^x}
=
 b_Nx^{r_N}
\exp\left(
\lambda_Nx
+
\sum_{j\ge1}
\frac{B_{2j}}{2j(2j)!}W_{2j}(N)x^{2j}
\right),
}
\]

where

\[
\boxed{
\lambda_N=\frac{N(N+1)}4.
}
\]

### Proof

Exactly \(r_N\) factors have even exponent and vanish simply. Their leading coefficients and the nonzero odd factors form \(b_N\ne0\). Lemma 6.1 shows that the total linear term is

\[
\frac12\sum_{m=1}^{N}m
=\frac{N(N+1)}4,
\]

and the even nonlinear terms group into \(W_{2j}(N)\). ∎

## Corollary 6.3 — Binary evenness

After removing depth, residual, and linear drift, every binary factorial quotient germ is even.

Thus in the notation of Section 3,

\[
J=0.
\]

---

# 7. Binary two-endpoint reduction and curvature

Fix \(0<A<B\).

If \(A\ge2\), put

\[
g=\gcd(r_A,r_B),
\qquad
(e_A,e_B)
=
\left(\frac{r_B}{g},-\frac{r_A}{g}\right).
\]

If \(A=1\), put

\[
(e_A,e_B)=(1,0).
\]

Define

\[
M_{2j}=e_AW_{2j}(A)+e_BW_{2j}(B).
\]

The normalized zero-depth ratio has germ

\[
\boxed{
Z_{A,B}(-e^x)
=
\exp\bigl(\lambda x+H(x)\bigr),
}
\]

where

\[
\lambda=e_A\lambda_A+e_B\lambda_B
\]

and

\[
\boxed{
H(x)
=
\sum_{j\ge1}
\frac{B_{2j}}{2j(2j)!}M_{2j}x^{2j}.
}
\]

Define

\[
\boxed{
C=H''(0)=\frac{M_2}{12},
\qquad
D_4=H^{(4)}(0)=-\frac{M_4}{120},
\qquad
T=-\frac{D_4}{C}.
}
\]

## Proposition 7.1 — Closed binary visibility moments

For \(R\ge0\),

\[
\boxed{
W_2(2R)=\frac{R(2R+1)(8R-1)}3,
}
\]

\[
\boxed{
W_2(2R+1)
=
\frac{(R+1)(2R+1)(8R+9)}3,
}
\]

\[
\boxed{
W_4(2R)
=
\frac{R(2R+1)
(384R^3-132R^2-194R+97)}{15},
}
\]

and

\[
\boxed{
W_4(2R+1)
=
\frac{(R+1)(2R+1)
(384R^3+1284R^2+1222R+225)}{15}.
}
\]

### Proof

Split each weighted moment into even and odd power sums and insert the classical formulas for

\[
\sum m^2
\qquad\text{and}\qquad
\sum m^4.
\]

Expansion gives the stated expressions. ∎

## Lemma 7.2 — Binary quadratic visibility never vanishes

For every \(0<A<B\),

\[
\boxed{C\ne0.}
\]

### Proof

For \(A=1\),

\[
C=\frac{W_2(1)}{12}=\frac14.
\]

Assume \(A\ge2\). Define

\[
\mathcal F(N)=\frac{W_2(N)}{\lfloor N/2\rfloor}.
\]

Then

\[
M_2
=
\frac{r_Ar_B}{g}
\bigl(\mathcal F(A)-\mathcal F(B)\bigr).
\]

On each parity class, Proposition 7.1 shows that \(\mathcal F\) is strictly increasing.

For a cross-parity equality, write the odd argument as \(2s+1\). The formula

\[
\mathcal F(2s+1)
=
\frac{16s^3+42s^2+35s+9}{3s}
\]

shows that equality with an even value forces \(s\mid9\). Thus

\[
s\in\{1,3,9\}.
\]

Direct substitution gives no even index with the same value. Therefore \(\mathcal F\) is injective and \(M_2\ne0\). ∎

---

# 8. The binary centered lattice

By Corollary 4.4, five-jet dependence for three pairwise distinct drift values gives

\[
x_1+x_2+x_3=0,
\]

\[
n_i=N-\frac{x_i^2}{C},
\]

and

\[
x_1^2+x_2^2+x_3^2=T.
\]

The drift \(\lambda\) has denominator at most two. Let

\[
L=\operatorname{den}(\lambda)\in\{1,2\}.
\]

Since

\[
p_i=\beta_i+n_i\lambda,
\qquad
\beta_i,n_i\in\mathbb Z,
\]

we have

\[
p_i\in\frac1L\mathbb Z.
\]

Define

\[
\boxed{z_i=3Lx_i\in\mathbb Z.}
\]

Then

\[
\boxed{z_1+z_2+z_3=0}
\]

and

\[
\boxed{
M:=9L^2T=z_1^2+z_2^2+z_3^2.
}
\tag{8.1}
\]

Thus five-jet dependence requires

\[
M\in\mathbb Z_{\ge0}.
\]

Write

\[
\boxed{
9L^2C=\frac PQ
}
\]

in lowest terms with \(P>0\).

## Lemma 8.1 — Square-difference divisibility

Under five-jet dependence,

\[
\boxed{
P\mid z_i^2-z_j^2
\qquad(1\le i,j\le3).
}
\]

### Proof

From the parabola equation,

\[
\begin{aligned}
n_i-n_j
&=-\frac{x_i^2-x_j^2}{C}\\
&=-\frac{z_i^2-z_j^2}{9L^2C}\\
&=-\frac{Q(z_i^2-z_j^2)}P.
\end{aligned}
\]

The left side is integral and \(\gcd(P,Q)=1\). ∎

## Corollary 8.2 — Radius domination

If

\[
\boxed{P>M,}
\]

then the five-jet columns are independent unless the functions are already exactly dependent.

### Proof

Equation (8.1) gives

\[
|z_i^2-z_j^2|\le M<P.
\]

Lemma 8.1 forces all square differences to vanish. Three distinct integers of zero sum cannot all have the same square. ∎

---

# 9. Exact binary endpoint classification

Assume \(A\ge2\). Write

\[
A=2a+\varepsilon,
\qquad
B=2b+\eta,
\qquad
\varepsilon,\eta\in\{0,1\},
\]

where

\[
a=r_A,
\qquad
b=r_B,
\qquad
g=\gcd(a,b).
\]

Before division by \(g\), put

\[
\boxed{
\begin{aligned}
m_2&=bW_2(A)-aW_2(B),\\
m_4&=bW_4(A)-aW_4(B).
\end{aligned}
}
\]

Then

\[
\boxed{
C=\frac{m_2}{12g},
\qquad
D_4=-\frac{m_4}{120g},
\qquad
T=\frac{m_4}{10m_2}.
}
\]

Whenever \(T\ge0\), the sufficient inequality

\[
\boxed{
5m_2^2>6g|m_4|
}
\tag{9.1}
\]

implies \(P>M\).

## Project Lemma 9.1 — Complete binary endpoint alternative

For every pair \(0<A<B\), at least one of the following applies:

1. \(A=1\);
2. \(A\) is even and \(B=A+1\);
3. \(M\notin\mathbb Z\);
4. \((A,B)=(2,4)\);
5. \(P>M\).

### Proof

This is an exact finite polynomial certificate.

Put

\[
b=a+r.
\]

The four parity patterns are \(EE,EO,OE,OO\). The case \(EO\) with \(r=0\) is exactly the adjacent even–odd family

\[
(A,B)=(2a,2a+1).
\]

For all remaining infinite cones, use

\[
g=\gcd(a,b)=\gcd(a,r)\le\min(a,r)
\]

and square (9.1). The resulting sufficient polynomial is

\[
\boxed{
\mathscr S=25m_2^4-36G^2m_4^2,
}
\]

where \(G\) is the corresponding upper bound for \(g\).

After the substitutions below, every coefficient of \(\mathscr S\) is nonnegative and the constant coefficient is positive.

| Parity | Infinite region | Substitution |
|---|---:|---:|
| \(EE\) | \(r\ge a+1\) | \(r=a+u+1\) |
| \(EE\) | \(a\ge r+1\) | \(a=r+u+1\) |
| \(EO\) | \(r\ge a+1\) | \(r=a+u+1\) |
| \(EO\) | \(a\ge r+1\) | \(a=r+u+1\) |
| \(OE\) | \(r\ge a+3\) | \(r=a+u+3\) |
| \(OE\) | \(a\ge r+3,\ r\ge2\) | \(r=X+2,\ a=X+Y+5\) |
| \(OO\) | \(r\ge a+2\) | \(r=a+u+2\) |
| \(OO\) | \(a\ge r+2\) | \(a=r+u+2\) |

Each expanded certificate has 143 monomials; the least coefficient over the eight certificates is \(20227\).

The remaining boundary lines are one-variable polynomial certificates. Coefficient positivity begins at:

| Boundary | Starting value |
|---|---:|
| \(EE:r=a\) | \(a\ge2\) |
| \(EO:r=a\) | \(a\ge2\) |
| \(OE:r=a-2\) | \(a\ge5\) |
| \(OE:r=a-1\) | \(a\ge3\) |
| \(OE:r=a\) | \(a\ge3\) |
| \(OE:r=a+1\) | \(a\ge2\) |
| \(OE:r=a+2\) | \(a\ge2\) |
| \(OE:r=1\) | \(a\ge20\) |
| \(OO:r=a-1\) | \(a\ge3\) |
| \(OO:r=a\) | \(a\ge3\) |
| \(OO:r=a+1\) | \(a\ge2\) |

Thus every uncovered pair lies in

\[
2\le A<B\le40.
\]

Exact rational enumeration leaves, after removing adjacent even–odd pairs,

\[
\begin{aligned}
\mathcal E=\{&
(2,4),(2,5),
(3,4),(3,5),(3,6),(3,7),(3,8),\\
&(5,6),(5,7),(5,8),(5,9),(7,8),(9,10),(9,12),\\
&(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),\\
&(23,24),(25,26),(27,28),(29,30),(31,32),(33,34),\\
&(35,36),(37,38),(39,40)\}.
\end{aligned}
\]

For every pair in \(\mathcal E\) except \((2,4)\), exact reduction gives

\[
M\notin\mathbb Z.
\]

For \((2,4)\), one has \(M=36\). ∎

### Caution 9.2 — Nature of the proof

Lemma 9.1 is machine-assisted but exact. It consists only of integer-polynomial expansion, coefficient-sign checking, and finite rational enumeration. No floating-point sampling is used.

---

# 10. The isolated binary pair \((2,4)\)

For \((A,B)=(2,4)\),

\[
\boxed{
\lambda=-2,
\qquad
C=-3,
\qquad
D_4=12,
\qquad
T=4,
\qquad
L=1,
\qquad
M=36.
}
\]

Five-jet dependence would give

\[
z_1+z_2+z_3=0,
\qquad
z_1^2+z_2^2+z_3^2=36.
\]

Putting \(z_3=-z_1-z_2\) yields

\[
\boxed{
z_1^2+z_1z_2+z_2^2=18.
}
\]

## Lemma 10.1 — Parity obstruction

The equation

\[
x^2+xy+y^2=18
\]

has no integer solution.

### Proof

Modulo two, the quadratic form \(x^2+xy+y^2\) vanishes only when \(x\) and \(y\) are both even. The left side is then divisible by four, whereas \(18\) is not. ∎

Thus \((2,4)\) cannot produce five-jet rank loss.

---

# 11. The two exact binary identity families

The remaining alternatives of Lemma 9.1 do admit five-jet dependence, but only because the corresponding germs satisfy an exact identity.

## 11.1 The family \(A=1\)

The primitive normalized ratio is

\[
Z(q)=\frac{1-q}{2}.
\]

At \(q=-e^x\),

\[
\boxed{
Z(-e^x)=e^{x/2}\cosh(x/2).
}
\]

Therefore

\[
\lambda=\frac12,
\qquad
H(x)=\log\cosh(x/2),
\]

and

\[
C=\frac14,
\qquad
D_4=-\frac18,
\qquad
T=\frac12.
\]

The centered lattice equations force, after reordering,

\[
x_1=-\frac12,
\qquad
x_2=0,
\qquad
x_3=\frac12,
\]

and

\[
n_1=N-1,
\qquad
n_2=N,
\qquad
n_3=N-1.
\]

After a common factor is removed, the three germs are

\[
e^{-x/2},
\qquad
\cosh(x/2),
\qquad
 e^{x/2}.
\]

Hence

\[
\boxed{
e^{-x/2}+e^{x/2}-2\cosh(x/2)=0.
}
\]

Every five-jet rank loss in this family is an exact functional dependence.

## 11.2 Adjacent even–odd endpoints

Let

\[
A=2r,
\qquad
B=2r+1.
\]

The zero-depth ratio collapses to

\[
\frac{(q;q)_{B-1}}{(q;q)_B}
=
\frac1{1-q^B}.
\]

After normalization at \(q=-1\),

\[
\boxed{
Z(q)=\frac2{1-q^B}.
}
\]

Since \(B\) is odd,

\[
\boxed{
Z(-e^x)
=
\frac{e^{-Bx/2}}{\cosh(Bx/2)}.
}
\]

Thus

\[
\lambda=-\frac B2,
\qquad
H(x)=-\log\cosh(Bx/2),
\]

and

\[
C=-\frac{B^2}{4},
\qquad
D_4=\frac{B^4}{8},
\qquad
T=\frac{B^2}{2}.
\]

Set

\[
u_i=\frac{2x_i}{B}.
\]

Five-jet dependence gives

\[
\sum_i u_i=0,
\qquad
\sum_i u_i^2=2,
\]

and all square differences \(u_i^2-u_j^2\) are integers.

## Lemma 11.1 — Rational square classification

If \(u_1,u_2,u_3\in\mathbb Q\) satisfy

\[
\sum_i u_i=0,
\qquad
\sum_i u_i^2=2,
\]

and every difference \(u_i^2-u_j^2\) is integral, then after reordering

\[
\boxed{(u_1,u_2,u_3)=(-1,0,1).}
\]

### Proof

The three squares have one common fractional part. Their sum is two. The only possible fractional patterns are

\[
\left\{\frac23,\frac23,\frac23\right\},
\qquad
\left\{\frac43,\frac13,\frac13\right\},
\qquad
\{1,1,0\}.
\]

The first two require irrational square roots. The last gives \(-1,0,1\) from the zero-sum condition. ∎

Therefore, after a common factor is removed, the germs are

\[
e^{-Bx/2+H(x)},
\qquad
1,
\qquad
 e^{Bx/2+H(x)}.
\]

Since

\[
e^{H(x)}=\frac1{\cosh(Bx/2)},
\]

one has

\[
\boxed{
e^{-Bx/2+H(x)}+e^{Bx/2+H(x)}-2=0.
}
\]

Again, every rank loss is an exact identity.

---

# 12. Binary five-jet injectivity

## Project Theorem 12.1 — Five jets determine the binary three-term span

Fix \(0<A<B\). Let

\[
\mathcal V
=
\operatorname{span}
\{e^{p_ix+n_iH(x)}:1\le i\le3\}.
\]

After quotienting exact functional identities, the truncation map

\[
\boxed{
\mathcal V\longrightarrow K[[x]]/(x^5)
}
\]

is injective.

Equivalently, every nonzero element of \(\mathcal V\) has order at most four.

### Proof

If \(\dim\mathcal V=1\), the claim is immediate.

If \(\dim\mathcal V=2\), two distinct parameter pairs are separated by rows zero and one when their \(p\)-values differ, and by row two when their \(p\)-values agree, because \(C\ne0\).

Assume \(\dim\mathcal V=3\). If the five-jet columns were dependent, Lemma 4.2 and Corollary 4.4 would yield the centered lattice equations.

- If \(A=1\), Section 11.1 shows that the rank loss is an exact identity.
- If \(A\) is even and \(B=A+1\), Section 11.2 gives an exact identity.
- If \(M\notin\mathbb Z\), the lattice radius equation is impossible.
- If \((A,B)=(2,4)\), Lemma 10.1 gives a contradiction.
- In every remaining case, Lemma 9.1 gives \(P>M\), and Corollary 8.2 gives a contradiction.

Thus no nontrivial three-dimensional span loses rank in its first five jets. ∎

---

# 13. The sharp binary theorem

## Project Theorem 13.1 — Binary upper bound

Let

\[
F(q)=\sum_{i=1}^{s}c_iT_i(q),
\qquad
1\le s\le3,
\]

be a nonzero factorial circuit whose terms have common binary depth \(h\) and use at most two positive factorial endpoints. Then

\[
\boxed{
\operatorname{ord}_{q=-1}F\le h+4.
}
\]

### Proof

In the coordinate \(q=-e^x\), factor \(x^h\) from every term, absorb the nonzero leading residuals into the coefficients, and remove one common unit. Proposition 2.2 reduces the remaining span to at most three germs

\[
e^{p_ix+n_iH(x)}.
\]

Theorem 12.1 bounds the order of every nonzero combination of these unit germs by four. Restoring \(x^h\) gives the result. ∎

## Sharpness Theorem 13.2 — Exact binary capacity

\[
\boxed{C^{\mathrm{cd}}_2(3,2)=4.}
\]

### Proof

Theorem 13.1 gives the upper bound.

For sharpness, use

\[
1+
\frac{(1-q)^2}{2q}
+
\frac{(1-q)^4}{16q^2}
=
\frac{(q+1)^4}{16q^2}.
\]

Multiplying by \((q;q)_2\) gives

\[
\boxed{
(q;q)_2
+
\frac{q^{-1}}2(q;q)_1^2(q;q)_2
+
\frac{q^{-2}}{16}(q;q)_1^4(q;q)_2
=
\frac{(q-1)^2(q+1)^5}{16q^2}.
}
\]

All three terms use only endpoints \(1,2\). Since

\[
v_{q+1}((q;q)_1)=0,
\qquad
v_{q+1}((q;q)_2)=1,
\]

all terms have common depth \(h=1\). The right side has order five at \(q=-1\), so the excess is four. ∎

---

# 14. The ternary context

Set

\[
d=3,
\qquad
K_3=\mathbb Q(\zeta_3)=\mathbb Q(\sqrt{-3}).
\]

The real subfield of \(K_3\) is \(\mathbb Q\), and the anti-real subspace is \(\sqrt{-3}\,\mathbb Q\).

## Proposition 14.1 — Ternary cumulant fields

For every visible two-endpoint direction, after residual and linear drift are removed,

\[
\boxed{
C,D_4\in\mathbb Q,
\qquad
J\in\sqrt{-3}\,\mathbb Q.
}
\]

### Proof

Theorem 3.1 gives

\[
C,D_4\in K_3^+,
\qquad
\bar J=-J.
\]

Since \(K_3^+=\mathbb Q\), the even cumulants are rational. The anti-real elements of \(K_3\) are precisely \(\sqrt{-3}\,\mathbb Q\). ∎

## Corollary 14.2 — Ternary chiral conic

If \(C\ne0\) and three pairwise distinct ternary drift values lose rank in their first five jets, then

\[
\sum_i x_i=-\frac{J}{2C}
\in\sqrt{-3}\,\mathbb Q,
\]

\[
n_i=N-\frac{x_i^2}{C},
\]

and

\[
\sum_i x_i^2
=
\frac{7J^2-4CD_4}{4C^2}
\in\mathbb Q.
\]

Thus the ternary problem reduces to exact arithmetic on a quadratic-field conic.

## Caution 14.3 — What is not proved for \(d=3\)

The universal construction gives

\[
C^{\mathrm{cd}}_3(3,2)\ge4.
\]

This chapter does not prove the matching upper bound. Two ternary issues remain:

1. the subcritical endpoint pair \((A,B)=(1,2)\), for which common depth gives a two-dimensional exponent lattice;
2. the complete classification of integral parameter points on the chiral conic for all visible endpoint pairs.

Therefore the exact statement

\[
C^{\mathrm{cd}}_3(3,2)=4
\]

remains a conjecture here.

---

# 15. Does the capacity depend on \(d\)?

The results now support a precise answer.

## Theorem 15.1 — What is already independent of \(d\)

For every \(d\ge1\):

1. the capacity is finite;
2. the capacity is at least four;
3. every visible endpoint pair reduces to a two-parameter germ \(e^{px+nH(x)}\);
4. when \(C\ne0\), five-jet rank loss is governed by the same conic equations (4.1)–(4.3).

### Proof

Finiteness is Part XII. The lower bound is Theorem 5.4. The visible-pair reduction is Proposition 2.2. The universal rank-loss classification is Theorem 4.3. ∎

## Corollary 15.2 — Growth with \(\varphi(d)\) is not forced analytically

There is no formal five-jet mechanism that makes the required jet depth grow with \(\varphi(d)\). If the capacity grows with \(d\), the cause must be arithmetic or combinatorial:

- additional rational or cyclotomic-field points on the chiral conic;
- vanishing of early cumulants;
- subcritical endpoint pairs.

## Project Conjecture 15.3 — Uniform common-depth capacity

For every \(d\ge1\),

\[
\boxed{
C^{\mathrm{cd}}_d(3,2)=4.
}
\]

This conjecture is proved at

\[
d=1
\qquad\text{and}\qquad
d=2,
\]

and the lower bound is proved for every \(d\).

## Three possible outcomes

The remaining general-d problem can still resolve in one of three ways.

### Outcome I — Constant capacity

\[
C^{\mathrm{cd}}_d(3,2)=4
\qquad(d\ge1).
\]

This is the conjecture favored by the universal lower bound and the order-independent five-jet algebra.

### Outcome II — Achiral/chiral split

\[
C^{\mathrm{cd}}_1(3,2)
=C^{\mathrm{cd}}_2(3,2)=4,
\]

but a different constant holds for every \(d\ge3\). This would require a uniform chiral arithmetic phenomenon not visible in the formal conic alone.

### Outcome III — Genuine growth

The capacity grows with \(d\) or \(\varphi(d)\). By Corollary 15.2, such growth would have to come from increasingly complicated arithmetic solutions or increasingly delayed spectral visibility, not from an increasing number of local parameters.

At present only Outcome I is consistent with all proved exact values, but Outcomes II and III are not excluded.

---

# 16. Consequences for compressed identity testing

Suppose the uniform conjecture is true. Then every common-depth three-term, two-endpoint circuit would be certified locally at every context by the first five regularized coefficients:

\[
0,1,2,3,4.
\]

The required local depth would be independent of \(d\). Higher contexts would cost more only because arithmetic in

\[
\mathbb Q(\zeta_d)
\]

has output size comparable to \(\varphi(d)\), not because more derivatives are required.

If the conjecture fails, Theorem 4.3 still sharply localizes the failure. A counterexample must come from at least one of:

1. a subcritical pair \(A,B<d\);
2. a visible direction with \(C=0\);
3. a nonidentity integral point on the chiral conic;
4. a higher-order rank loss after the five-jet conic is satisfied.

Thus the general problem is no longer an unstructured search over circuits. It is an endpoint-arithmetic classification problem.

---

# 17. Theorem inventory

The proved results of this chapter are:

1. **Universal visible-pair normal form**
   \[
   f_{p,n}(x)=e^{px+nH(x)}.
   \]

2. **Chiral five-jet conic**
   \[
   \sum_i x_i=-\frac{J}{2C},
   \qquad
   n_i=N-\frac{x_i^2}{C},
   \qquad
   \sum_i x_i^2=\frac{7J^2-4CD_4}{4C^2}.
   \]

3. **Universal sharp lower bound**
   \[
   C^{\mathrm{cd}}_d(3,2)\ge4
   \qquad(d\ge1).
   \]

4. **Binary quadratic visibility**
   \[
   C\ne0
   \]
   for every binary endpoint pair.

5. **Complete binary endpoint alternative**, by an exact polynomial certificate.

6. **Binary five-jet injectivity** modulo exact identities.

7. **Sharp binary capacity**
   \[
   \boxed{C^{\mathrm{cd}}_2(3,2)=4.}
   \]

8. **Ternary quadratic-field reduction**
   \[
   C,D_4\in\mathbb Q,
   \qquad
   J\in\sqrt{-3}\,\mathbb Q.
   \]

The principal open statement is

\[
\boxed{C^{\mathrm{cd}}_d(3,2)=4\quad(d\ge3).}
\]

---

# 18. Boundaries and next theorem

## 18.1 Common depth

Nothing here determines the full unequal-depth constant

\[
C_d(3,2).
\]

Different depths can cancel only after several valuation layers are combined, and the one-line endpoint reduction no longer directly controls the whole circuit.

## 18.2 Subcritical endpoint pairs

For \(d\ge3\), pairs

\[
0<A<B<d
\]

have zero endpoint depth in both directions. Common depth therefore gives no one-dimensional exponent lattice. Any uniform theorem must treat this finite but structurally different sector separately for each \(d\), or find a new reduction independent of depth.

## 18.3 Vanishing quadratic cumulant

The chiral five-jet conic assumes

\[
C\ne0.
\]

At \(d=2\), Lemma 7.2 proves this for every endpoint pair. At general \(d\), quadratic spectral cancellation may occur. A complete uniform theorem must classify such directions and pass to the first visible nonlinear cumulant.

## 18.4 Exact identities

As at \(d=1,2\), a five-jet rank loss may reflect an exact functional identity rather than a nonzero high-order collision. Every endpoint classification must quotient exact identities before interpreting a determinant zero as excess contact.

## 18.5 The next high-value theorem

The clean next target is:

> **General visible-pair five-jet rigidity.** Prove that for every \(d\ge3\), every visible two-endpoint direction with \(C\ne0\), every solution of the chiral five-jet conic compatible with the exponent lattice comes from an exact functional identity.

Together with separate treatment of subcritical pairs and quadratically invisible directions, this would prove the uniform-capacity conjecture.

---

# 19. Final synthesis

The coherent conclusion of the rank-three two-endpoint investigation is now:

\[
\boxed{
C^{\mathrm{cd}}_1(3,2)=4,
\qquad
C^{\mathrm{cd}}_2(3,2)=4,
\qquad
C^{\mathrm{cd}}_d(3,2)\ge4\ \text{for all }d.
}
\]

At every visible endpoint pair, common depth produces the same two-parameter local family

\[
e^{px+nH(x)}.
\]

At self-conjugate contexts, \(H\) is even. At nonreal contexts, its odd cumulants encode chirality. Nevertheless, the first possible three-column rank loss is always governed by one explicit five-jet conic.

Thus the evidence does not support growth with \(\varphi(d)\) at the level of formal jet geometry. The remaining question is arithmetic:

\[
\boxed{
\text{Does every cyclotomic endpoint lattice avoid nonidentity points on the chiral conic?}
}
\]

A positive answer gives the uniform theorem

\[
\boxed{C^{\mathrm{cd}}_d(3,2)=4\quad(d\ge1).}
\]

That theorem remains open for \(d\ge3\), and this chapter states exactly what must be proved to close it.

---

## End of Part XVII
