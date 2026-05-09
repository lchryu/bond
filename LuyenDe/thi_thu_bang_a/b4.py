def sumupto(n):
    b = n //3
    r = n % 3
    s = 9 * (b - 1) * b // 2 + 6 * b
    
    if b % 2 == 1 :
        if r == 1:
            s += 3 * b + 3
        else:
            s += 6 * b + 5
    else:
        if r == 1:
            s += 3 * b + 1
        else:
            s += 6 * b + 3
        
    
    return s

l = int(input())
r = int(input())
print(sumupto(r) - sumupto(l - 1))