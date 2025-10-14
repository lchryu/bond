def count_digit (a) -> int:
    cnt = 0 
    if a == 0 :
        cnt = 1
        return cnt
    while a > 0 :
        a = a // 10
        cnt = cnt + 1 
    return cnt

a = int(input())
print(count_digit(a))    
        