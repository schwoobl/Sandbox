import random, sys

def NumberGuesser():
    number = random.randint(1,10)
    guesses = 4
    while True:  
        if guesses <= 0:
            print(f"Unfortunately you ran out of guesses, the number i thought of was {number}")
        else:
            print("You have " + str(guesses) + " guesses.")
            print("Guess the number!")
            guess = int(input(">"))
        if guess == number:
            print("Congratulations, you guessed the correct number!")
            sys.exit("Exiting...")
        elif guess > number:
            print("Wrong, that was too high. Guess again.")
            guesses = guesses - 1
        elif guess < number:
            print("Wrong, that was too low. Guess again. ")
            guesses = guesses - 1
    return(number,guesses)

