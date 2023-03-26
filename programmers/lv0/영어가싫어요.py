def solution(numbers):
    alphabets = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        numbers = numbers.replace(alphabets[i], str(i))
    return int(numbers)