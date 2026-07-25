
import time

print("Is it raining?")
answer = input(">").lower().strip()

if answer == "no":
    print("Go outside.")
else:
    print("Have an Umbrella?")
    umbrella = input(">").strip().lower()


while answer != "no":
    print("Wait a while.")
    time.sleep(5)
    print("Is it raining?")
    answer = input(">")
    if answer == "no":
        print("Go outside.")


