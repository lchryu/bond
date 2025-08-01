def avg (k) :
    i = 0   
    add = 0
    cnt = 0
    while True:
        if i % 3 != 0:
            add += i
            cnt += 1
        if cnt == k :
            break
        i += 1
    avg  = add / cnt
    return avg 

k = int(input())
print(f'{avg(k):.1f}')    