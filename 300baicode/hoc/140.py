a = int(input())
b = [int(input())for i in range (a)]

def is_prime (a) :
    if a <= 1 : 
        return False
    for i in range (2 ,int( (a**0.5))+1) :
        if a % i == 0 :return False
    return True
c = -999999999999999999999999999999999999999999
for index in range(a) :
    if is_prime (index) :
        if index > c :
            c = index
d = b.find(c)            
print(c ,end=" ")
print('d') 