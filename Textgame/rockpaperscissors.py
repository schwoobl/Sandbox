import random
import sys

 #game logic:
 #r > s, p > r, s > p

def main():
    wins = 0
    losses = 0
    ties = 0

    while True: #Main game loop
        while True:
            print(f"{wins} wins, {losses} losses, {ties} ties!")
            player_choice = input("(R)ock, (p)aper or (s)cissors?! >").strip().lower()
            if player_choice not in ["r", "p", "s", "q"]:
                print("Please enter valid (r, p, s, q)!")
            elif player_choice == "q":
                sys.exit("Exiting..")
            else:
                break
        computer_choice = random.choice(["r", "p", "s"])
        
        if player_choice == computer_choice:
            print ("It's a tie!")
            ties += 1
        elif player_choice == "r" and computer_choice == "s" or player_choice == "s" and computer_choice == "p" or player_choice == "p" and computer_choice == "r":
            print("Player wins!")
            wins += 1
        else:
            print("Computer wins!")
            losses += 1
main()