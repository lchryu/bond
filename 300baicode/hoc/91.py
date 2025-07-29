def gtln (a) :
    gtln = -1
    while a > 0 :
        r = a % 10
        a //= 10
        if r > gtln :
            gtln = r
    return gtln

if __name__ == "__main__" :
    a = int(input())
    print(gtln(a))    