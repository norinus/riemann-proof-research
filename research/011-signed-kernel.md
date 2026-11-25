# Research 011 — signed quadratic kernel
Status: unconditional identities; target estimate open.
D=2P1^2-P0 P2 = (1/(2x^2)) sum_{n,m>=1} Lambda(n)Lambda(m) exp(-(n+m)/x) (4nm-n^2-m^2).
Absolute convergence follows from Lambda(n)<=log n. The kernel factors as -(n-(2+sqrt(3))m)(n-(2-sqrt(3))m). It is positive precisely when 2-sqrt(3)<n/m<2+sqrt(3).
Group by N=n+m and define C(N)=sum_{n=1}^{N-1} Lambda(n)Lambda(N-n)[6n(N-n)-N^2].
Then D=(1/(2x^2)) sum_{N>=2} C(N) exp(-N/x).
The continuous uniform model cancels exactly: integral_0^N [6u(N-u)-N^2]du=0. The discrete unweighted sum equals -N (using sums of n and n^2). Thus the unweighted model has D=O(1), but replacing Lambda(n)Lambda(N-n) by a constant is not justified.
Sufficient target: B(Y)=sum_{N<=Y} C(N)=O_epsilon(Y^(7/2+epsilon)). Partial summation gives D=O_epsilon(x^(3/2+epsilon)) and research 010 implies RH. No such bound is established here. Trivial absolute estimates give B=O(Y^4 log^2 Y), or O(Y^4) using Chebyshev psi=O(Y).
Do not assume pointwise Goldbach asymptotics or independence of prime pairs. The signed kernel cancels the continuous main term, not automatically the arithmetic discrepancy.
No neural training or Lean verification performed. Next: derive exact discrete orthogonal kernel and isolate weighted additive correlation discrepancy.