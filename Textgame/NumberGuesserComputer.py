import random
import time

#This is a number guessing game. The computer defines a random number and the player has x
#number of guesses to get the correct number. 
#This script is meant for use in other programs.

def main():
    number = random.randint(1,10)   #Defines a random number between and including 1 and 10
    guesses = 5                     #Number of guesses the player has
    while guesses > 0:              #Main game loop
        print(f"You have {guesses} guesses.")
        time.sleep(1)
        print("Guess the number!")
        time.sleep(1)
        while True:
            try:
                guess = int(input("Your guess: "))     #Takes the players input and converts to an integer
                break
            except ValueError: 
                print("That's not a valid number!!")
            except KeyboardInterrupt:
                print("Exiting")
        if guess == number:         #This if-statement evaluates the players guess and gives a hint. 
            break                   #This is the victory condition!
        elif guess > number:
            print("Nope, that was too high. Guess again.")
            time.sleep(1.3)
            guesses -= 1
        elif guess < number:
            print("Nope, that was too low. Guess again.")
            time.sleep(1.3)
            guesses -= 1
    else:
        print(f"Unfortunately you ran out of guesses, the number I thought of was {number}.")
        time.sleep(3)
    if guesses != 0:
        victory = 1
    else:
        victory = 0
    return victory