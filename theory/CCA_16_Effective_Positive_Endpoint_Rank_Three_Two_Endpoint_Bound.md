# Cyclotomic Coefficient Arithmetic

## Part XVI — Effective Positive-Endpoint Rank-Three Two-Endpoint Bound and the Holonomic Obstruction

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete partial-resolution chapter  
**Scope:** The exact shift quotient of the universal normalized factorial germ, the failure of a fixed-order holonomic differential reduction, common-depth three-term circuits with two factorial endpoints at the positive context, a five-jet rank theorem, exact endpoint arithmetic, the sharp formula

\[
\boxed{C^{\mathrm{cd}}_1(3,2)=4,}
\]

exact verification code, and the remaining higher-context and unequal-depth problems.

---

# 0. Purpose, relation to Parts XII–XIII, and exact status

Part XII proved a uniform local multiplicity theorem for compressed factorial circuits. For every fixed cyclotomic order \(d\), top fan-in \(m\), and endpoint complexity \(S\), there is a finite constant

\[
C_d(m,S)<\infty
\]

controlling the residual Wronskian multiplicity and hence the local contact order of every nonzero circuit.

The proof is Noetherian. It establishes finiteness but does not provide a numerical formula.

Part XIII solved the first boundary regimes at the positive endpoint \(q=1\):

\[
C^{\mathrm{cd}}_1(2,S)=\gamma(S),
\qquad
C^{\mathrm{cd}}_1(m,S)=m-1\quad(S\le1),
\]

where

\[
\gamma(S)=
\begin{cases}
1,&S\le1,\\[1mm]
2S-2,&S\ge2.
\end{cases}
\]

It left open the first genuinely higher-rank box

\[
\boxed{m=3,\qquad S=2.}
\]

The corrected conjecture predicts

\[
C^{\mathrm{cd}}_1(3,2)
=(3-1)(2\cdot2-2)=4.
\]

This chapter proves that prediction.

The proof has two logically separate parts.

1. The proposed holonomic route is examined exactly. The normalized factorial germ has a simple mixed shift ratio in the quotient parameter \(R\), but it has no parameter-uniform finite-order differential annihilator in the local variable \(x\). Consequently, the requested closure-under-determinant estimate cannot be obtained by assigning one fixed D-finite order to each endpoint factor.

2. The actual smallest open case is solved by exploiting the special geometry of two endpoints at \(q=1\). Common depth forces all factorial exponent vectors onto one affine lattice line. The remaining monomial drift contributes a second direction. A complete classification of the first five jets shows that three independent terms are always distinguished by order four.

The principal theorem is

\[
\boxed{
C^{\mathrm{cd}}_1(3,2)=4.
}
\]

This statement is exact and sharp.

The chapter does **not** prove:

- an explicit value of the full unequal-depth constant \(C_1(3,2)\) from Part XII;
- an explicit value of \(C_d(3,2)\) for \(d\ge2\);
- a bit-polynomial identity test for arbitrary three-term two-endpoint circuits, because compact exact addition of enormous residual constants remains a separate arithmetic issue.

The labels used below are:

- **Classical lemma:** standard input, proved here;
- **Project theorem:** a theorem established in this chapter;
- **Algorithmic theorem:** an exact computational consequence;
- **Obstruction theorem:** a proof that a proposed method cannot supply the desired uniform parameter;
- **Sharpness statement:** an example attaining the upper bound;
- **Caution:** a boundary that must not be blurred.

Throughout,

\[
q=e^x
\]

at the positive endpoint, so that

\[
D=q\frac d{dq}=\frac d{dx}.
\]

All arithmetic is exact.

---

# 1. The universal normalized factorial germ and its exact shift ratio

Fix a cyclotomic order \(d\ge1\), a primitive \(d\)-th root \(\zeta\), and a residue

\[
0\le s<d.
\]

For an integer \(R\ge0\), set

\[
A=dR+s.
\]

Part XII defines the normalized factorial germ

\[
\mathcal U_{d,s}(R;x)
=
\frac{x^{-R}(q;q)_{dR+s}|_{q=\zeta e^x}}
{B_{d,s}(R)},
\qquad
\mathcal U_{d,s}(R;0)=1,
\]

where

\[
B_{d,s}(R)
=
\lim_{x\to0}
 x^{-R}(q;q)_{dR+s}|_{q=\zeta e^x}.
\]

Define

\[
A_s(\zeta)=\prod_{u=1}^{s}(1-\zeta^u),
\qquad
A_0(\zeta)=1.
\]

## Proposition 1.1 — Exact leading residual

For every \(R\ge0\),

\[
\boxed{
B_{d,s}(R)
=
(-1)^R d^{2R}R!\,A_s(\zeta).
}
\]

### Proof

The multiples of \(d\) among \(1,\ldots,dR+s\) are

\[
d,2d,\ldots,Rd.
\]

At \(q=\zeta e^x\), their leading product is

\[
\prod_{j=1}^{R}(1-e^{djx})
=
(-d)^R R!\,x^R+O(x^{R+1}).
\]

Every complete block of nonzero residues contributes

\[
\prod_{u=1}^{d-1}(1-\zeta^u)=d.
\]

There are \(R\) complete nonzero-residue blocks, followed by the terminal product \(A_s(\zeta)\). Hence the nonvanishing channels contribute

\[
d^R A_s(\zeta).
\]

Multiplying gives

\[
(-d)^RR!\,d^R A_s(\zeta)
=
(-1)^Rd^{2R}R!A_s(\zeta).
\]

∎

## Project Theorem 1.2 — Exact quotient shift

For every \(R\ge0\),

\[
\boxed{
\frac{\mathcal U_{d,s}(R+1;x)}
{\mathcal U_{d,s}(R;x)}
=
-rac1{d^2(R+1)x}
\prod_{u=1}^{d}
\left(
1-\zeta^{s+u}e^{(dR+s+u)x}
\right).
}
\]

### Proof

The quotient of the unnormalized factorials is one block of length \(d\):

\[
\frac{(q;q)_{d(R+1)+s}}
{(q;q)_{dR+s}}
=
\prod_{u=1}^{d}
(1-q^{dR+s+u}).
\]

The power \(x^{-R}\) contributes one additional factor \(x^{-1}\), while Proposition 1.1 gives

\[
\frac{B_{d,s}(R)}{B_{d,s}(R+1)}
=
-rac1{d^2(R+1)}.
\]

Substitute \(q=\zeta e^x\). ∎

## Corollary 1.3 — Mixed hypergeometric form

Let

\[
Q=e^{dx},
\qquad
Y=Q^R.
\]

Then the shift quotient is

\[
-rac1{d^2(R+1)x}
\prod_{u=1}^{d}
\left(1-c_u(x)Y\right),
\]

where

\[
c_u(x)=\zeta^{s+u}e^{(s+u)x}.
\]

Thus the quotient is a degree-\(d\) polynomial in \(Q^R\), divided by \((R+1)x\). In the quotient parameter \(R\), the normalized germ is a mixed ordinary/\(q\)-hypergeometric term.

### Caution 1.4 — What this does not imply

A first-order shift recurrence in \(R\) does not imply a finite-order differential equation in \(x\) whose order is independent of \(R\).

The Noetherian multiplicity problem concerns the first nonzero coefficient in the \(x\)-series after arbitrary parameter specialization. A recurrence transporting the value from \(R\) to \(R+1\) does not by itself bound that coefficient index.

---

# 2. Why the proposed fixed-order holonomic route stalls

The standard holonomic closure theorems require a finite annihilating rank for the input functions in the variable in which the Wronskian is formed. Here that variable is \(x\).

Already the simplest specialization has unbounded differential order.

Set

\[
d=1,
\qquad
s=0,
\qquad
\zeta=1.
\]

Then Proposition 1.1 gives

\[
B_{1,0}(R)=(-1)^RR!,
\]

and therefore

\[
\boxed{
\mathcal U_{1,0}(R;x)
=
\prod_{n=1}^{R}
\frac{e^{nx}-1}{nx}.
}
\]

Define

\[
P_R(z)=\prod_{n=1}^{R}(z^n-1).
\]

Then

\[
\mathcal U_{1,0}(R;x)
=
\frac{P_R(e^x)}{R!x^R}.
\]

## Classical Lemma 2.1 — Exponential independence over rational functions

Let

\[
\lambda_1,\ldots,\lambda_t
\]

be distinct constants. Then

\[
e^{\lambda_1x},\ldots,e^{\lambda_tx}
\]

are linearly independent over \(\mathbb C(x)\).

### Proof

Suppose a nontrivial relation of minimal length exists:

\[
\sum_{j=1}^{t}r_j(x)e^{\lambda_jx}=0,
\qquad
r_j(x)\in\mathbb C(x).
\]

Clear denominators so that the \(r_j\) are polynomials. Divide by one exponential and differentiate enough times to eliminate one term by the usual minimal-relation argument. More explicitly, after dividing by \(e^{\lambda_tx}\), apply the operator

\[
\frac d{dx}-\frac{r_t'}{r_t}
\]

where \(r_t\ne0\). The last term vanishes, while every surviving exponential still has a distinct exponent. This produces a shorter nontrivial rational-function relation, contradicting minimality. ∎

## Lemma 2.2 — Sparse support lower bound

Let \(t_R\) be the number of nonzero monomials of \(P_R(z)\). Then

\[
\boxed{t_R\ge R+1.}
\]

### Proof

The polynomial \(P_R\) has a zero of multiplicity exactly \(R\) at \(z=1\), because every factor \(z^n-1\) has a simple zero there.

A nonzero Laurent polynomial with \(t\) monomials has multiplicity at most \(t-1\) at any nonzero point, by the sparse Vandermonde theorem of Part XI. Hence

\[
R\le t_R-1.
\]

∎

## Obstruction Theorem 2.3 — No uniform finite differential order

There is no nonzero differential operator

\[
L(R,x,\partial_x)
=
\sum_{j=0}^{r}a_j(R,x)\partial_x^j,
\qquad
a_j\in\mathbb C(R,x),
\]

of fixed finite order \(r\), such that

\[
L(R,x,\partial_x)\mathcal U_{1,0}(R;x)=0
\]

for every nonnegative integer \(R\) outside a finite exceptional set.

### Proof

For a fixed \(R\), write

\[
P_R(e^x)=
\sum_{k\in E_R}c_ke^{kx},
\qquad
c_k\ne0,
\qquad
|E_R|=t_R.
\]

By Lemma 2.1, the exponentials \(e^{kx}\), \(k\in E_R\), are linearly independent over \(\mathbb C(x)\). Therefore the derivatives of \(P_R(e^x)\) span a \(t_R\)-dimensional cyclic differential space, and every scalar differential annihilator over \(\mathbb C(x)\) has order at least \(t_R\).

Multiplication by the nonzero rational function \(1/(R!x^R)\) is a gauge transformation and does not reduce the minimal differential order over \(\mathbb C(x)\). Thus every annihilator of \(\mathcal U_{1,0}(R;x)\) has order at least

\[
t_R\ge R+1
\]

by Lemma 2.2.

If a fixed-order operator \(L\) existed, then after specializing \(R\) away from the finitely many poles and zeros of its leading coefficient, it would give an annihilator of order at most \(r\). Choosing \(R>r\) yields a contradiction. ∎

## Corollary 2.4 — Failure of the proposed determinant-order propagation

The endpoint unit \(\mathcal U_{d,s}(R;x)\) cannot be assigned an \(x\)-differential order bounded only by \(d\). Consequently, multiplying \(S\) endpoint units and expanding a residual determinant cannot produce a parameter-uniform Wronskian order merely by standard D-finite closure estimates.

### Interpretation 2.5

Creative telescoping is designed to eliminate a summation or integration variable from a holonomic or proper hypergeometric input. The present factorial germ is indeed hypergeometric in the discrete quotient parameter \(R\), but the desired multiplicity is measured in the independent local variable \(x\).

The shift relation of Theorem 1.2 is useful computational structure. It is not the missing Bautin bound.

The obstruction is not a weakness of a particular package. It is a mismatch between:

\[
\boxed{
\text{first-order transport in }R
}
\]

and

\[
\boxed{
\text{uniform first-visible coefficient in }x.
}
\]

---

# 3. The smallest open case at the positive endpoint

We now specialize to

\[
d=1,
\qquad
m=3,
\qquad
S=2.
\]

Fix two positive endpoints

\[
0<a<b.
\]

Consider a common-depth circuit

\[
F(q)
=
\sum_{i=1}^{r}
 c_iq^{\alpha_i}
 (q;q)_a^{u_i}
 (q;q)_b^{v_i},
\qquad
1\le r\le3,
\]

with

\[
au_i+bv_i=h
\]

for every \(i\).

Let

\[
g=\gcd(a,b).
\]

## Lemma 3.1 — Primitive two-endpoint direction

For every pair of terms,

\[
(u_i-u_1,v_i-v_1)
=
 n_i\left(\frac bg,-\frac ag\right)
\]

for some integer \(n_i\).

### Proof

The depth equation gives

\[
a(u_i-u_1)+b(v_i-v_1)=0.
\]

The primitive integer kernel of the row vector \((a,b)\) is generated by

\[
\left(\frac bg,-\frac ag\right).
\]

∎

Define the primitive zero-depth ratio

\[
\boxed{
R(q)
=
(q;q)_a^{b/g}
(q;q)_b^{-a/g}.
}
\]

It satisfies

\[
v_{q-1}(R)=0.
\]

Choose one term as a base. Lemma 3.1 gives

\[
F(q)
=
T_0(q)
\sum_{i=1}^{r}d_iq^{\beta_i}R(q)^{n_i}
\]

for nonzero rational \(d_i\) and integers \(\beta_i,n_i\).

The base factor \(T_0\) contributes only the common depth. Therefore the excess contact is the order of

\[
G(q)=\sum_{i=1}^{r}d_iq^{\beta_i}R(q)^{n_i}.
\]

Let

\[
B=R(1)
e0,
\qquad
Z(q)=\frac{R(q)}B.
\]

Absorb \(B^{n_i}\) into the outer coefficients. It is enough to study

\[
\boxed{
G(q)=\sum_{i=1}^{r}c_iq^{\beta_i}Z(q)^{n_i}.
}
\]

---

# 4. The exact two-endpoint logarithmic germ

Use \(q=e^x\). Part XIII gives

\[
\log Z(e^x)
=
\lambda x+H(x),
\]

where \(H\) is even and has zero constant term.

Define

\[
S_k(N)=\sum_{j=1}^{N}j^k.
\]

Set

\[
M_k
=
\frac bgS_k(a)-\frac agS_k(b).
\]

Then

\[
\boxed{
\lambda=\frac{M_1}{2},
}
\]

and

\[
\boxed{
H(x)
=
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}
M_{2r}x^{2r}.
}
\]

Define

\[
C=H''(0),
\qquad
D=H^{(4)}(0).
\]

## Proposition 4.1 — The first two even derivatives

One has

\[
\boxed{
C=\frac{M_2}{12},
\qquad
D=-\frac{M_4}{120}.
}
\]

Moreover,

\[
\boxed{C<0,\qquad D>0.}
\]

### Proof

The formulas follow from

\[
B_2=\frac16,
\qquad
B_4=-\frac1{30}.
\]

The exact moment factorizations below show that both \(M_2\) and \(M_4\) have the sign of \(a-b\), hence are negative. ∎

## Proposition 4.2 — Closed endpoint formulas

Let

\[
L=2a+2b+3
\]

and

\[
\begin{aligned}
P(a,b)={}&
6a^3+6a^2b+15a^2
+6ab^2+15ab+10a\\
&+6b^3+15b^2+10b.
\end{aligned}
\]

Then

\[
\boxed{
M_2
=
\frac{ab(a-b)L}{6g},
}
\]

and

\[
\boxed{
M_4
=
\frac{ab(a-b)P(a,b)}{30g}.
}
\]

Consequently,

\[
\boxed{
|C|
=
\frac{ab(b-a)L}{72g},
}
\]

and

\[
\boxed{
-\frac DC
=
\frac{M_4}{10M_2}
=
\frac{P(a,b)}{50L}.
}
\]

### Proof

Use the classical formulas

\[
S_2(N)=\frac{N(N+1)(2N+1)}6
\]

and

\[
S_4(N)
=
\frac{N(N+1)(2N+1)(3N^2+3N-1)}{30}.
\]

Substitute into

\[
M_k=\frac bgS_k(a)-\frac agS_k(b)
\]

and factor. ∎

## Corollary 4.3 — Exact quadratic visibility

\[
\boxed{C\ne0.}
\]

Thus the even germ \(H\) has exact order two.

This is the two-endpoint instance of the strict cumulative-moment rigidity theorem from Part XIII.

---

# 5. Five jets of one normalized term

For an integer pair \((\beta,n)\), define

\[
p=\beta+n\lambda.
\]

Then

\[
q^\beta Z(q)^n\big|_{q=e^x}
=
\exp\bigl(px+nH(x)\bigr).
\]

Write

\[
f_{p,n}(x)=\exp\bigl(px+nH(x)\bigr).
\]

Because \(H\) is even,

\[
H'(0)=H^{(3)}(0)=0.
\]

## Lemma 5.1 — Exact first five derivatives

The derivatives of \(f_{p,n}\) at zero are

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

Apply the complete Bell-polynomial formulas to the exponent

\[
px+nH(x).
\]

At zero, its first four derivatives are

\[
p,
\quad nC,
\quad0,
\quad nD.
\]

Substitution gives the displayed expressions. ∎

Define the five-jet column

\[
\boxed{
J(p,n)=
\begin{pmatrix}
1\\
p\\
p^2+nC\\
p^3+3pnC\\
p^4+6p^2nC+3n^2C^2+nD
\end{pmatrix}.
}
\]

A nonzero three-term combination can have order at least five only if the three columns \(J(p_i,n_i)\) are linearly dependent.

---

# 6. Classification of five-jet dependence

## Project Lemma 6.1 — Repeated drift values are already separated

Let \((p_i,n_i)\), \(1\le i\le3\), be distinct pairs.

1. If all \(p_i\) are equal, then the three five-jet columns are independent.
2. If exactly two of the \(p_i\) are equal, then the three five-jet columns are independent.

### Proof

Suppose first that

\[
p_1=p_2=p_3=p.
\]

Distinctness of the pairs forces \(n_1,n_2,n_3\) to be distinct.

Use derivative rows \(0,2,4\). Subtract \(p^2\) times row zero from row two, obtaining

\[
Cn_i.
\]

From row four subtract its constant and linear-in-\(n_i\) parts using rows zero and two. The remaining row is

\[
3C^2n_i^2.
\]

The resulting determinant is a nonzero scalar times

\[
\det
\begin{pmatrix}
1&1&1\\
n_1&n_2&n_3\\
n_1^2&n_2^2&n_3^2
\end{pmatrix},
\]

which is nonzero because the \(n_i\) are distinct and \(C\ne0\).

Now suppose

\[
p_1=p_2\ne p_3.
\]

Then \(n_1\ne n_2\). The determinant of rows \(0,1,2\) is, up to sign,

\[
C(n_2-n_1)(p_3-p_1),
\]

which is nonzero. ∎

Hence five-jet dependence can occur only when

\[
p_1,p_2,p_3
\]

are pairwise distinct.

## Project Lemma 6.2 — Necessary centered-square equations

Assume \(p_1,p_2,p_3\) are pairwise distinct and the columns

\[
J(p_1,n_1),J(p_2,n_2),J(p_3,n_3)
\]

are linearly dependent.

Put

\[
\sigma_1=p_1+p_2+p_3,
\qquad
t=\frac{\sigma_1}{3},
\qquad
x_i=p_i-t.
\]

Then

\[
\boxed{x_1+x_2+x_3=0,}
\]

and there is a constant \(N\) such that

\[
\boxed{
n_i=N-\frac{x_i^2}{C}.
}
\]

Moreover,

\[
\boxed{
\sum_{i=1}^{3}x_i^2
=-\frac DC.
}
\]

### Proof

Rows zero and one are independent because the \(p_i\) are distinct. Dependence of all five rows implies that row two is affine in \(p_i\). Thus there are constants \(A,B\) satisfying

\[
p_i^2+Cn_i=Ap_i+B.
\]

Equivalently,

\[
Cn_i=-p_i^2+Ap_i+B.
\tag{6.1}
\]

Row three becomes

\[
\begin{aligned}
p_i^3+3p_iCn_i
&=p_i^3+3p_i(-p_i^2+Ap_i+B)\\
&=-2p_i^3+3Ap_i^2+3Bp_i.
\end{aligned}
\]

Its values at \(p_1,p_2,p_3\) must also be affine in \(p_i\). Therefore the cubic above differs from an affine polynomial by

\[
-2\prod_{i=1}^{3}(p-p_i).
\]

Comparing the coefficient of \(p^2\) gives

\[
3A=2\sigma_1.
\]

Hence

\[
A=2t.
\]

Substitute \(p_i=t+x_i\) into (6.1):

\[
Cn_i
=-(t+x_i)^2+2t(t+x_i)+B
=t^2-x_i^2+B.
\]

Thus

\[
n_i=N-\frac{x_i^2}{C},
\qquad
N=\frac{t^2+B}{C}.
\]

It remains to use row four. Substitute (6.1) into its expression from Lemma 5.1. Writing

\[
r=\frac DC,
\]

the result is the quartic polynomial

\[
-2p^4+(3A^2-r)p^2+(6AB+Ar)p+(3B^2+Br).
\]

Its values at the three \(p_i\) must be affine. Hence, after subtracting an affine polynomial, it is divisible by

\[
\prod_{i=1}^{3}(p-p_i).
\]

The quotient has leading term \(-2p\). Comparing the \(p^2\)-coefficient gives

\[
3A^2-r=2(\sigma_1^2-\sigma_2),
\]

where

\[
\sigma_2=p_1p_2+p_1p_3+p_2p_3.
\]

Using \(A=2\sigma_1/3\), this simplifies to

\[
r
=2\sigma_2-\frac23\sigma_1^2.
\]

But

\[
\sum_i x_i^2
=
\sum_i p_i^2-\frac13\sigma_1^2
=
-2\sigma_2+\frac23\sigma_1^2.
\]

Therefore

\[
\sum_i x_i^2=-r=-\frac DC.
\]

∎

### Interpretation 6.3

Five-jet dependence forces the three lattice points \((p_i,n_i)\) onto a centered parabola

\[
n=N-\frac{(p-t)^2}{C}
\]

and fixes the total centered square radius to the endpoint-dependent number

\[
-\frac DC.
\]

The remainder of the proof is arithmetic: for almost every endpoint pair, the vertical lattice spacing is too coarse to fit three such points.

---

# 7. The endpoint arithmetic inequality

Set

\[
T(a,b)=-\frac DC=\frac{P(a,b)}{50(2a+2b+3)}.
\]

This is positive.

## Project Lemma 7.1 — Coarse spacing dominates the radius

For all integers

\[
0<a<b,
\]

except

\[
(a,b)=(1,2)
\quad\text{and}\quad
(a,b)=(2,3),
\]

one has

\[
\boxed{|C|>T(a,b).}
\]

### Proof

Put

\[
r=b-a,
\qquad
L=2a+2b+3.
\]

Since

\[
g=\gcd(a,b)=\gcd(a,r)\le\min(a,r),
\]

we have

\[
\frac{abr}{g}
\ge
b\max(a,r).
\]

Therefore

\[
|C|
=
\frac{abrL}{72g}
\ge
\frac{b\max(a,r)L}{72}.
\]

It is enough to prove

\[
25b\max(a,r)L^2>36P(a,a+r).
\tag{7.1}
\]

We split into two cases.

### Case 1: \(r\ge a\)

Define

\[
\Psi(a,r)
=25brL^2-36P(a,a+r).
\]

A direct expansion gives

\[
\Psi(a,a)
=
90a(2a+1)(10a^2-13a-12).
\]

For \(a\ge2\), this is positive.

Furthermore,

\[
\frac{\partial^3\Psi}{\partial r^3}
=24(125a+100r+21)>0.
\]

At \(r=a\),

\[
\frac{\partial^2\Psi}{\partial r^2}
=2(2900a^2+288a-315)>0
\]

and

\[
\frac{\partial\Psi}{\partial r}
=3(1300a^3-124a^2-675a-120)>0.
\]

Thus \(\Psi(a,r)\) is strictly increasing for \(r\ge a\).

When \(a=1\), the value \(r=1\) is the exceptional pair \((1,2)\), while

\[
\Psi(1,2)=1050>0.
\]

Monotonicity handles every \(r\ge2\).

### Case 2: \(r<a\)

Define

\[
\Phi(a,r)
=25abL^2-36P(a,a+r).
\]

For fixed \(r\ge1\), its third derivative in \(a\) is

\[
\frac{\partial^3\Phi}{\partial a^3}
=48(200a+100r-33)>0.
\]

At the smallest allowed value \(a=r+1\),

\[
\frac{\partial^2\Phi}{\partial a^2}
=2(5300r^2+6012r+213)>0
\]

and

\[
\frac{\partial\Phi}{\partial a}
=5100r^3+8452r^2+639r-2702>0.
\]

The final inequality holds for every \(r\ge1\): at \(r=1\) its value is \(11489\), and its derivative in \(r\) is positive. Hence \(\Phi(a,r)\) is increasing for \(a\ge r+1\).

At that boundary,

\[
\Phi(r+1,r)
=
1800r^4+3660r^3-178r^2-4053r-1979.
\]

Its second derivative is

\[
4(5400r^2+5490r-89)>0
\qquad(r\ge1),
\]

and its first derivative at \(r=1\) is positive. Therefore it is increasing for \(r\ge1\).

The value at \(r=1\) is negative and corresponds to \((a,b)=(2,3)\). The next value is

\[
\Phi(3,2)=47283>0.
\]

Thus (7.1) holds in every remaining case. ∎

## Corollary 7.2 — Generic five-jet independence

For every endpoint pair other than \((1,2)\) and \((2,3)\), three distinct parameter pairs \((p_i,n_i)\) have independent five-jet columns.

### Proof

Assume dependence. Lemma 6.2 gives

\[
\sum_i x_i^2=T(a,b)
\]

and

\[
n_i-n_j=-\frac{x_i^2-x_j^2}{C}.
\]

Since

\[
|x_i^2-x_j^2|
\le
\sum_kx_k^2
=T(a,b)
<|C|,
\]

and \(n_i-n_j\) is an integer, it follows that

\[
n_i=n_j
\]

for every pair.

With common \(n\) and distinct \(p_i\), the determinant of rows \(0,1,2\) is the ordinary Vandermonde determinant in the \(p_i\), hence is nonzero. Contradiction. ∎

---

# 8. The two exceptional endpoint pairs

## 8.1 The pair \((2,3)\)

For \((a,b)=(2,3)\), one computes

\[
\lambda=-\frac32,
\qquad
C=-\frac{13}{12},
\qquad
T=-\frac DC=\frac{29}{26}.
\]

Because

\[
p_i=\beta_i+n_i\lambda,
\qquad
\beta_i,n_i\in\mathbb Z,
\]

we have

\[
y_i=2p_i\in\mathbb Z.
\]

Define

\[
z_i=3y_i-(y_1+y_2+y_3).
\]

Then

\[
x_i=\frac{z_i}{6}.
\]

If five-jet dependence occurred, Lemma 6.2 would give

\[
\sum_i z_i^2
=36\sum_i x_i^2
=36\cdot\frac{29}{26}
=\frac{522}{13},
\]

which is not an integer. This is impossible because every \(z_i\) is an integer.

Hence the five-jet columns are independent for \((2,3)\).

## 8.2 The pair \((1,2)\)

For \((a,b)=(1,2)\),

\[
\lambda=-\frac12,
\qquad
C=-\frac14,
\qquad
T=\frac12.
\]

Again

\[
y_i=2p_i\in\mathbb Z
\]

and

\[
x_i=\frac{z_i}{6},
\qquad
z_i=3y_i-(y_1+y_2+y_3).
\]

Five-jet dependence would force

\[
\sum_i z_i^2
=36\cdot\frac12
=18
\]

and

\[
z_1+z_2+z_3=0.
\]

The only integer solutions are permutations of

\[
(-3,0,3).
\]

Indeed, the only decompositions of \(18\) into three squares are

\[
9+9+0
\quad\text{and}\quad
16+1+1,
\]

and the second cannot have signed sum zero.

Thus, after relabeling,

\[
(x_1,x_2,x_3)
=
\left(-\frac12,0,\frac12\right).
\]

Lemma 6.2 gives

\[
n_i=N+4x_i^2,
\]

so the three \(n\)-values are

\[
N+1,N,N+1.
\]

The lattice condition

\[
\beta_i=p_i+\frac{n_i}{2}\in\mathbb Z
\]

then shows that, after factoring one common term, the three germs are

\[
e^{-x/2+H(x)},
\qquad
1,
\qquad
e^{x/2+H(x)}.
\]

For these endpoints,

\[
R(q)=\frac{(q;q)_1^2}{(q;q)_2}
=\frac1{1+q},
\qquad
B=\frac12.
\]

Hence

\[
Z(e^x)=\frac2{1+e^x}
=\frac{e^{-x/2}}{\cosh(x/2)},
\]

so

\[
H(x)=-\log\cosh(x/2).
\]

Therefore

\[
\begin{aligned}
e^{-x/2+H(x)}+e^{x/2+H(x)}
&=2e^{H(x)}\cosh(x/2)\\
&=2.
\end{aligned}
\]

Thus the only possible five-jet dependence is an **exact functional dependence**.

It cannot produce a nonzero circuit of order at least five.

---

# 9. The sharp rank-three two-endpoint theorem

## Project Theorem 9.1 — Five jets determine the three-term span

Let

\[
0<a<b
\]

and let

\[
f_i(x)=\exp(p_ix+n_iH(x)),
\qquad
1\le i\le r\le3,
\]

arise from normalized common-depth two-endpoint factorial terms as above.

Then the map

\[
\operatorname{span}\{f_1,\ldots,f_r\}
\longrightarrow
K^5,
\qquad
f\longmapsto
\bigl(f(0),f'(0),\ldots,f^{(4)}(0)\bigr),
\]

is injective.

### Proof

Combine proportional terms first.

If the actual span has dimension at most two, Part XIII's sharp two-term theorem gives excess contact at most

\[
\gamma(2)=2,
\]

and injectivity through order four follows.

Suppose the span has dimension three. If the five-jet columns were dependent, Lemmas 6.1 and 6.2 would apply.

- Generic endpoint pairs are excluded by Corollary 7.2.
- The pair \((2,3)\) is excluded by the integrality contradiction of Section 8.1.
- For \((1,2)\), Section 8.2 shows that five-jet dependence forces exact linear dependence, contradicting the assumed three-dimensional span.

Thus the five-jet columns are independent. ∎

## Project Theorem 9.2 — Effective rank-three two-endpoint bound

Let

\[
F(q)
=
\sum_{i=1}^{r}
 c_iq^{\alpha_i}
 (q;q)_a^{u_i}
 (q;q)_b^{v_i},
\qquad
1\le r\le3,
\]

be a common-depth circuit at \(q=1\):

\[
au_i+bv_i=h
\]

for every \(i\).

If \(F\not\equiv0\), then

\[
\boxed{
\operatorname{ord}_{q=1}F
\le h+4.
}
\]

Equivalently,

\[
\boxed{
C^{\mathrm{cd}}_1(3,2)\le4.
}
\]

### Proof

Factor a base term as in Section 3. The remaining normalized sum is a linear combination of at most three functions

\[
f_i(x)=e^{p_ix+n_iH(x)}.
\]

By Theorem 9.1, a nonzero element of their span has a nonzero derivative of order at most four. Multiplication by the base term restores the common depth \(h\). ∎

## Sharpness Theorem 9.3 — Exact capacity

\[
\boxed{
C^{\mathrm{cd}}_1(3,2)=4.
}
\]

### Proof

The upper bound is Theorem 9.2.

For the lower bound, take

\[
X(q)=\frac{q}{(1+q)^2}
=
q\frac{(q;q)_1^4}{(q;q)_2^2}.
\]

This uses exactly two factorial endpoints and has depth zero. Moreover,

\[
4X(q)-1
=-\frac{(q-1)^2}{(q+1)^2}.
\]

Therefore the three-term circuit

\[
(4X(q)-1)^2
=16X(q)^2-8X(q)+1
\]

has exact order four:

\[
\boxed{
(4X(q)-1)^2
=
\frac{(q-1)^4}{(q+1)^4}.
}
\]

Thus no bound below four is possible. ∎

## Corollary 9.4 — The corrected conjecture in the first open box

Part XIII's conjectural formula

\[
C^{\mathrm{cd}}_1(m,S)
=(m-1)\gamma(S)
\]

is now proved for

\[
(m,S)=(3,2).
\]

---

# 10. Exact certificate and computation theorem

## Algorithmic Theorem 10.1 — Five-coefficient identity certificate

Under the hypotheses of Theorem 9.2,

\[
F\equiv0
\]

if and only if the five regularized coefficients

\[
[x^{h+j}]F(e^x)
\qquad
(0\le j\le4)
\]

all vanish.

### Proof

Identity implies vanishing of every coefficient.

Conversely, if the five displayed coefficients vanish and \(F\ne0\), then

\[
\operatorname{ord}_{q=1}F\ge h+5,
\]

contradicting Theorem 9.2. ∎

## Algorithm 10.2 — Exact compressed five-jet computation

For each input term:

1. compute its common depth
   \[
   h=au_i+bv_i;
   \]
2. compute its exact leading residual
   \[
   (-1)^h(a!)^{u_i}(b!)^{v_i};
   \]
3. compute the logarithmic coefficients through order four using
   \[
   \lambda_i
   =\alpha_i+\frac12\bigl(u_iS_1(a)+v_iS_1(b)\bigr),
   \]
   \[
   \ell_{i,2}
   =\frac{B_2}{2\cdot2!}
   \bigl(u_iS_2(a)+v_iS_2(b)\bigr),
   \]
   and
   \[
   \ell_{i,4}
   =\frac{B_4}{4\cdot4!}
   \bigl(u_iS_4(a)+v_iS_4(b)\bigr);
   \]
4. reconstruct ordinary coefficients through order four by the exponential Bell recurrence;
5. multiply by the leading residual and outer coefficient;
6. add the three exact coefficient vectors.

Every operation is rational or integer arithmetic. No root approximation and no floating point arithmetic is required.

### Caution 10.3 — Multiplicity effectiveness is not yet bit-polynomial PIT

The jet count is now constant: five coefficients suffice.

However, the leading residuals may contain integers such as

\[
(a!)^{u_i}(b!)^{v_i}
\]

whose expanded bit length is enormous compared with the compressed input. Exact zero testing of a sum of such compact constants is a separate arithmetic problem.

Therefore Theorem 9.2 solves the **multiplicity obstacle** for \((d,m,S)=(1,3,2)\) in the common-depth regime. It does not, by itself, solve the compact-arithmetic obstacle identified in Part XIII.

---

# 11. Exact computational verification

The accompanying script

```text
src/ccat/research/effective_rank3_two_endpoint.py
```

implements:

1. the shift quotient of Theorem 1.2;
2. the growing differential-order witness from Section 2;
3. exact Faulhaber sums and Bernoulli cumulants;
4. exact normalized unit series;
5. exact vanishing-sequence computation;
6. exhaustive finite-box checks;
7. randomized large-endpoint checks;
8. the sharp three-term example.

The tests use SymPy rational arithmetic only.

## Verification 11.1 — Exhaustive parameter boxes

For

\[
-3\le\beta\le3,
\qquad
-3\le n\le3,
\]

all triples were checked for the endpoint pairs

\[
(1,2),
(1,3),
(2,3),
(2,5),
(3,5),
(4,7).
\]

The maximum observed finite vanishing orders were:

| endpoints | maximum order |
|---|---:|
| \((1,2)\) | 4 |
| \((1,3)\) | 4 |
| \((2,3)\) | 4 |
| \((2,5)\) | 2 |
| \((3,5)\) | 2 |
| \((4,7)\) | 2 |

No finite order exceeded four.

## Verification 11.2 — Large endpoints

One hundred exact randomized trials were run with endpoints as large as several thousand, including

\[
(17,53),
(101,233),
(1000,1001),
(987,1597).
\]

The local coefficients were computed by Faulhaber and Bernoulli formulas, not by expanding the \(q\)-factorials. No trial exceeded order four.

## Verification 11.3 — Direct expansion and factorization of true circuits

Four concrete three-term rational circuits were constructed from their actual finite \(q\)-factorials, combined exactly, and factored over \(\mathbb Q[q]\). The coefficients were chosen from exact nullspaces of the preceding jet rows.

| endpoints | parameter pairs \((\beta,n)\) | outer coefficients | exact order | numerator cofactor at \(q=1\) | denominator at \(q=1\) |
|---|---|---|---:|---:|---:|
| \((1,3)\) | \((-3,-3),(0,-1),(3,1)\) | \((1,-2,1)\) | 4 | 1089 | 1296 |
| \((2,3)\) | \((-3,-3),(0,-1),(3,1)\) | \((1,-2,1)\) | 4 | 123201 | 104976 |
| \((2,5)\) | \((-2,-1),(1,0),(3,2)\) | \((26/9,-35/9,1)\) | 2 | 383484375000 | 3280500000 |
| \((1,2)\) | \((0,0),(1,2),(2,4)\) | \((1,-2,1)\) | 4 | 1 | 16 |

In each row, the numerator was divided exactly by the displayed power of \(q-1\); the remaining numerator cofactor and the denominator both evaluate nonzero at \(q=1\). This certifies the stated order independently of the local-series computation.

The sharp example simplifies to

\[
\frac{(q-1)^4}{(q+1)^4}.
\]

For large endpoints, direct global expansion is intentionally avoided; the exact compressed Faulhaber/Bernoulli jet computation is the relevant certificate mechanism.

## Verification 11.4 — Software tests

The supplied test suite contains six exact tests:

- special endpoint invariants;
- unbounded differential-order witness;
- exhaustive small boxes;
- randomized large endpoints;
- direct sharpness factorization;
- direct expansion and factorization of four true circuits.

All tests pass without floating point arithmetic.

---

# 12. Relation to holonomic and creative-telescoping theory

Holonomic-function packages correctly provide:

- annihilating ideals for known holonomic inputs;
- closure under addition, multiplication, and substitution;
- creative telescoping for sums and integrals;
- order-degree estimates for proper hypergeometric or \(\partial\)-finite inputs.

The present obstruction is more specific.

The family

\[
\mathcal U_{d,s}(R;x)
\]

has a compact first-order recurrence in \(R\), but the minimal scalar differential order in \(x\) grows with \(R\). Therefore the family does not supply a fixed \(x\)-holonomic rank from which a determinant closure bound depending only on \(d,m,S\) can be read.

The following references describe the relevant positive holonomic theory:

1. C. Koutschan, *Creative Telescoping for Holonomic Functions*.
2. S. Chen and M. Kauers, *Order-Degree Curves for Hypergeometric Creative Telescoping*.
3. S. Chen, M. Kauers, and C. Koutschan, *A Generalized Apagodu–Zeilberger Algorithm*.
4. M. Kauers, *Bounds for D-Finite Closure Properties*.
5. The `HolonomicFunctions` and `ore_algebra` package documentation.

Theorem 2.3 explains why those closure bounds cannot be applied in the direct manner proposed for the universal factorial unit.

This does not rule out every possible use of Ore algebra. It rules out the specific strategy

\[
\text{fixed endpoint-unit differential order}
\Longrightarrow
\text{fixed determinant differential order}
\Longrightarrow
\text{uniform Bautin index}.
\]

---

# 13. Theorem inventory

| No. | Result | Exact conclusion | Status |
|---:|---|---|---|
| 1.1 | Leading residual | \(B_{d,s}(R)=(-1)^Rd^{2R}R!A_s(\zeta)\) | Proved |
| 1.2 | Quotient shift | Exact mixed hypergeometric ratio in \(R\) | Proved |
| 2.3 | Holonomic obstruction | No fixed finite \(x\)-differential order uniform in \(R\) | Proved |
| 3.1 | Primitive endpoint direction | Common-depth exponent differences are integral multiples of one vector | Proved |
| 4.2 | Endpoint invariants | Closed formulas for \(C,D,-D/C\) | Proved |
| 5.1 | Five derivatives | Exact jet vector through order four | Proved |
| 6.2 | Dependence classification | Five-jet dependence forces a centered parabola and fixed square radius | Proved |
| 7.1 | Endpoint spacing inequality | \(|C|>-D/C\) except \((1,2),(2,3)\) | Proved |
| 8.1 | Exceptional pair \((2,3)\) | Dependence impossible by integrality | Proved |
| 8.2 | Exceptional pair \((1,2)\) | Dependence is an exact functional identity | Proved |
| 9.1 | Five-jet injectivity | First five jets determine every three-term span | Proved |
| 9.2 | Effective upper bound | Common-depth contact is at most \(h+4\) | Proved |
| 9.3 | Exact capacity | \(C^{\mathrm{cd}}_1(3,2)=4\) | Proved and sharp |
| 10.1 | Identity certificate | Five regularized coefficients suffice | Proved |

---

# 14. Boundaries of this result

## 14.1 Common depth is essential to the present reduction

The equation

\[
au_i+bv_i=h
\]

places the factorial exponent vectors on one affine line. The monomial powers \(\alpha_i\) provide the second direction handled by the five-jet theorem.

For unequal depths, the germs contain different powers \(x^{h_i}\). The full residual-Wronskian constant from Part XII is not computed here.

## 14.2 The result is at \(d=1\)

At a primitive root of order \(d\ge2\):

- endpoint quotients and residues both enter;
- odd chiral cumulants generally survive;
- the two-endpoint logarithmic germ is not constrained to one linear term plus one even function;
- the positive-endpoint parabola argument does not transfer unchanged.

Thus no formula for \(C_d(3,2)\), \(d\ge2\), is claimed.

## 14.3 The holonomic obstruction is method-specific

Theorem 2.3 rules out a uniform scalar D-finite order in \(x\). It does not prove that every conceivable symbolic-summation method must fail.

A successful higher-context method may need:

- a nonlinear differential algebra;
- a finite jet algebra rather than a full holonomic annihilator;
- direct control of coefficient ideals;
- residue-channel total positivity;
- a Grassmann-Wronskian argument adapted to the finite top fan-in.

## 14.4 Compact arithmetic remains open

The constant multiplicity bound is now explicit in this box. A genuine bit-polynomial PIT additionally requires a polynomial-time zero test for the resulting bounded sums of compact factorial residuals.

## 14.5 Higher fan-in

The theorem supports the conjectural formula

\[
C^{\mathrm{cd}}_1(m,2)=2(m-1),
\]

but proves only \(m\le3\) and the affine-line subclass for arbitrary \(m\).

The next unsolved positive-endpoint box is

\[
(m,S)=(4,2)
\]

or, independently,

\[
(m,S)=(3,3).
\]

---

# 15. Suggested next theorem

The structure of the proof suggests the following finite-jet formulation.

## Conjecture 15.1 — Two-endpoint finite-jet rank bound

Let

\[
f_i(x)=\exp(p_ix+n_iH(x)),
\]

where \(H\) is the primitive two-endpoint even germ with \(H''(0)\ne0\). Then every \(m\)-dimensional span generated by such functions is determined by its first

\[
2m-1
\]

derivatives:

\[
\boxed{
\operatorname{ord}_x f\le2m-2
}
\]

for every nonzero element of the span.

This is equivalent to

\[
\boxed{
C^{\mathrm{cd}}_1(m,2)=2m-2.
}
\]

The present chapter proves the conjecture for \(m=3\). Part XIII and the affine-line theorem prove its boundary and sharpness cases.

A plausible route for \(m=4\) is to classify the rank of the seven-jet feature map

\[
(p,n)
\longmapsto
\bigl(f^{(j)}_{p,n}(0)\bigr)_{0\le j\le6}
\]

and identify every exceptional rank drop with an exact algebraic dependence of the underlying factorial ratio.

---

# 16. Final synthesis

The universal factorial germ does possess an exact quotient recurrence:

\[
\boxed{
\frac{\mathcal U_{d,s}(R+1;x)}
{\mathcal U_{d,s}(R;x)}
=
-rac1{d^2(R+1)x}
\prod_{u=1}^{d}
\left(1-\zeta^{s+u}e^{(dR+s+u)x}\right).
}
\]

This confirms the mixed hypergeometric structure anticipated in Part XII.

But the differential order in the local variable is not bounded uniformly in \(R\). Hence standard holonomic determinant closure does not produce the missing effective Bautin index.

The smallest open case can nevertheless be solved directly. At \(q=1\), two shared endpoints reduce every common-depth three-term circuit to three functions

\[
e^{p_ix+n_iH(x)}
\]

with one even nonlinear germ \(H\). Their first five jets are independent unless the functions themselves are dependent. Therefore

\[
\boxed{
C^{\mathrm{cd}}_1(3,2)=4.
}
\]

The bound is attained by

\[
\left(\frac{4q}{(1+q)^2}-1\right)^2
=
\frac{(q-1)^4}{(q+1)^4}.
\]

Thus the first genuinely higher-rank multiplicity box is closed exactly.

What remains is now sharply separated:

\[
\boxed{
\begin{array}{c}
\text{positive-endpoint multiplicity: solved for }(3,2),\\[1mm]
\text{unequal-depth and }d\ge2\text{ multiplicity: open},\\[1mm]
\text{compact bit-polynomial jet arithmetic: open}.
\end{array}
}
\]

---

## End of Part XVI
