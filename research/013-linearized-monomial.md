# Research 013 — linearized monomial combination
Status: exact identities and equivalent criterion, not RH proof.
Let t=log x, f=P0/x-1, primes denote t derivatives. Moment differentiation gives e0=xf, e1=x(f+f'), e2=x(2f+3f'+f'').
Consequently D/x^2=(1+f)(f'-f'')+2(f')^2 exactly.
The linear combination L=4e1-2e0-e2=x(f'-f'') has Mellin multiplier -(s-1)(s-2) Gamma(s) times -zeta'/zeta for the corresponding uncentered combination, up to sign convention: explicitly 4Gamma(s+1)-2Gamma(s)-Gamma(s+2)=-(s-1)(s-2)Gamma(s). The main term cancels. This multiplier does not vanish at nontrivial zeros.
Thus a bound L=O_epsilon(x^(1/2+epsilon)) is sufficient for RH by Mellin continuation, splitting at x=1; small-x uncentered combination decays exponentially. Conversely RH gives this bound by partial summation.
The quadratic term is not automatically negligible at the desired scale from PNT alone. If all e_j=O(x^theta), its contribution is O(x^(2theta)); theta<=3/4 suffices for the quadratic term alone, but such a fixed power saving is not established here.
No new zero-free region, neural training or Lean verification. Next: seek independent estimates of the linear signed exponential kernel, not assume the equivalent bound.