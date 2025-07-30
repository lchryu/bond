from random import randint
an_so =randint(10,99)
for i in range (7) :
    input = int(input('your number : '))
    if input > an_so :
        print ('your number is too big')
    elif input < an_so :
        print ('your number is too small') 
    elif input == an_so :
        print ('haha bingo')
        break