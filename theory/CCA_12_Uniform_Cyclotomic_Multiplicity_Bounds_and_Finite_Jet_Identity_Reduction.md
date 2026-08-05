# Cyclotomic Coefficient Arithmetic

## Part XII — Uniform Cyclotomic Multiplicity Bounds and Finite-Jet Identity Reduction

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete theorem chapter for uniform finite multiplicity and finite-jet reduction  
**Scope:** Sums of compressed factorial quotients, endpoint complexity, universal regularized factorial germs, residual Wronskians, Noetherian multiplicity bounds, vanishing sequences, weighted matroid profiles, depth clustering, exact finite-jet identity reduction, positive-endpoint fingerprint separation, lower bounds, Gaussian-multinomial consequences, and the remaining effectivity boundary for deterministic polynomial-time identity testing.

---

# 0. Purpose, relation to Parts VI, VIII, and XI, and status boundary

Part VI showed that a single compressed factorial quotient

\[
T(q)=q^\alpha\prod_j(q;q)_{A_j}^{e_j}
\]

admits exact, non-expanding computation of:

- its cyclotomic depth;
- its leading local residual;
- any prescribed finite list of cyclotomic cumulants;
- any prescribed finite local jet.

Part VIII proved that sufficiently many cyclotomic jets determine a polynomial once an expanded span bound is known.

Part XI replaced expanded span by ordinary monomial sparsity. For a Laurent polynomial with \(t\) nonzero monomials, one nonzero local context has contact capacity exactly \(t-1\).

The principal open problem left by Part XI was the passage from monomial sparsity to **compressed-term sparsity**:

> If a function is a sum of only a few compressed \(q\)-factorial quotients, is its local multiplicity bounded independently of the enormous expanded degrees of those terms?

The present chapter answers the finite-boundedness question affirmatively.

Fix:

- a cyclotomic context order \(d\);
- a top fan-in bound \(m\);
- a bound \(S\) on the number of distinct factorial endpoints used by the entire circuit.

Then there exists a finite constant

\[
\boxed{C_d(m,S)<\infty}
\]

such that every nonzero sum of at most \(m\) compressed factorial terms has local order within \(C_d(m,S)\) of the depth of one of its summands.

The proof has four layers:

\[
\boxed{
\text{polynomial universal germs}
\longrightarrow
\text{Noetherian residual Wronskians}
\longrightarrow
\text{vanishing-sequence control}
\longrightarrow
\text{uniform multiplicity bound}.
}
\]

This closes the **existence** of a general degree-free multiplicity bound for bounded compressed complexity.

It does **not** yet close the stronger uniform complexity claim. The argument proves that \(C_d(m,S)\) is finite, but it does not supply a polynomial upper bound in \(d,m,S\). Moreover, exact bit-complexity control for sums of enormous factored residuals requires an additional arithmetic representation theorem.

The precise status is therefore:

\[
\boxed{
\begin{array}{ll}
\text{Uniform finite multiplicity bound at fixed }(d,m,S):&\textbf{proved},\\[1mm]
\text{Finite exact jet reduction from any valid bound}:&\textbf{proved},\\[1mm]
\text{Polynomial bound for }C_d(m,S):&\textbf{open},\\[1mm]
\text{Uniform deterministic polynomial-time bit test}:&\textbf{open}.
\end{array}
}
\]

The chapter also proves a new explicit positive-endpoint fingerprint theorem: at \(q=1\), the first \(2S\) normalized logarithmic coefficients distinguish individual factorial terms supported on \(S\) fixed endpoints.

The labels used below are:

- **Classical lemma:** standard algebraic input, proved here;
- **Project theorem:** a theorem established in this project;
- **Algorithmic theorem:** an exact finite procedure once its stated bound is supplied;
- **Corollary:** a formal consequence;
- **Sharpness statement:** a lower bound or obstruction showing that a proposed estimate cannot hold;
- **Caution:** a distinction required for exact mathematics or software.

Throughout,

\[
D=q\frac d{dq},
\qquad
q=\zeta e^x,
\]

so that locally

\[
D=\frac d{dx}.
\]

All coefficient fields have characteristic zero.

---

# 1. Compressed factorial circuits

## 1.1 Canonical endpoint support

Let

\[
0<A_1<A_2<\cdots<A_S
\]

be distinct positive integers.

### Definition 1.1 — Factorial term

A **compressed factorial term** supported on the endpoints \(A_1,\ldots,A_S\) is a nonzero rational function

\[
\boxed{
T(q)
=
q^\alpha
\prod_{j=1}^{S}(q;q)_{A_j}^{e_j},
}
\]

where

\[
\alpha,e_j\in\mathbb Z.
\]

Zero exponents are allowed. Thus one common endpoint list may be used for all terms even when a particular term uses only part of it.

The endpoint \(0\) is omitted because

\[
(q;q)_0=1.
\]

### Definition 1.2 — Factorial circuit

A **factorial circuit** of top fan-in \(r\) is a sum

\[
\boxed{
F(q)=\sum_{i=1}^{r}c_iT_i(q),
}
\]

where

\[
0\ne c_i\in\mathbb Q,
\qquad
1\le r\le m,
\]

and every \(T_i\) is supported on the same canonical endpoint list

\[
A_1<\cdots<A_S.
\]

The number \(S\) is the **endpoint complexity** of the circuit.

### Caution 1.3 — Endpoint complexity does not count monomial shifts

The exponents \(\alpha_i\) of the monomial factors \(q^{\alpha_i}\) are not counted among the factorial endpoints.

This distinction is essential. Even with \(S=0\), a sum of \(m\) monomials can have local multiplicity \(m-1\). Therefore every universal multiplicity bound must contain a baseline depending on \(m\), independently of \(S\).

## 1.2 Local depth profile

Fix \(d\ge1\), and let \(\zeta\) be a primitive \(d\)-th root of unity.

Write

\[
A_j=dR_j+s_j,
\qquad
R_j\ge0,
\qquad
0\le s_j<d.
\]

For the term

\[
T_i(q)=q^{\alpha_i}\prod_{j=1}^{S}(q;q)_{A_j}^{e_{ij}},
\]

Part I gives

\[
\boxed{
h_i
:=
v_{\Phi_d}(T_i)
=
\sum_{j=1}^{S}e_{ij}R_j.
}
\]

The integer \(h_i\) is the **local depth** of the term.

Negative depths are permitted when an individual term has a pole. All local arguments take place in the Laurent-series field

\[
K((x)),
\qquad
K=\mathbb Q(\zeta).
\]

### Definition 1.4 — Depth profile

The multiset

\[
\boxed{
\mathcal H_d(F)=\{h_1,\ldots,h_r\}
}
\]

is the **depth profile** of the circuit at context \(d\).

### Definition 1.5 — Local order

For a nonzero local Laurent series

\[
f(x)=\sum_{n\ge N}a_nx^n,
\qquad
 a_N\ne0,
\]

define

\[
\operatorname{ord}_x f=N.
\]

For a nonzero rational function \(F(q)\), define

\[
\operatorname{ord}_{\zeta}F
=
\operatorname{ord}_xF(\zeta e^x).
\]

If \(F\in\mathbb Q[q,q^{-1}]\), then

\[
\operatorname{ord}_{\zeta}F
=
v_{\Phi_d}(F).
\]

For the zero function, set the order to \(+\infty\).

---

# 2. Universal regularized factorial germs

The Noetherian proof requires one uniform parameter space containing all normalized local germs with fixed residue data.

## 2.1 One endpoint

Fix a residue

\[
0\le s<d.
\]

For an integer \(R\ge0\), put

\[
A=dR+s.
\]

At \(q=\zeta e^x\), the factorial has order \(R\):

\[
(q;q)_{dR+s}\big|_{q=\zeta e^x}
=
B_{d,s}(R)x^R U_{d,s}(R;x),
\]

where

\[
B_{d,s}(R)\in K^\times,
\qquad
U_{d,s}(R;0)=1.
\]

An explicit leading scalar is

\[
B_{d,s}(R)
=
(-d)^R R!
\prod_{\substack{1\le n\le dR+s\\d\nmid n}}
(1-\zeta^n).
\]

### Lemma 2.1 — Exact normalized logarithm

For every integer \(R\ge0\),

\[
\boxed{
\begin{aligned}
\log U_{d,s}(R;x)
&=
\sum_{\ell=1}^{R}
\log\left(\frac{1-e^{d\ell x}}{-d\ell x}\right)\\
&\quad+
\sum_{\substack{1\le n\le dR+s\\d\nmid n}}
\log\left(
\frac{1-\zeta^ne^{nx}}{1-\zeta^n}
\right).
\end{aligned}
}
\]

Every logarithm is the formal logarithm of a series with constant term \(1\).

#### Proof

Expand

\[
(q;q)_{dR+s}
=
\prod_{n=1}^{dR+s}(1-q^n)
\]

at

\[
q=\zeta e^x.
\]

If \(n=d\ell\), then

\[
1-q^n
=
1-e^{d\ell x}
=
(-d\ell x)
\left(
\frac{1-e^{d\ell x}}{-d\ell x}
\right).
\]

If \(d\nmid n\), then \(1-\zeta^n\ne0\), and

\[
1-q^n
=
(1-\zeta^n)
\left(
\frac{1-\zeta^ne^{nx}}{1-\zeta^n}
\right).
\]

The product of all extracted factors \(-d\ell x\) and \(1-\zeta^n\) is exactly

\[
B_{d,s}(R)x^R.
\]

The remaining normalized factors all have constant term \(1\). Taking their formal logarithm gives the formula. ∎

## 2.2 Polynomial dependence on the endpoint quotient

Recall the universal one-factor cumulant kernel \(K_r(\rho)\) from Part IV. For \(r\ge1\), the \(r\)-th derivative at zero of the normalized logarithm in Lemma 2.1 is

\[
\begin{aligned}
\lambda_{d,s,r}(R)
&=
K_r(1)d^r\sum_{\ell=1}^{R}\ell^r\\
&\quad+
\sum_{a=1}^{d-1}K_r(\zeta^a)
\sum_{\substack{1\le n\le dR+s\\n\equiv a\pmod d}}n^r.
\end{aligned}
\]

For fixed \(d,s,r\), every sum on the right is an arithmetic-progression power sum.

### Project Theorem 2.2 — Polynomial universal endpoint germ

For fixed \(d\) and \(s\), there exists a unique formal power series

\[
\boxed{
\mathscr U_{d,s}(R;x)
\in
K[R][[x]]
}
\]

such that for every integer \(R\ge0\),

\[
\mathscr U_{d,s}(R;x)
=
U_{d,s}(R;x).
\]

Equivalently, for every \(n\ge0\), the coefficient

\[
[x^n]U_{d,s}(R;x)
\]

is a polynomial in \(R\) with coefficients in \(K\).

#### Proof

For every fixed \(r\ge1\), Lemma 2.1 and the one-factor cumulant formulas of Part IV give

\[
\left.
\frac{d^r}{dx^r}
\log U_{d,s}(R;x)
\right|_{x=0}
=
\lambda_{d,s,r}(R).
\]

The singular-channel sum

\[
\sum_{\ell=1}^{R}\ell^r
\]

is a polynomial in \(R\) by Faulhaber's theorem.

For a nonzero residue \(a\), the integers in the interval \([1,dR+s]\) congruent to \(a\pmod d\) are

\[
a,
\ a+d,
\ldots,
\ a+d(L_a(R)-1),
\]

where

\[
L_a(R)=
\begin{cases}
R+1,&a\le s,\\
R,&a>s.
\end{cases}
\]

Therefore

\[
\sum_{t=0}^{L_a(R)-1}(a+dt)^r
\]

is also a polynomial in \(R\).

Hence

\[
\lambda_{d,s,r}(R)\in K[R]
\]

for every \(r\).

Define

\[
\mathscr U_{d,s}(R;x)
=
\exp\left(
\sum_{r\ge1}
\lambda_{d,s,r}(R)\frac{x^r}{r!}
\right).
\]

The coefficient of \(x^n\) in this exponential is the complete Bell polynomial in

\[
\lambda_{d,s,1}(R),\ldots,\lambda_{d,s,n}(R),
\]

divided by \(n!\). It therefore lies in \(K[R]\).

For every integer \(R\ge0\), the formal logarithm agrees coefficientwise with the exact logarithm in Lemma 2.1, and both normalized series have constant term \(1\). Thus the series themselves agree. ∎

### Corollary 2.3 — Polynomial dependence under arbitrary integer powers

Let \(E\) be an indeterminate. Then

\[
\boxed{
\mathscr U_{d,s}(R;x)^E
:=
\exp\bigl(E\log\mathscr U_{d,s}(R;x)\bigr)
\in
K[R,E][[x]].
}
\]

For every integer specialization \(E=e\), including negative \(e\), this specializes to the ordinary formal power \(U_{d,s}(R;x)^e\).

#### Proof

The logarithm has zero constant term and coefficients in \(K[R]\). Multiplication by \(E\) places it in \(K[R,E][[x]]\). Exponentiation shows coefficientwise polynomial dependence on \(R,E\).

For an integer specialization \(E=e\), the formal exponential identity

\[
\exp(e\log U)=U^e
\]

holds for every unit series \(U\) with constant term \(1\), including negative \(e\). ∎

## 2.3 Universal term units

Fix a residue pattern

\[
\mathbf s=(s_1,\ldots,s_S),
\qquad
0\le s_j<d.
\]

Introduce endpoint-quotient variables

\[
R_1,\ldots,R_S,
\]

and for each term slot \(i\) introduce variables

\[
\mathsf a_i,
\qquad
\mathsf e_{i1},\ldots,\mathsf e_{iS}.
\]

Define

\[
\boxed{
\mathscr U_i(x)
=
e^{\mathsf a_i x}
\prod_{j=1}^{S}
\mathscr U_{d,s_j}(R_j;x)^{\mathsf e_{ij}}.
}
\]

Its constant term is \(1\).

Define also the universal depth

\[
\boxed{
\mathsf h_i
=
\sum_{j=1}^{S}\mathsf e_{ij}R_j.
}
\]

### Corollary 2.4 — Universal coefficient ring

For \(k\) term slots, every coefficient of every \(\mathscr U_i(x)\) belongs to the polynomial ring

\[
\boxed{
\mathscr R_{\mathbf s,k}
=
K[
R_1,\ldots,R_S,
\mathsf a_1,\ldots,\mathsf a_k,
\mathsf e_{ij}:1\le i\le k,1\le j\le S
].
}
\]

Every universal depth \(\mathsf h_i\) also belongs to this ring.

#### Proof

The exponential \(e^{\mathsf a_i x}\) has coefficient \(\mathsf a_i^n/n!\). Corollary 2.3 gives coefficientwise polynomial dependence for every endpoint factor. Finite multiplication preserves the coefficient ring. The depth formula is visibly polynomial. ∎

---

# 3. Residual Wronskians

The multiplicity of a linear combination is controlled by the Wronskians of the term germs.

## 3.1 Derivative factorization

For an integer \(h\), a unit series \(U(x)\), and \(a\ge0\), define the falling factorial

\[
(h)_r
=
h(h-1)\cdots(h-r+1),
\qquad
(h)_0=1.
\]

### Lemma 3.1 — Derivative of a depth-normalized germ

For every \(a\ge0\),

\[
\boxed{
\frac{d^a}{dx^a}
\bigl(x^hU(x)\bigr)
=
x^{h-a}
\sum_{b=0}^{a}
\binom ab
(h)_{a-b}x^bU^{(b)}(x).
}
\]

The identity is valid in the Laurent-series field for every integer \(h\).

#### Proof

Apply the Leibniz rule:

\[
\frac{d^a}{dx^a}(x^hU)
=
\sum_{b=0}^{a}
\binom ab
\frac{d^{a-b}}{dx^{a-b}}x^h
\,U^{(b)}.
\]

For every integer \(h\),

\[
\frac{d^{a-b}}{dx^{a-b}}x^h
=(h)_{a-b}x^{h-a+b}.
\]

Factor out \(x^{h-a}\). ∎

## 3.2 Wronskian factorization

For germs \(f_1,\ldots,f_k\), define

\[
W(f_1,\ldots,f_k)
=
\det\left(
\frac{d^{a-1}}{dx^{a-1}}f_i
\right)_{1\le a,i\le k}.
\]

Let

\[
f_i(x)=b_i x^{h_i}U_i(x),
\qquad
b_i\ne0,
\qquad
U_i(0)=1.
\]

### Project Theorem 3.2 — Residual Wronskian factorization

One has

\[
\boxed{
W(f_1,\ldots,f_k)
=
\left(\prod_{i=1}^{k}b_i\right)
 x^{\sum_i h_i-\binom{k}{2}}
 Q(f_1,\ldots,f_k;x),
}
\]

where

\[
\boxed{
Q(f_1,\ldots,f_k;x)
=
\det\left(
\sum_{b=0}^{a-1}
\binom{a-1}{b}
(h_i)_{a-1-b}x^bU_i^{(b)}(x)
\right)_{1\le a,i\le k}
}
\]

is a formal power series.

#### Proof

By Lemma 3.1, the entry in row \(a\), column \(i\) is

\[
b_i x^{h_i-a+1}
\sum_{b=0}^{a-1}
\binom{a-1}{b}
(h_i)_{a-1-b}x^bU_i^{(b)}(x).
\]

Factor \(b_i x^{h_i}\) from column \(i\), and factor \(x^{-a+1}\) from row \(a\). The total extracted power is

\[
\sum_{i=1}^{k}h_i
-
\sum_{a=1}^{k}(a-1)
=
\sum_i h_i-\binom{k}{2}.
\]

The remaining determinant is exactly the displayed residual series. ∎

### Corollary 3.3 — Universal residual Wronskian coefficients

For the universal units \(\mathscr U_i\) and universal depths \(\mathsf h_i\) of Section 2, define

\[
\mathscr Q_{\mathbf s,k}(x)
=
\det\left(
\sum_{b=0}^{a-1}
\binom{a-1}{b}
(\mathsf h_i)_{a-1-b}
 x^b\mathscr U_i^{(b)}(x)
\right)_{1\le a,i\le k}.
\]

Then

\[
\boxed{
\mathscr Q_{\mathbf s,k}(x)
=
\sum_{n\ge0}q_{\mathbf s,k,n}x^n
\in
\mathscr R_{\mathbf s,k}[[x]].
}
\]

#### Proof

Every falling factorial \((\mathsf h_i)_r\) is a polynomial in \(\mathsf h_i\), hence belongs to \(\mathscr R_{\mathbf s,k}\). Every coefficient of every derivative \(\mathscr U_i^{(b)}\) belongs to the same ring. Determinants preserve coefficientwise membership. ∎

---

# 4. The Noetherian residual bound

The universal residual Wronskian contains infinitely many coefficients, but they generate an ideal in a Noetherian ring.

## 4.1 Coefficient ideals

For fixed \(\mathbf s\) and \(k\), define

\[
\mathfrak J_{\mathbf s,k}
=
(q_{\mathbf s,k,0},q_{\mathbf s,k,1},q_{\mathbf s,k,2},\ldots)
\subseteq
\mathscr R_{\mathbf s,k}.
\]

The polynomial ring \(\mathscr R_{\mathbf s,k}\) is Noetherian by Hilbert's basis theorem.

### Classical Lemma 4.1 — Initial finite generation

There exists an integer

\[
N_{\mathbf s,k}\ge0
\]

such that

\[
\boxed{
\mathfrak J_{\mathbf s,k}
=
(q_{\mathbf s,k,0},\ldots,q_{\mathbf s,k,N_{\mathbf s,k}}).
}
\]

#### Proof

Because the ring is Noetherian, the ideal \(\mathfrak J_{\mathbf s,k}\) is generated by finitely many of its elements. Every chosen generator is one coefficient

\[
q_{\mathbf s,k,n}.
\]

Let \(N\) be the maximum index among a finite generating set. Then all chosen generators belong to

\[
(q_0,\ldots,q_N),
\]

so

\[
\mathfrak J_{\mathbf s,k}
\subseteq
(q_0,\ldots,q_N).
\]

The reverse inclusion is immediate because every \(q_n\) belongs to \(\mathfrak J_{\mathbf s,k}\). ∎

## 4.2 Specialization consequence

A specialization of the universal parameters to actual integers gives a ring homomorphism

\[
\sigma:\mathscr R_{\mathbf s,k}\to K.
\]

### Lemma 4.2 — Finite vanishing forces universal residual vanishing after specialization

If

\[
\sigma(q_{\mathbf s,k,n})=0
\qquad
(0\le n\le N_{\mathbf s,k}),
\]

then

\[
\boxed{
\sigma(\mathscr Q_{\mathbf s,k}(x))=0
\quad\text{in }K[[x]].
}
\]

#### Proof

For every \(n>N_{\mathbf s,k}\), Lemma 4.1 gives polynomials \(a_{n,j}\in\mathscr R_{\mathbf s,k}\) such that

\[
q_{\mathbf s,k,n}
=
\sum_{j=0}^{N_{\mathbf s,k}}
a_{n,j}q_{\mathbf s,k,j}.
\]

Apply \(\sigma\). Every term on the right vanishes, so

\[
\sigma(q_{\mathbf s,k,n})=0.
\]

Thus every coefficient of the specialized residual series is zero. ∎

### Project Theorem 4.3 — Uniform residual Wronskian bound

Fix \(d,m,S\). There exists a finite integer

\[
\boxed{C_d^{\mathrm{Wr}}(m,S)}
\]

such that the following holds.

For every factorial circuit of endpoint complexity at most \(S\), every \(k\le m\), and every linearly independent \(k\)-tuple of term germs

\[
f_i(x)=T_i(\zeta e^x),
\]

the residual Wronskian in Theorem 3.2 satisfies

\[
\boxed{
0\le
\operatorname{ord}_xQ(f_1,\ldots,f_k;x)
\le
C_d^{\mathrm{Wr}}(m,S).
}
\]

#### Proof

There are only finitely many residue patterns

\[
\mathbf s\in\{0,1,\ldots,d-1\}^S
\]

and finitely many integers \(1\le k\le m\).

For every pair \((\mathbf s,k)\), choose \(N_{\mathbf s,k}\) from Lemma 4.1, and define

\[
C_d^{\mathrm{Wr}}(m,S)
=
\max_{\mathbf s,\,1\le k\le m}
N_{\mathbf s,k}.
\]

Now specialize the universal parameters to the actual endpoint quotients, monomial exponents, and factorial exponents of the chosen \(k\)-tuple. By Corollary 3.3, the specialized universal residual is exactly the residual Wronskian \(Q\) of that tuple.

If

\[
\operatorname{ord}_xQ>N_{\mathbf s,k},
\]

then the first \(N_{\mathbf s,k}+1\) coefficients vanish. Lemma 4.2 would force the entire residual series to vanish.

By Theorem 3.2, this would force the full Wronskian to vanish. Over characteristic zero, a finite family of formal Laurent series has zero Wronskian if and only if it is linearly dependent over the constant field. This contradicts the assumed independence.

Therefore

\[
\operatorname{ord}_xQ\le N_{\mathbf s,k}
\le C_d^{\mathrm{Wr}}(m,S).
\]

The lower bound is automatic for a nonzero formal power series. ∎

### Caution 4.4 — Finiteness is not yet an explicit polynomial estimate

The proof uses finite generation of an infinite coefficient ideal. It proves existence of a finite bound, but it does not provide a usable estimate such as

\[
C_d^{\mathrm{Wr}}(m,S)
\le
\operatorname{poly}(d,m,S).
\]

Obtaining such an estimate is the principal remaining multiplicity problem.

---

# 5. Vanishing sequences and Wronskian minima

The residual Wronskian theorem controls independent subsets of the input terms. We now convert it into a bound for every linear combination.

## 5.1 Adapted bases

Let \(V\subseteq K((x))\) be a finite-dimensional vector space.

### Definition 5.1 — Vanishing sequence

An **adapted basis** of \(V\) is a basis

\[
g_1,\ldots,g_r
\]

whose orders satisfy

\[
\nu_1<\nu_2<\cdots<\nu_r,
\qquad
\nu_i=\operatorname{ord}_x g_i.
\]

The increasing sequence

\[
\boxed{
\nu(V)=(\nu_1,\ldots,\nu_r)
}
\]

is the **vanishing sequence** of \(V\).

### Classical Lemma 5.2 — Existence and uniqueness of the vanishing sequence

Every finite-dimensional subspace \(V\subseteq K((x))\) has an adapted basis. The resulting sequence of orders is independent of the adapted basis.

Moreover, every nonzero element of \(V\) has order equal to one of the \(\nu_i\).

#### Proof

Choose a nonzero element of minimum order in \(V\), call it \(g_1\), and normalize its leading coefficient to \(1\).

For every other vector, subtract a scalar multiple of \(g_1\) to eliminate its coefficient at order \(\nu_1\). The resulting codimension-one subspace has all nonzero orders strictly larger than \(\nu_1\).

Repeat inductively. This constructs a basis with strictly increasing orders.

The filtration

\[
V_{\ge n}
=
\{f\in V:\operatorname{ord}_xf\ge n\}
\]

is intrinsic. The jumps of the dimension function

\[
n\longmapsto\dim_KV_{\ge n}
\]

occur exactly at the orders \(\nu_i\). Hence the sequence is independent of the chosen adapted basis.

Finally, write a nonzero vector as

\[
f=\sum_{i=1}^{r}a_ig_i.
\]

Let \(j\) be the least index with \(a_j\ne0\). No basis vector with index greater than \(j\) has a term of order \(\nu_j\), so the leading term of \(f\) is the leading term of \(a_jg_j\). Therefore

\[
\operatorname{ord}_xf=\nu_j.
\]

∎

## 5.2 Wronskian order of an adapted basis

### Classical Lemma 5.3 — Wronskian order formula

Let \(g_1,\ldots,g_k\) be linearly independent Laurent series with strictly increasing orders

\[
\lambda_1<\cdots<\lambda_k.
\]

Then

\[
\boxed{
\operatorname{ord}_xW(g_1,\ldots,g_k)
=
\sum_{j=1}^{k}\lambda_j-\binom{k}{2}.
}
\]

#### Proof

Write

\[
g_j(x)=a_jx^{\lambda_j}+O(x^{\lambda_j+1}),
\qquad
 a_j\ne0.
\]

The \((r,j)\)-entry of the Wronskian matrix has leading term

\[
a_j(\lambda_j)_{r-1}x^{\lambda_j-r+1}.
\]

Factor \(a_jx^{\lambda_j}\) from column \(j\), and \(x^{-r+1}\) from row \(r\). The extracted order is

\[
\sum_j\lambda_j-\binom{k}{2}.
\]

The remaining leading determinant is

\[
\det\bigl((\lambda_j)_{r-1}\bigr)_{1\le r,j\le k}.
\]

The falling-factorial polynomials

\[
1,
\ X,
\ X(X-1),
\ldots
\]

are monic of successive degrees. Their evaluation determinant is therefore the ordinary Vandermonde determinant

\[
\prod_{1\le i<j\le k}(\lambda_j-\lambda_i),
\]

which is nonzero because the \(\lambda_j\) are distinct and the field has characteristic zero. ∎

### Corollary 5.4 — Wronskian order of an arbitrary independent tuple

Let \(f_1,\ldots,f_k\) be independent, and let

\[
\lambda_1<\cdots<\lambda_k
\]

be the vanishing sequence of their span. Then

\[
\boxed{
\operatorname{ord}_xW(f_1,\ldots,f_k)
=
\sum_{j=1}^{k}\lambda_j-\binom{k}{2}.
}
\]

#### Proof

An invertible constant change of basis transforms \((f_i)\) into an adapted basis of the same span. The Wronskian is multiplied by the determinant of that constant change-of-basis matrix, which is a nonzero scalar and does not alter its order. Apply Lemma 5.3. ∎

## 5.3 Minimum over generator subsets

Let

\[
f_1,\ldots,f_r
\]

span a space \(V\) of dimension \(r_0\), with vanishing sequence

\[
\nu_1<\cdots<\nu_{r_0}.
\]

### Project Theorem 5.5 — Generator-subset Wronskian minimum

For every \(1\le k\le r_0\),

\[
\boxed{
\min_{\substack{I\subseteq\{1,\ldots,r\}\\|I|=k,\ I\text{ independent}}}
\operatorname{ord}_xW(f_i:i\in I)
=
\sum_{j=1}^{k}\nu_j-\binom{k}{2}.
}
\]

#### Proof

First consider any independent \(k\)-subset \(I\). Let

\[
\lambda_1^{(I)}<\cdots<\lambda_k^{(I)}
\]

be the vanishing sequence of its span.

Express an adapted basis of that subspace in an adapted basis of \(V\). Row reduction shows that its pivot indices satisfy

\[
p_1<\cdots<p_k,
\qquad
p_j\ge j,
\]

and its vanishing orders are

\[
\lambda_j^{(I)}=\nu_{p_j}.
\]

Hence

\[
\lambda_j^{(I)}\ge\nu_j.
\]

By Corollary 5.4,

\[
\operatorname{ord}W(f_i:i\in I)
=
\sum_j\lambda_j^{(I)}-\binom{k}{2}
\ge
\sum_{j=1}^{k}\nu_j-\binom{k}{2}.
\]

Thus the minimum is at least the claimed value.

For the reverse inequality, choose adapted vectors

\[
g_1,\ldots,g_k\in V
\]

of orders \(\nu_1,\ldots,\nu_k\). Each \(g_j\) is a constant linear combination of the generators \(f_i\). By multilinearity of the Wronskian,

\[
W(g_1,\ldots,g_k)
=
\sum_I a_IW(f_i:i\in I),
\]

where the sum ranges over \(k\)-subsets and the coefficients \(a_I\) are constants.

The left side has order

\[
\sum_{j=1}^{k}\nu_j-\binom{k}{2}
\]

by Lemma 5.3. The order of a sum is at least the minimum order of its nonzero summands. Therefore at least one independent subset \(I\) satisfies

\[
\operatorname{ord}W(f_i:i\in I)
\le
\sum_{j=1}^{k}\nu_j-\binom{k}{2}.
\]

Combine the two inequalities. ∎

---

# 6. The weighted matroid depth profile

The input terms define a vector matroid: a subset is independent precisely when the corresponding germs are linearly independent over \(K\).

Assign to term \(i\) the integer weight

\[
h_i.
\]

For \(0\le k\le r_0\), define

\[
\boxed{
M_k
=
\min_{\substack{I\subseteq\{1,\ldots,r\}\\|I|=k,\ I\text{ independent}}}
\sum_{i\in I}h_i,
}
\]

with

\[
M_0=0.
\]

## 6.1 Greedy increments

### Classical Lemma 6.1 — Weighted matroid greedy theorem

Order the elements by nondecreasing weight, breaking ties arbitrarily, and greedily accept an element whenever it increases the rank.

Let the accepted weights be

\[
\gamma_1,\ldots,\gamma_{r_0}.
\]

Then for every \(k\), the first \(k\) accepted elements form a minimum-weight independent \(k\)-set. Consequently,

\[
\boxed{
M_k=\gamma_1+\cdots+\gamma_k
}
\]

and

\[
\boxed{
M_k-M_{k-1}=\gamma_k,
}
\]

where every \(\gamma_k\) is one of the input depths \(h_i\).

#### Proof

Let \(G_k\) be the first \(k\) elements selected by the greedy algorithm, and let \(I\) be any independent \(k\)-set.

List the greedy choices in selection order. By the matroid exchange property, after the first \(j-1\) greedy choices have been matched with \(j-1\) elements of \(I\), there exists an element of \(I\) that can be added to the current greedy independent set. Greedy selects an available element of no larger weight than that element of \(I\).

Inductively, the \(j\)-th greedy weight is no greater than the weight of a suitable distinct element of \(I\). Summing gives

\[
\operatorname{wt}(G_k)
\le
\operatorname{wt}(I).
\]

Thus \(G_k\) is minimum weight, and its weight is \(M_k\). The increment formula follows. ∎

---

# 7. The General Factorial-Circuit Multiplicity Theorem

We now combine the Noetherian Wronskian bound, the vanishing-sequence minimum, and the weighted matroid profile.

Let

\[
C=C_d^{\mathrm{Wr}}(m,S).
\]

### Project Theorem 7.1 — General Factorial-Circuit Multiplicity Theorem

Fix \(d,m,S\). Let

\[
F(q)=\sum_{i=1}^{r}c_iT_i(q),
\qquad
r\le m,
\]

be a factorial circuit of endpoint complexity at most \(S\), and let

\[
h_i=v_{\Phi_d}(T_i).
\]

There exists a finite constant

\[
\boxed{C_d(m,S)<\infty}
\]

depending only on \(d,m,S\), such that every nonzero element of the span of the term germs has local order in

\[
\boxed{
\bigcup_{i=1}^{r}
[h_i-C_d(m,S),\ h_i+C_d(m,S)].
}
\]

In particular, if the circuit sum is nonzero, then

\[
\boxed{
\operatorname{ord}_{\zeta}F
\in
\bigcup_{i=1}^{r}
[h_i-C_d(m,S),\ h_i+C_d(m,S)].
}
\]

One may take

\[
C_d(m,S)=C_d^{\mathrm{Wr}}(m,S).
\]

#### Proof

Let \(V\) be the span of the term germs

\[
f_i(x)=T_i(\zeta e^x),
\]

and let its dimension be \(r_0\). Write its vanishing sequence as

\[
\nu_1<\cdots<\nu_{r_0}.
\]

For every independent subset \(I\) of size \(k\), Theorem 3.2 gives

\[
\operatorname{ord}W(f_i:i\in I)
=
\sum_{i\in I}h_i
-
\binom{k}{2}
+
\delta_I,
\]

where

\[
\delta_I
=
\operatorname{ord}Q(f_i:i\in I;x).
\]

By Theorem 4.3,

\[
0\le\delta_I\le C.
\]

Take the minimum over independent \(k\)-subsets. By Theorem 5.5,

\[
\sum_{j=1}^{k}\nu_j-\binom{k}{2}
=
\min_I
\left(
\sum_{i\in I}h_i-\binom{k}{2}+\delta_I
\right).
\]

Cancel \(\binom{k}{2}\):

\[
\sum_{j=1}^{k}\nu_j
=
\min_I
\left(
\sum_{i\in I}h_i+\delta_I
\right).
\]

By definition of \(M_k\),

\[
M_k
\le
\sum_{j=1}^{k}\nu_j
\le
M_k+C.
\]

Write

\[
\sum_{j=1}^{k}\nu_j
=M_k+\varepsilon_k,
\qquad
0\le\varepsilon_k\le C,
\]

and put \(\varepsilon_0=0\).

Then

\[
\begin{aligned}
\nu_k
&=
\left(\sum_{j=1}^{k}\nu_j\right)
-
\left(\sum_{j=1}^{k-1}\nu_j\right)\\
&=
(M_k-M_{k-1})
+
(\varepsilon_k-\varepsilon_{k-1}).
\end{aligned}
\]

By Lemma 6.1,

\[
M_k-M_{k-1}=\gamma_k
\]

for some input depth \(\gamma_k=h_i\). Also

\[
-C\le\varepsilon_k-\varepsilon_{k-1}\le C.
\]

Therefore

\[
|\nu_k-\gamma_k|\le C.
\]

Every nonzero element of \(V\) has order equal to one of the \(\nu_k\) by Lemma 5.2. Hence its order lies within \(C\) of an input depth. Apply this to the circuit sum whenever it is nonzero. ∎

## 7.1 Common-depth form

### Corollary 7.2 — Common-depth multiplicity bound

Assume

\[
h_1=\cdots=h_r=h.
\]

Then every nonzero circuit sum satisfies

\[
\boxed{
h\le\operatorname{ord}_{\zeta}F\le h+C_d(m,S).}
\]

Equivalently,

\[
\boxed{
F\ne0
\Longrightarrow
v_{\Phi_d}(F)
\le
h+C_d(m,S)
}
\]

whenever the circuit is a Laurent polynomial.

#### Proof

Every term is divisible locally by \(x^h\), so every sum has order at least \(h\). Theorem 7.1 places every finite order within \(C_d(m,S)\) of the only input depth \(h\). ∎

## 7.2 Immediate global bounds

### Corollary 7.3 — Coarse maximum-depth bound

Every nonzero circuit sum satisfies

\[
\boxed{
\operatorname{ord}_{\zeta}F
\le
\max_i h_i+C_d(m,S).
}
\]

It also satisfies

\[
\boxed{
\operatorname{ord}_{\zeta}F
\ge
\min_i h_i-C_d(m,S).
}
\]

#### Proof

Both statements follow immediately from the union of intervals in Theorem 7.1. ∎

### Corollary 7.4 — One-term normalization

One may take

\[
\boxed{C_d(1,S)=0.}
\]

#### Proof

A nonzero one-term circuit has order exactly its term depth. ∎

---

# 8. Depth clustering and exact finite-jet reduction

The theorem can be converted into a finite local identity criterion that does not require iterating through the possibly enormous absolute depths.

Fix any valid constant

\[
C\ge C_d(m,S).
\]

Sort the terms so that

\[
h_1\le h_2\le\cdots\le h_r.
\]

## 8.1 Depth clusters

### Definition 8.1 — \(C\)-depth clusters

Partition the sorted terms into maximal consecutive blocks

\[
\mathcal B_1,\ldots,\mathcal B_t
\]

such that within each block every consecutive depth gap is at most \(C\):

\[
h_{i+1}-h_i\le C.
\]

At a boundary between two consecutive blocks,

\[
\boxed{
\min_{i\in\mathcal B_{u+1}}h_i
>
\max_{i\in\mathcal B_u}h_i+C.
}
\]

For a block \(\mathcal B\), define

\[
h_-(\mathcal B)=\min_{i\in\mathcal B}h_i,
\qquad
h_+(\mathcal B)=\max_{i\in\mathcal B}h_i,
\]

and

\[
F_{\mathcal B}(q)
=
\sum_{i\in\mathcal B}c_iT_i(q).
\]

### Lemma 8.2 — Cluster width bound

If \(|\mathcal B|=b\), then

\[
\boxed{
h_+(\mathcal B)-h_-(\mathcal B)\le(b-1)C.}
\]

#### Proof

The difference between the maximum and minimum is the sum of the \(b-1\) consecutive gaps inside the block. Every gap is at most \(C\). ∎

## 8.2 Cluster separation

### Project Theorem 8.3 — Depth-cluster independence

The full circuit is zero if and only if every cluster sum is zero:

\[
\boxed{
F=0
\iff
F_{\mathcal B_u}=0
\text{ for every }u.
}
\]

#### Proof

The reverse implication is immediate.

For the forward direction, suppose that some cluster sum is nonzero, and choose the first such cluster \(\mathcal B_u\) in increasing depth order.

All earlier cluster sums are zero. By Corollary 7.3 applied to the subcircuit \(F_{\mathcal B_u}\),

\[
\operatorname{ord}_{\zeta}F_{\mathcal B_u}
\le
h_+(\mathcal B_u)+C.
\]

Every term in a later cluster has depth at least

\[
\min_{i\in\mathcal B_{u+1}}h_i
>
h_+(\mathcal B_u)+C.
\]

Therefore every later cluster sum has order strictly greater than the order of \(F_{\mathcal B_u}\). Its leading term cannot be canceled by later clusters.

Hence the full circuit sum is nonzero, a contradiction. Thus every cluster sum must vanish. ∎

## 8.3 Regularized cluster jets

For a block \(\mathcal B\), define its regularized local germ

\[
\boxed{
G_{\mathcal B}(x)
=
x^{-h_-(\mathcal B)}
F_{\mathcal B}(\zeta e^x).
}
\]

Every term of this germ has nonnegative order.

Define

\[
R_{\mathcal B}
=
h_+(\mathcal B)-h_-(\mathcal B)+C.
\]

### Algorithmic Theorem 8.4 — Exact finite-jet criterion for one cluster

For every cluster \(\mathcal B\),

\[
\boxed{
F_{\mathcal B}=0
\iff
[x^n]G_{\mathcal B}(x)=0
\quad(0\le n\le R_{\mathcal B}).
}
\]

Equivalently,

\[
\boxed{
F_{\mathcal B}=0
\iff
\left.
\frac{d^n}{dx^n}G_{\mathcal B}(x)
\right|_{x=0}=0
\quad(0\le n\le R_{\mathcal B}).
}
\]

#### Proof

If the cluster sum is zero, every coefficient vanishes.

Conversely, suppose all displayed coefficients vanish and the cluster sum is nonzero. Then

\[
\operatorname{ord}_{\zeta}F_{\mathcal B}
>
h_-(\mathcal B)+R_{\mathcal B}
=
h_+(\mathcal B)+C.
\]

This contradicts Corollary 7.3 applied to the cluster subcircuit. ∎

### Corollary 8.5 — Degree-free finite-jet reduction

For a cluster of size \(b\), it is enough to test at most

\[
\boxed{bC+1}
\]

regularized coefficients.

For the full circuit, at most

\[
\boxed{rC+t\le mC+m}
\]

regularized coefficient equalities are required across all clusters.

#### Proof

By Lemma 8.2,

\[
R_{\mathcal B}
\le
(b-1)C+C=bC.
\]

Thus the tested orders are \(0,\ldots,bC\), a total of \(bC+1\). Summing over all clusters gives

\[
\sum_{u=1}^{t}(|\mathcal B_u|C+1)
=rC+t.
\]

∎

## 8.4 Exact certificate format

A complete local identity certificate relative to a supplied valid bound \(C\) consists of:

```text
FactorialCircuitJetCertificate(
    context_order=d,
    primitive_context=zeta,
    endpoint_list=(A_1,...,A_S),
    term_depths=(h_1,...,h_r),
    certified_bound=C,
    depth_clusters=(B_1,...,B_t),
    regularized_cluster_jets={
        B_u: ([x^0]G_Bu,...,[x^R_u]G_Bu)
    }
)
```

A verifier checks:

1. every depth by the floor-valuation formula;
2. the cluster partition inequalities;
3. every regularized jet by the cumulant and Bell-polynomial machinery of Parts IV and VI;
4. vanishing of the finite jet lists;
5. applicability of the certified multiplicity bound.

If all checks pass, Theorems 8.3 and 8.4 prove the circuit identity.

---

# 9. Positive-endpoint finite fingerprint separation

The Noetherian theorem is non-effective in general. At the real context \(q=1\), one can nevertheless prove an explicit finite separation theorem for **individual normalized terms**.

This does not yet bound arbitrary sums, but it gives a concrete first step toward an effective multiplicity estimate.

## 9.1 Endpoint cumulants at \(q=1\)

Put

\[
q=e^x.
\]

For \(A\ge1\), define the normalized endpoint unit

\[
\boxed{
U_A(x)
=
\frac{(e^x;e^x)_A}{(-x)^AA!}
=
\prod_{n=1}^{A}
\frac{1-e^{nx}}{-nx}.
}
\]

It satisfies \(U_A(0)=1\).

Define the power sums

\[
p_r(A)=\sum_{n=1}^{A}n^r.
\]

### Lemma 9.1 — Exact positive-endpoint logarithm

One has

\[
\boxed{
\log U_A(x)
=
\frac{p_1(A)}2x
+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}
 p_{2r}(A)x^{2r}.
}
\]

In particular, after the linear term, every odd logarithmic coefficient vanishes.

#### Proof

Part IV gives for every \(n\ge1\)

\[
\log\left(\frac{1-e^{nx}}{-nx}\right)
=
\frac{nx}{2}
+
\sum_{r\ge1}
\frac{B_{2r}}{2r(2r)!}(nx)^{2r}.
\]

Sum this identity over \(n=1,\ldots,A\). ∎

## 9.2 A Faulhaber–Vandermonde factorization

### Classical Lemma 9.2 — Even power-sum factorization

For every \(r\ge1\), there exists a polynomial

\[
Q_{r-1}(z)\in\mathbb Q[z]
\]

of degree exactly \(r-1\) such that

\[
\boxed{
p_{2r}(A)=p_2(A)Q_{r-1}(A(A+1)).}
\]

The leading coefficient of \(Q_{r-1}\) is nonzero.

#### Proof

Let \(P_{2r}(X)\in\mathbb Q[X]\) be the Faulhaber polynomial satisfying

\[
P_{2r}(A)=p_{2r}(A)
\]

for nonnegative integers \(A\).

Using Bernoulli polynomials,

\[
P_{2r}(X)
=
\frac{B_{2r+1}(X+1)-B_{2r+1}}{2r+1}.
\]

Since \(2r+1>1\) is odd,

\[
B_{2r+1}=0.
\]

The reflection identity

\[
B_n(1-X)=(-1)^nB_n(X)
\]

implies

\[
P_{2r}(-X-1)=-P_{2r}(X).
\]

Therefore \(P_{2r}\) vanishes at

\[
X=0,
\qquad
X=-1,
\qquad
X=-\frac12.
\]

Hence it is divisible by

\[
X(X+1)(2X+1).
\]

But

\[
p_2(X)=\frac{X(X+1)(2X+1)}6.
\]

Thus

\[
R_r(X):=\frac{P_{2r}(X)}{p_2(X)}
\]

is a polynomial.

Both numerator and denominator change sign under

\[
X\mapsto-X-1,
\]

so the quotient is invariant:

\[
R_r(-X-1)=R_r(X).
\]

Put

\[
y=X+\frac12.
\]

The involution becomes \(y\mapsto-y\). Therefore \(R_r\) is an even polynomial in \(y\), hence a polynomial in

\[
y^2=X(X+1)+\frac14.
\]

Equivalently,

\[
R_r(X)=Q_{r-1}(X(X+1))
\]

for some \(Q_{r-1}\in\mathbb Q[z]\).

The degree of \(P_{2r}\) is \(2r+1\), while the degree of \(p_2\) is \(3\). Thus \(R_r\) has degree \(2r-2\) in \(X\), so \(Q_{r-1}\) has degree \(r-1\) in \(z=X(X+1)\). Its leading coefficient is nonzero because the leading coefficient of the Faulhaber polynomial is nonzero. ∎

### Project Theorem 9.3 — Even power-sum evaluation matrix

Let

\[
1\le A_1<\cdots<A_S.
\]

Then the \(S\times S\) matrix

\[
\boxed{
\mathcal P
=
\bigl(p_{2r}(A_j)\bigr)_{1\le r,j\le S}
}
\]

is invertible over \(\mathbb Q\).

#### Proof

Put

\[
z_j=A_j(A_j+1).
\]

The \(z_j\) are pairwise distinct because the function \(A\mapsto A(A+1)\) is strictly increasing for \(A\ge0\).

By Lemma 9.2,

\[
p_{2r}(A_j)
=
p_2(A_j)Q_{r-1}(z_j).
\]

Factor \(p_2(A_j)\ne0\) from column \(j\). It remains to show that

\[
\det(Q_{r-1}(z_j))_{1\le r,j\le S}
\ne0.
\]

The polynomials

\[
Q_0,Q_1,\ldots,Q_{S-1}
\]

have exact degrees

\[
0,1,\ldots,S-1
\]

and nonzero leading coefficients. The change-of-basis matrix from

\[
1,z,\ldots,z^{S-1}
\]

to this polynomial basis is triangular with nonzero diagonal. Therefore their evaluation determinant is a nonzero scalar multiple of the Vandermonde determinant

\[
\prod_{1\le i<j\le S}(z_j-z_i),
\]

which is nonzero. ∎

## 9.3 Individual-term separation

Let

\[
T(q)=q^\alpha\prod_{j=1}^{S}(q;q)_{A_j}^{e_j}.
\]

Its depth at \(q=1\) is

\[
h(T)=\sum_{j=1}^{S}e_jA_j.
\]

Let \(B(T)\) be its nonzero leading scalar in the coordinate \(q=e^x\), and define the normalized unit

\[
\boxed{
\mathcal N_T(x)
=
\frac{x^{-h(T)}T(e^x)}{B(T)}.
}
\]

Then \(\mathcal N_T(0)=1\).

### Project Theorem 9.4 — Positive-Endpoint Pairwise Fingerprint Theorem

Fix distinct endpoints

\[
1\le A_1<\cdots<A_S.
\]

Let

\[
T(q)=q^\alpha\prod_j(q;q)_{A_j}^{e_j},
\qquad
\widetilde T(q)=q^{\widetilde\alpha}
\prod_j(q;q)_{A_j}^{\widetilde e_j}.
\]

If

\[
\boxed{
\left.
\frac{d^n}{dx^n}
\log\mathcal N_T(x)
\right|_{x=0}
=
\left.
\frac{d^n}{dx^n}
\log\mathcal N_{\widetilde T}(x)
\right|_{x=0}
\quad(1\le n\le2S),
}
\]

then

\[
\boxed{
e_j=\widetilde e_j\text{ for all }j,
\qquad
\alpha=\widetilde\alpha.}
\]

Consequently,

\[
\boxed{
\mathcal N_T(x)=\mathcal N_{\widetilde T}(x).
}
\]

Equivalently, if the normalized logarithmic germs are distinct, then their difference has order at most \(2S\):

\[
\boxed{
\operatorname{ord}_x
\left(
\log\mathcal N_T-
\log\mathcal N_{\widetilde T}
\right)
\le2S.
}
\]

#### Proof

Put

\[
\Delta e_j=e_j-\widetilde e_j,
\qquad
\Delta\alpha=\alpha-\widetilde\alpha.
\]

By Lemma 9.1,

\[
\begin{aligned}
\log\mathcal N_T(x)
-
\log\mathcal N_{\widetilde T}(x)
&=
\Delta\alpha\,x
+
\sum_{j=1}^{S}\Delta e_j\log U_{A_j}(x).
\end{aligned}
\]

At each even derivative order \(2r\), where \(1\le r\le S\), the equality of fingerprints gives

\[
\sum_{j=1}^{S}\Delta e_jp_{2r}(A_j)=0,
\]

because \(B_{2r}\ne0\); indeed, Euler's formula gives \(B_{2r}=(-1)^{r-1}2(2r)!\zeta(2r)/(2\pi)^{2r}\).

The matrix of this linear system is the invertible matrix from Theorem 9.3. Therefore

\[
\Delta e_j=0
\qquad
(1\le j\le S).
\]

Now compare the first derivative. All endpoint contributions cancel, leaving

\[
\Delta\alpha=0.
\]

Thus all exponents agree, and the normalized germs are equal.

The order statement is the contrapositive: if the two normalized logarithmic germs are distinct, at least one derivative among orders \(1,\ldots,2S\) differs. ∎

### Interpretation 9.5

At \(q=1\), one normalized factorial term supported on \(S\) fixed endpoints has an explicit finite fingerprint:

\[
\boxed{
\text{linear cumulant}
+
S\text{ even cumulants}
}
\]

already determines all \(S+1\) exponent parameters.

The theorem is a pairwise separation result. It does not by itself bound the multiplicity of an arbitrary linear combination of \(m\) such germs; that requires control of higher residual Wronskians, which is supplied non-effectively by Theorem 4.3.

---

# 10. Lower bounds and correction of a naïve conjecture

The uniform constant cannot be smaller than the ordinary sparse contact capacity.

### Sharpness Theorem 10.1 — Universal \(m-1\) lower bound

For every

\[
d\ge1,
\qquad
m\ge1,
\qquad
S\ge0,
\]

one has

\[
\boxed{C_d(m,S)\ge m-1.}
\]

This lower bound already occurs in a common-depth circuit.

#### Proof

Choose any nonzero compressed factorial term \(H(q)\) of endpoint complexity at most \(S\). For \(S=0\), take \(H(q)=1\).

Let

\[
h=v_{\Phi_d}(H).
\]

Consider

\[
\begin{aligned}
F(q)
&=
H(q)(q^d-1)^{m-1}\\
&=
\sum_{k=0}^{m-1}
(-1)^{m-1-k}
\binom{m-1}{k}
H(q)q^{dk}.
\end{aligned}
\]

This is a sum of exactly \(m\) compressed terms. Every summand has the same factorial exponents as \(H\), and multiplication by \(q^{dk}\) does not change its \(\Phi_d\)-depth. Thus every term has depth \(h\).

At a primitive \(d\)-th root,

\[
q^d-1
\]

has a simple zero. Therefore

\[
\operatorname{ord}_{\zeta}F
=
h+m-1.
\]

Any valid common-depth excess bound must therefore be at least \(m-1\). ∎

### Corollary 10.2 — Failure of the bound \(2(m-1)(S-1)\)

Under Definition 1.2 of endpoint complexity, the estimate

\[
C_1(m,S)
\le
2(m-1)(S-1)
\]

is false.

#### Proof

Take \(S=1\), choose any \(A\ge1\), and put

\[
H(q)=(q;q)_A.
\]

The construction in Theorem 10.1 gives an \(m\)-term common-depth circuit with excess multiplicity \(m-1\), while the proposed right side equals zero. ∎

### Caution 10.3 — Any corrected explicit estimate needs a monomial baseline

Because monomial shifts alone realize excess \(m-1\), every plausible explicit upper bound must satisfy

\[
\widehat C_d(m,S)\ge m-1.
\]

Endpoint-dependent terms may add further multiplicity, but they cannot replace this baseline.

---

# 11. Gaussian and multinomial circuit consequences

Gaussian binomials and multinomials are compressed factorial quotients, so the general theorem applies immediately to bounded-endpoint sums.

## 11.1 Gaussian multinomial sums

Let

\[
M_i(q)
=
{n_i\brack k_{i1},\ldots,k_{ic_i}}_q
=
\frac{(q;q)_{n_i}}
{\prod_{\nu=1}^{c_i}(q;q)_{k_{i\nu}}}.
\]

Let \(\mathcal A\) be the union of all positive factorial indices appearing among

\[
n_i,
\quad
k_{i\nu}.
\]

Put

\[
S=|\mathcal A|.
\]

### Corollary 11.1 — Uniform multiplicity for bounded-endpoint multinomial sums

Fix \(d,m,S\). Let

\[
F(q)
=
\sum_{i=1}^{r}
c_iq^{\alpha_i}M_i(q),
\qquad
r\le m,
\]

and suppose the total number of distinct positive factorial indices is at most \(S\).

For every term define

\[
\boxed{
h_i
=
\left\lfloor\frac{n_i}{d}\right\rfloor
-
\sum_{\nu=1}^{c_i}
\left\lfloor\frac{k_{i\nu}}{d}\right\rfloor.
}
\]

If \(F\ne0\), then

\[
\boxed{
\operatorname{ord}_{\zeta}F
\in
\bigcup_{i=1}^{r}
[h_i-C_d(m,S),h_i+C_d(m,S)].
}
\]

#### Proof

Write every multinomial as one numerator factorial and denominator factorials. After collecting the union of all distinct indices into one endpoint list, the sum is a factorial circuit of endpoint complexity at most \(S\).

The displayed depth is exactly the compressed factorial valuation from Part I. Apply Theorem 7.1. ∎

### Corollary 11.2 — Common-defect multinomial collision bound

Suppose all multinomial terms have the same defect \(h\) at context \(d\). Then every nonzero linear combination satisfies

\[
\boxed{
h\le\operatorname{ord}_{\zeta}F\le h+C_d(m,S).}
\]

#### Proof

Apply Corollary 7.2. ∎

## 11.2 Fixed-content word and CSP expressions

Many cyclic-sieving polynomials for fixed-content words are Gaussian multinomials. If a proposed identity or correction term is a sum of at most \(m\) such expressions using at most \(S\) distinct factorial endpoints, then its local differential CSP order cannot escape the finite neighborhoods of the individual multinomial defects unless the correction is identically zero.

### Corollary 11.3 — Bounded-endpoint differential rigidity

Let

\[
P(q)=\sum_{i=1}^{r}c_iq^{\alpha_i}M_i(q)
\]

be as in Corollary 11.1. If

\[
D^jP(\zeta)=0
\qquad
(0\le j\le\max_i h_i+C_d(m,S)),
\]

then

\[
\boxed{P=0.}
\]

#### Proof

If \(P\ne0\), Corollary 7.3 gives

\[
\operatorname{ord}_{\zeta}P
\le
\max_i h_i+C_d(m,S),
\]

contradicting the assumed vanishing of all derivatives through that order. ∎

The depth-cluster formulation of Section 8 is usually much cheaper because it avoids iterating from zero through a huge absolute depth.

---

# 12. Exact arithmetic reduction and the polynomial-time boundary

## 12.1 What the finite multiplicity theorem gives

For any supplied valid bound \(C\ge C_d(m,S)\), Theorems 8.3 and 8.4 reduce identity testing to finitely many exact regularized jets.

Each term in a cluster has the form

\[
T_i(\zeta e^x)
=
B_i x^{h_i}U_i(x),
\qquad
U_i(0)=1.
\]

After factoring the minimum cluster depth \(h_-\),

\[
x^{-h_-}T_i(\zeta e^x)
=
B_i x^{h_i-h_-}U_i(x).
\]

Part VI computes the coefficients of \(U_i\) through any prescribed order from:

1. arithmetic-progression power sums;
2. cyclotomic cumulants;
3. complete Bell polynomials.

Thus every coefficient required by Theorem 8.4 is an exact finite expression in the compressed parameters.

### Algorithmic Theorem 12.1 — Finite exact reduction from a valid multiplicity bound

Assume a valid integer \(C\ge C_d(m,S)\) is supplied.

Then factorial-circuit identity at context \(d\) reduces exactly to:

1. integer floor arithmetic for the depths;
2. sorting and clustering the depths;
3. computation of at most \(mC+m\) regularized local coefficients;
4. exact zero tests for those coefficients.

The reduction is correct and independent of the expanded degrees and coefficient counts of the terms.

#### Proof

Depth computation is exact by the cyclotomic valuation formula.

The cluster partition is exact integer comparison.

Corollary 8.5 bounds the number of required regularized coefficients by \(mC+m\).

Theorem 8.4 proves that vanishing of the coefficient list is equivalent to vanishing of each cluster sum, and Theorem 8.3 proves that all cluster sums vanish exactly when the full circuit vanishes.

All local coefficients are computed exactly from the compressed representation by the cumulant and Bell reconstruction theorems of Parts IV and VI. ∎

## 12.2 Conditional arithmetic-operation complexity

### Corollary 12.2 — Conditional polynomial arithmetic count

Suppose an explicit bound

\[
\widehat C_d(m,S)
\ge C_d(m,S)
\]

is available and satisfies

\[
\widehat C_d(m,S)
\le\operatorname{poly}(d,m,S).
\]

In a unit-cost exact-arithmetic model for \(K=\mathbb Q(\zeta_d)\), the number of arithmetic operations needed by the finite-jet reduction is polynomial in:

- the compressed circuit length;
- \(d,m,S\);
- the bit lengths of the integer parameters;
- the requested cyclotomic-field output dimension.

#### Proof

The number of required jet orders is polynomial by Corollary 8.5. Each fixed-order endpoint cumulant is a finite combination of arithmetic-progression power sums, computable by Faulhaber formulas using polynomially many arithmetic operations in the order and compressed input length. Bell reconstruction is polynomial in the requested order. Summing the term contributions and testing the resulting field elements adds polynomially many exact arithmetic operations. ∎

## 12.3 Why the uniform deterministic polynomial-time bit theorem remains open

Two separate effectivity problems remain.

### Open effectivity problem A — Polynomial multiplicity estimate

The Noetherian argument proves

\[
C_d(m,S)<\infty
\]

but does not prove

\[
C_d(m,S)
\le\operatorname{poly}(d,m,S).
\]

Without an explicit bound, the finite jet threshold is not a uniform executable parameter.

### Open effectivity problem B — Compact exact zero testing of jet sums

Even a low-order leading residual may contain factorials such as

\[
R!,
\]

whose ordinary binary expansion has length on the order of

\[
R\log R.
\]

When \(R\) itself is supplied in binary, materializing this integer may require time exponential in the compressed input length.

Individual products admit compact factored representations, but a circuit jet is a **sum** of such terms. A uniform bit-polynomial test requires a compact exact representation or a certified modular method for deciding whether such sums vanish.

### Caution 12.3 — Arithmetic-operation complexity is not bit complexity

A polynomial number of operations on exact cyclotomic-field elements does not by itself imply polynomial bit complexity when those elements may have exponentially long ordinary representations.

Therefore the deterministic polynomial-time theorem requires both:

\[
\boxed{
\text{an explicit polynomial multiplicity bound}
+
\text{a polynomial-time compact zero test for bounded jets}.
}
\]

Neither requirement is supplied by the present Noetherian proof.

---

# 13. Relation to the preceding theory

## 13.1 Relation to Part VI

Part VI provided exact local computation for one compressed term and local nonidentity certificates for differences.

The present chapter supplies the missing completeness principle for bounded compressed sums:

\[
\boxed{
\text{bounded top fan-in}
+
\text{bounded endpoint complexity}
\Longrightarrow
\text{finite local contact capacity}.
}
\]

Thus finitely many local coefficients are not merely a one-sided nonidentity witness. Once a valid uniform bound is known, they become a complete local identity certificate.

## 13.2 Relation to Part VIII

Part VIII used expanded span:

\[
\sum_d\varphi(d)v_{\Phi_d}(P)
\le\operatorname{span}(P).
\]

The present theorem is degree-free but class-dependent. It replaces global span by three compressed parameters:

\[
(d,m,S).
\]

The two bounds are complementary:

- use the global contact budget when span is moderate;
- use the factorial-circuit bound when expanded span is enormous but compressed complexity is bounded.

## 13.3 Relation to Part XI

Part XI proves the sharp monomial-sparse law

\[
\operatorname{ord}_{\zeta}P\le t-1.
\]

The present theorem extends finite local capacity from monomial terms to factorial terms, but loses sharpness and effectivity:

\[
\boxed{
\begin{array}{c|c|c}
\text{class}&\text{capacity}&\text{status}\\ \hline
\text{monomial-sparse}&t-1&\text{explicit and sharp}\\
\text{factorial-circuit}&C_d(m,S)&\text{finite, non-explicit}
\end{array}
}
\]

The lower bound \(C_d(m,S)\ge m-1\) shows that the sparse theorem remains embedded as the unavoidable baseline.

---

# 14. Software primitives

The chapter suggests the following exact interfaces.

## 14.1 `factorial_circuit_depth_profile`

```text
input:
    compressed terms T_i
    cyclotomic order d

output:
    canonical endpoint union
    term depths h_i
```

Correctness follows from Part I.

## 14.2 `factorial_circuit_depth_clusters`

```text
input:
    depths h_i
    certified multiplicity bound C

output:
    maximal C-depth clusters
    regularized order limits R_B
```

The routine verifies every boundary inequality from Definition 8.1.

## 14.3 `factorial_cluster_jets`

```text
input:
    one depth cluster B
    context d
    order R_B

output:
    exact coefficients of
    x^(-h_min(B)) * sum_{i in B} c_i T_i(zeta exp(x))
    through degree R_B
```

The implementation uses endpoint cumulants, Bell polynomials, and exact leading residuals.

## 14.4 `verify_factorial_circuit_identity`

```text
input:
    circuit F
    context d
    certified valid bound C

steps:
    compute depths
    build depth clusters
    compute each finite regularized jet list
    accept iff all coefficients vanish
```

Correctness is Theorems 8.3 and 8.4.

### Caution 14.1 — Bound provenance

Until an explicit formula for \(C_d(m,S)\) is proved, software must not silently invent one.

A certificate must state the theorem, external proof object, or restricted subclass from which the supplied bound is obtained.

---

# 15. Theorem inventory

| Result | Statement | Status | Role |
|---|---|---|---|
| Polynomial universal endpoint germ | Normalized endpoint coefficients lie in \(K[R]\) | Project theorem | Finite parameterization |
| Residual Wronskian factorization | Extract depths from the Wronskian | Project theorem | Separates explicit depth from residual cancellation |
| Noetherian residual bound | Nonzero residual Wronskians have uniformly bounded order | Project theorem | Core finite multiplicity input |
| Adapted-basis Wronskian law | Wronskian order equals sum of vanishing orders minus \(\binom{k}{2}\) | Classical lemma | Converts local order geometry to determinants |
| Generator-subset minimum | First \(k\) vanishing orders equal the minimum generator Wronskian profile | Project theorem | Links term subsets to the whole span |
| Weighted matroid profile | Minimum depth increments are input depths | Classical lemma | Locates vanishing orders near term depths |
| General factorial-circuit multiplicity | Every nonzero order lies within \(C_d(m,S)\) of an input depth | Project theorem | Degree-free local capacity |
| Common-depth bound | Excess multiplicity is at most \(C_d(m,S)\) | Corollary | Collision bound |
| Depth-cluster independence | Widely separated depth blocks cannot cancel | Project theorem | Efficient decomposition |
| Finite cluster jet criterion | At most width plus \(C\) jets decide a cluster | Algorithmic theorem | Complete exact local test |
| Positive-endpoint pairwise fingerprint | First \(2S\) logarithmic coefficients distinguish one term | Project theorem | Explicit individual-term separation |
| Universal lower bound | \(C_d(m,S)\ge m-1\) | Sharpness theorem | Corrects naïve estimates |
| Multinomial circuit consequence | Bounded-endpoint sums inherit the general bound | Corollary | Main CCA application |
| Finite exact reduction | A supplied valid bound reduces PIT to finitely many exact jets | Algorithmic theorem | Computational consequence |

---

# 16. Open problems

## 16.1 Explicit polynomial multiplicity bound

Find an explicit function \(P(d,m,S)\), preferably polynomial, such that

\[
\boxed{C_d(m,S)\le P(d,m,S).}
\]

The pairwise theorem at \(q=1\) suggests that endpoint cumulants become identifiable after order \(2S\), but arbitrary \(m\)-term Wronskian cancellation may require a larger threshold.

## 16.2 Sharp positive-endpoint bound

Determine the optimal value of

\[
C_1(m,S).
\]

Any candidate must satisfy

\[
C_1(m,S)\ge m-1.
\]

The theorem of Section 9 provides explicit pairwise separation at order \(2S\), but no sharp many-term formula is currently proved.

## 16.3 Explicit general-context fingerprint matrices

At \(d\ge2\), the cumulants split into residue channels

\[
K_r(\zeta^a)P_{r,a}.
\]

Find an explicit finite set of derivative orders and Galois coordinates that recovers the exponent vector of one normalized term supported on \(S\) endpoints.

## 16.4 Effective residual-Wronskian ideals

The proof of Theorem 4.3 uses the ideal generated by infinitely many universal residual coefficients. Develop:

1. a finite differential recurrence for those coefficients;
2. an effective Gröbner-basis truncation theorem;
3. explicit degree bounds for the stabilized coefficient ideal.

Any of these could turn the Noetherian existence theorem into a computable bound.

## 16.5 Compact exact arithmetic for jet sums

Develop a polynomial-time equality test for bounded sums of expressions involving:

- factorial powers;
- partial cyclotomic products;
- rational powers of \(d\);
- bounded-order Bell-polynomial combinations.

A modular method must include a deterministic bound proving that enough moduli have been tested.

## 16.6 Restricted subclasses

Before the full theorem is effective, determine explicit bounds for:

- common factorial content times sparse monomial sums;
- two-term factorial collisions;
- fixed exponent alphabet \(e_{ij}\in\{-1,0,1\}\);
- Gaussian binomial sums with common top index;
- fixed-content multinomial families;
- reciprocal factorial circuits at \(q=\pm1\).

## 16.7 Formal verification

Machine-check:

1. coefficientwise polynomiality of universal germs;
2. residual Wronskian factorization;
3. the Noetherian specialization argument;
4. the vanishing-sequence minimum theorem;
5. the weighted matroid step;
6. the depth-cluster identity criterion.

---

# 17. Final statement

For fixed cyclotomic order \(d\), top fan-in \(m\), and endpoint complexity \(S\), sums of compressed factorial quotients have a finite local contact capacity independent of their enormous expanded degrees:

\[
\boxed{
F\ne0
\Longrightarrow
\operatorname{ord}_{\zeta_d}F
\in
\bigcup_i
[h_i-C_d(m,S),h_i+C_d(m,S)].
}
\]

The proof is not a degree argument. It is a finite-parameter argument:

\[
\boxed{
\text{compressed endpoint data}
\longrightarrow
\text{polynomial universal germs}
\longrightarrow
\text{Noetherian Wronskian bound}
\longrightarrow
\text{finite multiplicity}.
}
\]

Given any valid bound, the identity problem reduces exactly to finitely many regularized cyclotomic jets, with the number of required jets controlled only by the compressed circuit parameters.

At the positive endpoint, the first \(2S\) normalized logarithmic coefficients already distinguish individual terms supported on \(S\) endpoints.

The remaining high-value theorem is now sharply isolated:

\[
\boxed{
\text{make }C_d(m,S)\text{ explicit and polynomial,}
}
\]

and combine it with compact exact arithmetic for the resulting bounded jet expressions. That is the missing step from finite determination to a uniform deterministic polynomial-time exact identity test.
