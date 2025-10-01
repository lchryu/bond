from math import ceil

a , b , c = map(int, input() .split())
a = ceil (a / 2)
b = ceil(b / 2)
c = ceil(c / 2)
print(a + b + c)