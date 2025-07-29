def gtln (a) :
    check = False
    gtln = -1
    while a > 0 :
        r = a % 10
        a //= 10
        if r > gtln and r % 2 == 1 :
            gtln = r
            check = True
    return gtln , check

if __name__ == "__main__" :
    a = int(input())
    _, check = gtln(a)
    if check:
        print(_)
    else :
        print("-")    