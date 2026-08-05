# Cyclotomic Coefficient Arithmetic

## Part X — Reciprocal Cyclotomic Hermite Interpolation and Half-Budget Reconstruction

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete theorem chapter  
**Scope:** Reciprocal polynomial cores, real cyclotomic contexts, the lifting identity from real cyclotomic polynomials to ordinary cyclotomic polynomials, ramification at $q=\pm1$, reciprocal jet packets, local and global real-cyclotomic Hermite interpolation, optimal reconstruction, the reciprocal contact budget, half-budget finite determination, sharpness, Gaussian-multinomial consequences, and exact certificate design.

---

# 0. Purpose and relation to Parts VIII–IX

Part VIII proved the Global Cyclotomic Contact Budget

$$
\sum_{d\ge1}\varphi(d)v_{\Phi_d}(P)
\le
\operatorname{span}(P)
$$

and converted sufficiently many matching root-of-unity jets into a complete identity certificate.

Part IX proved the complementary Cyclotomic Hermite Interpolation Theorem:

$$
\mathbb Q[q]_{<B}
\cong
\bigoplus_{d\in\mathcal D}\mathbb Q(\zeta_d)^{r_d},
\qquad
B=\sum_{d\in\mathcal D}\varphi(d)r_d.
$$

That theorem treats the full polynomial space. Many principal CCA families, however, lie in the much smaller reciprocal subspace. A polynomial of degree at most $E$ has $E+1$ independent rational coefficients, while a reciprocal polynomial of formal degree $E$ has only

$$
\left\lfloor\frac E2\right\rfloor+1
$$

independent coefficients.

The present chapter incorporates that symmetry directly into the interpolation theory.

The fundamental substitution is

$$
\boxed{x=q+q^{-1}.}
$$

After removing a known monomial and, in odd degree, the mandatory factor $1+q$, every reciprocal polynomial becomes an ordinary polynomial in $x$. Primitive roots $\zeta_d$ and $\zeta_d^{-1}$ collapse to the same real-cyclotomic context

$$
\alpha_d=\zeta_d+\zeta_d^{-1}.
$$

For $d\ge3$, one local value now lies in the maximal real subfield

$$
K_d^+=\mathbb Q(\alpha_d),
\qquad
[K_d^+:\mathbb Q]=\frac{\varphi(d)}2.
$$

The main reconstruction theorem becomes

$$
\boxed{
\mathbb Q[x]_{<B^+}
\cong
\bigoplus_{d\in\mathcal D}(K_d^+)^{r_d},
\qquad
B^+=\sum_{d\in\mathcal D}\lambda_d r_d,
}
$$

where

$$
\lambda_d=
\begin{cases}
1,&d=1,2,\\[1mm]
\varphi(d)/2,&d\ge3.
\end{cases}
$$

Thus the correct interpolation weight for reciprocal data is the **real cyclotomic degree** $\lambda_d$, not the full cyclotomic degree $\varphi(d)$.

The global picture is

$$
\boxed{
\text{reciprocity}
\longrightarrow
\text{one-variable core in }x=q+q^{-1}
\longrightarrow
\text{real cyclotomic jets}
\longrightarrow
\text{optimal half-budget reconstruction}.
}
$$

The labels used below are:

- **Classical lemma:** standard algebraic input, proved here.
- **Project theorem:** a theorem established in this project.
- **Corollary:** a formal consequence.
- **Algorithmic theorem:** a correctness theorem for exact reconstruction.
- **Sharpness statement:** a theorem proving optimality.
- **Caution:** a distinction required for exact mathematics or software.

Throughout,

$$
D=q\frac d{dq}.
$$

---

# 1. Reciprocal polynomial spaces

## 1.1 Formal reciprocal degree

### Definition 1.1 — Reciprocal polynomial of formal degree $E$

A polynomial $P(q)\in\mathbb Q[q]$ is **reciprocal of formal degree $E$** if

$$
\boxed{P(q)=q^E P(q^{-1}).}
$$

The actual degree of $P$ may be smaller than $E$, provided the missing high coefficients are matched by missing low coefficients. For a nonzero polynomial with nonzero constant term, the natural formal degree is its ordinary degree.

Let

$$
\mathcal R_E
=
\{P\in\mathbb Q[q]:P(q)=q^E P(q^{-1})\}.
$$

This is a rational vector space.

### Lemma 1.2 — Coefficient symmetry

Write

$$
P(q)=\sum_{j=0}^{E}a_jq^j,
$$

allowing zero coefficients at the endpoints. Then

$$
P\in\mathcal R_E
\iff
\boxed{a_j=a_{E-j}\quad(0\le j\le E).}
$$

#### Proof

One has

$$
q^EP(q^{-1})
=
\sum_{j=0}^{E}a_jq^{E-j}.
$$

Comparison of the coefficient of $q^j$ gives $a_j=a_{E-j}$. The converse follows by reversing the same calculation. ∎

### Corollary 1.3 — Dimension of the reciprocal space

$$
\boxed{
\dim_{\mathbb Q}\mathcal R_E
=
\left\lfloor\frac E2\right\rfloor+1.
}
$$

#### Proof

The coefficients are determined by one representative from each pair

$$
\{j,E-j\}.
$$

There are $\lfloor E/2\rfloor+1$ such pairs, with the middle coefficient fixed by itself when $E$ is even. ∎

## 1.2 The reciprocal core

Write

$$
E=2m+\varepsilon,
\qquad
\varepsilon\in\{0,1\}.
$$

Define the known reciprocal prefactor

$$
\boxed{
A_E(q)=q^m(1+q)^\varepsilon.
}
$$

### Classical Lemma 1.4 — Symmetric Laurent polynomials

The fixed ring of the involution

$$
q\longmapsto q^{-1}
$$

on $\mathbb Q[q,q^{-1}]$ is

$$
\boxed{
\mathbb Q[q,q^{-1}]^{q\leftrightarrow q^{-1}}
=
\mathbb Q[q+q^{-1}].
}
$$

#### Proof

Put

$$
x=q+q^{-1}.
$$

Every polynomial in $x$ is invariant under inversion.

Conversely, let

$$
S(q)=a_0+\sum_{j=1}^{N}a_j(q^j+q^{-j})
$$

be an invariant Laurent polynomial. Define recursively

$$
T_0(x)=2,
\qquad
T_1(x)=x,
\qquad
T_{j+1}(x)=xT_j(x)-T_{j-1}(x).
$$

A direct induction gives

$$
T_j(q+q^{-1})=q^j+q^{-j}.
$$

Hence $S(q)$ is a polynomial in $x$. ∎

### Project Theorem 1.5 — Reciprocal Core Theorem

Let

$$
E=2m+\varepsilon,
\qquad
\varepsilon\in\{0,1\}.
$$

For every $P\in\mathcal R_E$, there exists a unique polynomial

$$
Q_P(x)\in\mathbb Q[x],
\qquad
\deg Q_P\le m,
$$

such that

$$
\boxed{
P(q)=A_E(q)Q_P(q+q^{-1}).
}
$$

Equivalently,

$$
\boxed{
P(q)=
\begin{cases}
q^mQ_P(q+q^{-1}),&E=2m,\\[1mm]
q^m(1+q)Q_P(q+q^{-1}),&E=2m+1.
\end{cases}
}
$$

#### Proof

### Even degree

Assume $E=2m$. Then

$$
S(q)=q^{-m}P(q)
$$

satisfies

$$
S(q^{-1})
=q^mP(q^{-1})
=q^mq^{-2m}P(q)
=q^{-m}P(q)
=S(q).
$$

Thus $S$ is an inversion-invariant Laurent polynomial. By Lemma 1.4,

$$
S(q)=Q_P(q+q^{-1})
$$

for a unique $Q_P\in\mathbb Q[x]$. Since $S$ has Laurent exponents between $-m$ and $m$, the polynomial $Q_P$ has degree at most $m$.

### Odd degree

Assume $E=2m+1$. Reciprocity at $q=-1$ gives

$$
P(-1)=(-1)^{2m+1}P(-1)=-P(-1),
$$

so

$$
P(-1)=0.
$$

Hence $1+q\mid P(q)$. Define

$$
S(q)=\frac{q^{-m}P(q)}{1+q}.
$$

Then

$$
\begin{aligned}
S(q^{-1})
&=
\frac{q^mP(q^{-1})}{1+q^{-1}}\\
&=
\frac{q^mq^{-(2m+1)}P(q)}{(1+q)/q}\\
&=
\frac{q^{-m}P(q)}{1+q}
=S(q).
\end{aligned}
$$

Again Lemma 1.4 gives

$$
S(q)=Q_P(q+q^{-1})
$$

with $\deg Q_P\le m$.

Uniqueness in both cases follows from injectivity of the substitution map

$$
\mathbb Q[x]\longrightarrow\mathbb Q[q,q^{-1}],
\qquad
Q(x)\longmapsto Q(q+q^{-1}).
$$

Indeed, a nonzero polynomial of degree $s$ maps to a Laurent polynomial with nonzero terms $q^s$ and $q^{-s}$. ∎

### Definition 1.6 — Reciprocal core map

Define

$$
\boxed{
\operatorname{Core}_E(P)=Q_P.
}
$$

Theorem 1.5 gives a vector-space isomorphism

$$
\boxed{
\operatorname{Core}_E:
\mathcal R_E
\overset\sim\longrightarrow
\mathbb Q[x]_{\le m}.
}
$$

---

# 2. Real cyclotomic contexts

Fix a primitive $d$-th root of unity $\zeta_d$. Define

$$
\boxed{
\alpha_d=\zeta_d+\zeta_d^{-1}.
}
$$

For $d=1,2$, this gives

$$
\alpha_1=2,
\qquad
\alpha_2=-2.
$$

### Definition 2.1 — Real cyclotomic field

Define

$$
\boxed{
K_d^+=\mathbb Q(\alpha_d).
}
$$

For $d=1,2$, one has $K_d^+=\mathbb Q$.

Let $\Psi_d(x)\in\mathbb Z[x]$ denote the minimal polynomial of $\alpha_d$ over $\mathbb Q$. Thus

$$
\Psi_1(x)=x-2,
\qquad
\Psi_2(x)=x+2.
$$

Define

$$
\boxed{
\lambda_d=\deg\Psi_d=[K_d^+:\mathbb Q].
}
$$

### Classical Lemma 2.2 — Degree of the real cyclotomic field

$$
\boxed{
\lambda_d=
\begin{cases}
1,&d=1,2,\\[1mm]
\varphi(d)/2,&d\ge3.
\end{cases}
}
$$

#### Proof

The cases $d=1,2$ are immediate.

Assume $d\ge3$. Complex conjugation acts nontrivially on

$$
K_d=\mathbb Q(\zeta_d),
$$

and its fixed field is the maximal real subfield

$$
K_d^+=\mathbb Q(\zeta_d+\zeta_d^{-1}).
$$

The extension $K_d/K_d^+$ has degree two because $\zeta_d$ satisfies

$$
t^2-\alpha_dt+1=0
$$

over $K_d^+$, while $\zeta_d\notin\mathbb R$. Therefore

$$
[K_d^+:\mathbb Q]
=
\frac{[K_d:\mathbb Q]}2
=
\frac{\varphi(d)}2.
$$

∎

### Lemma 2.3 — Pairwise distinction of real cyclotomic contexts

If $d\ne e$, then

$$
\boxed{\Psi_d\ne\Psi_e.}
$$

Consequently, the family $\{\Psi_d:d\ge1\}$ is pairwise coprime in $\mathbb Q[x]$.

#### Proof

Suppose $\Psi_d$ and $\Psi_e$ shared a root $\beta$. Then

$$
\beta=\xi+\xi^{-1}=\eta+\eta^{-1},
$$

where $\xi$ is a primitive $d$-th root and $\eta$ is a primitive $e$-th root.

Both $\xi$ and $\eta$ solve

$$
t^2-\beta t+1=0.
$$

That quadratic has only the roots $\xi$ and $\xi^{-1}$. Hence

$$
\eta\in\{\xi,\xi^{-1}\}.
$$

Therefore $\eta$ and $\xi$ have the same multiplicative order, so $d=e$, a contradiction.

Thus the irreducible polynomials $\Psi_d$ are distinct and hence pairwise coprime. ∎

---

# 3. The real-to-complex cyclotomic lifting identity

The substitution $x=q+q^{-1}$ identifies inverse pairs of primitive roots. The following theorem gives the exact polynomial relation.

Define the ramification index

$$
\boxed{
e_d=
\begin{cases}
2,&d=1,2,\\
1,&d\ge3.
\end{cases}
}
$$

### Project Theorem 3.1 — Real Cyclotomic Lifting Identity

For every $d\ge1$,

$$
\boxed{
q^{\lambda_d}\Psi_d(q+q^{-1})
=
\Phi_d(q)^{e_d}.
}
$$

Explicitly,

$$
\boxed{
q\bigl(q+q^{-1}-2\bigr)=(q-1)^2,
}
$$

$$
\boxed{
q\bigl(q+q^{-1}+2\bigr)=(q+1)^2,
}
$$

and, for $d\ge3$,

$$
\boxed{
q^{\varphi(d)/2}
\Psi_d(q+q^{-1})
=
\Phi_d(q).
}
$$

#### Proof

For $d=1$,

$$
q\Psi_1(q+q^{-1})
=q(q+q^{-1}-2)
=q^2+1-2q
=(q-1)^2.
$$

For $d=2$,

$$
q\Psi_2(q+q^{-1})
=q(q+q^{-1}+2)
=q^2+1+2q
=(q+1)^2.
$$

Now assume $d\ge3$, and put

$$
\lambda_d=\varphi(d)/2.
$$

The expression

$$
R_d(q)=q^{\lambda_d}\Psi_d(q+q^{-1})
$$

is a monic polynomial of degree $2\lambda_d=\varphi(d)$. Indeed, if $\Psi_d$ has degree $\lambda_d$, then multiplication by $q^{\lambda_d}$ clears all negative powers, and the highest term is $q^{2\lambda_d}$.

Let $\xi$ be any primitive $d$-th root. Then

$$
\xi+\xi^{-1}
$$

is a Galois conjugate of $\alpha_d$, so

$$
\Psi_d(\xi+\xi^{-1})=0.
$$

Hence every primitive $d$-th root is a root of $R_d$. There are $\varphi(d)$ such roots, and $R_d$ is monic of degree $\varphi(d)$. Therefore

$$
R_d(q)=\Phi_d(q).
$$

∎

### Corollary 3.2 — Valuation transfer to the reciprocal core

Let

$$
P(q)=A_E(q)Q(q+q^{-1})
\in\mathcal R_E,
\qquad
E=2m+\varepsilon.
$$

Then

$$
\boxed{
 v_{\Phi_d}(P)
 =
 e_d\,v_{\Psi_d}(Q)
 +\varepsilon\,\mathbf 1_{d=2}.
}
$$

Equivalently,

$$
\boxed{
\begin{aligned}
v_{q-1}(P)&=2v_{x-2}(Q),\\
v_{q+1}(P)&=\varepsilon+2v_{x+2}(Q),\\
v_{\Phi_d}(P)&=v_{\Psi_d}(Q),\qquad d\ge3.
\end{aligned}
}
$$

#### Proof

By Theorem 3.1,

$$
\Psi_d(q+q^{-1})
=q^{-\lambda_d}\Phi_d(q)^{e_d}.
$$

The Laurent monomial $q^{-\lambda_d}$ is a unit at every root of unity. Thus each factor $\Psi_d(x)$ in $Q(x)$ contributes exactly $e_d$ factors of $\Phi_d(q)$ after substitution.

The prefactor $q^m$ is a unit at every root of unity. The factor $(1+q)^\varepsilon$ contributes one additional $\Phi_2=q+1$ exactly when $\varepsilon=1$. ∎

### Corollary 3.3 — Reciprocity parity at the fixed contexts

For $P\in\mathcal R_E$,

$$
\boxed{v_{q-1}(P)\equiv0\pmod2,}
$$

and

$$
\boxed{v_{q+1}(P)\equiv E\pmod2.}
$$

#### Proof

Apply Corollary 3.2 and use $\varepsilon\equiv E\pmod2$. ∎

This recovers, in polynomial form, the parity phenomenon behind the binary even-germ theorem of Part IV.

---

# 4. Reciprocal jet packets

Let

$$
P\in\mathcal R_E,
\qquad
Q=\operatorname{Core}_E(P).
$$

### Definition 4.1 — Order-$r$ reciprocal cyclotomic jet

For $d\ge1$ and $r\ge1$, define

$$
\boxed{
J^+_{d,r}(P)
=
\bigl(
Q(\alpha_d),
Q'(\alpha_d),
\ldots,
Q^{(r-1)}(\alpha_d)
\bigr)
\in(K_d^+)^r.
}
$$

This is the jet of the reciprocal core in the real cyclotomic coordinate.

## 4.1 Nonfixed contexts

Assume $d\ge3$, and put

$$
u(q)=q-q^{-1}.
$$

At a primitive $d$-th root,

$$
u(\zeta_d)\ne0.
$$

Define the local derivation

$$
\boxed{
\nabla=\frac1{q-q^{-1}}D.
}
$$

### Lemma 4.2 — Core derivative identity

For every polynomial $Q(x)$,

$$
\boxed{
\nabla^jQ(q+q^{-1})
=Q^{(j)}(q+q^{-1})
}
$$

for every $j\ge0$ wherever $q-q^{-1}\ne0$.

#### Proof

Since

$$
D(q+q^{-1})=q-q^{-1},
$$

one has

$$
\nabla Q(q+q^{-1})=Q'(q+q^{-1}).
$$

Apply the same argument inductively to $Q',Q'',\ldots$. ∎

### Project Theorem 4.3 — Euler-jet/reciprocal-jet equivalence for $d\ge3$

Fix $E$, $d\ge3$, and $r\ge1$. For $P\in\mathcal R_E$, the ordinary Euler jet

$$
\bigl(P(\zeta_d),DP(\zeta_d),\ldots,D^{r-1}P(\zeta_d)\bigr)
$$

and the reciprocal jet

$$
J^+_{d,r}(P)
$$

determine each other through an invertible triangular transformation over $K_d$.

#### Proof

Write

$$
P(q)=A_E(q)S(q),
\qquad
S(q)=Q(q+q^{-1}).
$$

Since $d\ge3$, one has

$$
A_E(\zeta_d)\ne0.
$$

The Leibniz rule shows that the first $r$ Euler derivatives of $P$ and $S$ are related by a lower-triangular system whose diagonal entry at every order is $A_E(\zeta_d)\ne0$. Thus their jets determine each other.

Next,

$$
D=u(q)\nabla.
$$

Repeated application gives

$$
D^j
=
u(q)^j\nabla^j
+
\sum_{s<j}c_{j,s}(q)\nabla^s
$$

for suitable rational functions $c_{j,s}(q)$ regular at $\zeta_d$. Therefore the Euler derivatives of $S$ and the $\nabla$-derivatives of $S$ are related by a lower-triangular system with diagonal entries

$$
u(\zeta_d)^j\ne0.
$$

By Lemma 4.2,

$$
\nabla^jS(\zeta_d)=Q^{(j)}(\alpha_d).
$$

Both triangular transformations are invertible. ∎

### Interpretation 4.4

The ordinary jet lies in $K_d^r$, but reciprocity forces it into a constrained rational subspace isomorphic to

$$
(K_d^+)^r.
$$

Its true rational dimension is therefore

$$
r\lambda_d=r\frac{\varphi(d)}2,
$$

not $r\varphi(d)$.

---

# 5. Ramified contexts and endpoint even germs

At $q=\pm1$, the coordinate map

$$
q\longmapsto q+q^{-1}
$$

is ramified because

$$
q-q^{-1}=0.
$$

The correct local coordinate is quadratic.

Let

$$
E=2m+\varepsilon,
\qquad
P(q)=A_E(q)Q(q+q^{-1}).
$$

## 5.1 The context $q=1$

Set

$$
q=e^t.
$$

Then

$$
q+q^{-1}=2\cosh t.
$$

Define the normalized endpoint germ

$$
\boxed{
\mathcal E_{+,P}(t)
=
A_E(e^t)^{-1}P(e^t)
=
Q(2\cosh t).
}
$$

### Project Theorem 5.1 — Positive endpoint even-germ theorem

The germ $\mathcal E_{+,P}(t)$ is even:

$$
\boxed{
\mathcal E_{+,P}(-t)=\mathcal E_{+,P}(t).
}
$$

Moreover, for every $r\ge1$, the values

$$
Q(2),Q'(2),\ldots,Q^{(r-1)}(2)
$$

and the even Taylor coefficients of $\mathcal E_{+,P}$ through order $2r-2$ determine each other through an invertible triangular system over $\mathbb Q$.

#### Proof

Evenness follows from $\cosh(-t)=\cosh t$.

Near $t=0$,

$$
2\cosh t-2=t^2+O(t^4).
$$

Expand $Q$ at $x=2$:

$$
Q(x)
=
\sum_{j\ge0}
\frac{Q^{(j)}(2)}{j!}(x-2)^j.
$$

After substituting $x=2\cosh t$, the term indexed by $j$ begins with

$$
\frac{Q^{(j)}(2)}{j!}t^{2j}.
$$

Hence the coefficient of $t^{2j}$ depends only on

$$
Q(2),Q'(2),\ldots,Q^{(j)}(2),
$$

with nonzero diagonal coefficient $1/j!$. This is an invertible triangular system. ∎

## 5.2 The context $q=-1$

Set

$$
q=-e^t.
$$

Then

$$
q+q^{-1}=-2\cosh t.
$$

After cancelling the known factor $(1+q)^\varepsilon$, define

$$
\boxed{
\mathcal E_{-,P}(t)
=
A_E(-e^t)^{-1}P(-e^t)
=
Q(-2\cosh t).
}
$$

The quotient is interpreted after the exact polynomial cancellation guaranteed by Theorem 1.5 when $\varepsilon=1$.

### Project Theorem 5.2 — Negative endpoint even-germ theorem

The germ $\mathcal E_{-,P}(t)$ is even:

$$
\boxed{
\mathcal E_{-,P}(-t)=\mathcal E_{-,P}(t).
}
$$

For every $r\ge1$, the values

$$
Q(-2),Q'(-2),\ldots,Q^{(r-1)}(-2)
$$

and the even Taylor coefficients of $\mathcal E_{-,P}$ through order $2r-2$ determine each other through an invertible triangular system over $\mathbb Q$.

#### Proof

Again, evenness follows from evenness of $\cosh t$.

Near zero,

$$
-2\cosh t+2=-t^2+O(t^4).
$$

Expand $Q$ at $-2$:

$$
Q(x)
=
\sum_{j\ge0}
\frac{Q^{(j)}(-2)}{j!}(x+2)^j.
$$

The term indexed by $j$ begins after substitution with

$$
\frac{(-1)^jQ^{(j)}(-2)}{j!}t^{2j}.
$$

The resulting system is triangular with nonzero diagonal coefficients $(-1)^j/j!$. ∎

### Corollary 5.3 — Two-for-one endpoint contact

Let $P\in\mathcal R_E$ be nonzero, with core $Q$. Then

$$
\boxed{
(x-2)^r\mid Q
\iff
(q-1)^{2r}\mid P,
}
$$

and

$$
\boxed{
(x+2)^r\mid Q
\iff
(q+1)^{2r+\varepsilon}\mid P.
}
$$

#### Proof

This is Corollary 3.2 for $d=1,2$. ∎

Thus one order of real-coordinate contact at an endpoint corresponds to two orders of ordinary root contact. At $q=-1$, odd reciprocal degree contributes one additional mandatory factor.

---

# 6. The Local Real-Cyclotomic Hermite Isomorphism

Fix $d\ge1$ and $r\ge1$.

### Definition 6.1 — Local real-cyclotomic jet map

For $Q\in\mathbb Q[x]$, define

$$
\boxed{
\mathcal J^+_{d,r}(Q)
=
\bigl(
Q(\alpha_d),
Q'(\alpha_d),
\ldots,
Q^{(r-1)}(\alpha_d)
\bigr)
\in(K_d^+)^r.
}
$$

### Lemma 6.2 — Kernel of the real jet map

For $Q\in\mathbb Q[x]$,

$$
\boxed{
\mathcal J^+_{d,r}(Q)=0
\iff
\Psi_d(x)^r\mid Q(x).
}
$$

#### Proof

If $\Psi_d^r\mid Q$, then $Q$ has a zero of multiplicity at least $r$ at every root of $\Psi_d$, including $\alpha_d$. Hence the first $r$ derivatives vanish.

Conversely, suppose

$$
Q^{(j)}(\alpha_d)=0
\qquad(0\le j<r).
$$

Then $\alpha_d$ is a root of multiplicity at least $r$. Because $Q$ has rational coefficients, every Galois conjugate of $\alpha_d$ is a root with the same multiplicity. Therefore every root of the irreducible polynomial $\Psi_d$ occurs in $Q$ with multiplicity at least $r$, so

$$
\Psi_d^r\mid Q.
$$

∎

### Project Theorem 6.3 — Local Real-Cyclotomic Hermite Isomorphism

The map

$$
\boxed{
\mathbb Q[x]/(\Psi_d^r)
\longrightarrow
(K_d^+)^r,
\qquad
[Q]\longmapsto\mathcal J^+_{d,r}(Q),
}
$$

is a $\mathbb Q$-linear isomorphism.

#### Proof

Lemma 6.2 shows that the map is well defined and injective.

The source has rational dimension

$$
\deg(\Psi_d^r)=r\lambda_d.
$$

The target has rational dimension

$$
r[K_d^+:\mathbb Q]=r\lambda_d.
$$

An injective map between finite-dimensional vector spaces of equal dimension is bijective. ∎

### Corollary 6.4 — Arbitrary local reciprocal-jet realization

For every packet

$$
(a_0,\ldots,a_{r-1})\in(K_d^+)^r,
$$

there exists a unique polynomial

$$
Q(x)\in\mathbb Q[x],
\qquad
\deg Q<r\lambda_d,
$$

such that

$$
\boxed{
Q^{(j)}(\alpha_d)=a_j
\qquad(0\le j<r).
}
$$

#### Proof

Theorem 6.3 gives a unique residue class modulo $\Psi_d^r$. Choose its unique representative of degree less than $r\lambda_d$. ∎

### Interpretation 6.5 — Exact local information dimension

An order-$r$ reciprocal jet at context $d$ contains exactly

$$
\boxed{r\lambda_d}
$$

independent rational scalars.

For $d\ge3$, this is

$$
\boxed{r\varphi(d)/2,}
$$

exactly half the dimension of an unrestricted order-$r$ cyclotomic jet.

---

# 7. Constructive local reconstruction

The local isomorphism has a triangular constructive form.

### Classical Lemma 7.1 — Unique $\Psi_d$-adic normal form

Every class in

$$
\mathbb Q[x]/(\Psi_d^r)
$$

has a unique representative of the form

$$
\boxed{
B_0(x)+B_1(x)\Psi_d(x)+\cdots+B_{r-1}(x)\Psi_d(x)^{r-1},
}
$$

where

$$
\deg B_j<\lambda_d.
$$

#### Proof

Repeated Euclidean division by $\Psi_d$ gives existence. If two such forms represented the same class, reducing their difference successively modulo $\Psi_d$ would force

$$
B_0=B_1=\cdots=B_{r-1}=0.
$$

∎

Let

$$
c_d=\Psi_d'(\alpha_d).
$$

Since $\Psi_d$ is separable in characteristic zero,

$$
c_d\ne0.
$$

### Lemma 7.2 — First visible derivative of a real cyclotomic power

For $j\ge0$,

$$
\frac{d^s}{dx^s}\Psi_d(x)^j\bigg|_{x=\alpha_d}=0
\qquad(0\le s<j),
$$

and

$$
\boxed{
\frac{d^j}{dx^j}\Psi_d(x)^j\bigg|_{x=\alpha_d}
=j!c_d^j.
}
$$

#### Proof

Near $x=\alpha_d$,

$$
\Psi_d(x)=c_d(x-\alpha_d)+O((x-\alpha_d)^2).
$$

Therefore

$$
\Psi_d(x)^j
=c_d^j(x-\alpha_d)^j+O((x-\alpha_d)^{j+1}).
$$

The derivative statement follows. ∎

### Proposition 7.3 — Triangular real-cyclotomic reconstruction

Let

$$
Q(x)
\equiv
\sum_{j=0}^{r-1}B_j(x)\Psi_d(x)^j
\pmod{\Psi_d^r},
\qquad
\deg B_j<\lambda_d.
$$

Then the jet values

$$
Q(\alpha_d),Q'(\alpha_d),\ldots,Q^{(r-1)}(\alpha_d)
$$

determine

$$
B_0(\alpha_d),B_1(\alpha_d),\ldots,B_{r-1}(\alpha_d)
$$

successively through a triangular system with diagonal entries

$$
0!c_d^0,
1!c_d^1,
\ldots,
(r-1)!c_d^{r-1}.
$$

#### Proof

At derivative order $s$, every term with index $j>s$ vanishes by Lemma 7.2. The contribution involving $B_s(\alpha_d)$ is

$$
B_s(\alpha_d)
\frac{d^s}{dx^s}\Psi_d(x)^s\bigg|_{x=\alpha_d}
=
B_s(\alpha_d)s!c_d^s.
$$

All other contributions at order $s$ depend only on the previously determined values

$$
B_0(\alpha_d),\ldots,B_{s-1}(\alpha_d).
$$

The diagonal scalar is nonzero, so the system can be solved recursively. ∎

### Algorithmic Corollary 7.4 — Exact local reciprocal reconstruction

An order-$r$ reciprocal jet is converted to the unique residue modulo $\Psi_d^r$ by:

1. solving the triangular system of Proposition 7.3;
2. expressing each $B_j(\alpha_d)\in K_d^+$ by its unique polynomial representative of degree less than $\lambda_d$;
3. returning
   $$
   \sum_{j=0}^{r-1}B_j(x)\Psi_d(x)^j.
   $$

No complex cyclotomic-field arithmetic is required.

---

# 8. Global Reciprocal Cyclotomic Hermite Interpolation

Let $\mathcal D$ be a finite set of positive integers. For each $d\in\mathcal D$, choose a depth

$$
r_d\ge1.
$$

Define the real-cyclotomic modulus

$$
\boxed{
M^+_{\mathcal D,\mathbf r}(x)
=
\prod_{d\in\mathcal D}\Psi_d(x)^{r_d}.
}
$$

Its degree is

$$
\boxed{
B^+(\mathcal D,\mathbf r)
=
\sum_{d\in\mathcal D}\lambda_dr_d.
}
$$

### Classical Lemma 8.1 — Real-cyclotomic Chinese remainder theorem

The natural map

$$
\boxed{
\mathbb Q[x]/(M^+_{\mathcal D,\mathbf r})
\longrightarrow
\bigoplus_{d\in\mathcal D}
\mathbb Q[x]/(\Psi_d^{r_d})
}
$$

is a ring isomorphism.

#### Proof

By Lemma 2.3, the polynomials $\Psi_d$ are pairwise coprime. Their powers remain pairwise coprime, so the ordinary Chinese remainder theorem applies. ∎

### Project Theorem 8.2 — Global Real-Cyclotomic Hermite Isomorphism

The map

$$
\boxed{
\mathbb Q[x]/(M^+_{\mathcal D,\mathbf r})
\longrightarrow
\bigoplus_{d\in\mathcal D}(K_d^+)^{r_d},
}
$$

sending a core polynomial to all selected derivative packets is a $\mathbb Q$-linear isomorphism.

#### Proof

Lemma 8.1 decomposes the source into the direct sum of the local residue rings. Theorem 6.3 identifies each local residue ring with $(K_d^+)^{r_d}$. Taking the direct sum proves the result. ∎

### Project Theorem 8.3 — Reciprocal Cyclotomic Hermite Interpolation Theorem

For every family of target packets

$$
\mathbf a_d
=
(a_{d,0},\ldots,a_{d,r_d-1})
\in(K_d^+)^{r_d},
\qquad d\in\mathcal D,
$$

there exists a unique polynomial

$$
Q(x)\in\mathbb Q[x]
$$

with

$$
\boxed{
\deg Q<B^+(\mathcal D,\mathbf r)
}
$$

such that

$$
\boxed{
Q^{(j)}(\alpha_d)=a_{d,j}
\qquad
(d\in\mathcal D,
\ 0\le j<r_d).
}
$$

#### Proof

Theorem 8.2 gives a unique residue class modulo the monic polynomial $M^+_{\mathcal D,\mathbf r}$. Every residue class has a unique representative of degree less than its degree $B^+$. ∎

### Corollary 8.4 — Canonical reciprocal reconstruction

Fix a parity $\varepsilon\in\{0,1\}$, and put

$$
E_B=2(B^+-1)+\varepsilon.
$$

Every reciprocal jet packet of total real weight $B^+$ is realized by a unique reciprocal polynomial

$$
P(q)=q^{B^+-1}(1+q)^\varepsilon Q(q+q^{-1})
$$

of formal degree at most $E_B$.

#### Proof

Theorem 8.3 gives the unique core $Q$ of degree at most $B^+-1$. Apply the Reciprocal Core Theorem. ∎

### Corollary 8.5 — Fixed-degree reciprocal isomorphism

Let

$$
E=2m+\varepsilon.
$$

If

$$
\boxed{B^+(\mathcal D,\mathbf r)=m+1,}
$$

then the reciprocal jet map is a rational vector-space isomorphism

$$
\boxed{
\mathcal R_E
\cong
\bigoplus_{d\in\mathcal D}(K_d^+)^{r_d}.
}
$$

#### Proof

The core map identifies $\mathcal R_E$ with $\mathbb Q[x]_{\le m}=\mathbb Q[x]_{<m+1}$. Apply Theorem 8.3 with $B^+=m+1$. ∎

---

# 9. Explicit global reconstruction

For each $d\in\mathcal D$, define

$$
M_d^+(x)
=
\frac{M^+_{\mathcal D,\mathbf r}(x)}{\Psi_d(x)^{r_d}}.
$$

Because $M_d^+$ is coprime to $\Psi_d^{r_d}$, choose

$$
U_d(x)M_d^+(x)
\equiv1
\pmod{\Psi_d(x)^{r_d}}.
$$

Define the CRT idempotent

$$
\boxed{
E_d^+(x)
=U_d(x)M_d^+(x)
\pmod{M^+_{\mathcal D,\mathbf r}(x)}.
}
$$

Then

$$
E_d^+\equiv1\pmod{\Psi_d^{r_d}}
$$

and

$$
E_d^+\equiv0\pmod{\Psi_e^{r_e}}
\qquad(e\ne d).
$$

### Algorithmic Theorem 9.1 — Explicit reciprocal reconstruction

For each $d$, let $H_d(x)$ be the unique local representative of degree less than $r_d\lambda_d$ having the prescribed order-$r_d$ jet at $\alpha_d$. Then the unique global core is

$$
\boxed{
Q(x)
\equiv
\sum_{d\in\mathcal D}H_d(x)E_d^+(x)
\pmod{M^+_{\mathcal D,\mathbf r}(x)},
}
$$

chosen as the representative of degree less than $B^+$.

The corresponding reciprocal polynomial of parity $\varepsilon$ is

$$
\boxed{
P(q)=q^{B^+-1}(1+q)^\varepsilon Q(q+q^{-1}).
}
$$

#### Proof

Modulo $\Psi_e^{r_e}$, all summands with $d\ne e$ vanish, while the $e$-summand reduces to $H_e$. Hence the reconstructed core has every prescribed local residue and therefore every prescribed local jet. Uniqueness follows from Theorem 8.3. The final formula is the reciprocal lift from Theorem 1.5. ∎

## 9.1 Pseudocode

```text
input:
    contexts d in D
    depths r_d
    exact reciprocal jets a[d][0:r_d]
    reciprocal parity epsilon in {0,1}

for each d in D:
    H_d = real_jet_to_residue(d, r_d, a[d])

M_plus = product(Psi_d(x)^r_d for d in D)
Q = 0

for each d in D:
    M_d = M_plus / Psi_d(x)^r_d
    U_d = inverse_mod(M_d, Psi_d(x)^r_d)
    E_d = U_d * M_d
    Q += H_d * E_d

Q = remainder(Q, M_plus)
P(q) = q^(deg_bound) * (1+q)^epsilon * Q(q+q^(-1))
return Q, P
```

The core $Q$ is often the preferable output: it has about half the degree and lives over the real coordinate.

---

# 10. The Reciprocal Cyclotomic Contact Budget

The contact budget of Part VIII has a sharper reciprocal form after passing to the core.

Let

$$
0\ne P\in\mathcal R_E,
\qquad
E=2m+\varepsilon,
\qquad
Q=\operatorname{Core}_E(P).
$$

### Definition 10.1 — Real-cyclotomic contact mass

Define

$$
\boxed{
\mathfrak C^+(P)
=
\sum_{d\ge1}\lambda_dv_{\Psi_d}(Q).
}
$$

Only finitely many terms are nonzero.

### Project Theorem 10.2 — Reciprocal Cyclotomic Contact Budget

For every nonzero reciprocal polynomial of formal degree $E=2m+\varepsilon$,

$$
\boxed{
\mathfrak C^+(P)
\le
\deg Q
\le
m.
}
$$

Equivalently,

$$
\boxed{
\frac{v_{q-1}(P)}2
+
\frac{v_{q+1}(P)-\varepsilon}2
+
\sum_{d\ge3}
\frac{\varphi(d)}2v_{\Phi_d}(P)
\le
m.
}
$$

#### Proof

The polynomials $\Psi_d$ are pairwise coprime. Hence

$$
\prod_{d\ge1}\Psi_d(x)^{v_{\Psi_d}(Q)}
\mid Q(x).
$$

Taking degrees gives

$$
\sum_{d\ge1}\lambda_dv_{\Psi_d}(Q)
\le
\deg Q.
$$

The Reciprocal Core Theorem gives $\deg Q\le m$.

The raw cyclotomic form follows from Corollary 3.2:

$$
v_{\Psi_1}(Q)=\frac{v_{q-1}(P)}2,
$$

$$
v_{\Psi_2}(Q)=\frac{v_{q+1}(P)-\varepsilon}2,
$$

and, for $d\ge3$,

$$
v_{\Psi_d}(Q)=v_{\Phi_d}(P),
\qquad
\lambda_d=\frac{\varphi(d)}2.
$$

∎

### Project Theorem 10.3 — Saturation of the reciprocal budget

Equality

$$
\mathfrak C^+(P)=\deg Q
$$

holds if and only if

$$
\boxed{
Q(x)=c\prod_{d\in S}\Psi_d(x)^{a_d}
}
$$

for some finite set $S$, positive integers $a_d$, and $c\in\mathbb Q^\times$.

Equivalently,

$$
\boxed{
P(q)=
A_E(q)c
\prod_{d\in S}
\Psi_d(q+q^{-1})^{a_d}.
}
$$

#### Proof

Factor

$$
Q(x)
=
\left(
\prod_d\Psi_d(x)^{v_{\Psi_d}(Q)}
\right)R(x),
$$

where $R$ has no real-cyclotomic factor. Then

$$
\deg Q
=
\mathfrak C^+(P)+\deg R.
$$

Equality holds exactly when $R$ is constant. ∎

### Interpretation 10.4

One order of reciprocal contact at context $d$ consumes exactly

$$
\boxed{\lambda_d}
$$

units of reciprocal-core degree.

For $d\ge3$, inverse primitive roots are one real context, so the cost is $\varphi(d)/2$. At $d=1,2$, the cost is one core degree but produces two ordinary orders of contact because the map $q\mapsto q+q^{-1}$ is ramified.

---

# 11. Half-Budget Finite Determination

Let

$$
F,G\in\mathcal R_E,
\qquad
E=2m+\varepsilon.
$$

Write

$$
Q_F=\operatorname{Core}_E(F),
\qquad
Q_G=\operatorname{Core}_E(G).
$$

### Project Theorem 11.1 — Reciprocal Finite Determination Theorem

Let $\mathcal D$ be finite and choose depths $r_d\ge1$. Suppose

$$
\boxed{
J^+_{d,r_d}(F)=J^+_{d,r_d}(G)
\qquad(d\in\mathcal D).
}
$$

If

$$
\boxed{
\sum_{d\in\mathcal D}\lambda_dr_d>m,
}
$$

then

$$
\boxed{F=G.}
$$

#### Proof

Put

$$
H(x)=Q_F(x)-Q_G(x).
$$

If $F\ne G$, then $H\ne0$ and

$$
\deg H\le m.
$$

Equality of the first $r_d$ reciprocal jets at context $d$ gives

$$
\Psi_d(x)^{r_d}\mid H(x)
$$

by Lemma 6.2. Since the selected factors are pairwise coprime,

$$
\prod_{d\in\mathcal D}\Psi_d(x)^{r_d}
\mid H(x).
$$

The divisor has degree

$$
\sum_{d\in\mathcal D}\lambda_dr_d>m\ge\deg H,
$$

which is impossible for a nonzero polynomial. Thus $H=0$, and the core isomorphism gives $F=G$. ∎

### Corollary 11.2 — Nonfixed-context half budget

If every selected context satisfies $d\ge3$, then the criterion becomes

$$
\boxed{
\sum_{d\in\mathcal D}
\frac{\varphi(d)}2r_d>m.
}
$$

Equivalently,

$$
\boxed{
\sum_{d\in\mathcal D}\varphi(d)r_d>2m.
}
$$

The rational certificate payload is

$$
\sum_d\frac{\varphi(d)}2r_d,
$$

exactly half the unrestricted payload assigned by Part IX to the same context-depth schedule.

### Corollary 11.3 — Endpoint-enhanced determination

Suppose the schedule includes depths $r_1,r_2$ at $q=1,-1$. Then the determination condition is

$$
\boxed{
r_1+r_2+
\sum_{d\ge3}\frac{\varphi(d)}2r_d>m.
}
$$

The endpoint depths correspond in the original $q$-coordinate to contact depths

$$
2r_1
$$

at $q=1$, and

$$
2r_2+\varepsilon
$$

at $q=-1$.

### Corollary 11.4 — First distinguishing reciprocal context

If $F\ne G$, then for every finite schedule satisfying

$$
\sum_{d\in\mathcal D}\lambda_dr_d>m,
$$

at least one selected reciprocal jet must differ.

Thus adaptive comparison terminates once the accumulated real weight exceeds the reciprocal-core degree bound.

---

# 12. Sharpness and information-theoretic optimality

### Project Theorem 12.1 — Sharpness at exact reciprocal budget

Let $\mathcal D$ be finite and choose $r_d\ge1$. Define

$$
M^+(x)=\prod_{d\in\mathcal D}\Psi_d(x)^{r_d}.
$$

Then

$$
\deg M^+
=
B^+=\sum_d\lambda_dr_d,
$$

and every selected reciprocal jet of depth $r_d$ vanishes on $M^+$, although

$$
M^+\ne0.
$$

Consequently, the strict inequality

$$
B^+>m
$$

in Theorem 11.1 cannot be weakened to $B^+\ge m$ in general.

#### Proof

Each $\Psi_d^{r_d}$ divides $M^+$, so the first $r_d$ derivatives vanish at $\alpha_d$. Pairwise coprimeness gives the degree formula. The product is nonzero. If $B^+=m$, it is a nonzero core of degree $m$ invisible to all selected packets. ∎

### Project Theorem 12.2 — Optimal rational dimension

The reciprocal jet space

$$
\bigoplus_{d\in\mathcal D}(K_d^+)^{r_d}
$$

has rational dimension

$$
\boxed{B^+=\sum_d\lambda_dr_d.}
$$

The core space $\mathbb Q[x]_{<B^+}$ has the same dimension. Therefore no universal rational-linear reconstruction map using fewer than $B^+$ independent rational scalar measurements can recover every core of degree less than $B^+$.

#### Proof

The target dimension is

$$
\sum_d r_d[K_d^+:\mathbb Q]
=
\sum_d\lambda_dr_d
=B^+.
$$

The source dimension is also $B^+$. Any injective linear map from a $B^+$-dimensional vector space requires a target of dimension at least $B^+$. ∎

### Corollary 12.3 — Exact half-dimension principle

For $d\ge3$, one unrestricted local derivative value lies in a field of rational degree $\varphi(d)$, while one reciprocal-core derivative value lies in a field of rational degree $\varphi(d)/2$.

Thus the reciprocal theory removes exactly the redundant complex-conjugate half of the local data.

### Caution 12.4 — What “half budget” means

The theorem halves the **rational information dimension** and the exact field representation size at nonfixed contexts. It does not claim that every implementation computes a reciprocal jet in exactly half the runtime, nor that the same identity always needs half as many derivative orders. Computational cost depends on the chosen representation and the structured family.

---

# 13. Gaussian and multinomial applications

Gaussian binomial and multinomial coefficients are reciprocal.

Let

$$
M_{\mathbf k}(q)
={n\brack k_1,\ldots,k_c}_q,
\qquad
\sum_{\nu=1}^{c}k_\nu=n.
$$

Its degree is

$$
\boxed{
E(\mathbf k)
=
\sum_{\mu<\nu}k_\mu k_\nu
=
\frac{n^2-\sum_\nu k_\nu^2}{2}.
}
$$

It satisfies

$$
\boxed{
M_{\mathbf k}(q)
=q^{E(\mathbf k)}M_{\mathbf k}(q^{-1}).
}
$$

### Corollary 13.1 — Reciprocal-core representation of a Gaussian multinomial

Write

$$
E(\mathbf k)=2m+\varepsilon.
$$

There is a unique polynomial

$$
Q_{\mathbf k}(x)\in\mathbb Q[x],
\qquad
\deg Q_{\mathbf k}\le m,
$$

such that

$$
\boxed{
M_{\mathbf k}(q)
=q^m(1+q)^\varepsilon
Q_{\mathbf k}(q+q^{-1}).
}
$$

#### Proof

Apply Theorem 1.5 to the reciprocal multinomial. ∎

### Corollary 13.2 — Finite determination of equal-degree multinomials

Let $\mathbf k$ and $\mathbf l$ be two content vectors whose Gaussian multinomials have the same degree

$$
E=2m+\varepsilon.
$$

If their reciprocal jets agree according to a schedule satisfying

$$
\boxed{
\sum_d\lambda_dr_d>m,
}
$$

then

$$
\boxed{
M_{\mathbf k}(q)=M_{\mathbf l}(q).
}
$$

Consequently, after deleting zero parts,

$$
\boxed{
\{k_1,\ldots,k_c\}
=
\{l_1,\ldots,l_c\}
}
$$

as multisets.

#### Proof

Theorem 11.1 gives equality of the polynomials. Equality of the Gaussian multinomials implies equality of their denominator factorial products after cancelling the common numerator $(q;q)_n$. The uniqueness of compressed factorial representations from Part VI then gives equality of the positive part multiplicities. ∎

### Corollary 13.3 — Degree as a zeroth reciprocal fingerprint

If

$$
E(\mathbf k)\ne E(\mathbf l),
$$

then the two Gaussian multinomials are unequal.

Thus reciprocal interpolation is required only after the degree fingerprint has matched.

### Corollary 13.4 — Binary contact parity for multinomials

For every Gaussian multinomial,

$$
\boxed{
v_{q+1}(M_{\mathbf k})
\equiv
E(\mathbf k)
\pmod2.
}
$$

This is the polynomial divisibility form of the binary reciprocity law developed in Part IV.

### Application 13.5 — Real-field cumulant storage

At a context $d\ge3$, the normalized reciprocal core jet belongs to $K_d^+$. Therefore a software implementation may store the reciprocal amplitude data in a basis of the maximal real subfield rather than in a full basis of $K_d$.

The chiral odd phase information of Part IV is not discarded: it is reconstructed from the known reciprocal prefactor and the triangular conversion between reciprocal jets and ordinary Euler jets.

---

# 14. Reciprocal identity and reconstruction certificates

A reciprocal certificate should record the core degree bound and real-cyclotomic packets rather than unrestricted complex packets.

## 14.1 Equality certificate

```text
ReciprocalIdentityCertificate(
    formal_degree=E,
    core_degree_bound=floor(E/2),
    contexts=[
        (d_1, reciprocal_depth=r_1),
        ...,
        (d_s, reciprocal_depth=r_s)
    ],
    real_weight=sum(lambda(d_i)*r_i),
    conclusion="equal"
)
```

A verifier checks:

1. both expressions are reciprocal of the same formal degree $E$;
2. the claimed reciprocal jets agree exactly;
3. the accumulated weight satisfies
   $$
   \sum_i\lambda(d_i)r_i>\left\lfloor\frac E2\right\rfloor.
   $$

Theorem 11.1 then proves equality.

## 14.2 Reconstruction certificate

```text
ReciprocalReconstructionCertificate(
    parity=epsilon,
    contexts=[...],
    local_real_residues=[...],
    real_crt_modulus=product(Psi_d(x)^r_d),
    reconstructed_core=Q(x),
    reciprocal_lift=A_E(q)*Q(q+q^(-1))
)
```

A verifier checks each local congruence

$$
Q(x)\equiv H_d(x)\pmod{\Psi_d(x)^{r_d}}
$$

and the final reciprocal lift.

## 14.3 Exact comparison workflow

```text
input: reciprocal expressions F and G of formal degree E
m = floor(E/2)
weight = 0

for selected contexts d:
    compare reciprocal jets successively
    if a mismatch appears:
        return NONIDENTICAL with the first mismatching jet
    weight += lambda_d * matched_depth
    if weight > m:
        return IDENTICAL by reciprocal finite determination
```

This is the reciprocal analogue of the two-sided certificate engine from Parts VIII–IX.

---

# 15. Comparison with unrestricted cyclotomic interpolation

For a schedule supported on contexts $d\ge3$, Part IX assigns total weight

$$
B=\sum_d\varphi(d)r_d.
$$

The present chapter assigns

$$
\boxed{
B^+=\sum_d\frac{\varphi(d)}2r_d
=\frac B2.
}
$$

The ambient polynomial dimensions scale in the same way:

$$
\dim\mathbb Q[q]_{\le E}=E+1,
$$

while

$$
\dim\mathcal R_E
=
\left\lfloor\frac E2\right\rfloor+1.
$$

Thus the real-cyclotomic theory is not a heuristic compression. It is the exact Hermite interpolation theory of the reciprocal subspace.

At $d=1,2$, the local field does not shrink because it is already $\mathbb Q$. Instead, the coordinate map ramifies:

$$
q\Psi_1(q+q^{-1})=\Phi_1(q)^2,
$$

$$
q\Psi_2(q+q^{-1})=\Phi_2(q)^2.
$$

This produces the endpoint two-for-one law:

$$
\boxed{
1\text{ core derivative}
\longleftrightarrow
2\text{ constrained Euler orders}.
}
$$

The three theories therefore fit together as follows:

$$
\boxed{
\begin{array}{c}
\text{Part VIII: weighted contact gives uniqueness}\\[1mm]
\Downarrow\\[1mm]
\text{Part IX: unrestricted jets give optimal reconstruction}\\[1mm]
\Downarrow\\[1mm]
\text{Part X: reciprocity descends the theory to real contexts}\\[1mm]
\text{and removes the redundant conjugate half.}
\end{array}
}
$$

---

# 16. Theorem inventory

| Result | Statement | Status | Consequence |
|---|---|---|---|
| Reciprocal Core Theorem | $P=A_EQ(q+q^{-1})$, $\deg Q\le\lfloor E/2\rfloor$ | Project theorem | Reduces reciprocal polynomials to one real variable |
| Real cyclotomic degree | $\lambda_d=1$ for $d=1,2$, $\varphi(d)/2$ for $d\ge3$ | Classical lemma | Correct reciprocal context weight |
| Real Cyclotomic Lifting Identity | $q^{\lambda_d}\Psi_d(q+q^{-1})=\Phi_d^{e_d}$ | Project theorem | Transfers valuations exactly |
| Valuation transfer | $v_{\Phi_d}(P)=e_dv_{\Psi_d}(Q)+\varepsilon\mathbf1_{d=2}$ | Corollary | Explains endpoint parity and ramification |
| Euler/reciprocal jet equivalence | Ordinary and real jets are triangularly equivalent for $d\ge3$ | Project theorem | Existing CCA jets can be converted exactly |
| Endpoint even-germ theorems | Normalized germs at $q=\pm1$ are even | Project theorem | Only even local orders contain new data |
| Local Real-Cyclotomic Hermite Isomorphism | $\mathbb Q[x]/(\Psi_d^r)\cong(K_d^+)^r$ | Project theorem | Exact local realization and uniqueness |
| Global Real-Cyclotomic Hermite Isomorphism | CRT direct sum over real contexts | Project theorem | Independent multi-context packets |
| Reciprocal Hermite Interpolation | Unique core of degree $<B^+$ | Project theorem | Exact reciprocal reconstruction |
| Explicit reciprocal CRT | $Q\equiv\sum H_dE_d^+\pmod{M^+}$ | Algorithmic theorem | Implementable reconstruction |
| Reciprocal Contact Budget | $\sum\lambda_dv_{\Psi_d}(Q)\le\deg Q\le\lfloor E/2\rfloor$ | Project theorem | Global conservation law in the reciprocal subspace |
| Reciprocal Finite Determination | Matching weight $>\lfloor E/2\rfloor$ forces equality | Project theorem | Complete half-budget identity certificates |
| Sharpness | Product of selected $\Psi_d^{r_d}$ saturates the threshold | Sharpness theorem | Strict inequality is optimal |
| Gaussian reciprocal determination | Equal-degree multinomials are determined by sufficient real jets | Corollary | Smaller exact certificates for the main CCA family |

---

# 17. Open problems

## 17.1 Integral reciprocal interpolation

Classify the image of

$$
\mathbb Z[x]/(M^+)
$$

inside

$$
\bigoplus_d(\mathcal O_{K_d^+})^{r_d}.
$$

Equivalently, determine the exact denominator and congruence conditions for a real-cyclotomic packet to arise from an integer reciprocal polynomial.

## 17.2 Direct compressed-core reconstruction

The reconstructed core $Q(x)$ may still have enormous degree. Determine when it admits a compact representation by recurrences, circuits, orthogonal-polynomial bases, or transformed factorial quotients.

## 17.3 Optimal reciprocal schedules

Given a structured reciprocal family and a cost model, minimize exact computation while accumulating real weight greater than the core-degree bound.

The endpoint contexts may be especially efficient because one core order corresponds to two ordinary contact orders.

## 17.4 Sparse reciprocal recovery

If the reciprocal core has few nonzero coefficients or few factors but enormous degree, can it be reconstructed from substantially less than its degree using sparse real-cyclotomic jets?

## 17.5 Chiral reconstruction from real cores

For $d\ge3$, make the triangular conversion between real-core derivatives and the amplitude/chirality cumulants of Part IV fully explicit to all orders.

## 17.6 Formal verification

Implement the lifting identity, local real residue rings, triangular inversion, and reciprocal CRT in SageMath, OSCAR, or Lean, with machine-checkable equality certificates.

---

# 18. Final statement

The main structural identity of Part X is

$$
\boxed{
P(q)=q^m(1+q)^\varepsilon Q(q+q^{-1}),
\qquad
E=2m+\varepsilon.
}
$$

It converts reciprocal polynomial arithmetic into ordinary polynomial arithmetic in the real coordinate

$$
x=q+q^{-1}.
$$

Every cyclotomic context descends to a real context $\alpha_d$, with exact lifting law

$$
\boxed{
q^{\lambda_d}\Psi_d(q+q^{-1})
=
\Phi_d(q)^{e_d}.
}
$$

The resulting interpolation theorem is

$$
\boxed{
\mathbb Q[x]_{<B^+}
\cong
\bigoplus_{d\in\mathcal D}(K_d^+)^{r_d},
\qquad
B^+=\sum_d\lambda_dr_d.
}
$$

For a reciprocal polynomial of formal degree $E=2m+\varepsilon$, matching reciprocal jets of total weight greater than $m$ force equality:

$$
\boxed{
\sum_d\lambda_dr_d>m
\quad\Longrightarrow\quad
F=G.
}
$$

The threshold is sharp, and the information dimension is optimal.

Thus Parts VIII–X now provide three exact layers:

$$
\boxed{
\begin{array}{c}
\text{global contact budget}\\[1mm]
\Downarrow\\[1mm]
\text{unrestricted cyclotomic reconstruction}\\[1mm]
\Downarrow\\[1mm]
\text{reciprocal real-cyclotomic reconstruction at half dimension}.
\end{array}
}
$$

For the reciprocal families central to Cyclotomic Coefficient Arithmetic, the redundant complex-conjugate half of the generic jet data has been removed exactly rather than approximately.
