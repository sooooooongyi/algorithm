def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=lambda x: (x, len(x)))
    for index in range(len(phone_book)-1):
        if phone_book[index] == phone_book[index+1][:len(phone_book[index])]:
            return False
    return answer

print(solution(["1195524421", "97674223", "119"]))