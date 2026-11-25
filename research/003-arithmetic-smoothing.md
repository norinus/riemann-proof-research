# Research 003 — arithmetic smoothing and finite-difference barrier
Status: unconditional identities and conditional implications; no RH proof.

For x>=1, A(x)=integral_1^x (psi(t)-t)dt
=sum_{p^k<=x}(x-p^k)log p -(x^2-1)/2, by finite interchange.

For 0<h<x-1, monotonicity of psi yields
(A(x)-A(x-h))/h-h/2 <= psi(x)-x <= (A(x+h)-A(x))/h+h/2.
If |A(x)|=O(x^a), 1<a<2, choose h=x^(a/2) to obtain
psi(x)-x=O(x^(a/2)).
Thus a=3/2+epsilon gives only 3/4+epsilon/2 by this elementary route, not 1/2. The Mellin route in research 002 avoids this loss.

Independent candidate target: exploit cancellation in the weighted prime-power sum. Merely bounding absolute values or invoking prime number theorem does not give the required exponent. Do not label this target a verified lemma.
Next: compare arithmetic convolution identities and identify a genuinely weaker sufficient one-sided estimate using analytic continuation and positivity.
