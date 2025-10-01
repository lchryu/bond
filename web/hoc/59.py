def odd_even(a):
    s = 0
    theck = False
    for i in a:
        if int(i) % 2 == 0:
            s += int(i)            
            theck = True
    if  theck:
        print(s)
    else:
        print('-')
        
if __name__ == "__main__":
    a = input()
    odd_even(a)    