"""Exact rational quadratic certificates for the discrete Beurling approximation.
Finite certificates do not prove RH; the infinite-dimension limit remains open here.
"""
from fractions import Fraction as F
from math import lcm


def residue(n, k):
    return F(n % k, k)


def mobius(m):
    mu = [0] * (m + 1)
    mu[1] = 1
    for k in range(1, m + 1):
        for j in range(2 * k, m + 1, k):
            mu[j] -= mu[k]
    return mu


def prefix_fit(m):
    assert m >= 1
    mu = mobius(m)
    c = {k: F(-mu[k]) for k in range(2, m + 1)}
    c[m + 1] = (m + 1) * sum((F(mu[k], k) for k in range(1, m + 1)), F(0))
    return c


def residual(n, c):
    return 1 - sum((v * residue(n, k) for k, v in c.items()), F(0))


def error_interval(c, m):
    assert m >= 1 and all(k >= 2 for k in c)
    lower = sum((residual(n, c)**2 / (n * (n + 1)) for n in range(1, m + 1)), F(0))
    lo = 1 - sum((v * F(k - 1, k) for k, v in c.items() if v > 0), F(0))
    hi = 1 - sum((v * F(k - 1, k) for k, v in c.items() if v < 0), F(0))
    return lower, lower + max(abs(lo), abs(hi))**2 / (m + 1)


def solve(a, b):
    a = [list(row) + [v] for row, v in zip(a, b)]
    for i in range(len(a)):
        p = next(j for j in range(i, len(a)) if a[j][i])
        a[i], a[p] = a[p], a[i]
        a[i] = [v / a[i][i] for v in a[i]]
        for j in range(len(a)):
            if j != i:
                q = a[j][i]
                a[j] = [v - q * u for v, u in zip(a[j], a[i])]
    return [row[-1] for row in a]


def quadratic_fit(N, m, lam):
    assert N >= 2 and m >= N and lam >= 0
    ks = list(range(2, N + 1))
    f = [[residue(n, k) for n in range(1, m + 1)] for k in ks]
    w = [F(1, n * (n + 1)) for n in range(1, m + 1)]
    g = [[sum((a*b*t for a,b,t in zip(fi,fj,w)), F(0)) + (lam if i == j else 0)
          for j, fj in enumerate(f)] for i, fi in enumerate(f)]
    b = [sum((a*t for a,t in zip(fi,w)), F(0)) for fi in f]
    return dict(zip(ks, solve(g, b)))


def ridge_fit(N, m):
    """Minimize a proved (possibly loose) upper quadratic, not the full norm."""
    return quadratic_fit(N, m, F(N, m + 1))


def distance_interval(N, m):
    """Enclose the minimum infinite error over span of residues 2 through N."""
    low_c = quadratic_fit(N, m, F(0))
    high_c = ridge_fit(N, m)
    return error_interval(low_c, m)[0], error_interval(high_c, m)[1]


def self_test():
    import unittest
    class Checks(unittest.TestCase):
        def test_prefix_and_period(self):
            for m in range(1, 31):
                c = prefix_fit(m)
                self.assertTrue(all(residual(n, c) == 0 for n in range(1, m + 1)))
                self.assertEqual(residual(lcm(*c), c), 1)
        def test_tail_intervals(self):
            for m in range(1, 13):
                c = prefix_fit(m)
                a, b = error_interval(c, 64)
                d, e = error_interval(c, 128)
                self.assertLessEqual(a, d)
                self.assertLessEqual(e, b)
                self.assertLessEqual(d, b)
        def test_ridge(self):
            for N in range(2, 9):
                m = 128
                c = ridge_fit(N, m)
                e, upper = error_interval(c, m)
                lam = F(N, m + 1)
                obj = e + lam * (1 + sum(v*v for v in c.values()))
                self.assertLessEqual(upper, obj)
                self.assertLess(obj, 1 + F(N - 1, m + 1))
                for k in c:
                    gradient = sum((residual(n, c)*residue(n, k)/(n*(n+1)) for n in range(1,m+1)), F(0))
                    self.assertEqual(gradient, lam*c[k])
        def test_distance_interval(self):
            for N in range(2, 9):
                a, b = distance_interval(N, 64)
                d, e = distance_interval(N, 128)
                self.assertLessEqual(a, d)
                self.assertLessEqual(d, b)
                self.assertLessEqual(d, e)
                self.assertGreater(a, 0)
        def test_mobius(self):
            mu = mobius(100)
            for n in range(1, 101):
                self.assertEqual(sum(mu[k] for k in range(1,n+1) if n%k==0), int(n==1))
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Checks)
    if not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful():
        raise SystemExit(1)
    for N in (2, 4, 8):
        a, b = distance_interval(N, 128)
        print(f'N={N} M=128 distance squared interval [{float(a):.9f}, {float(b):.9f}]')


if __name__ == '__main__':
    self_test()
