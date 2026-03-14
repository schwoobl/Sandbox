import NumberGuesserComputer, time, NumberGuesserHuman

#Initialization & Overview
name = "Bob"
player_name = ""
answer = ""
human_guess = 0
computer_guess = 0

#Main Game
print(f"Hi, my name is {name}, what is yours?") #f{name} inserts the predefined name variable into the print statment for readability
time.sleep(1)
player_name = input("> ")
time.sleep(1)
print(f"{name}: Hi {player_name}, nice to meet you!") 
time.sleep(1.5)
print(f"{name}: Let's play a game. I am going to guess a random number \
between 1 and 10 and I want you to guess the number.")
time.sleep(4)
print(f"{name}: Are you ready?")
time.sleep(1)
answer = input("Yes/no? > ").strip().lower() #strip() removes accidental spaces, lower() changes input to lowercase
time.sleep(1.5)

while True:
    if answer == "yes":
        print(f"{name}: Great, let's get started!")
        time.sleep(1.5)
        human_guess = NumberGuesserComputer.Main()
        break
    elif answer == "no":
        print(f"{name}: Too bad, we're starting anyway!")
        time.sleep(1.5)
        human_guess = NumberGuesserComputer.Main()
        break
    else:
        print("Sorry,? I didn't catch that!")
        answer = input("Yes/no ?").strip().lower()
        time.sleep(1.5)

if human_guess == 1:
    print(f"{name}: Nice work {player_name}, you actually did it! But it wasn't all that difficult...")
else:
    print(f"{name}: Awh shucks. Better luck next time!")

time.sleep(2)
print(f"{name}: Let's play a different game. I want YOU to think of a number, \
and I will guess what it is!")
time.sleep(4)
print(f"{name}: This is gonna be a hoot. Are you ready?")
time.sleep(1.5)
answer = input("Yes/No > ").strip().lower()

while True:
    if answer == "yes":
        print(f"{name}: Great, let's get started!")
        time.sleep(1)
        computer_guess = NumberGuesserHuman.Main(10)
        break
    elif answer == "no":
        print(f"{name}: Too bad, we're starting anyway!")
        time.sleep(1)
        computer_guess = NumberGuesserHuman.Main(10)
        break
    else:
        print("Sorry,? I didn't catch that!")
        answer = input("Yes/no ?").strip().lower()
        time.sleep(1.5)

if computer_guess == 1:
    print(f"{name}: Heh, not too bad, if I do say so myself")
else:
    print(f"{name}: Aw man, I almost had you!")