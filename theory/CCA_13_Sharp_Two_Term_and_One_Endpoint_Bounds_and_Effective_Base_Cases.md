# Cyclotomic Coefficient Arithmetic

## Part XIII — Sharp Two-Term and One-Endpoint Bounds and Effective Base Cases

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete theorem chapter  
**Scope:** Positive-endpoint local normal forms, sharp multiplicity of zero-depth factorial ratios, exact two-term factorial-circuit collisions, exact arbitrary-rank one-endpoint capacity, corrected multiplicity conjecture, and deterministic bit-polynomial identity tests for the resulting effective subclasses.

---

# 0. Purpose and exact status

Part XII proved that, for fixed cyclotomic order, top fan-in, and endpoint complexity, every nonzero factorial circuit has finite local contact capacity. Its Noetherian proof does not supply a polynomial bound for the general arbitrary-rank class.

The present chapter takes the next effective step at the positive endpoint

\[
q=1.
\]

It solves two complete boundary regimes.

1. **Two summands, arbitrarily many endpoints.**  
   Every nonzero two-term circuit has an explicit sharp excess-contact bound.

2. **Arbitrarily many summands, at most one factorial endpoint.**  
   Every common-depth circuit reduces to a sparse Laurent polynomial, giving the exact capacity \(m-1\) and a deterministic bit-polynomial test.

The main sharp function is

\[
\boxed{
\gamma(S)=
\begin{cases}
1,&S=0\text{ or }S=1,\\[1mm]
2S-2,&S\ge2.
\end{cases}}
\]

The principal theorems are

\[
\boxed{
C^{\mathrm{cd}}_1(2,S)=\gamma(S)
}
\]

and

\[
\boxed{
C^{\mathrm{cd}}_1(m,0)=C^{\mathrm{cd}}_1(m,1)=m-1.
}
\]

Here \(C^{\mathrm{cd}}_1(m,S)\) denotes the optimal excess-contact constant for common-depth circuits at \(q=1\).

The chapter also proves the universal lower bound

\[
\boxed{
C^{\mathrm{cd}}_1(m,S)\ge (m-1)\gamma(S),
}
\]

which leads to the corrected sharp conjecture

\[
\boxed{
C^{\mathrm{cd}}_1(m,S)=(m-1)\gamma(S).
}
\]

This conjecture is proved here when

- \(m\le2\);
- \(S\le1\);
- or the exponent vectors lie on one affine multiplicative line, by Part XII.

It remains open for genuinely higher-rank circuits with

\[
m\ge3,
\qquad
S\ge2.
\]

Thus this chapter proves genuine deterministic polynomial-time subclasses, but does **not** claim the full arbitrary-rank polynomial-time theorem.

---

# 1. Factorial circuits at the positive endpoint

Let

\[
(q;q)_A=\prod_{n=1}^{A}(1-q^n),
\qquad
(q;q)_0=1.
\]

A compressed factorial term is

\[
T(q)=q^\alpha\prod_{j=1}^{S}(q;q)_{A_j}^{e_j},
\]

where

\[
\alpha,e_j\in\mathbb Z,
\qquad
0<A_1<\cdots<A_S.
\]

Negative exponents are permitted; hence a term may be a rational function.

At \(q=1\), the cyclotomic depth is

\[
\boxed{
h(T)=v_{q-1}(T)=\sum_{j=1}^{S}e_jA_j.
}
\]

Indeed, every factor \(1-q^n\) has a simple zero at \(q=1\), so

\[
v_{q-1}((q;q)_A)=A.
\]

A factorial circuit is

\[
F(q)=\sum_{i=1}^{r}c_iT_i(q),
\qquad
1\le r\le m,
\qquad
c_i\in\mathbb Q^\times.
\]

## Definition 1.1 — Common depth

The circuit has **common depth** \(h\) at \(q=1\) if

\[
h(T_i)=h
\qquad
(1\le i\le r).
\]

## Definition 1.2 — Optimal common-depth excess capacity

Let \(C^{\mathrm{cd}}_1(m,S)\) be the least integer \(C\ge0\) such that every nonzero common-depth circuit with at most \(m\) terms and endpoint complexity at most \(S\) satisfies

\[
\boxed{
\operatorname{ord}_{q=1}F\le h+C.
}
\]

Part XII proves that this number is finite. The purpose here is to determine it exactly in the first effective regimes.

---

# 2. Exact positive-endpoint factorial normal form

Use the exponential coordinate

\[
q=e^x.
\]

Then

\[
q-1=x+O(x^2),
\]

so \(x\)-order and \((q-1)\)-order coincide.

For \(k\ge0\), write

\[
S_k(A)=\sum_{n=1}^{A}n^k,
\qquad
S_k(0)=0.
\]

In particular,

\[
S_0(A)=A.
\]

We use the Bernoulli convention

\[
\frac{z}{e^z-1}=\sum_{n\ge0}B_n\frac{z^n}{n!},
\qquad
B_1=-\frac12.
\]

## Lemma 2.1 — Regularized one-factor expansion

For every positive integer \(n\),

\[
\boxed{
\log\frac{1-e^{nx}}{-nx}
=
\frac{nx}{2}
+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}(nx)^{2r}.
}
\]

### Proof

Since

\[
1-e^y=-2e^{y/2}\sinh(y/2),
\]

we have

\[
\frac{1-e^y}{-y}
=
e^{y/2}\frac{\sinh(y/2)}{y/2}.
\]

The second factor is even and has constant term one, so its logarithm contains only even powers.

To identify the coefficients, differentiate:

\[
\frac{d}{dy}\log\frac{e^y-1}{y}
=
\frac{e^y}{e^y-1}-\frac1y.
\]

The Bernoulli generating series gives

\[
\frac{e^y}{e^y-1}-\frac1y
=
\frac12+
\sum_{r\ge1}\frac{B_{2r}}{(2r)!}y^{2r-1}.
\]

Integrating and using zero constant term yields

\[
\log\frac{e^y-1}{y}
=
\frac y2+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}y^{2r}.
\]

Because

\[
\frac{1-e^y}{-y}=\frac{e^y-1}{y},
\]

substitute \(y=nx\). ∎

## Proposition 2.2 — Exact factorial germ at \(q=1\)

For every \(A\ge0\),

\[
\boxed{
(q;q)_A\big|_{q=e^x}
=
(-1)^AA!x^A
\exp\left(
\frac{S_1(A)}2x
+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}S_{2r}(A)x^{2r}
\right).
}
\]

### Proof

Write

\[
(q;q)_A\big|_{q=e^x}
=
\prod_{n=1}^{A}(1-e^{nx}).
\]

For each factor,

\[
1-e^{nx}
=(-nx)
\exp\left(
\frac{nx}{2}
+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}(nx)^{2r}
\right)
\]

by Lemma 2.1. Multiplying the leading terms gives

\[
\prod_{n=1}^{A}(-nx)=(-1)^AA!x^A.
\]

The logarithmic exponents add. Their linear sum is

\[
\frac12\sum_{n=1}^{A}n=\frac{S_1(A)}2,
\]

and their \(2r\)-th sum is

\[
\sum_{n=1}^{A}n^{2r}=S_{2r}(A).
\]

This proves the formula. ∎

## Corollary 2.3 — Exact term normal form

Let

\[
T(q)=q^\alpha\prod_{j=1}^{S}(q;q)_{A_j}^{e_j}
\]

and put

\[
h=\sum_j e_jA_j.
\]

Then

\[
\boxed{
T(e^x)
=
b(T)x^h
\exp\left(
\lambda(T)x+
\sum_{r\ge1}c_rM_{2r}(T)x^{2r}
\right),
}
\]

where

\[
\boxed{
b(T)=(-1)^h\prod_{j=1}^{S}(A_j!)^{e_j},
}
\]

\[
\boxed{
\lambda(T)=
\alpha+
\frac12\sum_{j=1}^{S}e_jS_1(A_j),
}
\]

\[
\boxed{
M_{2r}(T)=\sum_{j=1}^{S}e_jS_{2r}(A_j),
}
\]

and

\[
\boxed{
c_r=\frac{B_{2r}}{2r(2r)!}\ne0.
}
\]

### Proof

Apply Proposition 2.2 to every factorial factor and multiply by

\[
q^\alpha=e^{\alpha x}.
\]

The depth, leading constant, linear exponent, and even logarithmic moments add with multiplicities \(e_j\). The even Bernoulli numbers are nonzero, hence \(c_r\ne0\). ∎

---

# 3. Zero-depth ratios and logarithmic fingerprints

Let

\[
R(q)=q^\beta\prod_{j=1}^{s}(q;q)_{a_j}^{e_j},
\qquad
0<a_1<\cdots<a_s,
\]

be canonical, meaning every \(e_j\ne0\).

Assume

\[
\boxed{
v_{q-1}(R)=\sum_{j=1}^{s}e_ja_j=0.
}
\]

Then \(R\) is a local unit at \(q=1\). Define its positive-endpoint residual by

\[
\boxed{
B(R)=\lim_{x\to0}R(e^x).
}
\]

Corollary 2.3 gives

\[
\boxed{
B(R)=\prod_{j=1}^{s}(a_j!)^{e_j}\in\mathbb Q_{>0}.
}
\]

The sign disappears because the zero-depth relation makes

\[
(-1)^{\sum e_ja_j}=1.
\]

Define the normalized logarithmic germ

\[
L_R(x)=\log\frac{R(e^x)}{B(R)}.
\]

## Proposition 3.1 — Complete positive-endpoint ratio fingerprint

One has

\[
\boxed{
L_R(x)
=
\Lambda(R)x+
\sum_{r\ge1}c_rM_{2r}(R)x^{2r},
}
\]

where

\[
\boxed{
\Lambda(R)=
\beta+
\frac12\sum_{j=1}^{s}e_jS_1(a_j)
}
\]

and

\[
\boxed{
M_{2r}(R)=\sum_{j=1}^{s}e_jS_{2r}(a_j).
}
\]

There are no odd logarithmic terms beyond the linear drift.

### Proof

Apply Corollary 2.3 with depth zero and divide by the leading constant. Taking the formal logarithm removes the outer exponential. ∎

## Lemma 3.2 — Exponential order preservation

If

\[
0\ne L(x)\in xK[[x]]
\]

for a characteristic-zero field \(K\), then

\[
\boxed{
\operatorname{ord}_x(e^{L(x)}-1)
=
\operatorname{ord}_xL(x).
}
\]

### Proof

Factor

\[
e^L-1=L\left(1+\frac L{2!}+\frac{L^2}{3!}+\cdots\right).
\]

The parenthesized factor has constant term one and is therefore a unit. ∎

## Corollary 3.3 — Exact first-mismatch rule

If \(R\not\equiv B(R)\), then

\[
\boxed{
\operatorname{ord}_{q=1}
\left(\frac{R(q)}{B(R)}-1\right)
=
\operatorname{ord}_xL_R(x).
}
\]

Consequently:

1. if \(\Lambda(R)\ne0\), the order is exactly \(1\);
2. if \(\Lambda(R)=0\), the order is the least \(2r\) for which
   \[
   M_{2r}(R)\ne0.
   \]

### Proof

The normalized ratio equals \(e^{L_R(x)}\). Apply Lemma 3.2 and use

\[
q-1=x+O(x^2).
\]

∎

---

# 4. The nested cumulative-moment determinant

The next determinant is the rigidity mechanism behind the explicit endpoint bound.

## Theorem 4.1 — Strict cumulative-moment determinant

Let

\[
0<a_1<\cdots<a_s
\]

be positive integers. Then

\[
\boxed{
\det\bigl(S_{2r}(a_i)\bigr)_{
0\le r\le s-1,
1\le i\le s}
>0.
}
\]

In particular, the matrix is invertible over \(\mathbb Q\).

### Proof

Let \(N=a_s\). Define the \(s\times N\) matrix

\[
V_{r,n}=n^{2r},
\qquad
0\le r\le s-1,
\qquad
1\le n\le N,
\]

and the \(N\times s\) incidence matrix

\[
H_{n,i}=\mathbf 1_{n\le a_i}.
\]

Then

\[
(VH)_{r,i}
=
\sum_{n=1}^{N}n^{2r}\mathbf1_{n\le a_i}
=
S_{2r}(a_i).
\]

Hence the desired matrix is \(VH\).

By the Cauchy--Binet formula,

\[
\det(VH)
=
\sum_{1\le n_1<\cdots<n_s\le N}
\det\bigl(n_j^{2r}\bigr)_{r,j}
\det\bigl(H_{n_j,i}\bigr)_{j,i}.
\]

The first determinant is the Vandermonde determinant in the strictly increasing positive numbers

\[
n_1^2<\cdots<n_s^2:
\]

\[
\det\bigl(n_j^{2r}\bigr)_{0\le r<s,1\le j\le s}
=
\prod_{1\le u<v\le s}(n_v^2-n_u^2)>0.
\]

The incidence determinant is either zero or one. Indeed, every row of

\[
\bigl(H_{n_j,i}\bigr)
\]

consists of an initial block of zeros followed by ones. It has determinant one exactly when

\[
\boxed{
a_{j-1}<n_j\le a_j
\qquad(1\le j\le s),
}
\]

where \(a_0=0\); otherwise two rows have the same first nonzero position or the matrix is rank deficient.

At least one admissible tuple exists: choose

\[
n_j=a_{j-1}+1.
\]

Therefore every nonzero Cauchy--Binet summand is positive and at least one is positive. Hence the total determinant is strictly positive. ∎

## Corollary 4.2 — Endpoint moment rigidity

If numbers \(e_1,\ldots,e_s\in\mathbb Q\) satisfy

\[
\sum_{i=1}^{s}e_iS_0(a_i)=0
\]

and

\[
\sum_{i=1}^{s}e_iS_{2r}(a_i)=0
\qquad
(1\le r\le s-1),
\]

then

\[
\boxed{e_1=\cdots=e_s=0.}
\]

### Proof

The displayed equations say that the vector \((e_i)^T\) lies in the kernel of the invertible matrix from Theorem 4.1. ∎

---

# 5. Sharp multiplicity of one zero-depth ratio

Recall

\[
\gamma(S)=
\begin{cases}
1,&S\le1,\\
2S-2,&S\ge2.
\end{cases}
\]

## Theorem 5.1 — Sharp positive-endpoint ratio bound

Let

\[
R(q)=q^\beta\prod_{j=1}^{s}(q;q)_{a_j}^{e_j}
\]

be a nonconstant canonical factorial ratio with

\[
v_{q-1}(R)=0.
\]

Then

\[
\boxed{
\operatorname{ord}_{q=1}
\left(\frac{R(q)}{B(R)}-1\right)
\le\gamma(s).
}
\]

More precisely:

1. if \(\Lambda(R)\ne0\), the order is \(1\);
2. if \(\Lambda(R)=0\) and \(s\ge2\), the order is the least \(2r\), with
   \[
   1\le r\le s-1,
   \]
   such that
   \[
   M_{2r}(R)\ne0.
   \]

### Proof

If \(s=0\), then

\[
R(q)=q^\beta.
\]

Nonconstancy gives \(\beta\ne0\), and

\[
q^\beta-1=\beta(q-1)+O((q-1)^2),
\]

so the order is one.

If \(s=1\), the zero-depth condition is

\[
e_1a_1=0.
\]

Since \(a_1>0\), this forces \(e_1=0\). Canonicalization removes the factorial endpoint, reducing again to the monomial case. Hence the order is one.

Assume \(s\ge2\). If \(\Lambda(R)\ne0\), Corollary 3.3 gives exact order one.

Now suppose \(\Lambda(R)=0\). The zero-depth condition is

\[
M_0(R)=\sum_{j=1}^{s}e_ja_j=0.
\]

Suppose for contradiction that

\[
M_2(R)=M_4(R)=\cdots=M_{2s-2}(R)=0.
\]

Then Corollary 4.2 gives

\[
e_1=\cdots=e_s=0.
\]

The drift equation becomes

\[
\Lambda(R)=\beta=0.
\]

Thus \(R\equiv1\), contradicting nonconstancy.

Therefore some

\[
M_{2r}(R)\ne0,
\qquad
1\le r\le s-1.
\]

Corollary 3.3 says that the first such moment gives the exact order, which is at most \(2s-2\). ∎

## Theorem 5.2 — Sharpness for every endpoint complexity

For every \(S\ge0\), there is a nonconstant zero-depth factorial ratio with endpoint complexity at most \(S\) satisfying

\[
\boxed{
\operatorname{ord}_{q=1}
\left(\frac{R(q)}{B(R)}-1\right)
=\gamma(S).
}
\]

### Proof

For \(S=0\) or \(S=1\), take

\[
R(q)=q.
\]

It has zero factorial depth, residual one, and contact order one.

Let \(S\ge2\), and fix any endpoint set

\[
0<a_1<\cdots<a_S.
\]

Consider the \((S-1)\times S\) matrix

\[
\bigl(S_{2r}(a_i)\bigr)_{
0\le r\le S-2,
1\le i\le S}.
\]

By Theorem 4.1 it has rank \(S-1\), so its nullspace is one-dimensional. Choose a nonzero rational vector

\[
(e_1,\ldots,e_S)
\]

in that nullspace and scale it to be integral. Then

\[
\sum_i e_i a_i=0
\]

and

\[
\sum_i e_iS_{2r}(a_i)=0
\qquad
(1\le r\le S-2).
\]

Because the full \(S\times S\) matrix of Theorem 4.1 is invertible,

\[
\sum_i e_iS_{2S-2}(a_i)\ne0.
\]

Multiply the exponent vector by two if necessary so that

\[
\beta=-\frac12\sum_i e_iS_1(a_i)
\]

is an integer. Then the corresponding ratio has

\[
\Lambda(R)=0,
\]

all even moments through order \(2S-4\) vanish, and the moment of order \(2S-2\) is nonzero. Theorem 5.1 gives exact contact \(2S-2\). ∎

---

# 6. Exact two-term collision theorem

Let

\[
F(q)=c_1T_1(q)+c_2T_2(q),
\qquad
c_1,c_2\in\mathbb Q^\times,
\]

where the union of the factorial endpoints of \(T_1,T_2\) has size at most \(S\).

Write

\[
h_i=v_{q-1}(T_i).
\]

## Theorem 6.1 — Complete two-term positive-endpoint collision law

Assume \(F\not\equiv0\).

### Different depths

If

\[
h_1\ne h_2,
\]

then

\[
\boxed{
\operatorname{ord}_{q=1}F=\min(h_1,h_2).
}
\]

### Equal depths

Suppose

\[
h_1=h_2=h.
\]

Set

\[
R(q)=\frac{T_1(q)}{T_2(q)}
\]

and

\[
B=B(R)=\lim_{q\to1}R(q).
\]

Then:

1. if
   \[
   c_2+c_1B\ne0,
   \]
   then
   \[
   \boxed{\operatorname{ord}_{q=1}F=h;}
   \]

2. if
   \[
   c_2+c_1B=0,
   \]
   then \(R\) is nonconstant and
   \[
   \boxed{
   \operatorname{ord}_{q=1}F
   =
   h+
   \operatorname{ord}_{q=1}
   \left(\frac{R(q)}B-1\right)
   \le h+\gamma(S).
   }
   \]

In the second case the excess order is classified exactly by the drift and moments of Section 3.

### Proof

Use the local forms

\[
T_i(e^x)=b_ix^{h_i}U_i(x),
\qquad
b_i\ne0,
\qquad
U_i(0)=1.
\]

If \(h_1<h_2\), then

\[
F(e^x)
=
x^{h_1}
\left(c_1b_1U_1(x)+x^{h_2-h_1}c_2b_2U_2(x)\right).
\]

The parenthesized series has nonzero constant term \(c_1b_1\). Hence the order is \(h_1\). The other inequality is symmetric.

Now assume \(h_1=h_2=h\). Factor \(T_2\):

\[
F=T_2(c_2+c_1R).
\]

The ratio \(R\) has depth zero and local residual

\[
B=\frac{b_1}{b_2}.
\]

If \(c_2+c_1B\ne0\), the second factor is a local unit, so the order is \(h\).

If \(c_2+c_1B=0\), then

\[
F=c_1T_2(R-B).
\]

Therefore

\[
\operatorname{ord}_{q=1}F
=
h+
\operatorname{ord}_{q=1}(R-B)
=
h+
\operatorname{ord}_{q=1}\left(\frac RB-1\right).
\]

If \(R\) were constant, uniqueness of canonical factorial representations would force \(R\equiv1\), and the coefficient relation would make \(F\equiv0\), contrary to hypothesis. Thus \(R\) is nonconstant, and Theorem 5.1 gives the bound. ∎

## Corollary 6.2 — Sharp two-term capacity

For every \(S\ge0\),

\[
\boxed{
C^{\mathrm{cd}}_1(2,S)=\gamma(S).
}
\]

### Proof

The upper bound is Theorem 6.1.

For sharpness, choose a ratio \(R\) from Theorem 5.2 and set

\[
F(q)=R(q)-B(R).
\]

This is a two-term common-depth circuit of depth zero and has contact exactly \(\gamma(S)\). ∎

## Corollary 6.3 — Pairwise fingerprint certificate

For two equal-depth terms, the complete positive-endpoint collision ladder is:

\[
\boxed{
\begin{array}{c|c}
\text{first mismatch}&\operatorname{ord}_{q=1}F\\
\hline
c_2+c_1B\ne0&h\\
\Lambda(R)\ne0&h+1\\
M_2=\cdots=M_{2r-2}=0,\ M_{2r}\ne0&h+2r
\end{array}}
\]

with

\[
2r\le2S-2
\]

in the final row.

---

# 7. Arbitrary rank with no factorial endpoint

If \(S=0\), every term is a Laurent monomial

\[
T_i(q)=q^{\alpha_i}.
\]

After combining equal exponents, write

\[
P(q)=\sum_{\nu=1}^{t}d_\nu q^{a_\nu},
\qquad
a_1<\cdots<a_t,
\qquad
d_\nu\ne0.
\]

## Lemma 7.1 — Sparse endpoint contact

If \(P\ne0\), then

\[
\boxed{
\operatorname{ord}_{q=1}P\le t-1.
}
\]

### Proof

Let

\[
D=q\frac d{dq}.
\]

Then

\[
D^jP(1)=\sum_{\nu=1}^{t}d_\nu a_\nu^j.
\]

If the first \(t\) Euler derivatives vanished, then

\[
\sum_{\nu=1}^{t}d_\nu a_\nu^j=0
\qquad
(0\le j<t).
\]

This is the homogeneous system with Vandermonde matrix

\[
(a_\nu^j)_{0\le j<t,1\le\nu\le t}.
\]

Its determinant is

\[
\prod_{\mu<\nu}(a_\nu-a_\mu)\ne0.
\]

Hence every \(d_\nu=0\), a contradiction. Therefore some derivative of order at most \(t-1\) is nonzero. ∎

## Corollary 7.2 — Exact zero-endpoint capacity

For every \(m\ge1\),

\[
\boxed{
C^{\mathrm{cd}}_1(m,0)=m-1.
}
\]

### Proof

Every term has depth zero. Lemma 7.1 gives the upper bound after combining equal exponents.

For sharpness, use

\[
(q-1)^{m-1}
=
\sum_{k=0}^{m-1}
(-1)^{m-1-k}\binom{m-1}{k}q^k.
\]

It has exactly \(m\) nonzero monomials and order \(m-1\) at \(q=1\). ∎

---

# 8. Arbitrary rank with one factorial endpoint

Fix one positive endpoint \(A\). A term has the form

\[
T_i(q)=q^{\alpha_i}(q;q)_A^{e_i}.
\]

Its depth is

\[
h_i=Ae_i.
\]

## Theorem 8.1 — One-endpoint common-depth factorization

Suppose

\[
F(q)=\sum_{i=1}^{r}c_iq^{\alpha_i}(q;q)_A^{e_i}
\]

has common depth \(h\). Then every \(e_i\) is equal to

\[
e=\frac hA,
\]

and

\[
\boxed{
F(q)=(q;q)_A^eP(q),
\qquad
P(q)=\sum_{i=1}^{r}c_iq^{\alpha_i}.
}
\]

### Proof

Common depth gives

\[
Ae_i=h
\]

for every \(i\). Since \(A>0\), all \(e_i=h/A\). Factor the common factorial power. ∎

## Theorem 8.2 — Exact one-endpoint multiplicity theorem

Let \(t\) be the number of distinct monomial exponents remaining after equal powers of \(q\) are combined. If \(F\not\equiv0\), then

\[
\boxed{
\operatorname{ord}_{q=1}F
=
h+
\operatorname{ord}_{q=1}P
\le h+t-1
\le h+m-1.
}
\]

### Proof

The factor \((q;q)_A^e\) has order \(h\). The remaining factor is the nonzero \(t\)-sparse Laurent polynomial \(P\). Apply Lemma 7.1. ∎

## Corollary 8.3 — Exact one-endpoint capacity

For every \(m\ge1\),

\[
\boxed{
C^{\mathrm{cd}}_1(m,1)=m-1.
}
\]

### Proof

The upper bound is Theorem 8.2.

For sharpness, fix any integer \(e\) and use

\[
F(q)=(q;q)_A^e(q-1)^{m-1}.
\]

Its binomial expansion has \(m\) factorial terms, all of common depth

\[
h=eA,
\]

and total order

\[
h+m-1.
\]

∎

## Corollary 8.4 — Correction to the former endpoint conjecture

The formula

\[
2(m-1)(S-1)
\]

cannot be a valid general upper bound at \(S=1\), because it gives zero while

\[
\boxed{C^{\mathrm{cd}}_1(m,1)=m-1.}
\]

The missing direction is the monomial drift \(q^\alpha\), which remains free even when the factorial exponent is forced by common depth.

---

# 9. Universal sharp lower bound and corrected conjecture

The preceding sharp ratios can be composed with sparse outer polynomials.

## Theorem 9.1 — Universal affine-line lower bound

For every \(m\ge1\) and \(S\ge0\),

\[
\boxed{
C^{\mathrm{cd}}_1(m,S)
\ge
(m-1)\gamma(S).
}
\]

### Proof

Choose a zero-depth ratio \(R\) with

\[
\operatorname{ord}_{q=1}
\left(\frac R{B(R)}-1\right)
=
\gamma(S)
\]

from Theorem 5.2.

Define

\[
F(q)=
\left(
\frac{R(q)}{B(R)}-1
\right)^{m-1}.
\]

The binomial expansion contains exactly \(m\) powers of \(R\):

\[
F(q)=
\sum_{k=0}^{m-1}
(-1)^{m-1-k}
\binom{m-1}{k}
B(R)^{-k}R(q)^k.
\]

Every summand has depth zero, and every summand uses only the endpoints already used by \(R\). Therefore this is an admissible common-depth circuit with at most \(m\) terms and endpoint complexity at most \(S\).

Its order is

\[
(m-1)
\operatorname{ord}_{q=1}
\left(
\frac R{B(R)}-1
\right)
=
(m-1)\gamma(S).
\]

∎

## Conjecture 9.2 — Corrected sharp positive-endpoint capacity

For all \(m\ge1\) and \(S\ge0\),

\[
\boxed{
C^{\mathrm{cd}}_1(m,S)
=
(m-1)\gamma(S).
}
\]

Equivalently,

\[
\boxed{
C^{\mathrm{cd}}_1(m,S)
=
\begin{cases}
 m-1,&S=0\text{ or }1,\\[1mm]
 2(m-1)(S-1),&S\ge2.
\end{cases}}
\]

### Proven cases

The conjecture is proved in the following regimes.

1. \(m=1\): trivially \(C=0\).
2. \(m=2\): Corollary 6.2.
3. \(S=0\): Corollary 7.2.
4. \(S=1\): Corollary 8.3.
5. Affine-line exponent families: the effective affine-line theorem of Part XII.

### Remaining case

The unsolved regime is

\[
\boxed{
m\ge3,
\qquad
S\ge2,
}
\]

with exponent vectors spanning more than one affine multiplicative direction.

The lower bound is already sharp on an affine line. What remains is to prove that higher-rank interaction cannot create more contact than the affine-line extremizer.

---

# 10. Deterministic bit-polynomial identity tests in the solved regimes

The original full-class goal is a deterministic algorithm polynomial in the compressed input bit length. The general problem remains open, but the present boundary classes admit such tests.

## 10.1 Two-term global identity

Consider

\[
F(q)=c_1T_1(q)+c_2T_2(q).
\]

Canonicalize each term by combining equal endpoints and deleting zero exponents.

### Theorem 10.1 — Polynomial-time two-term PIT

The circuit is identically zero if and only if

1. the canonical monomial powers of \(T_1,T_2\) agree;
2. their canonical endpoint-exponent maps agree;
3. \(c_1+c_2=0\).

This can be decided in deterministic time polynomial in the compressed input bit length.

### Proof

If the canonical term data agree, then \(T_1=T_2\), and

\[
F=(c_1+c_2)T_1.
\]

Thus \(F=0\) exactly when \(c_1+c_2=0\).

Conversely, suppose \(F=0\). Then

\[
\frac{T_1}{T_2}=-\frac{c_2}{c_1}
\]

is a nonzero rational constant. The uniqueness theorem for compressed factorial representations implies that a quotient of two canonical coefficient-one factorial terms is constant only when their monomial powers and endpoint-exponent maps agree. In that case the quotient is one, and hence \(c_1+c_2=0\).

Canonicalization consists of sorting integer endpoints, adding integer exponents, and exact rational addition. These operations are polynomial in the compressed bit length. ∎

### Caution 10.2

The global two-term identity test is polynomial-time because it avoids evaluating enormous residual factorial products. Computing the **exact local collision order** from the fingerprint may still require comparing a rational coefficient with a compact product of factorials. That separate compact-arithmetic question is not silently resolved here.

## 10.2 Common-depth one-endpoint circuits

By Theorem 8.1,

\[
F=(q;q)_A^eP(q)
\]

with sparse Laurent polynomial

\[
P(q)=\sum_i c_iq^{\alpha_i}.
\]

### Algorithm 10.3 — One-endpoint common-depth PIT

```text
input:
    A
    terms (c_i, alpha_i, e_i)

1. Compute h_i = A*e_i.
2. Verify that all h_i are equal.
3. Group terms by alpha_i and add their rational coefficients.
4. Delete zero coefficient groups.
5. If no groups remain, return IDENTICAL.
6. Otherwise return NONIDENTICAL.
```

### Theorem 10.4 — Correctness and bit complexity

Algorithm 10.3 decides identity in deterministic polynomial bit time.

### Proof

Common depth forces all \(e_i\) equal, so the circuit is a nonzero common factorial factor times the grouped sparse Laurent polynomial. A Laurent polynomial is zero exactly when every grouped coefficient is zero.

The algorithm uses integer multiplication, comparison, sorting or hashing of binary exponents, and exact rational addition. All have polynomial bit complexity in the input size. ∎

## 10.3 Exact local contact in the one-endpoint class

After grouping, let

\[
P(q)=\sum_{\nu=1}^{t}d_\nu q^{a_\nu}.
\]

Compute the moments

\[
\mu_j=\sum_{\nu=1}^{t}d_\nu a_\nu^j,
\qquad
0\le j<t.
\]

The first nonzero \(\mu_j\) is the exact excess contact order.

### Theorem 10.5 — Polynomial-time exact contact

For a nonzero common-depth one-endpoint circuit,

\[
\boxed{
\operatorname{ord}_{q=1}F
=
h+
\min\{j:0\le j<t,\ \mu_j\ne0\}.
}
\]

The value can be computed in deterministic polynomial bit time.

### Proof

Since

\[
D^jP(1)=\mu_j,
\]

the first nonzero moment is the local order. Lemma 7.1 guarantees that it occurs before \(j=t\).

Because \(j<t\le m\), the integer \(a_\nu^j\) has bit length

\[
O(m\log(1+|a_\nu|)).
\]

Thus all moments through order \(t-1\) can be computed with polynomially many arithmetic operations on polynomial-bit-length integers and rationals. ∎

---

# 11. What this does and does not prove about polynomial time

The present chapter proves deterministic bit-polynomial algorithms for:

1. arbitrary two-term factorial-circuit identity;
2. arbitrary-rank common-depth circuits with no factorial endpoint;
3. arbitrary-rank common-depth circuits with one factorial endpoint;
4. exact positive-endpoint contact in the one-endpoint class.

It also proves a sharp explicit multiplicity bound for every two-term collision at \(q=1\).

It does **not** prove deterministic bit-polynomial PIT for general

\[
m\ge3,
\qquad
S\ge2.
\]

Two obstacles remain there.

### Multiplicity obstacle

The corrected conjectural bound is

\[
(m-1)\gamma(S).
\]

Its upper bound is not yet proved for genuinely higher-rank exponent configurations.

### Compact-arithmetic obstacle

Even when only finitely many jets are required, a jet may be a sum of compact products containing enormous factorial powers. A polynomial-time exact zero test for those sums remains unavailable in general.

The contribution of this chapter is to isolate the first genuinely unsolved parameter box:

\[
\boxed{
\text{top fan-in at least three}
\quad+\quad
\text{at least two factorial endpoints}
\quad+\quad
\text{multiplicative rank at least two}.
}
\]

Everything below that box is now effective at the positive endpoint in the senses proved above.

---

# 12. Theorem inventory

| No. | Result | Exact conclusion | Status |
|---:|---|---|---|
| 2.2 | Positive-endpoint factorial normal form | Exact depth, residual, drift, and all even moments | Proved |
| 3.1 | Ratio fingerprint | One linear and then only even logarithmic channels | Proved |
| 4.1 | Cumulative-moment determinant | Strict positivity and endpoint-moment invertibility | Proved |
| 5.1 | Sharp ratio bound | Nonconstant zero-depth ratio has contact at most \(\gamma(S)\) | Proved |
| 5.2 | Ratio sharpness | Every \(\gamma(S)\) is attained | Proved |
| 6.1 | Complete two-term collision law | Exact depth cases and excess bound \(\gamma(S)\) | Proved |
| 6.2 | Exact two-term capacity | \(C^{\mathrm{cd}}_1(2,S)=\gamma(S)\) | Proved |
| 7.2 | Zero-endpoint capacity | \(C^{\mathrm{cd}}_1(m,0)=m-1\) | Proved |
| 8.3 | One-endpoint capacity | \(C^{\mathrm{cd}}_1(m,1)=m-1\) | Proved |
| 9.1 | Universal lower bound | \(C^{\mathrm{cd}}_1(m,S)\ge(m-1)\gamma(S)\) | Proved |
| 9.2 | Corrected sharp capacity | Equality with the lower bound | Conjecture outside solved regimes |
| 10.1 | Two-term PIT | Deterministic polynomial bit time | Proved |
| 10.4 | One-endpoint common-depth PIT | Deterministic polynomial bit time | Proved |
| 10.5 | One-endpoint exact contact | Deterministic polynomial bit time | Proved |

---

# 13. Final synthesis

The positive-endpoint theory now has an exact effective base layer.

For one zero-depth multiplicative direction,

\[
\boxed{
\text{endpoint complexity }S
\Longrightarrow
\text{maximum contact }\gamma(S).
}
\]

For two summands,

\[
\boxed{
C^{\mathrm{cd}}_1(2,S)=\gamma(S).
}
\]

For one or zero factorial endpoints and arbitrary top fan-in,

\[
\boxed{
C^{\mathrm{cd}}_1(m,S)=m-1
\qquad(S\le1).
}
\]

For every \(m,S\), the affine-line construction forces

\[
\boxed{
C^{\mathrm{cd}}_1(m,S)
\ge
(m-1)\gamma(S).
}
\]

The corrected central conjecture is therefore

\[
\boxed{
C^{\mathrm{cd}}_1(m,S)
=(m-1)\gamma(S).
}
\]

The remaining multiplicity problem is no longer vague. It is precisely the assertion that genuinely higher-rank interaction cannot outperform the already sharp affine-line collision.

The remaining complexity problem is likewise precise: after that upper bound is proved, one must still decide bounded sums of compact factorial jet values in deterministic polynomial bit time.

Thus the next frontier is

\[
\boxed{
\text{higher-rank upper bound}
\quad+\quad
\text{compact exact jet arithmetic}.
}
\]

---

## End of Part XIII
