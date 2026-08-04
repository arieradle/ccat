# ccat — Cyclotomic Coefficient Arithmetic

Cyclotomic Coefficient Arithmetic (CCA), also called Cyclotomic Cumulant Theory, is a monograph project developing exact arithmetic for structured `q`-polynomials — Gaussian binomials, Gaussian multinomials, and compressed `q`-factorial quotients — by resolving them into their local behavior at roots of unity.

The core dictionary underlying the whole theory:

```
common arithmetic spacing  <->  cyclotomic congruence  <->  root-of-unity collision  <->  agreement of local jets
```

Every result is exact: no floating-point approximation of a root of unity is used anywhere. The payoff is computational as much as theoretical — cyclotomic depth, leading residuals, and higher local jets of these structured polynomials can all be computed directly from compressed parameters (e.g. the indices of a Gaussian binomial), in time independent of the polynomial's degree or coefficient count.

## Contents

The theory is developed across six parts in [`theory/`](theory):

| Part | File | Scope |
|---|---|---|
| I | [`CCA_01_Foundations.md`](theory/CCA_01_Foundations.md) | Coefficient-spacing arithmetic, cyclotomic valuation of `q`-factorial quotients, the Gaussian valuation law, the `q`-Lucas contextual fingerprint, local jets at roots of unity |
| II | [`CCA_02_Gaussian_Collision_Arithmetic.md`](theory/CCA_02_Gaussian_Collision_Arithmetic.md) | The Simple-Collision Theorem, stable central-block content and spacing, specialization at `q=1`, the two exceptional binary families |
| III | [`CCA_03_Multinomial_Defects_and_Local_Residual_Geometry.md`](theory/CCA_03_Multinomial_Defects_and_Local_Residual_Geometry.md) | Gaussian multinomial residue defects, local factorial normal forms, first visible Euler jets, Fourier-moment cancellation, the regularized collision hierarchy |
| IV | [`CCA_04_Cyclotomic_Cumulants_and_Reciprocity.md`](theory/CCA_04_Cyclotomic_Cumulants_and_Reciprocity.md) | Logarithmic local germs, cyclotomic cumulant kernels, reciprocity, the `d=2` even-germ theorem, complex chirality for `d>=3`, the Spectral Visibility Theorem |
| V | [`CCA_05_Differential_Cyclic_Sieving_and_Orbit_Jets.md`](theory/CCA_05_Differential_Cyclic_Sieving_and_Orbit_Jets.md) | Canonical orbit polynomials, the cyclic sieving phenomenon as a congruence, differential (higher-jet) cyclic sieving, fixed-content word applications |
| VI | [`CCA_06_Applications_Compressed_Computation_and_Certificates.md`](theory/CCA_06_Applications_Compressed_Computation_and_Certificates.md) | Turning the theory into algorithms: instant cyclotomic valuation, stable Gaussian gcd certificates, non-expanding cumulant computation, exact collision certificates |

Each part is proof-complete and states its dependencies on earlier parts, its theorem inventory, and its open boundaries at the end.

## Central results

- **Valuation law**: the cyclotomic valuation of a compressed `q`-factorial quotient is a floor-sum on its compressed parameters — computable without ever expanding the polynomial.
- **Multinomial defect theorem**: the exact order of vanishing of a Gaussian multinomial at a primitive `d`-th root is the *residue defect* `h = (sum of residues)/d`, with an explicit nonzero leading local residual.
- **Stable Gaussian gcd theorems**: for `t >= 5` and `n >= 3t-2`, the polynomial content and spacing gcds of central Gaussian binomial blocks are exactly a terminal product of cyclotomic polynomials, and their integer specializations agree except in exactly two classified binary exceptional families.
- **Cyclotomic cumulants**: every compressed factorial quotient has an exact logarithmic local expansion at any root of unity, governed by a universal kernel built from polylogarithms at roots of unity and Bernoulli numbers.
- **Differential cyclic sieving**: ordinary cyclic sieving only matches values at roots of unity; this theory extends it to a full hierarchy of matching Euler-derivative jets, with an exact congruence-mod-`N` theorem bridging graded and orbit-theoretic jets.

## Status

This is a mathematics monograph, not (yet) a software package. Part VI specifies the algorithms, data structures, and API surface (`cyclotomic_valuation`, `q_multinomial_defect`, `cyclotomic_cumulants`, `cyclotomic_collision_certificate`, `stable_gaussian_content`, etc.) that the theory supports, as a blueprint for an eventual exact-arithmetic implementation (e.g. as a SageMath/OSCAR contribution). No implementation currently exists in this repository.
