def cnt(n):
    x = 0
    while n > 0 :
        d = n % 10
        if d % 2 == 1:
            x += 1
        n //= 10
    return x        

a = int(input())
print(cnt(a))