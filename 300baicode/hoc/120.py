def ifprime(n) :
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

m , n = map(int,input().split())
cnt = 0
sum = 0
for i in range(m, n + 1):
    if ifprime(i):
        sum += i
        cnt+= 1
print(f'{sum / cnt :.1f}')