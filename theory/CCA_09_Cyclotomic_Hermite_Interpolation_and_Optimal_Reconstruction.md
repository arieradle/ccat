# Cyclotomic Coefficient Arithmetic

## Part IX — Cyclotomic Hermite Interpolation and Optimal Jet Reconstruction

**Project:** Cyclotomic Coefficient Arithmetic / Cyclotomic Cumulant Theory  
**Document status:** Proof-complete theorem chapter  
**Scope:** Local jet–residue equivalence, cyclotomic Hermite interpolation, simultaneous reconstruction across several root-of-unity contexts, explicit Chinese-remainder reconstruction, optimality of the weighted contact budget, adaptive exact reconstruction, and certificate design.

---

# 0. Purpose and relation to Part VIII

Part VIII proved the **Global Cyclotomic Contact Budget**:

\[
\sum_{d\ge1}\varphi(d)v_{\Phi_d}(P)
\le \operatorname{span}(P)
\]

for every nonzero rational Laurent polynomial \(P\). It then deduced finite determination: if enough local Euler jets of two bounded-span polynomials agree, then the two polynomials are identical.

That result was a uniqueness theorem. The present chapter proves the complementary existence and reconstruction theorem.

Fix finitely many cyclotomic contexts \(d\), and at context \(d\) request a jet of depth \(r_d\):

\[
P(\zeta_d),\ DP(\zeta_d),\ldots,D^{r_d-1}P(\zeta_d),
\qquad
D=q\frac d{dq}.
\]

The total weighted size of this data is

\[
B=\sum_d\varphi(d)r_d.
\]

The main theorem of this chapter states:

\[
\boxed{
\text{Every exact jet packet of weighted size }B
\text{ is realized by a unique polynomial of degree }<B.
}
\]

Equivalently, the jet map

\[
\mathbb Q[q]_{<B}
\longrightarrow
\bigoplus_d\mathbb Q(\zeta_d)^{r_d}
\]

is a \(\mathbb Q\)-linear isomorphism.

Thus the weighted budget from Part VIII is not only a degree obstruction. It is the exact dimension of the available local information.

The resulting global picture is

\[
\boxed{
\text{cyclotomic jets}
\longleftrightarrow
\text{residues modulo powers of cyclotomic polynomials}
\longleftrightarrow
\text{unique bounded-degree polynomial}.
}
\]

This is a cyclotomic form of Hermite interpolation, adapted to rational polynomials, Galois orbits of roots of unity, and Euler derivatives.

The labels used below are:

- **Classical lemma:** standard algebraic input, proved here.
- **Project theorem:** a theorem established in this project.
- **Corollary:** a formal consequence.
- **Algorithmic theorem:** a correctness theorem for an exact reconstruction procedure.
- **Sharpness statement:** a result proving optimality.
- **Caution:** a distinction required for exact mathematics or software.

Throughout, \(\zeta_d\) denotes one fixed primitive \(d\)-th root of unity and

\[
K_d=\mathbb Q(\zeta_d).
\]

---

# 1. Jet packets and cyclotomic residue rings

## 1.1 Truncated polynomial spaces

For an integer \(B\ge0\), define

\[
\mathbb Q[q]_{<B}
=
\{P\in\mathbb Q[q]:\deg P<B\}.
\]

This is a \(B\)-dimensional vector space over \(\mathbb Q\), with basis

\[
1,q,\ldots,q^{B-1}.
\]

For \(B=0\), the space is \(\{0\}\).

## 1.2 Local jet packet

Fix \(d\ge1\) and \(r\ge1\).

### Definition 1.1 — Order-\(r\) cyclotomic jet

For \(P\in\mathbb Q[q]\), define

\[
\boxed{
J_{d,r}(P)
=
\bigl(P(\zeta_d),DP(\zeta_d),\ldots,D^{r-1}P(\zeta_d)\bigr)
\in K_d^r.
}
\]

This definition uses one primitive root, but because \(P\) has rational coefficients, the values at all primitive \(d\)-th roots are obtained by Galois conjugation.

### Lemma 1.2 — Kernel of the local jet map

For \(P\in\mathbb Q[q]\),

\[
\boxed{
J_{d,r}(P)=0
\iff
\Phi_d(q)^r\mid P(q).
}
\]

#### Proof

By the local jet criterion from Part I,

\[
D^jP(\zeta_d)=0
\quad(0\le j<r)
\]

if and only if

\[
v_{\Phi_d}(P)\ge r.
\]

The latter is equivalent to \(\Phi_d^r\mid P\). ∎

### Corollary 1.3 — Jet equality and congruence

For \(P,Q\in\mathbb Q[q]\),

\[
\boxed{
J_{d,r}(P)=J_{d,r}(Q)
\iff
P\equiv Q\pmod{\Phi_d^r}.
}
\]

#### Proof

Apply Lemma 1.2 to \(P-Q\). ∎

Thus the order-\(r\) jet is exactly the same information as the residue class modulo \(\Phi_d^r\).

---

# 2. The Local Cyclotomic Hermite Isomorphism

The residue ring

\[
\mathbb Q[q]/(\Phi_d^r)
\]

has dimension

\[
r\deg\Phi_d=r\varphi(d)
\]

over \(\mathbb Q\). The target jet space \(K_d^r\) has the same rational dimension:

\[
\dim_{\mathbb Q}K_d^r
=r[K_d:\mathbb Q]
=r\varphi(d).
\]

This dimension equality converts the local jet criterion into an exact representation theorem.

### Project Theorem 2.1 — Local Cyclotomic Hermite Isomorphism

For every \(d\ge1\) and \(r\ge1\), the map

\[
\boxed{
\mathcal J_{d,r}:
\mathbb Q[q]/(\Phi_d^r)
\longrightarrow
K_d^r,
\qquad
[P]\longmapsto J_{d,r}(P),
}
\]

is a well-defined \(\mathbb Q\)-linear isomorphism.

#### Proof

By Corollary 1.3, two polynomial representatives define the same jet exactly when their difference is divisible by \(\Phi_d^r\). Hence the map is well defined.

It is \(\mathbb Q\)-linear because evaluation and the Euler derivation are \(\mathbb Q\)-linear.

Its kernel consists of residue classes \([P]\) satisfying

\[
J_{d,r}(P)=0.
\]

By Lemma 1.2, this means \(\Phi_d^r\mid P\), so \([P]=0\) in the quotient. Thus the map is injective.

The source has rational dimension

\[
\deg(\Phi_d^r)=r\varphi(d).
\]

The target has rational dimension

\[
r\dim_{\mathbb Q}K_d=r\varphi(d).
\]

An injective linear map between finite-dimensional vector spaces of equal dimension is bijective. ∎

### Corollary 2.2 — Arbitrary local jet realization

For every tuple

\[
(a_0,a_1,\ldots,a_{r-1})\in K_d^r,
\]

there exists a unique polynomial \(P\in\mathbb Q[q]\) with

\[
\deg P<r\varphi(d)
\]

such that

\[
\boxed{
D^jP(\zeta_d)=a_j
\qquad(0\le j<r).
}
\]

#### Proof

Theorem 2.1 gives a unique residue class modulo \(\Phi_d^r\). Every residue class has a unique representative of degree less than

\[
\deg\Phi_d^r=r\varphi(d).
\]

∎

### Interpretation 2.3

One order-\(r\) jet at one primitive \(d\)-th root contains exactly

\[
r\varphi(d)
\]

independent rational scalar coordinates.

The factor \(\varphi(d)\) is not an overcount. A single value in \(K_d\) already carries the values at all primitive \(d\)-th roots through Galois conjugation.

---

# 3. A constructive local normal form

The dimension proof establishes existence and uniqueness. For exact computation, it is useful to have a triangular normal form.

## 3.1 Cyclotomic-adic expansion

### Classical Lemma 3.1 — Unique \(\Phi_d\)-adic normal form

Every residue class in

\[
\mathbb Q[q]/(\Phi_d^r)
\]

has a unique representative of the form

\[
\boxed{
A_0(q)+A_1(q)\Phi_d(q)+\cdots+A_{r-1}(q)\Phi_d(q)^{r-1},
}
\]

where

\[
\deg A_m<\varphi(d)
\qquad(0\le m<r).
\]

#### Proof

Existence follows by repeated Euclidean division by \(\Phi_d\).

Given \(P\), divide by \(\Phi_d\):

\[
P=A_0+\Phi_dP_1,
\qquad
\deg A_0<\deg\Phi_d.
\]

Then divide \(P_1\) by \(\Phi_d\):

\[
P_1=A_1+\Phi_dP_2.
\]

Continue through \(r-1\) steps. Modulo \(\Phi_d^r\), this gives the displayed form.

For uniqueness, suppose

\[
\sum_{m=0}^{r-1}A_m\Phi_d^m
\equiv0\pmod{\Phi_d^r}.
\]

Reducing modulo \(\Phi_d\) gives \(A_0\equiv0\pmod{\Phi_d}\). Since \(\deg A_0<\deg\Phi_d\), one has \(A_0=0\).

Divide the remaining congruence by \(\Phi_d\), then reduce again modulo \(\Phi_d\). This gives \(A_1=0\). Continue inductively. ∎

## 3.2 Triangularity of the jet system

Let

\[
c_d=D\Phi_d(\zeta_d)
=\zeta_d\Phi_d'(\zeta_d).
\]

Since \(\zeta_d\) is a simple root of \(\Phi_d\),

\[
c_d\ne0.
\]

### Lemma 3.2 — First visible derivative of a cyclotomic power

For \(m\ge0\),

\[
D^j\bigl(\Phi_d(q)^m\bigr)\big|_{q=\zeta_d}=0
\qquad(0\le j<m),
\]

and

\[
\boxed{
D^m\bigl(\Phi_d(q)^m\bigr)\big|_{q=\zeta_d}
=m!\,c_d^m.
}
\]

#### Proof

Use the exponential coordinate

\[
q=\zeta_de^x.
\]

Then

\[
\Phi_d(\zeta_de^x)=c_dx+O(x^2),
\]

because

\[
\frac d{dx}\Phi_d(\zeta_de^x)\bigg|_{x=0}
=D\Phi_d(\zeta_d)=c_d.
\]

Therefore

\[
\Phi_d(\zeta_de^x)^m
=c_d^mx^m+O(x^{m+1}).
\]

Since \(D=d/dx\), the derivatives below order \(m\) vanish, and the \(m\)-th derivative is \(m!c_d^m\). ∎

### Proposition 3.3 — Triangular local reconstruction

Suppose

\[
P(q)
\equiv
\sum_{m=0}^{r-1}A_m(q)\Phi_d(q)^m
\pmod{\Phi_d^r},
\qquad
\deg A_m<\varphi(d).
\]

Then the jet values

\[
P(\zeta_d),DP(\zeta_d),\ldots,D^{r-1}P(\zeta_d)
\]

determine the field elements

\[
A_0(\zeta_d),A_1(\zeta_d),\ldots,A_{r-1}(\zeta_d)
\]

successively by a triangular system whose diagonal entries are

\[
0!c_d^0,\ 1!c_d^1,\ldots,(r-1)!c_d^{r-1}.
\]

#### Proof

At derivative order \(j\), every term with \(m>j\) vanishes by Lemma 3.2. Thus

\[
D^jP(\zeta_d)
\]

depends only on

\[
A_0,\ldots,A_j.
\]

The contribution involving \(A_j\) is obtained by applying the Leibniz rule to

\[
A_j\Phi_d^j.
\]

At total derivative order \(j\), every term in which fewer than \(j\) derivatives land on \(\Phi_d^j\) vanishes at \(\zeta_d\). Hence the only nonzero contribution containing \(A_j(\zeta_d)\) is

\[
A_j(\zeta_d)
D^j(\Phi_d^j)(\zeta_d)
=
A_j(\zeta_d)j!c_d^j.
\]

This diagonal scalar is nonzero. Therefore, after \(A_0(\zeta_d),\ldots,A_{j-1}(\zeta_d)\) have been recovered, the order-\(j\) equation uniquely determines \(A_j(\zeta_d)\). ∎

### Corollary 3.4 — Exact local reconstruction algorithm

An order-\(r\) jet at context \(d\) can be converted exactly into the unique residue modulo \(\Phi_d^r\) by:

1. solving the triangular equations of Proposition 3.3 for \(A_m(\zeta_d)\in K_d\);
2. converting each field element \(A_m(\zeta_d)\) to its unique polynomial representative \(A_m(q)\) of degree less than \(\varphi(d)\);
3. returning
   \[
   \sum_{m=0}^{r-1}A_m(q)\Phi_d(q)^m.
   \]

The procedure uses exact arithmetic in \(K_d\) and rational polynomial arithmetic only.

---

# 4. Simultaneous cyclotomic Hermite interpolation

Let \(\mathcal D\) be a finite set of positive integers. For each \(d\in\mathcal D\), choose a depth

\[
r_d\ge1.
\]

Define the global interpolation modulus

\[
\boxed{
M_{\mathcal D,\mathbf r}(q)
=
\prod_{d\in\mathcal D}\Phi_d(q)^{r_d}.
}
\]

Its degree is

\[
\boxed{
B(\mathcal D,\mathbf r)
=
\deg M_{\mathcal D,\mathbf r}
=
\sum_{d\in\mathcal D}\varphi(d)r_d.
}
\]

## 4.1 Chinese remainder decomposition

### Classical Lemma 4.1 — Cyclotomic Chinese remainder theorem

The natural map

\[
\boxed{
\mathbb Q[q]/(M_{\mathcal D,\mathbf r})
\longrightarrow
\bigoplus_{d\in\mathcal D}
\mathbb Q[q]/(\Phi_d^{r_d})
}
\]

is a ring isomorphism.

#### Proof

Distinct cyclotomic polynomials are distinct irreducible polynomials in \(\mathbb Q[q]\), hence pairwise coprime. Their positive powers remain pairwise coprime. The ordinary Chinese remainder theorem applies. ∎

## 4.2 Global jet isomorphism

Define

\[
\mathcal J_{\mathcal D,\mathbf r}(P)
=
\bigl(J_{d,r_d}(P)\bigr)_{d\in\mathcal D}.
\]

### Project Theorem 4.2 — Global Cyclotomic Hermite Isomorphism

The map

\[
\boxed{
\mathcal J_{\mathcal D,\mathbf r}:
\mathbb Q[q]/(M_{\mathcal D,\mathbf r})
\longrightarrow
\bigoplus_{d\in\mathcal D}K_d^{r_d}
}
\]

is a \(\mathbb Q\)-linear isomorphism.

#### Proof

By Lemma 4.1,

\[
\mathbb Q[q]/(M_{\mathcal D,\mathbf r})
\cong
\bigoplus_{d\in\mathcal D}
\mathbb Q[q]/(\Phi_d^{r_d}).
\]

By Theorem 2.1, each summand is isomorphic through its local jet map to

\[
K_d^{r_d}.
\]

Taking the direct sum of these local isomorphisms proves the result. ∎

### Project Theorem 4.3 — Cyclotomic Hermite Interpolation Theorem

For every family of target jets

\[
\mathbf a_d
=
(a_{d,0},a_{d,1},\ldots,a_{d,r_d-1})
\in K_d^{r_d},
\qquad d\in\mathcal D,
\]

there exists a unique polynomial

\[
P(q)\in\mathbb Q[q]
\]

with

\[
\boxed{
\deg P<B(\mathcal D,\mathbf r)
}
\]

such that

\[
\boxed{
D^jP(\zeta_d)=a_{d,j}
\qquad
(d\in\mathcal D,\ 0\le j<r_d).
}
\]

#### Proof

Theorem 4.2 gives a unique residue class modulo

\[
M_{\mathcal D,\mathbf r}.
\]

Every residue class modulo a monic degree-\(B\) polynomial has a unique representative of degree less than \(B\). ∎

### Corollary 4.4 — No cross-context compatibility condition over \(\mathbb Q\)

Arbitrary tuples

\[
\mathbf a_d\in K_d^{r_d}
\]

may be prescribed independently for distinct contexts \(d\).

#### Proof

The target of the isomorphism in Theorem 4.2 is the full direct sum

\[
\bigoplus_dK_d^{r_d}.
\]

Surjectivity shows that every element of this direct sum occurs. ∎

### Caution 4.5 — Rational versus integral interpolation

Theorem 4.3 produces a polynomial in \(\mathbb Q[q]\). Arbitrary local jet packets need not be realizable by a polynomial in \(\mathbb Z[q]\).

Integral realizability imposes lattice conditions inside the rational jet space. Those conditions depend on the integral structure of

\[
\mathbb Z[q]/(M_{\mathcal D,\mathbf r})
\]

and are not classified in this chapter.

---

# 5. Explicit Chinese-remainder reconstruction

The preceding theorem can be made constructive.

For each \(d\in\mathcal D\), define

\[
M_d(q)
=
\frac{M_{\mathcal D,\mathbf r}(q)}{\Phi_d(q)^{r_d}}.
\]

Since \(M_d\) is coprime to \(\Phi_d^{r_d}\), there exist polynomials

\[
U_d(q),V_d(q)\in\mathbb Q[q]
\]

such that

\[
U_d(q)M_d(q)+V_d(q)\Phi_d(q)^{r_d}=1.
\]

Define the CRT idempotent

\[
\boxed{
E_d(q)
=U_d(q)M_d(q)
\pmod{M_{\mathcal D,\mathbf r}(q)}.
}
\]

Then

\[
E_d\equiv1\pmod{\Phi_d^{r_d}},
\]

while for \(e\ne d\),

\[
E_d\equiv0\pmod{\Phi_e^{r_e}}.
\]

### Algorithmic Theorem 5.1 — Explicit global reconstruction

For every \(d\in\mathcal D\), let \(H_d(q)\) be the unique polynomial of degree less than

\[
r_d\varphi(d)
\]

whose order-\(r_d\) jet equals the prescribed local packet at \(\zeta_d\).

Then the unique global interpolant of Theorem 4.3 is

\[
\boxed{
P(q)
\equiv
\sum_{d\in\mathcal D}H_d(q)E_d(q)
\pmod{M_{\mathcal D,\mathbf r}(q)},
}
\]

taken as the unique representative of degree less than \(B(\mathcal D,\mathbf r)\).

#### Proof

Fix \(e\in\mathcal D\). Modulo \(\Phi_e^{r_e}\), every summand with \(d\ne e\) vanishes because

\[
E_d\equiv0\pmod{\Phi_e^{r_e}}.
\]

The remaining summand satisfies

\[
H_eE_e\equiv H_e\pmod{\Phi_e^{r_e}}.
\]

Therefore the reconstructed polynomial has the same residue modulo \(\Phi_e^{r_e}\) as \(H_e\), and hence the prescribed jet at context \(e\).

This holds for every \(e\). Uniqueness follows from Theorem 4.3. ∎

## 5.1 Reconstruction pseudocode

```text
input:
    finite contexts d in D
    depths r_d
    exact jet packets a[d][0:r_d]

for each d in D:
    H_d = local_jet_to_residue(d, r_d, a[d])

M = product(Phi_d(q)^r_d for d in D)
P = 0

for each d in D:
    M_d = M / Phi_d(q)^r_d
    U_d = inverse_mod(M_d, Phi_d(q)^r_d)
    E_d = U_d * M_d
    P += H_d * E_d

return remainder(P, M)
```

Every step is exact.

---

# 6. Laurent-window interpolation

Cyclotomic contact is invariant under multiplication by a monomial, while ordinary degree is not. The interpolation theorem therefore has a Laurent form.

Fix an integer \(L\). Let

\[
q^L\mathbb Q[q]_{<B}
=
\{q^LQ(q):Q\in\mathbb Q[q],\ \deg Q<B\}.
\]

These are Laurent polynomials supported inside

\[
[L,L+B-1].
\]

### Lemma 6.1 — Jet transformation under monomial shift

For every integer \(L\), every \(j\ge0\), and every Laurent polynomial \(P\),

\[
\boxed{
D^j(q^{-L}P)
=
q^{-L}
\sum_{s=0}^{j}
\binom js(-L)^{j-s}D^sP.
}
\]

#### Proof

The Euler derivation satisfies

\[
D(q^{-L})=-Lq^{-L}.
\]

More generally,

\[
D^m(q^{-L})=(-L)^mq^{-L}.
\]

Apply the binomial Leibniz rule to \(q^{-L}P\). ∎

At \(q=\zeta_d\), this is an invertible lower-triangular transformation between the first \(r\) jets of \(P\) and those of \(q^{-L}P\), because its diagonal entries are \(\zeta_d^{-L}\ne0\).

### Project Theorem 6.2 — Laurent Cyclotomic Hermite Interpolation

Let

\[
B=\sum_{d\in\mathcal D}\varphi(d)r_d.
\]

Fix an integer \(L\). For every prescribed family of local jets

\[
\mathbf a_d\in K_d^{r_d},
\]

there exists a unique Laurent polynomial

\[
P(q)\in q^L\mathbb Q[q]_{<B}
\]

with those jets.

#### Proof

Use Lemma 6.1 to transform the prescribed jets of \(P\) into prescribed jets for

\[
Q=q^{-L}P.
\]

The transformation is invertible at every context. Apply Theorem 4.3 to obtain the unique \(Q\in\mathbb Q[q]_{<B}\), then set

\[
P=q^LQ.
\]

∎

### Corollary 6.3 — Exact span-window reconstruction

A rational Laurent polynomial known a priori to have support in an interval of width \(B-1\) is uniquely determined by any cyclotomic jet schedule of total weight \(B\).

---

# 7. Optimality of the weighted budget

The interpolation theorem proves that the weighted cost

\[
B=\sum_d\varphi(d)r_d
\]

is sufficient. It is also exactly necessary in the universal linear-algebraic sense.

## 7.1 Dimension optimality

### Project Theorem 7.1 — Information-theoretic optimality

The global jet map

\[
\mathbb Q[q]_{<B}
\longrightarrow
\bigoplus_{d\in\mathcal D}K_d^{r_d}
\]

uses exactly \(B\) rational scalar dimensions on both sides.

Consequently, no \(\mathbb Q\)-linear measurement map with target dimension less than \(B\) can determine every polynomial in \(\mathbb Q[q]_{<B}\).

#### Proof

The source has dimension \(B\). The target dimension is

\[
\sum_d r_d[K_d:\mathbb Q]
=
\sum_d r_d\varphi(d)
=B.
\]

The first assertion follows.

Now let

\[
T:\mathbb Q[q]_{<B}\to V
\]

be any linear map with

\[
\dim_{\mathbb Q}V<B.
\]

By rank-nullity,

\[
\dim\ker T
\ge B-\dim V>0.
\]

Hence \(T\) has a nonzero kernel element and cannot be injective. ∎

### Interpretation 7.2

A depth-\(r_d\) jet at context \(d\) is not merely assigned the weight \(\varphi(d)r_d\) because of factor degrees. It genuinely carries that many independent rational coordinates.

The global contact budget and the interpolation dimension are the same number because they describe dual sides of one structure:

\[
\boxed{
\text{degree consumed by vanishing}
=
\text{information supplied by jets}.
}
\]

## 7.2 Sharp failure below threshold

### Project Theorem 7.3 — Universal ambiguity below full budget

Let \(N\ge0\). Suppose a cyclotomic jet schedule has total weight

\[
B\le N.
\]

Then the schedule cannot determine every polynomial of degree at most \(N\).

More precisely, the nonzero polynomial

\[
M(q)=\prod_{d\in\mathcal D}\Phi_d(q)^{r_d}
\]

has degree \(B\le N\) and has zero prescribed jet at every selected context.

Thus \(0\) and \(M\) are indistinguishable by the schedule.

#### Proof

The degree formula is

\[
\deg M
=
\sum_d\varphi(d)r_d
=B.
\]

For every selected \(d\), the factor \(\Phi_d^{r_d}\) divides \(M\), so the first \(r_d\) jets vanish by Lemma 1.2. ∎

This is the reconstruction counterpart of the sharpness theorem in Part VIII.

---

# 8. Finite determination revisited as interpolation uniqueness

The finite-determination theorem of Part VIII now follows as a direct corollary of interpolation.

### Corollary 8.1 — Finite determination from equal jet packets

Let \(F,G\in\mathbb Q[q]\) satisfy

\[
\deg(F-G)<B,
\]

where

\[
B=\sum_{d\in\mathcal D}\varphi(d)r_d.
\]

If

\[
J_{d,r_d}(F)=J_{d,r_d}(G)
\qquad(d\in\mathcal D),
\]

then

\[
\boxed{F=G.}
\]

#### Proof

Both \(F\) and \(G\) are degree-\(<B\) representatives of the same global jet packet. Theorem 4.3 gives uniqueness. ∎

### Corollary 8.2 — First mismatch principle

Let \(F\ne G\) and suppose

\[
\deg(F-G)<B.
\]

Then at least one selected context contains a mismatching jet:

\[
D^jF(\zeta_d)\ne D^jG(\zeta_d)
\]

for some

\[
d\in\mathcal D,
\qquad
0\le j<r_d.
\]

#### Proof

Otherwise all selected jet packets would agree, and Corollary 8.1 would imply equality. ∎

### Definition 8.3 — Schedule-relative first separating fingerprint

Fix an order on the pairs

\[
(d,j),
\qquad d\in\mathcal D,
\quad0\le j<r_d.
\]

For \(F\ne G\), the first pair at which

\[
D^jF(\zeta_d)\ne D^jG(\zeta_d)
\]

is the **first separating fingerprint relative to the schedule**.

It is a compact exact nonidentity certificate.

---

# 9. Adaptive exact reconstruction

Interpolation can be performed incrementally. This matters when contexts and jet depths have different computational costs.

Suppose a sequence of local queries is chosen:

\[
(d_1,r_1),
(d_2,r_2),
\ldots,
\]

with distinct contexts, or with repeated contexts interpreted as increasing the known depth.

After stage \(s\), define

\[
M_s(q)
=
\prod_d\Phi_d(q)^{r_d^{(s)}},
\]

where \(r_d^{(s)}\) is the total depth known at context \(d\). Put

\[
B_s=\deg M_s
=
\sum_d\varphi(d)r_d^{(s)}.
\]

### Project Theorem 9.1 — Nested reconstruction theorem

At every stage \(s\), the collected jets determine a unique remainder

\[
R_s(q)\in\mathbb Q[q],
\qquad
\deg R_s<B_s,
\]

such that every polynomial compatible with the collected data satisfies

\[
\boxed{
P(q)\equiv R_s(q)\pmod{M_s(q)}.
}
\]

If stage \(s+1\) extends the data, then

\[
\boxed{
R_{s+1}\equiv R_s\pmod{M_s}.
}
\]

#### Proof

The existence and uniqueness of \(R_s\) is Theorem 4.3 applied to the stage-\(s\) schedule.

At stage \(s+1\), every compatible polynomial has the old jets as well as the new ones. Hence its new remainder \(R_{s+1}\) has the same residue modulo each old \(\Phi_d^{r_d^{(s)}}\) as \(R_s\). By the Chinese remainder theorem,

\[
R_{s+1}\equiv R_s\pmod{M_s}.
\]

∎

### Corollary 9.2 — Termination under a degree bound

Suppose the unknown polynomial \(P\) is known to satisfy

\[
\deg P\le N.
\]

As soon as

\[
B_s>N,
\]

one has

\[
\boxed{R_s=P.}
\]

#### Proof

Both \(P\) and \(R_s\) match the stage-\(s\) jets. Also

\[
\deg R_s<B_s
\]

and

\[
\deg P\le N<B_s.
\]

Theorem 4.3 gives uniqueness among degree-\(<B_s\) polynomials. ∎

### Algorithmic consequence

An exact black-box polynomial with a known degree bound can be reconstructed by querying root-of-unity jets until the accumulated weight exceeds that bound.

The algorithm need never sample the polynomial at a generic point.

---

# 10. Two-sided identity certificates

Parts VI and VIII introduced a terminating comparison strategy for structured expressions. The interpolation theorem clarifies its certificate semantics.

Let \(F\) and \(G\) be structured expressions whose exact jets can be computed without expansion. Let

\[
P=F-G.
\]

Assume a certified span or degree bound

\[
\operatorname{span}(P)\le N.
\]

## 10.1 Nonidentity certificate

A single mismatch

\[
D^jF(\zeta_d)\ne D^jG(\zeta_d)
\]

proves

\[
F\ne G.
\]

The certificate consists of:

- the context \(d\);
- the derivative order \(j\);
- exact representations of both algebraic values;
- a proof that the values differ in \(K_d\).

## 10.2 Identity certificate

A collection of matching jets with total weight

\[
B>N
\]

proves

\[
F=G.
\]

The certificate consists of:

- the span bound \(N\);
- the schedule \((d,r_d)\);
- exact equality proofs for every required jet;
- the arithmetic check
  \[
  \sum_d\varphi(d)r_d>N.
  \]

### Project Theorem 10.1 — Completeness of the two-sided certificate procedure

Assume exact jet computation is available and a finite span bound \(N\) is known. Then an adaptive procedure that keeps requesting jet data and whose accumulated weight eventually exceeds \(N\) must terminate with either:

1. a valid nonidentity certificate at the first mismatch; or
2. a valid identity certificate when the accumulated weight exceeds \(N\).

#### Proof

If a mismatch appears, equality is impossible.

If no mismatch appears before the accumulated weight exceeds \(N\), the finite-determination theorem gives equality.

Because the schedule is assumed eventually to exceed \(N\), one of these events occurs after finitely many queries. ∎

---

# 11. Application to compressed \(q\)-factorial expressions

Let

\[
F(q)=\sum_{u=1}^{m}c_uF_u(q),
\qquad
c_u\in\mathbb Q,
\]

where each \(F_u\) is a compressed \(q\)-factorial quotient that is known to be a polynomial or Laurent polynomial.

Parts III, IV, and VI give non-expanding methods for computing finite jets of each summand at primitive roots of unity. Linearity gives jets of \(F\).

If a support hull

\[
[L,U]
\]

is known for the entire sum, then

\[
\operatorname{span}(F)\le U-L.
\]

### Application Theorem 11.1 — Exact reconstruction of a structured sum

Let

\[
B=\sum_{d\in\mathcal D}\varphi(d)r_d.
\]

If

\[
B>U-L,
\]

then the selected cyclotomic jets determine the structured sum \(F\) uniquely.

More precisely, they reconstruct the unique Laurent polynomial supported in

\[
[L,L+B-1]
\]

with those jets, and this polynomial is \(F\).

#### Proof

By the support assumption, \(F\) belongs to

\[
q^L\mathbb Q[q]_{<U-L+1}.
\]

Since

\[
U-L+1\le B,
\]

it also belongs to

\[
q^L\mathbb Q[q]_{<B}.
\]

Apply Theorem 6.2. ∎

### Practical limitation

Reconstructing the full expanded polynomial may be output-prohibitive even though uniqueness is easy to certify.

A software implementation should therefore support three modes:

1. **certificate-only:** prove identity without expanding;
2. **modulus remainder:** return the unique remainder modulo the current interpolation modulus;
3. **full reconstruction:** materialize the polynomial only when its output size is acceptable.

---

# 12. Gaussian and multinomial reconstruction

Gaussian binomial and multinomial polynomials are monic, have constant term \(1\), and have known degree.

For

\[
M_{\mathbf k}(q)
=
{n\brack k_1,\ldots,k_c}_q,
\]

its degree is

\[
E(\mathbf k)
=
\sum_{\mu<\nu}k_\mu k_\nu.
\]

### Corollary 12.1 — Reconstruction of one Gaussian multinomial

Let

\[
B=\sum_{d\in\mathcal D}\varphi(d)r_d.
\]

If

\[
B>E(\mathbf k),
\]

then the selected local jets determine

\[
M_{\mathbf k}(q)
\]

uniquely among all rational polynomials of degree at most \(E(\mathbf k)\).

#### Proof

Apply Theorem 4.3 with the degree bound. ∎

### Corollary 12.2 — Improved comparison of two monic constant-one polynomials

Let \(F,G\in\mathbb Q[q]\) be monic of common degree \(E\), both with constant term \(1\). If \(F\ne G\), then

\[
\operatorname{span}(F-G)\le E-2.
\]

Therefore a matching jet schedule of total weight

\[
\boxed{B>E-2}
\]

forces \(F=G\).

#### Proof

The equal constant terms imply

\[
v_q(F-G)\ge1.
\]

The equal leading coefficients imply

\[
\deg(F-G)\le E-1.
\]

Hence

\[
\operatorname{span}(F-G)
\le(E-1)-1=E-2.
\]

Apply Part VIII or Corollary 8.1 after a monomial shift. ∎

This endpoint saving is directly applicable to Gaussian multinomial comparison.

---

# 13. Differential cyclic sieving reconstruction

Let \(C_N\) act on a finite set \(X\), and let

\[
O_X(q)
\]

be its canonical orbit polynomial from Part V. Suppose \(F(q)\) is a candidate graded polynomial.

If local jets of \(F\) and \(O_X\) are known at selected contexts, interpolation reconstructs their difference modulo the corresponding cyclotomic modulus.

### Project Theorem 13.1 — Finite reconstruction of a CSP correction

Let

\[
H(q)=F(q)-O_X(q).
\]

Suppose

\[
\deg H\le N.
\]

Choose a jet schedule of total weight

\[
B>N.
\]

Then the selected differences

\[
D^jF(\zeta_d)-D^jO_X(\zeta_d)
\]

reconstruct \(H(q)\) uniquely.

In particular:

- if all selected jet differences vanish, then \(F=O_X\);
- otherwise, the complete correction polynomial \(H\) can be recovered exactly.

#### Proof

Apply Theorem 4.3 to \(H\). The supplied data are exactly its local jets. ∎

### Corollary 13.2 — Reconstruction from orbit data and graded jets

If the orbit-size distribution of the action is known, then Part V computes every jet of \(O_X\) exactly from orbit moments. Therefore sufficiently many exact jets of \(F\) determine the entire graded correction

\[
F-O_X.
\]

This upgrades differential CSP from a congruence test to an exact reconstruction mechanism under a degree bound.

---

# 14. Context schedules and computational cost

The theory assigns mathematical weight

\[
w(d,r)=\varphi(d)r
\]

to a depth-\(r\) query at context \(d\). Computational cost need not be proportional to this weight.

For compressed factorial quotients, the practical cost depends on:

- the number of compressed factors;
- the derivative depth;
- the arithmetic complexity of \(K_d\);
- the representation size \(\varphi(d)\);
- simplification of residue-channel sums;
- special symmetries, especially at \(d=2\).

Thus an optimal schedule should maximize information gained per unit computational cost.

### Definition 14.1 — Information efficiency

For an estimated exact-computation cost \(C(d,r)>0\), define

\[
\boxed{
\eta(d,r)
=
\frac{\varphi(d)r}{C(d,r)}.
}
\]

This is a software-planning quantity, not an invariant of the polynomial.

### Caution 14.2

The interpolation theorem proves that every schedule with sufficient total weight is mathematically complete. It does not prove that every such schedule is computationally efficient.

At \(d=2\), the parity theorem from Part IV may make deep jets unusually cheap because all normalized higher odd cumulants vanish. At larger \(d\), exact cyclotomic-field arithmetic may dominate.

---

# 15. Theorem inventory

| Result | Statement | Status | Computational consequence |
|---|---|---|---|
| Kernel of local jet map | \(J_{d,r}(P)=0\iff\Phi_d^r\mid P\) | From Part I | Jets and residues are equivalent |
| Local Cyclotomic Hermite Isomorphism | \(\mathbb Q[q]/(\Phi_d^r)\cong K_d^r\) | Project theorem | Every local jet packet is realizable and unique modulo \(\Phi_d^r\) |
| \(\Phi_d\)-adic normal form | Unique \(\sum_{m<r}A_m\Phi_d^m\), \(\deg A_m<\varphi(d)\) | Classical lemma | Constructive local representation |
| Triangular local reconstruction | Jets recover \(A_m(\zeta_d)\) successively | Project proposition | Exact local inversion algorithm |
| Global Cyclotomic Hermite Isomorphism | \(\mathbb Q[q]/(\prod\Phi_d^{r_d})\cong\bigoplus K_d^{r_d}\) | Project theorem | Independent multi-context jet packets |
| Cyclotomic Hermite Interpolation | Unique degree-\(<B\) polynomial for any packet of weight \(B\) | Project theorem | Exact reconstruction |
| CRT reconstruction formula | \(P\equiv\sum H_dE_d\pmod M\) | Algorithmic theorem | Implementable reconstruction |
| Laurent interpolation | Unique support-window representative | Project theorem | Shift-invariant reconstruction |
| Information-theoretic optimality | Jet space and polynomial space both have dimension \(B\) | Project theorem | Weighted budget is exact |
| Ambiguity below budget | Product modulus is a nonzero kernel witness | Sharpness theorem | No smaller universal schedule suffices |
| Nested reconstruction | Stage remainders are compatible modulo earlier moduli | Project theorem | Adaptive interpolation |
| Two-sided certificate completeness | Mismatch proves inequality; excess matching weight proves equality | Project theorem | Terminating exact comparison |
| Structured-sum reconstruction | Non-expanding jets recover bounded-support sums | Application theorem | Symbolic computation without expansion |
| CSP correction reconstruction | Jets determine \(F-O_X\) under a degree bound | Project theorem | Exact differential-CSP correction |

---

# 16. Conceptual synthesis

Parts I–IV established the local equivalence

\[
\boxed{
\Phi_d^r\mid P-Q
\iff
\text{the first }r\text{ Euler jets agree at }\zeta_d.
}
\]

Part VIII established the global obstruction

\[
\boxed{
\sum_d\varphi(d)v_{\Phi_d}(P-Q)
\le
\operatorname{span}(P-Q).
}
\]

The present chapter adds the converse reconstruction theorem

\[
\boxed{
\mathbb Q[q]/\left(\prod_d\Phi_d^{r_d}\right)
\cong
\bigoplus_dK_d^{r_d}.
}
\]

Together, they form a complete local-to-global theory:

\[
\boxed{
\begin{array}{c}
\text{local jet packets}\[1mm]
\Updownarrow\[1mm]
\text{cyclotomic residue classes}\[1mm]
\Updownarrow\[1mm]
\text{unique polynomial below the weighted degree threshold}.
\end{array}
}
\]

The totient weight \(\varphi(d)\) has three simultaneous meanings:

1. it is the degree of the cyclotomic context \(\Phi_d\);
2. it is the rational dimension of one field value in \(K_d\);
3. it is the amount of global span consumed by one extra order of contact.

This threefold identity is the structural reason the theory closes exactly.

---

# 17. Open problems

## 17.1 Integral cyclotomic Hermite interpolation

Classify the image of

\[
\mathbb Z[q]/(M)
\]

inside

\[
\bigoplus_dK_d^{r_d}.
\]

Equivalently, determine exact congruence and denominator conditions for a rational jet packet to arise from an integer polynomial.

## 17.2 Optimal schedules for compressed factorial quotients

Given a span bound and a cost model for exact local cumulants, find a context-depth schedule minimizing total runtime while exceeding the required information budget.

## 17.3 Direct reconstruction in compressed form

The CRT interpolant may be enormous when expanded. Determine when the reconstructed polynomial admits a compact factorial-quotient, product, recurrence, or circuit representation.

## 17.4 Sparse recovery

If the unknown polynomial has few nonzero coefficients but very large span, can cyclotomic jets recover it from substantially less than the full span budget under a sparsity hypothesis?

## 17.5 Reciprocal-subspace interpolation

Reciprocal polynomials form a lower-dimensional linear subspace. Determine optimal cyclotomic jet schedules that exploit reciprocity directly rather than only through endpoint savings.

## 17.6 Integral proof certificates

Design certificate formats in which local residues, CRT idempotents, and reconstructed remainders can be verified inside SageMath, OSCAR, Lean, or another formal system using only exact integer and polynomial arithmetic.

---

# 18. Final statement

The main theorem of Part IX is the exact reconstruction law

\[
\boxed{
\mathbb Q[q]_{<B}
\cong
\bigoplus_{d\in\mathcal D}
\mathbb Q(\zeta_d)^{r_d},
\qquad
B=\sum_{d\in\mathcal D}\varphi(d)r_d,
}
\]

where the isomorphism sends a polynomial to its selected Euler jets.

Part VIII showed that more than \(N\) units of matching weighted contact force equality for a difference of span at most \(N\). Part IX shows why that threshold is exact: a schedule of weight \(B\) contains exactly enough information to parametrize every polynomial of degree less than \(B\), and no universally smaller linear data set can do so.

The theory therefore supports both directions:

\[
\boxed{
\text{jets}\to\text{identity certificate}
\qquad\text{and}\qquad
\text{jets}\to\text{exact reconstruction}.
}
\]
