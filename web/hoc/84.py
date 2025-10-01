def print_digit(a) -> int:
    b = ""
    if a == 0 :
        return 0
    
    while a > 0 :
        b = str(a % 10) + b
        a = a // 10
    return b

if __name__=="__main__" :
       a = int(input())
       print(print_digit(a))