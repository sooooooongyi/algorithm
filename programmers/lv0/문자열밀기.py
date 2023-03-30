from collections import deque

def solution(A, B):
    Alist = deque(A)
    Blist = deque(B)
    for i in range(len(Alist)):
        if Alist == Blist:
            return i
        Alist.rotate(1)
    return -1