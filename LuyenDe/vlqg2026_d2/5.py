a = int(input())
b = []
for i in range (1, a + 1):
    while True:
        if i % 2 == 0:
            i = i // 2
        else : 
            break    
    b.append(i)
print(sum(b))        