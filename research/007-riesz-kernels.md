# Research 007 — Riesz kernels
Status: classical conditional criterion, no RH proof.
For integer m>=0 define S_m(x)=sum_{n<=x} Lambda(n)(1-n/x)^m (m=0 means weight 1).
For Re(s)>1, its Mellin transform is W_m(s)*(-zeta'(s)/zeta(s)), where W_m(s)=B(s,m+1)=m!/[s(s+1)...(s+m)] by substitution. W_m is nonzero for Re(s)>0 and W_m(1)=1/(m+1).
Set E_m(x)=S_m(x)-x/(m+1). Its transform is -W_m(s) zeta'(s)/zeta(s)-1/[(m+1)(s-1)]. The pole at 1 cancels.
If for every epsilon>0 E_m(x)<=C_epsilon x^(1/2+epsilon), apply Landau to the nonnegative function C_epsilon x^(1/2+epsilon)-E_m(x), with Mellin measure x^(-s-1)dx. The continuation has no real singularity above 1/2+epsilon, because zeta has no real zeros in (0,1) or (1,infty). Thus the transform converges there and is holomorphic, contradicting any off-line zero pole since W_m is nonzero. Reflection proves RH. The same works for a lower bound. Conversely RH implies the bound by partial summation from the classical Chebyshev estimate.
For m=1, x E_1(x)=A(x)-1/2, so this includes research 004.
Smoothing improves decay in imaginary direction but cannot change the real exponent of an individual zero term. Increasing m alone is not a proof.
Next: seek an independent arithmetic inequality for E_m, or test kernel optimization with rigorous uniform constants. No Lean execution or neural training performed.