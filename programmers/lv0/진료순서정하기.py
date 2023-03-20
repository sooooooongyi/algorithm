def solution(emergency):
    answer = sorted(emergency, reverse=True)
    return [answer.index(i)+1 for i in emergency]