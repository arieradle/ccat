"""Stable-range Gaussian-binomial content, spacing, and integer
specialization theorems (CCA_02 Sections 4-15).

These are proved only for ``t >= 5, n >= 3t - 2`` ("the stable range").
CCA_02 Proposition 7.1 shows this bound is sharp -- at ``n = 3t - 3`` an
extra, unpredicted cyclotomic factor (``Phi_{t-1}``) already divides the
actual content -- so every function here raises
:class:`~ccat.exceptions.StableRangeError` rather than silently
extrapolating outside the proved range.
"""

from __future__ import annotations

from .exceptions import StableRangeError
from .numtheory import is_prime_power
from .polynomials import FactoredCyclotomicPolynomial

__all__ = ["stable_content", "stable_spacing", "stable_integer_spacing"]


def _validate_stable_range(n: int, t: int) -> None:
    if t < 5:
        raise StableRangeError(f"the stable-range theorems require t >= 5; got t={t}")
    if n < 3 * t - 2:
        raise StableRangeError(
            f"the stable-range theorems require n >= 3t - 2; got n={n}, t={t} "
            f"(3t - 2 = {3 * t - 2})"
        )


def stable_content(n: int, t: int) -> FactoredCyclotomicPolynomial:
    """The polynomial content ``C_{n,t}(q) = gcd_{t<=k<=n-t} C(n,k)_q`` of
    the central Gaussian-binomial block.

    Project Theorem 5.1, CCA_02 (Stable Content Theorem), for
    ``t >= 5, n >= 3t - 2``::

        C_{n,t}(q) = prod_{d=n-t+1}^{n} Phi_d(q)

    Returned as a factored, non-expanding
    :class:`~ccat.polynomials.FactoredCyclotomicPolynomial` (CCA_06
    Algorithm 4.1); call ``.expand()`` for the materialized polynomial.
    """
    _validate_stable_range(n, t)
    return FactoredCyclotomicPolynomial(0, tuple(range(n - t + 1, n + 1)))


def stable_spacing(n: int, t: int) -> FactoredCyclotomicPolynomial:
    """The polynomial spacing
    ``Delta_{n,t}(q) = gcd_{t<=i<j<=n-t} (C(n,j)_q - C(n,i)_q)`` of the
    central Gaussian-binomial block.

    Project Theorem 6.1, CCA_02 (Stable Content-Spacing Decomposition
    Theorem), for ``t >= 5, n >= 3t - 2``::

        Delta_{n,t}(q) = q**(t+1) * C_{n,t}(q)
                       = q**(t+1) * prod_{d=n-t+1}^{n} Phi_d(q)

    Returned as a factored, non-expanding
    :class:`~ccat.polynomials.FactoredCyclotomicPolynomial` (CCA_06
    Algorithm 4.2); call ``.expand()`` for the materialized polynomial.
    """
    _validate_stable_range(n, t)
    return FactoredCyclotomicPolynomial(t + 1, tuple(range(n - t + 1, n + 1)))


def _rho(m: int) -> int:
    """``rho(m) = p`` if ``m = p**a`` for a prime ``p``, integer ``a>=1``;
    otherwise ``1``.

    Classical Lemma 8.1, CCA_02: ``Phi_m(1) = rho(m)`` for ``m > 1``.
    """
    base = is_prime_power(m)
    return base if base is not None else 1


def _is_power_of_two(value: int) -> bool:
    return value >= 1 and (value & (value - 1)) == 0


def stable_integer_spacing(n: int, t: int) -> int:
    """The integer spacing
    ``G_{n,t} = gcd_{t<=i<j<=n-t} |C(n,j) - C(n,i)|`` of the central
    binomial-coefficient block (the ``q=1`` specialization of
    :func:`stable_spacing`, up to the exceptional factor below).

    Project Theorem 9.1 (Stable Integer Content Theorem: the companion
    result ``H_{n,t} = gcd_{t<=k<=n-t} C(n,k) = prod_{d=n-t+1}^{n}
    rho(d)``) + Project Theorem 13.1 (Binary Exceptional-Family
    Classification) + Project Theorem 15.1 (Stable Specialization
    Theorem), CCA_02, for ``t >= 5, n >= 3t - 2``::

        G_{n,t} = eta(n,t) * prod_{d=n-t+1}^{n} rho(d)

        eta(n,t) = 2  if n = 2**s - 1
                 = 2  if n = 3*2**s - 1 and t = 2**s
                 = 1  otherwise

    -- exactly these two families (Theorem 15.1's proof shows no odd
    prime, and never a factor of 4, can divide the specialization gap
    ``G_{n,t} / H_{n,t}``). ``rho`` is computed via
    :func:`ccat.numtheory.is_prime_power`, so no large ``d`` in the
    terminal interval is ever fully factored.
    """
    _validate_stable_range(n, t)

    product = 1
    for d in range(n - t + 1, n + 1):
        product *= _rho(d)

    if _is_power_of_two(n + 1):
        eta = 2
    elif _is_power_of_two(t) and n + 1 == 3 * t:
        eta = 2
    else:
        eta = 1

    return eta * product
