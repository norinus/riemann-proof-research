"""Finite checks of research 023, not a proof of RH."""
import unittest
import mpmath as mp
import sympy as sp


def derivative_polys(order):
    u = sp.Symbol('u')
    p = sp.Integer(1)
    out = [p]
    for j in range(order):
        p = sp.expand((u-j)*p-u*sp.diff(p,u))
        out.append(p)
    return u, out


class SamplingTest(unittest.TestCase):
    def test_derivative_recurrence(self):
        u, polys = derivative_polys(8)
        x, n = sp.symbols('x n', positive=True)
        f = sp.exp(-n/x)
        for j, p in enumerate(polys):
            self.assertEqual(sp.simplify(x**j*sp.diff(f,x,j)/f-p.subs(u,n/x)),0)

    def test_model_discrete_mellin_pole(self):
        # For H(x)=x^rho, sum minus integral is k*zeta(1+k*(s-rho))-1/(s-rho).
        with mp.workdps(100):
            for k in (1,4,20,100):
                h = mp.mpf('1e-24')
                for z in (h, -h, mp.j*h):
                    v = k*mp.zeta(1+k*z)-1/z
                    self.assertLess(abs(v-k*mp.euler), mp.mpf('1e-18'))

    def test_geometric_alias(self):
        # Positive density on [1,infinity); integrate analytically with incomplete gamma.
        with mp.workdps(50):
            b,r,beta,delta = mp.mpf(16),mp.mpf(2),mp.mpf('.75'),mp.mpf('.5')
            gamma = 2*mp.pi/mp.log(b)
            rho = beta+mp.j*gamma
            c = mp.gamma(rho)*(r**(rho-1)-1)
            phase = mp.j*abs(c)/c
            def p(x):
                return x*mp.exp(-1/x)+delta*mp.re(phase*x**rho*mp.gammainc(rho,1/x,mp.inf))
            def d(x):
                return p(r*x)/r-p(x)
            for n in (2,4,8,12):
                self.assertLess(abs(d(b**n)), 3)
            for offset, sign in ((mp.mpf('.25'),-1),(mp.mpf('.75'),1)):
                x = b**(12+offset)
                self.assertLess(abs(d(x)/x**beta-sign*delta*abs(c)),mp.mpf('1e-9'))


if __name__ == '__main__':
    unittest.main()
