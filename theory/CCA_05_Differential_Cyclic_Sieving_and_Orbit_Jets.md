# Cyclotomic Coefficient Arithmetic

## Part V — Differential Cyclic Sieving and Orbit Jets

**Status:** Proof-complete chapter  
**Scope:** Cyclic actions, canonical orbit polynomials, CSP congruence, local and global higher-order contact, exact orbit jets, and the fixed-content word application.

---

## 1. Purpose of this chapter

Ordinary cyclic sieving compares a polynomial with a cyclic action only at roots of unity. If a cyclic group \(C_N\) acts on a finite set \(X\), and if \(F(q)\in\mathbb Z[q]\) is a cyclic-sieving polynomial, then

\[
F(\omega^j)=\#\operatorname{Fix}(c^j)
\]

for every power of a primitive \(N\)-th root \(\omega\), where \(c\) is a generator of \(C_N\).

Cyclotomic Coefficient Arithmetic asks for the local information discarded by evaluation:

\[
F(\zeta),\quad DF(\zeta),\quad D^2F(\zeta),\quad\ldots,
\qquad D=q\frac{d}{dq}.
\]

The central distinction of this chapter is the distinction between two different jets.

1. The **canonical orbit jet** comes from the cyclic action itself.
2. The **graded jet** comes from the chosen CSP polynomial \(F(q)\).

Ordinary CSP identifies their zeroth terms. In general it does **not** identify their higher derivatives exactly. It identifies them modulo the group order, and exact higher-order agreement occurs precisely when the two polynomials have deeper cyclotomic contact.

The resulting structure is

\[
\boxed{
\text{cyclic action}
\longrightarrow
\text{canonical orbit polynomial}
\longrightarrow
\text{canonical orbit jets}
}
\]

and

\[
\boxed{
\text{CSP polynomial}
=
\text{canonical orbit polynomial}
+
(q^N-1)\times\text{graded correction}.
}
\]

This chapter proves that statement and its higher-order consequences.

---

## 2. Notation and conventions

Let

\[
C_N=\langle c\rangle
\]

be a cyclic group of order \(N\), acting on a finite set \(X\).

Let \(\omega\) be a primitive \(N\)-th root of unity. For \(j\in\mathbb Z\), write

\[
X^{c^j}=\{x\in X:c^j x=x\}.
\]

For a positive integer \(L\), define the \(q\)-integer

\[
[L]_z=1+z+\cdots+z^{L-1}=\frac{1-z^L}{1-z}.
\]

For a polynomial \(P(q)\), use the Euler derivation

\[
D=q\frac{d}{dq}.
\]

If \(q=\zeta e^x\), then

\[
D=\frac{d}{dx}.
\]

For a primitive \(d\)-th root \(\zeta\), write

\[
v_{\Phi_d}(P)
\]

for the multiplicity of the cyclotomic polynomial \(\Phi_d(q)\) in \(P(q)\).

By Part I, this multiplicity is the local vanishing order at \(q=\zeta\):

\[
\boxed{
v_{\Phi_d}(P)
=
\min\{r\ge0:D^rP(\zeta)\ne0\},
}
\]

with the usual convention that the minimum is infinite for the zero polynomial.

---

## 3. The canonical polynomial of one cyclic orbit

Let \(\mathcal O\subseteq X\) be an orbit of size \(L\). Since \(L\mid N\), define its **canonical orbit polynomial** by

\[
\boxed{
O_L(q)
=
[L]_{q^{N/L}}
=
\sum_{u=0}^{L-1}q^{(N/L)u}.
}
\]

The exponents are the equally spaced residues

\[
0,\frac NL,2\frac NL,\ldots,(L-1)\frac NL
\]

in \(\mathbb Z/N\mathbb Z\).

### Theorem 3.1 — Single-Orbit Evaluation Theorem

For every integer \(j\),

\[
\boxed{
O_L(\omega^j)
=
\begin{cases}
L,&L\mid j,\\
0,&L\nmid j.
\end{cases}
}
\]

This equals the number of points of the orbit \(\mathcal O\) fixed by \(c^j\).

#### Proof

Put

\[
\rho=\omega^{jN/L}.
\]

Then

\[
\rho^L=\omega^{jN}=1.
\]

Therefore

\[
O_L(\omega^j)=\sum_{u=0}^{L-1}\rho^u.
\]

If \(\rho=1\), the sum is \(L\). If \(\rho\ne1\), it is a complete geometric sum over the powers of a nontrivial \(L\)-th root of unity, so it is zero.

It remains to identify the condition \(\rho=1\). Since \(\omega\) has exact order \(N\),

\[
\omega^{jN/L}=1
\iff
N\mid \frac{jN}{L}
\iff
L\mid j.
\]

On an orbit of size \(L\), the generator \(c\) acts as an \(L\)-cycle. The power \(c^j\) fixes one point of that orbit if and only if it acts trivially on the entire orbit, which occurs exactly when \(L\mid j\). In that case all \(L\) points are fixed. Thus the polynomial evaluation equals the fixed-point count. ∎

---

## 4. The canonical orbit polynomial of an action

Let \(a_L\) denote the number of orbits of size \(L\), for each divisor \(L\mid N\). Define

\[
\boxed{
O_X(q)
=
\sum_{\mathcal O\in X/C_N}O_{|\mathcal O|}(q)
=
\sum_{L\mid N}a_L[L]_{q^{N/L}}.
}
\]

### Theorem 4.1 — Canonical Orbit Polynomial Theorem

For every integer \(j\),

\[
\boxed{
O_X(\omega^j)=\#X^{c^j}.
}
\]

Moreover,

\[
\deg O_X<N.
\]

#### Proof

The action is the disjoint union of its orbits. By Theorem 3.1, the contribution of each orbit polynomial at \(q=\omega^j\) equals the number of points of that orbit fixed by \(c^j\). Summing over all orbits gives the total fixed-point count.

For an orbit of size \(L\),

\[
\deg O_L
=
\frac NL(L-1)
=
N-\frac NL
<N.
\]

Hence every summand has degree strictly less than \(N\), and so does their sum. ∎

### Corollary 4.2 — Orbit-Count Formula

For every divisor \(m\mid N\),

\[
\boxed{
\#X^{c^m}
=
\sum_{L\mid m}L a_L.
}
\]

#### Proof

An orbit of size \(L\) contributes all \(L\) of its points precisely when \(L\mid m\), and contributes zero otherwise. ∎

### Corollary 4.3 — Möbius Recovery of the Orbit Distribution

For every divisor \(L\mid N\),

\[
\boxed{
a_L
=
\frac1L
\sum_{e\mid L}
\mu\!\left(\frac Le\right)
\#X^{c^e}.
}
\]

#### Proof

Corollary 4.2 has the divisor-sum form

\[
f(m)=\sum_{L\mid m}g(L),
\qquad
f(m)=\#X^{c^m},
\qquad
g(L)=La_L.
\]

Möbius inversion gives

\[
g(L)=\sum_{e\mid L}\mu(L/e)f(e).
\]

Dividing by \(L\) yields the result. ∎

### Interpretation

The full list of ordinary fixed-point counts already determines the orbit-size distribution. Therefore the canonical orbit polynomial is an invariant of the cyclic action itself. Higher derivatives of \(O_X\) do not add independent information beyond the complete orbit distribution, but they reorganize that information into local cyclotomic moments.

---

## 5. Cyclic sieving as a canonical congruence

A triple

\[
(X,C_N,F(q))
\]

with \(F(q)\in\mathbb Z[q]\) exhibits the **cyclic sieving phenomenon** if

\[
F(\omega^j)=\#X^{c^j}
\]

for every integer \(j\).

### Theorem 5.1 — Canonical CSP Congruence

The triple \((X,C_N,F(q))\) exhibits cyclic sieving if and only if

\[
\boxed{
F(q)\equiv O_X(q)\pmod{q^N-1}.
}
\]

Equivalently, there is a unique polynomial \(H(q)\in\mathbb Z[q]\) such that

\[
\boxed{
F(q)-O_X(q)=(q^N-1)H(q).
}
\]

#### Proof

Suppose first that \((X,C_N,F)\) exhibits CSP. By Theorem 4.1,

\[
F(\omega^j)-O_X(\omega^j)=0
\]

for all \(j=0,1,\ldots,N-1\). Thus the difference vanishes at every root of \(q^N-1\).

Over characteristic zero,

\[
q^N-1
\]

is squarefree, because its derivative is \(Nq^{N-1}\), which has no common root with \(q^N-1\). Therefore every linear factor of \(q^N-1\) divides \(F-O_X\), and hence

\[
q^N-1\mid F-O_X
\]

over \(\mathbb C[q]\).

Because the divisor is monic and both polynomials have integer coefficients, ordinary polynomial division gives an integer-coefficient quotient and remainder. The remainder has degree less than \(N\) and vanishes at all \(N\) roots of \(q^N-1\), so it is zero. Thus the quotient lies in \(\mathbb Z[q]\).

Conversely, if

\[
F-O_X=(q^N-1)H,
\]

then at every \(N\)-th root \(\omega^j\),

\[
F(\omega^j)=O_X(\omega^j)=\#X^{c^j}.
\]

Hence the triple exhibits CSP. Uniqueness of \(H\) follows because \(\mathbb Z[q]\) is an integral domain. ∎

### Corollary 5.2 — Canonical Remainder Theorem

If \((X,C_N,F)\) exhibits CSP, then \(O_X(q)\) is the unique polynomial of degree less than \(N\) congruent to \(F(q)\) modulo \(q^N-1\).

#### Proof

Theorem 4.1 gives \(\deg O_X<N\), and Theorem 5.1 gives the congruence. Uniqueness is the uniqueness of the Euclidean remainder modulo the monic polynomial \(q^N-1\). ∎

### Structural meaning

Every CSP polynomial splits canonically as

\[
\boxed{
F(q)
=
O_X(q)
+
(q^N-1)H(q).
}
\]

The first term records the cyclic action. The second term records the choice of graded lift. Ordinary cyclic sieving cannot see \(H\), because \(q^N-1\) vanishes at all relevant roots.

Higher derivatives can see it.

---

## 6. Euler derivatives of the CSP correction

The Euler derivation satisfies the binomial Leibniz rule

\[
D^m(AB)
=
\sum_{r=0}^{m}\binom mr D^rA\,D^{m-r}B.
\]

Also,

\[
D^r(q^N)=N^r q^N.
\]

Therefore, for every \(r\ge1\),

\[
D^r(q^N-1)=N^r q^N.
\]

At an \(N\)-th root \(\zeta\), this becomes

\[
\boxed{
D^r(q^N-1)\big|_{q=\zeta}=N^r.
}
\]

### Theorem 6.1 — Exact Differential CSP Comparison Formula

Suppose

\[
F(q)-O_X(q)=(q^N-1)H(q).
\]

Then for every \(N\)-th root \(\zeta\) and every integer \(m\ge0\),

\[
\boxed{
D^mF(\zeta)-D^mO_X(\zeta)
=
\sum_{r=1}^{m}
\binom mr
N^rD^{m-r}H(\zeta).
}
\]

For \(m=0\), the sum is empty and the formula says

\[
F(\zeta)=O_X(\zeta).
\]

#### Proof

Apply \(D^m\) to

\[
F-O_X=(q^N-1)H.
\]

By the Leibniz rule,

\[
D^m(F-O_X)
=
\sum_{r=0}^{m}
\binom mr
D^r(q^N-1)D^{m-r}H.
\]

At \(q=\zeta\), the term with \(r=0\) vanishes because \(\zeta^N-1=0\). For \(r\ge1\),

\[
D^r(q^N-1)(\zeta)=N^r.
\]

Substitution gives the claimed formula. ∎

### Corollary 6.2 — Differential CSP Congruence

For every \(m\ge0\),

\[
\boxed{
D^mF(\zeta)
\equiv
D^mO_X(\zeta)
\pmod{N\mathbb Z[\zeta]}.
}
\]

#### Proof

For \(m=0\), the two sides are equal. For \(m\ge1\), every term in Theorem 6.1 contains a factor \(N^r\), hence a factor \(N\). Since \(H\in\mathbb Z[q]\), every \(D^sH(\zeta)\) belongs to the ring of cyclotomic integers \(\mathbb Z[\zeta]\). ∎

### Important warning

Ordinary CSP gives exact equality only at derivative order zero. In general,

\[
DF(\zeta)\ne DO_X(\zeta).
\]

What ordinary CSP always gives is the weaker but exact arithmetic statement

\[
DF(\zeta)-DO_X(\zeta)\in N\mathbb Z[\zeta].
\]

---

## 7. Higher-order differential cyclic sieving

The correction polynomial \(H\) measures the failure of higher jets to agree. This leads to a precise hierarchy.

### Definition 7.1 — Local Differential CSP Order

Let \(\zeta\) be a primitive \(d\)-th root, with \(d\mid N\). Define

\[
\boxed{
\delta_d(F,X)
=
v_{\Phi_d}(F-O_X).
}
\]

Equivalently, \(\delta_d(F,X)\) is the local contact order of the graded polynomial \(F\) with the canonical orbit polynomial at the context \(q=\zeta\).

Ordinary CSP guarantees

\[
\delta_d(F,X)\ge1
\]

for every divisor \(d\mid N\).

### Theorem 7.2 — Local Higher-Order CSP Criterion

For an integer \(r\ge1\), the following are equivalent:

1. \(\delta_d(F,X)\ge r\);
2. \(\Phi_d(q)^r\mid F(q)-O_X(q)\);
3. for one, equivalently every, primitive \(d\)-th root \(\zeta\),
   \[
   D^jF(\zeta)=D^jO_X(\zeta)
   \qquad(0\le j<r).
   \]

#### Proof

The equivalence of the first two statements is the definition of the valuation. By the local jet criterion proved in Part I,

\[
v_{\Phi_d}(P)\ge r
\iff
D^jP(\zeta)=0
\quad(0\le j<r).
\]

Apply this to

\[
P=F-O_X.
\]

This gives the equivalence with the third statement. Because \(F-O_X\) has rational, indeed integer, coefficients, vanishing at one primitive \(d\)-th root propagates to every Galois conjugate primitive \(d\)-th root. ∎

### Definition 7.3 — Global Differential CSP Order

Define

\[
\boxed{
\delta_N(F,X)
=
\min_{d\mid N}\delta_d(F,X).
}
\]

The triple has **global differential CSP order at least \(r\)** if

\[
\delta_N(F,X)\ge r.
\]

### Theorem 7.4 — Global Higher-Order CSP Criterion

For \(r\ge1\), the following are equivalent:

1. \(\delta_N(F,X)\ge r\);
2. for every divisor \(d\mid N\),
   \[
   \Phi_d(q)^r\mid F(q)-O_X(q);
   \]
3. \[
   \boxed{(q^N-1)^r\mid F(q)-O_X(q);}
   \]
4. for every \(N\)-th root \(\zeta\),
   \[
   D^jF(\zeta)=D^jO_X(\zeta)
   \qquad(0\le j<r).
   \]

#### Proof

The first two statements are equivalent by definition.

Over \(\mathbb Z[q]\),

\[
q^N-1=\prod_{d\mid N}\Phi_d(q),
\]

and the cyclotomic factors are pairwise coprime. Therefore

\[
(q^N-1)^r
=
\prod_{d\mid N}\Phi_d(q)^r
\]

divides \(F-O_X\) if and only if every \(\Phi_d^r\) does.

The equivalence with the fourth statement follows by applying Theorem 7.2 at every cyclotomic context whose order divides \(N\). ∎

### Interpretation

Ordinary CSP is precisely global differential order at least one:

\[
F-O_X\in(q^N-1).
\]

Second-order differential CSP means

\[
F-O_X\in(q^N-1)^2,
\]

so both values and first Euler derivatives agree at every \(N\)-th root.

In general, order \(r\) means agreement of the first \(r\) local Taylor coefficients at every cyclic context.

---

## 8. Exact jets of a single orbit

Let \(\zeta\) be any \(N\)-th root of unity. For an orbit size \(L\mid N\), put

\[
a=\frac NL,
\qquad
\rho=\zeta^a.
\]

Then \(\rho^L=1\).

### Theorem 8.1 — Single-Orbit Jet Formula

For every integer \(m\ge0\),

\[
\boxed{
D^mO_L(\zeta)
=
\left(\frac NL\right)^m
\sum_{u=0}^{L-1}u^m\rho^u.
}
\]

#### Proof

Since

\[
O_L(q)=\sum_{u=0}^{L-1}q^{au},
\]

and

\[
D^mq^{au}=(au)^mq^{au},
\]

we obtain

\[
D^mO_L(\zeta)
=
\sum_{u=0}^{L-1}(au)^m\zeta^{au}
=
a^m\sum_{u=0}^{L-1}u^m\rho^u.
\]

Substituting \(a=N/L\) proves the formula. ∎

The inner sum

\[
\sum_{u=0}^{L-1}u^m\rho^u
\]

is a finite Fourier moment of the position coordinate on the orbit.

### Corollary 8.2 — Fixed-Orbit Jet

If \(\rho=1\), equivalently if the corresponding group element fixes the orbit pointwise, then

\[
\boxed{
D^mO_L(\zeta)
=
\left(\frac NL\right)^m
\sum_{u=0}^{L-1}u^m.
}
\]

Thus fixed orbits contribute ordinary power sums.

### Corollary 8.3 — Nonfixed First Jet

If \(\rho\ne1\), then

\[
\boxed{
DO_L(\zeta)
=-\frac{N}{1-\rho}.
}
\]

#### Proof

For \(\rho^L=1\) and \(\rho\ne1\), differentiate the finite geometric sum:

\[
\sum_{u=0}^{L-1}u\rho^u
=
\rho\frac{d}{d\rho}
\left(\frac{1-\rho^L}{1-\rho}\right).
\]

A direct simplification at \(\rho^L=1\) gives

\[
\sum_{u=0}^{L-1}u\rho^u
=-\frac{L}{1-\rho}.
\]

Multiplying by \(N/L\) yields the result. ∎

### Theorem 8.4 — Single-Orbit Local Depth

Let \(\zeta\) have exact order \(d\mid N\). Then

\[
\boxed{
v_{q-\zeta}(O_L)
=
\begin{cases}
0,&\zeta^{N/L}=1,\\
1,&\zeta^{N/L}\ne1.
\end{cases}
}
\]

Equivalently,

\[
\boxed{
v_{\Phi_d}(O_L)
=
\begin{cases}
0,&d\mid N/L,\\
1,&d\nmid N/L.
\end{cases}
}
\]

#### Proof

If \(\zeta^{N/L}=1\), then Theorem 3.1 gives

\[
O_L(\zeta)=L\ne0,
\]

so the local depth is zero.

If \(\zeta^{N/L}\ne1\), use the local identity

\[
O_L(q)=\frac{1-q^N}{1-q^{N/L}}.
\]

At \(q=\zeta\), the denominator is nonzero and hence a unit in the local ring. The numerator \(1-q^N\) has a simple zero, because

\[
\frac{d}{dq}(1-q^N)\bigg|_{q=\zeta}
=-N\zeta^{N-1}\ne0.
\]

Therefore \(O_L\) has local depth exactly one.

Finally,

\[
\zeta^{N/L}=1
\iff
d\mid N/L.
\]

This proves the cyclotomic form. ∎

### Consequence

A single nonfixed orbit vanishes only simply at a cyclic context. Higher-order vanishing of the total orbit polynomial can therefore arise only through cancellation among the first and subsequent jets of several orbit contributions.

---

## 9. Canonical orbit jets from the orbit profile

Let \(a_L\) be the orbit counts. By linearity:

### Theorem 9.1 — Orbit-Profile Jet Transform

For every \(m\ge0\),

\[
\boxed{
D^mO_X(\zeta)
=
\sum_{L\mid N}
a_L
\left(\frac NL\right)^m
\sum_{u=0}^{L-1}
u^m\left(\zeta^{N/L}\right)^u.
}
\]

#### Proof

Apply Theorem 8.1 to every orbit polynomial and sum. ∎

This is a linear transform from the orbit-size vector

\[
(a_L)_{L\mid N}
\]

to the local jet sequence

\[
\left(D^mO_X(\zeta)\right)_{m\ge0}.
\]

### Exact non-expanding computation

The formula need not be evaluated by iterating over \(u=0,\ldots,L-1\). For fixed derivative order \(r\), define

\[
S_L(x;\rho)
=
\sum_{u=0}^{L-1}\rho^ue^{ux}
=
\frac{1-e^{Lx}}{1-\rho e^x}.
\]

Then

\[
\boxed{
\sum_{u=0}^{L-1}u^m\rho^u
=
\left.\frac{d^m}{dx^m}S_L(x;\rho)\right|_{x=0}.
}
\]

For \(\rho\ne1\), the denominator is a unit at \(x=0\), so a truncated power-series division computes all moments through order \(r\) using \(O(r^2)\) exact cyclotomic-field operations.

For \(\rho=1\), the moments are ordinary Faulhaber sums and can be computed from Bernoulli numbers, also without iterating through all \(L\) positions.

Thus the first \(r\) canonical orbit jets can be computed in time polynomial in \(r\), the number of supported orbit sizes, and the bit length of \(N\), independently of \(|X|\).

---

## 10. Why ordinary CSP does not imply derivative equality

The following example is decisive.

### Example 10.1 — A free rotation action with a second-order graded zero

Let \(X\) be the set of words of length six in which six distinct letters each occur once. Then

\[
|X|=6!=720.
\]

Let \(C_6\) act by cyclic rotation. Because all letters are distinct, no nonidentity rotation fixes a word. The action is free, so there are

\[
720/6=120
\]

orbits, all of size six.

Hence the canonical orbit polynomial is

\[
O_X(q)=120[6]_q.
\]

The standard CSP polynomial is

\[
F(q)=[6]_q!,
\]

the \(q\)-factorial.

Let \(\zeta\) be a primitive cube root of unity. The factors \([3]_q\) and \([6]_q\) both vanish simply at \(q=\zeta\), while the other \(q\)-integer factors do not. Therefore

\[
v_{\Phi_3}(F)=2,
\]

so

\[
F(\zeta)=DF(\zeta)=0.
\]

On the other hand,

\[
O_X(\zeta)=120\sum_{u=0}^{5}\zeta^u=0,
\]

but

\[
DO_X(\zeta)
=120\sum_{u=0}^{5}u\zeta^u.
\]

Using \(\zeta^3=1\),

\[
\sum_{u=0}^{5}u\zeta^u
=3+5\zeta+7\zeta^2
=-2(2+\zeta).
\]

Hence

\[
\boxed{
DO_X(\zeta)=-240(2+\zeta)\ne0.
}
\]

Thus

\[
DF(\zeta)\ne DO_X(\zeta).
\]

Nevertheless,

\[
DO_X(\zeta)-DF(\zeta)
=-240(2+\zeta)
\in6\mathbb Z[\zeta],
\]

exactly as predicted by Corollary 6.2.

### Lesson

The second-order vanishing of \(F\) is a property of the chosen grading. It is not forced by the ungraded cyclic action. Ordinary CSP remembers the value but forgets the transverse derivative.

---

## 11. Fixed-content words and the multinomial CSP

Let

\[
\mathbf k=(k_1,\ldots,k_c),
\qquad
k_1+\cdots+k_c=n.
\]

Let \(X_{\mathbf k}\) be the set of words of length \(n\) over an alphabet of \(c\) letters, with letter \(\nu\) appearing exactly \(k_\nu\) times. Let \(C_n\) act by cyclic rotation.

Define

\[
M_{\mathbf k}(q)
=
{n\brack k_1,\ldots,k_c}_q.
\]

### Theorem 11.1 — Fixed-Content Rotation CSP

The triple

\[
\boxed{
\left(X_{\mathbf k},C_n,M_{\mathbf k}(q)\right)
}
\]

exhibits the cyclic sieving phenomenon.

#### Proof

Let \(c^j\) be a rotation, and let its order be \(d\). Then

\[
d=\frac{n}{\gcd(n,j)}.
\]

The permutation of the \(n\) positions induced by \(c^j\) consists of

\[
a=\frac nd
\]

cycles, each of length \(d\).

A word fixed by \(c^j\) must be constant on each position-cycle. Therefore each content \(k_\nu\) must be divisible by \(d\). If

\[
k_\nu=dr_\nu
\]

for every \(\nu\), then one chooses which \(r_\nu\) of the \(a\) cycles receive letter \(\nu\), giving

\[
\#X_{\mathbf k}^{c^j}
=
\binom{a}{r_1,\ldots,r_c}.
\]

If some \(k_\nu\) is not divisible by \(d\), there are no fixed words.

Now let \(\zeta\) be a primitive \(d\)-th root. Write

\[
k_\nu=r_\nu d+s_\nu,
\qquad
0\le s_\nu<d.
\]

By the Multinomial Defect Theorem from Part III,

\[
v_{\Phi_d}(M_{\mathbf k})
=h,
\qquad
\sum_\nu s_\nu=hd.
\]

If every \(s_\nu=0\), then \(h=0\), and the local residual formula gives

\[
M_{\mathbf k}(\zeta)
=
\frac{a!}{\prod_\nu r_\nu!}
=
\binom{a}{r_1,\ldots,r_c}.
\]

If some \(s_\nu\ne0\), then \(h\ge1\), so

\[
M_{\mathbf k}(\zeta)=0.
\]

Thus the root-of-unity evaluation equals the fixed-word count for every group element. ∎

---

## 12. Defect depth and orbit-moment congruences

Continue with

\[
n=ad,
\qquad
k_\nu=r_\nu d+s_\nu,
\qquad
\sum_\nu s_\nu=hd.
\]

Let \(\zeta\) be primitive of order \(d\), and let

\[
O_{\mathbf k}(q)=O_{X_{\mathbf k}}(q)
\]

be the canonical orbit polynomial of the rotation action.

By Part III,

\[
D^mM_{\mathbf k}(\zeta)=0
\qquad(0\le m<h),
\]

and

\[
\boxed{
\frac{D^hM_{\mathbf k}(\zeta)}{h!}
=
(-1)^hd^{2h}
\frac{a!}{\prod_\nu r_\nu!}
\frac1{\prod_\nu A_{s_\nu}(\zeta)},
}
\]

where

\[
A_s(\zeta)=\prod_{u=1}^{s}(1-\zeta^u),
\qquad A_0(\zeta)=1.
\]

### Theorem 12.1 — Defect-to-Orbit Moment Congruence

For every \(m<h\),

\[
\boxed{
D^mO_{\mathbf k}(\zeta)
\equiv0
\pmod{n\mathbb Z[\zeta]}.
}
\]

At the first visible order,

\[
\boxed{
D^hO_{\mathbf k}(\zeta)
\equiv
h!(-1)^hd^{2h}
\frac{a!}{\prod_\nu r_\nu!}
\frac1{\prod_\nu A_{s_\nu}(\zeta)}
\pmod{n\mathbb Z[\zeta]}.
}
\]

#### Proof

By Theorem 11.1, the multinomial is a CSP polynomial for the rotation action. Therefore Corollary 6.2 gives

\[
D^mM_{\mathbf k}(\zeta)
\equiv
D^mO_{\mathbf k}(\zeta)
\pmod{n\mathbb Z[\zeta]}.
\]

For \(m<h\), the left side is zero by the defect theorem, yielding the first congruence.

For \(m=h\), substitute the explicit first-visible-jet formula from Part III. ∎

### Orbit-profile form

If \(a_L(\mathbf k)\) denotes the number of rotation orbits of size \(L\) in \(X_{\mathbf k}\), then Theorem 9.1 rewrites the congruence as

\[
\boxed{
\sum_{L\mid n}
a_L(\mathbf k)
\left(\frac nL\right)^m
\sum_{u=0}^{L-1}
u^m
\left(\zeta^{n/L}\right)^u
\equiv0
\pmod{n\mathbb Z[\zeta]}
}
\]

for \(0\le m<h\).

At \(m=h\), the same left side is congruent to the explicit defect-core residual above.

### Significance

The residue defect does not force the canonical orbit polynomial to vanish to order \(h\). Instead it forces a hierarchy of exact divisibility relations among the Fourier moments of the orbit-size distribution.

This is the correct action-level shadow of the multinomial vanishing theorem.

---

## 13. Local correction germs

Fix an \(N\)-th root \(\zeta\), and use

\[
q=\zeta e^x.
\]

Write

\[
f(x)=F(\zeta e^x),
\qquad
o(x)=O_X(\zeta e^x),
\qquad
h(x)=H(\zeta e^x).
\]

Since \(\zeta^N=1\), the canonical CSP congruence becomes

\[
\boxed{
f(x)-o(x)=(e^{Nx}-1)h(x).
}
\]

This is the local normal form of differential cyclic sieving.

### Theorem 13.1 — Local Differential Normal Form

At every cyclic context,

\[
\boxed{
F(\zeta e^x)
=
O_X(\zeta e^x)
+
(e^{Nx}-1)H(\zeta e^x).
}
\]

Consequently, the action and grading have the same constant term, while every higher discrepancy is generated by the universal transverse factor

\[
e^{Nx}-1
=Nx+\frac{N^2x^2}{2!}+\cdots.
\]

#### Proof

Substitute \(q=\zeta e^x\) into

\[
F-O_X=(q^N-1)H.
\]

Because \(\zeta^N=1\),

\[
q^N-1=(\zeta e^x)^N-1=e^{Nx}-1.
\]

The conclusion follows. ∎

### Corollary 13.2 — Regularized Differential Correction

The quotient

\[
\boxed{
\mathcal H_\zeta(x)
=
\frac{F(\zeta e^x)-O_X(\zeta e^x)}{e^{Nx}-1}
}
\]

is analytic at \(x=0\) and equals \(H(\zeta e^x)\).

Its Taylor coefficients measure the successive failures of exact higher-order cyclic sieving.

---

## 14. Action data versus grading data

The theory separates three levels.

### Level 0 — Fixed points

\[
F(\zeta)=O_X(\zeta)=\#\operatorname{Fix}(g).
\]

This is ordinary CSP.

### Level 1 — Canonical orbit geometry

\[
DO_X(\zeta),\quad D^2O_X(\zeta),\ldots
\]

These are exact transforms of the orbit-size distribution.

### Level 2 — Graded transverse geometry

\[
DF(\zeta),\quad D^2F(\zeta),\ldots
\]

These depend on the chosen statistic or grading represented by \(F\).

The difference is controlled by

\[
F-O_X=(q^N-1)H.
\]

Hence

\[
\boxed{
\text{action jet}
+
\text{universal cyclic normal direction}
\times
\text{graded correction germ}
=
\text{graded jet}.
}
\]

The correction is invisible to ordinary CSP but visible to derivatives.

---

## 15. Exact computational architecture

This section records the intended non-expanding implementation.

### 15.1 Orbit-profile representation

Represent a cyclic action by

```text
CyclicOrbitProfile(
    group_order=N,
    orbit_counts={L: a_L for L | N}
)
```

Validation rules:

- \(N\ge1\);
- every supported \(L\) is positive and divides \(N\);
- every \(a_L\) is a nonnegative integer;
- zero counts are removed during normalization.

The total set size is

\[
|X|=\sum_{L\mid N}La_L.
\]

### 15.2 Canonical orbit polynomial

For moderate \(N\), construct

\[
O_X(q)=\sum_{L\mid N}a_L[L]_{q^{N/L}}.
\]

For enormous \(N\), do not expand it. Retain the orbit-profile representation.

### 15.3 Exact orbit jet API

A natural API is

```python
orbit_jet(profile, d, order)
```

where \(d\mid N\), and the context is represented by an exact primitive \(d\)-th root in a cyclotomic field.

The return value should contain

```text
OrbitJet(
    context_order=d,
    derivatives=(J_0, J_1, ..., J_order),
    coefficient_field=Q(zeta_d)
)
```

with

\[
J_m=D^mO_X(\zeta_d).
\]

### 15.4 Moment computation without orbit expansion

For each supported orbit size \(L\), compute

\[
\rho=\zeta_d^{N/L}.
\]

If \(\rho=1\), use Faulhaber power sums.

If \(\rho\ne1\), truncate

\[
\frac{1-e^{Lx}}{1-\rho e^x}
\]

through degree `order`. This yields every moment

\[
\sum_{u=0}^{L-1}u^m\rho^u
\]

without \(O(L)\) iteration.

For maximum derivative order \(r\), the arithmetic cost is

\[
O(sr^2)
\]

cyclotomic-field operations, where \(s\) is the number of supported orbit sizes.

### 15.5 CSP comparison API

Given a symbolic or compressed polynomial \(F\), expose

```python
compare_csp_jet(F, orbit_profile, d, order)
```

returning

```text
DifferentialCSPCertificate(
    context_order=d,
    contact_order=delta,
    graded_jet=(...),
    orbit_jet=(...),
    differences=(...),
    differences_mod_group_order=(...)
)
```

The certificate must distinguish:

- exact equality in \(\mathbb Z[\zeta_d]\);
- equality modulo \(N\mathbb Z[\zeta_d]\);
- local contact order \(v_{\Phi_d}(F-O_X)\).

### 15.6 Exact arithmetic requirement

Never use floating-point approximations to decide whether a jet vanishes or whether two jets agree.

Use one of:

- a quotient ring \(\mathbb Q[q]/(\Phi_d(q))\);
- an exact cyclotomic field;
- a library-native algebraic-number type.

---

## 16. Testing plan

### 16.1 Orbit evaluation tests

For every small \(N\), every divisor \(L\mid N\), and every \(j\), verify

\[
[L]_{(\omega^j)^{N/L}}
=
\begin{cases}
L,&L\mid j,\\
0,&L\nmid j.
\end{cases}
\]

### 16.2 Canonical remainder tests

Generate random small orbit profiles and random correction polynomials \(H(q)\). Set

\[
F=O_X+(q^N-1)H.
\]

Verify:

- root evaluations match fixed counts;
- the remainder of \(F\) modulo \(q^N-1\) is exactly \(O_X\);
- Theorem 6.1 holds through several derivative orders.

### 16.3 Higher-contact tests

Generate

\[
F=O_X+(q^N-1)^rH
\]

and verify exact equality of all jets through order \(r-1\) at every \(N\)-th root, with generic inequality at order \(r\).

### 16.4 Orbit-moment tests

Compare the non-expanding truncated-series computation with direct sums

\[
\sum_{u=0}^{L-1}u^m\rho^u
\]

for small \(L\).

### 16.5 Fixed-content word tests

For small contents \(\mathbf k\):

1. enumerate words and rotation orbits;
2. construct the orbit profile;
3. construct the \(q\)-multinomial;
4. verify CSP evaluations;
5. verify differential congruences modulo \(n\);
6. verify defect-to-orbit moment congruences.

### 16.6 Regression example

Include Example 10.1 as a permanent test showing that ordinary CSP does not imply first-derivative equality.

---

## 17. Theorem inventory

| No. | Theorem | Hypotheses | Conclusion | Status |
|---:|---|---|---|---|
| 3.1 | Single-Orbit Evaluation | Orbit size \(L\mid N\) | \(O_L(\omega^j)\) equals the orbit fixed-point count | Proved |
| 4.1 | Canonical Orbit Polynomial | Finite \(C_N\)-set | \(O_X(\omega^j)=\#X^{c^j}\), \(\deg O_X<N\) | Proved |
| 4.3 | Möbius Orbit Recovery | Fixed counts for divisors of \(N\) | Exact recovery of every orbit count \(a_L\) | Proved |
| 5.1 | Canonical CSP Congruence | \(F\in\mathbb Z[q]\) | CSP iff \(F\equiv O_X\pmod{q^N-1}\) | Proved |
| 5.2 | Canonical Remainder | CSP triple | \(O_X\) is the unique degree-\(<N\) remainder | Proved |
| 6.1 | Differential Comparison | \(F-O_X=(q^N-1)H\) | Exact formula for every derivative difference | Proved |
| 6.2 | Differential Congruence | CSP triple | Jets agree modulo \(N\mathbb Z[\zeta]\) | Proved |
| 7.2 | Local Higher-Order Criterion | Primitive \(d\)-context | Contact order equals number of matching jets | Proved |
| 7.4 | Global Higher-Order Criterion | All \(N\)-th-root contexts | \((q^N-1)^r\) divisibility iff all jets below \(r\) agree | Proved |
| 8.1 | Single-Orbit Jet Formula | Orbit size \(L\mid N\) | Exact finite Fourier-moment formula | Proved |
| 8.4 | Single-Orbit Local Depth | Primitive \(d\)-context | A nonfixed orbit has depth exactly one | Proved |
| 9.1 | Orbit-Profile Jet Transform | Orbit counts \(a_L\) | Exact linear transform to canonical jets | Proved |
| 11.1 | Fixed-Content Rotation CSP | Words of content \(\mathbf k\) | \(q\)-multinomial exhibits rotation CSP | Proved |
| 12.1 | Defect-to-Orbit Congruence | \(n=ad\), defect \(h\) | First \(h-1\) orbit moments vanish modulo \(n\); order \(h\) has explicit residue | Proved |
| 13.1 | Local Differential Normal Form | CSP triple and \(N\)-th root \(\zeta\) | \(f-o=(e^{Nx}-1)h\) | Proved |

---

## 18. What is established and what remains open

### Established

The following are exact theorems:

1. every cyclic action has a canonical orbit polynomial;
2. every CSP polynomial is congruent to it modulo \(q^N-1\);
3. all higher graded jets agree with canonical orbit jets modulo \(N\);
4. exact higher-order agreement is equivalent to higher powers of cyclotomic or global cyclic divisibility;
5. canonical orbit jets are exact Fourier moments of orbit positions;
6. multinomial residue defects imply explicit congruences for rotation-orbit moments.

### Not yet established

The following should not be claimed as completed results:

1. a universal positive combinatorial interpretation of \(D^mF(\zeta)\) for an arbitrary CSP polynomial;
2. a theorem saying that multinomial defect \(h\) forces \(F-O_X\) to have depth \(h\);
3. a canonical statistic on ungraded orbits whose ordinary moments always equal the graded jet exactly;
4. a general finite-jet completeness theorem deciding equality of arbitrary compressed CSP polynomials;
5. a classification of actions or gradings with global differential order greater than one.

---

## 19. Principal open problems

### Open Problem 19.1 — Exact combinatorial meaning of the graded jet

Find a natural signed or weighted statistic \(\mu_m\) on cyclic objects such that

\[
D^mF(\zeta)
=
\sum_{x\in X}\mu_m(x;\zeta)
\]

for broad CSP families, with the construction depending intrinsically on the grading.

### Open Problem 19.2 — Classification of higher-order CSP lifts

Classify all CSP polynomials satisfying

\[
F(q)\equiv O_X(q)\pmod{(q^N-1)^r}.
\]

Even the case \(r=2\) asks for a structural characterization of gradings whose first derivative is completely determined by the action.

### Open Problem 19.3 — Orbit interpretation of multinomial defect

The defect

\[
h=v_{\Phi_d}(M_{\mathbf k})
\]

is the first visible graded derivative order. Find an action-level or orbit-complex interpretation that explains the modulo-\(n\) moment cancellations of Theorem 12.1 directly.

### Open Problem 19.4 — Differential CSP for other families

Develop analogous local-jet theories for:

- Gaussian binomial subset actions;
- plane partitions;
- noncrossing partitions;
- promotion and rowmotion actions;
- finite-field Grassmannians;
- cyclic actions arising from representation theory.

### Open Problem 19.5 — Efficient exact implementation

Implement canonical orbit jets and compressed graded jets in SageMath or OSCAR, then benchmark contexts with enormous group order and compressed orbit profiles.

---

## 20. Final synthesis

Ordinary cyclic sieving is the zeroth-order statement

\[
\boxed{
F(\zeta)=O_X(\zeta).
}
\]

Differential cyclic sieving replaces equality of values by a hierarchy of local contacts:

\[
\boxed{
F-O_X\in(\Phi_d)^r
\iff
D^jF(\zeta)=D^jO_X(\zeta)
\quad(0\le j<r).
}
\]

Globally,

\[
\boxed{
F-O_X\in(q^N-1)^r
\iff
\text{the first }r\text{ jets agree at every cyclic context}.
}
\]

Without additional hypotheses, ordinary CSP yields the universal congruence

\[
\boxed{
D^mF(\zeta)
\equiv
D^mO_X(\zeta)
\pmod{N\mathbb Z[\zeta]}.
}
\]

For fixed-content words, the multinomial defect upgrades this to explicit orbit-moment congruences. Thus the complete conceptual chain is

\[
\boxed{
\text{contextual collapse}
+
\text{local vanishing depth}
+
\text{transverse jets}
=
\text{Differential Cyclic Sieving}.
}
\]

---

## Dependency map

This chapter uses the following earlier results:

- **Part I:** cyclotomic depth, local rings, and the jet criterion;
- **Part III:** multinomial defect, local residual, and first visible jet.

It supplies the action-theoretic bridge needed for subsequent algorithmic and application chapters.
