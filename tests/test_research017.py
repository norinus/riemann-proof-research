"""Finite exact algebra checks, not analytic or RH verification."""
import unittest
from fractions import Fraction
from random import Random
from synthesis.polynomial import rising, synthesize, cancels_main_term


def triangular(a, b, y):
    return sum(a[n] * b[m] * (4*n*m-n*n-m*m)
               for n in range(1, y) for m in range(1, y-n+1))


class Research017(unittest.TestCase):
    def test_basis_roundtrip(self):
        rng = Random(17)
        for degree in range(13):
            for _ in range(20):
                p = [Fraction(rng.randint(-20, 20), rng.randint(1, 9))
                     for _ in range(degree+1)]
                c = synthesize(p)
                recovered = [Fraction(0)] * len(p)
                for k, v in enumerate(c):
                    for i, b in enumerate(rising(k)):
                        recovered[i] += v*b
                self.assertEqual(recovered, p)
                self.assertEqual(cancels_main_term(c), sum(p) == 0)

    def test_examples(self):
        self.assertEqual(synthesize([1,-2,1]), [1,-3,1])
        self.assertEqual(synthesize([-1,3,-3,1]), [-1,7,-6,1])
        self.assertEqual(synthesize([-6,11,-6,1]), [-6,18,-9,1])

    def test_triangular_split_and_bound(self):
        rng = Random(170)
        for y in range(2, 51):
            a = [0] + [rng.randrange(8) for _ in range(y)]
            h = [0] + [rng.randrange(8) for _ in range(y)]
            w = [u+v for u,v in zip(a,h)]
            diff = triangular(w,w,y)-triangular(a,a,y)
            self.assertEqual(diff, triangular(h,w,y)+triangular(a,h,y))
            self.assertLessEqual(abs(diff), 2*y*y*sum(w)*sum(h))

    def test_uniform_baseline(self):
        for y in range(2, 51):
            a = [0] + [1]*y
            self.assertEqual(triangular(a,a,y), y*(y*y-1)//3)

    def test_kernel_bound(self):
        for n in range(1, 50):
            for m in range(1, 50):
                self.assertLessEqual(abs(4*n*m-n*n-m*m), (n+m)**2)


if __name__ == '__main__':
    unittest.main()
