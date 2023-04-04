# lv1 해시 - 폰켓몬

def solution(nums):
    setLen = len(set(nums))
    if len(nums) // 2 > setLen:
        return setLen
    return len(nums) // 2