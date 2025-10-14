from math import gcd
a , b = map(int,input().split())

x = gcd(a , b)
print(f'{a // x}/{b // x}')