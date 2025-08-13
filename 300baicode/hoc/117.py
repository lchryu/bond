def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    


n = int(input())
m = int(input())

cnt = 0

for i in range(n, m + 1):
    if is_prime(i):
        cnt = 1
        print(i, end=' ')

if cnt == 0:
    print('-')
