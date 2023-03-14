def solution(num_list):
    odd = 0
    even = 0
    for num in num_list:
        if num % 2:
            even += 1
        else:
            odd += 1
    return [odd, even]