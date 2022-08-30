price = int(input())

won500 = price // 500
price %= 500

won100 = price // 100
price %= 100

won50 = price // 50

print(won500 + won100 + won50)