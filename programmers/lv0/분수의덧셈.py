import math

def lcm(a,b):
    return (a * b) // math.gcd(a,b)

def solution(numer1, denom1, numer2, denom2):
    answer = []
    demom3 = lcm(denom1, denom2)
    numer3 = numer1*(demom3//denom1) + numer2*(demom3//denom2)
    
    gcd3 = math.gcd(demom3, numer3)
    return [numer3//gcd3, demom3//gcd3]