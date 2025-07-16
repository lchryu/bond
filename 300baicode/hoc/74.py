def counteven (a, b ) :
    cnt = 0
    arr = []
    for i in range (a , b + 1) :
        if i % 2 == 0 :
            cnt += 1 
            arr.append(i)
    return cnt, arr
a = int(input())
b = int(input())
cnt, arr = counteven(a, b)

if cnt == 0:
    print("-")
else:
    for x in arr: print(x, end=' ')