
def gcd (a , b) :
    a = abs(a)
    b = abs (b)
    while a != b :
        if a > b :
            a = a - b
        else :
            b = b - a
    return a                        
    
a , b = map(int , input().split())
print(gcd (a , b))