a = input()
b = int(input())
d = []
for i in a:
    c = ord(i) + b
    d.append(chr(c))
print(*d, sep="")
