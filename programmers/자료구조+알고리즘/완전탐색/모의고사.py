def solution(answers):
    answer = []
    cnt = []
    first = [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    answer.append(len([i for i in range(len(answers)) if answers[i] == first[i]]))
    answer.append(len([i for i in range(len(answers)) if answers[i] == second[i]]))
    answer.append(len([i for i in range(len(answers)) if answers[i] == third[i]]))
                  
    if answer.count(max(answer)) > 1:
        for i in range(3):
            if answer[i] == max(answer):
                  cnt.append(i+1)
    else:
        cnt.append(answer.index(max(answer)) + 1)
                  
    return cnt