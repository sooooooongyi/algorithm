def solution(numbers):
    setOneToNine = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    setNumbers = set(numbers)
    return sum(setOneToNine ^ setNumbers)