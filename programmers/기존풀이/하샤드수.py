def solution(x):
    cnt = 0
    for i in str(x):
      cnt += int(i)

    if int(x)%cnt == 0:
      return True
    else:
      return False