# Cyclotomic Coefficient Arithmetic

## Part III — Multinomial Defects and Local Residual Geometry

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Theorem chapter; every theorem stated in this chapter is proved below.  
**Scope:** Gaussian multinomial coefficients, residue defects, exact cyclotomic depth, local factorial normal forms, leading transverse residuals, first visible Euler jets, Fourier-moment cancellation, universal defect cores, the binary subset stratum, and the complete regularized multinomial collision hierarchy.

---

## 0. Purpose, dependencies, and status conventions

Parts I and II established the general dictionary

$$
\text{cyclotomic divisibility}
\longleftrightarrow
\text{root-of-unity vanishing}
\longleftrightarrow
\text{agreement of Euler jets},
$$

and applied it to Gaussian binomial rows. This chapter moves from two-part Gaussian coefficients to arbitrary Gaussian multinomials.

The central new integer is the **residue defect**

$$
h
=
\frac{s_1+\cdots+s_c}{d},
$$

where the content parts are written

$$
k_\nu=r_\nu d+s_\nu,
\qquad
0\le s_\nu<d.
$$

The main theorem identifies three apparently different quantities:

$$
\boxed{
\text{residue defect}
=
\text{cyclotomic depth}
=
\text{first nonzero differential order}.
}
$$

More precisely, for a primitive $d$-th root $\zeta$,

$$
\boxed{
M_{\mathbf k}(q)
=
(q^d-1)^h
\left(
\mathcal R_d(\mathbf k;\zeta)+O(q-\zeta)
\right)
\quad\text{in the local ring at }q=\zeta.
}
$$

The labels used below are:

- **Classical lemma:** standard algebraic or enumerative input, proved here when used.
- **Project theorem:** a theorem established as part of this project.
- **Corollary:** a formal consequence of a proved theorem.
- **Caution:** a distinction required for mathematical and computational correctness.
- **Software corollary:** a direct exact-computation consequence.

No floating-point approximation to a root of unity is required anywhere in this chapter.

---

# 1. Gaussian multinomials and Euler jets

## 1.1 The $q$-factorial

For an integer $m\ge0$, define

$$
(q;q)_m
=
\prod_{j=1}^{m}(1-q^j),
\qquad
(q;q)_0=1.
$$

## 1.2 Gaussian multinomial coefficients

Let

$$
\mathbf k=(k_1,\ldots,k_c),
\qquad
k_\nu\ge0,
\qquad
k_1+\cdots+k_c=n.
$$

The Gaussian multinomial coefficient is

$$
{n\brack k_1,\ldots,k_c}_q
=
\frac{(q;q)_n}
{(q;q)_{k_1}\cdots(q;q)_{k_c}}.
$$

We abbreviate it by

$$
M_{\mathbf k}(q)
=
{n\brack k_1,\ldots,k_c}_q.
$$

It is invariant under permutation of the parts $k_1,\ldots,k_c$.

## 1.3 The Euler derivation

Define

$$
D=q\frac{d}{dq}.
$$

At a nonzero point $q=\zeta$, introduce the exponential local coordinate

$$
q=\zeta e^x.
$$

Then

$$
D=\frac{d}{dx}.
$$

Thus, for every function $F$ regular at $\zeta$,

$$
D^jF(\zeta)
=
\left.
\frac{d^j}{dx^j}F(\zeta e^x)
\right|_{x=0}.
$$

This is why Euler derivatives, rather than ordinary derivatives, are the natural jets at cyclotomic contexts.

---

# 2. Residue defects

Fix an integer

$$
d\ge2
$$

and suppose the total size is a multiple of $d$:

$$
n=ad.
$$

Write every content part uniquely as

$$
k_\nu=r_\nu d+s_\nu,
\qquad
r_\nu\ge0,
\qquad
0\le s_\nu<d.
$$

Because $\sum_\nu k_\nu=ad$,

$$
d\sum_{\nu=1}^{c}r_\nu
+
\sum_{\nu=1}^{c}s_\nu
=
ad.
$$

### Definition 2.1 — Residue defect

Define

$$
\boxed{
h
=
a-\sum_{\nu=1}^{c}r_\nu.}
$$

Equivalently,

$$
\boxed{
\sum_{\nu=1}^{c}s_\nu=hd.
}
$$

The vector

$$
\mathbf s=(s_1,\ldots,s_c)
$$

is the **residue content**, and $h$ is its defect.

### Lemma 2.2 — Integrality and bounds

The defect $h$ is an integer satisfying

$$
\boxed{0\le h\le c-1.}
$$

#### Proof

The relation

$$
\sum_\nu s_\nu=hd
$$

shows immediately that $h$ is an integer.

Each residue is nonnegative, so

$$
hd=\sum_\nu s_\nu\ge0,
$$

and hence $h\ge0$.

Also,

$$
\sum_\nu s_\nu
\le
c(d-1)
<
cd.
$$

Therefore $h<c$. Since $h$ is an integer,

$$
h\le c-1.
$$

This proves the bounds. ∎

### Corollary 2.3 — Zero defect

The following are equivalent:

1. $h=0$;
2. $s_\nu=0$ for every $\nu$;
3. every content part $k_\nu$ is divisible by $d$.

#### Proof

If $h=0$, then

$$
\sum_\nu s_\nu=0.
$$

Every $s_\nu$ is nonnegative, so every residue is zero. The converse is immediate. The equivalence with divisibility follows from

$$
k_\nu=r_\nu d+s_\nu.
$$

∎

### Interpretation 2.4 — Multi-carry defect

The residues $s_\nu$ add to a multiple $hd$. Thus $h$ counts the number of full copies of $d$ carried from the residue layer into the quotient layer when the parts $k_\nu$ are summed.

For a binomial coefficient there are only two residues, so $h\in\{0,1\}$. For a $c$-part multinomial, the defect can reach $c-1$, which is the source of genuinely higher-order cyclotomic vanishing.

---

# 3. The multinomial defect theorem

Part I proved the exact valuation

$$
v_{\Phi_d}\bigl((q;q)_m\bigr)
=
\left\lfloor\frac md\right\rfloor.
$$

We now apply it to a Gaussian multinomial.

### Project Theorem 3.1 — $q$-Multinomial Defect Theorem

Let

$$
n=ad,
\qquad
\mathbf k=(k_1,\ldots,k_c),
\qquad
\sum_\nu k_\nu=ad,
$$

and let $h$ be the residue defect from Definition 2.1. Then

$$
\boxed{
v_{\Phi_d}\left(
{ad\brack k_1,\ldots,k_c}_q
\right)=h.
}
$$

#### Proof

By additivity of cyclotomic valuation,

$$
\begin{aligned}
v_{\Phi_d}(M_{\mathbf k})
&=
v_{\Phi_d}\bigl((q;q)_{ad}\bigr)
-
\sum_{\nu=1}^{c}
v_{\Phi_d}\bigl((q;q)_{k_\nu}\bigr)\\
&=
\left\lfloor\frac{ad}{d}\right\rfloor
-
\sum_{\nu=1}^{c}
\left\lfloor\frac{k_\nu}{d}\right\rfloor.
\end{aligned}
$$

Since

$$
\left\lfloor\frac{ad}{d}\right\rfloor=a
$$

and

$$
\left\lfloor\frac{k_\nu}{d}\right\rfloor=r_\nu,
$$

we obtain

$$
v_{\Phi_d}(M_{\mathbf k})
=
a-\sum_\nu r_\nu
=
h.
$$

∎

### Corollary 3.2 — Exact root-of-unity vanishing criterion

For a primitive $d$-th root $\zeta$,

$$
M_{\mathbf k}(\zeta)\ne0
\iff
h=0
\iff
d\mid k_\nu\text{ for every }\nu.
$$

If $h>0$, then $M_{\mathbf k}(\zeta)=0$.

#### Proof

A rational-coefficient polynomial vanishes at a primitive $d$-th root exactly when it is divisible by $\Phi_d$. Apply Theorem 3.1 and Corollary 2.3. ∎

### Software Corollary 3.3 — Constant-size defect computation

The exact cyclotomic depth can be computed from the integer parts alone:

```text
r_nu = k_nu // d
s_nu = k_nu % d
h    = a - sum(r_nu)
```

Equivalently,

```text
h = sum(s_nu) // d
```

The running time depends on $c$ and on the bit lengths of the integers, not on the degree or coefficient count of the multinomial polynomial.

---

# 4. Root products and residue factors

Fix a primitive $d$-th root $\zeta$.

### Definition 4.1 — Partial root product

For $0\le s<d$, define

$$
A_s(\zeta)
=
\prod_{u=1}^{s}(1-\zeta^u),
\qquad
A_0(\zeta)=1.
$$

Since $1\le u<d$ implies $\zeta^u\ne1$, every $A_s(\zeta)$ is nonzero.

### Classical Lemma 4.2 — Complete root product

For a primitive $d$-th root $\zeta$,

$$
\boxed{
A_{d-1}(\zeta)
=
\prod_{u=1}^{d-1}(1-\zeta^u)
=
d.
}
$$

#### Proof

Factor

$$
x^d-1=(x-1)\prod_{u=1}^{d-1}(x-\zeta^u).
$$

After dividing by $x-1$,

$$
1+x+\cdots+x^{d-1}
=
\prod_{u=1}^{d-1}(x-\zeta^u).
$$

Set $x=1$. The left side is $d$, and the right side is

$$
\prod_{u=1}^{d-1}(1-\zeta^u).
$$

∎

### Lemma 4.3 — Conjugation phase

For $0\le s<d$,

$$
\boxed{
\overline{A_s(\zeta)}
=
(-1)^s
\zeta^{-s(s+1)/2}
A_s(\zeta).
}
$$

#### Proof

Because $\overline\zeta=\zeta^{-1}$,

$$
\begin{aligned}
\overline{A_s(\zeta)}
&=
\prod_{u=1}^{s}(1-\zeta^{-u})\\
&=
\prod_{u=1}^{s}
\bigl(-\zeta^{-u}(1-\zeta^u)\bigr)\\
&=
(-1)^s
\zeta^{-\sum_{u=1}^{s}u}
A_s(\zeta)\\
&=
(-1)^s
\zeta^{-s(s+1)/2}
A_s(\zeta).
\end{aligned}
$$

∎

### Lemma 4.4 — Complementary residue product

For $1\le s<d$,

$$
\boxed{
A_s(\zeta)A_{d-s}(\zeta)
=
(-1)^{s-1}
 d\,
\zeta^{\binom{s}{2}}
(1-\zeta^s).
}
$$

#### Proof

By Lemma 4.2,

$$
d
=
A_{d-1}(\zeta)
=
A_{d-s}(\zeta)
\prod_{u=d-s+1}^{d-1}(1-\zeta^u).
$$

Put $v=d-u$. Then $v=1,\ldots,s-1$, and

$$
\begin{aligned}
\prod_{u=d-s+1}^{d-1}(1-\zeta^u)
&=
\prod_{v=1}^{s-1}(1-\zeta^{-v})\\
&=
(-1)^{s-1}
\zeta^{-\binom{s}{2}}
A_{s-1}(\zeta).
\end{aligned}
$$

Therefore

$$
A_{d-s}(\zeta)
=
(-1)^{s-1}
 d\,
\zeta^{\binom{s}{2}}
A_{s-1}(\zeta)^{-1}.
$$

Multiplying by

$$
A_s(\zeta)=A_{s-1}(\zeta)(1-\zeta^s)
$$

gives the claimed identity. ∎

These products encode the complete residue dependence of the leading local multinomial term.

---

# 5. Local factorial normal form

The defect theorem gives the order of vanishing. The next theorem computes the exact leading local coefficient.

### Project Theorem 5.1 — Local Factorial Normal Form

Let

$$
m=rd+s,
\qquad
r\ge0,
\qquad
0\le s<d.
$$

For a primitive $d$-th root $\zeta$,

$$
\boxed{
\lim_{q\to\zeta}
\frac{(q;q)_{rd+s}}
{(1-q^d)^r}
=
r!\,d^r A_s(\zeta).
}
$$

The quotient is understood as a rational function regular at $q=\zeta$, or equivalently as an element of the local ring at $\zeta$.

#### Proof

Separate the factors in $(q;q)_{rd+s}$ according to their residue modulo $d$:

$$
\begin{aligned}
(q;q)_{rd+s}
&=
\prod_{j=1}^{r}(1-q^{jd})\\
&\quad\cdot
\prod_{t=0}^{r-1}
\prod_{u=1}^{d-1}(1-q^{td+u})\\
&\quad\cdot
\prod_{u=1}^{s}(1-q^{rd+u}).
\end{aligned}
$$

The first line contains the $r$ factors whose exponents are divisible by $d$. Divide those factors by $(1-q^d)^r$:

$$
\prod_{j=1}^{r}
\frac{1-q^{jd}}{1-q^d}
=
\prod_{j=1}^{r}
\left(1+q^d+\cdots+q^{(j-1)d}\right).
$$

As $q\to\zeta$, one has $q^d\to1$, so the $j$-th factor tends to $j$. Therefore the first normalized product tends to

$$
1\cdot2\cdots r=r!.
$$

For each complete nonzero-residue block indexed by $t$,

$$
\prod_{u=1}^{d-1}(1-q^{td+u})
\longrightarrow
\prod_{u=1}^{d-1}(1-\zeta^u)
=d
$$

by Lemma 4.2. There are $r$ such complete blocks, so they contribute $d^r$.

Finally,

$$
\prod_{u=1}^{s}(1-q^{rd+u})
\longrightarrow
\prod_{u=1}^{s}(1-\zeta^u)
=A_s(\zeta).
$$

Multiplying the three limits gives

$$
r!\,d^rA_s(\zeta).
$$

∎

### Corollary 5.2 — Compressed $q$-factorial quotient normal form

Let

$$
F(q)=q^\alpha\prod_{i=1}^{N}(q;q)_{m_i}^{\varepsilon_i},
\qquad
\alpha,\varepsilon_i\in\mathbb Z,
$$

and write

$$
m_i=r_i d+s_i,
\qquad
0\le s_i<d.
$$

Put

$$
H=\sum_{i=1}^{N}\varepsilon_i r_i.
$$

Then

$$
\boxed{
\lim_{q\to\zeta}
\frac{F(q)}{(1-q^d)^H}
=
\zeta^\alpha
\prod_{i=1}^{N}
\left(r_i!\,d^{r_i}A_{s_i}(\zeta)\right)^{\varepsilon_i}.
}
$$

#### Proof

Apply Theorem 5.1 to each factorial factor. Cyclotomic normalization is multiplicative, including negative exponents, because every normalized factor has a finite nonzero value at $\zeta$. Also $q^\alpha\to\zeta^\alpha$. ∎

This is the local computational engine for compressed $q$-factorial quotients.

---

# 6. Multinomial transverse residual

Return to

$$
M_{\mathbf k}(q)
=
{ad\brack k_1,\ldots,k_c}_q
$$

with defect $h$.

### Definition 6.1 — Leading local residual

Define the residual relative to the local parameter $q^d-1$ by

$$
\mathcal R_d(\mathbf k;\zeta)
=
\lim_{q\to\zeta}
\frac{M_{\mathbf k}(q)}{(q^d-1)^h}.
$$

The existence and exact value follow from the next theorem.

### Project Theorem 6.2 — Multinomial Local Residual Formula

With the notation above,

$$
\boxed{
\mathcal R_d(\mathbf k;\zeta)
=
(-1)^h d^h
\frac{a!}{\prod_{\nu=1}^{c}r_\nu!}
\frac{1}{\prod_{\nu=1}^{c}A_{s_\nu}(\zeta)}.
}
$$

In particular, the residual is nonzero.

#### Proof

Apply Theorem 5.1 to the numerator. Since

$$
ad=a\,d+0,
$$

we have

$$
\lim_{q\to\zeta}
\frac{(q;q)_{ad}}{(1-q^d)^a}
=
a!\,d^a.
$$

For each denominator factor,

$$
\lim_{q\to\zeta}
\frac{(q;q)_{k_\nu}}{(1-q^d)^{r_\nu}}
=
r_\nu!\,d^{r_\nu}A_{s_\nu}(\zeta).
$$

Taking the quotient gives

$$
\begin{aligned}
\lim_{q\to\zeta}
\frac{M_{\mathbf k}(q)}{(1-q^d)^h}
&=
\frac{a!d^a}
{\prod_\nu r_\nu!d^{r_\nu}A_{s_\nu}(\zeta)}\\
&=
d^{a-\sum_\nu r_\nu}
\frac{a!}{\prod_\nu r_\nu!}
\frac1{\prod_\nu A_{s_\nu}(\zeta)}\\
&=
d^h
\frac{a!}{\prod_\nu r_\nu!}
\frac1{\prod_\nu A_{s_\nu}(\zeta)}.
\end{aligned}
$$

Since

$$
q^d-1=-(1-q^d),
$$

we have

$$
(q^d-1)^h=(-1)^h(1-q^d)^h.
$$

Therefore

$$
\frac{1}{(q^d-1)^h}
=
(-1)^h\frac{1}{(1-q^d)^h},
$$

which supplies the factor $(-1)^h$. Every denominator factor $A_{s_\nu}(\zeta)$ is nonzero, so the residual is nonzero. ∎

### Corollary 6.3 — Local geometric normal form

In the local ring

$$
\mathscr O_\zeta
=
\mathbb Q(\zeta)[q]_{(q-\zeta)},
$$

one has

$$
\boxed{
M_{\mathbf k}(q)
=
(q^d-1)^hR_{\mathbf k,\zeta}(q),
\qquad
R_{\mathbf k,\zeta}(\zeta)
=
\mathcal R_d(\mathbf k;\zeta)\ne0.
}
$$

Equivalently,

$$
\boxed{
M_{\mathbf k}(q)
=
(q^d-1)^h
\left(
\mathcal R_d(\mathbf k;\zeta)+O(q-\zeta)
\right).
}
$$

#### Proof

Theorem 3.1 gives local order $h$. Since $q^d-1$ has a simple zero at $\zeta$, it is associated to $q-\zeta$ in the local ring. Division by $(q^d-1)^h$ therefore produces a local unit, whose value is the limit calculated in Theorem 6.2. ∎

### Caution 6.4 — Local division is not global divisibility

The expression

$$
\frac{M_{\mathbf k}(q)}{(q^d-1)^h}
$$

is generally **not** a polynomial in $\mathbb Q[q]$.

Globally,

$$
q^d-1
=
\prod_{e\mid d}\Phi_e(q).
$$

Theorem 3.1 guarantees only

$$
\Phi_d(q)^h\mid M_{\mathbf k}(q).
$$

It does not guarantee $\Phi_e(q)^h\mid M_{\mathbf k}(q)$ for proper divisors $e\mid d$. At the primitive $d$-th root $\zeta$, those other factors are nonzero and hence are units in $\mathscr O_\zeta$. That is exactly why division by $(q^d-1)^h$ is legitimate locally.

Any implementation must preserve this distinction.

### Corollary 6.5 — Galois covariance

Let $m$ be coprime to $d$, and let

$$
\sigma_m:\mathbb Q(\zeta)\to\mathbb Q(\zeta),
\qquad
\sigma_m(\zeta)=\zeta^m.
$$

Then

$$
\boxed{
\sigma_m\left(
\mathcal R_d(\mathbf k;\zeta)
\right)
=
\mathcal R_d(\mathbf k;\zeta^m).
}
$$

#### Proof

The rational and integer factors in Theorem 6.2 are fixed by $\sigma_m$, while

$$
\sigma_m(A_s(\zeta))
=
\prod_{u=1}^{s}(1-\zeta^{mu})
=
A_s(\zeta^m).
$$

Apply $\sigma_m$ to the residual formula. ∎

---

# 7. First visible jets

The local residual determines the first nonzero Euler derivative.

### Project Theorem 7.1 — First Visible Jet Theorem

Let $M_{\mathbf k}$ have defect $h$ at a primitive $d$-th root $\zeta$. Then

$$
\boxed{
D^jM_{\mathbf k}(\zeta)=0
\qquad
(0\le j<h),
}
$$

and

$$
\boxed{
\frac{D^hM_{\mathbf k}(\zeta)}{h!}
=
d^h\mathcal R_d(\mathbf k;\zeta).
}
$$

Consequently,

$$
\boxed{
\frac{D^hM_{\mathbf k}(\zeta)}{h!}
=
(-1)^h d^{2h}
\frac{a!}{\prod_\nu r_\nu!}
\frac1{\prod_\nu A_{s_\nu}(\zeta)}.
}
$$

#### Proof

Use the exponential coordinate

$$
q=\zeta e^x.
$$

Then

$$
q^d-1=e^{dx}-1=dx+O(x^2).
$$

By Corollary 6.3,

$$
M_{\mathbf k}(q)
=(q^d-1)^hR_{\mathbf k,\zeta}(q),
$$

with

$$
R_{\mathbf k,\zeta}(\zeta)
=
\mathcal R_d(\mathbf k;\zeta).
$$

Therefore

$$
\begin{aligned}
M_{\mathbf k}(\zeta e^x)
&=
\left(dx+O(x^2)\right)^h
\left(
\mathcal R_d(\mathbf k;\zeta)+O(x)
\right)\\
&=
d^h\mathcal R_d(\mathbf k;\zeta)x^h
+O(x^{h+1}).
\end{aligned}
$$

The coefficients of $x^0,\ldots,x^{h-1}$ vanish, while the coefficient of $x^h$ is

$$
d^h\mathcal R_d(\mathbf k;\zeta).
$$

Since $D=d/dx$, this coefficient equals

$$
\frac{D^hM_{\mathbf k}(\zeta)}{h!}.
$$

Substituting Theorem 6.2 gives the explicit formula. ∎

### Corollary 7.2 — Triple identification

$$
\boxed{
\begin{aligned}
h
&=
v_{\Phi_d}(M_{\mathbf k})\\
&=
\min\{j\ge0:D^jM_{\mathbf k}(\zeta)\ne0\}.
\end{aligned}
}
$$

#### Proof

The first equality is Theorem 3.1. The second follows from Theorem 7.1 and the nonvanishing of its explicit $h$-th derivative. ∎

### Corollary 7.3 — Zero-defect root value

If every $k_\nu$ is divisible by $d$, so that

$$
k_\nu=r_\nu d
\quad\text{and}\quad
\sum_\nu r_\nu=a,
$$

then

$$
\boxed{
M_{\mathbf k}(\zeta)
=
\frac{a!}{r_1!\cdots r_c!}.
}
$$

#### Proof

Here $h=0$, every $s_\nu=0$, and $A_0=1$. Theorem 7.1 at order zero gives the formula. ∎

### Combinatorial interpretation 7.4

Consider rotation of $ad$ positions by $a=ad/d$ places. This rotation has $a$ cycles of length $d$. A fixed word must be constant on each cycle, so every color count must be divisible by $d$. When $k_\nu=r_\nu d$, the number of fixed words is

$$
\frac{a!}{r_1!\cdots r_c!},
$$

matching Corollary 7.3.

---

# 8. Word enumerators and Fourier moments

The differential theorem has a direct enumerative meaning.

Let $\mathcal W(\mathbf k)$ be the set of words on the ordered alphabet

$$
1<2<\cdots<c
$$

with exactly $k_\nu$ occurrences of the letter $\nu$.

For a word $w=w_1\cdots w_n$, define

$$
\operatorname{inv}(w)
=
\#\{(i,j):i<j,\ w_i>w_j\}.
$$

### Classical Theorem 8.1 — Multiset inversion enumerator

$$
\boxed{
M_{\mathbf k}(q)
=
\sum_{w\in\mathcal W(\mathbf k)}
q^{\operatorname{inv}(w)}.
}
$$

#### Proof

We first prove the binary case. Let $B_{n,k}(q)$ be the inversion generating polynomial for binary words of length $n$ with $k$ ones and $n-k$ zeros, where an inversion is a pair $1$ before $0$.

Partition such words according to their last symbol.

- If the last symbol is $1$, deleting it leaves a binary word of length $n-1$ with $k-1$ ones, and creates no new inversion.
- If the last symbol is $0$, deleting it leaves a binary word of length $n-1$ with $k$ ones. The deleted zero lies after all $k$ ones and therefore contributes exactly $k$ new inversions.

Hence

$$
B_{n,k}(q)
=
B_{n-1,k-1}(q)
+
q^kB_{n-1,k}(q).
$$

The Gaussian binomial coefficients satisfy the same recurrence

$$
{n\brack k}_q
=
{n-1\brack k-1}_q
+
q^k{n-1\brack k}_q,
$$

with the same boundary conditions

$$
B_{n,0}=B_{n,n}=1,
\qquad
{n\brack0}_q={n\brack n}_q=1.
$$

Therefore, by induction,

$$
B_{n,k}(q)={n\brack k}_q.
$$

Now prove the multinomial statement by induction on the alphabet size $c$. Separate the positions occupied by the largest letter $c$. Replacing every $c$ by $1$ and every smaller letter by $0$ produces a binary word with $k_c$ ones. Its inversions count exactly the inversions involving the letter $c$. Once the positions of $c$ are fixed, the remaining positions contain a word of content

$$
(k_1,\ldots,k_{c-1}),
$$

and its inversions are precisely the inversions not involving $c$.

Thus the generating polynomial factors as

$$
{n\brack k_c}_q
{n-k_c\brack k_1,\ldots,k_{c-1}}_q.
$$

By cancellation of $q$-factorials,

$$
{n\brack k_c}_q
{n-k_c\brack k_1,\ldots,k_{c-1}}_q
=
{n\brack k_1,\ldots,k_c}_q.
$$

This completes the induction. ∎

### Lemma 8.2 — Euler derivatives are weighted moments

For every integer $j\ge0$,

$$
\boxed{
D^jM_{\mathbf k}(\zeta)
=
\sum_{w\in\mathcal W(\mathbf k)}
\operatorname{inv}(w)^j
\zeta^{\operatorname{inv}(w)}.
}
$$

#### Proof

For every monomial $q^m$,

$$
D^jq^m=m^jq^m.
$$

Apply $D^j$ term by term to Theorem 8.1 and set $q=\zeta$. ∎

### Project Theorem 8.3 — Fourier-Moment Cancellation Theorem

Let $h$ be the defect of $M_{\mathbf k}$ at the primitive $d$-th root $\zeta$. Then

$$
\boxed{
\sum_{w\in\mathcal W(\mathbf k)}
\operatorname{inv}(w)^j
\zeta^{\operatorname{inv}(w)}
=0
\qquad
(0\le j<h),
}
$$

while

$$
\boxed{
\sum_{w\in\mathcal W(\mathbf k)}
\operatorname{inv}(w)^h
\zeta^{\operatorname{inv}(w)}
=
h!(-1)^hd^{2h}
\frac{a!}{\prod_\nu r_\nu!}
\frac1{\prod_\nu A_{s_\nu}(\zeta)}.
}
$$

#### Proof

By Lemma 8.2, the weighted Fourier moment of order $j$ is exactly $D^jM_{\mathbf k}(\zeta)$. Theorem 7.1 gives the vanishing for $j<h$ and the exact value at $j=h$. ∎

### Interpretation 8.4

The residue defect is exactly the order of Fourier-moment cancellation:

$$
\boxed{
 h
=
\min\left\{
 j:\sum_w
\operatorname{inv}(w)^j
\zeta^{\operatorname{inv}(w)}
e0
\right\}.
}
$$

MacMahon's classical equidistribution theorem allows $\operatorname{inv}$ to be replaced by the major index. That external equidistribution theorem is not required for any proof in this chapter; the inversion enumerator already gives a self-contained derivation.

---

# 9. Universal defect cores

The first visible jet separates into a quotient-scale multinomial factor and a residue-only core.

Let

$$
\mathbf s=(s_1,\ldots,s_c),
\qquad
0\le s_\nu<d,
\qquad
\sum_\nu s_\nu=hd.
$$

### Definition 9.1 — Defect-core polynomial

Define

$$
C_{\mathbf s}(q)
=
{hd\brack s_1,\ldots,s_c}_q.
$$

Every denominator part is smaller than $d$, so its quotient parameter is zero. The total quotient parameter is $h$. Therefore the defect of $C_{\mathbf s}$ is exactly $h$.

### Project Theorem 9.2 — Universal Defect Core Theorem

For

$$
M_{\mathbf k}(q)
=
{ad\brack k_1,\ldots,k_c}_q,
\qquad
k_\nu=r_\nu d+s_\nu,
$$

with defect $h$,

$$
\boxed{
\frac{D^hM_{\mathbf k}(\zeta)}{h!}
=
\binom{a}{r_1,\ldots,r_c,h}
\frac{D^hC_{\mathbf s}(\zeta)}{h!}.
}
$$

Here

$$
\binom{a}{r_1,\ldots,r_c,h}
=
\frac{a!}{r_1!\cdots r_c!h!},
$$

and the entries sum to $a$ because

$$
r_1+\cdots+r_c+h=a.
$$

#### Proof

Apply Theorem 7.1 to the core. Its total quotient is $h$, every denominator quotient is zero, and its residue vector is $\mathbf s$. Therefore

$$
\frac{D^hC_{\mathbf s}(\zeta)}{h!}
=
(-1)^hd^{2h}
\frac{h!}{\prod_\nu A_{s_\nu}(\zeta)}.
$$

Multiplying by the ordinary multinomial coefficient gives

$$
\begin{aligned}
\binom{a}{r_1,\ldots,r_c,h}
\frac{D^hC_{\mathbf s}(\zeta)}{h!}
&=
\frac{a!}{h!\prod_\nu r_\nu!}
(-1)^hd^{2h}
\frac{h!}{\prod_\nu A_{s_\nu}(\zeta)}\\
&=
(-1)^hd^{2h}
\frac{a!}{\prod_\nu r_\nu!}
\frac1{\prod_\nu A_{s_\nu}(\zeta)}.
\end{aligned}
$$

The last expression is exactly the first visible jet of $M_{\mathbf k}$ from Theorem 7.1. ∎

### Corollary 9.3 — Exact weighted defect model

The first visible jet can be computed by the following auxiliary weighted construction:

1. divide the $ad$ positions into $a$ labeled positional cycles of size $d$;
2. choose $h$ cycles to carry the defect core;
3. among the remaining cycles, choose $r_\nu$ monochromatic cycles of color $\nu$;
4. place a word of content $\mathbf s$ on the $hd$ defect positions;
5. assign that core word the weight
   $$
   \frac{\operatorname{inv}(w)^h}{h!}
   \zeta^{\operatorname{inv}(w)}.
   $$

The total weighted sum is

$$
\frac{D^hM_{\mathbf k}(\zeta)}{h!}.
$$

#### Proof

The number of ways to perform steps 2 and 3 is

$$
\binom{a}{r_1,\ldots,r_c,h}.
$$

By Lemma 8.2, the weighted sum in steps 4 and 5 is

$$
\frac{D^hC_{\mathbf s}(\zeta)}{h!}.
$$

Multiply and apply Theorem 9.2. ∎

### Caution 9.4 — Weighted model versus direct decomposition

Corollary 9.3 is an exact identity of weighted sums. It does **not** yet provide a statistic-preserving bijection that decomposes the original word set $\mathcal W(\mathbf k)$ into monochromatic cycles and a literal defect-core word while preserving inversion phases term by term.

Constructing such a bijection would be a stronger combinatorial theorem.

---

# 10. The binary subset stratum

Gaussian binomial coefficients appear as the two-color case. The defect can then only be zero or one.

Let

$$
n=ad,
\qquad
k=rd+s,
\qquad
1\le s<d.
$$

Then

$$
ad-k=(a-r-1)d+(d-s),
$$

so the two residues are $s$ and $d-s$, whose sum is $d$. Hence $h=1$.

### Corollary 10.1 — First derivative of a nonfixed Gaussian binomial

For a primitive $d$-th root $\zeta$,

$$
\boxed{
D{ad\brack rd+s}_q\Big|_{q=\zeta}
=
(-1)^s ad
\binom{a-1}{r}
\frac{\zeta^{-\binom{s}{2}}}
{1-\zeta^s}.
}
$$

Equivalently, because $D=\zeta\,d/dq$ at $q=\zeta$,

$$
\boxed{
\zeta
\left.
\frac{d}{dq}{ad\brack rd+s}_q
\right|_{q=\zeta}
=
(-1)^s ad
\binom{a-1}{r}
\frac{\zeta^{-\binom{s}{2}}}
{1-\zeta^s}.
}
$$

#### Proof

Apply Theorem 7.1 with $h=1$:

$$
D{ad\brack rd+s}_q\Big|_{q=\zeta}
=
-d^2
\frac{a!}
{r!(a-r-1)!A_s(\zeta)A_{d-s}(\zeta)}.
$$

By Lemma 4.4,

$$
A_s(\zeta)A_{d-s}(\zeta)
=
(-1)^{s-1}d
\zeta^{\binom{s}{2}}(1-\zeta^s).
$$

Therefore

$$
\begin{aligned}
D{ad\brack rd+s}_q\Big|_{q=\zeta}
&=
-d^2
\frac{a!}{r!(a-r-1)!}
\frac{(-1)^{s-1}\zeta^{-\binom{s}{2}}}
{d(1-\zeta^s)}\\
&=
(-1)^s d
\frac{a!}{r!(a-r-1)!}
\frac{\zeta^{-\binom{s}{2}}}{1-\zeta^s}\\
&=
(-1)^s ad
\binom{a-1}{r}
\frac{\zeta^{-\binom{s}{2}}}{1-\zeta^s}.
\end{aligned}
$$

∎

Thus the familiar first-order subset formula is exactly the $c=2$, $h=1$ stratum of the multinomial defect theory.

---

# 11. The first genuinely second-order event

### Example 11.1 — Content $(2,2,2)$ at a cubic root

Let

$$
d=3,
\qquad
\mathbf k=(2,2,2),
\qquad
n=6=2d,
\qquad
a=2.
$$

Every quotient parameter is zero and every residue is two:

$$
r_1=r_2=r_3=0,
\qquad
s_1=s_2=s_3=2.
$$

Hence

$$
h=a-(r_1+r_2+r_3)=2.
$$

For a primitive cubic root $\zeta$,

$$
A_2(\zeta)
=(1-\zeta)(1-\zeta^2)
=3.
$$

Theorem 7.1 gives

$$
M_{(2,2,2)}(\zeta)=0,
\qquad
DM_{(2,2,2)}(\zeta)=0,
$$

while

$$
\begin{aligned}
\frac{D^2M_{(2,2,2)}(\zeta)}{2!}
&=
3^4
\frac{2!}{3^3}\\
&=6.
\end{aligned}
$$

Therefore

$$
\boxed{D^2M_{(2,2,2)}(\zeta)=12.}
$$

This is a genuine order-two contextual emergence: both the value and tangent vanish, while the quadratic transverse jet survives.

---

# 12. The multinomial collision hierarchy

Let

$$
M_{\mathbf k}(q),
\qquad
M_{\mathbf l}(q)
$$

be two Gaussian multinomials of the same total size $ad$. Let their defects at the primitive $d$-th root $\zeta$ be

$$
h_{\mathbf k},
\qquad
h_{\mathbf l}.
$$

Part I already gives the unregularized jet criterion:

$$
v_{\Phi_d}(M_{\mathbf k}-M_{\mathbf l})\ge r
\iff
D^jM_{\mathbf k}(\zeta)=D^jM_{\mathbf l}(\zeta)
\quad(0\le j<r).
$$

The defect normal form sharpens this criterion.

### Project Theorem 12.1 — Different-defect collision law

If

$$
h_{\mathbf k}\ne h_{\mathbf l},
$$

then

$$
\boxed{
v_{\Phi_d}
\left(M_{\mathbf k}-M_{\mathbf l}\right)
=
\min(h_{\mathbf k},h_{\mathbf l}).
}
$$

#### Proof

Assume without loss of generality that

$$
h_{\mathbf k}<h_{\mathbf l}.
$$

By Corollary 6.3,

$$
M_{\mathbf k}(q)
=
(q^d-1)^{h_{\mathbf k}}
\left(
\mathcal R_d(\mathbf k;\zeta)+O(q-\zeta)
\right),
$$

with nonzero leading residual, while

$$
M_{\mathbf l}(q)
=
(q^d-1)^{h_{\mathbf l}}
\left(
\mathcal R_d(\mathbf l;\zeta)+O(q-\zeta)
\right).
$$

Factor the smaller power:

$$
\begin{aligned}
M_{\mathbf k}-M_{\mathbf l}
&=
(q^d-1)^{h_{\mathbf k}}
\Bigl(
\mathcal R_d(\mathbf k;\zeta)
+O(q-\zeta)\\
&\hspace{39mm}
-(q^d-1)^{h_{\mathbf l}-h_{\mathbf k}}
(\mathcal R_d(\mathbf l;\zeta)+O(q-\zeta))
\Bigr).
\end{aligned}
$$

The bracket has value

$$
\mathcal R_d(\mathbf k;\zeta)\ne0
$$

at $q=\zeta$. Thus it is a local unit, and the difference has local order exactly $h_{\mathbf k}$. Local order equals $\Phi_d$-valuation. ∎

Now suppose the defects are equal:

$$
h_{\mathbf k}=h_{\mathbf l}=h.
$$

### Definition 12.2 — Regularized residual germ

In the exponential coordinate, define

$$
\boxed{
\mathcal G_{\mathbf k,\zeta}(x)
=
\frac{M_{\mathbf k}(\zeta e^x)}
{(e^{dx}-1)^h}.
}
$$

This is regular at $x=0$, and

$$
\mathcal G_{\mathbf k,\zeta}(0)
=
\mathcal R_d(\mathbf k;\zeta).
$$

### Project Theorem 12.3 — Regularized Collision Hierarchy

For every integer $r\ge0$,

$$
\boxed{
v_{\Phi_d}(M_{\mathbf k}-M_{\mathbf l})
\ge h+r
}
$$

if and only if

$$
\boxed{
\mathcal G_{\mathbf k,\zeta}^{(j)}(0)
=
\mathcal G_{\mathbf l,\zeta}^{(j)}(0)
\qquad
(0\le j<r).
}
$$

Equivalently, if

$$
R_{\mathbf k,\zeta}(q)
=
\frac{M_{\mathbf k}(q)}{(q^d-1)^h}
$$

and similarly for $\mathbf l$ in the local ring, then

$$
\boxed{
v_{\Phi_d}(M_{\mathbf k}-M_{\mathbf l})
\ge h+r
\iff
D^jR_{\mathbf k,\zeta}(\zeta)
=
D^jR_{\mathbf l,\zeta}(\zeta)
\quad(0\le j<r).
}
$$

#### Proof

By definition,

$$
M_{\mathbf k}(\zeta e^x)
=
(e^{dx}-1)^h
\mathcal G_{\mathbf k,\zeta}(x),
$$

and similarly for $\mathbf l$. Therefore

$$
M_{\mathbf k}(\zeta e^x)-M_{\mathbf l}(\zeta e^x)
=
(e^{dx}-1)^h
\left(
\mathcal G_{\mathbf k,\zeta}(x)
-
\mathcal G_{\mathbf l,\zeta}(x)
\right).
$$

The power series $e^{dx}-1$ has order one at $x=0$. Hence the order of the difference is

$$
h+
\operatorname{ord}_{x=0}
\left(
\mathcal G_{\mathbf k,\zeta}
-
\mathcal G_{\mathbf l,\zeta}
\right).
$$

This order is at least $h+r$ exactly when the first $r$ Taylor coefficients of the two regularized germs agree, equivalently when their derivatives of orders $0,\ldots,r-1$ agree.

The order in $x$ equals the local order in $q-\zeta$, which equals $\Phi_d$-valuation. Finally,

$$
\mathcal G_{\mathbf k,\zeta}(x)
=
R_{\mathbf k,\zeta}(\zeta e^x),
$$

so

$$
\mathcal G_{\mathbf k,\zeta}^{(j)}(0)
=
D^jR_{\mathbf k,\zeta}(\zeta).
$$

∎

### Corollary 12.4 — Leading residual collision criterion

For equal defect $h$,

$$
\boxed{
v_{\Phi_d}(M_{\mathbf k}-M_{\mathbf l})
\ge h+1
\iff
\mathcal R_d(\mathbf k;\zeta)
=
\mathcal R_d(\mathbf l;\zeta).
}
$$

If the residuals are unequal, then

$$
\boxed{
v_{\Phi_d}(M_{\mathbf k}-M_{\mathbf l})=h.}
$$

#### Proof

Take $r=1$ in Theorem 12.3. ∎

### Corollary 12.5 — Explicit first residual test

For two multinomials of the same total $ad$ and the same defect $h$, an extra order of collision occurs exactly when

$$
\boxed{
\frac{a!}{\prod_\nu r_{\mathbf k,\nu}!}
\frac1{\prod_\nu A_{s_{\mathbf k,\nu}}(\zeta)}
=
\frac{a!}{\prod_\nu r_{\mathbf l,\nu}!}
\frac1{\prod_\nu A_{s_{\mathbf l,\nu}}(\zeta)}.
}
$$

The common factor $(-1)^hd^h$ in the two residuals has been cancelled.

#### Proof

Substitute Theorem 6.2 into Corollary 12.4. ∎

### Corollary 12.6 — Primitive-root independence of collision depth

If the residual equality, or any higher regularized-jet equality, holds at one primitive $d$-th root, then the corresponding equality holds at every primitive $d$-th root.

#### Proof

The polynomial

$$
M_{\mathbf k}-M_{\mathbf l}
$$

has rational coefficients. Its multiplicity at one primitive root is therefore the exponent of the irreducible polynomial $\Phi_d$, and is the same at every Galois-conjugate primitive root.

Equivalently, apply the automorphisms $\sigma_m$ from Corollary 6.5 to the residual and regularized-jet equalities. ∎

### Structural conclusion 12.7

The multinomial collision problem separates into layers:

$$
\boxed{
\begin{array}{c|c}
\text{layer}&\text{data}\\
\hline
\text{depth}&h\\
\text{leading transverse term}&\mathcal R_d\\
\text{higher transverse terms}&\mathcal G^{(j)}(0)\\
\text{collision multiplicity}&v_{\Phi_d}(M_{\mathbf k}-M_{\mathbf l})
\end{array}
}
$$

Different depths settle the collision immediately. Equal depths require residual comparison. Equal residuals require successive regularized jets.

---

# 13. Exact computational architecture

The theorems in this chapter yield a non-expanding implementation path.

## 13.1 Defect computation

Input:

```text
parts = [k_1, ..., k_c]
d
```

Requirements:

```text
sum(parts) % d == 0
```

Compute:

```text
a = sum(parts) // d
r = [k // d for k in parts]
s = [k % d for k in parts]
h = a - sum(r)
```

This is exact integer arithmetic.

## 13.2 Residual representation

The leading residual is

$$
(-1)^hd^h
\frac{a!}{\prod r_\nu!}
\prod_\nu A_{s_\nu}(\zeta)^{-1}.
$$

It should be represented in the exact cyclotomic field

$$
\mathbb Q(\zeta_d),
$$

or as a residue class modulo $\Phi_d(q)$. Numerical complex approximations must not be used for equality testing.

## 13.3 First visible jet

Multiply the residual by $d^h h!$ to obtain

$$
D^hM_{\mathbf k}(\zeta).
$$

All lower derivatives are exactly zero.

## 13.4 Defect core

The quotient-scale dependence can be separated from the residue dependence:

```text
ordinary_factor = multinomial(a; r_1, ..., r_c, h)
core            = q_multinomial(h*d; s_1, ..., s_c)
```

Only the first visible jet of the core is needed; the core polynomial itself need not be expanded because its derivative is given by Theorem 7.1.

## 13.5 Collision certificate

For two multinomials:

1. compute both defects;
2. if they differ, return their minimum as the exact collision depth;
3. if they agree, compare exact leading residuals;
4. if those differ, return the common defect;
5. otherwise compare successive regularized jets.

A structured result may contain:

```text
context_order       = d
left_defect         = h_left
right_defect        = h_right
contact_order       = v_{Phi_d}(left - right)
leading_residuals   = (..., ...)
first_differing_jet = r
```

The present chapter proves the defect and leading-residual layers completely. Efficient closed formulas for arbitrary higher regularized jets lead into the cumulant theory of the next part.

---

# 14. Testing blueprint

A reference implementation should include exact tests of the following forms.

1. **Defect valuation.** For small compositions, expand the Gaussian multinomial, factor it, and compare the exponent of $\Phi_d$ with $h$.
2. **Local factorial normal form.** Symbolically divide $(q;q)_{rd+s}$ by $(1-q^d)^r$ and evaluate modulo $\Phi_d$.
3. **Leading residual.** Compare Theorem 6.2 with direct local series expansion.
4. **First visible jet.** Verify that derivatives below $h$ vanish and that the $h$-th derivative matches Theorem 7.1.
5. **Fourier moments.** Enumerate small multiset words, compute inversion moments, and compare with the derivative formulas.
6. **Defect core.** Verify Theorem 9.2 for all small residue vectors.
7. **Binary stratum.** Compare Corollary 10.1 with direct differentiation of Gaussian binomials.
8. **Second-order event.** Confirm
   $$
   D^2{6\brack2,2,2}_q\big|_{q=\zeta_3}=12.
   $$
9. **Different defects.** Check that the difference valuation is the smaller defect.
10. **Equal defects.** Compare exact residual equality with the occurrence of one additional $\Phi_d$-factor.
11. **Galois covariance.** Evaluate the exact formulas at every primitive conjugate.
12. **Huge parameters.** Use parts with hundreds of digits and verify that defect and residual-parameter construction do not depend on polynomial degree.

---

# 15. Theorem inventory

| Number | Result | Status | Exact conclusion | Main proof mechanism |
|---|---|---|---|---|
| 2.2 | Defect bounds | Elementary | $0\le h\le c-1$ | Residue sum $hd$ |
| 3.1 | $q$-Multinomial Defect Theorem | Project theorem | $v_{\Phi_d}(M_{\mathbf k})=h$ | Floor valuation of $q$-factorials |
| 4.2 | Complete root product | Classical lemma | $A_{d-1}(\zeta)=d$ | Factorization of $(x^d-1)/(x-1)$ |
| 4.3 | Conjugation phase | Elementary | Exact phase of $\overline{A_s}$ | Pair each factor with its inverse |
| 4.4 | Complementary residue product | Project-supporting lemma | Closed form for $A_sA_{d-s}$ | Complete root product |
| 5.1 | Local Factorial Normal Form | Project theorem | Normalized $(q;q)_{rd+s}$ tends to $r!d^rA_s$ | Residue-block decomposition |
| 5.2 | Compressed quotient normal form | Consequence | Exact local leading term of any compressed factorial quotient | Multiplicativity |
| 6.2 | Multinomial Local Residual Formula | Project theorem | Exact nonzero transverse residual | Apply factorial normal form to numerator and denominator |
| 7.1 | First Visible Jet Theorem | Project theorem | First nonzero Euler derivative occurs at order $h$ | Exponential local coordinate |
| 8.1 | Multiset inversion enumerator | Classical theorem, proved here | $q$-multinomial is the inversion generating polynomial | Binary recurrence and alphabet induction |
| 8.3 | Fourier-Moment Cancellation | Project theorem | First $h$ twisted moments vanish except the explicit $h$-th moment | Euler derivatives of the enumerator |
| 9.2 | Universal Defect Core Theorem | Project theorem | First jet factors into an ordinary multinomial and residue core jet | Compare explicit residual formulas |
| 10.1 | Binary first-derivative formula | Project corollary | Exact derivative of ${ad\brack rd+s}_q$ at $\zeta_d$ | Complementary root-product identity |
| 12.1 | Different-defect collision law | Project theorem | Difference depth is the smaller defect | Local leading-order comparison |
| 12.3 | Regularized Collision Hierarchy | Project theorem | Extra depth equals matching order of residual germs | Factor common $(e^{dx}-1)^h$ |
| 12.4 | Leading residual criterion | Project corollary | Equal defect gains one order iff residuals agree | Zeroth regularized jet |

---

# 16. Unified geometric normal form

The entire chapter can be compressed into one exact statement:

$$
\boxed{
M_{\mathbf k}(q)
=
(q^d-1)^h
\left(
(-1)^hd^h
\frac{a!}{\prod_\nu r_\nu!}
\frac1{\prod_\nu A_{s_\nu}(\zeta)}
+
O(q-\zeta)
\right)
}
$$

in the local ring at a primitive $d$-th root $\zeta$.

The associated dictionary is

$$
\boxed{
\begin{array}{c|c}
\text{geometric notion}&\text{cyclotomic realization}\\
\hline
\text{context}&q=\zeta\\
\text{context kernel}&(\Phi_d)\\
\text{contact depth}&h\\
\text{transverse residual}&\mathcal R_d(\mathbf k;\zeta)\\
\text{first visible osculating order}&D^hM_{\mathbf k}(\zeta)\\
\text{higher transverse profile}&\mathcal G_{\mathbf k,\zeta}^{(j)}(0)\\
\text{collision multiplicity}&v_{\Phi_d}(M_{\mathbf k}-M_{\mathbf l})
\end{array}
}
$$

Thus:

$$
\boxed{
\text{residue carry structure}
\longrightarrow
\text{cyclotomic depth}
\longrightarrow
\text{transverse residual}
\longrightarrow
\text{higher local jets}.
}
$$

---

# 17. Boundaries of this part

This chapter proves the exact depth and leading local term of Gaussian multinomials, together with the abstract hierarchy of higher residual jets. It does not yet derive closed cumulant formulas for all those higher jets.

The next natural chapter is:

> **Part IV — Cyclotomic Cumulants and Reciprocity:** normalized local germs, logarithmic cumulants, the even-germ parity law at $d=2$, reciprocity drift and curvature, the complex chiral geometry for $d\ge3$, and the spectral visibility theorem.

Differential cyclic sieving and orbit-polynomial congruences can then be exported as a separate subsequent chapter.

---

## End of Part III
