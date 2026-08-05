# Cyclotomic Coefficient Arithmetic

## Part VIII — Global Cyclotomic Contact Budget and Finite Determination

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete theorem chapter  
**Scope:** Global conservation of cyclotomic contact, weighted contact spectra, sharp finite determination by root-of-unity jets, bounded-span identity certificates, compressed span bounds, Gaussian-multinomial rigidity, and mixed-order differential cyclic-sieving rigidity.

---

# 0. Purpose, dependencies, and the new theorem

Parts I–IV developed a local theory. At one primitive root of unity $\zeta_d$, the multiplicity

$$
v_{\Phi_d}(P)
$$

is simultaneously:

1. the exponent of the cyclotomic factor $\Phi_d(q)$;
2. the order of vanishing of $P$ at $q=\zeta_d$;
3. the number of initial Euler jets that vanish;
4. for a difference $F-G$, the order to which the two local germs agree.

Parts VI–VII converted this local theory into exact certificates. A remaining question was global:

> Can a nonzero polynomial have arbitrarily deep contact at arbitrarily many cyclotomic contexts?

The answer is no. Every cyclotomic context consumes polynomial span. The cost of one unit of contact at context $d$ is exactly

$$
\deg \Phi_d=\varphi(d).
$$

This yields the new global law:

$$
\boxed{
\sum_{d\ge1}\varphi(d)\,v_{\Phi_d}(P)
\le
\operatorname{span}(P).
}
$$

Applied to $P=F-G$, it becomes a finite-determination theorem:

$$
\boxed{
\sum_{d\in\mathcal D}\varphi(d)r_d>N
\quad\Longrightarrow\quad
F=G,
}
$$

provided $\operatorname{span}(F-G)\le N$ and the first $r_d$ Euler jets of $F$ and $G$ agree at each selected context $d$.

Thus the local theory closes globally:

$$
\boxed{
\text{local contact depths}
\longrightarrow
\text{finite global budget}
\longrightarrow
\text{finite identity determination}.
}
$$

The labels used below are:

- **Classical lemma:** standard algebraic input, proved here.
- **Project theorem:** a theorem established in this project.
- **Corollary:** a formal consequence.
- **Sharpness statement:** an example proving that a bound cannot be improved in its stated generality.
- **Software corollary:** an exact computational consequence.

Throughout, coefficients are rational unless explicitly stated otherwise. This hypothesis is essential when one primitive root is used to represent its entire Galois orbit.

---

# 1. Laurent span and support geometry

The correct global size measure is not always ordinary degree. Multiplying by a monomial changes degree but does not change any cyclotomic contact. The invariant quantity is support span.

## 1.1 Lower and upper exponents

Let

$$
P(q)=\sum_{j=L}^{U}a_jq^j\in\mathbb Q[q,q^{-1}],
$$

where

$$
a_L\ne0,
\qquad
a_U\ne0.
$$

Define

$$
\operatorname{low}(P)=L,
\qquad
\operatorname{high}(P)=U.
$$

### Definition 1.1 — Laurent span

For nonzero $P$, define

$$
\boxed{
\operatorname{span}(P)
=
\operatorname{high}(P)-\operatorname{low}(P).
}
$$

Set

$$
\operatorname{span}(0)=-\infty
$$

only as a formal convention; every budget theorem below treats the zero polynomial separately.

For an ordinary polynomial,

$$
\operatorname{low}(P)=v_q(P),
$$

so

$$
\boxed{
\operatorname{span}(P)=\deg P-v_q(P).
}
$$

### Lemma 1.2 — Monomial normalization

Let $P\ne0$, and put

$$
L=\operatorname{low}(P),
\qquad
\widetilde P(q)=q^{-L}P(q).
$$

Then

$$
\boxed{
\widetilde P\in\mathbb Q[q],
\qquad
\widetilde P(0)\ne0,
\qquad
\deg \widetilde P=\operatorname{span}(P).
}
$$

Moreover, for every $d\ge1$,

$$
\boxed{
v_{\Phi_d}(\widetilde P)=v_{\Phi_d}(P).
}
$$

#### Proof

By definition of $L$, every exponent in $q^{-L}P$ is nonnegative, and the coefficient of $q^0$ is $a_L\ne0$. Its highest exponent is $U-L$, which is the span.

Every cyclotomic polynomial has nonzero constant term:

$$
\Phi_d(0)=\pm1.
$$

Hence $q$ is coprime to $\Phi_d$, and multiplication by the Laurent monomial $q^{-L}$ does not change the $\Phi_d$-valuation. ∎

### Lemma 1.3 — Hull bound for a difference

Let $F,G\in\mathbb Q[q,q^{-1}]$. Define their support hull width by

$$
H(F,G)
=
\max\bigl(\operatorname{high}(F),\operatorname{high}(G)\bigr)
-
\min\bigl(\operatorname{low}(F),\operatorname{low}(G)\bigr).
$$

If $F\ne G$, then

$$
\boxed{
\operatorname{span}(F-G)\le H(F,G).
}
$$

#### Proof

Every exponent occurring in $F-G$ lies in the union of the supports of $F$ and $G$, hence inside the displayed hull interval. Cancellation can shrink the support but cannot enlarge it. ∎

---

# 2. The Global Cyclotomic Contact Budget

For a nonzero Laurent polynomial $P$, define its cyclotomic contact profile by

$$
c_d(P)=v_{\Phi_d}(P),
\qquad d\ge1.
$$

Every $c_d(P)$ is a nonnegative integer.

### Definition 2.1 — Global cyclotomic contact budget

Define

$$
\boxed{
\mathfrak C(P)
=
\sum_{d\ge1}\varphi(d)c_d(P).
}
$$

The sum will be proved finite.

## 2.1 Main budget theorem

### Project Theorem 2.2 — Global Cyclotomic Contact Budget

Let

$$
0\ne P(q)\in\mathbb Q[q,q^{-1}].
$$

Then only finitely many $c_d(P)$ are nonzero, and

$$
\boxed{
\sum_{d\ge1}\varphi(d)v_{\Phi_d}(P)
\le
\operatorname{span}(P).
}
$$

Equivalently,

$$
\boxed{
\mathfrak C(P)\le\operatorname{span}(P).
}
$$

#### Proof

Use Lemma 1.2 to write

$$
P(q)=q^L\widetilde P(q),
$$

where

$$
\widetilde P\in\mathbb Q[q],
\qquad
\widetilde P(0)\ne0,
\qquad
\deg\widetilde P=\operatorname{span}(P).
$$

The cyclotomic valuations of $P$ and $\widetilde P$ are equal.

Factor from $\widetilde P$ all its cyclotomic factors:

$$
\widetilde P(q)
=
\left(
\prod_{d\ge1}\Phi_d(q)^{c_d(P)}
\right)R(q),
$$

where $R(q)\in\mathbb Q[q]$ has no cyclotomic factor. Because $\widetilde P$ has finite degree, only finitely many irreducible factors occur, so only finitely many $c_d(P)$ are nonzero.

Cyclotomic polynomials are pairwise distinct irreducible polynomials in $\mathbb Q[q]$, hence pairwise coprime. Therefore the degree of their product is the sum of their degrees:

$$
\deg
\prod_{d\ge1}\Phi_d(q)^{c_d(P)}
=
\sum_{d\ge1}c_d(P)\deg\Phi_d.
$$

Since

$$
\deg\Phi_d=\varphi(d),
$$

we obtain

$$
\deg
\prod_{d\ge1}\Phi_d(q)^{c_d(P)}
=
\sum_{d\ge1}\varphi(d)c_d(P).
$$

This product divides $\widetilde P$, so its degree cannot exceed $\deg\widetilde P$. Hence

$$
\sum_{d\ge1}\varphi(d)c_d(P)
\le
\deg\widetilde P
=
\operatorname{span}(P).
$$

∎

## 2.2 Equality characterization

### Project Theorem 2.3 — Saturation of the contact budget

For nonzero $P\in\mathbb Q[q,q^{-1}]$, equality

$$
\mathfrak C(P)=\operatorname{span}(P)
$$

holds if and only if

$$
\boxed{
P(q)
=
cq^L
\prod_{d\in S}\Phi_d(q)^{m_d}
}
$$

for some

$$
c\in\mathbb Q^\times,
\qquad
L\in\mathbb Z,
\qquad
m_d\in\mathbb Z_{>0},
$$

and some finite set $S$.

#### Proof

Using the factorization from the proof of Theorem 2.2,

$$
P(q)
=q^L
\left(
\prod_d\Phi_d(q)^{c_d(P)}
\right)R(q).
$$

The span of $P$ is

$$
\deg\widetilde P
=
\sum_d\varphi(d)c_d(P)+\deg R.
$$

Therefore equality in the budget holds exactly when

$$
\deg R=0.
$$

That is, $R$ is a nonzero rational constant. This gives the stated form. The converse is immediate by taking degrees. ∎

### Interpretation 2.4 — Contact as a conserved resource

One unit of contact at a primitive $d$-th-root context consumes

$$
\varphi(d)
$$

units of span because the same contact occurs at all $\varphi(d)$ primitive conjugate roots.

A nonzero polynomial cannot spend more contact than its support geometry permits.

## 2.3 Root-of-unity multiplicity interpretation

Let

$$
\mu_\omega(P)
$$

be the ordinary zero multiplicity of $P$ at a root of unity $\omega\ne0$.

### Corollary 2.5 — Total root-of-unity zero multiplicity

For nonzero $P\in\mathbb Q[q,q^{-1}]$,

$$
\boxed{
\mathfrak C(P)
=
\sum_{\omega\text{ a root of unity}}
\mu_\omega(P).
}
$$

Consequently,

$$
\boxed{
\sum_{\omega\text{ a root of unity}}
\mu_\omega(P)
\le
\operatorname{span}(P).
}
$$

#### Proof

For every $d$, the polynomial $\Phi_d$ has exactly $\varphi(d)$ distinct primitive $d$-th roots. Because $P$ has rational coefficients, all primitive roots of the same order occur with the common multiplicity

$$
v_{\Phi_d}(P).
$$

Thus the total multiplicity contributed by order $d$ is

$$
\varphi(d)v_{\Phi_d}(P).
$$

Summing over $d$ gives $\mathfrak C(P)$, and Theorem 2.2 gives the inequality. ∎

## 2.4 Immediate exclusions

### Corollary 2.6 — Impossible high-degree context

If

$$
\varphi(d)>\operatorname{span}(P),
$$

then

$$
\boxed{
v_{\Phi_d}(P)=0.}
$$

#### Proof

If the valuation were positive, its contribution alone to the global budget would be at least $\varphi(d)$, contradicting Theorem 2.2. ∎

### Corollary 2.7 — Bound on the number of collision contexts

The number of indices $d$ for which

$$
\Phi_d\mid P
$$

is at most $\operatorname{span}(P)$.

More strongly,

$$
\boxed{
\sum_{d\ge1}v_{\Phi_d}(P)
\le
\operatorname{span}(P).
}
$$

#### Proof

Since $\varphi(d)\ge1$,

$$
\sum_dv_{\Phi_d}(P)
\le
\sum_d\varphi(d)v_{\Phi_d}(P)
\le
\operatorname{span}(P).
$$

The number of positive summands is no larger than their sum. ∎

---

# 3. The global collision spectrum of two polynomials

Let

$$
F,G\in\mathbb Q[q,q^{-1}].
$$

If $F\ne G$, define their order-$d$ contact by

$$
\boxed{
\operatorname{cont}_d(F,G)
=
v_{\Phi_d}(F-G).
}
$$

If $F=G$, set every contact depth to $+\infty$.

By Part I, for a primitive $d$-th root $\zeta_d$,

$$
\operatorname{cont}_d(F,G)\ge r
$$

if and only if

$$
D^jF(\zeta_d)=D^jG(\zeta_d)
\qquad
(0\le j<r),
$$

where

$$
D=q\frac d{dq}.
$$

### Project Theorem 3.1 — Global Collision Spectrum Bound

If $F\ne G$, then

$$
\boxed{
\sum_{d\ge1}
\varphi(d)\operatorname{cont}_d(F,G)
\le
\operatorname{span}(F-G).
}
$$

Hence also

$$
\boxed{
\sum_{d\ge1}
\varphi(d)\operatorname{cont}_d(F,G)
\le
H(F,G).
}
$$

#### Proof

Apply Theorem 2.2 to the nonzero Laurent polynomial

$$
P=F-G.
$$

Then apply Lemma 1.3. ∎

### Interpretation 3.2

The local collision hierarchy cannot grow independently at different roots of unity. Every extra matched jet at order $d$ spends another $\varphi(d)$ units from one finite global budget.

Thus a collision may be:

- deep at a few contexts;
- shallow at many contexts;
- or distributed between them;

but the weighted total cannot exceed the span of the difference.

## 3.1 Endpoint savings

The span of $F-G$ can be much smaller than a naive degree bound because endpoint coefficients may already agree.

### Proposition 3.3 — Low- and high-coefficient savings

Let

$$
F,G\in\mathbb Q[q]
$$

have degree at most $N$. Suppose their coefficients agree in the first $s$ positions:

$$
[q^j]F=[q^j]G
\qquad(0\le j<s),
$$

and in the last $t$ positions relative to the common degree ceiling $N$:

$$
[q^{N-j}]F=[q^{N-j}]G
\qquad(0\le j<t).
$$

If $F\ne G$, then

$$
\boxed{
\operatorname{span}(F-G)
\le
N-s-t.
}
$$

Consequently,

$$
\boxed{
\sum_d\varphi(d)\operatorname{cont}_d(F,G)
\le
N-s-t.
}
$$

#### Proof

The low-coefficient agreement implies

$$
v_q(F-G)\ge s.
$$

The high-coefficient agreement implies

$$
\deg(F-G)\le N-t.
$$

Therefore

$$
\operatorname{span}(F-G)
=
\deg(F-G)-v_q(F-G)
\le
(N-t)-s.
$$

Apply Theorem 3.1. ∎

### Corollary 3.4 — Common constant term

If $F$ and $G$ have degree at most $N$ and the same constant term, then for $F\ne G$,

$$
\boxed{
\mathfrak C(F-G)\le N-1.
}
$$

### Corollary 3.5 — Common constant and leading terms

If $F$ and $G$ both have degree exactly $N$, the same constant term, and the same leading coefficient, then for $F\ne G$,

$$
\boxed{
\mathfrak C(F-G)\le N-2.
}
$$

These endpoint credits become important for reciprocal and Gaussian polynomials, which are typically monic with constant term $1$.

---

# 4. Finite Cyclotomic Determination

The budget theorem converts local jet agreement into a complete global identity test.

## 4.1 Arbitrary mixed-depth schedule

Let

$$
\mathcal D\subset\mathbb Z_{\ge1}
$$

be finite. For every $d\in\mathcal D$, choose an integer

$$
r_d\ge1
$$

and one primitive $d$-th root $\zeta_d$.

### Project Theorem 4.1 — Finite Cyclotomic Determination Theorem

Let

$$
F,G\in\mathbb Q[q,q^{-1}]
$$

and suppose a known integer $N\ge0$ satisfies

$$
\operatorname{span}(F-G)\le N
$$

whenever $F\ne G$. Assume that for every $d\in\mathcal D$,

$$
D^jF(\zeta_d)=D^jG(\zeta_d)
\qquad
(0\le j<r_d).
$$

If

$$
\boxed{
\sum_{d\in\mathcal D}\varphi(d)r_d>N,
}
$$

then

$$
\boxed{F=G.}
$$

#### Proof

Assume for contradiction that $F\ne G$, and put

$$
P=F-G.
$$

For each $d\in\mathcal D$, the first $r_d$ Euler derivatives of $P$ vanish at $\zeta_d$:

$$
D^jP(\zeta_d)=0
\qquad(0\le j<r_d).
$$

By the local cyclotomic jet criterion from Part I,

$$
v_{\Phi_d}(P)\ge r_d.
$$

Therefore

$$
\begin{aligned}
\mathfrak C(P)
&=
\sum_{e\ge1}\varphi(e)v_{\Phi_e}(P)\\
&\ge
\sum_{d\in\mathcal D}\varphi(d)v_{\Phi_d}(P)\\
&\ge
\sum_{d\in\mathcal D}\varphi(d)r_d\\
&>N.
\end{aligned}
$$

But the Global Cyclotomic Contact Budget gives

$$
\mathfrak C(P)
\le
\operatorname{span}(P)
\le N,
$$

which is a contradiction. Hence $F=G$. ∎

## 4.2 Divisibility proof

The theorem also admits a direct global factor proof.

For each $d\in\mathcal D$, jet agreement implies

$$
\Phi_d(q)^{r_d}\mid F(q)-G(q).
$$

The factors are pairwise coprime, so

$$
\prod_{d\in\mathcal D}\Phi_d(q)^{r_d}
\mid F(q)-G(q).
$$

The divisor has degree

$$
\sum_{d\in\mathcal D}\varphi(d)r_d>N.
$$

After removing a Laurent monomial from $F-G$, the remaining polynomial has degree at most $N$. A nonzero polynomial cannot be divisible by a polynomial of larger degree. Therefore the difference is zero.

This second proof shows that finite determination is a cyclotomic Hermite interpolation theorem.

## 4.3 Sharpness

### Project Theorem 4.2 — Sharpness at exact budget

The strict inequality in Theorem 4.1 is optimal.

Let $\mathcal D$ and $r_d\ge1$ be arbitrary, and define

$$
M(q)
=
\prod_{d\in\mathcal D}\Phi_d(q)^{r_d}.
$$

Then

$$
\operatorname{span}(M)
=
\sum_{d\in\mathcal D}\varphi(d)r_d,
$$

and for every selected context,

$$
D^jM(\zeta_d)=0
\qquad(0\le j<r_d),
$$

but

$$
M\ne0.
$$

Thus equality

$$
\sum_{d\in\mathcal D}\varphi(d)r_d=N
$$

cannot force a polynomial of span $N$ to vanish.

#### Proof

Each $\Phi_d^{r_d}$ divides $M$, so the required jets vanish by the local jet criterion. The constant term of every cyclotomic polynomial is nonzero, so $M(0)\ne0$, and therefore its span equals its degree. Pairwise coprimeness gives

$$
\deg M
=
\sum_d r_d\deg\Phi_d
=
\sum_d\varphi(d)r_d.
$$

Finally, $M$ is plainly nonzero. ∎

### Interpretation 4.3

The theorem is not merely sufficient up to a loose constant. The budget threshold is exact:

$$
\boxed{
\text{weighted contact capacity}>\text{possible span}
}
$$

is precisely the universal point at which nonidentity becomes impossible.

---

# 5. Rectangular determination grids

A convenient special case uses all contexts up to some order and the same number of derivatives at each context.

Define the summatory totient function

$$
\boxed{
T(D)=\sum_{d=1}^{D}\varphi(d).
}
$$

The number $T(D)$ is exactly the number of roots of unity whose exact order is at most $D$.

## 5.1 Uniform jet depth

### Corollary 5.1 — Rectangular finite-determination criterion

Let $F,G\in\mathbb Q[q,q^{-1}]$, and suppose

$$
\operatorname{span}(F-G)\le N
$$

when $F\ne G$. Fix integers

$$
D\ge1,
\qquad
R\ge0.
$$

For every $1\le d\le D$, let $\zeta_d$ be primitive of order $d$. If

$$
D^jF(\zeta_d)=D^jG(\zeta_d)
$$

for all

$$
1\le d\le D,
\qquad
0\le j\le R,
$$

and

$$
\boxed{
(R+1)T(D)>N,
}
$$

then

$$
\boxed{F=G.}
$$

#### Proof

Apply Theorem 4.1 with

$$
r_d=R+1
$$

for every $d\le D$. ∎

### Corollary 5.2 — Values-only determination

If

$$
F(\zeta_d)=G(\zeta_d)
\qquad(1\le d\le D)
$$

and

$$
\boxed{T(D)>N,}
$$

then $F=G$.

Thus higher derivatives are not logically required for finite determination. Their value is computational: they let a small number of cheap contexts replace a much larger set of root evaluations.

### Corollary 5.3 — Single-context determination

Fix one context $d$. If

$$
D^jF(\zeta_d)=D^jG(\zeta_d)
\qquad(0\le j\le R)
$$

and

$$
\boxed{
(R+1)\varphi(d)>N,
}
$$

then $F=G$.

At $d=1$, this recovers ordinary finite Taylor determination at $q=1$.

## 5.2 The first distinguishing context

Define

$$
\boxed{
D_N
=
\min\{D:T(D)>N\}.
}
$$

### Project Corollary 5.4 — First distinguishing cyclotomic context

If $F\ne G$ and

$$
\operatorname{span}(F-G)\le N,
$$

then there exists some

$$
1\le d\le D_N
$$

such that

$$
\boxed{
F(\zeta_d)\ne G(\zeta_d).
}
$$

#### Proof

If the values agreed for every $d\le D_N$, Corollary 5.2 would imply equality because

$$
T(D_N)>N.
$$

∎

This is a complete finite root-of-unity identity test for bounded-span rational Laurent polynomials.

## 5.3 Elementary quadratic context bound

The exact threshold $D_N$ can be computed from totients. A simple universal estimate shows that only $O(\sqrt N)$ root orders are required in the values-only test.

### Lemma 5.5 — Elementary lower bound for the summatory totient

For every integer $D\ge1$,

$$
\boxed{
T(D)\ge\frac{D^2}{8}+\frac12.
}
$$

#### Proof

Let $C(D)$ be the number of ordered pairs

$$
(a,b)\in\{1,\ldots,D\}^2
$$

with

$$
\gcd(a,b)=1.
$$

Counting pairs with $a\le b$ and reflecting across the diagonal gives

$$
\boxed{
C(D)=2T(D)-1.
}
$$

Indeed, for each $b$, the number of $a$ with

$$
1\le a\le b,
\qquad
\gcd(a,b)=1
$$

is $\varphi(b)$, with the convention $\varphi(1)=1$. The only coprime diagonal pair is $(1,1)$, which is counted twice by reflection and must be subtracted once.

Now bound the noncoprime pairs. If $\gcd(a,b)>1$, then some prime $p$ divides both. By the union bound, the number of noncoprime ordered pairs is at most

$$
\sum_{p\le D}\left\lfloor\frac Dp\right\rfloor^2
\le
D^2\sum_{p\le D}\frac1{p^2}
\le
D^2\sum_{m=2}^{\infty}\frac1{m^2}.
$$

Using

$$
\frac1{m^2}
\le
\frac1{m(m-1)}
=
\frac1{m-1}-\frac1m
\qquad(m\ge3),
$$

we obtain

$$
\sum_{m=2}^{\infty}\frac1{m^2}
=
\frac14+
\sum_{m=3}^{\infty}\frac1{m^2}
\le
\frac14+\frac12
=
\frac34.
$$

Hence at least $D^2/4$ ordered pairs are coprime:

$$
C(D)\ge\frac{D^2}{4}.
$$

Since $C(D)=2T(D)-1$,

$$
T(D)
=
\frac{C(D)+1}{2}
\ge
\frac{D^2}{8}+\frac12.
$$

∎

### Corollary 5.6 — Explicit values-only context bound

If

$$
D^2>8N,
$$

then

$$
T(D)>N.
$$

Therefore any two rational Laurent polynomials whose difference has span at most $N$ are determined by their values at one primitive root of every order

$$
1\le d\le\lfloor\sqrt{8N}\rfloor+1.
$$

### Remark 5.7 — True asymptotic scale

The classical asymptotic

$$
T(D)
\sim
\frac{3}{\pi^2}D^2
$$

shows that the optimal values-only order cutoff is asymptotically

$$
D_N
\sim
\frac{\pi}{\sqrt3}\sqrt N.
$$

This asymptotic is not needed for any theorem in this chapter. The exact criterion is always $T(D)>N$.

---

# 6. Compressed span bounds

Finite determination requires a bound for $\operatorname{span}(F-G)$. For the structured families of this theory, such bounds are computable directly from compressed parameters.

## 6.1 One compressed factorial quotient

Let

$$
F(q)
=
q^\alpha
\prod_{m\ge1}(q;q)_m^{e_m},
$$

where only finitely many $e_m\in\mathbb Z$ are nonzero. Assume $F$ is a Laurent polynomial.

Define

$$
\delta(m)=\deg(q;q)_m
=1+2+\cdots+m
=\binom{m+1}{2}.
$$

### Project Theorem 6.1 — Exact compressed span formula

Under the polynomiality hypothesis,

$$
\boxed{
\operatorname{low}(F)=\alpha,
}
$$

$$
\boxed{
\operatorname{high}(F)
=
\alpha+
\sum_{m\ge1}e_m\binom{m+1}{2},
}
$$

and

$$
\boxed{
\operatorname{span}(F)
=
\sum_{m\ge1}e_m\binom{m+1}{2}.
}
$$

#### Proof

Put

$$
Q(q)=\prod_m(q;q)_m^{e_m}.
$$

Every $(q;q)_m$ has constant term $1$. Hence the rational function $Q$ has value $1$ at $q=0$. Since $Q$ is assumed to be a polynomial after cancellation, it has nonzero constant term $1$. Therefore

$$
\operatorname{low}(Q)=0
$$

and

$$
\operatorname{low}(F)=\alpha.
$$

The degree of a product or quotient of nonzero rational functions is additive, where the degree of a rational function is numerator degree minus denominator degree. Thus

$$
\deg Q
=
\sum_m e_m\deg(q;q)_m
=
\sum_m e_m\binom{m+1}{2}.
$$

Because $Q$ is a polynomial with nonzero constant term, this degree is its support span. Multiplication by $q^\alpha$ shifts both support endpoints by $\alpha$ and leaves span unchanged. ∎

### Software Corollary 6.2

The exact span of a polynomial compressed factorial quotient is computable using one multiplication and addition per canonical factor. No expansion is required.

## 6.2 Structured sums

Let

$$
P(q)=\sum_{i=1}^{s}c_iF_i(q),
\qquad
c_i\in\mathbb Q,
$$

where each $F_i$ is a Laurent polynomial with known support interval

$$
[L_i,U_i].
$$

### Proposition 6.3 — Hull span of a structured sum

If $P\ne0$, then

$$
\boxed{
\operatorname{span}(P)
\le
\max_iU_i-
\min_iL_i.
}
$$

#### Proof

Every monomial occurring in $P$ comes from at least one summand, so the support of $P$ is contained in the union of the summand support intervals and therefore in their convex hull. ∎

### Project Corollary 6.4 — Complete identity test for compressed sums

Let

$$
P(q)=\sum_{i=1}^{s}c_iF_i(q)
$$

be a rational linear combination of polynomial compressed factorial quotients. Compute the hull bound

$$
N=
\max_iU_i-
\min_iL_i
$$

from Theorem 6.1. If a finite cyclotomic jet schedule has total capacity

$$
\sum_{d\in\mathcal D}\varphi(d)r_d>N
$$

and all corresponding jets of $P$ vanish, then

$$
\boxed{P=0.}
$$

#### Proof

Proposition 6.3 gives $\operatorname{span}(P)\le N$ if $P\ne0$. Apply Theorem 4.1 to $P$ and the zero polynomial. ∎

### Significance

Part VI left open the problem of finding classes of structured sums for which finitely many cyclotomic certificates form a complete identity test. Theorem 4.1 and Corollary 6.4 solve that problem whenever a finite support-hull bound is available.

---

# 7. Gaussian and multinomial finite rigidity

Gaussian binomial and multinomial polynomials have especially simple endpoint geometry.

## 7.1 Degree and endpoints

For a composition

$$
\mathbf k=(k_1,\ldots,k_c),
\qquad
\sum_\nu k_\nu=n,
$$

write

$$
M_{\mathbf k}(q)
=
{n\brack k_1,\ldots,k_c}_q.
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

It is monic and has constant term $1$.

### Lemma 7.1 — Endpoint savings for multinomial differences

Let $M_{\mathbf k}\ne M_{\mathbf l}$, and put

$$
E_{\max}
=
\max(E(\mathbf k),E(\mathbf l)).
$$

Then

$$
\boxed{
\operatorname{span}
\left(M_{\mathbf k}-M_{\mathbf l}\right)
\le E_{\max}-1.
}
$$

If additionally

$$
E(\mathbf k)=E(\mathbf l)=E,
$$

then

$$
\boxed{
\operatorname{span}
\left(M_{\mathbf k}-M_{\mathbf l}\right)
\le E-2.
}
$$

#### Proof

Both multinomials have constant term $1$, so their difference has zero constant term and therefore $q$-order at least one. Its degree is at most $E_{\max}$. Hence its span is at most $E_{\max}-1$.

If the degrees are equal, both polynomials are monic, so their leading terms also cancel. The difference then has degree at most $E-1$ and $q$-order at least one, giving span at most $E-2$. ∎

## 7.2 Multinomial finite determination

### Project Theorem 7.2 — Gaussian-Multinomial Finite Determination

Let $\mathbf k$ and $\mathbf l$ be two compositions of the same integer $n$. Let $\mathcal D$ be finite, with jet depths $r_d\ge1$. Suppose

$$
D^jM_{\mathbf k}(\zeta_d)
=
D^jM_{\mathbf l}(\zeta_d)
$$

for every

$$
d\in\mathcal D,
\qquad
0\le j<r_d.
$$

If

$$
\boxed{
\sum_{d\in\mathcal D}\varphi(d)r_d
\ge E_{\max},
}
$$

then

$$
\boxed{
M_{\mathbf k}(q)=M_{\mathbf l}(q).
}
$$

If the two multinomials have the same degree $E$, the weaker threshold

$$
\boxed{
\sum_{d\in\mathcal D}\varphi(d)r_d
\ge E-1
}
$$

already forces equality.

#### Proof

Assume the multinomials are distinct. Lemma 7.1 gives

$$
\operatorname{span}(M_{\mathbf k}-M_{\mathbf l})
\le E_{\max}-1.
$$

The jet hypotheses imply

$$
v_{\Phi_d}(M_{\mathbf k}-M_{\mathbf l})\ge r_d.
$$

Therefore the global contact budget of the difference is at least

$$
\sum_{d\in\mathcal D}\varphi(d)r_d
\ge E_{\max},
$$

contradicting the upper bound $E_{\max}-1$.

In the equal-degree case, the span is at most $E-2$, while the assumed contact capacity is at least $E-1$, again a contradiction. ∎

## 7.3 Recovery of the content multiset

### Project Theorem 7.3 — Multinomial content rigidity

Under the hypotheses of Theorem 7.2, the multisets of positive content parts coincide:

$$
\boxed{
\{k_\nu:k_\nu>0\}
=
\{l_\mu:l_\mu>0\}
}
$$

with multiplicity.

Zero parts are invisible and may be inserted or removed.

#### Proof

Theorem 7.2 gives

$$
{n\brack k_1,\ldots,k_c}_q
=
{n\brack l_1,\ldots,l_s}_q.
$$

Cancel the common numerator $(q;q)_n$. Then

$$
\prod_\nu(q;q)_{k_\nu}
=
\prod_\mu(q;q)_{l_\mu}.
$$

For every positive integer $m$, let $a_m$ be the multiplicity of $m$ among the positive $k_\nu$, and let $b_m$ be the corresponding multiplicity among the positive $l_\mu$. Then

$$
\prod_{m\ge1}(q;q)_m^{a_m-b_m}=1.
$$

Assume some exponent differs, and let $M$ be the largest index with

$$
a_M-b_M\ne0.
$$

Take the $\Phi_M$-valuation. For $m<M$,

$$
v_{\Phi_M}((q;q)_m)
=
\left\lfloor\frac mM\right\rfloor
=0,
$$

while

$$
v_{\Phi_M}((q;q)_M)=1.
$$

There are no nonzero exponents above $M$. Hence the valuation of the left side is

$$
a_M-b_M\ne0,
$$

whereas the valuation of $1$ is zero. This is a contradiction. Therefore $a_m=b_m$ for every $m$, proving equality of the positive-part multisets. ∎

### Interpretation 7.4

A sufficiently large finite collection of local cyclotomic jets does not merely determine the multinomial polynomial. It determines the unordered content itself.

This is a global rigidity theorem built from local collision data.

---

# 8. Adaptive finite identity certificates

The finite-determination theorem suggests a two-sided exact algorithm.

## 8.1 Capacity of a jet query

A query asking for derivatives

$$
D^jF(\zeta_d),
\qquad 0\le j<r,
$$

at one primitive order-$d$ context has **contact capacity**

$$
\boxed{
\operatorname{cap}(d,r)=\varphi(d)r.
}
$$

If all queried jets match, this capacity is spent from the maximal possible contact budget of the difference.

## 8.2 Adaptive algorithm

```text
input:
    exact structured expressions F and G
    a certified span bound N for F-G
    a sequence of context/depth queries (d_1,r_1),(d_2,r_2),...

budget = 0

for each query (d,r):
    compute exact Euler jets of F and G at one primitive d-th root
    if a mismatch occurs at order j < r:
        return NONIDENTICAL with the local mismatch certificate
    budget += phi(d)*r
    if budget > N:
        return IDENTICAL with the finite-determination certificate
```

### Project Theorem 8.1 — Correctness and termination

Assume the query schedule eventually reaches cumulative capacity greater than $N$. Then the algorithm terminates and returns the correct answer.

#### Proof

If a mismatch occurs, then the two exact algebraic jet values differ, so $F\ne G$.

If no mismatch has occurred and the accumulated capacity exceeds $N$, all queried contacts hold to their requested depths. Theorem 4.1 then gives $F=G$.

If $F\ne G$, the Global Collision Spectrum Bound implies that matching contacts can consume at most $N$. Hence a schedule whose capacity eventually exceeds $N$ must encounter a mismatch before that point.

If $F=G$, every query matches, so the algorithm terminates when the capacity threshold is crossed. ∎

### Corollary 8.2 — Complete proof-carrying identity test

For compressed factorial-quotient sums with a computable hull bound, cyclotomic jet certificates form a complete deterministic identity test.

A nonidentity certificate consists of one exact mismatching jet. An identity certificate consists of:

1. a verified span bound $N$;
2. a list of exact matching jet records;
3. a capacity sum exceeding $N$.

The checker never needs to expand the polynomial.

## 8.3 Context-selection tradeoff

The theorem allows arbitrary mixtures of contexts and depths. Thus a system may trade:

- many low-degree fields and shallow jets;
- a few contexts and deep jets;
- binary contexts accelerated by parity;
- contexts selected by valuation imbalance or residue sparsity.

The mathematically relevant quantity is always

$$
\sum_d\varphi(d)r_d.
$$

The computationally optimal schedule depends on the cost of exact arithmetic in each cyclotomic field and on the structure of the input family.

---

# 9. Mixed-order differential cyclic-sieving rigidity

Part V proved that ordinary cyclic sieving gives one order of contact at every context dividing the group order, while higher-order differential CSP gives deeper contact. The global budget now supplies an exact rigidity criterion.

Let a cyclic group $C_N$ act on $X$, let $O_X(q)$ be the canonical orbit polynomial, and let $F(q)\in\mathbb Z[q]$ be a proposed graded polynomial.

For every $d\mid N$, define

$$
\delta_d(F,X)
=
v_{\Phi_d}(F-O_X).
$$

### Project Theorem 9.1 — Mixed-Order Differential CSP Rigidity

Let $\mathcal D$ be any finite set of positive integers, not necessarily all divisors of $N$. Suppose

$$
\delta_d(F,X)\ge r_d
\qquad(d\in\mathcal D).
$$

If a known bound $B$ satisfies

$$
\operatorname{span}(F-O_X)\le B
$$

when $F\ne O_X$, and

$$
\boxed{
\sum_{d\in\mathcal D}\varphi(d)r_d>B,
}
$$

then

$$
\boxed{F(q)=O_X(q).}
$$

#### Proof

Apply Theorem 4.1 to the pair $F,O_X$. ∎

### Corollary 9.2 — Uniform global differential CSP rigidity

If

$$
(q^N-1)^r\mid F(q)-O_X(q),
$$

then every divisor context $d\mid N$ has depth at least $r$. Since

$$
\sum_{d\mid N}\varphi(d)=N,
$$

the total guaranteed contact capacity is

$$
rN.
$$

Therefore, if

$$
\boxed{
\operatorname{span}(F-O_X)<rN,
}
$$

then

$$
\boxed{F=O_X.}
$$

#### Proof

Apply Theorem 9.1 with all $d\mid N$ and $r_d=r$. ∎

### Corollary 9.3 — Canonical remainder rigidity

Ordinary CSP gives $r=1$. Hence if $F$ exhibits CSP and

$$
\operatorname{span}(F-O_X)<N,
$$

then

$$
F=O_X.
$$

This recovers the uniqueness of the degree-$<N$ canonical representative and extends it to Laurent support-span bounds.

---

# 10. Families and common spacing

The budget also controls common cyclotomic collapse across an entire polynomial family.

Let

$$
\mathcal F=\{F_i:i\in I\}
\subseteq\mathbb Q[q,q^{-1}]
$$

be finite. Fix a basepoint $i_0$, and suppose every difference has hull span at most $N$:

$$
\operatorname{span}(F_i-F_{i_0})\le N
\qquad(i\in I).
$$

### Project Theorem 10.1 — Finite determination of a collapsing family

Suppose that for every $d\in\mathcal D$ and every $i\in I$,

$$
D^jF_i(\zeta_d)
=
D^jF_{i_0}(\zeta_d)
\qquad(0\le j<r_d).
$$

If

$$
\sum_{d\in\mathcal D}\varphi(d)r_d>N,
$$

then

$$
\boxed{
F_i=F_{i_0}
\quad\text{for every }i\in I.
}
$$

#### Proof

Apply Theorem 4.1 separately to every pair $(F_i,F_{i_0})$. ∎

### Corollary 10.2 — Budget for a nonzero spacing polynomial

Let $\Delta_{\mathcal F}$ be the monic gcd of all pairwise differences, and suppose it is nonzero. Then

$$
\boxed{
\sum_{d\ge1}\varphi(d)v_{\Phi_d}(\Delta_{\mathcal F})
\le
\operatorname{span}(\Delta_{\mathcal F}).
}
$$

This is Theorem 2.2 applied to the spacing polynomial itself.

---

# 11. Rationality, exactness, and boundaries

## 11.1 Why rational coefficients matter

For $P\in\mathbb Q[q]$, vanishing to order $r$ at one primitive $d$-th root implies divisibility by

$$
\Phi_d(q)^r.
$$

Hence one local check automatically represents all $\varphi(d)$ Galois-conjugate roots, producing the weight $\varphi(d)$.

Over a coefficient field that already distinguishes the primitive roots, contact at one selected root costs only its ordinary multiplicity, not automatically $\varphi(d)$. The correct global theorem over an algebraically closed field is then the total-zero-multiplicity bound over individually selected roots.

## 11.2 A span bound is indispensable

No fixed finite set of root-of-unity jets determines polynomials of unbounded span. Given any finite schedule, the nonzero product

$$
\prod_{d\in\mathcal D}\Phi_d(q)^{r_d}
$$

matches the zero polynomial to every requested order.

Finite determination becomes possible only after the admissible difference span is bounded.

## 11.3 Exact arithmetic is indispensable

Approximate numerical agreement at roots of unity does not prove exact jet equality. Every identity certificate must use:

- exact cyclotomic fields;
- exact residue-class arithmetic;
- symbolic factored residuals;
- or another mathematically exact representation.

## 11.4 The binary context

The global budget treats $d=2$ with weight

$$
\varphi(2)=1.
$$

The special even-germ theorem from Part IV does not alter the global degree cost. It alters which jet orders can be the first mismatch and can therefore reduce computation in an adaptive algorithm.

---

# 12. Sharp model examples

## 12.1 Mixed-depth saturation

Let

$$
P(q)=
\Phi_2(q)^3
\Phi_3(q)^2
\Phi_5(q).
$$

Then

$$
\operatorname{span}(P)
=
3\varphi(2)+2\varphi(3)+\varphi(5)
=3+4+4
=11.
$$

Its contact depths are

$$
c_2=3,
\qquad
c_3=2,
\qquad
c_5=1,
$$

and zero elsewhere. The global budget is saturated:

$$
\mathfrak C(P)=11.
$$

Thus eleven units of span can be distributed as three binary contacts, two cubic-context contacts, and one fifth-order context contact.

## 12.2 Sharp values-only grid

Let

$$
P_D(q)=\prod_{d=1}^{D}\Phi_d(q).
$$

Then

$$
\operatorname{span}(P_D)=T(D),
$$

and

$$
P_D(\zeta_d)=0
\qquad(1\le d\le D).
$$

Thus values at all primitive contexts up to order $D$ do not determine polynomials of span $T(D)$. The strict condition

$$
T(D)>N
$$

in Corollary 5.2 is exact.

## 12.3 Sharp single-context depth

For fixed $d,r$, the polynomial

$$
P(q)=\Phi_d(q)^r
$$

has span

$$
r\varphi(d)
$$

and agrees with zero through Euler order $r-1$ at a primitive $d$-th root. Hence the threshold

$$
r\varphi(d)>N
$$

in single-context determination is also sharp.

---

# 13. Theorem inventory

| No. | Result | Status | Main consequence |
|---:|---|---|---|
| 1.2 | Monomial normalization | Proved here | Replaces degree by Laurent span |
| 2.2 | Global Cyclotomic Contact Budget | New project theorem | Weighted total contact is bounded by span |
| 2.3 | Budget saturation characterization | New project theorem | Equality exactly for monomial times cyclotomic product |
| 2.5 | Total root-of-unity multiplicity | Corollary | Geometric meaning of the budget |
| 3.1 | Global Collision Spectrum Bound | New project theorem | Local collisions share one global resource |
| 3.3 | Endpoint savings | Proved here | Stronger budgets for normalized families |
| 4.1 | Finite Cyclotomic Determination | New project theorem | Sufficient matching jets force equality |
| 4.2 | Sharpness at exact budget | New project theorem | Strict threshold is optimal |
| 5.1 | Rectangular criterion | Corollary | Uniform context/jet identity test |
| 5.4 | First distinguishing context | Corollary | A mismatch occurs at finite bounded order |
| 5.5 | Elementary summatory-totient bound | Proved here | Values-only cutoff $O(\sqrt N)$ |
| 6.1 | Compressed span formula | New application theorem | Span without polynomial expansion |
| 6.4 | Complete identity test for structured sums | New application theorem | Closes finite-certificate completeness problem |
| 7.2 | Gaussian-Multinomial Finite Determination | New project theorem | Finite jets determine the polynomial |
| 7.3 | Multinomial content rigidity | New project theorem | Finite jets determine the positive-part multiset |
| 8.1 | Adaptive certificate correctness | New algorithm theorem | Two-sided terminating identity test |
| 9.1 | Mixed-order differential CSP rigidity | New project theorem | Enough local CSP depth forces canonical equality |
| 10.1 | Finite determination of a family | Corollary | A whole collapsing family must be constant |

---

# 14. Final synthesis

The previous theory was local:

$$
\boxed{
\operatorname{cont}_d(F,G)
=
\text{number of matching initial jets at context }d.
}
$$

The new theorem is global:

$$
\boxed{
\sum_d\varphi(d)\operatorname{cont}_d(F,G)
\le
\operatorname{span}(F-G)
\qquad(F\ne G).
}
$$

This turns local fingerprints into a complete finite logic.

A first mismatch proves inequality. If no mismatch occurs and the accumulated weighted contact exceeds the maximum possible span, equality is forced.

The complete chain is therefore

$$
\boxed{
\text{compressed expression}
\longrightarrow
\text{finite span bound}
\longrightarrow
\text{exact cyclotomic jets}
\longrightarrow
\text{weighted contact accumulation}
\longrightarrow
\text{identity or nonidentity certificate}.
}
$$

The decisive conceptual advance is:

$$
\boxed{
\text{cyclotomic contact is globally budgeted, not merely locally measurable.}
}
$$

And the decisive computational consequence is:

$$
\boxed{
\text{bounded-span structured polynomials are finitely determined by cyclotomic jets.}
}
$$
