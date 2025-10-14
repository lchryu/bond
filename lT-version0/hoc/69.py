last = int(input())
count = 0
sum =  0 

for i in range (1 , last + 1) : 
    if i % 5  == 0 :
        sum = sum+ i 
        count = count + 1
if count == 0:
    print('0.0')
else:
    print( f'{sum / count :.1f}')    