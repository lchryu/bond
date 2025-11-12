a = list(map(int, input().split()))
b = int(input())
for x in a :
    if x == b :
        a.remove(x)
print(*a)
print(len(a))