#
# Function to inverse a string chain
#

def string_inversion(a):
    b = a[::-1].split()         # Inverse the string chain and split it into a list of words
    c = []
    number = len(b)             # Save the numbers of words
    while number:
        number -= 1
        c.append(b[number])
        if( number > 0) :
            c.append(' ')
    return ''.join(c)



S = "we test coders"

test = string_inversion(S)

print( test )


# Result : ew tset sredoc
