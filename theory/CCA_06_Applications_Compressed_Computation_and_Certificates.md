# Cyclotomic Coefficient Arithmetic

## Part VI — Applications I: Compressed Exact Computation and Cyclotomic Certificates

**Status:** Proof-complete application chapter  
**Scope:** Turning the theory into exact algorithms for enormous structured \(q\)-expressions, rigorous local comparison certificates, stable Gaussian gcd computation, and reusable computer-algebra primitives.

---

## 1. Purpose of this chapter

The first five parts developed a structural theory:

\[
\text{cyclotomic context}
\longrightarrow
\text{vanishing depth}
\longrightarrow
\text{local residual}
\longrightarrow
\text{cumulant and jet hierarchy}.
\]

This chapter turns that theory into an application.

The principal computational problem is the following.

> A structured \(q\)-polynomial may have degree and coefficient count far beyond any feasible expansion. Can one nevertheless compute exact divisibility, local behavior at roots of unity, collision order, and arithmetic gcd data directly from its compressed parameters?

For the families treated in this theory, the answer is yes.

The resulting application is a system of **cyclotomic certificates**. Such a certificate records exact information of the form

\[
(d,h,B,\kappa_1,\kappa_2,\ldots,\kappa_R),
\]

where

- \(d\) specifies the cyclotomic context \(q=\zeta_d\);
- \(h\) is the cyclotomic depth;
- \(B\) is the first nonzero local residual in exponential coordinates;
- \(\kappa_r\) are normalized logarithmic derivatives;
- the first mismatch between two certificates gives the exact local order of collision.

The key application principle is

\[
\boxed{
\text{enormous expanded polynomial}
\quad\rightsquigarrow\quad
\text{small exact structured certificate}.
}
\]

This is useful immediately in:

1. exact computer algebra;
2. verification of large \(q\)-identities and nonidentities;
3. root-of-unity asymptotics;
4. cyclic-sieving computations;
5. Gaussian coefficient gcd calculations;
6. theorem-prover certificates;
7. testing and benchmarking symbolic libraries.

The chapter also distinguishes what is already proved from what remains exploratory. In particular, the present theory does **not** provide a general prime generator or a practical attack on modern cryptography.

---

## 2. The compressed computational model

### 2.1 Compressed \(q\)-factorial quotients

A compressed \(q\)-factorial quotient is an expression

\[
F(q)
=
q^\alpha
\prod_{i=1}^{s}(q;q)_{a_i}^{\varepsilon_i},
\]

where

\[
\alpha\in\mathbb Z,
\qquad
a_i\in\mathbb Z_{\ge0},
\qquad
\varepsilon_i\in\mathbb Z.
\]

The expression may represent a polynomial, a Laurent polynomial, or a rational function. The computational representation is the finite list

\[
\mathcal F=
\bigl(\alpha; (a_1,\varepsilon_1),\ldots,(a_s,\varepsilon_s)\bigr).
\]

Its compressed size depends on \(s\) and on the bit lengths of the integers, not on

\[
\deg F
\quad\text{or}\quad
\#\operatorname{supp}(F).
\]

Gaussian binomials and multinomials are special cases:

\[
{n\brack k}_q
=
(q;q)_n(q;q)_k^{-1}(q;q)_{n-k}^{-1},
\]

and

\[
{n\brack k_1,\ldots,k_c}_q
=
(q;q)_n\prod_{\nu=1}^{c}(q;q)_{k_\nu}^{-1}.
\]

### 2.2 Canonicalization

Combine terms with equal factorial index:

\[
e_m
=
\sum_{i:a_i=m}\varepsilon_i.
\]

Delete every pair with \(e_m=0\). Since

\[
(q;q)_0=1,
\]

terms with index zero may also be removed.

The canonical representation is therefore

\[
F(q)
=
q^\alpha
\prod_{m\in S}(q;q)_m^{e_m},
\]

where \(S\subset\mathbb Z_{>0}\) is finite and every \(e_m\ne0\).

### Application Theorem 2.1 — Uniqueness of the compressed factorial representation

Suppose

\[
q^\alpha\prod_{m\ge1}(q;q)_m^{e_m}
=
q^\beta\prod_{m\ge1}(q;q)_m^{f_m}
\]

as rational functions, where both exponent families have finite support. Then

\[
\boxed{
\alpha=\beta
\quad\text{and}\quad
e_m=f_m\text{ for every }m.
}
\]

Thus canonicalized compressed \(q\)-factorial quotients have unique representations.

#### Proof

Move the right side to the left:

\[
q^{\alpha-\beta}
\prod_{m\ge1}(q;q)_m^{g_m}
=1,
\qquad
g_m=e_m-f_m.
\]

Every \((q;q)_m\) has constant term \(1\). Hence its order at \(q=0\) is zero. Taking the order at \(q=0\) gives

\[
\alpha-\beta=0.
\]

Assume some \(g_m\ne0\), and let \(M\) be the largest index with \(g_M\ne0\). By the valuation formula from Part I,

\[
v_{\Phi_M}\bigl((q;q)_m\bigr)
=
\left\lfloor\frac{m}{M}\right\rfloor.
\]

For \(m<M\), this valuation is zero, while for \(m=M\), it is one. There are no nonzero exponents above \(M\). Therefore

\[
v_{\Phi_M}
\left(
\prod_m(q;q)_m^{g_m}
\right)
=g_M\ne0.
\]

But the rational function \(1\) has zero \(\Phi_M\)-valuation, a contradiction. Hence every \(g_m=0\). ∎

### Computational consequence

Equality of two pure compressed factorial quotients is decidable by:

1. canonicalizing both exponent maps;
2. comparing the powers of \(q\);
3. comparing the exponent maps.

No polynomial expansion, factorization, root-of-unity evaluation, or jet computation is needed.

This is important conceptually: the cyclotomic machinery is not needed to decide equality of two multiplicative representations. Its real power appears when studying:

- sums and differences;
- collision multiplicities;
- common gcds across families;
- local geometry;
- specialization gaps.

---

## 3. Application A — Instant cyclotomic valuation

Fix \(d\ge1\). For

\[
F(q)
=
q^\alpha\prod_{i=1}^{s}(q;q)_{a_i}^{\varepsilon_i},
\]

define

\[
V_d(F)
=
\sum_{i=1}^{s}\varepsilon_i
\left\lfloor\frac{a_i}{d}\right\rfloor.
\]

### Algorithm 3.1 — `cyclotomic_valuation`

```text
input:  alpha, pairs (a_i, epsilon_i), context d >= 1
output: V

V = 0
for (a, epsilon) in canonicalized_pairs:
    V += epsilon * (a // d)
return V
```

### Application Theorem 3.2 — Correctness of the valuation algorithm

Whenever \(F\) is a nonzero rational function,

\[
\boxed{
V_d(F)=v_{\Phi_d}(F).
}
\]

#### Proof

The cyclotomic factorization

\[
1-q^m
=
\prod_{e\mid m}\Phi_e(q)
\]

implies

\[
(q;q)_a
=
\prod_{m=1}^{a}(1-q^m).
\]

The factor \(\Phi_d(q)\) occurs once in \(1-q^m\) exactly when \(d\mid m\). Therefore

\[
v_{\Phi_d}((q;q)_a)
=
\#\{m\le a:d\mid m\}
=
\left\lfloor\frac ad\right\rfloor.
\]

Valuations add under multiplication and scale under integer powers. The monomial \(q^\alpha\) is coprime to every \(\Phi_d(q)\) for \(d\ge1\). Hence

\[
v_{\Phi_d}(F)
=
\sum_i\varepsilon_i
\left\lfloor\frac{a_i}{d}\right\rfloor.
\]

∎

### Complexity

For \(s\) canonical factors, the algorithm performs \(s\) integer divisions, multiplications, and additions. Its running time is polynomial in the bit lengths of the input integers and linear in the number of compressed factors.

It does not depend on the degree of \(F\).

For example, a Gaussian binomial with

\[
n=10^{1000}+123
\]

is still represented by three factorial indices, and one cyclotomic valuation requires only three integer divisions.

### Corollary 3.3 — Gaussian binomial valuation

\[
\boxed{
v_{\Phi_d}\left({n\brack k}_q\right)
=
\left\lfloor\frac nd\right\rfloor
-
\left\lfloor\frac kd\right\rfloor
-
\left\lfloor\frac{n-k}{d}\right\rfloor.
}
\]

### Corollary 3.4 — Multinomial defect computation

If \(n=ad\), and

\[
k_\nu=r_\nu d+s_\nu,
\qquad
0\le s_\nu<d,
\]

then

\[
\boxed{
v_{\Phi_d}
\left({ad\brack k_1,\ldots,k_c}_q\right)
=
a-\sum_\nu r_\nu
=
\frac{\sum_\nu s_\nu}{d}.
}
\]

The defect can therefore be computed from quotient-remainder data alone.

---

## 4. Application B — Stable Gaussian content and spacing certificates

For

\[
t\ge5,
\qquad
n\ge3t-2,
\]

Parts I and II prove

\[
C_{n,t}(q)
=
\gcd_{t\le k\le n-t}{n\brack k}_q
=
\prod_{d=n-t+1}^{n}\Phi_d(q),
\]

and

\[
\Delta_{n,t}(q)
=
\gcd_{t\le i<j\le n-t}
\left({n\brack i}_q-{n\brack j}_q\right)
=
q^{t+1}
\prod_{d=n-t+1}^{n}\Phi_d(q).
\]

These formulas are themselves algorithms.

### Algorithm 4.1 — Stable polynomial-content certificate

```text
input: n, t
require: t >= 5 and n >= 3*t - 2
output: factored cyclotomic representation of C_{n,t}(q)

return Product(Phi_d(q), d = n-t+1,...,n)
```

### Algorithm 4.2 — Stable polynomial-spacing certificate

```text
input: n, t
require: t >= 5 and n >= 3*t - 2
output: factored representation of Delta_{n,t}(q)

return q^(t+1) * Product(Phi_d(q), d = n-t+1,...,n)
```

### Application Theorem 4.3 — Correctness

Algorithms 4.1 and 4.2 return the exact monic gcds of the retained Gaussian values and pairwise differences.

#### Proof

This is precisely the Stable Content Theorem and the Stable Content–Spacing Decomposition Theorem proved in Part II. The algorithms merely return their factored right-hand sides. ∎

### Why this is computationally significant

A direct gcd computation would require constructing many Gaussian polynomials of potentially enormous degree. The certificate representation contains only \(t\) cyclotomic indices and one power of \(q\).

Thus the output size is \(O(t)\) symbolic factors even when \(n\) has thousands of digits.

### Integer specialization

Define

\[
\rho(m)
=
\begin{cases}
p,&m=p^a\text{ is a prime power},\\1,&\text{otherwise}.
\end{cases}
\]

Then

\[
\gcd_{t\le k\le n-t}\binom nk
=
\prod_{d=n-t+1}^{n}\rho(d).
\]

The spacing gcd is

\[
G_{n,t}
=
\eta(n,t)
\prod_{d=n-t+1}^{n}\rho(d),
\]

where

\[
\eta(n,t)
=
\begin{cases}
2,&n=2^s-1,\\
2,&n=3\cdot2^s-1\text{ and }t=2^s,\\
1,&\text{otherwise}.
\end{cases}
\]

### Algorithm 4.4 — Stable integer-spacing certificate

```text
input: n, t
require: t >= 5 and n >= 3*t - 2

P = 1
for d from n-t+1 through n:
    if d is a prime power p^a:
        P *= p

eta = 1
if n+1 is a power of 2:
    eta = 2
else if t is a power of 2 and n+1 == 3*t:
    eta = 2

return eta * P
```

### Application Theorem 4.5 — Correctness of integer specialization

Algorithm 4.4 returns

\[
\boxed{
G_{n,t}
=
\gcd_{t\le i<j\le n-t}
\left|\binom ni-\binom nj\right|.
}
\]

#### Proof

For every \(m>1\),

\[
\Phi_m(1)
=
\begin{cases}
p,&m=p^a,\\1,&\text{otherwise}.
\end{cases}
\]

Hence the specialization of the terminal cyclotomic interval is the product accumulated in \(P\). Part II proves that specialization introduces no extra spacing factor except in exactly the two binary families encoded by \(\eta\), and in those families the extra factor is exactly \(2\). ∎

### Certificate format

A verifier need not trust a giant expanded integer. It can verify the structured record

```text
StableSpacingCertificate(
    n=n,
    t=t,
    terminal_interval=(n-t+1, n),
    prime_powers=[...],
    exceptional_multiplier=eta
)
```

by checking:

1. the stable-range inequalities;
2. each claimed prime-power decomposition;
3. the exceptional-family predicate.

---

## 5. Application C — Exact leading local residuals

Valuation gives the order of vanishing. The next application computes the first nonzero local coefficient.

Fix a primitive \(d\)-th root \(\zeta\). Write

\[
a_i=r_i d+s_i,
\qquad
0\le s_i<d,
\]

and set

\[
h
=
\sum_i\varepsilon_i r_i
=
v_{\Phi_d}(F).
\]

Define

\[
A_s(\zeta)
=
\prod_{u=1}^{s}(1-\zeta^u),
\qquad
A_0(\zeta)=1.
\]

### Application Theorem 5.1 — Compact exponential residual formula

Assume \(F\) is regular at \(q=\zeta\), \(h\ge0\), and the regularized germ is nonzero. Then

\[
B_\zeta(F)
:=
\lim_{x\to0}x^{-h}F(\zeta e^x)
\]

is

\[
\boxed{
B_\zeta(F)
=
\zeta^\alpha
(-1)^h d^{2h}
\prod_i
\left(r_i!A_{s_i}(\zeta)\right)^{\varepsilon_i}.
}
\]

#### Proof

Part III gives

\[
\lim_{q\to\zeta}
\frac{F(q)}{(1-q^d)^h}
=
\zeta^\alpha
\prod_i
\left(r_i!d^{r_i}A_{s_i}(\zeta)\right)^{\varepsilon_i}.
\]

Since

\[
q=\zeta e^x
\quad\Longrightarrow\quad
1-q^d
=
1-e^{dx}
=
-dx+O(x^2),
\]

we have

\[
\lim_{x\to0}\frac{(1-e^{dx})^h}{x^h}
=(-d)^h.
\]

Also

\[
\prod_i d^{\varepsilon_i r_i}=d^h.
\]

Multiplying the two powers of \(d\) yields \(d^{2h}\), and the sign is \((-1)^h\). ∎

### Multinomial specialization

For

\[
M_{\mathbf k}(q)
={ad\brack k_1,\ldots,k_c}_q,
\qquad
k_\nu=r_\nu d+s_\nu,
\]

one obtains

\[
\boxed{
B_\zeta(M_{\mathbf k})
=
(-1)^h d^{2h}
\frac{a!}{\prod_\nu r_\nu!}
\frac{1}{\prod_\nu A_{s_\nu}(\zeta)}.
}
\]

### Compact versus materialized output

For huge \(r_i\), the integer \(r_i!\) itself may have an enormous number of digits. This cannot be avoided if the user requests its fully materialized value.

A practical library should therefore support two exact output modes.

#### Factored residual

```text
FactorizedCyclotomicResidual(
    root_power=alpha mod d,
    sign=(-1)^h,
    d_power=2*h,
    factorial_powers={r_i: epsilon_i},
    residue_products={s_i: epsilon_i}
)
```

#### Materialized algebraic residual

Construct the exact element of

\[
\mathbb Q(\zeta)
\cong
\mathbb Q[z]/(\Phi_d(z))
\]

only when its output size is acceptable.

### Application Theorem 5.2 — Soundness of a residual certificate

A record containing \(d,h\), the quotient-remainder pairs \((r_i,s_i)\), and the factored expression from Theorem 5.1 is a verifiable certificate for the first nonzero local coefficient of \(F\) at every primitive \(d\)-th root.

#### Proof

The verifier recomputes each Euclidean division

\[
a_i=r_i d+s_i,
\qquad0\le s_i<d,
\]

checks

\[
h=\sum_i\varepsilon_i r_i,
\]

and applies the proved closed formula. Every operation is exact in the formal cyclotomic field. ∎

---

## 6. Application D — Cyclotomic cumulants without expansion

The leading residual gives only the first visible term. Higher local information is encoded by cyclotomic cumulants.

Normalize

\[
G_{F,\zeta}(x)
=
\frac{x^{-h}F(\zeta e^x)}{B_\zeta(F)}.
\]

Then

\[
G_{F,\zeta}(0)=1.
\]

Define

\[
\kappa_r(F;\zeta)
=
\left.
\frac{d^r}{dx^r}
\log G_{F,\zeta}(x)
\right|_{x=0}.
\]

Part IV proves

\[
\boxed{
\kappa_r(F;\zeta)
=
\alpha\delta_{r,1}
+
\sum_i\varepsilon_i
\sum_{m=1}^{a_i}
m^rK_r(\zeta^m),
}
\]

where \(K_r\) is the universal regularized root-of-unity kernel.

A naive implementation still loops from \(1\) to \(a_i\), which is unacceptable for enormous indices. The residue-channel decomposition removes this problem.

### 6.1 Residue-channel power sums

For \(0\le a<d\), define

\[
P_{r,a}(F;d)
=
\sum_i\varepsilon_i
\sum_{\substack{1\le m\le a_i\\m\equiv a\pmod d}}
m^r.
\]

Then

\[
\boxed{
\kappa_r(F;\zeta)
=
\alpha\delta_{r,1}
+
\sum_{a=0}^{d-1}
K_r(\zeta^a)P_{r,a}(F;d).
}
\]

For a single upper bound \(N\), every residue-class sum is an arithmetic-progression power sum.

If \(1\le a<d\), set

\[
L_a(N)
=
\begin{cases}
0,&N<a,\\[1mm]
1+\left\lfloor\dfrac{N-a}{d}\right\rfloor,&N\ge a.
\end{cases}
\]

Then

\[
\sum_{\substack{1\le m\le N\\m\equiv a\pmod d}}m^r
=
\sum_{j=0}^{L_a(N)-1}(a+jd)^r.
\]

For the zero residue,

\[
\sum_{\substack{1\le m\le N\\d\mid m}}m^r
=
d^r
\sum_{j=1}^{\lfloor N/d\rfloor}j^r.
\]

### Lemma 6.1 — Exact progression power-sum formula

For integers \(a,d,L\ge0\),

\[
\boxed{
\sum_{j=0}^{L-1}(a+jd)^r
=
\sum_{u=0}^{r}
\binom ru
a^{r-u}d^u
S_u(L-1),
}
\]

where

\[
S_u(M)=\sum_{j=0}^{M}j^u
\]

is given exactly by Faulhaber's formula.

#### Proof

Expand by the binomial theorem:

\[
(a+jd)^r
=
\sum_{u=0}^{r}
\binom ru
a^{r-u}d^u j^u.
\]

Sum over \(j=0,\ldots,L-1\) and interchange the finite sums. ∎

### Algorithm 6.2 — `cyclotomic_cumulants`

```text
input:
    compressed quotient F
    context d
    exact primitive root zeta
    maximum order R

1. canonicalize F
2. compute h and B
3. for r = 1,...,R:
       for each residue a modulo d needed by the exact field representation:
           compute P_{r,a}(F;d) using progression power sums
       kappa_r = alpha*delta(r,1)
                 + sum_a K_r(zeta^a)*P_{r,a}
4. return (h, B, kappa_1,...,kappa_R)
```

### Application Theorem 6.3 — Correctness

Algorithm 6.2 returns the exact first \(R\) cyclotomic cumulants of \(F\) at \(\zeta\).

#### Proof

Part IV gives the exact cumulant formula and its residue-channel grouping. Lemma 6.1 evaluates each compressed power sum exactly without enumerating its terms. Substitution produces the same finite sums as the theorem, hence the exact cumulants. ∎

### Complexity and output sensitivity

For fixed \(d\) and \(R\), the arithmetic work is polynomial in:

- the number of compressed factors;
- the bit lengths of the indices;
- the requested jet order.

When \(d\) is itself large, an exact generic element of \(\mathbb Q(\zeta_d)\) may require \(\Omega(\varphi(d))\) coefficients. No algorithm can materialize such an output in sublinear time in its representation size.

The algorithm should therefore be understood as **output-sensitive**. It may return either:

1. a materialized cyclotomic-field element;
2. a residue-channel symbolic expression;
3. a factored spectral certificate.

---

## 7. Application E — Reconstructing exact finite jets

The cumulants determine ordinary derivatives through exponential Bell polynomials.

Let

\[
Y_m(x_1,\ldots,x_m)
\]

be the complete exponential Bell polynomial defined by

\[
\exp\left(
\sum_{r\ge1}x_r\frac{t^r}{r!}
\right)
=
\sum_{m\ge0}
Y_m(x_1,\ldots,x_m)
\frac{t^m}{m!}.
\]

Since

\[
F(\zeta e^x)
=
B_\zeta(F)x^h
\exp\left(
\sum_{r\ge1}\kappa_r(F;\zeta)
\frac{x^r}{r!}
\right),
\]

we obtain the following.

### Application Theorem 7.1 — Jet reconstruction formula

For every \(m\ge0\),

\[
\boxed{
D^{h+m}F(\zeta)
=
\frac{(h+m)!}{m!}
B_\zeta(F)
Y_m(\kappa_1,\ldots,\kappa_m).
}
\]

Equivalently,

\[
\boxed{
\frac{D^{h+m}F(\zeta)}{(h+m)!}
=
\frac{B_\zeta(F)}{m!}
Y_m(\kappa_1,\ldots,\kappa_m).
}
\]

#### Proof

By the defining generating function of the Bell polynomials,

\[
\exp\left(
\sum_{r\ge1}\kappa_r\frac{x^r}{r!}
\right)
=
\sum_{m\ge0}
Y_m(\kappa_1,\ldots,\kappa_m)
\frac{x^m}{m!}.
\]

Multiplying by \(B_\zeta(F)x^h\), the coefficient of \(x^{h+m}\) is

\[
\frac{B_\zeta(F)}{m!}
Y_m(\kappa_1,\ldots,\kappa_m).
\]

Since \(D=d/dx\) in the coordinate \(q=\zeta e^x\), multiplying that coefficient by \((h+m)!\) gives the derivative. ∎

### First few reconstructed jets

Writing \(B=B_\zeta(F)\),

\[
\frac{D^hF(\zeta)}{h!}=B,
\]

\[
\frac{D^{h+1}F(\zeta)}{(h+1)!}
=B\kappa_1,
\]

\[
\frac{D^{h+2}F(\zeta)}{(h+2)!}
=
\frac{B}{2}
(\kappa_1^2+\kappa_2),
\]

and

\[
\frac{D^{h+3}F(\zeta)}{(h+3)!}
=
\frac{B}{6}
(\kappa_1^3+3\kappa_1\kappa_2+\kappa_3).
\]

Thus exact derivatives never need to be obtained by symbolic differentiation of an expanded polynomial.

---

## 8. Application F — Exact cyclotomic collision certificates

Let

\[
F(q),G(q)
\]

be two compressed factorial quotients regular at a primitive \(d\)-th root \(\zeta\).

Write their local normal forms as

\[
F(\zeta e^x)
=
B_Fx^{h_F}
\exp\left(
\sum_{r\ge1}\kappa_r^F\frac{x^r}{r!}
\right),
\]

and

\[
G(\zeta e^x)
=
B_Gx^{h_G}
\exp\left(
\sum_{r\ge1}\kappa_r^G\frac{x^r}{r!}
\right).
\]

### Application Theorem 8.1 — Different-depth certificate

If

\[
h_F\ne h_G,
\]

then

\[
\boxed{
v_{\Phi_d}(F-G)=\min(h_F,h_G).}
\]

#### Proof

Assume \(h_F<h_G\). Then

\[
F(\zeta e^x)-G(\zeta e^x)
=
B_Fx^{h_F}+O(x^{h_F+1}),
\]

because \(G\) vanishes to strictly higher order. Since \(B_F\ne0\), the difference has \(x\)-order \(h_F\). By the local jet criterion from Part I, this is the \(\Phi_d\)-valuation. The other ordering is symmetric. ∎

### Application Theorem 8.2 — Fingerprint collision certificate

Assume

\[
h_F=h_G=h.
\]

Then:

1. if \(B_F\ne B_G\),
   \[
   \boxed{v_{\Phi_d}(F-G)=h;}
   \]

2. if \(B_F=B_G=B\), and for some \(m\ge1\),
   \[
   \kappa_r^F=\kappa_r^G
   \quad(1\le r<m),
   \]
   but
   \[
   \kappa_m^F\ne\kappa_m^G,
   \]
   then
   \[
   \boxed{v_{\Phi_d}(F-G)=h+m.}
   \]

#### Proof

The first statement follows immediately from

\[
F-G=(B_F-B_G)x^h+O(x^{h+1}).
\]

For the second, divide both germs by \(Bx^h\). Let

\[
U_F(x)=
\sum_{r\ge1}\kappa_r^F\frac{x^r}{r!},
\qquad
U_G(x)=
\sum_{r\ge1}\kappa_r^G\frac{x^r}{r!}.
\]

The hypothesis gives

\[
U_F(x)-U_G(x)
=
(\kappa_m^F-\kappa_m^G)
\frac{x^m}{m!}
+O(x^{m+1}).
\]

Since \(U_F(0)=U_G(0)=0\),

\[
e^{U_F(x)}-e^{U_G(x)}
=
(\kappa_m^F-\kappa_m^G)
\frac{x^m}{m!}
+O(x^{m+1}).
\]

Multiplying by \(Bx^h\) shows that \(F-G\) has exact \(x\)-order \(h+m\). Apply the local depth theorem. ∎

### Corollary 8.3 — Lower-bound certificate

If the fingerprints agree through order \(R\), then

\[
\boxed{
v_{\Phi_d}(F-G)\ge h+R+1.}
\]

This does not assert equality; a later cumulant may also agree.

### Certificate object

```text
CyclotomicCollisionCertificate(
    context=d,
    left_depth=h_F,
    right_depth=h_G,
    common_leading_residual=B,
    matched_cumulants=(kappa_1,...,kappa_{m-1}),
    first_mismatch_order=m,
    left_mismatch=kappa_m^F,
    right_mismatch=kappa_m^G,
    exact_difference_valuation=h+m
)
```

### Verification theorem

A verifier can check such a certificate using only:

1. Euclidean divisions of the factorial indices by \(d\);
2. exact arithmetic in \(\mathbb Q(\zeta_d)\);
3. progression power sums;
4. equality tests of exact algebraic numbers.

It never needs to construct \(F\), \(G\), or \(F-G\).

---

## 9. The special binary collision engine

At \(d=2\), reciprocity produces additional structure.

For a reciprocal polynomial of degree \(E\) and defect \(h\), the normalized germ

\[
x^{-h}e^{-Ex/2}F(-e^x)
\]

is even.

Therefore the logarithmic fingerprint has the form

\[
\log G(x)
=
\log B
+
\frac{\Theta}{2!}x^2
+
\frac{\Lambda}{4!}x^4
+
\frac{\kappa_6}{6!}x^6
+\cdots.
\]

### Application Theorem 9.1 — Binary parity acceleration

Let \(F\) and \(G\) be reciprocal real polynomials with the same defect \(h\), leading residual \(B\), and reciprocity degree \(E\) at \(q=-1\). If their first differing normalized even cumulant is of order \(2r\), then

\[
\boxed{
v_{q+1}(F-G)=h+2r.}
\]

#### Proof

After removal of \(x^h\), \(B\), and \(e^{Ex/2}\), both regularized germs are even. Their logarithms therefore contain no odd terms. Apply Theorem 8.2 to the first unequal cumulant, whose order must be even. Since \(q+1\) and \(x\) differ by a unit at \(q=-1\), the \(x\)-order is the \((q+1)\)-valuation. ∎

### Computational consequence

Once \(h\), \(B\), and \(E\) match, an implementation can skip all odd orders. The possible extra collision depths are

\[
h+2,
\quad h+4,
\quad h+6,
\quad\ldots.
\]

This halves the higher-order search and provides an internal consistency check: a nonzero normalized odd cumulant beyond the drift indicates an implementation error or a violated reciprocity hypothesis.

---

## 10. Structured polynomial comparison: what is complete and what is not

The theory yields several different comparison problems. They must not be conflated.

### 10.1 Multiplicative identity — complete

For two compressed products

\[
q^\alpha\prod_m(q;q)_m^{e_m},
\qquad
q^\beta\prod_m(q;q)_m^{f_m},
\]

Theorem 2.1 gives a complete identity test by canonicalization.

### 10.2 Nonidentity of a difference — certified locally

If any cyclotomic context produces a finite mismatch certificate, then

\[
F\ne G.
\]

Indeed, Theorem 8.1 or 8.2 proves that \(F-G\) has a finite, nonzero leading local coefficient.

### 10.3 Equality of arbitrary sums — not complete from finitely many fingerprints

Suppose

\[
P(q)=\sum_{i=1}^{u}F_i(q),
\qquad
Q(q)=\sum_{j=1}^{v}G_j(q),
\]

where each term is compressed.

A finite collection of matching cyclotomic fingerprints gives rigorous congruences and lower bounds, but does not by itself prove

\[
P=Q
\]

unless an independent degree bound or completeness theorem is supplied.

### Caution 10.1

Do not advertise finite cyclotomic fingerprinting as a complete general polynomial-identity test.

Its proved roles are:

- exact nonidentity certificates;
- exact local collision orders;
- exact divisibility lower bounds;
- complete comparison in special families with an additional theorem;
- heuristic context selection before formal verification.

---

## 11. Application G — Symbolic verification of enormous identities and congruences

A practical symbolic-verification workflow is:

1. parse each structured term into compressed factorial data;
2. canonicalize multiplicative subexpressions;
3. choose a set of cyclotomic contexts \(d\);
4. compute depth, residual, and cumulants;
5. stop at the first mismatch to obtain a rigorous nonidentity certificate;
6. when fingerprints match, record the corresponding proven divisibility.

### Example certificate statement

Suppose a computation returns

\[
h_F=h_G=6,
\qquad
B_F=B_G,
\qquad
\kappa_1^F=\kappa_1^G,
\qquad
\kappa_2^F\ne\kappa_2^G
\]

at \(d=2\). Then

\[
\boxed{v_{q+1}(F-G)=8.}
\]

This is stronger than merely stating \(F\ne G\). It identifies the exact order at which the two gigantic expressions separate.

### Proof-assistant use

The computation can be split between an untrusted producer and a small trusted verifier.

The producer supplies:

- quotient-remainder decompositions;
- exact algebraic residual expressions;
- progression power-sum values;
- the first mismatching fingerprint.

The verifier checks the closed formulas proved in this monograph.

This is analogous to proof certificates in integer factorization or linear programming: discovery may be expensive or sophisticated, while verification is small and deterministic.

---

## 12. Application H — Cyclic-sieving and orbit calculations

Part V associates a canonical orbit polynomial \(O_X(q)\) with a cyclic action and proves

\[
F(q)-O_X(q)
=(q^N-1)H(q)
\]

for every CSP polynomial \(F\).

The compressed jet engine can be applied to \(F\), while orbit power sums compute the jet of \(O_X\).

This gives an exact application pipeline:

\[
\boxed{
\text{compressed graded enumerator}
\longleftrightarrow
\text{canonical orbit jet}
\longrightarrow
\text{differential CSP comparison}.
}
\]

For fixed-content words, the multinomial defect immediately gives:

- the first nonzero graded derivative order;
- exact Fourier-moment cancellation below that order;
- congruences between the first visible graded moment and orbit moments.

### Practical use

Given a proposed cyclic-sieving polynomial, a library can:

1. verify ordinary CSP values;
2. compute its first several local jets;
3. compare them with canonical orbit jets;
4. return the exact higher-order contact at each context.

This turns differential CSP from a theoretical statement into a computable invariant of a graded cyclic action.

---

## 13. Application I — Arithmetic exploration of Gaussian families

The stable formulas provide an efficient engine for experimental arithmetic.

Instead of constructing all

\[
{n\brack k}_q,
\qquad
t\le k\le n-t,
\]

one can directly compute:

- their common cyclotomic content;
- their pairwise polynomial-spacing gcd;
- the specialized integer content;
- the specialized integer-spacing gcd;
- whether the parameters belong to an exceptional binary family.

This permits searches at parameter sizes impossible for coefficient-based experimentation.

### Example research workflow

1. Search outside the proved stable range.
2. Compute contextual fingerprints using \(q\)-Lucas.
3. detect extra collisions;
4. formulate a finite exceptional-family conjecture;
5. use local jets to determine whether collisions are simple or higher order;
6. attempt a proof using the contextual classification.

The algorithm is therefore not only a final application. It is a theorem-discovery instrument.

---

## 14. External application prospects

The following directions are plausible but have different levels of maturity.

### 14.1 Computer algebra — established and immediate

The strongest current application is exact symbolic computation for:

- \(q\)-binomials;
- \(q\)-multinomials;
- \(q\)-factorial quotients;
- root-of-unity limits;
- cyclotomic valuations;
- local jets;
- gcd and collision calculations.

This application is fully supported by the proved theorems.

### 14.2 Combinatorics and cyclic sieving — established framework, open interpretations

The local derivatives and orbit jets are exactly computable. The complete combinatorial meaning of every graded derivative remains open.

### 14.3 Coding theory — plausible research application

Gaussian coefficients count finite-field subspaces and occur throughout subspace coding and network coding. Cyclotomic certificates could be used to:

- compare compressed subspace enumerators;
- detect forced divisibility in counting formulas;
- test congruence constraints on candidate distributions;
- search for impossible parameter sets.

No new coding-theoretic bound is claimed in this chapter. This is a concrete application target requiring additional theorems.

### 14.4 Structured prime search — limited application

Cyclotomic values generate structured integer candidates, and the valuation engine can expose guaranteed algebraic factors before materialization. This may support an early-rejection sieve for specially constructed families.

However:

\[
\boxed{
\text{the present theory is not a faster general prime generator.}
}
\]

It neither removes the need for primality testing nor solves the factorization of general cyclotomic values.

### 14.5 Cryptographic auditing — exploratory only

Some cryptographic systems use cyclotomic polynomial rings. Local root-of-unity fingerprints may detect accidental structure in badly designed algebraic distributions.

But the current theory does not break AES, RSA, lattice cryptography, or any deployed cipher. Noise and modular reduction usually destroy the exact integral collision structure on which the present theorems rely.

Any cryptographic claim would require a separate distinguisher or key-recovery theorem with a measured advantage.

---

## 15. Suggested open-source architecture

### 15.1 Core data type

```python
@dataclass(frozen=True)
class QFactorialQuotient:
    q_power: int
    factors: tuple[tuple[int, int], ...]
```

The constructor should:

- reject negative factorial indices;
- combine repeated indices;
- delete zero exponents;
- sort factors by index;
- optionally record whether polynomiality has been certified.

### 15.2 Public API

```python
cyclotomic_valuation(F, d)
```

```python
q_binomial_cyclotomic_valuation(n, k, d)
```

```python
q_multinomial_defect(parts, d)
```

```python
cyclotomic_leading_residual(F, d, representation="factored")
```

```python
cyclotomic_cumulants(F, d, order, representation="spectral")
```

```python
cyclotomic_jet(F, d, order)
```

```python
cyclotomic_collision_certificate(F, G, d, max_order)
```

```python
stable_gaussian_content(n, t)
```

```python
stable_gaussian_spacing(n, t, specialize=False)
```

### 15.3 Exact algebraic representation

For moderate \(d\), use the exact cyclotomic field

\[
K_d=\mathbb Q[z]/(\Phi_d(z)).
\]

For large \(d\), allow a symbolic residue-channel representation to avoid materializing \(\varphi(d)\) coordinates prematurely.

### 15.4 First mergeable contribution

The smallest credible upstream contribution is:

> Add non-expanding cyclotomic valuations for Gaussian binomial and multinomial coefficients.

It requires only:

- the floor formulas;
- input validation;
- exhaustive small tests;
- impossible-to-expand examples;
- concise mathematical documentation.

The second contribution should add the multinomial defect and leading residual. Higher cumulants and collision certificates should follow only after the foundational API is accepted.

---

## 16. Testing and validation

### 16.1 Exhaustive small-case tests

For small \(n,k,d\):

1. construct the Gaussian polynomial;
2. factor it or repeatedly divide by \(\Phi_d(q)\);
3. compare with the floor valuation.

For multinomials:

1. expand the exact polynomial;
2. substitute \(q=\zeta e^x\) in a truncated formal series;
3. compare the first visible coefficient and reconstructed jets.

### 16.2 Collision tests

For small pairs \(F,G\):

1. compute \(F-G\) explicitly;
2. determine \(v_{\Phi_d}(F-G)\) directly;
3. compare with the first mismatching fingerprint.

### 16.3 Stable-block tests

For all manageable

\[
t\ge5,
\qquad
3t-2\le n\le N,
\]

compare:

- direct polynomial gcds;
- the terminal cyclotomic product;
- direct integer gcds;
- the predicted exceptional multiplier.

### 16.4 Property tests

Verify:

- additivity of valuations;
- additivity of cumulants;
- conjugation laws;
- reciprocity parity at \(d=2\);
- exact vanishing of binary odd cumulants after drift removal;
- consistency between Bell reconstruction and direct differentiation.

### 16.5 Performance tests

Use indices with hundreds or thousands of decimal digits. Confirm that:

- valuation computation scales with bit length;
- no array proportional to the degree is allocated;
- factored residual output remains compact;
- materialized algebraic output is explicitly output-sensitive.

---

## 17. Theorem inventory for this application chapter

| No. | Result | Status | Computational application |
|---:|---|---|---|
| 2.1 | Uniqueness of compressed factorial representation | Proved here | Complete identity test for multiplicative quotients |
| 3.2 | Correctness of valuation algorithm | Consequence of Part I, reproved | Instant exact \(\Phi_d\)-valuation |
| 4.3 | Stable polynomial certificate correctness | Part II application | Direct factored gcd output |
| 4.5 | Stable integer certificate correctness | Part II application | Exact specialized spacing gcd |
| 5.1 | Compact exponential residual formula | Consequence of Parts III–IV, proved here | Exact first local coefficient |
| 5.2 | Residual-certificate soundness | Proved here | Independently verifiable local certificate |
| 6.1 | Progression power-sum compression | Classical, proved here | Avoid iteration to enormous indices |
| 6.3 | Cumulant algorithm correctness | Part IV plus 6.1 | Exact higher local invariants |
| 7.1 | Bell-polynomial jet reconstruction | Proved here | Exact derivatives from cumulants |
| 8.1 | Different-depth collision certificate | Part III application, proved here | Exact valuation of a difference |
| 8.2 | Fingerprint collision certificate | Project application theorem, proved here | First mismatch gives exact contact order |
| 9.1 | Binary parity acceleration | Part IV application, proved here | Skip impossible odd collision increments |

---

## 18. Principal open application problems

### Open Problem 18.1 — Optimal context selection

Given two structured expressions, choose a cyclotomic context \(d\) likely to distinguish them with minimal computation.

Possible signals include:

- valuation imbalance;
- quotient-remainder entropy;
- residue-channel sparsity;
- reciprocity degree;
- expected algebraic-field size.

### Open Problem 18.2 — Complete comparison for structured sums

Find classes of sums of factorial quotients for which finitely many cyclotomic certificates form a complete identity test.

### Open Problem 18.3 — Compact algebraic residual comparison

Determine when two factored expressions involving

\[
A_s(\zeta)
\]

can be compared without fully constructing \(\mathbb Q(\zeta)\).

### Open Problem 18.4 — Coding-theory obstruction theorem

Use cyclotomic valuations or jets to rule out a candidate subspace-code enumerator or weight distribution that survives standard integer counting constraints.

### Open Problem 18.5 — Differential CSP implementation

Combine compressed graded jets with canonical orbit jets in SageMath or OSCAR and build a searchable database of higher-order CSP behavior.

### Open Problem 18.6 — Certified external package

Develop a standalone package whose outputs can be imported as proof certificates into a major computer-algebra system or theorem prover.

---

## 19. Final synthesis

The first practical application of Cyclotomic Coefficient Arithmetic is not generic prime generation or cipher breaking. It is **exact compressed analysis of structured polynomials that are too large to exist explicitly in memory**.

The proved computational chain is

\[
\boxed{
\text{compressed factorial data}
\longrightarrow
\text{cyclotomic depth}
\longrightarrow
\text{leading residual}
\longrightarrow
\text{cumulants}
\longrightarrow
\text{finite jets}
\longrightarrow
\text{collision certificate}.
}
\]

For stable Gaussian blocks, the chain becomes even shorter:

\[
\boxed{
(n,t)
\longrightarrow
\text{terminal cyclotomic interval}
\longrightarrow
\text{exact polynomial and integer gcds}.
}
\]

These are genuine applications because they replace computationally impossible expansion by exact arithmetic on the original parameters.

The theory therefore supplies three immediately reusable products:

1. **non-expanding invariants** for huge \(q\)-factorial quotients;
2. **verifiable certificates** for local equality, inequality, and collision depth;
3. **closed-form gcd engines** for stable Gaussian families.

The natural next step is implementation in a standalone exact-arithmetic package, followed by incremental upstream contributions to SageMath or OSCAR.

---

## Dependency map

This chapter uses:

- **Part I:** cyclotomic valuations, local rings, and jet criteria;
- **Part II:** stable Gaussian content, spacing, and specialization;
- **Part III:** defect, local factorial normal form, and residual geometry;
- **Part IV:** cumulants, reciprocity, and binary parity;
- **Part V:** canonical orbit jets and differential cyclic sieving.

It reframes those results as a coherent computational application and supplies correctness proofs for the resulting algorithms and certificates.
