# 연구 026 — 나머지 단항식과 정확한 이차 오차 증명서

상태: 독립 RH 증명 미완료. 025(9d680fa9886b6ff616dcf9c60bdebb4e70bdb21e)의 밀도 반례에 대응하여, 합성 가중치 대신 정확한 가분성 구조를 사용하는 별도 경로를 추가한다. HUMAN_FORMULA_OBJECTIVE의 낮은 차수 원칙을 적용한다. 기존 경로는 폐기하지 않는다.

## 1. 기저와 증명 목표

Báez-Duarte의 강화 Nyman–Beurling 기준 (https://arxiv.org/abs/math/0202141): RH iff chi_(0,1) lies in the L2(0,infty) closure of span rho(1/(kx)), k in positive integers, rho(t)=fractional part of t. To impose cancellation, subtract rho(1/x) times a=sum c_k/k from each candidate. On x>1 the original candidate is a/x, so approximation error tending to zero implies a->0; rho(1/x) has finite norm. Hence the span of g_k=rho(1/(kx))-rho(1/x)/k, k>=2, has the same approximation criterion. These functions vanish for x>1, and on 1/(n+1)<x<1/n equal f_k(n)=(n mod k)/k, because floor((1/x)/k)=floor(n/k). Endpoints are immaterial.

Define r_c(n)=1-sum_{k=2}^N c_k f_k(n), w_n=1/[n(n+1)], E(c)=sum_{n>=1} w_n r_c(n)^2. Then RH iff d_N^2=inf_c E(c) tends to zero as N->infty. Rational coefficients suffice by density and finite-dimensional continuity. This is a classical criterion, not a new RH proof.

## 2. Finite training error can always vanish

For M>=1, N=M+1, choose c_k=-mu(k) for 2<=k<=M, c_(M+1)=(M+1)sum_{k<=M}mu(k)/k. This is the unique exact prefix fit with these N-1 coefficients. Indeed A=sum c_k/k=1 from n=1, and f_k(n)-f_k(n-1)=1/k-1_{k|n}. The remaining conditions for n=2..M give sum_{k|n,k>=2}c_k=1 and hence c_n=-mu(n) by divisor inversion. The remaining coefficient fixes A. See https://dlmf.nist.gov/27.5.E3. Equivalently, for every n>=1 the residual of this fit is sum_{M<k<=n}mu(k)floor(n/k)+c_(M+1)floor(n/(M+1)), by sum_{k<=n}mu(k)floor(n/k)=1. It vanishes identically on the entire training prefix. Nevertheless at L=lcm(2,...,M+1), r_c(L)=1 and E(c)>=1/[L(L+1)]>0. The bound depends on M and does not rule out decay to zero as M grows. This failure concerns finite-prefix certification, not RH. Example M=1: c_2=2, residual 1 on even n and 0 on odd n; E=1-log 2, despite zero prefix error.

## 3. Quadratic certificates, including infinite tail

For fixed N and M>=N define G_ij=sum_{n<=M}w_n f_i(n)f_j(n), b_i=sum_{n<=M}w_n f_i(n), S=M/(M+1). Then E_M(c)=S-2b^T c+c^T G c. G positive definite: if sum c_k f_k(n)=0 for n<=N, n=1 gives A=0, then successive differences give sum_{k|n}c_k=0; induction yields each c_n=0. Thus c_low=G^-1 b minimizes E_M and E_M(c_low) <= d_N^2.

For any candidate r_c(n) lies between a=1-sum_{c_k>0} c_k(k-1)/k and b'=1-sum_{c_k<0} c_k(k-1)/k. Set B=max(|a|,|b'|). Since sum_{n>M}w_n=1/(M+1),
E_M(c) <= E(c) <= E_M(c)+B^2/(M+1).
By Cauchy-Schwarz B^2 <= N(1+sum c_k^2), so a tractable conservative upper quadratic is E_M(c)+lambda(1+||c||^2), lambda=N/(M+1). Its unique minimizing coefficient vector is

    (G + lambda I)c = b.

This is an unconditional exact linear relation, not a proof of RH. Use c_high=(G+lambda I)^-1 b and the tighter B bound to enclose d_N^2 between E_M(c_low) and E_M(c_high)+B^2/(M+1). All quantities rational for finite inputs. For fixed N, G and b converge entrywise to their infinite sums, G_infty is positive definite by the same finite prefix, and both coefficient vectors converge to G_infty^-1 b_infty as M->infty. B stays bounded, so both bounds converge to d_N^2. This does NOT justify exchanging N and M limits, or supply a uniform decay estimate in N.

## 4. Executed verification and next step

synthesis/research026.py: Python 3.13.5, 5 unittest groups passed in 0.332 s (prefix fits M=1..30, Mobius divisor sums n=1..100, 7 ridge dimensions, tail and distance bounds). At M=128, displayed rounded approximations to exact rational enclosing endpoints for d_N^2: N=2 [0.302991873,0.315440450], N=4 [0.064121990,0.077124301], N=8 [0.022997600,0.052693958]. Exact values reside in runtime Fraction results; rounded display endpoints are not outward-rounded certificates. Code blob SHA fd0f929506a6c959227edc2459f4f8c48b0af919. Lean/lake unavailable; draft algebra lemmas not checked. No neural training executed; curated dependencies are training labels only. No assumption of RH in certificate construction, no numerical extrapolation, no circular dependency on RH for bounds. Formal axiom audit and independent human review pending. Literature novelty not asserted.

Next: search explicit c^(N) using multiplicative/divisor identities and prove a uniform upper bound tending to zero; compare truncated-error ranking against certified-tail ranking. Do not claim finite decrease proves the limit.

External status separately: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ reports verification of Alpoge's original proof. https://math.mit.edu/~drew/shortgrh/ updated 2026-11-27 17:27 UTC reports all checks finished for shorter proof, including compact edition 76,149 nonblank noncomment code lines, standard three axioms, two-machine paranoid comparator passes for compact edition; readable edition second machine stopped for insufficient RAM. No use of those proofs as premises in this project. https://www.claymath.org/millennium/riemann-hypothesis/ is the official problem page. External verification is not project completion.
