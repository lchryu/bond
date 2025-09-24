n  = int(input())
a = list(map(int , input().split()))
check = False
for i in range (n) :
    if a[i] % 2  == 1 :
        check = True
        print(a[i])
if not check :
    print("-")        