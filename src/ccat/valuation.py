"""Non-expanding cyclotomic-valuation formulas (CCA_01, CCA_02 Section 3,
and the defect statement of CCA_03).

Every function here that is described as "closed-form" -- items 1, 2, 4, 8
below -- is computed directly from its compressed integer parameters via a
floor-sum or a single modular check, never by constructing or expanding a
``(q;q)_m``, a Gaussian binomial, or any other polynomial. Their cost and
correctness depend only on the bit length of the inputs, not on ``d`` or
the size of ``n``/``k``. The q-Lucas fingerprint (item 3) is the one
exception: it genuinely reduces a small polynomial modulo ``Phi_d(q)``,
but that polynomial has size bounded by ``d`` -- independent of how large
``n`` and ``k`` are, which is q-Lucas's entire point.

Out of scope for this module (left unimplemented, per CCA_03/04/05/06):
local residuals, Euler jets, cumulants, reciprocity/chirality, and
differential cyclic sieving.
"""

from __future__ import annotations

import math
from typing import Dict, Iterable, Sequence

from .exceptions import DegenerateCollisionError, InvalidParameterError, UnprovenRangeError
from .polynomials import Polynomial, cyclotomic_polynomial, qbinomial_small

__all__ = [
    "cyclotomic_valuation_q_factorial_quotient",
    "q_binomial_cyclotomic_valuation",
    "q_lucas_fingerprint",
    "contextual_collapse",
    "simple_collision_valuation",
    "q_multinomial_cyclotomic_valuation",
]


def _canonicalize(indices: Sequence[int], exponents: Sequence[int]) -> Dict[int, int]:
    """Merge equal indices (summing exponents) and drop zero-exponent
    entries -- the canonical representation of a compressed q-factorial
    quotient (CCA_06 Section 2.2 / Theorem 2.1)."""
    merged: Dict[int, int] = {}
    for a, e in zip(indices, exponents):
        merged[a] = merged.get(a, 0) + e
    return {a: e for a, e in merged.items() if e != 0}


def cyclotomic_valuation_q_factorial_quotient(
    indices: Sequence[int], exponents: Sequence[int], d: int
) -> int:
    """``v_Phi_d(F)`` for ``F(q) = q**alpha * prod_i (q;q)_{a_i}**{e_i}``.

    Theorem 4.2, CCA_01 ("Valuation of a compressed quotient")::

        v_Phi_d(F) = sum_i e_i * floor(a_i / d)

    Computed directly from ``(indices, exponents, d)`` via this floor-sum;
    ``(q;q)_m`` is never constructed or expanded. The ``q**alpha``
    prefactor contributes 0 to the valuation for every ``d >= 1`` (every
    cyclotomic polynomial has nonzero constant term, Theorem 4.2's proof),
    so ``alpha`` is not a parameter here.

    ``indices``/``exponents`` are canonicalized first (equal indices
    merged by summing exponents, zero-exponent entries dropped) -- this
    does not change the result, since the formula is linear in each
    index's exponent, but matches the theory's canonical representation
    of a compressed q-factorial quotient (CCA_06 Theorem 2.1).

    Supports arbitrarily large ``indices`` and ``d`` (hundreds/thousands
    of digits): cost is linear in the number of terms and polynomial in
    the bit length of the integers involved.
    """
    if d < 1:
        raise InvalidParameterError(f"d must be >= 1, got {d}")
    if len(indices) != len(exponents):
        raise InvalidParameterError(
            f"indices and exponents must have the same length "
            f"({len(indices)} != {len(exponents)})"
        )
    for a in indices:
        if not isinstance(a, int) or a < 0:
            raise InvalidParameterError(f"all indices must be nonnegative integers, got {a!r}")
    for e in exponents:
        if not isinstance(e, int):
            raise InvalidParameterError(f"all exponents must be integers, got {e!r}")

    canonical = _canonicalize(indices, exponents)
    return sum(e * (a // d) for a, e in canonical.items())


def q_binomial_cyclotomic_valuation(n: int, k: int, d: int) -> int:
    """``v_Phi_d(C(n,k)_q)``, the Gaussian binomial cyclotomic valuation.

    Theorem 5.1, CCA_01 (Gaussian valuation law), derived from Theorem 4.2
    by writing ``C(n,k)_q = (q;q)_n / ((q;q)_k * (q;q)_{n-k})``::

        v_Phi_d(C(n,k)_q) = floor(n/d) - floor(k/d) - floor((n-k)/d)

    which the theorem proves always lies in ``{0, 1}``.

    Implemented by delegating to
    :func:`cyclotomic_valuation_q_factorial_quotient`, mirroring the
    theorem's own derivation rather than duplicating the floor-sum.
    """
    if d < 1:
        raise InvalidParameterError(f"d must be >= 1, got {d}")
    if not (0 <= k <= n):
        raise InvalidParameterError(f"require 0 <= k <= n; got n={n}, k={k}")
    return cyclotomic_valuation_q_factorial_quotient([n, k, n - k], [1, -1, -1], d)


def q_lucas_fingerprint(n: int, k: int, d: int) -> Polynomial:
    """The q-Lucas contextual fingerprint ``Lambda_{n,d}(k)``: the residue
    of ``C(n,k)_q`` modulo ``Phi_d(q)``.

    Theorem 6.3, CCA_01 (q-Lucas congruence) + Definition 6.4: writing
    ``n = a*d + b``, ``k = r*d + s`` with ``0 <= b, s < d``::

        C(n,k)_q === C(a,r) * C(b,s)_q   (mod Phi_d(q))

    so ``Lambda_{n,d}(k) = C(a,r) * C(b,s)_q``, returned as its canonical
    representative of degree ``< deg(Phi_d) = phi(d)`` in
    ``Z[q]/(Phi_d(q))``.

    If ``s > b``, Corollary 6.6 gives ``C(b,s)_q = 0`` identically, so the
    fingerprint is the zero polynomial without constructing anything
    (this is also exactly the ``v_Phi_d(C(n,k)_q) == 1`` case, Corollary
    6.7). Otherwise the fingerprint is built from the *small* Gaussian
    binomial ``C(b,s)_q`` -- with ``b, s < d``, independent of how large
    ``n`` and ``k`` are -- reduced modulo ``Phi_d(q)``. This is q-Lucas's
    whole point: an in-principle-huge computation collapses to one
    bounded only by ``d``.
    """
    if d < 1:
        raise InvalidParameterError(f"d must be >= 1, got {d}")
    if not (0 <= k <= n):
        raise InvalidParameterError(f"require 0 <= k <= n; got n={n}, k={k}")

    a, b = divmod(n, d)
    r, s = divmod(k, d)
    if s > b:
        return Polynomial.zero()

    value = qbinomial_small(b, s) * math.comb(a, r)
    _, remainder = value.divmod_monic(cyclotomic_polynomial(d))
    return remainder


def contextual_collapse(n: int, index_set: Iterable[int], d: int) -> bool:
    """Whether ``Phi_d(q)`` divides
    ``Delta_K(q) = gcd_{i,j in K} (C(n,i)_q - C(n,j)_q)`` for the index
    set ``K``.

    Project Theorem 6.5, CCA_01 (arbitrary-subset contextual-collapse
    criterion)::

        Phi_d(q) | Delta_{n,K}(q)  <=>  Lambda_{n,d}(k) is constant on K

    Computed by comparing :func:`q_lucas_fingerprint` across every ``k``
    in ``K`` -- never by constructing ``Delta_K(q)`` or any full-size
    ``C(n,k)_q``. A set with fewer than two elements collapses trivially
    (Definition 2.1, CCA_01: the spacing of a one-member family is 0, and
    every polynomial divides 0).
    """
    if d < 1:
        raise InvalidParameterError(f"d must be >= 1, got {d}")
    indices = list(index_set)
    if not indices:
        raise InvalidParameterError("index_set must be nonempty")
    for k in indices:
        if not (0 <= k <= n):
            raise InvalidParameterError(
                f"every index must satisfy 0 <= k <= n; got k={k}, n={n}"
            )
    if len(indices) < 2:
        return True

    fingerprints = [q_lucas_fingerprint(n, k, d) for k in indices]
    first = fingerprints[0]
    return all(fp == first for fp in fingerprints[1:])


def simple_collision_valuation(d: int, M: int, i: int, j: int) -> int:
    """``v_Phi_d(C(n,i)_q - C(n,j)_q)`` for ``n = M*d - 1``,
    ``0 <= i < j <= d-1``.

    Project Theorem 3.4, CCA_02 (Simple-Collision Theorem): for
    ``M >= 2``::

        v_Phi_d(...) = 1  iff  2d | (i-j)(d-i-j-1),  else 0

    i.e. every nonzero collision in the first d-block is simple (order at
    most 1).

    Correction 3.5, CCA_02 handles ``M == 1`` (``n = d-1``) separately:
    ordinary Gaussian-binomial reflection symmetry
    ``C(d-1,i)_q = C(d-1,d-1-i)_q`` makes complementary pairs
    (``j == d-1-i``) *identical polynomials*, with no finite valuation --
    this raises :class:`~ccat.exceptions.DegenerateCollisionError` rather
    than returning 0 or 1. For ``M == 1`` non-complementary pairs,
    Theorem 3.4's own proof requires ``M >= 2`` (it uses
    ``Md-i-j-1 >= 2``), and Correction 3.5 states no separate formula for
    this case; rather than silently reusing the ``M >= 2`` criterion and
    hoping it extrapolates correctly, this raises
    :class:`~ccat.exceptions.UnprovenRangeError`.
    """
    if d < 2:
        raise InvalidParameterError(f"d must be >= 2, got {d}")
    if M < 1:
        raise InvalidParameterError(f"M must be >= 1, got {M}")
    if not (0 <= i < j <= d - 1):
        raise InvalidParameterError(f"require 0 <= i < j <= d-1; got i={i}, j={j}, d={d}")

    if M == 1:
        if j == d - 1 - i:
            raise DegenerateCollisionError(
                f"M=1: C({d - 1},{i})_q and C({d - 1},{j})_q are identical "
                f"polynomials by Gaussian-binomial reflection symmetry "
                f"(Correction 3.5, CCA_02); there is no finite valuation."
            )
        raise UnprovenRangeError(
            f"Theorem 3.4 (CCA_02) is proved only for M >= 2; M=1 with "
            f"non-complementary (i, j) = ({i}, {j}) is outside its proven "
            f"hypotheses, and no formula is claimed for it here."
        )

    residue = ((i - j) * (d - i - j - 1)) % (2 * d)
    return 1 if residue == 0 else 0


def q_multinomial_cyclotomic_valuation(parts: Sequence[int], d: int) -> int:
    """The residue defect ``h = v_Phi_d(M_k)`` of the Gaussian multinomial
    ``C(n; k_1,...,k_c)_q``, where ``n = sum(parts) = a*d``.

    Definition 2.1 + Project Theorem 3.1, CCA_03 (q-Multinomial Defect
    Theorem -- the valuation statement only; the local-residual and jet
    material later in CCA_03 is out of scope for this module)::

        k_nu = r_nu*d + s_nu,   0 <= s_nu < d
        h = a - sum(r_nu) = sum(s_nu) / d
        v_Phi_d(M_k) = h

    Requires ``n = sum(parts)`` to be an exact multiple of ``d`` -- the
    theorem's stated hypothesis (CCA_03 Section 2: "Fix ... d ... and
    suppose n = ad").
    """
    if d < 1:
        raise InvalidParameterError(f"d must be >= 1, got {d}")
    if not parts:
        raise InvalidParameterError("parts must be nonempty")
    for k in parts:
        if not isinstance(k, int) or k < 0:
            raise InvalidParameterError(f"all parts must be nonnegative integers, got {k!r}")

    n = sum(parts)
    if n % d != 0:
        raise InvalidParameterError(
            f"the Multinomial Defect Theorem requires d | sum(parts); "
            f"got sum(parts)={n}, d={d}"
        )
    a = n // d
    return a - sum(k // d for k in parts)
