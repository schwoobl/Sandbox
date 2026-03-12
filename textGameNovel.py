import NumberGuesserComputer, sys, time 

name = "Bob"
your_name = ""
answer = ""

print(f"Hi, my name is {name}, what is yours?") 
your_name = input("> ")
time.sleep(1)
print(f"{name}: Hi {your_name}, nice to meet you!") 
time.sleep(1.5)
print(f"{name}: Let's play a game. I am going to guess a random number \
      between 1 and 10 and I want you to guess the number.")
time.sleep(4)
print(f"{name}: Are you ready?")
time.sleep(1)
answer = input("Yes/no? > ").strip().lower()
time.sleep(1.5)

while True:
    if answer == "yes":
        print(f"{name}: Great, let's get started!")
        time.sleep(1)
        NumberGuesserComputer.Main()
        break
    elif answer == "no":
        print(f"{name}: Too bad, we're starting anyway!")
        time.sleep(1)
        NumberGuesserComputer.Main()
        break
    else:
        print("Sorry,? I didn't catch that!")
        answer = input("Yes / no ?").strip().lower()
        time.sleep(1.5)

print(f"{name}: Nice work, you actually did it! But it wasn't all that difficult...")
time.sleep(2)
print(f"{name}: Let's play a different game. I want YOU to think of a number, \
and I will guess what it is!")
time.sleep(4)
print(f"{name}: This is gonna be a hoot. Are you ready?")
time.sleep(1.5)
answer_2 = input("Yes/No > ").strip().lower()