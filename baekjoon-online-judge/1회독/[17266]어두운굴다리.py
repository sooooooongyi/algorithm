# 🌜 각 사이의 길이를 넣어두고, 처음 ~ 첫 가로등, 가로등 사이, 마지막 가로등 ~ 마지막 다 커버가 되어야하니까, 가장 큰 값!
# ✨ 꼭 그 길이만큼 밝힐 필요없고, 가로등과 가로등 사이는 //2 로 (대신, 홀수짝수 구분) 하면 최소!로 쓸수있음!

n = int(input())
m = int(input())

diff = []
pos = list(map(int, input().split()))

# 처음 ~ 첫 가로등 사이 거리
diff.append(pos[0] - 0)

# 가로등끼리 사이의 거리
if len(pos) > 1:
    for i in range(len(pos) - 1):
        if (pos[i+1] - pos[i]) % 2 == 0:
            diff.append((pos[i+1] - pos[i]) // 2)
        else:
            diff.append((pos[i+1] - pos[i]) // 2 + 1)

# 마지막 가로등 ~ 끝 사이 거리
diff.append(n - pos[-1])

print(max(diff))    