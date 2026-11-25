# Research 006 — binomial kernel and Mellin obstruction
Status: unconditional classical identities; no RH proof.
For real x>=1 define K(x)=log(floor(x)!)-2 log(floor(x/2)!).
Then K(x)=sum_{d<=x} Lambda(d) w(x/d), w(u)=floor(u)-2 floor(u/2), in {0,1}.
Equivalently K(x)=sum_{k>=1}(-1)^(k-1) psi(x/k), finite since psi(y)=0 for y<1.
Stirling gives K(x)=x log 2+O(log(2x)).
For Re(s)>1 the Mellin transform integral_1^infty K(x)x^(-s-1)dx equals eta(s)/s * (-zeta'(s)/zeta(s)) = -(1-2^(1-s)) zeta'(s)/s.
The strong elementary error in K does not imply a strong error in psi: eta(s)=(1-2^(1-s))zeta(s) cancels the poles at nontrivial zeros. Inversion would require controlling 1/eta, precisely where RH-related singularities occur.
Generalization: any finite linear combination of factorial logs has Mellin multiplier zeta(s) times a Dirichlet polynomial and thus the same cancellation.
Next: investigate non-factorial kernels whose Mellin transforms do not vanish at hypothetical off-line zeros, with independent arithmetic estimates. No neural training or Lean verification performed.
