a = int(input())
b = [int(input()) for i in range (a)]
x = int(input())
cnt = 0
check = False
for i in range (a) :
    if b[i] == x :
        print("Yes")
        print(i)
        check = True
        break
if check == False :
    print("No")       