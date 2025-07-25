n = int(input())

rev_b=[]

while n > 0:
    rev_b.append(n % 10)
    n = n // 10
    
for i in range(len(rev_b) - 1, -1, -1):
    print(rev_b[i], end=' ')