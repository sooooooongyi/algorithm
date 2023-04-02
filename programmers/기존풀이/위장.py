def solution(clothes):
    closet = {}
    total = 1

    for cloth in clothes:
        value = cloth[0]
        type = cloth[1]

        if type in closet:
            closet[type].append(value)
        else:
            closet[type] = [value]

    for value in closet.values():
        total *= (len(value)+1)
    return total - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))