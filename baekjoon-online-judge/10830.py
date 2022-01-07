import sys

input = sys.stdin.readline
A, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(A)]

def matrix_square(matrix1, matrix2):
    result = [[0]* A for _ in range(A)]
    for i in range(A):
        for j in range(A):
            for k in range(A):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    for i in range(A):
        for j in range(A):
            result[i][j] %= 1000

    return result

B = bin(B)[2:] # 이진수로 변환
identity_matrix = [[1 if i == j else 0 for i in range(A)] for j in range(A)]
result = identity_matrix[:]

for i in range(len(B)):
    if B[-i-1] == '1':
        temp = matrix[:]
        while i != 0:
            temp = matrix_square(temp, temp)
            i -= 1
        result = matrix_square(result, temp)

for i in result:
    print(*i)
