N = int(input())
K = int(input())
cnt = 0
for i in range (K):
    if i == 0 :
        cnt = N
    else:    
        cnt += 2 * (N - K * i)
print(cnt)