x = int(input())
ans = 10
for i in range (1, 10):
    for j in range (1, 10):
        if i * j == x :
            ans = min(i, ans)
if ans == 10:
    print(0)
else:
    print(ans)   