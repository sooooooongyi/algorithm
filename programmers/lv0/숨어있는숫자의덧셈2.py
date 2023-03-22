import re

def solution(my_string):
    answer = re.findall(r"[0-9]+", my_string)
    return sum([int(i) for i in answer])