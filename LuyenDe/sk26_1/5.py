a, k = map(int, input().split())
b = []
c = []
d = []
for i in range (1, a + 1 ):
    if i % 2 == 0 :
        b.append(i)
    elif i % 3 == 0:
        c.append(i)
    else:
        d.append(i)
e = b + c + d
s = 0
for i in range(k):
    s += e[i]
print(s)    

        
        