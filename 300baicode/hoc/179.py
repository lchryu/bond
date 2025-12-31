a = input()
b = (list(a))
b[0] = b[0].upper()
for i in range(1,len(b)):
    b[i] = b[i].lower()
print(*b, sep='')