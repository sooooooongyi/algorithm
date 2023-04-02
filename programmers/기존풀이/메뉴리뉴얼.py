from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
      temp = []
      for order in orders:
        combi = combinations(sorted(order), c)
        temp += combi
      counter = Counter(temp)

      print(counter)
      if len(counter) != 0 and max(counter.values()) != 1:
        answer += [''.join(x) for x in counter if counter[x] == max(counter.values())]

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))