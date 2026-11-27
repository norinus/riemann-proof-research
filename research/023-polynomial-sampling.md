# 연구 023: 다항식 격자에서의 단측 경계와 멜린 극점 보존

2026-11-27. 기준 main 0ddd80a45551475ad7ea2dc9b56836abb6a43143 (연구 022). 상태: **무조건 표본화 정리, 조건부 RH 동치, 일반 양의 측도에 대한 실패 반례. 독립 RH 증명 미완료.** 학계 최초라는 주장은 하지 않는다.

## 1. 모든 차수의 도함수 경계

연구 022의 P(x)=sum_{n>=1} Lambda(n) exp(-n/x), D_r(x)=P(rx)/r-P(x), 고정 r>1을 사용한다.
u=n/x라 하면 x^j (d/dx)^j exp(-n/x)=exp(-u) A_j(u), A_0=1,
A_{j+1}=(u-j)A_j-u A_j'. 이는 곱의 미분법으로 귀납한다.
Lambda(n)<=log n과 지수 감쇠로 모든 양의 x의 콤팩트 구간에서 항별 미분 가능하다.
Chebyshev psi(t)=O(t) 및 Stieltjes 부분합으로 모든 고정 다항식 A에 대해
sum Lambda(n) exp(-n/x)|A(n/x)|=O_A(x) (x>=1).
실제로 절댓값 다항식을 양의 계수 다항식으로 상계한 후 각 u^j exp(-u)를 부분적분하면 된다.
따라서 D_r^(j)(x)=O_{r,j}(x^(1-j)), j>=0. 제곱근 오차 경계는 사용하지 않았다.

## 2. 임의의 고정 양의 실수 k에서 극점 보존

Re s>1에서 S_k(s)=k sum_{n>=1} D_r(n^k)n^(-ks-1), I(s)=int_1^infty D_r(x)x^(-s-1)dx라 놓는다.
f_s(t)=D_r(t^k)t^(-ks-1)이면 I=k int_1^infty f_s(t)dt.
체인룰과 1절에서 f_s^(j)(t)=O_{K,r,k,j}(t^(k(1-Re s)-1-j)) (t>=1, s가 임의의 고정 콤팩트 집합 K에 속할 때).
이는 D_r^(l)(t^k)가 O(t^(k(1-l)))이고, t^k를 미분하는 인자들의 곱이 O(t^(kl-j))인 점과 Leibniz 법칙에서 나온다.
Euler–Maclaurin을 [1,N]에서 적용한 뒤 Re s>1에서 N->infty:
(S_k-I)/k=f_s(1)/2-sum_{j=1}^m B_{2j}/(2j)! f_s^(2j-1)(1)
-int_1^infty Btilde_{2m}(t)/(2m)! f_s^(2m)(t)dt.
주기 Bernoulli 함수는 유계다. 마지막 적분은 Re s>1-2m/k에서 국소 균일 절대수렴하며 정칙이다. 경계항은 s의 전체함수다.
m을 임의로 키울 수 있고 표현들이 원래 반평면에서 일치하므로 항등정리로 붙이면 S_k-I는 전체함수이다.
즉 유한 차수의 다항식 격자 n^k는 멜린 변환의 모든 극점을 보존한다. k가 클수록 필요한 미분 차수가 커지며 k->infty에 대한 균일성은 주장하지 않는다.

## 3. 단측 격자 정리

고정 1/2<=a<1, k>0, r>1에 대해 다음은 동치이다.
(A) Re rho>a인 제타 비자명 영점이 없다.
(B) 충분히 큰 모든 양의 정수 n에서 D_r(n^k)<=C n^(ka) 또는 D_r(n^k)>=-C n^(ka) 중 한 방향이 성립한다.
A=>B: 연구 022 §2의 연속 상한에서 즉시 따른다 (연구 021의 절대수렴 영점 공식 이용).
B=>A: C>0을 키워 모든 n에서 한 방향의 H_n=C n^(ka) minus/plus D_r(n^k)>=0이 성립하게 한다.
Re s>1에서 J(s)=k sum H_n n^(-ks-1)=Ck zeta(1+k(s-a)) minus/plus S_k(s).
연구 022의 I(s)는 Gamma(s)(r^(s-1)-1)(-zeta'/zeta)(s)에서 작은 x 적분 전체함수를 뺀 것이다. s=1은 제거 가능하며 실수 s>a에 특이점이 없다. 2절의 전체함수 보정 및 Ck zeta(1+k(s-a))를 더해도 이 사실은 보존된다.
Landau 정리를 J의 양의 이산 Laplace 측도 (질량 k H_n/n, 위치 k log n)에 적용한다. 유한 수렴 횡좌표는 실수 특이점이어야 하므로 횡좌표<=a (또는 -infinity)이다. 따라서 J는 Re s>a에서 정칙이다.
하지만 Re rho>a인 비자명 영점이 있다면 Gamma(rho)(r^(rho-1)-1)!=0이고 S_k의 극이 보존되므로 J도 거기 극을 갖는다. 모순.
a=1/2 및 함수방정식에서 RH와 동치. 예: r=2,k=100이면 D_2(n^100)<=C n^50 하나의 전 정수 꼬리 경계면 충분하다. 유한 표본이나 수치 적합은 충분하지 않다.

## 4. 지수 격자에 대한 실패 반례

임의의 b>1,r>1, 1/2<beta<1, 0<delta<1에 대해 gamma=2pi/log b, rho=beta+i gamma, c=Gamma(rho)(r^(rho-1)-1) !=0.
[1,infty) 위의 양의 밀도 m(t)=1+delta t^(beta-1) Re(z exp(i gamma log t))를 정의하고 z=i |c|/c로 잡는다. |z|=1, m>=1-delta>0, m(t)->1.
P_m(x)=int_1^infty exp(-t/x)m(t)dt=x+delta Re(z Gamma(rho)x^rho)+O(1), x>=1.
이는 감마 적분에서 [0,1]을 빼는 비용이 유계이고 상수 밀도 부분이 x exp(-1/x)=x+O(1)인 사실에서 나온다.
D_{r,m}(x)=P_m(rx)/r-P_m(x)=-delta |c| x^beta sin(gamma log x)+O(1).
따라서 D_{r,m}(b^n)=O(1)이지만 b^(n+1/4), b^(n+3/4)에서 양방향 x^beta 규모의 진동이 존재한다. 이는 지수 격자에 대한 일반 양의 측도 반례이지 실제 소수 가중치나 RH의 반례가 아니다. 실제 소수에 지수 격자 정리를 얻으려면 별도 산술적 구조가 필요하다.

## 5. 감사, 구현, 다음 단계

직접 증명해야 할 열린 명제: 정확한 Lambda 가중치에서 3절 B의 a=1/2 조건. 다항식 격자가 더 희소해져도 각 n에서 x=n^k 자체는 매우 커질 수 있으므로 증명 또는 계산이 쉬워졌다고 주장하지 않는다. RH를 전제하는 방향은 동치의 역방향으로만 구분했다. 순환논증, 소수 독립성, 유한 검산으로 무한 명제를 증명한다는 가정 없음. 의존성 그래프는 초벌이며 모든 형식 공리 의존성을 감사한 것은 아니다.
다음 과제: 정확한 Lambda=mu*log 또는 셀베르그 항등식의 실제 산술적 제약을 사용해 격자 경계를 직접 공격한다. 단순 표본화 반복보다 산술적 오차의 독립 상계가 우선이다.

실제 실행:
- Python 3.13.5에서 tests/test_research023.py unittest 3/3 통과. SymPy 도함수 0~8차, mpmath 모델 극점 12개 평가, 기하격자 4개 및 중간 위상 2개. 초기 60자리 극점 수치 검사는 소거 오차로 실패하여 100자리에서 다시 실행했다. 이는 수치 검산, 형식 증명 아님.
- data/research023-dependencies.json 12노드의 위상순서 검사 실행. 기존 neural/model.py와 신규 neural/train_research023.py, CPU PyTorch 2.10.0+cpu, seed 23, 훈련 목표 3개/120 steps. 훈련 BCE 0.7130478223 -> 0.4360913634. 홀드아웃 목표 grid-criterion은 훈련 후보 그래프에서도 제외. 실제 홀드아웃 hits@4=0/4, 일반화 실패; 학습 개선만 성공이며 정리 탐색 성능 성공으로 기록하지 않는다. 초기 실험은 홀드아웃 노드를 후보에 포함해 폐기했다. 데이터가 매우 작고 직접 의존성만 라벨링했으므로 다른 관련 정리를 부정하는 레이블이 아니다.
- Lean/lake 없음, 형식 검증 미실행. 모델, 테스트, 그래프, 훈련 스크립트의 원격 Git blob SHA와 실행본 일치 확인 (각각 8215e4c066dc955895e1bbf6522b11791f215026, 530cb3dc755981174431e9db62b9067564d22f6a, 5b961c2dacf2c9649cbef5aeeb5da766586d7220, a96e2e348154459399652803190ffaabe9b048fc). 재현: python -m unittest discover -s tests -p test_research023.py -v; python -m neural.train_research023.

Sources: NIST Euler–Maclaurin https://dlmf.nist.gov/2.10.E1 ; zeta https://dlmf.nist.gov/25.2 ; zeros https://dlmf.nist.gov/25.10 ; Gamma https://dlmf.nist.gov/5.2 ; research/021-triangular-zero-formula-and-endpoint.md and research/022-single-crossing-scale-difference.md. Landau theorem as in research/015-one-sided-monomial-criterion.md.
External status, separate from this project's proofs: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ (2026-11-21 joint certification); https://math.mit.edu/~drew/grh/ (2026-11-25 22:05 UTC update reports all checks complete for original Alpoge/Claude archive, including statement match and standard axioms); https://www.claymath.org/millennium/riemann-hypothesis/ still Active on 2026-11-27. External checks are reported by their authors, not executed in this project. None is used as a premise here.
