# Research 012 — discrete orthogonality
Status: unconditional identities; RH estimate open.
For N>=2, let K_N(n)=6n(N-n)-N^2 and L_N(n)=K_N(n)-N, 1<=n<N.
Sum L_N=0 by elementary power sums. Symmetry gives sum n L_N=0. For N=2,3 the polynomial vanishes on the grid; for N>=4 it is a nontrivial quadratic orthogonal to affine functions.
Let a_N(n)=Lambda(n)Lambda(N-n), G(N)=sum a_N(n), and b_N(n)=a_N(n)-G(N)/(N-1).
Then C(N)=sum b_N(n)L_N(n)+N G(N).
The correction contributes exactly P_0(x)P_1(x)/x to D(x) by ordered-pair symmetry: sum N G(N)e^(-N/x)=2x P_0(x)P_1(x). This is ~x by the prime number theorem. Its contribution to B(Y) is at most Y psi(Y)^2=O(Y^3). Both are below the respective RH-scale targets.
For H_N(j)=sum_{n<=j} b_N(n), H_N(N-1)=0. Discrete summation by parts gives sum b_N L_N=-6 sum_{j=1}^{N-2} H_N(j)(N-2j-1).
Hence sufficient condition: sum_{N<=Y} N^2 max_j |H_N(j)|=O_epsilon(Y^(7/2+epsilon)). This is only a sufficient target, not an established bound. Absolute discrepancy bounds do not imply it.
Alternative exact variance form: under weights a_N/G(N) when G(N)>0, sum b_N L_N=-6 G(N)[Var(n)-(N(N-2)/12)], by symmetry and the variance of the uniform grid 1..N-1. If G(N)=0 the term is zero.
No Goldbach asymptotic assumed. No neural training or Lean execution. Next: seek cancellation across N without requiring pointwise prime-pair equidistribution.