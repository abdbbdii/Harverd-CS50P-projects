import random

while True:
    levelInput = input("Level: ")
    if levelInput.isdigit() and int(levelInput) > 0:
        levelInput = int(levelInput)
        break
number = random.randint(1, levelInput)
while True:
    guessInput = input("Guess: ")
    if guessInput.isdigit():
        guessInput = int(guessInput)
        if number == guessInput:
            print("Just right!")
            break
        elif number < guessInput <= levelInput:
            print("Too large!")
            continue
        elif number > guessInput >= 0:
            print("Too small!")
            continue
        else:
            continue