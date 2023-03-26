from itertools import permutations

def solution(spell, dic):
    permutation = [''.join(i) for i in list(permutations(spell, len(spell)))]
    for i in dic:
        if i in permutation:
            return 1
    return 2