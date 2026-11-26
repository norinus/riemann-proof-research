# 연구 017: 실제 소수 지지집합의 한계와 소수 거듭제곱 제거
기준판 d2b1a36cca9fc7d3849add7cda0f25f967a116f1. 상태: 무조건적 환원 및 변형 가중치에 대한 반례, RH 미증명. 학계 최초라는 주장 없음. 2026-11-26.

## A. 실제 소수만 남겨도 목표는 변하지 않는다
theta(Y)=sum_{p<=Y} log p, psi(Y)=sum_{n<=Y} Lambda(n). Chebyshev bound theta(Y)=O(Y) gives
psi(Y)-theta(Y)=sum_{k>=2} theta(Y^(1/k))=O(sqrt(Y)+Y^(1/3)log Y)=O(sqrt(Y)).
Let P_j^p use only primes with exact log p weight. If h is the nonnegative measure of higher prime powers, h([0,Y])=O(sqrt(Y)). For fixed j, the kernel g_j(u)=u^j exp(-u), Stieltjes integration by parts gives
|P_j-P_j^p| <= C sqrt(x) integral_0^infty sqrt(u)|g_j'(u)|du=O_j(sqrt(x)).
Boundary terms vanish since h is zero near 0 and grows at most as sqrt(Y). All moments are O_j(x) for x>=1 by Chebyshev, hence D-D^p=O(x^(3/2)).
For the triangular polynomial W(n,m)=4nm-n²-m², |W|<=Y² on n+m<=Y because W=6nm-(n+m)² and 0<=nm<=(n+m)²/4. Write B as I(mu,mu) for mu=dpsi, nu=dtheta, h=mu-nu. Then B-B^p=I(h,mu)+I(nu,h)=O(Y² sqrt(Y) Y)=O(Y^(7/2)).
Consequently any of the previously obtained RH-equivalent one-sided or two-sided bounds (research 013–015) may use exact prime weights alone, with the same exponents. This is not an estimate of the remaining prime-only discrepancy.

## B. Stronger negative control: actual prime locations, almost exact weights
Fix 1/2<a<beta<1 and any nonzero real polynomial Q with Q(1)=0. There exist gamma>0 and 0<delta<1 such that
w(p)=log(p)[1+delta p^(beta-1) cos(gamma log p)], w(n)=0 at nonprimes.
These positive weights have the exact support of primes and w(p)/log p -> 1. By partial summation of theta(t)=O(t), the difference of their cumulative mass from theta(Y) is O(Y^beta); thus they obey PNT and any usual subexponential classical PNT error bound that theta obeys. They do not satisfy the exact arithmetic weight law.

Define F(s)=sum_p log(p)p^(-s) for Re(s)>1. Euler product gives F(s)=-zeta'(s)/zeta(s)-H(s), H(s)=sum_p sum_{k>=2} log(p)p^(-ks), holomorphic for Re(s)>1/2 by local uniform absolute convergence (geometric sum bounded by constant times p^(-2sigma)). F has a simple pole at 1 of residue 1.
Since zeta has no positive real zeros (eta identity for 0<s<1, Euler product for s>1), g(s)=(s-1)zeta(s) is continuous and nonvanishing on [a,2], including 1. Compactness gives eta>0 such that g is nonzero for a<=Re(s)<=2, |Im(s)|<eta. Beyond Re(s)>2 use the Euler product. Choose 0<2gamma<eta with Q(beta+i gamma)!=0 (a polynomial has only finitely many roots). No numerical zero verification is needed for this existence argument.

Put rho*=beta+i gamma. The transformed Dirichlet series is exactly
F_w(s)=F(s)+(delta/2)[F(s+1-rho*)+F(s+1-conjugate(rho*))].
Initially Re(s)>1, then meromorphic for Re(s)>a. At rho*, the first shifted term has a simple pole with residue delta/2. The base and other shifted terms are regular there: their arguments are rho* and 1+2i gamma, in the zero-free strip and not 1. Along the real axis s>a the only pole is s=1, from the base term.

For Q(s)=sum_j c_j (s)_j, define L_w(x)=sum_j c_j sum_p w(p)(p/x)^j exp(-p/x). Then
integral_0^infty L_w(x)x^(-s-1)dx=Gamma(s) Q(s) F_w(s), Re(s)>1.
Fubini follows from the absolute bounds above; the integral over (0,1) is entire by exponential decay. Q(1)=0 cancels the real pole. At rho* the residue is (delta/2)Gamma(rho*)Q(rho*) !=0.
If either L_w(x)<=Cx^a or L_w(x)>=-Cx^a eventually, enlarge C so Cx^a minus/plus L_w is nonnegative for x>=1. Its Mellin transform, equivalently a Laplace transform after x=exp(t), converges for Re(s)>1. Landau's theorem for nonnegative Laplace transforms forces a real singularity at any finite abscissa of convergence. Here the meromorphic expression has no real singularity above a. Thus the transform is holomorphic throughout Re(s)>a, contradicting the pole at rho*. Both one-sided bounds fail for the constructed weights. This rules out deducing the desired estimate from actual prime locations, positivity, asymptotically correct log weights and classical PNT error alone.

The same weights also defeat D_w=2(P_1^w)^2-P_0^w P_2^w in both directions at scale x^(1+a): research 015's terminal ODE uses only positivity, moment differentiation and PNT, all satisfied here. Either bound would give a one-sided bound on P_0^w-x at scale x^a, contradicted by the same Landau argument using Gamma(s)F_w(s)-1/(s-1) and subtracting the entire small-x integral. Laplace transfer in 015 then excludes either bound for B_w at scale Y^(3+a). This does not refute RH or the criteria for exact log weights.

## C. Dependencies and next task
Classical inputs: Chebyshev bound, PNT, Stieltjes partial summation, Euler product, zeta meromorphic continuation and real nonvanishing via alternating eta series, Gamma integral and nonvanishing, Landau theorem, identity theorem. No RH, prime independence, numerical zero certification or Goldbach asymptotics used. The analytic arguments are human-readable and not formally checked. The next task must exploit an identity specific to exact prime weights (e.g. divisor identity Lambda*1=log), not a generic moment or support property. The shifted model breaks that identity: at a prime p, sum_{d|p} w(d)=w(p), not necessarily log p.
References: https://dlmf.nist.gov/25.2 (Euler product); https://dlmf.nist.gov/25.10 (zeros); https://dlmf.nist.gov/25.16 (Chebyshev/PNT); https://dlmf.nist.gov/5.2 (Gamma); Landau's theorem as used in research/015-one-sided-monomial-criterion.md. External RH status: https://www.claymath.org/millennium/riemann-hypothesis/ lists Active; no external Claude proof relied upon.
Tests: local Python 3.13.5, five unittest methods passed on a copy of the fetched synthesis/polynomial.py and tests/test_research017.py; 260 rational basis cases, three explicit vectors, 49 finite triangular split/bound cases, 49 unit baselines, 2401 kernel bound pairs. These finite tests do not certify the analytic arguments. Lean/lake absent in local runtime; no Lean validation or neural training. Knowledge-graph seed is an annotated local dataset, not an ingestion of all mathematics.
