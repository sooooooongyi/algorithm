import math


prime = []

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return
    prime.append(n)

def solution(n):
    for i in range(2, n+1):
        is_prime(i)
    return [i for i in prime if n % i == 0]
            