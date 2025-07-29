def gtnn (a) :
    gtnn = 10
    while a != 0 :
        r = a % 10
        a //= 10
        if r < gtnn :
            gtnn = r
    return gtnn

if __name__ =="__main__"  :
    a = int(input())      
    print(gtnn(a)) 