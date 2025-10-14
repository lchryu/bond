import math

a , b , c = map (int , input().split())
cv = a + b + c
p = cv / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f'{cv:.1f}')
print(f'{s :.3f}')