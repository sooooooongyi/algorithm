# 수학 - 평균 점수

arr = []
for _ in range(5):
    score = int(input())
    if score < 40:
        score = 40
    arr.append(score)

print(int(sum(arr)/len(arr)))