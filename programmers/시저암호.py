def solution(s, n):
  answer =''
  for i in s:
    if 65 <= ord(i) <= 90:
      answer += chr((ord(i)-65+n)%26 + 65)
    elif 97 <= ord(i) <= 122:
      answer += chr((ord(i)-97+n)%26 + 97)
    elif i==' ':
      answer += i
  return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))