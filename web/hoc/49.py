a = int(input())

if a <= 1 :
    print('12000')
elif a <= 30 :
    print(12000 + (a - 1) * 10000)
else :
    print(12000 + 29 * 10000 + (a - 30)* 9000)