def solution(n):
    rootN = n ** 0.5
    if rootN == int(rootN):
      return (rootN+1) ** 2
    else:
      return -1