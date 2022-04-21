N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(K):
    if min(A) < max(B):
        A_min = min(A)
        B_max = max(B)
        A[A.index(A_min)], B[B.index(B_max)] = B[B.index(B_max)], A[A.index(A_min)]

print(sum(A))