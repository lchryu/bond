s1=int(input('so dau tien '))
s2=int(input('so thu hai '))
ncct=input( 'time / divide / plus / minus ')

if ncct == 'time' :
    print ( s1 * s2)
elif ncct == 'divide' :
    print(f'{s1 // s2} {s1 % s2}')
elif ncct == 'plus' :
    print(f'{s1 + s2}')
elif ncct == 'minus':
    print(f'{s1 - s2}')