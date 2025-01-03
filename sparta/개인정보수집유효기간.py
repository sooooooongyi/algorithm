def solution(today, terms, privacies):
    answer = []
    dic = {}
    
    todayList = list(map(int, today.split('.')))
    
    for term in terms:
        grade, m = term.split()
        dic[grade] = int(m) * 28
        
    for i in range(len(privacies)):
        date, s = privacies[i].split()
        privacyList = list(map(int, date.split('.')))
        
        year = (todayList[0] - privacyList[0]) * 336
        month = (todayList[1] - privacyList[1]) * 28
        day = todayList[2] - privacyList[2]
        
        if (year + month + day) >= dic[s]:
            answer.append(i+1)
            
    return answer