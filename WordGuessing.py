import random

#Guess the word game

words = [ "Hello" , "Test" , "Help", "pasta", "balloon"]
word = random.choice(words)
guesses = 10


while guesses != 0:
    guess = input("Guess the word >")
    
    for letter in word:
        if guess not in word:
            print("Nope, wrong. Guess again.")
            guesses -= 1
        elif guess in word:
            print(letter)
