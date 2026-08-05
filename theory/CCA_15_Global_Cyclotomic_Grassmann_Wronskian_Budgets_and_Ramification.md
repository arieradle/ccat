# Cyclotomic Coefficient Arithmetic

## Part XV — Global Cyclotomic Grassmann–Wronskian Budgets and Ramification

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete theorem chapter  
**Scope:** Polynomial subspaces in Laurent windows, local vanishing sequences, ordinary and Euler Wronskians, exact projective ramification conservation, Galois-weighted cyclotomic budgets, common-content and residual-ramification decomposition, cumulative jet-rank defects, pairwise collision reinterpretation, Gaussian-row consequences, stable-content reduction, Grassmannian reconstruction, sharpness, and exact rank certificates.

---

# 0. Purpose, dependencies, and the new theorem

Part II established exact Gaussian collision arithmetic. It identified simple root-of-unity collisions and determined the stable cyclotomic content and spacing of central Gaussian blocks.

Part VIII established the rank-one global contact law

$$
\sum_{d\ge1}\varphi(d)v_{\Phi_d}(P)
\le
\operatorname{span}(P).
$$

Part XIV established arbitrary-rank rigidity for a selected Gaussian row at the single context

$$
q=1.
$$

If

$$
V
=
\operatorname{span}
\left\{
{n\brack k_1}_q,\ldots,{n\brack k_m}_q
\right\},
$$

with distinct lower-half positions, then the vanishing orders attained by nonzero elements of $V$ at $q=1$ are exactly

$$
0,1,\ldots,m-1.
$$

The present chapter unifies these three levels by replacing one polynomial or one pair with an entire finite-dimensional polynomial space.

Let

$$
V\subseteq \mathbb Q[q,q^{-1}]
$$

be an $m$-dimensional space contained in a Laurent support window of width $N$. At a point $p\ne0$, let

$$
0\le a_0(p)<a_1(p)<\cdots<a_{m-1}(p)
$$

be the local vanishing sequence of $V$. Define its ramification weight by

$$
\boxed{
\operatorname{Ram}_p(V)
=
\sum_{i=0}^{m-1}\bigl(a_i(p)-i\bigr).
}
$$

The first main theorem identifies this weight with a Wronskian zero:

$$
\boxed{
\operatorname{ord}_{q=p}W_V(q)
=
\operatorname{Ram}_p(V).
}
$$

The projective Wronskian has a fixed total zero budget. After shifting the Laurent window to

$$
\mathbb Q[q]_{\le N},
$$

one obtains the exact conservation law

$$
\boxed{
\sum_{p\in\mathbb P^1(\overline{\mathbb Q})}
\operatorname{Ram}_p(V)
=
m(N-m+1).
}
$$

For a rational space, every primitive $d$-th root has the same ramification weight. Therefore the cyclotomic part of this conservation law is

$$
\boxed{
\sum_{d\ge1}
\varphi(d)\operatorname{Ram}_d(V)
\le
m(N-m+1),
}
$$

where $\operatorname{Ram}_d(V)$ is the weight at one primitive $d$-th root.

A sharper affine form is obtained from the lower and upper exponent sequences of the space:

$$
\boxed{
\sum_{d\ge1}
\varphi(d)\operatorname{Ram}_d(V)
\le
\operatorname{span}(W_V)
=
\sum_{i=0}^{m-1}(\beta_i-\alpha_i).
}
$$

Here

$$
0\le\alpha_0<\cdots<\alpha_{m-1}\le N
$$

is the lower exponent sequence and

$$
0\le\beta_0<\cdots<\beta_{m-1}\le N
$$

is the upper exponent sequence.

The local weight also has an exact jet-rank form. If

$$
J_{p,r}:V\longrightarrow\overline{\mathbb Q}^{\,r},
\qquad
f\longmapsto
\bigl(f(p),Df(p),\ldots,D^{r-1}f(p)\bigr),
$$

then

$$
\boxed{
\operatorname{Ram}_p(V)
=
\sum_{r\ge1}
\left(
\min(m,r)-\operatorname{rank}J_{p,r}
\right).
}
$$

Thus the global theorem may be read as

$$
\boxed{
\text{total Galois-weighted cumulative jet-rank defect}
\le
\text{one finite Grassmannian budget}.
}
$$

Finally, if $c_d(V)$ is the common $\Phi_d$-depth of the entire space and $\rho_d(V)$ is the residual ramification after this mandatory content is removed, then

$$
\boxed{
\operatorname{Ram}_d(V)
=
m c_d(V)+\rho_d(V),
}
$$

and hence

$$
\boxed{
\sum_d\varphi(d)
\bigl(mc_d(V)+\rho_d(V)\bigr)
\le
\operatorname{span}(W_V).
}
$$

This is the sought synthesis:

$$
\boxed{
\text{rank}\times\text{mandatory cyclotomic content}
\;+
\text{exceptional higher cancellation}
\;\le
\text{global Wronskian budget}.
}
$$

The labels used below are:

- **Classical lemma:** standard algebraic or Wronskian input, proved here;
- **Classical theorem:** a standard projective-linear-series statement, proved here in the polynomial form needed by CCA;
- **Project theorem:** a cyclotomic or structured consequence established in this chapter;
- **Corollary:** a formal consequence;
- **Sharpness statement:** an example proving optimality;
- **Algorithmic theorem:** a correctness theorem for reconstruction or certification;
- **Caution:** a boundary required for exact interpretation.

Throughout, the coefficient field has characteristic zero. Rationality is imposed whenever one primitive root is used to represent a complete Galois orbit.

---

# 1. Laurent windows and polynomial subspaces

## 1.1 Laurent support windows

Fix integers

$$
L\in\mathbb Z,
\qquad
N\ge0.
$$

Define the Laurent window

$$
\boxed{
\mathcal A_{L,N}
=
q^L\mathbb Q[q]_{\le N}
=
\operatorname{span}_{\mathbb Q}
\{q^L,q^{L+1},\ldots,q^{L+N}\}.
}
$$

Its dimension is

$$
N+1.
$$

Let

$$
V\subseteq\mathcal A_{L,N}
$$

be an $m$-dimensional subspace. Necessarily

$$
1\le m\le N+1.
$$

Multiplication by $q^{-L}$ gives an isomorphism

$$
V\longrightarrow \widetilde V=q^{-L}V
\subseteq\mathbb Q[q]_{\le N}.
$$

At every nonzero point, this monomial shift is multiplication by a local unit. Hence it does not change any local vanishing sequence or any cyclotomic ramification weight.

We will therefore prove the projective statements for

$$
V\subseteq\mathbb Q[q]_{\le N}
$$

and transfer them back to Laurent windows by monomial shift.

## 1.2 Lower exponent sequence

For a nonzero polynomial $f$, write

$$
\operatorname{ord}_0(f)=v_q(f).
$$

### Definition 1.1 — Lower exponent sequence

The lower exponent sequence of $V\subseteq\mathbb Q[q]_{\le N}$ is the strictly increasing sequence

$$
\boxed{
0\le\alpha_0<\alpha_1<\cdots<\alpha_{m-1}\le N
}
$$

for which there exists a basis

$$
f_0,\ldots,f_{m-1}
$$

satisfying

$$
\operatorname{ord}_0(f_i)=\alpha_i.
$$

Such a basis is called a **lower-adapted basis**.

## 1.3 Upper exponent sequence

### Definition 1.2 — Upper exponent sequence

The upper exponent sequence of $V$ is the strictly increasing sequence

$$
\boxed{
0\le\beta_0<\beta_1<\cdots<\beta_{m-1}\le N
}
$$

for which there exists a basis

$$
g_0,\ldots,g_{m-1}
$$

satisfying

$$
\deg g_i=\beta_i.
$$

Such a basis is called an **upper-adapted basis**.

### Classical Lemma 1.3 — Existence and uniqueness of endpoint sequences

Every finite-dimensional polynomial space has unique lower and upper exponent sequences.

#### Proof

Write the coefficient vectors of any basis in the monomial basis

$$
1,q,\ldots,q^N.
$$

Row reduction from the lowest exponent upward produces a basis with distinct first nonzero positions. These pivot positions are the $\alpha_i$. Reduced-row-echelon uniqueness shows that the set of pivot positions is independent of the starting basis.

Row reduction from the highest exponent downward produces a basis with distinct last nonzero positions. These positions are the $\beta_i$, and the same uniqueness argument applies. ∎

### Corollary 1.4 — Endpoint bounds

One has

$$
\boxed{
\alpha_i\ge i,
\qquad
\beta_i\le N-m+1+i.
}
$$

Consequently,

$$
\boxed{
\sum_{i=0}^{m-1}(\beta_i-\alpha_i)
\le
m(N-m+1).
}
$$

#### Proof

The $\alpha_i$ are $m$ distinct nonnegative integers, so the $i$-th smallest is at least $i$.

The $\beta_i$ are $m$ distinct integers at most $N$. The $i$-th smallest is therefore at most the $i$-th member of the largest possible set

$$
N-m+1,N-m+2,\ldots,N.
$$

Thus

$$
\beta_i\le N-m+1+i.
$$

Subtract and sum. ∎

---

# 2. Local vanishing sequences and jet filtrations

Fix a field extension $K/\mathbb Q$, a point

$$
p\in K,
$$

and an $m$-dimensional space

$$
V_K=V\otimes_{\mathbb Q}K.
$$

For a nonzero polynomial $f$, let

$$
\operatorname{ord}_p(f)
$$

be its zero multiplicity at $p$.

## 2.1 The osculating filtration

For $r\ge0$, define

$$
\boxed{
V_{\ge r}(p)
=
\{f\in V_K:\operatorname{ord}_p(f)\ge r\}.
}
$$

Then

$$
V_K=V_{\ge0}(p)
\supseteq
V_{\ge1}(p)
\supseteq
V_{\ge2}(p)
\supseteq\cdots.
$$

The quotient

$$
(q-p)^rK[q]_{(q-p)}
\big/
(q-p)^{r+1}K[q]_{(q-p)}
$$

is one-dimensional. Therefore the dimension of $V_{\ge r}(p)$ can drop by at most one when $r$ increases by one.

### Definition 2.1 — Local vanishing sequence

The local vanishing sequence of $V$ at $p$ is the unique strictly increasing sequence

$$
\boxed{
0\le a_0(p)<a_1(p)<\cdots<a_{m-1}(p)
}
$$

such that there exists a basis

$$
f_0,\ldots,f_{m-1}
$$

with

$$
\operatorname{ord}_p(f_i)=a_i(p).
$$

Such a basis is called **adapted at $p$**.

### Classical Lemma 2.2 — Existence of an adapted local basis

The local vanishing sequence exists and is unique. Moreover,

$$
\boxed{a_i(p)\ge i.}
$$

#### Proof

Expand each element in the local coordinate

$$
x=q-p.
$$

Row reduction on the infinite Taylor coefficient matrix produces a basis with distinct pivot orders. Since $V$ is finite-dimensional, only finitely many columns are required before all pivots appear. These pivot orders are the $a_i(p)$.

Equivalently, define $a_i(p)$ as the unique integers for which

$$
\dim V_{\ge r}(p)
=
\#\{i:a_i(p)\ge r\}.
$$

The filtration determines the sequence uniquely.

Since the sequence consists of distinct nonnegative integers, its $i$-th member is at least $i$. ∎

## 2.2 Ramification weight

### Definition 2.3 — Local ramification weight

Define

$$
\boxed{
\operatorname{Ram}_p(V)
=
\sum_{i=0}^{m-1}\bigl(a_i(p)-i\bigr).
}
$$

Every summand is nonnegative, so

$$
\operatorname{Ram}_p(V)\ge0.
$$

The space is called **unramified at $p$** when

$$
\operatorname{Ram}_p(V)=0.
$$

Equivalently,

$$
\boxed{
a_i(p)=i
\qquad(0\le i<m).
}
$$

This means that the first $m$ jets at $p$ form a complete coordinate system on $V$.

## 2.3 Euler jets

At a nonzero point $p$, use

$$
D=q\frac d{dq}.
$$

Because $q$ is a local unit at $p$, ordinary derivatives and Euler derivatives define the same vanishing filtration.

For $r\ge1$, define the truncated Euler-jet map

$$
\boxed{
J_{p,r}:V_K\longrightarrow K^r,
\qquad
f\longmapsto
\bigl(f(p),Df(p),\ldots,D^{r-1}f(p)\bigr).
}
$$

### Lemma 2.4 — Jet-kernel formula

$$
\boxed{
\ker J_{p,r}=V_{\ge r}(p).
}
$$

Consequently,

$$
\boxed{
\operatorname{rank}J_{p,r}
=
\#\{i:a_i(p)<r\}.
}
$$

#### Proof

The local Euler-jet criterion gives

$$
D^j f(p)=0
\quad(0\le j<r)
\iff
\operatorname{ord}_p(f)\ge r.
$$

This proves the kernel identity. Rank-nullity and the filtration description in Lemma 2.2 give the rank formula. ∎

### Project Theorem 2.5 — Cumulative jet-rank defect formula

For every nonzero point $p$,

$$
\boxed{
\operatorname{Ram}_p(V)
=
\sum_{r\ge1}
\left(
\min(m,r)-\operatorname{rank}J_{p,r}
\right).
}
$$

Only finitely many summands are nonzero.

#### Proof

For any nonnegative integer $a$,

$$
a=\sum_{r\ge1}\mathbf 1_{a\ge r}.
$$

Therefore

$$
\sum_i a_i(p)
=
\sum_{r\ge1}\#\{i:a_i(p)\ge r\}
=
\sum_{r\ge1}\dim V_{\ge r}(p).
$$

Similarly,

$$
\sum_{i=0}^{m-1}i
=
\sum_{r\ge1}\max(m-r,0).
$$

Subtracting gives

$$
\operatorname{Ram}_p(V)
=
\sum_{r\ge1}
\left(
\dim V_{\ge r}(p)-\max(m-r,0)
\right).
$$

By Lemma 2.4,

$$
\dim V_{\ge r}(p)=m-\operatorname{rank}J_{p,r}.
$$

If $r\le m$, the summand becomes

$$
r-\operatorname{rank}J_{p,r}.
$$

If $r>m$, it becomes

$$
m-\operatorname{rank}J_{p,r}.
$$

Both cases equal

$$
\min(m,r)-\operatorname{rank}J_{p,r}.
$$

For sufficiently large $r$, no nonzero element of the finite-degree space vanishes to order $r$, so $J_{p,r}$ is injective and has rank $m$. Hence the sum is finite. ∎

### Interpretation 2.6

At depth $r$, an $m$-dimensional space can contribute at most

$$
\min(m,r)
$$

independent initial-jet coordinates. The deficit from this maximum is

$$
\min(m,r)-\operatorname{rank}J_{p,r}.
$$

The ramification weight is the cumulative deficit over all depths.

---

# 3. Wronskians

## 3.1 Ordinary Wronskian

Let

$$
f_0,\ldots,f_{m-1}
$$

be a basis of $V$. Define

$$
\boxed{
W(f_0,\ldots,f_{m-1})(q)
=
\det
\left(
\frac{d^j f_i}{dq^j}(q)
\right)_{
\substack{0\le j<m\\0\le i<m}}.
}
$$

### Classical Lemma 3.1 — Basis covariance

If

$$
(g_0,\ldots,g_{m-1})
=(f_0,\ldots,f_{m-1})A
$$

for an invertible constant matrix $A$, then

$$
\boxed{
W(g_0,\ldots,g_{m-1})
=
\det(A)W(f_0,\ldots,f_{m-1}).
}
$$

#### Proof

The derivative matrix for the $g_i$ is the derivative matrix for the $f_i$ multiplied on the right by $A$. Taking determinants gives the formula. ∎

Thus the Wronskian is defined by the space $V$ up to a nonzero scalar. We write

$$
W_V(q)
$$

for any representative.

### Classical Lemma 3.2 — Nonvanishing criterion

In characteristic zero,

$$
\boxed{
W_V\ne0
\iff
\dim V=m.
}
$$

#### Proof

Linear dependence plainly forces the Wronskian to vanish.

Conversely, choose an upper-adapted basis with distinct degrees

$$
\beta_0<\cdots<\beta_{m-1}.
$$

Let $c_iq^{\beta_i}$ be the leading term of $f_i$. The leading term of the Wronskian is

$$
\left(
\prod_i c_i
\right)
\det\bigl((\beta_i)_j\bigr)_{0\le j,i<m}
q^{\sum_i\beta_i-\binom m2},
$$

where

$$
(\beta)_j
=
\beta(\beta-1)\cdots(\beta-j+1).
$$

The determinant of the falling-factorial evaluation matrix is the Vandermonde

$$
\prod_{i<j}(\beta_j-\beta_i),
$$

which is nonzero because the $\beta_i$ are distinct. Hence the Wronskian is nonzero. ∎

## 3.2 Common-factor law

### Classical Lemma 3.3 — Wronskian common-factor law

For every nonzero rational function $h(q)$,

$$
\boxed{
W(hf_0,\ldots,hf_{m-1})
=
h(q)^mW(f_0,\ldots,f_{m-1}).
}
$$

#### Proof

For each derivative order $j$, the Leibniz rule gives

$$
\frac{d^j}{dq^j}(hf_i)
=
\sum_{s=0}^{j}
\binom js h^{(j-s)}f_i^{(s)}.
$$

Thus the derivative matrix of $(hf_i)$ is obtained from the derivative matrix of $(f_i)$ by left multiplication by a lower triangular matrix whose diagonal entries are all $h$. Its determinant is $h^m$. ∎

## 3.3 Euler Wronskian

Define

$$
\boxed{
W_V^{D}(q)
=
\det\left(D^j f_i(q)\right)_{
\substack{0\le j<m\\0\le i<m}}.
}
$$

### Lemma 3.4 — Euler–ordinary Wronskian relation

$$
\boxed{
W_V^{D}(q)
=
q^{\binom m2}W_V(q).
}
$$

#### Proof

The operator identity

$$
D^j
=
\sum_{s=0}^{j}
\left\{\begin{matrix}j\\s\end{matrix}\right\}
q^s\frac{d^s}{dq^s}
$$

shows that the Euler derivative matrix is obtained from the ordinary derivative matrix by a lower triangular row transformation. Its diagonal entries are

$$
1,q,q^2,\ldots,q^{m-1}.
$$

Their product is

$$
q^{0+1+\cdots+(m-1)}
=
q^{\binom m2}.
$$

Taking determinants proves the formula. ∎

At every cyclotomic context, $q\ne0$, so ordinary and Euler Wronskians have the same local order.

---

# 4. Local Wronskian order and exact projective conservation

## 4.1 Local order theorem

### Classical Theorem 4.1 — Wronskian order from the vanishing sequence

Let

$$
0\le a_0(p)<\cdots<a_{m-1}(p)
$$

be the vanishing sequence of $V$ at a finite point $p$. Then

$$
\boxed{
\operatorname{ord}_{q=p}W_V(q)
=
\sum_{i=0}^{m-1}a_i(p)-\binom m2
=
\operatorname{Ram}_p(V).
}
$$

#### Proof

Choose a basis adapted at $p$. In the local coordinate

$$
x=q-p,
$$

write

$$
f_i(q)=c_ix^{a_i}+O(x^{a_i+1}),
\qquad
c_i\ne0.
$$

Then

$$
\frac{d^j f_i}{dq^j}
=
 c_i(a_i)_j x^{a_i-j}
+O(x^{a_i-j+1}).
$$

Factor $c_ix^{a_i}$ from column $i$ and $x^{-j}$ from row $j$. The leading term of the determinant is

$$
\left(\prod_i c_i\right)
\det\bigl((a_i)_j\bigr)
 x^{\sum_i a_i-\binom m2}.
$$

The determinant is the Vandermonde

$$
\prod_{i<j}(a_j-a_i),
$$

which is nonzero because the vanishing orders are strictly increasing. Hence the displayed exponent is exact. ∎

### Corollary 4.2 — Unramified criterion

The following are equivalent:

1. $V$ is unramified at $p$;
2. $W_V(p)\ne0$;
3. the first $m$ ordinary jets at $p$ have full rank;
4. if $p\ne0$, the first $m$ Euler jets at $p$ have full rank.

#### Proof

By Theorem 4.1,

$$
W_V(p)\ne0
\iff
\operatorname{Ram}_p(V)=0.
$$

The determinant defining the Wronskian is precisely the first $m$-jet matrix. At a nonzero point, Lemma 3.4 transfers the statement to Euler jets. ∎

## 4.2 Exact endpoint orders

Let

$$
\alpha_0<\cdots<\alpha_{m-1}
$$

and

$$
\beta_0<\cdots<\beta_{m-1}
$$

be the lower and upper exponent sequences.

### Corollary 4.3 — Exact lower order and degree of the Wronskian

$$
\boxed{
 v_q(W_V)
=
\sum_i\alpha_i-\binom m2,
}
$$

and

$$
\boxed{
\deg W_V
=
\sum_i\beta_i-\binom m2.
}
$$

Consequently,

$$
\boxed{
\operatorname{span}(W_V)
=
\sum_{i=0}^{m-1}(\beta_i-\alpha_i).
}
$$

#### Proof

The first formula is Theorem 4.1 at $p=0$.

The degree formula was proved in Lemma 3.2 by using an upper-adapted basis and showing that the leading Vandermonde coefficient is nonzero.

Subtracting the lower order from the degree gives the span formula. ∎

## 4.3 The point at infinity

View $V\subseteq\mathbb Q[q]_{\le N}$ as a linear series in

$$
H^0(\mathbb P^1,\mathcal O(N)).
$$

Use the local coordinate

$$
t=q^{-1}
$$

at infinity. The section represented by $f(q)$ becomes

$$
t^Nf(t^{-1}).
$$

If $\deg f=\beta$, its vanishing order at infinity is

$$
N-\beta.
$$

Thus the vanishing sequence at infinity is

$$
N-\beta_{m-1}
<
N-\beta_{m-2}
<\cdots<
N-\beta_0.
$$

### Corollary 4.4 — Ramification at infinity

$$
\boxed{
\operatorname{Ram}_{\infty}(V)
=
mN-\sum_i\beta_i-\binom m2.
}
$$

#### Proof

Sum the infinity vanishing sequence and subtract $\binom m2$. ∎

## 4.4 Exact projective conservation

### Classical Theorem 4.5 — Projective Wronskian conservation law

Let

$$
V\subseteq\mathbb Q[q]_{\le N}
$$

have dimension $m$. Then

$$
\boxed{
\sum_{p\in\mathbb P^1(\overline{\mathbb Q})}
\operatorname{Ram}_p(V)
=
m(N-m+1).
}
$$

#### Proof

By Theorem 4.1, the ramification weight at every finite point equals the zero multiplicity of $W_V$ there. Therefore

$$
\sum_{p\in\mathbb A^1(\overline{\mathbb Q})}
\operatorname{Ram}_p(V)
=
\deg W_V
=
\sum_i\beta_i-\binom m2.
$$

Add the infinity contribution from Corollary 4.4:

$$
\begin{aligned}
\sum_{p\in\mathbb P^1}
\operatorname{Ram}_p(V)
&=
\left(\sum_i\beta_i-\binom m2\right)
+
\left(mN-\sum_i\beta_i-\binom m2\right)\\
&=
mN-m(m-1)\\
&=
m(N-m+1).
\end{aligned}
$$

∎

### Interpretation 4.6 — Grassmannian dimension

The right side is

$$
\boxed{
m(N-m+1)=\dim\operatorname{Gr}(m,N+1).}
$$

Thus the total ramification of an $m$-plane in a polynomial window equals the dimension of its ambient Grassmannian.

This is not an analogy. It is the exact Wronskian conservation law behind the Schubert geometry developed later in the chapter.

## 4.5 Exact affine conservation

Remove the endpoint contributions at $0$ and $\infty$.

### Project Theorem 4.7 — Nonzero affine ramification budget

$$
\boxed{
\sum_{p\in\overline{\mathbb Q}^{\times}}
\operatorname{Ram}_p(V)
=
\operatorname{span}(W_V)
=
\sum_i(\beta_i-\alpha_i).
}
$$

Consequently,

$$
\boxed{
\sum_{p\in\overline{\mathbb Q}^{\times}}
\operatorname{Ram}_p(V)
\le
m(N-m+1).
}
$$

#### Proof

The sum over nonzero finite points is the degree of $W_V$ minus its zero order at $q=0$. By Corollary 4.3 this is

$$
\left(\sum_i\beta_i-\binom m2\right)
-
\left(\sum_i\alpha_i-\binom m2\right)
=
\sum_i(\beta_i-\alpha_i).
$$

The universal bound follows from Corollary 1.4. ∎

---

# 5. The Global Cyclotomic Grassmann–Wronskian Budget

Assume now that

$$
V\subseteq\mathbb Q[q,q^{-1}]
$$

is defined over $\mathbb Q$. Let $\zeta_d$ be one primitive $d$-th root.

### Definition 5.1 — Cyclotomic ramification weight

Define

$$
\boxed{
\operatorname{Ram}_d(V)
=
\operatorname{Ram}_{\zeta_d}(V).
}
$$

Because $V$ is rational, this number is independent of the chosen primitive $d$-th root.

Indeed, Galois conjugation sends the local jet matrix at $\zeta_d$ to the corresponding matrix at every conjugate primitive root and preserves all ranks and vanishing orders.

## 5.1 Wronskian valuation identity

### Project Theorem 5.2 — Cyclotomic Wronskian valuation

For every $d\ge1$,

$$
\boxed{
 v_{\Phi_d}(W_V)
=
\operatorname{Ram}_d(V).
}
$$

The same identity holds for the Euler Wronskian.

#### Proof

At one primitive $d$-th root $\zeta_d$, Theorem 4.1 gives

$$
\operatorname{ord}_{q=\zeta_d}W_V
=
\operatorname{Ram}_d(V).
$$

Since $W_V$ has rational coefficients up to a nonzero rational scalar, every Galois-conjugate primitive root has the same multiplicity. Therefore the exponent of the minimal polynomial $\Phi_d$ in $W_V$ is exactly this common multiplicity.

The Euler Wronskian differs by the monomial

$$
q^{\binom m2},
$$

which is coprime to every $\Phi_d$. ∎

## 5.2 Main budget theorem

### Project Theorem 5.3 — Global Cyclotomic Grassmann–Wronskian Budget

Let

$$
V\subseteq\mathcal A_{L,N}
$$

be an $m$-dimensional rational Laurent-polynomial space. Let

$$
\alpha_0<\cdots<\alpha_{m-1},
\qquad
\beta_0<\cdots<\beta_{m-1}
$$

be the lower and upper exponent sequences after shifting the window to $[0,N]$. Then

$$
\boxed{
\sum_{d\ge1}
\varphi(d)\operatorname{Ram}_d(V)
\le
\sum_{i=0}^{m-1}(\beta_i-\alpha_i)
\le
m(N-m+1).
}
$$

Equivalently,

$$
\boxed{
\sum_{d\ge1}
\varphi(d)v_{\Phi_d}(W_V)
\le
\operatorname{span}(W_V).
}
$$

#### Proof

By Theorem 5.2,

$$
\operatorname{Ram}_d(V)=v_{\Phi_d}(W_V).
$$

Apply the rank-one Global Cyclotomic Contact Budget from Part VIII to the nonzero Laurent polynomial $W_V$:

$$
\sum_d\varphi(d)v_{\Phi_d}(W_V)
\le
\operatorname{span}(W_V).
$$

The exact span formula is Corollary 4.3, and the universal Grassmannian bound is Corollary 1.4. ∎

## 5.3 Exact deficit decomposition

Let

$$
\mathcal R_{\mathrm{nc}}(V)
=
\sum_{
\substack{p\in\overline{\mathbb Q}^{\times}\\
p\text{ not a root of unity}}}
\operatorname{Ram}_p(V).
$$

### Project Theorem 5.4 — Exact cyclotomic/noncyclotomic decomposition

$$
\boxed{
\sum_{d\ge1}
\varphi(d)\operatorname{Ram}_d(V)
+
\mathcal R_{\mathrm{nc}}(V)
=
\operatorname{span}(W_V).
}
$$

Equivalently,

$$
\boxed{
\sum_d\varphi(d)\operatorname{Ram}_d(V)
=
\sum_i(\beta_i-\alpha_i)
-
\mathcal R_{\mathrm{nc}}(V).
}
$$

#### Proof

The nonzero affine points split disjointly into roots of unity and non-roots of unity. At order $d$, there are $\varphi(d)$ primitive roots, each with ramification weight $\operatorname{Ram}_d(V)$. Apply Theorem 4.7. ∎

### Corollary 5.5 — Affine cyclotomic saturation

Equality

$$
\sum_d\varphi(d)\operatorname{Ram}_d(V)
=
\operatorname{span}(W_V)
$$

holds if and only if every nonzero zero of the Wronskian is a root of unity.

Equivalently, up to a nonzero scalar and a Laurent monomial,

$$
\boxed{
W_V(q)
=
q^A\prod_{d\in S}\Phi_d(q)^{r_d}
}
$$

for a finite set $S$.

### Corollary 5.6 — Full Grassmannian saturation

Equality

$$
\sum_d\varphi(d)\operatorname{Ram}_d(V)
=
m(N-m+1)
$$

holds if and only if:

1. $V$ is unramified at $0$;
2. $V$ is unramified at $\infty$;
3. every finite ramification point is a root of unity.

#### Proof

Use Theorem 4.5 and the nonnegativity of every omitted ramification weight. ∎

## 5.4 Immediate exclusions

### Corollary 5.7 — Single-context bound

For every $d$,

$$
\boxed{
\operatorname{Ram}_d(V)
\le
\left\lfloor
\frac{\operatorname{span}(W_V)}{\varphi(d)}
\right\rfloor.
}
$$

In particular, if

$$
\varphi(d)>\operatorname{span}(W_V),
$$

then

$$
\boxed{V\text{ is unramified at every primitive }d\text{-th root}.}
$$

### Corollary 5.8 — Number of exceptional cyclotomic contexts

The number of orders $d$ for which

$$
\operatorname{Ram}_d(V)>0
$$

is at most

$$
\operatorname{span}(W_V).
$$

More strongly,

$$
\boxed{
\sum_d\operatorname{Ram}_d(V)
\le
\operatorname{span}(W_V).
}
$$

#### Proof

Use $\varphi(d)\ge1$ in Theorem 5.3. ∎

---

# 6. Mandatory content and residual ramification

A polynomial space may ramify because every member contains a common factor. This mandatory base content must be separated from genuine cancellation among the residual germs.

## 6.1 Cyclotomic common depth

### Definition 6.1 — Common cyclotomic depth

For every $d\ge1$, define

$$
\boxed{
 c_d(V)
=
\min_{0\ne f\in V}v_{\Phi_d}(f).
}
$$

Equivalently, if

$$
a_0(d)<a_1(d)<\cdots<a_{m-1}(d)
$$

is the vanishing sequence at a primitive $d$-th root, then

$$
\boxed{c_d(V)=a_0(d).}
$$

The cyclotomic common-content polynomial is

$$
\boxed{
C_V^{\mathrm{cyc}}(q)
=
\prod_{d\ge1}\Phi_d(q)^{c_d(V)}.
}
$$

Only finitely many factors occur because any basis member has finite degree.

Every element of $V$ is divisible by $C_V^{\mathrm{cyc}}$. Define the residual space

$$
\boxed{
U
=
\bigl(C_V^{\mathrm{cyc}}\bigr)^{-1}V.
}
$$

## 6.2 Residual vanishing sequence

At context $d$, multiplication by $\Phi_d^{c_d}$ shifts every vanishing order upward by $c_d$. Thus the residual sequence is

$$
\boxed{
 b_i(d)=a_i(d)-c_d(V).
}
$$

It satisfies

$$
0=b_0(d)<b_1(d)<\cdots<b_{m-1}(d).
$$

### Definition 6.2 — Residual ramification

Define

$$
\boxed{
\rho_d(V)
=
\sum_{i=0}^{m-1}\bigl(b_i(d)-i\bigr).
}
$$

Then $\rho_d(V)\ge0$.

### Project Theorem 6.3 — Content–ramification decomposition

For every $d$,

$$
\boxed{
\operatorname{Ram}_d(V)
=
m c_d(V)+\rho_d(V).
}
$$

Moreover,

$$
\boxed{
W_V
=
\bigl(C_V^{\mathrm{cyc}}\bigr)^mW_U
}
$$

up to a nonzero scalar.

#### Proof

Since

$$
a_i(d)=c_d+b_i(d),
$$

we have

$$
\begin{aligned}
\operatorname{Ram}_d(V)
&=
\sum_i(a_i(d)-i)\\
&=
\sum_i(c_d+b_i(d)-i)\\
&=
m c_d+\rho_d(V).
\end{aligned}
$$

The Wronskian factorization follows from the common-factor law, Lemma 3.3. ∎

### Project Theorem 6.4 — Global content–residual budget

$$
\boxed{
\sum_{d\ge1}
\varphi(d)
\bigl(mc_d(V)+\rho_d(V)\bigr)
\le
\operatorname{span}(W_V).
}
$$

Equivalently,

$$
\boxed{
 m\deg C_V^{\mathrm{cyc}}
+
\sum_d\varphi(d)\rho_d(V)
\le
\operatorname{span}(W_V).
}
$$

After removing the common cyclotomic content,

$$
\boxed{
\sum_d\varphi(d)\rho_d(V)
\le
\operatorname{span}(W_U).
}
$$

#### Proof

Insert Theorem 6.3 into Theorem 5.3. Since every cyclotomic polynomial has nonzero constant term,

$$
\operatorname{span}
\left(
(C_V^{\mathrm{cyc}})^mW_U
\right)
=
m\deg C_V^{\mathrm{cyc}}
+
\operatorname{span}(W_U).
$$

This gives the residual form. ∎

### Interpretation 6.5

The quantity

$$
m c_d(V)
$$

is unavoidable. It is the Wronskian cost of forcing all $m$ basis directions through the common factor $\Phi_d^{c_d}$.

The quantity

$$
\rho_d(V)
$$

measures the excess beyond this mandatory content. It records genuine higher-order dependence among the residual local germs.

---

# 7. The global jet-rank budget

Combine the cumulative rank-defect formula from Theorem 2.5 with the global cyclotomic budget.

### Project Theorem 7.1 — Global cyclotomic jet-rank budget

For every rational $m$-dimensional Laurent-polynomial space $V$,

$$
\boxed{
\sum_{d\ge1}\varphi(d)
\sum_{r\ge1}
\left(
\min(m,r)-\operatorname{rank}J_{d,r}
\right)
\le
\operatorname{span}(W_V).
}
$$

Here $J_{d,r}$ is the order-$r$ Euler-jet map at one primitive $d$-th root.

If $V\subseteq\mathcal A_{L,N}$, then

$$
\boxed{
\sum_{d\ge1}\varphi(d)
\sum_{r\ge1}
\left(
\min(m,r)-\operatorname{rank}J_{d,r}
\right)
\le
m(N-m+1).
}
$$

#### Proof

For each $d$, Theorem 2.5 identifies the inner sum with $\operatorname{Ram}_d(V)$. Apply Theorem 5.3. ∎

## 7.1 Truncated lower bounds

Exact ramification requires all ranks until the jet map becomes injective. Any finite truncation already gives a certified lower bound.

### Corollary 7.2 — Finite rank-defect lower bound

For arbitrary depths $R_d\ge1$,

$$
\boxed{
\sum_d\varphi(d)
\sum_{r=1}^{R_d}
\left(
\min(m,r)-\operatorname{rank}J_{d,r}
\right)
\le
\operatorname{span}(W_V).
}
$$

## 7.2 Dependence from excessive local degeneracy

Let

$$
F_1,\ldots,F_m\in\mathcal A_{L,N}
$$

be compressed or explicit Laurent polynomials. They are not assumed independent.

For each context and depth, form the jet matrix

$$
\mathcal J_{d,r}
=
\left(D^jF_i(\zeta_d)\right)_{
\substack{0\le j<r\\1\le i\le m}}.
$$

### Algorithmic Theorem 7.3 — Global rank-obstruction certificate

If a finite set of exact jet-rank calculations satisfies

$$
\boxed{
\sum_d\varphi(d)
\sum_{r=1}^{R_d}
\left(
\min(m,r)-\operatorname{rank}\mathcal J_{d,r}
\right)
>
m(N-m+1),
}
$$

then

$$
\boxed{F_1,\ldots,F_m\text{ are linearly dependent}.}
$$

#### Proof

Assume the $F_i$ were independent. Their span would be an $m$-dimensional subspace of $\mathcal A_{L,N}$, and the matrix ranks would equal the ranks of its jet maps. Corollary 7.2 would bound the displayed sum by $m(N-m+1)$, contradicting the strict inequality. ∎

### Caution 7.4 — Nature of the certificate

The theorem certifies dependence from excessive distributed degeneracy. It is not needed when a direct coefficient-space dependence test is already cheap.

Its value is greatest when:

- the polynomials have enormous expanded degree or support;
- exact local jets are available from compressed CCA formulas;
- several cyclotomic contexts each reveal only partial rank loss;
- no single local matrix is sufficient by itself.

---

# 8. Rank-one and rank-two specializations

## 8.1 Rank one recovers Part VIII

Let

$$
V=\operatorname{span}\{P\}.
$$

Then

$$
a_0(d)=v_{\Phi_d}(P),
$$

so

$$
\operatorname{Ram}_d(V)=v_{\Phi_d}(P).
$$

The Wronskian is

$$
W_V=P.
$$

Therefore Theorem 5.3 becomes exactly

$$
\boxed{
\sum_d\varphi(d)v_{\Phi_d}(P)
\le
\operatorname{span}(P),
}
$$

which is the Global Cyclotomic Contact Budget of Part VIII.

Thus Part VIII is precisely the rank-one case of the present theorem.

## 8.2 Rank two and excess collision order

Let

$$
V=\operatorname{span}\{F,G\}
$$

with $F,G$ linearly independent. At a primitive $d$-th root, write the vanishing sequence as

$$
a_0<a_1.
$$

Then

$$
\boxed{
\operatorname{Ram}_d(V)=a_0+a_1-1.
}
$$

The common depth is

$$
c_d=a_0,
$$

and the residual sequence is

$$
0,\ell,
\qquad
\ell=a_1-a_0\ge1.
$$

Hence

$$
\boxed{
\operatorname{Ram}_d(V)
=
2c_d+(\ell-1),
}
$$

and

$$
\boxed{
\rho_d(V)=\ell-1.
}
$$

### Interpretation 8.1

The first residual cancellation is forced by dimension: among two residual germs, one nonzero combination always cancels the constant term. This produces residual order at least one.

Ramification measures only the excess beyond this dimension-forced cancellation. Therefore:

- residual order $\ell=1$ contributes no residual ramification;
- residual order $\ell=2$ costs one unit;
- residual order $\ell=r$ costs $r-1$ units.

## 8.3 Simple collisions are unramified

Suppose

$$
F(\zeta_d)=G(\zeta_d)\ne0
$$

and

$$
 v_{\Phi_d}(F-G)=1.
$$

Then $F$ has order zero and $F-G$ has order one. Hence the vanishing sequence is

$$
0,1,
$$

so

$$
\boxed{
\operatorname{Ram}_d(\operatorname{span}\{F,G\})=0.
}
$$

This gives a geometric reinterpretation of the Simple-Collision Theorem from Part II:

$$
\boxed{
\text{a simple pairwise collision is not exceptional ramification;}
}
$$

it is exactly the generic order-one cancellation forced inside a two-dimensional local space.

Higher pairwise collision order is the first genuinely ramified event.

## 8.4 Global two-space collision budget

For any independent pair,

$$
\boxed{
\sum_d\varphi(d)
\left(
2c_d(V)+\ell_d-1
\right)
\le
\operatorname{span}(W(F,G)).
}
$$

Thus deep pairwise collisions at many contexts cannot occur independently. Their excess orders share one global Wronskian budget.

---

# 9. Gaussian-row ramification

Fix

$$
n\ge0
$$

and distinct lower-half positions

$$
0\le k_1<\cdots<k_m
\le
\left\lfloor\frac n2\right\rfloor.
$$

Set

$$
G_i(q)={n\brack k_i}_q,
\qquad
E_i=k_i(n-k_i).
$$

Part XIV proved that these polynomials are linearly independent and that their first $m$ Euler jets at $q=1$ have a nonzero exact Vandermonde determinant.

Let

$$
V_{n,\mathbf k}
=
\operatorname{span}_{\mathbb Q}\{G_1,\ldots,G_m\}.
$$

## 9.1 The positive endpoint is unramified

### Project Corollary 9.1 — Gaussian unramifiedness at $q=1$

The vanishing sequence of $V_{n,\mathbf k}$ at $q=1$ is

$$
\boxed{0,1,\ldots,m-1.}
$$

Therefore

$$
\boxed{
\operatorname{Ram}_1(V_{n,\mathbf k})=0.
}
$$

Equivalently,

$$
\boxed{W_{V_{n,\mathbf k}}(1)\ne0.}
$$

#### Proof

Part XIV proved that the first $m$ Euler jets form an invertible matrix. By Corollary 4.2, this is equivalent to unramifiedness. ∎

### Interpretation 9.2

Part XIV is the statement that the Gaussian row occupies the open osculating Schubert cell at the positive endpoint.

The present theorem shows what that local rigidity means globally: the context $d=1$ consumes none of the Gaussian space's ramification budget, leaving every unit of the budget to other roots and to the endpoints $0$ and $\infty$.

## 9.2 Exact Gaussian Wronskian degree

The degrees

$$
E_1<\cdots<E_m
$$

are distinct. Therefore they are the upper exponent sequence:

$$
\beta_i=E_{i+1}
$$

if indices are shifted to $0\le i<m$.

Let

$$
0\le\alpha_0<\cdots<\alpha_{m-1}
$$

be the lower exponent sequence at $q=0$.

### Project Theorem 9.3 — Global Gaussian-row ramification budget

$$
\boxed{
\sum_{d\ge1}
\varphi(d)\operatorname{Ram}_d(V_{n,\mathbf k})
\le
\sum_{i=1}^{m}E_i
-
\sum_{j=0}^{m-1}\alpha_j.
}
$$

In particular,

$$
\boxed{
\sum_{d\ge1}
\varphi(d)\operatorname{Ram}_d(V_{n,\mathbf k})
\le
\sum_{i=1}^{m}E_i-\binom m2.
}
$$

Moreover,

$$
\boxed{
\deg W_{V_{n,\mathbf k}}
=
\sum_{i=1}^{m}E_i-\binom m2.
}
$$

#### Proof

Apply Theorem 5.3 and Corollary 4.3. Since the $\alpha_j$ are distinct nonnegative integers,

$$
\sum_j\alpha_j\ge\binom m2.
$$

The degree formula follows from the upper exponent sequence. ∎

This theorem is global and all-context. It does not require the one-parameter Gaussian cumulant collapse to persist away from $q=1$.

## 9.3 Stable central blocks

Assume the stable range

$$
t\ge5,
\qquad
n\ge3t-2.
$$

Let

$$
K_{n,t}
=
\left\{t,t+1,\ldots,\left\lfloor\frac n2\right\rfloor\right\},
$$

and let

$$
m=|K_{n,t}|.
$$

Define the full distinct central-block space

$$
\boxed{
V_{n,t}
=
\operatorname{span}
\left\{
{n\brack k}_q:k\in K_{n,t}
\right\}.
}
$$

Part II proved that its common polynomial content is

$$
\boxed{
C_{n,t}(q)
=
\prod_{d=n-t+1}^{n}\Phi_d(q).
}
$$

Set

$$
\boxed{
L_{n,t}
=
\deg C_{n,t}
=
\sum_{d=n-t+1}^{n}\varphi(d).
}
$$

For every terminal context

$$
n-t+1\le d\le n,
$$

one has

$$
c_d(V_{n,t})=1.
$$

For every other $d$,

$$
c_d(V_{n,t})=0.
$$

### Project Theorem 9.4 — Stable content–ramification decomposition

Let

$$
E_k=k(n-k).
$$

Then

$$
\boxed{
 mL_{n,t}
+
\sum_{d\ge1}\varphi(d)\rho_d(V_{n,t})
\le
\operatorname{span}(W_{V_{n,t}}).
}
$$

After dividing the entire space by $C_{n,t}$,

$$
R_{n,t,k}(q)
=
\frac{{n\brack k}_q}{C_{n,t}(q)},
$$

one obtains

$$
\boxed{
\sum_{d\ge1}\varphi(d)\rho_d(V_{n,t})
\le
\sum_{k\in K_{n,t}}\bigl(E_k-L_{n,t}\bigr)
-
\sum_{j=0}^{m-1}\alpha_j,
}
$$

where $\alpha_j$ is the lower exponent sequence of the residual space. In particular,

$$
\boxed{
\sum_{d\ge1}\varphi(d)\rho_d(V_{n,t})
\le
\sum_{k\in K_{n,t}}\bigl(E_k-L_{n,t}\bigr)
-
\binom m2.
}
$$

#### Proof

The common-depth statement is exactly the Stable Content Theorem of Part II. Apply Theorem 6.4.

The factor $C_{n,t}$ has constant term one and degree $L_{n,t}$. Dividing by it lowers every upper degree by $L_{n,t}$ and preserves local orders at $q=0$, because it is a unit there. Therefore the residual upper degrees are

$$
E_k-L_{n,t},
$$

and the residual lower sequence is $(\alpha_j)$. Apply Theorem 5.3 to the residual space. ∎

### Interpretation 9.5

Part II gives the exact mandatory contribution

$$
\boxed{mL_{n,t}.}
$$

Part XV shows that every additional higher-order dependency among the primitive residual germs must fit inside the remaining Wronskian span.

Thus stable content and higher collision geometry are no longer separate statements. They are two summands in one conserved global quantity.

## 9.4 First-block simple collisions

Let

$$
n=Md-1,
\qquad
M\ge2,
$$

and choose

$$
0\le i<j\le d-1.
$$

When the Part II collision congruence

$$
2d\mid(i-j)(d-i-j-1)
$$

holds, the two Gaussian values agree at a primitive $d$-th root and their difference has exact $\Phi_d$-valuation one.

Therefore

$$
\boxed{
\operatorname{Ram}_d
\left(
\operatorname{span}
\left\{
{n\brack i}_q,{n\brack j}_q
\right\}
\right)
=0.
}
$$

This places the Simple-Collision Theorem at the bottom of the global hierarchy:

$$
\boxed{
\text{simple collision}
=
\text{dimension-forced cancellation}
=
\text{zero excess ramification}.
}
$$

---

# 10. Osculating Schubert geometry

The ramification weight has an intrinsic Grassmannian meaning.

Let

$$
A_N=\mathbb Q[q]_{\le N}.
$$

At a point $p\in\mathbb P^1$, define the osculating flag by vanishing order:

$$
\mathcal F_p^{r}
=
\{f\in A_N:\operatorname{ord}_p(f)\ge r\}.
$$

For finite $p$, this flag has codimension $r$ for $0\le r\le N+1$. At infinity, use sections of $\mathcal O(N)$.

An $m$-plane $V$ has vanishing sequence

$$
a_0(p)<\cdots<a_{m-1}(p).
$$

### Classical Theorem 10.1 — Schubert codimension of a vanishing sequence

The locus of $m$-planes whose vanishing sequence at $p$ is at least

$$
a_0<\cdots<a_{m-1}
$$

has Schubert codimension

$$
\boxed{
\sum_{i=0}^{m-1}(a_i-i).
}
$$

Thus

$$
\boxed{
\operatorname{Ram}_p(V)
=
\text{osculating Schubert codimension of }V\text{ at }p.
}
$$

#### Proof

Choose coordinates adapted to the complete flag

$$
A_N=\mathcal F_p^0\supset\mathcal F_p^1\supset\cdots.
$$

A row-echelon matrix representing $V$ has pivot positions $a_0,\ldots,a_{m-1}$. Relative to the open cell with pivot positions $0,1,\ldots,m-1$, shifting pivot $i$ from $i$ to $a_i$ imposes $a_i-i$ independent zero conditions. Summing gives the Schubert codimension. ∎

### Project Corollary 10.2 — Cyclotomic Schubert budget

For a rational $m$-plane in a width-$N$ Laurent window,

$$
\boxed{
\sum_{d\ge1}\varphi(d)
\operatorname{codim}
\bigl(	ext{osculating Schubert condition at }\zeta_d\bigr)
\le
\dim\operatorname{Gr}(m,N+1).
}
$$

The sharper affine bound replaces the Grassmannian dimension by

$$
\sum_i(\beta_i-\alpha_i).
$$

### Interpretation 10.3

A rational polynomial space cannot satisfy independently prescribed exceptional osculation conditions at arbitrarily many cyclotomic points.

Each primitive order contributes its Schubert codimension at all Galois-conjugate roots, hence the factor

$$
\varphi(d).
$$

The total weighted codimension cannot exceed the dimension of the Grassmannian in which the space moves.

---

# 11. Cyclotomic Grassmannian reconstruction

Part IX proved that a cyclotomic jet schedule of total weight at least the ambient polynomial dimension determines every individual polynomial. The same map determines every polynomial subspace.

## 11.1 Ambient jet map

Choose a finite set $\mathcal D$ and depths $r_d\ge1$. Put

$$
\boxed{
B
=
\sum_{d\in\mathcal D}\varphi(d)r_d.
}
$$

Define

$$
\boxed{
\mathcal J:
\mathcal A_{L,N}
\longrightarrow
\bigoplus_{d\in\mathcal D}
\mathbb Q(\zeta_d)^{r_d}
}
$$

by collecting the prescribed Euler jets.

By cyclotomic Hermite interpolation, if

$$
B\ge N+1,
$$

then $\mathcal J$ is injective.

### Project Theorem 11.1 — Grassmannian finite determination

Assume

$$
B\ge N+1.
$$

Then the induced map

$$
\boxed{
\operatorname{Gr}(m,\mathcal A_{L,N})
\longrightarrow
\operatorname{Gr}
\left(
 m,
\bigoplus_{d\in\mathcal D}
\mathbb Q(\zeta_d)^{r_d}
\right),
\qquad
V\longmapsto\mathcal J(V),
}
$$

is injective.

Thus an $m$-dimensional polynomial space is uniquely determined by the row space of any cyclotomic jet matrix whose ambient weighted budget is at least $N+1$.

#### Proof

Let $V_1,V_2$ satisfy

$$
\mathcal J(V_1)=\mathcal J(V_2).
$$

For $f\in V_1$, the vector $\mathcal J(f)$ lies in $\mathcal J(V_2)$, so there exists $g\in V_2$ with

$$
\mathcal J(f)=\mathcal J(g).
$$

Injectivity of $\mathcal J$ gives $f=g$, hence $V_1\subseteq V_2$. By symmetry, $V_2\subseteq V_1$. ∎

### Corollary 11.2 — Optimal exact reconstruction

If

$$
B=N+1,
$$

then the ambient jet map is a vector-space isomorphism onto its target. Every $m$-plane in the polynomial window corresponds bijectively to an $m$-plane in the exact jet-coordinate space.

### Algorithmic Theorem 11.3 — Subspace reconstruction

Given:

1. a Laurent window $\mathcal A_{L,N}$;
2. a cyclotomic jet schedule with $B\ge N+1$;
3. an exact basis for the image subspace $\mathcal J(V)$;

one reconstructs $V$ by applying the Part IX inverse Hermite map to every image-basis vector and taking their span.

#### Proof

The inverse exists on the image because $\mathcal J$ is injective. Exact local-to-residue conversion and Chinese-remainder reconstruction recover each polynomial basis vector. The resulting span maps back to the supplied image subspace and is unique by Theorem 11.1. ∎

### Caution 11.4 — Reconstruction versus ramification

The ambient reconstruction budget

$$
N+1
$$

and the Wronskian ramification budget

$$
m(N-m+1)
$$

serve different purposes.

- $N+1$ is the number of scalar coordinates required to reconstruct one polynomial and therefore the ambient space.
- $m(N-m+1)$ is the dimension of the Grassmannian and the total amount of exceptional osculation available to an $m$-plane.

They coincide only in special ranks.

---

# 12. Sharpness and extremal spaces

The universal cyclotomic budget is exact.

Let

$$
M(q)
=
\prod_{d\in\mathcal D}\Phi_d(q)^{r_d}
$$

be any nonzero cyclotomic product, and put

$$
R=\deg M
=
\sum_{d\in\mathcal D}\varphi(d)r_d.
$$

Fix $m\ge1$ and define

$$
\boxed{
V
=
M(q)\mathbb Q[q]_{<m}
=
\operatorname{span}
\{M,qM,\ldots,q^{m-1}M\}.
}
$$

This space lies in

$$
\mathbb Q[q]_{\le N},
\qquad
N=R+m-1.
$$

### Sharpness Theorem 12.1 — Universal budget saturation

For the space above:

1. at every selected context $d$,
   $$
   a_i(d)=r_d+i;
   $$
2. therefore
   $$
   \operatorname{Ram}_d(V)=mr_d;
   $$
3. the Wronskian is
   $$
   \boxed{W_V(q)=c_mM(q)^m}
   $$
   for a nonzero rational constant $c_m$;
4. and
   $$
   \boxed{
   \sum_d\varphi(d)\operatorname{Ram}_d(V)
   =mR
   =m(N-m+1).
   }
   $$

Thus the bound in Theorem 5.3 cannot be improved.

#### Proof

At a root of $M$ of multiplicity $r_d$, multiplication by $M$ shifts the vanishing sequence of

$$
\mathbb Q[q]_{<m}
$$

from

$$
0,1,\ldots,m-1
$$

to

$$
r_d,r_d+1,\ldots,r_d+m-1.
$$

Hence

$$
\operatorname{Ram}_d(V)
=
\sum_{i=0}^{m-1}r_d
=mr_d.
$$

The Wronskian common-factor law gives

$$
W_V=M^mW(1,q,\ldots,q^{m-1}).
$$

The final Wronskian is the nonzero constant

$$
\prod_{j=0}^{m-1}j!.
$$

Finally,

$$
N-m+1=R,
$$

so

$$
\sum_d\varphi(d)mr_d
=mR
=m(N-m+1).
$$

∎

### Interpretation 12.2

The extremizer spends the entire Grassmannian budget on mandatory cyclotomic content. It has:

- no ramification at $0$;
- no ramification at $\infty$;
- no noncyclotomic ramification;
- zero residual ramification after the common factor is removed.

Thus even the pure-content part of the theorem is already sharp in every rank.

---

# 13. Exact certificates and computation

## 13.1 Local ramification certificate

A local ramification certificate at context $d$ may consist of either:

1. an adapted basis with certified vanishing orders
   $$
   a_0<\cdots<a_{m-1};
   $$
2. the ranks
   $$
   \operatorname{rank}J_{d,r}
   $$
   through the first depth at which the rank reaches $m$;
3. the exact valuation
   $$
   v_{\Phi_d}(W_V).
   $$

The three forms are equivalent by Theorems 2.5 and 5.2.

## 13.2 Global budget certificate

A global certificate records:

- the ambient width $N$;
- the rank $m$;
- optionally the sharper endpoint sequences $\alpha_i,\beta_i$;
- selected contexts and exact jet ranks;
- the accumulated weighted defect.

A verifier checks

$$
\sum_d\varphi(d)
\sum_r
\left(
\min(m,r)-\operatorname{rank}J_{d,r}
\right)
\le
\sum_i(\beta_i-\alpha_i).
$$

Violation certifies linear dependence or an incorrect claimed jet packet.

## 13.3 Common-content certificate

For a structured space with known common cyclotomic content, a certificate records

$$
(d,c_d(V))
$$

for every nonzero common depth. The mandatory Wronskian contribution is

$$
\boxed{
m\sum_d\varphi(d)c_d(V).}
$$

Residual jet ranks are then checked against the reduced budget.

## 13.4 Gaussian-row certificate

For a selected Gaussian row, Part XIV supplies an immediate independence certificate:

$$
W_V(1)
e0.
$$

Part XV supplements it with a global consistency certificate:

$$
\sum_d\varphi(d)\operatorname{Ram}_d(V)
\le
\sum_iE_i-\sum_j\alpha_j.
$$

In a stable central block, Part II supplies the exact common-content charge

$$
mL_{n,t}.
$$

The three chapters therefore produce a proof-carrying package:

$$
\boxed{
\text{exact content}
+
\text{one-point independence}
+
\text{all-context ramification budget}.
}
$$

## 13.5 Complexity boundary

The chapter proves exact algebraic certificates. It does not claim that every generic Wronskian can be expanded in bit-polynomial time.

For compressed factorial families, local CCA formulas may compute the required jets without expansion. The total running time then depends on:

- the number of basis terms;
- the number of queried contexts;
- the maximum jet depth;
- exact arithmetic in the relevant cyclotomic fields;
- the bit size of the materialized certificate.

The budget theorem is independent of the implementation chosen for these local calculations.

---

# 14. Boundaries and exact status

## 14.1 Classical versus project content

The following ingredients are classical:

- Wronskian covariance and the common-factor law;
- the local Wronskian order formula;
- the projective total-ramification formula;
- the Schubert codimension of a vanishing sequence.

The project contribution of this chapter is their exact integration with CCA:

- grouping ramification by cyclotomic order;
- the Galois weight $\varphi(d)$;
- the common-content/residual decomposition;
- the cumulative cyclotomic jet-rank budget;
- the collision reinterpretation;
- the stable Gaussian content charge;
- the combination with Part XIV's Gaussian Jet–Vandermonde rigidity;
- exact compressed certificate design.

No external priority claim is made for the classical Wronskian identities themselves.

## 14.2 Characteristic zero

The proof uses:

- nonvanishing of ordinary Vandermonde determinants;
- the equivalence between Wronskian nonvanishing and linear independence;
- separability of cyclotomic polynomials;
- Galois conjugacy of primitive roots.

In positive characteristic, Wronskians may vanish for independent families, and the theorem requires Hasse derivatives or divided-power replacements.

## 14.3 Rationality

For a space over $\mathbb Q$, ramification at one primitive $d$-th root propagates with the same weight to every primitive conjugate. This is what produces the factor

$$
\varphi(d).
$$

For a space defined only over a larger field, the local Wronskian theorem remains true, but the Galois-weighted cyclotomic grouping must be modified according to the field of definition.

## 14.4 Ambient window

The universal quantity

$$
m(N-m+1)
$$

depends on the chosen minimal support window. Enlarging the window introduces artificial ramification capacity at infinity.

For the sharpest statement, use the smallest Laurent interval containing the entire space, or use the exact endpoint-sequence bound

$$
\sum_i(\beta_i-\alpha_i).
$$

## 14.5 Ramification does not identify the space

The Wronskian and its ramification divisor do not, in general, uniquely determine a polynomial subspace. The Wronski map may have several fibers.

Subspace reconstruction in Section 11 uses the full ambient cyclotomic jet image, not merely the Wronskian.

## 14.6 Pairwise versus arbitrary-rank data

Pairwise collision depths do not determine the full ramification sequence when $m\ge3$. Higher-rank jet minors contain genuinely new information.

The correct arbitrary-rank invariant is the complete vanishing sequence, equivalently the cumulative jet-rank defect.

---

# 15. Theorem inventory

| No. | Result | Status | Main consequence |
|---:|---|---|---|
| 1.3 | Endpoint adapted bases | Classical lemma | Defines lower and upper exponent sequences |
| 2.2 | Local adapted basis | Classical lemma | Produces the vanishing sequence |
| 2.5 | Cumulative jet-rank defect | New project theorem | Expresses ramification entirely through finite jet ranks |
| 3.3 | Wronskian common-factor law | Classical lemma | Common content contributes with rank multiplier $m$ |
| 3.4 | Euler–ordinary Wronskian relation | Project lemma | Transfers Wronskian geometry to CCA Euler jets |
| 4.1 | Local Wronskian order | Classical theorem | Ramification equals Wronskian multiplicity |
| 4.5 | Projective Wronskian conservation | Classical theorem | Total ramification equals $m(N-m+1)$ |
| 4.7 | Nonzero affine ramification budget | New project theorem | Exact span of the Wronskian controls all nonzero points |
| 5.2 | Cyclotomic Wronskian valuation | Main project theorem | $v_{\Phi_d}(W_V)=\operatorname{Ram}_d(V)$ |
| 5.3 | Global Cyclotomic Grassmann–Wronskian Budget | Main project theorem | Global all-context arbitrary-rank bound |
| 5.4 | Cyclotomic/noncyclotomic decomposition | New project theorem | Identifies the exact missing budget |
| 6.3 | Content–ramification decomposition | Main project theorem | $\operatorname{Ram}_d=mc_d+\rho_d$ |
| 6.4 | Global content–residual budget | Main project theorem | Unifies mandatory factors and exceptional cancellation |
| 7.1 | Global cyclotomic jet-rank budget | Main project theorem | Bounds cumulative rank loss over all contexts |
| 7.3 | Global rank-obstruction certificate | Algorithmic theorem | Excess local degeneracy certifies dependence |
| 8.1 | Rank-two excess law | Corollary | Simple collisions have zero residual ramification |
| 9.1 | Gaussian unramifiedness at $q=1$ | Corollary of Part XIV | Embeds Jet–Vandermonde rigidity into the global theory |
| 9.3 | Global Gaussian-row ramification budget | New project theorem | Controls all cyclotomic contexts of a selected row |
| 9.4 | Stable content–ramification decomposition | New project theorem | Charges Part II content against the Wronskian budget |
| 10.1 | Schubert codimension formula | Classical theorem | Gives the Grassmannian meaning of ramification |
| 10.2 | Cyclotomic Schubert budget | New project corollary | Weighted osculation cannot exceed Grassmannian dimension |
| 11.1 | Grassmannian finite determination | New project theorem | Full cyclotomic jet images determine polynomial spaces |
| 12.1 | Universal budget saturation | Sharpness theorem | Proves the bound is exact in every rank |

---

# 16. Final synthesis

Part II established the first exact Gaussian collision layer:

$$
\boxed{
\text{pairwise root collision}
\longrightarrow
\text{simple or higher cyclotomic contact}.
}
$$

Part VIII established the global rank-one law:

$$
\boxed{
\text{one polynomial}
\longrightarrow
\text{weighted cyclotomic contact}
\le
\text{support span}.
}
$$

Part XIV established optimal arbitrary-rank rigidity at one distinguished context:

$$
\boxed{
\text{Gaussian row at }q=1
\longrightarrow
\text{vanishing sequence }0,1,\ldots,m-1.
}
$$

Part XV places all three inside one exact geometric object: the Wronskian of the polynomial space.

At every point,

$$
\boxed{
\operatorname{Ram}_p(V)
=
\operatorname{ord}_pW_V.
}
$$

Globally,

$$
\boxed{
\sum_{p\in\mathbb P^1}
\operatorname{Ram}_p(V)
=
m(N-m+1).
}
$$

At cyclotomic points,

$$
\boxed{
 v_{\Phi_d}(W_V)
=
\operatorname{Ram}_d(V).
}
$$

Therefore

$$
\boxed{
\sum_d\varphi(d)\operatorname{Ram}_d(V)
\le
\sum_i(\beta_i-\alpha_i)
\le
m(N-m+1).
}
$$

The local invariant admits three exactly equivalent forms:

$$
\boxed{
\begin{aligned}
\operatorname{Ram}_d(V)
&=
\sum_i(a_i(d)-i)\\
&=
 v_{\Phi_d}(W_V)\\
&=
\sum_{r\ge1}
\bigl(\min(m,r)-\operatorname{rank}J_{d,r}\bigr).
\end{aligned}
}
$$

After separating common content,

$$
\boxed{
\operatorname{Ram}_d(V)
=
m c_d(V)+\rho_d(V).
}
$$

Thus the entire theory now has a common conservation law:

$$
\boxed{
\text{mandatory cyclotomic depth}
+
\text{higher local cancellation}
+
\text{noncyclotomic ramification}
+
\text{endpoint ramification}
=
\text{Grassmannian dimension}.
}
$$

For Gaussian blocks, this means:

$$
\boxed{
\text{Part II content}
+
\text{Part XIV one-point rigidity}
+
\text{all remaining root-of-unity degeneracy}
\subseteq
\text{one exact Wronskian divisor}.
}
$$

The theory has therefore moved from arithmetic of individual coefficients and pairwise collisions to the global cyclotomic geometry of an entire polynomial space.

---

## End of Part XV
