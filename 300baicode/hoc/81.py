import math
def gcd (a , b) :
    a = abs(a)
    b = abs (b)
    while a != b :
        if a > b :
            a = a - b
        else :
            b = b - a
    return a                        

def gcd(a, b):
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input().split())
print(gcd(a, b))

a , b = map(int , input().split())
print(gcd (a , b))