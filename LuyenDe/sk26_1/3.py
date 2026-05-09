a = int(input())
cnt = 0
for i in range (0 , a, 3):
    cnt += a - i
print(cnt *2 - a )    