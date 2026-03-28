import random
import sys

 #game logic:
 #r > s, p > r, s > p

def main():

    while True: #Main game loop
        player_choice = input("(R)ock, (p)aper or (s)cissors?! >").strip().lower()
        computer_choice = random.choice(["r", "p", "s"])
        while player_choice != "r" or "p" or "s" or "q":
            print("Please enter valid input")
        if player_choice == computer_choice:
            print ("It's a tie!")
        elif player_choice == "r" and computer_choice == "s" or player_choice == "s" and computer_choice == "p" or player_choice == "p" and computer_choice == "r":
            print("Player wins!")
        else:
            print("Computer wins!")
main()