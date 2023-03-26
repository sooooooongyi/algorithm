def solution(s):
    my_string = s.split(' ')
    for i in range(len(my_string)):
        if my_string[i] == 'Z':
            my_string[i] = -1 * int(my_string[i-1])
        else:
            my_string[i] = int(my_string[i])
    return sum(my_string)