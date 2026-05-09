N = int(input())
num = 0
for i in range(0 , N , 3):
    if i == 0 :
        num += N
    else :
        num += N - i
num = num * 2 - N
print(num)