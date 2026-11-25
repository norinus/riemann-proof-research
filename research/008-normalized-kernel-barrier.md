# Research 008 — normalized kernel barrier
Status: unconditional asymptotic analysis, not RH proof.
Normalize V_m(s)=(m+1) B(s,m+1), so V_m(1)=1.
For fixed s with Re(s)>0, gamma ratio asymptotics give V_m(s)=Gamma(s)m^(1-s)(1+O_s(1/m)).
Thus for a fixed hypothetical zero rho with beta=Re(rho) in (0,1), |V_m(rho)|~|Gamma(rho)| m^(1-beta). Increasing m does not suppress the normalized fixed-zero coefficient.
At x=my with fixed y>0, (1-n/(my))_+^m tends to exp(-n/y). Since Lambda(n)<=log(n), dominated convergence gives S_m(my) -> sum_{n>=1} Lambda(n) exp(-n/y). The domination follows from (1-z)^m<=exp(-mz) for 0<=z<=1. The main term my/(m+1) tends to y. Hence smoothing at large m changes the effective scale to x/m, rather than creating cancellation for free.
These fixed-s and fixed-y limits are not uniform in zero height or y. No interchange with an infinite zero sum is asserted.
Next: study the exponential prime sum and its independent arithmetic bounds; avoid rephrasing equivalent criteria without new estimates.
No neural training or Lean verification performed.