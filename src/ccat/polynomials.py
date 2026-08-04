"""A minimal exact integer-coefficient polynomial ring, plus the small pieces
of machinery built on it: cyclotomic polynomials, small Gaussian binomials,
and a factored (non-expanding) representation for the stable-range content
and spacing polynomials.

This module exists only because two theorems genuinely need a real (small)
polynomial: the q-Lucas fingerprint (Theorem 6.3, CCA_01) reduces a bounded
Gaussian binomial modulo ``Phi_d(q)``, and the stable content/spacing
theorems (CCA_02) are naturally represented -- and, per CCA_01 Section 4.1
and CCA_06 Algorithms 4.1/4.2, should be *returned* -- as a factored product
of cyclotomic polynomials rather than expanded. None of the closed-form
valuation formulas in :mod:`ccat.valuation` route through polynomial
construction at all.
"""

from __future__ import annotations

import functools
from dataclasses import dataclass
from typing import Iterable, Tuple, Union

Coefficients = Union["Polynomial", int]


class Polynomial:
    """An exact integer-coefficient polynomial in one variable ``q``.

    Coefficients are stored densely in ascending power order (index ``i``
    holds the coefficient of ``q**i``), with trailing zeros stripped, so
    equal polynomials always have equal ``coeffs`` tuples and the zero
    polynomial is always ``Polynomial(())``.
    """

    __slots__ = ("coeffs",)

    def __init__(self, coeffs: Iterable[int]):
        c = tuple(int(x) for x in coeffs)
        while c and c[-1] == 0:
            c = c[:-1]
        self.coeffs: Tuple[int, ...] = c

    @classmethod
    def zero(cls) -> "Polynomial":
        return cls(())

    @classmethod
    def constant(cls, value: int) -> "Polynomial":
        return cls((value,))

    @classmethod
    def monomial(cls, power: int, coeff: int = 1) -> "Polynomial":
        if power < 0:
            raise ValueError("power must be >= 0")
        return cls((0,) * power + (coeff,))

    @property
    def degree(self) -> int:
        """Degree of the polynomial; -1 for the zero polynomial."""
        return len(self.coeffs) - 1

    def is_zero(self) -> bool:
        return not self.coeffs

    def is_monic(self) -> bool:
        return bool(self.coeffs) and self.coeffs[-1] == 1

    def shift(self, k: int) -> "Polynomial":
        """Multiply by ``q**k`` for ``k >= 0``."""
        if k < 0:
            raise ValueError("k must be >= 0")
        if self.is_zero() or k == 0:
            return self
        return Polynomial((0,) * k + self.coeffs)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        if isinstance(other, int):
            return self.coeffs == Polynomial.constant(other).coeffs
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.coeffs)

    def __add__(self, other: Coefficients) -> "Polynomial":
        other = _as_polynomial(other)
        n = max(len(self.coeffs), len(other.coeffs))
        return Polynomial(
            _get(self.coeffs, i) + _get(other.coeffs, i) for i in range(n)
        )

    __radd__ = __add__

    def __sub__(self, other: Coefficients) -> "Polynomial":
        other = _as_polynomial(other)
        n = max(len(self.coeffs), len(other.coeffs))
        return Polynomial(
            _get(self.coeffs, i) - _get(other.coeffs, i) for i in range(n)
        )

    def __rsub__(self, other: Coefficients) -> "Polynomial":
        return _as_polynomial(other).__sub__(self)

    def __neg__(self) -> "Polynomial":
        return Polynomial(-c for c in self.coeffs)

    def __mul__(self, other: Coefficients) -> "Polynomial":
        other = _as_polynomial(other)
        if self.is_zero() or other.is_zero():
            return Polynomial.zero()
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i, a in enumerate(self.coeffs):
            if a == 0:
                continue
            for j, b in enumerate(other.coeffs):
                if b:
                    result[i + j] += a * b
        return Polynomial(result)

    __rmul__ = __mul__

    def divmod_monic(self, divisor: "Polynomial") -> Tuple["Polynomial", "Polynomial"]:
        """Exact division by a *monic* divisor, over the integers.

        Returns ``(quotient, remainder)`` with
        ``self == quotient * divisor + remainder`` and
        ``remainder.degree < divisor.degree``. Because the divisor is
        monic, every step of schoolbook division is exact over ``Z`` (no
        rational coefficients ever appear) -- this is what lets
        :func:`cyclotomic_polynomial` and the q-Lucas reduction stay
        integral throughout.
        """
        if divisor.is_zero():
            raise ZeroDivisionError("division by the zero polynomial")
        if not divisor.is_monic():
            raise ValueError("divisor must be monic")

        remainder = list(self.coeffs)
        d_deg = divisor.degree
        q_len = max(0, len(remainder) - d_deg)
        quotient = [0] * q_len

        for i in range(len(remainder) - 1, d_deg - 1, -1):
            coeff = remainder[i]
            if coeff == 0:
                continue
            quotient[i - d_deg] = coeff
            for j, dc in enumerate(divisor.coeffs):
                remainder[i - d_deg + j] -= coeff * dc

        return Polynomial(quotient), Polynomial(remainder)

    def __repr__(self) -> str:
        return f"Polynomial({self.coeffs!r})"


def _get(coeffs: Tuple[int, ...], i: int) -> int:
    return coeffs[i] if i < len(coeffs) else 0


def _as_polynomial(value: Coefficients) -> Polynomial:
    if isinstance(value, Polynomial):
        return value
    if isinstance(value, int):
        return Polynomial.constant(value)
    raise TypeError(f"cannot interpret {value!r} as a Polynomial")


def _proper_divisors(d: int) -> Iterable[int]:
    return (e for e in range(1, d) if d % e == 0)


@functools.lru_cache(maxsize=None)
def cyclotomic_polynomial(d: int) -> Polynomial:
    """The d-th cyclotomic polynomial ``Phi_d(q)``.

    Computed via the standard recursive identity (CCA_01 Section 3.1)
    ``q**d - 1 = prod_{e | d} Phi_e(q)``, i.e.
    ``Phi_d(q) = (q**d - 1) / prod_{e | d, e < d} Phi_e(q)``, using exact
    monic polynomial division (:meth:`Polynomial.divmod_monic`) -- every
    ``Phi_e`` is monic, so this never leaves the integers. Memoized.
    """
    if d < 1:
        raise ValueError("d must be >= 1")
    numerator = Polynomial.monomial(d) - Polynomial.constant(1)
    denominator = Polynomial.constant(1)
    for e in _proper_divisors(d):
        denominator = denominator * cyclotomic_polynomial(e)
    quotient, remainder = numerator.divmod_monic(denominator)
    assert remainder.is_zero(), "q**d - 1 must be exactly divisible by its proper cyclotomic factors"
    return quotient


@functools.lru_cache(maxsize=None)
def qbinomial_small(n: int, k: int) -> Polynomial:
    """The Gaussian binomial coefficient ``C(n,k)_q`` as an exact
    ``Polynomial``, via the q-Pascal recurrence

        ``C(n,k)_q = C(n-1,k-1)_q + q**k * C(n-1,k)_q``

    (CCA_01 Section 5, used implicitly by Lemma 6.1's induction). Only
    polynomial addition and monomial shifts are used -- no division, so
    there is no risk of a division-algorithm bug here. Memoized; intended
    for *small* ``n`` (this module's only caller uses it with ``n < d``
    inside the q-Lucas fingerprint) -- it is not the non-expanding engine
    that :mod:`ccat.valuation`'s closed-form functions rely on for huge
    parameters.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if k < 0 or k > n:
        return Polynomial.zero()
    if k == 0 or k == n:
        return Polynomial.constant(1)
    return qbinomial_small(n - 1, k - 1) + qbinomial_small(n - 1, k).shift(k)


@dataclass(frozen=True)
class FactoredCyclotomicPolynomial:
    """``q**q_power * prod(Phi_d(q) for d in phi_indices)``, kept factored.

    ``phi_indices`` may contain repeats to express multiplicity greater
    than one, though the stable-range theorems implemented in
    :mod:`ccat.stable` always produce multiplicity exactly one (CCA_02
    Theorem 5.1's proof: "the terminal factors occur in the content
    exactly once").

    Equality compares ``q_power`` and the exact ``phi_indices`` tuple, not
    the abstract polynomial -- reordering the indices does not change the
    product mathematically, but this type does not canonicalize order.
    :mod:`ccat.stable` always builds ``phi_indices`` as a sorted
    ``range(...)``, so this is not a practical concern for that usage.

    This is deliberately *not* expanded by default: CCA_01 Section 4.1
    treats a compressed quotient "structurally; it need not be expanded",
    and CCA_06 Algorithms 4.1/4.2 return exactly this factored form.
    Expanding ``prod Phi_d(q)`` over a wide range of ``d`` has degree
    growing roughly quadratically in the range width and would defeat the
    purpose for large inputs.
    """

    q_power: int
    phi_indices: Tuple[int, ...]

    def expand(self) -> Polynomial:
        """Materialize the fully expanded :class:`Polynomial`.

        Opt-in and potentially expensive -- intended for inspecting or
        testing small instances, not for production use on large ones.
        """
        result = Polynomial.constant(1)
        for d in self.phi_indices:
            result = result * cyclotomic_polynomial(d)
        return result.shift(self.q_power)

    def __repr__(self) -> str:
        factors = " * ".join(f"Phi_{d}(q)" for d in self.phi_indices)
        if self.q_power and factors:
            return f"q^{self.q_power} * {factors}"
        if factors:
            return factors
        return f"q^{self.q_power}" if self.q_power else "1"
