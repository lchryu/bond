import os
os.system('cls')
import random
import time
for i in range (1) :

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
    print('Next question ... Please wait')
    time.sleep(3)