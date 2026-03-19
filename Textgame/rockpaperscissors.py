import random
 #game logic:

 #r > s, p > r, s > p
def main():

    player_choice = input("(R)ock, (p)aper or (s)cissors?!").strip().lower()
    computer_choice = random.choice(["r", "p", "s"])

    if player_choice == computer_choice:
        print ("It's a tie!")