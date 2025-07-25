def greater_than_x (n , x) :
    s = 0
    while n >  0 :
        d = n % 10
        if d > x:
            s += d
        n //= 10
    return s  


if __name__== "__main__" :
    a , b = map(int,input().split()) 
    print(greater_than_x(a, b))

    