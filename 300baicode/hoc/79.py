def avg (a , b) :
    cnt = cnt7 = 0
    total = 0
    for i in range (a , b + 1) :
        if i % 2 == 0 or i % 3 == 0 :
            cnt += 1
            total += i
        if i % 7 == 0:
            cnt7 += 1
    return total , cnt, cnt7

if __name__ == "__main__":
    a , b  = map(int, input().split())
    total, cnt, cnt7 = avg(a, b)
    print(cnt7 , end = " ")
    if cnt > 0:
        avg_value = total / cnt
        print(f"{avg_value:.1f}")
    else:
        print('0.0')        