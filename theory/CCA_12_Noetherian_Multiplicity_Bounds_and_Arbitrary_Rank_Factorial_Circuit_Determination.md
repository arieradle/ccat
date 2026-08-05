# Cyclotomic Coefficient Arithmetic

## Part XII — Noetherian Multiplicity Bounds and Arbitrary-Rank Factorial-Circuit Determination

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete theorem chapter  
**Scope:** Sums of arbitrary compressed $q$-factorial quotients, fixed-context Laurent germs, universal normalized local expansions, Noetherian coefficient ideals, Bautin-type multiplicity bounds, residual Wronskians, vanishing sequences, weighted linear matroids, arbitrary-rank finite determination, unequal-depth certificates, sharp effective endpoint-jump bounds, affine-line factorial circuits, transfer to nested product systems, algorithmic limitations, and the remaining explicit-bound problem.

---

# 0. Purpose, relation to Part XI, and exact status

Part XI proved that a sparse Laurent polynomial

$$
P(q)=\sum_{\nu=1}^{t}c_\nu q^{e_\nu}
$$

cannot have contact order greater than $t-1$ at any nonzero context. The proof used the finite-dimensional power-moment sequence

$$
D^jP(\xi)
=
\sum_{\nu=1}^{t}
(c_\nu\xi^{e_\nu})e_\nu^j.
$$

That theorem gives an optimal identity test and exact Prony reconstruction for sums of monomials. It does not directly apply to a sum such as

$$
F(q)
=
\sum_{i=1}^{m}
 c_i q^{\alpha_i}
 \prod_{j=1}^{S}(q;q)_{A_j}^{e_{ij}},
$$

because each compressed summand may contain exponentially many monomials after expansion.

The central problem of the present chapter is therefore:

> For fixed top fan-in and fixed endpoint complexity, can arbitrary cancellations among compressed factorial quotients have unbounded local order as the endpoint sizes grow?

The answer is **no** at every fixed cyclotomic context.

Fix

$$
d\ge1,
\qquad
m\ge1,
\qquad
S\ge0.
$$

There exists a finite constant

$$
\boxed{C_d(m,S)<\infty}
$$

such that every nonzero linear combination of at most $m$ compressed factorial terms using at most $S$ distinct factorial endpoints has local order within $C_d(m,S)$ of the depth of one of its input terms.

In the common-depth case, this becomes

$$
\boxed{
F\ne0
\quad\Longrightarrow\quad
h\le \operatorname{ord}_{q=\zeta_d}F\le h+C_d(m,S).
}
$$

Thus finitely many jets at one context determine identity, independently of the magnitudes of the endpoint indices.

The proof has four components:

$$
\boxed{
\begin{array}{c}
\text{universal polynomial local expansions}\\[1mm]
\Downarrow\\[1mm]
\text{Noetherian coefficient-ideal bound}\\[1mm]
\Downarrow\\[1mm]
\text{uniform residual-Wronskian multiplicity}\\[1mm]
\Downarrow\\[1mm]
\text{vanishing sequences plus weighted matroid minima}.
\end{array}
}
$$

The theorem is mathematically complete, but its present proof is **non-effective** in the following precise sense:

- it proves that $C_d(m,S)$ exists;
- it does not provide an explicit numerical formula for $C_d(m,S)$;
- therefore it does not yet yield a polynomial-time PIT algorithm in the compressed input size.

The chapter also proves an explicit sharp theorem for the affine-line subclass. There the exact bound is controlled by endpoint jumps and top fan-in.

The labels used below are:

- **Classical lemma:** standard algebraic input, proved here;
- **Project theorem:** a theorem established in the CCA framework;
- **Corollary:** a formal consequence;
- **Algorithmic corollary:** a finite exact procedure once the required bound is supplied;
- **Sharpness statement:** a construction proving optimality;
- **Caution:** a distinction required for exact mathematics or complexity claims.

Throughout,

$$
D=q\frac d{dq},
\qquad
q=\zeta e^x,
$$

so that

$$
D=\frac d{dx}.
$$

All coefficient fields have characteristic zero.

---

# 1. Compressed factorial circuits

## 1.1 Shared endpoint representation

Fix distinct nonnegative integers

$$
0<A_1<\cdots<A_S.
$$

The case $S=0$ is allowed and means that no factorial factor occurs.

### Definition 1.1 — Compressed factorial term

A **compressed factorial term** supported on the endpoint set

$$
\mathcal A=\{A_1,\ldots,A_S\}
$$

is a nonzero rational function of the form

$$
\boxed{
T(q)
=
q^\alpha
\prod_{j=1}^{S}(q;q)_{A_j}^{e_j},
}
$$

where

$$
\alpha,e_j\in\mathbb Z.
$$

Zero exponents are permitted. Negative exponents are permitted, so a term may be a rational function rather than a polynomial.

### Definition 1.2 — Factorial circuit

A **factorial circuit of top fan-in at most $m$** is a sum

$$
\boxed{
F(q)=\sum_{i=1}^{r}c_iT_i(q),
\qquad
1\le r\le m,
}
$$

where

$$
c_i\ne0
$$

and every $T_i$ is supported on one common endpoint set of size at most $S$.

The common endpoint convention is not restrictive. Given arbitrary terms, take the union of all factorial endpoints and assign exponent zero when an endpoint is absent from a term.

### Definition 1.3 — Endpoint complexity

The **endpoint complexity** of a circuit is the number of distinct positive integers $A$ for which some factor $(q;q)_A$ occurs with nonzero exponent in some summand.

It is this union size—not the number of factors written before canonicalization—that is denoted by $S$.

## 1.2 Canonicalization

Part VI proved that a pure factorial quotient has a unique canonical exponent map. In the present setting, each summand is first canonicalized by:

1. combining repeated endpoints;
2. deleting endpoints with total exponent zero;
3. collecting the monomial power of $q$.

Two proportional terms may then be combined in the outer sum.

### Caution 1.4 — Linear dependence is still possible

Distinct canonical exponent vectors need not be linearly independent as rational functions once several terms are considered. The main theorem does not assume independence of all input terms. It passes to their actual linear span.

---

# 2. Local Laurent germs and cyclotomic depth

Fix a primitive $d$-th root of unity

$$
\zeta=\zeta_d.
$$

For $d=1$, take $\zeta=1$.

## 2.1 Order of a Laurent germ

Let

$$
f(x)=\sum_{n\ge N}a_nx^n\in K((x)),
\qquad
a_N\ne0.
$$

### Definition 2.1 — Local order

Define

$$
\boxed{
\operatorname{ord}_x f=N.
}
$$

Set

$$
\operatorname{ord}_x0=+\infty.
$$

For a rational function $R(q)$, define

$$
\boxed{
\operatorname{ord}_{\zeta}R
=
\operatorname{ord}_xR(\zeta e^x).
}
$$

Because $q-\zeta=\zeta x+O(x^2)$, this agrees with the ordinary zero or pole order at $q=\zeta$.

For a rational function over $\mathbb Q$, it also equals the cyclotomic valuation:

$$
\boxed{
\operatorname{ord}_{\zeta_d}R
=
v_{\Phi_d}(R).
}
$$

## 2.2 Depth of one factorial term

For

$$
T_i(q)
=
q^{\alpha_i}
\prod_{j=1}^{S}(q;q)_{A_j}^{e_{ij}},
$$

define

$$
\boxed{
h_i=v_{\Phi_d}(T_i).}
$$

Part I gives the exact formula

$$
\boxed{
 h_i
=
\sum_{j=1}^{S}
 e_{ij}
 \left\lfloor\frac{A_j}{d}\right\rfloor.
}
$$

The monomial $q^{\alpha_i}$ contributes no cyclotomic depth.

### Proposition 2.2 — Unit decomposition

For every nonzero factorial term $T_i$, there exist

$$
b_i\in\mathbb Q(\zeta)^\times
$$

and a unit power series

$$
U_i(x)\in1+x\mathbb Q(\zeta)[[x]]
$$

such that

$$
\boxed{
T_i(\zeta e^x)=b_ix^{h_i}U_i(x).
}
$$

#### Proof

Part IV gives the nonzero leading exponential-coordinate residual

$$
b_i
=
\lim_{x\to0}x^{-h_i}T_i(\zeta e^x).
$$

After division by $b_ix^{h_i}$, the remaining Laurent germ has order zero and constant term one. It is therefore a unit in the formal power-series ring. ∎

### Caution 2.3 — Negative depths

If $h_i<0$, the term has a pole at the context. The decomposition remains valid in the Laurent-series field. Every theorem below allows arbitrary integer depths.

---

# 3. Universal normalized factorial germs

The first substantive step is to prove that all normalized local coefficients belong to a finitely generated polynomial ring when $d,m,S$ are fixed.

## 3.1 Quotient and residue coordinates

Write each endpoint uniquely as

$$
\boxed{
A_j=dR_j+s_j,
\qquad
R_j\in\mathbb Z_{\ge0},
\qquad
0\le s_j<d.
}
$$

For fixed $d$ and $S$, there are only finitely many residue patterns

$$
\mathbf s=(s_1,\ldots,s_S)
\in\{0,1,\ldots,d-1\}^S.
$$

The quotient variables $R_j$ may be arbitrarily large.

## 3.2 Normalized germ of one factorial

For $A=dR+s$, define

$$
\mathcal U_{d,s}(R;x)
=
\frac{x^{-R}(q;q)_{dR+s}|_{q=\zeta e^x}}
{B_{d,s}(R)},
$$

where

$$
B_{d,s}(R)
=
\lim_{x\to0}
 x^{-R}(q;q)_{dR+s}|_{q=\zeta e^x}.
$$

Then

$$
\mathcal U_{d,s}(R;0)=1.
$$

Part IV gives

$$
\log \mathcal U_{d,s}(R;x)
=
\sum_{n\ge1}
\kappa_n(d,s;R)
\frac{x^n}{n!},
$$

where

$$
\kappa_n(d,s;R)
=
\sum_{a=0}^{d-1}
K_n(\zeta^a)
\sum_{\substack{1\le t\le dR+s\\t\equiv a\pmod d}}
t^n.
$$

The channel $a=0$ uses the regularized singular kernel from Part IV.

## 3.3 Polynomiality of progression sums

### Classical Lemma 3.1 — Progression power sums are polynomial

Fix integers

$$
d\ge1,
\qquad
0\le a<d,
\qquad
n\ge0.
$$

For each fixed choice of whether the terminal residue is included, the sum

$$
\sum_{\substack{1\le t\le dR+s\\t\equiv a\pmod d}}t^n
$$

is a polynomial in $R$ with rational coefficients.

#### Proof

For $1\le a<d$, the relevant terms are

$$
a,a+d,\ldots,a+(L-1)d,
$$

where $L$ equals either $R$ or $R+1$, determined only by whether $a\le s$.

By the binomial theorem,

$$
(a+jd)^n
=
\sum_{u=0}^{n}
\binom nu
 a^{n-u}d^u j^u.
$$

Summing over $j$ gives a linear combination of Faulhaber sums

$$
\sum_{j=0}^{L-1}j^u,
$$

which are polynomials in $L$, hence in $R$.

For $a=0$, the terms are

$$
d,2d,\ldots,Rd,
$$

and the sum is

$$
d^n\sum_{j=1}^{R}j^n,
$$

again polynomial in $R$. ∎

### Corollary 3.2 — Polynomial cumulants

For fixed $d,s,n$,

$$
\boxed{
\kappa_n(d,s;R)
\in
\mathbb Q(\zeta)[R].
}
$$

#### Proof

Every residue-channel power sum is polynomial in $R$ by Lemma 3.1. The kernel values $K_n(\zeta^a)$ are constants in $\mathbb Q(\zeta)$. Their finite linear combination is therefore polynomial. ∎

## 3.4 Polynomial Taylor coefficients

### Lemma 3.3 — Bell-polynomial coefficient principle

Let $R_0$ be a commutative $\mathbb Q$-algebra, and suppose

$$
L(x)=\sum_{n\ge1}\ell_n\frac{x^n}{n!}
\in xR_0[[x]].
$$

If

$$
U(x)=e^{L(x)}
=
\sum_{n\ge0}u_n\frac{x^n}{n!},
$$

then

$$
\boxed{
 u_n=Y_n(\ell_1,\ldots,\ell_n),
}
$$

where $Y_n$ is the complete exponential Bell polynomial. In particular,

$$
u_n\in\mathbb Q[\ell_1,\ldots,\ell_n].
$$

#### Proof

This is the defining generating identity of the complete exponential Bell polynomials:

$$
\exp\left(
\sum_{r\ge1}x_r\frac{t^r}{r!}
\right)
=
\sum_{n\ge0}
Y_n(x_1,\ldots,x_n)
\frac{t^n}{n!}.
$$

Substitute $x_r=\ell_r$. ∎

### Corollary 3.4 — Universal factorial-unit coefficients

Write

$$
\mathcal U_{d,s}(R;x)
=
\sum_{n\ge0}u_{d,s,n}(R)x^n.
$$

For every fixed $n$,

$$
\boxed{
 u_{d,s,n}(R)
\in
\mathbb Q(\zeta)[R].
}
$$

#### Proof

Corollary 3.2 gives polynomial logarithmic cumulants. Lemma 3.3 expresses the coefficient of order $n$ as a universal polynomial in the first $n$ cumulants. ∎

### Caution 3.5 — Meaning of the universal quotient variable

The original normalized germ $\mathcal U_{d,s}(R;x)$ is first defined for integers $R\ge0$. Corollary 3.4 gives a unique polynomial formula for each coefficient as a function of $R$. From this point onward, the notation

$$
\mathcal U_{d,s}(R;x)
\in
\mathbb Q(\zeta)[R][[x]]
$$

means the formal series obtained from those polynomial coefficient formulas. Specializing the indeterminate $R$ to a nonnegative integer recovers the actual normalized factorial germ.

## 3.5 Integer powers of a normalized unit

### Lemma 3.6 — Polynomial dependence on an integer exponent

Let

$$
U(x)=1+u_1x+u_2x^2+\cdots
$$

with coefficients in a commutative $\mathbb Q$-algebra. For an indeterminate $E$, define formally

$$
U(x)^E
=
\exp(E\log U(x)).
$$

For each $n\ge0$, the coefficient

$$
[x^n]U(x)^E
$$

is a polynomial in

$$
E,u_1,\ldots,u_n
$$

with rational coefficients.

For every integer specialization $E=e$, including negative integers, this formal series equals the ordinary integral power $U(x)^e$.

#### Proof

The coefficient of $x^n$ in $\log U$ is a rational polynomial in $u_1,\ldots,u_n$. Multiplication by $E$, followed by Lemma 3.3, proves polynomial dependence.

For integer $e\ge0$, the exponential definition equals repeated multiplication. For $e<0$, it equals the inverse of $U^{-e}$, because formal logarithm and exponential are inverse operations on unit series in characteristic zero. ∎

## 3.7 Universal unit attached to one term

For a symbolic term index $i$, introduce variables

$$
\Alpha_i,
\qquad
E_{i1},\ldots,E_{iS},
\qquad
R_1,\ldots,R_S.
$$

Fix a residue pattern $\mathbf s$. Define the universal normalized unit

$$
\boxed{
\mathscr U_i(x)
=
e^{\Alpha_i x}
\prod_{j=1}^{S}
\mathcal U_{d,s_j}(R_j;x)^{E_{ij}}.
}
$$

Let

$$
\mathscr R_{d,m,S,\mathbf s}
=
\mathbb Q(\zeta)
[
R_1,\ldots,R_S,
\Alpha_1,\ldots,\Alpha_m,
E_{ij}:1\le i\le m,1\le j\le S
].
$$

This is a finitely generated polynomial ring over a field and is therefore Noetherian.

### Project Lemma 3.7 — Universal coefficient ring

For every $i$,

$$
\boxed{
\mathscr U_i(x)
\in
1+x\mathscr R_{d,m,S,\mathbf s}[[x]].
}
$$

That is, every Taylor coefficient of $\mathscr U_i$ is a polynomial in the finite parameter list.

#### Proof

The coefficient of $e^{\Alpha_i x}$ at every fixed order is polynomial in $\Alpha_i$. Corollary 3.4 gives polynomial coefficients for each endpoint unit, and Lemma 3.6 gives polynomial dependence on $E_{ij}$. A finite product preserves polynomiality of every fixed Taylor coefficient. ∎

### Corollary 3.8 — Specialization to every factorial term

For any actual endpoint quotients $R_j$, monomial exponent $\alpha_i$, and factorial exponents $e_{ij}$, specializing

$$
\Alpha_i\mapsto\alpha_i,
\qquad
E_{ij}\mapsto e_{ij}
$$

sends $\mathscr U_i(x)$ to the normalized unit $U_i(x)$ in Proposition 2.2.

#### Proof

Both series have the same cumulant expansion and constant term one. ∎

---

# 4. The Noetherian coefficient-ideal principle

The existence of a uniform multiplicity bound comes from a simple but powerful consequence of Noetherianity.

### Classical Lemma 4.1 — Noetherian coefficient bound

Let $R$ be a Noetherian commutative ring, and let

$$
Q(x)=\sum_{n\ge0}q_nx^n\in R[[x]].
$$

Then there exists an integer

$$
C(Q)\ge0
$$

such that, for every ring homomorphism

$$
\varphi:R\to L
$$

into a field $L$, either

$$
\varphi(Q)=0
\quad\text{in }L[[x]],
$$

or

$$
\boxed{
\operatorname{ord}_x\varphi(Q)\le C(Q).
}
$$

Equivalently, if

$$
[x^n]\varphi(Q)=0
\qquad(0\le n\le C(Q)),
$$

then every coefficient of $\varphi(Q)$ vanishes.

#### Proof

Consider the ascending chain of coefficient ideals

$$
I_N=(q_0,q_1,\ldots,q_N)\subseteq R.
$$

Because $R$ is Noetherian, the full ideal

$$
I=(q_0,q_1,q_2,\ldots)
$$

is finitely generated. Choose coefficient generators

$$
q_{n_1},\ldots,q_{n_t}
$$

and set

$$
C(Q)=\max(n_1,\ldots,n_t).
$$

Suppose the first $C(Q)+1$ coefficients vanish after specialization. Then every selected generator vanishes:

$$
\varphi(q_{n_j})=0.
$$

Every coefficient $q_n$ lies in the ideal generated by those selected coefficients, so

$$
\varphi(q_n)=0
$$

for every $n$. Hence $\varphi(Q)=0$.

The contrapositive says that every nonzero specialization has a nonzero coefficient of index at most $C(Q)$, which is the order bound. ∎

### Definition 4.2 — Bautin index of a universal series

Any valid integer $C(Q)$ in Lemma 4.1 is called a **Bautin index** of the universal series $Q$.

The smallest valid value is the maximum finite order attained by a nonzero specialization.

### Caution 4.3 — Finiteness is not an explicit formula

Lemma 4.1 proves the existence of a finite coefficient cutoff. It does not identify the generator indices $n_j$, and therefore it does not by itself provide a usable numerical value of $C(Q)$.

No polynomial-time conclusion may be inferred solely from Noetherianity.

---

# 5. Formal Laurent Wronskians

## 5.1 Definition

For Laurent series

$$
f_1,\ldots,f_r\in K((x)),
$$

define their Wronskian by

$$
\boxed{
W(f_1,\ldots,f_r)
=
\det\left(f_j^{(i-1)}\right)_{1\le i,j\le r}.
}
$$

## 5.2 Vanishing-order basis

### Lemma 5.1 — Adapted basis

Let $V\subseteq K((x))$ be a finite-dimensional vector space of dimension $r$. Then there exists a basis

$$
g_1,\ldots,g_r
$$

with strictly increasing orders

$$
\boxed{
\nu_1<\nu_2<\cdots<\nu_r.
}
$$

The sequence $(\nu_1,\ldots,\nu_r)$ depends only on $V$, not on the chosen adapted basis.

#### Proof

Choose a nonzero element of minimal order and call it $g_1$. Subtract suitable multiples of $g_1$ from the remaining vectors to eliminate their coefficient at order $\nu_1$. The surviving vectors span a codimension-one subspace all of whose nonzero elements have order greater than $\nu_1$.

Repeat inductively.

At each stage, $\nu_j$ is characterized intrinsically as the smallest integer $n$ such that

$$
\dim(V/V_{\ge n+1})\ge j,
$$

where

$$
V_{\ge n}=
\{f\in V:\operatorname{ord}_xf\ge n\}.
$$

Hence the sequence is independent of the choices. ∎

### Corollary 5.2 — Orders occurring in a finite-dimensional space

Every nonzero element of $V$ has order equal to one of

$$
\nu_1,\ldots,\nu_r.
$$

#### Proof

Write

$$
f=\sum_{j=1}^{r}a_jg_j
$$

and let $j_0$ be the least index with $a_{j_0}\ne0$. Because the orders are strictly increasing, the leading term of $a_{j_0}g_{j_0}$ cannot cancel with any later basis vector. Thus

$$
\operatorname{ord}_xf=\nu_{j_0}.
$$

∎

## 5.3 Wronskian criterion and valuation

### Classical Lemma 5.3 — Formal Wronskian criterion

Over a field of characteristic zero,

$$
\boxed{
W(f_1,\ldots,f_r)\ne0
\iff
f_1,\ldots,f_r
\text{ are linearly independent over }K.
}
$$

#### Proof

If the series are linearly dependent, the columns of the Wronskian matrix are linearly dependent, so the determinant is zero.

Conversely, suppose they are independent, and let

$$
g_1,\ldots,g_r
$$

be an adapted basis of their span with orders

$$
\nu_1<\cdots<\nu_r.
$$

An invertible constant change of basis multiplies the Wronskian by a nonzero scalar, so it is enough to prove that

$$
W(g_1,\ldots,g_r)\ne0.
$$

Write

$$
g_j(x)=a_jx^{\nu_j}+O(x^{\nu_j+1}),
\qquad
a_j\ne0.
$$

Then

$$
g_j^{(i-1)}(x)
=
a_j(\nu_j)_{i-1}
 x^{\nu_j-i+1}
+O(x^{\nu_j-i+2}),
$$

where

$$
(z)_k=z(z-1)\cdots(z-k+1)
$$

is the falling factorial.

Factor $a_jx^{\nu_j}$ from column $j$ and $x^{-i+1}$ from row $i$. The leading determinant is

$$
\det\bigl((\nu_j)_{i-1}\bigr)_{i,j=1}^{r}.
$$

The falling-factorial polynomials form a monic polynomial basis, so this determinant equals the Vandermonde determinant

$$
\prod_{1\le u<v\le r}(\nu_v-\nu_u),
$$

which is nonzero because the orders are distinct. Therefore the Wronskian is nonzero. ∎

### Corollary 5.4 — Wronskian order of an adapted basis

With the notation above,

$$
\boxed{
\operatorname{ord}_xW(g_1,\ldots,g_r)
=
\sum_{j=1}^{r}\nu_j-\binom r2.
}
$$

#### Proof

The leading determinant calculated in Lemma 5.3 is nonzero, and the factored power of $x$ is

$$
\sum_j\nu_j-
\sum_{i=1}^{r}(i-1)
=
\sum_j\nu_j-\binom r2.
$$

∎

### Definition 5.5 — Shifted Wronskian weight

For an independent tuple $(f_1,\ldots,f_r)$, define

$$
\boxed{
\omega(f_1,\ldots,f_r)
=
\operatorname{ord}_xW(f_1,\ldots,f_r)+\binom r2.
}
$$

By Corollary 5.4, this equals the sum of the vanishing sequence of the tuple's span.

---

# 6. Universal residual Wronskians

We now remove the obvious depth contribution from every Wronskian and apply the Noetherian coefficient principle to the remaining unit determinant.

## 6.1 Derivative factorization

Let

$$
f_i(x)=b_ix^{h_i}U_i(x),
\qquad
b_i\ne0,
\qquad
U_i(0)=1.
$$

For $p\ge0$, Leibniz's rule gives

$$
\frac{d^p}{dx^p}(x^{h_i}U_i)
=
\sum_{k=0}^{p}
\binom pk
(h_i)_{p-k}
 x^{h_i-p+k}U_i^{(k)}(x).
$$

Therefore

$$
\boxed{
\frac{d^p}{dx^p}(x^{h_i}U_i)
=
x^{h_i-p}
\sum_{k=0}^{p}
\binom pk
(h_i)_{p-k}
x^kU_i^{(k)}(x).
}
$$

## 6.2 Residual determinant

For an index set

$$
I=\{i_1,\ldots,i_r\}\subseteq\{1,\ldots,m\},
$$

define

$$
A_{p,i}(x)
=
\sum_{k=0}^{p}
\binom pk
(h_i)_{p-k}
x^kU_i^{(k)}(x),
\qquad
0\le p<r.
$$

Define the residual Wronskian

$$
\boxed{
Q_I(x)=
\det\bigl(A_{p,i}(x)\bigr)_{
0\le p<r,\ i\in I}.
}
$$

### Proposition 6.1 — Exact residual-Wronskian factorization

For every tuple $I$,

$$
\boxed{
W(f_i:i\in I)
=
\left(\prod_{i\in I}b_i\right)
 x^{\sum_{i\in I}h_i-\binom r2}
 Q_I(x).
}
$$

#### Proof

Insert the derivative factorization into the Wronskian matrix. Factor

$$
b_ix^{h_i}
$$

from column $i$, and factor

$$
x^{-p}
$$

from the row indexed by derivative order $p$. The total row exponent is

$$
-\sum_{p=0}^{r-1}p
=-\binom r2.
$$

The remaining determinant is exactly $Q_I$. ∎

### Corollary 6.2 — Shifted Wronskian weight

If the tuple is independent, then

$$
\boxed{
\omega(f_i:i\in I)
=
\sum_{i\in I}h_i
+
\operatorname{ord}_xQ_I.
}
$$

#### Proof

The scalar product $\prod b_i$ is nonzero and contributes no order. Add $\binom r2$ to Proposition 6.1. ∎

## 6.3 Universal symbolic residual determinant

For the universal term $i$, define the symbolic depth

$$
\boxed{
\mathscr H_i
=
\sum_{j=1}^{S}E_{ij}R_j.
}
$$

For fixed residue pattern $\mathbf s$, this specializes to the actual cyclotomic depth, because

$$
R_j=\left\lfloor\frac{A_j}{d}\right\rfloor.
$$

Using $\mathscr H_i$ and the universal units $\mathscr U_i$, define

$$
\mathscr A_{p,i}(x)
=
\sum_{k=0}^{p}
\binom pk
(\mathscr H_i)_{p-k}
x^k\mathscr U_i^{(k)}(x),
$$

and

$$
\boxed{
\mathscr Q_{I,\mathbf s}(x)
=
\det\bigl(
\mathscr A_{p,i}(x)
\bigr)_{0\le p<|I|,\ i\in I}.
}
$$

### Project Lemma 6.3 — Noetherian residual family

For every fixed $I$ and residue pattern $\mathbf s$,

$$
\boxed{
\mathscr Q_{I,\mathbf s}(x)
\in
\mathscr R_{d,m,S,\mathbf s}[[x]].
}
$$

Every actual residual Wronskian $Q_I$ is obtained by specialization of one such universal series.

#### Proof

Lemma 3.7 places every $\mathscr U_i$ in the Noetherian coefficient ring. Formal differentiation preserves that ring. Falling factorials in $\mathscr H_i$ are polynomials in the parameters. Finite sums, products, and determinants remain in the same power-series ring.

Corollary 3.8 shows that specialization recovers every actual normalized unit and depth, hence every actual residual determinant. ∎

## 6.4 Uniform residual multiplicity

### Project Theorem 6.4 — Uniform residual-Wronskian bound

For fixed $d,m,S$, there exists a finite integer

$$
\boxed{C_d(m,S)\ge0}
$$

such that, for every factorial circuit of top fan-in at most $m$, every independent subset $I$ of its summands satisfies

$$
\boxed{
0\le\operatorname{ord}_xQ_I\le C_d(m,S).
}
$$

The bound is independent of:

- the endpoint magnitudes $A_j$;
- the monomial exponents $\alpha_i$;
- the factorial exponents $e_{ij}$;
- the outer coefficients $c_i$.

#### Proof

Fix a subset $I$ and a residue pattern $\mathbf s$. Apply Lemma 4.1 to the universal series

$$
\mathscr Q_{I,\mathbf s}(x)
$$

over the Noetherian ring

$$
\mathscr R_{d,m,S,\mathbf s}.
$$

It gives a finite specialization-order bound

$$
C(I,\mathbf s).
$$

There are finitely many subsets $I\subseteq\{1,\ldots,m\}$ and finitely many residue patterns $\mathbf s\in\{0,\ldots,d-1\}^S$. Define

$$
C_d(m,S)
=
\max_{I,\mathbf s}C(I,\mathbf s).
$$

Consider an actual independent subset $I$. By Lemma 5.3, its Wronskian is nonzero. Proposition 6.1 then implies that its residual determinant $Q_I$ is nonzero. It is a specialization of $\mathscr Q_{I,\mathbf s}$, so Lemma 4.1 gives

$$
\operatorname{ord}_xQ_I\le C(I,\mathbf s)
\le C_d(m,S).
$$

Because $Q_I$ is a power series, its nonzero order is nonnegative. ∎

### Corollary 6.5 — Uniform shifted-Wronskian estimate

Every independent subset $I$ of size $r$ satisfies

$$
\boxed{
\sum_{i\in I}h_i
\le
\omega(T_i:i\in I)
\le
\sum_{i\in I}h_i+C_d(m,S).
}
$$

#### Proof

Apply Corollary 6.2 and Theorem 6.4. ∎

---

# 7. Vanishing sequences generated by the input terms

Let

$$
V=\operatorname{span}_{K}
\{T_1(\zeta e^x),\ldots,T_r(\zeta e^x)\}
\subseteq K((x)),
$$

where

$$
K=\mathbb Q(\zeta)
$$

and $r\le m$.

Let

$$
\nu_1<\cdots<\nu_\rho
$$

be the vanishing sequence of $V$, where

$$
\rho=\dim_KV.
$$

## 7.1 Minimum Wronskian weights

For $1\le j\le\rho$, define

$$
\boxed{
\Delta_j
=
\min_{
\substack{I\subseteq\{1,\ldots,r\}\\
|I|=j,\ I\text{ independent}}
}
\omega(T_i:i\in I).
}
$$

Set

$$
\Delta_0=0.
$$

### Project Lemma 7.1 — Wronskian min-max formula

For every $j$,

$$
\boxed{
\Delta_j
=
\nu_1+\cdots+\nu_j.
}
$$

#### Proof

Let $I$ be any independent $j$-subset, and let $W_I\subseteq V$ be its span. Let

$$
\mu_1<\cdots<\mu_j
$$

be the vanishing sequence of $W_I$.

Fix $1\le k\le j$. Suppose, for contradiction, that

$$
\mu_k<\nu_k.
$$

Choose an adapted basis

$$
w_1,\ldots,w_j
$$

of $W_I$ with orders $\mu_1<\cdots<\mu_j$. The first $k$ basis vectors have orders strictly less than $\nu_k$. Their images in

$$
V/V_{\ge\nu_k}
$$

are linearly independent: a nontrivial combination has order equal to the smallest order occurring among them, hence remains below $\nu_k$ and cannot lie in $V_{\ge\nu_k}$.

But an adapted basis of $V$ shows that

$$
\dim(V/V_{\ge\nu_k})=k-1,
$$

because exactly $g_1,\ldots,g_{k-1}$ have order below $\nu_k$. This contradiction proves

$$
\mu_k\ge\nu_k
\qquad(1\le k\le j).
$$

By Definition 5.5 and Corollary 5.4,

$$
\omega(T_i:i\in I)
=
\mu_1+\cdots+\mu_j
\ge
\nu_1+\cdots+\nu_j.
$$

Hence

$$
\Delta_j\ge\nu_1+\cdots+\nu_j.
$$

It remains to prove equality is attained by an input subset.

Choose an adapted basis

$$
g_1,\ldots,g_\rho
$$

of $V$. Let

$$
\pi_j:V\to V/V_{\ge\nu_{j+1}}
$$

for $j<\rho$, and take $\pi_\rho$ to be the identity map. The quotient has dimension $j$, with basis given by the images of

$$
g_1,\ldots,g_j.
$$

Because the input terms span $V$, their images span this quotient. Therefore one can choose $j$ input terms whose images are linearly independent. Their span has vanishing sequence exactly

$$
\nu_1,\ldots,\nu_j.
$$

For that subset, the shifted Wronskian weight is the required sum. Thus equality holds. ∎

---

# 8. Weighted linear matroids of term depths

The input terms define a linear matroid: a subset is independent exactly when the corresponding Laurent germs are linearly independent.

Assign weight

$$
w_i=h_i
$$

to input term $i$.

For $0\le j\le\rho$, define

$$
\boxed{
H_j
=
\min_{
\substack{I\subseteq\{1,\ldots,r\}\\
|I|=j,\ I\text{ independent}}
}
\sum_{i\in I}h_i.
}
$$

Set

$$
H_0=0.
$$

## 8.1 Greedy weight increments

### Classical Lemma 8.1 — Weighted matroid greedy theorem

Sort the input elements by nondecreasing weight, breaking ties arbitrarily. Scan them in that order and add an element whenever it preserves independence.

Let the selected elements have weights

$$
\eta_1\le\eta_2\le\cdots\le\eta_\rho.
$$

Then for every $j$, the first $j$ selected elements form a minimum-weight independent $j$-set. Therefore

$$
\boxed{
H_j=\eta_1+\cdots+\eta_j,
}
$$

and

$$
\boxed{
H_j-H_{j-1}=\eta_j
\in\{h_1,\ldots,h_r\}.
}
$$

#### Proof

List all input elements in nondecreasing weight order. For a real threshold $t$, let

$$
E_{<t}=\{e:w(e)<t\}.
$$

Immediately before the greedy algorithm selects its $k$-th element of weight $\eta_k$, it has already constructed a basis of the span of all elements of weight strictly less than $\eta_k$. Hence

$$
\operatorname{rank}(E_{<\eta_k})\le k-1.
$$

Now let $I$ be any independent set of size $j$, and write its weights in nondecreasing order as

$$
\theta_1\le\cdots\le\theta_j.
$$

If $\theta_k<\eta_k$ for some $k$, then the first $k$ elements of $I$ would form an independent $k$-set contained in

$$
E_{<\eta_k},
$$

forcing

$$
\operatorname{rank}(E_{<\eta_k})\ge k,
$$

a contradiction. Therefore

$$
\theta_k\ge\eta_k
\qquad(1\le k\le j).
$$

Summing gives

$$
\sum_{e\in I}w(e)
\ge
\eta_1+\cdots+\eta_j.
$$

The first $j$ greedy selections are themselves independent and have exactly that weight, so they are minimum. The displayed formulas follow. ∎

### Caution 8.2 — Negative weights

The greedy theorem remains valid when depths are negative. Only their total ordering is used.

---

# 9. The Arbitrary-Rank Factorial-Circuit Contact Theorem

We now combine the Wronskian and matroid estimates.

### Project Theorem 9.1 — Arbitrary-Rank Factorial-Circuit Contact Theorem

Fix

$$
d\ge1,
\qquad
m\ge1,
\qquad
S\ge0.
$$

There exists a finite integer

$$
C_d(m,S)\ge0
$$

with the following property.

Let

$$
F(q)
=
\sum_{i=1}^{r}c_iT_i(q),
\qquad
1\le r\le m,
$$

be a factorial circuit using at most $S$ distinct endpoints, and let

$$
h_i=v_{\Phi_d}(T_i).
$$

If

$$
F\not\equiv0,
$$

then there exists an input index $i$ such that

$$
\boxed{
\left|
\operatorname{ord}_{\zeta_d}F-h_i
\right|
\le C_d(m,S).
}
$$

Equivalently,

$$
\boxed{
\operatorname{ord}_{\zeta_d}F
\in
\bigcup_{i=1}^{r}
[h_i-C_d(m,S),h_i+C_d(m,S)].
}
$$

The constant is independent of all numerical circuit parameters other than $d,m,S$.

#### Proof

Let

$$
V=
\operatorname{span}_{K}
\{T_1(\zeta e^x),\ldots,T_r(\zeta e^x)\},
\qquad
K=\mathbb Q(\zeta).
$$

Let

$$
\rho=\dim_KV
$$

and let

$$
\nu_1<\cdots<\nu_\rho
$$

be its vanishing sequence.

By Corollary 5.2, the nonzero element

$$
F(\zeta e^x)\in V
$$

has order

$$
\operatorname{ord}_{\zeta}F=\nu_j
$$

for some $j$.

By Lemma 7.1,

$$
\Delta_j
=
\nu_1+\cdots+\nu_j.
$$

By Corollary 6.5, every independent $j$-subset $I$ satisfies

$$
\sum_{i\in I}h_i
\le
\omega(T_i:i\in I)
\le
\sum_{i\in I}h_i+C_d(m,S).
$$

Taking minima over independent $j$-subsets gives

$$
\boxed{
H_j\le\Delta_j\le H_j+C_d(m,S).
}
$$

Write

$$
\Delta_j=H_j+\varepsilon_j,
\qquad
0\le\varepsilon_j\le C_d(m,S),
$$

and set

$$
\varepsilon_0=0.
$$

By Lemma 8.1,

$$
H_j-H_{j-1}=\eta_j
$$

for some input depth

$$
\eta_j\in\{h_1,\ldots,h_r\}.
$$

Therefore

$$
\begin{aligned}
\nu_j
&=
\Delta_j-\Delta_{j-1}\\
&=
(H_j-H_{j-1})
+(\varepsilon_j-\varepsilon_{j-1})\\
&=
\eta_j+\varepsilon_j-\varepsilon_{j-1}.
\end{aligned}
$$

Because both $\varepsilon_j$ and $\varepsilon_{j-1}$ lie in

$$
[0,C_d(m,S)],
$$

we obtain

$$
|\nu_j-\eta_j|
\le C_d(m,S).
$$

Since $\eta_j$ is one of the input depths and

$$
\operatorname{ord}_{\zeta}F=\nu_j,
$$

the claimed window follows. ∎

## 9.1 Common-depth form

### Corollary 9.2 — Common-depth multiplicity bound

Assume all nonzero input terms have the same depth

$$
h_1=\cdots=h_r=h.
$$

Then either $F\equiv0$, or

$$
\boxed{
h\le\operatorname{ord}_{\zeta_d}F\le h+C_d(m,S).}
$$

#### Proof

Every summand lies in

$$
x^hK[[x]],
$$

so their sum has order at least $h$ unless it is zero. Theorem 9.1 gives the upper bound because every depth window is centered at $h$. ∎

### Corollary 9.3 — Common-depth one-context identity criterion

Under the hypotheses of Corollary 9.2,

$$
\boxed{
F\equiv0
\iff
[x^{h+n}]F(\zeta_de^x)=0
\quad(0\le n\le C_d(m,S)).
}
$$

Equivalently,

$$
F\equiv0
$$

if and only if the first

$$
C_d(m,S)+1
$$

regularized Euler jets vanish.

#### Proof

The forward implication is immediate. Conversely, if the displayed coefficients vanish and $F\ne0$, then its order is at least

$$
h+C_d(m,S)+1,
$$

contradicting Corollary 9.2. ∎

## 9.2 Unequal-depth form

### Corollary 9.4 — Finite unequal-depth certificate

Define the finite set of candidate orders

$$
\boxed{
\mathcal W_d(F)
=
\bigcup_{i=1}^{r}
\left(
[h_i-C_d(m,S),h_i+C_d(m,S)]
\cap\mathbb Z
\right).
}
$$

Then

$$
\boxed{
F\equiv0
\iff
[x^n]F(\zeta_de^x)=0
\quad\text{for every }n\in\mathcal W_d(F).
}
$$

#### Proof

If $F\equiv0$, every Laurent coefficient vanishes.

Suppose the coefficients vanish on $\mathcal W_d(F)$, but $F\ne0$. Its first nonzero Laurent exponent is

$$
\operatorname{ord}_{\zeta_d}F.
$$

Theorem 9.1 places that integer in $\mathcal W_d(F)$, contradicting the assumed vanishing. ∎

### Corollary 9.5 — Certificate-size bound

The number of Laurent coefficients requested by Corollary 9.4 is at most

$$
\boxed{
r(2C_d(m,S)+1)
\le
m(2C_d(m,S)+1).
}
$$

Overlaps between windows can only reduce the number.

---

# 10. Depth separation and cancellation geometry

The main theorem does not claim that depth blocks can always be analyzed independently. A block of smaller input depth may acquire excess contact and meet the initial order of a deeper block; their leading coefficients can then cancel. What is true is a precise separation statement when the depth gap exceeds the universal residual bound.

For each integer $h$, define the depth block

$$
F_h(q)
=
\sum_{i:h_i=h}c_iT_i(q).
$$

Every nonzero block has common depth $h$, so Corollary 9.2 gives

$$
\boxed{
h\le\operatorname{ord}_{\zeta}F_h\le h+C_d(m,S).}
$$

### Proposition 10.1 — Isolated minimal-depth block

Let $h_0$ be the smallest input depth. Assume:

1. the block $F_{h_0}$ is not identically zero;
2. every other input depth satisfies
   $$
   h>h_0+C_d(m,S).
   $$

Then

$$
\boxed{
\operatorname{ord}_{\zeta}F
=
\operatorname{ord}_{\zeta}F_{h_0}
\in
[h_0,h_0+C_d(m,S)].
}
$$

#### Proof

Corollary 9.2 gives

$$
\operatorname{ord}_{\zeta}F_{h_0}
\le h_0+C_d(m,S).
$$

Every term outside the minimal block has order equal to its depth and hence strictly greater than $h_0+C_d(m,S)$. Therefore no higher-depth term contributes to the leading coefficient of $F_{h_0}$, and the total sum has the same order. ∎

### Corollary 10.2 — Iterative elimination across large gaps

Suppose the distinct input depths are grouped into clusters such that consecutive clusters are separated by more than $C_d(m,S)$. Starting from the lowest cluster:

- if its total contribution is nonzero, its leading order cannot be cancelled by any higher cluster;
- if it vanishes identically, it may be deleted and the argument repeated.

#### Proof

Apply Proposition 10.1 after treating all terms in the lowest cluster as one combined subcircuit. If that subcircuit is zero, remove it. Otherwise its order lies no higher than the top of its $C_d(m,S)$-neighborhood, while the next cluster begins beyond that neighborhood. ∎

### Caution 10.3 — Nearby depth blocks may interact

If two depth levels differ by at most $C_d(m,S)$, excess contact in the shallower block may bring its first nonzero term to the same order as the deeper block. Cross-block cancellation is then possible. The arbitrary-rank theorem already includes this phenomenon; no simpler blockwise minimum formula is valid in general.

### Interpretation 10.4

The depth windows define the only zones in which finite cross-depth interaction can occur. Exact cancellation may remove an entire block, while nonzero residual cancellation remains confined to bounded neighborhoods of the input depths.

---

# 11. Why compact logarithmic differentiation alone is insufficient

The successful theorem depends on the finite polynomial parameterization of the complete family, not merely on the existence of short logarithmic derivatives.

### Proposition 11.1 — Failure of the naive differential-complexity principle

There is no universal multiplicity bound depending only on the number of analytic units and on the fact that their logarithmic derivatives have short formulas.

#### Proof

For arbitrary $N\ge2$, define

$$
f_1(x)=1,
\qquad
f_2(x)=1+x,
\qquad
f_3(x)=1+2x+x^N.
$$

All three are analytic units at $x=0$, and each logarithmic derivative is represented by a rational function of constant descriptive size apart from the binary encoding of $N$:

$$
\frac{f_1'}{f_1}=0,
\qquad
\frac{f_2'}{f_2}=\frac1{1+x},
\qquad
\frac{f_3'}{f_3}=
\frac{2+Nx^{N-1}}{1+2x+x^N}.
$$

However,

$$
\boxed{
f_3-2f_2+f_1=x^N.}
$$

The contact order is $N$, which is unbounded.

Thus short logarithmic differentiation, by itself, does not control cancellation depth. ∎

### Interpretation 11.2

The factorial-circuit theorem succeeds because the entire coefficient family is contained in one finitely generated algebraic parameter ring for fixed $d,m,S$. The relevant hypothesis is not merely computational compactness; it is **Noetherian algebraic uniformity of all local coefficients**.

---

# 12. The explicit endpoint-jump theorem at $q=1$

The general constant $C_d(m,S)$ is not explicit. A strong effective theorem is available for a single multiplicative direction at $q=1$.

## 12.1 Cumulative power sums

For $a\ge0$, define

$$
S_k(a)=\sum_{n=1}^{a}n^k.
$$

Set

$$
S_k(0)=0.
$$

### Project Lemma 12.1 — Nested cumulative-moment determinant

Let

$$
0<a_1<a_2<\cdots<a_s
$$

and let

$$
0<\lambda_1<\lambda_2<\cdots.
$$

Define

$$
M_{r,i}
=
\sum_{n=1}^{a_i}\lambda_n^r,
\qquad
0\le r<s,
\qquad
1\le i\le s.
$$

Then

$$
\boxed{
\det(M_{r,i})_{0\le r<s,\ 1\le i\le s}>0.
}
$$

#### Proof

Let $A=a_s$. Define the matrices

$$
V_{r,n}=\lambda_n^r,
\qquad
0\le r<s,
\quad
1\le n\le A,
$$

and

$$
C_{n,i}=\mathbf1_{n\le a_i},
\qquad
1\le n\le A,
\quad
1\le i\le s.
$$

Then

$$
M=VC.
$$

By the Cauchy--Binet formula,

$$
\det M
=
\sum_{1\le n_1<\cdots<n_s\le A}
\det(V_{[:,n_1,\ldots,n_s]})
\det(C_{[n_1,\ldots,n_s],:}).
$$

The first determinant is the Vandermonde determinant

$$
\prod_{1\le u<v\le s}
(\lambda_{n_v}-\lambda_{n_u}),
$$

which is strictly positive.

For the staircase matrix $C$, every ordered minor is either zero or one. Indeed, the row indexed by $n_k$ changes from zero to one at the first column $i$ satisfying $n_k\le a_i$. The determinant is one exactly when these transition columns are all distinct.

At least one minor is one: choose

$$
n_i=a_i.
$$

Then

$$
C_{a_k,i}=\mathbf1_{a_k\le a_i}
=
\mathbf1_{k\le i},
$$

which is upper triangular with diagonal entries one.

Every nonzero summand in the Cauchy--Binet expansion is therefore positive, and at least one summand is positive. Hence $\det M>0$. ∎

### Corollary 12.2 — Even cumulative moments are independent

For distinct positive cutoffs $a_1<\cdots<a_s$, the matrix

$$
\boxed{
\bigl(S_{2r}(a_i)\bigr)_{0\le r<s,\ 1\le i\le s}
}
$$

is invertible.

#### Proof

Apply Lemma 12.1 with

$$
\lambda_n=n^2.
$$

Then

$$
\sum_{n=1}^{a_i}\lambda_n^r
=
\sum_{n=1}^{a_i}n^{2r}
=S_{2r}(a_i).
$$

∎

## 12.2 Zero-depth factorial ratios

Let

$$
R(q)
=
q^\beta
\prod_{i=1}^{s}(q;q)_{a_i}^{e_i},
$$

where

$$
0<a_1<\cdots<a_s,
\qquad
e_i\in\mathbb Z\setminus\{0\}.
$$

Assume zero depth at $q=1$:

$$
\boxed{
\sum_{i=1}^{s}e_i a_i=0.
}
$$

Then the regularized value

$$
B=\lim_{q\to1}R(q)
$$

is finite and nonzero.

### Lemma 12.3 — Exact logarithmic expansion

Put $q=e^x$. Then

$$
\boxed{
\log\frac{R(e^x)}B
=
\Lambda x
+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}
M_{2r}x^{2r},
}
$$

where

$$
\boxed{
\Lambda
=
\beta+
\frac12\sum_{i=1}^{s}e_iS_1(a_i)
}
$$

and

$$
\boxed{
M_{2r}
=
\sum_{i=1}^{s}e_iS_{2r}(a_i).
}
$$

#### Proof

For one linear factor,

$$
1-e^{nx}
=
-nx\,
\frac{e^{nx}-1}{nx}.
$$

The regularized singular expansion from Part IV is

$$
\log\frac{e^{nx}-1}{nx}
=
\frac{nx}{2}
+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}
 n^{2r}x^{2r}.
$$

Multiplying over $1\le n\le a_i$, raising to exponent $e_i$, and summing logarithms gives:

- a total power of $x$ equal to $\sum e_i a_i$, which is zero by hypothesis;
- a constant term absorbed into $B$;
- a linear term
  $$
  \beta x+
  \frac12
  \sum_i e_i
  \sum_{n=1}^{a_i}nx;
  $$
- an even term of order $2r$ proportional to
  $$
  \sum_i e_i
  \sum_{n=1}^{a_i}n^{2r}.
  $$

This is exactly the displayed formula. ∎

### Project Theorem 12.4 — Sharp endpoint-jump multiplicity theorem

If $R$ is nonconstant, then

$$
\boxed{
\operatorname{ord}_{q=1}
\left(
\frac{R(q)}B-1
\right)
\le2s-2.
}
$$

More precisely:

1. if $\Lambda\ne0$, the order is $1$;
2. if $\Lambda=0$, then
   $$
   \operatorname{ord}_{q=1}
   \left(\frac RB-1\right)
   =2r_*,
   $$
   where
   $$
   r_*
   =
   \min\{r\ge1:M_{2r}\ne0\},
   $$
   and necessarily
   $$
   r_*\le s-1.
   $$

#### Proof

By Lemma 12.3, the first nonzero term in

$$
\log(R/B)
$$

has the same order as the first nonzero term in

$$
R/B-1,
$$

because formal exponential preserves the first nonzero order.

If $\Lambda\ne0$, the order is one.

Assume $\Lambda=0$. The zero-depth condition is

$$
M_0
=
\sum_i e_iS_0(a_i)
=
\sum_i e_ia_i
=0.
$$

Suppose for contradiction that

$$
M_2=M_4=\cdots=M_{2s-2}=0.
$$

Then the nonzero exponent vector

$$
(e_1,\ldots,e_s)^T
$$

lies in the kernel of the matrix

$$
\bigl(S_{2r}(a_i)\bigr)_{0\le r<s,\ 1\le i\le s}.
$$

Corollary 12.2 says this matrix is invertible, a contradiction.

Therefore some

$$
M_{2r}\ne0
$$

with

$$
1\le r\le s-1.
$$

The order is the corresponding $2r$, hence at most $2s-2$. ∎

## 12.3 Universal sharpness

### Project Theorem 12.5 — Sharpness for every endpoint set

For every endpoint set

$$
0<a_1<\cdots<a_s
$$

with $s\ge2$, there exist integers

$$
e_1,\ldots,e_s
$$

and $\beta\in\mathbb Z$ such that the resulting nonconstant zero-depth ratio satisfies

$$
\boxed{
\operatorname{ord}_{q=1}
\left(
\frac{R(q)}{R(1)}-1
\right)
=2s-2.
}
$$

#### Proof

Consider the $(s-1)\times s$ matrix

$$
\bigl(S_{2r}(a_i)\bigr)_{0\le r\le s-2}.
$$

It has rank $s-1$, because it is obtained by deleting the last row from the invertible matrix in Corollary 12.2. Its nullspace is therefore one-dimensional and contains a nonzero rational vector

$$
(e_1,\ldots,e_s).
$$

Scale to make every $e_i$ integral. The row $r=0$ gives the zero-depth condition

$$
\sum_i e_ia_i=0.
$$

The full matrix is invertible, so the deleted final row does not annihilate this vector:

$$
\sum_i e_iS_{2s-2}(a_i)\ne0.
$$

Multiply all $e_i$ by two if necessary so that

$$
\beta
=
-\frac12\sum_i e_iS_1(a_i)
$$

is an integer. Then $\Lambda=0$, all moments through $2s-4$ vanish, and the moment of order $2s-2$ is nonzero. Theorem 12.4 gives exact contact order $2s-2$. ∎

### Example 12.6 — Two endpoints

Take

$$
R(q)
=
q\frac{(q;q)_1^4}{(q;q)_2^2}
=
\frac{q}{(1+q)^2}.
$$

Then

$$
R(1)=\frac14,
$$

and

$$
\boxed{
\frac{R(q)}{R(1)}-1
=
-\frac{(q-1)^2}{(q+1)^2}.
}
$$

The contact order is exactly two, equal to $2s-2$.

### Example 12.7 — Three endpoints

Take

$$
R(q)
=
q\frac{(q;q)_1^{13}(q;q)_3^3}{(q;q)_2^{11}}
=
q\frac{(1+q+q^2)^3}{(1+q)^8}.
$$

Its normalized germ has contact order four at $q=1$, saturating the bound for $s=3$.

---

# 13. Effective affine-line factorial circuits

The endpoint-jump theorem becomes a complete explicit identity bound when all exponent vectors lie on one affine line.

## 13.1 Circuit form

Let

$$
T_0(q)
$$

be a nonzero compressed factorial term, and let

$$
R(q)
$$

be a zero-depth factorial ratio at $q=1$ with

$$
B=R(1)\ne0.
$$

Let

$$
n_1,\ldots,n_m\in\mathbb Z
$$

be distinct, and define

$$
\boxed{
F(q)
=
T_0(q)
\sum_{\nu=1}^{m}c_\nu R(q)^{n_\nu}.
}
$$

The canonical exponent vectors of the summands lie on the affine line

$$
u_0+n_\nu v.
$$

## 13.2 Composition of local orders

### Lemma 13.1 — Composition multiplicity

Let $P(z)\in K[z,z^{-1}]$, let $B\ne0$, and let $R(q)$ satisfy

$$
R(q)-B
$$

of finite order $\rho$ at $q=1$. If

$$
\mu=\operatorname{ord}_{z=B}P(z),
$$

then

$$
\boxed{
\operatorname{ord}_{q=1}P(R(q))
=\mu\rho.
}
$$

#### Proof

Factor in the local ring at $z=B$:

$$
P(z)=(z-B)^\mu U(z),
\qquad
U(B)\ne0.
$$

Substituting $z=R(q)$ gives

$$
P(R(q))=(R(q)-B)^\mu U(R(q)).
$$

The second factor is a local unit at $q=1$, so the order is $\mu\rho$. ∎

## 13.3 Sparse outer polynomial

Define

$$
P(z)=\sum_{\nu=1}^{m}c_\nu z^{n_\nu}.
$$

Part XI gives the sharp sparse contact bound

$$
\boxed{
P\ne0
\quad\Longrightarrow\quad
\operatorname{ord}_{z=B}P\le m-1.
}
$$

### Project Theorem 13.2 — Effective affine-line multiplicity theorem

Suppose $R$ has $s$ distinct factorial endpoints and is nonconstant. Then, if the inner sum is nonzero,

$$
\boxed{
\operatorname{ord}_{q=1}
\sum_{\nu=1}^{m}c_\nu R(q)^{n_\nu}
\le
(m-1)(2s-2).
}
$$

If $T_0$ has depth $h_0$ at $q=1$, then

$$
\boxed{
\operatorname{ord}_{q=1}F
\le
h_0+(m-1)(2s-2).
}
$$

#### Proof

Let

$$
\rho
=
\operatorname{ord}_{q=1}(R/B-1)
=
\operatorname{ord}_{q=1}(R-B).
$$

Theorem 12.4 gives

$$
\rho\le2s-2.
$$

The sparse outer polynomial has multiplicity

$$
\mu\le m-1
$$

at $z=B$. Lemma 13.1 gives

$$
\operatorname{ord}_{q=1}P(R(q))
=
\mu\rho
\le
(m-1)(2s-2).
$$

Multiplication by $T_0$ adds its local depth $h_0$. ∎

### Corollary 13.3 — Explicit affine-line identity certificate

The affine-line circuit is identically zero if and only if its coefficients from order

$$
h_0
$$

through

$$
h_0+(m-1)(2s-2)
$$

all vanish at $q=1$.

The certificate length is

$$
\boxed{(m-1)(2s-2)+1.}
$$

## 13.4 Sharpness at two endpoints

### Project Theorem 13.4 — Multi-term sharpness

For every $m\ge1$, there is an $m$-term polynomial factorial circuit with two endpoint jumps whose contact order at $q=1$ is exactly

$$
2m-2.
$$

#### Proof

Take

$$
R(q)=\frac{q}{(1+q)^2},
\qquad
B=\frac14.
$$

Then

$$
4R(q)-1
=
-\frac{(q-1)^2}{(q+1)^2}.
$$

Let

$$
P(z)=(4z-1)^{m-1}.
$$

It has exactly $m$ terms in its binomial expansion and multiplicity $m-1$ at $z=B$. Hence

$$
P(R(q))
=
(-1)^{m-1}
\frac{(q-1)^{2m-2}}{(q+1)^{2m-2}}.
$$

Multiplying by $(1+q)^{2m-2}$, which is itself representable by factorial quotients, yields the polynomial identity

$$
\boxed{
\sum_{k=0}^{m-1}
(-1)^{m-1-k}
\binom{m-1}{k}
4^kq^k(1+q)^{2(m-1-k)}
=
(-1)^{m-1}(q-1)^{2m-2}.
}
$$

The left side has $m$ compressed summands and contact order exactly $2m-2$. This equals

$$
(m-1)(2s-2)
$$

for $s=2$. ∎

---

# 14. Transfer to nested product systems

The determinant mechanism is not intrinsically tied to $q$-factorials.

Let

$$
0<\lambda_1<\lambda_2<\cdots
$$

and define nested products

$$
\boxed{
U_a(x)=\prod_{j=1}^{a}(1+\lambda_jx).
}
$$

Consider

$$
R(x)=\prod_{i=1}^{s}U_{a_i}(x)^{e_i},
\qquad
0<a_1<\cdots<a_s.
$$

Because every $U_a(0)=1$, one has $R(0)=1$.

### Theorem 14.1 — Nested-product contact bound

If $R\not\equiv1$, then

$$
\boxed{
\operatorname{ord}_{x=0}(R(x)-1)\le s.
}
$$

#### Proof

The logarithm is

$$
\begin{aligned}
\log R(x)
&=
\sum_{i=1}^{s}e_i
\sum_{j=1}^{a_i}
\log(1+\lambda_jx)\\
&=
\sum_{r\ge1}
\frac{(-1)^{r-1}}r
\left(
\sum_{i=1}^{s}e_i
\sum_{j=1}^{a_i}\lambda_j^r
\right)x^r.
\end{aligned}
$$

Suppose the coefficients through order $s$ vanish. Then the exponent vector $(e_i)$ is annihilated by the matrix

$$
N_{r,i}
=
\sum_{j=1}^{a_i}\lambda_j^r,
\qquad
1\le r\le s.
$$

Factor $\lambda_j$ from every selected Vandermonde column in the Cauchy--Binet proof of Lemma 12.1. Because every $\lambda_j>0$, the determinant of $(N_{r,i})$ is strictly positive. Hence the exponent vector is zero, contradicting $R\not\equiv1$.

Therefore the logarithm has a nonzero coefficient of order at most $s$. Formal exponential preserves the first nonzero order, proving the theorem. ∎

### Theorem 14.2 — Nested-product affine-line bound

Let

$$
P(z)=\sum_{\nu=1}^{m}c_\nu z^{n_\nu}
$$

be a nonzero $m$-sparse Laurent polynomial. Then

$$
\boxed{
\operatorname{ord}_{x=0}P(R(x))
\le s(m-1).
}
$$

#### Proof

Theorem 14.1 gives

$$
\operatorname{ord}_{x=0}(R-1)\le s.
$$

Part XI gives

$$
\operatorname{ord}_{z=1}P\le m-1.
$$

Apply Lemma 13.1. ∎

### Interpretation 14.3

The underlying phenomenon is:

$$
\boxed{
\text{nested cutoffs}
+
\text{strict moment ordering}
\Longrightarrow
\text{finite endpoint-controlled contact}.
}
$$

The $q$-factorial theorem is therefore an application of a broader cumulative-moment rigidity principle rather than an isolated Gaussian identity.

---

# 15. Differential and computational formulations

## 15.1 Euler-jet form

For a common-depth circuit, write

$$
F(\zeta e^x)=x^hG(x).
$$

Then

$$
G^{(n)}(0)
$$

is the regularized Euler jet of order $n$.

Corollary 9.3 becomes:

### Corollary 15.1 — Regularized Euler-jet determination

There exists $C_d(m,S)$ such that

$$
\boxed{
F\equiv0
\iff
G^{(n)}(0)=0
\quad(0\le n\le C_d(m,S)).
}
$$

Equivalently,

$$
\boxed{
D^{h+n}F(\zeta)=0
\quad(0\le n\le C_d(m,S))
}
$$

when $h\ge0$, with the usual factorial normalization between Laurent coefficients and derivatives.

## 15.2 Exact coefficient computation

Part VI gives exact non-expanding algorithms for the local residual and every finite collection of cumulants of one factorial term. Bell-polynomial reconstruction gives its finite jet.

Therefore, once a valid explicit value of $C_d(m,S)$ is known, the identity certificate can be checked without expanding any summand.

### Algorithmic Corollary 15.2 — Conditional deterministic PIT

Assume an explicit computable upper bound

$$
\widehat C_d(m,S)\ge C_d(m,S)
$$

is supplied.

Then identity of a common-depth factorial circuit can be decided by:

1. canonicalizing the endpoint union;
2. computing the common depth $h$;
3. computing every summand's regularized jets through order $\widehat C_d(m,S)$;
4. adding them with the outer coefficients;
5. declaring identity exactly when every resulting jet vanishes.

The procedure is exact.

#### Proof

The jet algorithms are correct by Parts IV and VI. Corollary 9.3 proves that the finite vanishing test is equivalent to identity. ∎

### Caution 15.3 — Present complexity status

Theorem 9.1 alone does not provide $\widehat C_d(m,S)$. Therefore the arbitrary-rank theorem is presently a finite-determination theorem, not yet an explicit deterministic polynomial-time PIT theorem.

For the affine-line class, Theorem 13.2 supplies the explicit bound

$$
(m-1)(2s-2),
$$

so the corresponding PIT is effective.

---

# 16. Structural consequences

## 16.1 Endpoint-independent contact capacity

### Corollary 16.1

For fixed $d,m,S$, increasing the endpoint magnitudes

$$
A_j
$$

cannot create arbitrarily deep finite cancellation among nonzero factorial circuits unless an exact linear dependency appears.

#### Proof

All nonzero finite orders remain inside the bounded windows of Theorem 9.1. Exact dependencies correspond to the zero element and infinite order. ∎

## 16.2 Dichotomy between identity and bounded contact

### Corollary 16.2

For a common-depth family with fixed $d,m,S$, every specialization satisfies the dichotomy

$$
\boxed{
\text{either the combination is identically zero,}
\quad\text{or its excess contact is at most }C_d(m,S).
}
$$

This excludes sequences of nonzero circuits of fixed structural size whose contact tends to infinity.

## 16.3 Arbitrary affine rank

The proof never restricts the affine rank of the exponent vectors

$$
(\alpha_i,e_{i1},\ldots,e_{iS}).
$$

Thus Theorem 9.1 applies to:

- one affine direction;
- several independent directions;
- full affine rank;
- linearly dependent input terms;
- exact vanishing subsums;
- unequal cyclotomic depths.

The affine-line theorem is distinguished only because its bound is explicit and sharp.

## 16.4 Stability under monomial multiplication

Multiplying every term by one common monomial $q^L$ changes neither its cyclotomic depth nor the excess-contact bound.

Multiplying by a common factorial quotient adds one common depth to every term and translates every candidate-order window by that amount.

---

# 17. Examples and edge cases

## 17.1 One term

For $m=1$, every nonzero circuit is one factorial term. Its order is exactly its depth:

$$
\operatorname{ord}_{\zeta}F=h_1.
$$

Thus one may take

$$
\boxed{C_d(1,S)=0.}
$$

## 17.2 No factorial endpoints

For $S=0$, the circuit is a sparse Laurent polynomial

$$
F(q)=\sum_{i=1}^{m}c_iq^{\alpha_i}.
$$

Part XI gives the explicit sharp bound

$$
\operatorname{ord}_{\zeta}F\le m-1
$$

when the depths are all zero.

Thus one may take

$$
\boxed{C_d(m,0)=m-1.}
$$

The general Noetherian theorem is compatible with, but weaker than, this explicit result.

## 17.3 Proportional terms

If

$$
T_2=\lambda T_1,
\qquad
\lambda\ne0,
$$

then a suitable two-term combination may vanish identically. The Wronskian is zero, and such a subset is excluded from the independent-subset estimates.

If the outer coefficients do not create exact cancellation, the resulting sum is again proportional to $T_1$ and has order exactly $h_1$.

## 17.4 Distinct depths

Suppose

$$
h_1<h_2-C_d(m,S).
$$

Then no nonzero linear combination involving a surviving contribution from term one can have order near $h_2$. Either the entire shallower-depth contribution cancels identically, or the total order remains in the window around $h_1$.

This is a direct instance of the depth-block interpretation.

## 17.5 Root-of-unity residue patterns

At $d>1$, two endpoints with the same quotient $R$ but different residues $s$ have different normalized local units. The proof handles this by splitting into finitely many residue patterns before applying Noetherianity.

No uniformity in $d$ is claimed. The constant may grow with the cyclotomic order.

---

# 18. Theorem inventory

| Result | Statement | Status | Role |
|---|---|---|---|
| Polynomial progression sums | Residue-channel moments are polynomial in endpoint quotients | Classical lemma | Finite parameterization |
| Universal coefficient ring | All normalized local coefficients lie in one Noetherian polynomial ring | Project lemma | Algebraic uniformity |
| Noetherian coefficient bound | A universal power series has uniformly bounded nonzero specialization order | Classical lemma | Bautin mechanism |
| Formal Wronskian criterion | Independence is equivalent to nonzero Wronskian | Classical lemma | Detecting exact dependencies |
| Residual-Wronskian factorization | Depth contribution separates from a unit determinant | Project proposition | Local multiplicity decomposition |
| Uniform residual bound | Every nonzero residual Wronskian has bounded order | Project theorem | Arbitrary-rank control |
| Wronskian min-max formula | Minimum shifted Wronskian weight equals partial sum of the vanishing sequence | Project lemma | Passage from subsets to the whole span |
| Weighted matroid theorem | Minimum independent-set weights have greedy increments from input depths | Classical lemma | Relating vanishing orders to term depths |
| Arbitrary-Rank Contact Theorem | Every nonzero order lies near an input depth | Project theorem | Full finite determination |
| Common-depth criterion | Finitely many regularized jets decide identity | Corollary | One-context certificate |
| Unequal-depth certificate | Candidate-order windows decide identity | Corollary | General certificate |
| Cumulative-moment determinant | Nested endpoint moment matrix is strictly positive | Project lemma | Explicit endpoint rigidity |
| Endpoint-jump theorem | A zero-depth ratio has contact at most $2s-2$ | Project theorem | Explicit bound |
| Endpoint sharpness | The bound $2s-2$ is attained for every endpoint set | Project theorem | Optimality |
| Affine-line theorem | Contact at most $(m-1)(2s-2)$ | Project theorem | Effective PIT subclass |
| Nested-product transfer | Contact is bounded by cutoff count in general nested products | Project theorem | Non-specialized mechanism |

---

# 19. Boundaries and open problems

## 19.1 Explicit arbitrary-rank bound

The central remaining problem is to replace the Noetherian existence statement by an explicit estimate.

At $q=1$, the natural conjecture for common-depth circuits is

$$
\boxed{
C_1(m,S)
\le
2(m-1)(S-1).
}
$$

The affine-line construction with two endpoints proves that this scale is already sharp in one important subfamily.

A proof would upgrade Theorem 9.1 from structural finite determination to an explicit compressed PIT theorem.

## 19.2 Effective Bautin ideals

For each universal residual determinant

$$
\mathscr Q_{I,\mathbf s}(x)
=
\sum_{n\ge0}q_nx^n,
$$

determine an explicit finite generating set for the coefficient ideal

$$
(q_0,q_1,q_2,\ldots).
$$

Possible tools include:

- degree bounds for determinantal coefficient ideals;
- differential equations satisfied by the universal units;
- effective Hilbert basis estimates;
- Gröbner bases adapted to cumulant weight;
- finite recurrences in the endpoint quotient variables.

## 19.3 Growth in the cyclotomic order

The present theorem fixes $d$. Determine whether one can choose a bound polynomial in

$$
d,m,S
$$

or in

$$
\varphi(d),m,S.
$$

The residue-channel kernels and cyclotomic-field dimension both vary with $d$, so uniformity is not automatic.

## 19.4 Reconstruction, not only identity

Part XI recovers sparse monomial exponents and coefficients from local jets. Theorem 9.1 proves finite determination for factorial circuits but does not reconstruct the endpoint and exponent parameters.

Develop an arbitrary-rank reconstruction theory from a finite jet packet, including classification of unavoidable parameter nonuniqueness caused by exact factorial identities.

## 19.5 Integral and modular versions

The proof is over characteristic zero. In finite characteristic:

- Wronskian criteria require Hasse derivatives or additional hypotheses;
- falling factorials may vanish for arithmetic reasons;
- endpoint moment determinants can degenerate modulo the characteristic.

A modular theory requires separate treatment.

## 19.6 Other compressed product classes

The transfer theorem suggests studying:

- shifted $q$-Pochhammer symbols;
- ordinary rising and falling factorial products;
- gamma-function quotient germs;
- hypergeometric terms with finitely many moving cutoffs;
- orbit-product enumerators.

The decisive condition is a finitely generated algebraic parameter ring for every local coefficient together with a tractable residual Wronskian.

## 19.7 Formal verification

A proof-assistant implementation should formalize:

1. polynomiality of progression power sums;
2. the Noetherian coefficient lemma;
3. formal Laurent Wronskian valuation;
4. the Wronskian min-max formula;
5. weighted matroid greedy minima;
6. the arbitrary-rank contact theorem;
7. the cumulative-moment determinant and affine-line sharpness.

---

# 20. Final statement

For a factorial circuit

$$
F(q)
=
\sum_{i=1}^{r}
 c_iq^{\alpha_i}
 \prod_{j=1}^{S}(q;q)_{A_j}^{e_{ij}},
\qquad
r\le m,
$$

fix a primitive $d$-th root $\zeta_d$, and define the input depths

$$
\boxed{
 h_i
=
\sum_{j=1}^{S}
 e_{ij}
 \left\lfloor\frac{A_j}{d}\right\rfloor.
}
$$

For fixed $d,m,S$, the normalized local coefficients of every summand belong to one finitely generated polynomial parameter ring. Noetherianity therefore gives a finite uniform bound on every nonzero residual Wronskian.

Vanishing-sequence geometry and weighted matroid minima convert that Wronskian bound into the arbitrary-rank contact theorem:

$$
\boxed{
F\ne0
\quad\Longrightarrow\quad
\operatorname{ord}_{\zeta_d}F
\in
\bigcup_{i=1}^{r}
[h_i-C_d(m,S),h_i+C_d(m,S)].
}
$$

In particular, if all summands have common depth $h$, then

$$
\boxed{
F\ne0
\quad\Longrightarrow\quad
h\le\operatorname{ord}_{\zeta_d}F
\le h+C_d(m,S).
}
$$

Thus arbitrary-rank factorial circuits have finite endpoint-independent local contact capacity.

At $q=1$, a zero-depth ratio with $s$ endpoint jumps satisfies the explicit sharp law

$$
\boxed{
\operatorname{ord}_{q=1}
\left(\frac{R(q)}{R(1)}-1\right)
\le2s-2.
}
$$

For an $m$-term affine-line circuit, this yields

$$
\boxed{
\operatorname{ord}_{q=1}
\sum_{\nu=1}^{m}c_\nu R(q)^{n_\nu}
\le(m-1)(2s-2),
}
$$

and the bound is sharp already for two endpoint jumps.

The theory has therefore crossed the boundary left open in Part XI:

$$
\boxed{
\text{monomial sparsity}
\longrightarrow
\text{arbitrary sums of compressed dense factorial terms}.
}
$$

The remaining frontier is no longer existence of a finite identity bound. It is the explicit and complexity-theoretic problem of computing a sharp polynomial bound for

$$
C_d(m,S).
$$
