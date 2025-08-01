def SOL (k):
    cnt = i = 0
    lst = []
    while True   :
        if i % 3 == 0 and i % 9 != 0 :
            lst.append (i)
            cnt += 1
        if cnt == k : break
        i += 1
    return lst [k - 1]

if __name__ =="__main__" :
    print(SOL(int(input())))
    