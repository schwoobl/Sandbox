import random, sys

#This is a number guessing game. The computer defines a random number and the player has x
#number of guesses to get the correct number. 
#This script is meant for use in other programs.

def NumberGuesser():
    number = random.randint(1,10)   #Defines a random number between and including 1 and 10
    guesses = 4                     #Number of guesses the player has
    while guesses > 0: #Main game loop
        print("You have " + str(guesses) + " guesses.")
        print("Guess the number!")
        guess = int(input(">")) #Takes the players input and converts to an integer
        if guess == number: #This if-statement evaluates the players guess and gives a hint. 
            print("Congratulations, you guessed the correct number!")
            break
        elif guess > number:
            print("Wrong, that was too high. Guess again.")
            guesses = guesses - 1
        elif guess < number:
            print("Wrong, that was too low. Guess again. ")
            guesses = guesses - 1
    else:
        print(f"Unfortunately you ran out of guesses, the number i thought of was {number}")
    return(number,guesses)