a , b = map(int,input().split())
if a == 0 or b == 0 :
    print ('0')
elif a > 0 and b > 0 or a < 0 and b < 0 :
    print ('1')
else :
    print ('-1')