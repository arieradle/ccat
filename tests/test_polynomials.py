"""Unit tests for ccat.polynomials and ccat.numtheory: the small pieces of
machinery the closed-form valuation formulas build on (q-Lucas reduction,
stable-content factoring, and rho(m)). Cross-checked against sympy where a
genuine independent oracle is available.
"""

from __future__ import annotations

import random

import pytest
import sympy as sp

from ccat.numtheory import integer_nth_root, is_prime, is_prime_power
from ccat.polynomials import (
    FactoredCyclotomicPolynomial,
    Polynomial,
    cyclotomic_polynomial,
    qbinomial_small,
)

from conftest import ccat_polynomial_to_sympy, q, qbinom


# ---------------------------------------------------------------------------
# Polynomial
# ---------------------------------------------------------------------------


class TestPolynomial:
    def test_zero_and_constant(self):
        assert Polynomial.zero().is_zero()
        assert Polynomial.zero().degree == -1
        assert Polynomial.constant(5).coeffs == (5,)
        assert Polynomial.constant(0).is_zero()

    def test_trailing_zeros_are_stripped(self):
        assert Polynomial((1, 2, 0, 0)).coeffs == (1, 2)
        assert Polynomial((0, 0, 0)).coeffs == ()

    def test_monomial(self):
        assert Polynomial.monomial(3).coeffs == (0, 0, 0, 1)
        assert Polynomial.monomial(3, coeff=5).coeffs == (0, 0, 0, 5)
        assert Polynomial.monomial(0).coeffs == (1,)

    def test_add_sub(self):
        p = Polynomial((1, 2, 3))  # 1 + 2q + 3q^2
        r = Polynomial((1, -1))  # 1 - q
        assert (p + r).coeffs == (2, 1, 3)
        assert (p - r).coeffs == (0, 3, 3)
        assert (r - p).coeffs == (0, -3, -3)

    def test_mul(self):
        p = Polynomial((1, 2, 3))
        r = Polynomial((1, -1))
        # (1+2q+3q^2)(1-q) = 1 + q + q^2 - 3q^3
        assert (p * r).coeffs == (1, 1, 1, -3)
        assert (p * Polynomial.zero()).is_zero()

    def test_scalar_mul(self):
        p = Polynomial((1, 2))
        assert (p * 3).coeffs == (3, 6)
        assert (3 * p).coeffs == (3, 6)

    def test_shift(self):
        p = Polynomial((1, 2))
        assert p.shift(2).coeffs == (0, 0, 1, 2)
        assert p.shift(0) == p
        assert Polynomial.zero().shift(5).is_zero()
        with pytest.raises(ValueError):
            p.shift(-1)

    def test_equality_with_int(self):
        assert Polynomial.constant(5) == 5
        assert Polynomial.zero() == 0
        assert Polynomial((1, 1)) != 5

    def test_hashable(self):
        assert hash(Polynomial((1, 2))) == hash(Polynomial((1, 2)))
        assert len({Polynomial((1, 2)), Polynomial((1, 2)), Polynomial((3,))}) == 2

    def test_divmod_monic_exact(self):
        # (q^2 - 1) / (q - 1) = q + 1
        numerator = Polynomial((-1, 0, 1))
        divisor = Polynomial((-1, 1))
        quotient, remainder = numerator.divmod_monic(divisor)
        assert quotient.coeffs == (1, 1)
        assert remainder.is_zero()

    @pytest.mark.parametrize("seed", range(20))
    def test_divmod_monic_round_trips(self, seed):
        rng = random.Random(seed)
        numerator = Polynomial([rng.randint(-20, 20) for _ in range(rng.randint(0, 12))])
        divisor_degree = rng.randint(0, 6)
        divisor = Polynomial(
            [rng.randint(-20, 20) for _ in range(divisor_degree)] + [1]
        )
        quotient, remainder = numerator.divmod_monic(divisor)
        assert quotient * divisor + remainder == numerator
        assert remainder.is_zero() or remainder.degree < divisor.degree

    def test_divmod_monic_requires_monic(self):
        with pytest.raises(ValueError):
            Polynomial((1, 1)).divmod_monic(Polynomial((0, 2)))

    def test_divmod_monic_zero_divisor(self):
        with pytest.raises(ZeroDivisionError):
            Polynomial((1,)).divmod_monic(Polynomial.zero())

    def test_repr_is_stable(self):
        assert repr(Polynomial((1, 2))) == "Polynomial((1, 2))"


# ---------------------------------------------------------------------------
# cyclotomic_polynomial
# ---------------------------------------------------------------------------


class TestCyclotomicPolynomial:
    @pytest.mark.parametrize("d", range(1, 51))
    def test_matches_sympy(self, d):
        got = cyclotomic_polynomial(d)
        expected_poly = sp.Poly(sp.cyclotomic_poly(d, q), q)
        expected_coeffs = tuple(int(c) for c in reversed(expected_poly.all_coeffs()))
        assert got.coeffs == expected_coeffs

    def test_is_monic(self):
        for d in range(1, 30):
            assert cyclotomic_polynomial(d).is_monic()

    def test_rejects_d_less_than_one(self):
        with pytest.raises(ValueError):
            cyclotomic_polynomial(0)


# ---------------------------------------------------------------------------
# qbinomial_small
# ---------------------------------------------------------------------------


class TestQBinomialSmall:
    @pytest.mark.parametrize("n", range(0, 13))
    def test_matches_sympy(self, n):
        for k in range(0, n + 1):
            got = qbinomial_small(n, k)
            expected = sp.expand(qbinom(n, k))
            assert ccat_polynomial_to_sympy(got) == expected

    def test_out_of_range_is_zero(self):
        assert qbinomial_small(5, -1).is_zero()
        assert qbinomial_small(5, 6).is_zero()

    def test_rejects_negative_n(self):
        with pytest.raises(ValueError):
            qbinomial_small(-1, 0)


# ---------------------------------------------------------------------------
# FactoredCyclotomicPolynomial
# ---------------------------------------------------------------------------


class TestFactoredCyclotomicPolynomial:
    def test_expand_matches_manual_product(self):
        factored = FactoredCyclotomicPolynomial(2, (3, 4, 5))
        expected = (
            cyclotomic_polynomial(3) * cyclotomic_polynomial(4) * cyclotomic_polynomial(5)
        ).shift(2)
        assert factored.expand() == expected

    def test_expand_matches_sympy(self):
        factored = FactoredCyclotomicPolynomial(3, (6, 7))
        expected = sp.expand(
            q**3 * sp.cyclotomic_poly(6, q) * sp.cyclotomic_poly(7, q)
        )
        assert ccat_polynomial_to_sympy(factored.expand()) == expected

    def test_repr_is_readable(self):
        assert repr(FactoredCyclotomicPolynomial(0, (3,))) == "Phi_3(q)"
        assert repr(FactoredCyclotomicPolynomial(2, (3, 4))) == "q^2 * Phi_3(q) * Phi_4(q)"
        assert repr(FactoredCyclotomicPolynomial(5, ())) == "q^5"
        assert repr(FactoredCyclotomicPolynomial(0, ())) == "1"

    def test_equality(self):
        a = FactoredCyclotomicPolynomial(1, (2, 3))
        b = FactoredCyclotomicPolynomial(1, (2, 3))
        c = FactoredCyclotomicPolynomial(1, (2, 4))
        assert a == b
        assert a != c


# ---------------------------------------------------------------------------
# numtheory
# ---------------------------------------------------------------------------


class TestIntegerNthRoot:
    @pytest.mark.parametrize("seed", range(40))
    def test_matches_definition(self, seed):
        rng = random.Random(seed)
        m = rng.randrange(0, 10**6)
        a = rng.randrange(1, 8)
        root = integer_nth_root(m, a)
        assert root**a <= m < (root + 1) ** a

    def test_exact_powers(self):
        for base in range(2, 25):
            for a in range(1, 6):
                assert integer_nth_root(base**a, a) == base

    def test_zero(self):
        assert integer_nth_root(0, 5) == 0

    def test_rejects_bad_args(self):
        with pytest.raises(ValueError):
            integer_nth_root(5, 0)
        with pytest.raises(ValueError):
            integer_nth_root(-1, 2)


class TestIsPrime:
    def test_small_values(self):
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
        for n in range(0, 30):
            assert is_prime(n) == (n in primes)

    @pytest.mark.parametrize("seed", range(30))
    def test_matches_sympy(self, seed):
        rng = random.Random(1000 + seed)
        n = rng.randrange(2, 10**6)
        assert is_prime(n) == bool(sp.isprime(n))

    def test_large_known_prime(self):
        assert is_prime(2**127 - 1)  # Mersenne prime

    def test_large_known_composite(self):
        assert not is_prime(2**128)


class TestIsPrimePower:
    @pytest.mark.parametrize("seed", range(40))
    def test_matches_sympy_factorint(self, seed):
        rng = random.Random(2000 + seed)
        m = rng.randrange(2, 10**5)
        got = is_prime_power(m)
        factors = sp.factorint(m)
        expected = next(iter(factors)) if len(factors) == 1 else None
        assert got == expected

    def test_one_is_not_a_prime_power(self):
        assert is_prime_power(1) is None
        assert is_prime_power(0) is None

    def test_prime_powers(self):
        assert is_prime_power(3**200) == 3
        assert is_prime_power(2**1) == 2
        assert is_prime_power(101) == 101

    def test_non_prime_powers(self):
        assert is_prime_power(6) is None
        assert is_prime_power(12) is None
