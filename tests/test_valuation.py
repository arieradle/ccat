"""Brute-force and independent-formula cross-checks for the closed-form
valuation layer (CCA_01, CCA_02 Section 3, CCA_03's defect theorem).

Every non-huge-parameter check here constructs the actual polynomial via
sympy (never reusing ccat's own Polynomial/recurrence code) and compares.
The huge-parameter checks (functions 1, 2, 4, 8) instead compare against a
second, doc-grounded closed-form formula, since brute-force expansion is
infeasible at that scale (see module docstrings in conftest.py and below
for which alternate formula is used for each).
"""

from __future__ import annotations

import random

import pytest
import sympy as sp

import ccat
from ccat.exceptions import DegenerateCollisionError, InvalidParameterError, UnprovenRangeError

from conftest import (
    Stopwatch,
    ccat_polynomial_to_sympy,
    cyclotomic_poly_expr,
    independent_quotient_valuation,
    phi_valuation,
    q,
    qbinom,
    qfactorial,
    qmultinomial,
)

HUGE_TIME_LIMIT_SECONDS = 0.5


def _random_huge(rng: random.Random, min_digits: int = 300, max_digits: int = 1200) -> int:
    bits = rng.randint(int(min_digits * 3.32), int(max_digits * 3.32))
    return rng.getrandbits(bits) | 1  # ensure nonzero


# ---------------------------------------------------------------------------
# 1. cyclotomic_valuation_q_factorial_quotient
# ---------------------------------------------------------------------------


class TestQFactorialQuotientValuation:
    @pytest.mark.parametrize("d", range(1, 12))
    def test_single_factorial_matches_sympy(self, d):
        for m in range(0, 16):
            expected = phi_valuation(qfactorial(m), d)
            got = ccat.cyclotomic_valuation_q_factorial_quotient([m], [1], d)
            assert got == expected, f"m={m}, d={d}"

    @pytest.mark.parametrize("seed", range(15))
    def test_compound_quotient_matches_independent_construction(self, seed):
        rng = random.Random(seed)
        indices = [rng.randint(0, 10) for _ in range(rng.randint(1, 4))]
        exponents = [rng.choice([-2, -1, 1, 2]) for _ in indices]
        d = rng.randint(1, 8)
        expected = independent_quotient_valuation(indices, exponents, d)
        got = ccat.cyclotomic_valuation_q_factorial_quotient(indices, exponents, d)
        assert got == expected, f"indices={indices}, exponents={exponents}, d={d}"

    def test_canonicalization_does_not_change_result(self):
        # [5, 5, 3] with exponents [1, 1, -1] should equal [5, 3] with [2, -1].
        a = ccat.cyclotomic_valuation_q_factorial_quotient([5, 5, 3], [1, 1, -1], 2)
        b = ccat.cyclotomic_valuation_q_factorial_quotient([5, 3], [2, -1], 2)
        assert a == b

    def test_zero_exponent_entries_are_inert(self):
        a = ccat.cyclotomic_valuation_q_factorial_quotient([7], [1], 3)
        b = ccat.cyclotomic_valuation_q_factorial_quotient([7, 100], [1, 0], 3)
        assert a == b

    def test_d_equals_one_is_supported(self):
        # v_Phi_1((q;q)_m) = m, matching the general floor formula.
        assert ccat.cyclotomic_valuation_q_factorial_quotient([7], [1], 1) == 7

    def test_rejects_d_less_than_one(self):
        with pytest.raises(InvalidParameterError):
            ccat.cyclotomic_valuation_q_factorial_quotient([1], [1], 0)

    def test_rejects_mismatched_lengths(self):
        with pytest.raises(InvalidParameterError):
            ccat.cyclotomic_valuation_q_factorial_quotient([1, 2], [1], 2)

    def test_rejects_negative_index(self):
        with pytest.raises(InvalidParameterError):
            ccat.cyclotomic_valuation_q_factorial_quotient([-1], [1], 2)

    @pytest.mark.parametrize("seed", range(10))
    def test_huge_parameters_match_independent_formula_and_are_fast(self, seed):
        rng = random.Random(10_000 + seed)
        n_terms = rng.randint(1, 5)
        indices = [_random_huge(rng) for _ in range(n_terms)]
        exponents = [rng.choice([-3, -2, -1, 1, 2, 3]) for _ in indices]
        d = rng.randint(1, 10_000)

        # Independent code path: divmod() instead of //.
        def alt_valuation(indices, exponents, d):
            total = 0
            for a, e in zip(indices, exponents):
                quotient, _ = divmod(a, d)
                total += e * quotient
            return total

        expected = alt_valuation(indices, exponents, d)
        with Stopwatch() as sw:
            got = ccat.cyclotomic_valuation_q_factorial_quotient(indices, exponents, d)
        assert got == expected
        assert sw.elapsed < HUGE_TIME_LIMIT_SECONDS


# ---------------------------------------------------------------------------
# 2. q_binomial_cyclotomic_valuation
# ---------------------------------------------------------------------------


class TestQBinomialValuation:
    @pytest.mark.parametrize("n", range(0, 22))
    def test_matches_sympy(self, n):
        for k in range(0, n + 1):
            for d in range(1, 13):
                expected = phi_valuation(qbinom(n, k), d)
                got = ccat.q_binomial_cyclotomic_valuation(n, k, d)
                assert got == expected, f"n={n}, k={k}, d={d}"
                assert got in (0, 1)

    def test_rejects_d_less_than_one(self):
        with pytest.raises(InvalidParameterError):
            ccat.q_binomial_cyclotomic_valuation(5, 2, 0)

    @pytest.mark.parametrize("k", [-1, 11])
    def test_rejects_k_out_of_range(self, k):
        with pytest.raises(InvalidParameterError):
            ccat.q_binomial_cyclotomic_valuation(10, k, 3)

    @pytest.mark.parametrize("seed", range(10))
    def test_huge_parameters_match_q_lucas_carry_criterion_and_are_fast(self, seed):
        rng = random.Random(20_000 + seed)
        d = rng.randint(1, 10_000)
        n = _random_huge(rng)
        k = rng.randint(0, n)

        # Independent code path: Corollary 5.2's carry criterion
        # (valuation is 1 iff the least base-d digit of k exceeds that of
        # n), instead of the floor-difference formula.
        b = n % d
        s = k % d
        expected = 1 if s > b else 0

        with Stopwatch() as sw:
            got = ccat.q_binomial_cyclotomic_valuation(n, k, d)
        assert got == expected
        assert sw.elapsed < HUGE_TIME_LIMIT_SECONDS


# ---------------------------------------------------------------------------
# 3. q_lucas_fingerprint / contextual_collapse
# ---------------------------------------------------------------------------


def _sympy_fingerprint(n: int, k: int, d: int):
    """C(n,k)_q mod Phi_d(q), via direct construction (independent of
    ccat's q-Lucas machinery -- this uses the *original*, potentially
    large, n and k directly rather than the reduced a,r,b,s)."""
    _, remainder = sp.div(qbinom(n, k), cyclotomic_poly_expr(d), q)
    return sp.expand(remainder)


class TestQLucasFingerprint:
    @pytest.mark.parametrize("n", range(0, 16))
    def test_matches_direct_sympy_reduction(self, n):
        for k in range(0, n + 1):
            for d in range(1, 9):
                expected = _sympy_fingerprint(n, k, d)
                got = ccat.q_lucas_fingerprint(n, k, d)
                assert ccat_polynomial_to_sympy(got) == expected, f"n={n}, k={k}, d={d}"

    def test_zero_fingerprint_iff_valuation_one(self):
        # Corollary 6.7, CCA_01.
        for n in range(0, 16):
            for k in range(0, n + 1):
                for d in range(1, 9):
                    fingerprint = ccat.q_lucas_fingerprint(n, k, d)
                    valuation = ccat.q_binomial_cyclotomic_valuation(n, k, d)
                    assert fingerprint.is_zero() == (valuation == 1)

    def test_rejects_d_less_than_one(self):
        with pytest.raises(InvalidParameterError):
            ccat.q_lucas_fingerprint(5, 2, 0)

    def test_rejects_k_out_of_range(self):
        with pytest.raises(InvalidParameterError):
            ccat.q_lucas_fingerprint(5, 6, 3)


class TestContextualCollapse:
    @pytest.mark.parametrize("seed", range(30))
    def test_matches_direct_pairwise_congruence(self, seed):
        rng = random.Random(30_000 + seed)
        n = rng.randint(2, 18)
        d = rng.randint(1, 8)
        size = rng.randint(2, min(4, n + 1))
        index_set = rng.sample(range(0, n + 1), size)

        phi = cyclotomic_poly_expr(d)
        polys = [qbinom(n, k) for k in index_set]
        remainders = []
        for p in polys:
            _, rem = sp.div(p, phi, q)
            remainders.append(sp.expand(rem))
        expected = all(r == remainders[0] for r in remainders[1:])

        got = ccat.contextual_collapse(n, index_set, d)
        assert got == expected, f"n={n}, index_set={index_set}, d={d}"

    def test_singleton_is_trivially_true(self):
        assert ccat.contextual_collapse(10, [3], 4) is True

    def test_rejects_empty_index_set(self):
        with pytest.raises(InvalidParameterError):
            ccat.contextual_collapse(10, [], 3)

    def test_rejects_out_of_range_index(self):
        with pytest.raises(InvalidParameterError):
            ccat.contextual_collapse(10, [3, 11], 3)


# ---------------------------------------------------------------------------
# 4. simple_collision_valuation
# ---------------------------------------------------------------------------


class TestSimpleCollisionValuation:
    # d up to 9, M up to 4 (n = M*d-1 up to 35): checking every (i, j) pair
    # means this cost grows like d**2 per d, so it is kept modest -- each
    # check constructs and subtracts two genuine Gaussian binomials and
    # divides by Phi_d(q), unlike the O(1) closed-form check under test.
    @pytest.mark.parametrize("d", range(2, 10))
    def test_matches_sympy_for_m_at_least_two(self, d):
        for M in range(2, 5):
            n = M * d - 1
            for i in range(0, d):
                for j in range(i + 1, d):
                    expected = phi_valuation(sp.expand(qbinom(n, i) - qbinom(n, j)), d)
                    assert expected in (0, 1)
                    got = ccat.simple_collision_valuation(d, M, i, j)
                    assert got == expected, f"d={d}, M={M}, i={i}, j={j}"

    @pytest.mark.parametrize("d", range(2, 8))
    def test_m_equals_one_complementary_pairs_are_identical_polynomials(self, d):
        n = d - 1
        for i in range(0, d):
            j = d - 1 - i
            if j <= i:
                continue
            # Confirm the doc's claim independently: the two Gaussian
            # binomials really are equal as polynomials.
            assert sp.expand(qbinom(n, i) - qbinom(n, j)) == 0
            with pytest.raises(DegenerateCollisionError):
                ccat.simple_collision_valuation(d, 1, i, j)

    @pytest.mark.parametrize("d", range(3, 8))
    def test_m_equals_one_non_complementary_pairs_are_unproven(self, d):
        n = d - 1
        found_noncomplementary = False
        for i in range(0, d):
            for j in range(i + 1, d):
                if j == d - 1 - i:
                    continue
                found_noncomplementary = True
                with pytest.raises(UnprovenRangeError):
                    ccat.simple_collision_valuation(d, 1, i, j)
        assert found_noncomplementary

    def test_rejects_d_less_than_two(self):
        with pytest.raises(InvalidParameterError):
            ccat.simple_collision_valuation(1, 2, 0, 0)

    def test_rejects_m_less_than_one(self):
        with pytest.raises(InvalidParameterError):
            ccat.simple_collision_valuation(4, 0, 0, 1)

    @pytest.mark.parametrize("i,j,d", [(1, 0, 4), (0, 0, 4), (0, 5, 4)])
    def test_rejects_invalid_index_ordering(self, i, j, d):
        with pytest.raises(InvalidParameterError):
            ccat.simple_collision_valuation(d, 2, i, j)

    @pytest.mark.parametrize("seed", range(10))
    def test_huge_parameters_match_alternate_modular_formula_and_are_fast(self, seed):
        rng = random.Random(40_000 + seed)
        d = _random_huge(rng, min_digits=300, max_digits=800)
        M = rng.randint(2, 10)
        i = rng.randrange(0, d)
        j = rng.randrange(0, d)
        if i == j:
            j = (j + 1) % d
        i, j = min(i, j), max(i, j)

        # Independent code path: reduce each factor modulo 2d separately
        # before multiplying, instead of multiplying then reducing.
        two_d = 2 * d
        factor1 = (i - j) % two_d
        factor2 = (d - i - j - 1) % two_d
        expected = 1 if (factor1 * factor2) % two_d == 0 else 0

        with Stopwatch() as sw:
            got = ccat.simple_collision_valuation(d, M, i, j)
        assert got == expected
        assert sw.elapsed < HUGE_TIME_LIMIT_SECONDS


# ---------------------------------------------------------------------------
# 8. q_multinomial_cyclotomic_valuation
# ---------------------------------------------------------------------------


PART_TUPLES = [
    (2, 2, 2),
    (4, 4, 4),
    (3, 3, 3, 3),
    (6, 3, 3),
    (2, 4, 6),
    (5, 5, 5, 5, 5),
    (1, 2, 3),
    (0, 4, 4),
    (7, 1),
]


class TestQMultinomialValuation:
    @pytest.mark.parametrize("parts", PART_TUPLES)
    def test_matches_sympy(self, parts):
        n = sum(parts)
        for d in range(2, 9):
            if n % d != 0:
                continue
            expected = phi_valuation(qmultinomial(parts), d)
            got = ccat.q_multinomial_cyclotomic_valuation(list(parts), d)
            assert got == expected, f"parts={parts}, d={d}"

    def test_d_equals_one_is_always_zero(self):
        # Every part is trivially "divisible by 1", so the defect is 0
        # (consistent with Phi_1(1) != 0 for the ordinary multinomial
        # coefficient evaluated at q=1).
        assert ccat.q_multinomial_cyclotomic_valuation([3, 4, 5], 1) == 0

    def test_rejects_non_dividing_d(self):
        # sum([3, 4, 5]) == 12, and 5 does not divide 12.
        with pytest.raises(InvalidParameterError):
            ccat.q_multinomial_cyclotomic_valuation([3, 4, 5], 5)

    def test_rejects_empty_parts(self):
        with pytest.raises(InvalidParameterError):
            ccat.q_multinomial_cyclotomic_valuation([], 2)

    def test_rejects_negative_part(self):
        with pytest.raises(InvalidParameterError):
            ccat.q_multinomial_cyclotomic_valuation([3, -1, 4], 2)

    @pytest.mark.parametrize("seed", range(10))
    def test_huge_parameters_match_alternate_residue_formula_and_are_fast(self, seed):
        rng = random.Random(50_000 + seed)
        d = rng.randint(2, 10_000)
        c = rng.randint(1, 6)

        # Build parts = r_nu*d + s_nu directly, with huge r_nu (so parts
        # themselves have hundreds-to-thousands of digits) and s_nu forced
        # to sum to a multiple of d, so sum(parts) is exactly divisible
        # by d as the theorem requires.
        r = [_random_huge(rng) for _ in range(c)]
        s = [rng.randrange(0, d) for _ in range(c - 1)]
        s.append((-sum(s)) % d)
        parts = [ri * d + si for ri, si in zip(r, s)]

        # Independent code path: h = sum(s_nu) // d (CCA_03 Software
        # Corollary 3.3's stated equivalent form) instead of a - sum(r_nu).
        expected = sum(k % d for k in parts) // d

        with Stopwatch() as sw:
            got = ccat.q_multinomial_cyclotomic_valuation(parts, d)
        assert got == expected
        assert sw.elapsed < HUGE_TIME_LIMIT_SECONDS
