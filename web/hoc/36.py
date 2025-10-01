a , b = map (float,input().split())
c = (a + b * 2) / 3

print (f'{c:.1f}')

if c < 3.5 :
    print ('Kem')
elif c < 5 :
    print ('Yeu')
elif c < 6.5 :
    print ( 'Trung binh')
elif c < 8 :
    print ('Kha')
else :
    print ( 'Gioi' )