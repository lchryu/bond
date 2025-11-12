a = list(map(int, input().split()))
b = int(input())
while b in a :
    a.remove(b)
print(*a)
print(len(a))
