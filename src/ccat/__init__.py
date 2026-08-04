"""ccat: the valuation layer of Cyclotomic Coefficient Arithmetic (CCA).

Exact, non-expanding cyclotomic-valuation computations for q-factorial
quotients, Gaussian binomials/multinomials, and the stable central-block
content/spacing/specialization theorems of CCA_01 and CCA_02, plus the
q-Multinomial Defect Theorem of CCA_03.

Out of scope for this package (see ``theory/`` in the repository root):
local residuals, Euler jets, cumulants, reciprocity/chirality, and
differential cyclic sieving -- material from later in CCA_03 and from
CCA_04, CCA_05, CCA_06.
"""

from .exceptions import (
    CCAError,
    DegenerateCollisionError,
    InvalidParameterError,
    StableRangeError,
    UnprovenRangeError,
)
from .polynomials import FactoredCyclotomicPolynomial, Polynomial, cyclotomic_polynomial
from .stable import stable_content, stable_integer_spacing, stable_spacing
from .valuation import (
    contextual_collapse,
    cyclotomic_valuation_q_factorial_quotient,
    q_binomial_cyclotomic_valuation,
    q_lucas_fingerprint,
    q_multinomial_cyclotomic_valuation,
    simple_collision_valuation,
)

__all__ = [
    # valuation.py
    "cyclotomic_valuation_q_factorial_quotient",
    "q_binomial_cyclotomic_valuation",
    "q_lucas_fingerprint",
    "contextual_collapse",
    "simple_collision_valuation",
    "q_multinomial_cyclotomic_valuation",
    # stable.py
    "stable_content",
    "stable_spacing",
    "stable_integer_spacing",
    # polynomials.py
    "Polynomial",
    "FactoredCyclotomicPolynomial",
    "cyclotomic_polynomial",
    # exceptions.py
    "CCAError",
    "InvalidParameterError",
    "StableRangeError",
    "DegenerateCollisionError",
    "UnprovenRangeError",
]

__version__ = "0.1.0"
