# 🌜, ✨ 조건에 따라 판별

while True:
    pw = input()
    pwList = list(pw)
    isAccept = True
    
    if pw == 'end':
        break
    
    # 모음 반드시 하나
    vowelCnt = 0
    for i in pwList:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowelCnt += 1
    if vowelCnt == 0:
        print(f'<{pw}> is not acceptable.')
        isAccept = False
    if not isAccept:
        continue
    
    # 연속 모음 3개, 자음 3개 불가
    vowelCnt = 0
    consonantCnt = 0
    
    for i in pwList:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowelCnt += 1
            consonantCnt = 0
        else:
            consonantCnt += 1
            vowelCnt = 0
            
        if vowelCnt == 3 or consonantCnt == 3:
            print(f'<{pw}> is not acceptable.')
            isAccept = False
            break
    if not isAccept:
        continue
    
    ## 연속 글자 2번 불가
    dupliCnt = 0
    
    for i in range(1, len(pwList)):
        if pwList[i-1] == pwList[i]:
            if not (pwList[i-1]+pwList[i] == 'ee' or pwList[i-1]+pwList[i] == 'oo'):
                print(f'<{pw}> is not acceptable.')
                isAccept = False
                break
    if not isAccept:
        continue
                
    ## 최종
    print(f'<{pw}> is acceptable.')