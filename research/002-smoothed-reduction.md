# Research 002 — smoothed Mellin criterion
Status: rigorous conditional reduction; RH remains open in this project.

Define A(x)=integral from 1 to x of (psi(t)-t) dt.
For Re(s)>1, Fubini gives
integral_1^infty A(x)x^(-s-2) dx =
1/(s+1) integral_1^infty (psi(t)-t)t^(-s-1) dt.
Consequently
-zeta'(s)/zeta(s)=s/(s-1)+s(s+1) integral_1^infty A(x)x^(-s-2) dx.
If A(x)=O_epsilon(x^(3/2+epsilon)) for every epsilon>0, the integral is holomorphic on Re(s)>1/2 by locally uniform absolute convergence. Meromorphic uniqueness excludes zeros there; the functional equation excludes reflected nontrivial zeros.

OPEN: prove the smoothed estimate independently. Smoothing is not a proof of cancellation.
Rejected shortcut: bounding each zero term individually presupposes a bound on its real part. A numerical fit cannot establish the uniform asymptotic estimate.
Next experiment: derive arithmetic expressions for A(x) and seek unconditional cancellation estimates, tracking constants and quantifiers.
