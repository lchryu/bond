n = int(input())
k = int(input())
cnt = 0
for i in range(0,n, k):
    if i == 0: cnt += n
    else: cnt += (n - i)
print(cnt)