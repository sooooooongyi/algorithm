# def solution(n):
#     n=n+1
#     answer=[True]*n
#     for i in range(2, int(n**0.5)+1):
#         if answer[i] == True:
#             for j in range(i+i, n, i):
#                 answer[j] = False
#     a = [i for i in range(2, n) if answer[i]==True]
#     return len(a)

from itertools import permutations
import math

def is_prime_number(x):
    if x == 1 or x == 0:
        return False

    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(n):
    answer = []

    for i in range(1, len(n)+1):
        permute = list(permutations(n, i))
        for j in range(len(permute)):
            num = int(''.join(permute[j]))
            if is_prime_number(num):
                answer.append(num)
    return len(set(answer))

print(solution('011'))