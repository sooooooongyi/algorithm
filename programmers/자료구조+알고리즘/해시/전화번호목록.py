def solution(phone_book):
    dic = {}
    for i in phone_book:
        dic[i] = 0
    for i in phone_book:
        for j in range(len(i)):
            if i[:j] in dic:
                return False
    return True