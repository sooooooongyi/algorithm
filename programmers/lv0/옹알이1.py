from itertools import permutations

def solution(babbling):
    word = []
    answer = 0
    speek = ["aya","ye","woo","ma"]
    for i in range(1, len(speek)+1):
        for j in permutations(speek, i):
            word.append(''.join(j))
            
    for i in babbling:
        if i in word:
            answer += 1
    return answer