def solution(s):
    answer = []
    s = s[2:-2].split('},{').sort(key=len)
    s = s.split('},{')
    s.sort(key=len)

    for i in s:
      arr = i.split(',')
      for j in arr:
        if not int(j) in answer:
          answer.append(int(j))
    return answer