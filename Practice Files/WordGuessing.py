import random

#Guess the word game

words = [ "Hello" , "Test" , "Help"]

word = random.choice(words)

print("Guess the characters")

for chr in word:
    print(chr)
