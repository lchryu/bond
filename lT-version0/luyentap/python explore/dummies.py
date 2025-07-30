import time
import random
import os

jokes = [
    "Why is the computer cool? Because it opens Windows all day!",
    "Why do you like Halloween? Because you can say: Happy Halloween!",
    "There are 10 kinds of people: those who understand binary and those who don't!",
    "What animal will a Python programmer choose as a pet? An anaconda!",
    "You must type ? to reveal this joke"
]

secrets = [
    "Hey , you can laugh this way : hehahi :)))))",
    "The author is : Huyhehe@haha.hihi",
    "What shape is the square ? hahahaha",
    "Type tol to check if someone is lying or not"
]

commands_help = {
    "quit/bye/exit": "Exit the program",
    "joke/funny/msft": "Tell a joke",
    "?": "Reveal a random secret",
    "help": "Show this help menu",
    "about": "Information about the program",
    "clear": "Clear the screen",
    "time" :"Display the current time",
    "happy": "Laugh together and have fun",
    "lprps/lets rps":'Rock paper scissors !',
    "gn/ds/guess number":"lets guess the number from 10 to 99",
    " type ?" :"See if you can unlock an all brand new amazing stuff! "
}

def clear_screen():
    os.system("cls")

def show_welcome():
    print("=" * 50)
    print("WELCOME TO YOUR DUMMIES")
    print("=" * 50)
    print("Type 'help' to view the list of commands")
    print("Type 'quit', 'bye' or 'exit' to leave")
    print("-" * 50)

def show_help():
    print("\nLIST OF COMMANDS:")
    print("-" * 30)
    for cmd, desc in commands_help.items():
        print(f"  {cmd:<15} - {desc}")
    print("-" * 30)

def tell_joke():
    joke = random.choice(jokes)
    print("Here's a joke for you...")
    time.sleep(1)
    print(f"   {joke}")
    print("   Hahaha!")

def reveal_secret(cmd):
    secret = random.choice(secrets)
    print(f"You entered: '{cmd}'")
    time.sleep(1)
    print(f"   {secret}")
    print("   A little secret!")

def show_about():
    print("\nABOUT THIS PROGRAM:")
    print("   This is your simple dummies")
    print("   Written in Python")
    print("   Version: 5.0")
    print("   Author: This is a secret that you can discover when you enter : ?")

def show_time():
    current_time = time.strftime("%H:%M:%S - %d/%m/%Y")
    print(f"Current time: {current_time}")

def laugh () :
    print ('hehe')
    time.sleep(2)
    print ("hihi")
    print('lets laugh together')
    time.sleep(2)
    print ('haha')
    print ('You will know another way of laughing if you are lucky enough to reveal that secret : press the ? key ')
def rockpaperscissors() :
    choices ='rock','paper','scissors'
    bot=random.choice (choices )
    player=input('lets play rock paper scissors . your turn : ')
    print (f'bot chioice : {bot}')

    if player == bot :
        print ('oh , its a tie')
    elif player == 'rock' and bot == 'scissors' or \
        player=='scissors' and bot == 'paper' or \
        player=='paper'and bot == 'rock':
        print ('hey how did ya win ?')
    elif player == 'paper' and bot == 'scissors' or \
        player=='rock' and bot == 'paper' or \
    player=='scissors'and bot == 'rock':
        print ('ha ha ! you lose')
    else :
        print('that is not even an answer !!!!')
def tol_machine() :
    
    for i in range (1) :
        cat = input('press enter to continue')
        questions=  ['Did you lie when you were a kid?','Do you love your partner ?','Did you make something overcook ?','Did you steal anything ?','Did you poop on your trousers ?','Did you eat your rheum ?',"Did you step on shit ?"]   
        question = random.choice(questions)
        print (f'{question}')

        start = time.time()
        answer = input(">> ").lower()
        end = time.time()

        duration = end - start
        


        if duration > 5  and answer in ['ko', 'no', 'never']:
            print ('machine is working ...')
            time.sleep(5)
            print('I know you are lying')
        elif duration <= 10 and answer in ['ko', 'no', 'never']:
            print ('machine is working ...')
            time.sleep(5)
            print('You are telling the truth.')
        
        if answer in ['yes', 'already', 'co']:
            print ('machine is working ...')
            time.sleep(5) 
            print('Sounds not so suspicious. You are telling the truth.')

        if answer in ['yes','already','co','ko','no','never'] :
            pass
        else :
            print ('machine is working ...')
            time.sleep(5)
            print ('this answer is not accepted')
def ds () :
    an_so = random.randint(10,100)
    for i in range (7) :
        print('Your guess :')
        so_doan = int (input('>> '))
        if so_doan > an_so :
            print ( f'Your number is too big. Its your {i + 1} time of guessing ')
        elif so_doan < an_so :
            print (f'Your number is too small. Its your {i + 1} time of guessing')
        elif so_doan == an_so :
            print ('BINGO !')
            break
        elif so_doan == str :
            print ('This isnt even a number !')
        elif i == 6 :
            print ('You cant guess anymore . Game over ! You lose ! ')
            break
def process_command(cmd):
    cmd = cmd.lower().strip()

    if cmd in ["quit", "bye", "exit"]:
        print("Restarting...")
        time.sleep(1)
        print("Goodbye! See you next time!")
        return False

    elif cmd in ["joke", "funny", "msft", "make some funny thing"]:
        tell_joke()

    elif "?" in cmd:
        reveal_secret(cmd)

    elif cmd == "help":
        show_help()

    elif cmd == "about":
        show_about()

    elif cmd == "clear":
        clear_screen()
        show_welcome()

    elif cmd == "time":
        show_time()
    elif cmd == "happy" :
        laugh ()
    elif cmd in ["lprps","lets rps"] :
        rockpaperscissors ()
    elif cmd == "tol" :
        tol_machine ()
    elif cmd in ["ds",'gn','guess number']:
        ds()
    else:
        print(f"I don't understand the command '{cmd}'")
        print("Type 'help' to see available commands")

    return True

def main():
    clear_screen()
    show_welcome()

    while True:
        try:
            print()
            cmd = input("Enter command: ").strip()

            if not cmd:
                print("You didn't type anything!")
                continue

            if not process_command(cmd):
                break

        except KeyboardInterrupt:
            print("\nProgram interrupted with Ctrl+C")
            print("Goodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Please try again.")
if __name__ == "__main__":
    main()