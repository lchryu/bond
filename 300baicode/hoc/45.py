thg , nam = map(int,input().split())

if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0) :
    nm = "skibidi"
else :
    nm = 'hehe'

if  thg == 2 :
    if nm == 'skibidi':
        print (29)
    else :
        print (28)
elif thg == 9 or thg == 4 or thg == 6 or thg == 11 :
    print (30)
else :
    print (31)