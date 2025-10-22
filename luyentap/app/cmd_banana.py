# import statement

from time import *
from random import *
from os import *

# variable
help_list = "timer : there will be a timer for you"

# def
def welcome () :
    name_user = input('Enter your name')
    print(f'Hello {name_user} . WELCOME TO THE ULTRA SUPER DUPA ROBOT ')
    print("type /'help/'to check all command you can use. Type /'quit'/ to quit this robot ")

def help () :
    print(help_list)

def timing () :
    entering = input()
    a = time.time
    entering2  = input()    
    b = time.time()
    print( a - b )
# cmd
def cmd () :
    cmd_in = input()
    if cmd_in == "timer" :
        timing()
# main
welcome()
while True :
    cmd ()