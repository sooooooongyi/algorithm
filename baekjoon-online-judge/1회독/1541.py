# 그리디 알고리즘 - 잃어버린 괄호
# (ideas - "-" 뒤엔 괄호를 넣자)

data_list = list(input().split("-"))
sum = 0

for i in range(len(data_list)):
    if i == 0:
        for j in data_list[0].split("+"):
            sum += int(j)
    else:
        for j in data_list[i].split("+"):
            sum -= int(j)
    
print(sum)

# Solution - 처음 숫자는 0으로 시작할 수 있다는 점
# -> 1+03는 runtime error (eval 함수사용 불가)