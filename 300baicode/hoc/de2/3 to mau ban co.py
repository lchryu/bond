N = int(input())
K = int(input())
var = N + K
sum = 0
for i in range(K):
    var = var - K
    sum += var
sum = sum * 2 - N
print(sum)