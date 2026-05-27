N = int(input())
s = 0
c = []
a = 1
for i in range (1, N + 1):
    while True:
        
        if i % 2 == 1:
            c.append(i)
            break
        else:
            i = i/2
for x in c:
    s += x
print(int(s))    
            