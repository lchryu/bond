    
import time
import os
os.system('cls')
a = 0.01
pin = 100
while pin > 0 or tmp == "already charge":
    pin = pin - 1
    print(f'battery : {pin}')
    time.sleep (a)
    if pin == 50 :
        print('pls charge')
        tmp = input("press enter to continue ")
        a = 0.05

    if pin == 30 :
        print(' the energy saver is on')
        tmp2 = input('press enter to carry on')
        a = float (input('how slow for the down going battery ?'))
    if pin == 0 :
        print ('out of battery')
    
