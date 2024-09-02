# 🌜 금, 은, 동 총점으로 가보자! + rank 구현..!
# ✨ 총점은 안되고 개수가 서로 연관이 있어버림ㅠ sort를 여러번하는걸루.

n, k = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
s.sort(key=lambda x : (-x[1], -x[2], -x[3]))

for i in range(n):
    if s[i][0] == k:
        index = i
        
for i in range(n):
    if s[index][1:] == s[i][1:]:
        print(i + 1)
        break