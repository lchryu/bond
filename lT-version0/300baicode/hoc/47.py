from math import sqrt

a = int ( input())
if a < 0:
   print ("No")
else:
    x = int(sqrt(a))

    if x * x == a :
        print ('Yes')
    else :
        print ('No')