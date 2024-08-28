# 🌜, ✨ 등차수열, 끝 값 이용하기!

n = int(input())

answer = 1
boundary = 1

while boundary < n:
    boundary += answer * 6
    answer += 1

print(answer)