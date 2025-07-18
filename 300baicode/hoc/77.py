def average(a: int, b: int):
    add = 0
    cnt = 0
    for oi in range (a , b +1):
        if oi % 2 == 0 :
            add += oi
            cnt += 1
    if cnt == 0:
        return 0, 0
    return cnt, add // cnt       

n, m = map(int, input().split())
cnt, avg = average(n, m)

if __name__ == "__main__":
    if cnt == 0:
        print(0)
    else:
        print(avg)