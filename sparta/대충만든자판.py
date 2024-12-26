def solution(keymap, targets):
    answer = []
    
    for target in targets:
        times = 0
        
        for char in target:
            time = 101
            flag = False
            
            for key in keymap:
                if char in key:
                    time = min(key.index(char)+1, time)
                    flag = True
                    
            if not flag:
                times = -1
                break
            times += time
        
        answer.append(times)
    return answer