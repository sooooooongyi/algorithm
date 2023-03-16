def solution(numbers, direction):
    if direction == 'right':
        return [numbers[(i-1) % len(numbers)] for i in range(len(numbers))]
    if direction == 'left':
        return [numbers[(i+1) % len(numbers)] for i in range(len(numbers))]