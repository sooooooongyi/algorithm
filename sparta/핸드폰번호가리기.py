def solution(phone_number):
    return "".join(["*" for _ in list(phone_number)[:-4]]) + "".join(list(phone_number)[-4:])