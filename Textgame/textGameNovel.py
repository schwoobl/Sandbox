import time
import NumberGuesserComputer
import NumberGuesserHuman
import RPS

#Initialization & Overview
name = "Bob"
player_name = ""
answer = ""
player_guess = 0
computer_guess = 0
games_played = 0

def speak(text,delay=1.5): #Combines the print-call and time.sleep call into one function for readability
    print(text)
    time.sleep(delay)

#Main Game
speak(f"Hi, my name is {name}, what is yours?",1) #f{name} inserts the predefined name variable into the print statment for readability
player_name = input("> ")
time.sleep(1)
speak(f"{name}: Hi {player_name}, nice to meet you!")
speak(f"{name}: Let's play a game. I am going to guess a random number \
between 1 and 10 and I want you to guess the number.",4)
speak(f"{name}: Are you ready?",1)
answer = input("Yes/no? > ").strip().lower() #strip() removes accidental spaces, lower() changes input to lowercase
time.sleep(1)

while True:
    if answer == "yes":
        speak(f"{name}: Great, let's get started!")
        player_guess = NumberGuesserComputer.main()
        break
    elif answer == "no":
        speak(f"{name}: Too bad, we're starting anyway!")
        player_guess = NumberGuesserComputer.main()
        break
    else:
        speak(f"{name}: Sorry, I didn't catch that!")
        answer = input("Yes/no? > ").strip().lower()

if player_guess == 1:
    speak(f"{name}: Nice work {player_name}, you actually did it! But it wasn't all that difficult...",2.5)
else:
    speak(f"{name}: Awh shucks. Better luck next time!",2)

speak(f"{name}: Let's play a different game. I want YOU to think of a number, \
and I will guess what it is!",4)
speak(f"{name}: This is gonna be a hoot. Are you ready?")
answer = input("Yes/no? > ").strip().lower()
time.sleep(1.5)

while True:
    if answer == "yes":
        speak(f"{name}: Great, let's get started!",1)
        computer_guess = NumberGuesserHuman.main(10)
        break
    elif answer == "no":
        speak(f"{name}: Too bad, we're starting anyway!",1)
        computer_guess = NumberGuesserHuman.main(10)
        break
    else:
        speak(f"{name}: Sorry, I didn't catch that!",1)
        answer = input("Yes/no?").strip().lower()
        time.sleep(1.5)

if computer_guess == 1:
    speak(f"{name}: Heh, not too bad, if I do say so myself",2)
else:
    speak(f"{name}: Aw man, I almost had you!")

speak(f"{name}: Alrighty, and lastly we will play 10 games of Rock, paper scissors!",3)
speak(f"{name}: I assume you know the rules, yes?")
rules_known = input("Yes/no? > ").strip().lower()

while True:
    if rules_known == "no":
        speak(f"{name}: Alright, so here's the rules. Rock smashes scissor, scissor cuts paper and paper covers rock. Got it? Great.",4)
        break
    elif rules_known == "yes":
        speak(f"{name}: Great, lets get started then!")
        break
    else:
        speak(f"{name}: Sorry, I didn't catch that!")
        rules_known = input("Yes/no?").strip().lower()

while games_played != 10:
    games_played, wins, losses, ties = RPS.main()
    if wins > losses:
        speak(f"{name}: Damn, you're really good at this!")
    elif wins < losses:
        speak(f"{name}: Sometimes you lose, sometimes the others win...",2)
    else:
        speak(f"{name}: Well played Sir, well played, it's a draw!",2)


