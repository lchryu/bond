def divideThreeTwo (a, b):
    add = 0
    cnt = 0
    add5 = 0
    for i in range (a , b +1):
        if i % 6 == 0 :
            cnt+= 1
            add += i
        if i % 5 == 0: 
            add5 += i
    return cnt , add, add5        
            
def avg (a, b) :
    cnt , add, add5 = divideThreeTwo (a , b)
    print(add5, end=' ')
    if cnt == 0 :
       print('0')
    else :
        print(add // cnt)  

if __name__=='__main__' :
    a , b = map(int , input().split())
    avg(a, b)