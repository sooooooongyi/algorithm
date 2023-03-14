def solution(array, height):
    return len([element for element in array if height < element])