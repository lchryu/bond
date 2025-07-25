n = int(input())

rev_b=[]

while n > 0:
    d = n % 10
    if d % 2 == 0 :
        rev_b.append(d)
    n = n // 10

rev_b.reverse()

print(*rev_b)