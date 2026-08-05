# Cyclotomic Coefficient Arithmetic

## Part XVII — Sharp Binary Rank-Three Two-Endpoint Bound

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete theorem chapter with exact computer-algebra certificate  
**Scope:** Common-depth three-term factorial circuits with two shared endpoints at the binary context, the binary two-endpoint even germ, transfer of the five-jet classification from Part XVI, exact centered-lattice obstruction, classification of all exceptional endpoint pairs, exact cosh dependencies, and the sharp formula

\[
\boxed{C^{\mathrm{cd}}_2(3,2)=4.}
\]

---

# 0. Purpose, relation to Parts IV, XII, and XVI, and exact status

Part XII proved that, for every fixed cyclotomic order \(d\), top fan-in \(m\), and endpoint complexity \(S\), there is a finite common-depth excess-contact constant. Its proof is Noetherian and does not determine the constant effectively in the first higher-rank case.

Part XVI closed the positive-endpoint box

\[
\boxed{C^{\mathrm{cd}}_1(3,2)=4}
\]

by reducing every common-depth two-endpoint term to a germ

\[
\exp\bigl(px+nH(x)\bigr),
\]

where \(H\) is one fixed even nonlinear germ. A complete classification of the first five jets then reduced possible rank loss to a centered parabola and an endpoint-dependent norm equation.

Part IV proved that the same even-germ structure survives at the binary context

\[
q=-1.
\]

The present chapter carries out the suggested transfer completely.

The outcome is again sharp:

\[
\boxed{C^{\mathrm{cd}}_2(3,2)=4.}
\]

The five-jet algebra is literally the same as in Part XVI. The new content is the binary endpoint arithmetic. It has a different visibility moment, a different primitive zero-depth direction, and two exact cosh families that account for every possible five-jet rank drop.

The proof has four stages.

1. Common binary depth forces the two factorial-exponent vectors onto one affine lattice line.
2. Binary reciprocity removes every nonlinear odd logarithmic term, giving
   \[
   f_{p,n}(x)=\exp(px+nH(x)),\qquad H(-x)=H(x).
   \]
3. Five-jet dependence forces a centered norm equation together with strong divisibility of three square differences.
4. Exact endpoint inequalities exclude every pair except:
   - the zero-depth endpoint family \(A=1\);
   - the adjacent even–odd family \((A,B)=(2r,2r+1)\);
   - the isolated pair \((2,4)\).

The first two families yield exact functional identities, not nonzero high-order collisions. The pair \((2,4)\) is ruled out by parity.

The chapter does **not** prove:

- the unequal-depth constant \(C_2(3,2)\);
- any explicit \(C_d(3,2)\) for \(d\ge3\);
- an extension to every even \(d\).

The last point is structural. The binary context is the unique nontrivial self-conjugate cyclotomic context. For every \(d\ge3\), including even \(d\), primitive roots are nonreal and the odd imaginary chiral cumulants generally survive.

All arithmetic below is exact. The endpoint classification uses an explicit finite list of polynomial positivity certificates and exact rational enumeration; no floating point is used.

---

# 1. Binary common-depth factorial circuits

Let

\[
(q;q)_N=\prod_{j=1}^{N}(1-q^j),
\qquad
(q;q)_0=1.
\]

Fix two endpoints

\[
0<A<B.
\]

A compressed two-endpoint factorial term is

\[
T(q)=q^\alpha (q;q)_A^u(q;q)_B^v,
\qquad
\alpha,u,v\in\mathbb Z.
\]

Negative factorial exponents are permitted, so \(T\) may be rational.

At the binary context, put

\[
r_N=\left\lfloor\frac N2\right\rfloor.
\]

By the factorial valuation theorem,

\[
\boxed{
 v_{q+1}(T)=u r_A+v r_B.
}
\]

A three-term circuit is

\[
F(q)=\sum_{i=1}^{s}c_iT_i(q),
\qquad
1\le s\le3,
\qquad
c_i\in\mathbb Q^\times.
\]

## Definition 1.1 — Binary common depth

The circuit has **common binary depth** \(h\) if

\[
v_{q+1}(T_i)=h
\qquad(1\le i\le s).
\]

## Definition 1.2 — Binary common-depth excess capacity

Let \(C^{\mathrm{cd}}_2(m,S)\) be the least integer \(C\ge0\) such that every nonzero common-depth factorial circuit with at most \(m\) terms and at most \(S\) distinct positive factorial endpoints satisfies

\[
\boxed{
\operatorname{ord}_{q=-1}F\le h+C.
}
\]

Part XII proves that this number is finite. The purpose of this chapter is to determine it when

\[
(m,S)=(3,2).
\]

---

# 2. The exact binary factorial germ

Use the exponential coordinate

\[
q=-e^x.
\]

Then

\[
q+1=1-e^x=-x+O(x^2),
\]

so \(x\)-order and \((q+1)\)-order coincide.

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

The two weights arise from the two residue channels modulo \(2\).

## Lemma 2.1 — One-factor binary expansions

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

The even formula is the regularized singular expansion.

For odd \(m\), use

\[
\frac{1+e^{mx}}2
=e^{mx/2}\cosh(mx/2).
\]

The standard Bernoulli expansion of \(\log\cosh(y/2)\) is

\[
\log\cosh(y/2)
=
\sum_{j\ge1}
\frac{B_{2j}}{2j(2j)!}(2^{2j}-1)y^{2j}.
\]

Substitute \(y=mx\). ∎

## Proposition 2.2 — Binary endpoint normal form

For every \(N\ge0\), there is a nonzero exact residual \(b_N\) such that

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

Among \(1,\ldots,N\), exactly \(r_N\) exponents are even, and each corresponding factor vanishes simply at \(q=-1\). Their leading coefficients, together with all nonvanishing odd factors, form \(b_N\ne0\).

Every factor contributes linear drift \(m/2\). Hence the total drift is

\[
\frac12\sum_{m=1}^{N}m
=
\frac{N(N+1)}4.
\]

Lemma 2.1 shows that the \(2j\)-th logarithmic coefficient is the weighted moment \(W_{2j}(N)\). No nonlinear odd term occurs. ∎

## Corollary 2.3 — Binary evenness

After removing depth, residual, and linear drift, the factorial germ is even.

This is the factorial-quotient form of the Binary Even-Germ Theorem from Part IV.

---

# 3. Common depth gives one primitive endpoint direction

Let the exponent vector of a term be

\[
(u,v)\in\mathbb Z^2.
\]

Common depth means that all exponent vectors lie in one affine level set of

\[
(u,v)\longmapsto r_Au+r_Bv.
\]

## Lemma 3.1 — Primitive binary endpoint direction

Assume \(A\ge2\), and put

\[
g=\gcd(r_A,r_B).
\]

Every difference of two common-depth exponent vectors is an integer multiple of

\[
\boxed{
(e_A,e_B)
=
\left(\frac{r_B}{g},-\frac{r_A}{g}\right).
}
\]

If \(A=1\), then \(r_A=0\), common depth fixes the exponent of endpoint \(B\), and the only variable factorial direction is

\[
\boxed{(e_A,e_B)=(1,0).}
\]

### Proof

For \(A\ge2\), a difference \((\Delta u,\Delta v)\) satisfies

\[
r_A\Delta u+r_B\Delta v=0.
\]

The primitive integer kernel of \((r_A,r_B)\) is generated by

\[
(r_B/g,-r_A/g).
\]

For \(A=1\), the depth equation is \(r_Bv=h\), so \(v\) is fixed while \(u\) is free. ∎

Choose the corresponding zero-depth ratio

\[
R_{A,B}(q)
=(q;q)_A^{e_A}(q;q)_B^{e_B}.
\]

Normalize it by its nonzero binary residual:

\[
\boxed{
Z_{A,B}(q)
=
\frac{R_{A,B}(q)}{R_{A,B}(-1)},
\qquad
Z_{A,B}(-1)=1,
}
\]

where the value is interpreted after local cancellation when numerator and denominator both vanish.

The normal form of Proposition 2.2 gives

\[
\boxed{
Z_{A,B}(-e^x)
=
\exp\bigl(\lambda x+H(x)\bigr),
\qquad
H(-x)=H(x),
\qquad
H(0)=0,
}
\]

with

\[
\boxed{
\lambda=e_A\lambda_A+e_B\lambda_B
}
\]

and

\[
\boxed{
H(x)=
\sum_{j\ge1}
\frac{B_{2j}}{2j(2j)!}
M_{2j}x^{2j},
\qquad
M_{2j}=e_AW_{2j}(A)+e_BW_{2j}(B).
}
\]

## Proposition 3.2 — Reduction to the binary two-parameter family

After factoring one common-depth base term and absorbing nonzero residual constants into the outer coefficients, every term in the circuit has normalized germ

\[
\boxed{
f_{\beta,n}(x)
=
\exp\bigl((\beta+n\lambda)x+nH(x)\bigr),
\qquad
\beta,n\in\mathbb Z.
}
\]

Equivalently, with

\[
p=\beta+n\lambda,
\]

write

\[
\boxed{
f_{p,n}(x)=\exp(px+nH(x)).}
\]

### Proof

By Lemma 3.1, every factorial-exponent difference is \(n(e_A,e_B)\). Monomial powers differ independently by an integer \(\beta\). The sign \((-1)^\beta\) is included in the absorbed scalar so that the normalized monomial germ is \(e^{\beta x}\). ∎

---

# 4. The first binary curvature invariants

Define

\[
\boxed{
C=H''(0)=\frac{M_2}{12},
\qquad
D=H^{(4)}(0)=-\frac{M_4}{120},
\qquad
T=-\frac DC.
}
\]

The first two endpoint moments have closed forms.

## Proposition 4.1 — Closed binary visibility moments

For \(R\ge0\),

\[
\boxed{
W_2(2R)
=
\frac{R(2R+1)(8R-1)}3,
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

Split each weighted moment into even and odd power sums and substitute the classical formulas for \(\sum m^2\) and \(\sum m^4\). Expansion and collection give the displayed polynomials. ∎

## Lemma 4.2 — Exact quadratic visibility

For every \(0<A<B\),

\[
\boxed{C\ne0.}
\]

### Proof

The case \(A=1\) gives

\[
C=\frac{W_2(1)}{12}=\frac14.
\]

Assume \(A\ge2\). Put

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

It suffices to show that \(\mathcal F\) is injective on \(N\ge2\).

On each parity class, the formulas of Proposition 4.1 are strictly increasing.

For a cross-parity equality, write the odd argument as \(2s+1\). Since

\[
\mathcal F(2s+1)
=
\frac{16s^3+42s^2+35s+9}{3s},
\]

integrality of an equality with an even value forces

\[
s\mid9.
\]

Thus \(s\in\{1,3,9\}\). Direct substitution gives no integral solution for the even index. Hence no cross-parity equality occurs. Therefore \(M_2\ne0\), and so \(C\ne0\). ∎

---

# 5. The universal five-jet calculation

The following part is independent of the endpoint formulas. It uses only

\[
H'(0)=H^{(3)}(0)=0,
\qquad
H''(0)=C\ne0,
\qquad
H^{(4)}(0)=D.
\]

## Lemma 5.1 — First five derivatives

For

\[
f_{p,n}(x)=e^{px+nH(x)},
\]

one has

\[
\boxed{
\begin{aligned}
f_{p,n}(0)&=1,\\
f_{p,n}'(0)&=p,\\
f_{p,n}''(0)&=p^2+nC,\\
f_{p,n}^{(3)}(0)&=p^3+3pnC,\\
f_{p,n}^{(4)}(0)&=
 p^4+6p^2nC+3n^2C^2+nD.
\end{aligned}
}
\]

### Proof

Apply the complete Bell-polynomial formulas to the exponent \(px+nH(x)\). Its first four derivatives at zero are

\[
p,\qquad nC,\qquad0,\qquad nD.
\]

Substitution gives the formulas. ∎

Define the five-jet column

\[
J(p,n)=
\begin{pmatrix}
1\\
p\\
p^2+nC\\
p^3+3pnC\\
p^4+6p^2nC+3n^2C^2+nD
\end{pmatrix}.
\]

## Lemma 5.2 — Repeated drift values are separated

Let \((p_i,n_i)\), \(1\le i\le3\), be distinct.

1. If all \(p_i\) are equal, then the three columns \(J(p_i,n_i)\) are independent.
2. If exactly two \(p_i\) are equal, then the three columns are independent.

### Proof

If all \(p_i=p\), use rows \(0,2,4\). Elementary row operations reduce their determinant to a nonzero scalar multiple of

\[
\det
\begin{pmatrix}
1&1&1\\
n_1&n_2&n_3\\
n_1^2&n_2^2&n_3^2
\end{pmatrix},
\]

which is nonzero because the \(n_i\) are distinct and \(C\ne0\).

If \(p_1=p_2\ne p_3\), then \(n_1\ne n_2\), and the determinant of rows \(0,1,2\) is, up to sign,

\[
C(n_2-n_1)(p_3-p_1)\ne0.
\]

∎

## Project Lemma 5.3 — Centered-parabola classification

Assume \(p_1,p_2,p_3\) are pairwise distinct and the five-jet columns are dependent. Put

\[
t=\frac{p_1+p_2+p_3}{3},
\qquad
x_i=p_i-t.
\]

Then

\[
\boxed{x_1+x_2+x_3=0,}
\]

there is a constant \(N\) such that

\[
\boxed{
n_i=N-\frac{x_i^2}{C},
}
\]

and

\[
\boxed{
\sum_{i=1}^{3}x_i^2=T=-\frac DC.
}
\]

### Proof

Dependence of rows \(0,1,2\) implies that row two is affine in \(p_i\):

\[
p_i^2+Cn_i=Ap_i+B.
\tag{5.1}
\]

Dependence of row three then forces

\[
A=\frac{2(p_1+p_2+p_3)}3=2t.
\]

Substitute \(p_i=t+x_i\) into (5.1):

\[
Cn_i=t^2+B-x_i^2,
\]

which gives the parabola formula.

Substitute (5.1) into row four. The resulting quartic must agree with an affine polynomial at the three \(p_i\), hence its non-affine part is divisible by \(\prod_i(p-p_i)\). Comparing the quadratic coefficient gives

\[
\sum_i(p_i-t)^2=-\frac DC.
\]

This is the radius equation. ∎

Thus the binary problem has reached exactly the same universal five-jet geometry as the positive endpoint. The remaining work is arithmetic.

---

# 6. The centered binary lattice obstruction

The drift

\[
\lambda=e_A\lambda_A+e_B\lambda_B
\]

has denominator at most two. Let

\[
\boxed{L=\operatorname{den}(\lambda)\in\{1,2\}.}
\]

Since

\[
p_i=\beta_i+n_i\lambda,
\qquad
\beta_i,n_i\in\mathbb Z,
\]

one has

\[
p_i\in\frac1L\mathbb Z.
\]

Define centered integer coordinates

\[
\boxed{
z_i=3Lx_i.}
\]

Then

\[
\boxed{z_1+z_2+z_3=0.}
\]

The radius equation becomes

\[
\boxed{
M:=9L^2T=z_1^2+z_2^2+z_3^2.
}
\tag{6.1}
\]

In particular, five-jet dependence requires

\[
\boxed{M\in\mathbb Z_{\ge0}.}
\]

Now put

\[
\boxed{
K=9L^2C=\frac PQ
}
\]

in lowest terms, with \(P>0\).

## Lemma 6.1 — Square-difference divisibility

Under five-jet dependence,

\[
\boxed{
P\mid z_i^2-z_j^2
\qquad(1\le i,j\le3).
}
\]

### Proof

The centered-parabola equation gives

\[
n_i-n_j
=-\frac{x_i^2-x_j^2}{C}
=-\frac{z_i^2-z_j^2}{9L^2C}
=-\frac{Q(z_i^2-z_j^2)}P.
\]

The left side is integral and \(\gcd(P,Q)=1\). Therefore \(P\) divides every square difference. ∎

## Corollary 6.2 — Radius domination excludes dependence

If

\[
\boxed{P>M,}
\]

then the three five-jet columns are independent unless the underlying functions are already linearly dependent.

### Proof

By (6.1),

\[
|z_i^2-z_j^2|\le M<P.
\]

Lemma 6.1 then forces every square difference to be zero. Thus

\[
z_1^2=z_2^2=z_3^2.
\]

Three distinct integers with zero sum cannot all have the same square: a nonzero square permits only the two values \(\pm a\), while square zero gives only one value. This contradicts the pairwise distinctness of the \(p_i\). ∎

---

# 7. Exact endpoint arithmetic

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
b=r_B.
\]

Put

\[
g=\gcd(a,b).
\]

Before division by \(g\), define

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
D=-\frac{m_4}{120g},
\qquad
T=\frac{m_4}{10m_2}.
}
\]

Whenever \(T\ge0\), the sufficient inequality

\[
\boxed{
5m_2^2>6g|m_4|
}
\tag{7.1}
\]

implies

\[
|9L^2C|>9L^2T.
\]

Since the numerator \(P\) of \(9L^2C\) satisfies

\[
P\ge |9L^2C|,
\]

inequality (7.1) implies \(P>M\), and Corollary 6.2 applies.

## Project Lemma 7.1 — Complete binary endpoint classification

For every pair

\[
0<A<B,
\]

exactly one of the following alternatives applies.

1. \(A=1\).
2. \(A\) is even and \(B=A+1\).
3. The scaled radius \(M=9L^2T\) is not an integer.
4. \((A,B)=(2,4)\).
5. The reduced curvature numerator satisfies
   \[
   P>M.
   \]

### Proof

The proof is an exact finite polynomial certificate.

Set

\[
b=a+r.
\]

The four parity patterns are denoted

\[
EE,\ EO,\ OE,\ OO.
\]

The special case \(EO\) with \(r=0\) is exactly

\[
(A,B)=(2a,2a+1),
\]

which is alternative 2.

For all remaining infinite cones, use

\[
g=\gcd(a,b)=\gcd(a,r)\le\min(a,r)
\]

and square (7.1). The resulting sufficient polynomial is

\[
\boxed{
\mathscr S
=25m_2^4-36G^2m_4^2,
}
\]

where \(G\) is the relevant upper bound for \(g\).

After the indicated nonnegative-variable substitutions, every coefficient of \(\mathscr S\) is nonnegative and its constant coefficient is positive.

| Parity | Infinite region | Substitution | Terms in certificate |
|---|---:|---:|---:|
| \(EE\) | \(r\ge a+1\) | \(r=a+u+1\) | 143 |
| \(EE\) | \(a\ge r+1\) | \(a=r+u+1\) | 143 |
| \(EO\) | \(r\ge a+1\) | \(r=a+u+1\) | 143 |
| \(EO\) | \(a\ge r+1\) | \(a=r+u+1\) | 143 |
| \(OE\) | \(r\ge a+3\) | \(r=a+u+3\) | 143 |
| \(OE\) | \(a\ge r+3,\ r\ge2\) | \(r=X+2,\ a=X+Y+5\) | 143 |
| \(OO\) | \(r\ge a+2\) | \(r=a+u+2\) | 143 |
| \(OO\) | \(a\ge r+2\) | \(a=r+u+2\) | 143 |

The smallest coefficient in these exact expanded certificates is positive; the minimum over the eight certificates is \(20227\).

The finitely many boundary lines are handled by the same one-variable coefficient-positivity test. The required starting values are:

| Boundary | Positivity from |
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

Every boundary certificate has nonnegative coefficients and positive constant term. Ten contain 17 monomials; the line \(OE:r=1\) contains 13.

Consequently, every pair not already covered lies in the finite box

\[
2\le A<B\le40.
\]

Exact rational enumeration in that box finds the following pairs for which the coarse inequality does not already prove \(P>M\), after excluding adjacent even–odd pairs:

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

For every member of \(\mathcal E\) except \((2,4)\), exact reduction gives

\[
M\notin\mathbb Z.
\]

The pair \((2,4)\) has

\[
M=36.
\]

This proves the classification. ∎

### Caution 7.2 — Nature of the certificate

Lemma 7.1 is machine-assisted but exact. The supplied verifier expands integer polynomials, checks every coefficient sign, and enumerates a finite integer box using rational arithmetic. It does not infer positivity from sampling and does not use numerical approximations.

---

# 8. The isolated pair \((2,4)\)

For \((A,B)=(2,4)\), one obtains

\[
\boxed{
\lambda=-2,
\qquad
C=-3,
\qquad
D=12,
\qquad
T=4,
\qquad
L=1,
\qquad
M=36.
}
\]

Five-jet dependence would therefore give integers

\[
z_1+z_2+z_3=0,
\qquad
z_1^2+z_2^2+z_3^2=36.
\]

Put

\[
z_3=-z_1-z_2.
\]

Then

\[
\boxed{
z_1^2+z_1z_2+z_2^2=18.}
\]

## Lemma 8.1 — Binary parity obstruction

The equation

\[
z_1^2+z_1z_2+z_2^2=18
\]

has no integer solution.

### Proof

Modulo \(2\), the quadratic form

\[
x^2+xy+y^2
\]

vanishes only at \((x,y)=(0,0)\). Hence \(z_1\) and \(z_2\) must both be even. The left side is then divisible by \(4\), while \(18\) is not. Contradiction. ∎

Thus \((2,4)\) cannot produce five-jet dependence.

---

# 9. The exact cosh families

The remaining two alternatives of Lemma 7.1 do permit five-jet dependence, but only because the corresponding functions satisfy an exact identity.

## 9.1 The zero-depth endpoint family \(A=1\)

Here the primitive normalized ratio is

\[
Z(q)=\frac{1-q}{2}.
\]

At \(q=-e^x\),

\[
\boxed{
Z(-e^x)
=e^{x/2}\cosh(x/2).
}
\]

Therefore

\[
\lambda=\frac12,
\qquad
H(x)=\log\cosh(x/2),
\qquad
C=\frac14,
\qquad
D=-\frac18,
\qquad
T=\frac12.
\]

The centered-lattice equations force, after reordering,

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

After factoring \(e^{tx+(N-1)H(x)}\), the three functions become

\[
e^{-x/2},
\qquad
e^{H(x)}=\cosh(x/2),
\qquad
e^{x/2}.
\]

Hence

\[
\boxed{
e^{-x/2}+e^{x/2}-2e^{H(x)}=0.}
\]

Every five-jet rank drop is therefore an exact functional dependence.

## 9.2 The adjacent even–odd family

Let

\[
A=2r,
\qquad
B=2r+1.
\]

The primitive zero-depth ratio collapses globally:

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
\frac2{1+e^{Bx}}
=
\frac{e^{-Bx/2}}{\cosh(Bx/2)}.
}
\]

Thus

\[
\boxed{
\lambda=-\frac B2,
\qquad
H(x)=-\log\cosh(Bx/2),
}
\]

and

\[
\boxed{
C=-\frac{B^2}{4},
\qquad
D=\frac{B^4}{8},
\qquad
T=\frac{B^2}{2}.
}
\]

Under five-jet dependence, define

\[
u_i=\frac{2x_i}{B}.
\]

Then

\[
\sum_i u_i=0,
\qquad
\sum_i u_i^2=2,
\qquad
n_i=N+u_i^2.
\]

Therefore the rational numbers \(u_i^2\) differ pairwise by integers.

## Lemma 9.1 — Rational square classification

Let \(u_1,u_2,u_3\in\mathbb Q\) satisfy

\[
\sum_i u_i=0,
\qquad
\sum_i u_i^2=2,
\]

and suppose all pairwise differences \(u_i^2-u_j^2\) are integers. Then, after reordering,

\[
\boxed{(u_1,u_2,u_3)=(-1,0,1).}
\]

### Proof

All three squares have one common fractional part \(\theta\). Since their sum is \(2\), the possible fractional-square patterns are:

\[
\{2/3,2/3,2/3\},
\qquad
\{4/3,1/3,1/3\},
\qquad
\{1,1,0\},
\]

up to adding the only nonnegative integers compatible with total sum two.

The first two patterns require irrational square roots. Since the \(u_i\) are rational, they are impossible. The last pattern gives the three values \(-1,0,1\) from the zero-sum condition. ∎

Consequently,

\[
x_i\in\left\{-\frac B2,0,\frac B2\right\},
\qquad
n_i\in\{N+1,N,N+1\}.
\]

After factoring \(e^{tx+NH(x)}\), the three functions become

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

one has the exact identity

\[
\boxed{
e^{-Bx/2+H(x)}+e^{Bx/2+H(x)}-2=0.}
\]

Again every five-jet rank drop is an exact functional dependence.

---

# 10. Five-jet injectivity

## Project Theorem 10.1 — Binary five-jet rank theorem

Fix two endpoints

\[
0<A<B.
\]

Let

\[
\mathcal V
=
\operatorname{span}
\left\{
\exp(p_ix+n_iH(x)):1\le i\le3
\right\}.
\]

Then the truncation map

\[
\boxed{
\mathcal V\longrightarrow\mathbb Q[[x]]/(x^5)
}
\]

is injective.

Equivalently, every nonzero element of \(\mathcal V\) has order at most four.

### Proof

First quotient the list by exact functional dependencies, so its functions form a basis of \(\mathcal V\).

If \(\dim\mathcal V=1\), the assertion is immediate.

If \(\dim\mathcal V=2\), take two distinct parameter pairs. If their \(p\)-values differ, rows zero and one separate them. If their \(p\)-values agree, their \(n\)-values differ, and row two separates them because \(C\ne0\). Thus the first three jets are already injective.

Assume \(\dim\mathcal V=3\). If the five-jet columns were dependent, Lemmas 5.2 and 5.3 would give the centered lattice equations.

- If \(A=1\), Section 9.1 shows that such dependence is an exact functional dependence, contradicting \(\dim\mathcal V=3\).
- If \(A\) is even and \(B=A+1\), Section 9.2 gives the same contradiction.
- If \(M\notin\mathbb Z\), equation (6.1) is impossible.
- If \((A,B)=(2,4)\), Lemma 8.1 gives a contradiction.
- In every remaining case, Lemma 7.1 gives \(P>M\), and Corollary 6.2 gives a contradiction.

Therefore the five-jet columns are independent. ∎

---

# 11. The sharp binary capacity

## Project Theorem 11.1 — Effective binary rank-three two-endpoint bound

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

Factor \(x^h\) from all terms in the coordinate \(q=-e^x\), absorb the nonzero leading residuals into the coefficients, and factor one common base unit. Proposition 3.2 reduces the remaining unit span to at most three functions of the form

\[
\exp(p_ix+n_iH(x)).
\]

By Theorem 10.1, every nonzero combination of these units has \(x\)-order at most four. Restoring the common factor \(x^h\) gives the stated bound. ∎

## Sharpness Theorem 11.2 — Exact value of the binary capacity

\[
\boxed{
C^{\mathrm{cd}}_2(3,2)=4.
}
\]

### Proof

Theorem 11.1 gives the upper bound.

For sharpness, use the exact identity

\[
1+
\frac{(1-q)^2}{2q}
+
\frac{(1-q)^4}{16q^2}
=
\frac{(q+1)^4}{16q^2}.
\]

Multiply by \((q;q)_2=(1-q)(1-q^2)\):

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

The three terms use exactly the endpoints \(1,2\). Since

\[
v_{q+1}((q;q)_1)=0,
\qquad
v_{q+1}((q;q)_2)=1,
\]

each term has common depth

\[
h=1.
\]

The right side has order

\[
5
\]

at \(q=-1\). Hence the excess contact is

\[
5-1=4.
\]

Therefore no smaller constant is possible. ∎

---

# 12. Exact certificate algorithm

## Algorithmic Theorem 12.1 — Five-coefficient binary identity certificate

For a common-depth three-term, two-endpoint circuit at \(q=-1\), compute the regularized coefficients through degree four. Then

\[
\boxed{
F=0
\iff
[x^{h+j}]F(-e^x)=0
\quad(0\le j\le4).
}
\]

### Proof

If \(F=0\), all coefficients vanish.

Conversely, if the first five regularized coefficients vanish, the regularized circuit has order at least five. Theorem 11.1 says that every nonzero circuit has regularized order at most four. Hence the circuit is zero. ∎

## Algorithm 12.2 — Exact binary five-jet computation

For each term:

1. compute its depth
   \[
   h_i=\sum_N e_{i,N}\lfloor N/2\rfloor;
   \]
2. verify common depth;
3. compute the exact leading residual from the local factorial normal form;
4. compute \(\lambda\), \(M_2\), and \(M_4\) from the closed binary moments;
5. reconstruct the first five derivatives using Lemma 5.1;
6. add the columns with the exact outer coefficients.

All operations use integers and rationals. No root approximation is required because \(\zeta_2=-1\in\mathbb Q\).

### Caution 12.3 — Arithmetic output size

The multiplicity bound is effective. A bit-polynomial identity test additionally requires compact exact handling of the potentially enormous leading residuals. This chapter does not remove that separate output-size issue.

---

# 13. Exact computational verification

The accompanying module

```text
src/ccat/research/effective_binary_rank3_two_endpoint.py
```

implements the proof objects and regression checks.

## Verification 13.1 — Closed moment formulas

For \(1\le A<50\), the closed formulas for \(W_2(A)\) and \(W_4(A)\) are checked against their defining weighted sums.

## Verification 13.2 — Infinite endpoint certificate

The verifier expands:

- eight two-variable cone polynomials;
- eleven one-variable boundary polynomials.

It checks that every coefficient is nonnegative and every constant term is positive. The proof is over \(\mathbb Z\).

## Verification 13.3 — Finite endpoint box

Every pair in

\[
2\le A<B\le40
\]

is processed exactly. The program confirms the finite exception list in Lemma 7.1 and that \((2,4)\) is the unique non-special pair with integral scaled radius.

## Verification 13.4 — Centered lattice search

Every endpoint pair with

\[
1\le A<B\le81
\]

is checked by exact integer enumeration of the centered norm equation. Solutions occur only in the two exact cosh families.

## Verification 13.5 — Parameter boxes

For eleven representative endpoint pairs, all triples in

\[
-3\le\beta_i,n_i\le3
\]

are checked. No independent span has third pivot order above four.

## Verification 13.6 — Large endpoints

Two hundred exact randomized trials include endpoints as large as \(4000\), together with deliberately selected exceptional and near-exceptional families.

## Verification 13.7 — Direct rational factorization

Representative true circuits are constructed as exact rational functions in \(q\), and their predicted contact orders are compared with direct factor multiplicity of \(q+1\).

## Verification 13.8 — Test suite

The accompanying tests execute six exact test groups. The current result is

```text
6 passed
```

with no floating-point certificate arithmetic.

---

# 14. Theorem inventory

| Number | Result | Exact conclusion | Main mechanism |
|---|---|---|---|
| 2.2 | Binary endpoint normal form | Depth, drift, and all even logarithmic moments are explicit | Even/odd residue channels |
| 3.1 | Primitive endpoint direction | Common-depth exponent differences form one affine lattice line | Kernel of binary depth map |
| 4.1 | Closed \(W_2,W_4\) formulas | Polynomial endpoint invariants | Power-sum evaluation |
| 4.2 | Quadratic visibility | \(C\ne0\) for every endpoint pair | Injectivity of normalized \(W_2\) |
| 5.3 | Centered-parabola classification | Five-jet dependence forces fixed centered radius | Universal jet algebra |
| 6.1 | Square-difference divisibility | Curvature numerator divides all centered square differences | Parameter lattice |
| 7.1 | Endpoint classification | Only two cosh families and \((2,4)\) escape generic radius domination | Exact polynomial certificates |
| 8.1 | \((2,4)\) exclusion | No centered integral solution | Quadratic-form parity |
| 9.1 | Rational square classification | Adjacent even–odd rank loss is an exact identity | Rational norm geometry |
| 10.1 | Binary five-jet rank theorem | First five coefficients inject every independent three-term span | Classification plus arithmetic |
| 11.1 | Effective contact bound | Every nonzero circuit has order at most \(h+4\) | Five-jet injectivity |
| 11.2 | Sharp capacity | \(C^{\mathrm{cd}}_2(3,2)=4\) | Explicit sharp circuit |
| 12.1 | Identity certificate | Five regularized coefficients decide identity | Sharp multiplicity bound |

---

# 15. Boundaries and next problems

## 15.1 Common depth

The proof uses common depth to place the exponent vectors on one affine line. Unequal depths require the depth-block machinery of Part XII and remain open effectively at \(d=2\).

## 15.2 Two endpoints and three terms

The five-jet geometry is specific to rank three with one factorial-line parameter and one monomial-drift parameter. Increasing \(m\) or \(S\) changes the rank geometry.

## 15.3 The result does not extend to all even cyclotomic orders

The mechanism is not “even \(d\).” It is “self-conjugate primitive context.”

The primitive roots are real only for

\[
d=1,2.
\]

At every \(d\ge3\), including even \(d\), reciprocity pairs two distinct conjugate contexts. The normalized germ has real even amplitude cumulants but generally nonzero purely imaginary odd phase cumulants. Therefore the reduction to one even nonlinear germ fails.

The next genuinely new local geometry begins already at

\[
\boxed{d=3.}
\]

## 15.4 A plausible \(d\ge3\) replacement

For \(d\ge3\), a two-endpoint common-depth term should be written in the form

\[
\exp\bigl(
px+nH_{\mathrm{even}}(x)+in\Phi_{\mathrm{odd}}(x)
\bigr),
\]

with real even \(H_{\mathrm{even}}\) and real odd \(\Phi_{\mathrm{odd}}\). The first five jets now depend on an additional chiral invariant, so the centered-parabola classification must be replaced by a genuinely complex rank theorem.

## 15.5 Compact residual arithmetic

Even with a constant contact bound, enormous factorial residuals may have exponentially many output bits. A practical compressed PIT implementation still needs compact exact addition and zero testing for those constants.

---

# 16. Final synthesis

The binary context is the closest possible successor to the positive endpoint because Part IV’s reciprocity theorem again removes every nonlinear odd logarithmic term.

For two shared endpoints, common depth leaves one factorial-line parameter. Together with monomial drift, every normalized term has the universal form

\[
\exp(px+nH(x)),
\qquad H\text{ even}.
\]

The Part XVI five-jet classification therefore survives unchanged. The new binary endpoint arithmetic reduces potential rank loss to:

- nonintegral centered norms;
- curvature numerators larger than the available norm radius;
- one parity-impossible endpoint pair;
- or one of two exact cosh identities.

No independent three-dimensional span can vanish through order four. The explicit circuit

\[
(q;q)_2
\left(
1+rac{(1-q)^2}{2q}+rac{(1-q)^4}{16q^2}
\right)
=
\frac{(q-1)^2(q+1)^5}{16q^2}
\]

attains excess four.

Hence

\[
\boxed{C^{\mathrm{cd}}_2(3,2)=4.}
\]

Together with Part XVI, the first higher-rank two-endpoint box is now solved at both real cyclotomic contexts:

\[
\boxed{
C^{\mathrm{cd}}_1(3,2)
=
C^{\mathrm{cd}}_2(3,2)
=4.
}
\]

The next structural frontier is not \(d=4\), nor “all even \(d\).” It is the first chiral context

\[
\boxed{d=3.}
\]

---

## End of Part XVII
