from itertools import permutations

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**(1/2)) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    permutatedNum = set()
    answer = 0
    
    for i in range(1, len(numbers) + 1):
        permutation = permutations(numbers, i)
        for j in permutation:
            permutatedNum.add(int(''.join(j)))
            
    for i in permutatedNum:
        if isPrime(i):
            answer += 1
            
    return answer