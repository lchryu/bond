import math
N = int(input())
a = int(input())
b = int(input())
c =N // math.lcm(a, b)
a = N // a
b = N // b
print(N - (a + b - c))