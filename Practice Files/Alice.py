age = 12
print("What's your name?")
name = input(">")
if name == "Alice":
    print("Hi, Alice!")
    print("How old are you?")
    user_age = input(">")
    if  age < int(user_age):
        print("You are not Alice, kiddo!")
else:
    print("You are neither Alice nor a little kid.")