# Cyclotomic Coefficient Arithmetic

## Part II — Gaussian Collision Arithmetic

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Theorem chapter; all stated results are proved below.  
**Scope:** Gaussian adjacent-difference calculus, the Simple-Collision Theorem, stable central-block content and spacing, specialization at \(q=1\), integer content, the specialization gap, and the two exceptional binary families.

---

## 0. Purpose, dependencies, and status conventions

Part I developed the general framework:

- polynomial-family spacing as a gcd of differences;
- cyclotomic valuation of \(q\)-factorial quotients;
- the Gaussian valuation law;
- the \(q\)-Lucas contextual fingerprint;
- local depth and the Euler-jet collision criterion.

This part applies those tools to the Gaussian row

\[
F_k(q)={n\brack k}_q.
\]

The main stable-range conclusion is

\[
\boxed{
\Delta_{n,t}(q)
=
q^{t+1}
\prod_{d=n-t+1}^{n}\Phi_d(q),
}
\]

while its integer specialization satisfies

\[
\boxed{
G_{n,t}
=
\eta(n,t)
\prod_{d=n-t+1}^{n}\rho(d),
}
\]

with exactly two binary exceptional families.

The labels used below are:

- **Classical lemma:** standard algebraic or number-theoretic input, proved here when short.
- **Project theorem:** a theorem established in this project.
- **Correction:** an edge condition required for the exact statement.
- **Software corollary:** an immediate exact-computation consequence.

---

# 1. Central Gaussian blocks

Let

\[
{n\brack k}_q
=
\frac{(q;q)_n}{(q;q)_k(q;q)_{n-k}},
\qquad
(q;q)_m=\prod_{r=1}^{m}(1-q^r).
\]

Fix integers

\[
t\ge 1,
\qquad
n\ge 2t.
\]

The retained central block is

\[
\mathcal B_{n,t}
=
\left\{
{n\brack k}_q:t\le k\le n-t
\right\}.
\]

### Definition 1.1 — Polynomial content

Define

\[
C_{n,t}(q)
=
\gcd_{t\le k\le n-t}{n\brack k}_q,
\]

with the gcd chosen monic.

### Definition 1.2 — Polynomial spacing

Define

\[
\Delta_{n,t}(q)
=
\gcd_{t\le i<j\le n-t}
\left(
{n\brack j}_q-{n\brack i}_q
\right),
\]

again chosen monic.

### Definition 1.3 — Integer content and spacing

At \(q=1\), define

\[
H_{n,t}
=
\gcd_{t\le k\le n-t}\binom nk
\]

and

\[
G_{n,t}
=
\gcd_{t\le i<j\le n-t}
\left|
\binom nj-inom ni
\right|.
\]

Gaussian reciprocity gives

\[
{n\brack k}_q={n\brack n-k}_q.
\]

Therefore all four gcds may be computed using only

\[
t\le k\le \left\lfloor\frac n2\right\rfloor.
\]

---

# 2. Adjacent differences

The exact spacing is controlled by adjacent Gaussian coefficients.

### Lemma 2.1 — Chain reduction

Let \(A_t,A_{t+1},\ldots,A_u\) lie in a unique factorization domain. Then

\[
\boxed{
\gcd_{t\le i<j\le u}(A_j-A_i)
=
\gcd_{t\le k<u}(A_{k+1}-A_k).
}
\]

#### Proof

Every adjacent difference is one of the pairwise differences, so the pairwise gcd divides the adjacent gcd.

Conversely,

\[
A_j-A_i
=
\sum_{k=i}^{j-1}(A_{k+1}-A_k),
\]

so every common divisor of the adjacent differences divides every pairwise difference. ∎

### Proposition 2.2 — Gaussian adjacent-difference identity

For \(0\le k<n\),

\[
\frac{{n\brack k+1}_q}{{n\brack k}_q}
=
\frac{1-q^{n-k}}{1-q^{k+1}}.
\]

Hence

\[
\boxed{
{n\brack k+1}_q-{n\brack k}_q
=
q^{k+1}{n\brack k}_q
\frac{1-q^{n-2k-1}}{1-q^{k+1}}.
}
\]

When \(n-2k-1<0\), the displayed expression is interpreted as an identity of Laurent rational functions; the left side remains a polynomial. For the lower half \(k<(n-1)/2\), every exponent displayed is nonnegative.

#### Proof

The quotient formula follows by cancelling the common factors in the two Gaussian products:

\[
{n\brack k+1}_q
=
{n\brack k}_q
\frac{1-q^{n-k}}{1-q^{k+1}}.
\]

Subtracting \({n\brack k}_q\) gives

\[
{n\brack k}_q
\frac{(1-q^{n-k})-(1-q^{k+1})}{1-q^{k+1}}
=
{n\brack k}_q
\frac{q^{k+1}-q^{n-k}}{1-q^{k+1}},
\]

which is the claimed formula. ∎

### Corollary 2.3 — Cyclotomic valuation of an adjacent difference

Let \(d\ge2\), and assume

\[
n-2k-1\ne0.
\]

Then

\[
\boxed{
\begin{aligned}
v_{\Phi_d}
\left(
{n\brack k+1}_q-{n\brack k}_q
\right)
&=
v_{\Phi_d}\left({n\brack k}_q\right)\\
&\quad+
\mathbf 1_{d\mid n-2k-1}
-
\mathbf 1_{d\mid k+1}.
\end{aligned}
}
\]

Here \(\mathbf 1_E\) is \(1\) when \(E\) holds and \(0\) otherwise.

#### Proof

For every nonzero integer \(a\), the Laurent polynomial \(1-q^a\) has one factor \(\Phi_d(q)\) exactly when \(d\mid a\). Apply the valuation to Proposition 2.2. The monomial power of \(q\) is a unit at every primitive \(d\)-th root with \(d\ge2\), so it contributes no \(\Phi_d\)-valuation. ∎

### Corollary 2.4 — Exact \(q\)-order in the lower half

If

\[
0\le k<\frac{n-1}{2},
\]

then

\[
\boxed{
v_q
\left(
{n\brack k+1}_q-{n\brack k}_q
\right)
=k+1.
}
\]

#### Proof

In Proposition 2.2, the factor after \(q^{k+1}\) is a polynomial with constant term \(1\). Indeed, \({n\brack k}_q\) has constant term \(1\), and the quotient of the two \(1-q^m\) factors has formal power-series constant term \(1\). ∎

---

# 3. The Simple-Collision Theorem

This theorem gives the exact first-order collision law in the first \(d\)-block.

## 3.1 Root values

Fix

\[
d\ge2,
\qquad
M\ge2,
\qquad
n=Md-1,
\]

and let \(\zeta\) be a primitive \(d\)-th root of unity.

For \(0\le k\le d-1\), write

\[
F_k(q)={Md-1\brack k}_q.
\]

### Lemma 3.1 — First-block root value

For \(0\le k\le d-1\),

\[
\boxed{
F_k(\zeta)
=
(-1)^k\zeta^{-k(k+1)/2}.
}
\]

In particular, \(F_k(\zeta)\ne0\).

#### Proof

Using the product formula,

\[
F_k(q)
=
\prod_{r=1}^{k}
\frac{1-q^{Md-r}}{1-q^r}.
\]

At \(q=\zeta\),

\[
\frac{1-\zeta^{Md-r}}{1-\zeta^r}
=
\frac{1-\zeta^{-r}}{1-\zeta^r}
=
-\zeta^{-r}.
\]

Multiplying over \(r\) gives

\[
F_k(\zeta)
=(-1)^k\zeta^{-\sum_{r=1}^k r}
=(-1)^k\zeta^{-k(k+1)/2}.
\]

∎

### Lemma 3.2 — Zeroth-order collision criterion

For \(0\le i<j\le d-1\),

\[
F_i(\zeta)=F_j(\zeta)
\]

if and only if

\[
\boxed{
2d\mid(i-j)(d-i-j-1).
}
\]

#### Proof

By Lemma 3.1, equality is equivalent to

\[
(-1)^{i-j}
\zeta^{-\left(i(i+1)-j(j+1)\right)/2}
=1.
\]

Since

\[
i(i+1)-j(j+1)
=(i-j)(i+j+1),
\]

and \(\zeta=e^{2\pi i/d}\), the left side is

\[
\exp\left(
\frac{\pi i}{d}
(i-j)(d-i-j-1)
\right).
\]

It equals \(1\) exactly when the integer

\[
(i-j)(d-i-j-1)
\]

is divisible by \(2d\). ∎

## 3.2 First derivatives

Let

\[
D=q\frac{d}{dq}.
\]

### Lemma 3.3 — Logarithmic derivative in the first block

For \(0\le k\le d-1\),

\[
\boxed{
\frac{DF_k(\zeta)}{F_k(\zeta)}
=
Md\sum_{r=1}^{k}\frac1{1-\zeta^r}
-
\frac{k(k+1)}2.
}
\]

Its real part is

\[
\boxed{
\operatorname{Re}
\frac{DF_k(\zeta)}{F_k(\zeta)}
=
\frac{k(Md-k-1)}2.
}
\]

#### Proof

Differentiate the logarithm of

\[
F_k(q)
=
\prod_{r=1}^{k}
\frac{1-q^{Md-r}}{1-q^r}.
\]

Since

\[
D\log(1-q^a)
=-\frac{a q^a}{1-q^a},
\]

we obtain at \(q=\zeta\)

\[
\begin{aligned}
\frac{DF_k(\zeta)}{F_k(\zeta)}
&=
\sum_{r=1}^{k}
\left(
-\frac{(Md-r)\zeta^{-r}}{1-\zeta^{-r}}
+
\frac{r\zeta^r}{1-\zeta^r}
\right)\\
&=
\sum_{r=1}^{k}
\left(
\frac{Md-r}{1-\zeta^r}
+
\frac{r\zeta^r}{1-\zeta^r}
\right)\\
&=
Md\sum_{r=1}^{k}\frac1{1-\zeta^r}
-
\sum_{r=1}^{k}r.
\end{aligned}
\]

This proves the first formula.

For every \(z\) on the unit circle with \(z\ne1\),

\[
\operatorname{Re}\frac1{1-z}=\frac12.
\]

Therefore

\[
\operatorname{Re}
\frac{DF_k(\zeta)}{F_k(\zeta)}
=
\frac{Mdk}2-rac{k(k+1)}2
=
\frac{k(Md-k-1)}2.
\]

∎

### Project Theorem 3.4 — Simple-Collision Theorem

Let

\[
d\ge2,
\qquad
M\ge2,
\qquad
n=Md-1,
\qquad
0\le i<j\le d-1.
\]

Then

\[
\boxed{
v_{\Phi_d}
\left(
{n\brack i}_q-{n\brack j}_q
\right)
=
\begin{cases}
1,&2d\mid(i-j)(d-i-j-1),\\
0,&\text{otherwise}.
\end{cases}
}
\]

Thus every nonzero collision in the first \(d\)-block is simple.

#### Proof

If the divisibility condition fails, Lemma 3.2 gives

\[
F_i(\zeta)\ne F_j(\zeta),
\]

so \(\Phi_d\) does not divide their difference.

Assume now that the condition holds. Then

\[
F_i(\zeta)=F_j(\zeta)=A\ne0.
\]

By Lemma 3.3,

\[
\begin{aligned}
\operatorname{Re}
\left(
\frac{DF_j(\zeta)}{F_j(\zeta)}
-
\frac{DF_i(\zeta)}{F_i(\zeta)}
\right)
&=
\frac{j(Md-j-1)-i(Md-i-1)}2\\
&=
\frac{(j-i)(Md-i-j-1)}2.
\end{aligned}
\]

Because \(M\ge2\) and \(i+j+1\le2d-2\),

\[
Md-i-j-1\ge2.
\]

Hence the displayed real part is strictly positive. Therefore

\[
DF_j(\zeta)\ne DF_i(\zeta).
\]

The two polynomials agree at \(\zeta\) but have different first Euler derivatives there. By the local jet criterion from Part I, their difference has exactly one factor \(\Phi_d\). ∎

### Correction 3.5 — The degenerate case \(M=1\)

The hypothesis \(M\ge2\) is necessary for the blanket exact-one statement.

If \(M=1\), then \(n=d-1\), and Gaussian symmetry gives

\[
{d-1\brack i}_q
=
{d-1\brack d-1-i}_q
\]

identically. Thus complementary pairs have zero difference and infinite collision depth. Earlier shorthand statements of the theorem without \(M\ge2\) must be read in this corrected nondegenerate form.

---

# 4. Stable interval geometry

The stable range is

\[
\boxed{
t\ge5,
\qquad
n\ge3t-2.
}
\]

Two elementary interval lemmas drive the content and spacing proofs.

### Lemma 4.1 — Stable multiple lemma

Assume \(n\ge3t-2\). For every integer

\[
1\le d\le n-t,
\]

the interval

\[
[t,n-t]
\]

contains a multiple of \(d\).

#### Proof

If \(d\ge t\), then \(d\in[t,n-t]\).

If \(d\le t-1\), the interval contains

\[
n-2t+1\ge t-1\ge d
\]

consecutive integers. Every block of \(d\) consecutive integers contains a multiple of \(d\). ∎

### Lemma 4.2 — Stable noncollision witness

Assume

\[
t\ge5,
\qquad
n\ge3t-2,
\qquad
2\le d\le n-t.
\]

Then there exists

\[
k\in[t,n-t-1]
\]

such that

\[
{n\brack k+1}_q\ne {n\brack k}_q
\]

and

\[
\boxed{
\Phi_d(q)
\nmid
{n\brack k+1}_q-{n\brack k}_q.
}
\]

#### Proof

Write

\[
n=ad+b,
\qquad
0\le b<d.
\]

We use Corollary 2.3.

### Case 1: a noncentral multiple exists

Suppose there is a multiple

\[
m\in[t+1,n-t]
\]

of \(d\) with

\[
m\ne\frac{n+1}{2}.
\]

Set \(k=m-1\). Then \(k\equiv-1\pmod d\), so

\[
\mathbf 1_{d\mid k+1}=1.
\]

The Gaussian valuation is

\[
v_{\Phi_d}{n\brack k}_q
=
\begin{cases}
1,&b<d-1,\\
0,&b=d-1.
\end{cases}
\]

Also

\[
n-2k-1
\equiv b+1\pmod d,
\]

so

\[
\mathbf 1_{d\mid n-2k-1}
=
\begin{cases}
0,&b<d-1,\\
1,&b=d-1.
\end{cases}
\]

The three terms in Corollary 2.3 therefore sum to \(0\). The exclusion of \(m=(n+1)/2\) ensures that the adjacent difference is not the zero central-symmetry difference.

### Case 2: the only multiple is the center

Suppose the only multiple of \(d\) in \([t+1,n-t]\) is

\[
c=\frac{n+1}{2}.
\]

Then \(n\) is odd and \(d\mid c\). The interval \([t+1,n-t]\) has

\[
n-2t\ge t-2\ge3
\]

terms and is symmetric about \(c\).

The case \(d=2\) cannot occur. If the interval has at least five terms, then \(c-2\) is another even multiple whenever \(c\) is even. If it has exactly three terms, stable range forces \((t,n)=(5,13)\), for which \(c=7\) is odd.

Thus \(d>2\). Set

\[
k=c-2.
\]

Then

\[
n-2k-1=2,
\]

so \(d\nmid n-2k-1\). Moreover,

\[
k+1=c-1\not\equiv0\pmod d.
\]

Since

\[
n\equiv-1\pmod d,
\qquad
k\equiv-2\pmod d,
\]

the Gaussian valuation is zero. Hence the adjacent-difference valuation is zero.

### Case 3: no multiple occurs in \([t+1,n-t]\)

By Lemma 4.1, \([t,n-t]\) still contains a multiple of \(d\), so \(d\mid t\).

If \(d<t\), then \(d\) is a proper divisor of \(t\), hence \(d\le t/2\). Therefore

\[
t+d\le\frac{3t}{2}\le2t-2\le n-t,
\]

contradicting the assumption that \([t+1,n-t]\) contains no multiple.

Thus \(d=t\). The next multiple \(2t\) is not in the interval, so \(n<3t\). Together with \(n\ge3t-2\), this gives

\[
n\in\{3t-2,3t-1\}.
\]

Take \(k=t\). Modulo \(d=t\), the remainder of \(k\) is \(0\), while the remainder of \(n\) is respectively \(t-2\) or \(t-1\). Hence

\[
v_{\Phi_t}{n\brack t}_q=0.
\]

Furthermore,

\[
n-2t-1
=
\begin{cases}
t-3,&n=3t-2,\\
t-2,&n=3t-1,
\end{cases}
\]

which is positive and not divisible by \(t\), and \(t\nmid t+1\). Corollary 2.3 again gives valuation zero. ∎

---

# 5. Stable polynomial content

### Project Theorem 5.1 — Stable Content Theorem

Assume

\[
\boxed{
t\ge5,
\qquad
n\ge3t-2.
}
\]

Then

\[
\boxed{
C_{n,t}(q)
=
\prod_{d=n-t+1}^{n}\Phi_d(q).
}
\]

#### Proof

The cyclotomic valuation of a Gaussian coefficient is

\[
v_{\Phi_d}{n\brack k}_q
=
\left\lfloor\frac nd\right\rfloor
-
\left\lfloor\frac kd\right\rfloor
-
\left\lfloor\frac{n-k}{d}\right\rfloor,
\]

and is always \(0\) or \(1\).

### Terminal factors

Let

\[
n-t+1\le d\le n.
\]

For every retained \(k\),

\[
k\le n-t<d
\]

and

\[
n-k\le n-t<d.
\]

Also \(d>n/2\), so \(\lfloor n/d\rfloor=1\). Therefore

\[
v_{\Phi_d}{n\brack k}_q=1
\]

for every retained \(k\). Thus each terminal \(\Phi_d\) divides the content exactly at least once.

### No earlier factor

Let \(d\le n-t\). By Lemma 4.1, choose a retained \(k\) divisible by \(d\). Then

\[
k\bmod d=0\le n\bmod d,
\]

so the Gaussian carry criterion gives

\[
v_{\Phi_d}{n\brack k}_q=0.
\]

Thus \(\Phi_d\) does not divide every retained coefficient.

No irreducible factor other than cyclotomic polynomials occurs in a Gaussian binomial coefficient, since it is a quotient of products of \(1-q^m\). Because all Gaussian cyclotomic valuations are at most one, the terminal factors occur in the content exactly once. ∎

---

# 6. Stable polynomial spacing

### Project Theorem 6.1 — Stable Content–Spacing Decomposition Theorem

Assume

\[
\boxed{
t\ge5,
\qquad
n\ge3t-2.
}
\]

Then

\[
\boxed{
\Delta_{n,t}(q)
=
q^{t+1}C_{n,t}(q)
}
\]

and hence

\[
\boxed{
\Delta_{n,t}(q)
=
q^{t+1}
\prod_{d=n-t+1}^{n}\Phi_d(q).
}
\]

#### Proof

By Gaussian symmetry and Lemma 2.1, \(\Delta_{n,t}\) is the gcd of the nonzero adjacent differences in the retained chain.

## Step 1: the exact power of \(q\)

In the lower half, Corollary 2.4 gives

\[
v_q
\left(
{n\brack k+1}_q-{n\brack k}_q
\right)
=k+1.
\]

Every lower-half retained adjacent index satisfies \(k\ge t\), so every difference is divisible by \(q^{t+1}\). For \(k=t\), the order is exactly \(t+1\). Thus

\[
v_q(\Delta_{n,t})=t+1.
\]

## Step 2: the terminal cyclotomic interval divides the spacing

By Theorem 5.1, every retained coefficient is divisible by

\[
\prod_{d=n-t+1}^{n}\Phi_d(q).
\]

Therefore every difference is divisible by this product.

## Step 3: every terminal exponent is exactly one

Consider the first adjacent difference

\[
{n\brack t+1}_q-{n\brack t}_q.
\]

For a terminal index \(d\ge n-t+1\), Theorem 5.1 gives

\[
v_{\Phi_d}{n\brack t}_q=1.
\]

Also, stable range gives

\[
d\ge n-t+1\ge2t-1>t+1,
\]

so \(d\nmid t+1\). Moreover,

\[
0<n-2t-1<d,
\]

because

\[
n-2t-1\ge t-3>0
\]

and

\[
d-(n-2t-1)\ge t+2.
\]

Hence \(d\nmid n-2t-1\). Corollary 2.3 therefore gives

\[
v_{\Phi_d}
\left(
{n\brack t+1}_q-{n\brack t}_q
\right)
=1.
\]

Thus no terminal factor occurs in the spacing with exponent greater than one.

## Step 4: no earlier cyclotomic factor divides the spacing

Let \(2\le d\le n-t\). By Lemma 4.2, some retained adjacent difference is not divisible by \(\Phi_d\). Hence \(\Phi_d\nmid\Delta_{n,t}\).

## Step 5: no other irreducible factor occurs

The spacing divides the first adjacent difference

\[
{n\brack t+1}_q-{n\brack t}_q.
\]

By Proposition 2.2, this polynomial is a monomial times a quotient of products of factors \(1-q^m\). Since the result is a polynomial, every nonmonomial irreducible factor is cyclotomic. Steps 1–4 therefore exhaust its possible common irreducible factors. ∎

### Corollary 6.2 — Content and spacing carry the same cyclotomic interval

In stable range, the polynomial content and polynomial spacing have the same nonmonomial factors:

\[
\boxed{
\frac{\Delta_{n,t}(q)}{C_{n,t}(q)}=q^{t+1}.
}
\]

The difference between value content and spacing content is therefore purely the universal initial \(q\)-adic agreement of the retained Gaussian coefficients.

---

# 7. Sharpness of the stable range

### Proposition 7.1 — Uniform sharpness at \(n=3t-3\)

Let \(t\ge2\) and set

\[
n=3t-3.
\]

Then

\[
\Phi_{t-1}(q)
\mid
C_{n,t}(q),
\]

although

\[
t-1<n-t+1=2t-2.
\]

Thus the uniform threshold \(n\ge3t-2\) in Theorem 5.1 cannot be lowered to \(n\ge3t-3\).

#### Proof

Put

\[
d=t-1.
\]

Then \(n=3d\), and the retained indices satisfy

\[
t=d+1\le k\le n-t=2d-1.
\]

Modulo \(d\), these indices have the nonzero remainders \(1,2,\ldots,d-1\), while

\[
n\bmod d=0.
\]

The Gaussian carry criterion gives

\[
v_{\Phi_d}{n\brack k}_q=1
\]

for every retained \(k\). Thus \(\Phi_{t-1}\) is an extra common factor below the predicted terminal interval. ∎

---

# 8. Specialization of cyclotomic content at \(q=1\)

Define

\[
\rho(m)
=
\begin{cases}
p,&m=p^a\text{ for a prime }p\text{ and }a\ge1,\\
1,&m\text{ is not a prime power}.
\end{cases}
\]

### Classical Lemma 8.1 — Cyclotomic value at one

For \(m>1\),

\[
\boxed{
\Phi_m(1)=\rho(m).
}
\]

#### Proof

The Möbius product formula is

\[
\Phi_m(x)
=
\prod_{d\mid m}(x^d-1)^{\mu(m/d)}.
\]

Since

\[
\sum_{d\mid m}\mu(m/d)=0
\qquad(m>1),
\]

the factors \(x-1\) cancel in the limit \(x\to1\), giving

\[
\Phi_m(1)
=
\prod_{d\mid m}d^{\mu(m/d)}.
\]

Fix a prime \(p\), and write

\[
m=p^a u,
\qquad
p\nmid u.
\]

The exponent of \(p\) in the displayed product is

\[
\sum_{c\mid m}\mu(c)v_p(m/c).
\]

Only squarefree \(c\) contribute. Splitting according to whether \(p\mid c\), this exponent becomes

\[
\sum_{c'\mid u}\mu(c')
\bigl(a-(a-1)\bigr)
=
\sum_{c'\mid u}\mu(c').
\]

This is \(1\) when \(u=1\), and \(0\) when \(u>1\). Hence \(\Phi_m(1)\) is \(p\) if \(m\) is a power of \(p\), and is \(1\) if \(m\) has at least two distinct prime divisors. ∎

The formula \(\Phi_1(1)=0\) is exceptional and is not represented by \(\rho\). It never enters the stable terminal interval because that interval lies above \(1\).

---

# 9. Stable integer content

The equality

\[
H_{n,t}=C_{n,t}(1)
\]

is not automatic for an arbitrary polynomial family. Here it is true, but it requires a separate prime-adic proof.

### Project Theorem 9.1 — Stable Integer Content Theorem

Assume

\[
\boxed{
t\ge5,
\qquad
n\ge3t-2.
}
\]

Then

\[
\boxed{
H_{n,t}
=
\gcd_{t\le k\le n-t}\binom nk
=
\prod_{d=n-t+1}^{n}\rho(d).
}
\]

#### Proof

Fix a prime \(p\). Legendre's formula gives

\[
\boxed{
v_p\binom nk
=
\sum_{a\ge1}
\left(
\left\lfloor\frac n{p^a}\right\rfloor
-
\left\lfloor\frac k{p^a}\right\rfloor
-
\left\lfloor\frac{n-k}{p^a}\right\rfloor
\right).
}
\]

Each summand is the Gaussian cyclotomic valuation at \(\Phi_{p^a}\), and hence is \(0\) or \(1\).

Let \(p^u\) be the largest power of \(p\) satisfying

\[
p^u\le n-t.
\]

If no positive power satisfies this, take \(u=0\) and \(p^u=1\).

By Lemma 4.1, choose a retained \(k\) divisible by \(p^u\). For every \(a\le u\),

\[
k\bmod p^a=0,
\]

so the corresponding carry summand is zero.

For every \(a>u\) with \(p^a\le n\), one has

\[
n-t<p^a\le n.
\]

Since both \(k\) and \(n-k\) are at most \(n-t\), while \(p^a>n-t\ge n/2\) and \(p^a\le n\), the corresponding summand is exactly one. Thus

\[
v_p\binom nk
=
\#\{a:n-t<p^a\le n\}.
\]

Every retained \(k\) has at least these terminal contributions, so

\[
v_p(H_{n,t})
=
\#\{a:n-t<p^a\le n\}.
\]

On the other hand, Lemma 8.1 shows that the exponent of \(p\) in

\[
\prod_{d=n-t+1}^{n}\rho(d)
\]

is exactly the same count of powers \(p^a\) in the terminal interval. This holds for every prime \(p\), proving the formula. ∎

### Corollary 9.2 — Polynomial and integer content agree after specialization

In stable range,

\[
\boxed{
H_{n,t}=C_{n,t}(1).
}
\]

This equality is theorem-specific; it must not be treated as a general property of gcd specialization.

---

# 10. The specialization gap

Set

\[
H=H_{n,t}
\]

and define normalized retained coefficients

\[
B_k=\frac1H\binom nk.
\]

Then

\[
\gcd_{t\le k\le n-t}B_k=1.
\]

Because every original difference is divisible by \(H\), define the specialization gap

\[
E_{n,t}
=
\frac{G_{n,t}}{H_{n,t}}.
\]

By Lemma 2.1,

\[
\boxed{
E_{n,t}
=
\gcd_{t\le k<n-t}|B_{k+1}-B_k|.
}
\]

Write

\[
N=n+1.
\]

For \(m=k+1\), the adjacent ratio is

\[
\boxed{
\frac{\binom n{k+1}}{\binom nk}
=
\frac{N-m}{m}.
}
\]

The interval of adjacent-ratio parameters is

\[
J=[t+1,n-t]
=[t+1,N-t-1],
\]

and contains

\[
n-2t\ge t-2\ge3
\]

consecutive integers.

---

# 11. Exclusion of odd specialization primes

### Project Theorem 11.1 — No odd prime divides the stable specialization gap

Assume stable range. Then no odd prime divides \(E_{n,t}\).

#### Proof

Suppose an odd prime \(p\) divides \(E_{n,t}\). Then all normalized values \(B_k\) are congruent modulo \(p\).

Because their gcd is \(1\), their common residue cannot be zero. Hence every \(B_k\) is a \(p\)-adic unit, so

\[
v_p\binom nk=v_p(H)
\]

for every retained \(k\).

For adjacent indices, put \(m=k+1\). Equality of the two binomial valuations and the adjacent ratio give

\[
v_p(N-m)=v_p(m)=r.
\]

Write

\[
m=p^r u,
\qquad
N-m=p^r v,
\]

with \(u,v\) units modulo \(p\). Since

\[
B_{k+1}\equiv B_k\not\equiv0\pmod p,
\]

the unit part of their ratio is \(1\), so

\[
\frac vu\equiv1\pmod p.
\]

Equivalently,

\[
\boxed{
p^{r+1}\mid N-2m.}
\]

Now choose any three consecutive integers in \(J\). At most one is divisible by the odd prime \(p\), so two of them, say \(m_1,m_2\), satisfy \(r=0\). For both,

\[
N\equiv2m_i\pmod p.
\]

Thus

\[
p\mid2(m_1-m_2).
\]

But

\[
0<|m_1-m_2|\le2<p,
\]

which is impossible. Therefore no odd prime divides \(E_{n,t}\). ∎

---

# 12. Binary valuation symmetry

For \(p=2\), every nonzero residue modulo \(2\) is the same. Therefore the only issue is whether all normalized coefficients are odd.

### Lemma 12.1 — Parity-gap criterion

Let

\[
A=v_2(H_{n,t}).
\]

Then

\[
\boxed{
2\mid E_{n,t}
\iff
v_2\binom nk=A
\text{ for every retained }k.
}
\]

Equivalently,

\[
\boxed{
2\mid E_{n,t}
\iff
v_2(N-m)=v_2(m)
\text{ for every }m\in J.
}
\]

#### Proof

The condition \(2\mid E_{n,t}\) says that all \(B_k\) have the same parity. Their gcd is \(1\), so they cannot all be even. Thus they are all odd, which is equivalent to

\[
v_2\binom nk=A
\]

for every retained \(k\).

The valuations of consecutive binomial coefficients differ by

\[
\begin{aligned}
v_2\binom n{k+1}-v_2\binom nk
&=
v_2(N-m)-v_2(m).
\end{aligned}
\]

Hence the binomial valuation is constant across the retained chain exactly when the two valuations on the right agree for every \(m\in J\). Since \(A\) is the minimum retained valuation, a constant valuation must equal \(A\). ∎

### Lemma 12.2 — Exact \(2\)-adic symmetry set

Write

\[
N=2^s u,
\qquad
v_2(N)=s,
\qquad
v_2(u)=0,
\]

and put

\[
P=2^s.
\]

If \(u=1\), then

\[
\boxed{
v_2(N-m)=v_2(m)}
\]

for every \(0<m<N\).

If \(u>1\), then

\[
\boxed{
v_2(N-m)=v_2(m)
\iff
P\nmid m.}
\]

#### Proof

If \(u=1\), write \(m=2^r a\) with \(a\) odd and \(r<s\). Then

\[
N-m
=
2^r(2^{s-r}-a),
\]

and the parenthesis is odd. Hence both valuations equal \(r\).

Now assume \(u>1\).

If \(P\nmid m\), write \(m=2^r a\) with \(r<s\) and \(a\) odd. Then

\[
N-m
=
2^r(2^{s-r}u-a),
\]

and the parenthesis is odd, so the valuations agree.

If \(P\mid m\), write \(m=Pa\). Then

\[
N-m=P(u-a).
\]

Because \(u\) is odd, the integers \(a\) and \(u-a\) have opposite parity. Therefore

\[
v_2(a)\ne v_2(u-a),
\]

and the valuations of \(m\) and \(N-m\) do not agree. ∎

---

# 13. Classification of the two binary families

### Project Theorem 13.1 — Binary Exceptional-Family Classification

Assume

\[
\boxed{
t\ge5,
\qquad
n\ge3t-2.
}
\]

Then

\[
\boxed{
2\mid E_{n,t}
}
\]

if and only if exactly one of the following holds:

1. \(n=2^s-1\) for some \(s\ge1\);
2. \(n=3\cdot2^s-1\) and \(t=2^s\).

#### Proof

Put \(N=n+1\), and write

\[
N=uP,
\qquad
P=2^{v_2(N)},
\qquad
v_2(u)=0.
\]

By Lemmas 12.1 and 12.2, parity enhancement occurs precisely as follows.

### Family 1: \(u=1\)

Then \(N=P=2^s\), and valuation symmetry holds for every \(0<m<N\). Therefore

\[
n=N-1=2^s-1
\]

always gives \(2\mid E_{n,t}\).

### The case \(u>1\)

Now \(u\ge3\) is odd. Lemma 12.2 says that parity enhancement occurs exactly when the central interval

\[
J=[t+1,N-t-1]
\]

contains no multiple of \(P\).

Let

\[
a=\frac{u-1}{2}.
\]

The center \(N/2\) lies between the consecutive multiples

\[
aP
\qquad\text{and}\qquad
(a+1)P.
\]

Because \(J\) is connected and symmetric about \(N/2\), it contains no multiple of \(P\) exactly when

\[
t+1>aP
\]

and

\[
N-t-1<(a+1)P.
\]

Both inequalities are equivalent to

\[
\boxed{t\ge aP=\frac{u-1}{2}P.}
\]

Stable range gives

\[
n=N-1\ge3t-2,
\]

or equivalently

\[
3t\le uP+1.
\]

Combining this with the lower bound on \(t\),

\[
\frac{3(u-1)}2P
\le
uP+1,
\]

so

\[
\boxed{(u-3)P\le2.}
\]

Since \(u\ge3\) is odd, the only stable possibility with \(t\ge5\) is

\[
u=3.
\]

The no-multiple condition becomes

\[
t\ge P.
\]

The stable inequality becomes

\[
3t\le3P+1,
\]

so \(t\le P\). Hence

\[
t=P.
\]

Thus

\[
N=3P=3\cdot2^s,
\qquad
t=2^s,
\]

which is Family 2.

Conversely, if \(N=3P\) and \(t=P\), then

\[
J=[P+1,2P-1]
\]

contains no multiple of \(P\), so Lemmas 12.1 and 12.2 give \(2\mid E_{n,t}\). ∎

---

# 14. The binary gap has exact size two

### Project Theorem 14.1 — No factor four in the specialization gap

In either exceptional family,

\[
\boxed{4\nmid E_{n,t}.}
\]

#### Proof

We exhibit one normalized adjacent difference with exact \(2\)-adic valuation one.

## Family 1: \(N=2^s\)

Here

\[
n=N-1.
\]

Stable range with \(t\ge5\) implies \(N\ge16\). Every binomial coefficient

\[
\binom{N-1}{k}
\]

is odd, by Lucas's theorem or the no-carry criterion. Thus

\[
v_2(H)=0.
\]

The adjacent index interval contains at least three consecutive integers, so choose an even

\[
k\in[t,n-t-1].
\]

The ordinary adjacent-difference identity is

\[
\binom n{k+1}-\binom nk
=
\binom nk
\frac{n-2k-1}{k+1}.
\]

Now

\[
n-2k-1
=N-2k-2
=2\left(\frac N2-k-1\right).
\]

Since \(N/2\) and \(k\) are even, the parenthesis is odd. Also \(k+1\) is odd. Therefore the adjacent difference has exact \(2\)-adic valuation one. Since \(H\) is odd, the normalized adjacent difference also has valuation one.

## Family 2: \(N=3P\), \(t=P\)

Here

\[
n=3P-1,
\qquad
P=2^s\ge8.
\]

The terminal interval is

\[
(2P-1,3P-1],
\]

which contains exactly one power of two, namely \(2P\). Theorem 9.1 gives

\[
v_2(H)=1.
\]

Take \(k=P\). By Theorem 13.1, every retained binomial valuation is \(1\), so

\[
v_2\binom nP=1.
\]

Furthermore,

\[
n-2P-1
=P-2
=2\left(\frac P2-1\right),
\]

and \(P/2-1\) is odd because \(P\ge8\). The denominator \(P+1\) is odd. Thus the adjacent difference has valuation

\[
1+1=2.
\]

After division by \(H\), its valuation is exactly one.

In both families, one normalized adjacent difference is divisible by \(2\) but not by \(4\). Hence \(4\nmid E_{n,t}\). ∎

---

# 15. Stable Specialization Theorem

### Project Theorem 15.1 — Stable Specialization Theorem

Assume

\[
\boxed{
t\ge5,
\qquad
n\ge3t-2.
}
\]

Then

\[
\boxed{
G_{n,t}
=
\eta(n,t)H_{n,t},
}
\]

where

\[
\boxed{
\eta(n,t)
=
\begin{cases}
2,&n=2^s-1,\\
2,&n=3\cdot2^s-1\text{ and }t=2^s,\\
1,&\text{otherwise}.
\end{cases}
}
\]

Equivalently,

\[
\boxed{
G_{n,t}
=
\eta(n,t)
\prod_{d=n-t+1}^{n}\rho(d).
}
\]

#### Proof

By Theorem 9.1,

\[
H_{n,t}
=
\prod_{d=n-t+1}^{n}\rho(d).
\]

Let

\[
E_{n,t}=G_{n,t}/H_{n,t}.
\]

Theorem 11.1 shows that no odd prime divides \(E_{n,t}\). Therefore \(E_{n,t}\) is a power of two.

Theorem 13.1 shows that \(2\mid E_{n,t}\) exactly in the two stated binary families. Theorem 14.1 shows that even there \(4\nmid E_{n,t}\). Hence

\[
E_{n,t}
=
\begin{cases}
2,&\text{in the two binary families},\\
1,&\text{otherwise}.
\end{cases}
\]

Multiplying by \(H_{n,t}\) proves both formulas. ∎

### Corollary 15.2 — Exact specialization gap

In stable range,

\[
\boxed{
\frac{G_{n,t}}{\Delta_{n,t}(1)}
=
\eta(n,t).
}
\]

Indeed,

\[
\Delta_{n,t}(1)
=C_{n,t}(1)
=H_{n,t},
\]

because the factor \(q^{t+1}\) becomes \(1\).

Thus the failure of gcd specialization is completely classified: it is absent except for one extra factor \(2\) in exactly two binary families.

---

# 16. Structural interpretation

The stable theory now gives the chain

\[
\boxed{
\text{Gaussian value content}
\longrightarrow
\text{terminal cyclotomic interval}
\longrightarrow
\text{Gaussian spacing content}.
}
\]

More precisely,

\[
C_{n,t}(q)
=
\prod_{d=n-t+1}^{n}\Phi_d(q),
\]

\[
\Delta_{n,t}(q)
=
q^{t+1}C_{n,t}(q),
\]

\[
H_{n,t}
=C_{n,t}(1),
\]

and

\[
G_{n,t}
=
\eta(n,t)H_{n,t}.
\]

There are therefore two logically distinct specialization phenomena:

1. **content specialization**, which is exact in the stable range;
2. **spacing specialization**, which acquires one extra binary factor in the two exceptional families.

The polynomial factor \(q^{t+1}\) records universal agreement of the initial coefficient jets at \(q=0\). The exceptional integer factor \(2\) records a different phenomenon: constancy of the normalized row modulo \(2\), governed by the symmetry

\[
v_2(N-m)=v_2(m).
\]

---

# 17. Theorem inventory

| Number | Result | Status | Exact conclusion | Main proof mechanism |
|---|---|---|---|---|
| 2.2 | Gaussian adjacent-difference identity | Classical | Exact factorization of consecutive Gaussian differences | Gaussian ratio cancellation |
| 3.4 | Simple-Collision Theorem | Project theorem, corrected | First-block collision valuation is \(1\) exactly under the quadratic congruence, for \(M\ge2\) | Root phase plus nonzero reciprocity drift |
| 4.1 | Stable multiple lemma | Elementary | Every \(d\le n-t\) has a multiple in the retained block | Interval length |
| 4.2 | Stable noncollision witness | Project lemma | Every nonterminal \(\Phi_d\) fails on some retained adjacent difference | Adjacent valuation and residue cases |
| 5.1 | Stable Content Theorem | Project theorem | \(C_{n,t}=\prod_{d=n-t+1}^n\Phi_d\) | Gaussian carry criterion |
| 6.1 | Stable Content–Spacing Decomposition | Project theorem | \(\Delta_{n,t}=q^{t+1}C_{n,t}\) | Adjacent differences and stable witnesses |
| 7.1 | Sharpness at \(3t-3\) | Project proposition | \(\Phi_{t-1}\) is an extra content factor | Remainders modulo \(t-1\) |
| 9.1 | Stable Integer Content | Project theorem | \(H_{n,t}=\prod\rho(d)\) | Legendre/Kummer plus one multiple witness per prime |
| 11.1 | Odd-prime exclusion | Project theorem | No odd prime divides the specialization gap | Three consecutive adjacent ratios |
| 13.1 | Binary-family classification | Project theorem | Parity gap occurs only for \(2^s-1\) and \((3\cdot2^s-1,2^s)\) | Exact \(2\)-adic symmetry interval |
| 14.1 | Exact binary gap | Project theorem | The exceptional factor is \(2\), never \(4\) | Explicit adjacent difference |
| 15.1 | Stable Specialization Theorem | Project theorem | \(G_{n,t}=\eta H_{n,t}\) | Prime classification |

---

# 18. Software consequences

The proofs yield direct algorithms requiring no polynomial expansion.

## 18.1 Stable content

For \(t\ge5\) and \(n\ge3t-2\), return the compressed factor list

\[
[(d,1):n-t+1\le d\le n]
\]

for

\[
C_{n,t}(q).
\]

## 18.2 Stable spacing

Return

\[
q^{t+1}
\prod_{d=n-t+1}^{n}\Phi_d(q)
\]

as a factored object, without expanding it.

## 18.3 Integer content

For every prime \(p\), its exponent is

\[
\#\{a:n-t<p^a\le n\}.
\]

Thus the integer content can be computed by enumerating prime powers in a short terminal interval.

## 18.4 Specialization gap

The gap test is constant-time after recognizing the two forms:

```text
if n + 1 is a power of 2:
    eta = 2
elif t is a power of 2 and n + 1 == 3*t:
    eta = 2
else:
    eta = 1
```

The stable integer spacing is then

\[
G_{n,t}=\eta(n,t)H_{n,t}.
\]

## 18.5 Simple-collision certificate

For \(n=Md-1\) with \(M\ge2\) and \(0\le i<j<d\), a complete certificate is:

1. compute
   \[
   R=(i-j)(d-i-j-1)\bmod 2d;
   \]
2. if \(R\ne0\), return collision depth \(0\);
3. if \(R=0\), return collision depth \(1\).

No root-of-unity arithmetic is required at runtime once the theorem is installed.

---

# 19. Testing blueprint

A reference implementation should include the following exact tests.

1. Verify Proposition 2.2 by expansion for small \(n,k\).
2. Verify Theorem 3.4 for \(2\le d\le20\), \(2\le M\le8\), and all \(i<j<d\).
3. Include the \(M=1\) complementary-pair regression test.
4. Factor all retained Gaussian coefficients for small stable \((n,t)\) and verify Theorem 5.1.
5. Factor all adjacent differences and verify Theorem 6.1.
6. Test the sharpness example \(n=3t-3\).
7. Compute ordinary binomial gcds and verify Theorem 9.1.
8. Compute integer spacing gcds and verify both exceptional families.
9. Test nearby nonexceptional values:
   - \(n=2^s-2\);
   - \(n=2^s\);
   - \(n=3\cdot2^s-2\);
   - \(n=3\cdot2^s\);
   - \(n=3\cdot2^s-1\) with \(t\ne2^s\).
10. Confirm that the specialization gap is never divisible by an odd prime or by \(4\) throughout a large finite search.

---

# 20. Boundaries of this part

This chapter does not yet develop:

- multinomial residue defects;
- local factorial normal forms at arbitrary primitive roots;
- leading transverse residuals;
- Fourier-moment cancellation;
- universal defect cores;
- higher multinomial collision depth;
- reciprocity parity and cumulants at \(d=2\);
- chiral cumulants for \(d\ge3\);
- differential cyclic sieving.

Those topics belong to the next chapters.

A natural continuation is:

> **Part III — Multinomial Defects and Local Residual Geometry:** exact defect valuation, local factorial normal form, first visible jets, Fourier-moment cancellation, universal defect cores, and the multinomial collision hierarchy.

---

## End of Part II
