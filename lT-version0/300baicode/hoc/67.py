a = int(input())
x = 0 
for i in range(1 , a + 1):
    if i % 3  ==0 or i % 5 == 0 :
        x = i + x
print(x)        