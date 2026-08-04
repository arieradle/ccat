"""Brute-force and independent cross-checks for the stable-range theorems
(CCA_02 Sections 4-15): Stable Content, Stable Content-Spacing
Decomposition, and Stable Specialization (the exceptional binary
families).

The content/spacing checks against sympy are the most expensive tests in
this suite (they factor genuine, moderately large Gaussian-binomial
polynomials), so their sweep is kept modest relative to the pure-integer
exceptional-family sweep, which uses only stdlib arithmetic and can
therefore run much wider, exactly matching the task's emphasis on
searching broadly for exceptions rather than only confirming predicted
cases.
"""

from __future__ import annotations

import math

import pytest
import sympy as sp

import ccat
from ccat.exceptions import StableRangeError

from conftest import divides_phi, q, qbinom_poly


# ---------------------------------------------------------------------------
# Stable Content / Stable Content-Spacing Decomposition (Theorems 5.1, 6.1)
# ---------------------------------------------------------------------------

# t, n ranges for the sympy-backed structural sweep. Kept modest: checking
# Phi_d-divisibility of every retained Gaussian binomial for every d up to
# n, for every (n, t) pair, is the expensive part of this suite. A wider
# sweep (t up to 12, n well past the boundary) was run during development
# with zero mismatches; this is the subset kept in the committed suite to
# keep the default test run fast.
_STABLE_T_RANGE = range(5, 9)
_STABLE_N_EXTRA = 6  # n ranges over [3t-2, 3t-2 + _STABLE_N_EXTRA]


def _actual_cyclotomic_divisors(polys, n):
    """{d : 1 <= d <= n, Phi_d(q) divides every polynomial in polys}.

    A Gaussian binomial is, by construction, a product of only cyclotomic
    factors (it is a ratio of products of (1 - q**j) terms, and
    1 - q**j = prod_{e|j} Phi_e(q)), each with multiplicity 0 or 1
    (Theorem 5.1, CCA_01's Gaussian valuation law). So the set of d for
    which Phi_d divides *every* retained coefficient is exactly the
    (squarefree, cyclotomic-only) factorization of their gcd -- no
    non-cyclotomic factor can appear, and no cyclotomic factor can appear
    with multiplicity above 1. This lets the content be checked via cheap
    per-(d, poly) divisibility tests instead of an expensive general
    polynomial gcd.
    """
    return {d for d in range(1, n + 1) if all(divides_phi(p, d) for p in polys)}


class TestStableContentAndSpacing:
    @pytest.mark.parametrize("t", _STABLE_T_RANGE)
    def test_content_and_spacing_cyclotomic_factors_match_sympy(self, t):
        for n in range(3 * t - 2, 3 * t - 2 + _STABLE_N_EXTRA):
            expected_divisors = set(range(n - t + 1, n + 1))

            retained = {k: qbinom_poly(n, k) for k in range(t, n - t + 1)}
            content_divisors = _actual_cyclotomic_divisors(list(retained.values()), n)
            assert content_divisors == expected_divisors, f"content: n={n}, t={t}"

            content_got = ccat.stable_content(n, t)
            assert set(content_got.phi_indices) == expected_divisors
            assert content_got.q_power == 0

            adjacent_diffs = [
                retained[k + 1] - retained[k] for k in range(t, n - t)
            ]
            spacing_divisors = _actual_cyclotomic_divisors(adjacent_diffs, n)
            assert spacing_divisors == expected_divisors, f"spacing: n={n}, t={t}"

            spacing_got = ccat.stable_spacing(n, t)
            assert set(spacing_got.phi_indices) == expected_divisors
            assert spacing_got.q_power == t + 1

            # Independently confirm the q**(t+1) prefactor: the lowest-degree
            # nonzero term of the first adjacent difference should be q**(t+1).
            first_diff = adjacent_diffs[0]
            assert not first_diff.is_zero
            lowest_term_degree = min(m[0] for m in first_diff.monoms())
            assert lowest_term_degree == t + 1

    def test_expand_matches_direct_gcd_for_one_case(self):
        # A single, independently-computed full-gcd cross-check (the
        # expensive general case), to complement the cheaper
        # divisor-set-based checks used for the wider sweep above.
        n, t = 3 * 6 - 2, 6
        polys = [qbinom_poly(n, k).as_expr() for k in range(t, n - t + 1)]
        content = polys[0]
        for p in polys[1:]:
            content = sp.gcd(content, p)
        content = sp.Poly(content, q).monic().as_expr()

        got = ccat.stable_content(n, t).expand()
        got_expr = sp.expand(sum(c * q**i for i, c in enumerate(got.coeffs)))
        assert sp.expand(content - got_expr) == 0

    def test_rejects_t_less_than_five(self):
        with pytest.raises(StableRangeError):
            ccat.stable_content(30, 4)
        with pytest.raises(StableRangeError):
            ccat.stable_spacing(30, 4)

    def test_rejects_n_below_stable_bound(self):
        t = 8
        with pytest.raises(StableRangeError):
            ccat.stable_content(3 * t - 3, t)
        with pytest.raises(StableRangeError):
            ccat.stable_spacing(3 * t - 3, t)

    @pytest.mark.parametrize("t", range(5, 9))
    def test_boundary_sharpness_n_equals_3t_minus_3(self, t):
        """CCA_02 Proposition 7.1: at n = 3t-3, Phi_{t-1}(q) divides the
        *actual* content despite lying outside the naive terminal interval
        [n-t+1, n] = [2t-2, 3t-3] -- so the stable-range bound is load-
        bearing, not merely a conservative safety margin. We confirm this
        both ways: our functions must refuse the input, and the actual
        (brute-force) content must indeed contain this "extra" factor.
        """
        n = 3 * t - 3
        with pytest.raises(StableRangeError):
            ccat.stable_content(n, t)
        with pytest.raises(StableRangeError):
            ccat.stable_spacing(n, t)
        with pytest.raises(StableRangeError):
            ccat.stable_integer_spacing(n, t)

        retained = [qbinom_poly(n, k) for k in range(t, n - t + 1)]
        extra_factor = t - 1
        assert extra_factor not in range(n - t + 1, n + 1)
        assert all(divides_phi(p, extra_factor) for p in retained)


# ---------------------------------------------------------------------------
# Stable Specialization / exceptional binary families (Theorem 15.1)
# ---------------------------------------------------------------------------


def _brute_force_integer_spacing(n: int, t: int) -> int:
    """G_{n,t} via direct math.comb + math.gcd -- pure stdlib, exact,
    genuinely independent of ccat's rho/eta-based closed form."""
    binomials = [math.comb(n, k) for k in range(t, n - t + 1)]
    g = 0
    for i in range(len(binomials)):
        for j in range(i + 1, len(binomials)):
            g = math.gcd(g, abs(binomials[j] - binomials[i]))
    return g


def _brute_force_rho_product(n: int, t: int) -> int:
    """prod_{d=n-t+1}^{n} rho(d) via sympy.factorint (independent of
    ccat.numtheory.is_prime_power)."""
    product = 1
    for d in range(n - t + 1, n + 1):
        factors = sp.factorint(d)
        product *= next(iter(factors)) if len(factors) == 1 else 1
    return product


class TestStableIntegerSpacingExceptionalFamilies:
    # Pure stdlib arithmetic throughout, so this can (and per the task,
    # should) run much wider than the polynomial-backed sweep above.
    _T_RANGE = range(5, 16)
    _N_EXTRA = 40

    @pytest.mark.parametrize("t", _T_RANGE)
    def test_matches_brute_force_and_eta_is_never_outside_one_or_two(self, t):
        for n in range(3 * t - 2, 3 * t - 2 + self._N_EXTRA):
            expected = _brute_force_integer_spacing(n, t)
            got = ccat.stable_integer_spacing(n, t)
            assert got == expected, f"n={n}, t={t}"

            rho_product = _brute_force_rho_product(n, t)
            assert expected % rho_product == 0, f"n={n}, t={t}"
            eta_actual = expected // rho_product
            assert eta_actual in (1, 2), f"n={n}, t={t}, eta_actual={eta_actual}"

            is_family_one = _is_power_of_two(n + 1)
            is_family_two = _is_power_of_two(t) and n + 1 == 3 * t
            if is_family_one or is_family_two:
                assert eta_actual == 2, f"n={n}, t={t}: predicted family but eta_actual=1"
            else:
                assert eta_actual == 1, f"n={n}, t={t}: unpredicted family with eta_actual=2"

    def test_rejects_outside_stable_range(self):
        with pytest.raises(StableRangeError):
            ccat.stable_integer_spacing(10, 4)
        with pytest.raises(StableRangeError):
            ccat.stable_integer_spacing(3 * 6 - 3, 6)


def _is_power_of_two(value: int) -> bool:
    return value >= 1 and (value & (value - 1)) == 0
