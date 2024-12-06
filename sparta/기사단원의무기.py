def getPrimeNum(number):
    cnt = 0
    for i in range(1, int(number**0.5)+1):
        if number % i == 0:
            cnt += 1
            if i < number // i:
                cnt += 1
    return cnt

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        primeNum = getPrimeNum(i)
        if primeNum > limit:
            answer += power
        else:
            answer += primeNum
    
    return answer