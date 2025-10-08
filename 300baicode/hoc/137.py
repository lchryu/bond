a = int(input())
b = [int(input()) for i in range (a)]
c = []
for i in range (a):
    c.append(max(b))
    b.remove(max(b))
c.reverse()
print (*c)    