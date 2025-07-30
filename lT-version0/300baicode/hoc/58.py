
def odd_even (a) :
    theck = False
    for i in a :
        if int(i) % 2 == 1 :
            print(i , end = " ")
            theck = True
    if not theck :
        print('-')
a = input()
odd_even(a)