import random
print("Guess the right number from 1 to 100 to win, you have 6 chances!")
random_number = random.randint(1, 100)
limit = 1
cnt =  0
while True:
    if cnt == limit:
        print("YOU LOSE, LOSER! Replay the program to play again!")
        break
    guesses = int(input(f"chance number {cnt}: write the number here: "))
    if guesses == random_number:
        print("BINGO")
        print("You win! Replay the program to play again!")
        break
    elif guesses < random_number:
        print("too small")
    else :
        print("too large")
    cnt += 1

