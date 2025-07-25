def sum_digit (a) :
    s = 0 
    while a > 0 :
        d = a % 10
        if d % 2 == 0 :
            s += d 
        a //= 10     
    return s

n = int(input())
print(sum_digit(n))