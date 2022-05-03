def solution(phone_number):
    temp = list(phone_number)
    for i in range(len(temp)-4):
      temp[i] = '*'
    return ''.join(temp)