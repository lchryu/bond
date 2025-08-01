a , b = map(int , input().split())

mnt = 0
while a < b:
    tam_thoi = 0
    a = a + a / 50
    mnt += 1
print(mnt)    
    