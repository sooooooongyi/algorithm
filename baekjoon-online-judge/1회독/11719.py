# 구현 - 그대로 출력하기 2
# Solution
# (1) 파이썬은 EOF가 에러 (if문으로 처리x) -> o

while True:
    try:
        print(input())
    except EOFError:
        break