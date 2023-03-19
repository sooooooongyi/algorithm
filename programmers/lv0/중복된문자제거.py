def solution(my_string):
    answer = []
    for i in list(my_string):
        if not i in answer:
            answer.append(i)
    return ''.join(answer)