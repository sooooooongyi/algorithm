def solution(quiz):
    answer = []
    for i in quiz:
        formula = i.split(' = ')
        if eval(formula[0]) == int(formula[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer