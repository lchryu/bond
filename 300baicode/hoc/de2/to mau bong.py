import math
N = int(input())
a = int(input())
b = int(input())
num_a = N // a
num_b = N // b
num_a_b =N // math.lcm(num_a, num_b)
print(N - num_a - num_b + num_a_b)