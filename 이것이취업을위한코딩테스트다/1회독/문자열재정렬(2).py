data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()
if value != 0:
    result.append(str(value))

# ''.join은 문자간 공백없이 출력하게끔!
print(''.join(result))