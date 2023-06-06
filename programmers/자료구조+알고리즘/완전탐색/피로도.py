from itertools import permutations

def solution(k, dungeons):
    answer = []
    permutatedDungeons = permutations(dungeons, len(dungeons))
    
    for permutatedDungeon in permutatedDungeons:
        fatigue = k
        count = 0
        for i, order in enumerate(permutatedDungeon):
            if fatigue >= order[0]:
                fatigue -= order[1]
                count += 1
            else:
                break
        answer.append(count)
                
    return max(answer)