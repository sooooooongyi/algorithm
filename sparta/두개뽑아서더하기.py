from itertools import combinations

def solution(numbers):
    answer = []
    combi = list(combinations(numbers, 2))
    for number in combi:
        answer.append(sum(number))
    return sorted(list(set(answer)))