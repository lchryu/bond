x = int(input())
for i in range(1, 9):
    if x % i == 0 and 0 < x // i < 10 :
        print(i)
        break
