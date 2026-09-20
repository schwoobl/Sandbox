print("Is it raining?")
rain = input().strip().lower()  # Normalize input for case-insensitive comparison

if rain == "no":
    print("Go outside.")
elif rain == "yes":
    print("Have an umbrella?")
    umbrella = input().strip().lower()

    if umbrella == "yes":
        print("Go outside.")
    elif umbrella == "no":
        print("Wait a while.")
    else:
        print("Invalid input for umbrella.")
else:
    print("Invalid input for rain.")
