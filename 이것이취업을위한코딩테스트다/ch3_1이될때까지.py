# [그리디] 1이될때까지

# 내 코드
# ex) 25, 3 이라고 했을때 25-1 = 24로 만들고 24//3 하면 8이 남는거지 나눗셈을 8번 한다는 뜻이 아님 -> 애초에 로직이 문제..
'''
N, K = map(int,input().split())
count = 0

while N>0:
    if N%K==0:
        count += N//K
        break
    N -= 1
    count += 1

print(count)
'''
# 해설 코드
N, K = map(int,input().split())
count = 0

# while문을 썼다 -> 즉 한번에 구해지는게 아니라 진짜 1이 될때까지 만들어야함
while True:
    # 가장 근처의 배수 구하기
    target = (N//K)*K
    count += n-target
    # 나누고 남은 숫자
    N = target
    if N<K:
        break
    result += 1
    N //= K

count += (n-1)
print(count)