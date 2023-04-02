# 키 배열을 90도 돌리는 함수
def rotate_a_matrix_by_90_degree(a):
  n = len(a)
  m = len(a[0])

  result = [[0] * n for _ in range(m)]
  for i in range(n):
      for j in range(m):
        result[j][n-i-1] = a[i][j]
  return result

# 3배 커진 전체 자물쇠에서 진짜 자물쇠 속 조건을 확인하는 함수
def check(new_lock):
  lock_length = len(new_lock)//3
  for i in range(lock_length, lock_length * 2):
    for j in range(lock_length, lock_length * 2):
      if new_lock[i][j] != 1:
        return False
  return True

def solution(key, lock):
  n = len(lock)
  m = len(key)
  new_lock = [[0] * (n * 3) for _ in range(n * 3)]

  for i in range(n):
    for j in range(n):
      new_lock[i + n][j + n] = lock[i][j]

  for rotation in range(4):
    key = rotate_a_matrix_by_90_degree(key)
    for x in range(n * 2):
      for y in range(n * 2):
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + i] += key[i][j]

        if check(new_lock) == True:
          return True

        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + i] -= key[i][j]
            
  return False