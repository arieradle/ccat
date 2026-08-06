# Cyclotomic Coefficient Arithmetic

## Part XIX — Quaternary Visible Five-Jet Rigidity and First Subcritical Closure

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete for every visible endpoint pair at the quaternary context and for the subcritical pair \((1,2)\); the full quaternary capacity remains open only for the subcritical pairs \((1,3)\) and \((2,3)\)  
**Scope:** Exact \(d=4\) one-factor cumulants, complete quadratic and cubic visibility, the full quaternary endpoint-obstruction classification, visible five-jet injectivity modulo exact identities, exact visible capacity, a \(\Phi_4\)-Wronskian elimination theorem for \((1,2)\), and the precise remaining route to \(C^{\mathrm{cd}}_4(3,2)=4\).

---

# 0. Purpose, status, and relation to Part XVIII

Part XVIII established

\[
\boxed{C^{\mathrm{cd}}_3(3,2)=4}
\]

and reduced every visible five-jet failure at a nonreal context to three endpoint invariants

\[
\Omega_d,
\qquad
\Delta_d,
\qquad
\Sigma_d.
\]

The formal geometry was already uniform: if a visible direction has nonzero quadratic and cubic logarithmic cumulants, then five-jet dependence forces two opposite real centered drift points and one anti-real centered drift point. What remained was arithmetic.

The quaternary context

\[
d=4,
\qquad
\zeta=i
\]

is the first context at which three new phenomena coexist.

1. The local field is still quadratic,
   \[
   \mathbb Q(i),
   \]
   but the residue channels are no longer ternary.
2. A nontrivial residue channel can be self-conjugate:
   \[
   i^2=-1.
   \]
   Consequently the cubic cumulant can vanish.
3. There are three subcritical endpoint pairs:
   \[
   (1,2),\qquad(1,3),\qquad(2,3),
   \]
   rather than one.

This chapter proves the following results.

## Proved conclusion A — exact quaternary one-factor cumulants

For every

\[
N=4a+s,
\qquad
0\le s\le3,
\]

the first four regularized logarithmic cumulants of \((q;q)_N\) at \(q=i\) are given by explicit rational polynomials in \(a\).

## Proved conclusion B — complete visible spectral classification

For every visible two-endpoint direction at \(d=4\),

\[
\boxed{C\ne0.}
\]

Moreover,

\[
\boxed{J=0}
\]

occurs only for the exact adjacent same-block identity

\[
R(q)=\frac1{1-q^B},
\qquad
B\equiv2\pmod4.
\]

Thus there are no quadratically invisible visible directions and no nonidentity cubically invisible visible directions.

## Proved conclusion C — complete quaternary endpoint obstruction

For every visible direction with \(C,J\ne0\),

\[
\boxed{\Omega_4(A,B)=0}
\]

if and only if the endpoint ratio is one of the exact binomial units already classified in Part XVIII:

\[
R(q)=1-q
\]

or

\[
R(q)=\frac1{1-q^B}
\]

for adjacent endpoints in one \(4\)-block.

There are no nonidentity visible quaternary solutions of the chiral endpoint obstruction.

## Proved conclusion D — exact visible quaternary capacity

Every nonzero visible common-depth rank-three circuit with at most two positive endpoints satisfies

\[
\boxed{
\operatorname{ord}_{q=i}F\le h+4.
}
\]

The universal excess-four witness uses endpoints \((4,8)\), which are visible. Hence

\[
\boxed{
C^{\mathrm{cd,vis}}_4(3,2)=4.
}
\]

## Proved conclusion E — first subcritical quaternary closure

For the subcritical pair

\[
(A,B)=(1,2),
\]

the first five jets are injective on every three-dimensional function span. Therefore every nonzero circuit supported on \((1,2)\) satisfies

\[
\boxed{
\operatorname{ord}_{q=i}F\le4.
}
\]

## Exact remaining gap

The full theorem

\[
C^{\mathrm{cd}}_4(3,2)=4
\]

is now reduced to exactly two subcritical pairs:

\[
\boxed{(1,3)\quad\text{and}\quad(2,3).}
\]

No statement in this chapter assumes those two cases.

Throughout,

\[
D=q\frac d{dq},
\qquad
q=ie^x,
\]

so that

\[
D=\frac d{dx}.
\]

All arithmetic is exact. The finite polynomial sign checks and the Gröbner-basis elimination are reproduced in the appendices and in the companion certificate script.

---

# 1. Common-depth circuits at the quaternary context

For \(N\ge0\), write

\[
(q;q)_N=\prod_{m=1}^{N}(1-q^m).
\]

A two-endpoint factorial term is

\[
T(q)=q^\alpha(q;q)_A^u(q;q)_B^v,
\qquad
0<A<B,
\qquad
\alpha,u,v\in\mathbb Z.
\]

At \(d=4\), its cyclotomic depth is

\[
\boxed{
h_4(T)
=
 u\left\lfloor\frac A4\right\rfloor
+v\left\lfloor\frac B4\right\rfloor.
}
\]

A rank-three factorial circuit is

\[
F(q)=\sum_{r=1}^{m}c_rT_r(q),
\qquad
1\le m\le3,
\qquad
c_r\in\mathbb Q^\times.
\]

It has common depth \(h\) if

\[
h_4(T_r)=h
\qquad(1\le r\le m).
\]

Put

\[
r_A=\left\lfloor\frac A4\right\rfloor,
\qquad
r_B=\left\lfloor\frac B4\right\rfloor.
\]

The endpoint pair is **visible** when

\[
r_A+r_B>0,
\]

and **subcritical** when

\[
0<A<B<4.
\]

Thus the subcritical pairs are exactly

\[
(1,2),\qquad(1,3),\qquad(2,3).
\]

## 1.1 The visible one-direction reduction

Assume \((A,B)\) is visible. Put

\[
g=\gcd(r_A,r_B)
\]

when both depths are positive. The primitive zero-depth direction is

\[
(e_A,e_B)
=
\left(\frac{r_B}{g},-\frac{r_A}{g}\right).
\]

If \(r_A=0<r_B\), the primitive direction is

\[
(e_A,e_B)=(1,0).
\]

Define the zero-depth ratio

\[
\boxed{
R_{A,B}(q)
=(q;q)_A^{e_A}(q;q)_B^{e_B}.
}
\]

It is a local unit at \(q=i\).

Let

\[
R_0=R_{A,B}(i),
\qquad
\lambda=D\log R_{A,B}(i),
\]

and define

\[
\boxed{
H(x)
=
\log\frac{R_{A,B}(ie^x)}{R_0}
-
\lambda x.
}
\]

Then

\[
H(0)=H'(0)=0.
\]

After removing one common-depth base term and absorbing nonzero local constants into the outer coefficients, every term has the form

\[
\boxed{
f_{p,n}(x)=\exp(px+nH(x)),
}
\]

where

\[
p=\beta+n\lambda,
\qquad
\beta,n\in\mathbb Z.
\]

Write

\[
C=H''(0),
\qquad
J=H^{(3)}(0),
\qquad
D_4=H^{(4)}(0).
\]

The signed reciprocity degree \(E\) is defined by

\[
R(q^{-1})=\varepsilon q^{-E}R(q),
\qquad
\varepsilon\in\{\pm1\}.
\]

Then

\[
\lambda+\bar\lambda=E.
\]

Define the anti-real drift

\[
\boxed{
\mu=\lambda-\frac E2.
}
\]

At \(d=4\),

\[
\mu,J\in i\mathbb Q,
\qquad
C,D_4\in\mathbb Q.
\]

---

# 2. The quaternary residue kernels

The one-factor cumulants follow from four residue channels modulo four.

For \(\rho\ne1\), the universal kernel is

\[
K_r(\rho)=-\operatorname{Li}_{1-r}(\rho).
\]

For the singular channel \(\rho=1\), regularization gives

\[
K_1(1)=\frac12,
\qquad
K_2(1)=\frac1{12},
\qquad
K_3(1)=0,
\qquad
K_4(1)=-\frac1{120}.
\]

## Lemma 2.1 — Exact quaternary kernel table

For the four residues modulo four, the kernels through order four are

\[
\begin{array}{c|c|c|c|c}
\rho & K_1(\rho)&K_2(\rho)&K_3(\rho)&K_4(\rho)\\
\hline
1 & \frac12&\frac1{12}&0&-\frac1{120}\\[1mm]
i & \frac{1-i}{2}&\frac12&\frac i2&-1\\[1mm]
-1&\frac12&\frac14&0&-\frac18\\[1mm]
-i&\frac{1+i}{2}&\frac12&-\frac i2&-1
\end{array}
\]

### Proof

For \(\rho\ne1\), use

\[
K_1(\rho)=-\frac{\rho}{1-\rho},
\]

\[
K_2(\rho)=-\frac{\rho}{(1-\rho)^2},
\]

\[
K_3(\rho)=-\frac{\rho(1+\rho)}{(1-\rho)^3},
\]

and

\[
K_4(\rho)
=-\frac{\rho(1+4\rho+\rho^2)}{(1-\rho)^4}.
\]

Substitution of \(i,-1,-i\) gives the displayed values. The singular row is the Bernoulli regularization from Part IV. ∎

## 2.2 Residue-class power sums

For \(r\ge1\), define

\[
S_r(N)=\sum_{m=1}^{N}m^r.
\]

For residue \(c\in\{1,2,3,4\}\), define

\[
P_{r,c}(a)
=
\sum_{j=0}^{a-1}(4j+c)^r.
\]

If \(N=4a+s\), the residue classes \(1,\ldots,s\) contain one additional term. Every cumulant is therefore an explicit linear combination of arithmetic-progression power sums. This gives polynomial formulas with no root approximation.

---

# 3. Exact one-factor quaternary cumulants

Fix

\[
N=4a+s,
\qquad
0\le s\le3.
\]

For the regularized logarithmic germ of \((q;q)_N\) at \(i\), write

\[
D\log(q;q)_N(i)
=
\frac{N(N+1)}4+i\ell_s(a).
\]

Write the next three cumulants as

\[
C_s(a),
\qquad
i j_s(a),
\qquad
D_s(a).
\]

## Proposition 3.1 — Closed quaternary cumulant formulas

The anti-real drift coefficients are

\[
\boxed{
\begin{aligned}
\ell_0(a)&=a,\\
\ell_1(a)&=-\frac{2a+1}{2},\\
\ell_2(a)&=-\frac{2a+1}{2},\\
\ell_3(a)&=a+1.
\end{aligned}
}
\tag{3.1}
\]

The quadratic cumulants are

\[
\boxed{
\begin{aligned}
C_0(a)
&=\frac{2a(32a^2+3a-2)}9,\\[1mm]
C_1(a)
&=\frac{(2a+1)(64a^2+46a+9)}{18},\\[1mm]
C_2(a)
&=\frac{(2a+1)(64a^2+82a+27)}{18},\\[1mm]
C_3(a)
&=\frac{2(a+1)(32a^2+61a+27)}9.
\end{aligned}
}
\tag{3.2}
\]

The cubic anti-real coefficients are

\[
\boxed{
\begin{aligned}
j_0(a)&=-a(16a^2-3),\\
j_1(a)&=\frac{(2a+1)(16a^2+16a+1)}2,\\
j_2(a)&=\frac{(2a+1)(16a^2+16a+1)}2,\\
j_3(a)&=-(a+1)(16a^2+32a+13).
\end{aligned}
}
\tag{3.3}
\]

The fourth cumulants are

\[
\boxed{
\begin{aligned}
D_0(a)
&=-\frac{4a(6144a^4+60a^3-1460a^2+101)}{225},\\[1mm]
D_1(a)
&=-\frac{(2a+1)(12288a^4+22776a^3+14492a^2+3554a+225)}{225},\\[1mm]
D_2(a)
&=-\frac{(2a+1)(12288a^4+26376a^3+19892a^2+6254a+675)}{225},\\[1mm]
D_3(a)
&=-\frac{4(a+1)(6144a^4+24516a^3+35224a^2+21476a+4725)}{225}.
\end{aligned}
}
\tag{3.4}
\]

### Proof

The real part of every first-order residue kernel in Lemma 2.1 is \(1/2\). Hence

\[
\operatorname{Re}D\log(q;q)_N(i)
=
\frac12\sum_{m=1}^{N}m
=
\frac{N(N+1)}4.
\]

The imaginary contribution is

\[
\frac i2
\left(
\sum_{m\equiv3\,(4)}m
-
\sum_{m\equiv1\,(4)}m
\right).
\]

Evaluating these two progression sums gives (3.1).

For the second cumulant, Lemma 2.1 gives

\[
C_s(a)
=
\frac1{12}\sum_{4\mid m}m^2
+
\frac12\sum_{m\equiv1,3\,(4)}m^2
+
\frac14\sum_{m\equiv2\,(4)}m^2.
\tag{3.5}
\]

For the third cumulant,

\[
ij_s(a)
=
\frac i2
\left(
\sum_{m\equiv1\,(4)}m^3
-
\sum_{m\equiv3\,(4)}m^3
\right).
\tag{3.6}
\]

For the fourth cumulant,

\[
D_s(a)
=
-\frac1{120}\sum_{4\mid m}m^4
-
\sum_{m\equiv1,3\,(4)}m^4
-
\frac18\sum_{m\equiv2\,(4)}m^4.
\tag{3.7}
\]

Each sum is an arithmetic-progression power sum. Expanding

\[
\sum_{j=0}^{L-1}(4j+c)^r
=
\sum_{u=0}^{r}
\binom ru c^{r-u}4^u
\sum_{j=0}^{L-1}j^u
\]

and using the ordinary formulas for sums of powers gives (3.2)–(3.4). The companion exact certificate recomputes every formula directly from (3.5)–(3.7). ∎

---

# 4. Visible endpoint directions

Write

\[
A=4a+s,
\qquad
B=4b+t,
\qquad
0\le s,t\le3.
\]

We first treat

\[
a,b>0.
\]

The primitive common-depth direction is

\[
\left(\frac b g,-\frac a g\right),
\qquad
 g=\gcd(a,b).
\]

For zero/nonzero questions it is convenient to use the unscaled direction

\[
(b,-a).
\]

Define

\[
L=b\ell_s(a)-a\ell_t(b),
\]

\[
\mathcal C=bC_s(a)-aC_t(b),
\]

\[
\mathcal J=bj_s(a)-aj_t(b),
\]

and

\[
\mathcal D=bD_s(a)-aD_t(b).
\]

For the primitive direction,

\[
\mu=\frac{iL}{g},
\qquad
C=\frac{\mathcal C}{g},
\qquad
J=\frac{i\mathcal J}{g},
\qquad
D_4=\frac{\mathcal D}{g}.
\]

## Lemma 4.1 — Unscaled endpoint obstruction

Define

\[
\boxed{
\omega_{s,t}(a,b)
=
\mathcal J\mathcal C^2
-
L(\mathcal J^2+\mathcal C\mathcal D).
}
\tag{4.1}
\]

Then

\[
\boxed{
\Omega_4(A,B)
=
\frac{i}{g^3}\omega_{s,t}(a,b).
}
\tag{4.2}
\]

In particular,

\[
\Omega_4(A,B)=0
\iff
\omega_{s,t}(a,b)=0.
\]

### Proof

The general obstruction is

\[
\Omega_4
=
\mu(J^2-CD_4)+JC^2.
\]

Substitute

\[
\mu=\frac{iL}{g},
\qquad
J=\frac{i\mathcal J}{g},
\qquad
C=\frac{\mathcal C}{g},
\qquad
D_4=\frac{\mathcal D}{g}.
\]

Because

\[
J^2=-\frac{\mathcal J^2}{g^2},
\]

the result is

\[
\Omega_4
=
\frac i{g^3}
\left[
\mathcal J\mathcal C^2
-
L(\mathcal J^2+\mathcal C\mathcal D)
\right].
\]

∎

## 4.1 Canonical endpoint parametrization

The inequality \(A<B\) is equivalent to the following parametrization.

If \(s<t\), write

\[
b=a+h,
\qquad
h\ge0.
\]

If \(s\ge t\), write

\[
b=a+h+1,
\qquad
h\ge0.
\]

Thus every positive-depth endpoint pair is represented uniquely by

\[
a\ge1,
\qquad
h\ge0,
\qquad
(s,t)\in\{0,1,2,3\}^2.
\]

---

# 5. Complete quadratic and cubic visibility

The first issue is whether the general chiral conic is applicable.

## Theorem 5.1 — Quaternary quadratic visibility

For every visible endpoint direction at \(d=4\),

\[
\boxed{C\ne0.}
\]

Thus no visible quaternary direction is quadratically invisible.

### Proof

### Boundary-visible directions

If \(r_A=0<r_B\), then

\[
A\in\{1,2,3\}
\]

and the primitive ratio is

\[
R=(q;q)_A.
\]

Proposition 3.1 at \(a=0\) gives

\[
C=rac12,
\qquad
\frac32,
\qquad
6
\]

for \(A=1,2,3\), respectively. These are nonzero.

### Positive-depth directions

For \(a,b>0\), the unscaled quadratic cumulant is

\[
\mathcal C=bC_s(a)-aC_t(b).
\]

Substitute the parametrization of Section 4.1. The resulting sixteen rational polynomials have fixed nonzero sign, apart from two harmless sign changes with no zero.

The only exceptional sign locations are

\[
(s,t,a,h)=(3,0,\ast,0)
\]

and

\[
(s,t,a,h)=(3,1,1,0).
\]

More precisely:

- for \((s,t)=(3,0)\), \(\mathcal C>0\) at \(h=0\) and \(\mathcal C<0\) for \(h\ge1\);
- for \((s,t)=(3,1)\),
  \[
  \mathcal C(1,0)=\frac{15}{2}>0,
  \]
  while \(\mathcal C<0\) for \(h\ge1\) or \(a\ge2\);
- in every other residue cell, \(\mathcal C<0\).

These signs are proved by translating

\[
a=x+1
\]

and, when required,

\[
h=y+1
\quad\text{or}\quad
 a=x+2,
\]

after which the signed numerator has strictly positive rational coefficients. Appendix A performs all sixteen exact checks.

Therefore \(\mathcal C\ne0\), and since \(C=\mathcal C/g\), one has \(C\ne0\). ∎

## Theorem 5.2 — Quaternary cubic visibility classification

For every visible endpoint direction at \(d=4\),

\[
J=0
\]

if and only if

\[
\boxed{
A=4a+1,
\qquad
B=4a+2,
\qquad
a\ge1.
}
\tag{5.1}
\]

Equivalently, the ratio is

\[
\boxed{
R(q)=\frac1{1-q^B},
\qquad
B\equiv2\pmod4.
}
\tag{5.2}
\]

This is an exact binomial-identity family. In particular, every nonidentity visible direction has

\[
\boxed{J\ne0.}
\]

### Proof

The boundary-visible directions \(A=1,2,3\) have

\[
j=\frac12,
\qquad
\frac12,
\qquad
-13,
\]

respectively, so none has \(J=0\).

For \(a,b>0\), use

\[
\mathcal J=bj_s(a)-aj_t(b).
\]

The exact sign table is

\[
\begin{array}{c|cccc}
 &t=0&t=1&t=2&t=3\\
\hline
s=0&+&-&-&+\\
s=1&+&-&\boxed{0\text{ only at }h=0}&+\\
s=2&+&-&-&+\\
s=3&-\text{ at }h=0,\ +\text{ for }h\ge1&-&-&+
\end{array}
\tag{5.3}
\]

All nonzero signs are strict for every \(a\ge1\). As in Theorem 5.1, each cell is proved by a positive-coefficient translation. For the unique zero cell,

\[
(s,t)=(1,2),
\]

one has the exact factor

\[
\mathcal J
=-\frac h2
\left(
64a^3+96a^2h+48a^2+32ah^2+48ah-1
\right).
\tag{5.4}
\]

At \(h=0\), the endpoints are

\[
A=4a+1,
\qquad
B=4a+2,
\]

and

\[
r_A=r_B=a.
\]

Therefore the primitive ratio is

\[
R(q)
=
\frac{(q;q)_A}{(q;q)_B}
=
\frac1{1-q^B}.
\]

Since \(B\equiv2\pmod4\),

\[
i^B=-1.
\]

The local normalized logarithm is even after drift removal, so its cubic cumulant vanishes. Conversely, Appendix A proves that (5.4) has no other zero. ∎

## Corollary 5.3 — No hidden spectral delay in the visible sector

Every visible nonidentity quaternary endpoint direction lies in the genuinely chiral regime

\[
\boxed{C,J\ne0.}
\]

The only visible loss of cubic chirality is already explained by an exact binomial unit evaluated in the self-conjugate residue channel \(-1\).

---

# 6. The quaternary endpoint obstruction

Assume first

\[
C,J\ne0.
\]

Part XVIII gives the necessary condition

\[
\Omega_4(A,B)=0
\]

for a five-jet rank loss.

## Theorem 6.1 — Complete quaternary endpoint-obstruction classification

Let \((A,B)\) be visible at \(d=4\). Then

\[
\boxed{
\Omega_4(A,B)=0
}
\]

if and only if the endpoint ratio is one of the following exact identity units.

### Family I — invisible lower endpoint

\[
A=1,
\qquad
r_A=0<r_B,
\qquad
R(q)=1-q.
\]

### Family II — adjacent endpoints in one four-block

\[
B=A+1,
\qquad
r_A=r_B>0,
\qquad
R(q)=\frac1{1-q^B}.
\]

There are no other zeros of \(\Omega_4\).

### Proof

### Boundary-visible directions

If \(r_A=0<r_B\), then \(A=1,2,3\) and \(R=(q;q)_A\). Proposition 3.1 gives

\[
\begin{array}{c|c|c|c|c|c}
A&\mu&C&J&D_4&\Omega_4\\
\hline
1&-\frac i2&\frac12&\frac i2&-1&0\\[1mm]
2&-\frac i2&\frac32&\frac i2&-3&-i\\[1mm]
3&i&6&-13i&-84&-133i
\end{array}
\tag{6.1}
\]

Thus the boundary obstruction vanishes exactly at \(A=1\), where

\[
R=1-q.
\]

### Positive-depth directions

For \(a,b>0\), Lemma 4.1 reduces the zero question to

\[
\omega_{s,t}(a,b)=0.
\]

Using the canonical parameter \(h\), the exact sign table is

\[
\begin{array}{c|cccc}
 &t=0&t=1&t=2&t=3\\
\hline
s=0
&+
&0\ (h=0),\ +\ (h\ge1)
&+
&+\\[1mm]
s=1
&+\ (h=0),\ -\ (h\ge1)
&-
&0\ (h=0),\ -\ (h\ge1)
&-\\[1mm]
s=2
&+\ (h=0),\ -\ (h\ge1)
&-
&-
&0\ (h=0),\ -\ (h\ge1)\\[1mm]
s=3
&+
&-\ (h=0),\ +\ (h\ge1)
&-\ (h=0),\ +\ (h\ge1)
&+
\end{array}
\tag{6.2}
\]

Every displayed nonzero sign is strict for all \(a\ge1\).

The three zero cells are

\[
(s,t,h)=(0,1,0),
\qquad
(1,2,0),
\qquad
(2,3,0).
\]

They are precisely

\[
A=4a+s,
\qquad
B=4a+s+1,
\qquad
r_A=r_B=a,
\]

so

\[
R(q)=\frac{(q;q)_A}{(q;q)_B}
=
\frac1{1-q^B}.
\]

The sign table is an exact finite polynomial certificate. For every cell, after substituting

\[
a=x+1
\]

and either

\[
h=y
\quad\text{or}\quad
h=y+1,
\]

the appropriately signed numerator has strictly positive coefficients. Four boundary-switch cells are checked separately at \(h=0\). The single mixed polynomial in the \((3,0)\) cell has, at \(h=0\), the factor

\[
\begin{aligned}
P(a)
={}&171392a^6+935808a^5+1545936a^4+283504a^3\\
&-1434036a^2-1186704a-269325.
\end{aligned}
\tag{6.3}
\]

After \(a=x+1\), all coefficients of \(P\) are positive. Thus it has no positive-integer zero. Appendix A verifies every assertion over \(\mathbb Q\).

Therefore the obstruction vanishes only in the stated exact-identity families. ∎

## Corollary 6.2 — Quaternary visible endpoint rejection

Let \((A,B)\) be visible and not an exact identity pair. Then

\[
\boxed{
C\ne0,
\qquad
J\ne0,
\qquad
\Omega_4(A,B)\ne0.
}
\]

Consequently the first five local jet columns of three distinct parameter pairs cannot be dependent.

---

# 7. Exact binomial units at \(d=4\)

The obstruction vanishes on exact identities, so those families must be treated on the actual function span rather than rejected by a determinant.

Let

\[
R(q)=(1-q^k)^\varepsilon,
\qquad
\varepsilon\in\{1,-1\},
\qquad
4\nmid k.
\]

Then

\[
R^\varepsilon=1-q^k.
\]

## 7.1 Odd binomial units

Assume \(k\) is odd. Put

\[
\tau_k=
\begin{cases}
1,&k\equiv1\pmod4,\\
-1,&k\equiv3\pmod4.
\end{cases}
\]

## Lemma 7.1 — Odd quaternary binomial-unit invariants

For \(k\) odd,

\[
\boxed{
C=\varepsilon\frac{k^2}{2},
\qquad
J=\tau_k\varepsilon\frac{ik^3}{2},
\qquad
D_4=-\varepsilon k^4,
\qquad
\mu=-\tau_k\varepsilon\frac{ik}{2}.
}
\tag{7.1}
\]

Consequently,

\[
\boxed{
\Omega_4=0,
\qquad
\Delta_4=\varepsilon,
\qquad
\Sigma_4=k^2.
}
\tag{7.2}
\]

### Proof

If \(k\equiv1\pmod4\), then \(i^k=i\); if \(k\equiv3\pmod4\), then \(i^k=-i\). Apply the kernel table in Lemma 2.1 to the single factor \(1-q^k\), multiply the \(r\)-th kernel by \(\varepsilon k^r\), and subtract the reciprocity drift at order one. This gives (7.1).

Substitution into

\[
\Omega_4
=
\mu(J^2-CD_4)+JC^2,
\]

\[
\Delta_4
=
\frac{J^2-CD_4}{2C^3},
\]

and

\[
\Sigma_4
=
\frac{3J^2-2CD_4}{C^2}
\]

gives (7.2). ∎

## Lemma 7.2 — Odd binomial-unit rank loss is exact

Suppose three odd-binomial-unit columns have dependent first five jets. Then their functions are exactly linearly dependent.

### Proof

The axis-rigidity theorem applies because \(C,J\ne0\). After relabeling it gives

\[
n_1=n_2=n,
\qquad
n_3=n+\varepsilon,
\]

and

\[
\beta_1-\beta_2=\pm k.
\]

The parity equation is

\[
2\beta_3-\beta_1-\beta_2+\varepsilon k(n_3-n_1)=0.
\]

If \(\beta_1-\beta_2=k\), this gives

\[
\beta_3=\beta_2.
\]

Since

\[
R^\varepsilon=1-q^k,
\]

one has the exact identity

\[
\boxed{
q^{\beta_2}R^n
=
q^{\beta_2+k}R^n
+
q^{\beta_2}R^{n+\varepsilon}.
}
\tag{7.3}
\]

The other sign is obtained by interchanging the first two terms. ∎

## 7.2 The self-conjugate residue \(-1\)

Assume

\[
k\equiv2\pmod4.
\]

The only visible exact-identity family with this residue has

\[
R(q)=\frac1{1-q^k}.
\]

At \(q=ie^x\),

\[
q^k=-e^{kx}.
\]

Therefore

\[
\frac{R(ie^x)}{R(i)}
=
\frac{2}{1+e^{kx}}
=
\frac{e^{-kx/2}}{\cosh(kx/2)}.
\]

Thus

\[
\boxed{
\lambda=-\frac k2,
\qquad
H(x)=-\log\cosh(kx/2).
}
\tag{7.4}
\]

In particular,

\[
\boxed{
C=-\frac{k^2}{4},
\qquad
J=0,
\qquad
D_4=\frac{k^4}{8}.
}
\tag{7.5}
\]

## Lemma 7.3 — Rational square classification

Let \(u_1,u_2,u_3\in\mathbb Q\) satisfy

\[
\sum_i u_i=0,
\qquad
\sum_i u_i^2=2,
\]

and suppose

\[
u_i^2-u_j^2\in\mathbb Z
\]

for every \(i,j\). Then, after reordering,

\[
\boxed{(u_1,u_2,u_3)=(-1,0,1).}
\]

### Proof

The three rational squares have a common fractional part because their pairwise differences are integral. Write

\[
u_i^2=m_i+f,
\qquad
m_i\in\mathbb Z_{\ge0},
\qquad
0\le f<1.
\]

Since their sum is two,

\[
m_1+m_2+m_3+3f=2.
\]

Thus \(3f\in\mathbb Z\), so

\[
f\in\left\{0,\frac13,\frac23\right\}.
\]

The possible multisets of squares are therefore

\[
\{2,0,0\},
\qquad
\{1,1,0\},
\qquad
\left\{\frac43,\frac13,\frac13\right\},
\qquad
\left\{\frac23,\frac23,\frac23\right\}.
\]

The first, third, and fourth multisets contain a nonzero rational number that would have to equal \(\sqrt2\), \(1/\sqrt3\), or \(\sqrt{2/3}\), respectively, which is impossible. Hence the squares are \(\{1,1,0\}\). The zero-sum condition then gives \((-1,0,1)\) after reordering. ∎

## Lemma 7.4 — Even binomial-unit rank loss is exact

Let \(k\equiv2\pmod4\) and

\[
R=(1-q^k)^{-1}.
\]

If three columns have dependent first five jets, then their functions are exactly dependent.

### Proof

The chiral-conic calculation of Part XVII requires only \(C\ne0\); it remains valid when \(J=0\). Let

\[
x_i=p_i-t.
\]

The conic equations become

\[
\sum_i x_i=0,
\]

\[
n_i=N-\frac{x_i^2}{C}
=N+\frac{4x_i^2}{k^2},
\]

and

\[
\sum_i x_i^2
=-\frac{D_4}{C}
=\frac{k^2}{2}.
\]

Put

\[
u_i=\frac{2x_i}{k}.
\]

Then

\[
\sum_i u_i=0,
\qquad
\sum_i u_i^2=2,
\]

and

\[
u_i^2-u_j^2=n_i-n_j\in\mathbb Z.
\]

Also \(p_i\in\mathbb Z\), because \(k/2\in\mathbb Z\), so \(x_i\in\frac13\mathbb Z\) and \(u_i\in\mathbb Q\). Lemma 7.3 gives

\[
(u_1,u_2,u_3)=(-1,0,1)
\]

after reordering.

After removing the common factor \(e^{tx+NH(x)}\), the three germs are

\[
e^{-kx/2+H(x)},
\qquad
1,
\qquad
 e^{kx/2+H(x)}.
\]

By (7.4),

\[
e^{H(x)}=\frac1{\cosh(kx/2)}.
\]

Hence

\[
\boxed{
e^{-kx/2+H(x)}+e^{kx/2+H(x)}-2=0.
}
\tag{7.6}
\]

Thus every five-jet rank loss is an exact functional identity. ∎

---

# 8. Visible quaternary five-jet rigidity

## Lemma 8.1 — Two-term visible contact

Let

\[
h(q)=q^r(1-q^k)^s
\]

be nonconstant, with \(4\nmid k\). Normalize \(h(i)=1\). Then

\[
\boxed{
\operatorname{ord}_{q=i}(h-1)\le2.
}
\]

### Proof

The logarithmic derivative at \(i\) is

\[
r+sD\log(1-q^k)(i).
\]

If it is nonzero, \(h-1\) has order one.

If it vanishes and \(s\ne0\), the second logarithmic derivative is

\[
sC_k.
\]

By Lemma 2.1,

\[
C_k=rac{k^2}{2}
\]

for odd \(k\), while

\[
C_k=rac{k^2}{4}
\]

for \(k\equiv2\pmod4\). In either case it is nonzero, so the order is exactly two.

If \(s=0\), nonconstancy gives \(r\ne0\), and the order is one. ∎

## Theorem 8.2 — Visible quaternary five-jet injectivity

For every visible quaternary endpoint pair, the map

\[
\operatorname{span}
\{q^{\beta_r}R_{A,B}^{n_r}:1\le r\le3\}
\longrightarrow
\mathbb Q(i)[[x]]/(x^5)
\]

is injective.

Equivalently, every nonzero visible common-depth circuit satisfies

\[
\boxed{
\operatorname{ord}_{q=i}F\le h+4.
}
\tag{8.1}
\]

### Proof

Factor the common depth and pass to the local-unit family.

Assume first that the actual function span has dimension three.

If the endpoint pair is not an exact identity pair, Corollary 6.2 gives

\[
C,J\ne0
\]

and

\[
\Omega_4\ne0.
\]

The axis-rigidity theorem therefore excludes five-jet dependence.

If the endpoint ratio is an odd binomial unit, Lemma 7.2 shows that every five-jet dependence is an exact functional dependence, contradicting the assumption that the actual span has dimension three.

If the endpoint ratio is the even adjacent unit with \(B\equiv2\pmod4\), Lemma 7.4 gives the same conclusion.

Now assume that the actual function span has dimension at most two. Divide two distinct functions. By the exact visible identity classification from Part XVIII, every identity-family quotient has the form

\[
q^r(1-q^k)^s.
\]

Lemma 8.1 shows that a nonzero two-term combination has order at most two, hence cannot vanish to order five.

Therefore the five-jet map is injective on the actual span in every visible case. Restoring the common factor of depth \(h\) gives (8.1). ∎

---

# 9. Exact visible quaternary capacity

Define \(C^{\mathrm{cd,vis}}_4(3,2)\) to be the least integer \(C\) such that every nonzero visible common-depth rank-three circuit with at most two positive endpoints satisfies

\[
\operatorname{ord}_{q=i}F\le h+C.
\]

## Theorem 9.1 — Visible quaternary upper bound

\[
\boxed{
C^{\mathrm{cd,vis}}_4(3,2)\le4.
}
\]

### Proof

This is Theorem 8.2. ∎

## Theorem 9.2 — Universal excess-four witness at \(d=4\)

Define

\[
R_4(q)=\frac{(q;q)_4^2}{(q;q)_8}
\]

and

\[
Y_4(q)=q^{16}R_4(q)^2.
\]

Then, at \(q=i\),

\[
Y_4(i)=\frac14,
\qquad
DY_4(i)=0,
\qquad
D^2Y_4(i)\ne0.
\]

Consequently,

\[
\boxed{
\left(Y_4(q)-\frac14\right)^2
}
\]

is a three-term visible common-depth circuit of exact order four.

### Proof

The general witness theorem of Part XVIII gives, for every \(d\),

\[
R_d(q)=\frac{(q;q)_d^2}{(q;q)_{2d}},
\qquad
Y_d(q)=q^{d^2}R_d(q)^2,
\]

with

\[
Y_d(\zeta_d)=\frac14,
\qquad
DY_d(\zeta_d)=0,
\]

and

\[
D^2\log Y_d(\zeta_d)
=-\frac{d^2(2d^2+1)}6\ne0.
\]

Set \(d=4\). The endpoints \((4,8)\) are visible. Therefore \(Y_4-1/4\) has exact order two and its square has exact order four. ∎

## Sharpness Theorem 9.3 — Exact visible quaternary capacity

\[
\boxed{
C^{\mathrm{cd,vis}}_4(3,2)=4.
}
\]

### Proof

Theorem 9.1 gives the upper bound. Theorem 9.2 gives a visible excess-four witness. ∎

---

# 10. The subcritical pair \((1,2)\)

At \(d=4\), common depth is zero for every subcritical term.

For the pair \((1,2)\), every term can be written uniquely as

\[
q^\beta(q;q)_1^u(q;q)_2^v
=
q^\beta(1-q)^a(1+q)^b
\]

for integers \(\beta,a,b\).

Indeed,

\[
(q;q)_1=1-q
\]

and

\[
(q;q)_2=(1-q)(1-q^2)=(1-q)^2(1+q).
\]

## Lemma 10.1 — Two-term \((1,2)\) contact

Let

\[
h(q)=q^\beta(1-q)^a(1+q)^b
\]

be nonconstant. After normalizing \(h(i)=1\),

\[
\boxed{
\operatorname{ord}_{q=i}(h-1)\le2.
}
\]

### Proof

Put

\[
P(q)=q(q^2-1).
\]

A direct logarithmic derivative calculation gives

\[
\frac{h'}h=\frac{A(q)}{P(q)},
\]

where

\[
\boxed{
A(q)
=(\beta+a+b)q^2+(a-b)q-\beta.
}
\tag{10.1}
\]

If \(A(i)\ne0\), the normalized logarithm has nonzero first derivative and \(h-1\) has order one.

If \(A(i)=0\), then

\[
\Phi_4(q)=q^2+1
\]

divides \(A\). Since both have degree at most two,

\[
A=c\Phi_4.
\]

If \(c\ne0\), then \(A/P\) has a simple zero at \(i\), because \(P(i)\ne0\). Thus the logarithm and \(h-1\) have exact order two.

If \(c=0\), then \(h'/h=0\), so \(h\) is constant. ∎

## Lemma 10.2 — Wronskian numerator

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
\tag{10.2}
\]

where

\[
\boxed{
\mathcal N
=AB(B-A)+P(AB'-BA').
}
\tag{10.3}
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

one has

\[
\frac{f''}f
=
\frac{A^2+A'P-AP'}{P^2}
\]

and the analogous expression for \(g\). Substitute these formulas into

\[
W(1,f,g)=f'g''-f''g'.
\]

The terms containing \(P'\) cancel, leaving (10.2)–(10.3). Degree counting gives \(\deg\mathcal N\le6\). ∎

## Lemma 10.3 — Exact \(\Phi_4\)-Wronskian elimination

Let

\[
\Phi=q^2+1.
\]

For arbitrary quadratic polynomials \(A,B\in\mathbb Q[q]\), define \(\mathcal N\) by (10.3). If

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
\tag{10.4}
\]

The coefficient of \(q^6\) in \(\mathcal N\) is

\[
c=\alpha\beta(\beta-\alpha).
\]

Because \(\deg\mathcal N\le6\), divisibility by \(\Phi^3\) gives

\[
\mathcal N=c\Phi^3.
\tag{10.5}
\]

If \(c=0\), then (10.5) gives \(\mathcal N=0\).

Assume \(c\ne0\). Then \(\alpha\ne0\). Divide both quadratics by \(\alpha\), and put

\[
k=\frac\beta\alpha,
\qquad
U=\frac u\alpha,
\qquad
V=\frac v\alpha,
\qquad
R=\frac r\alpha,
\qquad
S=\frac s\alpha.
\]

Then

\[
k\ne0,1,
\]

and

\[
\widetilde A=\Phi+Uq+V,
\qquad
\widetilde B=k\Phi+Rq+S.
\]

Equation (10.5) becomes

\[
\widetilde{\mathcal N}-k(k-1)\Phi^3=0.
\tag{10.6}
\]

Equating the seven coefficients of \(q^0,\ldots,q^6\) gives an ideal in

\[
\mathbb Q(k)[U,V,R,S].
\]

Its reduced Gröbner basis in graded reverse lexicographic order is

\[
\boxed{U,\ V,\ R,\ S.}
\]

The exact computation is reproduced in Appendix A. Hence

\[
U=V=R=S=0.
\]

Undoing the normalization gives

\[
A=\alpha\Phi,
\qquad
B=\beta\Phi.
\]

∎

## Lemma 10.4 — Subcritical \((1,2)\) five-jet injectivity

The first five jets of the \((1,2)\) family at \(q=i\) are injective on every three-dimensional function span.

### Proof

Suppose a nonzero combination of

\[
1,f,g
\]

vanishes to order at least five.

If only two coefficients occur, Lemma 10.1 gives a contradiction. Thus all three coefficients are nonzero.

Solving for one function in terms of the other two plus an error of order five shows that

\[
W(1,f,g)=O((q-i)^3).
\]

The numerator \(\mathcal N\) has rational coefficients. Therefore vanishing to order three at \(i\) propagates to \(-i\), and

\[
\Phi_4^3\mid\mathcal N.
\]

Apply Lemma 10.3.

If

\[
\mathcal N=0,
\]

then

\[
\left(\frac{g'}{f'}\right)'=0
\]

where defined. Hence

\[
g'=cf'
\]

and

\[
g=cf+d.
\]

Thus \(1,f,g\) are exactly dependent, contradicting the assumption that their function span has dimension three.

Otherwise

\[
A=r\Phi_4,
\qquad
B=s\Phi_4.
\]

Let \(U\) be the local analytic function defined by

\[
U(i)=0,
\qquad
U'=\frac{\Phi_4}{P}.
\]

Because \(\Phi_4\) has a simple zero and \(P(i)\ne0\),

\[
\operatorname{ord}_{q=i}U=2.
\]

After constant normalization,

\[
f=e^{rU},
\qquad
g=e^{sU}.
\]

If \(r,s\) are distinct and nonzero, the coefficient matrix of

\[
1,
\qquad
U,
\qquad
U^2
\]

in

\[
1,
\qquad
e^{rU},
\qquad
e^{sU}
\]

has determinant

\[
\frac12rs(s-r)\ne0.
\]

Thus every nonzero linear combination has leading \(U\)-degree at most two. Since \(U\) has \(q-i\) order two, every nonzero combination has order at most four.

If \(r=0\), \(s=0\), or \(r=s\), the actual function span has dimension at most two, and Lemma 10.1 applies. ∎

## Theorem 10.5 — Subcritical \((1,2)\) upper bound

Every nonzero three-term circuit supported on the endpoint pair \((1,2)\) satisfies

\[
\boxed{
\operatorname{ord}_{q=i}F\le4.
}
\]

### Proof

If the function span has dimension three, apply Lemma 10.4. If it has dimension at most two, apply Lemma 10.1. ∎

---

# 11. The partial quaternary capacity theorem

## Theorem 11.1 — Quaternary upper bound outside two pairs

Let \(F\) be a nonzero common-depth rank-three factorial circuit with at most two positive endpoints. Suppose its endpoint support is not

\[
(1,3)
\]

or

\[
(2,3).
\]

Then

\[
\boxed{
\operatorname{ord}_{q=i}F\le h+4.
}
\]

### Proof

If the endpoint pair is visible, apply Theorem 8.2.

If it is the subcritical pair \((1,2)\), common depth is zero and Theorem 10.5 applies.

If the circuit uses fewer than two positive endpoints, the one-endpoint and two-term estimates of Part XIII give the same or a stronger bound.

The only remaining two-endpoint cases are \((1,3)\) and \((2,3)\), which are excluded by hypothesis. ∎

## Corollary 11.2 — Exact reduction of the full quaternary theorem

The universal witness gives

\[
\boxed{
C^{\mathrm{cd}}_4(3,2)\ge4.
}
\]

To prove

\[
\boxed{
C^{\mathrm{cd}}_4(3,2)=4,
}
\]

it is sufficient and necessary to prove five-jet injectivity for the two subcritical endpoint families

\[
\boxed{(1,3)\quad\text{and}\quad(2,3).}
\]

### Proof

Sufficiency follows from Theorem 11.1. Necessity is simply the fact that these are the only cases not covered by the theorem. ∎

## Corollary 11.3 — First four visible contexts have constant capacity

Combining Parts XVI–XIX,

\[
\boxed{
C^{\mathrm{cd}}_1(3,2)
=
C^{\mathrm{cd}}_2(3,2)
=
C^{\mathrm{cd}}_3(3,2)
=
C^{\mathrm{cd,vis}}_4(3,2)
=4.
}
\]

The first unresolved issue at \(d=4\) is not visible chirality, field dimension, or low-cumulant delay. It is purely subcritical two-endpoint geometry.

---

# 12. What the quaternary theorem proves about dependence on \(d\)

The quaternary calculation removes three possible mechanisms for growth of the common-depth capacity.

## 12.1 No visible growth from field dimension

The field

\[
\mathbb Q(i)
\]

has a different residue geometry from \(\mathbb Q(\zeta_3)\), but every nonidentity visible endpoint pair is still rejected within five jets.

## 12.2 No nonidentity cubic invisibility

The cubic cumulant can vanish at \(d=4\), but only in the self-conjugate residue channel of an exact binomial identity. There is no new collision family hidden behind \(J=0\).

## 12.3 No new visible endpoint obstruction

The complete zero locus of \(\Omega_4\) is the exact identity locus. Thus the endpoint arithmetic at \(d=4\) behaves exactly as the uniform-capacity conjecture predicts.

## 12.4 The remaining mechanism is subcritical

Any excess greater than four at \(d=4\) must come from one of

\[
(1,3),
\qquad
(2,3).
\]

Common depth gives no exponent relation there. The one-direction chiral conic and its endpoint obstruction are therefore irrelevant. A different Wronskian or logarithmic-derivative theorem is required.

---

# 13. Next exact theorem

The immediate next theorem is now sharply stated.

## Target Theorem 13.1 — Remaining quaternary subcritical rigidity

For each

\[
(A,B)\in\{(1,3),(2,3)\},
\]

the first five jets at \(q=i\) are injective on every three-dimensional span of functions

\[
q^\beta(q;q)_A^u(q;q)_B^v.
\]

If proved, then

\[
\boxed{
C^{\mathrm{cd}}_4(3,2)=4.
}
\]

The expected route is a Wronskian numerator theorem analogous to Lemma 10.3. The logarithmic derivatives now involve the additional factor

\[
1+q+q^2,
\]

so the numerator degree and elimination ideal are larger. The exact task is nevertheless finite and isolated.

---

# 14. Theorem inventory

This chapter establishes the following new results.

1. **Exact quaternary residue kernels.**  
   The kernels at \(1,i,-1,-i\) are explicit through order four.

2. **Closed one-factor cumulants.**  
   The drift, quadratic, cubic, and fourth cumulants of \((q;q)_{4a+s}\) are explicit polynomials.

3. **Complete quadratic visibility.**  
   Every visible quaternary direction has \(C\ne0\).

4. **Complete cubic visibility classification.**  
   The only visible direction with \(J=0\) is the exact adjacent unit with \(B\equiv2\pmod4\).

5. **Complete endpoint-obstruction classification.**  
   The zero locus of \(\Omega_4\) is exactly the visible binomial-identity locus.

6. **Visible five-jet injectivity.**  
   Every visible three-dimensional function span injects into the first five jets.

7. **Exact visible quaternary capacity.**  
   \[
   C^{\mathrm{cd,vis}}_4(3,2)=4.
   \]

8. **Exact \(\Phi_4\)-Wronskian elimination.**  
   Divisibility of the degree-six Wronskian numerator by \(\Phi_4^3\) has only the affine-dependence and common-\(\Phi_4\) alternatives.

9. **Subcritical \((1,2)\) closure.**  
   Every nonzero circuit on \((1,2)\) has order at most four.

10. **Two-pair reduction.**  
    The full quaternary capacity theorem remains open only for \((1,3)\) and \((2,3)\).

---

# Appendix A. Exact symbolic certificate

The companion script below verifies:

- the residue-kernel table;
- all one-factor cumulant formulas;
- nonvanishing of every visible quadratic cumulant;
- the unique visible cubic zero;
- the complete sign table for \(\omega_{s,t}\);
- the boundary values \(0,-1,-133\) of \(\Omega_4/i\);
- the \(\Phi_4\)-Wronskian Gröbner basis.

Every calculation is over \(\mathbb Q\) or \(\mathbb Q(k)\).

```python
import sympy as sp

# Exact certificates for Part XIX.
# All calculations are over QQ or QQ(k); no numerical approximation occurs.

a, h, x, y = sp.symbols('a h x y', integer=True, nonnegative=True)
q, k = sp.symbols('q k')
I = sp.I

# ---------------------------------------------------------------------------
# 1. Universal d=4 residue kernels through order four.
# ---------------------------------------------------------------------------

def K_values(z):
    K1 = sp.simplify(-z/(1-z))
    K2 = sp.simplify(-z/(1-z)**2)
    K3 = sp.simplify(-z*(1+z)/(1-z)**3)
    K4 = sp.simplify(-z*(1+4*z+z**2)/(1-z)**4)
    return K1, K2, K3, K4

assert K_values(I) == (sp.Rational(1,2)-I/sp.Integer(2), sp.Rational(1,2), I/sp.Integer(2), -1)
assert K_values(-I) == (sp.Rational(1,2)+I/sp.Integer(2), sp.Rational(1,2), -I/sp.Integer(2), -1)
assert K_values(sp.Integer(-1)) == (sp.Rational(1,2), sp.Rational(1,4), 0, sp.Rational(-1,8))

# Singular residue 0 mod 4: regularized values from Bernoulli numbers.
K0 = (sp.Rational(1,2), sp.Rational(1,12), 0, sp.Rational(-1,120))
assert K0 == (sp.Rational(1,2), sp.Rational(1,12), 0, sp.Rational(-1,120))

# ---------------------------------------------------------------------------
# 2. One-factor regularized cumulants for N=4a+s, s=0,1,2,3.
# D log = N(N+1)/4 + i*ell_s(a); J = i*j_s(a).
# ---------------------------------------------------------------------------

ell = [
    a,
    -(2*a+1)/2,
    -(2*a+1)/2,
    a+1,
]
C = [
    2*a*(32*a**2+3*a-2)/9,
    (2*a+1)*(64*a**2+46*a+9)/18,
    (2*a+1)*(64*a**2+82*a+27)/18,
    2*(a+1)*(32*a**2+61*a+27)/9,
]
j = [
    -a*(16*a**2-3),
    (2*a+1)*(16*a**2+16*a+1)/2,
    (2*a+1)*(16*a**2+16*a+1)/2,
    -(a+1)*(16*a**2+32*a+13),
]
D4 = [
    -4*a*(6144*a**4+60*a**3-1460*a**2+101)/225,
    -(2*a+1)*(12288*a**4+22776*a**3+14492*a**2+3554*a+225)/225,
    -(2*a+1)*(12288*a**4+26376*a**3+19892*a**2+6254*a+675)/225,
    -4*(a+1)*(6144*a**4+24516*a**3+35224*a**2+21476*a+4725)/225,
]

# Verify the closed formulas directly from residue-class progression sums.

def S(r, n):
    # sum_{m=1}^n m^r, exact polynomial expression from SymPy
    m = sp.symbols('m', integer=True, positive=True)
    return sp.summation(m**r, (m, 1, n))

def progression(residue, count, power):
    u = sp.symbols('u', integer=True, nonnegative=True)
    return sp.summation((4*u+residue)**power, (u, 0, count-1))

def direct_one_factor(s):
    N = 4*a+s
    counts = {
        0: a,
        1: a + (1 if s >= 1 else 0),
        2: a + (1 if s >= 2 else 0),
        3: a + (1 if s >= 3 else 0),
    }
    sums = {r: {c: sp.expand(progression(c if c else 4, counts[c], r)) for c in range(4)} for r in range(1,5)}
    # residue 0 is 4,8,...,4a, hence progression start 4 above.
    drift = sp.Rational(1,2)*S(1,N) + I*sp.Rational(1,2)*(sums[1][3]-sums[1][1])
    c2 = sp.Rational(1,12)*sums[2][0] + sp.Rational(1,2)*(sums[2][1]+sums[2][3]) + sp.Rational(1,4)*sums[2][2]
    c3 = I*sp.Rational(1,2)*(sums[3][1]-sums[3][3])
    c4 = -sp.Rational(1,120)*sums[4][0] - (sums[4][1]+sums[4][3]) - sp.Rational(1,8)*sums[4][2]
    return tuple(sp.factor(z) for z in (drift,c2,c3,c4))

for s in range(4):
    drift, c2, c3, c4 = direct_one_factor(s)
    N = 4*a+s
    assert sp.simplify(drift - (sp.Rational(1,4)*N*(N+1) + I*ell[s])) == 0
    assert sp.simplify(c2-C[s]) == 0
    assert sp.simplify(c3-I*j[s]) == 0
    assert sp.simplify(c4-D4[s]) == 0

# ---------------------------------------------------------------------------
# 3. Visible directions and exact sign certificates.
# For A=4a+s, B=4b+t with a,b>0 use the unscaled direction (b,-a).
# The primitive direction divides all cumulants by g=gcd(a,b), so zero/nonzero
# and signs of the real obstruction coefficient are unchanged.
# ---------------------------------------------------------------------------

def endpoint_data(s, t, b_expr):
    L = sp.expand(b_expr*ell[s] - a*ell[t].subs(a,b_expr))
    CC = sp.expand(b_expr*C[s] - a*C[t].subs(a,b_expr))
    JJ = sp.expand(b_expr*j[s] - a*j[t].subs(a,b_expr))
    DD = sp.expand(b_expr*D4[s] - a*D4[t].subs(a,b_expr))
    # mu=iL, J=iJJ, hence Omega=i*omega.
    omega = sp.factor(JJ*CC**2 - L*(JJ**2 + CC*DD))
    return sp.factor(L), sp.factor(CC), sp.factor(JJ), sp.factor(DD), omega

def all_positive_coeffs(expr, vars_):
    num = sp.together(expr).as_numer_denom()[0]
    P = sp.Poly(sp.expand(num), *vars_, domain=sp.QQ)
    return bool(P.coeffs()) and all(c > 0 for c in P.coeffs())

# 3a. Quadratic visibility: C never vanishes.
for s in range(4):
    for t in range(4):
        b_expr = a+h if s<t else a+h+1
        _, CC, _, _, _ = endpoint_data(s,t,b_expr)
        if (s,t)==(3,0):
            assert all_positive_coeffs(CC.subs({a:x+1,h:0}), (x,))
            assert all_positive_coeffs(-CC.subs({a:x+1,h:y+1}), (x,y))
        elif (s,t)==(3,1):
            assert CC.subs({a:1,h:0}) == sp.Rational(15,2)
            assert all_positive_coeffs(-CC.subs({a:x+2,h:0}), (x,))
            assert all_positive_coeffs(-CC.subs({a:x+1,h:y+1}), (x,y))
        else:
            assert all_positive_coeffs(-CC.subs({a:x+1,h:y}), (x,y))

# 3b. Cubic visibility: J vanishes exactly for (s,t,h)=(1,2,0).
pos_all = {(0,0),(0,3),(1,0),(1,3),(2,0),(2,3),(3,3)}
neg_all = {(0,1),(0,2),(1,1),(2,1),(2,2),(3,1),(3,2)}
for s in range(4):
    for t in range(4):
        b_expr = a+h if s<t else a+h+1
        _, _, JJ, _, _ = endpoint_data(s,t,b_expr)
        if (s,t) in pos_all:
            assert all_positive_coeffs(JJ.subs({a:x+1,h:y}), (x,y))
        elif (s,t) in neg_all:
            assert all_positive_coeffs(-JJ.subs({a:x+1,h:y}), (x,y))
        elif (s,t)==(1,2):
            assert sp.factor(JJ.subs(h,0)) == 0
            assert all_positive_coeffs(-JJ.subs({a:x+1,h:y+1}), (x,y))
        elif (s,t)==(3,0):
            assert all_positive_coeffs(-JJ.subs({a:x+1,h:0}), (x,))
            assert all_positive_coeffs(JJ.subs({a:x+1,h:y+1}), (x,y))
        else:
            raise AssertionError((s,t))

# 3c. Endpoint obstruction omega. Zeros occur exactly for adjacent same-block
# pairs (0,1),(1,2),(2,3) at h=0.
sign_table = {
    (0,0): +1,
    (0,1): +1,
    (0,2): +1,
    (0,3): +1,
    (1,0): -1,
    (1,1): -1,
    (1,2): -1,
    (1,3): -1,
    (2,0): -1,
    (2,1): -1,
    (2,2): -1,
    (2,3): -1,
    (3,0): +1,
    (3,1): +1,
    (3,2): +1,
    (3,3): +1,
}
identity_pairs = {(0,1),(1,2),(2,3)}
boundary_switch = {(1,0): +1,(2,0): +1,(3,1): -1,(3,2): -1}

for s in range(4):
    for t in range(4):
        b_expr = a+h if s<t else a+h+1
        _, _, _, _, om = endpoint_data(s,t,b_expr)
        if (s,t) in identity_pairs:
            assert sp.factor(om.subs(h,0)) == 0
            assert all_positive_coeffs(sign_table[(s,t)]*om.subs({a:x+1,h:y+1}), (x,y))
        elif (s,t) in boundary_switch:
            assert all_positive_coeffs(boundary_switch[(s,t)]*om.subs({a:x+1,h:0}), (x,))
            assert all_positive_coeffs(sign_table[(s,t)]*om.subs({a:x+1,h:y+1}), (x,y))
        elif (s,t)==(3,0):
            num0 = sp.factor(sp.together(om.subs(h,0)).as_numer_denom()[0])
            P0 = 171392*a**6+935808*a**5+1545936*a**4+283504*a**3-1434036*a**2-1186704*a-269325
            assert sp.factor(num0/((a+1)**3*P0)) in (1,-1)
            assert all_positive_coeffs(P0.subs(a,x+1), (x,))
            assert all_positive_coeffs(om.subs({a:x+1,h:y+1}), (x,y))
        else:
            assert all_positive_coeffs(sign_table[(s,t)]*om.subs({a:x+1,h:y}), (x,y))

# Boundary visible directions a=0<b: R=(q;q)_A for A=1,2,3.
# mu=i*ell, J=i*j and Omega=i*[j*C^2-ell*(j^2+C*D4)].
boundary_omega = {}
for A in (1,2,3):
    s=A
    e=sp.factor(ell[s].subs(a,0))
    c=sp.factor(C[s].subs(a,0))
    jj=sp.factor(j[s].subs(a,0))
    dd=sp.factor(D4[s].subs(a,0))
    assert c != 0 and jj != 0
    boundary_omega[A] = sp.factor(jj*c**2-e*(jj**2+c*dd))
assert boundary_omega == {1:0,2:-1,3:-133}

# ---------------------------------------------------------------------------
# 4. Exact Phi_4 Wronskian elimination for the subcritical pair (1,2).
# ---------------------------------------------------------------------------
U,V,R,S = sp.symbols('U V R S')
Phi = q**2+1
Pq = q*(q**2-1)
Aq = Phi+U*q+V
Bq = k*Phi+R*q+S
Nq = sp.expand(Aq*Bq*(Bq-Aq)+Pq*(Aq*sp.diff(Bq,q)-Bq*sp.diff(Aq,q)))
Fq = sp.Poly(sp.expand(Nq-k*(k-1)*Phi**3), q)
equations = [Fq.coeff_monomial(q**i) for i in range(7)]
K = sp.QQ.frac_field(k)
G = sp.groebner(equations,U,V,R,S,order='grevlex',domain=K)
assert [sp.factor(g.as_expr()) for g in G.polys] == [U,V,R,S]

print('All Part XIX exact certificates verified.')
```

---

# Final synthesis

The visible quaternary problem is completely solved:

\[
\boxed{
C^{\mathrm{cd,vis}}_4(3,2)=4.
}
\]

This is not merely another computed context. It proves that the first even nonreal context introduces neither a new visible obstruction nor a new delayed-cumulant collision. The self-conjugate residue channel \(-1\) does make the cubic cumulant vanish, but only inside an exact binomial identity.

The remaining quaternary uncertainty has been compressed to two explicitly named subcritical families:

\[
\boxed{(1,3),\qquad(2,3).}
\]

Thus the route to the full theorem is now finite:

\[
\boxed{
\text{close two subcritical Wronskians}
\Longrightarrow
C^{\mathrm{cd}}_4(3,2)=4.
}
\]

## End of Part XIX
