last = int(input())
count = 0
sum =  0 

for i in range (1 , last + 1) : 
    if i % 2  == 0 :
        sum = sum+ i 
        count = count + 1
if count == 0:
    print(0)
else:
    print( sum // count)    