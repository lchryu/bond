a = list(map(int, input().split()))
b = a.copy()
a.clear()
s = sum(b)
cnt = len(b)
avg = s / cnt
for x in b :
    if x < avg :
        a.append(x)
print(*a)
print(*b)