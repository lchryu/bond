def is_prime (a) :
    if a < 2 :
        return False
    for i in range (2 , int(a **0.5) + 1) :
        if a % i == 0 :
            return False
    return True            
check = False
a = int(input())
b = [int(input()) for i in range (a)]
for index in range (a) :
    if is_prime(b[index]):
        check = True
        print(b[index] , end = " ")
if check == False :
    print("-")