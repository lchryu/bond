n  = int(input())
a = list(map(int , input().split()))
s  = 0
for i in a :
    s += i
print (f"{s / len(a):.2f}")    