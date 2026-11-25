"""Exact rising-factorial basis synthesis; coefficients in ascending order."""
from fractions import Fraction
from math import factorial

def rising(k):
    p = [1]
    for j in range(k):
        q = [0]*(len(p)+1)
        for i,c in enumerate(p):
            q[i] += j*c
            q[i+1] += c
        p = q
    return p

def synthesize(coefficients):
    q = list(map(Fraction, coefficients))
    c = [Fraction(0)]*len(q)
    for k in range(len(q)-1,-1,-1):
        c[k] = q[k]
        for i,b in enumerate(rising(k)):
            q[i] -= c[k]*b
    assert not any(q)
    return c

def cancels_main_term(c):
    return sum(v*factorial(k) for k,v in enumerate(c)) == 0

if __name__ == "__main__":
    c = synthesize([1,-2,1])
    assert c == [1,-3,1]
    assert cancels_main_term(c)
    print(c)
