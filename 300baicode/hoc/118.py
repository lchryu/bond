from math import sqrt
import time
def is_prime (n) :

    if n < 2 :
        return False
    
    for i in range (2 , int(sqrt(n)) + 1) :
        if n % i == 0 :
            return False
    return True

def is_p_origin(n):
    if n < 2 :
        return False
    
    for i in range (2 , n) :
        if n % i == 0 :
            return False
    return True


# def check () :
#     n = int(input())
#     m = int(input())

#     cnt = 0
#     for i in range (n , m + 1) :
#         if is_prime(i) :
#             cnt += 1
#             # print(i)
#     print (cnt)

if __name__=="__main__" :
    a = time.time()
    is_prime(10000000001)
    b = time.time()
    print(b - a)
    
    x = time.time()
    is_p_origin(100000000000000000000000000000000000000000000000000000000000001)
    y = time.time()

    print(y-x)         