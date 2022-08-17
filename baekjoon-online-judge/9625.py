n = int(input())
a_count = [1, 0]
b_count = [0, 1]

for i in range(2, n+1):
    a_count.append(a_count[i-2] + a_count[i-1])
    b_count.append(b_count[i-2] + b_count[i-1])

print(a_count[-1], b_count[-1])
