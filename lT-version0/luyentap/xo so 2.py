import os
os.system('cls')

import random
choice=(0,100)
answer= random.randint(0,100)
for i in range (25) :
    player=int(input(f'lan {i + 1} hay chon 1 so'))
    if player > answer :
        print ('too high')
    if player < answer :
        print ('too low')
    if player == answer :
        print ('you win')
    break
