def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([i for i in my_string if not i in vowels])