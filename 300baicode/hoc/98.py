from math import isqrt
def isprime(n: int) :
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

a = int(input())
i = 0
sum = 0
_ = 0 
while True :
    if isprime (i) and isprime (i + 2) :
        sum += i
        _ += 1
    i += 1

    if _ == a :
        break
print (sum)        


