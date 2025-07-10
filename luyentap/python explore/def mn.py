import random 
an_so = random.randint(10,100)
for i in range (7) :
    print('Your guess :')
    so_doan = int (input('>>'))
    if so_doan > an_so :
        print ( f'Your number is too big. Its your {i + 1} time of guessing ')
    elif so_doan < an_so :
        print (f'Your number is too small. Its your {i} time of guessing')
    elif so_doan == an_so :
        print ('BINGO !')
        break
    elif so_doan == str :
        print ('This isnt even a number !')
    elif i == 7 :
        print ('You cant guess anymore . Game over ! You lose ! ')