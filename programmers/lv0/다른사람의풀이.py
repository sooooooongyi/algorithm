def solution(score):
    avg_score = [(i+j)/2 for i, j in score]
    sorted_score = sorted(avg_score, reverse = True)
    return [sorted_score.index(i)+1 for i in avg_score]