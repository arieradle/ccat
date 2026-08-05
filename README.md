# ccat — Cyclotomic Coefficient Arithmetic

Cyclotomic Coefficient Arithmetic (CCA), also called Cyclotomic Cumulant Theory, is a monograph project developing exact arithmetic for structured `q`-polynomials — Gaussian binomials, Gaussian multinomials, and compressed `q`-factorial quotients — by resolving them into their local behavior at roots of unity.

The core dictionary underlying the whole theory:

```
common arithmetic spacing  <->  cyclotomic congruence  <->  root-of-unity collision  <->  agreement of local jets
```

Every result is exact: no floating-point approximation of a root of unity is used anywhere. The payoff is computational as much as theoretical — cyclotomic depth, leading residuals, and higher local jets of these structured polynomials can all be computed directly from compressed parameters (e.g. the indices of a Gaussian binomial), in time independent of the polynomial's degree or coefficient count.

## Contents

The theory is developed across thirteen parts in [`theory/`](theory) (math is written in standard `$...$` / `$$...$$` LaTeX, so it renders directly on GitHub):

| Part | File | Scope |
|---|---|---|
| I | [`CCA_01_Foundations.md`](theory/CCA_01_Foundations.md) | Coefficient-spacing arithmetic, cyclotomic valuation of `q`-factorial quotients, the Gaussian valuation law, the `q`-Lucas contextual fingerprint, local jets at roots of unity |
| II | [`CCA_02_Gaussian_Collision_Arithmetic.md`](theory/CCA_02_Gaussian_Collision_Arithmetic.md) | The Simple-Collision Theorem, stable central-block content and spacing, specialization at `q=1`, the two exceptional binary families |
| III | [`CCA_03_Multinomial_Defects_and_Local_Residual_Geometry.md`](theory/CCA_03_Multinomial_Defects_and_Local_Residual_Geometry.md) | Gaussian multinomial residue defects, local factorial normal forms, first visible Euler jets, Fourier-moment cancellation, the regularized collision hierarchy |
| IV | [`CCA_04_Cyclotomic_Cumulants_and_Reciprocity.md`](theory/CCA_04_Cyclotomic_Cumulants_and_Reciprocity.md) | Logarithmic local germs, cyclotomic cumulant kernels, reciprocity, the `d=2` even-germ theorem, complex chirality for `d>=3`, the Spectral Visibility Theorem |
| V | [`CCA_05_Differential_Cyclic_Sieving_and_Orbit_Jets.md`](theory/CCA_05_Differential_Cyclic_Sieving_and_Orbit_Jets.md) | Canonical orbit polynomials, the cyclic sieving phenomenon as a congruence, differential (higher-jet) cyclic sieving, fixed-content word applications |
| VI | [`CCA_06_Applications_Compressed_Computation_and_Certificates.md`](theory/CCA_06_Applications_Compressed_Computation_and_Certificates.md) | Turning the theory into algorithms: instant cyclotomic valuation, stable Gaussian gcd certificates, non-expanding cumulant computation, exact collision certificates |
| VII | [`CCA_07_External_Applications_and_Research_Program.md`](theory/CCA_07_External_Applications_and_Research_Program.md) | Transfer to external domains: finite geometry, subspace codes, design obstructions, structured prime-factor search, statistical auditing, formal verification |
| VIII | [`CCA_08_Global_Cyclotomic_Contact_Budget_and_Finite_Determination.md`](theory/CCA_08_Global_Cyclotomic_Contact_Budget_and_Finite_Determination.md) | Global conservation of cyclotomic contact, weighted contact spectra, sharp finite determination by root-of-unity jets, bounded-span identity certificates |
| IX | [`CCA_09_Cyclotomic_Hermite_Interpolation_and_Optimal_Reconstruction.md`](theory/CCA_09_Cyclotomic_Hermite_Interpolation_and_Optimal_Reconstruction.md) | The converse of Part VIII's budget: cyclotomic Hermite interpolation, exact reconstruction from finite jet packets, explicit Chinese-remainder reconstruction, optimality, adaptive reconstruction, two-sided identity certificates |
| X | [`CCA_10_Reciprocal_Cyclotomic_Hermite_Interpolation_and_Half_Budget_Reconstruction.md`](theory/CCA_10_Reciprocal_Cyclotomic_Hermite_Interpolation_and_Half_Budget_Reconstruction.md) | Reciprocal-polynomial cores, ramification at `q=±1`, real-cyclotomic Hermite interpolation, the reciprocal contact budget and half-budget finite determination, Gaussian-multinomial consequences |
| XI | [`CCA_11_Sparse_Cyclotomic_Contact_Prony_Reconstruction_and_Compressed_Identity_Testing.md`](theory/CCA_11_Sparse_Cyclotomic_Contact_Prony_Reconstruction_and_Compressed_Identity_Testing.md) | Sparse Laurent polynomials, degree-independent contact bounds, optimal sparse identity testing, exact Prony reconstruction from Euler moments, cyclotomic de-aliasing, hybrid degree-sparsity certificates |
| XII | [`CCA_12_Noetherian_Multiplicity_Bounds_and_Arbitrary_Rank_Factorial_Circuit_Determination.md`](theory/CCA_12_Noetherian_Multiplicity_Bounds_and_Arbitrary_Rank_Factorial_Circuit_Determination.md) | Sums of arbitrary compressed `q`-factorial quotients, Noetherian coefficient ideals, Bautin-type multiplicity bounds, arbitrary-rank finite determination, affine-line factorial circuits |
| XIII | [`CCA_13_Sharp_Two_Term_and_One_Endpoint_Bounds_and_Effective_Base_Cases.md`](theory/CCA_13_Sharp_Two_Term_and_One_Endpoint_Bounds_and_Effective_Base_Cases.md) | Positive-endpoint local normal forms, exact two-term factorial-circuit collisions, exact arbitrary-rank one-endpoint capacity, deterministic bit-polynomial identity tests for the resulting effective subclasses |

Each part is proof-complete and states its dependencies on earlier parts, its theorem inventory, and its open boundaries at the end.

## Central results

- **Valuation law**: the cyclotomic valuation of a compressed `q`-factorial quotient is a floor-sum on its compressed parameters — computable without ever expanding the polynomial.
- **Multinomial defect theorem**: the exact order of vanishing of a Gaussian multinomial at a primitive `d`-th root is the *residue defect* `h = (sum of residues)/d`, with an explicit nonzero leading local residual.
- **Stable Gaussian gcd theorems**: for `t >= 5` and `n >= 3t-2`, the polynomial content and spacing gcds of central Gaussian binomial blocks are exactly a terminal product of cyclotomic polynomials, and their integer specializations agree except in exactly two classified binary exceptional families.
- **Cyclotomic cumulants**: every compressed factorial quotient has an exact logarithmic local expansion at any root of unity, governed by a universal kernel built from polylogarithms at roots of unity and Bernoulli numbers.
- **Differential cyclic sieving**: ordinary cyclic sieving only matches values at roots of unity; this theory extends it to a full hierarchy of matching Euler-derivative jets, with an exact congruence-mod-`N` theorem bridging graded and orbit-theoretic jets.

## Implementation

The `ccat` package (in [`src/ccat`](src/ccat)) implements the **valuation layer**: the non-expanding cyclotomic-valuation theorems of Parts I and II, plus the defect statement of Part III — deliberately the smallest coherent, independently-useful slice of the theory, shaped so it could plausibly become a future contribution to a project like SageMath. It does **not** implement local residuals, Euler jets, cumulants, reciprocity/chirality, differential cyclic sieving, or any of the contact-budget/interpolation/sparsity material (the rest of Part III, and Parts IV–XIII) — that is future work.

| Function | Theorem |
|---|---|
| `cyclotomic_valuation_q_factorial_quotient` | Theorem 4.2, CCA_01 |
| `q_binomial_cyclotomic_valuation` | Theorem 5.1, CCA_01 |
| `q_lucas_fingerprint`, `contextual_collapse` | Theorem 6.3 + Project Theorem 6.5, CCA_01 |
| `simple_collision_valuation` | Project Theorem 3.4 + Correction 3.5, CCA_02 |
| `stable_content`, `stable_spacing` | Project Theorems 5.1 and 6.1, CCA_02 |
| `stable_integer_spacing` | Project Theorems 9.1, 13.1, 15.1, CCA_02 |
| `q_multinomial_cyclotomic_valuation` | Project Theorem 3.1, CCA_03 |

Every formula is exact (integer/rational arithmetic only, no floating point) and, except for the q-Lucas fingerprint, computed directly from compressed integer parameters without ever constructing or expanding a polynomial — correctness and runtime depend only on the bit length of the inputs. The package itself has zero runtime dependencies; `sympy` is used only in the test suite as an independent brute-force oracle.

```
pip install -e '.[dev]'
pytest
```

## Status

Parts I, II, and the defect statement of III have a working, tested implementation (see above). The rest of the monograph — local residuals, jets, cumulants, reciprocity, differential cyclic sieving, contact budgets and Hermite reconstruction, sparse/Prony reconstruction, Noetherian multiplicity bounds, and the external-application chapters — remains theory only, in `theory/`, pending future implementation phases.
