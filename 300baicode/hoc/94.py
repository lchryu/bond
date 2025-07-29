def gtnn (a) :
    cnt = 0
    gtnn = 10
    while a != 0 :
        r = a % 10
        a //= 10
        if r < gtnn and r % 2 == 0  :
            gtnn = r
            cnt = 1
    return gtnn , cnt

if __name__ =="__main__"  :
    a = int(input())      
    gtnn2 , cnt = gtnn (a)
    if cnt == 1 :
        print(gtnn2)
    else :
        print("-")     