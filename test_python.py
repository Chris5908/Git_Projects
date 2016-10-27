def solution(a):
    # write your code in Python 2.7
    b = a[::-1].split()
    c = []
    number = len(b)
    while number:
        number -= 1
        c.append(b[number])
        if( number > 0) :
            c.append(' ')
    return ''.join(c)
#    pass



S = "we test coders"
test = solution(S)
print( test )
