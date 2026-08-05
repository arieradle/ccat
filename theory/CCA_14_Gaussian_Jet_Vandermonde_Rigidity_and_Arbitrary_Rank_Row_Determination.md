# Cyclotomic Coefficient Arithmetic

## Part XIV — Gaussian Jet–Vandermonde Rigidity and Arbitrary-Rank Row Determination

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete theorem chapter  
**Scope:** Positive-endpoint Gaussian local germs, collapse to the spectral coordinate $E=k(n-k)$, the polynomial-cumulant Jet–Vandermonde principle, an exact Gaussian Wronskian determinant, sharp arbitrary-rank contact bounds, explicit extremizers, complete osculating filtrations, one-point reconstruction, stable-content reduction, and degree-free identity certificates for Gaussian-row circuits.

---

# 0. Purpose, dependencies, and the new theorem

Part II determined the exact cyclotomic content and spacing geometry of stable Gaussian blocks. In particular, it proved

$$
\Delta_{n,t}(q)
=
q^{t+1}
\prod_{d=n-t+1}^{n}\Phi_d(q)
$$

in the stable range

$$
t\ge5,
\qquad
n\ge3t-2.
$$

Part XIII studied local multiplicity of compressed factorial circuits at the positive endpoint

$$
q=1.
$$

It proved sharp arbitrary-rank contact capacity when the full circuit uses at most one factorial endpoint, and sharp two-term capacity for arbitrary endpoint complexity. The genuinely higher-rank, multi-endpoint factorial-circuit problem remained open.

A Gaussian row lies beyond the one-endpoint regime. Its members are

$$
{n\brack k}_q
=
\frac{(q;q)_n}{(q;q)_k(q;q)_{n-k}},
$$

so a collection of many row entries may involve many distinct factorial endpoints. Nevertheless, the row has an additional structure that is invisible to a general endpoint count.

For fixed $n$, define the Gaussian degree coordinate

$$
\boxed{
E_n(k)=k(n-k).
}
$$

After normalization by the ordinary binomial value at $q=1$, the entire positive-endpoint germ of ${n\brack k}_q$ depends on $k$ only through $E_n(k)$. More strongly, its $r$-th Euler jet is a polynomial of exact degree $r$ in $E_n(k)$, with leading coefficient $2^{-r}$.

This produces an exact Vandermonde determinant.

Let

$$
0\le k_1<\cdots<k_m\le\left\lfloor\frac n2\right\rfloor,
\qquad
E_i=k_i(n-k_i),
$$

and put

$$
G_i(q)={n\brack k_i}_q,
\qquad
D=q\frac d{dq}.
$$

The main theorem is

$$
\boxed{
\det\left(D^rG_i(1)\right)_{
\substack{0\le r\le m-1\\1\le i\le m}}
=
2^{-\binom m2}
\left(\prod_{i=1}^{m}\binom n{k_i}\right)
\prod_{1\le i<j\le m}(E_j-E_i).
}
$$

Since

$$
E_j-E_i
=
(k_j-k_i)(n-k_i-k_j),
$$

this is equivalently

$$
\boxed{
\det\left(D^rG_i(1)\right)
=
2^{-\binom m2}
\left(\prod_{i=1}^{m}\binom n{k_i}\right)
\prod_{i<j}(k_j-k_i)(n-k_i-k_j).
}
$$

Every factor is nonzero in the lower half of the row. Therefore the first $m$ Euler jets at the single point $q=1$ form a complete coordinate system for every $m$-term Gaussian-row circuit.

The sharp multiplicity consequence is

$$
\boxed{
0\ne\sum_{i=1}^{m}c_i{n\brack k_i}_q
\quad\Longrightarrow\quad
\operatorname{ord}_{q=1}
\left(\sum_{i=1}^{m}c_i{n\brack k_i}_q\right)
\le m-1.
}
$$

The bound is attained for every chosen set of distinct row positions.

Thus the exact capacity of an $m$-dimensional Gaussian-row subspace at the positive endpoint is the theoretical minimum:

$$
\boxed{m-1.}
$$

The complete structural chain is

$$
\boxed{
\text{Gaussian reciprocity}
\longrightarrow
E=k(n-k)
\longrightarrow
\text{polynomial jet sequence}
\longrightarrow
\text{Vandermonde determinant}
\longrightarrow
\text{sharp arbitrary-rank rigidity}.
}
$$

The labels used below are:

- **Classical lemma:** standard algebraic input, proved here when used;
- **Project theorem:** a theorem established in this project;
- **Corollary:** a formal consequence;
- **Sharpness statement:** a construction proving optimality;
- **Algorithmic theorem:** a correctness theorem for exact reconstruction or identity testing;
- **Software corollary:** a direct non-expanding computational consequence;
- **Caution:** a boundary required for exact interpretation.

Throughout, coefficients lie in a characteristic-zero field unless a smaller coefficient ring is specified.

---

# 1. Gaussian rows and the positive endpoint

## 1.1 Gaussian binomial coefficients

For integers

$$
n\ge0,
\qquad
0\le k\le n,
$$

define

$$
G_{n,k}(q)
=
{n\brack k}_q
=
\frac{(q;q)_n}{(q;q)_k(q;q)_{n-k}},
$$

where

$$
(q;q)_A
=
\prod_{a=1}^{A}(1-q^a),
\qquad
(q;q)_0=1.
$$

Gaussian reciprocity gives

$$
\boxed{
G_{n,k}(q)=G_{n,n-k}(q).
}
$$

Its degree is

$$
\boxed{
\deg G_{n,k}=k(n-k).
}
$$

At the positive endpoint,

$$
\boxed{
G_{n,k}(1)=\binom nk.
}
$$

Every Gaussian coefficient is therefore regular and nonzero at $q=1$.

## 1.2 Euler jets

Use the Euler derivation

$$
D=q\frac d{dq}.
$$

In the exponential coordinate

$$
q=e^x,
$$

one has

$$
D=\frac d{dx}.
$$

Thus

$$
D^rG_{n,k}(1)
=
\left.
\frac{d^r}{dx^r}G_{n,k}(e^x)
\right|_{x=0}.
$$

### Definition 1.1 — Normalized Gaussian germ

Define

$$
\boxed{
U_{n,k}(x)
=
\frac{G_{n,k}(e^x)}{\binom nk}.
}
$$

Then

$$
U_{n,k}(0)=1.
$$

### Definition 1.2 — Gaussian jet polynomial at a row position

For $r\ge0$, define

$$
\boxed{
p_{r,n}(k)
=
U_{n,k}^{(r)}(0)
=
\frac{D^rG_{n,k}(1)}{\binom nk}.
}
$$

The central theorem will show that $p_{r,n}(k)$ is not an arbitrary function of $k$. It is a polynomial in the single coordinate

$$
E_n(k)=k(n-k).
$$

---

# 2. Exact positive-endpoint Gaussian germ

For $r\ge0$, write

$$
S_r(A)=\sum_{a=1}^{A}a^r,
\qquad
S_r(0)=0.
$$

We use the Bernoulli convention

$$
\frac z{e^z-1}
=
\sum_{j\ge0}B_j\frac{z^j}{j!},
\qquad
B_1=-\frac12.
$$

## 2.1 Factorial normal form

Part XIII proved the exact positive-endpoint expansion

$$
(q;q)_A\big|_{q=e^x}
=
(-1)^AA!x^A
\exp\left(
\frac{S_1(A)}2x
+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}
S_{2r}(A)x^{2r}
\right).
$$

We apply it to the Gaussian quotient.

### Project Proposition 2.1 — Exact normalized Gaussian germ

For every $0\le k\le n$,

$$
\boxed{
U_{n,k}(x)
=
\exp\left(
\frac{k(n-k)}2x
+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}
\Delta_{r,n}(k)x^{2r}
\right),
}
$$

where

$$
\boxed{
\Delta_{r,n}(k)
=
S_{2r}(n)-S_{2r}(k)-S_{2r}(n-k).
}
$$

### Proof

Apply the factorial normal form to the numerator and the two denominator factorials.

The powers of $x$ cancel because

$$
n-k-(n-k)=0,
$$

more explicitly,

$$
x^n\big/(x^kx^{n-k})=1.
$$

The signs cancel because

$$
(-1)^n
\big/
\left((-1)^k(-1)^{n-k}\right)=1.
$$

The factorial residual is

$$
\frac{n!}{k!(n-k)!}
=
\binom nk.
$$

After division by this residual, the linear logarithmic coefficient is

$$
\frac12
\left(
S_1(n)-S_1(k)-S_1(n-k)
\right).
$$

Since

$$
S_1(A)=\frac{A(A+1)}2,
$$

a direct calculation gives

$$
S_1(n)-S_1(k)-S_1(n-k)
=
k(n-k).
$$

For every $r\ge1$, the even logarithmic coefficient is exactly

$$
\frac{B_{2r}}{2r(2r)!}
\left(
S_{2r}(n)-S_{2r}(k)-S_{2r}(n-k)
\right).
$$

This proves the formula. ∎

## 2.2 Reciprocity normalization

The Gaussian coefficient is reciprocal of degree

$$
E_n(k)=k(n-k):
$$

$$
G_{n,k}(q^{-1})
=
q^{-E_n(k)}G_{n,k}(q).
$$

Therefore

$$
\boxed{
e^{-E_n(k)x/2}U_{n,k}(x)
}
$$

is an even formal power series. Proposition 2.1 displays this directly: after removal of the drift $E_n(k)x/2$, only even powers of $x$ remain.

The positive endpoint is therefore controlled by two layers:

$$
\boxed{
\text{degree drift }E_n(k)/2
\quad+
\text{even curvature hierarchy}.
}
$$

The new fact is that the entire curvature hierarchy is also polynomial in the same coordinate $E_n(k)$.

---

# 3. Collapse to the Gaussian spectral coordinate

Fix $n$. Put

$$
E=E_n(k)=k(n-k).
$$

The pair

$$
(k,n-k)
$$

has elementary symmetric functions

$$
k+(n-k)=n,
\qquad
k(n-k)=E.
$$

Every symmetric polynomial in $k$ and $n-k$ is therefore a polynomial in $n$ and $E$. Since $n$ is fixed, it becomes a polynomial in $E$ alone.

We first prove an elementary degree-controlled form of this statement.

## 3.1 Symmetric power recurrence

### Classical Lemma 3.1 — Two-root power recurrence

Let $u,v$ satisfy

$$
u+v=n,
\qquad
uv=E.
$$

For $j\ge0$, define

$$
R_j(n,E)=u^j+v^j.
$$

Then

$$
R_0(n,E)=2,
\qquad
R_1(n,E)=n,
$$

and

$$
\boxed{
R_j(n,E)
=
nR_{j-1}(n,E)-ER_{j-2}(n,E)
\qquad(j\ge2).
}
$$

Consequently,

$$
\boxed{
R_j(n,E)\in\mathbb Z[n,E],
\qquad
\deg_E R_j(n,E)\le\left\lfloor\frac j2\right\rfloor.
}
$$

### Proof

Because $u$ and $v$ are roots of

$$
z^2-nz+E=0,
$$

each satisfies

$$
u^j=nu^{j-1}-Eu^{j-2},
\qquad
v^j=nv^{j-1}-Ev^{j-2}.
$$

Adding gives the recurrence.

The polynomial and degree assertions follow by induction. Multiplication by $n$ does not change $E$-degree, while multiplication by $E$ increases it by one. Thus

$$
\deg_E R_j
\le
\max\left(
\left\lfloor\frac{j-1}{2}\right\rfloor,
1+\left\lfloor\frac{j-2}{2}\right\rfloor
\right)
=
\left\lfloor\frac j2\right\rfloor.
$$

∎

## 3.2 Polynomiality of the even Gaussian cumulants

Faulhaber's theorem says that $S_{2r}(z)$ is a polynomial in $z$ of degree $2r+1$ with rational coefficients and zero constant term.

### Project Lemma 3.2 — Gaussian cumulant collapse

For every $r\ge1$, there exists a unique universal polynomial

$$
Q_r(N,E)\in\mathbb Q[N,E]
$$

such that, for formal variables $u,v$,

$$
\boxed{
S_{2r}(u+v)-S_{2r}(u)-S_{2r}(v)
=
Q_r(u+v,uv).
}
$$

Moreover,

$$
\boxed{
\deg_E Q_r(N,E)\le r.
}
$$

For fixed $n$, write

$$
Q_{r,n}(E)=Q_r(n,E).
$$

Then

$$
\boxed{
\Delta_{r,n}(k)
=
Q_{r,n}\bigl(k(n-k)\bigr)
}
$$

for every $0\le k\le n$.

### Proof

The polynomial

$$
S_{2r}(u+v)-S_{2r}(u)-S_{2r}(v)
$$

is symmetric in $u,v$. By the fundamental theorem of symmetric polynomials in two variables, it has a unique expression as a polynomial in

$$
u+v
\quad\text{and}\quad
uv.
$$

This gives the unique universal polynomial $Q_r(N,E)$.

To prove the degree bound, write the Faulhaber polynomial as

$$
S_{2r}(z)=\sum_{j=1}^{2r+1}a_jz^j.
$$

Then

$$
\begin{aligned}
S_{2r}(u+v)-S_{2r}(u)-S_{2r}(v)
&=
\sum_{j=1}^{2r+1}
a_j\left((u+v)^j-u^j-v^j\right).
\end{aligned}
$$

By Lemma 3.1,

$$
u^j+v^j=R_j(u+v,uv),
$$

and $R_j$ has $E=uv$-degree at most $\lfloor j/2\rfloor$. The term $(u+v)^j$ has $E$-degree zero. Since

$$
j\le2r+1,
$$

we have

$$
\left\lfloor\frac j2\right\rfloor\le r.
$$

Therefore $\deg_EQ_r\le r$. Specializing $u=k$, $v=n-k$ gives the stated formula for $Q_{r,n}$. ∎

### Examples 3.3 — The first two collapsed cumulants

For $r=1$,

$$
\boxed{
Q_{1,n}(E)=(n+1)E.
}
$$

For $r=2$,

$$
\boxed{
Q_{2,n}(E)
=
(n+1)E\left(n^2+n-E\right).
}
$$

Thus

$$
\log U_{n,k}(x)
=
\frac E2x
+
\frac{n+1}{24}E x^2
-
\frac{(n+1)E(n^2+n-E)}{2880}x^4
+
\cdots,
$$

where $E=k(n-k)$.

The exact displayed denominators follow from

$$
\frac{B_2}{2\cdot2!}=\frac1{24},
\qquad
\frac{B_4}{4\cdot4!}=-\frac1{2880},
$$

together with the convention that $Q_{r,n}$ multiplies $x^{2r}$. Equivalently, in logarithmic derivative form,

$$
\kappa_2=\frac{n+1}{12}E,
\qquad
\kappa_4=-\frac1{120}(n+1)E(n^2+n-E).
$$

### Caution 3.4 — Series coefficient versus cumulant

The coefficient of $x^j$ in $\log U$ differs from the logarithmic derivative

$$
\kappa_j
=
\left.\frac{d^j}{dx^j}\log U(x)\right|_{x=0}
$$

by a factor of $j!$. The chapter uses both forms, and the normalization is always stated explicitly.

## 3.3 The one-parameter local normal form

Combining Proposition 2.1 and Lemma 3.2 gives the exact one-parameter representation

$$
\boxed{
U_{n,k}(x)
=
\mathcal U_n\bigl(E_n(k),x\bigr),
}
$$

where

$$
\boxed{
\mathcal U_n(E,x)
=
\exp\left(
\frac E2x
+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}
Q_{r,n}(E)x^{2r}
\right).
}
$$

Thus the symmetry classes

$$
k\leftrightarrow n-k
$$

are not merely equal as polynomials. Their complete positive-endpoint local geometry is parametrized by the same scalar coordinate $E$.

---

# 4. The polynomial-cumulant Jet–Vandermonde principle

The Gaussian determinant is an instance of a more general mechanism.

## 4.1 Formal setup

Let $K$ be a characteristic-zero field. Let

$$
A_j(T)\in K[T]
\qquad(j\ge1)
$$

satisfy

$$
A_1(T)=aT+b,
\qquad
a\ne0,
$$

and

$$
\deg A_j\le j-1
\qquad(j\ge2).
$$

Define the formal germ

$$
\boxed{
\mathcal F_T(x)
=
\exp\left(
\sum_{j\ge1}A_j(T)x^j
\right).
}
$$

For $r\ge0$, define

$$
P_r(T)
=
\left.
\frac{d^r}{dx^r}\mathcal F_T(x)
\right|_{x=0}.
$$

## 4.2 Degree theorem

### Project Theorem 4.1 — Polynomial-cumulant jet degree

For every $r\ge0$,

$$
\boxed{
P_r(T)\in K[T],
\qquad
\deg P_r=r,
}
$$

and the leading coefficient of $P_r$ is

$$
\boxed{a^r.}
$$

### Proof

Expand the exponential formally. A contribution to the coefficient of $x^r$ is indexed by nonnegative multiplicities

$$
\mu_1,\mu_2,\ldots
$$

satisfying

$$
\sum_{j\ge1}j\mu_j=r.
$$

The corresponding product has $T$-degree at most

$$
\begin{aligned}
\mu_1
+
\sum_{j\ge2}(j-1)\mu_j
&=
\sum_{j\ge1}j\mu_j
-
\sum_{j\ge2}\mu_j\\
&=
r-\sum_{j\ge2}\mu_j\\
&\le r.
\end{aligned}
$$

Equality can occur only when

$$
\mu_j=0
\qquad(j\ge2).
$$

Thus the unique contribution of possible degree $r$ comes from taking the linear logarithmic term $A_1(T)x$ exactly $r$ times. In the exponential series this contributes

$$
\frac{A_1(T)^r}{r!}x^r.
$$

After multiplication by $r!$ to obtain the $r$-th derivative, the leading term is

$$
a^rT^r.
$$

Every other contribution has degree at most $r-1$. Hence $P_r$ has exact degree $r$ and leading coefficient $a^r$. ∎

## 4.3 Exact determinant

### Project Theorem 4.2 — Abstract Jet–Vandermonde determinant

Let

$$
\theta_1,\ldots,\theta_m\in K
$$

be pairwise distinct. Then

$$
\boxed{
\det\left(P_r(\theta_i)\right)_{
\substack{0\le r\le m-1\\1\le i\le m}}
=
a^{\binom m2}
\prod_{1\le i<j\le m}(\theta_j-\theta_i).
}
$$

### Proof

The polynomials

$$
P_0(T),P_1(T),\ldots,P_{m-1}(T)
$$

have respective degrees

$$
0,1,\ldots,m-1
$$

and leading coefficients

$$
1,a,a^2,\ldots,a^{m-1}.
$$

Changing from the monomial basis

$$
1,T,T^2,\ldots,T^{m-1}
$$

to the basis $P_0,\ldots,P_{m-1}$ is lower triangular with diagonal entries

$$
1,a,a^2,\ldots,a^{m-1}.
$$

The evaluation matrix in the monomial basis is the Vandermonde matrix. Therefore

$$
\det\left(P_r(\theta_i)\right)
=
\left(\prod_{r=0}^{m-1}a^r\right)
\prod_{i<j}(\theta_j-\theta_i).
$$

Since

$$
\sum_{r=0}^{m-1}r=\binom m2,
$$

the formula follows. ∎

### Interpretation 4.3

The determinant does not depend on the lower polynomial terms in the logarithmic cumulants. Once the first cumulant is affine with nonzero slope and every higher logarithmic coefficient has subcritical parameter degree, the entire finite jet matrix is forced to be Vandermonde up to one explicit scalar.

This is the general mechanism behind the Gaussian theorem.

---

# 5. Exact Gaussian jet polynomials

Apply Theorem 4.1 to

$$
\mathcal U_n(E,x)
=
\exp\left(
\frac E2x
+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}
Q_{r,n}(E)x^{2r}
\right).
$$

The coefficient of $x$ is

$$
A_1(E)=\frac E2.
$$

For $j=2r\ge2$,

$$
A_{2r}(E)
=
\frac{B_{2r}}{2r(2r)!}Q_{r,n}(E),
$$

with

$$
\deg_EA_{2r}\le r\le2r-1.
$$

For odd $j\ge3$,

$$
A_j(E)=0.
$$

The hypotheses of the abstract theorem therefore hold with

$$
a=\frac12.
$$

### Project Theorem 5.1 — Gaussian jet-polynomial theorem

For every $n\ge0$ and $r\ge0$, there exists a polynomial

$$
p_{r,n}(E)\in\mathbb Q[E]
$$

such that

$$
\boxed{
\frac{D^rG_{n,k}(1)}{\binom nk}
=
p_{r,n}\bigl(k(n-k)\bigr)
}
$$

for all $0\le k\le n$. Moreover,

$$
\boxed{
\deg_Ep_{r,n}=r,
}
$$

and

$$
\boxed{
 p_{r,n}(E)
=
2^{-r}E^r
+
\text{terms of degree at most }r-1.
}
$$

### Proof

By the one-parameter local normal form,

$$
U_{n,k}(x)
=
\mathcal U_n(E_n(k),x).
$$

Apply Theorem 4.1 with parameter $T=E$ and slope $a=1/2$. The resulting derivative polynomial is exactly

$$
p_{r,n}(E)
=
\left.
\frac{d^r}{dx^r}\mathcal U_n(E,x)
\right|_{x=0}.
$$

The degree and leading coefficient follow from the abstract theorem. ∎

## 5.1 First jet polynomials

The first polynomials are

$$
\boxed{p_{0,n}(E)=1,}
$$

$$
\boxed{p_{1,n}(E)=\frac E2,}
$$

and

$$
\boxed{
p_{2,n}(E)
=
\frac{E^2}{4}
+
\frac{n+1}{12}E.
}
$$

Since the third logarithmic cumulant vanishes,

$$
\boxed{
p_{3,n}(E)
=
\frac{E^3}{8}
+
\frac{n+1}{8}E^2.
}
$$

Every further $p_{r,n}$ is obtained exactly from the collapsed cumulants by Bell-polynomial reconstruction.

## 5.2 Exact recurrence

Define the logarithmic derivatives

$$
\lambda_j(E)
=
\left.
\frac{d^j}{dx^j}
\log\mathcal U_n(E,x)
\right|_{x=0}.
$$

Then

$$
\lambda_1(E)=\frac E2,
$$

$$
\lambda_{2r}(E)
=
\frac{B_{2r}}{2r}Q_{r,n}(E),
\qquad
r\ge1,
$$

and

$$
\lambda_{2r+1}(E)=0,
\qquad
r\ge1.
$$

### Proposition 5.2 — Bell recurrence for Gaussian jets

The jet polynomials satisfy

$$
\boxed{
p_{0,n}(E)=1,
}
$$

and

$$
\boxed{
p_{r+1,n}(E)
=
\sum_{j=0}^{r}
\binom rj
\lambda_{r+1-j}(E)p_{j,n}(E).
}
$$

### Proof

Write

$$
\mathcal U_n(E,x)=e^{L(E,x)}.
$$

Then

$$
\frac d{dx}\mathcal U_n=L_x\mathcal U_n.
$$

Differentiate $r$ more times and apply the Leibniz rule:

$$
\mathcal U_n^{(r+1)}
=
\sum_{j=0}^{r}
\binom rj
L^{(r+1-j)}
\mathcal U_n^{(j)}.
$$

Evaluate at $x=0$. ∎

This recurrence gives a non-expanding exact algorithm for all jets needed in the chapter.

---

# 6. The Gaussian Jet–Vandermonde determinant

We now prove the main theorem.

Let

$$
0\le k_1<\cdots<k_m\le\left\lfloor\frac n2\right\rfloor.
$$

Put

$$
E_i=k_i(n-k_i),
\qquad
G_i(q)=G_{n,k_i}(q).
$$

## 6.1 Distinctness of the spectral nodes

### Lemma 6.1 — Strict lower-half degree ordering

The numbers

$$
E_1,E_2,\ldots,E_m
$$

are strictly increasing.

### Proof

For consecutive integers,

$$
E_n(k+1)-E_n(k)
=
(k+1)(n-k-1)-k(n-k)
=
n-2k-1.
$$

If

$$
0\le k<\left\lfloor\frac n2\right\rfloor,
$$

then

$$
n-2k-1>0.
$$

Therefore $E_n(k)$ is strictly increasing on the lower half. ∎

## 6.2 Exact determinant

### Project Theorem 6.2 — Gaussian Jet–Vandermonde Theorem

For

$$
0\le k_1<\cdots<k_m\le\left\lfloor\frac n2\right\rfloor,
$$

one has

$$
\boxed{
\det\left(
D^r{n\brack k_i}_q\big|_{q=1}
\right)_{
\substack{0\le r\le m-1\\1\le i\le m}}
=
2^{-\binom m2}
\left(\prod_{i=1}^{m}\binom n{k_i}\right)
\prod_{1\le i<j\le m}(E_j-E_i).
}
$$

Equivalently,

$$
\boxed{
\det\left(
D^r{n\brack k_i}_q\big|_{q=1}
\right)
=
2^{-\binom m2}
\left(\prod_{i=1}^{m}\binom n{k_i}\right)
\prod_{i<j}(k_j-k_i)(n-k_i-k_j).
}
$$

In particular, the determinant is strictly positive.

### Proof

By Theorem 5.1,

$$
D^rG_i(1)
=
\binom n{k_i}p_{r,n}(E_i).
$$

Factor $\binom n{k_i}$ from column $i$. This gives

$$
\det\left(D^rG_i(1)\right)
=
\left(\prod_i\binom n{k_i}\right)
\det\left(p_{r,n}(E_i)\right).
$$

The polynomials $p_{r,n}$ have exact degree $r$ and leading coefficient $2^{-r}$. By Theorem 4.2,

$$
\det\left(p_{r,n}(E_i)\right)
=
2^{-\binom m2}
\prod_{i<j}(E_j-E_i).
$$

Finally,

$$
\begin{aligned}
E_j-E_i
&=k_j(n-k_j)-k_i(n-k_i)\\
&=(k_j-k_i)n-(k_j^2-k_i^2)\\
&=(k_j-k_i)(n-k_i-k_j).
\end{aligned}
$$

Because $k_j>k_i$ and both indices lie in the lower half,

$$
n-k_i-k_j>0.
$$

Hence every factor is positive. ∎

## 6.3 Ordinary derivative form

Let

$$
\partial=\frac d{dq}.
$$

The Euler powers satisfy

$$
D^r
=
\sum_{s=0}^{r}
\left\{\begin{matrix}r\\s\end{matrix}\right\}
q^s\partial^s,
$$

where the braces are Stirling numbers of the second kind. At $q=1$, the transformation from

$$
\bigl(\partial^sP(1)\bigr)_{0\le s<m}
$$

to

$$
\bigl(D^rP(1)\bigr)_{0\le r<m}
$$

is lower unitriangular.

### Corollary 6.3 — Ordinary Wronskian determinant

The same determinant formula holds with ordinary derivatives:

$$
\boxed{
\det\left(
\frac{d^r}{dq^r}{n\brack k_i}_q\bigg|_{q=1}
\right)_{
\substack{0\le r\le m-1\\1\le i\le m}}
=
2^{-\binom m2}
\left(\prod_i\binom n{k_i}\right)
\prod_{i<j}(E_j-E_i).
}
$$

### Proof

The two derivative matrices differ by left multiplication by a lower triangular matrix with every diagonal entry equal to one. Its determinant is one. ∎

## 6.4 Initial-jet minors

The theorem applies to every subset of $r$ chosen row positions and the first $r$ jets.

### Corollary 6.4 — Strict positivity of all initial jet minors

For every

$$
1\le r\le m
$$

and every subset

$$
1\le i_1<\cdots<i_r\le m,
$$

one has

$$
\boxed{
\det\left(D^aG_{i_b}(1)\right)_{
\substack{0\le a\le r-1\\1\le b\le r}}>0.
}
$$

Thus the ordered lower-half Gaussian row is strictly sign-regular for initial positive-endpoint jets.

---

# 7. Sharp arbitrary-rank Gaussian contact

Let $K$ be a characteristic-zero field and define

$$
\mathcal V
=
\operatorname{span}_K
\left\{
G_1(q),\ldots,G_m(q)
\right\}.
$$

Because the degrees $E_i$ are distinct, the $G_i$ are globally linearly independent. The new theorem is much stronger: their first $m$ jets at one point already detect every linear combination.

## 7.1 Main contact bound

### Project Theorem 7.1 — Sharp Arbitrary-Rank Gaussian-Row Contact Theorem

Let

$$
F(q)=\sum_{i=1}^{m}c_i{n\brack k_i}_q,
\qquad
c_i\in K.
$$

If $F\ne0$, then

$$
\boxed{
\operatorname{ord}_{q=1}F\le m-1.
}
$$

Equivalently,

$$
\boxed{
D^rF(1)=0
\quad(0\le r<m)
\quad\Longrightarrow\quad
F=0.
}
$$

### Proof

Suppose

$$
D^rF(1)=0
\qquad(0\le r<m).
$$

Then the coefficient vector

$$
(c_1,\ldots,c_m)^T
$$

lies in the kernel of the jet matrix

$$
\left(D^rG_i(1)\right)_{
\substack{0\le r<m\\1\le i\le m}}.
$$

By Theorem 6.2, this matrix has nonzero determinant. Hence every $c_i=0$, so $F=0$.

Taking the contrapositive proves the multiplicity bound. ∎

### Interpretation 7.2 — Minimum possible capacity

Every $m$-dimensional space of analytic germs admits a nonzero element vanishing to order at least $m-1$: impose the first $m-1$ homogeneous jet equations on $m$ coefficients.

Therefore no universal upper bound below $m-1$ is possible.

Theorem 7.1 reaches this dimension-theoretic minimum exactly:

$$
\boxed{
\max_{0\ne F\in\mathcal V}
\operatorname{ord}_{q=1}F
=m-1.
}
$$

The Gaussian row is therefore maximally rigid at the positive endpoint.

## 7.2 Two-term specialization

For two distinct lower-half indices $i<j$, define

$$
H_{i,j}(q)
=
\frac{{n\brack i}_q}{\binom ni}
-
\frac{{n\brack j}_q}{\binom nj}.
$$

Then

$$
H_{i,j}(1)=0,
$$

while

$$
DH_{i,j}(1)
=
\frac{E_i-E_j}{2}\ne0.
$$

### Corollary 7.3 — Every normalized two-term row collision is simple

$$
\boxed{
\operatorname{ord}_{q=1}H_{i,j}=1.
}
$$

This is the positive-endpoint analogue of the simple-collision principle from Part II, now valid for every pair of distinct Gaussian symmetry classes in one row.

---

# 8. Explicit extremizers and the complete contact filtration

The upper bound $m-1$ is attained for every selected set of row positions.

## 8.1 Barycentric moment identities

Let

$$
E_1,\ldots,E_m
$$

be distinct, and define

$$
\boxed{
w_i
=
\frac1{\displaystyle\prod_{j\ne i}(E_i-E_j)}.
}
$$

### Classical Lemma 8.1 — Barycentric annihilation identities

One has

$$
\boxed{
\sum_{i=1}^{m}w_iE_i^r=0
\qquad(0\le r\le m-2),
}
$$

and

$$
\boxed{
\sum_{i=1}^{m}w_iE_i^{m-1}=1.
}
$$

### Proof

For every polynomial $P(E)$ of degree at most $m-1$, Lagrange interpolation gives

$$
P(E)
=
\sum_{i=1}^{m}
P(E_i)
\frac{\prod_{j\ne i}(E-E_j)}{\prod_{j\ne i}(E_i-E_j)}.
$$

Compare the coefficient of $E^{m-1}$. The coefficient on the right is

$$
\sum_iw_iP(E_i).
$$

For $P(E)=E^r$, the coefficient of $E^{m-1}$ is zero when $r<m-1$ and one when $r=m-1$. ∎

## 8.2 Universal extremal combination

### Project Theorem 8.2 — Explicit maximal-contact Gaussian combination

Define

$$
\boxed{
H(q)
=
\sum_{i=1}^{m}
\frac{w_i}{\binom n{k_i}}
{n\brack k_i}_q.
}
$$

Then

$$
\boxed{
D^rH(1)=0
\qquad(0\le r\le m-2),
}
$$

and

$$
\boxed{
D^{m-1}H(1)=2^{-(m-1)}.
}
$$

Consequently,

$$
\boxed{
\operatorname{ord}_{q=1}H=m-1.
}
$$

In exponential coordinates,

$$
\boxed{
H(e^x)
=
\frac{x^{m-1}}{2^{m-1}(m-1)!}
+
O(x^m).
}
$$

### Proof

By Theorem 5.1,

$$
D^rH(1)
=
\sum_{i=1}^{m}w_ip_{r,n}(E_i).
$$

For $r\le m-2$, the polynomial $p_{r,n}$ has degree at most $r\le m-2$. Lemma 8.1 therefore gives

$$
\sum_iw_ip_{r,n}(E_i)=0.
$$

At order $m-1$, write

$$
p_{m-1,n}(E)
=
2^{-(m-1)}E^{m-1}+R(E),
$$

where

$$
\deg R\le m-2.
$$

Then

$$
\begin{aligned}
D^{m-1}H(1)
&=
2^{-(m-1)}
\sum_iw_iE_i^{m-1}
+
\sum_iw_iR(E_i)\\
&=
2^{-(m-1)}.
\end{aligned}
$$

The Taylor expansion in $x$ follows because $D=d/dx$. ∎

## 8.3 Extremizers at every order

For $0\le r\le m-1$, choose any $r+1$ of the selected nodes, say

$$
E_1,\ldots,E_{r+1},
$$

and define their barycentric weights

$$
w_i^{(r)}
=
\frac1{\displaystyle\prod_{\substack{1\le j\le r+1\\j\ne i}}(E_i-E_j)}.
$$

Then

$$
H_r(q)
=
\sum_{i=1}^{r+1}
\frac{w_i^{(r)}}{\binom n{k_i}}
{n\brack k_i}_q
$$

has exact order $r$ and

$$
D^rH_r(1)=2^{-r}.
$$

Thus every order

$$
0,1,\ldots,m-1
$$

occurs inside the Gaussian-row span.

## 8.4 Contact filtration

For $r\ge0$, define

$$
\mathcal V_{\ge r}
=
\left\{
F\in\mathcal V:
\operatorname{ord}_{q=1}F\ge r
\right\}.
$$

### Project Theorem 8.3 — Complete Gaussian contact filtration

For

$$
0\le r\le m,
$$

one has

$$
\boxed{
\dim_K\mathcal V_{\ge r}=m-r.
}
$$

In particular,

$$
\mathcal V
supset
\mathcal V_{\ge1}
\supset
\cdots
\supset
\mathcal V_{\ge m-1}
\supset
\mathcal V_{\ge m}=\{0\}
$$

is a complete flag with one-dimensional successive quotients.

### Proof

The space $\mathcal V_{\ge r}$ is the kernel of the truncated jet map

$$
J_r:\mathcal V\longrightarrow K^r,
\qquad
F\longmapsto
\left(F(1),DF(1),\ldots,D^{r-1}F(1)\right).
$$

The first $r$ normalized jet polynomials

$$
p_{0,n},\ldots,p_{r-1,n}
$$

have distinct degrees

$$
0,\ldots,r-1.
$$

Their evaluation rows at the $m$ distinct nodes $E_i$ are linearly independent. Indeed, a linear dependence would produce a nonzero polynomial of degree at most $r-1$ vanishing at at least $m\ge r$ distinct points, which is impossible.

Hence

$$
\operatorname{rank}J_r=r.
$$

Since $\dim\mathcal V=m$, rank-nullity gives

$$
\dim\mathcal V_{\ge r}=m-r.
$$

∎

### Definition 8.4 — Local jet-Chebyshev system

A finite ordered family of analytic germs is called a **local jet-Chebyshev system at a point** if every nonzero combination of $m$ selected germs has vanishing order at most $m-1$ there.

### Corollary 8.5

Every ordered set of distinct lower-half Gaussian row entries is a local jet-Chebyshev system at $q=1$.

### Caution 8.6 — Local versus interval Chebyshev theory

The statement is local at $q=1$. It does not assert that every nonzero Gaussian-row combination has at most $m-1$ zeros on a real interval. Such an interval statement would require control of Wronskians away from the positive endpoint and is not proved here.

---

# 9. One-point reconstruction and identity certificates

The determinant theorem provides more than a multiplicity bound. It gives exact reconstruction of every row circuit from one finite jet packet.

## 9.1 Normalized row circuits

Define

$$
\widetilde G_i(q)
=
\frac{{n\brack k_i}_q}{\binom n{k_i}}.
$$

Let

$$
F(q)=\sum_{i=1}^{m}a_i\widetilde G_i(q).
$$

Then

$$
D^rF(1)
=
\sum_{i=1}^{m}a_ip_{r,n}(E_i).
$$

### Project Theorem 9.1 — Gaussian one-point jet isomorphism

The map

$$
\boxed{
\mathcal J_{n,\mathbf k}:
\operatorname{span}_K\{\widetilde G_1,\ldots,\widetilde G_m\}
\longrightarrow
K^m
}
$$

specified by

$$
\boxed{
F\longmapsto
\left(F(1),DF(1),\ldots,D^{m-1}F(1)\right)
}
$$

is a linear isomorphism.

### Proof

Its matrix in the normalized Gaussian basis is

$$
\left(p_{r,n}(E_i)\right)_{
\substack{0\le r<m\\1\le i\le m}}.
$$

By Theorem 6.2 after removal of the binomial column factors, its determinant is

$$
2^{-\binom m2}
\prod_{i<j}(E_j-E_i)
e0.
$$

∎

### Corollary 9.2 — Complete one-point identity criterion

For a Gaussian-row circuit with at most $m$ distinct symmetry classes,

$$
\boxed{
F=0
\iff
D^rF(1)=0
\quad(0\le r<m).
}
$$

A first nonzero jet is a nonidentity certificate. Vanishing of all first $m$ jets is an identity certificate.

## 9.2 Moment conversion

Write

$$
p_{r,n}(E)
=
2^{-r}E^r
+
\sum_{s=0}^{r-1}\beta_{r,s}(n)E^s.
$$

For a normalized circuit, define its spectral moments

$$
M_s
=
\sum_{i=1}^{m}a_iE_i^s.
$$

Then

$$
D^rF(1)
=
2^{-r}M_r
+
\sum_{s=0}^{r-1}\beta_{r,s}(n)M_s.
$$

This is a lower-triangular transformation with nonzero diagonal $2^{-r}$.

### Algorithmic Theorem 9.3 — Exact Gaussian-row reconstruction

The coefficients $a_i$ are recovered uniquely from the first $m$ Euler jets by:

1. recursively converting the jet packet into the moments
   $$
   M_0,M_1,\ldots,M_{m-1};
   $$
2. solving the transposed Vandermonde system
   $$
   M_s=\sum_i a_iE_i^s
   \qquad(0\le s<m).
   $$

Every step uses exact rational arithmetic.

### Proof

The jet-to-moment system is lower triangular with diagonal entries $2^{-r}$, hence invertible.

The moment-to-coefficient matrix is the Vandermonde matrix

$$
(E_i^s)_{
\substack{0\le s<m\\1\le i\le m}},
$$

whose determinant is

$$
\prod_{i<j}(E_j-E_i)\ne0.
$$

Thus both stages are uniquely invertible. ∎

## 9.3 Direct identity-test algorithm

```text
input:
    n
    distinct k_i in [0, floor(n/2)]
    normalized rational coefficients a_i

for r = 0,...,m-1:
    compute p_{r,n}(E_i) for all i
    J_r = sum_i a_i * p_{r,n}(E_i)
    if J_r != 0:
        return NONZERO with certificate (r, J_r)

return ZERO
```

The jet polynomials may be generated by Proposition 5.2. Their logarithmic inputs are computed from Faulhaber power sums, without expanding any Gaussian polynomial.

### Software Corollary 9.4 — Degree-free exact testing

The number of required jets is exactly the number of distinct Gaussian symmetry classes in the circuit. It is independent of

$$
\max_i\deg {n\brack k_i}_q
=
\max_i k_i(n-k_i),
$$

which may be quadratically large in $n$.

## 9.4 Bit complexity

For a binomial-normalized input

$$
F(q)=
\sum_{i=1}^{m}a_i
\frac{{n\brack k_i}_q}{\binom n{k_i}},
$$

with rational $a_i$, the exact values

$$
p_{r,n}(E_i),
\qquad
0\le r<m,
$$

can be computed using:

- Bernoulli numbers through index $2m$;
- Faulhaber power sums of order at most $2m$;
- Bell recurrence through order $m-1$;
- rational arithmetic on integers of bit length polynomial in $m\log n$.

### Algorithmic Theorem 9.5 — Polynomial-time normalized Gaussian-row PIT

The identity test in Section 9.3 runs in deterministic bit complexity polynomial in

$$
m,
\qquad
\log n,
\qquad
\text{and the bit length of the normalized coefficients }a_i.
$$

### Proof

Only $m$ jet orders are required. For each order, Faulhaber evaluation uses a number of rational operations polynomial in $m$. The integers $n$, $k_i$, and $E_i$ enter only through powers of exponent at most $O(m)$, whose bit lengths are $O(m\log n)$. Bernoulli numbers through order $2m$ have polynomial bit length in $m$, and the Bell recurrence uses polynomially many operations.

The final sums involve $m$ rational terms at each of $m$ orders. Standard exact rational arithmetic therefore gives polynomial bit complexity in the stated parameters. ∎

### Caution 9.6 — Unnormalized coefficient input

For a circuit written as

$$
\sum_i c_i{n\brack k_i}_q,
$$

the normalized coefficients are

$$
a_i=c_i\binom n{k_i}.
$$

Materializing $\binom n{k_i}$ may require $\Theta(n)$ output bits. The arithmetic-operation count remains polynomial in $m$, but a bit-polynomial claim in $\log n$ requires either normalized input or a separate compact arithmetic representation of the binomial weights.

This chapter therefore claims deterministic bit-polynomial complexity directly for the normalized model and an output-sensitive exact algorithm for the unnormalized model.

---

# 10. Stable central-block synthesis with Part II

Assume

$$
t\ge5,
\qquad
n\ge3t-2.
$$

Part II proved that the common polynomial content of the retained block is

$$
\boxed{
C_{n,t}(q)
=
\prod_{d=n-t+1}^{n}\Phi_d(q).
}
$$

For every retained index $k$, define the primitive row quotient

$$
\boxed{
R_{n,t,k}(q)
=
\frac{{n\brack k}_q}{C_{n,t}(q)}.
}
$$

This is a polynomial in $\mathbb Z[q]$.

Since every terminal index satisfies $d>1$,

$$
C_{n,t}(1)\ne0.
$$

More explicitly,

$$
C_{n,t}(1)
=
\prod_{d=n-t+1}^{n}\rho(d),
$$

where

$$
\rho(d)
=
\begin{cases}
p,&d=p^a\text{ is a prime power},\\
1,&\text{otherwise}.
\end{cases}
$$

## 10.1 Primitive-block determinant

Choose

$$
t\le k_1<\cdots<k_m
\le\left\lfloor\frac n2\right\rfloor.
$$

### Project Theorem 10.1 — Stable-core-reduced Jet–Vandermonde determinant

One has

$$
\boxed{
\det\left(D^rR_{n,t,k_i}(1)\right)_{
\substack{0\le r<m\\1\le i\le m}}
=
\frac{2^{-\binom m2}}{C_{n,t}(1)^m}
\left(\prod_i\binom n{k_i}\right)
\prod_{i<j}(E_j-E_i).
}
$$

In particular, the determinant is nonzero.

### Proof

For every $i$,

$$
G_i=C_{n,t}R_i.
$$

The Leibniz rule gives

$$
D^rG_i(1)
=
\sum_{s=0}^{r}
\binom rs
D^{r-s}C_{n,t}(1)
D^sR_i(1).
$$

Thus the Gaussian jet matrix is obtained from the primitive-quotient jet matrix by left multiplication by one lower triangular matrix whose diagonal entries are all

$$
C_{n,t}(1).
$$

Its determinant is

$$
C_{n,t}(1)^m.
$$

Apply Theorem 6.2 and divide. ∎

## 10.2 Primitive-block contact rigidity

### Corollary 10.2 — Sharp contact after removal of mandatory content

If

$$
0\ne
\sum_{i=1}^{m}c_iR_{n,t,k_i}(q),
$$

then

$$
\boxed{
\operatorname{ord}_{q=1}
\left(
\sum_i c_iR_{n,t,k_i}(q)
\right)
\le m-1.
}
$$

The bound is sharp for every selected set of indices.

### Proof

Multiplication by the common factor $C_{n,t}(q)$, which is a unit at $q=1$, preserves vanishing order. Therefore

$$
\operatorname{ord}_{q=1}
\left(C_{n,t}\sum_i c_iR_i\right)
=
\operatorname{ord}_{q=1}
\left(\sum_i c_iR_i\right).
$$

But

$$
C_{n,t}\sum_i c_iR_i
=
\sum_i c_iG_i.
$$

Apply Theorem 7.1 and the extremal construction from Theorem 8.2. ∎

## 10.3 Combined structural interpretation

Part II and the present chapter control two independent layers of the same Gaussian block.

Part II determines the mandatory global factor:

$$
\boxed{
\text{every retained row entry contains }
\prod_{d=n-t+1}^{n}\Phi_d(q).
}
$$

Part XIV determines the residual positive-endpoint cancellation capacity:

$$
\boxed{
\text{after removal of the mandatory factor, an }m\text{-term combination has contact at most }m-1.
}
$$

The combined decomposition is

$$
\boxed{
\text{stable cyclotomic content}
\quad+
\text{optimal one-point jet rigidity}.
}
$$

---

# 11. Arithmetic consequences of the determinant

The entries

$$
D^rG_{n,k}(1)
$$

are integers because $G_{n,k}(q)\in\mathbb Z[q]$ and the Euler derivation preserves integral coefficients.

Therefore the exact determinant formula produces divisibility statements.

## 11.1 A universal binary divisibility

### Project Corollary 11.1 — Gaussian Vandermonde divisibility

For every

$$
0\le k_1<\cdots<k_m\le\left\lfloor\frac n2\right\rfloor,
$$

one has

$$
\boxed{
2^{\binom m2}
\mid
\left(\prod_{i=1}^{m}\binom n{k_i}\right)
\prod_{i<j}(E_j-E_i).
}
$$

Equivalently,

$$
\boxed{
2^{\binom m2}
\mid
\left(\prod_i\binom n{k_i}\right)
\prod_{i<j}(k_j-k_i)(n-k_i-k_j).
}
$$

### Proof

By Theorem 6.2,

$$
2^{-\binom m2}
\left(\prod_i\binom n{k_i}\right)
\prod_{i<j}(E_j-E_i)
$$

is the determinant of an integer matrix. Hence it is an integer. ∎

This divisibility is not inserted artificially. It is forced by the integrality of the Gaussian jet lattice.

## 11.2 Consecutive blocks

Take

$$
k_i=a+i-1,
\qquad
1\le i\le m,
$$

with

$$
0\le a
\quad\text{and}\quad
a+m-1\le\left\lfloor\frac n2\right\rfloor.
$$

Then

$$
k_j-k_i=j-i,
$$

and

$$
n-k_i-k_j
=
n-2a-i-j+2.
$$

### Corollary 11.2 — Consecutive Gaussian jet determinant

$$
\boxed{
\det\left(D^r{n\brack a+i-1}_q\big|_{q=1}\right)
=
2^{-\binom m2}
\left(\prod_{i=1}^{m}\binom n{a+i-1}\right)
\prod_{i<j}(j-i)(n-2a-i-j+2).
}
$$

For the initial block $a=0$, this becomes

$$
\boxed{
2^{-\binom m2}
\left(\prod_{i=0}^{m-1}\binom ni\right)
\prod_{0\le i<j\le m-1}(j-i)(n-i-j).
}
$$

## 11.3 Lattice index interpretation

The normalized jet matrix

$$
\left(p_{r,n}(E_i)\right)
$$

is rational, while the unnormalized Gaussian jet matrix is integral. The determinant measures the covolume of the row-value lattice inside its positive-endpoint jet lattice.

The exact factorization

$$
\boxed{
\text{binomial residuals}
\times
\text{spectral Vandermonde}
\times
2^{-\binom m2}
}
$$

separates the arithmetic size of the row values from the geometric separation of the degree nodes.

---

# 12. Relation to factorial-circuit multiplicity

Part XIII introduced the optimal common-depth capacity

$$
C_1^{\mathrm{cd}}(m,S)
$$

for general positive-endpoint factorial circuits with top fan-in at most $m$ and endpoint complexity at most $S$.

The Gaussian-row family does not lie in the globally solved one-endpoint regime. For selected indices $k_i$, the collective endpoint set may contain

$$
n,
\quad
k_1,\ldots,k_m,
\quad
n-k_1,\ldots,n-k_m,
$$

and therefore may grow linearly with $m$.

A generic endpoint-count estimate does not explain the sharp capacity $m-1$.

The new theorem identifies the missing mechanism:

$$
\boxed{
\text{many factorial endpoints}
\quad\text{collapse onto one spectral parameter }E=k(n-k).
}
$$

The logarithmic cumulants are not independent endpoint moments. They lie on a polynomial curve in cumulant space:

$$
E
\longmapsto
\left(
\frac E2,
\frac{B_2}{2}Q_{1,n}(E),
0,
\frac{B_4}{4}Q_{2,n}(E),
0,
\ldots
\right).
$$

The degree filtration of this curve forces the Vandermonde determinant.

### Project Conclusion 12.1 — Structured arbitrary-rank closure

For Gaussian-row circuits, the arbitrary-rank positive-endpoint multiplicity problem is completely solved:

$$
\boxed{
\max_{0\ne F\in\operatorname{span}\{G_{n,k_1},\ldots,G_{n,k_m}\}}
\operatorname{ord}_{q=1}F
=m-1.
}
$$

This holds for every $n$, every $m$, and every set of distinct Gaussian symmetry classes.

## 12.1 What remains open

The theorem does not prove the general conjecture

$$
C_1^{\mathrm{cd}}(m,S)
=(m-1)\gamma(S)
$$

for arbitrary factorial circuits.

Its proof uses three special Gaussian features:

1. a common numerator endpoint $n$;
2. complementary denominator endpoints $k$ and $n-k$;
3. reciprocity, which collapses the local data to $E=k(n-k)$.

A general factorial circuit need not admit any one-dimensional spectral parametrization.

The reusable theorem is therefore the abstract Jet–Vandermonde principle from Section 4:

> Whenever a structured factorial subfamily has an affine first cumulant and subcritical polynomial degree in every higher cumulant, sharp arbitrary-rank contact follows automatically.

This provides a concrete strategy for discovering further solved subclasses.

---

# 13. Sharp model examples

## 13.1 Three-term row circuit

Choose

$$
0\le k_1<k_2<k_3\le\left\lfloor\frac n2\right\rfloor.
$$

Set

$$
E_i=k_i(n-k_i).
$$

The weights

$$
w_i
=
\frac1{(E_i-E_j)(E_i-E_\ell)},
\qquad
\{i,j,\ell\}=\{1,2,3\},
$$

give

$$
H(q)
=
\sum_{i=1}^{3}
\frac{w_i}{\binom n{k_i}}{n\brack k_i}_q.
$$

Then

$$
H(1)=0,
\qquad
DH(1)=0,
$$

but

$$
D^2H(1)=\frac14.
$$

Thus every three selected Gaussian row entries admit a nonzero combination of exact contact two, and no nonzero combination has contact three.

## 13.2 Full lower-half row

Let

$$
m=\left\lfloor\frac n2\right\rfloor+1
$$

and choose

$$
k_i=i-1.
$$

Then the entire set of distinct Gaussian coefficients in row $n$ is determined by the first $m$ jets at $q=1$.

Every linear combination of the full row satisfies

$$
\boxed{
F\ne0
\quad\Longrightarrow\quad
\operatorname{ord}_{q=1}F
\le\left\lfloor\frac n2\right\rfloor.
}
$$

The bound is attained by the barycentric extremizer.

This is dramatically smaller than the largest polynomial degree in the row,

$$
\left\lfloor\frac{n^2}{4}\right\rfloor.
$$

Thus the Gaussian-row local capacity grows linearly in $n$, while the ambient polynomial degree grows quadratically.

## 13.3 Stable-block primitive extremizer

In the stable range, let

$$
R_i(q)
=
\frac{{n\brack k_i}_q}{C_{n,t}(q)}.
$$

Using the same barycentric weights but replacing the residual normalization by

$$
R_i(1)
=
\frac{\binom n{k_i}}{C_{n,t}(1)},
$$

one obtains a primitive-block combination with exact order $m-1$.

Thus removal of the terminal cyclotomic interval changes the leading scalar but not the sharp contact capacity.

---

# 14. Algorithmic certificates

## 14.1 Nonidentity certificate

A nonidentity certificate for

$$
F(q)=\sum_i a_i\widetilde G_i(q)
$$

is a pair

$$
(r,J),
\qquad
0\le r<m,
\qquad
J=D^rF(1)\ne0.
$$

A verifier recomputes the collapsed cumulants and Bell recurrence only through order $r$.

## 14.2 Identity certificate

An identity certificate is the finite packet

$$
\boxed{
D^rF(1)=0
\qquad(0\le r<m).
}
$$

The verifier checks the $m$ exact equalities and invokes Theorem 7.1.

No degree bound, polynomial expansion, or evaluation at another point is required.

## 14.3 Reconstruction certificate

A reconstruction certificate consists of:

1. the distinct spectral nodes
   $$
   E_i=k_i(n-k_i);
   $$
2. the first $m$ jets;
3. the recovered moment vector;
4. the recovered coefficient vector.

Verification consists of two triangular/Vandermonde matrix multiplications.

### Software Corollary 14.1 — Proof-carrying Gaussian-row arithmetic

Every exact identity, nonidentity, and coefficient-recovery claim for a normalized Gaussian-row circuit admits a certificate whose length is polynomial in the compressed input size and in the top fan-in.

---

# 15. Boundaries and exact status

## 15.1 Characteristic zero

The proof uses:

- rational Bernoulli and Faulhaber formulas;
- division by powers of two;
- nonvanishing of ordinary Vandermonde determinants.

The stated theorem is therefore a characteristic-zero result.

Reduction modulo a prime may cause the determinant to vanish when the prime divides

$$
2
\prod_i\binom n{k_i}
\prod_{i<j}(E_j-E_i).
$$

A modular theory requires separate hypotheses.

## 15.2 Distinct symmetry classes

The restriction

$$
0\le k_i\le\left\lfloor\frac n2\right\rfloor
$$

chooses one representative from every reciprocal pair.

If both $k$ and $n-k$ are included, then

$$
{n\brack k}_q={n\brack n-k}_q
$$

identically, and no nonsingular determinant is possible.

The essential condition is that the spectral values

$$
E_i=k_i(n-k_i)
$$

be distinct.

## 15.3 Local statement

The contact theorem concerns the endpoint $q=1$. It does not determine collision multiplicity at a general primitive root of unity. At other cyclotomic contexts, residue defects and chiral cumulants enter, and the one-parameter collapse may fail.

## 15.4 Priority boundary

The chapter establishes the theorem internally from the preceding CCA machinery. It does not by itself establish external literature priority for the exact determinant formula or its multiplicity consequences.

## 15.5 Polynomial-time boundary

The normalized Gaussian-row identity test is bit-polynomial in compressed input size. For unnormalized coefficients, materialized binomial residuals may have bit length proportional to $n$. The chapter does not claim a sub-output-size materialization algorithm.

---

# 16. Theorem inventory

| No. | Result | Status | Main consequence |
|---:|---|---|---|
| 2.1 | Exact normalized Gaussian germ | Project proposition | Expresses the full local germ by power-sum defects |
| 3.1 | Two-root power recurrence | Classical lemma | Gives elementary symmetric degree control |
| 3.2 | Gaussian cumulant collapse | Project lemma | Every even cumulant is polynomial in $E=k(n-k)$ |
| 4.1 | Polynomial-cumulant jet degree | New project theorem | Jets have exact parameter degree |
| 4.2 | Abstract Jet–Vandermonde determinant | New project theorem | Converts cumulant degree into exact determinants |
| 5.1 | Gaussian jet-polynomial theorem | New project theorem | The $r$-th normalized jet has degree $r$ in $E$ |
| 5.2 | Bell recurrence | Project proposition | Exact non-expanding jet computation |
| 6.2 | Gaussian Jet–Vandermonde Theorem | Main new theorem | Closed determinant for arbitrary selected row entries |
| 6.3 | Ordinary Wronskian form | Corollary | Same determinant for ordinary derivatives |
| 6.4 | Initial-minor positivity | Corollary | Local sign-regularity of the ordered row |
| 7.1 | Sharp arbitrary-rank row contact | Main new theorem | Every nonzero $m$-term combination has order at most $m-1$ |
| 8.2 | Explicit maximal-contact combination | New project theorem | Sharpness for every selected set |
| 8.3 | Complete contact filtration | New project theorem | Vanishing-depth strata have dimensions $m-r$ |
| 9.1 | One-point jet isomorphism | New project theorem | First $m$ jets reconstruct every row circuit |
| 9.3 | Exact reconstruction algorithm | Algorithmic theorem | Jet-to-moment-to-coefficient recovery |
| 9.5 | Normalized Gaussian-row PIT | Algorithmic theorem | Deterministic bit-polynomial identity test |
| 10.1 | Stable-core-reduced determinant | New project theorem | Synthesizes Parts II and XIV |
| 11.1 | Gaussian Vandermonde divisibility | New arithmetic corollary | Forces a universal power-of-two divisor |

---

# 17. Final synthesis

Part II established exact pairwise and stable-block arithmetic:

$$
\boxed{
\text{Gaussian row}
\longrightarrow
\text{cyclotomic content and spacing}.
}
$$

Part XIII established sharp positive-endpoint multiplicity in the first effective factorial-circuit regimes:

$$
\boxed{
\text{compressed factorial circuit}
\longrightarrow
\text{bounded local contact}.
}
$$

The present chapter finds a stronger structure inside an entire Gaussian row.

The normalized local germ satisfies

$$
\boxed{
\frac{{n\brack k}_{e^x}}{\binom nk}
=
\mathcal U_n\bigl(k(n-k),x\bigr).
}
$$

Its $r$-th jet is

$$
\boxed{
2^{-r}E^r+	ext{lower powers of }E.
}
$$

Therefore every finite Gaussian jet matrix is a disguised Vandermonde matrix:

$$
\boxed{
\det J
=
2^{-\binom m2}
\left(\prod_i\binom n{k_i}\right)
\prod_{i<j}(E_j-E_i).
}
$$

This closes arbitrary-rank contact for Gaussian-row circuits:

$$
\boxed{
F\ne0
\quad\Longrightarrow\quad
\operatorname{ord}_{q=1}F\le m-1.
}
$$

The bound is exact, every contact order occurs, and the first $m$ jets form a complete coordinate system.

The decisive conceptual advance is

$$
\boxed{
\text{a multi-endpoint factorial family can have minimum contact capacity when its cumulants collapse onto one polynomial spectral coordinate.}
}
$$

The decisive computational consequence is

$$
\boxed{
\text{an }m\text{-term normalized Gaussian-row identity is decided by exactly }m\text{ jets at one point.}
}
$$

And the combined global-local picture is

$$
\boxed{
\text{mandatory stable cyclotomic content}
\quad+
\text{sharp residual Jet–Vandermonde rigidity}.
}
$$
