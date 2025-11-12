a = list(map(int, input().split()))
b = a.copy()
c = min(b)

while c in b:
    b.remove(c)

print(*a)
print(*b)