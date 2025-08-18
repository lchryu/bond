# import statement

from time import *
from random import *
from os import *

# variable
help_list = {'time':'timer'}

# def
def welcome () :
    name_user = input('Enter your name')
    print(f'Hello {name_user} . WELCOME TO THE ULTRA SUPER DUPA ROBOT ')
    print("type /'help/'to check all command you can use. Type /'quit'/ to quit this robot ")

def help () :
    print(help_list)

# cmd

# main