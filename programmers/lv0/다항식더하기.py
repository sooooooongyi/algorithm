def solution(polynomial):
    split_polynomial = polynomial.split(' + ')
    x_num = 0
    num = 0
    
    for i in split_polynomial:
        if 'x' in i:
            if len(i) == 1:
                x_num += 1
            else:
                x_num += int(i[:-1])
        else:
            num += int(i)
            
    if x_num == 0:
        return str(num)
    
    if x_num == 1:
        if num == 0:
            return 'x'
        else:
            return 'x + ' + str(num)
    
    if num == 0:
        return str(x_num)+'x'
    
    return str(x_num)+'x + '+str(num)