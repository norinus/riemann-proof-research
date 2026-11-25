# Research 004 — one-sided smoothed criterion
Status: conditional theorem, classical Landau method; not a proof of RH.

Assume for every epsilon>0 there exists C>0 such that A(x)<=C x^(3/2+epsilon) for x>=1. Fix 0<epsilon<1/2, a=1/2+epsilon. Put B(x)=C x^(a+1)-A(x)>=0.
For Re(s)>1 its Mellin transform is
M(s)=integral_1^infty B(x)x^(-s-2)dx
=C/(s-a)+(zeta'(s)/zeta(s)+s/(s-1))/(s(s+1)).
The apparent pole at 1 cancels because zeta has a simple pole there. For real s in (a,1), zeta(s) is nonzero by the alternating eta series (eta(s)>0 and 1-2^(1-s)<0). Thus the meromorphic continuation has no real singularities on (a,infty).
By Landau's theorem for Laplace transforms of nonnegative locally integrable functions (substitute x=exp(u)), a finite abscissa of convergence is a real singularity. Since A(x)=O(x^2 log x) trivially, the abscissa is finite above, or is minus infinity. Hence it is <=a. M is holomorphic on Re(s)>a. The displayed identity and meromorphic uniqueness exclude zeta zeros there: at any such zero rho the logarithmic derivative has nonzero residue, and rho is neither 0 nor -1. Let epsilon decrease to zero and use xi symmetry.
The reverse implication follows from the classical RH Chebyshev error bound by integration.
The analogous lower bound follows by using B=C x^(a+1)+A.
OPEN: prove either one-sided bound unconditionally. No improvement in established zero-free region is claimed. No Lean verification performed.
Next: derive exact arithmetic convolution identities and test whether they give a one-sided inequality without an RH-equivalent premise.
