import NumberGuesserSimple
import sys
import time

name = "Bob"
your_name = ""
answer = ""

print(f"Hi, my name is {name}, what is yours?") 
your_name = input(">")
time.sleep(1.5)
print(f"{name}: Hi {your_name}, nice to meet you!") 
time.sleep(1.5)
print(f"{name}: Let's play a game. I am going to guess a random number between 1 and 10 \
and I want you to guess the number")
time.sleep(1.5)
print(f"{name}: Are you ready?")
answer = input("Yes/no?")
time.sleep(1.5)

while answer != "Yes".strip().lower() or "No".strip().lower():
    if answer == "Yes".strip().lower():
        print(f"{name}: Great, lets start!")
        break 
    elif answer == "No".strip().lower():
        print(f"{name}: Too bad, cause we're starting, whether you want to or not!")
        break
    else:
        print(f"{name}: Sorry? I didn't catch that!")

NumberGuesserSimple.NumberGuesser()