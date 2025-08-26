def isprimt (a) :
    if a < 2 :
        return False
    for i in range (2 ,int( a ** 0.5) + 1) :
        if a % i == 0 :
            return False
    return True

a = int(input())

if isprimt(a) and isprimt( a + 2) :
    print("Yes")
else :
    print('No')        