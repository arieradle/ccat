"""Exception types for the CCA valuation layer.

Every error a caller can trigger by passing parameters outside a theorem's
proved hypotheses (or outside a formula's basic domain) raises one of these,
never a bare ``Exception``/``AssertionError``, so callers can distinguish
"bad input" from "input outside what has actually been proved".
"""

from __future__ import annotations


class CCAError(Exception):
    """Base class for all errors raised by :mod:`ccat`."""


class InvalidParameterError(CCAError, ValueError):
    """A parameter is outside the basic domain of the formula.

    Examples: ``d < 1``, a negative index, a binomial ``k`` outside
    ``[0, n]``, mismatched-length index/exponent lists, multinomial parts
    that don't sum to a multiple of ``d``.
    """


class StableRangeError(InvalidParameterError):
    """``(n, t)`` falls outside the stable range ``t >= 5, n >= 3t - 2``.

    The Stable Content, Stable Content-Spacing Decomposition, and Stable
    Specialization Theorems (Project Theorems 5.1, 6.1, 15.1 of CCA_02) are
    proved only in this range; CCA_02 Proposition 7.1 shows the range is
    sharp (n = 3t - 3 already admits an extra, unpredicted cyclotomic
    factor), so results outside it are not merely "unverified" but
    genuinely wrong if computed by the same formula.
    """


class DegenerateCollisionError(CCAError):
    """A requested Gaussian-binomial difference is identically the zero
    polynomial, so it has no finite cyclotomic valuation.

    Raised by :func:`ccat.valuation.simple_collision_valuation` for the
    ``M = 1`` complementary-pair case identified in Correction 3.5 of
    CCA_02: ``C(d-1, i)_q`` and ``C(d-1, d-1-i)_q`` are equal as
    polynomials (ordinary Gaussian-binomial reflection symmetry), not
    merely congruent modulo some ``Phi_d(q)``.
    """


class UnprovenRangeError(InvalidParameterError):
    """The requested input is outside the hypotheses actually proved by the
    cited theorem, and no formula is claimed for it.

    Raised by :func:`ccat.valuation.simple_collision_valuation` for
    ``M == 1`` non-complementary pairs: the Simple-Collision Theorem
    (Project Theorem 3.4, CCA_02) is proved only for ``M >= 2`` (its proof
    uses ``Md - i - j - 1 >= 2``), and CCA_02's Correction 3.5 states only
    the complementary-pair identity for ``M == 1`` -- it does not extend
    the mod-``2d`` criterion to that case.
    """
