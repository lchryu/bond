import random
import os
os.system('cls')
choice=['rock','paper','scissors']
bot=random.choice(choice)
player_choice=input('pls choose(rock,paper,scissors)').lower()
print(f'bot choice:{bot}')
if player_choice== bot:
    print('oh its a tie')
elif (player_choice=="scissors"and bot=='paper')or \
     (player_choice == 'rock'and bot =='scissors')or \
     (player_choice == 'paper'and bot == 'rock'):
    print ('you win')
elif (player_choice=="paper " and bot=='scissors')or \
     (player_choice == 'rock'and bot =='paper')or \
     (player_choice == 'scissors'and bot == 'rock'):
    print ('you lose')
else:
    print ('you arent going to answer like this')