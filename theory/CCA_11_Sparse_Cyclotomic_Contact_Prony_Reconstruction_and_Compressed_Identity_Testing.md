# Cyclotomic Coefficient Arithmetic

## Part XI — Sparse Cyclotomic Contact, Prony Reconstruction, and Compressed Identity Testing

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete theorem chapter  
**Scope:** Sparse Laurent polynomials, sharp local contact bounds, cyclotomic multiplicity bounds independent of degree, saturation and barycentric normal forms, optimal sparse identity testing, Euler-moment sequences, Hankel rank, annihilating recurrences, exact Prony reconstruction at one root-of-unity context, cyclotomic de-aliasing, reciprocal endpoint sparsity, even-jet reconstruction at $q=\pm1$, hybrid degree–sparsity certificates, differential cyclic-sieving consequences, exact algorithms, sharpness, and research boundaries.

---

# 0. Purpose, relation to Parts VIII–X, and novelty boundary

Part VIII proved the Global Cyclotomic Contact Budget

$$
\sum_{d\ge1}\varphi(d)v_{\Phi_d}(P)
\le
\operatorname{span}(P),
$$

and converted sufficiently many matching cyclotomic jets into a complete identity certificate.

Part IX proved optimal reconstruction in the full polynomial space. A jet schedule of weighted size

$$
B=\sum_d\varphi(d)r_d
$$

reconstructs a unique polynomial of degree less than $B$.

Part X descended that theory to reciprocal polynomials. After passing to the real coordinate

$$
x=q+q^{-1},
$$

the relevant information dimension is reduced to the real-cyclotomic half-budget.

All three results are controlled by an expanded degree or span. If an exponent is enormous, then the generic reconstruction budget can be enormous even when the expression has only a few nonzero terms.

The present chapter studies the opposite regime.

Let

$$
P(q)=\sum_{\nu=1}^{t}c_\nu q^{e_\nu},
\qquad
c_\nu\ne0,
\qquad
 e_\nu\in\mathbb Z
$$

with distinct exponents. The expanded span may be arbitrarily large, while the number of terms $t$ remains small.

The principal theorem is the sharp local law

$$
\boxed{
\operatorname{ord}_{q=\xi}P\le t-1
}
\qquad(\xi\ne0).
$$

At a primitive $d$-th root of unity, this becomes

$$
\boxed{
v_{\Phi_d}(P)\le t-1.
}
$$

Thus one local cyclotomic context has a finite **sparse contact capacity** independent of the exponent span.

Applied to a difference, this gives an optimal compressed identity test:

$$
\boxed{
\begin{array}{c}
\sigma(F)\le s,\quad \sigma(G)\le t,\\[1mm]
D^jF(\xi)=D^jG(\xi)\quad(0\le j<s+t)
\end{array}
\Longrightarrow
F=G.
}
$$

The same Euler jets are power moments of the unknown exponents:

$$
D^jP(\xi)
=
\sum_{\nu=1}^{t}
\bigl(c_\nu\xi^{e_\nu}\bigr)e_\nu^j.
$$

Consequently, the first $2t$ jets determine the exponent support and coefficients exactly through a Hankel recurrence and a Vandermonde solve.

The resulting structure is

$$
\boxed{
\text{sparse support}
\longrightarrow
\text{Euler moments}
\longrightarrow
\text{annihilating recurrence}
\longrightarrow
\text{exact exponent recovery}.
}
$$

The Vandermonde and Prony mechanisms are classical. The contribution of this chapter is their exact incorporation into Cyclotomic Coefficient Arithmetic:

1. a sharp cyclotomic contact theorem depending on sparsity rather than degree;
2. optimal one-context identity certificates;
3. root-of-unity reconstruction without residue-class aliasing;
4. a reciprocal endpoint theory measured by inversion-orbit sparsity;
5. a hybrid certificate framework combining Parts VIII–X with sparse reconstruction.

The labels used below are:

- **Classical lemma:** standard linear-algebraic or interpolation input, proved here;
- **Project theorem:** a theorem established in the CCA framework;
- **Corollary:** a formal consequence;
- **Algorithmic theorem:** a correctness theorem for an exact procedure;
- **Sharpness statement:** a theorem proving that a threshold cannot be improved;
- **Caution:** a boundary required for exact mathematics or software.

Throughout,

$$
D=q\frac d{dq}.
$$

All coefficient fields have characteristic zero unless stated otherwise.

---

# 1. Sparse Laurent polynomials and Euler jets

## 1.1 Sparse support

Let $K$ be a field of characteristic zero.

### Definition 1.1 — Laurent sparsity

For a nonzero Laurent polynomial

$$
P(q)=\sum_{e\in S}c_eq^e
\in K[q,q^{-1}],
\qquad c_e\ne0,
$$

define its support and sparsity by

$$
\boxed{
\operatorname{supp}(P)=S,
\qquad
\sigma(P)=|S|.
}
$$

Set

$$
\sigma(0)=0.
$$

The support exponents are always assumed distinct after equal exponents have been combined.

### Lemma 1.2 — Elementary sparsity rules

For Laurent polynomials $F,G$,

$$
\boxed{
\sigma(F+G)\le \sigma(F)+\sigma(G),
}
$$

and, for every integer $a$,

$$
\boxed{
\sigma(q^aF)=\sigma(F).
}
$$

If the supports of $F$ and $G$ are disjoint, then

$$
\sigma(F+G)=\sigma(F)+\sigma(G).
$$

#### Proof

Every exponent occurring in $F+G$ belongs to the union of the two supports. Equal exponents may cancel, so the support can shrink but cannot exceed that union.

Multiplication by $q^a$ translates every exponent by $a$ and preserves the number of support points.

If the supports are disjoint, no coefficient combination or cancellation occurs, so the union has exactly the sum of the two sizes. ∎

## 1.2 Euler moments at a nonzero context

Fix a nonzero element $\xi$ in some field extension $\Omega/K$.

### Definition 1.3 — Euler moment sequence

For

$$
P(q)=\sum_{\nu=1}^{t}c_\nu q^{e_\nu},
$$

define

$$
\boxed{
\mu_j(P;\xi)=D^jP(\xi)
\qquad(j\ge0).
}
$$

### Lemma 1.4 — Exact sparse moment formula

For every $j\ge0$,

$$
\boxed{
\mu_j(P;\xi)
=
\sum_{\nu=1}^{t}
w_\nu e_\nu^j,
\qquad
w_\nu=c_\nu\xi^{e_\nu}.
}
$$

Every weight $w_\nu$ is nonzero.

#### Proof

For every integer exponent $e$,

$$
D(q^e)=eq^e.
$$

Inductively,

$$
D^j(q^e)=e^jq^e.
$$

Therefore

$$
D^jP(\xi)
=
\sum_\nu c_\nu e_\nu^j\xi^{e_\nu}.
$$

Since $c_\nu\ne0$ and $\xi\ne0$, each weight $w_\nu$ is nonzero. ∎

### Interpretation 1.5

The unknown support exponents $e_\nu$ are the nodes of a finite power-moment problem. The coefficients enter only through the nonzero weights

$$
w_\nu=c_\nu\xi^{e_\nu}.
$$

At a root of unity, the values $\xi^{e_\nu}$ depend only on exponent residues. The factors $e_\nu^j$, however, retain the full integer exponents. Higher Euler jets therefore remove the residue aliasing present at derivative order zero.

## 1.3 Euler order and ordinary local order

### Lemma 1.6 — Exponential-coordinate order equivalence

Let $P\in\Omega[q,q^{-1}]$, and let $\xi\ne0$. Put

$$
q=\xi e^x.
$$

Then

$$
D=\frac d{dx},
$$

and

$$
\boxed{
\operatorname{ord}_{q=\xi}P
=
\operatorname{ord}_{x=0}P(\xi e^x).
}
$$

Consequently, for every integer $r\ge0$,

$$
\boxed{
\operatorname{ord}_{q=\xi}P\ge r
\iff
D^jP(\xi)=0
\quad(0\le j<r).
}
$$

#### Proof

The chain rule gives

$$
\frac d{dx}P(\xi e^x)
=
\xi e^xP'(\xi e^x)
=
DP(\xi e^x).
$$

Also,

$$
q-\xi
=
\xi(e^x-1)
=
\xi x+O(x^2).
$$

Thus $q-\xi$ and $x$ differ by a unit in the local power-series ring, so they define the same vanishing order.

A formal power series has order at least $r$ exactly when its first $r$ derivatives vanish. Replacing derivatives in $x$ by Euler derivatives proves the criterion. ∎

---

# 2. Vandermonde independence

The sparse contact theorem is a direct consequence of the linear independence of distinct exponential frequencies.

## 2.1 Vandermonde determinant

### Classical Lemma 2.1 — Vandermonde determinant

Let

$$
\lambda_1,\ldots,\lambda_t
$$

be distinct elements of a characteristic-zero field. Then

$$
V(\lambda_1,\ldots,\lambda_t)
=
\begin{pmatrix}
1&1&\cdots&1\\
\lambda_1&\lambda_2&\cdots&\lambda_t\\
\vdots&\vdots&&\vdots\\
\lambda_1^{t-1}&\lambda_2^{t-1}&\cdots&\lambda_t^{t-1}
\end{pmatrix}
$$

has determinant

$$
\boxed{
\det V
=
\prod_{1\le\mu<\nu\le t}
(\lambda_\nu-\lambda_\mu).
}
$$

In particular, $V$ is invertible.

#### Proof

The determinant is an alternating polynomial in the $\lambda_i$. Therefore it is divisible by every difference $\lambda_\nu-\lambda_\mu$. Both sides have total degree

$$
0+1+\cdots+(t-1)=\binom t2.
$$

Hence the determinant equals a scalar multiple of the displayed product. The coefficient of

$$
\lambda_2\lambda_3^2\cdots\lambda_t^{t-1}
$$

is $1$ on both sides, so the scalar is $1$. Distinctness makes every factor nonzero. ∎

### Corollary 2.2 — Moment independence

Let $\lambda_1,\ldots,\lambda_t$ be distinct and let $u_1,\ldots,u_t$ lie in the same field. If

$$
\sum_{\nu=1}^{t}u_\nu\lambda_\nu^j=0
\qquad(0\le j<t),
$$

then

$$
\boxed{u_1=\cdots=u_t=0.}
$$

#### Proof

The displayed equations are the matrix equation

$$
V(\lambda_1,\ldots,\lambda_t)
(u_1,\ldots,u_t)^T=0.
$$

The Vandermonde matrix is invertible. ∎

## 2.2 Barycentric null vector

The extremal sparse collisions require one fewer equation than unknown weights. Their unique form is controlled by Lagrange interpolation.

Let

$$
A(z)=\prod_{\nu=1}^{t}(z-\lambda_\nu).
$$

Then

$$
A'(\lambda_\nu)
=
\prod_{\mu\ne\nu}(\lambda_\nu-\lambda_\mu)
\ne0.
$$

### Classical Lemma 2.3 — Barycentric moment identities

For distinct $\lambda_1,\ldots,\lambda_t$,

$$
\boxed{
\sum_{\nu=1}^{t}
\frac{\lambda_\nu^j}{A'(\lambda_\nu)}
=
\begin{cases}
0,&0\le j\le t-2,\\[1mm]
1,&j=t-1.
\end{cases}
}
$$

#### Proof

For every polynomial $f(z)$ of degree at most $t-1$, Lagrange interpolation gives

$$
f(z)
=
\sum_{\nu=1}^{t}
f(\lambda_\nu)
\frac{A(z)}{(z-\lambda_\nu)A'(\lambda_\nu)}.
$$

The polynomial

$$
\frac{A(z)}{z-\lambda_\nu}
$$

is monic of degree $t-1$. Therefore the coefficient of $z^{t-1}$ on the right side is

$$
\sum_{\nu=1}^{t}
\frac{f(\lambda_\nu)}{A'(\lambda_\nu)}.
$$

Take $f(z)=z^j$. If $j\le t-2$, the coefficient of $z^{t-1}$ on the left is zero. If $j=t-1$, it is one. ∎

### Corollary 2.4 — One-dimensional extremal kernel

The solutions of

$$
\sum_{\nu=1}^{t}u_\nu\lambda_\nu^j=0
\qquad(0\le j\le t-2)
$$

form a one-dimensional vector space. Every solution has the form

$$
\boxed{
u_\nu=
\frac{C}{A'(\lambda_\nu)}
}
$$

for a scalar $C$.

Moreover,

$$
\sum_{\nu=1}^{t}u_\nu\lambda_\nu^{t-1}=C.
$$

#### Proof

The coefficient matrix is the first $t-1$ rows of a Vandermonde matrix. It has rank $t-1$, so its kernel is one-dimensional.

Lemma 2.3 shows that the vector

$$
\left(\frac1{A'(\lambda_1)},\ldots,
\frac1{A'(\lambda_t)}\right)
$$

lies in that kernel and is nonzero. It therefore spans the kernel. The final identity is the $j=t-1$ case of Lemma 2.3. ∎

---

# 3. The Sharp Sparse Contact Theorem

## 3.1 Universal local bound

### Project Theorem 3.1 — Sharp Sparse Contact Theorem

Let

$$
0\ne P(q)=\sum_{\nu=1}^{t}c_\nu q^{e_\nu}
\in K[q,q^{-1}],
$$

where the exponents $e_\nu\in\mathbb Z$ are distinct. Let $\xi\ne0$ lie in a field extension of $K$. Then

$$
\boxed{
\operatorname{ord}_{q=\xi}P
\le t-1.
}
$$

Equivalently,

$$
\boxed{
D^jP(\xi)=0
\quad(0\le j<t)
\Longrightarrow
P=0.
}
$$

#### Proof

Assume

$$
\operatorname{ord}_{q=\xi}P\ge t.
$$

By Lemma 1.6,

$$
D^jP(\xi)=0
\qquad(0\le j<t).
$$

By Lemma 1.4,

$$
0
=
D^jP(\xi)
=
\sum_{\nu=1}^{t}w_\nu e_\nu^j,
\qquad
w_\nu=c_\nu\xi^{e_\nu}.
$$

The integers $e_\nu$ are distinct elements of a characteristic-zero field. Corollary 2.2 gives

$$
w_1=\cdots=w_t=0.
$$

But $c_\nu\ne0$ and $\xi\ne0$, so every $w_\nu\ne0$. This is a contradiction.

Therefore the local order is at most $t-1$. ∎

### Corollary 3.2 — Sparse zero certificate

Let $P$ be known a priori to satisfy

$$
\sigma(P)\le s.
$$

For any $\xi\ne0$,

$$
\boxed{
P=0
\iff
D^jP(\xi)=0
\quad(0\le j<s).
}
$$

#### Proof

The forward implication is immediate. If the first $s$ jets vanish and $P\ne0$, then

$$
\operatorname{ord}_{q=\xi}P\ge s,
$$

while Theorem 3.1 gives

$$
\operatorname{ord}_{q=\xi}P
\le
\sigma(P)-1
\le s-1.
$$

Contradiction. ∎

## 3.2 Extremal contact normal form

### Project Theorem 3.3 — Saturation of sparse contact

Let

$$
P(q)=\sum_{\nu=1}^{t}c_\nu q^{e_\nu}
\ne0,
$$

with distinct exponents, and fix $\xi\ne0$. Put

$$
A(z)=\prod_{\nu=1}^{t}(z-e_\nu).
$$

Then

$$
\operatorname{ord}_{q=\xi}P=t-1
$$

if and only if there exists $C\ne0$ such that

$$
\boxed{
c_\nu\xi^{e_\nu}
=
\frac{C}{A'(e_\nu)}
\qquad(1\le\nu\le t).
}
$$

In that case,

$$
\boxed{
D^{t-1}P(\xi)=C.
}
$$

#### Proof

The condition

$$
\operatorname{ord}_{q=\xi}P\ge t-1
$$

is equivalent to

$$
\sum_{\nu=1}^{t}w_\nu e_\nu^j=0
\qquad(0\le j\le t-2),
$$

where

$$
w_\nu=c_\nu\xi^{e_\nu}.
$$

By Corollary 2.4, these equations hold exactly when

$$
w_\nu=\frac{C}{A'(e_\nu)}
$$

for some scalar $C$.

Since every $w_\nu\ne0$, one has $C\ne0$. Corollary 2.4 then gives

$$
D^{t-1}P(\xi)
=
\sum_{\nu=1}^{t}w_\nu e_\nu^{t-1}
=C\ne0.
$$

Thus the order is exactly $t-1$.

Conversely, if the order is exactly $t-1$, the first $t-1$ moment equations hold, and the same kernel characterization gives the displayed form. ∎

### Interpretation 3.4

Extremal sparse contact is rigid. Once the exponent support and context $\xi$ are fixed, there is only a one-dimensional family of coefficient vectors attaining the maximal order $t-1$.

## 3.3 Sharpness in rational cyclotomic form

### Sharpness Theorem 3.5 — Universal attainment

For every integer $d\ge1$ and every $t\ge1$, the polynomial

$$
\boxed{
P_{d,t}(q)=(q^d-1)^{t-1}
}
$$

has exactly $t$ nonzero monomials and satisfies

$$
\boxed{
v_{\Phi_d}(P_{d,t})=t-1.
}
$$

At every primitive $d$-th root $\zeta_d$,

$$
\operatorname{ord}_{q=\zeta_d}P_{d,t}=t-1.
$$

#### Proof

The binomial expansion is

$$
(q^d-1)^{t-1}
=
\sum_{j=0}^{t-1}
(-1)^{t-1-j}
\binom{t-1}{j}q^{dj}.
$$

All $t$ binomial coefficients are nonzero in characteristic zero, and the exponents $0,d,\ldots,(t-1)d$ are distinct. Hence the sparsity is exactly $t$.

The polynomial $q^d-1$ contains $\Phi_d(q)$ exactly once. Therefore its $(t-1)$-st power contains $\Phi_d^{t-1}$ exactly. Equivalently, $q^d-1$ has a simple zero at every primitive $d$-th root, so its $(t-1)$-st power has local order $t-1$. ∎

Thus Theorem 3.1 is optimal for every cyclotomic context and every sparsity level.

---

# 4. Cyclotomic sparse contact

## 4.1 Cyclotomic multiplicity bound

### Project Theorem 4.1 — Sparse Cyclotomic Multiplicity Bound

Let

$$
0\ne P(q)\in\mathbb Q[q,q^{-1}]
$$

have sparsity $t$. Then for every $d\ge1$,

$$
\boxed{
v_{\Phi_d}(P)\le t-1.
}
$$

#### Proof

Let $\zeta_d$ be a primitive $d$-th root. Multiplication by a Laurent monomial does not change either sparsity or $\Phi_d$-valuation, so one may shift $P$ to an ordinary polynomial if desired.

For rational coefficients, the multiplicity of $\Phi_d$ equals the local zero multiplicity at $q=\zeta_d$. By Theorem 3.1, that local multiplicity is at most $t-1$. ∎

### Corollary 4.2 — Hybrid degree–sparsity bound

For every nonzero rational Laurent polynomial $P$,

$$
\boxed{
v_{\Phi_d}(P)
\le
\min\left(
\sigma(P)-1,
\left\lfloor
\frac{\operatorname{span}(P)}{\varphi(d)}
\right\rfloor
\right).
}
$$

#### Proof

The first bound is Theorem 4.1.

Part VIII gives

$$
\varphi(d)v_{\Phi_d}(P)
\le
\sum_e\varphi(e)v_{\Phi_e}(P)
\le
\operatorname{span}(P).
$$

Since the valuation is an integer, the second bound follows. ∎

### Interpretation 4.3

The two bounds control different regimes.

- For a dense polynomial of moderate degree, the span budget may be stronger.
- For a few-term polynomial with enormous exponent gaps, the sparse bound may be exponentially stronger in the bit length of the exponents.

## 4.2 Sparse collision depth

### Corollary 4.4 — Sparse collision bound

Let $F,G\in\mathbb Q[q,q^{-1}]$ be distinct. Then

$$
\boxed{
v_{\Phi_d}(F-G)
\le
\sigma(F-G)-1
\le
\sigma(F)+\sigma(G)-1.
}
$$

#### Proof

Apply Theorem 4.1 to the nonzero difference. Then use Lemma 1.2. ∎

### Caution 4.5 — No global sparsity-only contact budget

There is no bound depending only on sparsity for

$$
\sum_d\varphi(d)v_{\Phi_d}(P).
$$

Indeed,

$$
P(q)=q^N-1
$$

has sparsity $2$, but

$$
q^N-1=\prod_{d\mid N}\Phi_d(q),
$$

so

$$
\sum_d\varphi(d)v_{\Phi_d}(P)
=
\sum_{d\mid N}\varphi(d)
=N.
$$

Thus sparsity gives a sharp bound at each fixed context, not a degree-free bound on the total number or total weight of all cyclotomic contexts.

This distinction is essential.

---

# 5. Optimal sparse identity testing

## 5.1 Unequal sparsity bounds

### Project Theorem 5.1 — One-Context Sparse Identity Theorem

Let

$$
F,G\in K[q,q^{-1}]
$$

satisf

$$
\sigma(F)\le s,
\qquad
\sigma(G)\le t.
$$

Fix $\xi\ne0$ in a field extension of $K$. If

$$
\boxed{
D^jF(\xi)=D^jG(\xi)
\qquad(0\le j<s+t),
}
$$

then

$$
\boxed{F=G.}
$$

#### Proof

Put

$$
H=F-G.
$$

By Lemma 1.2,

$$
\sigma(H)
\le s+t.
$$

The jet agreement implies

$$
D^jH(\xi)=0
\qquad(0\le j<s+t),
$$

so

$$
\operatorname{ord}_{q=\xi}H\ge s+t.
$$

If $H\ne0$, Theorem 3.1 gives

$$
\operatorname{ord}_{q=\xi}H
\le
\sigma(H)-1
\le s+t-1,
$$

a contradiction. Therefore $H=0$. ∎

### Corollary 5.2 — Equal-sparsity identity test

If

$$
\sigma(F),\sigma(G)\le s
$$

and

$$
D^jF(\xi)=D^jG(\xi)
\qquad(0\le j<2s),
$$

then

$$
\boxed{F=G.}
$$

### Corollary 5.3 — Cyclotomic sparse identity test

Let $\zeta_d$ be primitive of order $d$. If

$$
\sigma(F)\le s,
\qquad
\sigma(G)\le t,
$$

and

$$
D^jF(\zeta_d)=D^jG(\zeta_d)
\qquad(0\le j<s+t),
$$

then

$$
\boxed{F=G.}
$$

Equivalently,

$$
\boxed{
v_{\Phi_d}(F-G)\ge s+t
\Longrightarrow
F=G.
}
$$

## 5.2 Optimality

### Sharpness Theorem 5.4 — Optimal jet threshold

Fix positive integers $s,t,d$. There exist rational Laurent polynomials $F,G$ with

$$
\sigma(F)=s,
\qquad
\sigma(G)=t,
\qquad
F\ne G,
$$

such that at every primitive $d$-th root $\zeta_d$,

$$
D^jF(\zeta_d)=D^jG(\zeta_d)
\qquad(0\le j<s+t-1).
$$

Thus the $s+t$ jets in Theorem 5.1 cannot be replaced universally by only $s+t-1$ jets.

#### Proof

Consider

$$
R(q)=(q^d-1)^{s+t-1}.
$$

By Theorem 3.5, $R$ has exactly $s+t$ nonzero monomials and vanishes to order exactly $s+t-1$ at every primitive $d$-th root.

Partition its support into two disjoint sets $I,J$ of sizes $s,t$. Write

$$
R(q)=\sum_{u\in I}a_uq^u+
\sum_{u\in J}a_uq^u.
$$

Define

$$
F(q)=\sum_{u\in I}a_uq^u,
\qquad
G(q)=-\sum_{u\in J}a_uq^u.
$$

Then

$$
F-G=R,
$$

and the disjoint supports give

$$
\sigma(F)=s,
\qquad
\sigma(G)=t.
$$

Since $R$ has local order $s+t-1$, its Euler derivatives of orders

$$
0,1,\ldots,s+t-2
$$

vanish, while the next derivative does not. Hence the stated jets of $F$ and $G$ agree, although $F\ne G$. ∎

### Interpretation 5.5

The sparse identity threshold is exact:

$$
\boxed{
\text{combined support size}
=
\text{minimum universal number of one-context jets}.
}
$$

Unlike the generic contact budget, the threshold contains no exponent-span term.

---

# 6. Hankel matrices of Euler moments

Sparse identity testing proves uniqueness. Exact reconstruction requires recovering the support and weights.

Let

$$
\mu_j=
\sum_{\nu=1}^{t}w_\nu\lambda_\nu^j,
$$

where

$$
\lambda_1,\ldots,\lambda_t
$$

are distinct and every $w_\nu\ne0$.

For sparse Laurent reconstruction, one takes

$$
\lambda_\nu=e_\nu,
\qquad
w_\nu=c_\nu\xi^{e_\nu}.
$$

## 6.1 Hankel factorization

### Definition 6.1 — Hankel moment matrix

For $r\ge1$, define

$$
\boxed{
H_r(\mu)
=
(\mu_{i+j})_{0\le i,j<r}.
}
$$

Define the rectangular Vandermonde matrix

$$
V_r=
(\lambda_\nu^i)_{
0\le i<r,
1\le\nu\le t},
$$

and the diagonal weight matrix

$$
W=\operatorname{diag}(w_1,\ldots,w_t).
$$

### Classical Lemma 6.2 — Hankel–Vandermonde factorization

For every $r\ge1$,

$$
\boxed{
H_r=V_rWV_r^T.
}
$$

#### Proof

The $(i,j)$-entry of the right side is

$$
\sum_{\nu=1}^{t}
\lambda_\nu^iw_\nu\lambda_\nu^j
=
\sum_{\nu=1}^{t}w_\nu\lambda_\nu^{i+j}
=
\mu_{i+j}.
$$

This is the $(i,j)$-entry of $H_r$. ∎

## 6.2 Exact rank

### Classical Theorem 6.3 — Hankel rank theorem

For every $r\ge t$,

$$
\boxed{
\operatorname{rank}H_r=t.
}
$$

For $r=t$,

$$
\boxed{
\det H_t
=
\left(\prod_{\nu=1}^{t}w_\nu\right)
\left(
\prod_{1\le\mu<\nu\le t}
(\lambda_\nu-\lambda_\mu)
\right)^2
\ne0.
}
$$

#### Proof

For $r=t$, the matrix $V_t$ is square Vandermonde. Lemma 6.2 gives

$$
H_t=V_tWV_t^T.
$$

Taking determinants,

$$
\det H_t
=
(\det V_t)^2\det W.
$$

The Vandermonde determinant is the displayed product, and

$$
\det W=\prod_\nu w_\nu\ne0.
$$

Thus $H_t$ is invertible.

Now let $r\ge t$. The factorization gives

$$
\operatorname{rank}H_r\le t.
$$

The upper-left $t\times t$ submatrix of $H_r$ is $H_t$, which is invertible. Therefore

$$
\operatorname{rank}H_r\ge t.
$$

Hence the rank equals $t$. ∎

### Corollary 6.4 — Sparsity from moments

Suppose an unknown moment sequence has at most $s$ distinct nodes with nonzero weights. Then

$$
\boxed{
t=\operatorname{rank}H_s.
}
$$

The matrix $H_s$ uses only the moments

$$
\mu_0,\mu_1,\ldots,\mu_{2s-2}.
$$

#### Proof

If the actual number of nodes is $t\le s$, apply Theorem 6.3 with $r=s$. ∎

### Caution 6.5 — Leading minors below the true rank

For $r<t$, the determinant of $H_r$ may vanish because of cancellation among the weights. Therefore one should determine the unknown sparsity from the rank of a sufficiently large Hankel matrix, not from the first vanishing leading principal minor.

The full matrix $H_s$ has rank exactly $t$ when $s\ge t$.

---

# 7. The annihilating polynomial

## 7.1 Moment recurrence

Define

$$
\boxed{
A(z)=\prod_{\nu=1}^{t}(z-\lambda_\nu)
=z^t+a_{t-1}z^{t-1}+\cdots+a_0.
}
$$

Set $a_t=1$.

### Classical Lemma 7.1 — Annihilating recurrence

For every $j\ge0$,

$$
\boxed{
\mu_{j+t}
+a_{t-1}\mu_{j+t-1}
+\cdots
+a_0\mu_j
=0.
}
$$

Equivalently,

$$
\boxed{
\sum_{k=0}^{t}a_k\mu_{j+k}=0.
}
$$

#### Proof

Using the moment representation,

$$
\begin{aligned}
\sum_{k=0}^{t}a_k\mu_{j+k}
&=
\sum_{k=0}^{t}a_k
\sum_{\nu=1}^{t}w_\nu\lambda_\nu^{j+k}\\
&=
\sum_{\nu=1}^{t}
w_\nu\lambda_\nu^j
\sum_{k=0}^{t}a_k\lambda_\nu^k\\
&=
\sum_{\nu=1}^{t}
w_\nu\lambda_\nu^jA(\lambda_\nu).
\end{aligned}
$$

Every $\lambda_\nu$ is a root of $A$, so the sum is zero. ∎

## 7.2 Recovery from the first $2t$ moments

### Classical Theorem 7.2 — Exact annihilator recovery

The coefficients $a_0,\ldots,a_{t-1}$ are the unique solution of

$$
\boxed{
H_t
\begin{pmatrix}
a_0\\
a_1\\
\vdots\\
a_{t-1}
\end{pmatrix}
=
-
\begin{pmatrix}
\mu_t\\
\mu_{t+1}\\
\vdots\\
\mu_{2t-1}
\end{pmatrix}.
}
$$

Thus the first $2t$ moments determine the monic annihilating polynomial $A(z)$ exactly.

#### Proof

The $j$-th recurrence for $j=0,1,\ldots,t-1$ is

$$
\sum_{k=0}^{t-1}a_k\mu_{j+k}
=-\mu_{j+t}.
$$

These equations form the displayed Hankel system. Theorem 6.3 shows that $H_t$ is invertible, so the solution is unique.

It remains to prove that the recovered monic polynomial is exactly $A$, rather than merely some recurrence polynomial.

Let

$$
B(z)=z^t+b_{t-1}z^{t-1}+\cdots+b_0
$$

be the monic polynomial obtained from the system. The recurrence equations imply

$$
\sum_{\nu=1}^{t}
w_\nu\lambda_\nu^jB(\lambda_\nu)=0
\qquad(0\le j<t).
$$

In matrix form,

$$
V_tW
\begin{pmatrix}
B(\lambda_1)\\
\vdots\\
B(\lambda_t)
\end{pmatrix}
=0.
$$

Both $V_t$ and $W$ are invertible. Hence

$$
B(\lambda_\nu)=0
\qquad(1\le\nu\le t).
$$

The monic degree-$t$ polynomial $B$ has the same $t$ distinct roots as $A$. Therefore $B=A$. ∎

## 7.3 Minimality

### Classical Corollary 7.3 — Minimal recurrence order

No nonzero recurrence of order less than $t$ annihilates the entire moment sequence.

#### Proof

Suppose a nonzero polynomial $B(z)$ of degree $r<t$ satisfied

$$
\sum_k b_k\mu_{j+k}=0
\qquad(j\ge0).
$$

Using $j=0,\ldots,t-1$ as in the proof of Theorem 7.2 gives

$$
V_tW
(B(\lambda_1),\ldots,B(\lambda_t))^T=0.
$$

Hence $B(\lambda_\nu)=0$ for all $t$ distinct nodes. A nonzero polynomial of degree less than $t$ cannot have $t$ distinct roots. ∎

---

# 8. Cyclotomic Prony reconstruction

## 8.1 Reconstruction with known sparsity

### Project Theorem 8.1 — One-Context Sparse Reconstruction Theorem

Let

$$
P(q)=\sum_{\nu=1}^{t}c_\nu q^{e_\nu}
\in K[q,q^{-1}],
$$

where the integer exponents $e_\nu$ are distinct and the coefficients are nonzero. Fix $\xi\ne0$ in an extension field $\Omega$.

Then the jet packet

$$
\boxed{
\bigl(P(\xi),DP(\xi),\ldots,D^{2t-1}P(\xi)\bigr)
}
$$

uniquely determines:

1. the exponent set $\{e_1,\ldots,e_t\}$;
2. the weights $w_\nu=c_\nu\xi^{e_\nu}$;
3. the coefficients $c_\nu$;
4. the Laurent polynomial $P$.

#### Proof

Set

$$
\mu_j=D^jP(\xi).
$$

By Lemma 1.4,

$$
\mu_j
=
\sum_{\nu=1}^{t}w_\nu e_\nu^j,
\qquad
w_\nu=c_\nu\xi^{e_\nu}\ne0.
$$

Apply Theorem 7.2 with nodes

$$
\lambda_\nu=e_\nu.
$$

The first $2t$ moments recover the monic polynomial

$$
A(z)=\prod_{\nu=1}^{t}(z-e_\nu).
$$

Its distinct roots are exactly the integer exponents $e_\nu$. Thus the support is recovered.

Next use the first $t$ moment equations

$$
\mu_j
=
\sum_{\nu=1}^{t}w_\nu e_\nu^j
\qquad(0\le j<t).
$$

Their coefficient matrix is the invertible Vandermonde matrix

$$
V(e_1,\ldots,e_t).
$$

Hence the weights $w_\nu$ are uniquely recovered.

Finally,

$$
\boxed{
c_\nu=w_\nu\xi^{-e_\nu}.
}
$$

Since $\xi\ne0$, this is well defined. Therefore all terms of $P$ are recovered uniquely. ∎

### Corollary 8.2 — Degree-free determination

The number of required jets is $2t$, independent of

$$
\max e_\nu-
\min e_\nu.
$$

The support exponents may have arbitrarily large magnitude.

## 8.2 Unknown sparsity bounded by $s$

### Algorithmic Theorem 8.3 — Adaptive sparse reconstruction

Suppose only that

$$
\sigma(P)\le s.
$$

Then the first $2s$ Euler jets at one nonzero context $\xi$ reconstruct $P$ exactly by the following procedure.

```text
input:
    bound s
    context xi != 0
    moments mu_j = D^j P(xi), 0 <= j < 2s

1. Form the s x s Hankel matrix
       H_s = (mu_{i+j})_{0 <= i,j < s}.

2. Compute
       t = rank(H_s).

3. If t = 0, return P = 0.

4. Form H_t and solve
       H_t * (a_0,...,a_{t-1})^T
       = -(mu_t,...,mu_{2t-1})^T.

5. Set
       A(z) = z^t + a_{t-1}z^{t-1} + ... + a_0.

6. Factor A exactly. Its distinct integer roots are
       e_1,...,e_t.

7. Solve the Vandermonde system
       mu_j = sum_nu w_nu e_nu^j,
       0 <= j < t.

8. Set
       c_nu = w_nu * xi^(-e_nu).

9. Return
       P(q) = sum_nu c_nu q^(e_nu).
```

The procedure is correct.

#### Proof

If $P=0$, every moment is zero and $H_s=0$, so the procedure returns zero.

Assume $P\ne0$, and let its actual sparsity be $t\le s$. Corollary 6.4 gives

$$
\operatorname{rank}H_s=t.
$$

Thus Step 2 recovers the actual sparsity.

The first $2s$ moments contain the first $2t$ moments, so Theorem 7.2 proves that Steps 4–5 recover the exact annihilating polynomial

$$
A(z)=\prod_{\nu=1}^{t}(z-e_\nu).
$$

Its roots are distinct integers because that is the structure assumed for $P$. Step 6 therefore recovers the support.

The Vandermonde matrix in Step 7 is invertible, so the weights are recovered uniquely. Step 8 inverts the definition

$$
w_\nu=c_\nu\xi^{e_\nu}.
$$

The returned polynomial has the original support and coefficients. ∎

## 8.3 Exact certificate format

A sparse reconstruction certificate may contain

```text
SparsePronyCertificate(
    context=xi,
    sparsity=t,
    annihilator=A(z),
    exponents=[e_1,...,e_t],
    weights=[w_1,...,w_t],
    coefficients=[c_1,...,c_t]
)
```

A verifier checks:

1. $A(z)=\prod_\nu(z-e_\nu)$;
2. the exponents are distinct integers;
3. $w_\nu=c_\nu\xi^{e_\nu}$;
4. for every requested $0\le j<2s$,
   $$
   \mu_j=\sum_\nu w_\nu e_\nu^j.
   $$

No expanded exponent interval is inspected.

---

# 9. Cyclotomic de-aliasing

Ordinary evaluation at a root of unity identifies exponents only modulo the context order. Euler jets recover the actual integers.

## 9.1 Zeroth-order aliasing

Let $\zeta_d$ be primitive. If

$$
e\equiv f\pmod d,
$$

then

$$
\zeta_d^e=\zeta_d^f.
$$

Therefore the value

$$
P(\zeta_d)
$$

cannot by itself distinguish support exponents in the same residue class.

## 9.2 Full de-aliasing theorem

### Project Theorem 9.1 — Cyclotomic Prony De-Aliasing Theorem

Let

$$
P(q)=\sum_{\nu=1}^{t}c_\nu q^{e_\nu}
\in\mathbb Q[q,q^{-1}],
$$

with distinct integer exponents. Fix any primitive root $\zeta_d$, including $d=1$.

Then the first $2t$ Euler jets

$$
\boxed{
P(\zeta_d),DP(\zeta_d),\ldots,D^{2t-1}P(\zeta_d)
}
$$

recover the full integer exponents $e_\nu$, not merely their residue classes modulo $d$.

#### Proof

Apply Theorem 8.1 with

$$
\xi=\zeta_d.
$$

The moment nodes are the integers $e_\nu$, while the root-of-unity factors occur only in the nonzero weights

$$
w_\nu=c_\nu\zeta_d^{e_\nu}.
$$

The annihilating polynomial is

$$
A(z)=\prod_\nu(z-e_\nu),
$$

so its roots are the complete exponents. No reduction modulo $d$ occurs in the node variable. ∎

### Corollary 9.2 — Same-residue separation

Even if all exponents satisfy

$$
e_1\equiv e_2\equiv\cdots\equiv e_t\pmod d,
$$

the first $2t$ Euler jets at $\zeta_d$ reconstruct them exactly.

### Interpretation 9.3

At a root of unity, the decomposition

$$
D^jP(\zeta_d)
=
\sum_\nu
\underbrace{c_\nu\zeta_d^{e_\nu}}_{\text{periodic weight}}
\underbrace{e_\nu^j}_{\text{nonperiodic moment node}}
$$

separates periodic context information from the integer support geometry. This is the exact mechanism by which differential cyclotomic data breaks ordinary root-of-unity aliasing.

## 9.3 Rationality check

### Corollary 9.4 — Rational coefficient verification

Suppose a jet packet in $\mathbb Q(\zeta_d)$ is claimed to come from a rational sparse Laurent polynomial. After reconstruction, the recovered values

$$
c_\nu=w_\nu\zeta_d^{-e_\nu}
$$

must lie in $\mathbb Q$.

This is both necessary and sufficient once the reconstructed moments match the packet.

#### Proof

Necessity follows from the definition of the original polynomial. Conversely, if the reconstructed exponents are integers, the reconstructed coefficients are rational, and their moment sequence agrees with the given packet, then the rational Laurent polynomial built from those terms realizes the packet. Uniqueness follows from Theorem 8.1. ∎

---

# 10. Complexity and exact arithmetic

## 10.1 Arithmetic workload

For a sparsity bound $s$, adaptive reconstruction uses:

1. one $s\times s$ Hankel rank computation;
2. one linear solve of size $t\le s$;
3. exact factorization of a degree-$t$ polynomial known to split into distinct integer roots;
4. one $t\times t$ Vandermonde solve;
5. exponentiation of $\xi$ to the recovered integer exponents.

The number of field operations is polynomial in $s$. It is independent of the exponent span.

## 10.2 Bit complexity and output sensitivity

The bit complexity also depends on:

- the bit lengths of the exponents;
- the heights of the coefficients and moments;
- the exact representation of the context field;
- the cost of splitting the annihilator and writing its integer roots.

No algorithm can avoid the cost of outputting very large exponents or coefficients.

Therefore the reconstruction theorem is degree-free in the number of jets and arithmetic dimensions, while its bit complexity remains output-sensitive.

## 10.3 Evaluation from a known sparse representation

If $P$ is already given sparsely, one jet is

$$
D^jP(\xi)
=
\sum_{\nu=1}^{t}c_\nu\xi^{e_\nu}e_\nu^j.
$$

For a fixed context and maximum order $R$, the weights

$$
w_\nu=c_\nu\xi^{e_\nu}
$$

are computed once. Successive powers $e_\nu^j$ may then be updated multiplicatively. The entire packet through order $R$ can be computed without expanding any missing exponent positions.

## 10.4 Characteristic-zero boundary

### Caution 10.1 — Failure in small characteristic

The characteristic-zero hypothesis is essential.

In characteristic $p$, distinct integer exponents may become equal as field elements:

$$
e_\mu\equiv e_\nu\pmod p.
$$

The Vandermonde determinant may then vanish even when the integer exponents are distinct. Euler derivatives may also lose information because powers of the exponent are taken in the coefficient field.

The present chapter is therefore stated over characteristic zero, which is the setting of the CCA monograph.

---

# 11. Reciprocal sparse Laurent polynomials

Part X used the dimension of the full reciprocal polynomial space. A reciprocal polynomial may also be sparse in inversion orbits.

## 11.1 Centered reciprocal form

### Definition 11.1 — Centered reciprocal Laurent polynomial

A Laurent polynomial $P\in K[q,q^{-1}]$ is **centered reciprocal** if

$$
\boxed{P(q^{-1})=P(q).}
$$

Every nonzero centered reciprocal Laurent polynomial has a unique representation

$$
\boxed{
P(q)
=
a_0+
\sum_{\nu=1}^{t}
a_\nu(q^{e_\nu}+q^{-e_\nu}),
}
$$

where

$$
0<e_1<\cdots<e_t,
\qquad
a_\nu\ne0,
$$

and the central coefficient $a_0$ may be zero.

### Definition 11.2 — Inversion-orbit sparsity

Define

$$
\boxed{
\rho(P)
=
t+\mathbf1_{a_0\ne0}.
}
$$

Thus $\rho(P)$ counts the nonzero support orbits under

$$
e\longmapsto-e.
$$

### Lemma 11.3 — Ordinary sparsity and orbit sparsity

For nonzero centered reciprocal $P$,

$$
\boxed{
\sigma(P)=2t+\mathbf1_{a_0\ne0},
}
$$

and

$$
\boxed{
\rho(P)=
\left\lceil\frac{\sigma(P)}2\right\rceil.
}
$$

#### Proof

Every nonzero exponent orbit contributes exactly two monomials, and the central orbit contributes one if present. The second formula follows immediately. ∎

## 11.2 Endpoint evenness

Fix

$$
\varepsilon\in\{1,-1\}
$$

and set

$$
q=\varepsilon e^x.
$$

### Lemma 11.4 — Endpoint even germ

For a centered reciprocal Laurent polynomial,

$$
\boxed{
P(\varepsilon e^{-x})
=
P(\varepsilon e^x).
}
$$

Hence

$$
\boxed{
D^{2j+1}P(\varepsilon)=0
\qquad(j\ge0).
}
$$

#### Proof

Because $\varepsilon^{-1}=\varepsilon$,

$$
(\varepsilon e^x)^{-1}
=
\varepsilon e^{-x}.
$$

Centered reciprocity gives

$$
P(\varepsilon e^{-x})
=P((\varepsilon e^x)^{-1})
=P(\varepsilon e^x).
$$

Thus the local exponential-coordinate germ is even. Every odd derivative at zero vanishes, and $D=d/dx$. ∎

## 11.3 Relation to the reciprocal core of Part X

Let $P(q)$ be reciprocal of formal degree $E$. Write

$$
E=2m+\delta,
\qquad
\delta\in\{0,1\}.
$$

Part X proves the unique factorization

$$
P(q)=q^m(1+q)^\delta Q(q+q^{-1}).
$$

### Corollary 11.5 — Centered sparse-core normalization

If $E=2m$, then

$$
\boxed{
q^{-m}P(q)=Q(q+q^{-1})
}
$$

is a centered reciprocal Laurent polynomial.

If $E=2m+1$, then $1+q$ divides $P$, and

$$
\boxed{
q^{-m}(1+q)^{-1}P(q)=Q(q+q^{-1})
}
$$

is a centered reciprocal Laurent polynomial.

Thus the endpoint orbit-sparsity theory below applies directly to the Part X reciprocal core whenever that core has a sparse Laurent expansion.

#### Proof

The displayed identities are the Reciprocal Core Theorem of Part X. Every polynomial in $q+q^{-1}$ is invariant under $q\leftrightarrow q^{-1}$, so the normalized core is centered reciprocal. ∎

## 11.4 Endpoint squared-exponent moments

### Lemma 11.6 — Reciprocal endpoint moment formula

Let

$$
P(q)=a_0+
\sum_{\nu=1}^{t}
a_\nu(q^{e_\nu}+q^{-e_\nu}).
$$

For $j\ge0$, define

$$
\nu_j^{(\varepsilon)}(P)
=
D^{2j}P(\varepsilon).
$$

Then

$$
\boxed{
\nu_j^{(\varepsilon)}(P)
=
\mathbf1_{j=0}a_0
+
2\sum_{\nu=1}^{t}
a_\nu\varepsilon^{e_\nu}e_\nu^{2j}.
}
$$

Equivalently, introduce nodes and weights

$$
\lambda_0=0,
\qquad b_0=a_0
$$

when $a_0\ne0$, and

$$
\lambda_\nu=e_\nu^2,
\qquad
b_\nu=2a_\nu\varepsilon^{e_\nu}
\qquad(1\le\nu\le t).
$$

Then

$$
\boxed{
\nu_j^{(\varepsilon)}(P)
=
\sum_{\lambda\text{-nodes}}b_\lambda\lambda^j,
}
$$

with the standard moment convention $0^0=1$.

#### Proof

At $q=\varepsilon e^x$,

$$
q^{e_\nu}+q^{-e_\nu}
=
\varepsilon^{e_\nu}
(e^{e_\nu x}+e^{-e_\nu x})
=
2\varepsilon^{e_\nu}\cosh(e_\nu x).
$$

The $2j$-th derivative at zero is

$$
2\varepsilon^{e_\nu}e_\nu^{2j}.
$$

The constant term contributes only when $j=0$. This gives the formula and its moment interpretation. ∎

---

# 12. Sharp reciprocal endpoint contact

## 12.1 Orbit-sparsity bound

### Project Theorem 12.1 — Reciprocal Endpoint Contact Theorem

Let $0\ne P\in K[q,q^{-1}]$ be centered reciprocal, and let

$$
\rho=\rho(P).
$$

For each endpoint $\varepsilon\in\{1,-1\}$,

$$
\boxed{
\operatorname{ord}_{q=\varepsilon}P
\le
2(\rho-1).
}
$$

Equivalently,

$$
\boxed{
D^{2j}P(\varepsilon)=0
\quad(0\le j<\rho)
\Longrightarrow
P=0.
}
$$

All odd endpoint Euler derivatives vanish automatically.

#### Proof

By Lemma 11.4, the local germ

$$
f(x)=P(\varepsilon e^x)
$$

is even. Therefore its nonzero local order, if positive, is an even integer $2r$. The condition

$$
\operatorname{ord}_{q=\varepsilon}P\ge2\rho
$$

would imply

$$
D^{2j}P(\varepsilon)=0
\qquad(0\le j<\rho).
$$

By Lemma 11.6, these are the first $\rho$ moments of $\rho$ distinct nodes:

- the node $0$, if $a_0\ne0$;
- the positive distinct nodes $e_\nu^2$.

All corresponding weights are nonzero. Corollary 2.2 therefore forces every weight to vanish, contradicting $P\ne0$.

Hence the order is less than $2\rho$. Since it is even, it is at most

$$
2\rho-2.
$$

This proves the theorem. ∎

### Corollary 12.2 — Endpoint cyclotomic bounds

For centered reciprocal $P\ne0$,

$$
\boxed{
v_{q-1}(P)\le2(\rho(P)-1),
}
$$

and

$$
\boxed{
v_{q+1}(P)\le2(\rho(P)-1).
}
$$

These improve the generic monomial-sparsity bound whenever the reciprocal pairing is substantial.

## 12.2 Extremal endpoint form

Let the squared-exponent nodes, including zero when present, be

$$
\lambda_1,\ldots,\lambda_\rho,
$$

with endpoint weights

$$
b_1,\ldots,b_\rho.
$$

Define

$$
B(z)=\prod_{i=1}^{\rho}(z-\lambda_i).
$$

### Project Theorem 12.3 — Saturation of reciprocal endpoint contact

One has

$$
\operatorname{ord}_{q=\varepsilon}P
=2(\rho-1)
$$

if and only if there exists $C\ne0$ such that

$$
\boxed{
b_i=
\frac{C}{B'(\lambda_i)}
\qquad(1\le i\le\rho).
}
$$

In that case,

$$
\boxed{
D^{2(\rho-1)}P(\varepsilon)=C.
}
$$

#### Proof

The order is at least $2(\rho-1)$ exactly when

$$
D^{2j}P(\varepsilon)=0
\qquad(0\le j\le\rho-2),
$$

because all odd derivatives vanish automatically.

By Lemma 11.6, these equations are

$$
\sum_{i=1}^{\rho}b_i\lambda_i^j=0
\qquad(0\le j\le\rho-2).
$$

Corollary 2.4 gives the displayed barycentric form and then gives

$$
\sum_i b_i\lambda_i^{\rho-1}=C.
$$

The left side is

$$
D^{2(\rho-1)}P(\varepsilon).
$$

Since $C\ne0$, the local order is exactly $2(\rho-1)$. The converse follows from the same argument. ∎

## 12.3 Sharpness

### Sharpness Theorem 12.4 — Endpoint attainment

For every $\rho\ge1$, define

$$
P_{+,\rho}(q)
=
(q+q^{-1}-2)^{\rho-1}
=
q^{-(\rho-1)}(q-1)^{2(\rho-1)},
$$

and

$$
P_{-,\rho}(q)
=
(q+q^{-1}+2)^{\rho-1}
=
q^{-(\rho-1)}(q+1)^{2(\rho-1)}.
$$

Then both are centered reciprocal Laurent polynomials with

$$
\boxed{
\rho(P_{+,\rho})
=
\rho(P_{-,\rho})
=
\rho,
}
$$

and

$$
\boxed{
\operatorname{ord}_{q=1}P_{+,\rho}
=2(\rho-1),
}
$$

$$
\boxed{
\operatorname{ord}_{q=-1}P_{-,\rho}
=2(\rho-1).
}
$$

#### Proof

The displayed factorizations follow from

$$
q+q^{-1}-2=q^{-1}(q-1)^2,
$$

and

$$
q+q^{-1}+2=q^{-1}(q+1)^2.
$$

Thus the local orders are exactly $2(\rho-1)$.

The polynomial

$$
q^{-(\rho-1)}(q\mp1)^{2(\rho-1)}
$$

has nonzero coefficients at every exponent

$$
-(\rho-1),-(\rho-2),\ldots,\rho-1.
$$

These exponents form $\rho-1$ nonzero inversion pairs plus the central exponent zero. Hence the inversion-orbit sparsity is $\rho$. ∎

The endpoint bound is therefore sharp for every orbit-sparsity level.

---

# 13. Reciprocal endpoint Prony reconstruction

## 13.1 Reconstruction theorem

### Project Theorem 13.1 — Endpoint Orbit-Prony Reconstruction

Let $P$ be a centered reciprocal Laurent polynomial with

$$
\rho(P)=\rho.
$$

Fix $\varepsilon\in\{1,-1\}$. Then the $2\rho$ independent even Euler jets

$$
\boxed{
D^{0}P(\varepsilon),
D^{2}P(\varepsilon),
\ldots,
D^{4\rho-2}P(\varepsilon)
}
$$

uniquely reconstruct $P$.

#### Proof

Define the endpoint moment sequence

$$
\nu_j=D^{2j}P(\varepsilon)
\qquad(j\ge0).
$$

By Lemma 11.6, this is a $\rho$-node power-moment sequence. Its nodes are distinct:

- possibly $0$;
- the positive squares $e_\nu^2$.

All weights are nonzero.

The packet through derivative order $4\rho-2$ is exactly the moment packet

$$
\nu_0,\nu_1,\ldots,\nu_{2\rho-1}.
$$

Apply Theorem 8.1 to this moment sequence. It recovers the annihilating polynomial

$$
A(z)=\prod_{\lambda\text{-nodes}}(z-\lambda),
$$

the nodes, and the endpoint weights.

A zero node corresponds to the central coefficient $a_0$. Every positive node is a perfect square

$$
\lambda=e^2
$$

of a unique positive integer exponent $e$. Thus the positive exponents are recovered.

For a nonzero node,

$$
b=2a\varepsilon^e,
$$

so

$$
\boxed{
a=\frac{b}{2\varepsilon^e}.
}
$$

For the zero node, its weight is exactly $a_0$. Therefore the centered reciprocal Laurent polynomial is reconstructed uniquely. ∎

### Corollary 13.2 — Unknown orbit sparsity

If only

$$
\rho(P)\le r
$$

is known, the first $2r$ even endpoint jets reconstruct $P$ adaptively by applying Algorithm 8.3 to the even-moment sequence

$$
\nu_j=D^{2j}P(\varepsilon).
$$

## 13.2 Endpoint identity testing

### Project Theorem 13.3 — Reciprocal Endpoint Identity Test

Let $F,G$ be centered reciprocal Laurent polynomials with

$$
\rho(F)\le r,
\qquad
\rho(G)\le s.
$$

Fix $\varepsilon\in\{1,-1\}$. If

$$
\boxed{
D^{2j}F(\varepsilon)
=
D^{2j}G(\varepsilon)
\qquad(0\le j<r+s),
}
$$

then

$$
\boxed{F=G.}
$$

The odd derivatives agree automatically because they vanish for both polynomials.

#### Proof

The difference

$$
H=F-G
$$

is centered reciprocal and satisfies

$$
\rho(H)
\le
\rho(F)+\rho(G)
\le r+s.
$$

The assumed even-jet agreement and automatic odd-jet vanishing imply

$$
\operatorname{ord}_{q=\varepsilon}H
\ge2(r+s).
$$

If $H\ne0$, Theorem 12.1 gives

$$
\operatorname{ord}_{q=\varepsilon}H
\le
2(\rho(H)-1)
\le
2(r+s-1),
$$

a contradiction. Therefore $H=0$. ∎

### Sharpness Theorem 13.4 — Optimal endpoint threshold

The $r+s$ even jets in Theorem 13.3 are universally optimal.

For every positive $r,s$, there exist centered reciprocal Laurent polynomials $F\ne G$ with

$$
\rho(F)=r,
\qquad
\rho(G)=s,
$$

whose even Euler jets agree at $q=1$ through index $r+s-2$. The same holds at $q=-1$.

#### Proof

Let

$$
R(q)=(q+q^{-1}-2)^{r+s-1}.
$$

By Theorem 12.4, $R$ has inversion-orbit sparsity $r+s$ and local order

$$
2(r+s-1)
$$

at $q=1$.

Write $R$ as a sum over its $r+s$ nonzero inversion orbits. Partition those orbits into two sets of sizes $r$ and $s$. Let $F$ be the sum over the first set and let $G$ be the negative of the sum over the second set. Then

$$
F-G=R,
$$

with

$$
\rho(F)=r,
\qquad
\rho(G)=s.
$$

Since $R$ has order $2(r+s-1)$, its even derivatives

$$
D^{2j}R(1)
$$

vanish for

$$
0\le j\le r+s-2,
$$

but the next even derivative is nonzero. Therefore the corresponding jets of $F$ and $G$ agree through exactly that range.

For $q=-1$, use

$$
(q+q^{-1}+2)^{r+s-1}.
$$

∎

---

# 14. Hybrid CCA certificates

The sparse and degree-based theories may be used simultaneously.

## 14.1 Local nonidentity and global identity

Suppose $F,G$ belong to a class with:

1. a known span bound $N$ for $F-G$;
2. a known sparsity bound $S$ for $F-G$.

At a context $d$, any nonzero difference satisfies

$$
\boxed{
v_{\Phi_d}(F-G)
\le
\min\left(
S-1,
\left\lfloor\frac N{\varphi(d)}\right\rfloor
\right).
}
$$

Thus either bound may terminate the comparison first.

### Algorithm 14.1 — Hybrid comparison engine

```text
input:
    expressions F, G
    difference sparsity bound S
    difference span bound N
    selected cyclotomic contexts d

for each selected context d:
    compare Euler jets successively

    if the first mismatch appears:
        return NONIDENTICAL

    if matched_depth >= S:
        return IDENTICAL by sparse contact rigidity

    accumulate generic contact weight
        weight += phi(d) * newly_matched_depth

    if weight > N:
        return IDENTICAL by global contact budget
```

### Algorithmic Theorem 14.2 — Correctness

Algorithm 14.1 returns a correct identity decision whenever the supplied sparsity and span bounds are valid.

#### Proof

A mismatch of any jet proves nonidentity immediately.

If one context reaches matched depth $S$, then

$$
v_{\Phi_d}(F-G)\ge S.
$$

A nonzero difference of sparsity at most $S$ would have valuation at most $S-1$ by Theorem 4.1. Therefore the difference is zero.

If the accumulated weighted contact exceeds $N$, Part VIII implies that a nonzero difference of span at most $N$ is impossible.

Thus every termination condition is sound. ∎

## 14.2 Reciprocal hybrid certificates

For centered reciprocal differences, the endpoint test may use orbit sparsity:

$$
D^{2j}(F-G)(\pm1)=0
\qquad(0\le j<R)
$$

with

$$
R\ge\rho(F-G)
$$

forces equality.

For reciprocal polynomials of known formal degree, Part X supplies the independent real-cyclotomic half-budget. A comparison engine may therefore combine three capacities:

$$
\boxed{
\begin{array}{c}
\text{monomial sparsity},\\
\text{reciprocal orbit sparsity},\\
\text{real-cyclotomic degree budget}.
\end{array}
}
$$

---

# 15. Differential cyclic-sieving consequences

Part V associates to a cyclic action $X$ its canonical orbit polynomial $O_X(q)$. A CSP polynomial $F(q)$ has local differential order

$$
\delta_d(F,X)
=
v_{\Phi_d}(F-O_X).
$$

## 15.1 Sparse differential rigidity

### Project Theorem 15.1 — Sparse Differential CSP Rigidity

Suppose

$$
\sigma(F)\le s,
\qquad
\sigma(O_X)\le t.
$$

If at one primitive $d$-th root $\zeta_d$,

$$
D^jF(\zeta_d)
=
D^jO_X(\zeta_d)
\qquad(0\le j<s+t),
$$

then

$$
\boxed{F=O_X.}
$$

Equivalently, unless $F$ is exactly the canonical orbit polynomial,

$$
\boxed{
\delta_d(F,X)
\le s+t-1.
}
$$

#### Proof

Apply Theorem 5.1 to $F$ and $O_X$. ∎

### Interpretation 15.2

For sparse graded lifts and sparse orbit polynomials, sufficiently high differential cyclic-sieving order at a single context forces the graded lift to be canonical globally.

This is stronger than ordinary CSP, which controls only values modulo $q^N-1$.

## 15.2 Orbit-polynomial sparsity caution

The canonical orbit polynomial

$$
O_X(q)=
\sum_{L\mid N}a_L[L]_{q^{N/L}}
$$

need not be sparse after expansion, even when the orbit-size profile has few nonzero entries. Therefore Theorem 15.1 applies when actual monomial sparsity is controlled. A separate theory is required to exploit sparsity in the number of orbit sizes rather than sparsity in the expanded polynomial.

---

# 16. Examples

## 16.1 Two-term local contact

Let

$$
P(q)=aq^u+bq^v,
\qquad
u\ne v.
$$

Theorem 3.1 gives

$$
\operatorname{ord}_{q=\xi}P\le1.
$$

A collision occurs exactly when

$$
a\xi^u+b\xi^v=0.
$$

If it occurs, then

$$
DP(\xi)
=a\xi^uu+b\xi^vv
=a\xi^u(u-v)\ne0.
$$

Thus every nonzero two-term collision is simple.

This is the sparse analogue of the simple-collision phenomenon in Gaussian families.

## 16.2 Extremal three-term collision

Let

$$
P(q)=(q^d-1)^2
=q^{2d}-2q^d+1.
$$

It has three terms and

$$
v_{\Phi_d}(P)=2.
$$

This saturates

$$
v_{\Phi_d}(P)\le3-1.
$$

## 16.3 Root-of-unity de-aliasing

Let

$$
P(q)=c_1q^{r}+c_2q^{r+d}.
$$

At a primitive $d$-th root $\zeta$,

$$
P(\zeta)
=\zeta^r(c_1+c_2),
$$

so the two exponents are indistinguishable at order zero.

The first Euler jet is

$$
DP(\zeta)
=
\zeta^r
\bigl(c_1r+c_2(r+d)\bigr).
$$

The moment nodes are $r$ and $r+d$. Four jets reconstruct both nodes and both coefficients exactly by Theorem 9.1.

## 16.4 Reciprocal endpoint saturation

For

$$
P(q)=(q+q^{-1}-2)^m,
$$

one has

$$
\rho(P)=m+1,
$$

and

$$
\operatorname{ord}_{q=1}P=2m=2(\rho(P)-1).
$$

The double local parameter at the reciprocal endpoint converts one unit of orbit-moment cancellation into two Euler orders.

---

# 17. Software primitives

A CCA sparse module should expose the following exact operations.

## 17.1 `sparse_euler_jets`

```text
input:
    sparse terms (e_nu, c_nu)
    exact nonzero context xi
    maximum order R

weights w_nu = c_nu * xi^(e_nu)
for j = 0,...,R:
    mu_j = sum_nu w_nu * e_nu^j
return [mu_0,...,mu_R]
```

## 17.2 `sparse_contact_bound`

```text
input: sparsity t
return t - 1
```

For a rational cyclotomic context, this is an exact upper bound on $v_{\Phi_d}$ for every nonzero $t$-sparse Laurent polynomial.

## 17.3 `sparse_prony_reconstruct`

```text
input:
    sparsity bound s
    context xi
    moments mu_0,...,mu_(2s-1)

compute t = rank(H_s)
if t == 0:
    return zero polynomial
recover annihilator A
factor A into distinct integer roots e_nu
solve Vandermonde for weights w_nu
set c_nu = w_nu * xi^(-e_nu)
return sparse polynomial
```

## 17.4 `reciprocal_endpoint_reconstruct`

```text
input:
    orbit-sparsity bound r
    endpoint epsilon in {1,-1}
    even jets nu_j = D^(2j)P(epsilon), 0 <= j < 2r

run sparse Prony on nodes lambda
for each node:
    if lambda == 0:
        recover central coefficient
    else:
        require lambda is a positive integer square
        e = sqrt(lambda)
        a = weight / (2 * epsilon^e)
return centered reciprocal Laurent polynomial
```

## 17.5 Verification failures

A reconstruction attempt must reject a packet if any of the following occurs:

1. the recovered annihilator does not split into distinct integer roots;
2. the recovered weights vanish;
3. reconstructed coefficients fail the required base-field condition;
4. recomputed moments do not match the complete input packet;
5. in the reciprocal endpoint algorithm, a nonzero node is not a positive integer square.

Such a failure means the packet does not belong to the claimed sparse class.

---

# 18. Theorem inventory

| Result | Statement | Status | Consequence |
|---|---|---|---|
| Euler moment formula | $D^jP(\xi)=\sum c_\nu\xi^{e_\nu}e_\nu^j$ | Lemma | Converts jets into exponent moments |
| Vandermonde independence | Distinct exponent nodes give an invertible moment matrix | Classical lemma | Finite sparse contact capacity |
| Barycentric null vector | Maximal moment cancellation has weights $C/A'(e_\nu)$ | Classical lemma | Classifies extremal sparse collisions |
| Sharp Sparse Contact Theorem | $\operatorname{ord}_{\xi}P\le\sigma(P)-1$ | Project theorem | Degree-free local collision bound |
| Sparse cyclotomic bound | $v_{\Phi_d}(P)\le\sigma(P)-1$ | Project theorem | Compressed cyclotomic multiplicity bound |
| Universal sharpness | $(q^d-1)^{t-1}$ attains depth $t-1$ with $t$ terms | Sharpness theorem | Bound is exact at every context |
| Sparse identity theorem | $s+t$ matching jets force equality | Project theorem | One-context compressed PIT |
| Optimal identity threshold | $s+t-1$ jets do not suffice universally | Sharpness theorem | Certificate length is exact |
| Hankel rank theorem | $\operatorname{rank}H_s=t$ for $s\ge t$ | Classical theorem | Recovers unknown sparsity |
| Annihilating recurrence | Moments satisfy the support polynomial recurrence | Classical lemma | Converts moments into support data |
| Annihilator recovery | First $2t$ moments recover $\prod(z-e_\nu)$ | Classical theorem | Exact exponent recovery |
| Cyclotomic Prony Reconstruction | First $2t$ jets at one context recover $P$ | Project theorem | Degree-free exact reconstruction |
| Cyclotomic de-aliasing | Root-of-unity jets recover full exponents, not residues | Project theorem | Differential contexts break periodic aliasing |
| Reciprocal endpoint contact | $\operatorname{ord}_{\pm1}P\le2(\rho(P)-1)$ | Project theorem | Sharp orbit-sparsity capacity |
| Endpoint sharpness | $(q+q^{-1}\mp2)^{\rho-1}$ saturates the endpoint bound | Sharpness theorem | Endpoint threshold is exact |
| Endpoint Orbit-Prony | $2\rho$ even jets reconstruct a reciprocal sparse polynomial | Project theorem | Sparse reciprocal reconstruction |
| Reciprocal endpoint identity | $r+s$ even jets force equality | Project theorem | Optimal endpoint certificate |
| Hybrid comparison engine | Use sparse, span, and reciprocal budgets together | Algorithmic theorem | Earliest valid termination |
| Sparse Differential CSP Rigidity | Deep one-context contact forces $F=O_X$ | Project theorem | Sparse higher-order CSP uniqueness |

---

# 19. Boundaries and open problems

## 19.1 Sparse monomials versus compressed dense terms

The present chapter solves sparse interpolation when each term is a monomial

$$
cq^e.
$$

A sum of a few Gaussian multinomials or compressed factorial quotients may have only a few compressed summands while each summand is exponentially dense. Its local jet sequence is not a finite power-moment sequence in the exponent variable.

The highest-value extension is therefore:

> Determine which sums of compressed $q$-factorial quotients admit finite-dimensional annihilating recurrences in their cyclotomic cumulant or jet sequences.

That problem would move the sparse breakthrough from monomial sparsity to genuine CCA expression sparsity.

## 19.2 Sparse real-cyclotomic reconstruction away from endpoints

Part X reconstructs reciprocal cores in the variable

$$
x=q+q^{-1}.
$$

The present endpoint theory uses squared exponents at $x=\pm2$. Develop an equally explicit sparse reconstruction theory at nonramified real-cyclotomic contexts

$$
\alpha_d=\zeta_d+\zeta_d^{-1}.
$$

The natural basis involves Chebyshev-type values and their derivatives rather than pure powers of $e^2$.

## 19.3 Orbit-profile sparsity

The canonical CSP polynomial may be dense but have only a few nonzero orbit sizes. Find a Prony-type transform whose nodes are orbit sizes $L\mid N$ and whose moments are canonical orbit jets.

A successful theorem would give identity and reconstruction bounds in terms of the number of orbit-size classes rather than the expanded support of $O_X(q)$.

## 19.4 Multi-context low-order reconstruction

A single context requires $2t$ jets for general reconstruction. Determine optimal tradeoffs between:

- the number of contexts;
- the jet depth at each context;
- arithmetic cost in the corresponding cyclotomic fields;
- exponent-range side information.

Unlike the degree budget, local sparse capacities cannot simply be added across contexts because a two-term polynomial such as $q^N-1$ may vanish at many roots of unity.

Additional arithmetic structure is required.

## 19.5 Modular and finite-characteristic variants

Classify the exact failures and possible repairs in characteristic $p$, where exponent nodes may collide modulo $p$. Hasse derivatives, lifted exponents, or mixed characteristic may recover part of the lost information.

## 19.6 Stability under approximate jets

The current theory is exact. Numerical Prony reconstruction can be ill-conditioned when exponent nodes are close relative to the chosen scaling or when coefficients nearly cancel.

Develop certified error bounds and interval versions for approximate complex root-of-unity evaluations without weakening the exact symbolic results.

## 19.7 Formal verification

Implement and machine-check:

1. the sparse contact theorem;
2. the barycentric saturation theorem;
3. Hankel rank and recurrence recovery;
4. integer-root support reconstruction;
5. reciprocal endpoint orbit recovery;
6. hybrid CCA certificates.

## 19.8 Structured exponent sets

If exponents belong to an arithmetic progression, a union of progressions, or another low-complexity set, the annihilator may have additional structure. Determine whether fewer than $2t$ jets suffice when that structure is known in advance.

---

# 20. Final statement

For a nonzero sparse Laurent polynomial

$$
P(q)=\sum_{\nu=1}^{t}c_\nu q^{e_\nu},
$$

the Euler jets at any nonzero context are the power moments

$$
\boxed{
D^jP(\xi)
=
\sum_{\nu=1}^{t}
(c_\nu\xi^{e_\nu})e_\nu^j.
}
$$

Vandermonde independence gives the sharp contact law

$$
\boxed{
\operatorname{ord}_{q=\xi}P
\le t-1.
}
$$

At a primitive $d$-th root,

$$
\boxed{
v_{\Phi_d}(P)
\le t-1.
}
$$

The bound is saturated by

$$
(q^d-1)^{t-1}.
$$

For two sparse polynomials,

$$
\boxed{
\sigma(F)\le s,
\quad
\sigma(G)\le t,
\quad
D^jF(\xi)=D^jG(\xi)
\ (0\le j<s+t)
\Longrightarrow
F=G.
}
$$

This threshold is optimal.

The first $2t$ jets recover the annihilating polynomial

$$
\boxed{
A(z)=\prod_{\nu=1}^{t}(z-e_\nu),
}
$$

then the exponent support, weights, and coefficients. At a root of unity, the method recovers full integer exponents rather than only residue classes.

For centered reciprocal sparse Laurent polynomials, endpoint symmetry replaces exponent nodes by squared-exponent nodes and gives

$$
\boxed{
\operatorname{ord}_{q=\pm1}P
\le
2(\rho(P)-1).
}
$$

The first $2\rho(P)$ independent even endpoint jets reconstruct the polynomial exactly.

Thus Parts VIII–XI now provide four complementary information laws:

$$
\boxed{
\begin{array}{c}
\text{Part VIII: global contact is bounded by span},\\[1mm]
\text{Part IX: generic jets reconstruct by degree},\\[1mm]
\text{Part X: reciprocity reconstructs at half dimension},\\[1mm]
\text{Part XI: sparse jets reconstruct independently of degree}.
\end{array}
}
$$

The expanded-degree barrier has therefore been broken for the first nontrivial compressed class: sparse Laurent polynomials and their reciprocal endpoint counterparts.
