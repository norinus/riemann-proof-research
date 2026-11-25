# Research 005 — arithmetic convolution and remainder barrier
Status: unconditional reduction, not RH proof.

By Mobius inversion Lambda=mu*log. For y>=1 define H(y)=sum_{m<=y}(y-m)log m.
Then A(x)=sum_{d<=x}mu(d)d H(x/d)-(x^2-1)/2 exactly.
Using Stirling log(floor(t)!)=t log t-t+O(log(2t)) and integrating from 1 to y gives
H(y)= (y^2/2)log y-3y^2/4+O(y log(2y)).
Define R(y) by subtracting these two main terms. Thus
A(x)=x^2/2 sum_{d<=x}mu(d)/d log(x/d)
-3x^2/4 sum_{d<=x}mu(d)/d
+sum_{d<=x}mu(d)d R(x/d)-(x^2-1)/2.
The absolute remainder estimate is O(x sum_{d<=x}log(2x/d))=O(x^2), by integral comparison. This cannot establish the desired O_epsilon(x^(3/2+epsilon)).
Even exact evaluation of the two leading sums would not suffice without controlling the remainder. The cancellation must be proved jointly or through a sharper decomposition.
Reject treating Mobius signs as independent random variables: no such assumption is justified.
Next target: exploit exact factorial identity sum_{d<=x}Lambda(d) floor(x/d)=log(floor(x)!) and investigate whether floor-error correlations provide a noncircular bound.
No neural training or Lean execution performed.
