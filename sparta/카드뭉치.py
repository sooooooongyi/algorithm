def solution(cards1, cards2, goal):
    for i in range(len(goal)):
        if len(cards1) > 0 and cards1[0] == goal[i]:
            del cards1[0]
        elif len(cards2) > 0 and cards2[0] == goal[i]:
            del cards2[0]
        else:
            return "No"
    return "Yes"