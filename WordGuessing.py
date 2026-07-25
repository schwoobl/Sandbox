import random

#Guess the word game

words = [ "hello", "test", "help", "pasta", "balloon"]
word = random.choice(words)
guesses = 10

while guesses != 0:
    guess = input("Guess a letter >")
    
    for i in word:
        if i != guess:
            print("_", end=" ")
            guesses -= 1
        elif i == guess:
            print(i, end="")