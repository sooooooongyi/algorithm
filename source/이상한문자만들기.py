def solution(s):
    words = []
    
    for word in s.split(' '):
        cnt = 1
        for char in word:
            if cnt % 2 == 0:
                words.append(char.lower())
            else:
                words.append(char.upper())
            cnt += 1
        words.append(' ')
    return ''.join(words[:-1])