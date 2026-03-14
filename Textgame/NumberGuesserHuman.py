import random, time

#This is a number guessing game, where the player thinks of a random number
#that the computer has to guess correctly.
#This script is meant for use in other programs.

#right now the computer just blitzes through numbers until its got it correctly
#I want the computer to adjust its guess based on feedback, whether the guess was
#too high or too low.

def Main(x):
    #Initialization & overview of variables
    feedback = ""
    guesses = 4
    low = 1
    high = x 
    computer_guess = 0
    player_number = 0

    #Main game loop
    player_number = int(input(f"Think of a random number between 1 and {x}: "))
    time.sleep(2)
    while guesses > 0:
        computer_guess = random.randint(low, high)
        print(f"Hmmmm... {computer_guess} !")
        time.sleep(1)
        feedback = input("Please let me know if my guess was (l)ow, (h)igh, or (c)orrect > ")
        time.sleep(0.5)
        if feedback == "c":
            break
        elif feedback == "l":
            print("Too low huh? Alright...")
            guesses -= 1
            low = computer_guess + 1
            time.sleep(1.5)
        elif feedback == "h":
            print("Too high? Damn, alright...")
            guesses -= 1
            high = computer_guess - 1
            time.sleep(1.5)
    if guesses == 0:
        victory = 0
    else:
        victory = 1
    return(victory)
