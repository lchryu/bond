n = int ( input ())
s = 0


while (n != 0):
    s = s + n % 10
    n = n // 10


x = s % 10
print (x)

if x == 9 :
    print ( 'Yes')
else :
    print ('No')