# Cyclotomic Coefficient Arithmetic

## Part IV — Cyclotomic Cumulants and Reciprocity

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Theorem chapter; every theorem stated in this chapter is proved below.  
**Scope:** Exact logarithmic local germs of compressed \(q\)-factorial quotients, cyclotomic cumulant kernels, reciprocity, the \(d=2\) even-germ theorem, the fingerprints \(B,E,\Theta,\Lambda,\ldots\), the binary collision ladder, complex chirality for \(d\ge3\), and the Spectral Visibility Theorem.

---

## 0. Purpose, dependencies, and conventions

Part I identified cyclotomic valuation with local contact order and equality of Euler jets. Part III gave the exact defect and leading local residual of a Gaussian multinomial. The present chapter computes the entire regularized local germ logarithmically.

The central principle is

\[
\boxed{
\text{structured product}
\longrightarrow
\text{additive local logarithm}
\longrightarrow
\text{cyclotomic cumulants}.
}
\]

At the binary context \(q=-1\), reciprocity forces the normalized germ to be even. At a primitive root of order \(d\ge3\), reciprocity instead pairs a context with its complex conjugate and leaves a generally nonzero odd, purely imaginary phase profile.

Throughout,

\[
D=q\frac{d}{dq},
\qquad
q=\zeta e^x,
\]

so that

\[
D=\frac{d}{dx}.
\]

We use the Bernoulli-number convention

\[
\frac{z}{e^z-1}
=
\sum_{m\ge0}B_m\frac{z^m}{m!},
\qquad
B_1=-\frac12.
\]

The labels used below are:

- **Classical lemma:** standard input, with proof included.
- **Project theorem:** a theorem established in this project.
- **Corollary:** a formal consequence.
- **Caution:** a distinction required for exact mathematics or software.
- **Software corollary:** a direct non-expanding computational consequence.

All local logarithms may be read formally: if a germ has nonzero constant term \(c\), factor out \(c\) and apply the formal power-series logarithm to the remaining germ with constant term \(1\). No numerical branch of the complex logarithm is needed.

---

# 1. Compressed factorial quotients and regularized germs

## 1.1 Compressed representation

Let

\[
F(q)
=
q^\alpha
\prod_{i=1}^{s}(q;q)_{a_i}^{\varepsilon_i},
\qquad
(q;q)_a=\prod_{m=1}^{a}(1-q^m),
\]

where

\[
\alpha\in\mathbb Z,
\qquad
a_i\in\mathbb Z_{\ge0},
\qquad
\varepsilon_i\in\mathbb Z.
\]

The expression may initially be a rational function. At any fixed context, the formulas below apply whenever the indicated regularized germ is defined and nonzero.

Fix a primitive \(d\)-th root of unity \(\zeta\). Part I gives

\[
\boxed{
h=v_{\Phi_d}(F)
=
\sum_{i=1}^{s}\varepsilon_i
\left\lfloor\frac{a_i}{d}\right\rfloor.
}
\]

Set

\[
f_{F,\zeta}(x)=F(\zeta e^x).
\]

Whenever \(h\ge0\) and \(F\) is regular at \(\zeta\), define the regularized local germ

\[
H_{F,\zeta}(x)
=
x^{-h}F(\zeta e^x).
\]

It has a nonzero constant term.

## 1.2 Leading exponential-coordinate residual

### Proposition 1.1 — Exact leading \(x\)-residual

Let

\[
r_i=\left\lfloor\frac{a_i}{d}\right\rfloor.
\]

Then

\[
\boxed{
B_\zeta(F)
:=
\lim_{x\to0}x^{-h}F(\zeta e^x)
=
\zeta^\alpha
(-d)^h
\prod_{i=1}^{s}(r_i!)^{\varepsilon_i}
\prod_{i=1}^{s}
\prod_{\substack{1\le m\le a_i\\d\nmid m}}
(1-\zeta^m)^{\varepsilon_i}.
}
\]

#### Proof

Expand every factorial into its linear factors. If \(d\nmid m\), then

\[
1-(\zeta e^x)^m
=
1-\zeta^m+O(x),
\]

with nonzero constant term.

If \(m=d\ell\), then

\[
1-(\zeta e^x)^m
=
1-e^{d\ell x}
=
-d\ell x+O(x^2).
\]

Thus each multiple of \(d\) contributes one factor of \(x\) and leading coefficient \(-d\ell\). In \((q;q)_{a_i}\), the multiples are

\[
d,2d,\ldots,r_id,
\]

whose leading-coefficient product is

\[
(-d)^{r_i}r_i!.
\]

Raise these products to the exponents \(\varepsilon_i\), multiply by \((\zeta e^x)^\alpha\to\zeta^\alpha\), and use

\[
h=\sum_i\varepsilon_i r_i.
\]

This gives the formula. ∎

### Caution 1.2 — Coordinate dependence of the residual

The number \(B_\zeta(F)\) is normalized by the exponential coordinate \(x\). A residual normalized by \((q-\zeta)^h\), \(\Phi_d(q)^h\), or \((q^d-1)^h\) differs from it by an explicit nonzero unit.

The valuation and matching order are coordinate-independent; the leading scalar is not.

---

# 2. The one-factor logarithmic kernels

Every cumulant formula follows from two one-factor expansions: one for a nonvanishing residue channel and one for the singular channel \(\rho=1\).

## 2.1 Nontrivial residue channels

### Classical Lemma 2.1 — Polylogarithmic derivative formula

Let \(\rho\ne1\), let \(m\ge1\), and set

\[
g_{\rho,m}(x)=\log(1-\rho e^{mx}).
\]

For every integer \(r\ge1\),

\[
\boxed{
g_{\rho,m}^{(r)}(0)
=
-m^r\operatorname{Li}_{1-r}(\rho).
}
\]

#### Proof

For \(|z|<1\),

\[
\log(1-z)=-\sum_{\ell\ge1}\frac{z^\ell}{\ell}.
\]

Substitute \(z=\rho e^{mx}\) temporarily in a convergent region, differentiate \(r\) times, and evaluate at \(x=0\):

\[
\begin{aligned}
g_{\rho,m}^{(r)}(0)
&=
-\sum_{\ell\ge1}
\frac{\rho^\ell}{\ell}(m\ell)^r\\
&=
-m^r\sum_{\ell\ge1}\ell^{r-1}\rho^\ell\\
&=
-m^r\operatorname{Li}_{1-r}(\rho).
\end{aligned}
\]

For nonpositive integral polylogarithm order, the right side is a rational function of \(\rho\), with its only possible pole at \(\rho=1\). Hence the identity extends algebraically to every \(\rho\ne1\), including roots of unity. ∎

## 2.2 The singular channel

When \(\rho=1\), the factor \(1-e^{mx}\) vanishes. Remove its simple zero first.

### Classical Lemma 2.2 — Regularized singular expansion

For \(m\ge1\), define

\[
s_m(x)=\frac{1-e^{mx}}{-mx}.
\]

Then \(s_m(0)=1\), and

\[
\boxed{
\log s_m(x)
=
\frac{mx}{2}
+
\sum_{j\ge1}
\frac{B_{2j}}{2j(2j)!}
(mx)^{2j}.
}
\]

Equivalently,

\[
\boxed{
\left.\frac{d^r}{dx^r}\log s_m(x)\right|_{x=0}
=
\begin{cases}
\dfrac m2,&r=1,\\[2mm]
\dfrac{B_r}{r}m^r,&r\ge2\text{ even},\\[2mm]
0,&r\ge3\text{ odd}.
\end{cases}
}
\]

#### Proof

Because

\[
1-e^y=-2e^{y/2}\sinh(y/2),
\]

we have

\[
\frac{1-e^y}{-y}
=
e^{y/2}\frac{\sinh(y/2)}{y/2}.
\]

The second factor is even, so its logarithm contains only even powers. To identify the coefficients, differentiate:

\[
\frac{d}{dy}\log\frac{e^y-1}{y}
=
\frac{e^y}{e^y-1}-\frac1y.
\]

Using

\[
\frac{y}{e^y-1}
=
\sum_{r\ge0}B_r\frac{y^r}{r!},
\]

one obtains

\[
\frac{e^y}{e^y-1}-\frac1y
=
\frac12+
\sum_{j\ge1}
\frac{B_{2j}}{(2j)!}y^{2j-1}.
\]

Integrating and using that the logarithm vanishes at \(y=0\) gives

\[
\log\frac{e^y-1}{y}
=
\frac y2+
\sum_{j\ge1}
\frac{B_{2j}}{2j(2j)!}y^{2j}.
\]

Since \((1-e^y)/(-y)=(e^y-1)/y\), substitute \(y=mx\). The derivative statement follows by reading Taylor coefficients. ∎

## 2.3 Unified kernel notation

For a root of unity \(\rho\), define

\[
K_r(\rho)=
\begin{cases}
-\operatorname{Li}_{1-r}(\rho),&\rho\ne1,\\[1mm]
\dfrac12,&\rho=1,
\ r=1,\\[2mm]
\dfrac{B_r}{r},&\rho=1,
\ r\ge2\text{ even},\\[2mm]
0,&\rho=1,
\ r\ge3\text{ odd}.
\end{cases}
\]

The factor \(1-\rho e^{mx}\), after removing \(-mx\) when \(\rho=1\), contributes

\[
\boxed{m^rK_r(\rho)}
\]

to the \(r\)-th logarithmic derivative.

---

# 3. Cyclotomic cumulants of compressed factorial quotients

## 3.1 Definition

Normalize the regularized germ to constant term \(1\):

\[
G_{F,\zeta}(x)
=
\frac{x^{-h}F(\zeta e^x)}{B_\zeta(F)}.
\]

Then

\[
G_{F,\zeta}(0)=1.
\]

Define the cyclotomic cumulants by

\[
\boxed{
\kappa_r(F;\zeta)
=
\left.\frac{d^r}{dx^r}\log G_{F,\zeta}(x)\right|_{x=0}.
}
\]

Thus

\[
\boxed{
F(\zeta e^x)
=
B_\zeta(F)x^h
\exp\left(
\sum_{r\ge1}\kappa_r(F;\zeta)\frac{x^r}{r!}
\right).
}
\]

## 3.2 Exact cumulant formula

### Project Theorem 3.1 — Cyclotomic Cumulant Formula

For

\[
F(q)=q^\alpha\prod_i(q;q)_{a_i}^{\varepsilon_i},
\]

one has, for every \(r\ge1\),

\[
\boxed{
\kappa_r(F;\zeta)
=
\alpha\,\delta_{r,1}
+
\sum_i\varepsilon_i
\sum_{m=1}^{a_i}
m^rK_r(\zeta^m).
}
\]

Here the terms with \(\zeta^m=1\) use the regularized singular value in the definition of \(K_r\).

#### Proof

Write

\[
F(\zeta e^x)
=
\zeta^\alpha e^{\alpha x}
\prod_i\prod_{m=1}^{a_i}
(1-\zeta^m e^{mx})^{\varepsilon_i}.
\]

For \(d\mid m\), separate

\[
1-e^{mx}=(-mx)s_m(x).
\]

The total product of the powers of \(-mx\) supplies precisely \(B_\zeta(F)x^h\), by Proposition 1.1. After dividing by that leading term, all remaining factors have constant term \(1\).

Take the formal logarithm. Products become sums, and the monomial \(e^{\alpha x}\) contributes \(\alpha\) only to the first derivative. Lemma 2.1 supplies \(m^rK_r(\zeta^m)\) when \(\zeta^m\ne1\), and Lemma 2.2 supplies the same expression in the regularized singular channel. Summing with multiplicities \(\varepsilon_i\) proves the theorem. ∎

### Corollary 3.2 — Additivity

For compatible compressed quotients,

\[
\boxed{
\kappa_r(FG;\zeta)
=
\kappa_r(F;\zeta)+\kappa_r(G;\zeta),
}
\]

and

\[
\boxed{
\kappa_r(F/G;\zeta)
=
\kappa_r(F;\zeta)-\kappa_r(G;\zeta).
}
\]

#### Proof

The normalized logarithm of a product is the sum of the normalized logarithms, up to the already-separated leading constants and vanishing orders. Differentiation gives the formulas. ∎

## 3.3 Residue-class spectral form

For \(0\le a<d\), define the compressed power sum

\[
P_{r,a}(F;d)
=
\sum_i\varepsilon_i
\sum_{\substack{1\le m\le a_i\\m\equiv a\pmod d}}
m^r.
\]

### Corollary 3.3 — Spectral decomposition by residue channel

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

#### Proof

Group the terms of Theorem 3.1 according to the residue class of \(m\) modulo \(d\). ∎

This is the precise spectral meaning of a cyclotomic cumulant: each residue channel contributes a power-sum amplitude multiplied by a universal root-of-unity kernel.

---
# 4. Reciprocity at a root-of-unity context

Let \(P(q)\in\mathbb R[q]\) be reciprocal of degree \(E\):

\[
\boxed{P(q^{-1})=q^{-E}P(q).}
\]

Fix a primitive \(d\)-th root \(\zeta\), and define

\[
f_\zeta(x)=P(\zeta e^x).
\]

## 4.1 Conjugate-reciprocity identity

### Project Theorem 4.1 — Local reciprocity law

For every complex \(x\) sufficiently close to zero,

\[
\boxed{
\overline{f_\zeta(-\bar x)}
=
\zeta^{-E}e^{-Ex}f_\zeta(x).
}
\]

#### Proof

Because \(P\) has real coefficients,

\[
\overline{P(z)}=P(\bar z).
\]

Hence

\[
\begin{aligned}
\overline{f_\zeta(-\bar x)}
&=
\overline{P(\zeta e^{-\bar x})}\\
&=
P(\bar\zeta e^{-x})\\
&=
P((\zeta e^x)^{-1}).
\end{aligned}
\]

Apply reciprocity with \(q=\zeta e^x\):

\[
P((\zeta e^x)^{-1})
=
(\zeta e^x)^{-E}P(\zeta e^x)
=
\zeta^{-E}e^{-Ex}f_\zeta(x).
\]

This proves the identity. ∎

## 4.2 Leading phase constraint

Suppose

\[
f_\zeta(x)=c_\zeta x^h+O(x^{h+1}),
\qquad
c_\zeta\ne0.
\]

### Corollary 4.2 — Leading phase law

\[
\boxed{
(-1)^h\overline{c_\zeta}
=
\zeta^{-E}c_\zeta.
}
\]

Equivalently,

\[
\boxed{
\frac{c_\zeta}{\overline{c_\zeta}}
=
(-1)^h\zeta^E.
}
\]

#### Proof

Compare the coefficients of \(x^h\) in Theorem 4.1. The left side contributes \((-1)^h\overline{c_\zeta}\), while the right side contributes \(\zeta^{-E}c_\zeta\). ∎

The phase of the leading residual is therefore not arbitrary: reciprocity fixes it up to a real scalar.

## 4.3 Removing depth, phase, and drift

Define

\[
\boxed{
\mathcal G_\zeta(x)
=
\frac{x^{-h}e^{-Ex/2}f_\zeta(x)}{c_\zeta}.
}
\]

Then \(\mathcal G_\zeta(0)=1\).

### Project Theorem 4.3 — Normalized reciprocal-germ symmetry

\[
\boxed{
\overline{\mathcal G_\zeta(-\bar x)}
=
\mathcal G_\zeta(x).
}
\]

#### Proof

Using Theorem 4.1,

\[
\begin{aligned}
\overline{\mathcal G_\zeta(-\bar x)}
&=
\frac{(-x)^{-h}e^{Ex/2}\overline{f_\zeta(-\bar x)}}{\overline{c_\zeta}}\\
&=
\frac{(-1)^hx^{-h}e^{Ex/2}\zeta^{-E}e^{-Ex}f_\zeta(x)}{\overline{c_\zeta}}\\
&=
\frac{(-1)^h\zeta^{-E}c_\zeta}{\overline{c_\zeta}}
\frac{x^{-h}e^{-Ex/2}f_\zeta(x)}{c_\zeta}.
\end{aligned}
\]

By Corollary 4.2,

\[
(-1)^h\zeta^{-E}c_\zeta=\overline{c_\zeta}.
\]

The scalar factor is therefore \(1\), proving the theorem. ∎

## 4.4 Real amplitude and imaginary chirality

Write

\[
\log\mathcal G_\zeta(x)
=
\sum_{r\ge1}\gamma_r(\zeta)\frac{x^r}{r!}.
\]

### Project Theorem 4.4 — Parity-reality law

For every \(r\ge1\),

\[
\boxed{
\gamma_r(\zeta)
=
(-1)^r\overline{\gamma_r(\zeta)}.
}
\]

Thus

\[
\boxed{
\gamma_{2j}(\zeta)\in\mathbb R,
\qquad
\gamma_{2j+1}(\zeta)\in i\mathbb R.
}
\]

#### Proof

Theorem 4.3 and uniqueness of the formal logarithm with zero constant term give

\[
\overline{\log\mathcal G_\zeta(-\bar x)}
=
\log\mathcal G_\zeta(x).
\]

Expanding the left side yields

\[
\sum_{r\ge1}(-1)^r\overline{\gamma_r(\zeta)}\frac{x^r}{r!}.
\]

Comparison of coefficients proves the first formula. If \(r\) is even, \(\gamma_r=\bar\gamma_r\), hence it is real. If \(r\) is odd, \(\gamma_r=-\bar\gamma_r\), hence it is purely imaginary. ∎

### Corollary 4.5 — Amplitude-phase decomposition

For real \(x\), write

\[
\log\mathcal G_\zeta(x)=A_\zeta(x)+i\Phi_\zeta(x),
\]

with \(A_\zeta,\Phi_\zeta\) real. Then

\[
\boxed{
A_\zeta(-x)=A_\zeta(x),
\qquad
\Phi_\zeta(-x)=-\Phi_\zeta(x).
}
\]

Thus the even cumulants describe local amplitude and the odd cumulants describe local phase, or **chirality**.

#### Proof

The even coefficients of the logarithm are real and the odd coefficients are purely imaginary by Theorem 4.4. Their real and imaginary parts therefore have the stated parities. ∎

---

# 5. The binary context \(d=2\): the even-germ theorem

Set

\[
\zeta=-1.
\]

This context is self-conjugate. The general chiral symmetry collapses to genuine evenness.

## 5.1 Parity of degree and defect

### Lemma 5.1 — Reciprocity parity constraint at \(-1\)

Let \(P\in\mathbb R[q]\) be reciprocal of degree \(E\), and let

\[
h=v_{q+1}(P).
\]

Then

\[
\boxed{E\equiv h\pmod2.}
\]

#### Proof

At \(\zeta=-1\), Corollary 4.2 becomes

\[
(-1)^h\bar c=(-1)^{-E}c.
\]

The germ \(P(-e^x)\) has real coefficients as a formal power series, so its leading coefficient \(c\) is real and nonzero. Hence

\[
(-1)^h=(-1)^E.
\]

Therefore \(E\equiv h\pmod2\). ∎

## 5.2 Even normalized germ

### Project Theorem 5.2 — Binary Even-Germ Theorem

Let \(P\in\mathbb R[q]\) be reciprocal of degree \(E\), and let \(h=v_{q+1}(P)\). Then

\[
\boxed{
\mathcal E_P(x)
=
x^{-h}e^{-Ex/2}P(-e^x)
}
\]

is an even formal power series:

\[
\boxed{\mathcal E_P(-x)=\mathcal E_P(x).}
\]

#### Proof

Reciprocity gives

\[
P(-e^{-x})
=
(-e^x)^{-E}P(-e^x)
=
(-1)^Ee^{-Ex}P(-e^x).
\]

Therefore

\[
\begin{aligned}
\mathcal E_P(-x)
&=
(-x)^{-h}e^{Ex/2}P(-e^{-x})\\
&=
(-1)^hx^{-h}e^{Ex/2}(-1)^Ee^{-Ex}P(-e^x)\\
&=
(-1)^{E+h}\mathcal E_P(x).
\end{aligned}
\]

By Lemma 5.1, \(E+h\) is even, so the sign is \(1\). ∎

### Corollary 5.3 — Vanishing of higher odd cumulants

After removing the depth and reciprocity drift, every odd logarithmic cumulant vanishes:

\[
\boxed{
\left.\frac{d^{2j+1}}{dx^{2j+1}}
\log\mathcal E_P(x)\right|_{x=0}
=0
\qquad(j\ge0).
}
\]

Here the \(j=0\) case says that the drift has already been removed.

#### Proof

The logarithm of an even unit is even. All odd Taylor coefficients therefore vanish. ∎

### Structural interpretation

The binary context has no independent higher odd geometry:

\[
\boxed{
\text{depth}
\;+
\text{leading residual}
\;+
\text{linear reciprocity drift}
\;+
\text{even curvature ladder}.
}
\]

This is the local mechanism behind the exceptional rigidity of \(d=2\).

---

# 6. Exact binary fingerprints for Gaussian multinomials

Let

\[
\mathbf k=(k_1,\ldots,k_c),
\qquad
k_1+\cdots+k_c=n,
\]

and

\[
M_{\mathbf k}(q)
=
{n\brack k_1,\ldots,k_c}_q.
\]

## 6.1 Defect, degree, and leading residual

Define

\[
r=\left\lfloor\frac n2\right\rfloor,
\qquad
r_\nu=\left\lfloor\frac{k_\nu}{2}\right\rfloor.
\]

### Proposition 6.1 — Binary defect

\[
\boxed{
h=v_{q+1}(M_{\mathbf k})
=r-\sum_{\nu=1}^{c}r_\nu.}
\]

#### Proof

Apply the factorial valuation formula

\[
v_{q+1}((q;q)_a)=\left\lfloor\frac a2\right\rfloor
\]

to the numerator and denominator. ∎

### Proposition 6.2 — Reciprocity degree

The multinomial is reciprocal of degree

\[
\boxed{
E(\mathbf k)
=
\sum_{1\le\mu<\nu\le c}k_\mu k_\nu
=
\frac{n^2-\sum_\nu k_\nu^2}{2}.
}
\]

#### Proof

The degree of \((q;q)_a\), ignoring its sign-normalized reciprocal transformation, is

\[
1+2+\cdots+a=\frac{a(a+1)}2.
\]

The degree of the quotient is therefore

\[
\frac{n(n+1)-\sum_\nu k_\nu(k_\nu+1)}2.
\]

Since \(\sum k_\nu=n\), the linear terms cancel, leaving

\[
\frac{n^2-\sum k_\nu^2}{2}
=
\sum_{\mu<\nu}k_\mu k_\nu.
\]

The standard reciprocal identity for each factorial quotient then gives reciprocity of this degree. ∎

### Project Proposition 6.3 — Positive \((q+1)\)-residual

Define

\[
B(\mathbf k)
=
\left.
\frac{M_{\mathbf k}(q)}{(q+1)^h}
\right|_{q=-1}.
\]

Then

\[
\boxed{
B(\mathbf k)
=
\frac{r!}{\prod_\nu r_\nu!}.
}
\]

In particular, \(B(\mathbf k)\) is a positive integer.

#### Proof

Use Proposition 1.1 with \(d=2\). For a single factorial \((q;q)_a\), the even factors contribute

\[
(-2)^{\lfloor a/2\rfloor}
\left\lfloor\frac a2\right\rfloor!,
\]

while every odd factor contributes

\[
1-(-1)=2.
\]

The net power of \(2\) in the multinomial quotient is

\[
\begin{aligned}
&\left(\left\lfloor\frac n2\right\rfloor
-
\sum_\nu\left\lfloor\frac{k_\nu}{2}\right\rfloor\right)
+
\left(\left\lceil\frac n2\right\rceil
-
\sum_\nu\left\lceil\frac{k_\nu}{2}\right\rceil\right)\\
&=h-h=0,
\end{aligned}
\]

because \(\lceil a/2\rceil=a-\lfloor a/2\rfloor\) and \(\sum k_\nu=n\).

Thus the exponential-coordinate leading coefficient is

\[
(-1)^h\frac{r!}{\prod r_\nu!}.
\]

Since

\[
q+1=1-e^x=-x+O(x^2),
\]

division by \((q+1)^h\) removes the factor \((-1)^hx^h\). The remaining value is

\[
\frac{r!}{\prod r_\nu!}.
\]

It is integral because \(\sum r_\nu=r-h\), so

\[
\frac{r!}{\prod r_\nu!}
=
h!\binom{r}{r_1,\ldots,r_c,h}.
\]

∎

## 6.2 Weighted binary power sums

For \(j\ge1\), define

\[
\boxed{
W_{2j}(a)
=
\sum_{\substack{1\le m\le a\\2\mid m}}m^{2j}
+
(2^{2j}-1)
\sum_{\substack{1\le m\le a\\2\nmid m}}m^{2j}.
}
\]

The factor \(2^{2j}-1\) is the relative visibility weight of the \(-1\) residue channel.

### Lemma 6.4 — Binary kernel values

For \(j\ge1\),

\[
\boxed{
-\operatorname{Li}_{1-2j}(-1)
=
\frac{(2^{2j}-1)B_{2j}}{2j}.
}
\]

#### Proof

Use the elementary factorization

\[
1-e^{2y}=(1-e^y)(1+e^y).
\]

After normalizing the two vanishing factors, this becomes

\[
1+e^y
=
2\,
\frac{(1-e^{2y})/(-2y)}{(1-e^y)/(-y)}.
\]

Take logarithms and apply Lemma 2.2:

\[
\begin{aligned}
\log(1+e^y)
&=
\log2
+
\log\frac{1-e^{2y}}{-2y}
-
\log\frac{1-e^y}{-y}\\
&=
\log2+
\frac y2
+
\sum_{j\ge1}
\frac{(2^{2j}-1)B_{2j}}{2j(2j)!}y^{2j}.
\end{aligned}
\]

On the other hand, Lemma 2.1 with \(\rho=-1\) and \(m=1\) says that the \(2j\)-th derivative at zero is

\[
-\operatorname{Li}_{1-2j}(-1).
\]

Reading the \(y^{2j}\)-coefficient from the displayed expansion gives

\[
-\operatorname{Li}_{1-2j}(-1)
=
\frac{(2^{2j}-1)B_{2j}}{2j}.
\]

∎

## 6.3 Complete binary cumulant normal form

### Project Theorem 6.5 — Binary Multinomial Cumulant Formula

The exact local expansion at \(q=-1\) is

\[
\boxed{
M_{\mathbf k}(-e^x)
=
(-1)^hB(\mathbf k)x^h
\exp\left(
\frac{E(\mathbf k)}2x
+
\sum_{j\ge1}
\kappa_{2j}(\mathbf k)
\frac{x^{2j}}{(2j)!}
\right),
}
\]

where every higher odd cumulant vanishes and

\[
\boxed{
\kappa_{2j}(\mathbf k)
=
\frac{B_{2j}}{2j}
\left(
W_{2j}(n)
-
\sum_{\nu=1}^{c}W_{2j}(k_\nu)
\right).
}
\]

#### Proof

The leading factor is Proposition 6.3 translated from \((q+1)^h\) to \(x^h\): since \(q+1=-x+O(x^2)\), it is \((-1)^hB(\mathbf k)x^h\).

For the first logarithmic derivative, Theorem 3.1 shows that every factor index \(m\), whether even or odd, contributes \(m/2\):

- if \(m\) is even, this is the singular kernel of Lemma 2.2;
- if \(m\) is odd, then
  \[
  -m\operatorname{Li}_0(-1)
  =-m\left(-\frac12\right)=\frac m2.
  \]

Therefore the first cumulant of \((q;q)_a\) is

\[
\frac12\sum_{m=1}^{a}m
=
\frac{a(a+1)}4.
\]

The multinomial quotient gives

\[
\frac{n(n+1)-\sum k_\nu(k_\nu+1)}4
=
\frac{E(\mathbf k)}2.
\]

For order \(2j\), an even index contributes

\[
\frac{B_{2j}}{2j}m^{2j}
\]

by the singular expansion. An odd index contributes

\[
-m^{2j}\operatorname{Li}_{1-2j}(-1)
=
\frac{(2^{2j}-1)B_{2j}}{2j}m^{2j}
\]

by Lemma 6.4. Summing gives the stated weighted power sum, and subtracting denominator factorials gives the multinomial formula.

All odd cumulants of order at least three vanish both in the singular channel and in the \(-1\) channel; equivalently, they vanish by the Binary Even-Germ Theorem. ∎

---
# 7. The binary fingerprint hierarchy

Theorem 6.5 suggests naming the first coefficients of the logarithmic germ.

## 7.1 Definitions

Define

\[
\boxed{
\Theta(\mathbf k)
=
\frac{\kappa_2(\mathbf k)}{2!}
}
\]

and

\[
\boxed{
\Lambda(\mathbf k)
=
\frac{\kappa_4(\mathbf k)}{4!}.
}
\]

More generally, define

\[
\boxed{
\Lambda_j(\mathbf k)
=
\frac{\kappa_{2j}(\mathbf k)}{(2j)!}
\qquad(j\ge1),
}
\]

so that \(\Lambda_1=\Theta\) and \(\Lambda_2=\Lambda\).

Then

\[
\boxed{
M_{\mathbf k}(-e^x)
=
(-1)^hB(\mathbf k)x^h
\exp\left(
\frac{E(\mathbf k)}2x
+
\Theta(\mathbf k)x^2
+
\Lambda(\mathbf k)x^4
+
\Lambda_3(\mathbf k)x^6
+\cdots
\right).
}
\]

The ordered local fingerprint is

\[
\boxed{
\bigl(h,B,E,\Theta,\Lambda,\Lambda_3,\ldots\bigr).
}
\]

## 7.2 Closed quadratic curvature formula

For \(j=1\),

\[
W_2(a)
=
\sum_{2\mid m}m^2+3\sum_{2\nmid m}m^2.
\]

### Lemma 7.1 — Closed form for \(W_2\)

\[
\boxed{
W_2(a)
=
\frac{a(a+1)\bigl(4a+2-3(-1)^a\bigr)}6.
}
\]

#### Proof

If \(a=2r\), then

\[
\sum_{2\mid m\le a}m^2
=4\sum_{j=1}^{r}j^2,
\]

and

\[
\sum_{2\nmid m\le a}m^2
=
\sum_{j=1}^{r}(2j-1)^2.
\]

Using

\[
\sum_{j=1}^{r}j^2=\frac{r(r+1)(2r+1)}6,
\qquad
\sum_{j=1}^{r}(2j-1)^2=\frac{r(4r^2-1)}3,
\]

one obtains

\[
W_2(2r)
=
\frac{(2r)(2r+1)(8r-1)}6.
\]

This is the stated formula for even \(a\).

If \(a=2r+1\), the even sum still has \(r\) terms and the odd sum has \(r+1\) terms. The same formulas give

\[
W_2(2r+1)
=
\frac{(2r+1)(2r+2)(8r+9)}6,
\]

which is the stated formula for odd \(a\). ∎

### Corollary 7.2 — Explicit curvature

Because \(B_2=1/6\),

\[
\kappa_2(\mathbf k)
=
\frac1{12}
\left(W_2(n)-\sum_\nu W_2(k_\nu)\right).
\]

Hence

\[
\boxed{
\Theta(\mathbf k)
=
\frac1{24}
\left(W_2(n)-\sum_\nu W_2(k_\nu)\right).
}
\]

Equivalently,

\[
\boxed{
\Theta(\mathbf k)
=
\frac1{144}
\left[
 n(n+1)(4n+2-3(-1)^n)
-
\sum_\nu k_\nu(k_\nu+1)(4k_\nu+2-3(-1)^{k_\nu})
\right].
}
\]

## 7.3 Quartic fingerprint

Since \(B_4=-1/30\),

\[
\boxed{
\Lambda(\mathbf k)
=
-\frac1{2880}
\left(
W_4(n)-\sum_\nu W_4(k_\nu)
\right),
}
\]

where

\[
W_4(a)
=
\sum_{2\mid m\le a}m^4
+15\sum_{2\nmid m\le a}m^4.
\]

## 7.4 Collision theorem from fingerprints

### Project Theorem 7.3 — Binary Fingerprint Collision Ladder

Let \(M_{\mathbf k}\) and \(M_{\mathbf l}\) be Gaussian multinomials. Assume they have the same binary defect \(h\).

1. If
   \[
   B(\mathbf k)\ne B(\mathbf l),
   \]
   then
   \[
   \boxed{v_{q+1}(M_{\mathbf k}-M_{\mathbf l})=h.}
   \]

2. If \(B(\mathbf k)=B(\mathbf l)\) but
   \[
   E(\mathbf k)\ne E(\mathbf l),
   \]
   then
   \[
   \boxed{v_{q+1}(M_{\mathbf k}-M_{\mathbf l})=h+1.}
   \]

3. Suppose \(B\) and \(E\) agree. Let \(j\ge1\) be the least index for which
   \[
   \Lambda_j(\mathbf k)\ne\Lambda_j(\mathbf l).
   \]
   Then
   \[
   \boxed{v_{q+1}(M_{\mathbf k}-M_{\mathbf l})=h+2j.}
   \]

Thus, once the linear reciprocity drift agrees, additional collision depth can increase only in even steps.

#### Proof

By Theorem 6.5,

\[
M_{\mathbf k}(-e^x)
=
(-1)^hx^hB_{\mathbf k}
\exp\left(
\frac{E_{\mathbf k}}2x
+
\sum_{r\ge1}\Lambda_r(\mathbf k)x^{2r}
\right),
\]

and similarly for \(\mathbf l\).

If the leading residuals differ, the coefficient of \(x^h\) in the difference is nonzero, proving part 1.

Assume the leading residuals agree and call the common value \(B\). Then

\[
M_{\mathbf k}(-e^x)-M_{\mathbf l}(-e^x)
=
(-1)^hBx^h
\left(e^{A_{\mathbf k}(x)}-e^{A_{\mathbf l}(x)}\right),
\]

where

\[
A_{\mathbf k}(x)
=
\frac{E_{\mathbf k}}2x+
\sum_{r\ge1}\Lambda_r(\mathbf k)x^{2r}.
\]

For any two zero-constant formal series \(A,C\),

\[
e^A-e^C=e^C(e^{A-C}-1),
\]

and \(e^C\) is a unit. Therefore

\[
\operatorname{ord}_x(e^A-e^C)
=
\operatorname{ord}_x(A-C).
\]

If the degrees differ, the first term of \(A_{\mathbf k}-A_{\mathbf l}\) is

\[
\frac{E_{\mathbf k}-E_{\mathbf l}}2x,
\]

so the total order is \(h+1\), proving part 2.

If \(E\) agrees, the difference of the logarithmic exponents is even. If \(j\) is the first differing even fingerprint, then

\[
A_{\mathbf k}(x)-A_{\mathbf l}(x)
=
\bigl(\Lambda_j(\mathbf k)-\Lambda_j(\mathbf l)\bigr)x^{2j}
+O(x^{2j+2}).
\]

Hence the difference has order \(h+2j\) in \(x\). Since \(q+1=-x+O(x^2)\), the \(x\)-order equals the \((q+1)\)-valuation. ∎

### Corollary 7.4 — No independent cubic fingerprint

If two equal-defect multinomials have the same \(B\), \(E\), and \(\Theta\), then their difference cannot first appear at order \(h+3\). It either has depth at least \(h+4\), or the polynomials agree to all orders.

#### Proof

After \(B\) and \(E\) agree, the logarithmic exponent difference is even. There is no cubic term. Apply Theorem 7.3. ∎

## 7.5 A sixth-order collision detected by the quartic fingerprint

### Example 7.5

Let

\[
\mathbf k=(12,4,3,3,3,1),
\qquad
\mathbf l=(11,6,5,2,1,1).
\]

Both have total size \(26\). Their half-floor data give

\[
h_{\mathbf k}=h_{\mathbf l}=2.
\]

Their leading residuals are equal:

\[
\begin{aligned}
B(\mathbf k)
&=
\frac{13!}{6!\,2!\,1!\,1!\,1!\,0!}
=4,324,320,\\
B(\mathbf l)
&=
\frac{13!}{5!\,3!\,2!\,1!\,0!\,0!}
=4,324,320.
\end{aligned}
\]

Their reciprocity degrees agree:

\[
E(\mathbf k)=E(\mathbf l)=244.
\]

Their quadratic curvatures also agree:

\[
\Theta(\mathbf k)=\Theta(\mathbf l)=\frac{1779}{4}.
\]

But the quartic fingerprints are

\[
\Lambda(\mathbf k)
=-\frac{1042017}{160},
\qquad
\Lambda(\mathbf l)
=-\frac{1042177}{160},
\]

so

\[
\boxed{\Lambda(\mathbf k)-\Lambda(\mathbf l)=1.}
\]

Theorem 7.3 therefore gives

\[
\boxed{
v_{q+1}
\left(
M_{\mathbf k}(q)-M_{\mathbf l}(q)
\right)
=2+4=6.
}
\]

Moreover, because \(q+1=-x+O(x^2)\) and the first exponent difference is exactly \(x^4\),

\[
\boxed{
\left.
\frac{M_{\mathbf k}(q)-M_{\mathbf l}(q)}{(q+1)^6}
\right|_{q=-1}
=4,324,320.
}
\]

This example demonstrates why \(B,E,\Theta\) are not the end of the theory: the first distinguishing datum may be the quartic cumulant.

---

# 8. The complex geometry for \(d\ge3\)

For \(d\ge3\), a primitive root \(\zeta\) is not real, so \(\zeta\) and \(\bar\zeta\) are distinct contexts. Reciprocity does not force an even local germ at either context separately.

## 8.1 Chiral normal form

Let \(P\in\mathbb R[q]\) be reciprocal of degree \(E\), and suppose

\[
P(\zeta e^x)=c_\zeta x^h+O(x^{h+1}).
\]

Theorem 4.3 gives

\[
\mathcal G_\zeta(x)
=
\frac{x^{-h}e^{-Ex/2}P(\zeta e^x)}{c_\zeta},
\qquad
\overline{\mathcal G_\zeta(-\bar x)}=\mathcal G_\zeta(x).
\]

Hence

\[
\boxed{
P(\zeta e^x)
=
c_\zeta x^h e^{Ex/2}
\exp\left(
\sum_{j\ge1}a_{2j}x^{2j}
+i\sum_{j\ge0}b_{2j+1}x^{2j+1}
\right),
}
\]

with

\[
a_{2j},b_{2j+1}\in\mathbb R.
\]

The \(a_{2j}\) are amplitude cumulants. The \(b_{2j+1}\) are phase or chiral cumulants.

### Project Theorem 8.1 — Chiral Reciprocity Theorem

At every primitive context of order \(d\ge3\):

1. even normalized cumulants are real;
2. odd normalized cumulants are purely imaginary;
3. reciprocity does not force the odd cumulants to vanish;
4. the conjugate context reverses the phase orientation.

#### Proof

Statements 1 and 2 are Theorem 4.4. For statement 3, the symmetry condition is

\[
\gamma_{2j+1}=-\overline{\gamma_{2j+1}},
\]

which permits any purely imaginary value; unlike the \(d=2\) identity, it does not identify the germ with its own reflection without conjugation.

For real \(x\), Corollary 4.5 writes the normalized logarithm as

\[
A_\zeta(x)+i\Phi_\zeta(x)
\]

with \(A\) even and \(\Phi\) odd. Replacing \(\zeta\) by \(\bar\zeta\) complex-conjugates the local data, hence changes \(i\Phi\) to \(-i\Phi\). This reverses the phase orientation. ∎

### Corollary 8.2 — The binary context is singular

The \(d=2\) theory is not the generic member of a uniform real family. It is the self-conjugate fixed-context degeneration of the chiral law.

#### Proof

For \(d=2\), \(\zeta=\bar\zeta=-1\), so conjugate reflection acts within the same real germ and forces evenness. For \(d\ge3\), the primitive context and its conjugate are distinct. ∎

---

# 9. The Spectral Visibility Theorem

The exact cumulant kernel in a nontrivial residue channel is

\[
-\operatorname{Li}_{1-r}(\rho).
\]

We now classify precisely when this kernel can vanish at a root of unity.

## 9.1 Eulerian polynomial representation

For \(n\ge1\), let

\[
A_n(z)
=
\sum_{k=0}^{n-1}
\left\langle{n\atop k}\right\rangle z^k
\]

be the \(n\)-th Eulerian polynomial.

### Classical Lemma 9.1 — Rational form of negative polylogarithms

For \(n\ge1\),

\[
\boxed{
\operatorname{Li}_{-n}(z)
=
\frac{zA_n(z)}{(1-z)^{n+1}}.
}
\]

#### Proof

Start with

\[
\operatorname{Li}_0(z)=\frac{z}{1-z}.
\]

The operator

\[
z\frac{d}{dz}
\]

raises the power in the defining series:

\[
z\frac{d}{dz}\operatorname{Li}_{-n}(z)
=
\operatorname{Li}_{-(n+1)}(z).
\]

Assume

\[
\operatorname{Li}_{-n}(z)
=
\frac{zA_n(z)}{(1-z)^{n+1}}.
\]

Differentiating gives

\[
\operatorname{Li}_{-(n+1)}(z)
=
\frac{zA_{n+1}(z)}{(1-z)^{n+2}},
\]

where

\[
\boxed{
A_{n+1}(z)
=(1+nz)A_n(z)+z(1-z)A_n'(z).
}
\]

This is the Eulerian recurrence, with \(A_1(z)=1\). Induction proves the rational form. ∎

## 9.2 Location of Eulerian roots

### Classical Lemma 9.2 — Eulerian roots are simple and negative

For every \(n\ge2\), all roots of \(A_n(z)\) are real, simple, and strictly negative.

#### Proof

We argue by induction. For \(n=2\),

\[
A_2(z)=1+z,
\]

whose single root is \(-1\).

Assume \(A_n\) has degree \(n-1\) and simple negative roots

\[
r_1<r_2<\cdots<r_{n-1}<0.
\]

At a root \(r_i\), the recurrence from Lemma 9.1 gives

\[
A_{n+1}(r_i)
=
r_i(1-r_i)A_n'(r_i).
\]

Because \(r_i<0\) and \(1-r_i>0\), the factor \(r_i(1-r_i)\) is negative. The derivative signs at consecutive simple roots of a real polynomial alternate. Hence the values

\[
A_{n+1}(r_i)
\]

also alternate in sign. By the intermediate value theorem, \(A_{n+1}\) has a root in every interval

\[
(r_i,r_{i+1}).
\]

Also,

\[
A_{n+1}(0)=1>0.
\]

At the largest root \(r_{n-1}\),

\[
A_n'(r_{n-1})>0,
\]

so

\[
A_{n+1}(r_{n-1})
=r_{n-1}(1-r_{n-1})A_n'(r_{n-1})<0.
\]

Hence there is a root in \((r_{n-1},0)\).

At the smallest root \(r_1\), the derivative has sign \((-1)^{n-2}\), so

\[
\operatorname{sgn}A_{n+1}(r_1)=(-1)^{n-1}.
\]

Because \(A_{n+1}\) has degree \(n\) and positive leading coefficient,

\[
\operatorname{sgn}A_{n+1}(z)=(-1)^n
\]

for sufficiently large negative \(z\). These signs are opposite, so there is one further root in \(( -\infty,r_1)\).

We have found \(n\) distinct negative roots, equal to the degree of \(A_{n+1}\). Therefore all roots are real, negative, and simple. ∎

## 9.3 Palindromicity and the root \(-1\)

### Classical Lemma 9.3 — Eulerian reciprocity

\[
\boxed{
A_n(z)=z^{n-1}A_n(z^{-1}).
}
\]

#### Proof

The Eulerian number

\[
\left\langle{n\atop k}\right\rangle
\]

counts permutations of \(n\) with \(k\) descents. Reverse the order of a permutation and complement every value \(i\mapsto n+1-i\). This bijection sends \(k\) descents to \(n-1-k\) descents. Hence

\[
\left\langle{n\atop k}\right\rangle
=
\left\langle{n\atop n-1-k}\right\rangle,
\]

which is exactly the reciprocal-polynomial identity. ∎

### Lemma 9.4 — When \(-1\) is an Eulerian root

For \(n\ge1\),

\[
\boxed{
A_n(-1)=0
\iff
n\text{ is even}.
}
\]

#### Proof

If \(n\) is even, then \(n-1\) is odd. Lemma 9.3 gives

\[
A_n(-1)=(-1)^{n-1}A_n(-1)=-A_n(-1),
\]

so \(A_n(-1)=0\).

Now let \(n\) be odd. Then \(A_n\) has even degree \(n-1\). By Lemma 9.2, all its roots are simple and negative. Lemma 9.3 pairs every root \(r\) with its reciprocal \(r^{-1}\). Every root other than \(-1\) belongs to a two-element reciprocal pair. If \(-1\) were also a simple root, removing it would leave an odd number of roots, which could not be partitioned into reciprocal pairs. Therefore \(-1\) is not a root. ∎

## 9.4 Visibility classification

### Project Theorem 9.5 — Spectral Visibility Theorem

Let \(\rho\ne1\) be a root of unity, and let \(r\ge1\). Then

\[
\boxed{
\operatorname{Li}_{1-r}(\rho)=0
\iff
\rho=-1
\text{ and }
r\ge3\text{ is odd}.
}
\]

#### Proof

For \(r=1\),

\[
\operatorname{Li}_0(\rho)=\frac{\rho}{1-\rho}\ne0.
\]

Now let \(r\ge2\) and put

\[
n=r-1\ge1.
\]

Lemma 9.1 gives

\[
\operatorname{Li}_{1-r}(\rho)
=
\operatorname{Li}_{-n}(\rho)
=
\frac{\rho A_n(\rho)}{(1-\rho)^{n+1}}.
\]

Because \(\rho\ne0,1\), this vanishes exactly when

\[
A_n(\rho)=0.
\]

By Lemma 9.2, every Eulerian root is real and negative. The only negative real root of unity is \(-1\). Hence \(\rho=-1\).

By Lemma 9.4, \(-1\) is a root of \(A_n\) exactly when \(n\) is even. Since \(n=r-1\), this is equivalent to \(r\) being odd. As \(r\ge2\), the first possibility is \(r=3\). This proves the classification. ∎

---

# 10. Consequences of spectral visibility

## 10.1 Full and blind channels

### Corollary 10.1 — Non-self-inverse channels see every order

If \(\rho\) is a root of unity with

\[
\rho\ne\pm1,
\]

then

\[
\boxed{
\operatorname{Li}_{1-r}(\rho)\ne0
\qquad\text{for every }r\ge1.
}
\]

Thus no cumulant order is universally invisible in such a channel.

#### Proof

The only vanishing case in Theorem 9.5 has \(\rho=-1\). ∎

### Corollary 10.2 — The \(-1\) channel loses exactly the higher odd ladder

For \(\rho=-1\),

\[
\operatorname{Li}_{1-r}(-1)=0
\]

exactly for odd \(r\ge3\). The first order and every even order remain visible.

#### Proof

This is Theorem 9.5 specialized to \(-1\). ∎

## 10.2 Unique achirality of \(d=2\)

### Project Corollary 10.3 — Unique nontrivial achiral context

Among primitive root-of-unity contexts, \(d=2\) is the unique nontrivial context in which the entire regularized spectrum is structurally blind to all higher odd cumulants.

#### Proof

At \(d=2\), the residue channels are:

- \(\rho=1\) for even factor indices, whose regularized singular kernel has no odd terms beyond the linear drift by Lemma 2.2;
- \(\rho=-1\) for odd factor indices, whose higher odd kernels vanish by Corollary 10.2.

Therefore every higher odd cumulant vanishes structurally.

For \(d\ge3\), the primitive channel \(\rho=\zeta\) satisfies \(\zeta\ne\pm1\). Corollary 10.1 shows that its kernel is nonzero at every order. Thus higher odd information is available in the spectrum, although a particular factorial quotient may still cancel it accidentally. ∎

### Caution 10.4 — Visibility is not noncancellation

The Spectral Visibility Theorem classifies zeros of the universal channel kernel. It does not say that every polynomial has a nonzero cumulant in every visible order. Different residue-class power sums may cancel.

The correct statement is:

\[
\boxed{
\text{for }\rho\ne\pm1,
\text{ vanishing is family-specific, not kernel-forced}.
}
\]

---

# 11. Exact non-expanding computation

The formulas of this chapter do not require construction of the polynomial.

## 11.1 Power sums in arithmetic progressions

For each factorial cutoff \(a\), residue class \(b\pmod d\), and order \(r\), one needs

\[
\sum_{\substack{1\le m\le a\\m\equiv b\pmod d}}m^r.
\]

Write the terms as

\[
b+d\ell,
\]

with the appropriate range of \(\ell\). Expanding by the binomial theorem reduces the sum to ordinary power sums

\[
\sum_{\ell=0}^{N}\ell^j,
\]

which are computed exactly by Faulhaber polynomials or Bernoulli polynomials.

Thus the cost depends polynomially on the cumulant order, the number of compressed factorials, the number of residue channels examined, and the bit length of the cutoffs—not on the degree or number of coefficients of \(F(q)\).

## 11.2 Exact coefficient fields

For a primitive \(d\)-th root \(\zeta\):

- \(B_\zeta(F)\) lies in \(\mathbb Q(\zeta)\), up to explicit integer factorial factors;
- every kernel \(K_r(\zeta^a)\) lies in \(\mathbb Q(\zeta)\);
- every cumulant is therefore exact in the cyclotomic field.

No floating-point approximation should be used to decide equality, reality, imaginary parity, or vanishing.

## 11.3 Suggested data structure

A local fingerprint object may contain

```text
CyclotomicCumulantGerm(
    context_order=d,
    valuation=h,
    leading_residual=B,
    reciprocity_degree=E or None,
    cumulants=(kappa_1, ..., kappa_R),
    normalization="x-coordinate"
)
```

At \(d=2\), a specialized object may expose

```text
BinaryReciprocalFingerprint(
    defect=h,
    residual=B,
    degree=E,
    theta=Theta,
    lambda4=Lambda,
    higher_even=(Lambda_3, ...)
)
```

Normalization metadata is mandatory because \(x\)-, \((q+1)\)-, \(\Phi_d\)-, and \((q^d-1)\)-residuals differ by units.

---

# 12. Testing blueprint

A reference implementation should include the following exact tests.

1. Expand single factors \(1-\rho e^{mx}\) and verify Lemmas 2.1 and 2.2 to several orders.
2. Compare Theorem 3.1 against direct symbolic expansion of small factorial quotients.
3. Verify the conjugate-reciprocity identity for random small reciprocal polynomials.
4. Verify the leading phase law at primitive roots of orders \(2\) through at least \(10\).
5. Verify that the normalized germ is even at \(d=2\).
6. Verify that normalized even cumulants are real and odd cumulants are purely imaginary for \(d\ge3\).
7. For small multinomials, compare the formulas for \(h\), \(B\), \(E\), \(\Theta\), and \(\Lambda\) with direct expansion at \(q=-1\).
8. Verify Theorem 7.3 across all small equal-defect pairs.
9. Include Example 7.5 as a regression test with depth \(6\) and residual \(4,324,320\).
10. Verify the Eulerian rational form and root classification for small \(n\).
11. Verify Theorem 9.5 for roots of unity of many small orders and cumulant orders.
12. Test enormous compressed cutoffs for which polynomial expansion is impossible.

---

# 13. Theorem inventory

| Number | Result | Status | Exact conclusion | Main mechanism |
|---|---|---|---|---|
| 1.1 | Exact leading \(x\)-residual | Project structural formula | Closed leading residual of a compressed factorial quotient | Separate multiples and nonmultiples of \(d\) |
| 2.1 | Polylogarithmic derivative formula | Classical, proved here | Regular-channel logarithmic derivatives are \(-m^r\operatorname{Li}_{1-r}(\rho)\) | Geometric-series logarithm |
| 2.2 | Regularized singular expansion | Classical, proved here | Singular-channel drift and Bernoulli even cumulants | \(\sinh\) and Bernoulli series |
| 3.1 | Cyclotomic Cumulant Formula | Project theorem | Exact cumulants of compressed \(q\)-factorial quotients | Additivity of logarithms |
| 4.1 | Local reciprocity law | Project theorem | Conjugate-reflection identity at \(\zeta\) | Reality plus polynomial reciprocity |
| 4.3 | Normalized reciprocal-germ symmetry | Project theorem | Remove depth, phase, and drift to obtain conjugate parity | Leading phase constraint |
| 4.4 | Parity-reality law | Project theorem | Even cumulants real, odd cumulants imaginary | Coefficient comparison |
| 5.2 | Binary Even-Germ Theorem | Project theorem | \(x^{-h}e^{-Ex/2}P(-e^x)\) is even | Self-conjugate reciprocity context |
| 6.3 | Binary leading residual | Project proposition | \(B=r!/\prod r_\nu!\) | Even/odd factor cancellation |
| 6.5 | Binary Multinomial Cumulant Formula | Project theorem | Exact \(B,E\), and all even cumulants | Binary kernel values |
| 7.3 | Binary Fingerprint Collision Ladder | Project theorem | Depth determined successively by \(B,E,\Lambda_1,\Lambda_2,\ldots\) | Difference of exponential germs |
| 8.1 | Chiral Reciprocity Theorem | Project theorem | \(d\ge3\) has real amplitude and imaginary phase cumulants | Distinct conjugate contexts |
| 9.5 | Spectral Visibility Theorem | Project theorem | Kernel vanishes only at \(-1\) in higher odd orders | Eulerian root geometry |
| 10.3 | Unique nontrivial achiral context | Project corollary | Only \(d=2\) loses the entire higher odd ladder | Channel classification |

---

# 14. Unified normal forms

## 14.1 General compressed quotient

\[
\boxed{
F(\zeta e^x)
=
B_\zeta(F)x^{v_{\Phi_d}(F)}
\exp\left(
\sum_{r\ge1}
\kappa_r(F;\zeta)\frac{x^r}{r!}
\right).
}
\]

Each cumulant is a finite spectral sum

\[
\boxed{
\kappa_r
=
\alpha\delta_{r,1}
+
\sum_{a=0}^{d-1}
K_r(\zeta^a)P_{r,a}.
}
\]

## 14.2 Reciprocal polynomial at \(d\ge3\)

\[
\boxed{
P(\zeta e^x)
=
c_\zeta x^he^{Ex/2}
\exp\bigl(
\text{real even amplitude}
+
i\,\text{real odd phase}
\bigr).
}
\]

## 14.3 Reciprocal polynomial at \(d=2\)

\[
\boxed{
P(-e^x)
=
c x^he^{Ex/2}
\exp\bigl(
\text{real even curvature series}
\bigr).
}
\]

For a Gaussian multinomial,

\[
\boxed{
M_{\mathbf k}(-e^x)
=
(-1)^hBx^h
\exp\left(
\frac E2x+\Theta x^2+\Lambda x^4+\cdots
\right).
}
\]

This is the complete reciprocity-based local fingerprint architecture.

---

# 15. Boundaries of this part

This chapter establishes the exact local cumulant calculus and reciprocity geometry. It does not yet give the orbit-theoretic interpretation of the jets.

The next natural chapter is:

> **Part V — Differential Cyclic Sieving:** orbit polynomials, the local-context form of CSP, exact and congruence-level derivative formulas, Fourier moments of cyclic orbits, and higher-order differential sieving for fixed-content words and subsets.

---

## End of Part IV
