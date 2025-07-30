import math


a , b , c =  map(int,input().split())
p = (a + b + c )/2
s =  math.sqrt(p * (p - a) * (p - b) * (p - c))
r = (a * c* b) / (4 * s)
print(f'{r:.3f}')