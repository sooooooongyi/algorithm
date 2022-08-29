# DP - 피보나치 함수
# Solution
# (1) ex f(3) = f(2) + f(1) 라는걸 이용하면, 각각 0과 1의 횟수도 피보나치 수열로 연결된걸 확인할 수 있다! -> o

zero_case = [1, 0]
one_case = [0, 1]

for i in range(2, 41):
    zero_case.append(zero_case[i-1]+zero_case[i-2])
    one_case.append(one_case[i-1]+one_case[i-2])

T = int(input())
for _ in range(T):
    n = int(input())
    print(zero_case[n], one_case[n])