# Cyclotomic Coefficient Arithmetic

## Part VII — Applications II: External Domains and Research Program

**Status:** Proof-complete application and research-program chapter  
**Scope:** Transfer of Cyclotomic Coefficient Arithmetic to finite geometry, subspace codes, design obstructions, structured prime-factor searches, statistical auditing, formal verification, and open-source computer algebra.

---

## 1. Purpose and epistemic boundary

The first six parts established an exact theory for structured polynomial families and converted it into non-expanding algorithms. This chapter asks a different question:

> Where can the theory solve a problem outside its original Gaussian-coefficient setting, and what would count as a genuine application rather than a superficial analogy?

The answer has four levels.

### Level I — proved transfer

Whenever an external counting problem is represented by a compressed $q$-factorial quotient, all previously proved valuation, residual, cumulant, jet, and collision theorems apply immediately.

### Level II — exact application theorem

The transferred invariants can yield rigorous divisibility certificates, obstruction witnesses, symmetry checks, and proof-carrying computations in the external domain.

### Level III — implementable research hypothesis

The theory suggests an algorithm or test whose correctness is clear, but whose usefulness must be established experimentally on real datasets or open parameter problems.

### Level IV — speculation

There is only a thematic relation, such as the common appearance of cyclotomic polynomials, but no demonstrated algorithmic advantage.

The chapter uses the labels

- **Established**,
- **Developing**,
- **Experimental**, and
- **Speculative**

throughout. These labels are part of the mathematical specification and must not be removed in later summaries.

The governing caution is

$$
\boxed{
\text{shared cyclotomic language}
\not\Rightarrow
\text{shared computational power}.
}
$$

In particular, the present theory does not by itself provide a faster general-purpose prime generator and does not constitute an attack on standard lattice cryptography.

---

## 2. The external transfer principle

### 2.1 CCA-admissible families

Let $R$ be a commutative integral domain. A family of rational functions is called **CCA-admissible** if every member has a compressed representation

$$
F(q)
=
q^\alpha
\prod_{i=1}^{s}(q;q)_{a_i}^{\varepsilon_i},
\qquad
\alpha\in\mathbb Z,
\quad
a_i\in\mathbb Z_{\ge0},
\quad
\varepsilon_i\in\mathbb Z,
$$

or a finite product of such expressions with monomials and explicitly represented cyclotomic-field constants.

The external interpretation of $F$ may be:

- a finite-geometry count;
- a code-parameter bound;
- a flag enumerator;
- an orbit-generating polynomial;
- a partition function;
- a symbolic identity appearing in a proof assistant;
- a structured integer after specializing $q=Q$.

The theory depends only on the compressed expression, not on the interpretation.

### Application Theorem 2.1 — External transfer

Let $\mathcal F$ be a CCA-admissible family. For every primitive $d$-th root of unity $\zeta$, every member of $\mathcal F$ inherits exact non-expanding algorithms for:

$$
\boxed{
 v_{\Phi_d}(F),
 \quad
 \text{its regularized local residual at }\zeta,
 \quad
 \text{its finite cyclotomic jets},
 \quad
 \text{and its local collision order with another member}.
}
$$

The computational cost is polynomial in:

1. the number of compressed factors;
2. the bit lengths of their indices and exponents;
3. the requested jet order;
4. the cost of exact arithmetic in $\mathbb Q(\zeta)$.

It is independent of the number of coefficients in the expanded polynomial.

#### Proof

Write

$$
F(q)=q^\alpha\prod_i(q;q)_{a_i}^{\varepsilon_i}.
$$

Part I proved

$$
v_{\Phi_d}(F)
=
\sum_i\varepsilon_i
\left\lfloor\frac{a_i}{d}\right\rfloor.
$$

This requires one integer division per compressed factor.

Parts III and IV showed that after removing the singular factor of order

$$
h=v_{\Phi_d}(F),
$$

the logarithm of the regularized germ is a finite signed sum of one-factor kernels. Its derivatives through order $r$ are therefore finite signed sums of progression power sums and exact cyclotomic-field terms. Bell-polynomial reconstruction then recovers the ordinary derivatives through order $r$.

For two expressions $F,G$, the local collision order is determined by their valuations and by the first unequal coefficient of their regularized germs. Every calculation is performed on the compressed factor lists and finite jets. No expanded coefficient sequence is required. ∎

### Application Corollary 2.2 — Interpretation invariance

If the same compressed expression represents two different combinatorial objects, every cyclotomic certificate computed from that expression is valid for both interpretations.

#### Proof

The certificate is an algebraic property of the rational function. An interpretation does not alter the rational function. ∎

### Practical significance

This theorem gives a rigorous test for whether an external application is real:

> Can the important quantity be written as, reduced to, or locally compared with a CCA-admissible expression?

If yes, the transfer is exact. If no, additional mathematics is required.

---

## 3. Integer specialization and guaranteed divisors

External applications often use a prime power or integer $Q\ge2$ rather than a formal variable.

### Application Theorem 3.1 — Specialized cyclotomic divisor

Let $F(q)\in\mathbb Z[q]$, and suppose

$$
v_{\Phi_d}(F)=h.
$$

Then for every integer $Q$,

$$
\boxed{
\Phi_d(Q)^h\mid F(Q).
}
$$

#### Proof

By definition of the polynomial valuation,

$$
F(q)=\Phi_d(q)^hG(q)
$$

for some $G(q)\in\mathbb Z[q]$. Evaluating at $q=Q$ gives

$$
F(Q)=\Phi_d(Q)^hG(Q).
$$

Therefore $\Phi_d(Q)^h\mid F(Q)$. ∎

### Warning 3.2 — Specialized multiplicity need not be exact

The theorem supplies a guaranteed divisor, not necessarily the complete prime factorization of $F(Q)$. Distinct integers $\Phi_d(Q)$ and $\Phi_e(Q)$ can share prime factors. Additional divisibility can also arise accidentally after evaluation.

Thus

$$
v_{\Phi_d}(F)=h
$$

does not imply that every prime dividing $\Phi_d(Q)$ occurs in $F(Q)$ with exactly the exponent predicted solely by $h$.

This is the same specialization distinction that produced the binary gap in Part II.

### Application Theorem 3.3 — Specialized quotient certificate

Let

$$
F(q)=\prod_{d\in S}\Phi_d(q)^{e_d}
$$

with $e_d\ge0$. Then the finite list

$$
\mathcal C_Q(F)=\{(d,e_d,\Phi_d(Q)):e_d>0\}
$$

is a verifiable divisibility certificate for $F(Q)$: a verifier need only check each cyclotomic evaluation and multiply the certified factors.

#### Proof

The factorization is exact in $\mathbb Z[q]$. Evaluation is a ring homomorphism. Therefore

$$
F(Q)=\prod_{d\in S}\Phi_d(Q)^{e_d}.
$$

The listed values reproduce the integer exactly. ∎

---

## 4. Finite geometry

### 4.1 Why Gaussian coefficients occur

Let $Q$ be a prime power and let $V=\mathbb F_Q^n$. The Grassmannian

$$
\operatorname{Gr}_Q(k,n)
$$

is the set of $k$-dimensional subspaces of $V$.

### Application Theorem 4.1 — Grassmannian counting theorem

The number of $k$-dimensional subspaces of $\mathbb F_Q^n$ is

$$
\boxed{
\#\operatorname{Gr}_Q(k,n)
=
{n\brack k}_Q.
}
$$

#### Proof

Count ordered linearly independent $k$-tuples in $\mathbb F_Q^n$. The first vector may be any nonzero vector, giving $Q^n-1$ choices. After choosing $j$ independent vectors, their span has $Q^j$ elements, so the next vector has $Q^n-Q^j$ choices. Hence the number of ordered independent $k$-tuples is

$$
\prod_{j=0}^{k-1}(Q^n-Q^j).
$$

Every $k$-dimensional subspace has

$$
\prod_{j=0}^{k-1}(Q^k-Q^j)
$$

ordered bases. Dividing gives

$$
\#\operatorname{Gr}_Q(k,n)
=
\prod_{j=0}^{k-1}
\frac{Q^n-Q^j}{Q^k-Q^j}.
$$

Canceling $Q^j$ in each factor yields

$$
\prod_{j=0}^{k-1}
\frac{Q^{n-j}-1}{Q^{k-j}-1}
=
{n\brack k}_Q.
$$
∎

### Application Theorem 4.2 — Flag-counting theorem

Let

$$
0=r_0<r_1<\cdots<r_c=n,
\qquad
k_i=r_i-r_{i-1}.
$$

The number of flags

$$
0=V_0<V_1<\cdots<V_c=\mathbb F_Q^n,
\qquad
\dim V_i=r_i,
$$

is

$$
\boxed{
{n\brack k_1,\ldots,k_c}_Q.
}
$$

#### Proof

Choose $V_1$, then $V_2/V_1$, and continue in the quotient spaces. The number is

$$
{n\brack r_1}_Q
{n-r_1\brack r_2-r_1}_Q
\cdots
{n-r_{c-1}\brack r_c-r_{c-1}}_Q.
$$

Writing each Gaussian binomial as a quotient of $Q$-factorials causes all intermediate factorials to cancel, leaving

$$
{n\brack k_1,\ldots,k_c}_Q.
$$
∎

### Application Theorem 4.3 — Cyclotomic Grassmannian divisor

For every $d\ge1$, define

$$
e_d(n,k)
=
\left\lfloor\frac nd\right\rfloor
-
\left\lfloor\frac kd\right\rfloor
-
\left\lfloor\frac{n-k}{d}\right\rfloor.
$$

Then $e_d(n,k)\in\{0,1\}$, and

$$
\boxed{
\prod_{d\ge1}\Phi_d(Q)^{e_d(n,k)}
=
\#\operatorname{Gr}_Q(k,n).
}
$$

Equivalently, $\Phi_d(Q)$ divides the Grassmannian size exactly when adding $k$ and $n-k$ modulo $d$ produces a carry.

#### Proof

Part I proved the polynomial factorization

$$
{n\brack k}_q
=
\prod_{d\ge1}\Phi_d(q)^{e_d(n,k)}.
$$

The exponent is a floor-function carry and therefore is either zero or one. Evaluate at $q=Q$, then use Theorem 4.1. ∎

### Application Theorem 4.4 — Flag-defect divisor

Let $n=ad$, and write

$$
k_i=r_id+s_i,
\qquad
0\le s_i<d,
\qquad
\sum_i s_i=hd.
$$

Then the number of flags of increments $(k_1,\ldots,k_c)$ is divisible by

$$
\boxed{
\Phi_d(Q)^h.
}
$$

#### Proof

Part III proved

$$
v_{\Phi_d}
\left(
{ad\brack k_1,\ldots,k_c}_q
\right)=h.
$$

Apply Theorem 3.1 and the flag-counting theorem. ∎

### Interpretation

The residue defect $h$ has two simultaneous meanings:

1. it is the number of base-$d$ carries distributed among the flag increments;
2. it is a guaranteed exponent of the integer divisor $\Phi_d(Q)$ in the flag count.

This is already a practical finite-geometry application: divisibility of enormous flag counts can be certified from the dimensions alone, with no integer expansion.

---

## 5. Subspace designs and incidence obstructions

### 5.1 Definition

A $t$-$(n,k,\lambda)_Q$ **subspace design** is a collection $\mathcal B$ of $k$-dimensional subspaces of $\mathbb F_Q^n$ such that every $t$-dimensional subspace lies in exactly $\lambda$ members of $\mathcal B$.

Let

$$
b=|\mathcal B|.
$$

### Application Theorem 5.1 — Basic incidence equation

Every $t$-$(n,k,\lambda)_Q$ subspace design satisfies

$$
\boxed{
 b{k\brack t}_Q
=
\lambda{n\brack t}_Q.
}
$$

#### Proof

Count pairs $(T,B)$, where $T$ is a $t$-subspace and $B\in\mathcal B$ contains $T$.

Counting first by blocks, each $k$-space contains ${k\brack t}_Q$ $t$-spaces, so the number of pairs is

$$
b{k\brack t}_Q.
$$

Counting first by $t$-spaces, there are ${n\brack t}_Q$ such spaces and each occurs in $\lambda$ blocks, so the number is

$$
\lambda{n\brack t}_Q.
$$

Equate the two counts. ∎

### Application Corollary 5.2 — Exact integer obstruction

A necessary condition for the existence of a $t$-$(n,k,\lambda)_Q$ design is

$$
\boxed{
\frac{{k\brack t}_Q}
{\gcd\left({k\brack t}_Q,{n\brack t}_Q\right)}
\mid\lambda.
}
$$

#### Proof

The incidence equation says

$$
{k\brack t}_Q
\mid
\lambda{n\brack t}_Q.
$$

For integers $A,B$, the divisibility $A\mid \lambda B$ is equivalent to

$$
\frac{A}{\gcd(A,B)}\mid\lambda.
$$

Take $A={k\brack t}_Q$ and $B={n\brack t}_Q$. ∎

### 5.2 Cyclotomic witnesses

The full integer gcd can be difficult when the Gaussian numbers are enormous. CCA provides small candidate witnesses.

### Application Theorem 5.3 — Prime witness obstruction

Let $p$ be a prime satisfying

$$
p\mid {k\brack t}_Q,
\qquad
p\nmid {n\brack t}_Q.
$$

If a $t$-$(n,k,\lambda)_Q$ design exists, then

$$
\boxed{p\mid\lambda.}
$$

#### Proof

Reduce the incidence equation

$$
b{k\brack t}_Q
=
\lambda{n\brack t}_Q
$$

modulo $p$. The left side is zero. Since ${n\brack t}_Q\not\equiv0\pmod p$, it is invertible modulo $p$, so $\lambda\equiv0\pmod p$. ∎

### Application Corollary 5.4 — Cyclotomic search reduction

To find a prime witness, it is sufficient to inspect contexts

$$
d\in S(k,t)\setminus S(n,t),
$$

where

$$
S(a,b)=
\left\{
 d:
 v_{\Phi_d}\left({a\brack b}_q\right)=1
\right\}.
$$

Any prime divisor of $\Phi_d(Q)$ that does not divide ${n\brack t}_Q$ is a valid witness.

#### Proof

For $d\in S(k,t)$, Theorem 4.3 gives

$$
\Phi_d(Q)
\mid
{k\brack t}_Q.
$$

If a prime factor $p\mid\Phi_d(Q)$ does not divide the numerator Gaussian number, Theorem 5.3 applies. ∎

### What CCA contributes

Without CCA, one may attempt to construct and factor two enormous Gaussian integers. With CCA, one first computes the sparse context difference

$$
S(k,t)\setminus S(n,t)
$$

using floor arithmetic. Only the corresponding cyclotomic values need to be inspected.

This does not solve every design-existence problem. It creates a targeted arithmetic obstruction engine.

### Developing research problem 5.A

**Question.** Do CCA-generated prime witnesses rule out parameter sets that survive the standard elementary divisibility conditions used in current subspace-design searches?

**Success criterion.** Produce at least one parameter family for which a small cyclotomic context yields a new compulsory divisor of $\lambda$, or reduces the feasible parameter space substantially.

**Failure criterion.** Every witness is already implied by the conventional incidence divisibility calculations at lower computational cost.

---

## 6. Constant-dimension codes and network coding

A constant-dimension subspace code is a subset

$$
\mathcal C\subseteq\operatorname{Gr}_Q(k,n)
$$

usually equipped with the subspace distance

$$
d_S(U,V)=2k-2\dim(U\cap V).
$$

Such codes arose naturally in error control for random linear network coding because packets span vector spaces and channel errors alter those spaces.

The theory does not automatically optimize code distance. Its direct role is arithmetic and symmetry analysis.

### Application Theorem 6.1 — Ambient-size certificate

The size of the ambient space of every constant-dimension code has the exact compressed certificate

$$
\boxed{
\#\operatorname{Gr}_Q(k,n)
=
\prod_{d\in S(n,k)}\Phi_d(Q),
}
$$

where $S(n,k)$ is computed by the carry criterion.

#### Proof

This is Theorem 4.3. ∎

### Application Theorem 6.2 — Free automorphism divisibility

Let a finite group $G$ act freely on a code $\mathcal C$. Then

$$
\boxed{|G|\mid|\mathcal C|.}
$$

#### Proof

Every orbit has size $|G|$ by the orbit-stabilizer theorem because every stabilizer is trivial. The code is a disjoint union of such orbits. ∎

This elementary theorem becomes useful when $|\mathcal C|$ or an upper-bound candidate is a structured Gaussian expression. CCA can determine large guaranteed divisors of that expression without evaluating it.

### Application Theorem 6.3 — Differential orbit consistency test

Suppose a cyclic group $C_N$ acts on a finite code $\mathcal C$, and $F(q)\in\mathbb Z[q]$ is proposed as a CSP polynomial for the action. Let $O_{\mathcal C}(q)$ be the canonical orbit polynomial from Part V. Then necessarily

$$
\boxed{
F(q)-O_{\mathcal C}(q)
\in(q^N-1)\mathbb Z[q].
}
$$

Consequently, for every $N$-th root $\zeta$ and every $j\ge0$,

$$
\boxed{
D^jF(\zeta)
\equiv
D^jO_{\mathcal C}(\zeta)
\pmod{N\mathbb Z[\zeta]}.
}
$$

Failure of any congruence disproves the proposed CSP model.

#### Proof

This is the Canonical CSP Congruence and Differential Comparison Theorem of Part V, applied to the code as the finite $C_N$-set. ∎

### Developing application 6.A — Symmetric code enumerators

Many code constructions carry cyclic, semilinear, or Singer-cycle symmetries. The proposed workflow is:

1. derive or conjecture a structured enumerator $F(q)$;
2. compute its CCA jets at divisors of the automorphism order;
3. compute canonical orbit moments from the proposed orbit distribution;
4. reject the model at the first incompatible jet.

The value is strongest when $F(q)$ is too large to expand but has a compressed Gaussian form.

### Boundary

CCA does not currently:

- construct an optimal subspace code;
- improve a distance bound automatically;
- decode network errors;
- replace rank-metric or linear-programming methods.

Its plausible contribution is an exact arithmetic and symmetry filter inside those searches.

---

## 7. Structured prime factors

### 7.1 What cyclotomic values guarantee

Cyclotomic values are natural sources of integers whose prime factors have controlled multiplicative order.

### Application Theorem 7.1 — Order of a cyclotomic prime divisor

Let $a\ge2$, $d\ge1$, and let $p$ be a prime such that

$$
p\nmid ad
\qquad\text{and}\qquad
p\mid\Phi_d(a).
$$

Then the multiplicative order of $a$ modulo $p$ is exactly $d$:

$$
\boxed{
\operatorname{ord}_p(a)=d.
}
$$

In particular,

$$
\boxed{d\mid p-1.}
$$

#### Proof

Since $\Phi_d(a)\mid a^d-1$, one has

$$
a^d\equiv1\pmod p.
$$

Let $r=\operatorname{ord}_p(a)$. Then $r\mid d$.

Suppose $r<d$. Since

$$
a^d-1=\prod_{e\mid d}\Phi_e(a),
$$

a prime divisor whose order is $r$ belongs to the factor corresponding to $r$, except for the well-known repeated-root phenomenon in characteristic dividing $d$. That phenomenon is excluded by $p\nmid d$.

For completeness, work in $\mathbb F_p[x]$. Because $p\nmid d$, the derivative of $x^d-1$ is

$$
dx^{d-1},
$$

which is nonzero at every nonzero root. Thus $x^d-1$ is squarefree. Its cyclotomic factors modulo $p$ are pairwise coprime. The element $a\bmod p$ is a root of $\Phi_d(x)$, so it cannot simultaneously be a root of $x^r-1$, whose irreducible factors come from $\Phi_e(x)$ with $e\mid r<d$. This contradicts $a^r\equiv1\pmod p$. Hence $r=d$.

Finally, $\mathbb F_p^\times$ has order $p-1$, so Lagrange's theorem gives $d\mid p-1$. ∎

### Application Corollary 7.2 — Congruence-constrained prime factors

Under the hypotheses above,

$$
\boxed{p\equiv1\pmod d.}
$$

Thus prime factors of $\Phi_d(a)$, away from primes dividing $ad$, are candidates for applications requiring an element of order $d$, including finite-field transforms and cyclic subgroup constructions.

### Application Theorem 7.3 — Structured-factor sieve for CCA expressions

Let

$$
F(q)=q^\alpha\prod_i(q;q)_{a_i}^{\varepsilon_i}
\in\mathbb Z[q].
$$

For every context with

$$
h_d=v_{\Phi_d}(F)>0,
$$

and every integer $a\ge2$,

$$
\boxed{
\Phi_d(a)^{h_d}\mid F(a).
}
$$

Any prime $p\nmid ad$ found in this factor has

$$
\operatorname{ord}_p(a)=d.
$$

#### Proof

The divisibility follows from Theorem 3.1. The order statement follows from Theorem 7.1. ∎

### Practical algorithm

Given a compressed expression and a desired order range:

1. compute $h_d$ by floor arithmetic;
2. discard every $d$ with $h_d\le0$;
3. evaluate only the surviving $\Phi_d(a)$;
4. trial-divide or factor those values;
5. certify the order of every prime factor not dividing $ad$.

This can be valuable when the target is not “find any prime,” but rather:

> find a prime factor supporting a prescribed cyclic order.

### Honest limitation

This is a **structured-factor sieve**, not a general fast prime generator.

It does not prove that $\Phi_d(a)$ is prime, that it has a large prime factor, or that factoring it is easy. Ordinary random generation plus primality testing remains the standard method for finding generic cryptographic primes.

### Experimental research problem 7.A

Benchmark whether CCA context filtering reduces the cost of finding prime factors with prescribed order in families of large factorial quotients.

**Success criterion.** Lower total evaluated bit volume or factoring effort than scanning unstructured candidates with the same order constraint.

**Failure criterion.** Cyclotomic evaluation and factorization dominate, producing no improvement over direct methods.

---

## 8. Fourier auditing and cryptographic boundaries

### 8.1 A rigorous statistical application

Let $X$ be an integer-valued random variable considered modulo $d$, and let $\zeta=e^{2\pi i/d}$. Define its discrete Fourier coefficients

$$
\widehat\mu(r)
=
\mathbb E[\zeta^{rX}],
\qquad
0\le r<d.
$$

### Application Theorem 8.1 — Fourier uniformity criterion

The distribution of $X\bmod d$ is uniform if and only if

$$
\boxed{
\widehat\mu(r)=0
\quad
(1\le r<d).
}
$$

#### Proof

Let

$$
p_j=\Pr(X\equiv j\pmod d).
$$

Then

$$
\widehat\mu(r)
=
\sum_{j=0}^{d-1}p_j\zeta^{rj}.
$$

The inverse discrete Fourier transform gives

$$
p_j
=
\frac1d
\sum_{r=0}^{d-1}
\widehat\mu(r)\zeta^{-rj}.
$$

Since $\widehat\mu(0)=1$, vanishing of all nontrivial coefficients gives

$$
p_j=\frac1d.
$$

Conversely, for the uniform distribution,

$$
\widehat\mu(r)
=
\frac1d\sum_{j=0}^{d-1}\zeta^{rj}=0
$$

for $r\ne0$. ∎

### Application Theorem 8.2 — Exact structured-statistic audit

Let a finite set $\Omega$ carry an integer statistic $s:\Omega\to\mathbb Z$, and let

$$
F(q)=\sum_{\omega\in\Omega}q^{s(\omega)}.
$$

If $\omega$ is sampled uniformly from $\Omega$, then

$$
\boxed{
\mathbb E[\zeta^{rs(\omega)}]
=
\frac{F(\zeta^r)}{F(1)}.
}
$$

Therefore, if $F$ is CCA-admissible, the modular bias of $s$ can be audited exactly without enumerating $\Omega$.

#### Proof

By uniformity on $\Omega$,

$$
\mathbb E[\zeta^{rs(\omega)}]
=
\frac1{|\Omega|}
\sum_{\omega\in\Omega}
\zeta^{rs(\omega)}.
$$

The numerator is $F(\zeta^r)$, and $|\Omega|=F(1)$. ∎

### Application Corollary 8.3 — Moment-enhanced audit

For $j\ge0$,

$$
\boxed{
\mathbb E
\left[
 s(\omega)^j\zeta^{rs(\omega)}
\right]
=
\frac{D^jF(\zeta^r)}{F(1)}.
}
$$

#### Proof

Since

$$
D^jq^m=m^jq^m,
$$

differentiate termwise and evaluate. ∎

This makes the Fourier-moment cancellation theorem of Part III into an exact statistical test for structured combinatorial samplers.

### Potential uses

- detecting modular bias in random word or flag generators;
- validating symmetry-preserving samplers;
- checking whether an implementation matches a claimed $q$-enumerator;
- producing exact expected values for property-based tests.

### 8.2 Relation to lattice cryptography

Ring-LWE and related systems use polynomial or number rings, often involving cyclotomic fields. Separately, root-evaluation attacks are known for specially weak Poly-LWE or Ring-LWE instances.

The current theory does **not** directly transfer to a general noisy ring equation. The reason is structural:

$$
\text{CCA analyzes exact factorial-quotient enumerators,}
$$

whereas

$$
\text{LWE security concerns noisy linear samples in quotient rings.}
$$

The common use of roots of unity is insufficient to bridge that gap.

### Experimental cryptographic audit 8.A

A legitimate experiment is nevertheless possible:

1. identify a cryptographic sampler whose exact distribution has a structured generating function;
2. compute its nontrivial Fourier coefficients and weighted jets;
3. test whether an unintended modular bias survives the protocol's reduction and noise layers;
4. quantify distinguishing advantage.

A successful result must exhibit an explicit advantage, entropy loss, or complexity reduction. Merely finding a nonzero symbolic cumulant is not a cryptographic attack.

### Boundary statement

$$
\boxed{
\text{CCA may audit structured distributions; it does not currently break standard ciphers.}
}
$$

---

## 9. Proof-carrying symbolic computation

One of the strongest external applications is not a new branch of mathematics but a new form of verifiable computation.

### 9.1 Certificate types

A **valuation certificate** for

$$
F(q)=q^\alpha\prod_i(q;q)_{a_i}^{\varepsilon_i}
$$

at context $d$ consists of the factor list and the claimed integer

$$
h=\sum_i\varepsilon_i\left\lfloor\frac{a_i}{d}\right\rfloor.
$$

A **residual certificate** additionally records the exact local residual in $\mathbb Q(\zeta_d)$.

A **jet certificate** records

$$
(h,B,\kappa_1,\ldots,\kappa_R)
$$

and enough exact intermediate sums for a checker to reconstruct the jet.

A **difference certificate** gives the first context and jet order distinguishing two compressed expressions.

### Application Theorem 9.1 — Soundness of valuation certificates

A checker that verifies

$$
h=
\sum_i\varepsilon_i
\left\lfloor\frac{a_i}{d}\right\rfloor
$$

may soundly conclude

$$
\boxed{v_{\Phi_d}(F)=h.}
$$

#### Proof

This is exactly the cyclotomic valuation theorem for compressed $q$-factorial quotients from Part I. The checker verifies its right-hand side. ∎

### Application Theorem 9.2 — Soundness of local difference certificates

Let $F$ and $G$ be polynomials. Suppose a certificate proves that

1. both have the same depth $h$ at $\zeta$;
2. their regularized germs agree through order $r-1$;
3. their regularized germs differ at order $r$.

Then

$$
\boxed{
v_{\Phi_d}(F-G)=h+r.}
$$

#### Proof

Write locally

$$
F=(q^d-1)^hR_F,
\qquad
G=(q^d-1)^hR_G,
$$

where $R_F,R_G$ are units or regular germs. Then

$$
F-G=(q^d-1)^h(R_F-R_G).
$$

Agreement through order $r-1$ and disagreement at order $r$ means

$$
\operatorname{ord}_{q=\zeta}(R_F-R_G)=r.
$$

Since $q^d-1$ has a simple zero at $\zeta$,

$$
\operatorname{ord}_{q=\zeta}(F-G)=h+r.
$$

Local depth equals $v_{\Phi_d}$. ∎

### Application Theorem 9.3 — Small-checker principle

For fixed jet order $R$, a CCA certificate can be checked using memory polynomial in the compressed input size and the degree $[\mathbb Q(\zeta_d):\mathbb Q]=\varphi(d)$, independently of the expanded degree of $F$.

#### Proof

The checker stores:

- the compressed factor map;
- $O(R)$ exact sums for each factor or residue channel;
- $O(R)$ cyclotomic-field elements;
- the Bell-polynomial reconstruction table through order $R$.

No coefficient array of $F$ is constructed. Every stored integer has size controlled by the input bit lengths, $R$, and the output arithmetic. ∎

### Consequence for formal methods

A theorem prover need not normalize an enormous polynomial. It may verify a compact arithmetic certificate whose soundness follows from a small library of general lemmas:

- floor valuations;
- cyclotomic-field identities;
- local derivative rules;
- Bell-polynomial reconstruction;
- exact comparison.

This is a natural path toward Lean, Coq, Isabelle, or proof-producing CAS integrations.

---

## 10. Open-source computer algebra

### 10.1 Existing integration points

As of August 2026:

- SageMath has a mature `sage.combinat.q_analogues` module containing Gaussian binomial, multinomial, factorial, and related functions;
- OSCAR exposes an experimental QAnalogs component, making it a natural location for exploratory exact cyclotomic functionality.

The theory's best first contribution is not a monolithic “CCA framework.” It is a narrow, independently useful primitive.

### Recommended first API

```python
q_factorial_quotient_cyclotomic_valuation(factors, d)
q_binomial_cyclotomic_valuation(n, k, d)
q_multinomial_cyclotomic_valuation(parts, d)
```

### Application Theorem 10.1 — Constant-output valuation complexity

For a canonical compressed quotient with $s$ nonzero factorial exponents, a single context valuation requires exactly $s$ floor divisions and $s-1$ additions after input validation.

#### Proof

Use

$$
v_{\Phi_d}(F)
=
\sum_{i=1}^{s}
\varepsilon_i
\left\lfloor\frac{a_i}{d}\right\rfloor.
$$

Each summand requires one division; their sum requires $s-1$ additions. ∎

### Recommended PR sequence

#### PR 1 — valuation primitives

- no polynomial expansion;
- exhaustive small tests against direct factorization;
- huge-parameter examples;
- public proof in the documentation.

#### PR 2 — local residuals

- exact cyclotomic-field output;
- explicit normalization convention;
- local/global division warnings.

#### PR 3 — finite jets

- logarithmic cumulants;
- Bell reconstruction;
- binary parity optimization.

#### PR 4 — comparison certificates

- first distinguishing context;
- contact order;
- exact residual difference;
- optional proof object.

### Why the contribution is credible

The host libraries already implement the relevant $q$-analogues. CCA adds a different operation:

$$
\boxed{
\text{inspect exact cyclotomic structure without constructing the }q\text{-analogue.}
}
$$

That is a well-scoped algorithmic capability, not merely a new name for an existing expansion routine.

---

## 11. A ranked research program

### 11.1 Program A — Production-quality cyclotomic certificates

**Status:** Established mathematics; engineering required.

#### Objective

Implement the Part VI algorithms in a standalone package, then upstream the valuation layer.

#### Deliverables

1. canonical compressed data type;
2. exact valuation engine;
3. residual and jet engine;
4. exhaustive cross-check suite;
5. benchmarks at indices with hundreds or thousands of digits;
6. machine-readable certificates.

#### Success criterion

Compare or certify polynomials whose expanded degree exceeds $10^{20}$, with runtime controlled by compressed size.

#### Main risk

The higher-jet API may be too specialized or normalization-dependent for a core library. The valuation layer has much lower risk.

---

### 11.2 Program B — Complete identity testing for bounded compressed classes

**Status:** Open mathematical problem.

#### Question

For a bounded class of compressed $q$-factorial quotients, does a finite, explicitly bounded set of cyclotomic contexts and jet orders determine equality?

The unrestricted pure factorial-quotient representation already has a trivial complete test by canonical exponent maps. The interesting version allows:

- sums of a bounded number of quotients;
- shifted quotients;
- orbit polynomials;
- structured linear combinations.

#### Target theorem

Find explicit functions $D(S,B)$ and $R(S,B)$ such that two expressions of sparsity at most $S$ and parameter bit bound $B$ are equal if and only if all cyclotomic jets agree for

$$
d\le D(S,B),
\qquad
r\le R(S,B).
$$

#### Value

This would turn the fingerprint system into a deterministic polynomial identity test for a nontrivial compressed class.

#### Failure mode

Construct pairs with arbitrarily long initial agreement across all small contexts and jets, proving that no practical universal bound exists in the proposed class.

---

### 11.3 Program C — Differential cyclic sieving as combinatorics

**Status:** Developing theory.

#### Question

What combinatorial objects are counted by

$$
D^jF(\zeta)
$$

or by the regularized first visible jet after a CSP evaluation vanishes?

#### Target theorem

Interpret

$$
\frac{D^hF(\zeta)}{h!}
$$

as a signed or weighted count of objects at a defined transverse distance from the fixed locus.

#### Success criterion

A natural statistic on cyclic orbits whose enumerator reproduces the defect core and higher jets without reverse-engineering the algebraic formula.

#### Value

This would upgrade differential CSP from a congruence formalism into a new enumerative principle.

---

### 11.4 Program D — High-order collision classification for $d\ge3$

**Status:** Open.

#### Known structure

At $d=2$, reciprocity forces the normalized germ to be even. At $d\ge3$, odd cumulants are generally nonzero and purely imaginary after normalization.

#### Question

Classify pairs of Gaussian multinomials for which

$$
v_{\Phi_d}(M_{\mathbf k}-M_{\mathbf l})
\ge h+r
$$

for $r\ge1$.

#### Target

A residue-combinatorial classification in terms of:

- defect;
- leading residual;
- reciprocal degree;
- chiral cumulants;
- residue-channel visibility.

#### Success criterion

An analogue of the binary fingerprint ladder that is finite and explicit for every fixed $d$.

---

### 11.5 Program E — Finite-geometry obstruction engine

**Status:** Implementable hypothesis.

#### Objective

Apply cyclotomic context supports to parameter searches for:

- subspace designs;
- large sets of designs;
- orbit codes;
- symmetric constant-dimension codes;
- flag-transitive structures.

#### First experiment

For each unresolved or computationally difficult parameter set:

1. derive all incidence equations;
2. compute denominator-only context supports;
3. search small cyclotomic values for prime witnesses;
4. compare against known admissibility filters.

#### Success criterion

A new parameter exclusion, forced divisor, or meaningful search-space reduction.

#### Failure criterion

No witness improves on standard divisibility conditions.

---

### 11.6 Program F — Structured prime-factor search

**Status:** Experimental.

#### Objective

Use CCA valuations to select only cyclotomic values guaranteed to divide a target structured integer, then search them for prime factors of prescribed multiplicative order.

#### Success criterion

A reproducible improvement in searches where order constraints dominate.

#### Non-goal

Competing with generic random-prime generation when no multiplicative-order structure is required.

---

### 11.7 Program G — Structured-distribution auditing

**Status:** Experimental; cryptographic relevance unproved.

#### Objective

Use exact Fourier and weighted-jet values to detect modular bias in combinatorial samplers with compressed generating functions.

#### Success criterion

Find a real implementation whose claimed distribution is contradicted by an exact cyclotomic moment, or prove a nontrivial uniformity guarantee.

#### Cryptographic threshold

To claim cryptographic significance, demonstrate a measurable distinguishing advantage or security reduction. Symbolic nonuniformity alone is insufficient.

---

### 11.8 Program H — Formal verification

**Status:** Established certificate mathematics; formalization required.

#### Objective

Formalize the valuation theorem and certificate checker first, then local residuals and jets.

#### Success criterion

A proof assistant verifies a large non-expansion certificate generated by an external CAS.

#### Value

This creates proof-carrying symbolic algebra: the fast engine computes, while a small trusted kernel checks.

---

## 12. Application triage table

| Domain | Direct algebraic bridge | Present status | Concrete useful output | Main unresolved issue |
|---|---|---:|---|---|
| Computer algebra | Compressed $q$-factorial quotient | Established | Valuations, residuals, jets, collision certificates | API and integration |
| Finite geometry | Gaussian counts of subspaces and flags | Established | Guaranteed divisors of huge counts | Strength beyond known counting formulas |
| Subspace designs | Incidence equations with Gaussian factors | Developing | Prime/divisibility obstruction witnesses | New exclusions in live parameter searches |
| Constant-dimension codes | Grassmannian sizes and cyclic symmetries | Developing | Arithmetic and orbit-consistency filters | Link to improved bounds or constructions |
| Differential CSP | Root evaluations and orbit jets | Developing theory | Higher-order symmetry congruences | Natural combinatorial interpretation |
| Prime-factor search | $\Phi_d(a)$ factors with controlled order | Experimental | Order-certified prime factors | Factoring cost and hit rate |
| Randomness auditing | Exact Fourier moments of structured enumerators | Experimental | Bias certificates and sampler tests | Real-world structured distributions |
| Cryptanalysis | Only indirect root-of-unity analogy so far | Speculative | No current attack | Noise and arbitrary ring samples fall outside CCA class |
| Formal verification | Small arithmetic certificates | Established design | Proof-carrying CAS results | Formal library implementation |
| Open-source libraries | Existing $q$-analogue modules | Immediately actionable | Mergeable valuation PR | Maintainer API decisions |

---

## 13. Theorem inventory

| Theorem | Status | External consequence |
|---|---|---|
| External Transfer Theorem | Proved | Every compressed external enumerator inherits CCA algorithms |
| Specialized Cyclotomic Divisor | Proved | Formal valuations yield guaranteed integer divisors |
| Grassmannian Counting | Classical, proved here | Gaussian coefficients count finite-field subspaces |
| Flag Counting | Classical, proved here | Multinomials count finite flags |
| Cyclotomic Grassmannian Divisor | Proved | Carry contexts factor ambient code spaces |
| Flag-Defect Divisor | Proved | Residue defect forces divisibility of flag counts |
| Subspace-Design Incidence Equation | Classical, proved here | Necessary design divisibility conditions |
| Prime Witness Obstruction | Proved | A single prime can force a divisor of $\lambda$ |
| Differential Orbit Consistency | Proved in Part V | Reject false CSP models for symmetric codes |
| Cyclotomic Prime-Order Theorem | Classical, proved here | Prime factors have prescribed multiplicative order |
| Structured-Factor Sieve | Proved | CCA narrows order-constrained factor searches |
| Fourier Uniformity Criterion | Classical, proved here | Exact root evaluations certify modular uniformity or bias |
| Structured-Statistic Audit | Proved | CCA evaluates exact Fourier biases without enumeration |
| Certificate Soundness | Proved | Small checkers verify enormous symbolic claims |
| Complete bounded jet identity test | Open | Would create a new deterministic PIT class |
| Differential CSP interpretation | Open | Would give higher jets direct combinatorial meaning |
| Finite-geometry obstruction gains | Experimental | Must be demonstrated on unresolved parameters |
| Practical prime-search speedup | Experimental | Must beat direct order-constrained searches |
| Cryptographic distinguisher | Speculative | No current evidence against standard systems |

---

## 14. Recommended next action

The highest-value next action is not to pursue cryptography or prime generation first. It is to build the exact certificate engine and then use it in two parallel demonstrations.

### Demonstration 1 — Impossible expansion

Compare two structured expressions of degree greater than $10^{20}$ and return a rigorous first-difference certificate in seconds or less.

### Demonstration 2 — External obstruction

Apply context-support analysis to a finite-geometry or subspace-design parameter search and produce either:

- a new forced divisor;
- a new impossibility witness;
- or a quantified negative result showing that the method adds no strength in that class.

The combination matters:

$$
\boxed{
\text{one undeniable computational win}
+
\text{one genuine external mathematical test}.
}
$$

That is the shortest path from a new theory to a credible research and software contribution.

---

## 15. References and external context

The following sources motivate the external domains; the theorems in this chapter are proved independently above.

1. R. Kötter and F. R. Kschischang, *Coding for Errors and Erasures in Random Network Coding*, IEEE Transactions on Information Theory 54 (2008), 3579–3591.  
   https://arxiv.org/abs/cs/0703061

2. M. Kiermaier, *On $\alpha$-points of $q$-analogs of the Fano plane*, describing subspace designs and the open $q$-Fano-plane problem.  
   https://arxiv.org/abs/2105.00365

3. V. Lyubashevsky, C. Peikert, and O. Regev, *A Toolkit for Ring-LWE Cryptography*.  
   https://web.eecs.umich.edu/~cpeikert/pubs/toolkit.pdf

4. Y. Elias, K. E. Lauter, E. Ozman, and K. E. Stange, *Provably Weak Instances of Ring-LWE*.  
   https://eprint.iacr.org/2015/106

5. SageMath, official $q$-analogues documentation.  
   https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/q_analogues.html

6. OSCAR, experimental QAnalogs documentation.  
   https://docs.oscar-system.org/dev/Experimental/QAnalogs/q_analogs/

---

## 16. Final perspective

Cyclotomic Coefficient Arithmetic is most useful when a problem has three features:

1. the object is represented by a huge structured $q$-expression;
2. expansion is infeasible or conceptually obscuring;
3. divisibility, root-of-unity behavior, symmetry, or exact comparison matters more than the coefficient list itself.

In that regime, the theory replaces expansion by local arithmetic:

$$
\boxed{
\text{structured parameters}
\longrightarrow
\text{cyclotomic contexts}
\longrightarrow
\text{depths and jets}
\longrightarrow
\text{rigorous external certificates}.
}
$$

The immediate practical achievement is exact symbolic compression. The strongest external mathematical opportunity is finite geometry and differential cyclic sieving. Prime-factor search is plausible but specialized. Cryptographic application remains a carefully delimited research hypothesis.
