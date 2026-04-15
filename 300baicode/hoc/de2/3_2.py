N = int(input())
K = int(input())
sum = 0

for i in range(0, N, K):
    if i == 0:
        sum += N
    else:
        sum += 2 * (N - i)
print(sum)