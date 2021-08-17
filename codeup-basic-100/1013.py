num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
print("%d %d" %(num1, num2))

# c의 scanf처럼 표준 포맷에 의해(stdin)으로 입력이 안되기때문에, str로 받아서 split 한 뒤 str값을 다시 int로 바꿔줘야함.. Umm..