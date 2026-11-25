# Research 009: monomial discovery
Define P_k(y)=sum_{n>=1} Lambda(n)(n/y)^k exp(-n/y), y>0, k>=0.
All moments converge and are positive. Cauchy-Schwarz gives P_k^2 <= P_(k-1) P_(k+1) for k>=1.
Thus Q_k=P_k^2/(P_(k-1) P_(k+1)) <=1, unconditionally.
PNT and dominated convergence give P_k(y)/y -> k! as y->infty, hence Q_k -> k/(k+1).
Candidate (OPEN): |Q_k-k/(k+1)|=O_epsilon(y^(-1/2+epsilon)). Do not assume this or claim it suffices for RH without a separate proof.
For k=1, P_1^2<=P_0 P_2 is an exact positive moment constraint, not a new theorem in the literature.
Proof data: Cauchy-Schwarz, positivity of Lambda, PNT, exponential smoothing from research 008.
Search design: enumerate integer exponent vectors on positive moments, enforce sum of exponents zero for scale invariance; certify inequalities by nonnegative combinations of adjacent log-convexity inequalities. Do not treat numerical ranking as proof.
