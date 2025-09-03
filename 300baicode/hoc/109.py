def rev_num (n) :
    space_answ = 0
    while n > 0 :
        space_answ *= 10
        space_answ += n % 10
        n = n // 10
    return space_answ

if __name__ == "__main__" :
    n = int(input())
    if n == rev_num (n) :
        print('Yes')
    else : print('No')    

