a = int(input())
b = [int(input())for i in range (a)]

def is_prime (a) :
    if a <= 1 : 
        return False
    for i in range (2 ,int( (a**0.5))+1) :
        if a % i == 0 :return False
    return True
index_prime = -1
max_prime = -1
for i in range (a) :
    if is_prime (b[i]) and b[i] > max_prime :
        max_prime = b[i]
        index_prime = i
print(max_prime , index_prime)        