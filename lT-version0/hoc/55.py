def max (a , b):
    if a > b :
        return a
    else:
        return b
    
def max_4 (a , c , b , d) :
    return max(max(a , b),max(c,d))

a , b , c , d = map(int,input().split())
if a == b == c == d :
    print('=')
else:    
    print(max_4(a , b , c, d))   