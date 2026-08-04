"""Number-theoretic helpers backing ``rho(m)`` (Classical Lemma 8.1, CCA_02),
used by :mod:`ccat.stable`.

Stdlib only. ``is_prime_power`` never factors its input -- it finds a prime
base (if one exists) via exact integer nth-roots plus a primality test, in
time polynomial in the bit length of the input.
"""

from __future__ import annotations

import math
import random

_SMALL_PRIMES = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
    149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
)

# Fixed witness set proven deterministic for every n below this bound (a
# well-known strengthening of Miller-Rabin -- see e.g. Sorenson & Webster,
# "Strong Pseudoprimes to Twelve Prime Bases", 2015).
_DETERMINISTIC_BOUND = 3_317_044_064_679_887_385_961_981
_DETERMINISTIC_WITNESSES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
_PROBABILISTIC_ROUNDS = 40


def integer_nth_root(m: int, a: int) -> int:
    """Exact floor of the integer ``a``-th root of ``m``.

    Satisfies ``integer_nth_root(m, a) ** a <= m < (integer_nth_root(m, a)
    + 1) ** a``. Computed by exact-integer binary search -- no floating
    point anywhere.
    """
    if a < 1:
        raise ValueError("a must be >= 1")
    if m < 0:
        raise ValueError("m must be >= 0")
    if m == 0:
        return 0
    if a == 1:
        return m
    if a == 2:
        return math.isqrt(m)

    high = 1
    while high**a <= m:
        high <<= 1
    low = high >> 1
    while low < high:
        mid = (low + high + 1) // 2
        if mid**a <= m:
            low = mid
        else:
            high = mid - 1
    return low


def is_prime(n: int) -> bool:
    """Primality test.

    Deterministic for every ``n < 3_317_044_064_679_887_385_961_981``
    (~3.3e24) via a proven-sufficient fixed Miller-Rabin witness set. Above
    that bound it falls back to 40 independent random-witness Miller-Rabin
    rounds -- the standard practice used by essentially every real system,
    since no primality test that is both polynomial-time and practical is
    known to be unconditionally deterministic at arbitrary scale. This is
    the one place in :mod:`ccat` where "exact" is honestly a documented
    probabilistic-but-effectively-certain guarantee rather than a proof.
    """
    if n < 2:
        return False
    for p in _SMALL_PRIMES:
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    def is_witness_composite(a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    if n < _DETERMINISTIC_BOUND:
        witnesses = [a for a in _DETERMINISTIC_WITNESSES if a < n]
    else:
        witnesses = [random.randrange(2, n - 1) for _ in range(_PROBABILISTIC_ROUNDS)]

    return not any(is_witness_composite(a) for a in witnesses)


def is_prime_power(m: int):
    """If ``m == p ** a`` for a prime ``p`` and integer ``a >= 1``, return
    ``p``; otherwise return ``None``.

    Never factors ``m``: tries each candidate exponent ``a`` from 1 up to
    ``m.bit_length()``, computes the exact integer ``a``-th root, and
    checks it is both an exact power and prime. A prime power has a unique
    valid ``(a, p)`` pair (any exponent that divides the true one yields a
    non-prime root), so the first match found is returned directly.
    """
    if m < 2:
        return None
    for a in range(1, m.bit_length() + 1):
        root = integer_nth_root(m, a)
        if root >= 2 and root**a == m and is_prime(root):
            return root
    return None
