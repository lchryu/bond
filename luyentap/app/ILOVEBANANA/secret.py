import random
missing_password = ["Lol 1234","Bond is handsome 6116","12345654321","hello","I stink", "bond super smart", "I am dumb"]
print(*missing_password)
pass_= random.choice(missing_password)
while True :
    a = input()
    if a == pass_ :
        print('lol how did you know that')
        break
    else :
        print ('again , you are real dumb')