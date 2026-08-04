"""Shared sympy-based independent oracle for cross-checking ccat's exact,
closed-form theory against direct polynomial/integer construction.

These helpers deliberately do NOT import or reuse any of ccat's own
machinery (Polynomial, cyclotomic_polynomial, qbinomial_small, ...) -- they
exist to catch bugs in that code, not to duplicate it. pytest adds this
file's directory to sys.path, so test modules import from it with
``from conftest import ...``.
"""

from __future__ import annotations

import functools
import time

import sympy as sp

q = sp.symbols("q")


# ---------------------------------------------------------------------------
# Direct polynomial construction (expression form, for smaller sweeps)
# ---------------------------------------------------------------------------


@functools.lru_cache(maxsize=None)
def qfactorial(m: int):
    """``(q;q)_m = prod_{j=1}^m (1 - q**j)``, expanded, as a sympy expr.

    Memoized: this is called repeatedly across sweeps with overlapping
    ``n``/``k``, and re-expanding it from scratch each time dominated
    runtime before this cache was added.
    """
    p = sp.Integer(1)
    for j in range(1, m + 1):
        p *= 1 - q**j
    return sp.expand(p)


@functools.lru_cache(maxsize=None)
def qbinom(n: int, k: int):
    """``C(n,k)_q`` via direct construction and exact polynomial division.

    Memoized for the same reason as :func:`qfactorial`.
    """
    if k < 0 or k > n:
        return sp.Integer(0)
    num = qfactorial(n)
    den = sp.expand(qfactorial(k) * qfactorial(n - k))
    quotient, remainder = sp.div(num, den, q)
    assert sp.expand(remainder) == 0
    return sp.expand(quotient)


@functools.lru_cache(maxsize=None)
def qmultinomial(parts):
    """``C(n; k_1,...,k_c)_q`` via direct construction and exact division.

    ``parts`` must be a hashable sequence (e.g. a tuple).
    """
    n = sum(parts)
    num = qfactorial(n)
    den = sp.Integer(1)
    for k in parts:
        den *= qfactorial(k)
    den = sp.expand(den)
    quotient, remainder = sp.div(num, den, q)
    assert sp.expand(remainder) == 0
    return sp.expand(quotient)


@functools.lru_cache(maxsize=None)
def cyclotomic_poly_expr(d: int):
    """``Phi_d(q)`` as a sympy expression. Memoized -- computing it fresh
    dominated runtime in sweeps that check many ``(n, k)`` against the
    same handful of ``d`` values."""
    return sp.cyclotomic_poly(d, q)


def phi_valuation(poly_expr, d: int) -> int:
    """``v_Phi_d`` of a sympy polynomial expression, by repeated exact
    division (independent of ccat's floor-sum formulas)."""
    phi = cyclotomic_poly_expr(d)
    v = 0
    p = poly_expr
    while True:
        quotient, remainder = sp.div(p, phi, q)
        if sp.expand(remainder) != 0:
            return v
        p = sp.expand(quotient)
        v += 1


def independent_quotient_valuation(indices, exponents, d: int) -> int:
    """``v_Phi_d`` of ``prod_i (q;q)_{a_i}**{e_i}`` via actually
    constructing numerator and denominator and factoring each by repeated
    division -- a genuinely different method from the floor-sum formula
    under test."""
    num = sp.Integer(1)
    den = sp.Integer(1)
    for a, e in zip(indices, exponents):
        if e > 0:
            num *= qfactorial(a) ** e
        elif e < 0:
            den *= qfactorial(a) ** (-e)
    return phi_valuation(sp.expand(num), d) - phi_valuation(sp.expand(den), d)


def ccat_polynomial_to_sympy(poly):
    """Convert a ``ccat.Polynomial`` to a sympy expression for comparison."""
    return sp.expand(sum(c * q**i for i, c in enumerate(poly.coeffs)))


# ---------------------------------------------------------------------------
# Poly-based construction (faster, used for the stable-range sweeps which
# otherwise spend most of their time re-parsing sympy expressions)
# ---------------------------------------------------------------------------


@functools.lru_cache(maxsize=None)
def qfactorial_poly(m: int):
    return sp.Poly(qfactorial(m), q, domain="ZZ")


@functools.lru_cache(maxsize=None)
def cyclotomic_poly_sympy(d: int):
    return sp.Poly(sp.cyclotomic_poly(d, q), q, domain="ZZ")


def qbinom_poly(n: int, k: int):
    if k < 0 or k > n:
        return sp.Poly(0, q, domain="ZZ")
    num = qfactorial_poly(n)
    den = qfactorial_poly(k) * qfactorial_poly(n - k)
    quotient, remainder = sp.div(num, den)
    assert remainder.is_zero
    return quotient


def divides_phi(poly, d: int) -> bool:
    _, remainder = sp.div(poly, cyclotomic_poly_sympy(d))
    return remainder.is_zero


# ---------------------------------------------------------------------------
# Misc test utilities
# ---------------------------------------------------------------------------


class Stopwatch:
    """``with Stopwatch() as sw: ...`` then assert ``sw.elapsed < limit``."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *exc_info):
        self.elapsed = time.perf_counter() - self.start
